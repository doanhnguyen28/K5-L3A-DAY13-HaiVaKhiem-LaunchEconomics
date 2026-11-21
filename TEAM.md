# Team

## Thông tin nhóm

- Tên nhóm: HaiVaKhiem
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-HaiVaKhiem-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: <https://github.com/doanhnguyen28/K5-L3A-DAY13-HaiVaKhiem-LaunchEconomics> · `main` · (điền hash commit chốt)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Hoàng Gia Khiêm | 2A202603540 | khiemhg0709@gmail.com | khiemhg79 | Người viết code ca 1 (14:00–15:20), kiểm số ca 2 |
|   2 | Đặng Thanh Hải | 2A202603570 | haidangbk.nd@gmail.com | HaiDang0502 | Người kiểm số ca 1, người viết code ca 2 (15:35–18:00) |
|   3 | Nguyễn Đăng Doanh | 2A202603597 | (điền) | doanhnguyen28 | Người gắn nhãn 1 |
|   4 | (điền) | (điền) | (điền) | (điền) | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

Phân công chi tiết theo checkpoint: [chiaviec.md](chiaviec.md).

**Ghi chú nhiệm vụ C:** nhóm không thực hiện bước hai người gắn nhãn độc lập; nhãn trong `report/team/bang_loi.md` lấy theo bảng tham khảo của tài liệu và đã ghi rõ trong file.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## NguyenDangDoanh-2A202603597

### Phần việc phụ trách

- Người gắn nhãn 1 (TV3): `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/phieu_cham.md`, câu trả lời A2, A3, B3, B4, năm câu D2, soát checklist nộp bài.
- Nhận thêm trong buổi: `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`.

### Đóng góp cụ thể

- `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`: điền đủ, số lấy từ `lab13.py`, số giả lập có nhãn `simulated`.
- Làm một bản `lab13.py` song song để đối chiếu (cùng kết quả số); khi gộp, nhóm giữ bản `lab13.py`, `bang_chi_phi.md`, `pilot_plan.yaml` của TV1/TV2.
- `bang_loi.md`: bảng khắc phục 5 ca; nhãn 20 ca theo bảng tham khảo (không gắn độc lập).
- Dùng Claude Code cho phần lớn code và văn bản; tự kiểm tra bằng cách so với số đối chiếu trong tài liệu (chi tiết trong báo cáo cá nhân).

### Bằng chứng

- Báo cáo cá nhân: [report/team/2A202603597_NguyenDangDoanh.md](report/team/2A202603597_NguyenDangDoanh.md)
- Output `cd src && python lab13.py`: ba phép thử ĐẠT, chi phí mỗi việc thành công 4.472 đ [simulated].
- Commit: (điền hash)

## HoangGiaKhiem-2A202603540

### Phần việc phụ trách

- Người viết code ca 1 (TV1): `src/lab13.py` phần CP1 (A1–A4) và CP2 (B1–B4), bàn giao cho TV2 trước giải lao.
- Chủ file `report/team/bang_chi_phi.md`; sau giải lao làm người kiểm số (CP3).
- CP4: kiểm tay DE và câu e, điền `report/team/pilot_plan.yaml`. CP5: soạn các dòng rủi ro kinh tế E2 cho `chi_so.md`.
- Trình hồ sơ ở buổi duyệt chéo Gate 2a cùng TV4; chạy thử `lab13.py` trên máy khác máy TV2.

### Đóng góp cụ thể

- Viết 3 hàm A1, ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- Viết `mo_hinh(...)`: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu; cả hệ thống 5.865 đ/yêu cầu = 0,49× [simulated].
- A3: quoc_te 1,88× không đáng chạy, chạy lại không giúp (ok 30% → 11,4% → 2,2%); A4: phạm vi noi_dia + hang_nang cộng cố định 4.599 đ = 0,38× [simulated].
- B1–B4: số ca làm lại nhạy nhất (+51,8%); giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ); xem lại 100% ≈ 0,98–1,03× [simulated].
- `pilot_plan.yaml`: chia theo nhân viên 20 + 20, MDE 6 điểm, n = 859/nhóm, DE 6,96, m ≥ 299; luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ; qua `yaml.safe_load`, không còn `?`.

### Bằng chứng

- Báo cáo cá nhân: [report/team/2A202603540_HoangGiaKhiem.md](report/team/2A202603540_HoangGiaKhiem.md)
- Commit `4ce4ab5`: `src/lab13.py` (CP1 + CP2) và `report/team/bang_chi_phi.md`; commit điền `pilot_plan.yaml`.

## DangThanhHai-2A202603570

### Phần việc phụ trách

- Người kiểm số ca 1, người viết code ca 2 (theo `chiaviec.md`).

### Đóng góp cụ thể

- (TV2 tự điền)

### Bằng chứng

- (TV2 tự điền: commit, file, báo cáo cá nhân)

## (Họ tên TV4)-(MSSV)

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ (theo `chiaviec.md`).

### Đóng góp cụ thể

- (TV4 tự điền)

### Bằng chứng

- (TV4 tự điền: commit, file, báo cáo cá nhân)