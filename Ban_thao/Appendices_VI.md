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

Các tập rộng không giới hạn quốc gia trả về 576 bản ghi ở PubMed, 506 ở Europe PMC, 2.961 ở OpenAlex, 1.526 ở Cochrane CENTRAL và 21 ở RePEc. Các tập này được dùng để lấy giá trị tham số — độ co giãn giá, mức truyền dẫn, nguy cơ tương đối và chi phí — chứ không sàng lọc từng bản ghi, vì nghiên cứu cần ước lượng từ bất kỳ bối cảnh so sánh được nào, không phải một tổng quan hệ thống về tác động của thuế.

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

*Về tham số.* Độ co giãn, mức truyền dẫn, nguy cơ tương đối và chi phí đều có từ bối cảnh so sánh được nhưng không có từ Việt Nam, ngoại trừ ước lượng chi phí đái tháo đường.[34,35] Đây là nguồn gốc của hai ràng buộc chính được nhận diện ở Phụ lục B: tỷ trọng giá xuất xưởng trong giá bán lẻ, và tỷ lệ mắc bệnh theo ngũ phân vị.

**A.9 Duy trì nhật ký**

Nhật ký sàng lọc, lý do loại ở bước toàn văn, nhật ký xác minh ở A.7 và ngày tìm kiếm được lưu cùng protocol tại https://doi.org/10.5281/zenodo.23852908. Mọi chuỗi bị sửa sau khi đăng ký được ghi ở Phụ lục C.

---

## Phụ lục B. Nhật ký bằng chứng tham số

Mỗi tham số một dòng. Cột "Loại" phân biệt giá trị lấy từ nguồn công bố, giá trị suy ra bằng số học từ dữ liệu công bố, và giả định không có cơ sở thực nghiệm trực tiếp. Cột cuối ghi khả năng điền từ dữ liệu hiện có (có / một phần / không); khi là *không* hoặc *một phần*, phần ghi chú nêu phương án thay thế.

**B.1 Bảng tóm tắt**

| # | Tham số | Giá trị trung tâm đề xuất | Khoảng bất định | Phân phối | Nguồn | Loại | Khả thi |
|---|---|---|---|---|---|---|---|
| 1 | Dân số theo tuổi và ngũ phân vị, 2027–2050 | Dự báo TCTK; tổng 2027 ≈104 triệu | — | Cố định | Dự báo dân số 2024–2074 [27] | Nguồn | Có |
| 2 | Xu hướng tiêu thụ nền | +2,0%/năm | 0 đến +4,0% | Đều | CAGR Euromonitor 2009–2023 [6] | Suy ra | Một phần |
| 3 | Tiêu thụ theo tuổi, giới, ngũ phân vị | 145 mL/người/ngày | 90 đến 220 | Gamma | Euromonitor [6]; GNS 2019–20 [28]; VHLSS [36] | Suy ra | Một phần |
| 4 | Tỷ trọng đồ uống chịu thuế trên 5 g/100 mL | 0,80 | 0,60 đến 0,95 | Beta(8;2) | Giả định; không đo | Giả định | Không |
| 5 | Tỷ trọng giá xuất xưởng trong giá bán lẻ | 0,55 | 0,40 đến 0,70 | Tam giác | Không có nguồn Việt Nam; cấu trúc biên FMCG | Giả định | **Không** |
| 6 | Mức truyền dẫn | 0,90 | 0,50 đến 1,30 | Tam giác | World Bank 2020 [29]; Barbados, Mexico [40] | Nguồn (nước ngoài) | Một phần |
| 7a | Độ co giãn giá riêng | −1,20 | −0,80 đến −1,80 | Log-chuẩn trên \|ε\| | Andreyeva [30]; Cabrera Escobar [24]; Colchero [21] | Nguồn | Một phần |
| 7b | Độ co giãn giá chéo sang đồ uống không chịu thuế | +0,35 | +0,10 đến +0,65 | Log-chuẩn | Hệ thống cầu Chile và Mexico [21] | Nguồn | Một phần |
| 7c | Gradient độ co giãn theo ngũ phân vị | Q1 = 1,4 × Q5 | 1,0 đến 1,8 | — | Colchero [21] | Suy ra | Không |
| 8a | Mật độ năng lượng | 44 kcal/100 mL | 30 đến 55 | Cố định | Bảng thành phần thực phẩm VN [31] | Nguồn | Có |
| 8b | Bù trừ năng lượng | 30% | 15% đến 45% | Đều | Văn liệu can thiệp [24] | Giả định | Không |
| 9 | Nguy cơ tương đối BMI–bệnh | trên 2 kg/m²: CHD 1,11; đột quỵ thiếu máu 1,12 (1,09–1,15); đột quỵ xuất huyết 1,08 (1,04–1,12) | xem ghi chú | Log-chuẩn | APCSC [32,33] | Nguồn | Có |
| 10 | Tỷ lệ mắc, tử vong, trọng số khuyết tật | GBD 2021, Việt Nam, theo tuổi và giới | — | Beta; gamma | GBD 2021 [26] | Nguồn | Có |
| 10b | Gradient nguy cơ bệnh nền theo ngũ phân vị (chỉ dùng cho độ nhạy) | 1,15 (Q1) đến 0,88 (Q5) | 1,00 đến 1,25 | — | Chỉ có hướng; chưa đo ở Việt Nam | Giả định | Không |
| 11 | Chi phí y tế theo ca bệnh | Đái tháo đường 8,0 triệu đồng/bệnh nhân-năm; tim thiếu máu 84,9 triệu/đợt cấp; đột quỵ 10,5 triệu/đợt cấp | −30% đến +100% | Gamma | Le 2017 [34]; Pham 2020 [35]; Pham 2024 [41]; Doãn 2022 [42] | Nguồn | Có |
| 12 | Chi tiêu hộ theo ngũ phân vị | Bình quân 3,0 triệu đồng/người-tháng; tỷ số Q5/Q1 = 3,1 | — | Cố định | VHLSS 2024 [36] | Nguồn | Có |
| 13 | Độ trễ BMI → nguy cơ | 2 năm | 1 đến 5 | Đều | Giả định | Giả định | Không |
| 14 | Suất chiết khấu | 3% | 0%; 5% | Cố định | CHEERS 2022 [38] | Nguồn | Có |

