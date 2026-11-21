# Báo cáo cá nhân — HoVaTen-MSSV (TV1)

> Đổi tên file thành `MSSV_HoTen.md` (vd. `20241234_NguyenVanAn.md`) và điền các chỗ `...`.

## 1. Thông tin thành viên

- Họ tên: Hoàng Gia Khiêm   
- MSSV: 2A202603540
- Email: khiemhg0709@gmail.com
- Vai trong nhóm: **Người viết code ca 1**

## 2. Phần việc phụ trách

- `src/lab13.py` tới giải lao: CP1 (A1–A4) và CP2 (B1–B4), bàn giao cho TV2 làm CP4.
- `report/team/bang_chi_phi.md` (chủ file): bảng A1–A4, B1–B4 và các câu trả lời.
- CP4: kiểm tay câu e và DE, điền mọi dấu `?` trong `report/team/pilot_plan.yaml`, ghi D1 + D2 ở phần chú thích.
- CP5: viết mục E2 · Rủi ro kinh tế trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) → ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- Viết `mo_hinh(...)`: tử số cộng token + tool của **mọi** lần chạy (kể cả lỗi) + phút xem lại/làm lại [simulated]; mẫu số chỉ đếm `thanh_cong` (978). Kết quả 4.472 đ/việc thành công [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu (274,7 đ).
- Viết `tach_theo_loai`, `ti_le_ok_theo_lan_thu` (A3), `chi_phi_co_dinh` (A4), `bang_do_nhay` (B1 9 kịch bản + B2 cặp), `chi_phi_ca_he_thong` (B3), `xem_lai_toan_bo` (B4, kèm mức hoà vốn phút xem lại).
- Kết luận chính: quoc_te 1,88× không đáng chạy, chạy lại không giúp (ok 30% → 11,4% → 2,2%); giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ); xem lại 100% ≈ 0,98–1,03× [simulated].
- Pilot plan: chia theo nhân viên 20 + 20, MDE 6 điểm, n = 859/nhóm, DE 6,96, m ≥ 299; 4 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ.
- E2: 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy, có nhãn simulated và người phụ trách.

## 4. Bằng chứng

- Commit: ... (vd. `CP1: mo_hinh + bang A2`, `CP2: bang do nhay B1-B4`, `CP4: dien pilot_plan.yaml`, `CP5: rui ro kinh te`)
- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, mục E2 của `report/team/chi_so.md`.
- Số đối chiếu với slide chữa: A2 4.472 đ, A3 2.696 / 8.221 / 22.515 / 10.215 đ, B1 +5,6% … −8,1%, B3 6.901.220 đ, B4 11.743 đ — lệch 0% (≤ 2%).

## 5. Công cụ AI đã dùng

- Dùng Claude để gợi ý khung code `mo_hinh` và các hàm B, và để soạn nháp bảng trong `bang_chi_phi.md`.
- Tự kiểm tra: chạy `python lab13.py` → ba phép thử ĐẠT; tính tay token = Σ(tokens_in/1000 × 26 + tokens_out/1000 × 130) và tool = 5.600 × 15 = 84.000 đ; kiểm quy tắc "giảm một nửa = nửa mức gấp đôi" (40,7 → 20,3); giải tay câu e: 20m ≥ 859 × (0,98 + 0,02m) → m ≥ 298,5 → 299; kiểm `yaml.safe_load` và `grep` không còn `?`.

## 6. Tự đánh giá

- **Mức hoàn thành:** xong phần việc được giao. Ba phép thử A1 ĐẠT; số A2–A4, B1–B4 khớp số đối chiếu (lệch 0%, ngưỡng 2%); `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?`, có 4 luật dừng đủ 4 vế.
- **Làm tốt:** viết `mo_hinh(...)` nhận sẵn tham số nên phần B chỉ cần gọi lại; tách được hai con số dễ nhầm: chi phí mỗi việc thành công 4.472 đ và chi phí cả hệ thống 5.865 đ = 0,49× [simulated]; chỉ ra giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ [simulated]) dù không phải giới hạn có chi phí mỗi việc thành công thấp nhất.
...