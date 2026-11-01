# Kiểm toán sản phẩm — bản rút gọn 1 tuần

> Dùng khi không đủ thời gian cho bản đầy đủ ở Phụ lục C (4 tuần, 2 thành phố + 2 huyện, 3 kênh).
> **Cửa sổ: phải xong trước 31/12/2026.** Sau ngày đó không thể lấy lại mốc giá trước thực thi.
> Bản rút gọn vẫn cho ra ba thứ không thể thay thế: tỷ trọng sản phẩm vượt ngưỡng 5 g/100 mL, danh sách SKU sát ngưỡng cho kịch bản S3, và mốc giá bán lẻ trước thuế.

---

## 1. Phạm vi

| Hạng mục | Bản đầy đủ | **Bản rút gọn** |
|---|---|---|
| Địa bàn | Hà Nội, TP.HCM + 2 huyện | **Hà Nội, TP.HCM** |
| Kênh | Hiện đại, truyền thống, online | **Hiện đại + online** (bỏ truyền thống) |
| Cửa hàng | ~24 | **12** (5 siêu thị + 3 chuỗi tiện lợi + 4 shop online, mỗi thành phố) |
| SKU mục tiêu | 200–250 | **100–120** |
| Thời gian | 4 tuần | **1 tuần** (5 ngày thực địa + 2 ngày xử lý) |
| Người | 2 điều tra viên + giám sát + phân tích | **2 người, kiêm nhiệm** |

**Cái mất đi:** độ phủ kênh truyền thống (tạp hóa, chợ) — nơi giá thấp hơn và sản phẩm khác chủng loại — và đại diện nông thôn. Viết đúng một câu trong Hạn chế: *"Kiểm toán chỉ phủ kênh hiện đại tại hai đô thị lớn; giá ở kênh truyền thống và vùng nông thôn có thể thấp hơn, nên mức giá cơ sở có thể bị ước tính cao."*

**Cái không mất:** ba đầu ra chính vẫn tính được, vì chúng phụ thuộc vào **thành phần sản phẩm**, không vào số cửa hàng.

---

## 2. Lịch 7 ngày

| Ngày | Việc | Đầu ra |
|---|---|---|
| D1 | Chốt danh sách cửa hàng; in phiếu; thử 1 siêu thị | Danh sách 12 điểm; phiếu đã sửa |
| D2–D4 | Thực địa Hà Nội (6 điểm) | Ảnh + phiếu |
| D5–D6 | Thực địa TP.HCM (6 điểm) | Ảnh + phiếu |
| D7 | Nhập liệu, phân xử sát biên, tính toán | Bộ CSV + 4 con số |

Nếu chỉ có 1 người: D2–D6 rút còn 4 ngày, mỗi ngày 2–3 điểm.

---

## 3. Cách chọn sản phẩm

**Không chọn.** Trong mỗi cửa hàng, ghi **mọi** SKU thuộc phạm vi có trên kệ. Chọn lọc là nguồn sai số lớn nhất và dễ bị phản biện nhất.

Phạm vi (theo TCVN 12828:2019): nước ngọt có ga, nước ngọt không ga, nước tăng lực, nước thể thao/điện giải, trà pha sẵn, cà phê pha sẵn, đồ uống thảo mộc, đồ uống chứa nước trái cây, đồ uống từ ngũ cốc.

Ngoài phạm vi, **ghi riêng một dòng** để chứng minh đã xét: sữa và sản phẩm sữa, thực phẩm lỏng dinh dưỡng, nước khoáng/đóng chai, nước ép 100%, nectar, ca cao.

---

## 4. Phiếu thu thập (một dòng = một SKU)

Sao chép khối dưới vào Google Sheets/Excel, hoặc dùng làm biểu mẫu giấy.

| Trường | Kiểu | Ghi chú |
|---|---|---|
| `sku_id` | text | `HN-SM1-014` = thành phố-cửa hàng-số thứ tự |
| `city` | text | HN / HCM |
| `channel` | list | sieuthi / tienloi / online |
| `outlet` | text | tên cửa hàng |
| `date` | date | yyyy-mm-dd |
| `brand` | text | như in trên bao bì |
| `product` | text | tên đầy đủ |
| `barcode` | text | để trống nếu không có |
| `pack_ml` | number | quy về mL (330 mL, 1.5 L = 1500) |
| `category` | list | soda_co_ga / soda_khong_ga / tang_luc / the_thao / tra / ca_phe / thao_moc / chua_nuoc_qua / ngu_coc |
| `sugar_g_per_100ml` | number | **TỔNG đường trên nhãn** — không phải đường bổ sung |
| `sweetener_type` | list | duong / phi_calo / ca_hai / khong_ro |
| `price_vnd` | number | giá trên kệ, đã gồm VAT |
| `promo` | y/n | có khuyến mại không |
| `photo_front` | y/n | đã chụp mặt trước |
| `photo_nutrition` | y/n | đã chụp nhãn dinh dưỡng |
| `photo_price` | y/n | đã chụp tem giá |
| `borderline` | y/n | chạm một trong 4 quy tắc ở mục 6 |
| `note` | text | |

