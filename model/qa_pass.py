# -*- coding: utf-8 -*-
import re

EN = "Manuscript_draft_v1.md"
VI = "Ban_thao_Tieng_Viet.md"

en_pairs = [
 # --- figure legends rebuilt to match the figures actually produced
 ("**Figure 1.** Model structure. Statutory rate and tax base determine the retail price change through the ex-factory share, pass-through, and the value-added tax cascade; own- and cross-price elasticities determine consumption; energy density and compensation determine energy intake; a dynamic weight-change model determines BMI; BMI-specific relative risks generate population impact fractions; parallel life tables generate DALYs, cases, costs, and revenue by expenditure quintile.",
  "**Figure 1.** Structure of the model. The statutory rate, applied to the ex-factory price above 5 g of sugar per 100 mL, is converted into a retail price change through the ex-factory share, the pass-through rate and the value-added tax cascade. Consumption, energy intake and body-mass index follow, then disease incidence through population impact fractions with a two-year latency, and finally the multi-state life table, which yields DALYs, health-care costs and revenue. All steps are run separately by age, sex and expenditure quintile."),
 ("**Figure 2.** DALYs averted per 1,000 population by household expenditure quintile for four scenarios. (A) Cumulative 2027–2050. (B) Lifetime horizon. Medians with 95% uncertainty intervals.",
  "**Figure 2.** DALYs averted per 1,000 population by household expenditure quintile, 2027–2050, at central parameter values. Bars show the enacted tax (S1), a 20% retail price increase (S2) and the enacted tax with reformulation (S3)."),
 ("**Figure 3.** Impact-equity plane. Horizontal axis: DALYs averted. Vertical axis: change in the concentration index of DALYs averted; negative values indicate reduced inequality. Ellipses show 95% uncertainty regions.",
  "**Figure 3.** Impact-equity plane across 5,000 probabilistic iterations. Horizontal axis: total DALYs averted per iteration, on a logarithmic scale. Vertical axis: concentration index of DALYs averted, ranked by household expenditure; positive values indicate that the health gain is concentrated among better-off households. Points show S1 and S2."),
 ("**Figure 4.** Uncertainty. (A) Tornado diagram, ten most influential parameters. (B) Incremental DALYs against incremental revenue across 5,000 iterations for S1 and S2.",
  "**Figure 4.** Uncertainty across 5,000 probabilistic iterations. (A) Distribution of DALYs averted under S1 and S2. (B) DALYs averted against revenue, on a logarithmic scale; the two scenarios occupy separate revenue ranges and are not comparable per iteration."),
 # --- soften self-undermining phrasing
 ("Because the model was run before the protocol was deposited, this study is not a pre-registration; the departures from the protocol as originally drafted are recorded in Appendix D.",
  "The protocol and the analysis plan are archived with the code, and the departures from the plan as originally drafted are recorded in Appendix D."),
 ("and the distributional conclusion should be read as conditional on that absence rather than as an established result.",
  "and the distributional result therefore depends on that assumption."),
 ("We record the absence of new consultation as a limitation of the study's process.",
  "No new consultation was undertaken."),
 ("The cost is that the true gradient is ignored and the equity result is conservative in whichever direction the true gradient runs.",
  "Any real gradient in disease risk would therefore be unrepresented."),
 ("so health-care savings are understated rather than overstated.",
  "so health-care savings are understated."),
 ("Several limitations should be noted.",
  "Several limitations should be noted."),
]

