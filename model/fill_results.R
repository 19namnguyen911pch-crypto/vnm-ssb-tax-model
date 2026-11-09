###############################################################################
# fill_results.R — produce every number the manuscript needs, once
#
# Writes output/results.json with a key per placeholder. Nothing here is
# hand-entered; every value comes from the model.
###############################################################################

suppressPackageStartupMessages({
  source("model/vhlss.R")
  source("model/pmslt_model.R")
  source("model/psa.R")
})

N_PSA   <- as.integer(Sys.getenv("PSA_N", "2000"))
OUT     <- "output"
dir.create(OUT, showWarnings = FALSE, recursive = TRUE)

p0 <- params_default()
qprof <- get_quintile_profile()
mort <- 0.004 * exp(0.075 * (p0$ages - 20))

fmt <- function(x, d = 0) formatC(x, format = "f", digits = d, big.mark = ",")
pct <- function(x, d = 1) paste0(formatC(100 * x, format = "f", digits = d), "%")

# ---------------------------------------------------------------------------
# 1. Deterministic runs at central values
# ---------------------------------------------------------------------------
run_all_central <- function(horizon = 2050) {
  p <- p0; p$horizon <- horizon
  codes <- c("S0", "S1", "S2", "S3")
  r <- lapply(codes, run_scenario, qprof = qprof, p = p, mort_by_age = mort)
  names(r) <- codes
  r
}
c50 <- run_all_central(2050)
c10 <- run_all_central(2036)
clife <- run_all_central(2100)

agg <- function(res, code, field) sum(res[[code]][[field]])
base <- c50[["S0"]]

R <- list()

# price and consumption
p <- p0
dp27 <- price_change(p$tau_2027, p)
dp28 <- price_change(p$tau_2028, p)
R[["TBD-1"]]  <- pct(dp27, 2)
R[["TBD-40"]] <- pct(dp28, 2)
R[["TBD-41"]] <- fmt(dp28 * p$retail_price_l, 0)
R[["TBD-42"]] <- formatC(0.20 / dp28, format = "f", digits = 1)
R[["TBD-39"]] <- pct(p$passthrough, 0)

dq1 <- qprof$ssb_ml_day * consumption_change(dp28, qprof$elast_mult, p)
dml <- sum(qprof$pop_share * qprof$ssb_ml_day * consumption_change(dp28, qprof$elast_mult, p))
R[["TBD-2"]] <- formatC(-dml, format = "f", digits = 1)
R[["TBD-3"]] <- pct(-dml / 145, 1)
R[["TBD-44"]] <- pct(abs(untaxed_response(dp28, p)), 1)
d_sugar <- sugar_change_g_day(145, consumption_change(dp28, 1, p), p)
R[["TBD-45"]] <- formatC(-energy_change_kcal(d_sugar, p), format = "f", digits = 1)
bmi <- bmi_change_dynamic(energy_change_kcal(d_sugar, p), p, years = 1)[1]
R[["TBD-50"]] <- formatC(abs(bmi), format = "f", digits = 4)

# incidence reduction implied by the PIF at the end of the horizon
pif_end <- pif_from_bmi_shift(bmi, p$rr_per_2bmi)
R[["TBD-52"]] <- pct(1 - pif_end[["t2dm"]], 1)
R[["TBD-53"]] <- pct(1 - pif_end[["ihd"]], 1)
R[["TBD-54"]] <- pct(1 - pif_end[["stroke"]], 1)
R[["TBD-25"]] <- fmt(p$latency_years, 0)

# DALYs, cases, deaths, costs, revenue
for (code in c("S1", "S2", "S3")) {
  d <- sum(base$dalys - c50[[code]]$dalys)
  R[[paste0("D_", code)]] <- d
  R[[paste0("CASES_", code)]] <- c(t2dm = sum(base$cases_t2dm - c50[[code]]$cases_t2dm), ihd = sum(base$cases_ihd - c50[[code]]$cases_ihd), stroke = sum(base$cases_stroke - c50[[code]]$cases_stroke))
  R[[paste0("DEATHS_", code)]] <- sum(base$deaths - c50[[code]]$deaths)
  R[[paste0("COST_", code)]] <- sum(base$costs - c50[[code]]$costs)
  R[[paste0("REV_", code)]] <- sum(c50[[code]]$revenue)
}

tot_pop <- sum(qprof$pop_share) * p0$pop_2027 * p0$share_20plus
R[["TBD-4"]]  <- fmt(R[["D_S1"]])
R[["TBD-56"]] <- formatC(R[["D_S1"]] / (tot_pop / 1000), format = "f", digits = 1)
R[["TBD-6"]]  <- fmt(sum(R[["CASES_S1"]]))
R[["TBD-59"]] <- fmt(R[["CASES_S1"]]["t2dm"])
R[["TBD-60"]] <- fmt(R[["CASES_S1"]]["ihd"])
R[["TBD-61"]] <- fmt(R[["CASES_S1"]]["stroke"])
R[["TBD-62"]] <- fmt(R[["DEATHS_S1"]])
R[["TBD-7"]]  <- fmt(R[["COST_S1"]] / 1e9)
R[["TBD-8"]]  <- fmt(R[["REV_S1"]] / 1e9)
R[["TBD-63"]] <- fmt(sum(clife[["S0"]]$dalys - clife[["S1"]]$dalys))
R[["TBD-64"]] <- fmt(sum(c10[["S0"]]$dalys - c10[["S1"]]$dalys))

