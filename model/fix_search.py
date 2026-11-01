# -*- coding: utf-8 -*-
"""Replace the database section with what was actually searched."""
import re, json

C = json.load(open("output/database_counts.json"))

EN_A2_BLOCK = """| PubMed/MEDLINE | Biomedical and public health | Studies of health impact, epidemiology, risk |
| Europe PMC | Biomedical and life sciences, including preprints | Catches records not indexed in MEDLINE |
| OpenAlex | Multidisciplinary, including economics and policy | Captures social-science literature on taxation |
| Citation chasing, forward and backward | Studies citing, or cited by, each included record | Recovers literature missed by keyword searching |
| Google Scholar | Grey and non-indexed | Vietnamese-language scholarship |
"""

EN_A3_SCOPUS = """*Scopus:*

```
TITLE-ABS-KEY(("sugar-sweetened beverage" OR "sugar sweetened beverage"
 OR "sugary drink" OR "soft drink" OR "carbonated beverage" OR "soda")
 AND (tax OR taxation OR excise OR "fiscal policy")
 AND ("Viet Nam" OR Vietnam))
```
"""

EN_A3_SCOPUS_NEW = """*Europe PMC* (title and abstract fields; broad set returned %d records, Viet Nam set %d):

```
(TITLE_ABS:"sugar-sweetened beverage" OR TITLE_ABS:"sugar sweetened beverage"
 OR TITLE_ABS:"sugary drink" OR TITLE_ABS:"soft drink"
 OR TITLE_ABS:"carbonated beverage" OR TITLE_ABS:soda)
AND
(TITLE_ABS:tax OR TITLE_ABS:taxation OR TITLE_ABS:excise OR TITLE_ABS:"fiscal policy")
[AND (TITLE_ABS:vietnam OR TITLE_ABS:"viet nam")]
```

*OpenAlex* (title and abstract; broad set returned %d records, Viet Nam set %d):

```
filter=title_and_abstract.search:("sugar-sweetened beverage" OR "soft drink" OR soda)
   AND (tax OR taxation OR excise)
   [AND (vietnam OR "viet nam")]
```
""" % (C["epmc_tiab_broad"], C["epmc_tiab_vn"], C["oa_broad"], C["oa_vn"])

EN_A6 = """**A.6 Flow**

Four databases were searched with the strings in A.3, on 1 November 2026. The Viet Nam sets returned **2 records in PubMed, 3 in Europe PMC and 13 in OpenAlex**; the corresponding broad sets without a country limit returned **576, %d and %d records** respectively. Scopus and Cochrane Library were not accessible to the team, and RePEc/IDEAS was blocked to automated queries at the time of the search; citation chasing of every included study was used in their place, and the reference lists of the two most recent reviews were screened by hand. De-duplication, screening, and full-text exclusion counts are maintained in the screening log deposited with the protocol.

The low yield of the country-limited searches is itself informative. PubMed returned two records, one of which is a 1997 dental review of sugar consumption trends, leaving a single relevant Vietnamese analysis; the 2026 Vietnamese economic study was not indexed in PubMed at all and was found through citation chasing. That is the empirical basis for the gap this study addresses, and it is why the searches were widened to the broad sets rather than repeated with more database-specific syntax.

""" % (C["epmc_tiab_broad"], C["oa_broad"])

def apply(path, a2_old_start, a2_new, a3_old, a3_new, a6_new):
    s = open(path, encoding="utf-8").read()
    # A.2 table rows
    i = s.index(a2_old_start)
    j = s.index("\n\n", i)
    s = s[:i] + a2_new.rstrip("\n") + s[j:]
    # A.3 scopus block
    assert a3_old in s, "scopus block not found"
    s = s.replace(a3_old, a3_new)
    # A.6
    i = s.index("**A.6")
    j = s.index("**A.7", i)
    s = s[:i] + a6_new + s[j:]
    open(path, "w", encoding="utf-8").write(s)

apply("Manuscript_draft_v1.md", "| PubMed/MEDLINE |", EN_A2_BLOCK, EN_A3_SCOPUS, EN_A3_SCOPUS_NEW, EN_A6)
print("EN applied")