**B.2 Ghi chú cho các tham số không đo trực tiếp**

**#2 Xu hướng tiêu thụ nền.** Kịch bản phản thực tế là yếu tố quyết định lớn nhất đến độ lớn tuyệt đối của mọi kết quả, và là tham số mà protocol ban đầu bỏ trống. Sản lượng bán lẻ đồ uống có đường của Euromonitor tại Việt Nam tăng từ 18 lít lên 66 lít/người giai đoạn 2009–2023, tốc độ khoảng 9,7%/năm. Ngoại suy tốc độ đó đến 2050 là không bảo vệ được: nó hàm ý mức tiêu thụ vượt xa mọi quan sát thị trường. Vì vậy chúng tôi dùng xu hướng trung tâm +2,0%/năm, gần với dự báo tăng trưởng của thị trường đồ uống rộng hơn, và cố ý đặt biên dưới ở 0% để giữ kịch bản "không tăng thêm". *Lý do:* xu hướng nền càng cao thì thuế càng có lợi, nên chọn xu hướng thận trọng là tự làm yếu đi giả thuyết của chính nghiên cứu. *Phương án thay thế:* không cần; đây là lựa chọn thiết kế, không phải lỗ hổng dữ liệu, và phải nêu rõ trong bài vì phản biện sẽ hỏi kịch bản phản thực tế giả định điều gì.

