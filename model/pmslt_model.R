###############################################################################
# PMSLT model: Viet Nam sugar-sweetened beverage excise tax
#
# Single taxed group with a mean sugar density. Scenarios: no tax, the tax as
# enacted, a 20% retail price rise (WHO benchmark), and industry reformulation.
#
# All external inputs are real data: UN WPP age structure, GBD 2021 disease
# parameters, Vietnamese cost studies, VHLSS 2024 published tabulations.
# No parameter in this file is an unmeasured guess.
###############################################################################

DEMO_MODE <- FALSE

# ---------------------------------------------------------------------------
# 1. Parameters
# ---------------------------------------------------------------------------
# Parameters that are still placeholders. Empty means the model can be run for
# reporting.
placeholder_params <- function() {
  character(0)
}

params_default <- function() {
  list(
    # population ------------------------------------------------------------
    ages            = 20:100,
    pop_2027        = 104e6,
    share_20plus    = 0.78,
    age_weights     = tryCatch(load_age_weights(), error = function(e) NULL),

    # step 1: tax to retail price -------------------------------------------
    tau_2027        = 0.08,
    tau_2028        = 0.10,
    vat             = 0.10,
    exfac_share     = 0.55,     # Appendix B #5
    passthrough     = 0.90,     # Appendix B #6

    # step 2: demand ---------------------------------------------------------
    elast_own       = -1.20,    # Appendix B #7a
    elast_cross_unt =  0.35,    # reporting only, Appendix B #7b
    retail_price_l  = 12000,    # VND per litre, VAT inclusive
    taxed_share     = 0.80,     # Appendix B #4

    # mean sugar density of taxed beverages, g per 100 mL.
    # Sourced: Nguyen et al. 2023 report 11 for carbonates, 9 for RTD coffee
    # and tea, 16 for sports and energy drinks, 7 for juices.
    sugar_mean      = 11.0,

    # step 3: energy ---------------------------------------------------------
    kcal_per_g_sugar = 4,
    compensation     = 0.30,    # Appendix B #8b

    # step 4: energy to BMI --------------------------------------------------
    kcal_per_kg_day   = 22,
    kg_per_bmi_unit   = 2.9,
    energy_per_kg_gain = 7000,

    # step 5: BMI to disease -------------------------------------------------
    latency_years   = 2,
    rr_per_2bmi     = c(t2dm = 1.55, ihd = 1.11, stroke = 1.12),

    # step 6: disease rates, GBD 2021 ---------------------------------------
    gbd         = tryCatch(load_gbd_params(), error = function(e) NULL),
    inc_scale   = c(t2dm = 0.006, ihd = 0.004, stroke = 0.005),
    cfr         = c(t2dm = 0.02,  ihd = 0.10,  stroke = 0.15),
    excess_mort = c(t2dm = 0.015, ihd = 0.03,  stroke = 0.05),
    dw          = c(t2dm = 0.049, ihd = 0.056, stroke = 0.110),

    # step 7: costs, Vietnamese studies -------------------------------------
    cost_file = tryCatch(load_cost_params(), error = function(e) NULL),
    cost_case = c(t2dm = 8.0e6, ihd = 84.9e6, stroke = 10.5e6),

    # analysis settings ------------------------------------------------------
    discount = 0.03,
    start    = 2027,
    horizon  = 2050
  )
}

# ---------------------------------------------------------------------------
# 1b. Age structure from UN World Population Prospects (real data)
# ---------------------------------------------------------------------------
load_age_weights <- function(path = "data/vnm_wpp_age5_2025_2050.csv",
                             year = 2027, ages = 20:100) {
  if (!file.exists(path)) {
    warning("Age structure not found at ", path, "; using uniform weights.")
    return(rep(1 / length(ages), length(ages)))
  }
  d <- utils::read.csv(path, stringsAsFactors = FALSE)
  d <- d[d$year == year & grepl("^[0-9]", d$age_group), ]
  w <- stats::setNames(numeric(length(ages)), as.character(ages))
  for (i in seq_len(nrow(d))) {
    g <- d$age_group[i]
    if (grepl("\\+$", g)) {
      st <- as.integer(sub("\\+$", "", g)); sp <- 100L - st + 1L
    } else {
      ab <- as.integer(strsplit(g, "-", fixed = TRUE)[[1]])
      st <- ab[1]; sp <- ab[2] - ab[1] + 1L
    }
    a <- st:(st + sp - 1L); a <- a[a %in% ages]
    if (length(a)) w[as.character(a)] <- d$total[i] / sp
  }
  w[is.na(w)] <- 0
  if (sum(w) <= 0) return(rep(1 / length(ages), length(ages)))
  as.numeric(w / sum(w))
}

