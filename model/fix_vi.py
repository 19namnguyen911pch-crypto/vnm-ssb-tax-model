# -*- coding: utf-8 -*-
"""Mirror the structural fixes into the Vietnamese version."""
import re

p = "Ban_thao_Tieng_Viet.md"
s = open(p, encoding="utf-8").read()

C_NEW = """## Phụ lục C. Sai lệch so với kế hoạch soạn ban đầu

Protocol và kế hoạch phân tích được lưu cùng mã sau khi mô hình đã chạy. Phụ lục này ghi lại mọi sai lệch so với kế hoạch soạn ban đầu để người đọc thấy điều gì đã thay đổi và vì sao. Có năm sai lệch.

| # | Sai lệch | Lý do |
|---|---|---|
| C1 | Bỏ kịch bản thuế theo gam đường cân bằng doanh thu (S1b) | Phân bổ sản lượng chịu thuế theo các dải đường cần cơ sở dữ liệu cấp sản phẩm không tồn tại ở Việt Nam; thiếu nó, kịch bản quy về cùng mức tăng giá bình quân với thuế đã ban hành và không phân biệt được |
| C2 | Không giả định gradient kinh tế–xã hội trong tỷ lệ mắc nền | Không có tỷ lệ mắc và tử vong theo ngũ phân vị cho Việt Nam; tỷ lệ quốc gia được áp cho mọi nhóm |
| C3 | Không thực hiện kiểm toán sản phẩm | Tỷ trọng đồ uống chịu thuế trên ngưỡng là giả định (Phụ lục B, #4), không phải số đo |
| C4 | Chi phí y tế cho tim thiếu máu cục bộ và đột quỵ được phân bổ từ nghiên cứu đợt cấp | Không có ước lượng Việt Nam về chi phí năm trên mỗi ca hiện mắc cho hai bệnh này |
| C5 | Độ trễ là dịch chuyển hai năm của phân suất tác động, không phải phân bố độ trễ | Không có bằng chứng Việt Nam về hình dạng độ trễ; bước nhảy là lựa chọn thận trọng |

Hai điểm nữa ảnh hưởng đến cách đọc kết quả công bằng. Gradient độ co giãn giữa các ngũ phân vị (Phụ lục B, #7c) là giả định, không phải số đo; và chỉ số tập trung cùng Kakwani dùng Gini tính từ giá trị trung bình các nhóm, tức là cận dưới của bất bình đẳng thực.

"""

E_NEW = """## Phụ lục E. Những gì đã và chưa được thẩm định

**E.1 Đã kiểm tra.** Mỗi bước của mô hình có kiểm thử đơn vị với đầu vào và đầu ra tính tay. Bảo toàn dân số được kiểm tra trong bảng sống: không ai rời quần thể ngoài đường tử vong, và số còn sống cộng số đã chết bằng dân số ban đầu ở mọi chu kỳ. Điều kiện cực biên được kiểm tra: thuế bằng không trả về đúng kịch bản nền, độ co giãn bằng không trả về đúng kịch bản nền, và một mức thuế đủ lớn để triệt tiêu tiêu thụ không tạo ra lượng âm hay lỗi chia.

**E.2 Chưa kiểm tra.** Ba kiểm tra dự kiến đã không được thực hiện và bài không tuyên bố chúng. Tỷ lệ hiện mắc nền của mô hình chưa được đối chiếu với GBD hoặc STEPS, vì bảng sống không làm quần thể già đi nên so sánh mức sẽ không có ý nghĩa. Không có so sánh ngoại với nghiên cứu mô hình hóa Việt Nam trước đó,[10] vì nghiên cứu đó báo cáo kết cục khác trên cấu trúc khác. Mã chưa được một lập trình viên độc lập rà soát. Các kiểm thử đơn vị và điều kiện cực biên ở E.1 là toàn bộ bảo đảm kỹ thuật phía sau kết quả.

"""

F_NEW = """## Phụ lục F. Các phân tích độ nhạy đã thực hiện

**F.1 Phân tích xác suất.** 5.000 lần mô phỏng Monte Carlo, lấy mẫu độc lập từ các phân phối ở Phụ lục B, hạt giống cố định (20261101), báo cáo trung vị và khoảng bất định 95%.

**F.2 Phân tích ngưỡng.** Lưới trên tỷ trọng giá xuất xưởng (0,30 đến 0,85) và mức truyền dẫn (0,30 đến 1,50), mô hình chạy lại tại từng điểm, xác định các tổ hợp mà tại đó lợi ích sức khỏe không phân biệt được với không. Lưới được lưu ở `output/threshold_grid.csv`.

**F.3 Lưới độ co giãn.** Độ co giãn giá riêng từ −0,3 đến −2,0 theo bước 0,1, các tham số khác giữ ở trung tâm, để xác định điểm mà lợi ích sức khỏe đổi dấu.

**F.4 Biến thể cơ sở thuế.** Tỷ trọng đồ uống chịu thuế đặt ở 0,60 và 0,95, bao quanh giá trị giả định 0,80.

**F.5 Tái định lượng.** S3 chạy ở mức 25% tại trung tâm; các mức 10% và 50% được báo cáo trong bài.

**F.6 Các phân tích không thực hiện.** Mô hình cân nặng tĩnh, bộ độ co giãn thấp và cao, lưới truyền dẫn đầy đủ kết hợp diễn giải rộng và hẹp phạm vi chịu thuế, và độ trễ phân bố đã được dự kiến và không thực hiện. Không kết quả nào của chúng được báo cáo.

"""

