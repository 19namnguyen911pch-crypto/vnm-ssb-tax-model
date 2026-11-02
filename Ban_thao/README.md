# Bản thảo — gói nộp bài

Tác giả: **Nguyen Thanh Nam**, **Khanh Linh Lam Ngoc** (liên hệ)
Khoa Y tế Công cộng, Đại học Y Dược Thành phố Hồ Chí Minh

Tạp chí mục tiêu: *The Lancet Regional Health – Western Pacific*

## Nội dung

| Tệp | Dùng để |
|---|---|
| `Manuscript_EN.docx` | **Bản nộp chính** — A4, Times New Roman 12, giãn dòng đôi, số dòng liên tục |
| `Manuscript_VI.docx` | Bản dịch, cho hội đồng và cơ quan chủ trì đọc |
| `Appendices_EN.docx` | Phụ lục A–H (tài liệu bổ sung) |
| `Appendices_VI.docx` | Phụ lục A–H, bản dịch |
| `Cover_letter.docx` | Thư gửi toà soạn |
| `*.md` | Nguồn Markdown, để sửa và chuyển lại DOCX |
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

- [x] Đã chuyển sang `.docx` (A4, TNR 12, giãn đôi, số dòng)
- [ ] Đổi tên hình theo quy ước của tạp chí (thường `Figure1.png`, `Figure2.png`…)
- [ ] Kiểm tra lại độ dài tóm tắt so với giới hạn hiện hành của *Lancet Regional Health – WP*
- [ ] Điền thông tin tài khoản nộp bài trên Editorial Manager
- [ ] Chuẩn bị checklist CHEERS 2022 (Phụ lục E) dưới dạng tệp riêng nếu toà soạn yêu cầu

## Ghi chú kỹ thuật

- Bốn hình sinh từ `output/` trong kho mã, bằng `Rscript Ban_thao/Figures/make_figures.R`
- Mọi con số trong bản thảo lấy từ `output/results.json`
- Mã và dữ liệu: https://doi.org/10.5281/zenodo.23852908
