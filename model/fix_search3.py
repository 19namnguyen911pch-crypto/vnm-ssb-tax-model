# -*- coding: utf-8 -*-
"""Final Appendix A: six sources, real counts, real screening flow."""
import re

EN_A2 = "| OpenAlex | Multidisciplinary, including economics and policy | Captures social-science literature on taxation |\n| Scopus | Multidisciplinary | Economics and policy journals not indexed in MEDLINE |\n"
EN_A2_NEW = EN_A2 + "| Cochrane Library (CDSR and CENTRAL) | Systematic reviews and trials | Reviews of SSB interventions; trial evidence on price and consumption |\n| RePEc/IDEAS | Economics working papers and journals | Pass-through, incidence and tax design |\n"

VI_A2 = "| OpenAlex | Đa ngành, gồm kinh tế và chính sách | Bao phủ văn liệu khoa học xã hội về thuế |\n| Scopus | Đa ngành | Tạp chí kinh tế và chính sách không có trong MEDLINE |\n"
VI_A2_NEW = VI_A2 + "| Cochrane Library (CDSR và CENTRAL) | Tổng quan hệ thống và thử nghiệm | Tổng quan về can thiệp SSB; bằng chứng thử nghiệm về giá và tiêu thụ |\n| RePEc/IDEAS | Working paper và tạp chí kinh tế | Truyền dẫn, quy giáng và thiết kế thuế |\n"

EN_A3 = """*Cochrane Library* (CDSR and CENTRAL; line-numbered sets):

```
#1 ("sugar-sweetened beverage" OR "sugar sweetened beverage" OR "sugary drink"
    OR "soft drink" OR "carbonated beverage" OR soda):ti,ab,kw
#2 (tax OR taxes OR taxation OR excise OR "fiscal policy" OR "price elasticity"):ti,ab,kw
#3 (vietnam OR "viet nam"):ti,ab,kw
#4 #1 AND #2
#5 #4 AND #3
```

*RePEc/IDEAS* (EconPapers advanced search, title and abstract), supplemented by
`site:ideas.repec.org OR site:econpapers.repec.org ("sugar-sweetened beverage" OR "soft drink" OR soda) (tax OR taxation OR excise)`:

```
("sugar-sweetened beverage" OR "soft drink" OR soda)
AND (tax OR taxation OR excise)
AND (vietnam OR "viet nam" OR asia OR "developing countr*")
```

"""
VI_A3 = """*Cochrane Library* (CDSR và CENTRAL; tập đánh số dòng):

```
#1 ("sugar-sweetened beverage" OR "sugar sweetened beverage" OR "sugary drink"
    OR "soft drink" OR "carbonated beverage" OR soda):ti,ab,kw
#2 (tax OR taxes OR taxation OR excise OR "fiscal policy" OR "price elasticity"):ti,ab,kw
#3 (vietnam OR "viet nam"):ti,ab,kw
#4 #1 AND #2
#5 #4 AND #3
```

*RePEc/IDEAS* (tìm nâng cao EconPapers, tiêu đề và tóm tắt), bổ sung bằng
`site:ideas.repec.org OR site:econpapers.repec.org ("sugar-sweetened beverage" OR "soft drink" OR soda) (tax OR taxation OR excise)`:

```
("sugar-sweetened beverage" OR "soft drink" OR soda)
AND (tax OR taxation OR excise)
AND (vietnam OR "viet nam" OR asia OR "developing countr*")
```

"""

EN_A6 = """**A.6 Flow**

Six sources were searched on 1 November 2026 with the strings in A.3. The country-limited searches returned **2 records in PubMed, 3 in Europe PMC, 11 in OpenAlex, 6 in Scopus, 3 in Cochrane Library and none in RePEc/IDEAS**, a total of 25. After removing duplicates across databases, **14 unique records** remained.

Eight were included: two quantitative analyses that model SSB taxation in Viet Nam; one distributional analysis of the 2025 design using household survey data; one empirical study of excise effects on beverage consumption; one human-rights assessment of the enacted tax; one study of public acceptability; one regional analysis of the distributional impacts of health taxes; and one Cochrane systematic review of environmental interventions to reduce SSB consumption.

Six were excluded. A 1997 dental review of sugar consumption trends is not about taxation. A historical article on Lyndon Johnson was retrieved by the country term as a false positive. An urban food-systems paper and a study of food marketing to children report no SSB-tax estimate. A peer-led dietary education trial and a caries prevalence study mention Viet Nam but contain no tax exposure. The record-level log, with the decision and the reason for each record, is in `data/screening_log.csv` and in the supplementary material.

The broad sets without a country limit returned 576 records in PubMed, 506 in Europe PMC, 2,961 in OpenAlex, 1,526 in Cochrane CENTRAL and 21 in RePEc. These were used to source parameter values — price elasticities, pass-through, relative risks and cost estimates — rather than screened record by record, because the study needs parameter estimates from any comparable setting and not a systematic review of tax effects.

Two features of this flow are themselves findings. The yield of the country-limited searches is very small: fourteen unique records for the whole Vietnamese literature on SSB taxation, of which eight are relevant. And the 1997 dental review is retrieved by every database because it names Viet Nam in a list of countries with rising sugar consumption — a reminder that country-term searches in this field are noisy.

"""