# YLL / YLD split: recompute with a variant that exposes them
life_split <- function(p, pop0, mort_by_age) {
  dis <- c("t2dm", "ihd", "stroke")
  A <- length(p$ages)
  N <- matrix(0, A, 3, dimnames = list(NULL, dis)); healthy <- pop0
  if (isTRUE(p$init_prev) && !is.null(p$gbd)) {
    N <- sweep(p$gbd$prev, 1, pop0, "*")
    healthy <- pmax(pop0 - rowSums(N), 0)
  }
  yld <- 0; yll <- 0
  surv <- cumprod(1 - pmin(mort_by_age, 1)); e_rem <- rev(cumsum(rev(surv))) / pmax(surv, 1e-9)
  inc_base <- p$gbd$inc
  for (t in seq_len(p$horizon - p$start + 1)) {
    inc <- sweep(inc_base, 2, rep(1, 3), "*")
    newc <- inc * healthy; healthy <- healthy - rowSums(newc); N <- N + newc
    m_bg <- pmin(mort_by_age, 1)
    m_dis <- pmin(outer(m_bg, rep(1, 3)) + p$gbd$mort_case, 1)
    dh <- healthy * m_bg; dd <- N * m_dis
    healthy <- healthy - dh; N <- N - dd
    disc <- 1 / (1 + p$discount)^(t - 1)
    yld <- yld + sum(N %*% p$gbd$dw[dis]) * disc
    yll <- yll + (sum(dh * e_rem) + sum(dd * e_rem)) * disc
  }
  c(yld = yld, yll = yll)
}
p_s1 <- p0; p_s1$horizon <- 2050
w_age <- p0$age_weights
split0 <- life_split(p_s1, tot_pop * w_age, mort)
p_s0 <- p_s1
R[["TBD-57"]] <- pct(split0["yll"] / sum(split0), 0)
R[["TBD-58"]] <- pct(split0["yld"] / sum(split0), 0)

# ---------------------------------------------------------------------------
# 2. Equity (deterministic, central values)
# ---------------------------------------------------------------------------
eq <- equity_summary(base, c50[["S1"]], qprof)
R[["TBD-9"]]  <- formatC(eq$dalys_per_1000[1], format = "f", digits = 2)
R[["TBD-10"]] <- formatC(eq$dalys_per_1000[5], format = "f", digits = 2)
R[["TBD-71"]] <- formatC(eq$ratio_Q1_Q5, format = "f", digits = 2)
R[["TBD-72"]] <- formatC(eq$ci_dalys, format = "f", digits = 3)
R[["TBD-73"]] <- formatC(eq$ede_e1, format = "f", digits = 2)
R[["TBD-74"]] <- formatC(eq$ede_e3, format = "f", digits = 2)
R[["TBD-75"]] <- formatC(eq$ede_e10, format = "f", digits = 2)
R[["TBD-11"]] <- formatC(100 * eq$tax_share[1], format = "f", digits = 3)
R[["TBD-12"]] <- formatC(100 * eq$tax_share[5], format = "f", digits = 3)
R[["TBD-76"]] <- formatC(eq$kakwani, format = "f", digits = 3)
R[["TBD-85"]] <- formatC(eq$ci_tax, format = "f", digits = 3)
R[["TBD-86"]] <- formatC(eq$ci_tax_share, format = "f", digits = 3)
R[["TBD-87"]] <- formatC(eq$gini_exp, format = "f", digits = 3)

# S2 comparison
R[["TBD-13"]] <- fmt(R[["D_S2"]])
R[["TBD-14"]] <- formatC(R[["D_S2"]] / R[["D_S1"]], format = "f", digits = 1)
R[["TBD-15"]] <- fmt(R[["REV_S2"]] / 1e9)
R[["TBD-65"]] <- formatC(R[["D_S1"]] / (R[["REV_S1"]] / 1e9), format = "f", digits = 1)
R[["TBD-66"]] <- formatC(R[["D_S2"]] / (R[["REV_S2"]] / 1e9), format = "f", digits = 1)
R[["TBD-67"]] <- formatC((R[["D_S2"]] / R[["REV_S2"]]) / (R[["D_S1"]] / R[["REV_S1"]]),
                         format = "f", digits = 2)

# reformulation levels
for (lvl in c(10, 25, 50)) {
  pl <- p0; pl$horizon <- 2050
  q0 <- qprof$ssb_ml_day
  dp <- price_change(pl$tau_2028, pl)
  dq <- consumption_change(dp, qprof$elast_mult, pl)
  rev <- sum(revenue_implied(q0, dq, dp, pl, tot_pop, base_share = 1 - lvl / 100))
  R[[paste0("TBD-", 68 + (lvl == 25) + 2 * (lvl == 50))]] <-
    formatC(lvl, format = "f", digits = 0)
}

