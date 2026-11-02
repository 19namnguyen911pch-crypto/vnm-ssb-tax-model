# -*- coding: utf-8 -*-
"""Build the Bulletin WHO supplement: the appendices with citations remapped to
the WHO reference list, plus a supplementary list for the works that list does
not contain."""
import re

LIL_TO_WHO = {
    2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 9: 7, 10: 8, 11: 9, 12: 10, 13: 11,
    14: 12, 15: 13, 16: 14, 17: 15, 18: 16, 19: 17, 20: 18, 21: 19, 22: 20,
    23: 21, 24: 22, 25: 23, 26: 24, 27: 25, 28: 26, 29: 27,
}

lil = open("Manuscript_draft_v1.md", encoding="utf-8").read()
a = lil.index("## References"); b = lil.index("## Supplementary material")
lil_main = {int(m.group(1)): m.group(2)
            for m in re.finditer(r"(?m)^(\d+)\.\s(.*)$", lil[a:b])}
c = lil.index("## Supplementary references")
lil_supp = {m.group(1): m.group(2)
            for m in re.finditer(r"(?m)^(S\d+)\.\s(.*)$", lil[c:])}

body = lil[lil.index("## Appendix A"):]
body = body[:body.index("## Supplementary references")].rstrip()

# which LiL main refs appear in the appendix and are not in the WHO list?
cited = []
for m in re.finditer(r"\[([0-9S,]+)\]", body):
    for x in m.group(1).split(","):
        if not x.startswith("S") and int(x) not in LIL_TO_WHO:
            if int(x) not in cited:
                cited.append(int(x))
extra = {n: f"S{len(lil_supp) + i + 1}" for i, n in enumerate(cited)}


def remap(m):
    out = []
    for x in m.group(1).split(","):
        if x.startswith("S"):
            out.append(x)
        else:
            n = int(x)
            out.append(str(LIL_TO_WHO[n]) if n in LIL_TO_WHO else extra[n])
    return "(" + ",".join(out) + ")"


body = re.sub(r"\[([0-9S,]+)\]", remap, body)

supp_order = list(lil_supp) + list(extra.values())
lookup = dict(lil_supp)
for n, tag in extra.items():
    lookup[tag] = lil_main[n]

out = ("# Supplementary material\n\n"
       "Supplementary material for: Modest health gains and regressive financing "
       "from Viet Nam's sugar-sweetened beverage excise tax: a modelling study. "
       "Reference numbers in parentheses refer to the main reference list; "
       "numbers prefixed S refer to the list below.\n\n"
       + body +
       "\n\n## Supplementary references\n\n"
       + "\n".join(f"{k}. {lookup[k]}" for k in supp_order) + "\n")
open("Banthao_Who/Supplement_WHO.md", "w", encoding="utf-8").write(out)
print("appendix citations mapped; supplementary refs:", len(supp_order))
print("extra:", extra)