VI_A6 = """**A.6 Sơ đồ dòng**

Sáu nguồn được tìm ngày 1/11/2026 bằng chuỗi ở A.3. Các tìm kiếm giới hạn quốc gia trả về **2 bản ghi ở PubMed, 3 ở Europe PMC, 11 ở OpenAlex, 6 ở Scopus, 3 ở Cochrane Library và không có bản ghi nào ở RePEc/IDEAS**, tổng cộng 25. Sau khi loại trùng giữa các cơ sở dữ liệu, còn **14 bản ghi duy nhất**.

Tám bản ghi được đưa vào: hai phân tích định lượng mô hình hóa thuế đồ uống có đường tại Việt Nam; một phân tích phân bố của thiết kế 2025 dùng dữ liệu khảo sát hộ; một nghiên cứu thực nghiệm về tác động của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống; một đánh giá nhân quyền về thuế đã ban hành; một nghiên cứu về mức chấp nhận của công chúng; một phân tích khu vực về tác động phân bố của thuế sức khỏe; và một tổng quan hệ thống Cochrane về các can thiệp môi trường nhằm giảm tiêu thụ đồ uống có đường.

Sáu bản ghi bị loại. Một tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường không bàn về thuế. Một bài lịch sử về Lyndon Johnson bị từ khóa quốc gia bắt nhầm. Một bài về hệ thống thực phẩm đô thị và một nghiên cứu về tiếp thị thực phẩm cho trẻ em không có ước lượng nào về thuế đồ uống có đường. Một thử nghiệm giáo dục dinh dưỡng do đồng đẳng dẫn dắt và một nghiên cứu về tỷ lệ sâu răng có nêu Việt Nam nhưng không có phơi nhiễm thuế. Nhật ký theo từng bản ghi, kèm quyết định và lý do, nằm ở `data/screening_log.csv` và trong tài liệu bổ sung.

Các tập rộng không giới hạn quốc gia trả về 576 bản ghi ở PubMed, 506 ở Europe PMC, 2.961 ở OpenAlex, 1.526 ở Cochrane CENTRAL và 21 ở RePEc. Các tập này được dùng để lấy giá trị tham số — độ co giãn giá, mức truyền dẫn, nguy cơ tương đối và chi phí — chứ không sàng lọc từng bản ghi, vì nghiên cứu cần ước lượng tham số từ bất kỳ bối cảnh so sánh được nào, không phải một tổng quan hệ thống về tác động của thuế.

Hai đặc điểm của sơ đồ này tự chúng là phát hiện. Năng suất của các tìm kiếm giới hạn quốc gia rất thấp: mười bốn bản ghi duy nhất cho toàn bộ văn liệu Việt Nam về thuế đồ uống có đường, trong đó tám bản ghi có liên quan. Và tổng quan nha khoa 1997 được mọi cơ sở dữ liệu trả về vì nó nêu tên Việt Nam trong danh sách các nước có tiêu thụ đường tăng — một lời nhắc rằng tìm theo từ khóa quốc gia trong lĩnh vực này rất nhiễu.

"""

def apply(path, a2_old, a2_new, a3_block, a6):
    s = open(path, encoding="utf-8").read()
    assert a2_old in s
    s = s.replace(a2_old, a2_new, 1)
    marker = "*Vietnamese-language sources*" if "*Vietnamese-language" in s else "*Nguồn tiếng Việt*"
    assert marker in s
    s = s.replace(marker, a3_block + marker, 1)
    i = s.index("**A.6"); j = s.index("**A.7", i)
    s = s[:i] + a6 + s[j:]
    open(path, "w", encoding="utf-8").write(s)

apply("Manuscript_draft_v1.md", EN_A2, EN_A2_NEW, EN_A3, EN_A6)
apply("Ban_thao_Tieng_Viet.md", VI_A2, VI_A2_NEW, VI_A3, VI_A6)
print("applied")
