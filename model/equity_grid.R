# -*- coding: utf-8 -*-
# 3x3 grid: disease gradient x elasticity gradient, for the equity results.
suppressPackageStartupMessages({
  source("model/vhlss.R"); source("model/pmslt_model.R")
})

p0 <- params_default()
mort <- 0.004 * exp(0.075 * (p0$ages - 20))
elast_base <- c(1.18, 1.09, 1.00, 0.92, 0.85)

# elasticity gradient expressed as the Q1/Q5 ratio of the multiplier
elast_mult_for <- function(R) {
  t <- (R - 1) / (0.18 + 0.15 * R)
  1 + t * (elast_base - 1)
}

disease <- list(
  "risk rises"  = c(0.88, 0.94, 1.00, 1.08, 1.15),
  "none"        = c(1, 1, 1, 1, 1),
  "risk falls"  = c(1.15, 1.08, 1.00, 0.94, 0.88)
)

rows <- list()
for (dn in names(disease)) for (R in c(1.0, 1.39, 1.8)) {
  qp <- get_quintile_profile()
  qp$elast_mult <- elast_mult_for(R)
  p <- p0
  p$disease_grad <- disease[[dn]]
  b <- run_scenario("S0", qp, p, mort)
  s1 <- run_scenario("S1", qp, p, mort)
  e <- equity_summary(b, s1, qp)
  rows[[length(rows) + 1]] <- data.frame(
    disease = dn, elast = R,
    ratio = round(e$ratio_Q1_Q5, 2),
    ci = round(e$ci_dalys, 3),
    kakwani = round(e$kakwani, 3),
    tax_q1 = round(100 * e$tax_share[1], 3),
    tax_q5 = round(100 * e$tax_share[5], 3),
    dalys = round(sum(b$dalys - s1$dalys))
  )
}
out <- do.call(rbind, rows)
print(out, row.names = FALSE)
write.csv(out, "output/equity_grid.csv", row.names = FALSE)