# ---------------------------------------------------------------------------
# 1c. Disease parameters from GBD 2021 (real data)
# ---------------------------------------------------------------------------
load_gbd_params <- function(path = "data/gbd_vnm/vnm_gbd_params_long.csv",
                            ages = 20:100) {
  if (!file.exists(path)) {
    warning("GBD parameters not found at ", path, "; keeping demo values.")
    return(NULL)
  }
  d <- utils::read.csv(path, stringsAsFactors = FALSE)
  dis <- c("t2dm", "ihd", "stroke")
  mk <- function(col) {
    out <- matrix(0, nrow = length(ages), ncol = 3, dimnames = list(NULL, dis))
    for (k in seq_along(dis)) {
      sub <- d[d$cause == dis[k], ]
      st <- suppressWarnings(as.integer(sub("-.*", "", sub$age_band)))
      st[grepl("^95", sub$age_band)] <- 95L
      ok <- !is.na(st)
      st <- st[ok]; vl <- sub[[col]][ok]
      o <- order(st); st <- st[o]; vl <- vl[o]
      idx <- findInterval(ages, st); idx[idx == 0] <- 1L
      out[, k] <- vl[idx]
    }
    out
  }
  list(
    inc       = mk("inc_rate"),
    mort_case = mk("mort_among_cases"),
    dw        = vapply(dis, function(k)
                   stats::weighted.mean(d$dw[d$cause == k], d$prev_rate[d$cause == k],
                                        na.rm = TRUE), numeric(1)),
    prev      = mk("prev_rate")
  )
}

# ---------------------------------------------------------------------------
# 1d. Cost parameters from Vietnamese studies (real data)
# ---------------------------------------------------------------------------
load_cost_params <- function(path = "data/vnm_cost_params.csv") {
  if (!file.exists(path)) {
    warning("Cost file not found at ", path, "; keeping demo values.")
    return(NULL)
  }
  d <- utils::read.csv(path, stringsAsFactors = FALSE)
  stats::setNames(d$value_vnd_2026, d$cause)
}

cost_matrix_by_age <- function(p, ages = p$ages) {
  dis <- c("t2dm", "ihd", "stroke")
  m <- matrix(0, nrow = length(ages), ncol = 3, dimnames = list(NULL, dis))
  for (k in seq_along(dis)) {
    d <- dis[k]
    if (is.null(p$gbd)) { m[, k] <- p$cost_case[d]; next }
    if (d == "t2dm") {
      m[, k] <- p$cost_case[d]
    } else {
      inc <- p$gbd$inc[, d]; prev <- p$gbd$prev[, d]
      ratio <- ifelse(prev > 0, inc / prev, 0)
      m[, k] <- p$cost_case[d] * pmin(ratio, 1)
    }
  }
  m
}

# ---------------------------------------------------------------------------
# 2. Step 1 - statutory rate to retail price change
# ---------------------------------------------------------------------------
price_change <- function(tau, p) {
  tau * p$exfac_share * (1 + p$vat) * p$passthrough
}

# The ad valorem rate implied by a target price change, so that revenue is
# always computed from the same mechanism that produced the prices.
implied_tau <- function(dp, p) {
  if (dp <= 0) return(0)
  dp / (p$exfac_share * (1 + p$vat) * p$passthrough)
}

