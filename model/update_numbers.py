# -*- coding: utf-8 -*-
"""Refresh every number that changed after the revenue and S3 fixes."""
import json, re

R = json.load(open("output/results.json", encoding="utf-8"))

def num(x):
    m = re.search(r"-?\d[\d,\.]*", str(x))
    return float(m.group(0).replace(",", "")) if m else 0.0

dp1 = num(R["TBD-40"]) / 100
d_s1, d_s2, d_s3 = num(R["D_S1"]), num(R["D_S2"]), num(R["D_S3"])
pop = 104 * 0.78 * 1e6
per1000 = lambda d: d / (pop / 1000)
c_s1 = [num(R["TBD-59"]), num(R["TBD-60"]), num(R["TBD-61"])]
c_s2 = [num(x) for x in R["CASES_S2"].split()]
c_s3 = [num(x) for x in R["CASES_S3"].split()]
gbn = lambda k: num(R[k]) / 1e9
cons = lambda dp: -1.20 * dp * 145

rows_en = [
 f"| Retail price change, taxed beverages (%) | {dp1*100:.1f} | 20.0 | {dp1*100:.1f} |",
 f"| Consumption change (mL/person/day) | {cons(dp1):.1f} | {cons(0.20):.1f} | {cons(dp1):.1f} |",
 f"| DALYs averted (median, 95% UI) | {d_s1:,.0f} ({R['TBD-5']}) | {d_s2:,.0f} | {d_s3:,.0f} |",
 f"| DALYs averted per 1,000 population | {per1000(d_s1):.2f} | {per1000(d_s2):.2f} | {per1000(d_s3):.2f} |",
 f"| Type 2 diabetes cases averted | {c_s1[0]:,.0f} | {c_s2[0]:,.0f} | {c_s3[0]:,.0f} |",
 f"| Ischaemic heart disease cases averted | {c_s1[1]:,.0f} | {c_s2[1]:,.0f} | {c_s3[1]:,.0f} |",
 f"| Stroke cases averted | {c_s1[2]:,.0f} | {c_s2[2]:,.0f} | {c_s3[2]:,.0f} |",
 f"| Health-care costs saved (VND bn, 2026) | {gbn('COST_S1'):,.0f} | {gbn('COST_S2'):,.0f} | {gbn('COST_S3'):,.0f} |",
 f"| Revenue, 2027–2050, discounted (VND bn) | {gbn('REV_S1'):,.0f} | {gbn('REV_S2'):,.0f} | {gbn('REV_S3'):,.0f} |",
 f"| DALYs averted per VND bn of revenue | {d_s1/gbn('REV_S1'):.1f} | {d_s2/gbn('REV_S2'):.1f} | {d_s3/gbn('REV_S3'):.1f} |",
]

def fmt_vi(s):
    out = re.sub(r"(\d),(\d{3})", lambda m: m.group(1) + "X" + m.group(2), s)
    out = re.sub(r"(\d)\.(\d)", r"\1,\2", out)
    return out.replace("X", ".")

p = "Manuscript_draft_v1.md"
s = open(p, encoding="utf-8").read()
i = s.index("| Outcome | S1 | S2 | S3")
j = s.index("\n\n", s.index("| DALYs averted per VND bn of revenue |"))
block = "\n".join(rows_en)
s = s[:i] + block + s[j:]

# comparison paragraph
i = s.index("The 20% price increase would avert")
j = s.index("\n", i)
s = s[:i] + (
 f"The 20% price increase would avert {d_s2:,.0f} DALYs, {d_s2/d_s1:.1f} times the gain from the enacted tax, "
 f"at a discounted revenue of VND {gbn('REV_S2'):,.0f} billion against VND {gbn('REV_S1'):,.0f} billion. "
 f"Per billion dong of revenue the enacted tax delivered {d_s1/gbn('REV_S1'):.1f} DALYs and the benchmark "
 f"{d_s2/gbn('REV_S2'):.1f}, a ratio of {(d_s2/gbn('REV_S2'))/(d_s1/gbn('REV_S1')):.2f}. "
 f"Reformulation at 10%, 25% and 50% removed a corresponding share of the tax base and lowered revenue by the same proportion; "
 f"at 25% it raised the health gain to {d_s3:,.0f} DALYs, because the reformulated products carry less sugar even though they leave the base.") + s[j:]
open(p, "w", encoding="utf-8").write(s)
print("EN numbers refreshed")
print("revenue S1:", f"{gbn('REV_S1'):,.0f}", "| DALYs/bn S1:", f"{d_s1/gbn('REV_S1'):.1f}")