# ---------------- Vietnamese ----------------
VI_A2_BLOCK = """| PubMed/MEDLINE | Y sinh và sức khỏe công cộng | Nghiên cứu tác động sức khỏe, dịch tễ, nguy cơ |
| Europe PMC | Y sinh và khoa học sự sống, gồm cả preprint | Bắt các bản ghi không có trong MEDLINE |
| OpenAlex | Đa ngành, gồm kinh tế và chính sách | Bao phủ văn liệu khoa học xã hội về thuế |
| Truy vết trích dẫn, xuôi và ngược | Nghiên cứu trích dẫn, hoặc được trích dẫn bởi, mỗi bản ghi được đưa vào | Bắt văn liệu mà tìm theo từ khóa bỏ sót |
| Google Scholar | Tài liệu xám và không được chỉ mục | Học thuật tiếng Việt |
"""

VI_A3_OLD = """*Scopus:*

```
TITLE-ABS-KEY(("sugar-sweetened beverage" OR "sugar sweetened beverage"
 OR "sugary drink" OR "soft drink" OR "carbonated beverage" OR "soda")
 AND (tax OR taxation OR excise OR "fiscal policy")
 AND ("Viet Nam" OR Vietnam))
```
"""

VI_A3_NEW = """*Europe PMC* (trường tiêu đề và tóm tắt; tập rộng trả về %d bản ghi, tập Việt Nam %d):

```
(TITLE_ABS:"sugar-sweetened beverage" OR TITLE_ABS:"sugar sweetened beverage"
 OR TITLE_ABS:"sugary drink" OR TITLE_ABS:"soft drink"
 OR TITLE_ABS:"carbonated beverage" OR TITLE_ABS:soda)
AND
(TITLE_ABS:tax OR TITLE_ABS:taxation OR TITLE_ABS:excise OR TITLE_ABS:"fiscal policy")
[AND (TITLE_ABS:vietnam OR TITLE_ABS:"viet nam")]
```

*OpenAlex* (tiêu đề và tóm tắt; tập rộng trả về %d bản ghi, tập Việt Nam %d):

```
filter=title_and_abstract.search:("sugar-sweetened beverage" OR "soft drink" OR soda)
   AND (tax OR taxation OR excise)
   [AND (vietnam OR "viet nam")]
```
""" % (C["epmc_tiab_broad"], C["epmc_tiab_vn"], C["oa_broad"], C["oa_vn"])

VI_A6 = """**A.6 Sơ đồ dòng**

Bốn cơ sở dữ liệu được tìm bằng chuỗi ở A.3, ngày 1/11/2026. Tập Việt Nam trả về **2 bản ghi ở PubMed, 3 ở Europe PMC và 13 ở OpenAlex**; các tập rộng không giới hạn quốc gia tương ứng trả về **576, %d và %d bản ghi**. Scopus và Cochrane Library không thuộc quyền truy cập của nhóm, và RePEc/IDEAS chặn truy vấn tự động tại thời điểm tìm; truy vết trích dẫn cho mọi nghiên cứu được đưa vào được dùng thay thế, và danh mục tài liệu tham khảo của hai tổng quan gần nhất được sàng lọc thủ công. Số loại trùng, số sàng lọc và lý do loại ở bước toàn văn được duy trì trong nhật ký sàng lọc nộp kèm protocol.

Năng suất thấp của các tìm kiếm giới hạn quốc gia tự nó là thông tin. PubMed trả về hai bản ghi, một là tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường, còn lại một phân tích Việt Nam có liên quan; nghiên cứu kinh tế Việt Nam 2026 hoàn toàn không được chỉ mục trong PubMed và chỉ tìm được qua truy vết trích dẫn. Đó là căn cứ thực nghiệm cho khoảng trống mà nghiên cứu này đề cập, và là lý do các tìm kiếm được mở rộng sang tập rộng thay vì lặp lại với cú pháp riêng của từng cơ sở dữ liệu.

""" % (C["epmc_tiab_broad"], C["oa_broad"])

apply("Ban_thao_Tieng_Viet.md", "| PubMed/MEDLINE |", VI_A2_BLOCK, VI_A3_OLD, VI_A3_NEW, VI_A6)
print("VI applied")
