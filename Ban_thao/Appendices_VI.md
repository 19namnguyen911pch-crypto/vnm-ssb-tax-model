## Phụ lục A. Tìm kiếm bằng chứng

**A.1 Các câu hỏi mà cuộc tìm kiếm phải trả lời**

Ba, theo thứ tự quan trọng. (i) Đã có ai mô hình hóa đúng mức thuế đồ uống có đường mà Việt Nam đã ban hành, hoặc hệ quả phân bố của nó, chưa? (ii) Giá trị tham số tốt nhất hiện có cho các bước giá, cầu, năng lượng và nguy cơ của mô hình là gì, cho Việt Nam hoặc cho bối cảnh so sánh được? (iii) Bản thân văn bản pháp luật nói gì? Câu hỏi thứ ba được trả lời từ nguồn pháp lý gốc và ghi nhật ký riêng ở A.7, vì một mô hình thuế dựng trên mô tả thứ cấp của luật là mô hình dựng trên sai cơ sở.

**A.2 Nguồn**

| Nguồn | Phạm vi | Mục đích |
|---|---|---|
| PubMed/MEDLINE | Y sinh và sức khỏe công cộng | Nghiên cứu tác động sức khỏe, dịch tễ, nguy cơ |
| Scopus | Đa ngành | Bắt các tạp chí kinh tế và chính sách không có trong MEDLINE |
| Truy vết trích dẫn, xuôi và ngược | Nghiên cứu trích dẫn, hoặc được trích dẫn bởi, mỗi bản ghi được đưa vào | Bắt văn liệu mà tìm theo từ khóa bỏ sót |
| Cochrane Library (CDSR và CENTRAL) | Tổng quan hệ thống và thử nghiệm có đối chứng | Tổng quan về hiệu quả thuế, bằng chứng thử nghiệm về giá và tiêu thụ |
| RePEc/IDEAS | Working paper và tạp chí kinh tế | Độ co giãn, truyền dẫn, phân tích phúc lợi |
| Google Scholar | Tài liệu xám và không được chỉ mục | Luận văn, working paper, học thuật tiếng Việt |
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

*Scopus:*

```
TITLE-ABS-KEY(("sugar-sweetened beverage" OR "sugar sweetened beverage"
 OR "sugary drink" OR "soft drink" OR "carbonated beverage" OR "soda")
 AND (tax OR taxation OR excise OR "fiscal policy")
 AND ("Viet Nam" OR Vietnam))
```

*Cochrane Library* (CDSR và CENTRAL; Cochrane dùng các tập đánh số dòng):

```
#1 ("sugar-sweetened beverage" OR "sugar sweetened beverage" OR "sugary drink"
 OR "soft drink" OR "carbonated beverage" OR soda):ti,ab,kw
#2 (tax OR taxation OR excise OR "fiscal policy" OR "price elasticity"):ti,ab,kw
#3 ("Viet Nam" OR Vietnam):ti,ab,kw
#4 #1 AND #2
#5 #4 AND #3
```

Tập #4 được chạy không giới hạn quốc gia vì văn liệu tổng quan và thử nghiệm về thuế đồ uống có đường rất mỏng và gần như toàn bộ không phải của Việt Nam; #5 tách riêng tập con Việt Nam.

*RePEc/IDEAS* (tìm nâng cao EconPapers, theo tiêu đề và tóm tắt):

```
(sugar-sweetened OR "soft drink" OR sugary OR soda)
AND (tax OR taxation OR excise OR "fiscal policy")
AND (Vietnam OR "Viet Nam" OR "developing countr*" OR Asia)
```

IDEAS chỉ hỗ trợ cú pháp Boolean hạn chế, nên tìm kiếm được bổ sung bằng một truy vấn giới hạn tên miền, `site:ideas.repec.org "sugar-sweetened" tax`, chạy trên Google Scholar và Google.

*Truy vết trích dẫn.* Danh mục tài liệu tham khảo của mọi nghiên cứu được đưa vào được sàng lọc thủ công, và chức năng "được trích dẫn bởi" của Scopus và Google Scholar được dùng cho hai phân tích Việt Nam và cho từng tổng quan hệ thống được đưa vào.


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

**A.5 Sàng lọc**

Các bản ghi được loại trùng, sàng lọc theo tiêu đề và tóm tắt, sau đó theo toàn văn. Một mẫu ngẫu nhiên 20% được hai người sàng lọc độc lập, bất đồng được giải quyết bằng thảo luận và ghi lại hệ số kappa Cohen. Khi mức đồng thuận đạt yêu cầu, phần còn lại do một người sàng lọc, với người thứ hai kiểm tra mọi bản ghi đề xuất loại. Lý do loại ở bước toàn văn được ghi và đếm.

**A.6 Sơ đồ dòng**

Các tìm kiếm PubMed đã được chạy và có số: tập Việt Nam trả về **2 bản ghi**, tập rộng về thuế đồ uống có đường không giới hạn quốc gia trả về **576 bản ghi**. Các cơ sở dữ liệu còn lại được tìm bằng chuỗi ở A.3; số bản ghi, số loại trùng và lý do loại ở bước toàn văn được duy trì trong nhật ký sàng lọc và nộp kèm protocol. Vì tập Việt Nam chỉ trả về hai bản ghi — một là tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường — năng suất thực tế của tìm kiếm y sinh là một phân tích có liên quan duy nhất, và nghiên cứu kinh tế Việt Nam 2026 chỉ tìm được qua RePEc và Google Scholar.

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

