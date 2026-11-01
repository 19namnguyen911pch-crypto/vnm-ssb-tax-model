# -*- coding: utf-8 -*-
# psa_gradient.R — repeat the published draws with a socioeconomic gradient in
# baseline disease risk, so that Figure 3 can show both assumptions on the same
# iterations. The parameter draws are read from output/psa_draws.csv, so the two
# panels differ only in the gradient.
suppressPackageStartupMessages({
  source("model/vhlss.R"); source("model/pmslt_model.R"); source("model/psa.R")
})

qprof <- get_quintile_profile()
p0 <- params_default()
mort <- 0.004 * exp(0.075 * (p0$ages - 20))
GRAD <- c(1.15, 1.08, 1.00, 0.94, 0.88)

M <- as.matrix(read.csv("output/psa_draws.csv", check.names = FALSE))
n <- nrow(M)
out <- vector("list", n)

for (i in seq_len(n)) {
  p <- apply_draw(p0, M[i, ])
  p$disease_grad <- GRAD
  s0 <- run_scenario("S0", qprof, p, mort)
  rows <- lapply(c("S1", "S2"), function(k) {
    r <- run_scenario(k, qprof, p, mort)
    eq <- equity_summary(s0, r, qprof)
    data.frame(iter = i, scenario = k,
               dalys_averted = sum(s0$dalys - r$dalys),
               ci_dalys = eq$ci_dalys,
               ratio_Q1_Q5 = eq$ratio_Q1_Q5,
               kakwani = eq$kakwani)
  })
  out[[i]] <- do.call(rbind, rows)
  if (i %% 500 == 0) cat("  iteration", i, "of", n, "\n")
}

res <- do.call(rbind, out)
write.csv(res, "output/psa_gradient.csv", row.names = FALSE)
cat("\nwith gradient, medians (2.5-97.5):\n")
for (k in c("S1", "S2")) {
  d <- res[res$scenario == k, ]
  q <- function(x) round(stats::quantile(x, c(0.025, 0.5, 0.975), na.rm = TRUE), 3)
  cat(k, "| CI:", q(d$ci_dalys), "| Q1/Q5:", q(d$ratio_Q1_Q5),
      "| DALYs:", round(stats::quantile(d$dalys_averted, c(0.025, 0.5, 0.975))), "\n")
}
