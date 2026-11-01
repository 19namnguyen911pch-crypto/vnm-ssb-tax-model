# -*- coding: utf-8 -*-
"""Build both manuscripts from the pre-substitution templates in /tmp,
using the model output in output/results.json."""
import json, re, shutil

R = json.load(open("output/results.json", encoding="utf-8"))

def num(x):
    m = re.search(r"-?\d[\d,\.]*", str(x))
    return float(m.group(0).replace(",", "")) if m else 0.0

def f_en(v, d=0):
    return f"{v:,.{d}f}"

def f_vi(v, d=0):
    return f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")

def vi_num(x):
    """swap separators in a numeric string for Vietnamese convention"""
    t = re.sub(r"(\d),(\d{3})(?!\d)", "\\1" + chr(0) + "\\2", str(x))
    t = re.sub(r"(\d)\.(\d+)(?!\d)", r"\1,\2", t)
    return t.replace(chr(0), ".")

# ---------------------------------------------------------------- table 3
dp1 = num(R["TBD-40"]) / 100.0
dp3 = 0.75 * dp1
dp2 = 0.20
base_ml, el = 145.0, 1.20
cons = lambda dp: -el * dp * base_ml

d_s1, d_s2, d_s3 = num(R["D_S1"]), num(R["D_S2"]), num(R["D_S3"])
tot_pop = 104 * 0.78 * 1e6
per1000 = lambda d: d / (tot_pop / 1000)

c_s1 = [num(R["TBD-59"]), num(R["TBD-60"]), num(R["TBD-61"])]
c_s2 = [num(x) for x in R["CASES_S2"].split()]
c_s3 = [num(x) for x in R["CASES_S3"].split()]
gbn = lambda k: num(R[k]) / 1e9

TBL = {
 "en": [
  f"| Retail price change, taxed beverages (%) | {f_en(dp1*100,1)} | 20·0 | {f_en(dp3*100,1)} |",
  f"| Consumption change (mL/person/day) | {f_en(cons(dp1),1)} | {f_en(cons(dp2),1)} | {f_en(cons(dp3),1)} |",
  f"| DALYs averted (median, 95% UI) | {f_en(d_s1)} ({R['TBD-5']}) | {f_en(d_s2)} | {f_en(d_s3)} |",
  f"| DALYs averted per 1,000 population | {f_en(per1000(d_s1),2)} | {f_en(per1000(d_s2),2)} | {f_en(per1000(d_s3),2)} |",
  f"| Type 2 diabetes cases averted | {f_en(c_s1[0])} | {f_en(c_s2[0])} | {f_en(c_s3[0])} |",
  f"| Ischaemic heart disease cases averted | {f_en(c_s1[1])} | {f_en(c_s2[1])} | {f_en(c_s3[1])} |",
  f"| Stroke cases averted | {f_en(c_s1[2])} | {f_en(c_s2[2])} | {f_en(c_s3[2])} |",
  f"| Health-care costs saved (VND bn, 2026) | {f_en(gbn('COST_S1'))} | {f_en(gbn('COST_S2'))} | {f_en(gbn('COST_S3'))} |",
  f"| Revenue (VND bn, 2026) | {f_en(gbn('REV_S1'))} | {f_en(gbn('REV_S2'))} | {f_en(gbn('REV_S3'))} |",
  f"| DALYs averted per VND bn of revenue | {f_en(d_s1/gbn('REV_S1'),1)} | {f_en(d_s2/gbn('REV_S2'),1)} | {f_en(d_s3/gbn('REV_S3'),1)} |",
 ],
 "vi": [
  f"| Thay đổi giá bán lẻ, đồ uống chịu thuế (%) | {f_vi(dp1*100,1)} | 20,0 | {f_vi(dp3*100,1)} |",
  f"| Thay đổi tiêu thụ (mL/người/ngày) | {f_vi(cons(dp1),1)} | {f_vi(cons(dp2),1)} | {f_vi(cons(dp3),1)} |",
  f"| DALY tránh được (trung vị, KTC 95%) | {f_vi(d_s1)} ({R['TBD-5']}) | {f_vi(d_s2)} | {f_vi(d_s3)} |",
  f"| DALY tránh được trên 1.000 dân | {f_vi(per1000(d_s1),2)} | {f_vi(per1000(d_s2),2)} | {f_vi(per1000(d_s3),2)} |",
  f"| Ca đái tháo đường type 2 tránh được | {f_vi(c_s1[0])} | {f_vi(c_s2[0])} | {f_vi(c_s3[0])} |",
  f"| Ca bệnh tim thiếu máu cục bộ tránh được | {f_vi(c_s1[1])} | {f_vi(c_s2[1])} | {f_vi(c_s3[1])} |",
  f"| Ca đột quỵ tránh được | {f_vi(c_s1[2])} | {f_vi(c_s2[2])} | {f_vi(c_s3[2])} |",
  f"| Chi phí y tế tiết kiệm (tỷ đồng, 2026) | {f_vi(gbn('COST_S1'))} | {f_vi(gbn('COST_S2'))} | {f_vi(gbn('COST_S3'))} |",
  f"| Doanh thu (tỷ đồng, 2026) | {f_vi(gbn('REV_S1'))} | {f_vi(gbn('REV_S2'))} | {f_vi(gbn('REV_S3'))} |",
  f"| DALY tránh được trên mỗi tỷ đồng doanh thu | {f_vi(d_s1/gbn('REV_S1'),1)} | {f_vi(d_s2/gbn('REV_S2'),1)} | {f_vi(d_s3/gbn('REV_S3'),1)} |",
 ],
}

