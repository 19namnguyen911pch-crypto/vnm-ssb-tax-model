# data/ — nguồn dữ liệu và trạng thái

## Đã tải được

| Tệp | Nguồn | Nội dung | Giấy phép / điều kiện |
|---|---|---|---|
| `vnm_wpp_age5_2025_2050.csv` | UN World Population Prospects 2024, medium variant | Dân số Việt Nam theo nhóm tuổi 5 năm × giới × năm, 2025–2050 (nghìn người) | Mở, không cần đăng nhập |
| `vnm_population_wb.csv` | World Bank API, `SP.POP.TOTL` | Tổng dân số 2000–2025 | CC BY 4.0 |
| `wb_diabetes_raw.json` | World Bank API, `SH.STA.DIAB.ZS` | Tỷ lệ đái tháo đường 20–79 tuổi (định nghĩa IDF) — chỉ có 2011: 3,2% và 2024: 3,4% | CC BY 4.0 |
| `nso_pop_proj.pdf` | Tổng cục Thống kê, *Dự báo dân số Việt Nam 2024–2074* | Bản PDF 14 MB, có text, chưa phân tích | Công khai |

**Con số kiểm tra:** WPP 2024 cho dân số Việt Nam **102,5 triệu (2027)** và **110,0 triệu (2050)**.
Nếu bạn dùng dự báo TCTK (thấp hơn) thì ghi rõ nguồn nào trong bài — hai bộ số khác nhau khoảng 1–2%.

## Đã tích hợp vào mô hình

`load_age_weights()` đọc `vnm_wpp_age5_2025_2050.csv` và phân bổ dân số mỗi ngũ phân vị
theo cơ cấu tuổi thật, thay cho giả định phân bố đều.

Tác động: tỷ số DALY Q1/Q5 **giảm từ 1,40 xuống 1,05**. Nghĩa là giả định phân bố
tuổi đều đã **thổi phồng** kết quả công bằng. Đây là lý do phải dùng cơ cấu tuổi thật.

Trong mỗi nhóm 5 năm, dân số được chia đều cho từng tuổi — xấp xỉ có ghi chép, không
phải tuyên bố về cơ cấu tuổi đơn.

## Bị chặn — cần đăng nhập

**ĐÃ LẤY ĐƯỢC.** Sau khi đăng nhập IHME, dữ liệu GBD 2021 cho Việt Nam đã tải về:

| Tệp | Nội dung |
|---|---|
| `gbd_vnm/vnm_gbd_2021.csv` | 1.020 dòng thô từ GBD Results Tool: 5 measure × 3 bệnh × 2 giới × 15 nhóm tuổi × 2 metric, năm 2021 |
| `gbd_vnm/vnm_gbd_params_long.csv` | Bảng dẫn xuất: tỷ lệ mắc, tỷ lệ hiện mắc, tử vong, YLD, trọng số khuyết tật, tử vong trong số ca hiện mắc — theo bệnh × giới × nhóm tuổi |

Truy vấn đã dùng: location 20 (Viet Nam); cause 976/493/494; measure 1,2,3,5,6;
metric 1,3; sex 1,2; year 2021; API `php/data.php`, tối đa 3 measure mỗi lần.

Giá trị kiểm tra: DW đái tháo đường **0,093**, tim thiếu máu **0,045**, đột quỵ **0,210**.
Tỷ lệ hiện mắc ĐTĐ type 2 ở nam 50–54 tuổi: **7,2%**.

Lưu ý: GBD cho tỷ lệ ĐTĐ type 2 toàn dân thấp hơn STEPS 2021 (đo đường huyết tăng,
7,3% ở người 18–69). Hai định nghĩa khác nhau — ghi rõ khi tham chiếu.

Cần lấy cho Việt Nam, ba bệnh **đái tháo đường type 2, bệnh tim thiếu máu cục bộ, đột quỵ**:

| Chiều | Giá trị |
|---|---|
| Location | Viet Nam |
| Year | 1990–2023 (cần 2021 và 2023 để ngoại suy) |
| Age | 20–100, từng năm hoặc nhóm 5 năm |
| Sex | Male, Female |
| Cause | Diabetes mellitus type 2; Ischemic heart disease; Stroke |
| Measure | Incidence; Prevalence; Deaths; DALYs (YLDs) |
| Metric | Rate và Number |

Xuất CSV, đặt vào `data/gbd_vnm/`.

## Không dùng được

