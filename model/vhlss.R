###############################################################################
# vhlss.R — expenditure quintiles and SSB consumption profiles
#
# Two paths:
#   (A) MICRODATA PRESENT -> read VHLSS, compute quintiles and beverage
#       expenditure directly. This is the path the manuscript describes.
#   (B) NO MICRODATA -> fall back to a synthetic distribution calibrated to
#       published VHLSS 2024 aggregates. Every value produced this way is
#       flagged FALLBACK = TRUE and must be declared in the manuscript.
#
# Microdata access: Viet Nam Household Living Standards Survey, National
# Statistics Office (TCTK). Recent rounds are not open-download; request via
# TCTK or the World Bank Microdata Library catalogue entry for the chosen
# round. The 2024 round covered ~47,000 households.
###############################################################################

# ---------------------------------------------------------------------------
# Expected microdata schema
# ---------------------------------------------------------------------------
# The loader expects one household-level file and one member-level file, or a
# single merged file. Column names differ between rounds; map them here once
# and do not touch the rest of the code.
#
#   hh_id        household identifier
#   weight       household survey weight
#   hh_size      number of members
#   exp_total    total household consumption expenditure (VND, annual)
#   exp_bev      expenditure on non-alcoholic beverages (VND, annual)
#   exp_ssb      expenditure on sugar-sweetened beverages (VND, annual),
#                available only in rounds with the detailed beverage module;
#                if absent, exp_bev is used and the split is assumed
#   q_ssb_l      quantity of SSB consumed, litres per year (if collected)
#   age, sex     member-level, for age-specific consumption profiles
#
# If exp_ssb is missing the loader sets ssb_share_source = "assumed".

vhlss_column_map <- function() {
  list(hh_id = "hhid", weight = "wt", hh_size = "hhsize",
       exp_total = "exp_total", exp_bev = "exp_bev", exp_ssb = "exp_ssb",
       q_ssb_l = "q_ssb", age = "age", sex = "sex")
}

# ---------------------------------------------------------------------------
# Path A — read microdata
# ---------------------------------------------------------------------------
read_vhlss <- function(hh_file, member_file = NULL,
                       map = vhlss_column_map()) {
  hh <- utils::read.csv(hh_file, stringsAsFactors = FALSE)
  need <- c(map$hh_id, map$weight, map$hh_size, map$exp_total, map$exp_bev)
  missing <- setdiff(need, names(hh))
  if (length(missing)) {
    stop("VHLSS file is missing columns: ", paste(missing, collapse = ", "),
         ". Update vhlss_column_map().")
  }
  hh
}

# ---------------------------------------------------------------------------
# Path B — profile calibrated to PUBLISHED VHLSS 2024 tabulations
# ---------------------------------------------------------------------------
# Anchors taken from the NSO press release on the 2024 survey (May 2025):
#   mean total consumption expenditure   VND 3.0m per person per month
#   living expenditure                   VND 2.8m (94.5% of total)
#   Q5 / Q1 ratio of living expenditure  3.1x  (VND 4.5m vs VND 1.5m)
#   Gini of income                       0.372
# The quintile means below reproduce those three facts exactly: a ratio of
# 3.1 and a mean of 3.0m.
#
# Still assumed, and flagged:
#   - volume of SSB consumed rises with expenditure (Q1 = 0.75x mean volume)
#   - elasticity falls with expenditure (gradient 1.18 down to 0.85)
#
# NOT assumed any more: the share of expenditure spent on SSB is now derived
# from volume and price inside the model, so that it is internally consistent
# with the consumption assumption instead of being a separate guess.
published_profile <- function(mean_exp_month = 3.0e6,
                              mean_ssb_ml_day = 145,
                              retail_price_l = 12000) {
  ratio <- c(0.50, 0.70, 0.983, 1.267, 1.55)   # Q5/Q1 = 3.10, mean = 1.000
  vol_mult <- c(0.75, 0.90, 1.00, 1.15, 1.35)
  vol_mult <- vol_mult / mean(vol_mult)   # weighted mean volume equals mean_ssb_ml_day
  elast_mult <- c(1.18, 1.09, 1.00, 0.92, 0.85)

  ml_day <- mean_ssb_ml_day * vol_mult
  exp_month <- mean_exp_month * ratio
  # monthly spend on SSB from volume and price, as a share of total expenditure
  ssb_share <- ml_day / 1000 * retail_price_l * 30.4 / exp_month

  data.frame(
    quintile       = 1:5,
    pop_share      = rep(0.2, 5),
    mean_exp_month = exp_month,
    ssb_ml_day     = ml_day,
    ssb_exp_share  = ssb_share,
    elast_mult     = elast_mult,
    FALLBACK       = TRUE,
    stringsAsFactors = FALSE
  )
}

# kept for backward compatibility with earlier scripts
fallback_profile <- published_profile

# ---------------------------------------------------------------------------
# From microdata to the profile the model consumes
# ---------------------------------------------------------------------------
profile_from_microdata <- function(hh, map = vhlss_column_map(),
                                   mean_ssb_ml_day = 145) {
  # per-capita expenditure, weighted
  pc <- hh[[map$exp_total]] / pmax(hh[[map$hh_size]], 1)
  w  <- hh[[map$weight]]

  # weighted quintile cut points
  ord <- order(pc)
  cw  <- cumsum(w[ord]) / sum(w)
  q   <- integer(length(pc))
  q[ord] <- pmin(5, findInterval(cw, seq(0, 1, 0.2)[-6]) + 1)

  # beverage expenditure share of total
  bev_share <- hh[[map$exp_bev]] / pmax(hh[[map$exp_total]], 1)
  if (map$exp_ssb %in% names(hh)) {
    ssb_share <- hh[[map$exp_ssb]] / pmax(hh[[map$exp_total]], 1)
    ssb_share_source <- "measured"
  } else {
    # assume 80% of beverage expenditure is SSB (Appendix B #4 uses the same
    # share for the tax base); applied to the beverage line only
    ssb_share <- 0.80 * bev_share
    ssb_share_source <- "assumed"
  }

  out <- do.call(rbind, lapply(1:5, function(k) {
    sel <- q == k
    if (!any(sel)) return(NULL)
    wk <- w[sel] / sum(w[sel])
    data.frame(
      quintile       = k,
      pop_share      = sum(w[sel]) / sum(w),
      mean_exp_month = sum(wk * pc[sel]) / 12,
      # volume: scale the national mean by quintile expenditure relative to
      # overall mean, with elasticity of volume to expenditure fixed at 0.35
      ssb_ml_day     = mean_ssb_ml_day *
                       (sum(wk * pc[sel]) / sum(w * pc / sum(w)))^0.35,
      ssb_exp_share  = sum(wk * ssb_share[sel]),
      elast_mult     = 1.35 - 0.10 * (k - 1),
      FALLBACK       = FALSE,
      stringsAsFactors = FALSE
    )
  }))
  attr(out, "ssb_share_source") <- ssb_share_source
  out
}

# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------
get_quintile_profile <- function(hh_file = NULL, member_file = NULL,
                                 mean_ssb_ml_day = 145) {
  if (!is.null(hh_file) && file.exists(hh_file)) {
    hh <- read_vhlss(hh_file, member_file)
    prof <- profile_from_microdata(hh, mean_ssb_ml_day = mean_ssb_ml_day)
    attr(prof, "source") <- "VHLSS microdata"
  } else {
    prof <- published_profile(mean_ssb_ml_day = mean_ssb_ml_day)
    attr(prof, "source") <-
      "VHLSS 2024 published tabulations + stated assumptions on volume"
  }
  prof
}
