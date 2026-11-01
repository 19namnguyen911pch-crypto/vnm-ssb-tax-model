## Phụ lục A. Tìm kiếm bằng chứng

**A.1 Các câu hỏi mà cuộc tìm kiếm phải trả lời**

Ba, theo thứ tự quan trọng. (i) Đã có ai mô hình hóa đúng mức thuế đồ uống có đường mà Việt Nam đã ban hành, hoặc hệ quả phân bố của nó, chưa? (ii) Giá trị tham số tốt nhất hiện có cho các bước giá, cầu, năng lượng và nguy cơ của mô hình là gì, cho Việt Nam hoặc cho bối cảnh so sánh được? (iii) Bản thân văn bản pháp luật nói gì? Câu hỏi thứ ba được trả lời từ nguồn pháp lý gốc và ghi nhật ký riêng ở A.7, vì một mô hình thuế dựng trên mô tả thứ cấp của luật là mô hình dựng trên sai cơ sở.

**A.2 Nguồn**

| Nguồn | Phạm vi | Mục đích |
|---|---|---|
| PubMed/MEDLINE | Y sinh và sức khỏe công cộng | Nghiên cứu tác động sức khỏe, dịch tễ, nguy cơ |
| Europe PMC | Y sinh và khoa học sự sống, gồm cả preprint | Bắt các bản ghi không có trong MEDLINE |
| OpenAlex | Đa ngành, gồm kinh tế và chính sách | Bao phủ văn liệu khoa học xã hội về thuế |
| Scopus | Đa ngành | Tạp chí kinh tế và chính sách không có trong MEDLINE |
| Cochrane Library (CDSR và CENTRAL) | Tổng quan hệ thống và thử nghiệm | Tổng quan về can thiệp SSB; bằng chứng thử nghiệm về giá và tiêu thụ |
| RePEc/IDEAS | Working paper và tạp chí kinh tế | Truyền dẫn, quy giáng và thiết kế thuế |
| Truy vết trích dẫn, xuôi và ngược | Nghiên cứu trích dẫn, hoặc được trích dẫn bởi, mỗi bản ghi được đưa vào | Bắt văn liệu mà tìm theo từ khóa bỏ sót |
| Google Scholar | Tài liệu xám và không được chỉ mục | Học thuật tiếng Việt |
| WHO IRIS | Chính sách y tế toàn cầu | Báo cáo và tài liệu kỹ thuật của WHO |
| World Bank, IMF, ADB | Kinh tế phát triển | Tài liệu thiết kế thuế và doanh thu |
| Bộ Tài chính, Bộ Y tế, HSPI, NIN, TCTK | Nguồn chính thức Việt Nam | Văn bản pháp luật, dự toán ngân sách, tài liệu khảo sát |
| Thuvienphapluat, vanban.chinhphu.vn, Công báo | Pháp lý Việt Nam | Văn bản pháp luật gốc |
| Euromonitor Passport | Dữ liệu thị trường thương mại | Sản lượng và giá trị thị trường đồ uống |
| GHAI, Vital Strategies, HealthBridge, UNICEF, WHO Việt Nam | Vận động chính sách và chương trình | Tài liệu xám về quá trình chính sách tại Việt Nam |

**A.3 Chuỗi tìm kiếm**

Chuỗi được báo cáo đầy đủ để có thể chạy lại. Mỗi chuỗi được thực hiện theo cú pháp của chính cơ sở dữ liệu; từ khóa MeSH chỉ dùng cho PubMed.

*PubMed, tập Việt Nam (trả về 2 bản ghi):*

```
("sugar-sweetened beverage"[tiab] OR "sugar sweetened beverage"[tiab]
 OR "sugary drink"[tiab] OR "sugary drinks"[tiab] OR "soft drink"[tiab]
 OR "soft drinks"[tiab] OR "carbonated beverage"[tiab]
 OR "carbonated beverages"[tiab] OR "sugary beverage"[tiab]
 OR "SSB"[tiab] OR "SSBs"[tiab] OR "soda tax"[tiab])
AND
("tax"[tiab] OR "taxes"[tiab] OR "taxed"[tiab] OR "taxing"[tiab]
 OR "taxation"[tiab] OR "excise"[tiab] OR "fiscal policy"[tiab]
 OR "price elasticity"[tiab] OR "pass-through"[tiab])
AND
("Viet Nam"[tiab] OR Vietnam[tiab] OR "Vietnam"[MeSH Terms])
```

*PubMed, tập rộng về thuế đồ uống có đường không giới hạn quốc gia, dùng để đo quy mô lĩnh vực và tìm tham số từ bối cảnh so sánh được (trả về 576 bản ghi):*

```
("sugar-sweetened beverage"[tiab] OR "sugary drink"[tiab]
 OR "soft drink"[tiab] OR "soda"[tiab])
AND
("tax"[tiab] OR "taxes"[tiab] OR "taxation"[tiab] OR "excise"[tiab])
```

*Europe PMC* (trường tiêu đề và tóm tắt; tập rộng trả về 506 bản ghi, tập Việt Nam 3):

```
(TITLE_ABS:"sugar-sweetened beverage" OR TITLE_ABS:"sugar sweetened beverage"
 OR TITLE_ABS:"sugary drink" OR TITLE_ABS:"soft drink"
 OR TITLE_ABS:"carbonated beverage" OR TITLE_ABS:soda)
AND
(TITLE_ABS:tax OR TITLE_ABS:taxation OR TITLE_ABS:excise OR TITLE_ABS:"fiscal policy")
[AND (TITLE_ABS:vietnam OR TITLE_ABS:"viet nam")]
```

*OpenAlex* (tiêu đề và tóm tắt; tập rộng trả về 2961 bản ghi, tập Việt Nam 11):

```
filter=title_and_abstract.search:("sugar-sweetened beverage" OR "soft drink" OR soda)
   AND (tax OR taxation OR excise)
   [AND (vietnam OR "viet nam")]
```

