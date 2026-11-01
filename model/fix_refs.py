# -*- coding: utf-8 -*-
"""Merge the duplicated STEPS references and renumber, fix the Table 2 label."""
import re

def merge_refs(path, total=38):
    s = open(path, encoding="utf-8").read()

    # 1. drop reference 2 (duplicate of 1)
    lines = s.split("\n")
    out = []
    for ln in lines:
        if re.match(r"^2\.\s", ln) and "STEPS" in ln:
            continue
        out.append(ln)
    s = "\n".join(out)

    # 2. renumber list entries 3..38 -> 2..37
    def renum_line(m):
        n = int(m.group(1))
        return f"{n-1}. " if 3 <= n <= total else m.group(0)
    s = re.sub(r"^(\d+)\.\s", lambda m: renum_line(m) if m.start() else m.group(0),
               s, flags=re.M)
    s = re.sub(r"(?m)^(\d+)\.\s", renum_line, s)

    # 3. renumber in-text citations: [2]->[1], [n]->[n-1] for n>=3
    def fix_group(m):
        nums = [int(x) for x in m.group(1).split(",")]
        new = sorted({1 if x == 2 else (x - 1 if x >= 3 else x) for x in nums})
        return "[" + ",".join(str(x) for x in new) + "]"
    s = re.sub(r"\[(\d+(?:,\d+)*)\]", fix_group, s)

    open(path, "w", encoding="utf-8").write(s)

    # report
    maxcit = max(int(x) for g in re.findall(r"\[(\d+(?:,\d+)*)\]", s)
                 for x in g.split(","))
    nrefs = len(re.findall(r"(?m)^\d+\.\s", s))
    print(path, "| max citation:", maxcit, "| numbered lines:", nrefs)


merge_refs("Manuscript_draft_v1.md")
merge_refs("Ban_thao_Tieng_Viet.md")

# Table 2 label: sexes are combined, so do not claim sex stratification
for p in ["Manuscript_draft_v1.md", "Ban_thao_Tieng_Viet.md"]:
    s = open(p, encoding="utf-8").read()
    s = s.replace("| Population by age, sex, quintile, 2027–2050 |",
                  "| Population by age and quintile, 2027–2050 |")
    s = s.replace("| Dân số theo tuổi, giới, ngũ phân vị, 2027–2050 |",
                  "| Dân số theo tuổi và ngũ phân vị, 2027–2050 |")
    s = s.replace("38 references", "37 references")
    s = s.replace("38 tài liệu tham khảo", "37 tài liệu tham khảo")
    open(p, "w", encoding="utf-8").write(s)
print("labels fixed")