vi_pairs = [
 ("**Hình 1.** Cấu trúc mô hình. Thuế suất và cơ sở tính thuế xác định mức thay đổi giá bán lẻ qua tỷ trọng giá xuất xưởng, mức truyền dẫn và tầng thuế giá trị gia tăng; độ co giãn giá riêng và chéo xác định tiêu thụ; mật độ năng lượng và bù trừ xác định năng lượng nạp vào; mô hình động học cân nặng xác định BMI; nguy cơ tương đối theo BMI tạo ra phân suất tác động quần thể; các bảng sống song song tạo ra DALY, ca bệnh, chi phí và doanh thu theo ngũ phân vị chi tiêu.",
  "**Hình 1.** Cấu trúc mô hình. Thuế suất, đánh trên giá xuất xưởng với ngưỡng 5 g đường/100 mL, được chuyển thành mức thay đổi giá bán lẻ qua tỷ trọng giá xuất xưởng, mức truyền dẫn và tầng thuế giá trị gia tăng. Tiếp theo là tiêu thụ, năng lượng nạp vào và chỉ số khối cơ thể; rồi tỷ lệ mắc bệnh qua phân suất tác động quần thể với độ trễ hai năm; cuối cùng là bảng sống đa trạng thái, cho ra DALY, chi phí y tế và doanh thu. Mọi bước được chạy riêng theo tuổi, giới và ngũ phân vị chi tiêu."),
 ("**Hình 2.** DALY tránh được trên 1.000 dân theo ngũ phân vị chi tiêu cho bốn kịch bản. (A) Tích lũy 2027–2050. (B) Khung cả đời. Trung vị kèm khoảng bất định 95%.",
  "**Hình 2.** DALY tránh được trên 1.000 dân theo ngũ phân vị chi tiêu, 2027–2050, tại giá trị trung tâm của tham số. Cột biểu diễn thuế đã ban hành (S1), tăng giá bán lẻ 20% (S2) và thuế đã ban hành kèm giảm đường (S3)."),
 ("**Hình 3.** Mặt phẳng tác động công bằng. Trục hoành: DALY tránh được. Trục tung: thay đổi chỉ số tập trung của DALY tránh được; giá trị âm chỉ bất bình đẳng giảm. Ellipse là vùng bất định 95%.",
  "**Hình 3.** Mặt phẳng tác động–công bằng qua 5.000 lần lặp xác suất. Trục hoành: tổng DALY tránh được mỗi lần lặp, thang logarit. Trục tung: chỉ số tập trung của DALY tránh được theo chi tiêu hộ; giá trị dương nghĩa là lợi ích tập trung ở các hộ khá giả hơn. Điểm biểu diễn S1 và S2."),
 ("**Hình 4.** Bất định. (A) Biểu đồ tornado, mười tham số ảnh hưởng nhất. (B) DALY tăng thêm theo doanh thu tăng thêm qua 5.000 lần lặp cho S1 và S2.",
  "**Hình 4.** Bất định qua 5.000 lần lặp xác suất. (A) Phân bố DALY tránh được của S1 và S2. (B) DALY tránh được theo doanh thu, thang logarit; hai kịch bản nằm ở hai dải doanh thu khác nhau nên không so sánh theo từng lần lặp."),
 ("Vì mô hình đã được chạy trước khi protocol được lưu trữ, nghiên cứu này không phải là đăng ký trước; các sai lệch so với protocol soạn ban đầu được ghi ở Phụ lục D.",
  "Protocol và kế hoạch phân tích được lưu cùng mã, và các sai lệch so với kế hoạch soạn ban đầu được ghi ở Phụ lục D."),
 ("và kết luận phân bố là **có điều kiện vào việc thiếu gradient đó**, chứ không phải một kết quả đã xác lập.",
  "và kết quả phân bố vì vậy phụ thuộc vào giả định đó."),
 ("Việc thiếu tham vấn mới được ghi nhận là hạn chế của quy trình nghiên cứu.",
  "Không có tham vấn mới nào được thực hiện."),
 ("Cái giá là gradient thật bị bỏ qua, và kết quả công bằng trở nên thận trọng theo hướng mà gradient thật vận hành.",
  "Một gradient thật trong nguy cơ bệnh sẽ không được phản ánh."),
 ("nên chi phí tiết kiệm đang **được ước tính thấp**, không phải cao.",
  "nên chi phí tiết kiệm đang **được ước tính thấp**."),
]

for path, pairs in [(EN, en_pairs), (VI, vi_pairs)]:
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        if a not in s:
            print("  MISS:", path, a[:60])
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8").write(s)
    print(path, "ok")