*Về câu hỏi Việt Nam.* Tìm kiếm PubMed đã hoàn tất trả về **576 bản ghi về thuế đồ uống có đường trên toàn cầu và 2 bản ghi cho Việt Nam** — một là tổng quan nha khoa năm 1997 về xu hướng tiêu thụ đường, một là nghiên cứu mô hình hóa 2023. Phân tích kinh tế năm 2026 không được chỉ mục trong PubMed và được tìm thấy qua RePEc và Google Scholar. Vậy tổng cộng có hai phân tích. Một nghiên cứu mô hình hóa năm kịch bản thuế ở mức tăng giá bán lẻ 5%, 11% và 19–20% khi luật còn đang thảo luận, và ước tính tác động lên cân nặng và đái tháo đường.[10] Nghiên cứu còn lại dùng Khảo sát mức sống hộ gia đình 2018 với hệ thống cầu hiệu chỉnh chất lượng để mô phỏng tác động lên tiêu thụ và phúc lợi theo luật 2025, nhưng coi đồ uống không cồn là một nhóm gộp gồm đồ uống có đường, nước đóng chai và nước ép 100%, và không mô hình hóa bệnh.[11] Cả hai đều không mô hình hóa thiết kế đã ban hành trên đúng cơ sở tính thuế, và không báo cáo lợi ích sức khỏe cùng thuế phải trả trên cùng một thang đo công bằng.

*Về câu hỏi quốc tế.* Đến năm 2024, 64 quốc gia đã áp dụng thuế đồ uống có đường, bao phủ 3,5 tỷ người; 45% theo tỷ lệ giá, 44% theo lượng và 5% theo hàm lượng đường.[5] Đánh giá năm 2025 của chính WHO đi đến kết luận nhất quán và ghi nhận rằng cơ sở tính thuế cùng điểm đánh thuế trên chuỗi giá khác nhau đến mức việc so sánh chuẩn hóa giữa các nước là khó[30] — chính vì vậy một phân tích neo vào cơ sở tính thuế theo luật, thay vì vào thuế suất danh nghĩa, mới là đơn vị so sánh hữu ích.

*Về tham số.* Độ co giãn, mức truyền dẫn, nguy cơ tương đối và chi phí đều có từ bối cảnh so sánh được nhưng không có từ Việt Nam, ngoại trừ ước lượng chi phí đái tháo đường.[22,23] Đây là nguồn gốc của hai ràng buộc chính được nhận diện ở Phụ lục B: tỷ trọng giá xuất xưởng trong giá bán lẻ, và tỷ lệ mắc bệnh theo ngũ phân vị.

**A.9 Duy trì nhật ký**

Nhật ký sàng lọc, lý do loại ở bước toàn văn, nhật ký xác minh ở A.7 và ngày tìm kiếm được lưu cùng protocol tại https://doi.org/10.5281/zenodo.23852996. Mọi chuỗi bị sửa sau khi đăng ký được ghi ở Phụ lục D.

---

## Phụ lục B. Nhật ký bằng chứng tham số

Mỗi tham số một dòng. Cột "Loại" phân biệt giá trị lấy từ nguồn công bố, giá trị suy ra bằng số học từ dữ liệu công bố, và giả định không có cơ sở thực nghiệm trực tiếp. Cột cuối ghi khả năng điền từ dữ liệu hiện có (có / một phần / không); khi là *không* hoặc *một phần*, phần ghi chú nêu phương án thay thế.

**B.1 Bảng tóm tắt**

| # | Tham số | Giá trị trung tâm đề xuất | Khoảng bất định | Phân phối | Nguồn | Loại | Khả thi |
|---|---|---|---|---|---|---|---|
| 1 | Dân số theo tuổi và ngũ phân vị, 2027–2050 | Dự báo TCTK; tổng 2027 ≈104 triệu | — | Cố định | Dự báo dân số 2024–2074 [18] | Nguồn | Có |
| 2 | Xu hướng tiêu thụ nền | +2,0%/năm | 0 đến +4,0% | Đều | CAGR Euromonitor 2009–2023 [2] | Suy ra | Một phần |
| 3 | Tiêu thụ theo tuổi, giới, ngũ phân vị | 145 mL/người/ngày | 90 đến 220 | Gamma | Euromonitor [2]; GNS 2019–20 [31]; VHLSS [24] | Suy ra | Một phần |
| 4 | Tỷ trọng sản phẩm trên 5 g/100 mL | 0,80 | 0,60 đến 0,95 | Beta(8;2) | Kiểm toán sản phẩm (Phụ lục C) | Sơ cấp | Có |
| 5 | Tỷ trọng giá xuất xưởng trong giá bán lẻ | 0,55 | 0,40 đến 0,70 | Tam giác | Không có nguồn Việt Nam; cấu trúc biên FMCG | Giả định | **Không** |
| 6 | Mức truyền dẫn | 0,90 | 0,50 đến 1,30 | Tam giác | World Bank 2020 [19]; Barbados, Mexico [28] | Nguồn (nước ngoài) | Một phần |
| 7a | Độ co giãn giá riêng | −1,20 | −0,80 đến −1,80 | Log-chuẩn trên \|ε\| | Andreyeva [20]; Cabrera Escobar [15]; Colchero [13] | Nguồn | Một phần |
| 7b | Độ co giãn giá chéo sang đồ uống không chịu thuế | +0,35 | +0,10 đến +0,65 | Log-chuẩn | Hệ thống cầu Chile và Mexico [13] | Nguồn | Một phần |
| 7c | Gradient độ co giãn theo ngũ phân vị | Q1 = 1,4 × Q5 | 1,0 đến 1,8 | — | Colchero [13] | Suy ra | Không |
| 8a | Mật độ năng lượng | 44 kcal/100 mL | 30 đến 55 | Cố định | Bảng thành phần thực phẩm VN [32] | Nguồn | Có |
| 8b | Bù trừ năng lượng | 30% | 15% đến 45% | Đều | Văn liệu can thiệp [15] | Giả định | Không |
| 9 | Nguy cơ tương đối BMI–bệnh | trên 2 kg/m²: CHD 1,11; đột quỵ thiếu máu 1,12 (1,09–1,15); đột quỵ xuất huyết 1,08 (1,04–1,12) | xem ghi chú | Log-chuẩn | APCSC [21,33] | Nguồn | Có |
| 10 | Tỷ lệ mắc, tử vong, trọng số khuyết tật | GBD 2021, Việt Nam, theo tuổi và giới | — | Beta; gamma | GBD 2021 [17] | Nguồn | Có |
| 11 | Chi phí y tế theo ca bệnh | Đái tháo đường 8,0 triệu đồng/bệnh nhân-năm; tim thiếu máu 84,9 triệu/đợt cấp; đột quỵ 10,5 triệu/đợt cấp | −30% đến +100% | Gamma | Le 2017 [22]; Pham 2020 [23]; Pham 2024 [36]; Doãn 2022 [37] | Nguồn | Có |
| 12 | Chi tiêu hộ theo ngũ phân vị | Bình quân 3,0 triệu đồng/người-tháng; tỷ số Q5/Q1 = 3,1 | — | Cố định | VHLSS 2024 [24] | Nguồn | Có |
| 13 | Độ trễ BMI → nguy cơ | 2 năm | 1 đến 5 | Đều | Giả định | Giả định | Không |
| 14 | Suất chiết khấu | 3% | 0%; 5% | Cố định | CHEERS 2022 [25] | Nguồn | Có |