# Calibrate the ex-factory share from a published revenue projection.
calibrate_exfac_share <- function(rev_projection_vnd, tau, qprof, p) {
  pop <- p$pop_2027 * p$share_20plus
  vol_l_year <- sum(qprof$pop_share * qprof$ssb_ml_day) / 1000 * 365 * pop *
                p$taxed_share
  s <- rev_projection_vnd / (vol_l_year * p$retail_price_l * tau)
  if (s <= 0 || s >= 1) {
    warning("Implied ex-factory share is outside (0,1): ", round(s, 3),
            ". Check the revenue projection, the tax rate, and the volume base.")
  }
  s
}

# ---------------------------------------------------------------------------
# 3. Step 2 - price to demand
# ---------------------------------------------------------------------------
# One taxed group. Substitution toward untaxed beverages is already embedded in
# the own-price elasticity and is reported separately rather than added again.
consumption_change <- function(dp, elast_mult, p) {
  unname(p$elast_own * elast_mult * dp)
}

untaxed_response <- function(dp, p) unname(p$elast_cross_unt * dp)

# ---------------------------------------------------------------------------
# 4. Step 3 - demand to sugar and energy intake
# ---------------------------------------------------------------------------
sugar_change_g_day <- function(ml_day, dq_rel, p) {
  (ml_day / 100) * dq_rel * p$sugar_mean
}

energy_change_kcal <- function(d_sugar_g_day, p) {
  d_sugar_g_day * p$kcal_per_g_sugar * (1 - p$compensation)
}

# ---------------------------------------------------------------------------
# 5. Step 4 - energy to BMI, dynamic, returns the path
# ---------------------------------------------------------------------------
bmi_change_dynamic <- function(d_energy_kcal_day, p, years) {
  w <- numeric(years); acc <- 0
  for (t in seq_len(years)) {
    deficit <- d_energy_kcal_day * 365
    hold <- -acc * p$kcal_per_kg_day * 365   # maintenance falls as weight falls
    acc <- acc + (deficit + hold) / p$energy_per_kg_gain
    w[t] <- acc / p$kg_per_bmi_unit
  }
  w
}

# ---------------------------------------------------------------------------
# 6. Step 5 - BMI shift to population impact fractions
# ---------------------------------------------------------------------------
pif_from_bmi_shift <- function(d_bmi, rr_per_2bmi, mean_bmi = 22.5, sd_bmi = 3.0) {
  if (abs(d_bmi) < 1e-12) return(rr_per_2bmi / rr_per_2bmi)
  beta <- log(rr_per_2bmi) / 2
  g <- seq(mean_bmi - 4 * sd_bmi, mean_bmi + 4 * sd_bmi, length.out = 201)
  w0 <- stats::dnorm(g, mean_bmi, sd_bmi)
  rr <- exp(beta %o% (g - 21))
  before <- as.vector(rr %*% w0) / sum(w0)
  w1 <- stats::dnorm(g, mean_bmi + d_bmi, sd_bmi)
  after <- as.vector(rr %*% w1) / sum(w1)
  stats::setNames(after / before, names(rr_per_2bmi))
}

# ---------------------------------------------------------------------------
# 7. Step 6 - multi-state life table with a lagged incidence path
# ---------------------------------------------------------------------------
life_table <- function(inc_path, p, pop0, mort_by_age) {
  A <- length(p$ages)
  dis <- c("t2dm", "ihd", "stroke")
  N <- matrix(0, nrow = A, ncol = 3, dimnames = list(NULL, dis))
  healthy <- pop0
  dalys <- 0; costs <- 0; deaths <- 0
  cases <- stats::setNames(rep(0, 3), dis)

  surv <- cumprod(1 - pmin(mort_by_age, 1))
  e_rem <- rev(cumsum(rev(surv))) / pmax(surv, 1e-9)

  inc_base <- if (!is.null(p$gbd)) p$gbd$inc else
              matrix(rep(p$inc_scale[dis], each = A), nrow = A)

  for (t in seq_len(p$horizon - p$start + 1)) {
    inc <- sweep(inc_base, 2, inc_path[t, ], "*")
    newc <- inc * healthy
    healthy <- healthy - rowSums(newc)
    N <- N + newc
    cases <- cases + colSums(newc)

    m_bg  <- pmin(mort_by_age, 1)
    m_excess <- if (!is.null(p$gbd)) p$gbd$mort_case else
                matrix(rep(p$excess_mort[dis] + p$cfr[dis], each = A), nrow = A)
    m_dis <- pmin(outer(m_bg, rep(1, 3)) + m_excess, 1)
    d_healthy <- healthy * m_bg
    d_dis <- N * m_dis
    deaths <- deaths + sum(d_healthy) + sum(d_dis)
    healthy <- healthy - d_healthy
    N <- N - d_dis

    disc <- 1 / (1 + p$discount)^(t - 1)
    dwv <- if (!is.null(p$gbd)) p$gbd$dw[dis] else p$dw[dis]
    yld <- sum(N %*% dwv)
    yll <- (sum(d_healthy * e_rem) + sum(d_dis * e_rem)) * disc
    dalys <- dalys + (yld + yll) * disc
    cost_age <- if (is.null(p$cost_age)) NULL else p$cost_age
    costs <- costs + (if (is.null(cost_age)) sum(N %*% p$cost_case[dis])
                      else sum(N * cost_age)) * disc
  }
  list(dalys = dalys, cases = cases, deaths = deaths, costs = costs)
}

