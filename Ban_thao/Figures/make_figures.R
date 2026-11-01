# -*- coding: utf-8 -*-
# make_figures.R — generate Figures 1-4 from the model output
# Run from the repository root:  Rscript Ban_thao/Figures/make_figures.R

suppressPackageStartupMessages({
  source("model/vhlss.R")
  source("model/pmslt_model.R")
})

OUT <- "Ban_thao/Figures"
dir.create(OUT, showWarnings = FALSE, recursive = TRUE)

p0 <- params_default()
qprof <- get_quintile_profile()
mort <- 0.004 * exp(0.075 * (p0$ages - 20))

png_ <- function(name, w = 7, h = 4.2) {
  png(file.path(OUT, name), width = w, height = h, units = "in", res = 300)
}

# ---------------------------------------------------------------------------
# Figure 1 — model structure
# ---------------------------------------------------------------------------
png_("fig1_model_structure.png", 6.4, 6.8)
par(mar = c(0.4, 0.4, 0.4, 0.4))
plot.new(); plot.window(xlim = c(0, 100), ylim = c(0, 100))

box_at <- function(y, label, h = 9, w = 74, cex = 0.76, fill = "#eef3f7") {
  x <- 50
  rect(x - w/2, y - h/2, x + w/2, y + h/2, col = fill, border = "grey35", lwd = 1.2)
  text(x, y, label, cex = cex, col = "grey10")
}
down <- function(y0, y1) arrows(50, y0, 50, y1, length = 0.09, lwd = 1.2, col = "grey45")

box_at(88, "Statutory rate (8%, then 10%) applied to the\nex-factory price, above 5 g sugar/100 mL", h = 11)
box_at(71, "Retail price change\n(ex-factory share, pass-through, 10% VAT cascade)", h = 11)
box_at(54, "Consumption change, energy intake and BMI\n(own-price elasticity, sugar density, dynamic weight model)", h = 11)
box_at(37, "Disease incidence\n(population impact fractions, 2-year latency)", h = 11)
box_at(20, "Multi-state life table\n(healthy, type 2 diabetes, ischaemic heart disease, stroke, dead)", h = 11)
box_at(5,  "DALYs  ·  health-care costs  ·  revenue", h = 8, fill = "#f7f1ea", cex = 0.85)

down(82.5, 76.5); down(65.5, 59.5); down(48.5, 42.5); down(31.5, 25.5); down(14.5, 9)

text(50, 97, "Figure 1. Structure of the model", cex = 1.0, font = 2)
text(9, 88, "by age\nand sex", cex = 0.68, col = "grey45", adj = 1)
text(9, 54, "by expenditure\nquintile", cex = 0.68, col = "grey45", adj = 1)
dev.off()

# ---------------------------------------------------------------------------
# Scenarios at central values
# ---------------------------------------------------------------------------
codes <- c("S1", "S2", "S3")
res <- lapply(c("S0", codes), run_scenario, qprof = qprof, p = p0, mort_by_age = mort)
names(res) <- c("S0", codes)
base <- res[["S0"]]
per1000 <- sapply(codes, function(k)
  (base$dalys - res[[k]]$dalys) / (res[[k]]$pop / 1000))

# ---------------------------------------------------------------------------
# Figure 2 — DALYs averted per 1,000 by quintile
# ---------------------------------------------------------------------------
png_("fig2_dalys_by_quintile.png", 7, 4)
par(mar = c(4.2, 4.4, 2.2, 1))
cols <- c("#2c5f7c", "#c8792a", "#7a8b5a")
bp <- barplot(t(per1000), beside = TRUE, col = cols, border = NA,
              ylab = "DALYs averted per 1,000 population",
              names.arg = paste0("Q", 1:5), xlab = "Household expenditure quintile",
              ylim = c(0, max(per1000) * 1.25), cex.names = 0.9)
legend("topleft", legend = c("Enacted tax (S1)", "20% price rise (S2)",
                             "Enacted + reformulation (S3)"),
       fill = cols, border = NA, bty = "n", cex = 0.78)
title(main = "Figure 2. Distribution of health gain across expenditure quintiles",
      cex.main = 0.95, font.main = 2)
dev.off()

# ---------------------------------------------------------------------------
# Figures 3 and 4 — from the PSA
# ---------------------------------------------------------------------------
psa <- read.csv("output/psa_results.csv")
d1 <- psa[psa$scenario == "S1", ]
d2 <- psa[psa$scenario == "S2", ]