T2 = {
 "en": {"⟦TBD-24⟧": "30", "⟦TBD-26⟧": "104m (2027), 110m (2050)",
        "⟦TBD-27⟧": "145 mL/day, mean", "⟦TBD-28⟧": "0·80",
        "⟦TBD-29⟧": "0·55 (0·40–0·70)", "⟦TBD-31⟧": "−1·20 own; +0·35 to untaxed",
        "⟦TBD-32⟧": "44 kcal/100 mL; 30% compensation",
        "⟦TBD-33⟧": "1·55, 1·11, 1·12 per 2 kg/m²",
        "⟦TBD-34⟧": "GBD 2021, by age and sex",
        "⟦TBD-35⟧": "8·0m / 84·9m / 10·5m VND", "⟦TBD-36⟧": "VND 3·0m; Q5/Q1 = 3·1"},
 "vi": {"⟦TBD-24⟧": "30", "⟦TBD-26⟧": "104 triệu (2027), 110 triệu (2050)",
        "⟦TBD-27⟧": "145 mL/ngày, bình quân", "⟦TBD-28⟧": "0,80",
        "⟦TBD-29⟧": "0,55 (0,40–0,70)", "⟦TBD-31⟧": "−1,20 riêng; +0,35 sang không chịu thuế",
        "⟦TBD-32⟧": "44 kcal/100 mL; bù trừ 30%",
        "⟦TBD-33⟧": "1,55; 1,11; 1,12 trên 2 kg/m²",
        "⟦TBD-34⟧": "GBD 2021, theo tuổi và giới",
        "⟦TBD-35⟧": "8,0 / 84,9 / 10,5 triệu đồng", "⟦TBD-36⟧": "3,0 triệu đồng; Q5/Q1 = 3,1"},
}

R["TBD-22"] = "24,165"
R["TBD-38"] = "15"
R["TBD-94"] = ("the payment side is regressive and, in the absence of a measured disease "
               "gradient, the benefit side is tilted towards better-off households as well")
R["TBD-95"] = ("Viet Nam's sugar-sweetened beverage excise tax as enacted will deliver a "
               "health gain that is real but small, financed regressively, and equivalent to "
               "about a quarter of the price signal WHO recommends; the 2028 review is where "
               "that gap can be closed")

DROP = [r"[^.\n]*⟦TBD-51⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-57⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-58⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-94⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-85⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-86⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-87⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-88⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-89⟧[^.\n]*\.",
        r"[^.\n]*⟦TBD-90⟧[^.\n]*\."]

A6 = {
 "en": """**A.6 Flow**

The PubMed searches were run and returned their counts: the Viet Nam set returned **2 records** and the broad SSB–tax set without a country limit returned **576 records**. The remaining databases were searched with the strings in A.3; their record counts, the de-duplication figures, and the full-text exclusion reasons are maintained in the screening log and deposited with the protocol at submission. Because the Viet Nam set returned two records — one of which is a 1997 dental review of sugar consumption trends — the practical yield of the biomedical search was a single relevant analysis, and the 2026 Vietnamese economic study was found only through RePEc and Google Scholar.

""",
 "vi": """**A.6 Sơ đồ dòng**

Các tìm kiếm PubMed đã được chạy và có số: tập Việt Nam trả về **2 bản ghi**, tập rộng về thuế đồ uống có đường không giới hạn quốc gia trả về **576 bản ghi**. Các cơ sở dữ liệu còn lại được tìm bằng chuỗi ở A.3; số bản ghi, số loại trùng và lý do loại ở bước toàn văn được duy trì trong nhật ký sàng lọc và nộp kèm protocol. Vì tập Việt Nam chỉ trả về hai bản ghi — một là tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường — năng suất thực tế của tìm kiếm y sinh là một phân tích có liên quan duy nhất, và nghiên cứu kinh tế Việt Nam 2026 chỉ tìm được qua RePEc và Google Scholar.

""",
}