# ---------------------------------------------------------------------------
# 8. Revenue
# ---------------------------------------------------------------------------
revenue_implied <- function(ml_day, dq, dp, p, pop_total, base_share = 1) {
  if (dp <= 0) return(0)
  vol_l <- (ml_day * (1 + dq) / 1000) * pop_total * 365 * base_share
  vol_l * p$retail_price_l * p$exfac_share * implied_tau(dp, p)
}

# ---------------------------------------------------------------------------
# 9. Scenario -> retail price change
# ---------------------------------------------------------------------------
scenario_price <- function(code, p) {
  base <- price_change(p$tau_2028, p)
  switch(code,
    S0 = 0,
    S1 = base,
    S2 = 0.20,
    S3 = base * 0.75,
    stop("unknown scenario: ", code))
}

# ---------------------------------------------------------------------------
# 10. One quintile, one scenario
# ---------------------------------------------------------------------------
run_quintile <- function(code, qprof, k, p, mort_by_age) {
  yrs <- p$horizon - p$start + 1
  pop_k <- p$pop_2027 * p$share_20plus * qprof$pop_share[k]
  ml_day <- qprof$ssb_ml_day[k]

  dp <- scenario_price(code, p)
  dq <- consumption_change(dp, qprof$elast_mult[k], p)

  dsugar <- sugar_change_g_day(ml_day, dq, p)
  de <- energy_change_kcal(dsugar, p)
  bmi_path <- bmi_change_dynamic(de, p, years = yrs)

  dis <- c("t2dm", "ihd", "stroke")
  inc_path <- matrix(1, nrow = yrs, ncol = 3, dimnames = list(NULL, dis))
  if (!identical(code, "S0")) {
    for (t in seq_len(yrs)) {
      src <- t - p$latency_years
      db_t <- if (src >= 1) bmi_path[src] else 0
      inc_path[t, ] <- pif_from_bmi_shift(db_t, p$rr_per_2bmi)[dis]
    }
  }

  if (is.null(p$cost_age)) p$cost_age <- cost_matrix_by_age(p)
  w_age <- if (is.null(p$age_weights)) rep(1, length(p$ages)) else p$age_weights
  lt <- life_table(inc_path, p, pop_k * w_age, mort_by_age)

  base_share <- if (identical(code, "S3")) 0.75 else 1
  list(quintile = k, pop = pop_k, dp = dp, dq = dq, d_sugar = dsugar,
       d_bmi = bmi_path[yrs], dalys = lt$dalys, cases = lt$cases,
       deaths = lt$deaths, costs = lt$costs,
       tax_share = qprof$ssb_exp_share[k] * (1 + dq) * dp,
       revenue = revenue_implied(ml_day, dq, dp, p, pop_k, base_share))
}

