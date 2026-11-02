# -*- coding: utf-8 -*-
import re

NAMES_EN = "Nguyen Thanh Nam, Khanh Linh Lam Ngoc"
NAMES_VI = "Nguyen Thanh Nam, Khanh Linh Lam Ngoc"
AFF_EN = ("¹Faculty of Public Health, University of Medicine and Pharmacy at "
          "Ho Chi Minh City, 217 Hong Bang Street, Cho Lon Ward, Ho Chi Minh City, Vietnam")
AFF_VI = ("¹Khoa Y tế Công cộng, Đại học Y Dược Thành phố Hồ Chí Minh, "
          "217 Hồng Bàng, Phường Chợ Lớn, Thành phố Hồ Chí Minh, Việt Nam")
CORR_EN = ("Nguyen Thanh Nam, Faculty of Public Health, University of Medicine and Pharmacy "
           "at Ho Chi Minh City, 217 Hong Bang Street, Cho Lon Ward, Ho Chi Minh City, Vietnam. "
           "Email: ntnam.ddytcc23@ump.edu.vn")
CORR_VI = ("Nguyen Thanh Nam, Khoa Y tế Công cộng, Đại học Y Dược Thành phố Hồ Chí Minh, "
           "217 Hồng Bàng, Phường Chợ Lớn, Thành phố Hồ Chí Minh, Việt Nam. "
           "Email: ntnam.ddytcc23@ump.edu.vn")

CREDIT_EN = ("Nguyen Thanh Nam: conceptualisation, methodology, software, formal analysis, "
             "data curation, writing – original draft, visualisation, supervision. "
             "Khanh Linh Lam Ngoc: investigation, data curation, validation, "
             "writing – review and editing. Both authors had full access to all the data "
             "in the study, verified the underlying data, and accept responsibility for the "
             "decision to submit.")
CREDIT_VI = ("Nguyen Thanh Nam: xây dựng ý tưởng, phương pháp, phần mềm, phân tích chính thức, "
             "quản lý dữ liệu, viết bản nháp, trực quan hóa, giám sát. "
             "Khanh Linh Lam Ngoc: điều tra, quản lý dữ liệu, thẩm định, "
             "viết – rà soát và chỉnh sửa. Cả hai tác giả đều có quyền truy cập đầy đủ dữ liệu "
             "của nghiên cứu, đã kiểm chứng dữ liệu nền, và chịu trách nhiệm về quyết định nộp bài.")

FUND_EN = ("This study received no specific grant from any funding agency in the public, "
           "commercial, or not-for-profit sectors.")
FUND_VI = ("Nghiên cứu này không nhận tài trợ từ bất kỳ cơ quan nào thuộc khu vực công, "
           "thương mại hay phi lợi nhuận.")

ROLE_EN = ("The study had no funder, and therefore no funder had any role in study design, "
           "data collection, data analysis, data interpretation, or writing of the report.")
ROLE_VI = ("Nghiên cứu không có nhà tài trợ, và do đó không có bên nào có vai trò trong việc "
           "thiết kế nghiên cứu, thu thập dữ liệu, phân tích, diễn giải hay viết báo cáo.")

COI_EN = "We declare no competing interests."
COI_VI = "Chúng tôi tuyên bố không có xung đột lợi ích."

ACK_EN = "Not applicable."
ACK_VI = "Không áp dụng."

def fill(path, lang):
    s = open(path, encoding="utf-8").read()
    if lang == "en":
        s = s.replace("**Authors:** ⟦TBD-authors⟧", f"**Authors:** {NAMES_EN}")
        s = s.replace("**Affiliations:** ⟦điền⟧", f"**Affiliations:** {AFF_EN}")
        s = s.replace("**Correspondence:** ⟦điền⟧", f"**Correspondence:** {CORR_EN}")
        s = s.replace("⟦TBD-a⟧", CREDIT_EN)
        s = s.replace("**Funding**\n⟦TBD-19⟧", f"**Funding**\n{FUND_EN}")
        s = s.replace("⟦TBD-19⟧", FUND_EN)
        s = s.replace("⟦TBD-d⟧", ROLE_EN)
        s = s.replace("⟦TBD-b⟧", COI_EN)
        s = s.replace("⟦TBD-c⟧", ACK_EN)
    else:
        s = s.replace("**Tác giả:** ⟦TBD-authors⟧", f"**Tác giả:** {NAMES_VI}")
        s = s.replace("**Đơn vị:** ⟦điền⟧", f"**Đơn vị:** {AFF_VI}")
        s = s.replace("**Tác giả liên hệ:** ⟦điền⟧", f"**Tác giả liên hệ:** {CORR_VI}")
        s = s.replace("⟦TBD-a⟧", CREDIT_VI)
        s = s.replace("⟦TBD-19⟧", FUND_VI)
        s = s.replace("⟦TBD-d⟧", ROLE_VI)
        s = s.replace("⟦TBD-b⟧", COI_VI)
        s = s.replace("⟦TBD-c⟧", ACK_VI)
    open(path, "w", encoding="utf-8").write(s)
    left = sorted(set(re.findall(r"⟦[^⟧]*⟧", s)))
    print(path, "remaining:", left)

fill("Manuscript_draft_v1.md", "en")
fill("Ban_thao_Tieng_Viet.md", "vi")
