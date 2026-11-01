# -*- coding: utf-8 -*-
p = "Ban_thao_Tieng_Viet.md"
s = open(p, encoding="utf-8").read()
i = s.index("## Giới thiệu")
j = s.index("## Phương pháp")
new = """## Giới thiệu

Bệnh không lây nhiễm chiếm hơn 80% số ca tử vong tại Việt Nam, tỷ lệ thừa cân ở người trưởng thành tăng từ 15,6% năm 2015 lên 19,5% năm 2021, và đến năm 2021 có 7,3% nam và 6,9% nữ có đường huyết tăng hoặc đang dùng thuốc điều trị đái tháo đường.[2] Đồ uống có đường góp phần chủ yếu qua tăng cân, và là nguồn đường bổ sung trong khẩu phần nhạy cảm nhất với giá. Tiêu thụ nước ngọt — nhóm rộng hơn nhóm đồ uống chịu thuế — tăng từ 18 lít/người năm 2009 lên 66 lít năm 2023, một trong những mức tăng nhanh nhất khu vực Tây Thái Bình Dương.[3] Thuế là can thiệp có nền bằng chứng mạnh nhất để giảm lượng đường nạp vào,[4] mức tăng giá 20% có thể giảm tiêu thụ khoảng 20%,[5] và WHO khuyến nghị ít nhất mức đó.[6] Đến 2024, 64 quốc gia đã áp thuế đồ uống có đường, nhưng chỉ 5% đánh theo hàm lượng đường,[7] và so sánh giữa các nước khó khăn vì cơ sở thuế và điểm đánh thuế khác nhau.[8]

Ngày 14/6/2025, Quốc hội Việt Nam thông qua Luật số 66/2025/QH15, lần đầu đưa đồ uống không cồn có trên 5 g đường/100 mL vào diện chịu thuế tiêu thụ đặc biệt.[9] Thuế suất là 0% năm 2026, 8% từ tháng 1/2027 và 10% từ tháng 1/2028.[9,10] Hàm lượng đường là tổng đường ghi trên nhãn dinh dưỡng, và giá tính thuế là giá bán của nhà sản xuất hoặc nhà nhập khẩu chưa gồm thuế giá trị gia tăng và thuế tiêu thụ đặc biệt;[10,11] thuế giá trị gia tăng 10% sau đó áp trên giá đã gồm thuế tiêu thụ đặc biệt, nên thuế đến tay người tiêu dùng qua một tầng cộng dồn.[12] Nhóm chịu thuế được xác định theo tiêu chuẩn quốc gia về nước giải khát TCVN 12828:2019, với các trường hợp loại trừ mang tính định nghĩa chứ không liệt kê, và ranh giới giữa nước ép trái cây và đồ uống có chứa nước ép — cùng vị thế của nước dừa — chưa rõ ràng về mặt pháp lý.[11,13]

Ba câu hỏi được đặt ra. Thứ nhất, thuế suất theo giá trên cơ sở xuất xưởng không đồng nghĩa với thay đổi giá bán lẻ: mức thay đổi đến tay người tiêu dùng chỉ là một phần của thuế suất danh nghĩa, và lợi ích sức khỏe tỷ lệ với mức thay đổi đó, không phải với thuế suất. Thứ hai, chưa rõ gánh nặng chi trả có rơi không cân xứng vào các hộ nghèo hơn hay không, cũng chưa rõ tính lũy thoái đó có được bù đắp bởi phân bố lợi ích sức khỏe hay không. Thứ ba, luật quy định rà soát năm 2028, khi lựa chọn giữa thuế suất theo giá cao hơn và thuế theo gam đường sẽ được xem xét. Mô hình hóa trước đây cho Việt Nam khảo sát các mức thuế giả định trước khi luật được thông qua và tập trung vào cân nặng và đái tháo đường;[14] một phân tích sau đó mô phỏng thiết kế đã ban hành trên dữ liệu khảo sát hộ nhưng không tách được đồ uống có đường khỏi các đồ uống không cồn khác và không mô hình hóa bệnh.[15] Cả hai đều không báo cáo lợi ích sức khỏe và thuế phải trả trên cùng một thang công bằng.

Vì vậy chúng tôi ước tính, cho thuế như đã ban hành, thay đổi giá bán lẻ và tiêu thụ, số DALY và số ca đái tháo đường type 2, bệnh tim thiếu máu cục bộ và đột quỵ tránh được, chi phí y tế tiết kiệm và doanh thu thu được, cùng phân bố của các lợi ích và khoản chi trả này theo ngũ phân vị chi tiêu hộ, so sánh thiết kế đã ban hành với mức tăng giá bán lẻ 20% và với việc ngành tái định lượng sản phẩm.

"""
s = s[:i] + new + s[j:]
open(p, "w", encoding="utf-8").write(s)
print("VI introduction rewritten")