- **WHO GHO API** trả 500 ở mọi endpoint (`ghoapi.azureedge.net`) — dịch vụ hỏng, không phải lỗi cấu hình.
- **UN WPP Data Portal API** trả 401 (cần API key). Bù lại, các tệp CSV hàng loạt trên
  `population.un.org/wpp/assets/` **mở hoàn toàn** — đó là đường đã dùng.

## Còn thiếu, ngoài GBD

| Dữ liệu | Nguồn | Ghi chú |
|---|---|---|
| VHLSS microdata | TCTK / World Bank Microdata Library | Cần đăng ký; xem `model/vhlss.R` |

## VHLSS — dùng số công bố thay cho microdata

Từ Thông cáo báo chí kết quả VHLSS 2024 của TCTK (5/2025):

| Mốc | Giá trị |
|---|---|
| Chi tiêu bình quân | **3,0 triệu đồng**/người/tháng |
| Chi đời sống | 2,8 triệu (94,5% tổng chi) |
| Chênh lệch chi đời sống nhóm 5 / nhóm 1 | **3,1 lần** (4,5 triệu so với 1,5 triệu) |
| Hệ số Gini thu nhập | **0,372** |

`published_profile()` đặt giá trị trung bình 5 nhóm sao cho **tái tạo đúng** hai mốc
đầu tiên. Tỷ trọng chi cho đồ uống có đường được **suy ra** từ sản lượng × giá,
không còn là giả định riêng — nên không thể mâu thuẫn với giả định tiêu thụ.

Vẫn là giả định: sản lượng SSB tăng theo chi tiêu, và gradient độ co giãn.
Microdata sẽ thay cả hai.
| Dự toán thu thuế SSB 2027 | Bộ Tài chính | **Đã tìm, không có.** Dự toán NSNN 2027 công bố ở mức tổng (3.334,3 nghìn tỷ), không tách dòng cho thuế đồ uống có đường. Xem ghi chú dưới. |
| Chi phí y tế theo bệnh | Nghiên cứu chi phí VN, dữ liệu BHXH | Đái tháo đường đã có (Le 2017; Pham 2020); tim và đột quỵ chưa |


## Dự toán thu thuế đồ uống có đường — không công bố

Đã tra: báo cáo dự toán NSNN 2027 (Quốc hội, 17/10/2026), cổng Bộ Tài chính, VnEconomy,
Nhân Dân, Hải quan. Tất cả chỉ có tổng thu, không có dòng riêng cho thuế tiêu thụ đặc biệt
đồ uống có đường.

Hệ quả: **tham số #5 (`exfac_share`) không hiệu chuẩn được từ số công bố.** Giữ phân phối
tam giác (0,40–0,55–0,70) và dùng phân tích ngưỡng để trả lời.

Nếu sau này có con số, chạy:

```r
source("model/pmslt_model.R")
calibrate_exfac_share(rev_projection_vnd = 2.0e12, tau = 0.08,
                      qprof = get_quintile_profile(), p = params_default())
```

Hàm này cũng là một phép kiểm tra: dự toán trên khoảng 2,7 nghìn tỷ ở mức 8% sẽ cho tỷ trọng
> 1, tức là mâu thuẫn với cơ sở sản lượng — dấu hiệu phải xem lại giả định tiêu thụ.

## Không còn dùng gradient bệnh theo ngũ phân vị

Báo cáo STEPS 2021 không có bảng đường huyết theo ngũ phân vị chi tiêu, nên thay vì
giả định một gradient, mô hình **giả định không có gradient**: áp tỷ lệ quốc gia cho
mọi nhóm. Hệ quả là chênh lệch công bằng chỉ đến từ tiêu thụ và phản ứng giá.

## Hàm lượng đường hai phân đoạn

Không cần kiểm toán để có số này: Nguyen và cộng sự 2023 (PLoS One) báo cáo cho thị
trường Việt Nam — nước ngọt có ga **11 g**/100 mL, nước ép **7 g**, cà phê và trà pha
sẵn **9 g**, nước thể thao và tăng lực **16 g**. Mô hình dùng 11 cho phân đoạn nhiều
đường và 7 cho phân đoạn ít đường.

Kiểm toán sản phẩm vẫn có giá trị nhưng không còn là điều kiện: nó cho **tỷ trọng sản
lượng** của mỗi phân đoạn, mốc giá trước thuế, và danh sách sản phẩm sát ngưỡng cho S3.
