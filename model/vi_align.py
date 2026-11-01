# -*- coding: utf-8 -*-
"""Align the Vietnamese text with the English: panel wording, citation numbers
after the loss of one reference, parameter-sources sentence, Table 2, baseline
cost wording, and the abstract."""
p = "Ban_thao_Tieng_Viet.md"
s = open(p, encoding="utf-8").read()


def rep(old, new):
    global s
    assert old in s, "NOT FOUND: " + old[:80]
    s = s.replace(old, new, 1)


# --- panel: the three Vietnamese studies are no longer in the list, and the
# --- panel must not promise what the paper does not do
rep("Các bản ghi còn lại mô tả tác động thực nghiệm của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống,[1] mức chấp nhận của công chúng,[2] cách diễn giải quyền con người về thuế đã ban hành,[3] một phân tích pháp lý về thiết kế đã ban hành,[4] và tác động phân bố của thuế sức khỏe trong khu vực.",
"Các bản ghi còn lại mô tả tác động thực nghiệm của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống[1] và tác động phân bố của thuế sức khỏe trong khu vực.")

rep("để đánh đổi giữa hiệu quả và công bằng được **đo** chứ không phải được giả định, đồng thời ước tính lợi ích sức khỏe trên mỗi đồng doanh thu của một mức thuế theo gam đường cân bằng doanh thu — thiết kế nhiều khả năng được xem xét tại kỳ rà soát luật.",
"để lợi ích và khoản chi trả có thể được đọc cùng nhau, đồng thời nêu rõ phần nào của kết quả phân bố dựa trên một gradient bệnh giả định và phần nào không.")

# --- citation numbers shift by one from [16] onward (one reference was dropped)
pairs = [
    ("vì độ co giãn lớn hơn ở các hộ thu nhập thấp.[17]", "vì độ co giãn lớn hơn ở các hộ thu nhập thấp.[16]"),
    ("được dùng để báo cáo mức thay thế[18]", "được dùng để báo cáo mức thay thế[17]"),
    ("chi phí năng lượng duy trì cân nặng giảm dần khi BMI tăng,[19]", "chi phí năng lượng duy trì cân nặng giảm dần khi BMI tăng,[18]"),
    ("từ Nghiên cứu đoàn hệ châu Á–Thái Bình Dương,[20,21]", "từ Nghiên cứu đoàn hệ châu Á–Thái Bình Dương,[19,20]"),
    ("được phân bổ từ các nghiên cứu đợt cấp.[22,23,24,25]", "được phân bổ từ các nghiên cứu đợt cấp.[21,22,23,24]"),
    ("nhân trọng số khuyết tật.[26]", "nhân trọng số khuyết tật.[25]"),
    ("gần 100% trong các đánh giá.[27,28,29]", "gần 100% trong các đánh giá.[26,27,28]"),
    ("với danh mục kiểm tra ở Phụ lục D.[30]", "với danh mục kiểm tra ở Phụ lục D.[29]"),
    ("còn thấp hơn nếu mức truyền dẫn chỉ là một phần.[27]", "còn thấp hơn nếu mức truyền dẫn chỉ là một phần.[26]"),
]
for old, new in pairs:
    rep(old, new)

# --- parameter sources: the variance decomposition, not two favourites
rep("Hai tham số mang phần lớn bất định: tỷ trọng giá xuất xưởng, chưa có ước lượng Việt Nam, và mức truyền dẫn, dao động từ dưới 50% đến gần 100% trong các đánh giá.[26,27,28]",
"Trong các tham số ở Phụ lục B, độ co giãn giá riêng chiếm một nửa phương sai được giải thích của DALY tránh được, mức truyền dẫn một phần năm và nguy cơ tương đối BMI–đái tháo đường một phần tám; tỷ trọng giá xuất xưởng, chưa có ước lượng Việt Nam, chiếm 7%. Mức truyền dẫn dao động từ dưới 50% đến gần 100% trong các đánh giá.[26,27,28]")

