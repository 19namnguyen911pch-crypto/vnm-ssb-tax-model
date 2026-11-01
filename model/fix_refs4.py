# -*- coding: utf-8 -*-
"""Add the four included studies, then renumber every reference in order of
first citation, in both language versions."""
import re

NEW = {
 39: "Luong L, Vu LH. Impacts of excise taxation on non-alcoholic beverage consumption in Vietnam. Sustainability. 2020;12(3):1092.",
 40: "Nguyen LM, De Steur H. Public acceptability of policy interventions to reduce sugary drink consumption in urban Vietnam. Sustainability. 2021;13(23):13422.",
 41: "Nguyen LG, Nguyen TD. Between commerce and conscience: a human rights assessment of Vietnam's excise tax on sugar-sweetened beverages. Nord J Hum Rights. 2025;43(4):405–18.",
 42: "Nguyen TNC, Nguyen NA, Tran CN. Excise tax on sugar-sweetened beverages in Viet Nam: a view from theory and international experience. VLUTE J Sci. 2026;2(2). doi:10.64215/h1bmvr13",
}

def split_refs(s, head, tail):
    i, j = s.index(head), s.index(tail)
    block = s[i:j]
    refs = {int(m.group(1)): m.group(2) for m in
            re.finditer(r"(?m)^(\d+)\.\s(.*)$", block)}
    return s[:i], refs, s[j:], block

def rebuild(path, head, tail, add_citations=None, cite_map=None):
    s = open(path, encoding="utf-8").read()
    pre, refs, post, block = split_refs(s, head, tail)
    refs.update(NEW)

    if add_citations:
        for a, b in add_citations:
            assert a in pre, a[:60]
            pre = pre.replace(a, b)

    # order of first appearance in the text (pre + post)
    order = []
    for m in re.finditer(r"\[(\d+(?:,\d+)*)\]", pre + post):
        for x in m.group(1).split(","):
            n = int(x)
            if n not in order:
                order.append(n)
    for n in sorted(refs):
        if n not in order:
            order.append(n)
    mapping = {old: i + 1 for i, old in enumerate(order)}

    def remap(text):
        def f(m):
            nums = sorted({mapping[int(x)] for x in m.group(1).split(",")})
            return "[" + ",".join(map(str, nums)) + "]"
        return re.sub(r"\[(\d+(?:,\d+)*)\]", f, text)

    pre2, post2 = remap(pre), remap(post)
    newblock = head + "\n\n" + "\n".join(
        f"{mapping[n]}. {refs[n]}" for n in order) + "\n\n"
    open(path, "w", encoding="utf-8").write(pre2 + newblock + post2)
    return mapping

# ---------------- English ----------------
EN_ADD = [
 ("The remaining records describe the empirical effect of excise taxation on beverage consumption, public acceptability, the human-rights framing of the enacted tax, and the distributional impacts of health taxes regionally.",
  "The remaining records describe the empirical effect of excise taxation on beverage consumption,[39] public acceptability of SSB policies,[40] the human-rights framing of the enacted tax,[41] a legal analysis of the enacted design,[42] and the distributional impacts of health taxes regionally."),
]
m = rebuild("Manuscript_draft_v1.md", "## References", "## Supplementary material", EN_ADD)
print("EN refs:", len(m))

# ---------------- Vietnamese ----------------
VI_ADD = [
 ("Các bản ghi còn lại mô tả tác động thực nghiệm của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống, mức chấp nhận của công chúng, cách diễn giải quyền con người về thuế đã ban hành, và tác động phân bố của thuế sức khỏe trong khu vực.",
  "Các bản ghi còn lại mô tả tác động thực nghiệm của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống,[39] mức chấp nhận của công chúng,[40] cách diễn giải quyền con người về thuế đã ban hành,[41] một phân tích pháp lý về thiết kế đã ban hành,[42] và tác động phân bố của thuế sức khỏe trong khu vực."),
]
m2 = rebuild("Ban_thao_Tieng_Viet.md", "## Tài liệu tham khảo", "## Phụ lục A", VI_ADD)
print("VI refs:", len(m2))
print("maps equal:", m == m2)
