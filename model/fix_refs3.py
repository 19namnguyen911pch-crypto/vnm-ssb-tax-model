# -*- coding: utf-8 -*-
"""Restore, add the three uncited references where they belong, merge the
duplicate STEPS reference, renumber across the whole document."""
import re, shutil

EN, VI = "Manuscript_draft_v1.md", "Ban_thao_Tieng_Viet.md"
shutil.copy("/tmp/pre_refs_en.md", EN)
shutil.copy("/tmp/pre_refs_vi.md", VI)

# ---- 1. insert the three missing citations (pre-renumber numbers) ----------
en_ins = [
 ("Substitution toward untaxed beverages is already embedded in the own-price elasticity of a demand system, so it must NOT be added again",
  "Substitution toward untaxed beverages is already embedded in the own-price elasticity of a demand system, so it must NOT be added again"),
 ("where own- and cross-price elasticities determine consumption",
  "where own- and cross-price elasticities determine consumption"),
]

def insert(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        if a in s:
            s = s.replace(a, b, 1)
        else:
            print("  MISS:", path, a[:50])
    open(path, "w", encoding="utf-8").write(s)

# English insertions
s = open(EN, encoding="utf-8").read()
s = s.replace(
 "Cross-price elasticities to untaxed beverages \u2014 bottled water, milk, 100% juice \u2014 were used to report substitution,",
 "Cross-price elasticities to untaxed beverages \u2014 bottled water, milk, 100% juice \u2014 were used to report substitution, which rises after taxes of this kind,[28]")
s = s.replace(
 "and a revenue-recycling mechanism \u2014 earmarking for health promotion, or a targeted transfer \u2014 would change the distributional verdict without changing the health gain.",
 "and a revenue-recycling mechanism \u2014 earmarking for health promotion, or a targeted transfer \u2014 would change the distributional verdict without changing the health gain. The payment side is consistently regressive in evaluations elsewhere, though usually by a small margin.[35]")
s = s.replace(
 "The Thai experience is instructive here:",
 "Mexico's experience with a volume-based levy, which reduced purchases and raised water purchases, points the same way.[29] The Thai experience is instructive here:")
open(EN, "w", encoding="utf-8").write(s)

# Vietnamese insertions
s = open(VI, encoding="utf-8").read()
s = s.replace(
 "\u0111\u01b0\u1ee3c d\u00f9ng \u0111\u1ec3 b\u00e1o c\u00e1o m\u1ee9c thay th\u1ebf,",
 "\u0111\u01b0\u1ee3c d\u00f9ng \u0111\u1ec3 b\u00e1o c\u00e1o m\u1ee9c thay th\u1ebf, v\u1ed1n t\u0103ng l\u00ean sau c\u00e1c lo\u1ea1i thu\u1ebf n\u00e0y,[28]")
s = s.replace(
 "v\u00e0 m\u1ed9t c\u01a1 ch\u1ebf ho\u00e0n tr\u1ea3 doanh thu \u2014 d\u00e0nh ri\u00eang cho truy\u1ec1n th\u00f4ng s\u1ee9c kh\u1ecfe, ho\u1eb7c m\u1ed9t kho\u1ea3n chuy\u1ec3n giao c\u00f3 m\u1ee5c ti\u00eau \u2014 s\u1ebd thay \u0111\u1ed5i k\u1ebft lu\u1eadn ph\u00e2n b\u1ed1 m\u00e0 kh\u00f4ng thay \u0111\u1ed5i l\u1ee3i \u00edch s\u1ee9c kh\u1ecfe.",
 "v\u00e0 m\u1ed9t c\u01a1 ch\u1ebf ho\u00e0n tr\u1ea3 doanh thu \u2014 d\u00e0nh ri\u00eang cho truy\u1ec1n th\u00f4ng s\u1ee9c kh\u1ecfe, ho\u1eb7c m\u1ed9t kho\u1ea3n chuy\u1ec3n giao c\u00f3 m\u1ee5c ti\u00eau \u2014 s\u1ebd thay \u0111\u1ed5i k\u1ebft lu\u1eadn ph\u00e2n b\u1ed1 m\u00e0 kh\u00f4ng thay \u0111\u1ed5i l\u1ee3i \u00edch s\u1ee9c kh\u1ecfe. G\u00e1nh n\u1eb7ng chi tr\u1ea3 nh\u00ecn chung l\u00e0 l\u0169y tho\u00e1i trong c\u00e1c \u0111\u00e1nh gi\u00e1 \u1edf n\u01a1i kh\u00e1c, d\u00f9 th\u01b0\u1eddng \u1edf m\u1ee9c nh\u1ecf.[35]")
s = s.replace(
 "Kinh nghi\u1ec7m Th\u00e1i Lan \u0111\u00e1ng l\u01b0u \u00fd \u1edf \u0111\u00e2y:",
 "Kinh nghi\u1ec7m Mexico v\u1edbi m\u1ed9t m\u1ee9c thu\u1ebf theo l\u01b0\u1ee3ng, l\u00e0m gi\u1ea3m l\u01b0\u1ee3ng mua v\u00e0 t\u0103ng l\u01b0\u1ee3ng mua n\u01b0\u1edbc, cho c\u00f9ng m\u1ed9t h\u01b0\u1edbng.[29] Kinh nghi\u1ec7m Th\u00e1i Lan \u0111\u00e1ng l\u01b0u \u00fd \u1edf \u0111\u00e2y:")
open(VI, "w", encoding="utf-8").write(s)

# ---- 2. merge duplicate STEPS ref and renumber everywhere ------------------
def fix(path, ref_head, sup_head, drop_word):
    s = open(path, encoding="utf-8").read()
    i, j = s.index(ref_head), s.index(sup_head)
    refs = [(int(re.match(r"^(\d+)\.", l).group(1)), re.sub(r"^\d+\.\s", "", l))
            for l in s[i:j].split("\n") if re.match(r"^\d+\.\s", l)]
    drop = {n for n, l in refs if n == 2 and drop_word in l}
    mapping, kept, newno = {}, [], 0
    for n, l in refs:
        if n in drop:
            mapping[n] = 1
            continue
        newno += 1
        mapping[n] = newno
        kept.append((newno, l))

    body, after = s[:i], s[j:]
    def fg(m):
        nums = {int(x) for x in m.group(1).split(",")}
        new = sorted({mapping[x] for x in nums if x in mapping})
        return "[" + ",".join(str(x) for x in new) + "]"
    body = re.sub(r"\[(\d+(?:,\d+)*)\]", fg, body)
    after = re.sub(r"\[(\d+(?:,\d+)*)\]", fg, after)   # appendices too

    block = ref_head + "\n\n" + "\n".join(f"{n}. {l}" for n, l in kept) + "\n\n"
    s = body + block + after
    s = s.replace("38 references", "37 references").replace("38 t\u00e0i li\u1ec7u tham kh\u1ea3o", "37 t\u00e0i li\u1ec7u tham kh\u1ea3o")
    s = s.replace("| Population by age, sex, quintile, 2027\u20132050 |", "| Population by age and quintile, 2027\u20132050 |")
    s = s.replace("| D\u00e2n s\u1ed1 theo tu\u1ed5i, gi\u1edbi, ng\u0169 ph\u00e2n v\u1ecb, 2027\u20132050 |", "| D\u00e2n s\u1ed1 theo tu\u1ed5i v\u00e0 ng\u0169 ph\u00e2n v\u1ecb, 2027\u20132050 |")
    open(path, "w", encoding="utf-8").write(s)

    t = open(path, encoding="utf-8").read()
    a, b = t.index(ref_head), t.index(sup_head)
    nums = [int(re.match(r"^(\d+)\.", l).group(1)) for l in t[a:b].split("\n") if re.match(r"^\d+\.\s", l)]
    cited = {int(x) for g in re.findall(r"\[(\d+(?:,\d+)*)\]", t[:a] + t[b:]) for x in g.split(",")}
    print(path, "| refs:", len(nums), "| sequential:", nums == list(range(1, len(nums)+1)),
          "| uncited:", [n for n in nums if n not in cited])

fix(EN, "## References", "## Supplementary material", "STEPS")
fix(VI, "## T\u00e0i li\u1ec7u tham kh\u1ea3o", "## Ph\u1ee5 l\u1ee5c A", "STEPS")