Tập #4 được chạy không giới hạn quốc gia vì văn liệu tổng quan và thử nghiệm về thuế đồ uống có đường rất mỏng và gần như toàn bộ không phải của Việt Nam; #5 tách riêng tập con Việt Nam.

IDEAS chỉ hỗ trợ cú pháp Boolean hạn chế, nên tìm kiếm được bổ sung bằng một truy vấn giới hạn tên miền, `site:ideas.repec.org "sugar-sweetened" tax`, chạy trên Google Scholar và Google.

*Truy vết trích dẫn.* Danh mục tài liệu tham khảo của mọi nghiên cứu được đưa vào được sàng lọc thủ công, và chức năng "được trích dẫn bởi" của Google Scholar được dùng cho hai phân tích Việt Nam và cho từng tổng quan hệ thống được đưa vào.


*Scopus* (tiêu đề, tóm tắt và từ khóa; tập Việt Nam trả về 6 bản ghi):

```
TITLE-ABS-KEY(("sugar-sweetened beverage" OR "sugar sweetened beverage"
 OR "sugary drink" OR "soft drink" OR "carbonated beverage" OR "soda")
 AND (tax OR taxation OR excise OR "fiscal policy"))
AND TITLE-ABS-KEY("Viet Nam" OR Vietnam)
```

*Scopus, tập rộng không giới hạn quốc gia:* hai khối đầu, bỏ dòng quốc gia.

*Cochrane Library* (CDSR và CENTRAL; tập đánh số dòng):

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

*Nguồn tiếng Việt* (Google Scholar và vjol.info, chuỗi không đặt trong ngoặc kép):

```
thuế tiêu thụ đặc biệt nước giải khát; thuế đồ uống có đường;
độ co giãn giá đồ uống; gánh nặng đái tháo đường Việt Nam
```

*Nguồn pháp lý:* tìm theo số hiệu văn bản sau khi đã xác định, và theo từ khóa `nước giải khát`, `hàm lượng đường`, `thuế tiêu thụ đặc biệt` trên `vanban.chinhphu.vn` và `thuvienphapluat.vn`.

**A.4 Tiêu chí lựa chọn**

*Đưa vào:* nghiên cứu mô hình hóa, thực nghiệm tự nhiên và đánh giá thuế đồ uống có đường báo cáo kết cục về giá, mua, tiêu thụ, cân nặng, bệnh, chi phí, doanh thu hoặc phân bố; tổng quan hệ thống và phân tích gộp về độ co giãn hoặc hiệu quả; nghiên cứu chi phí bệnh và chi phí điều trị cho ba bệnh trong mô hình tại Việt Nam hoặc bối cảnh so sánh được; nghiên cứu định tính về trải nghiệm người bệnh dùng cho diễn giải; và văn bản pháp lý, ngân sách gốc.

*Loại ra:* nghiên cứu về thuế đánh vào thực phẩm khác đồ uống, hoặc vào chất dinh dưỡng khác đường, mà không có ước lượng riêng cho đồ uống có đường; bình luận, xã luận và tài liệu vận động không có dữ liệu gốc, trừ khi được dùng làm bằng chứng xám về quá trình chính sách; nghiên cứu không trích xuất được kết cục; và báo cáo thị trường không bình duyệt, trừ Euromonitor — chỉ dùng cho sản lượng và giá trị, và được ghi rõ là dữ liệu thương mại ở mọi chỗ trích dẫn.

*Giới hạn:* công bố từ năm 2000 trở đi với văn liệu về thuế, không giới hạn thời gian với dịch tễ, nguy cơ tương đối và bảng thành phần thực phẩm; ngôn ngữ tiếng Anh và tiếng Việt.

**A.5 Quy trình sàng lọc**

1. Mỗi cơ sở dữ liệu được tìm ngày 1/11/2026 bằng chuỗi ở A.3 và kết quả được xuất toàn bộ sang phần mềm quản lý tài liệu tham khảo.
2. Bản ghi được loại trùng theo hai lượt: theo DOI nếu có, nếu không thì theo tiêu đề đã chuẩn hóa (chữ thường, bỏ dấu, bỏ dấu câu).
3. Tiêu đề và tóm tắt được sàng lọc theo tiêu chí ở A.4. Mọi bản ghi đều được giữ lại hoặc loại kèm lý do ghi nhận; không bản ghi nào bị bỏ im lặng.
4. Toàn văn của mọi bản ghi được giữ lại đều được lấy về và đối chiếu với cùng tiêu chí.
5. Một người đọc thứ hai kiểm tra mọi đề xuất loại, bất đồng được giải quyết bằng thảo luận. Hệ số kappa không được tính vì số bản ghi cần quyết định nhỏ.
6. Kết quả từng bước được ghi ở cấp bản ghi trong `data/screening_log.csv`, tệp này được nộp cùng protocol và in lại trong tài liệu bổ sung.

**A.6 Sơ đồ dòng**

| Giai đoạn | PubMed | Europe PMC | OpenAlex | Scopus | Cochrane | RePEc | Tổng |
|---|---|---|---|---|---|---|---|
| Xác định được, tập giới hạn quốc gia | 2 | 3 | 11 | 6 | 3 | 0 | **25** |
| Loại do trùng lặp | | | | | | | 11 |
| Bản ghi duy nhất được sàng lọc | | | | | | | **14** |
| Loại khi sàng lọc | | | | | | | 6 |
| Đưa vào | | | | | | | **8** |

Tám bản ghi được đưa vào: hai phân tích định lượng mô hình hóa thuế đồ uống có đường tại Việt Nam; một phân tích phân bố của thiết kế 2025 dùng dữ liệu khảo sát hộ; một nghiên cứu thực nghiệm về tác động của thuế tiêu thụ đặc biệt lên tiêu thụ đồ uống; một đánh giá nhân quyền về thuế đã ban hành; một nghiên cứu về mức chấp nhận của công chúng; một phân tích khu vực về tác động phân bố của thuế sức khỏe; và một tổng quan hệ thống Cochrane về các can thiệp môi trường nhằm giảm tiêu thụ đồ uống có đường.

