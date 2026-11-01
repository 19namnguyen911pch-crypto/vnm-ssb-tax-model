# -*- coding: utf-8 -*-
# psa_all.R — 5,000-draw PSA for all three scenarios, so that Table 3 and the
# text can report the same quantity everywhere.
suppressPackageStartupMessages({
  source("model/vhlss.R"); source("model/pmslt_model.R"); source("model/psa.R")
})
qprof <- get_quintile_profile()
res <- run_psa(n = 5000, qprof = qprof, scenarios = c("S1", "S2", "S3"), verbose = FALSE)
write.csv(res, "output/psa_results.csv", row.names = FALSE)
write.csv(as.data.frame(attr(res, "draws")), "output/psa_draws.csv", row.names = FALSE)
write.csv(summarise_psa(res), "output/psa_summary.csv", row.names = FALSE)
print(summarise_psa(res)[, c("scenario", "dalys_median", "dalys_lo", "dalys_hi",
                             "revenue_median_bn", "dalys_per_bn_median")])
