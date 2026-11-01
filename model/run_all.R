###############################################################################
# run_all.R — driver
#
#   Rscript model/run_all.R            # development: PSA with 200 draws
#   PSA_N=5000 Rscript model/run_all.R # final run
#
# Set VHLSS_FILE to the path of the household microdata file to use real
# expenditure data; otherwise the documented fallback profile is used and the
# output says so.
###############################################################################

suppressPackageStartupMessages({
  source("model/vhlss.R")
  source("model/pmslt_model.R")
  source("model/psa.R")
})

psa_n <- as.integer(Sys.getenv("PSA_N", "200"))
vhlss_file <- Sys.getenv("VHLSS_FILE", "")

cat("================================================================\n")
cat("PMSLT model — Viet Nam SSB excise tax\n")
cat("DEMO_MODE:", DEMO_MODE, "\n")
cat("Placeholders left:", length(placeholder_params()), "\n")
cat("PSA draws:", psa_n, "\n")
cat("Age structure:", if (is.null(params_default()$age_weights)) "UNIFORM (no data file)" else "UN WPP 2024, Viet Nam", "\n")
cat("Placeholder parameters:", paste(placeholder_params(), collapse=", "), "\n")

qprof <- get_quintile_profile(if (nzchar(vhlss_file)) vhlss_file else NULL)
cat("Quintile profile:", attr(qprof, "source"), "\n")
if (isTRUE(qprof$FALLBACK[1])) {
  cat("  >> Quintile means are calibrated to the PUBLISHED VHLSS 2024\n")
  cat("     tabulations (mean 3.0m VND, Q5/Q1 = 3.1). SSB volume by quintile\n")
  cat("     and the elasticity gradient are stated assumptions. Microdata\n")
  cat("     would replace both.\n")
}
cat("================================================================\n\n")

cat("--- deterministic run (central parameter values) ---\n")
d <- demo(qprof)
print(d$main)

cat("\n--- equity, S1 vs S0 ---\n")
eq <- d$equity[["S1"]]
cat(sprintf("DALYs averted per 1,000: Q1 = %.2f, Q5 = %.2f (ratio %.2f)\n",
            eq$dalys_per_1000[1], eq$dalys_per_1000[5], eq$ratio_Q1_Q5))
cat(sprintf("Concentration index of DALYs averted: %.3f (negative = pro-poor)\n",
            eq$ci_dalys))
cat(sprintf("Tax as %% of expenditure: Q1 = %.3f%%, Q5 = %.3f%%\n",
            100 * eq$tax_share[1], 100 * eq$tax_share[5]))
cat(sprintf("Kakwani index: %.3f (negative = regressive financing)\n", eq$kakwani))
cat(sprintf("Gini of expenditure (quintile means only, lower bound): %.3f\n",
            eq$gini_exp))

cat("\n--- probabilistic sensitivity analysis ---\n")
res <- run_psa(n = psa_n, qprof = qprof,
               scenarios = c("S1", "S2"))
cat("\n")
print(summarise_psa(res))
cat("\nP(S2 > S1) =", round(prob_beats(res, "S2", "S1"), 3), "\n")


write_psa_outputs(res)

cat("\n================================================================\n")
cat("If DEMO_MODE is TRUE none of the above is a result.\n")
cat("================================================================\n")
