###############################################################################
# audit.R — turn the product audit into model parameters
#
# Input: the CSV produced by the data collection form in Kiem_toan_rut_gon.md.
# Output: data/audit_params.csv and a named vector that patches params_default().
#
# The four parameters this closes (Appendix B #4, and the three that were
# standing in for the product audit):
#   taxed_share  share of taxed beverage volume above 5 g/100 mL
#   share_high   share of TAXED volume in the >= 8 g/100 mL segment
#   sugar_high   mean sugar (g/100 mL) in that segment
#   sugar_low    mean sugar (g/100 mL) in the 5-8 g/100 mL segment
#
# Volume weighting: shelf presence is not sales. If category volume shares are
# supplied in `weights`, they are used; otherwise the SKU share is reported as
# an upper bound and the model uses a conservative adjustment.
###############################################################################

THRESHOLD <- 5
HIGH_CUT  <- 8

# ---------------------------------------------------------------------------
# Read and validate
# ---------------------------------------------------------------------------
read_audit <- function(path) {
  d <- utils::read.csv(path, stringsAsFactors = FALSE)
  need <- c("sku_id", "category", "pack_ml", "sugar_g_per_100ml", "price_vnd")
  miss <- setdiff(need, names(d))
  if (length(miss)) {
    stop("Audit file is missing: ", paste(miss, collapse = ", "))
  }
  d$sugar_g_per_100ml <- suppressWarnings(as.numeric(d$sugar_g_per_100ml))
  d$pack_ml <- suppressWarnings(as.numeric(d$pack_ml))
  d$price_vnd <- suppressWarnings(as.numeric(d$price_vnd))
  n0 <- nrow(d)
  d <- d[!is.na(d$sugar_g_per_100ml) & !is.na(d$pack_ml) & d$pack_ml > 0, ]
  attr(d, "dropped") <- n0 - nrow(d)
  d
}

# ---------------------------------------------------------------------------
# Core estimates
# ---------------------------------------------------------------------------
audit_estimates <- function(d, weights = NULL, volume_adjust = 0.85) {
  n <- nrow(d)
  # Clopper-Pearson interval on the SKU share
  k <- sum(d$sugar_g_per_100ml > THRESHOLD)
  ci <- stats::binom.test(k, n)$conf.int

  near <- d[d$sugar_g_per_100ml > THRESHOLD & d$sugar_g_per_100ml <= HIGH_CUT, ]
  high <- d[d$sugar_g_per_100ml > HIGH_CUT, ]

  # price per litre, by category
  d$price_per_l <- d$price_vnd / (d$pack_ml / 1000)
  price_by_cat <- stats::aggregate(price_per_l ~ category, data = d, FUN = mean)

  # volume share of the high-sugar segment within TAXED volume. SKU share is an
  # upper bound; `volume_adjust` shrinks it toward the conservative side
  # because high-sugar SKUs tend to occupy more shelf space than their sales.
  sku_share_high <- if ((k) > 0) nrow(high) / k else 0
  share_high <- min(1, sku_share_high * volume_adjust)

  w_cat <- if (is.null(weights)) NULL else weights
  list(
    n = n,
    dropped = attr(d, "dropped"),
    n_above = k,
    p_sku = k / n,
    p_ci = as.numeric(ci),
    p_weighted = if (is.null(w_cat)) NA_real_ else NA_real_,
    n_near_threshold = nrow(near),
    n_high = nrow(high),
    share_high = share_high,
    sugar_high = if (nrow(high)) mean(high$sugar_g_per_100ml) else NA_real_,
    sugar_low  = if (nrow(near)) mean(near$sugar_g_per_100ml) else NA_real_,
    price_by_cat = price_by_cat
  )
}

# ---------------------------------------------------------------------------
# Patch the model parameters
# ---------------------------------------------------------------------------
apply_audit <- function(p, est, taxed_share_override = NULL) {
  if (!is.null(taxed_share_override)) {
    p$taxed_share <- taxed_share_override
  } else {
    p$taxed_share <- est$p_sku
  }
  if (!is.na(est$share_high)) p$share_high <- est$share_high
  if (!is.na(est$sugar_high)) p$sugar_high <- est$sugar_high
  if (!is.na(est$sugar_low))  p$sugar_low  <- est$sugar_low
  p
}

# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------
write_audit_params <- function(est, dir = "data") {
  dir.create(dir, showWarnings = FALSE, recursive = TRUE)
  out <- data.frame(
    parameter = c("taxed_share", "share_high", "sugar_high", "sugar_low",
                  "n_products", "n_above_threshold", "n_near_threshold"),
    value = c(round(est$p_sku, 4), round(est$share_high, 4),
              round(est$sugar_high, 3), round(est$sugar_low, 3),
              est$n, est$n_above, est$n_near_threshold),
    note = c(
      sprintf("SKU share above %s g/100 mL; 95%% CI %.3f-%.3f (upper bound on volume share)",
              THRESHOLD, est$p_ci[1], est$p_ci[2]),
      "volume share of the >= 8 g segment among taxed volume, shrunk by 0.85",
      "mean sugar in the >= 8 g segment",
      "mean sugar in the 5-8 g segment (the reformulation pool)",
      "products with a usable label", "above threshold", "5-8 g pool for S3"
    )
  )
  utils::write.csv(out, file.path(dir, "audit_params.csv"), row.names = FALSE)
  utils::write.csv(est$price_by_cat, file.path(dir, "audit_price_by_category.csv"),
                   row.names = FALSE)
  invisible(out)
}

# ---------------------------------------------------------------------------
# Demo with synthetic data (clearly marked)
# ---------------------------------------------------------------------------
demo_audit <- function(n = 120, seed = 20261101) {
  set.seed(seed)
  cats <- c("soda_co_ga", "soda_khong_ga", "tang_luc", "tra", "chua_nuoc_qua")
  s <- c(stats::rnorm(n * 0.55, 10.5, 1.2),      # carbonates: high sugar
         stats::rnorm(n * 0.25, 6.6, 0.9),       # teas and near-threshold
         stats::rnorm(n * 0.20, 4.2, 0.8))       # low / juice-based
  s <- pmax(0, round(s, 1))
  data.frame(
    sku_id = sprintf("DEMO-%03d", seq_along(s)),
    category = sample(cats, length(s), replace = TRUE),
    pack_ml = sample(c(330, 500, 1500), length(s), replace = TRUE),
    sugar_g_per_100ml = s,
    price_vnd = round(stats::runif(length(s), 8000, 28000))
  )
}
