# -*- coding: utf-8 -*-
"""Update the WHO manuscript to the corrected model run (RR 1.37)."""
p = "Banthao_Who/Manuscript_WHO.md"
s = open(p, encoding="utf-8").read()

PAIRS = [
    ("24 767", "19 387"),
    ("10 046–52 842", "7 136–42 913"),
    ("32 625", "24 574"),
    ("29 077", "20 894"),
    ("2 682", "2 778"),
    ("725", "631"),
    ("89 991", "70 670"),
    ("105 442", "76 041"),
    ("3 179", "3 307"),
    ("9 837", "10 181"),
    ("38 514", "30 169"),
    ("45 197", "32 503"),
    ("1 350", "1 405"),
    ("4 179", "4 328"),
    ("1 500", "1 087"),
    ("5 438", "3 956"),
    ("2 331", "1 691"),
    ("53 509", "41 027"),
    ("7 822", "6 280"),
    ("39 894", "31 345"),
    ("18 724", "14 639"),
    ("13 784", "10 784"),
    ("35 710", "27 968"),
    ("16 534", "12 937"),
    ("37 075", "29 039"),
    ("22 632", "17 682"),
    ("8.6%", "8.8%"),
    ("94%", "93%"),
    ("89% of averted cases", "85% of averted cases"),
    ("0.44 to 1.28", "0.43 to 1.28"),
]
for old, new in PAIRS:
    if old not in s:
        print("missing:", old)
    s = s.replace(old, new)

s = s.replace(
    "with the own-price elasticity accounting for 50% of the explained variance, pass-through 18% and the diabetes relative risk 12%",
    "with the own-price elasticity accounting for 45% of the explained variance, the diabetes relative risk 17% and pass-through 16%")
s = s.replace(
    "| DALYs averted per 1 000 population | 0.31 | 1.11 | 0.47 |",
    "| DALYs averted per 1 000 population | 0.24 | 0.87 | 0.37 |")
s = s.replace(
    "| DALYs averted per VND bn of revenue | 0.5 | 0.6 | 1.1 |",
    "| DALYs averted per VND bn of revenue | 0.4 | 0.5 | 0.8 |")
s = s.replace(
    "DALYs averted per 1 000 (Fig. 2) were 0.27 in the poorest quintile and 0.35 in the richest",
    "DALYs averted per 1 000 (Fig. 2) were 0.21 in the poorest quintile and 0.27 in the richest")
s = s.replace(
    "The gain is 0.27 DALYs per 1 000 in the poorest quintile and 0.35 in the richest",
    "The gain is 0.21 DALYs per 1 000 in the poorest quintile and 0.27 in the richest")
s = s.replace("or 0.31 per 1 000 population", "or 0.24 per 1 000 population")
open(p, "w", encoding="utf-8").write(s)
print("WHO updated")