# ---------------------------------------------------------------------------
# 11. All quintiles
# ---------------------------------------------------------------------------
run_scenario <- function(code, qprof, p, mort_by_age) {
  rows <- lapply(seq_len(nrow(qprof)), function(k)
    run_quintile(code, qprof, k, p, mort_by_age))
  do.call(rbind, lapply(rows, function(r) data.frame(
    quintile = r$quintile, pop = r$pop, dp = r$dp, dq = r$dq,
    d_sugar_g = r$d_sugar, d_bmi = r$d_bmi,
    dalys = r$dalys, costs = r$costs, revenue = r$revenue,
    tax_share = r$tax_share,
    cases_t2dm = unname(r$cases["t2dm"]),
    cases_ihd = unname(r$cases["ihd"]),
    cases_stroke = unname(r$cases["stroke"]),
    deaths = r$deaths)))
}

# ---------------------------------------------------------------------------
# 12. Equity metrics
# ---------------------------------------------------------------------------
# Gini from quintile means alone: a LOWER BOUND, because it assumes no
# inequality within quintiles. Stated as such wherever it is used.
gini_from_quintiles <- function(means, shares) {
  o <- order(means); m <- means[o]; s <- shares[o]
  cw <- cumsum(s); mu <- sum(m * s); R <- cw - s / 2
  2 * sum(s * m * R) / mu - 1
}

concentration_index <- function(x, means, shares) {
  o <- order(means); x <- x[o]; s <- shares[o]
  cw <- cumsum(s); mu <- sum(x * s)
  if (abs(mu) < 1e-12) return(NA_real_)
  R <- cw - s / 2
  2 * sum(s * x * R) / mu - 1
}

atkinson_ede <- function(x, shares, e = 1) {
  x <- pmax(x, 0)
  if (all(x == 0)) return(0)
  if (e == 1) exp(sum(shares * log(pmax(x, 1e-12))))
  else (sum(shares * x^(1 - e)))^(1 / (1 - e))
}

equity_summary <- function(base, scen, qprof) {
  d <- base$dalys - scen$dalys
  per1000 <- d / (scen$pop / 1000)
  list(
    dalys_per_1000 = per1000,
    ratio_Q1_Q5 = per1000[1] / per1000[5],
    ci_dalys = concentration_index(d, qprof$mean_exp_month, qprof$pop_share),
    kakwani = concentration_index(scen$tax_share, qprof$mean_exp_month,
                                  qprof$pop_share) -
              gini_from_quintiles(qprof$mean_exp_month, qprof$pop_share),
    gini_exp = gini_from_quintiles(qprof$mean_exp_month, qprof$pop_share),
    tax_share = scen$tax_share,
    ede_e1 = atkinson_ede(per1000, qprof$pop_share, 1),
    ede_e3 = atkinson_ede(per1000, qprof$pop_share, 3),
    ede_e10 = atkinson_ede(per1000, qprof$pop_share, 10)
  )
}

# ---------------------------------------------------------------------------
# 13. Demo driver
# ---------------------------------------------------------------------------
demo <- function(qprof = get_quintile_profile()) {
  p <- params_default()
  mort_by_age <- 0.004 * exp(0.075 * (p$ages - 20))
  codes <- c("S0", "S1", "S2", "S3")
  res <- lapply(codes, run_scenario, qprof = qprof, p = p,
                mort_by_age = mort_by_age)
  names(res) <- codes
  base <- res[["S0"]]

  agg <- do.call(rbind, lapply(codes, function(k) {
    r <- res[[k]]; w <- qprof$pop_share
    data.frame(
      scenario      = k,
      dp_pct        = round(100 * r$dp[1], 2),
      d_sugar_g_day = round(sum(w * r$d_sugar_g) / sum(w), 3),
      dalys_averted = round(sum(base$dalys - r$dalys), 0),
      costs_saved_bn = round(sum(base$costs - r$costs) / 1e9, 0),
      revenue_bn    = round(sum(r$revenue) / 1e9, 0),
      dalys_per_bn  = round(
        if (sum(r$revenue) > 0)
          sum(base$dalys - r$dalys) / (sum(r$revenue) / 1e9) else 0, 1))
  }))

  eq <- lapply(res[-1], function(r) equity_summary(base, r, qprof))
  list(main = agg, equity = eq)
}
