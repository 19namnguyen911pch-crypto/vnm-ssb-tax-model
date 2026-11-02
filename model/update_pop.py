# -*- coding: utf-8 -*-
"""Update every absolute quantity after the adult population was corrected from
81.1m to 72.0m (UN WPP 2024). Rates, ratios and indices are unchanged."""
import re


def apply(path, pairs, extra=()):
    s = open(path, encoding="utf-8").read()
    for old, new in list(pairs) + list(extra):
        if old not in s:
            print(f"  {path}: missing {old}")
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)
    print(f"{path} updated")


COMMA = [
    ("19,387", "17,209"), ("7,136–42,913", "6,335–38,093"), ("24,574", "21,814"),
    ("20,894", "18,547"), ("2,778", "2,466"), ("631", "560"),
    ("70,670", "62,733"), ("76,041", "67,501"), ("3,307", "2,936"), ("10,181", "9,037"),
    ("58,696", "52,104"), ("63,179", "56,083"), ("2,743", "2,435"), ("8,446", "7,498"),
    ("1,087", "965"), ("3,956", "3,512"), ("3,287", "2,918"),
    ("47,635", "42,284"), ("142,803", "126,764"), ("35,726", "31,713"),
    ("31,345", "27,824"), ("14,639", "12,995"), ("10,784", "9,573"), ("27,968", "24,827"),
    ("12,937", "11,484"), ("29,039", "25,777"), ("6,280", "5,575"), ("41,027", "36,419"),
    ("17,682", "15,696"), ("35,168", "31,218"), ("97,532", "86,578"),
]
# 902 -> 801 must be word-bounded to avoid touching other numbers
EXTRA = [
    ("902 of ischaemic heart disease", "801 of ischaemic heart disease"),
    ("| 902 | 3,307 | 2,435 |", "| 801 | 2,936 | 2,435 |"),
]
apply("Manuscript_draft_v1.md", COMMA, EXTRA)

SPACE = [(a.replace(",", " "), b.replace(",", " ")) for a, b in COMMA]
EXTRA_W = [
    ("902 of ischaemic heart disease", "801 of ischaemic heart disease"),
    ("| 902 | 3 307 | 2 435 |", "| 801 | 2 936 | 2 435 |"),
    ("19 387 to 17 682", "17 209 to 15 696"),
]
apply("Banthao_Who/Manuscript_WHO.md", SPACE, EXTRA_W)

DOT = [(a.replace(",", "."), b.replace(",", ".")) for a, b in COMMA]
EXTRA_V = [
    ("902 ca bệnh tim thiếu máu cục bộ", "801 ca bệnh tim thiếu máu cục bộ"),
    ("| 902 | 3.307 | 2.435 |", "| 801 | 2.936 | 2.435 |"),
    ("19.387 xuống 17.682", "17.209 xuống 15.696"),
]
apply("Ban_thao_Tieng_Viet.md", DOT, EXTRA_V)
