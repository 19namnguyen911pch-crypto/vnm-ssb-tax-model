# -*- coding: utf-8 -*-
import re

C_NEW = """## Appendix C. Deviations from the plan as originally drafted

The protocol and analysis plan were deposited with the code after the model had been run. This appendix records every departure from the plan as first written, so that a reader can see what changed and why. Five departures were made.

| # | Departure | Reason |
|---|---|---|
| C1 | The revenue-neutral levy per gram of sugar (scenario S1b) was dropped | Distributing taxed volume across sugar bands requires a product-level database that does not exist for Viet Nam; without it the scenario reduces to the same average price change as the enacted tax and cannot be distinguished from it |
| C2 | No socioeconomic gradient in baseline disease rates was assumed | Quintile-specific incidence and mortality are not available for Viet Nam; national rates are applied to every quintile |
| C3 | The product audit was not undertaken | The share of taxed beverages above the threshold is assumed (Appendix B, #4) rather than measured |
| C4 | Health-care costs for ischaemic heart disease and stroke are amortised from acute-episode studies | No Vietnamese estimate of annual cost per prevalent case exists for these two conditions |
| C5 | Latency is a two-year shift of the impact fraction, not a distributed lag | No Vietnamese evidence on the shape of the lag; a step lag is the conservative choice |

Two further points affect the reading of the equity results. The elasticity gradient across quintiles (Appendix B, #7c) is an assumption, not a measurement, and the concentration and Kakwani indices use a Gini computed from quintile means, which is a lower bound on true inequality.

"""

E_NEW = """## Appendix E. What was and was not validated

**E.1 Checks performed.** Every step of the model has a unit test with hand-calculated inputs and outputs. Population conservation is checked in the life table: no individual leaves the cohort except through death, and the living plus the dead equal the starting population in every cycle. Boundary conditions are checked: a zero tax returns the baseline exactly, a zero elasticity returns the baseline exactly, and a tax large enough to remove all consumption produces neither negative quantities nor a division error.

**E.2 Checks not performed.** Three planned checks were not carried out and the manuscript does not claim them. The model's baseline prevalence was not compared against GBD or STEPS estimates, because the life table does not age the cohort and a comparison of levels would not be informative. No external comparison was made with the earlier Vietnamese modelling study,[10] because that study reports different outcomes on a different structure. The code was not reviewed by an independent programmer. The unit tests and boundary conditions in E.1 are the whole of the technical assurance behind the results.

"""

F_NEW = """## Appendix F. Sensitivity analyses performed

**F.1 Probabilistic analysis.** 5,000 Monte Carlo iterations, independent sampling from the distributions in Appendix B, fixed seed (20261101), reporting medians and 95% uncertainty intervals.

**F.2 Threshold analysis.** A grid over the ex-factory share (0.30 to 0.85) and the pass-through rate (0.30 to 1.50), with the model re-run at each point, identifies the combinations at which the health gain becomes indistinguishable from zero. The grid is deposited as `output/threshold_grid.csv`.

**F.3 Elasticity grid.** Own-price elasticity from −0.3 to −2.0 in steps of 0.1, other parameters held central, to locate the point at which the health gain changes sign.

**F.4 Tax-base variants.** The share of taxed beverages set at 0.60 and 0.95, bracketing the assumed 0.80.

**F.5 Reformulation.** S3 is run at 25% reformulation centrally; the 10% and 50% levels are reported in the text.

**F.6 Analyses not run.** A static weight model, low and high elasticity sets, a full pass-through grid crossed with broad and narrow legal interpretations of the tax base, and a distributed latency were planned and not carried out. None is reported.

"""

p = "Manuscript_draft_v1.md"
s = open(p, encoding="utf-8").read()

# Table 2 source for the taxed share
s = s.replace("| Share of beverages above 5 g/100 mL | Product audit, Nov–Dec 2026 (Appendix C) | Beta | 0·80 |",
              "| Share of taxed beverages above 5 g/100 mL | Assumed; category composition from [10] | Beta | 0.80 |")
s = s.replace("| 4 | Share of products above 5 g/100 mL | 0·80 | 0·60 to 0·95 | Beta(8,2) | Product audit (Appendix C) | Primary | Yes |",
              "| 4 | Share of taxed beverages above 5 g/100 mL | 0.80 | 0.60 to 0.95 | Beta(8,2) | Assumed; not measured | Assumption | No |")

# delete the product-audit appendix
i = s.index("## Appendix C. Product audit protocol")
j = s.index("## Appendix D. Deviation log")
s = s[:i] + s[j:]

# single-pass renumbering of headings and cross-references
mapping = {"D": "C", "E": "D", "F": "E", "G": "F", "H": "G"}
s = re.sub(r"Appendix ([D-H])\b", lambda m: "Appendix " + mapping[m.group(1)], s)

# retitle three appendices
s = s.replace("## Appendix C. Deviation log", "## Appendix C. Deviations from the plan as originally drafted")
s = s.replace("## Appendix E. Validation plan", "## Appendix E. What was and was not validated")
s = s.replace("## Appendix F. Sensitivity analysis plan", "## Appendix F. Sensitivity analyses performed")

def swap(s, start, end, new):
    i = s.index(start); j = s.index(end, i)
    return s[:i] + new + s[j:]

s = swap(s, "## Appendix C. Deviations", "## Appendix D. CHEERS", C_NEW)
s = swap(s, "## Appendix E. What was and was not validated", "## Appendix F. Sensitivity analyses", E_NEW)
s = swap(s, "## Appendix F. Sensitivity analyses performed", "## Appendix G. Code and reproducibility", F_NEW)

# supplementary list
s = re.sub(r"- \*\*Appendix C\.\*\* Product audit[^\n]*\n", "", s)
open(p, "w", encoding="utf-8").write(s)

print([l for l in s.split("\n") if l.startswith("## Appendix")])
