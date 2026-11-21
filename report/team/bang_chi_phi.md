# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (= (1 − 0,2²) / 0,8) · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (= 1 / 0,8) · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (= 1,24 / 0,992 = 1/p, k triệt tiêu) · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu (4.472 / 274,7) [simulated]; giờ nhân viên chiếm 92,5% tổng chi phí.
- Khoản lớn nhất là **làm lại, 51,8%** [simulated], tiếp theo là xem lại 40,7% [simulated]; token + tool chỉ 7,5%.
- So với 12.000 đ phải dùng chi phí cả hệ thống: (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated] (không viết 0,37× vì chưa cộng 222 ca không thành công nhân viên làm thay).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

Tỉ lệ ok theo lần thử (đo từ trace): quoc_te 30,0% → 11,4% → 2,2%; doi_tac 51,5% → 18,2% → 14,8%; hang_nang 70,9% → 39,1% → 17,9%; noi_dia 91,0% → 75,7% → 38,9%.

- **quoc_te không đáng chạy:** 22.515 đ = 1,88× [simulated], chỉ 27,3% thành công. Chạy lại không giúp vì lỗi lặp trên cùng yêu cầu: lần 2 chỉ ok 11,4%, lần 3 chỉ 2,2%.
- doi_tac sát ngưỡng (0,85× [simulated]) và có điều khoản riêng → cũng loại khỏi phạm vi pilot; giữ noi_dia + hang_nang.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Chi phí mỗi việc thành công trong phạm vi = 3.072.513 / 900 = 3.414 đ [simulated]; việc thành công mỗi tháng = 45.000 × 900 / 1.200.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Cố định 40 triệu/tháng **không đổi kết luận** ở quy mô đầy đủ (0,38×) nhưng tăng gấp đôi khi khối lượng còn một nửa (+2.370 đ/việc, 0,48×) [simulated]; giai đoạn pilot khối lượng nhỏ nên phải ghi rõ đã cộng cố định ở khối lượng nào.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" đúng bằng nửa mức "gấp đôi" (5,6 → 2,8 · 40,7 → 20,3 · 51,8 → 25,9) vì mô hình tuyến tính.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated] = 5,6% + 40,7%, đúng tổng hai tác động riêng.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (±51,8% / 25,9%) · 2. **tỉ lệ xem lại** (±40,7% / 20,3%) · 3. **lương nhân viên** (+23,1%) [simulated]. Giá token chỉ +5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ (thấp nhất) [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | **6.901.220 đ (rẻ nhất)** [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- **Giới hạn 2 lần rẻ nhất cho công ty** (6.901.220 đ [simulated]), không trùng với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ).
- Tối ưu riêng chi phí mỗi việc thành công (1 lần) đẩy thêm 85 việc sang nhân viên, cả hệ thống đắt hơn 548.561 đ [simulated].

## B4 · Nếu phải xem lại tất cả

Phạm vi noi_dia + hang_nang (982 yêu cầu): 948 yêu cầu có ≥ 1 lần ok × 5 phút = 9.480.000 đ; 48 ca lam_lai; token + tool 224.513 đ; 900 việc thành công.

- Làm lại 9 phút/ca (đề cho): 10.568.513 / 900 = **11.743 đ = 0,98×** [simulated]. Làm lại 15,3 phút/ca (trung bình cột `phut_lam_lai_simulated`): **12.415 đ = 1,03×** [simulated], đắt hơn nhân viên tự làm.
- Hoà vốn: mỗi lần xem lại ≤ **5,1 phút** (làm lại 9 phút) hoặc ≤ **4,8 phút** (làm lại 15,3 phút) [simulated]; xem lại chiếm ~90% chi phí.
- Pilot phải học được tỉ lệ xem lại giảm an toàn xuống mức nào và mỗi lần xem lại có dưới 5 phút được không; xem lại 100% thì trợ lý gần như không tiết kiệm.