# -*- coding: utf-8 -*-
"""Final pass: tighter abstract, explicit search and screening procedure."""
import re

EN_ABS = """## Summary

**Background**
Viet Nam legislated its first excise tax on sugar-sweetened beverages in June 2025: 8% from January 2027 and 10% from January 2028 on drinks containing more than 5 g of sugar per 100 mL. Per-capita consumption rose from 18 L in 2009 to 66 L in 2023, and non-communicable diseases cause more than 80% of deaths. The effects of the tax have not been quantified.

**Methods**
We built a proportional multi-state life-table model of the Vietnamese population aged 20 years and older, stratified by age and household expenditure quintile, linking the statutory rate to the retail price through the ex-factory base and the value-added tax cascade, price to demand, demand to energy intake, energy to body-mass index, and BMI to the incidence of type 2 diabetes, ischaemic heart disease, and stroke. We compared four scenarios: no tax, the tax as enacted, a 20% retail price increase (the WHO benchmark), and the enacted tax with industry reformulation. Uncertainty was propagated through 5,000 Monte Carlo iterations; outcomes were discounted at 3% per year.

**Findings**
The enacted tax would raise the retail price of taxed beverages by 4.36% in 2027 and 5.45% in 2028, reducing consumption by 9.6 mL per person per day. Over 2027–2050 it would avert 24 767 DALYs (95% uncertainty interval 9956–53 043) and 32 625 cases of type 2 diabetes, ischaemic heart disease, and stroke, save VND 1500 billion in health-care costs, and raise VND 2731 billion in revenue. DALYs averted per 1000 population were 0.27 in the poorest quintile and 0.35 in the richest; tax payments were 0.133% and 0.079% of household expenditure. A 20% price increase would avert 89 991 DALYs, 3.6 times as many.

**Interpretation**
Because the excise is levied on an ex-factory base and cascaded through value-added tax, the enacted rates produce a retail price increase about a quarter of the WHO benchmark, and a proportionally small health gain. The financing burden is regressive, and without a measured gradient in disease risk the health benefit also accrues disproportionately to better-off households. The 2028 review is the decisive opportunity.

**Funding**
No specific funding.

---

"""

VI_ABS = """## Tóm tắt

**Bối cảnh**
Tháng 6/2025, Việt Nam lần đầu ban hành thuế tiêu thụ đặc biệt đối với đồ uống có đường: 8% từ tháng 1/2027 và 10% từ tháng 1/2028 đối với đồ uống có trên 5 g đường/100 mL. Tiêu thụ bình quân đầu người tăng từ 18 lít năm 2009 lên 66 lít năm 2023, và bệnh không lây nhiễm gây hơn 80% số ca tử vong. Tác động của thuế chưa được định lượng.

**Phương pháp**
Chúng tôi xây dựng mô hình bảng sống đa trạng thái tỷ lệ cho dân số Việt Nam từ 20 tuổi trở lên, phân tầng theo tuổi và ngũ phân vị chi tiêu hộ, nối thuế suất với giá bán lẻ qua cơ sở xuất xưởng và tầng thuế giá trị gia tăng; giá với cầu; cầu với năng lượng nạp vào; năng lượng với chỉ số khối cơ thể; và BMI với tỷ lệ mắc đái tháo đường type 2, bệnh tim thiếu máu cục bộ và đột quỵ. Bốn kịch bản được so sánh: không thuế, thuế đã ban hành, tăng giá bán lẻ 20% (mốc của WHO), và thuế đã ban hành kèm giảm đường. Bất định được lan truyền qua 5.000 lần mô phỏng Monte Carlo; kết cục chiết khấu 3%/năm.

**Kết quả**
Thuế đã ban hành sẽ làm giá bán lẻ đồ uống chịu thuế tăng 4,36% năm 2027 và 5,45% năm 2028, làm tiêu thụ giảm 9,6 mL/người/ngày. Giai đoạn 2027–2050, thuế tránh được 24.767 DALY (khoảng bất định 95%: 9.956–53.043) và 32.625 ca đái tháo đường type 2, bệnh tim thiếu máu cục bộ, đột quỵ, tiết kiệm 1.500 tỷ đồng chi phí y tế và tạo 2.731 tỷ đồng doanh thu. DALY tránh được trên 1.000 dân là 0,27 ở nhóm nghèo nhất và 0,35 ở nhóm giàu nhất; thuế phải trả tương ứng 0,133% và 0,079% chi tiêu hộ. Tăng giá 20% tránh được 89.991 DALY, gấp 3,6 lần.

**Diễn giải**
Vì thuế đánh trên cơ sở xuất xưởng và chịu tầng thuế giá trị gia tăng, các mức thuế đã ban hành chỉ tạo ra mức tăng giá bán lẻ khoảng một phần tư mốc WHO khuyến nghị, và lợi ích sức khỏe nhỏ tương ứng. Gánh nặng chi trả là lũy thoái, và khi thiếu một gradient nguy cơ bệnh đo được thì lợi ích sức khỏe cũng rơi nhiều hơn vào các hộ khá giả. Kỳ rà soát 2028 là cơ hội quyết định.

**Tài trợ**
Không có tài trợ riêng.

---

"""

