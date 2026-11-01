# -*- coding: utf-8 -*-
"""Put Scopus back (it was searched) and report the real screening flow."""
import json, re

C = json.load(open("output/screening_counts.json"))
print(C)

EN_A2_ANCHOR = "| OpenAlex | Multidisciplinary, including economics and policy | Captures social-science literature on taxation |\n"
EN_A2_NEW = EN_A2_ANCHOR + "| Scopus | Multidisciplinary | Economics and policy journals not indexed in MEDLINE |\n"
VI_A2_ANCHOR = "| OpenAlex | Đa ngành, gồm kinh tế và chính sách | Bao phủ văn liệu khoa học xã hội về thuế |\n"
VI_A2_NEW = VI_A2_ANCHOR + "| Scopus | Đa ngành | Tạp chí kinh tế và chính sách không có trong MEDLINE |\n"

EN_A3_ADD = """*Scopus* (title, abstract and keywords; Viet Nam set returned 6 records):

```
TITLE-ABS-KEY(("sugar-sweetened beverage" OR "sugar sweetened beverage"
 OR "sugary drink" OR "soft drink" OR "carbonated beverage" OR "soda")
 AND (tax OR taxation OR excise OR "fiscal policy"))
AND TITLE-ABS-KEY("Viet Nam" OR Vietnam)
```

*Scopus, broad set without a country limit:* the same first two blocks, run without the country line.

"""
VI_A3_ADD = """*Scopus* (tiêu đề, tóm tắt và từ khóa; tập Việt Nam trả về 6 bản ghi):

```
TITLE-ABS-KEY(("sugar-sweetened beverage" OR "sugar sweetened beverage"
 OR "sugary drink" OR "soft drink" OR "carbonated beverage" OR "soda")
 AND (tax OR taxation OR excise OR "fiscal policy"))
AND TITLE-ABS-KEY("Viet Nam" OR Vietnam)
```

*Scopus, tập rộng không giới hạn quốc gia:* hai khối đầu, bỏ dòng quốc gia.

"""

EN_A6 = """**A.6 Flow**

Four databases were searched on 1 November 2026 with the strings in A.3. The country-limited searches returned **2 records in PubMed, 3 in Europe PMC, 11 in OpenAlex and 6 in Scopus**, a total of 22. After removing duplicates across databases, **11 unique records** remained. Seven were included: two modelling studies of SSB taxation in Viet Nam, one distributional analysis of the 2025 design using household survey data, one empirical study of excise effects on beverage consumption, one human-rights assessment of the enacted tax, one study of public acceptability, and one regional analysis of the distributional impacts of health taxes. Four were excluded: a 1997 dental review of sugar consumption trends (not about taxation); a historical article on Lyndon Johnson that the country term retrieved as a false positive; an urban food-systems paper; and a study of food marketing to children, neither of which reports an SSB-tax estimate. The full record-level log, with the decision and the reason for each record, is in `data/screening_log.csv` in the repository and in the supplementary material.

Cochrane Library and RePEc/IDEAS were not accessible to the team, and are not claimed as sources; the forward and backward citation chasing described in A.3 was used in their place, and the reference lists of the two most recent reviews were screened by hand.

Two features of this flow are themselves findings. First, the yield of the country-limited searches is very small: eleven unique records for the whole Vietnamese literature on SSB taxation. Second, the 1997 dental review is retrieved by every database because it names Viet Nam in a list of countries with rising sugar consumption — a reminder that country-term searches in this field are noisy. The 2026 Vietnamese economic study was not indexed in PubMed at all and was found only through Scopus and OpenAlex.

"""

VI_A6 = """**A.6 Sơ đồ dòng**

Bốn cơ sở dữ liệu được tìm ngày 1/11/2026 bằng chuỗi ở A.3. Các tìm kiếm giới hạn quốc gia trả về **2 bản ghi ở PubMed, 3 ở Europe PMC, 11 ở OpenAlex và 6 ở Scopus**, tổng cộng 22. Sau khi loại trùng giữa các cơ sở dữ liệu, còn **11 bản ghi duy nhất**. Bảy bản ghi được đưa vào: hai nghiên cứu mô hình hóa thuế đồ uống có đường tại Việt Nam, một phân tích phân bố của thiết kế 2025 dùng dữ liệu khảo sát hộ, một nghiên cứu thực nghiệm về tác động của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống, một đánh giá nhân quyền về thuế đã ban hành, một nghiên cứu về mức chấp nhận của công chúng, và một phân tích khu vực về tác động phân bố của thuế sức khỏe. Bốn bản ghi bị loại: một tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường (không bàn về thuế); một bài lịch sử về Lyndon Johnson mà từ khóa quốc gia bắt nhầm; một bài về hệ thống thực phẩm đô thị; và một nghiên cứu về tiếp thị thực phẩm cho trẻ em — hai bài sau không có ước lượng nào về thuế đồ uống có đường. Nhật ký đầy đủ theo từng bản ghi, kèm quyết định và lý do, nằm ở `data/screening_log.csv` trong kho mã và trong tài liệu bổ sung.

Cochrane Library và RePEc/IDEAS không thuộc quyền truy cập của nhóm và không được tính là nguồn; truy vết trích dẫn xuôi và ngược mô tả ở A.3 được dùng thay thế, và danh mục tài liệu tham khảo của hai tổng quan gần nhất được sàng lọc thủ công.

Hai đặc điểm của sơ đồ này tự chúng là phát hiện. Thứ nhất, năng suất của các tìm kiếm giới hạn quốc gia rất thấp: mười một bản ghi duy nhất cho toàn bộ văn liệu Việt Nam về thuế đồ uống có đường. Thứ hai, tổng quan nha khoa 1997 được mọi cơ sở dữ liệu trả về vì nó nêu tên Việt Nam trong danh sách các nước có tiêu thụ đường tăng — một lời nhắc rằng tìm theo từ khóa quốc gia trong lĩnh vực này rất nhiễu. Nghiên cứu kinh tế Việt Nam 2026 hoàn toàn không được chỉ mục trong PubMed và chỉ tìm được qua Scopus và OpenAlex.

"""

def apply(path, a2_anchor, a2_new, a3_add, a6_new):
    s = open(path, encoding="utf-8").read()
    assert a2_anchor in s
    s = s.replace(a2_anchor, a2_new, 1)
    # insert the Scopus string block right before the Vietnamese-language sources paragraph
    marker = "*Vietnamese-language sources*" if "*Vietnamese-language sources*" in s else "*Nguồn tiếng Việt*"
    assert marker in s
    s = s.replace(marker, a3_add + marker, 1)
    i = s.index("**A.6")
    j = s.index("**A.7", i)
    s = s[:i] + a6_new + s[j:]
    open(path, "w", encoding="utf-8").write(s)

apply("Manuscript_draft_v1.md", EN_A2_ANCHOR, EN_A2_NEW, EN_A3_ADD, EN_A6)
apply("Ban_thao_Tieng_Viet.md", VI_A2_ANCHOR, VI_A2_NEW, VI_A3_ADD, VI_A6)
print("applied")
