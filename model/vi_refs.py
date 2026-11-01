# -*- coding: utf-8 -*-
"""Replace the Vietnamese reference list with the 30 main references and the
supplementary list, and remap the appendix citations."""
import json
import re

MAP = json.load(open("/tmp/refmap.json"))
MAP["27"] = "S2"          # General Nutrition Survey, cited once in Appendix B

p = "Ban_thao_Tieng_Viet.md"
vi = open(p, encoding="utf-8").read()

en = open("Manuscript_draft_v1.md", encoding="utf-8").read()
a = en.index("## References")
b = en.index("## Supplementary material")
main_block = en[a:b].strip()
c = en.index("## Supplementary references")
supp_block = en[c:].strip()

# split the Vietnamese file at its reference heading
i = vi.index("## Tài liệu tham khảo")
j = vi.index("## Phụ lục A")
head = vi[:i]
app = vi[j:]

# remap appendix citations
def f(m):
    out = []
    for x in m.group(1).split(","):
        out.append(MAP.get(x, "#" + x))
    return "[" + ",".join(out) + "]"

app = re.sub(r"\[(\d+(?:,\d+)*)\]", f, app)
leftover = sorted(set(re.findall(r"\[#\d+\]", app)))
if leftover:
    raise SystemExit("unmapped citations: " + ", ".join(leftover))

virefs = main_block.replace("## References", "## Tài liệu tham khảo")
visupp = supp_block.replace("## Supplementary references",
                            "## Tài liệu tham khảo bổ sung")

out = head + virefs + "\n\n" + app.rstrip() + "\n\n" + visupp + "\n"
open(p, "w", encoding="utf-8").write(out)
print("VI references replaced; appendix citations remapped")
