# -*- coding: utf-8 -*-
p = "Ban_thao_Tieng_Viet.md"
s = open(p, encoding="utf-8").read()
i = s.index("## Phương pháp")
j = s.index("### Giá và tiêu thụ")
new = """## Phương pháp

### Thiết kế và tổng quan

Chúng tôi xây dựng mô hình đa trạng thái tỷ lệ cho tỷ lệ mắc và tỷ lệ hiện mắc bệnh ở dân số Việt Nam từ 20 tuổi trở lên, phân tầng theo tuổi từng năm (20 đến 100+) và ngũ phân vị chi tiêu hộ. Đầu vào dịch tễ được lấy riêng cho nam và nữ rồi gộp lại theo trọng số dân số, vì các trạng thái bệnh trong mô hình không phân biệt giới. Cùng một tỷ lệ mắc và tỷ lệ tử vong nền được áp cho mọi tầng, với điều chỉnh theo tầng qua phân suất tác động quần thể. Quần thể là một tồn lượng theo tuổi cố định ở phân bố Dự báo dân số UN năm 2027, và mỗi chu kỳ năm áp tỷ lệ mắc theo tuổi cho nhóm khỏe mạnh cùng tỷ lệ tử vong nền cộng tử vong ca bệnh cho từng trạng thái. Cá thể không được làm già đi giữa các chu kỳ và không áp hiệu chỉnh nửa chu kỳ, nên mô hình là mô hình mắc–hiện mắc có trọng số sống còn chứ không phải bảng sống theo thuần tập, và quá trình già hóa dân số giai đoạn 2027–2050 không được phản ánh; các khung vì vậy được nêu theo năm lịch (2036, 2050, hoặc khung mở rộng đến 2100), không phải tuổi thọ của thuần tập 2027.

Chi phí được đánh giá theo quan điểm hệ thống y tế, phân bố theo quan điểm hộ gia đình, và doanh thu theo quan điểm chính phủ. Chi phí và kết cục được chiết khấu 3%/năm, với 0% và 5% trong phân tích độ nhạy, và báo cáo bằng đồng Việt Nam năm 2026 quy đổi 24.165 VND/USD. Phân tích dùng R 4.6.1.

### Các kịch bản chính sách

Bốn kịch bản được mô hình hóa (Bảng 1). S0 là không thuế. S1 là thuế như đã ban hành: 8% từ 2027 và 10% từ 2028 cho đồ uống trên ngưỡng luật định, với các trường hợp loại trừ theo luật, đánh trên giá xuất xưởng. S2 là mức tăng giá bán lẻ 20%, mốc tham chiếu của WHO. S3 áp thuế suất đã ban hành trong khi 10%, 25% hoặc 50% sản phẩm gần ngưỡng tái định lượng xuống dưới 5 g đường/100 mL; các sản phẩm đó ra khỏi cơ sở thuế, không chịu thay đổi giá, và mật độ đường giảm từ 6,5 xuống 4,5 g/100 mL, nên mức thay đổi giá và tiêu thụ báo cáo cho S3 là trung bình trên cả nhóm chịu thuế. Mức truyền dẫn được xử lý như tham số độ nhạy chứ không phải kịch bản, vì bằng chứng Việt Nam chưa có.

**Bảng 1. Các kịch bản chính sách**

| Mã | Kịch bản | Đặc tả | Vai trò |
|---|---|---|---|
| S0 | Không thuế | Xu hướng tiêu thụ nền 2027–2050 | Phản thực tế |
| S1 | Thuế như đã ban hành | 8% (2027), 10% (2028 trở đi); >5 g/100 mL; cơ sở xuất xưởng; tầng VAT 10%; loại trừ theo luật | Chính sách cần đánh giá |
| S2 | Mốc tham chiếu WHO | Tăng giá bán lẻ 20% cho đồ uống chịu thuế từ 2027 | Tham chiếu |
| S3 | Thuế đã ban hành kèm tái định lượng | 10%, 25%, 50% sản phẩm gần ngưỡng tái định lượng xuống dưới 5 g/100 mL | Phản ứng của ngành |

### Cấu trúc mô hình

**Giá.** Mức thay đổi giá bán lẻ tỷ lệ là ΔP/P = τ(P_sx/P_bl)(1+v)κ, trong đó τ là thuế suất theo giá, P_sx/P_bl là tỷ trọng giá xuất xưởng trong giá bán lẻ đã gồm VAT, v là thuế suất giá trị gia tăng và κ là mức truyền dẫn. Thừa số (1+v) phản ánh VAT đánh trên thuế tiêu thụ đặc biệt, làm thuế suất danh nghĩa tăng thêm một phần mười.[9,10,12]

**Cầu.** Thay đổi tiêu thụ tỷ lệ của nhóm j là ε_jj(ΔP_j/P_j) + Σ_k ε_jk(ΔP_k/P_k). Độ co giãn giá riêng khác nhau theo ngũ phân vị khi có bằng chứng, vì độ co giãn lớn hơn ở các hộ thu nhập thấp.[17] Độ co giãn giá chéo sang đồ uống không chịu thuế được dùng để báo cáo mức thay thế[18] nhưng không cộng thêm như một số hạng dương riêng, vì độ co giãn giá riêng đã bao hàm thay thế và cộng cả hai là đếm trùng.[15] Đồ uống chịu thuế được mô hình hóa thành một nhóm với mật độ đường trung bình 11 g/100 mL.[14]

**Năng lượng và cân nặng.** Thay đổi năng lượng bằng thay đổi lượng nhân mật độ năng lượng (44 kcal/100 mL) trừ đi phần bù trừ cho năng lượng bị thay thế, mô hình hóa ở mức 30% (khoảng 15–45%); đây là giả định (Phụ lục B). Thay đổi năng lượng được chuyển thành thay đổi BMI bằng mô hình cân nặng động có tính đến chi phí năng lượng duy trì cân nặng giảm dần khi BMI tăng,[19] và thay đổi BMI được chuyển thành thay đổi tỷ lệ mắc qua phân suất tác động quần thể với nguy cơ tương đối trên mỗi 2 kg/m² từ Nghiên cứu đoàn hệ châu Á–Thái Bình Dương,[20,21] kèm độ trễ hai năm.

**Trạng thái bệnh, chi phí và doanh thu.** Mỗi ngũ phân vị có một trạng thái khỏe mạnh và ba trạng thái bệnh. Mỗi chu kỳ, tỷ lệ mắc chuyển người từ trạng thái khỏe mạnh sang bệnh, tử vong nền áp cho nhóm khỏe mạnh, và tử vong nền cộng tử vong ca bệnh áp cho từng trạng thái; đồng mắc là cộng gộp và ca bệnh được đếm ở lần khởi phát đầu tiên. Chi phí đái tháo đường áp theo ca hiện mắc mỗi năm, còn chi phí bệnh tim thiếu máu cục bộ và đột quỵ được phân bổ từ các nghiên cứu đợt cấp.[22,23,24,25] DALY là tổng số năm sống mất đi từ mức tử vong của mô hình và số năm sống với khuyết tật từ tỷ lệ hiện mắc nhân trọng số khuyết tật.[26] Doanh thu là lượng chịu thuế nhân giá bán lẻ, tỷ trọng xuất xưởng và thuế suất hàm ý, tích lũy 2027–2050 với cùng suất chiết khấu như DALY.

### Nguồn tham số

Phụ lục B liệt kê từng tham số với nguồn, khoảng giá trị, phân phối, lý do và đánh giá khả thi. Hai tham số mang phần lớn bất định: tỷ trọng giá xuất xưởng, chưa có ước lượng Việt Nam, và mức truyền dẫn, dao động từ dưới 50% đến gần 100% trong các đánh giá.[27,28,29]

### Phân tích công bằng

Mô hình chạy riêng cho từng ngũ phân vị với tiêu thụ và độ co giãn đặc thù. Tỷ lệ bệnh quốc gia được áp cho mọi ngũ phân vị ở kịch bản cơ sở, để khác biệt về lợi ích sức khỏe chỉ phát sinh từ tiêu thụ và phản ứng giá; toàn bộ phân tích sau đó được lặp lại với gradient theo từng chiều. Bốn đầu ra được báo cáo: DALY tránh được trên 1.000 dân ở từng nhóm; thuế phải trả theo tỷ lệ chi tiêu hộ; chỉ số Kakwani, tính bằng chỉ số tập trung của khoản thuế tuyệt đối trừ Gini chi tiêu hộ; và giá trị tương đương đã điều chỉnh bất bình đẳng của lợi ích trên đầu người ở mức e ngại 1, 3 và 10. Vì mô hình cho kết cục ở cấp ngũ phân vị, các thước đo dựa trên Atkinson là xấp xỉ trong nội bộ nhóm.

### Bất định và phân tích độ nhạy

Bất định tham số được lan truyền bằng mô phỏng Monte Carlo 5.000 lần, lấy mẫu độc lập từ các phân phối ở Phụ lục B và báo cáo trung vị kèm khoảng bất định 95%. Bất định cấu trúc được khảo sát bằng các lần chạy một chiều ở giá trị trung tâm cho suất chiết khấu (0% và 5%), mức truyền dẫn (0,50; 0,90 và 1,30), độ co giãn giá riêng (−0,80; −1,20 và −1,80) và khung phân tích (2036, 2050 và 2100), cùng lưới hai chiều trên tỷ trọng giá xuất xưởng (0,30 đến 0,85) và mức truyền dẫn (0,30 đến 1,50). Phân bố lợi ích sức khỏe được tính lại dưới ba giả định về gradient nguy cơ bệnh nền: không có gradient, nguy cơ giảm theo chi tiêu, và nguy cơ tăng theo chi tiêu.

### Thẩm định

Mỗi bước của mô hình có kiểm thử đơn vị với đầu vào và đầu ra tính tay; bảo toàn dân số được kiểm tra ở mọi chu kỳ, và điều kiện cực biên được kiểm tra với thuế bằng không và độ co giãn bằng không. Tỷ lệ hiện mắc nền được so sánh với GBD 2021 và STEPS 2021. Hai kiểm tra đã không được thực hiện: so sánh ngoại với nghiên cứu mô hình hóa Việt Nam trước đó,[14] và rà soát mã bởi người độc lập. Phụ lục E ghi lại những gì đã và chưa được kiểm tra.

### Báo cáo, đăng ký và đạo đức

Nghiên cứu được báo cáo theo CHEERS 2022, với danh mục kiểm tra ở Phụ lục D.[30] Protocol và kế hoạch phân tích được lưu cùng mã tại https://doi.org/10.5281/zenodo.23852908, và các sai lệch so với kế hoạch soạn ban đầu được ghi ở Phụ lục C. Không thu thập dữ liệu người tham gia và không cần phê duyệt đạo đức.

"""
s = s[:i] + new + s[j:]
open(p, "w", encoding="utf-8").write(s)
print("VI methods rewritten")
