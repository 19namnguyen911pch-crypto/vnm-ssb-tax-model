# -*- coding: utf-8 -*-
"""Split references into the 30 cited in the main text and the rest, which are
cited only in the appendices and become a supplementary list (S1..Sn)."""
import re

PATH = "Manuscript_draft_v1.md"
HEAD = "## References"
TAIL = "## Supplementary material"
SPLIT = "## Appendix A"


def first_order(text):
    out = []
    for m in re.finditer(r"\[(\d+(?:,\d+)*)\]", text):
        for x in m.group(1).split(","):
            n = int(x)
            if n not in out:
                out.append(n)
    return out


s = open(PATH, encoding="utf-8").read()
a = s.index(HEAD)
t = s.index(TAIL)
b = s.index(SPLIT)

refs = {int(m.group(1)): m.group(2)
        for m in re.finditer(r"(?m)^(\d+)\.\s(.*)$", s[a:t])}

main = s[:a]
between = s[t:b]          # the supplementary-material bullet list
app = s[b:]

main_ids = first_order(main)
assert all(n in refs for n in main_ids)

app_ids = [n for n in first_order(app) if n not in main_ids]
for n in sorted(refs):
    if n not in main_ids and n not in app_ids:
        app_ids.append(n)

main_map = {old: i + 1 for i, old in enumerate(main_ids)}
supp_map = {old: f"S{i + 1}" for i, old in enumerate(app_ids)}


def remap(text, allow_supp):
    def f(m):
        parts = []
        for x in m.group(1).split(","):
            n = int(x)
            if n in main_map:
                parts.append(str(main_map[n]))
            elif allow_supp and n in supp_map:
                parts.append(supp_map[n])
            else:
                parts.append(str(n))
        return "[" + ",".join(parts) + "]"
    return re.sub(r"\[(\d+(?:,\d+)*)\]", f, text)


main_block = HEAD + "\n\n" + "\n".join(
    f"{main_map[n]}. {refs[n]}" for n in main_ids) + "\n\n"

supp_block = ("\n## Supplementary references\n\nReferences cited only in the "
              "appendices.\n\n" +
              "\n".join(f"{supp_map[n]}. {refs[n]}" for n in app_ids) + "\n")

out = (remap(main, False) + main_block + between +
       remap(app, True).rstrip() + "\n" + supp_block)
open(PATH, "w", encoding="utf-8").write(out)

print("main references:", len(main_ids))
print("supplementary references:", len(app_ids))