EN_A5 = """**A.5 Screening procedure**

1. Each database was searched on 1 November 2026 with the strings in A.3 and the results exported in full to a reference manager.
2. Records were de-duplicated in two passes: by DOI where one was present, and otherwise by normalised title (lower case, diacritics removed, punctuation stripped).
3. Titles and abstracts were screened against the eligibility criteria in A.4. Every record was retained or excluded with a recorded reason; no record was dropped silently.
4. The full text of every retained record was obtained and checked against the same criteria.
5. A second reader checked every proposed exclusion, and disagreements were resolved by discussion. A formal inter-rater kappa was not computed, because the number of records requiring a decision was small.
6. The outcome of every step is recorded at record level in `data/screening_log.csv`, which is deposited with the protocol and reproduced in the supplementary material.

"""

VI_A5 = """**A.5 Quy trình sàng lọc**

1. Mỗi cơ sở dữ liệu được tìm ngày 1/11/2026 bằng chuỗi ở A.3 và kết quả được xuất toàn bộ sang phần mềm quản lý tài liệu tham khảo.
2. Bản ghi được loại trùng theo hai lượt: theo DOI nếu có, nếu không thì theo tiêu đề đã chuẩn hóa (chữ thường, bỏ dấu, bỏ dấu câu).
3. Tiêu đề và tóm tắt được sàng lọc theo tiêu chí ở A.4. Mọi bản ghi đều được giữ lại hoặc loại kèm lý do ghi nhận; không bản ghi nào bị bỏ im lặng.
4. Toàn văn của mọi bản ghi được giữ lại đều được lấy về và đối chiếu với cùng tiêu chí.
5. Một người đọc thứ hai kiểm tra mọi đề xuất loại, bất đồng được giải quyết bằng thảo luận. Hệ số kappa không được tính vì số bản ghi cần quyết định nhỏ.
6. Kết quả từng bước được ghi ở cấp bản ghi trong `data/screening_log.csv`, tệp này được nộp cùng protocol và in lại trong tài liệu bổ sung.

"""

EN_A6 = """**A.6 Flow**

| Stage | PubMed | Europe PMC | OpenAlex | Scopus | Cochrane | RePEc | Total |
|---|---|---|---|---|---|---|---|
| Identified, country-limited set | 2 | 3 | 11 | 6 | 3 | 0 | **25** |
| Removed as duplicates | | | | | | | 11 |
| Unique records screened | | | | | | | **14** |
| Excluded at screening | | | | | | | 6 |
| Included | | | | | | | **8** |

Eight records were included: two quantitative analyses that model SSB taxation in Viet Nam; one distributional analysis of the 2025 design using household survey data; one empirical study of excise effects on beverage consumption; one human-rights assessment of the enacted tax; one study of public acceptability; one regional analysis of the distributional impacts of health taxes; and one Cochrane systematic review of environmental interventions to reduce SSB consumption.

Six were excluded. A 1997 dental review of sugar consumption trends is not about taxation; a historical article on Lyndon Johnson was retrieved by the country term as a false positive; an urban food-systems paper and a study of food marketing to children report no SSB-tax estimate; and a peer-led dietary education trial and a caries prevalence study mention Viet Nam but contain no tax exposure.

The broad sets without a country limit returned 576 records in PubMed, 506 in Europe PMC, 2,961 in OpenAlex, 1,526 in Cochrane CENTRAL and 21 in RePEc. These were used to source parameter values — price elasticities, pass-through, relative risks and cost estimates — rather than screened record by record, because the study needs estimates from any comparable setting rather than a systematic review of tax effects.

Two features of this flow are themselves findings. The yield of the country-limited searches is very small: fourteen unique records for the whole Vietnamese literature on SSB taxation, of which eight are relevant. And the 1997 dental review is retrieved by every database because it names Viet Nam in a list of countries with rising sugar consumption — a reminder that country-term searches in this field are noisy.

"""

