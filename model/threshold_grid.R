# -*- coding: utf-8 -*-
# threshold_grid.R — two-way grid over the ex-factory share and pass-through.
# Writes output/threshold_grid.csv.
suppressPackageStartupMessages({
  source("model/vhlss.R"); source("model/pmslt_model.R")
})
qprof <- get_quintile_profile()
p0 <- params_default()
mort <- 0.004 * exp(0.075 * (p0$ages - 20))
base <- run_scenario("S0", qprof, p0, mort)
grid <- expand.grid(exfac = seq(0.30, 0.85, by = 0.05),
                    kappa = seq(0.30, 1.50, by = 0.10))
out <- do.call(rbind, lapply(seq_len(nrow(grid)), function(i) {
  p <- p0; p$exfac_share <- grid$exfac[i]; p$passthrough <- grid$kappa[i]
  r <- run_scenario("S1", qprof, p, mort)
  data.frame(exfac = grid$exfac[i], kappa = grid$kappa[i],
             dalys = sum(base$dalys - r$dalys))
}))
dir.create("output", showWarnings = FALSE)
write.csv(out, "output/threshold_grid.csv", row.names = FALSE)
cat("wrote", nrow(out), "grid points\n")