Sáu bản ghi bị loại. Một tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường không bàn về thuế; một bài lịch sử về Lyndon Johnson bị từ khóa quốc gia bắt nhầm; một bài về hệ thống thực phẩm đô thị và một nghiên cứu về tiếp thị thực phẩm cho trẻ em không có ước lượng nào về thuế đồ uống có đường; một thử nghiệm giáo dục dinh dưỡng do đồng đẳng dẫn dắt và một nghiên cứu về tỷ lệ sâu răng có nêu Việt Nam nhưng không có phơi nhiễm thuế.

Các tập rộng không giới hạn quốc gia trả về 576 bản ghi ở PubMed, 506 ở Europe PMC, 2.961 ở OpenAlex, 1.526 ở Cochrane CENTRAL và 21 ở RePEc. Các tập này được sàng lọc để lấy bằng chứng tham số — độ co giãn giá, mức truyền dẫn, nguy cơ tương đối và chi phí — chứ không sàng lọc từng bản ghi, vì nghiên cứu cần ước lượng từ bất kỳ bối cảnh so sánh được nào, không phải một tổng quan hệ thống về tác động của thuế. Tập RePEc không có nghiên cứu Việt Nam nhưng có hai đánh giá thuế nước ngọt châu Âu báo cáo mức truyền dẫn, và cả hai được trích cho tham số đó (Phụ lục B, #5). 21 bản ghi thu được, kèm quyết định cho từng bản ghi, nằm ở `data/repec_screening.csv`.

Hai đặc điểm của sơ đồ này tự chúng là phát hiện. Năng suất của các tìm kiếm giới hạn quốc gia rất thấp: mười bốn bản ghi duy nhất cho toàn bộ văn liệu Việt Nam về thuế đồ uống có đường, trong đó tám bản ghi có liên quan. Và tổng quan nha khoa 1997 được mọi cơ sở dữ liệu trả về vì nó nêu tên Việt Nam trong danh sách các nước có tiêu thụ đường tăng — một lời nhắc rằng tìm theo từ khóa quốc gia trong lĩnh vực này rất nhiễu.

**A.7 Nhật ký xác minh nguồn pháp lý và ngân sách**

Các khẳng định pháp lý trong một mô hình thuế là khẳng định chịu lực và không thể trích dẫn qua tay thứ hai. Mỗi văn bản được đọc toàn văn và điều khoản cụ thể dùng trong mô hình được ghi kèm.

| Văn bản | Điều khoản sử dụng | Điều được chốt | Xác minh tại |
|---|---|---|---|
| Luật số 66/2025/QH15, 14/6/2025 | Điều 2 khoản 1 điểm l; biểu thuế Điều 8 | Nhóm chịu thuế; lộ trình 0%/8%/10%; Điều 3 không có danh mục miễn trừ cho đồ uống | Văn bản Quốc hội, bản dịch chính thức |
| Nghị định 360/2025/NĐ-CP, 31/12/2025 | Điều 3 khoản 4; Điều 5 | TCVN 12828:2019 là chuẩn phân nhóm; đường = **tổng** đường trên nhãn; giá tính thuế = giá bán của nhà sản xuất/nhập khẩu, chưa VAT và chưa TTĐB | Văn bản Chính phủ, bản dịch chính thức |
| Thông tư 158/2025/TT-BTC, 31/12/2025 | Hướng dẫn Nghị định 360 | Thủ tục; không thay đổi thực chất cơ sở hay phạm vi | Bộ Tài chính |
| Nghị định 174/2025/NĐ-CP, 30/6/2025 | Phụ lục II | Hàng chịu thuế TTĐB bị loại khỏi diện giảm VAT 8%; mức 10% áp từ 2027 | `vanban.chinhphu.vn`, docid 214310 |
| TCVN 12828:2019 | Điều khoản phạm vi | Sản phẩm trong và ngoài nhóm nước giải khát; nguồn gốc của việc loại trừ mang tính định nghĩa | Văn bản tiêu chuẩn và hướng dẫn thi hành |

**A.8 Những gì cuộc tìm kiếm xác lập trước khi chạy mô hình**

*Về câu hỏi Việt Nam.* Tìm kiếm PubMed đã hoàn tất trả về **576 bản ghi về thuế đồ uống có đường trên toàn cầu và 2 bản ghi cho Việt Nam** — một là tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường, một là nghiên cứu mô hình hóa 2023. Phân tích kinh tế năm 2026 không được chỉ mục trong PubMed và được tìm thấy qua RePEc và Google Scholar. Vậy tổng cộng có hai phân tích. Một nghiên cứu mô hình hóa năm kịch bản thuế ở mức tăng giá bán lẻ 5%, 11% và 19–20% khi luật còn đang thảo luận, và ước tính tác động lên cân nặng và đái tháo đường.[17] Nghiên cứu còn lại dùng Khảo sát mức sống hộ gia đình 2018 với hệ thống cầu hiệu chỉnh chất lượng để mô phỏng tác động lên tiêu thụ và phúc lợi theo luật 2025, nhưng coi đồ uống không cồn là một nhóm gộp gồm đồ uống có đường, nước đóng chai và nước ép 100%, và không mô hình hóa bệnh.[18] Cả hai đều không mô hình hóa thiết kế đã ban hành trên đúng cơ sở tính thuế, và không báo cáo lợi ích sức khỏe cùng thuế phải trả trên cùng một thang đo công bằng.

*Về câu hỏi quốc tế.* Đến năm 2024, 64 quốc gia đã áp dụng thuế đồ uống có đường, bao phủ 3,5 tỷ người; 45% theo tỷ lệ giá, 44% theo lượng và 5% theo hàm lượng đường.[10] Đánh giá năm 2025 của chính WHO đi đến kết luận nhất quán và ghi nhận rằng cơ sở tính thuế cùng điểm đánh thuế trên chuỗi giá khác nhau đến mức việc so sánh chuẩn hóa giữa các nước là khó[11] — chính vì vậy một phân tích neo vào cơ sở tính thuế theo luật, thay vì vào thuế suất danh nghĩa, mới là đơn vị so sánh hữu ích.

*Về tham số.* Độ co giãn, mức truyền dẫn, nguy cơ tương đối và chi phí đều có từ bối cảnh so sánh được nhưng không có từ Việt Nam, ngoại trừ ước lượng chi phí đái tháo đường.[35,36] Đây là nguồn gốc của hai ràng buộc chính được nhận diện ở Phụ lục B: tỷ trọng giá xuất xưởng trong giá bán lẻ, và tỷ lệ mắc bệnh theo ngũ phân vị.

**A.9 Duy trì nhật ký**

Nhật ký sàng lọc, lý do loại ở bước toàn văn, nhật ký xác minh ở A.7 và ngày tìm kiếm được lưu cùng protocol tại https://doi.org/10.5281/zenodo.23852908. Mọi chuỗi bị sửa sau khi protocol được lưu được ghi ở Phụ lục C.

---

## Phụ lục B. Nhật ký bằng chứng tham số

Mỗi tham số một dòng. Cột "Loại" phân biệt giá trị lấy từ nguồn công bố, giá trị suy ra bằng số học từ dữ liệu công bố, và giả định không có cơ sở thực nghiệm trực tiếp. Cột cuối ghi khả năng điền từ dữ liệu hiện có (có / một phần / không); khi là *không* hoặc *một phần*, phần ghi chú nêu phương án thay thế.

**B.1 Bảng tóm tắt**

| # | Tham số | Giá trị trung tâm đã dùng | Khoảng bất định | Phân phối | Nguồn | Loại | Khả thi |
|---|---|---|---|---|---|---|---|
| 1 | Dân số từ 20 tuổi, theo tuổi và ngũ phân vị | 81 triệu, phân bố năm 2027 giữ cho mọi năm | — | Cố định | Dự báo dân số UN 2024 [26] | Nguồn | Có |
| 2 | Xu hướng tiêu thụ nền | +2,0%/năm | 0 đến +4,0% | Đều | CAGR Euromonitor 2009–2023 [6] | Suy ra | Một phần |
| 3 | Tiêu thụ theo tuổi, giới, ngũ phân vị | 145 mL/người/ngày | 90 đến 220 | Gamma | Euromonitor [6]; GNS 2019–20 [27]; VHLSS [37] | Suy ra | Một phần |
| 4 | Tỷ trọng giá xuất xưởng trong giá bán lẻ | 0,55 | 0,40 đến 0,70 | Tam giác | Không có nguồn Việt Nam; cấu trúc biên FMCG | Giả định | **Không** |
| 5 | Mức truyền dẫn | 0,90 | 0,50 đến 1,30 | Tam giác | World Bank 2020 [28]; Barbados, Mexico [41]; Bồ Đào Nha, Pháp [29,30] | Nguồn (nước ngoài) | Một phần |
| 6a | Độ co giãn giá riêng | −1,20 | −0,80 đến −1,80 | Log-chuẩn trên \|ε\| | Andreyeva [31]; Cabrera Escobar [42]; Colchero [21] | Nguồn | Một phần |
| 6b | Độ co giãn giá chéo sang đồ uống không chịu thuế | +0,35 | +0,10 đến +0,65 | Log-chuẩn | Hệ thống cầu Chile và Mexico [21] | Nguồn | Một phần |
| 6c | Gradient độ co giãn theo ngũ phân vị | Q1 = 1,4 × Q5 | 1,0 đến 1,8 | — | Colchero [21] | Suy ra | Không |
| 7a | Mật độ năng lượng | 44 kcal/100 mL | 30 đến 55 | Cố định | Bảng thành phần thực phẩm VN [32] | Nguồn | Có |
| 7b | Bù trừ năng lượng | 30% | 15% đến 45% | Đều | Giả định; không có ước lượng Việt Nam | Giả định | Không |
| 8 | Nguy cơ tương đối BMI–bệnh | trên 2 kg/m²: CHD 1,11; đột quỵ thiếu máu 1,12 (1,09–1,15); đột quỵ xuất huyết 1,08 (1,04–1,12) | xem ghi chú | Log-chuẩn | APCSC [33,34] | Nguồn | Có |
| 9 | Tỷ lệ mắc, tử vong, trọng số khuyết tật | GBD 2021, Việt Nam, theo tuổi và giới | — | Beta; gamma | GBD 2021 [25] | Nguồn | Có |
| 9b | Gradient nguy cơ bệnh nền theo ngũ phân vị (chỉ dùng cho độ nhạy) | Cả hai chiều: 1,15 (Q1) giảm còn 0,88 (Q5), và chiều ngược lại | 0,85 đến 1,20 | — | Chưa xác lập chiều ở Việt Nam | Giả định | Không |
| 10 | Chi phí y tế theo ca bệnh | Đái tháo đường 8,0 triệu đồng/bệnh nhân-năm; tim thiếu máu 84,9 triệu/đợt cấp; đột quỵ 10,5 triệu/đợt cấp | −30% đến +100% | Gamma | Le 2017 [35]; Pham 2020 [36]; Pham 2024 [43]; Doãn 2022 [44] | Nguồn | Có |
| 11 | Chi tiêu hộ theo ngũ phân vị | Bình quân 3,0 triệu đồng/người-tháng; tỷ số Q5/Q1 = 3,1 | — | Cố định | VHLSS 2024 [37] | Nguồn | Có |
| 12 | Độ trễ BMI → nguy cơ | 2 năm | 1 đến 5 | Đều | Giả định | Giả định | Không |
| 13 | Suất chiết khấu | 3% | 0%; 5% | Cố định | CHEERS 2022 [39] | Nguồn | Có |

**B.2 Ghi chú cho các tham số không đo trực tiếp**

**#2 Xu hướng tiêu thụ nền.** Kịch bản phản thực tế là yếu tố quyết định lớn nhất đến độ lớn tuyệt đối của mọi kết quả, và là tham số mà protocol ban đầu bỏ trống. Sản lượng bán lẻ đồ uống có đường của Euromonitor tại Việt Nam tăng từ 18 lít lên 66 lít/người giai đoạn 2009–2023, tốc độ khoảng 9,7%/năm. Ngoại suy tốc độ đó đến 2050 là không bảo vệ được: nó hàm ý mức tiêu thụ vượt xa mọi quan sát thị trường. Vì vậy chúng tôi dùng xu hướng trung tâm +2,0%/năm, gần với dự báo tăng trưởng của thị trường đồ uống rộng hơn, và cố ý đặt biên dưới ở 0% để giữ kịch bản "không tăng thêm". *Lý do:* xu hướng nền càng cao thì thuế càng có lợi, nên chọn xu hướng thận trọng là tự làm yếu đi giả thuyết của chính nghiên cứu. *Phương án thay thế:* không cần; đây là lựa chọn thiết kế, không phải lỗ hổng dữ liệu, và phải nêu rõ trong bài vì phản biện sẽ hỏi kịch bản phản thực tế giả định điều gì.

**#3 Khối lượng đồ uống chịu thuế.** Euromonitor báo cáo 66 L/người năm 2023 cho nhóm nước ngọt; tập dữ liệu chúng tôi có không tách tổng này theo nhóm phụ, nên không thể dùng trực tiếp làm khối lượng đồ uống chịu thuế. Giá trị 145 mL/ngày dùng ở trung tâm là khối lượng suy ra khi áp tỷ lệ tiêu thụ trên ngưỡng giả định lên tổng đó, và được mang như một tham số với khoảng 90 đến 220 mL/ngày chứ không phải số đo. Một cơ sở dữ liệu cấp sản phẩm sẽ thay thế nó.

**#11 và #3, ghi chú về cấu trúc chi tiêu.** Giá trị trung bình các nhóm được đặt sao cho bình quân (3,0 triệu đồng/người-tháng) và tỷ số Q5/Q1 (3,1) tái tạo đúng số công bố của VHLSS 2024. Tỷ trọng chi tiêu dành cho đồ uống có đường sau đó được **suy ra** từ sản lượng và giá bán lẻ ngay trong mô hình, thay vì giả định riêng, để nó không thể mâu thuẫn với giả định tiêu thụ. Cách suy ra cho 2,6% ở Q1 và 1,5% ở Q5. Chỉ số Gini dùng cho Kakwani được tính chỉ từ giá trị trung bình các nhóm nên là **cận dưới**, khiến mức lũy thoái ước tính bị kéo về phía không; Gini thu nhập công bố là 0,372. **#3 Tiêu thụ theo tuổi, giới và ngũ phân vị.** Sản lượng bán lẻ bình quân đầu người cho biết mức, không cho biết phân bố. Phân bố theo tuổi và giới lấy từ Điều tra dinh dưỡng toàn quốc 2019–2020, có ghi nhận lượng đồ uống theo nhóm. Phân bố theo ngũ phân vị lấy từ chi tiêu đồ uống trong VHLSS 2024, hiệu chỉnh về tổng sản lượng Euromonitor để hai nguồn nhất quán. Giá trị trung tâm 145 mL/người/ngày được suy ra là 66 lít/năm × 0,80 (tỷ trọng trên ngưỡng) ÷ 365, không quan sát trực tiếp. *Phương án thay thế:* nếu không ánh xạ được nhóm đồ uống của GNS sang nhóm chịu thuế, áp dụng profile tuổi đồng nhất và ghi nhận là hạn chế.

**#4 Tỷ trọng giá xuất xưởng trong giá bán lẻ — ràng buộc chính.** Không có ước lượng công bố nào của Việt Nam. Giá trị này quyết định toàn bộ hiệu ứng giá: với τ = 0,10, *v* = 0,10 và κ = 0,90, tỷ trọng 0,40 cho mức tăng giá bán lẻ 4,0% và tỷ trọng 0,70 cho 6,9% — một khoảng bao trùm phần lớn không gian kết quả khả dĩ. Chúng tôi dùng phân phối tam giác với trung tâm 0,55, suy từ cấu trúc điển hình của chuỗi phân phối hàng tiêu dùng nhanh Việt Nam (giá bán nhà sản xuất, biên bán buôn và bán lẻ, và tầng VAT 10%). Đây là giả định và không có ước lượng Việt Nam. Giá trị sẽ được hiệu chuẩn trực tiếp nếu Bộ Tài chính công bố dự toán thu cho thuế này, vì cơ sở chịu thuế hàm ý bởi dự toán là R/τ và chia cho giá trị bán lẻ của lượng chịu thuế đã trừ VAT sẽ cho ra tỷ trọng; phân tích này không có dự toán đó.

**#5 Mức truyền dẫn.** Mức truyền dẫn đo được đã dao động từ dưới 50% (Berkeley, Chile, Vương quốc Anh) đến gần 100% (Philadelphia, Mexico).[28] Tại Barbados, thuế 10% làm giá đồ uống có đường tăng 5,9% sau sáu tháng, hàm ý mức truyền dẫn khoảng 60%. Hai đánh giá nữa lấy từ văn liệu kinh tế, về thuế nước ngọt của Bồ Đào Nha và Pháp, báo cáo mức truyền dẫn gần đầy đủ vào giá bán lẻ.[29,30] Vì Việt Nam chưa có dữ liệu giá sau thực thi tại thời điểm viết bài, chúng tôi đặt trung tâm hơi dưới mức truyền dẫn đầy đủ và cho phép vượt 100%, điều quan sát được khi doanh nghiệp làm tròn giá lên. *Phương án:* không cần; khoảng giá trị chính là phương án.

**#6 Độ co giãn.** Độ co giãn giá riêng gộp của đồ uống có đường tập trung trong khoảng −1,0 đến −1,4: −1,30 (KTC 95%: −1,09 đến −1,51) trong một phân tích gộp chín nghiên cứu,[42] −1,16 với đồ uống có đường tại Mexico,[21] −1,37 với nước ngọt tại Chile, và −0,79 (khoảng −1,24 đến −0,33) với nước ngọt trong một tổng quan trước đó.[31] Chúng tôi đặt trung tâm −1,20 và cho phép toàn bộ khoảng quan sát. Gradient theo ngũ phân vị là yếu tố yếu nhất: phát hiện nhất quán là độ co giãn lớn hơn ở hộ thu nhập thấp hơn,[21] nhưng độ lớn cho Việt Nam chưa biết, nên gradient 1,4 được áp dụng và kết quả được báo cáo như một phân tích độ nhạy chứ không phải một phát hiện.

**#7b Bù trừ năng lượng.** Một phần năng lượng mất đi từ đồ uống được thay thế từ nguồn khác. Ước lượng công bố rất khác nhau, và lựa chọn này ảnh hưởng đáng kể đến đường BMI. Chúng tôi dùng phân phối đều từ 15% đến 45%, trung tâm 30%, và ghi rõ đây là giả định chứ không phải ước lượng Việt Nam; không có đo lường nào ở Việt Nam và không có giá trị nào từ bối cảnh tương đương mà chúng tôi kiểm chứng được, nên giá trị này không kèm trích dẫn.

**#8 Nguy cơ tương đối.** Từ Nghiên cứu đoàn hệ châu Á–Thái Bình Dương: mỗi 2 kg/m² BMI thấp hơn gắn với nguy cơ đột quỵ thiếu máu cục bộ thấp hơn 12% (KTC 95%: 9–15) và nguy cơ đột quỵ xuất huyết thấp hơn 8% (KTC 95%: 4–12),[33] với ước lượng tương đương cho bệnh mạch vành.[33] Nguy cơ đái tháo đường lấy từ cùng nhóm nghiên cứu.[34] Vì nguy cơ tương đối được áp lên *nhóm* BMI qua phân suất tác động quần thể, chúng tôi chuyển các ước lượng trên 2 đơn vị thành giá trị đặc thù theo nhóm, dùng điểm giữa các ngưỡng châu Á chuẩn (18,5; 23; 25; 30). *Lý do ưu tiên APCSC:* đây là bộ bằng chứng gộp châu Á duy nhất đủ lớn, và dùng ước lượng phương Tây sẽ phóng đại nguy cơ ở một quần thể gầy.

**Mật độ đường của đồ uống chịu thuế.** Giá trị trung tâm 11 g/100 mL không phải giả định: Nguyễn và cộng sự báo cáo 11 g/100 mL với nước ngọt có ga, 9 g với cà phê và trà pha sẵn, 16 g với nước thể thao và tăng lực, và 7 g với nước ép trên thị trường Việt Nam.[17] Nước ngọt có ga chiếm phần lớn sản lượng chịu thuế, nên 11 được dùng làm giá trị trung tâm, và toàn dải theo nhóm (7–16) được khảo sát trong phân tích độ nhạy.

**#9 Tỷ lệ mắc nền theo ngũ phân vị.** GBD 2021 cung cấp tỷ lệ mắc, tỷ lệ hiện mắc và tử vong quốc gia cho cả ba bệnh, và STEPS 2021 cung cấp tỷ lệ hiện mắc đái tháo đường đo được. Không nguồn nào phân tầng theo chi tiêu hộ. Vì vậy ở kịch bản cơ sở chúng tôi áp tỷ lệ quốc gia cho mọi ngũ phân vị, nghĩa là mọi chênh lệch công bằng chỉ phát sinh từ khác biệt về tiêu thụ và phản ứng giá. Chiều của gradient thật chưa được xác lập ở Việt Nam: tỷ lệ mắc và tử vong theo ngũ phân vị không được công bố, và chúng tôi không xác minh được nguồn nào đủ để đặt giá trị trung tâm. Vì vậy chúng tôi chạy phân tích với ba giả định — không gradient, nguy cơ giảm theo chi tiêu, và nguy cơ tăng theo chi tiêu — và báo cáo kết quả công bằng dưới dạng khoảng (Phụ lục F, Hình 3).

**B.3 Điều gì sẽ thay đổi ước tính nhiều nhất**

Trong phân rã phương sai, độ co giãn giá riêng chiếm một nửa phương sai được giải thích, mức truyền dẫn một phần năm và nguy cơ tương đối BMI–đái tháo đường một phần tám; tỷ trọng giá xuất xưởng chiếm 7%, vì nó chỉ đi vào qua mức thay đổi giá và một phần bị mức truyền dẫn hấp thụ. Một gradient nguy cơ bệnh nền được đo (#9b) không làm thay đổi phương sai của DALY, nhưng sẽ xác định kết quả phân bố. Một cơ sở dữ liệu cấp sản phẩm cho đồ uống chịu thuế sẽ thay thế mật độ đường giả định và cho phép mô hình hóa thuế theo gam đường; cả hai đều chưa có ở Việt Nam và bài không tuyên bố chúng.

---

## Phụ lục C. Sai lệch so với kế hoạch soạn ban đầu

Protocol và kế hoạch phân tích được lưu cùng mã sau khi mô hình đã chạy. Phụ lục này ghi lại mọi sai lệch so với kế hoạch soạn ban đầu để người đọc thấy điều gì đã thay đổi và vì sao. Có năm sai lệch.

| # | Sai lệch | Lý do |
|---|---|---|
| C1 | Bỏ kịch bản thuế theo gam đường cân bằng doanh thu (S1b) | Phân bổ sản lượng chịu thuế theo các dải đường cần cơ sở dữ liệu cấp sản phẩm không tồn tại ở Việt Nam; thiếu nó, kịch bản quy về cùng mức tăng giá bình quân với thuế đã ban hành và không phân biệt được |
| C2 | Không giả định gradient kinh tế–xã hội trong tỷ lệ mắc nền ở kịch bản cơ sở | Không có tỷ lệ mắc và tử vong theo ngũ phân vị cho Việt Nam, nên tỷ lệ quốc gia được áp cho mọi nhóm; toàn bộ phân tích được lặp lại với gradient theo từng chiều (Phụ lục B, #9b) và cả ba lần chạy được báo cáo ở Hình 3 |
| C3 | Không thực hiện kiểm toán sản phẩm | Mật độ đường của nhóm chịu thuế lấy từ [17] và nhóm tái định lượng cho S3 là giả định, không phải số đo |
| C4 | Chi phí y tế cho tim thiếu máu cục bộ và đột quỵ được phân bổ từ nghiên cứu đợt cấp | Không có ước lượng Việt Nam về chi phí năm trên mỗi ca hiện mắc cho hai bệnh này |
| C5 | Độ trễ là dịch chuyển hai năm của phân suất tác động, không phải phân bố độ trễ | Không có bằng chứng Việt Nam về hình dạng độ trễ; bước nhảy là lựa chọn thận trọng |

Hai điểm nữa ảnh hưởng đến cách đọc kết quả công bằng. Gradient độ co giãn giữa các ngũ phân vị (Phụ lục B, #6c) là giả định, không phải số đo; và chỉ số tập trung cùng Kakwani dùng Gini tính từ giá trị trung bình các nhóm, tức là cận dưới của bất bình đẳng thực.

## Phụ lục D. Danh mục kiểm tra CHEERS 2022

| # | Mục | Báo cáo ở |
|---|---|---|
| 1 | Tiêu đề | Trang bìa |
| 2 | Tóm tắt | Tóm tắt |
| 3 | Bối cảnh và mục tiêu | Giới thiệu |
| 4 | Kế hoạch phân tích kinh tế y tế | Phương pháp, *Bất định và phân tích độ nhạy*; protocol đã lưu trữ |
| 5 | Quần thể nghiên cứu | Phương pháp, *Thiết kế và tổng quan* |
| 6 | Bối cảnh và địa điểm | Phương pháp, *Thiết kế và tổng quan* |
| 7 | Đối chứng | Phương pháp, *Các kịch bản chính sách*; Bảng 1 |
| 8 | Quan điểm | Phương pháp, *Thiết kế và tổng quan* |
| 9 | Khung thời gian | Phương pháp, *Thiết kế và tổng quan* |
| 10 | Suất chiết khấu | Phương pháp; Phụ lục F |
| 11 | Lựa chọn kết cục | Phương pháp; tóm tắt kết cục ở Giới thiệu |
| 12 | Đo lường kết cục | Phương pháp, *Cấu trúc mô hình* bước 5–7 |
| 13 | Định giá kết cục | Phương pháp bước 7; trọng số khuyết tật từ GBD 2021 |
| 14 | Đo lường và định giá nguồn lực, chi phí | Phương pháp bước 7; Bảng 2 |
| 15 | Tiền tệ, năm giá, quy đổi | Phương pháp, *Thiết kế và tổng quan* |
| 16 | Lý do và mô tả mô hình | Phương pháp, *Cấu trúc mô hình*; Hình 1 |
| 17 | Phân tích và giả định | Phương pháp; Phụ lục B; Phụ lục F |
| 18 | Mô tả tính không đồng nhất | Phương pháp, *Phân tích công bằng*; Kết quả, *Công bằng* |
| 19 | Mô tả tác động phân bố | Phương pháp, *Phân tích công bằng*; Hình 3 |
| 20 | Mô tả bất định | Phương pháp; Kết quả, *Bất định*; Phụ lục F |
| 21 | Cách tiếp cận tham vấn người bệnh và các bên liên quan | Phương pháp, *Kiểm chứng* |
| 22 | Tham số nghiên cứu | Bảng 2; Phụ lục B |
| 23 | Tóm tắt kết quả chính | Kết quả; Bảng 3 |
| 24 | Ảnh hưởng của bất định | Kết quả, *Bất định*; Hình 4 |
| 25 | Ảnh hưởng của tham vấn | Phương pháp, *Kiểm chứng*; Thảo luận, Hạn chế |
| 26 | Phát hiện, hạn chế và diễn giải | Thảo luận |
| 27 | Khả năng khái quát hóa | Thảo luận, *Hàm ý chính sách* |
| 28 | Nguồn tài trợ, xung đột lợi ích, khả năng truy cập dữ liệu | Trang bìa; Tuyên bố xung đột lợi ích; Chia sẻ dữ liệu |

---

## Phụ lục E. Những gì đã và chưa được thẩm định

**E.1 Đã kiểm tra.** Mỗi bước của mô hình có kiểm thử đơn vị với đầu vào và đầu ra tính tay. Bảo toàn dân số được kiểm tra ở mọi chu kỳ: không ai rời quần thể ngoài đường tử vong, và số còn sống cộng số đã chết bằng dân số ban đầu ở mọi chu kỳ. Điều kiện cực biên được kiểm tra: thuế bằng không trả về đúng kịch bản nền, độ co giãn bằng không trả về đúng kịch bản nền, và một mức thuế đủ lớn để triệt tiêu tiêu thụ không tạo ra lượng âm hay lỗi chia.

**E.2 So sánh nền.** Tỷ lệ hiện mắc do chính mô hình tạo ra ở cuối khung phân tích được so với nguồn mà các tham số bệnh lấy từ đó, trên cùng cơ cấu tuổi 2027: 5,1% so với 6,2% với đái tháo đường type 2, 0,4% so với 1,6% với bệnh tim thiếu máu cục bộ, và 1,2% so với 1,9% với đột quỵ (GBD 2021). Đái tháo đường, chiếm 89% số ca tránh được, là gần nhất. Khoảng cách ở hai bệnh tim mạch phát sinh từ việc khởi đầu năm 2027 không có tồn lưu hiện mắc và áp tỷ lệ tử vong ca bệnh cao cho ca mới; điều này được ghi ở phần Hạn chế và ảnh hưởng đến mức số năm sống với khuyết tật, không ảnh hưởng đến chiều của khác biệt tránh được.

**E.3 Chưa kiểm tra.** Hai kiểm tra đã không được thực hiện và bài không tuyên bố chúng. Không có so sánh ngoại với nghiên cứu mô hình hóa Việt Nam trước đó,[17], vì nghiên cứu đó báo cáo kết cục khác trên cấu trúc mô hình khác và so sánh sẽ không tách được sai số mô hình. Mã chưa được một lập trình viên độc lập rà soát. Các kiểm thử đơn vị, điều kiện cực biên ở E.1 và so sánh nền ở E.2 là toàn bộ bảo đảm kỹ thuật phía sau kết quả.

## Phụ lục F. Các phân tích độ nhạy đã thực hiện

**F.1 Phân tích xác suất.** 5.000 lần mô phỏng Monte Carlo, lấy mẫu độc lập từ các phân phối ở Phụ lục B, hạt giống cố định (20261101), báo cáo trung vị và khoảng bất định 95%. Đóng góp của từng tham số vào phương sai của DALY tránh được được tính từ một mô hình tuyến tính của 5.000 lần rút trên các tham số đã lấy mẫu, dùng bình phương tương quan bán phần chia cho phương sai được giải thích; mô hình đó giải thích 94% biến thiên.

**F.2 Phân tích ngưỡng.** Lưới trên tỷ trọng giá xuất xưởng (0,30 đến 0,85) và mức truyền dẫn (0,30 đến 1,50), mô hình chạy lại tại từng điểm, xác định các tổ hợp mà tại đó lợi ích sức khỏe không phân biệt được với không. Lưới được lưu ở `output/threshold_grid.csv`.

**F.3 Lưới độ co giãn.** Độ co giãn giá riêng từ −0,3 đến −2,0 theo bước 0,1, các tham số khác giữ ở trung tâm, để xác định điểm mà lợi ích sức khỏe đổi dấu.

**F.5 Tái định lượng.** S3 chạy ở mức 25% tại trung tâm; các mức 10% và 50% được báo cáo trong bài.

**F.6 Độ nhạy cấu trúc một chiều.** Suất chiết khấu 0% và 5%; mức truyền dẫn 0,50; 0,90 và 1,30; độ co giãn giá riêng −0,80; −1,20 và −1,80; khung 2036, 2050 và 2100; và một lần chạy khởi đầu từ tồn lưu hiện mắc GBD 2021 thay vì từ không. Ở giá trị trung tâm, lợi ích sức khỏe là 39.894 và 18.724 DALY ở suất chiết khấu 0% và 5%; 13.784 và 35.710 ở mức truyền dẫn 0,50 và 1,30; 16.534 và 37.075 ở độ co giãn −0,80 và −1,80; 7.822, 24.767 và 53.509 ở khung 10 năm, 2050 và 2100; và 22.632 khi khởi tạo tồn lưu hiện mắc từ GBD 2021. Lưu ở `output/sensitivity.csv`.

**F.7 Gradient nguy cơ bệnh nền.** Toàn bộ phân tích xác suất được lặp lại trên cùng 5.000 lần rút dưới hai gradient kinh tế–xã hội, nguy cơ giảm theo chi tiêu (1,15 ở Q1 xuống 0,88 ở Q5) và nguy cơ tăng theo chi tiêu (0,88 ở Q1 lên 1,15 ở Q5). Trung vị tỷ số Q1/Q5 dịch từ 0,77 lên 0,99 ở trường hợp đầu và xuống 0,60 ở trường hợp sau, chỉ số tập trung từ 0,047 xuống −0,002 và lên 0,097; chỉ số Kakwani không đổi vì chỉ phụ thuộc vào khoản thuế phải trả. Lưu ở `output/psa_gradient.csv`.

**F.8 Các phân tích không thực hiện.** Mô hình cân nặng tĩnh, lưới truyền dẫn đầy đủ kết hợp diễn giải rộng và hẹp phạm vi chịu thuế, và độ trễ phân bố đã được xem xét và không thực hiện. Không kết quả nào của chúng được báo cáo.

## Phụ lục G. Mã và khả năng tái lập

**G.1 Môi trường.** R phiên bản 4.6.1, chỉ dùng R gốc, không có gói phụ thuộc. Mô hình, phân tích xác suất và các hình chạy được trên một bản cài R sạch; các tệp DOCX được tạo bằng Python 3 và `python-docx`.

**G.2 Cấu trúc kho lưu trữ.** `model/` chứa mô hình (`pmslt_model.R`), hồ sơ ngũ phân vị (`vhlss.R`), phân tích xác suất (`psa.R`, `psa_all.R`, `psa_gradient.R`) và script ghi mọi con số trong bản thảo (`fill_results.R`). `data/` chứa tham số đầu vào và nhật ký sàng lọc. `output/` chứa ma trận rút, các lần rút, lưới ngưỡng và lần chạy có gradient. `Ban_thao/` chứa bản nguồn bản thảo, script vẽ hình và các tệp DOCX đã tạo.

**G.3 Tái lập.** Kết quả chính được tái lập qua năm bước, mỗi bước ghi đầu ra vào `output/`:

```
Rscript model/psa_all.R        # 5.000 lần rút, hạt giống 20261101 -> psa_results.csv, psa_draws.csv
Rscript model/psa_gradient.R   # cùng các lần rút, ba gradient bệnh -> psa_gradient.csv
Rscript model/sensitivity.R    # các lần chạy cấu trúc một chiều -> sensitivity.csv
Rscript model/fill_results.R   # mọi con số trong bản thảo -> results.json
Rscript Ban_thao/Figures/make_figures.R   # Hình 1-4
```

Hạt giống cố định ở 20261101, và ma trận rút được công bố ở `output/psa_draws.csv` để kiểm tra kết quả xác suất mà không cần chạy lại bước lấy mẫu. Toàn bộ phân tích mất khoảng 40 phút trên một máy xách tay; riêng kết quả tất định dưới một phút. Kho lưu trữ công khai tại https://doi.org/10.5281/zenodo.23852908 theo giấy phép MIT.


---