**#12 và #3, ghi chú về cấu trúc chi tiêu.** Giá trị trung bình các nhóm được đặt sao cho bình quân (3,0 triệu đồng/người-tháng) và tỷ số Q5/Q1 (3,1) tái tạo đúng số công bố của VHLSS 2024. Tỷ trọng chi tiêu dành cho đồ uống có đường sau đó được **suy ra** từ sản lượng và giá bán lẻ ngay trong mô hình, thay vì giả định riêng, để nó không thể mâu thuẫn với giả định tiêu thụ. Cách suy ra cho 2,6% ở Q1 và 1,5% ở Q5. Chỉ số Gini dùng cho Kakwani được tính chỉ từ giá trị trung bình các nhóm nên là **cận dưới**, khiến mức lũy thoái ước tính bị kéo về phía không; Gini thu nhập công bố là 0,372. **#3 Tiêu thụ theo tuổi, giới và ngũ phân vị.** Sản lượng bán lẻ bình quân đầu người cho biết mức, không cho biết phân bố. Phân bố theo tuổi và giới lấy từ Điều tra dinh dưỡng toàn quốc 2019–2020, có ghi nhận lượng đồ uống theo nhóm. Phân bố theo ngũ phân vị lấy từ chi tiêu đồ uống trong VHLSS 2024, hiệu chỉnh về tổng sản lượng Euromonitor để hai nguồn nhất quán. Giá trị trung tâm 145 mL/người/ngày được suy ra là 66 lít/năm × 0,80 (tỷ trọng trên ngưỡng) ÷ 365, không quan sát trực tiếp. *Phương án thay thế:* nếu không ánh xạ được nhóm đồ uống của GNS sang nhóm chịu thuế, áp dụng profile tuổi đồng nhất và ghi nhận là hạn chế.

**#5 Tỷ trọng giá xuất xưởng trong giá bán lẻ — ràng buộc chính.** Không có ước lượng công bố nào của Việt Nam. Giá trị này quyết định toàn bộ hiệu ứng giá: với τ = 0,10, *v* = 0,10 và κ = 0,90, tỷ trọng 0,40 cho mức tăng giá bán lẻ 4,0% và tỷ trọng 0,70 cho 6,9% — một khoảng bao trùm phần lớn không gian kết quả khả dĩ. Chúng tôi đề xuất phân phối tam giác với trung tâm 0,55, suy từ cấu trúc điển hình của chuỗi phân phối hàng tiêu dùng nhanh Việt Nam (giá bán nhà sản xuất, biên bán buôn và bán lẻ, và tầng VAT 10%), và đề xuất **hiệu chuẩn nó bằng thực nghiệm** thay vì để là giả định:

> **Quy trình hiệu chuẩn.** Nếu Bộ Tài chính công bố dự toán thu từ thuế đồ uống có đường cho ngân sách 2027, cơ sở chịu thuế hàm ý bởi dự toán đó là R/τ. Chia cho giá trị bán lẻ ước tính của lượng chịu thuế, đã trừ VAT, cho ra ước lượng trực tiếp của tỷ trọng xuất xưởng. Hai dự toán công bố độc lập, hoặc một dự toán cộng với giá trị thị trường của lượng chịu thuế, là đủ. Bước này biến tham số yếu nhất của mô hình thành tham số được hiệu chuẩn, và là nhiệm vụ dữ liệu có giá trị cao nhất của nghiên cứu.

*Phương án nếu không có dự toán:* giữ giả định tam giác, báo cáo phân tích ngưỡng (các tổ hợp truyền dẫn và tỷ trọng mà tại đó lợi ích sức khỏe không phân biệt được với không), và nêu trong Hạn chế rằng hiệu ứng giá là do giả định chứ không phải do ước lượng.

**#6 Mức truyền dẫn.** Mức truyền dẫn đo được đã dao động từ dưới 50% (Berkeley, Chile, Vương quốc Anh) đến gần 100% (Philadelphia, Mexico).[29] Tại Barbados, thuế 10% làm giá đồ uống có đường tăng 5,9% sau sáu tháng, hàm ý mức truyền dẫn khoảng 60%. Vì Việt Nam chưa có dữ liệu giá sau thực thi tại thời điểm viết bài, chúng tôi đặt trung tâm hơi dưới mức truyền dẫn đầy đủ và cho phép vượt 100%, điều quan sát được khi doanh nghiệp làm tròn giá lên. *Phương án:* không cần; khoảng giá trị chính là phương án.

