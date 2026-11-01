# -*- coding: utf-8 -*-
"""Merge duplicate STEPS refs, renumber, and make sure every reference is cited."""
import re

def content_of(s, n):
    i = s.index("## References"); j = s.index("## Supplementary material")
    for l in s[i:j].split("\n"):
        m = re.match(r"^(\d+)\.\s", l)
        if m and int(m.group(1)) == n:
            return l
    return ""

def fix(path):
    s = open(path, encoding="utf-8").read()
    i = s.index("## References"); j = s.index("## Supplementary material")
    refs = [(int(re.match(r"^(\d+)\.", l).group(1)), re.sub(r"^\d+\.\s", "", l))
            for l in s[i:j].split("\n") if re.match(r"^\d+\.\s", l)]

    # drop the duplicate STEPS entry (old #2), keep #1
    drop = {n for n, l in refs if n == 2 and "STEPS" in l}
    mapping, kept, newno = {}, [], 0
    for n, l in refs:
        if n in drop:
            mapping[n] = 1
            continue
        newno += 1
        mapping[n] = newno
        kept.append((newno, l))

    body, tail = s[:i], s[j:]
    def fix_group(m):
        nums = {int(x) for x in m.group(1).split(",")}
        new = sorted({mapping[x] for x in nums if x in mapping})
        return "[" + ",".join(str(x) for x in new) + "]"
    body = re.sub(r"\[(\d+(?:,\d+)*)\]", fix_group, body)

    newblock = "## References\n\n" + "\n".join(f"{n}. {l}" for n, l in kept) + "\n\n"
    s = body + newblock + tail
    s = s.replace("38 references", "37 references").replace("38 tài liệu tham khảo", "37 tài liệu tham khảo")
    s = s.replace("| Population by age, sex, quintile, 2027–2050 |", "| Population by age and quintile, 2027–2050 |")
    s = s.replace("| Dân số theo tuổi, giới, ngũ phân vị, 2027–2050 |", "| Dân số theo tuổi và ngũ phân vị, 2027–2050 |")
    open(path, "w", encoding="utf-8").write(s)

    t = open(path, encoding="utf-8").read()
    k = t.index("## References"); k2 = t.index("## Supplementary material")
    nums = [int(re.match(r"^(\d+)\.", l).group(1)) for l in t[k:k2].split("\n") if re.match(r"^\d+\.\s", l)]
    b = t[:k]
    cited = {int(x) for g in re.findall(r"\[(\d+(?:,\d+)*)\]", b) for x in g.split(",")}
    print(path, "| refs:", len(nums), "| sequential:", nums == list(range(1, len(nums) + 1)),
          "| uncited:", [n for n in nums if n not in cited])

fix("Manuscript_draft_v1.md")
fix("Ban_thao_Tieng_Viet.md")