**B.2 Ghi chú cho các tham số không đo trực tiếp**

**#2 Xu hướng tiêu thụ nền.** Kịch bản phản thực tế là yếu tố quyết định lớn nhất đến độ lớn tuyệt đối của mọi kết quả, và là tham số mà protocol ban đầu bỏ trống. Sản lượng bán lẻ đồ uống có đường của Euromonitor tại Việt Nam tăng từ 18 lít lên 66 lít/người giai đoạn 2009–2023, tốc độ khoảng 9,7%/năm. Ngoại suy tốc độ đó đến 2050 là không bảo vệ được: nó hàm ý mức tiêu thụ vượt xa mọi quan sát thị trường. Vì vậy chúng tôi dùng xu hướng trung tâm +2,0%/năm, gần với dự báo tăng trưởng của thị trường đồ uống rộng hơn, và cố ý đặt biên dưới ở 0% để giữ kịch bản "không tăng thêm". *Lý do:* xu hướng nền càng cao thì thuế càng có lợi, nên chọn xu hướng thận trọng là tự làm yếu đi giả thuyết của chính nghiên cứu. *Phương án thay thế:* không cần; đây là lựa chọn thiết kế, không phải lỗ hổng dữ liệu, và phải nêu rõ trong bài vì phản biện sẽ hỏi kịch bản phản thực tế giả định điều gì.

**#12 và #3, ghi chú về cấu trúc chi tiêu.** Giá trị trung bình các nhóm được đặt sao cho bình quân (3,0 triệu đồng/người-tháng) và tỷ số Q5/Q1 (3,1) tái tạo đúng số công bố của VHLSS 2024. Tỷ trọng chi tiêu dành cho đồ uống có đường sau đó được **suy ra** từ sản lượng và giá bán lẻ ngay trong mô hình, thay vì giả định riêng, để nó không thể mâu thuẫn với giả định tiêu thụ. Cách suy ra cho 2,6% ở Q1 và 1,5% ở Q5. Chỉ số Gini dùng cho Kakwani được tính chỉ từ giá trị trung bình các nhóm nên là **cận dưới**, khiến mức lũy thoái ước tính bị kéo về phía không; Gini thu nhập công bố là 0,372. **#3 Tiêu thụ theo tuổi, giới và ngũ phân vị.** Sản lượng bán lẻ bình quân đầu người cho biết mức, không cho biết phân bố. Phân bố theo tuổi và giới lấy từ Điều tra dinh dưỡng toàn quốc 2019–2020, có ghi nhận lượng đồ uống theo nhóm. Phân bố theo ngũ phân vị lấy từ chi tiêu đồ uống trong VHLSS 2024, hiệu chỉnh về tổng sản lượng Euromonitor để hai nguồn nhất quán. Giá trị trung tâm 145 mL/người/ngày được suy ra là 66 lít/năm × 0,80 (tỷ trọng trên ngưỡng) ÷ 365, không quan sát trực tiếp. *Phương án thay thế:* nếu không ánh xạ được nhóm đồ uống của GNS sang nhóm chịu thuế, áp dụng profile tuổi đồng nhất và ghi nhận là hạn chế.

**#5 Tỷ trọng giá xuất xưởng trong giá bán lẻ — ràng buộc chính.** Không có ước lượng công bố nào của Việt Nam. Giá trị này quyết định toàn bộ hiệu ứng giá: với τ = 0,10, *v* = 0,10 và κ = 0,90, tỷ trọng 0,40 cho mức tăng giá bán lẻ 4,0% và tỷ trọng 0,70 cho 6,9% — một khoảng bao trùm phần lớn không gian kết quả khả dĩ. Chúng tôi đề xuất phân phối tam giác với trung tâm 0,55, suy từ cấu trúc điển hình của chuỗi phân phối hàng tiêu dùng nhanh Việt Nam (giá bán nhà sản xuất, biên bán buôn và bán lẻ, và tầng VAT 10%), và đề xuất **hiệu chuẩn nó bằng thực nghiệm** thay vì để là giả định:

> **Quy trình hiệu chuẩn.** Nếu Bộ Tài chính công bố dự toán thu từ thuế đồ uống có đường cho ngân sách 2027, cơ sở chịu thuế hàm ý bởi dự toán đó là R/τ. Chia cho giá trị bán lẻ ước tính của lượng chịu thuế, đã trừ VAT, cho ra ước lượng trực tiếp của tỷ trọng xuất xưởng. Hai dự toán công bố độc lập, hoặc một dự toán cộng với giá trị thị trường của lượng chịu thuế, là đủ. Bước này biến tham số yếu nhất của mô hình thành tham số được hiệu chuẩn, và là nhiệm vụ dữ liệu có giá trị cao nhất của nghiên cứu.

*Phương án nếu không có dự toán:* giữ giả định tam giác, báo cáo phân tích ngưỡng (các tổ hợp truyền dẫn và tỷ trọng mà tại đó lợi ích sức khỏe không phân biệt được với không), và nêu trong Hạn chế rằng hiệu ứng giá là do giả định chứ không phải do ước lượng.

