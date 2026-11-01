# -*- coding: utf-8 -*-
"""Mirror the 3x3 equity grid into the Vietnamese file."""
p = "Ban_thao_Tieng_Viet.md"
s = open(p, encoding="utf-8").read()


def rep(old, new):
    global s
    assert old in s, "NOT FOUND: " + old[:80]
    s = s.replace(old, new, 1)


rep("Vì chiều của gradient bệnh chưa được đo, phân bố lợi ích được báo cáo dưới dạng khoảng: nghiêng về nhóm giàu nhất khi nguy cơ tăng theo chi tiêu (tỷ số 0,60; chỉ số tập trung 0,097), trung gian khi không có gradient (0,77; 0,047), và gần tỷ lệ thuận khi nguy cơ giảm theo chi tiêu (0,99; −0,002). Chỉ số Kakwani giống nhau ở cả ba vì chỉ phụ thuộc vào khoản thuế phải trả. Lợi ích chỉ trở nên nghiêng về nhóm nghèo ở gradient dốc hơn 1,16 tại Q1 giảm còn 0,87 tại Q5.",
"Không gradient bệnh và cũng không gradient độ co giãn nào được đo, và hai yếu tố tác động cùng nhau: qua chín tổ hợp ở Phụ lục F, tỷ số Q1/Q5 chạy từ 0,44 khi nguy cơ nền tăng theo chi tiêu và gradient độ co giãn bằng phẳng, qua 0,77 ở tổ hợp trung tâm, đến 1,28 khi nguy cơ giảm theo chi tiêu và gradient độ co giãn là 1,8, với chỉ số tập trung từ 0,160 đến −0,054. Phân bố lợi ích vì vậy chạy từ nghiêng rõ về nhóm giàu đến nghiêng nhẹ về nhóm nghèo, và gần tỷ lệ thuận ở các giả định trung tâm.")

rep("Phân bố lợi ích sức khỏe kém chắc chắn hơn: nghiêng về nhóm giàu khi không có gradient, gần tỷ lệ thuận trong trường hợp thuận lợi nhất, và chỉ nghiêng về nhóm nghèo ở gradient dốc hơn khoảng 1,16 tại Q1 giảm còn 0,87 tại Q5.",
"Phân bố lợi ích sức khỏe kém chắc chắn hơn: qua các tổ hợp đã thử, nó chạy từ nghiêng rõ về nhóm giàu (Q1/Q5 là 0,44) đến nghiêng nhẹ về nhóm nghèo (1,28), và gần tỷ lệ thuận ở các giả định trung tâm.")

rep("Kết quả phân bố là một khoảng vì gradient chưa được đo. Phía chi trả dựa trên hồ sơ hiệu chỉnh theo bảng công bố của VHLSS chứ không phải dữ liệu vi mô, và trên gradient độ co giãn 1,4; với gradient từ 1,0 đến 1,8, tỷ số Q1/Q5 dịch từ 0,56 đến 1,00 (Phụ lục F), nên phía tài chính cũng có điều kiện.",
"Kết quả phân bố là một khoảng vì không gradient nào được đo: qua chín tổ hợp, tỷ số Q1/Q5 chạy từ 0,44 đến 1,28, trong khi chỉ số Kakwani chỉ dịch từ −0,101 đến −0,093, nên phía chi trả là phía ổn định hơn trong hai phía.")

i = s.index("**F.8 Gradient độ co giãn.**")
j = s.index("**F.9 Các phân tích không thực hiện.**")
s = s[:i] + """**F.8 Gradient bệnh và gradient độ co giãn cùng lúc.** Cả hai gradient đều là giả định, nên được báo cáo cùng nhau. Bảng dưới cho tỷ số Q1/Q5 của DALY tránh được và chỉ số tập trung ở từng tổ hợp giữa gradient bệnh (nguy cơ nền tăng theo chi tiêu, không có, giảm theo chi tiêu) và gradient độ co giãn theo ngũ phân vị (1,0; 1,39 ở kịch bản cơ sở; 1,8). Chỉ số Kakwani và tỷ lệ thuế dịch ít hơn nhiều, vì khoản chi trả phụ thuộc vào tiêu thụ chứ không vào nguy cơ bệnh.

| Nguy cơ nền | Gradient độ co giãn | Q1/Q5 | Chỉ số tập trung | Kakwani | Thuế, Q1 (%) | Thuế, Q5 (%) |
|---|---|---|---|---|---|---|
| Tăng theo chi tiêu | 1,0 | 0,44 | 0,160 | −0,101 | 0,135 | 0,078 |
| Tăng theo chi tiêu | 1,39 | 0,60 | 0,096 | −0,096 | 0,133 | 0,079 |
| Tăng theo chi tiêu | 1,8 | 0,78 | 0,045 | −0,093 | 0,132 | 0,080 |
| Không có | 1,0 | 0,56 | 0,112 | −0,101 | 0,135 | 0,078 |
| Không có | 1,39 | 0,77 | 0,047 | −0,096 | 0,133 | 0,079 |
| Không có | 1,8 | 1,00 | −0,005 | −0,093 | 0,132 | 0,080 |
| Giảm theo chi tiêu | 1,0 | 0,71 | 0,063 | −0,101 | 0,135 | 0,078 |
| Giảm theo chi tiêu | 1,39 | 0,99 | −0,003 | −0,096 | 0,133 | 0,079 |
| Giảm theo chi tiêu | 1,8 | 1,28 | −0,054 | −0,093 | 0,132 | 0,080 |

Lưu ở `output/equity_grid.csv`.

""" + s[j:]

open(p, "w", encoding="utf-8").write(s)
print("VI grid integrated")
