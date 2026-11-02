###############################################################################
# psa.R — probabilistic sensitivity analysis and output writing
#
# Deliberately simple: draw a parameter matrix, re-run the model for each row,
# store results, publish the matrix. The matrix is part of the published
# materials (Appendix H), so anyone can reproduce the distributions without
# re-running the sampling.
#
# Runtime: one model run is ~3 ms; 5,000 iterations x 5 scenarios x 5 quintiles
# is roughly 20-40 minutes on a laptop. Use n = 500 while developing.
###############################################################################

# ---------------------------------------------------------------------------
# Distributions for the parameters that carry real uncertainty
# ---------------------------------------------------------------------------
# Each entry: name, distribution, arguments, and where it enters params.
# Appendix B fixes the values; this function must stay in step with it.
psa_spec <- function() {
  list(
    list(name = "exfac_share",  dist = "tri",  args = list(min = 0.40, mode = 0.55, max = 0.70), scale = 1),
    list(name = "passthrough",  dist = "tri",  args = list(min = 0.50, mode = 0.90, max = 1.30), scale = 1),
    list(name = "elast_own",    dist = "lnorm_abs", args = list(meanlog = log(1.20), sdlog = 0.30), scale = 1),
    list(name = "elast_cross_unt", dist = "lnorm", args = list(meanlog = log(0.35), sdlog = 0.40), scale = 1),
    list(name = "compensation", dist = "unif", args = list(min = 0.15, max = 0.45), scale = 1),
    list(name = "rr_t2dm",      dist = "lnorm", args = list(meanlog = log(1.37), sdlog = 0.08), scale = 1),
    list(name = "rr_ihd",       dist = "lnorm", args = list(meanlog = log(1.11), sdlog = 0.06), scale = 1),
    list(name = "rr_stroke",    dist = "lnorm", args = list(meanlog = log(1.12), sdlog = 0.06), scale = 1)
  )
}

sample_one <- function(spec) {
  d <- spec$dist
  a <- spec$args
  switch(d,
    tri = {
      # inverse CDF of the triangular distribution
      u <- stats::runif(1)
      Fm <- (a$mode - a$min) / (a$max - a$min)
      if (u < Fm) a$min + sqrt(u * (a$max - a$min) * (a$mode - a$min))
      else a$max - sqrt((1 - u) * (a$max - a$min) * (a$max - a$mode))
    },
    unif   = stats::runif(1, a$min, a$max),
    beta   = stats::rbeta(1, a$shape1, a$shape2),
    lnorm  = stats::rlnorm(1, a$meanlog, a$sdlog),
    lnorm_abs = -stats::rlnorm(1, a$meanlog, a$sdlog),
    stop("unknown distribution: ", d)
  )
}

draw_parameter_matrix <- function(n = 500, seed = 20261101) {
  set.seed(seed)
  spec <- psa_spec()
  M <- sapply(spec, function(s) replicate(n, sample_one(s)))
  colnames(M) <- vapply(spec, `[[`, character(1), "name")
  M
}

# ---------------------------------------------------------------------------
# Map one draw onto a parameter list
# ---------------------------------------------------------------------------
apply_draw <- function(p, row) {
  p$exfac_share    <- row[["exfac_share"]]
  p$passthrough    <- row[["passthrough"]]
  p$elast_own      <- row[["elast_own"]]
  p$elast_cross_unt <- row[["elast_cross_unt"]]
  p$compensation   <- row[["compensation"]]
  p$rr_per_2bmi    <- c(t2dm = row[["rr_t2dm"]],
                        ihd  = row[["rr_ihd"]],
                        stroke = row[["rr_stroke"]])
  p
}

# ---------------------------------------------------------------------------
# Run the PSA
# ---------------------------------------------------------------------------
run_psa <- function(n = 500, qprof = get_quintile_profile(),
                    scenarios = c("S1", "S2"), seed = 20261101,
                    verbose = TRUE) {
  p0 <- params_default()
  mort <- 0.004 * exp(0.075 * (p0$ages - 20))
  M <- draw_parameter_matrix(n, seed)

  out <- vector("list", n)
  for (i in seq_len(n)) {
    if (verbose && i %% 50 == 0) cat("  iteration", i, "of", n, "\n")
    p <- apply_draw(p0, M[i, ])
    s0 <- run_scenario("S0", qprof, p, mort)
    rows <- lapply(scenarios, function(k) {
      r <- run_scenario(k, qprof, p, mort)
      eq <- equity_summary(s0, r, qprof)
      data.frame(
        iter = i, scenario = k,
        dp_avg = r$dp[1],
        dalys_averted = sum(s0$dalys - r$dalys),
        costs_saved = sum(s0$costs - r$costs),
        revenue = sum(r$revenue),
        dalys_per_1000_Q1 = eq$dalys_per_1000[1],
        dalys_per_1000_Q5 = eq$dalys_per_1000[5],
        ci_dalys = eq$ci_dalys,
        kakwani = eq$kakwani,
        ede_e3 = eq$ede_e3
      )
    })
    out[[i]] <- do.call(rbind, rows)
  }
  res <- do.call(rbind, out)
  attr(res, "draws") <- M
  attr(res, "seed") <- seed
  res
}

# ---------------------------------------------------------------------------
# Summarise
# ---------------------------------------------------------------------------
summarise_psa <- function(res) {
  do.call(rbind, lapply(split(res, res$scenario), function(d) {
    q <- function(x) stats::quantile(x, c(0.025, 0.5, 0.975), na.rm = TRUE)
    data.frame(
      scenario = d$scenario[1],
      dp_median = round(100 * q(d$dp_avg)[2], 2),
      dp_lo = round(100 * q(d$dp_avg)[1], 2),
      dp_hi = round(100 * q(d$dp_avg)[3], 2),
      dalys_median = round(q(d$dalys_averted)[2], 0),
      dalys_lo = round(q(d$dalys_averted)[1], 0),
      dalys_hi = round(q(d$dalys_averted)[3], 0),
      revenue_median_bn = round(q(d$revenue)[2] / 1e9, 0),
      dalys_per_bn_median = round(q(d$dalys_averted / (d$revenue / 1e9))[2], 1),
      prob_positive = round(mean(d$dalys_averted > 0, na.rm = TRUE), 3)
    )
  }))
}

# Probability that one scenario beats another, matched by iteration.
prob_beats <- function(res, better = "S2", worse = "S1") {
  a <- res[res$scenario == better, c("iter", "dalys_averted")]
  b <- res[res$scenario == worse,  c("iter", "dalys_averted")]
  m <- merge(a, b, by = "iter")
  mean(m$dalys_averted.x > m$dalys_averted.y, na.rm = TRUE)
}

# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------
write_psa_outputs <- function(res, dir = "output") {
  dir.create(dir, showWarnings = FALSE, recursive = TRUE)
  utils::write.csv(res, file.path(dir, "psa_results.csv"), row.names = FALSE)
  utils::write.csv(as.data.frame(attr(res, "draws")),
                   file.path(dir, "psa_draws.csv"), row.names = FALSE)
  utils::write.csv(summarise_psa(res),
                   file.path(dir, "psa_summary.csv"), row.names = FALSE)
  cat("Seed:", attr(res, "seed"), "\n")
  cat("Written to", normalizePath(dir), "\n")
  invisible(TRUE)
}