**#6 Mức truyền dẫn.** Mức truyền dẫn đo được đã dao động từ dưới 50% (Berkeley, Chile, Vương quốc Anh) đến gần 100% (Philadelphia, Mexico).[19] Tại Barbados, thuế 10% làm giá đồ uống có đường tăng 5,9% sau sáu tháng, hàm ý mức truyền dẫn khoảng 60%. Vì Việt Nam chưa có dữ liệu giá sau thực thi tại thời điểm viết bài, chúng tôi đặt trung tâm hơi dưới mức truyền dẫn đầy đủ và cho phép vượt 100%, điều quan sát được khi doanh nghiệp làm tròn giá lên. *Phương án:* không cần; khoảng giá trị chính là phương án.

**#7 Độ co giãn.** Độ co giãn giá riêng gộp của đồ uống có đường tập trung trong khoảng −1,0 đến −1,4: −1,30 (KTC 95%: −1,09 đến −1,51) trong một phân tích gộp chín nghiên cứu,[15] −1,16 với đồ uống có đường tại Mexico,[13] −1,37 với nước ngọt tại Chile, và −0,79 (khoảng −1,24 đến −0,33) với nước ngọt trong một tổng quan trước đó.[20] Chúng tôi đặt trung tâm −1,20 và cho phép toàn bộ khoảng quan sát. Gradient theo ngũ phân vị là yếu tố yếu nhất: phát hiện nhất quán là độ co giãn lớn hơn ở hộ thu nhập thấp hơn,[13] nhưng độ lớn cho Việt Nam chưa biết, nên gradient 1,4 được áp dụng và kết quả được báo cáo như một phân tích độ nhạy chứ không phải một phát hiện.

**#8b Bù trừ năng lượng.** Một phần năng lượng mất đi từ đồ uống được thay thế từ nguồn khác. Ước lượng công bố rất khác nhau, và lựa chọn này ảnh hưởng đáng kể đến đường BMI. Chúng tôi dùng phân phối đều từ 15% đến 45%, trung tâm 30%, và ghi rõ đây là giả định chứ không phải ước lượng Việt Nam. *Phương án thay thế:* báo cáo song song độ nhạy với hệ số quy đổi tĩnh, để người đọc thấy kết quả phụ thuộc bao nhiêu vào bước này.

**#9 Nguy cơ tương đối.** Từ Nghiên cứu đoàn hệ châu Á–Thái Bình Dương: mỗi 2 kg/m² BMI thấp hơn gắn với nguy cơ đột quỵ thiếu máu cục bộ thấp hơn 12% (KTC 95%: 9–15) và nguy cơ đột quỵ xuất huyết thấp hơn 8% (KTC 95%: 4–12),[21] với ước lượng tương đương cho bệnh mạch vành.[21] Nguy cơ đái tháo đường lấy từ cùng nhóm nghiên cứu.[33] Vì nguy cơ tương đối được áp lên *nhóm* BMI qua phân suất tác động quần thể, chúng tôi chuyển các ước lượng trên 2 đơn vị thành giá trị đặc thù theo nhóm, dùng điểm giữa các ngưỡng châu Á chuẩn (18,5; 23; 25; 30). *Lý do ưu tiên APCSC:* đây là bộ bằng chứng gộp châu Á duy nhất đủ lớn, và dùng ước lượng phương Tây sẽ phóng đại nguy cơ ở một quần thể gầy.

**Mật độ đường của đồ uống chịu thuế.** Giá trị trung tâm 11 g/100 mL không phải giả định: Nguyễn và cộng sự báo cáo 11 g/100 mL với nước ngọt có ga, 9 g với cà phê và trà pha sẵn, 16 g với nước thể thao và tăng lực, và 7 g với nước ép trên thị trường Việt Nam.[10] Nước ngọt có ga chiếm phần lớn sản lượng chịu thuế, nên 11 được dùng làm giá trị trung tâm, và toàn dải theo nhóm (7–16) được khảo sát trong phân tích độ nhạy.

**#10 Tỷ lệ mắc nền theo ngũ phân vị.** GBD 2021 cung cấp tỷ lệ mắc, tỷ lệ hiện mắc và tử vong quốc gia cho cả ba bệnh, và STEPS 2021 cung cấp tỷ lệ hiện mắc đái tháo đường đo được. Không nguồn nào phân tầng theo chi tiêu hộ. Vì vậy chúng tôi áp tỷ lệ quốc gia cho **mọi** ngũ phân vị và giả định **không có** gradient kinh tế–xã hội trong tỷ lệ mắc nền. Đây là đơn giản hóa có chủ đích: mọi chênh lệch công bằng trong mô hình chỉ phát sinh từ khác biệt về tiêu thụ và phản ứng giá, không bao giờ từ một gradient bệnh giả định. Một gradient thật trong nguy cơ bệnh sẽ không được phản ánh.

**B.3 Thứ tự các nhiệm vụ dữ liệu, theo giá trị**