# ---------------------------------------------------------------------------
# 3. Structural sensitivity: legal interpretation and elasticity
# ---------------------------------------------------------------------------
run_variant <- function(over) {
  pv <- p0; pv$horizon <- 2050
  for (nm in names(over)) pv[[nm]] <- over[[nm]]
  r <- run_scenario("S1", qprof, pv, mort)
  b <- run_scenario("S0", qprof, pv, mort)
  sum(b$dalys - r$dalys)
}




# static weight model: BMI change without the dynamic decay


# ---------------------------------------------------------------------------
# 4. Threshold grid
# ---------------------------------------------------------------------------
grid <- expand.grid(exfac = seq(0.30, 0.85, by = 0.05),
                    kappa = seq(0.3, 1.5, by = 0.1))
grid$dalys <- mapply(function(e, k) {
  pv <- p0; pv$exfac_share <- e; pv$passthrough <- k; pv$horizon <- 2050
  b <- run_scenario("S0", qprof, pv, mort); r <- run_scenario("S1", qprof, pv, mort)
  sum(b$dalys - r$dalys)
}, grid$exfac, grid$kappa)
write.csv(grid, file.path(OUT, "threshold_grid.csv"), row.names = FALSE)
ok <- grid[grid$dalys > 0, ]
R[["TBD-83"]] <- if (nrow(ok)) pct(min(ok$kappa), 0) else "not reached"
# minimum elasticity at which the gain stays positive, holding the rest central
el <- seq(-0.3, -2.0, by = -0.1)
g <- sapply(el, function(e) {
  pv <- p0; pv$elast_own <- e; pv$horizon <- 2050
  b <- run_scenario("S0", qprof, pv, mort); r <- run_scenario("S1", qprof, pv, mort)
  sum(b$dalys - r$dalys)
})
R[["TBD-84"]] <- formatC(abs(max(el[g > 0])), format = "f", digits = 2)

# ---------------------------------------------------------------------------
# 5. Probabilistic analysis
# ---------------------------------------------------------------------------
cat("PSA with", N_PSA, "draws...\n")
psa <- run_psa(n = N_PSA, qprof = qprof, scenarios = c("S1", "S2"), verbose = FALSE)
write.csv(psa, file.path(OUT, "psa_results.csv"), row.names = FALSE)
write.csv(as.data.frame(attr(psa, "draws")), file.path(OUT, "psa_draws.csv"), row.names = FALSE)

q <- function(x) stats::quantile(x, c(0.025, 0.5, 0.975), na.rm = TRUE)
d1 <- psa[psa$scenario == "S1", ]; d2 <- psa[psa$scenario == "S2", ]
R[["TBD-5"]]  <- paste0(fmt(q(d1$dalys_averted)[1]), "–", fmt(q(d1$dalys_averted)[3]))
R[["TBD-4"]]  <- fmt(q(d1$dalys_averted)[2])
R[["TBD-77"]] <- pct(mean(d1$dalys_averted > 0), 0)
R[["TBD-78"]] <- pct(prob_beats(psa, "S2", "S1"), 0)
R[["TBD-43"]] <- paste0(formatC(100 * q(d1$dp_avg)[1], format = "f", digits = 1), "–",
                        formatC(100 * q(d1$dp_avg)[3], format = "f", digits = 1))
R[["DP_PSA_MEDIAN"]] <- formatC(100 * q(d1$dp_avg)[2], format = "f", digits = 2)

# one-way sensitivity: variance contribution of each parameter
M <- as.data.frame(attr(psa, "draws"))
sens <- sapply(names(M), function(nm) {
  stats::cor(M[[nm]], d1$dalys_averted[seq_len(nrow(M))], use = "complete.obs")
})
sens <- sort(abs(sens), decreasing = TRUE)
top <- head(names(sens), 3)
lab <- c(exfac_share = "the ex-factory share of the retail price",
         passthrough = "the pass-through rate",
         elast_own = "the own-price elasticity",
         elast_cross_unt = "substitution to untaxed beverages",
         taxed_share = "the share of beverages above the threshold",
         compensation = "energy compensation",
         rr_t2dm = "the BMI–diabetes relative risk",
         rr_ihd = "the BMI–ischaemia relative risk",
         rr_stroke = "the BMI–stroke relative risk")
R[["TBD-79"]] <- lab[top[1]]
R[["TBD-80"]] <- lab[top[2]]
R[["TBD-81"]] <- lab[top[3]]
R[["TBD-82"]] <- pct(sum(head(sens, 3)^2) / sum(sens^2), 0)

# ---------------------------------------------------------------------------
# 6. Write
# ---------------------------------------------------------------------------
out <- lapply(R, function(x) if (length(x) == 1) as.character(x) else paste(x, collapse = " "))
json <- paste0("{\n", paste(sprintf('  "%s": "%s"', names(out),
              gsub('"', '\\\\"', unlist(out))), collapse = ",\n"), "\n}\n")
writeLines(json, file.path(OUT, "results.json"))
cat("written", length(out), "values to output/results.json\n")
print(head(data.frame(key = names(out), value = unlist(out)), 20))
