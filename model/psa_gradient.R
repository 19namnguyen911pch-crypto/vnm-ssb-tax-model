# -*- coding: utf-8 -*-
# psa_gradient.R — repeat the published draws under two socioeconomic gradients
# in baseline disease risk, in both directions, so that the manuscript can
# report a range rather than a single assumed direction.
# The parameter draws are read from output/psa_draws.csv, so every run differs
# only in the gradient.
suppressPackageStartupMessages({
  source("model/vhlss.R"); source("model/pmslt_model.R"); source("model/psa.R")
})

qprof <- get_quintile_profile()
p0 <- params_default()
mort <- 0.004 * exp(0.075 * (p0$ages - 20))

GRADS <- list(
  none    = c(1.00, 1.00, 1.00, 1.00, 1.00),
  pro_poor = c(1.15, 1.08, 1.00, 0.94, 0.88),   # risk falls as expenditure rises
  pro_rich = c(0.88, 0.94, 1.00, 1.08, 1.15)    # risk rises with expenditure
)

M <- as.matrix(read.csv("output/psa_draws.csv", check.names = FALSE))
n <- nrow(M)
out <- list()

for (gn in names(GRADS)) {
  cat("\n== gradient:", gn, "==\n")
  rows <- vector("list", n)
  for (i in seq_len(n)) {
    p <- apply_draw(p0, M[i, ])
    p$disease_grad <- GRADS[[gn]]
    s0 <- run_scenario("S0", qprof, p, mort)
    rr <- lapply(c("S1", "S2"), function(k) {
      r <- run_scenario(k, qprof, p, mort)
      eq <- equity_summary(s0, r, qprof)
      data.frame(iter = i, scenario = k, grad = gn,
                 dalys_averted = sum(s0$dalys - r$dalys),
                 ci_dalys = eq$ci_dalys,
                 ratio_Q1_Q5 = eq$ratio_Q1_Q5,
                 ci_tax = eq$ci_tax,
                 kakwani = eq$kakwani)
    })
    rows[[i]] <- do.call(rbind, rr)
    if (i %% 1000 == 0) cat("  iteration", i, "of", n, "\n")
  }
  out[[gn]] <- do.call(rbind, rows)
}

res <- do.call(rbind, out)
write.csv(res, "output/psa_gradient.csv", row.names = FALSE)

cat("\nmedians (2.5-97.5) with each gradient:\n")
for (gn in names(GRADS)) for (k in c("S1", "S2")) {
  d <- res[res$grad == gn & res$scenario == k, ]
  q <- function(x) round(stats::quantile(x, c(0.025, 0.5, 0.975), na.rm = TRUE), 3)
  cat(sprintf("%-8s %s | CI %s | Q1/Q5 %s | DALYs %s\n", gn, k,
              paste(q(d$ci_dalys), collapse = " "),
              paste(q(d$ratio_Q1_Q5), collapse = " "),
              paste(round(stats::quantile(d$dalys_averted, c(0.025, 0.5, 0.975))), collapse = " ")))
}