1. Hiệu chuẩn tỷ trọng giá xuất xưởng (#5) từ một dự toán ngân sách đã công bố — giá trị cao nhất, vì nó đặt quy mô cho mọi kết quả.
2. Hoàn tất kiểm toán sản phẩm (#4) — đặt cơ sở thuế và nhóm ứng viên tái định lượng cho S3.
3. Ánh xạ nhóm đồ uống của GNS 2019–2020 sang nhóm chịu thuế (#3).
4. Lấy ước lượng chi phí Việt Nam cho bệnh tim thiếu máu cục bộ và đột quỵ (#11); chi phí đái tháo đường đã có.
5. Chốt xu hướng nền (#2) và ghi quyết định vào nhật ký sai lệch nếu khác protocol đã đăng ký.

---

## Phụ lục C. Protocol kiểm toán sản phẩm

**C.1 Mục đích**

Kiểm toán có ba nhiệm vụ, và đó là lý do ba tuần thực địa là đáng. Nó đo **tỷ trọng thị trường trên ngưỡng 5 g/100 mL**, đặt quy mô cơ sở thuế (tham số 4, Phụ lục B). Nó đo **phân bố hàm lượng đường quanh ngưỡng**, xác định có bao nhiêu sản phẩm có thể tái định lượng và do đó khoảng của kịch bản S3. Và nó thiết lập **mốc giá bán lẻ trước thực thi**, để mức thay đổi giá ước tính từ công thức thuế sau này có thể đối chiếu với thực tế. Nghiên cứu không cần phê duyệt đạo đức: không có người tham gia, không thu thập dữ liệu cá nhân, chỉ ghi giá niêm yết công khai và thông tin trên nhãn.

**C.2 Thiết kế và thời điểm**

Kiểm toán giá bán lẻ cắt ngang đồ uống không cồn đóng gói, thực hiện **tháng 11–12/2026**, trước khi mức 8% có hiệu lực ngày 1/1/2027. Thời điểm này quan trọng: kiểm toán sau thực thi không dùng được để lập mốc nền, còn mốc nền lấy sau khi thuế được công bố nhưng trước khi áp dụng là điểm so sánh sạch nhất hiện có. Nếu đủ nguồn lực, protocol nên được lặp lại **tháng 2–3/2027** tại đúng các cửa hàng đó, biến mốc nền tĩnh thành so sánh giá trước–sau và cho nghiên cứu ước lượng truyền dẫn của chính mình — tham số hiện đang vay từ nước khác.

**C.3 Khung mẫu**

*Trong phạm vi*, theo TCVN 12828:2019: đồ uống hương liệu gồm nước ngọt có ga, nước ngọt không ga, nước tăng lực, nước thể thao và nước điện giải; đồ uống pha sẵn từ cà phê và từ chè; đồ uống thảo mộc; đồ uống có chứa nước trái cây; đồ uống từ ngũ cốc.

*Ngoài phạm vi*, ghi nhận riêng để có thể kiểm chứng việc loại trừ: sữa và sản phẩm từ sữa, thực phẩm lỏng dinh dưỡng, nước khoáng thiên nhiên và nước uống đóng chai, nước ép rau quả 100%, nectar, sản phẩm từ ca cao.

*Kênh*, lấy mẫu ở cả ba vì giá và cơ cấu hàng khác nhau: kênh hiện đại (siêu thị và chuỗi cửa hàng tiện lợi), kênh truyền thống (tạp hóa và sạp chợ), và kênh trực tuyến (hai sàn thương mại điện tử lớn và một ứng dụng giao nhanh).

*Địa bàn*: Hà Nội và TP. Hồ Chí Minh, cộng thêm một huyện nông thôn hoặc ven đô có chủ đích ở mỗi vùng để nắm gradient giá. Chỉ hai thành phố sẽ phóng đại giá bình quân; thêm một huyện nông thôn tốn ít và loại bỏ một phản biện hiển nhiên.

**C.4 Chiến lược và cỡ mẫu**

Lấy mẫu theo hạn mức, phân theo nhóm sản phẩm × kênh, với hạn mức tỷ lệ với số SKU quan sát được trong một lượt khảo sát thí điểm bốn cửa hàng mỗi thành phố. Ở cấp sản phẩm lấy mẫu có chủ đích, ở cấp cửa hàng lấy toàn bộ: trong mỗi cửa hàng được chọn, ghi **mọi** SKU trong phạm vi có trên kệ. Mục tiêu n ≈ 200 SKU, 250 nếu đủ nguồn lực. Với p = 0,80, n = 200 cho khoảng tin cậy 95% khoảng ±5,5 điểm phần trăm quanh tỷ trọng ước tính trên ngưỡng; n = 250 cho ±5,0. Vì tổng thể SKU phân biệt trên toàn quốc chỉ ở mức vài nghìn chứ không phải hàng triệu, không cần hiệu chỉnh tổng thể hữu hạn ở cỡ mẫu này.

**C.5 Các trường dữ liệu**

Mỗi SKU: nhãn hiệu; tên sản phẩm như in trên bao bì; nhà sản xuất hoặc nhà nhập khẩu; mã vạch; dung tích và đơn vị (mL); nhóm sản phẩm theo C.3; **tổng lượng đường trên 100 mL như in trên nhãn dinh dưỡng**; loại chất tạo ngọt (ngọt calo, ngọt phi calo, hoặc cả hai) theo danh mục thành phần; giá trên kệ tính bằng đồng; giá có khuyến mại hay không; mã cửa hàng, kênh và địa bàn; ngày quan sát; và ba ảnh — mặt trước, nhãn dinh dưỡng, và tem giá trên kệ. Phân biệt đường tổng và đường bổ sung có ý nghĩa pháp lý và rất dễ nhầm: Nghị định 360/2025/NĐ-CP quy định cơ sở tính thuế là **tổng lượng đường trên nhãn**, không phải đường bổ sung. Chỉ ghi đường bổ sung sẽ phân loại sai sản phẩm.

**C.6 Quy trình đo**

Hai điều tra viên làm việc độc lập ở mỗi cửa hàng và đối chiếu khác biệt cuối ngày, với một người thứ ba phân xử các trường hợp chưa thống nhất. Toàn bộ dữ liệu được nhập hai lần. Ảnh được lưu để mọi giá trị có thể kiểm lại với bao bì. Khi nhãn dinh dưỡng không có hoặc không đọc được, SKU được ghi là *không có nhãn* thay vì nội suy, và tỷ lệ SKU không có nhãn được báo cáo — bản thân nó là một phát hiện về khả năng thực thi của một loại thuế dựa trên nhãn.

**C.7 Phân loại sản phẩm sát biên**

Ngưỡng nằm trong một ranh giới loại mà luật không giải quyết: khác biệt giữa nước quả và đồ uống có chứa nước quả đang tranh cãi, và địa vị của nước dừa chưa rõ (phần Giới thiệu). Kiểm toán vì vậy áp một cây quyết định bốn quy tắc tường minh và ghi lại mọi trường hợp sát biên kèm ảnh:

1. Nếu nhãn công bố 100% nước quả và danh mục thành phần không có đường bổ sung hay nước thêm vào, phân loại là **nước quả, ngoài phạm vi**.
2. Nếu sản phẩm chứa nước quả **và** có đường bổ sung hoặc nước thêm vào, phân loại là **đồ uống chứa nước quả, trong phạm vi**.
3. Nếu nhãn ghi "nectar" hoặc hàm lượng quả dưới 100% kèm đường bổ sung, phân loại là **nectar, ngoài phạm vi**, nhưng đánh dấu, vì nectar là nhóm dễ bị phân loại lại nhất trong hướng dẫn.
4. Nước dừa: **ngoài phạm vi** nếu thành phần duy nhất là nước dừa; nếu không, **trong phạm vi**. Mọi SKU chạm quy tắc 2, 3 hoặc 4 được liệt kê riêng trong kết quả kiểm toán, để cách diễn giải rộng và hẹp của cơ sở thuế trong mô hình được dựng trực tiếp từ sản phẩm quan sát thay vì từ giả định.

**C.8 Phân tích**

Đầu ra chính là tỷ trọng SKU trên ngưỡng, kèm khoảng tin cậy chính xác Clopper–Pearson. Vì sản phẩm nhiều đường thường chiếm diện tích kệ nhiều hơn so với thị phần, **tỷ trọng SKU không trọng số là cận trên của tỷ trọng theo lượng**. Vì vậy chúng tôi báo cáo ba ước lượng: tỷ trọng SKU không trọng số; tỷ trọng SKU có trọng số theo sản lượng nhóm từ Euromonitor; và một cận dưới thu được khi giả định rằng trong mỗi nhóm, các sản phẩm trên ngưỡng mang sản lượng bình quân của nhóm. Mô hình dùng ước lượng có trọng số làm giá trị trung tâm và cận dưới làm kịch bản bi quan.

Đầu ra phụ: phân bố hàm lượng đường tổng thể và theo nhóm, chia bin 1 g/100 mL, kèm số sản phẩm trong dải 5,0–8,0 g — nhóm mà S3 lấy ứng viên tái định lượng; giá bình quân mỗi lít theo nhóm và kênh; giá trên mỗi gam đường, tức đại lượng mà một loại thuế theo gam sẽ tác động; và tỷ trọng sản phẩm có chất tạo ngọt phi calo một phần hoặc toàn phần, liên quan trực tiếp đến câu hỏi chưa ngã ngũ về việc các sản phẩm đó có thuộc cơ sở thuế hay không.

**C.9 Hạn chế phải nêu trong bài**

Kiểm toán quan sát diện tích kệ, không quan sát doanh số, nên trọng số theo lượng phụ thuộc dữ liệu nhóm từ bên ngoài. Giá trị trên nhãn chịu dung sai mà quy định ghi nhãn dinh dưỡng cho phép và không phải đo phòng thí nghiệm; khi giá trị công bố nằm trong 0,5 g/100 mL quanh ngưỡng, SKU được xử lý là sát biên và tỷ trọng cơ sở thuế được tính lại với nó ở mỗi phía. Hai thành phố cộng hai huyện không đại diện quốc gia, và độ phủ kênh truyền thống tất yếu không đầy đủ. Cuối cùng, kiểm toán là ảnh chụp một thời điểm: tái định lượng và điều chỉnh giá sau tháng 1/2027 không được nắm bắt trừ khi vòng lặp được cấp kinh phí.

**C.10 Nguồn lực và tiến độ**

| Tuần | Hoạt động |
|---|---|
| 1 | Hoàn thiện biểu mẫu; thí điểm bốn cửa hàng mỗi thành phố; sửa danh mục nhóm và hạn mức |
| 2 | Thực địa Hà Nội và TP. Hồ Chí Minh, kênh hiện đại và truyền thống |
| 3 | Thực địa kênh trực tuyến và huyện nông thôn; nhập liệu hai lần; đối chiếu |
| 4 | Phân xử phân loại; phân tích; báo cáo kiểm toán và bộ dữ liệu đọc được bằng máy |

Nhân lực: hai điều tra viên, một giám sát, một chuyên viên phân tích 50% thời gian. Chi phí trực tiếp khiêm tốn — đi lại, công tác phí và một máy tính bảng mỗi điều tra viên — và bộ dữ liệu nên được công bố cùng bài, vì đây là dữ liệu sơ cấp duy nhất của nghiên cứu.

**C.11 Đầu ra**

Bộ dữ liệu đọc được bằng máy của toàn bộ SKU đã kiểm toán với các trường ở C.5; bốn ước lượng dẫn xuất ở C.8; danh sách sản phẩm sát biên kèm ảnh; và một ghi chú phương pháp ngắn phù hợp để công bố như phần của Phụ lục C. Bộ dữ liệu cung cấp đầu vào cho tham số 3, 4 và 5 ở Phụ lục B, và danh sách SKU sát ngưỡng xác định nhóm tái định lượng cho kịch bản S3.

---

## Phụ lục D. Nhật ký sai lệch

Nhật ký được mở tại thời điểm đăng ký và duy trì đến khi nộp bài. Mỗi mục ghi protocol đã đăng ký nói gì, thực tế đã làm gì, thay đổi khi nào và vì sao. Sai lệch được công bố trong bản thảo kể cả khi chúng cải thiện phân tích, vì giá trị của việc đăng ký phụ thuộc vào tính đầy đủ của bản ghi.

**D.1 Mẫu cấu trúc**

| # | Ngày | Protocol đã đăng ký | Đã làm | Lý do | Ảnh hưởng đến kết quả |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

**D.2 Sai lệch đã biết tại thời điểm soạn thảo**

Những mục này phát sinh từ khác biệt giữa protocol v3.0 và thiết kế hiện đề xuất. Chúng phải được chốt **trước** khi đăng ký chứ không ghi nhật ký sau, vì đây là quyết định thiết kế, không phải sai lệch.

| # | Mục | Protocol v3.0 | Hiện đề xuất | Lý do |
|---|---|---|---|---|
| D1 | Xu hướng tiêu thụ nền | "tham số xu hướng công bố", không nêu | +2,0%/năm, khoảng 0 đến +4,0% (Phụ lục B #2) | Kịch bản phản thực tế quyết định mọi kết quả tuyệt đối mà chưa có giá trị xác định; xu hướng thận trọng tránh làm lợi cho giả thuyết của chính nghiên cứu |
| D2 | Tỷ trọng giá xuất xưởng | Không được nhận diện là tham số | Tham số #5 tường minh, kèm quy trình hiệu chuẩn | Tham số này quyết định toàn bộ hiệu ứng giá và đã thiếu trong danh sách ban đầu |
| D3 | Tầng thuế giá trị gia tăng | "cần xác minh trong văn bản luật" | Đã xác nhận: VAT 10% trên giá đã gồm thuế TTĐB | Nghị định 360 và Nghị định 174 chốt cơ chế |
| D4 | Định nghĩa đường | "đường tổng hay đường bổ sung, cần xác minh" | Tổng lượng đường trên nhãn (NĐ 360, Điều 3 khoản 4) | Đã giải quyết bằng nghị định hướng dẫn |
| D5 | Phạm vi nhóm chịu thuế | "danh mục miễn trừ, cần xác minh" | Mang tính định nghĩa, qua TCVN 12828:2019; mô hình hóa cả diễn giải rộng và hẹp | Luật không có danh mục miễn trừ cho đồ uống |
| D6 | Bộ kịch bản | 6 kịch bản | 4 | Truyền dẫn chuyển sang độ nhạy; kịch bản thuế theo hàm lượng đường bỏ vì thiếu dữ liệu |
| D7 | Tham vấn người bệnh và cộng đồng | "tham vấn chuyên gia" | Không tham vấn mới; dùng bằng chứng định tính đã công bố | Ghi nhận là hạn chế quy trình (Phương pháp) |
| D8 | Sâu răng và nhóm dưới 20 tuổi | Loại trừ | Vẫn loại trừ, nêu là hạn chế | Ràng buộc nguồn lực; đánh dấu cho bài mở rộng |

**D.3 Những gì phải ghi nhật ký sau khi đăng ký**

Mọi thay đổi về: giá trị tham số ở Phụ lục B; bộ độ co giãn; giả định độ trễ; suất chiết khấu; tập kịch bản; kết cục chính; phương pháp tính sức khỏe tương đương; và mọi thay đổi mã làm thay đổi kết quả chứ không chỉ thay đổi cách trình bày. Mỗi mục được ghi ngày và ký bởi chuyên viên phân tích thực hiện.

---

## Phụ lục E. Danh mục kiểm tra CHEERS 2022

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
| 10 | Suất chiết khấu | Phương pháp; Phụ lục G |
| 11 | Lựa chọn kết cục | Phương pháp; tóm tắt kết cục ở Giới thiệu |
| 12 | Đo lường kết cục | Phương pháp, *Cấu trúc mô hình* bước 5–7 |
| 13 | Định giá kết cục | Phương pháp bước 7; trọng số khuyết tật từ GBD 2021 |
| 14 | Đo lường và định giá nguồn lực, chi phí | Phương pháp bước 7; Bảng 2 |
| 15 | Tiền tệ, năm giá, quy đổi | Phương pháp, *Thiết kế và tổng quan* |
| 16 | Lý do và mô tả mô hình | Phương pháp, *Cấu trúc mô hình*; Hình 1 |
| 17 | Phân tích và giả định | Phương pháp; Phụ lục B; Phụ lục G |
| 18 | Mô tả tính không đồng nhất | Phương pháp, *Phân tích công bằng*; Kết quả, *Công bằng* |
| 19 | Mô tả tác động phân bố | Phương pháp, *Phân tích công bằng*; Hình 3 |
| 20 | Mô tả bất định | Phương pháp; Kết quả, *Bất định*; Phụ lục G |
| 21 | Cách tiếp cận tham vấn người bệnh và các bên liên quan | Phương pháp, *Kiểm chứng* |
| 22 | Tham số nghiên cứu | Bảng 2; Phụ lục B |
| 23 | Tóm tắt kết quả chính | Kết quả; Bảng 3 |
| 24 | Ảnh hưởng của bất định | Kết quả, *Bất định*; Hình 4 |
| 25 | Ảnh hưởng của tham vấn | Phương pháp, *Kiểm chứng*; Thảo luận, Hạn chế |
| 26 | Phát hiện, hạn chế và diễn giải | Thảo luận |
| 27 | Khả năng khái quát hóa | Thảo luận, *Hàm ý chính sách* |
| 28 | Nguồn tài trợ, xung đột lợi ích, khả năng truy cập dữ liệu | Trang bìa; Tuyên bố xung đột lợi ích; Chia sẻ dữ liệu |

---

## Phụ lục F. Kế hoạch kiểm chứng

**F.1 Thẩm định bên trong**

Mô hình phải tái tạo, cho kịch bản nền và trước khi áp thuế, số liệu dịch tễ Việt Nam đã công bố cho từng bệnh trong mô hình. Tiêu chí chấp nhận được định trước để việc kiểm tra không biến thành việc đi tìm một đặc tả nào đó cho qua.

| Kiểm tra | Chuẩn đối chiếu | Tiêu chí chấp nhận |
|---|---|---|
| Tỷ lệ hiện mắc đái tháo đường, 20+ | Tỷ lệ đo được của STEPS 2021 | Trong ±15% giá trị công bố |
| Tỷ lệ mắc, cả ba bệnh | GBD 2021, Việt Nam | Trong ±15% theo giới và nhóm tuổi 10 năm |
| Tử vong do mọi nguyên nhân theo tuổi, giới | GBD 2021 / bảng sống TCTK | Trong ±5% |
| Tổng dân số 2027–2050 | Dự báo TCTK | Trong ±1% ở mọi năm |
| Trọng số khuyết tật áp dụng | GBD 2021 | Khớp chính xác giá trị công bố |

Thất bại ở bước này được báo cáo, không được chỉnh cho qua. Khi một tham số được điều chỉnh để đạt hiệu chuẩn, mức điều chỉnh và độ lớn được ghi ở Phụ lục D và giá trị đã hiệu chỉnh được dùng với khoảng bất định mở rộng.

**F.2 Kiểm tra kỹ thuật**

Kiểm thử đơn vị cho từng bước trong bảy bước, với đầu vào đã biết và đầu ra tính tay. Bảo toàn dân số: không ai rời bảng sống ngoài đường tử vong. Điều kiện cực biên: độ co giãn bằng không và thuế bằng không đều phải trả về đúng kịch bản nền; một mức thuế cao đến mức tiêu thụ về không không được tạo ra tiêu thụ âm hay lỗi chia. Bước thuế–giá được kiểm tra với một phép tính dạng đóng cho một sản phẩm đơn lẻ có cấu trúc giá đã biết.

**F.3 Thẩm định bên ngoài**

Ở mức tăng giá bán lẻ 20%, ước tính DALY tránh được của chúng tôi được so với Nguyễn và cộng sự,[10] phân tích Việt Nam đã công bố gần nhất. Khác biệt được phân rã thành bốn nguồn theo thứ tự: bộ kết cục, suất chiết khấu, khung thời gian và cấu trúc mô hình. Phân rã được báo cáo đầy đủ, vì một khác biệt phần trăm không giải thích còn tệ hơn một khác biệt đã được ghi chép.

**F.4 Rà soát độc lập**

Một người rà soát độc lập không tham gia phân tích chạy lại mô hình từ kho công khai và tái tạo Hình 2 và Bảng 3. Rà soát bao gồm mã, không bao gồm phương pháp. Khác biệt được giải quyết trước khi nộp.

---

## Phụ lục G. Kế hoạch phân tích độ nhạy

**G.1 Phân tích xác suất**

5.000 lần rút, lấy mẫu độc lập từ các phân phối ở Phụ lục B, lấy mẫu hypercube Latin với hạt giống cố định. Báo cáo: trung vị, khoảng bất định 95%, và các phát biểu xác suất trong phần Kết quả. Hội tụ được đánh giá bằng cách so nửa đầu và nửa sau các lần rút; nếu trung vị khác nhau quá 2%, chạy lại với 10.000 lần.

**G.2 Phân tích một chiều**

Biểu đồ tornado cho mười tham số đóng góp nhiều nhất vào phương sai, mỗi tham số biến thiên trong khoảng bách phân vị 2,5–97,5 trong khi các tham số khác giữ ở giá trị trung tâm.

**G.3 Kịch bản cấu trúc**

| Kịch bản | Kiểm tra điều gì | Hướng kỳ vọng |
|---|---|---|
| Quy đổi cân nặng tĩnh | Mô hình cân nặng động có dẫn dắt kết quả không | Lợi ích nhỏ hơn |
| Bộ độ co giãn thấp (−0,8) | Mức phản ứng của cầu | Lợi ích nhỏ hơn |
| Bộ độ co giãn cao (−1,8) | Mức phản ứng của cầu | Lợi ích lớn hơn |
| Truyền dẫn 50% | Doanh nghiệp có hấp thụ thuế không | Lợi ích nhỏ hơn nhiều |
| Truyền dẫn 150% | Chuyển giá vượt mức | Lợi ích lớn hơn |
| Tỷ trọng chịu thuế 0,60 | Cơ sở thuế hẹp | Lợi ích nhỏ hơn |
| Tỷ trọng chịu thuế 0,95 | Cơ sở thuế rộng | Lợi ích lớn hơn |
| Diễn giải pháp lý rộng | Nectar và đồ uống chứa nước quả bị đánh thuế | Lợi ích lớn hơn |
| Diễn giải pháp lý hẹp | Chỉ nước ngọt rõ ràng bị đánh thuế | Lợi ích nhỏ hơn |
| S3 ở 10%, 25%, 50% | Kênh tái định lượng | Lợi ích giảm khi cơ sở thuế co lại, nhưng lượng đường nạp vào giảm |

**G.4 Phân tích ngưỡng**

Trên một lưới truyền dẫn (0,3 đến 1,5) và tỷ trọng giá xuất xưởng (0,30 đến 0,85), mô hình báo cáo DALY thu được. Đầu ra xác định đường biên mà tại đó lợi ích sức khỏe không phân biệt được với không, và chính đường biên đó — chứ không phải ước lượng điểm — là phát biểu vững nhất của nghiên cứu về điều thuế có thể đạt được.

**G.5 Báo cáo**

Mọi kết quả độ nhạy được báo cáo dù có ủng hộ kết luận chính hay không. Phần Thảo luận nêu rõ kết luận nào vượt qua toàn bộ bộ kiểm tra và kết luận nào không.

---

## Phụ lục H. Mã và khả năng tái lập

**H.1 Môi trường**

R phiên bản 4.6.1. Phiên bản các gói được ghim trong `renv.lock`; kho lưu trữ ghi lại thông tin phiên đầy đủ của lần chạy tạo ra từng bảng và hình.

**H.2 Cấu trúc kho lưu trữ**

```
/model bảy bước mô hình, mỗi bước một tệp, cộng động cơ bảng sống
/params bảng tham số, ma trận rút PSA, CSV nhật ký bằng chứng
/analysis script tạo từng bảng và hình theo thứ tự
/output bảng và hình đã tạo, tên tệp kèm hạt giống
/tests kiểm thử đơn vị và kiểm thử điều kiện cực biên
/docs protocol, các phụ lục, nhật ký sai lệch
```

**H.3 Khả năng tái lập**

Một script duy nhất tái tạo mọi con số trong bản thảo từ tệp tham số và một hạt giống cố định. Ma trận đầu vào PSA được công bố dạng CSV để kết quả có thể kiểm tra mà không cần chạy lại bước lấy mẫu. Thời gian chạy của toàn bộ phân tích được ghi lại để người rà soát đánh giá được tính khả thi.

**H.4 Giấy phép và trích dẫn**

Mã được phát hành theo giấy phép mở khi bài được nhận; kho lưu trữ có DOI. Nhật ký bằng chứng tham số được phát hành dạng tệp dữ liệu, có cột ghi nguồn cho từng giá trị.

---
