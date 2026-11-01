# -*- coding: utf-8 -*-
"""Mirror the last three fixes into the Vietnamese file: panel completeness,
Table 2 sources, and the elasticity-gradient sensitivity."""
p = "Ban_thao_Tieng_Viet.md"
s = open(p, encoding="utf-8").read()


def rep(old, new):
    global s
    assert old in s, "NOT FOUND: " + old[:80]
    s = s.replace(old, new, 1)


# panel: name the three records again, cited as supplementary
rep("Các bản ghi còn lại mô tả tác động thực nghiệm của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống[1] và tác động phân bố của thuế sức khỏe trong khu vực.",
"Các bản ghi còn lại mô tả tác động thực nghiệm của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống,[1] mức chấp nhận của công chúng,[S8] cách diễn giải quyền con người về thuế đã ban hành,[S9] một phân tích pháp lý về thiết kế đã ban hành,[S10] và tác động phân bố của thuế sức khỏe trong khu vực.")

# Table 2 source column with numbers
for old, new in [
    ("| Dân số từ 20 tuổi, theo tuổi và ngũ phân vị | Dự báo dân số UN 2024 | Cố định | 81 triệu, phân bố năm 2027 |",
     "| Dân số từ 20 tuổi, theo tuổi và ngũ phân vị | Dự báo dân số UN 2024 (Phụ lục B) | Cố định | 81 triệu, phân bố năm 2027 |"),
    ("| Khối lượng đồ uống chịu thuế | Euromonitor; Điều tra dinh dưỡng toàn quốc 2019–20 | Gamma | 145 mL/ngày (90–220) |",
     "| Khối lượng đồ uống chịu thuế | Euromonitor; Điều tra dinh dưỡng toàn quốc (Phụ lục B) | Gamma | 145 mL/ngày (90–220) |"),
    ("| Mức truyền dẫn | Đánh giá tại Mexico, Chile, Barbados, Bồ Đào Nha, Pháp | Tam giác | 0,90 (0,50–1,30) |",
     "| Mức truyền dẫn | Đánh giá tại Mexico, Chile, Barbados [26], Bồ Đào Nha và Pháp [27,28] | Tam giác | 0,90 (0,50–1,30) |"),
    ("| Độ co giãn giá riêng | Phân tích gộp cho nước thu nhập thấp–trung bình và châu Á | Log-chuẩn | −1,20 (−0,80 đến −1,80) |",
     "| Độ co giãn giá riêng | Phân tích gộp cho nước thu nhập thấp–trung bình và châu Á [16] | Log-chuẩn | −1,20 (−0,80 đến −1,80) |"),
    ("| Mật độ năng lượng; bù trừ | Bảng thành phần thực phẩm Việt Nam | Cố định; đều | 44 kcal/100 mL; 30% (15–45%) |",
     "| Mật độ năng lượng; bù trừ | Bảng thành phần thực phẩm Việt Nam (Phụ lục B) | Cố định; đều | 44 kcal/100 mL; 30% (15–45%) |"),
    ("| Nguy cơ tương đối BMI–bệnh | Nghiên cứu đoàn hệ châu Á–Thái Bình Dương | Log-chuẩn | 1,55; 1,11; 1,12 mỗi 2 kg/m² |",
     "| Nguy cơ tương đối BMI–bệnh | Nghiên cứu đoàn hệ châu Á–Thái Bình Dương [19,20] | Log-chuẩn | 1,55; 1,11; 1,12 mỗi 2 kg/m² |"),
    ("| Tỷ lệ mắc, tử vong, trọng số | GBD 2021; STEPS 2021 | Beta; gamma | Theo tuổi và giới |",
     "| Tỷ lệ mắc, tử vong, trọng số | GBD 2021 [25]; STEPS 2021 [2] | Beta; gamma | Theo tuổi và giới |"),
    ("| Chi phí y tế mỗi ca | Các nghiên cứu chi phí bệnh Việt Nam | Gamma | 8,0 / 84,9 / 10,5 triệu đồng |",
     "| Chi phí y tế mỗi ca | Các nghiên cứu chi phí bệnh Việt Nam [21,22,23,24] | Gamma | 8,0 / 84,9 / 10,5 triệu đồng |"),
    ("| Chi tiêu hộ theo ngũ phân vị | VHLSS 2024 | Cố định; log-chuẩn | 3,0 triệu đồng; Q5/Q1 = 3,1 |",
     "| Chi tiêu hộ theo ngũ phân vị | VHLSS 2024 (Phụ lục B) | Cố định; log-chuẩn | 3,0 triệu đồng; Q5/Q1 = 3,1 |"),
]:
    rep(old, new)

# the paragraph that followed the table must stay a paragraph
rep("| Chi tiêu hộ theo ngũ phân vị | VHLSS 2024 (Phụ lục B) | Cố định; log-chuẩn | 3,0 triệu đồng; Q5/Q1 = 3,1 | Trong các tham số",
    "| Chi tiêu hộ theo ngũ phân vị | VHLSS 2024 (Phụ lục B) | Cố định; log-chuẩn | 3,0 triệu đồng; Q5/Q1 = 3,1 |\n\nTrong các tham số")

# limitations: elasticity gradient tested
rep("và trên gradient độ co giãn 1,4, cả hai đều là giả định.",
"và trên gradient độ co giãn 1,4; với gradient từ 1,0 đến 1,8, tỷ số Q1/Q5 dịch từ 0,56 đến 1,00 (Phụ lục F), nên phía tài chính cũng có điều kiện.")

# Appendix F: new section
rep("**F.8 Các phân tích không thực hiện.**",
"""**F.8 Gradient độ co giãn.** Gradient độ co giãn giá riêng theo ngũ phân vị là giả định. Ở giá trị trung tâm, giữ mọi thứ khác cố định, tỷ số Q1/Q5 của DALY tránh được là 0,56 ở gradient 1,0; 0,78 ở 1,4 (kịch bản cơ sở) và 1,00 ở 1,8, với chỉ số tập trung tương ứng 0,112; 0,046 và −0,005. Vì thuế phải trả cũng tỷ lệ với tiêu thụ, chỉ số Kakwani dịch theo cùng giả định này.

**F.9 Các phân tích không thực hiện.**""")

# supplementary references
s = s.rstrip() + """

S8. Nguyen LM, De Steur H. Public acceptability of policy interventions to reduce sugary drink consumption in urban Vietnam. Sustainability. 2021;13(23):13422.
S9. Nguyen LG, Nguyen TD. Between commerce and conscience: a human rights assessment of Vietnam's excise tax on sugar-sweetened beverages. Nord J Hum Rights. 2025;43(4):405–18.
S10. Nguyen TNC, Nguyen NA, Tran CN. Excise tax on sugar-sweetened beverages in Viet Nam: a view from theory and international experience. VLUTE J Sci. 2026;2(2). doi:10.64215/h1bmvr13
"""
open(p, "w", encoding="utf-8").write(s)
print("VI mirrored")