**#7 Độ co giãn.** Độ co giãn giá riêng gộp của đồ uống có đường tập trung trong khoảng −1,0 đến −1,4: −1,30 (KTC 95%: −1,09 đến −1,51) trong một phân tích gộp chín nghiên cứu,[24] −1,16 với đồ uống có đường tại Mexico,[21] −1,37 với nước ngọt tại Chile, và −0,79 (khoảng −1,24 đến −0,33) với nước ngọt trong một tổng quan trước đó.[30] Chúng tôi đặt trung tâm −1,20 và cho phép toàn bộ khoảng quan sát. Gradient theo ngũ phân vị là yếu tố yếu nhất: phát hiện nhất quán là độ co giãn lớn hơn ở hộ thu nhập thấp hơn,[21] nhưng độ lớn cho Việt Nam chưa biết, nên gradient 1,4 được áp dụng và kết quả được báo cáo như một phân tích độ nhạy chứ không phải một phát hiện.

**#8b Bù trừ năng lượng.** Một phần năng lượng mất đi từ đồ uống được thay thế từ nguồn khác. Ước lượng công bố rất khác nhau, và lựa chọn này ảnh hưởng đáng kể đến đường BMI. Chúng tôi dùng phân phối đều từ 15% đến 45%, trung tâm 30%, và ghi rõ đây là giả định chứ không phải ước lượng Việt Nam. *Phương án thay thế:* báo cáo song song độ nhạy với hệ số quy đổi tĩnh, để người đọc thấy kết quả phụ thuộc bao nhiêu vào bước này.

**#9 Nguy cơ tương đối.** Từ Nghiên cứu đoàn hệ châu Á–Thái Bình Dương: mỗi 2 kg/m² BMI thấp hơn gắn với nguy cơ đột quỵ thiếu máu cục bộ thấp hơn 12% (KTC 95%: 9–15) và nguy cơ đột quỵ xuất huyết thấp hơn 8% (KTC 95%: 4–12),[32] với ước lượng tương đương cho bệnh mạch vành.[32] Nguy cơ đái tháo đường lấy từ cùng nhóm nghiên cứu.[33] Vì nguy cơ tương đối được áp lên *nhóm* BMI qua phân suất tác động quần thể, chúng tôi chuyển các ước lượng trên 2 đơn vị thành giá trị đặc thù theo nhóm, dùng điểm giữa các ngưỡng châu Á chuẩn (18,5; 23; 25; 30). *Lý do ưu tiên APCSC:* đây là bộ bằng chứng gộp châu Á duy nhất đủ lớn, và dùng ước lượng phương Tây sẽ phóng đại nguy cơ ở một quần thể gầy.

**Mật độ đường của đồ uống chịu thuế.** Giá trị trung tâm 11 g/100 mL không phải giả định: Nguyễn và cộng sự báo cáo 11 g/100 mL với nước ngọt có ga, 9 g với cà phê và trà pha sẵn, 16 g với nước thể thao và tăng lực, và 7 g với nước ép trên thị trường Việt Nam.[17] Nước ngọt có ga chiếm phần lớn sản lượng chịu thuế, nên 11 được dùng làm giá trị trung tâm, và toàn dải theo nhóm (7–16) được khảo sát trong phân tích độ nhạy.

**#10 Tỷ lệ mắc nền theo ngũ phân vị.** GBD 2021 cung cấp tỷ lệ mắc, tỷ lệ hiện mắc và tử vong quốc gia cho cả ba bệnh, và STEPS 2021 cung cấp tỷ lệ hiện mắc đái tháo đường đo được. Không nguồn nào phân tầng theo chi tiêu hộ. Vì vậy chúng tôi áp tỷ lệ quốc gia cho **mọi** ngũ phân vị và giả định **không có** gradient kinh tế–xã hội trong tỷ lệ mắc nền. Đây là đơn giản hóa có chủ đích: mọi chênh lệch công bằng trong mô hình chỉ phát sinh từ khác biệt về tiêu thụ và phản ứng giá, không bao giờ từ một gradient bệnh giả định. Một gradient thật trong nguy cơ bệnh sẽ không được phản ánh.

**B.3 Thứ tự các nhiệm vụ dữ liệu, theo giá trị**