**Ba lỗi chết người cần tránh:**

1. Ghi **đường bổ sung** thay vì **tổng đường**. Nghị định 360 dùng tổng đường trên nhãn. Ghi sai sẽ phân loại sai sản phẩm.
2. Ghi giá **chưa VAT**. Giá kệ đã gồm VAT — giữ nguyên, đừng trừ.
3. Bỏ qua sản phẩm không có nhãn. Ghi `sugar_g_per_100ml` để trống và đánh dấu `khong_ro` — tỷ lệ này tự nó là một phát hiện.

---

## 5. Chụp ảnh

Ba ảnh mỗi SKU, đặt tên `sku_id_1.jpg`, `_2`, `_3`. Ảnh nhãn dinh dưỡng là ảnh quan trọng nhất — không có nó thì không kiểm lại được số.

Nếu cửa hàng không cho chụp: ghi số vào phiếu ngay tại chỗ, và ghi chú `no_photo`.

---

## 6. Bốn quy tắc cho sản phẩm sát biên

Đánh dấu `borderline = y` và ghi lý do khi chạm một trong bốn:

1. Nhãn ghi **100% nước quả**, không có đường bổ sung, không có nước thêm → **ngoài phạm vi** (nước quả).
2. Có **nước quả + đường bổ sung hoặc nước thêm** → **trong phạm vi** (đồ uống chứa nước quả).
3. Nhãn ghi **"nectar"** hoặc hàm lượng quả <100% kèm đường → **ngoài phạm vi**, nhưng đánh dấu.
4. **Nước dừa**: thành phần chỉ có nước dừa → ngoài phạm vi; có thêm đường → trong phạm vi.

Các sản phẩm này sẽ được liệt kê riêng để dựng kịch bản diễn giải rộng/hẹp.

---

## 7. Tính toán (ngày 7)

Chạy bốn phép tính, xuất một bảng:

**7.1 Tỷ trọng vượt ngưỡng — ba ước lượng**

```
p_sku      = số SKU có sugar > 5  /  tổng số SKU
CI         = khoảng Clopper–Pearson 95% cho p_sku
p_weighted = Σ (w_c × p_c)   với w_c = tỷ trọng sản lượng nhóm c (Euromonitor)
p_lower    = tỷ trọng khi giả định sản phẩm trên ngưỡng chỉ chiếm sản lượng bình quân nhóm
```

Dùng `p_weighted` làm giá trị trung tâm cho tham số #4, `p_lower` làm kịch bản bi quan.

**7.2 Phân bố hàm lượng đường** — histogram bin 1 g/100 mL; đếm riêng số SKU trong dải **5,0–8,0 g** (nhóm ứng viên giảm đường cho S3).

**7.3 Giá bình quân mỗi lít** theo nhóm và theo kênh: `price_vnd / (pack_ml/1000)`.

**7.4 Giá trên mỗi gam đường**: `price_vnd / (pack_ml/100 × sugar)`. Đây là đại lượng mà thuế theo gam sẽ tác động.

---

## 8. Câu viết vào bài

Chỉ cần ba câu, đặt ở Phụ lục C:

> Tổng cộng ⟦n⟧ sản phẩm thuộc phạm vi được ghi nhận tại 12 cửa hàng thuộc kênh hiện đại và trực tuyến ở Hà Nội và TP.Hồ Chí Minh trong tháng ⟦11/2026⟧. Trong đó ⟦n1⟧ sản phẩm (⟦p⟧%, KTC 95% ⟦⟧–⟦⟧) có hàm lượng đường trên 5 g/100 mL, và ⟦n2⟧ sản phẩm nằm trong dải 5,0–8,0 g/100 mL. Kênh truyền thống và địa bàn nông thôn không được khảo sát.

---

## 9. Nếu chỉ làm được một nửa

Thứ tự cắt, từ nên giữ đến nên bỏ:

1. **Giữ** — ảnh nhãn dinh dưỡng của mọi SKU (cho tham số #4 và S3).
2. **Giữ** — giá của ít nhất 40 SKU (cho mốc giá).
3. **Giữ** — đánh dấu sản phẩm sát biên.
4. Bỏ — kênh online.
5. Bỏ — thành phố thứ hai (chỉ Hà Nội vẫn dùng được, kém đại diện hơn).

Một thành phố, 60 SKU, một người, ba ngày: vẫn hơn không có gì.