# --- Table 2 back in the main text
rep("Phụ lục B liệt kê từng tham số với nguồn, khoảng giá trị, phân phối, lý do và đánh giá khả thi.",
"""Bảng 2 nêu giá trị trung tâm và khoảng của các tham số quyết định kết quả; Phụ lục B liệt kê từng tham số với nguồn, phân phối, lý do và đánh giá khả thi.

**Bảng 2. Các tham số chính của mô hình**

| Tham số | Nguồn | Phân phối | Giá trị hoặc khoảng |
|---|---|---|---|
| Dân số từ 20 tuổi, theo tuổi và ngũ phân vị | Dự báo dân số UN 2024 | Cố định | 81 triệu, phân bố năm 2027 |
| Khối lượng đồ uống chịu thuế | Euromonitor; Điều tra dinh dưỡng toàn quốc 2019–20 | Gamma | 145 mL/ngày (90–220) |
| Tỷ trọng giá xuất xưởng | Không có ước lượng Việt Nam | Tam giác | 0,55 (0,40–0,70) |
| Mức truyền dẫn | Đánh giá tại Mexico, Chile, Barbados, Bồ Đào Nha, Pháp | Tam giác | 0,90 (0,50–1,30) |
| Độ co giãn giá riêng | Phân tích gộp cho nước thu nhập thấp–trung bình và châu Á | Log-chuẩn | −1,20 (−0,80 đến −1,80) |
| Mật độ năng lượng; bù trừ | Bảng thành phần thực phẩm Việt Nam | Cố định; đều | 44 kcal/100 mL; 30% (15–45%) |
| Nguy cơ tương đối BMI–bệnh | Nghiên cứu đoàn hệ châu Á–Thái Bình Dương | Log-chuẩn | 1,55; 1,11; 1,12 mỗi 2 kg/m² |
| Tỷ lệ mắc, tử vong, trọng số | GBD 2021; STEPS 2021 | Beta; gamma | Theo tuổi và giới |
| Chi phí y tế mỗi ca | Các nghiên cứu chi phí bệnh Việt Nam | Gamma | 8,0 / 84,9 / 10,5 triệu đồng |
| Chi tiêu hộ theo ngũ phân vị | VHLSS 2024 | Cố định; log-chuẩn | 3,0 triệu đồng; Q5/Q1 = 3,1 |""")

# --- baseline cost wording
rep("khởi tạo tồn lưu từ GBD 2021 làm chi phí nền tăng từ 203.411 tỷ đồng lên 574.378 tỷ đồng và giảm lợi ích tránh được 8,6% cùng chi phí tránh được 8,1%",
"khởi tạo tồn lưu từ GBD 2021 làm chi phí y tế đã chiết khấu của kịch bản không thuế giai đoạn 2027–2050 tăng từ 203.411 tỷ đồng lên 574.378 tỷ đồng và giảm lợi ích tránh được 8,6% cùng chi phí tránh được 8,1%")

# --- abstract: both gradient directions
rep("khi không có gradient, lợi ích nghiêng nhẹ về phía khá giả; với một gradient hợp lý, lợi ích gần như tỷ lệ thuận.",
"khi không có gradient, lợi ích nghiêng về phía khá giả; gần tỷ lệ thuận khi nguy cơ giảm theo chi tiêu, và nghiêng mạnh nhất về phía khá giả khi nguy cơ tăng theo chi tiêu.")

# --- abstract methods: scenarios and discounting
rep("liên kết thuế suất qua giá, cầu, năng lượng nạp vào và chỉ số khối cơ thể đến tỷ lệ mắc đái tháo đường type 2, bệnh tim thiếu máu cục bộ và đột quỵ.",
"liên kết thuế suất qua giá, cầu, năng lượng nạp vào và chỉ số khối cơ thể đến tỷ lệ mắc đái tháo đường type 2, bệnh tim thiếu máu cục bộ và đột quỵ. Chúng tôi so sánh bốn kịch bản — không thuế, thuế như đã ban hành, tăng giá 20% và thuế kèm tái định lượng — với bất định lan truyền qua 5.000 lần lặp và kết cục chiết khấu 3%/năm.")

open(p, "w", encoding="utf-8").write(s)
print("VI aligned")