1. Hiệu chuẩn tỷ trọng giá xuất xưởng (#5) từ một dự toán ngân sách đã công bố — giá trị cao nhất, vì nó đặt quy mô cho mọi kết quả.
2. Hoàn tất kiểm toán sản phẩm (#4) — đặt cơ sở thuế và nhóm ứng viên tái định lượng cho S3.
3. Ánh xạ nhóm đồ uống của GNS 2019–2020 sang nhóm chịu thuế (#3).
4. Lấy ước lượng chi phí Việt Nam cho bệnh tim thiếu máu cục bộ và đột quỵ (#11); chi phí đái tháo đường đã có.
5. Chốt xu hướng nền (#2) và ghi quyết định vào nhật ký sai lệch nếu khác protocol đã đăng ký.

---

## Phụ lục C. Sai lệch so với kế hoạch soạn ban đầu

Protocol và kế hoạch phân tích được lưu cùng mã sau khi mô hình đã chạy. Phụ lục này ghi lại mọi sai lệch so với kế hoạch soạn ban đầu để người đọc thấy điều gì đã thay đổi và vì sao. Có năm sai lệch.

| # | Sai lệch | Lý do |
|---|---|---|
| C1 | Bỏ kịch bản thuế theo gam đường cân bằng doanh thu (S1b) | Phân bổ sản lượng chịu thuế theo các dải đường cần cơ sở dữ liệu cấp sản phẩm không tồn tại ở Việt Nam; thiếu nó, kịch bản quy về cùng mức tăng giá bình quân với thuế đã ban hành và không phân biệt được |
| C2 | Không giả định gradient kinh tế–xã hội trong tỷ lệ mắc nền ở kịch bản cơ sở | Không có tỷ lệ mắc và tử vong theo ngũ phân vị cho Việt Nam, nên tỷ lệ quốc gia được áp cho mọi nhóm; toàn bộ phân tích được lặp lại với một gradient giả định (Phụ lục B, #10b) và hai lần chạy được báo cáo ở Hình 3 |
| C3 | Không thực hiện kiểm toán sản phẩm | Tỷ trọng đồ uống chịu thuế trên ngưỡng là giả định (Phụ lục B, #4), không phải số đo |
| C4 | Chi phí y tế cho tim thiếu máu cục bộ và đột quỵ được phân bổ từ nghiên cứu đợt cấp | Không có ước lượng Việt Nam về chi phí năm trên mỗi ca hiện mắc cho hai bệnh này |
| C5 | Độ trễ là dịch chuyển hai năm của phân suất tác động, không phải phân bố độ trễ | Không có bằng chứng Việt Nam về hình dạng độ trễ; bước nhảy là lựa chọn thận trọng |

Hai điểm nữa ảnh hưởng đến cách đọc kết quả công bằng. Gradient độ co giãn giữa các ngũ phân vị (Phụ lục B, #7c) là giả định, không phải số đo; và chỉ số tập trung cùng Kakwani dùng Gini tính từ giá trị trung bình các nhóm, tức là cận dưới của bất bình đẳng thực.

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

**E.1 Đã kiểm tra.** Mỗi bước của mô hình có kiểm thử đơn vị với đầu vào và đầu ra tính tay. Bảo toàn dân số được kiểm tra trong bảng sống: không ai rời quần thể ngoài đường tử vong, và số còn sống cộng số đã chết bằng dân số ban đầu ở mọi chu kỳ. Điều kiện cực biên được kiểm tra: thuế bằng không trả về đúng kịch bản nền, độ co giãn bằng không trả về đúng kịch bản nền, và một mức thuế đủ lớn để triệt tiêu tiêu thụ không tạo ra lượng âm hay lỗi chia.

**E.2 Chưa kiểm tra.** Ba kiểm tra dự kiến đã không được thực hiện và bài không tuyên bố chúng. Tỷ lệ hiện mắc nền của mô hình chưa được đối chiếu với GBD hoặc STEPS, vì bảng sống không làm quần thể già đi nên so sánh mức sẽ không có ý nghĩa. Không có so sánh ngoại với nghiên cứu mô hình hóa Việt Nam trước đó,[17] vì nghiên cứu đó báo cáo kết cục khác trên cấu trúc khác. Mã chưa được một lập trình viên độc lập rà soát. Các kiểm thử đơn vị và điều kiện cực biên ở E.1 là toàn bộ bảo đảm kỹ thuật phía sau kết quả.

## Phụ lục F. Các phân tích độ nhạy đã thực hiện

**F.1 Phân tích xác suất.** 5.000 lần mô phỏng Monte Carlo, lấy mẫu độc lập từ các phân phối ở Phụ lục B, hạt giống cố định (20261101), báo cáo trung vị và khoảng bất định 95%.

**F.2 Phân tích ngưỡng.** Lưới trên tỷ trọng giá xuất xưởng (0,30 đến 0,85) và mức truyền dẫn (0,30 đến 1,50), mô hình chạy lại tại từng điểm, xác định các tổ hợp mà tại đó lợi ích sức khỏe không phân biệt được với không. Lưới được lưu ở `output/threshold_grid.csv`.

**F.3 Lưới độ co giãn.** Độ co giãn giá riêng từ −0,3 đến −2,0 theo bước 0,1, các tham số khác giữ ở trung tâm, để xác định điểm mà lợi ích sức khỏe đổi dấu.

**F.4 Biến thể cơ sở thuế.** Tỷ trọng đồ uống chịu thuế đặt ở 0,60 và 0,95, bao quanh giá trị giả định 0,80.

**F.5 Tái định lượng.** S3 chạy ở mức 25% tại trung tâm; các mức 10% và 50% được báo cáo trong bài.

**F.6 Gradient nguy cơ bệnh nền.** Toàn bộ phân tích xác suất được lặp lại với gradient kinh tế–xã hội trong tỷ lệ mắc nền, 1,15 ở Q1 giảm xuống 0,88 ở Q5, trên cùng 5.000 lần lấy mẫu. Chỉ số tập trung của DALY tránh được dịch từ trung vị 0,047 xuống −0,002 và tỷ số Q1/Q5 từ 0,77 lên 0,99, còn chỉ số Kakwani không đổi vì chỉ phụ thuộc vào thuế phải trả. Hai lần chạy được trình bày cạnh nhau ở Hình 3 và lưu ở `output/psa_gradient.csv`.

**F.7 Các phân tích không thực hiện.** Mô hình cân nặng tĩnh, bộ độ co giãn thấp và cao, lưới truyền dẫn đầy đủ kết hợp diễn giải rộng và hẹp phạm vi chịu thuế, và độ trễ phân bố đã được dự kiến và không thực hiện. Không kết quả nào của chúng được báo cáo.

## Phụ lục G. Mã và khả năng tái lập

**G.1 Môi trường.** R phiên bản 4.6.1, chỉ dùng R gốc, không có gói phụ thuộc. Mô hình, phân tích xác suất và các hình chạy được trên một bản cài R sạch; các tệp DOCX được tạo bằng Python 3 và `python-docx`.

**G.2 Cấu trúc kho lưu trữ.** `model/` chứa mô hình (`pmslt_model.R`), hồ sơ ngũ phân vị (`vhlss.R`), phân tích xác suất (`psa.R`, `psa_all.R`, `psa_gradient.R`) và script ghi mọi con số trong bản thảo (`fill_results.R`). `data/` chứa tham số đầu vào và nhật ký sàng lọc. `output/` chứa ma trận rút, các lần rút, lưới ngưỡng và lần chạy có gradient. `Ban_thao/` chứa bản nguồn bản thảo, script vẽ hình và các tệp DOCX đã tạo.

**G.3 Tái lập.** Kết quả chính được tái lập qua bốn bước, mỗi bước ghi đầu ra vào `output/`:

```
Rscript model/psa_all.R        # 5.000 lần rút, hạt giống 20261101 -> psa_results.csv, psa_draws.csv
Rscript model/psa_gradient.R   # cùng các lần rút với gradient bệnh -> psa_gradient.csv
Rscript model/fill_results.R   # mọi con số trong bản thảo -> results.json
Rscript Ban_thao/Figures/make_figures.R   # Hình 1-4
```

Hạt giống cố định ở 20261101, và ma trận rút được công bố ở `output/psa_draws.csv` để kiểm tra kết quả xác suất mà không cần chạy lại bước lấy mẫu. Toàn bộ phân tích mất khoảng 40 phút trên một máy xách tay; riêng kết quả tất định dưới một phút. Kho lưu trữ công khai tại https://doi.org/10.5281/zenodo.23852908 theo giấy phép MIT.


---
