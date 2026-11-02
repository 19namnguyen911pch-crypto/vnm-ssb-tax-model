# -*- coding: utf-8 -*-
"""Update every number that changed when the BMI-diabetes relative risk was
corrected from 1.55 to 1.37 (the APCSC estimate)."""
import re

PAIRS = [
    # headline results
    ("24,767", "19,387"),
    ("10,046–52,842", "7,136–42,913"),
    ("32,625", "24,574"),
    ("29,077", "20,894"),
    ("2,682", "2,778"),
    ("725", "631"),
    ("89,991", "70,670"),
    ("105,442", "76,041"),
    ("3,179", "3,307"),
    ("9,837", "10,181"),
    ("38,514", "30,169"),
    ("45,197", "32,503"),
    ("1,350", "1,405"),
    ("4,179", "4,328"),
    ("1,500", "1,087"),
    ("5,438", "3,956"),
    ("2,331", "1,691"),
    # sensitivity
    ("53,509", "41,027"),
    ("7,822", "6,280"),
    ("39,894", "31,345"),
    ("18,724", "14,639"),
    ("13,784", "10,784"),
    ("35,710", "27,968"),
    ("16,534", "12,937"),
    ("37,075", "29,039"),
    ("22,632", "17,682"),
    ("8.6%", "8.8%"),
    # variance decomposition
    ("94%", "93%"),
    ("accounted for 50%", "accounted for 45%"),
    ("pass-through 18% and the BMI–diabetes relative risk 12%",
     "the BMI–diabetes relative risk 17% and pass-through 16%"),
    ("89% of averted cases", "85% of averted cases"),
    ("0.44 to 1.28", "0.43 to 1.28"),
]

p = "Manuscript_draft_v1.md"
s = open(p, encoding="utf-8").read()
for old, new in PAIRS:
    if old in s:
        s = s.replace(old, new)
    else:
        print("not present:", old)

# table 3 and the per-1,000 / per-billion rows need context-specific edits
s = s.replace(
"| DALYs averted per 1,000 population | 0.31 | 1.11 | 0.47 |",
"| DALYs averted per 1,000 population | 0.24 | 0.87 | 0.37 |")
s = s.replace(
"| DALYs averted per VND bn of revenue | 0.5 | 0.6 | 1.1 |",
"| DALYs averted per VND bn of revenue | 0.4 | 0.5 | 0.8 |")
s = s.replace(
"DALYs averted per 1,000 were 0.27 in Q1 and 0.35 in Q5, a ratio of 0.77",
"DALYs averted per 1,000 were 0.21 in Q1 and 0.27 in Q5, a ratio of 0.77")
s = s.replace(
"DALYs averted per 1,000 population were 0.27 in Q1 and 0.35 in Q5, a ratio of 0.77",
"DALYs averted per 1,000 population were 0.21 in Q1 and 0.27 in Q5, a ratio of 0.77")
s = s.replace("the enacted tax would deliver 0.5 DALYs and the benchmark 0.6",
              "the enacted tax would deliver 0.4 DALYs and the benchmark 0.5")
s = s.replace("or 0.31 per 1,000 population", "or 0.24 per 1,000 population")
open(p, "w", encoding="utf-8").write(s)
print("Lancet updated")
