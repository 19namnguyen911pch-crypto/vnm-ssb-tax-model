# -*- coding: utf-8 -*-
"""Renumber every reference in order of first appearance, in both languages."""
import re


def renumber(path, head, tail):
    s = open(path, encoding="utf-8").read()
    i, j = s.index(head), s.index(tail)
    block = s[i:j]
    refs = {int(m.group(1)): m.group(2)
            for m in re.finditer(r"(?m)^(\d+)\.\s(.*)$", block)}
    pre, post = s[:i], s[j:]
    body = pre + post

    order = []
    for m in re.finditer(r"\[(\d+(?:,\d+)*)\]", body):
        for x in m.group(1).split(","):
            n = int(x)
            if n not in order:
                order.append(n)
    for n in sorted(refs):
        if n not in order:
            order.append(n)

    missing = [n for n in order if n not in refs]
    if missing:
        raise SystemExit(f"{path}: cited but not listed: {missing}")

    mapping = {old: k + 1 for k, old in enumerate(order)}

    def remap(text):
        def f(m):
            nums = sorted({mapping[int(x)] for x in m.group(1).split(",")})
            return "[" + ",".join(map(str, nums)) + "]"
        return re.sub(r"\[(\d+(?:,\d+)*)\]", f, text)

    newblock = head + "\n\n" + "\n".join(
        f"{mapping[n]}. {refs[n]}" for n in order) + "\n\n"
    open(path, "w", encoding="utf-8").write(remap(pre) + newblock + remap(post))
    print(path, "references:", len(order))


renumber("Manuscript_draft_v1.md", "## References", "## Supplementary material")
renumber("Ban_thao_Tieng_Viet.md", "## Tài liệu tham khảo", "## Phụ lục A")