VI_A6 = """**A.6 Sơ đồ dòng**

| Giai đoạn | PubMed | Europe PMC | OpenAlex | Scopus | Cochrane | RePEc | Tổng |
|---|---|---|---|---|---|---|---|
| Xác định được, tập giới hạn quốc gia | 2 | 3 | 11 | 6 | 3 | 0 | **25** |
| Loại do trùng lặp | | | | | | | 11 |
| Bản ghi duy nhất được sàng lọc | | | | | | | **14** |
| Loại khi sàng lọc | | | | | | | 6 |
| Đưa vào | | | | | | | **8** |

Tám bản ghi được đưa vào: hai phân tích định lượng mô hình hóa thuế đồ uống có đường tại Việt Nam; một phân tích phân bố của thiết kế 2025 dùng dữ liệu khảo sát hộ; một nghiên cứu thực nghiệm về tác động của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống; một đánh giá nhân quyền về thuế đã ban hành; một nghiên cứu về mức chấp nhận của công chúng; một phân tích khu vực về tác động phân bố của thuế sức khỏe; và một tổng quan hệ thống Cochrane về các can thiệp môi trường nhằm giảm tiêu thụ đồ uống có đường.

Sáu bản ghi bị loại. Một tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường không bàn về thuế; một bài lịch sử về Lyndon Johnson bị từ khóa quốc gia bắt nhầm; một bài về hệ thống thực phẩm đô thị và một nghiên cứu về tiếp thị thực phẩm cho trẻ em không có ước lượng nào về thuế đồ uống có đường; một thử nghiệm giáo dục dinh dưỡng do đồng đẳng dẫn dắt và một nghiên cứu về tỷ lệ sâu răng có nêu Việt Nam nhưng không có phơi nhiễm thuế.

Các tập rộng không giới hạn quốc gia trả về 576 bản ghi ở PubMed, 506 ở Europe PMC, 2.961 ở OpenAlex, 1.526 ở Cochrane CENTRAL và 21 ở RePEc. Các tập này được dùng để lấy giá trị tham số — độ co giãn giá, mức truyền dẫn, nguy cơ tương đối và chi phí — chứ không sàng lọc từng bản ghi, vì nghiên cứu cần ước lượng từ bất kỳ bối cảnh so sánh được nào, không phải một tổng quan hệ thống về tác động của thuế.

Hai đặc điểm của sơ đồ này tự chúng là phát hiện. Năng suất của các tìm kiếm giới hạn quốc gia rất thấp: mười bốn bản ghi duy nhất cho toàn bộ văn liệu Việt Nam về thuế đồ uống có đường, trong đó tám bản ghi có liên quan. Và tổng quan nha khoa 1997 được mọi cơ sở dữ liệu trả về vì nó nêu tên Việt Nam trong danh sách các nước có tiêu thụ đường tăng — một lời nhắc rằng tìm theo từ khóa quốc gia trong lĩnh vực này rất nhiễu.

"""

def apply(path, abs_new, a5_new, a6_new, abs_start, ric_start):
    s = open(path, encoding="utf-8").read()
    i = s.index(abs_start); j = s.index(ric_start)
    s = s[:i] + abs_new + s[j:]
    # replace A.5 and A.6
    i = s.index("**A.5")
    j = s.index("**A.7", i)
    s = s[:i] + a5_new + a6_new + s[j:]
    open(path, "w", encoding="utf-8").write(s)

apply("Manuscript_draft_v1.md", EN_ABS, EN_A5, EN_A6, "## Summary", "## Research in context")
apply("Ban_thao_Tieng_Viet.md", VI_ABS, VI_A5, VI_A6, "## Tóm tắt", "## Bối cảnh nghiên cứu")
print("applied")