# The same 5,000 draws under two assumptions about the gradient in baseline
# disease risk, side by side, so that the reader can see how much of the
# apparent equity result is carried by the assumption.
g1 <- read.csv("output/psa_gradient.csv")
g1 <- g1[g1$scenario == "S1", ]
g2 <- read.csv("output/psa_gradient.csv")
g2 <- g2[g2$scenario == "S2", ]

png_("fig3_impact_equity.png", 7.4, 4.0)
par(mfrow = c(1, 2), mar = c(4.4, 4.4, 2.6, 1), oma = c(0, 0, 1.2, 0))

panel <- function(x1, y1, x2, y2, ylim_all, title, show_y) {
  plot(NA, xlim = range(c(x1, x2), na.rm = TRUE), ylim = ylim_all,
       log = "x", xaxt = "n",
       xlab = "Total DALYs averted (log scale)",
       ylab = if (show_y) "Concentration index of DALYs averted" else "",
       main = title, cex.main = 0.82, font.main = 1)
  at <- axTicks(1, log = TRUE)
  axis(1, at = at, labels = format(at, big.mark = ",", scientific = FALSE))
  points(x2, y2, pch = 16, cex = 0.42, col = adjustcolor("#c8792a", 0.25))
  points(x1, y1, pch = 16, cex = 0.42, col = adjustcolor("#2c5f7c", 0.30))
  abline(h = 0, lty = 2, col = "grey40")
}

ylim_all <- range(c(d1$ci_dalys, d2$ci_dalys, g1$ci_dalys, g2$ci_dalys),
                  na.rm = TRUE)
ylim_all <- ylim_all + c(-0.02, 0.02) * diff(ylim_all)

panel(d1$dalys_averted, d1$ci_dalys, d2$dalys_averted, d2$ci_dalys, ylim_all,
      "A  No gradient in disease risk", TRUE)
legend("left", inset = 0.02, legend = c("Enacted tax (S1)", "20% price rise (S2)"),
       pch = 16, col = c("#2c5f7c", "#c8792a"), bty = "n", cex = 0.75,
       title = "above zero = gain concentrated\namong the better-off", title.adj = 0)
panel(g1$dalys_averted, g1$ci_dalys, g2$dalys_averted, g2$ci_dalys, ylim_all,
      "B  Gradient 1.15 (Q1) to 0.88 (Q5)", FALSE)
mtext("Figure 3. Impact-equity plane under two assumptions about the socioeconomic gradient",
      outer = TRUE, cex = 0.95, font = 2)
dev.off()

png_("fig4_uncertainty.png", 7, 6.6)
par(mfrow = c(2, 1), mar = c(4.2, 4.6, 1.8, 1))
br <- seq(0, max(c(d1$dalys_averted, d2$dalys_averted), na.rm = TRUE), length.out = 40)
hist(d1$dalys_averted, breaks = br, col = adjustcolor("#2c5f7c", 0.55), border = NA,
     xlab = "DALYs averted", main = "A  Distribution of DALY gains",
     cex.main = 0.9, font.main = 1)
hist(d2$dalys_averted, breaks = br, col = adjustcolor("#c8792a", 0.45),
     border = NA, add = TRUE)
legend("topright", legend = c("S1 enacted", "S2 20% benchmark"),
       fill = c("#2c5f7c", "#c8792a"), border = NA, bty = "n", cex = 0.8)

plot(NA, xlim = range(c(d1$revenue, d2$revenue) / 1e9, na.rm = TRUE),
     ylim = range(c(d1$dalys_averted, d2$dalys_averted), na.rm = TRUE),
     log = "x", xaxt = "n",
     xlab = "Revenue (billion VND, log scale)", ylab = "DALYs averted",
     main = "B  Health gain against revenue", cex.main = 0.9, font.main = 1)
at <- axTicks(1, log = TRUE)
axis(1, at = at, labels = format(at, big.mark = ",", scientific = FALSE))
points(d2$revenue / 1e9, d2$dalys_averted, pch = 16, cex = 0.35,
       col = adjustcolor("#c8792a", 0.25))
points(d1$revenue / 1e9, d1$dalys_averted, pch = 16, cex = 0.35,
       col = adjustcolor("#2c5f7c", 0.30))
dev.off()

# Journal-standard filenames alongside the descriptive ones, so that the figure
# that ends up in the submission is traceable to the script that made it.
for (i in 1:4) {
  src <- file.path(OUT, sprintf("fig%d_%s.png", i,
                  c("model_structure", "dalys_by_quintile",
                    "impact_equity", "uncertainty")[i]))
  file.copy(src, file.path(OUT, sprintf("Figure%d.png", i)), overwrite = TRUE)
}

cat("written to", OUT, ":\n")
print(basename(list.files(OUT, pattern = "\\.png$")))
