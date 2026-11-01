# -*- coding: utf-8 -*-
# sensitivity.R — the structural sensitivity analyses reported in the manuscript.
# Deterministic runs at central values; writes output/sensitivity.csv.
suppressPackageStartupMessages({
  source("model/vhlss.R"); source("model/pmslt_model.R")
})

qprof <- get_quintile_profile()
p0 <- params_default()
mort <- 0.004 * exp(0.075 * (p0$ages - 20))

dalys_averted <- function(over = list()) {
  p <- p0
  for (nm in names(over)) p[[nm]] <- over[[nm]]
  s0 <- run_scenario("S0", qprof, p, mort)
  s1 <- run_scenario("S1", qprof, p, mort)
  data.frame(dalys = sum(s0$dalys - s1$dalys),
             revenue_bn = sum(s1$revenue) / 1e9)
}

rows <- list()

add <- function(label, over) {
  r <- dalys_averted(over)
  rows[[length(rows) + 1]] <<- data.frame(analysis = label, value = "",
                                          dalys = round(r$dalys),
                                          revenue_bn = round(r$revenue_bn))
}

add("Base case", list())

# discount rate
for (d in c(0, 0.05))
  add("Discount rate", list(discount = d))
rows[[length(rows)]]$value <- "5%"
rows[[length(rows) - 1]]$value <- "0%"

# pass-through
for (k in c(0.50, 0.90, 1.30)) {
  add("Pass-through rate", list(passthrough = k))
  rows[[length(rows)]]$value <- sprintf("%.2f", k)
}

# own-price elasticity
for (e in c(-0.80, -1.20, -1.80)) {
  add("Own-price elasticity", list(elast_own = e))
  rows[[length(rows)]]$value <- sprintf("%.2f", e)
}

# start from the GBD prevalent stock rather than from zero
add("Initial prevalent stock", list(init_prev = TRUE))
rows[[length(rows)]]$value <- "GBD 2021"

# horizon
for (h in c(2036, 2050, 2100)) {
  add("Horizon", list(horizon = h))
  rows[[length(rows)]]$value <- if (h == 2100) "2100" else as.character(h)
}

out <- do.call(rbind, rows)
out$dalys_per_bn <- round(out$dalys / out$revenue_bn, 2)
write.csv(out, "output/sensitivity.csv", row.names = FALSE)
print(out, row.names = FALSE)