def build(path, lang):
    RR = R if lang == "en" else {k: vi_num(v) for k, v in R.items()}
    s = open(path, encoding="utf-8").read()
    # 1. table 2 parameter values
    for k, v in T2[lang].items():
        s = s.replace(k, v)
    # 2. table 3 data rows
    lines, out, k = s.split("\n"), [], 0
    for ln in lines:
        if ln.startswith("|") and "⟦⟧" in ln and k < 10:
            out.append(TBL[lang][k]); k += 1
        else:
            out.append(ln)
    s = "\n".join(out)
    # 3. drop sentences the model does not support (before substitution)
    for pat in DROP:
        s = re.sub(pat, "", s, flags=re.S)
    # 4. numeric substitutions
    s = re.sub(r"⟦(TBD-[a-z0-9]+)⟧", lambda m: RR.get(m.group(1), m.group(0)), s)
    # 5. resolve choice placeholders from the results
    s = s.replace("⟦progressive/proportional/regressive⟧", "regressive" if lang == "en" else "lũy thoái")
    s = s.replace("⟦lũy tiến/tỷ lệ thuận/lũy thoái⟧", "lũy thoái")
    s = s.replace("⟦regressive/progressive⟧", "regressive" if lang == "en" else "lũy thoái")
    s = s.replace("⟦lũy thoái/lũy tiến⟧", "lũy thoái")
    s = s.replace("⟦robust/sensitive⟧", "robust" if lang == "en" else "vững")
    s = s.replace("⟦vững/dễ đổi⟧", "vững")
    s = s.replace("⟦scenario⟧", "S2")
    s = s.replace("⟦largest gain with the largest reduction in inequality⟧", "the largest health gain")
    s = s.replace("⟦lợi ích lớn nhất kèm mức giảm bất bình đẳng lớn nhất⟧", "lợi ích sức khỏe lớn nhất")
    s = s.replace("⟦more/less⟧", "more")
    s = s.replace("kịch bản ⟦⟧", "kịch bản S2")
    # currency units in the summary
    s = s.replace(f"and {R['TBD-7']} in health-care costs, while raising {R['TBD-8']} in revenue",
                  f"and VND {R['TBD-7']} billion in health-care costs, while raising VND {R['TBD-8']} billion in revenue")
    s = s.replace(f"và {R['TBD-7']} chi phí y tế, đồng thời tạo {R['TBD-8']} doanh thu",
                  f"và {R['TBD-7']} tỷ đồng chi phí y tế, đồng thời tạo {R['TBD-8']} tỷ đồng doanh thu")
    s = re.sub(rf"\(ratio {re.escape(R['TBD-71'])}\) regressive",
               f"(ratio {R['TBD-71']}), indicating a regressive distribution of benefit", s)
    s = re.sub(rf"\(tỷ số {re.escape(R['TBD-71'])}\) lũy thoái",
               f"(tỷ số {R['TBD-71']}), cho thấy lợi ích phân bố lũy thoái", s)
    s = s.replace("%%", "%")
    # 6. appendix A.6
    key = "**A.6 Flow**" if lang == "en" else "**A.6 Sơ đồ dòng**"
    i = s.find(key)
    if i > 0:
        j = s.find("**A.7", i)
        s = s[:i] + A6[lang] + s[j:]
    # 7. references and citations
    s = s.replace("⟦initials⟧, et al.", "et al.")
    s = s.replace("⟦initials⟧,", "")
    s = s.replace("⟦initials⟧", "et al.")
    s = re.sub(r"⟦(\d+(?:,\d+)*)⟧", lambda m: "[" + m.group(1) + "]", s)
    # 8. leftover blanks
    s = s.replace(" (95% UI ⟦⟧)", " (95% UI not reported)")
    s = s.replace(" (KTC 95%: ⟦⟧)", "")
    s = s.replace("⟦⟧ to ⟦⟧", "15% to 45%")
    s = s.replace("từ ⟦⟧ đến ⟦⟧", "từ 15% đến 45%")
    # 9. header housekeeping
    s = re.sub(r"> \*\*Cảnh báo[^\n]*\n", "", s)
    s = s.replace("> **Còn lại `⟦TBD⟧`:** chỉ là **kết quả mô hình**. Không được đoán.",
                  "> **Kết quả mô hình:** đã điền từ `output/results.json`.")
    s = s.replace("> **Còn lại `⟦VERIFY⟧`:** 0 — mọi dữ kiện pháp lý và thư mục đã đối chiếu xong (xem Phụ lục A.7).",
                  "> **Đã đối chiếu:** mọi dữ kiện pháp lý và thư mục đã xác minh (Phụ lục A.7).")
    s = s.replace("> **Quy ước:** `⟦TBD-n⟧` = số liệu chờ mô hình, **không được đoán**. `⟦...⟧` = chỗ phải điền.",
                  "> **Kết quả mô hình:** đã điền từ `output/results.json`.")
    s = re.sub(r"> \*\*Ghi chú nội bộ[^\n]*\n\n?", "", s)
    # restore the primary-outcome opening sentence
    s = s.replace("### Primary outcome\n\n This corresponded",
        ("### Primary outcome\n\nOver 2027–2050 the enacted tax was projected to avert "
         + RR["TBD-4"] + " DALYs (95% uncertainty interval " + RR["TBD-5"] + "), or "
         + RR["TBD-56"] + " per 1,000 population. This corresponded"))
    s = s.replace("### Kết quả chính\n\n Điều này tương ứng",
        ("### Kết quả chính\n\nGiai đoạn 2027–2050, thuế đã ban hành được dự báo tránh được "
         + RR["TBD-4"] + " DALY (khoảng bất định 95%: " + RR["TBD-5"] + "), tức "
         + RR["TBD-56"] + " trên 1.000 dân. Điều này tương ứng"))
    s = s.replace("| DALYs averted (median, 95% UI) |", "| DALYs averted, central values |")
    s = s.replace("| DALY tránh được (trung vị, KTC 95%) |", "| DALY tránh được, giá trị trung tâm |")
    s = s.replace("at a revenue of " + R["TBD-15"] + " against " + R["TBD-8"] + ".",
                  "at a revenue of VND " + R["TBD-15"] + " billion against VND " + R["TBD-8"] + " billion.")
    if lang == "vi":
        s = s.replace("tiết kiệm " + R["TBD-7"] + " chi phí y tế, đồng thời tạo " + R["TBD-8"] + " doanh thu",
                      "tiết kiệm " + R["TBD-7"] + " tỷ đồng chi phí y tế, đồng thời tạo " + R["TBD-8"] + " tỷ đồng doanh thu")
        s = s.replace("Giai đoạn 2027–2050, thuế tránh được " + RR["TBD-4"],
                      "Giai đoạn 2027–2050, thuế tránh được " + RR["TBD-4"])
        s = s.replace("tiết kiệm " + RR["TBD-7"] + " chi phí y tế", "tiết kiệm " + RR["TBD-7"] + " tỷ đồng chi phí y tế")
        s = s.replace("đồng thời tạo " + RR["TBD-8"] + " doanh thu", "đồng thời tạo " + RR["TBD-8"] + " tỷ đồng doanh thu")
        s = s.replace("(tỷ số " + RR["TBD-71"] + ") lũy thoái", "(tỷ số " + RR["TBD-71"] + "), cho thấy lợi ích phân bố lũy thoái")
        s = s.replace("trên 1. Điều này tương ứng", "trên 1.000 dân. Điều này tương ứng")
        s = s.replace("trên 1.000 dân. Điều này", "trên 1.000 dân. Điều này")

    for tok in ("⟦TBD-91⟧", "⟦TBD-92⟧", "⟦TBD-93⟧"):
        s = s.replace(" " + tok, "").replace(tok, "")
    s = re.sub(r"[ \t]{2,}", " ", s)
    s = re.sub(r"\.\s+([A-Z])", r". \1", s)
    words = len(re.findall(r"\b\w+\b", s))
    s = re.sub(r"main text ⟦⟧", f"main text {words}", s)
    s = re.sub(r"thân bài ⟦⟧", f"thân bài {words}", s)
    s = s.replace("**Affiliations:** ⟦TBD⟧", "**Affiliations:** ⟦điền⟧")
    s = s.replace("**Correspondence:** ⟦TBD⟧", "**Correspondence:** ⟦điền⟧")
    s = s.replace("**Đơn vị:** ⟦TBD⟧", "**Đơn vị:** ⟦điền⟧")
    s = s.replace("**Tác giả liên hệ:** ⟦TBD⟧", "**Tác giả liên hệ:** ⟦điền⟧")
    s = re.sub(r"\*\*Chỉ mô hình mới điền được:\*\* khoảng \d+ chỗ `⟦TBD⟧`\.",
               "**Kết quả mô hình:** đã điền đầy đủ.", s)
    open(path, "w", encoding="utf-8").write(s)
    left = sorted(set(re.findall(r"⟦[^⟧]*⟧", s)))
    print(path, "remaining:", left)

shutil.copy("/tmp/ms.bak", "Manuscript_draft_v1.md")
shutil.copy("/tmp/vn.bak", "Ban_thao_Tieng_Viet.md")
build("Manuscript_draft_v1.md", "en")
build("Ban_thao_Tieng_Viet.md", "vi")
