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
# disease risk, both directions. Panel B carries the level shift that a fixed
# gradient imposes, so the two panels share one vertical scale.
g <- read.csv("output/psa_gradient.csv")
g1 <- g[g$scenario == "S1", ]

png_("fig3_impact_equity.png", 7.4, 4.2)
par(mfrow = c(1, 2), mar = c(4.6, 4.6, 2.8, 1.2), oma = c(0, 0, 1.2, 0))

ylim_all <- range(c(d1$ci_dalys, d2$ci_dalys, g1$ci_dalys), na.rm = TRUE)
ylim_all <- ylim_all + c(-0.06, 0.06) * diff(ylim_all)
xlim_all <- range(c(d1$dalys_averted, d2$dalys_averted, g1$dalys_averted), na.rm = TRUE)

frame_panel <- function(title, ylab) {
  plot(NA, xlim = xlim_all, ylim = ylim_all, log = "x", xaxt = "n",
       xlab = "Total DALYs averted (log scale)", ylab = ylab,
       main = title, cex.main = 0.82, font.main = 1, cex.axis = 0.85)
  at <- axTicks(1, log = TRUE)
  axis(1, at = at, labels = format(at, big.mark = ",", scientific = FALSE),
       cex.axis = 0.82)
  abline(h = 0, lty = 2, col = "grey45")
}

frame_panel("A  No gradient in disease risk",
            "Concentration index of DALYs averted")
points(d2$dalys_averted, d2$ci_dalys, pch = 16, cex = 0.40,
       col = adjustcolor("#c8792a", 0.22))
points(d1$dalys_averted, d1$ci_dalys, pch = 16, cex = 0.40,
       col = adjustcolor("#2c5f7c", 0.28))
legend("topleft", legend = c("Enacted tax (S1)", "20% price rise (S2)"),
       pch = 16, col = c("#2c5f7c", "#c8792a"), bty = "n", cex = 0.74)


frame_panel("B  Gradient in disease risk, both directions", "")
points(g1$dalys_averted[g1$grad == "pro_rich"],
       g1$ci_dalys[g1$grad == "pro_rich"], pch = 15, cex = 0.36,
       col = adjustcolor("#7a8b5a", 0.30))
points(g1$dalys_averted[g1$grad == "pro_poor"],
       g1$ci_dalys[g1$grad == "pro_poor"], pch = 17, cex = 0.36,
       col = adjustcolor("#2c5f7c", 0.30))
abline(h = median(d1$ci_dalys, na.rm = TRUE), lty = 3, col = "#c8792a", lwd = 1.2)
legend(x = 3800, y = 0.082, cex = 0.72, bty = "n",
       legend = c("risk rises with expenditure",
                  "risk falls with expenditure"),
       pch = c(15, 17), col = c("#7a8b5a", "#2c5f7c"))


mtext("Figure 3. Impact-equity plane under three assumptions about the socioeconomic gradient",
      outer = TRUE, cex = 0.92, font = 2)
dev.off()

png_("fig4_uncertainty.png", 7.6, 7.2)
par(mfrow = c(2, 1), mar = c(5.0, 6.0, 1.8, 1), mgp = c(4.0, 0.7, 0))
br <- seq(0, max(c(d1$dalys_averted, d2$dalys_averted), na.rm = TRUE), length.out = 40)
hist(d1$dalys_averted, breaks = br, col = adjustcolor("#2c5f7c", 0.55), border = NA,
     xlab = "DALYs averted", main = "A  Distribution of DALY gains",
     cex.main = 0.9, font.main = 1, xaxt = "n", yaxt = "n")
axis(1, at = axTicks(1), labels = format(axTicks(1), big.mark = ",",
     scientific = FALSE), cex.axis = 0.78)
axis(2, at = axTicks(2), labels = format(axTicks(2), big.mark = ",",
     scientific = FALSE), las = 1, cex.axis = 0.78)
hist(d2$dalys_averted, breaks = br, col = adjustcolor("#c8792a", 0.45),
     border = NA, add = TRUE)
legend("topright", legend = c("S1 enacted", "S2 20% benchmark"),
       fill = c("#2c5f7c", "#c8792a"), border = NA, bty = "n", cex = 0.8)

plot(NA, xlim = range(c(d1$revenue, d2$revenue) / 1e9, na.rm = TRUE),
     ylim = range(c(d1$dalys_averted, d2$dalys_averted), na.rm = TRUE),
     log = "x", xaxt = "n", xaxs = "r",
     xlab = "Revenue (billion VND, log scale)", ylab = "DALYs averted",
     main = "B  Health gain against revenue", cex.main = 0.9, font.main = 1,
     yaxt = "n")
axis(2, at = axTicks(2), labels = format(axTicks(2), big.mark = ",",
     scientific = FALSE), las = 1, cex.axis = 0.78)
at <- axTicks(1, log = TRUE)
axis(1, at = at, labels = format(at, big.mark = ",", scientific = FALSE),
     cex.axis = 0.72, las = 1)
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
