# model/ — mô hình PMSLT

## Chạy

```bash
Rscript model/run_all.R                 # phát triển: 200 lần PSA
PSA_N=5000 Rscript model/run_all.R      # chạy chính thức
VHLSS_FILE=data/vhlss_hh.csv Rscript model/run_all.R
```

Không cần gói ngoài base R.

## Tệp

| Tệp | Nội dung |
|---|---|
| `vhlss.R` | Nạp microdata VHLSS → 5 ngũ phân vị; nếu không có thì dự phòng từ số công bố |
| `pmslt_model.R` | 7 bước mô hình, cầu 2 phân đoạn, vòng 5 ngũ phân vị, hiệu chuẩn S1b, chỉ số công bằng |
| `psa.R` | Lấy mẫu phân phối, chạy PSA, tóm tắt, xuất CSV |
| `policy_levers.R` | Kịch bản cơ sở tính thuế bán lẻ và già hóa dân số, xuất `output/policy_levers.csv` |
| `threshold_grid.R` | Lưới hai chiều tỷ trọng xuất xưởng × mức truyền dẫn, xuất `output/threshold_grid.csv` |
| `audit.R` | Nạp CSV kiểm toán sản phẩm → 4 tham số, xuất `data/audit_params.csv` |
| `run_all.R` | Điều khiển toàn bộ |

## VHLSS

Microdata **không tải được công khai** cho các vòng gần đây. Cần đăng ký với TCTK
hoặc qua World Bank Microdata Library. Vòng 2024 có khoảng 47.000 hộ.

`vhlss.R` có hai đường:

- **Có microdata** → `profile_from_microdata()` tính ngũ phân vị theo chi tiêu
  bình quân đầu người có trọng số khảo sát, và tỷ trọng chi cho đồ uống.
- **Không có** → `fallback_profile()` dựng 5 nhóm từ các mốc công bố
  (chi tiêu bình quân 3,0 triệu/người/tháng; tỷ số Q5/Q1 ≈ 4,5) cộng ba giả định:
  sản lượng SSB tăng theo chi tiêu, tỷ trọng chi cho SSB giảm theo chi tiêu,
  và độ co giãn giảm theo chi tiêu.

Mọi dòng do đường dự phòng tạo ra đều mang `FALLBACK = TRUE`, và `run_all.R`
in cảnh báo. **Không được báo cáo kết quả công bằng mà không khai điều này.**

Cột mong đợi và cách ánh xạ ở `vhlss_column_map()`. Tên cột khác nhau giữa các
vòng — sửa ở đó, đừng sửa phần còn lại.

## Hai phân đoạn sản phẩm — vì sao cần

Nếu mô hình chỉ có **một** nhóm đồ uống chịu thuế với **một** độ co giãn, thì
thuế theo gam đường và thuế theo giá **cho kết quả giống hệt nhau khi cân bằng
doanh thu**. Lý do: cân bằng doanh thu buộc mức tăng giá bình quân phải bằng
nhau, và với một độ co giãn thì cùng mức tăng giá bình quân cho cùng mức giảm
tiêu thụ. Khi đó câu "thuế theo gam đường hiệu quả hơn trên mỗi đồng doanh thu"
là **không có cơ sở trong mô hình**.

Cơ chế thật chỉ xuất hiện khi tách sản phẩm theo hàm lượng đường: thuế theo gam
đánh mạnh vào nhóm nhiều đường, gây thay thế **trong nội bộ** nhóm chịu thuế
(từ nhiều đường sang ít đường), và đó là phần lợi ích mà thuế theo giá không tạo
ra. Mô hình vì vậy có hai phân đoạn: nhiều đường (≥8 g/100 mL) và ít đường
(5–8 g/100 mL), với độ co giãn chéo giữa chúng.

## Chỉ số công bằng

- `concentration_index()` — dương nghĩa là tập trung ở nhóm giàu.
- `gini_from_quintiles()` — **cận dưới**, vì bỏ qua bất bình đẳng trong nội bộ nhóm.
- `atkinson_ede()` — sức khỏe tương đương ở e = 1, 3, 10.

## Đã sửa trong vòng này

**Độ trễ.** `bmi_change_dynamic()` giờ trả về **đường** BMI theo từng năm, không
phải một giá trị. PIF ở chu kỳ *t* dùng BMI của năm *t − latency*. Hệ quả: lợi
ích giảm khoảng 29% so với bản áp PIF ngay từ năm đầu — tức bản trước đã ước
tính cao.

**Dấu của số hạng thay thế.** Bản trước cộng thêm `elast_cross_unt × dp` vào
tiêu thụ đồ uống chịu thuế. Đó là đếm hai lần và sai dấu: khi độ co giãn chéo
lớn hơn |độ co giãn riêng|, một lần **tăng** giá lại làm **tăng** tiêu thụ, và
DALY tránh được ra âm. Đã bỏ; độ co giãn chéo giờ chỉ dùng để báo cáo mức thay
thế sang đồ uống không chịu thuế.

**Hiệu chuẩn tỷ trọng xuất xưởng.** `calibrate_exfac_share(rev, tau, qprof, p)`
nhận dự toán thu và trả về tỷ trọng hàm ý. Đây là hàm dùng ngay khi có số từ Bộ
Tài chính.

## Đã có dữ liệu thật

| Đầu vào | Nguồn | Hàm nạp |
|---|---|---|
| Cơ cấu tuổi | UN WPP 2024 | `load_age_weights()` |
| Dịch tễ 3 bệnh | GBD 2021, Việt Nam | `load_gbd_params()` |
| Chi phí y tế | Le 2017; Phạm 2024; Doãn 2022 | `load_cost_params()` |
| Kiểm toán sản phẩm | **chưa có** | `read_audit()` → `apply_audit()` |

## Không còn tham số giả định nào



Ba cái giữa đóng được bằng một tuần kiểm toán: xuất CSV theo phiếu ở
`Kiem_toan_rut_gon.md`, rồi

```r
source("model/audit.R")
est <- audit_estimates(read_audit("data/audit.csv"))
p <- apply_audit(params_default(), est)
write_audit_params(est)
```

## Hai việc còn lại

1. **Dự toán thu** → `calibrate_exfac_share()`.
2. **** → kiểm toán sản phẩm, hoặc khảo sát trên toàn dải ở Phụ lục G.