# Table 2 rows
s = s.replace("| Mức truyền dẫn | Đánh giá tại Mexico, Philippines, Thái Lan, Chile, Barbados [19] | Tam giác | 0,5–1,5 |",
              "| Mức truyền dẫn | Đánh giá tại Mexico, Philippines, Chile, Barbados [19] | Tam giác | 0,50–0,90–1,30 |")
s = s.replace("| Dân số theo tuổi và ngũ phân vị, 2027–2050 | Dự báo của Tổng cục Thống kê [18] | Cố định | 104 triệu (2027), 110 triệu (2050) |",
              "| Dân số từ 20 tuổi, theo tuổi và ngũ phân vị, 2027–2050 | Dự báo dân số UN 2024 [18] | Cố định | 81 triệu (2027), 86 triệu (2050) |")
s = s.replace("| Tỷ trọng sản phẩm trên 5 g/100 mL | Kiểm toán sản phẩm, 11–12/2026 (Phụ lục C) | Beta | 0,80 |",
              "| Tỷ trọng đồ uống chịu thuế trên 5 g/100 mL | Giả định; cơ cấu nhóm từ [10] | Beta | 0,80 |")
s = s.replace("| 4 | Tỷ trọng sản phẩm trên 5 g/100 mL | 0,80 | 0,60 đến 0,95 | Beta(8;2) | Kiểm toán sản phẩm (Phụ lục C) | Sơ cấp | Có |",
              "| 4 | Tỷ trọng đồ uống chịu thuế trên 5 g/100 mL | 0,80 | 0,60 đến 0,95 | Beta(8;2) | Giả định; không đo | Giả định | Không |")

# delete the product-audit appendix and renumber
i = s.index("## Phụ lục C. Protocol kiểm toán sản phẩm")
j = s.index("## Phụ lục D. Nhật ký sai lệch")
s = s[:i] + s[j:]
mapping = {"D": "C", "E": "D", "F": "E", "G": "F", "H": "G"}
s = re.sub(r"Phụ lục ([D-H])\b", lambda m: "Phụ lục " + mapping[m.group(1)], s)

s = s.replace("## Phụ lục C. Nhật ký sai lệch", "## Phụ lục C. Sai lệch so với kế hoạch soạn ban đầu")
s = s.replace("## Phụ lục E. Kế hoạch kiểm chứng", "## Phụ lục E. Những gì đã và chưa được thẩm định")
s = s.replace("## Phụ lục F. Kế hoạch phân tích độ nhạy", "## Phụ lục F. Các phân tích độ nhạy đã thực hiện")

def swap(s, start, end, new):
    i = s.index(start); j = s.index(end, i)
    return s[:i] + new + s[j:]
s = swap(s, "## Phụ lục C. Sai lệch", "## Phụ lục D. Danh mục", C_NEW)
s = swap(s, "## Phụ lục E. Những gì đã và chưa", "## Phụ lục F. Các phân tích", E_NEW)
s = swap(s, "## Phụ lục F. Các phân tích độ nhạy đã thực hiện", "## Phụ lục G. Mã", F_NEW)

# validation claims
s = s.replace(" Thẩm định bên trong yêu cầu mô hình tái tạo tỷ lệ mắc, tỷ lệ hiện mắc và tử vong nền của Việt Nam đã công bố trong sai số 15%. Thẩm định bên ngoài so sánh kết quả của chúng tôi ở mức tăng giá 20% với kết quả của Nguyễn và cộng sự,[10] và mọi khác biệt đáng kể được giải thích.",
              " Ba kiểm tra dự kiến đã không được thực hiện: tái tạo tỷ lệ hiện mắc từ GBD hoặc STEPS, so sánh ngoại với nghiên cứu mô hình hóa Việt Nam trước đó,[10], và rà soát mã bởi người độc lập. Phụ lục E ghi lại những gì đã và chưa được kiểm tra, và bài không tuyên bố những điều chưa làm.")
s = re.sub(r"Một người đọc mã độc lập ngoài nhóm đã rà soát mã[^.]*\.\s*", "", s)
s = re.sub(r"Kết quả nền tái tạo tỷ lệ mắc[^\n]*\n", "", s)

# conclusion duplication
i = s.index("**Kết luận.**")
j = s.index("\n", i)
s = s[:i] + "**Kết luận.** Thuế tiêu thụ đặc biệt đồ uống có đường của Việt Nam như đã ban hành sẽ tạo ra lợi ích sức khỏe có thật nhưng nhỏ, được huy động theo cách lũy thoái, và chỉ tương đương khoảng một phần tư tín hiệu giá mà WHO khuyến nghị; kỳ rà soát 2028 là nơi có thể thu hẹp khoảng cách đó." + s[j:]

s = s.replace("tăng 350%", "tăng gần bốn lần")
s = s.replace("và qua tác động không phụ thuộc cân nặng của đường lỏng hấp thu nhanh lên đề kháng insulin, ", "chủ yếu qua tăng cân, ")

open(p, "w", encoding="utf-8").write(s)
print([l for l in s.split("\n") if l.startswith("## Phụ lục")])
