# Bản thảo — gói nộp bài

Tác giả: **Nguyen Thanh Nam** (liên hệ), **Khanh Linh Lam Ngoc**
Khoa Y tế Công cộng, Đại học Y Dược Thành phố Hồ Chí Minh

Tạp chí mục tiêu: *The Lancet Regional Health – Western Pacific*

## Nội dung

| Tệp | Dùng để |
|---|---|
| `Manuscript_EN.md` | Bản nộp chính (tiếng Anh) |
| `Manuscript_VI.md` | Bản dịch, cho hội đồng và cơ quan chủ trì đọc |
| `Appendices_EN.md` | Phụ lục A–H (tài liệu bổ sung) |
| `Appendices_VI.md` | Phụ lục A–H, bản dịch |
| `Cover_letter.md` | Thư gửi toà soạn |
| `Figures/fig1–4.png` | Bốn hình, 300 dpi |
| `Figures/make_figures.R` | Script sinh lại toàn bộ hình |

## Số liệu chính

| | |
|---|---|
| Tăng giá bán lẻ 2027 / 2028 | 4,36% / 5,45% |
| DALY tránh được, 2027–2050 | 23.614 (KTC 95%: 9.956–53.043) |
| Ca bệnh tránh được | 32.625 |
| Chi phí y tế tiết kiệm | 1.500 tỷ đồng |
| Doanh thu | 2.731 tỷ đồng |
| DALY/1.000 dân: Q1 / Q5 | 0,27 / 0,35 |
| Thuế / chi tiêu hộ: Q1 / Q5 | 0,133% / 0,079% |
| Kakwani | −0,326 |

## Trước khi nộp

- [ ] Chuyển `.md` sang `.docx` theo mẫu của tạp chí (Lancet yêu cầu Word; có thể dùng Pandoc hoặc Google Docs → Download as .docx)
- [ ] Đổi tên hình theo quy ước của tạp chí (thường `Figure1.png`, `Figure2.png`…)
- [ ] Kiểm tra lại độ dài tóm tắt so với giới hạn hiện hành của *Lancet Regional Health – WP*
- [ ] Điền thông tin tài khoản nộp bài trên Editorial Manager
- [ ] Chuẩn bị checklist CHEERS 2022 (Phụ lục E) dưới dạng tệp riêng nếu toà soạn yêu cầu

## Ghi chú kỹ thuật

- Bốn hình sinh từ `output/` trong kho mã, bằng `Rscript Ban_thao/Figures/make_figures.R`
- Mọi con số trong bản thảo lấy từ `output/results.json`
- Mã và dữ liệu: https://doi.org/10.5281/zenodo.23852996
