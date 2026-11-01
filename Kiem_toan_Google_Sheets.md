# Bảng nhập kiểm toán — dựng trên Google Sheets

## 1. Tạo bảng (2 phút)

1. Vào [sheets.new](https://sheets.new) → đặt tên `Kiem toan SSB 2026`.
2. **File → Import → Upload** → chọn `data/audit_template.csv`.
3. Chọn *Replace spreadsheet*. Chọn dấu phân cách là **dấu phẩy**.
4. Xoá 3 dòng ví dụ (dòng 2–4). Giữ nguyên dòng 1.

## 2. Cột

| Cột | Tên | Ghi gì |
|---|---|---|
| A | `sku_id` | `HN-WM-001` = thành phố-nguồn-số thứ tự |
| B | `date` | `2026-11-05` |
| C | `source` | tên cửa hàng hoặc website |
| D | `channel` | `online` / `sieu_thi` / `tien_loi` |
| E | `city` | `Ha Noi` / `HCM` |
| F | `brand` | như in trên bao bì |
| G | `product` | tên đầy đủ + dung tích |
| H | `pack_ml` | **số mL** (1,5 L = 1500) |
| I | `category` | xem danh mục bên dưới |
| J | `sugar_printed_g` | **số gam đường in trên nhãn** — đúng như in |
| K | `sugar_basis_ml` | số mL mà con số đó ứng với |
| L | `sugar_g_per_100ml` | **công thức tự tính — không gõ tay** |
| M | `sweetener_type` | `duong` / `phi_calo` / `ca_hai` / `khong_ro` |
| N | `price_vnd` | giá, đơn vị đồng, không chấm phẩy |
| O | `promo` | `y` / `n` |
| P | `borderline` | `y` nếu là nước ép / nectar / nước dừa |
| Q | `photo_link` | dán link ảnh nếu lưu trên Drive |
| R | `note` | ghi chú |

## 3. Công thức cột L — dòng quan trọng nhất

Ô **L2**:

```
=IFERROR(J2/K2*100,"")
```

Kéo xuống hết bảng.

Đây là chỗ chống lỗi lớn nhất. Nhãn dinh dưỡng Việt Nam thường ghi theo **khẩu phần**, không theo 100 mL:

| Nhãn ghi | Nhập J | Nhập K | L tự ra |
|---|---|---|---|
| 10,6 g / 100 mL | `10.6` | `100` | **10,6** |
| 35 g / 330 mL | `35` | `330` | **10,6** |
| 12 g / 250 mL | `12` | `250` | **4,8** |

Nếu bạn gõ thẳng 35 vào L, mô hình sẽ tưởng sản phẩm có 35 g/100 mL — sai gấp ba, và nó sẽ đẩy sản phẩm vào sai phân đoạn.

## 4. Danh sách cho dropdown

Tạo sheet mới tên `Lists`, dán vào:

**Cột A — category** (đặt tên vùng `cat_list`):
```
soda_co_ga
soda_khong_ga
tang_luc
the_thao
tra
ca_phe
thao_moc
chua_nuoc_qua
ngu_coc
ngoai_pham_vi
```

**Cột B — channel** (`channel_list`): `online`, `sieu_thi`, `tien_loi`

**Cột C — sweetener** (`sweet_list`): `duong`, `phi_calo`, `ca_hai`, `khong_ro`

**Cột D — yes/no** (`yn_list`): `y`, `n`

Rồi chọn vùng dữ liệu → **Data → Data validation → Add rule → Dropdown (from a range)** → trỏ tới vùng tương ứng.

## 5. Ba quy tắc định dạng có điều kiện

**Data → Conditional formatting**, áp cho `L2:L1000`:

| Điều kiện | Màu | Nghĩa |
|---|---|---|
| `L2 > 5` | đỏ nhạt | sản phẩm chịu thuế |
| `L2 > 5` và `L2 <= 8` | vàng | **nhóm ứng viên giảm đường cho S3** |
| `L2 <= 5` | xám | ngoài diện |

Áp cho `J2:K1000`: định dạng **Number → 1 chữ số thập phân**, để tránh `10,6` thành `106`.

## 6. Nhập nhanh trên điện thoại

Dùng **app Google Sheets**, mở bảng, thêm dòng bằng nút `+`. Bật **Data validation** thì mỗi ô chỉ cần chạm chọn.

Với ảnh: chụp bằng camera điện thoại, cuối ngày tải lên Drive, dán link vào cột Q. Hoặc bỏ cột Q nếu ảnh chỉ để đối chiếu cá nhân.

## 7. Xuất để chạy mô hình

**File → Download → Comma-separated values (.csv)** → đặt vào `data/audit.csv`.

Kiểm tra nhanh trước khi giao:

```r
source("model/audit.R")
d <- read_audit("data/audit.csv")
nrow(d)                     # phải bằng số dòng bạn nhập
sum(is.na(d$sugar_g_per_100ml))   # phải bằng 0
summary(d$sugar_g_per_100ml)      # phải nằm trong 0-20, không có 35 hay 106
```

Dòng cuối là phép kiểm tra quan trọng nhất. Nếu `max` lớn hơn ~20, gần như chắc chắn có dòng chưa quy đổi khẩu phần — quay lại cột J/K.

## 8. Thứ tự ưu tiên khi thiếu thời gian

1. Cột **J, K, H, I** của mọi sản phẩm — đây là thứ mô hình cần
2. Cột **P** (sát biên) — cho kịch bản diễn giải rộng/hẹp
3. Cột **N** (giá) — cho mốc giá
4. Cột **M** (chất tạo ngọt) — trả lời câu hỏi pháp lý còn mở

Không có cột A–G thì vẫn chạy được. Không có J–K thì không.
