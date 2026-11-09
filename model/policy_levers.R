# -*- coding: utf-8 -*-
# policy_levers.R — deterministic counterfactuals reported in the main text:
# the excise base moved to the retail price, and population ageing.
# Writes output/policy_levers.csv.
suppressPackageStartupMessages({
  source("model/vhlss.R"); source("model/pmslt_model.R")
})

qprof <- get_quintile_profile()
p0 <- params_default()
mort <- 0.004 * exp(0.075 * (p0$ages - 20))

run_one <- function(label, over = list()) {
  p <- p0
  for (nm in names(over)) p[[nm]] <- over[[nm]]
  s0 <- run_scenario("S0", qprof, p, mort)
  s1 <- run_scenario("S1", qprof, p, mort)
  d <- sum(s0$dalys - s1$dalys)
  rev <- sum(s1$revenue) / 1e9
  data.frame(
    analysis = label,
    price_change_pct = round(100 * s1$dp[1], 2),
    dalys = round(d),
    costs_saved_bn = round(sum(s0$costs - s1$costs) / 1e9),
    revenue_bn = round(rev),
    dalys_per_bn = round(d / rev, 3)
  )
}

rows <- list(
  run_one("Enacted tax, ex-factory base"),
  run_one("Same 10% rate on retail base", list(exfac_share = 1)),
  run_one("2050 age distribution", list(age_weights = load_age_weights(year = 2050))),
  run_one("2050 age distribution + zero stock",
          list(age_weights = load_age_weights(year = 2050), init_prev = FALSE))
)

out <- do.call(rbind, rows)
dir.create("output", showWarnings = FALSE)
write.csv(out, "output/policy_levers.csv", row.names = FALSE)
print(out)
