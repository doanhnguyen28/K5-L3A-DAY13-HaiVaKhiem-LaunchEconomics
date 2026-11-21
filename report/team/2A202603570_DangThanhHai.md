# Báo cáo cá nhân — DangThanhHai-2A202603570

## 1. Thông tin thành viên

- Họ tên: Đặng Thanh Hải
- MSSV: 2A202603570
- Email: haidangbk.nd@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người kiểm số ca 1, người viết code ca 2 (TV2)

## 2. Phần việc phụ trách

- Theo phân công (`chiaviec.md`): kiểm số và điền bảng A, B trong `report/team/bang_chi_phi.md` ở ca 1; nhận `src/lab13.py` sau giải lao và viết `TODO CP4` (cỡ mẫu D1); tính ba chỉ số E; làm hội đồng chấm chéo cùng TV3 (`phieu_cham.md`); gộp commit cuối và push `main`.
- Chủ file: `src/lab13.py` (sau giải lao), `report/team/pilot_plan.yaml` (TV1 điền nội dung theo phân công CP4).

## 3. Đóng góp cụ thể

- **Kiểm số ca 1 (CP1, CP2):** đối chiếu bảng A2–A4, B1–B4 trong `bang_chi_phi.md` (do TV1 commit) với output `lab13.py`: số việc thành công 978; chi phí mỗi việc thành công 4.472 đ [simulated]; chi phí cả hệ thống 0,49× [simulated]; tỉ lệ ok theo lần thử của quoc_te 30,0% → 11,4% → 2,2%. Kiểm quy tắc "giảm một nửa = nửa mức gấp đôi" (5,6 → 2,8 · 40,7 → 20,3 · 51,8 → 25,9) và "cặp = tổng hai tác động" (5,6% + 40,7% = 46,3%).
- **Code ca 2 (CP4) trong `src/lab13.py`:**
  - `co_mau(p1, p2)`: cỡ mẫu mỗi nhóm khi so hai tỉ lệ, z chính xác → **1.251**.
  - `he_so_thiet_ke(m)`: DE = 1 + (m − 1) × ICC.
  - `cau_d1()`: năm câu D1 — b DE 2,48 → **3.103** mỗi nhóm (42 người/nhóm > 40); c tối đa **1.000**; d tối đa **300**; e giải bằng công thức m ≥ n(1 − ICC) / (20 − n·ICC) → **m ≥ 299**, DE 6,96; power ở mức 5 điểm khi n = 859 là **0,64** (statsmodels `NormalIndPower`).
  - Tỉ lệ `mo_lai_trong_7_ngay` hiện tại **4,25%** (51/1.200), trong phạm vi noi_dia + hang_nang **3,97%** — số dùng để đặt luật dừng an toàn.
- **CP5:** `chi_so_e()` tính ba chỉ số trên 1.200 yêu cầu chạy thử: chính **82,83%** (994/1.200) · dùng **27,12%** (48/177) · an toàn **4,25%** (51/1.200).
- **Sửa lỗi chạy trên Windows:** `python lab13.py` báo `UnicodeEncodeError` khi in tiếng Việt (console cp1252); thêm `sys.stdout.reconfigure(encoding='utf-8')` để máy khác trong nhóm chạy được không cần đặt biến môi trường.
- **Soát `pilot_plan.yaml` của TV1:** `yaml.safe_load` đọc được, không còn dấu `?` ngoài chú thích, số D1 khớp output code, 4 luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ.
- Gửi số D1 cho TV1 (điền `pilot_plan.yaml`) và ba chỉ số cho TV3, TV4 (`chi_so.md`, hồ sơ launch).

## 4. Bằng chứng

- Commit `6e137c2` — "CP4+CP5: co_mau, 5 câu D1, power 0,64, tỉ lệ mở lại, 3 chỉ số E; sửa lỗi in tiếng Việt trên Windows" (`src/lab13.py`, +74 dòng).
- Output `cd src && python lab13.py` (đoạn cuối):

  ```text
  == D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ==
  a) Chia theo yêu cầu: 1,251 yêu cầu mỗi nhóm
  b) Theo nhân viên, m = 75: DE = 2.48 → 3,103 mỗi nhóm → 42 người mỗi nhóm, tổng 84 > 40: không đủ người
  c) 20 nhân viên mỗi nhóm: tối đa 1,000 < 1,251: không đạt
  d) 6 depot mỗi nhóm: tối đa 300
  e) Mức chênh 6 điểm (859 mỗi nhóm), 20 người mỗi nhóm: m ≥ 299 yêu cầu mỗi người (DE 6.96)
  Power ở mức 5 điểm khi n = 859: 0.64
  Tỉ lệ mo_lai_trong_7_ngay hiện tại: 4.25% (51/1200) · trong phạm vi noi_dia + hang_nang: 3.97%

  == E · Ba chỉ số trên 1.200 yêu cầu chạy thử ==
  Chính    82.83% (994/1200)
  Dùng     27.12% (48/177)
  An toàn  4.25% (51/1200)
  ```

- Commit gộp cuối và push `main`: (điền hash)

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Opus):** kiểm tra tiến độ phần việc so với `chiaviec.md`; viết các hàm `co_mau`, `he_so_thiet_ke`, `cau_d1`, `chi_so_e` và phần in kết quả D1, E.
- **Cách tự kiểm tra:**
  - Chạy `lab13.py` và so từng con số với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: cả năm câu D1, power 0,64, tỉ lệ mở lại và ba chỉ số đều khớp (lệch 0%).
  - Kiểm tay câu e: 20m ≥ 859 × (0,98 + 0,02m) → 2,82m ≥ 841,82 → m ≥ 298,5 → 299; DE = 1 + 298 × 0,02 = 6,96; 20 × 299 / 6,96 = 859,2 ≥ 859.
  - Kiểm tay câu b: 1 + 74 × 0,02 = 2,48; 1.251 × 2,48 = 3.102,5 → 3.103; 3.103 / 75 = 41,4 → 42 người mỗi nhóm.
  - Không ghi sẵn đáp án vào code: câu e được giải từ công thức nên đổi ICC hoặc mức chênh thì kết quả tự đổi theo.

## 6. Tự đánh giá

- Hiểu và giải thích được: vì sao chia theo nhân viên 20 + 20 không đủ mẫu cho mức chênh 5 điểm (cỡ mẫu hiệu dụng tối đa c / ICC = 1.000 < 1.251); vì sao số cụm, không phải tổng số yêu cầu, quyết định cỡ mẫu; vì sao chấp nhận mức chênh 6 điểm phải nói kèm con số bất lợi power 0,64; vì sao không đặt ngưỡng an toàn tuyệt đối 3% khi tỉ lệ hiện tại đã là 4,25%.
- Hạn chế: phần code ca 2 chủ yếu do AI viết, tôi kiểm tra bằng cách chạy và tính tay đối chiếu; bảng A, B được TV1 commit nên phần kiểm số ca 1 của tôi không có commit riêng.
