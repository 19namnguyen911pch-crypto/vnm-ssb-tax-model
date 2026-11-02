# -*- coding: utf-8 -*-
"""Update the Vietnamese manuscript to the corrected model run (RR 1.37)."""
p = "Ban_thao_Tieng_Viet.md"
s = open(p, encoding="utf-8").read()

PAIRS = [
    ("24.767", "19.387"),
    ("10.046–52.842", "7.136–42.913"),
    ("32.625", "24.574"),
    ("29.077", "20.894"),
    ("2.682", "2.778"),
    ("725", "631"),
    ("89.991", "70.670"),
    ("105.442", "76.041"),
    ("3.179", "3.307"),
    ("9.837", "10.181"),
    ("38.514", "30.169"),
    ("45.197", "32.503"),
    ("1.350", "1.405"),
    ("4.179", "4.328"),
    ("1.500", "1.087"),
    ("5.438", "3.956"),
    ("2.331", "1.691"),
    ("53.509", "41.027"),
    ("7.822", "6.280"),
    ("39.894", "31.345"),
    ("18.724", "14.639"),
    ("13.784", "10.784"),
    ("35.710", "27.968"),
    ("16.534", "12.937"),
    ("37.075", "29.039"),
    ("22.632", "17.682"),
    ("8,6%", "8,8%"),
    ("94%", "93%"),
    ("89% số ca", "85% số ca"),
    ("30.274", "23.704"),
    ("52.196", "40.915"),
    ("0,44", "0,43"),
]
for old, new in PAIRS:
    if old not in s:
        print("missing:", old)
    s = s.replace(old, new)

s = s.replace(
    "| DALY tránh được trên 1.000 dân | 0,31 | 1,11 | 0,47 |",
    "| DALY tránh được trên 1.000 dân | 0,24 | 0,87 | 0,37 |")
s = s.replace(
    "| DALY tránh được trên mỗi tỷ đồng doanh thu | 0,5 | 0,6 | 1,1 |",
    "| DALY tránh được trên mỗi tỷ đồng doanh thu | 0,4 | 0,5 | 0,8 |")
s = s.replace(
    "DALY tránh được trên 1.000 dân là 0,27 ở Q1 và 0,35 ở Q5",
    "DALY tránh được trên 1.000 dân là 0,21 ở Q1 và 0,27 ở Q5")
s = s.replace(
    "DALY tránh được trên 1.000 dân là 0,27 ở nhóm nghèo nhất và 0,35 ở nhóm giàu nhất",
    "DALY tránh được trên 1.000 dân là 0,21 ở nhóm nghèo nhất và 0,27 ở nhóm giàu nhất")
s = s.replace("tức 0,31 trên 1.000 dân", "tức 0,24 trên 1.000 dân")
s = s.replace("thuế đã ban hành tạo 0,5 DALY và mốc tham chiếu 0,6",
              "thuế đã ban hành tạo 0,4 DALY và mốc tham chiếu 0,5")
s = s.replace("độ co giãn giá riêng chiếm 50% phương sai được giải thích, mức truyền dẫn 18% và nguy cơ tương đối BMI–đái tháo đường 12%",
              "độ co giãn giá riêng chiếm 45% phương sai được giải thích, nguy cơ tương đối BMI–đái tháo đường 17% và mức truyền dẫn 16%")
open(p, "w", encoding="utf-8").write(s)
print("VI updated")
