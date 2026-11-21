# Chia việc Lab 13 — Launch Economics (nhóm 4 người)

Bám theo 4 vai trong [TEAM.md](TEAM.md) và lịch 5 checkpoint trong [CHECKPOINTS.md](CHECKPOINTS.md). Điền tên vào bảng dưới rồi copy cột "Vai" sang `TEAM.md`.

## 1. Vai và người phụ trách

| TV | Họ tên | Vai chính | File sở hữu (chỉ người này sửa) |
| -- | ------ | --------- | ------------------------------- |
| TV1 | | **Người viết code ca 1** (14:00–15:20) → kiểm số ca 2 | `src/lab13.py` (tới giải lao), `report/team/bang_chi_phi.md` |
| TV2 | | **Người kiểm số ca 1** → **người viết code ca 2** (15:35–18:00) | `src/lab13.py` (sau giải lao), `report/team/pilot_plan.yaml` |
| TV3 | | **Người gắn nhãn 1** — đọc đề, canh điều kiện "Xong khi", canh giờ | `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/phieu_cham.md` |
| TV4 | Đoàn Văn Tú — 2A202603595 | **Người gắn nhãn 2, kiêm giữ hồ sơ** — điền hồ sơ từ đầu buổi | `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md` |

Đổi người viết code sau giải lao là yêu cầu của đề: TV1 và TV2 đều phải tự tay tính được chi phí mỗi việc thành công.

## 2. Việc từng người theo checkpoint

### 14:00 – Chuẩn bị (10 phút)
- **TV1:** fork/đổi tên repo `K5-L3A-DAY13-TenNhom-LaunchEconomics`, mời 3 bạn, cài venv trong `src/`, chạy `python lab13.py`.
- **TV2, TV3:** clone repo nhóm, cài venv trên máy mình (để cuối buổi chạy thử trên máy khác).
- **TV4:** điền phần "Thông tin nhóm" + bảng thành viên trong `TEAM.md`; mở sẵn `ho_so_launch_v0.md`.

### CP1 · A — Chi phí mỗi việc thành công (14:10–14:53)
| TV | Việc |
| -- | ---- |
| TV1 | Viết 3 hàm A1 → phải in ĐẠT (1,20 · 1,25 · 1,25) mới đi tiếp. Viết `mo_hinh(...)` (A2), gọi theo từng `loai` (A3), cộng cố định 40 triệu/tháng cho `noi_dia + hang_nang` (A4). Đọc CSV có `keep_default_na=False`. |
| TV2 | Tính tay 1–2 con số để đối chiếu (vd. tiền token = tokens/1000 × giá; số việc thành công = 978). Điền bảng A2 (9 dòng, 2 dòng xem lại/làm lại ghi `simulated`), A3 (4 dòng), A4 vào `bang_chi_phi.md`. Tính tỉ lệ ok theo lần thử của `quoc_te`. |
| TV3 | Đọc [docs/du_lieu_va_cong_thuc.md](docs/du_lieu_va_cong_thuc.md) và đề `.docx`; viết sẵn 2 câu trả lời A (≤ 3 dòng, có số): vì sao tử số tính mọi lần chạy / mẫu số chỉ đếm thành công; loại nào không đáng chạy và vì sao chạy lại không giúp. |
| TV4 | Điền mục 1 và 3 của hồ sơ (chi phí mỗi việc thành công, so với 12.000 đ — **dùng con số cả hệ thống 0,49×**, không viết 0,37×), trạng thái "Giả lập". |

### CP2 · B — Bảng độ nhạy (14:53–15:20)
| TV | Việc |
| -- | ---- |
| TV1 | Code `TODO CP2`: 9 kịch bản B1, 1 cặp B2, giới hạn 1/2/3 lần chạy + chi phí cả hệ thống B3, xem lại 100% B4. |
| TV2 | Kiểm tra quy tắc "giảm một nửa = nửa mức tăng gấp đôi" và "cặp = tổng hai tác động". Điền B1–B4 vào `bang_chi_phi.md`, ghi xếp hạng 3 yếu tố. B4 ghi cả hai con số (9 phút và 15,3 phút làm lại) + mức hoà vốn phút xem lại. |
| TV3 | Viết câu trả lời B3, B4 (≤ 3 dòng, có số). Chuẩn bị bảng định nghĩa 5 loại lỗi PAIR (chưa xem đáp án). |
| TV4 | Điền mục 2 hồ sơ (ba yếu tố nhạy nhất), bắt đầu nháp mục 7 (rủi ro kinh tế) từ số B1/B4. |

*Giải lao 15:20–15:35. TV1 commit + push `lab13.py` trước giải lao, bàn giao cho TV2.*

### CP3 · C — Bảng lỗi (15:35–16:08)
| TV | Việc |
| -- | ---- |
| TV3 + TV4 | **Ngồi tách nhau, gắn nhãn độc lập 20 ca trong 8 phút, không trao đổi, không xem đáp án.** Ghi bộ nhãn của mình vào giấy/file riêng trước. Sau đó so nhãn, tính đồng thuận (cần ≥ 16/20), ghi quy tắc phân biệt cho ca lệch. **Không sửa bộ nhãn độc lập sau khi so.** |
| TV3 | Chép hai bộ nhãn + tỉ lệ đồng thuận + quy tắc vào `bang_loi.md`. Điền bảng khắc phục 5 ca (mỗi loại 1 ca), mỗi dòng có cách phát hiện đo được (event, ngưỡng, tần suất) và **một vai trò** phụ trách. |
| TV2 | Nhận code: chạy lại toàn bộ `lab13.py` trên máy mình, hoàn thiện phần B còn sót; bắt đầu `TODO CP4` (hàm `co_mau`). |
| TV1 | Chuyển sang kiểm số: soát lại `bang_chi_phi.md` so với slide chữa (lệch ≤ 2%), soát nhãn `simulated`. |

### CP4 · D — pilot_plan.yaml (16:08–16:36)
| TV | Việc |
| -- | ---- |
| TV2 | Code `TODO CP4`: 5 câu D1 (a 1.251 · b DE 2,48 / 3.103 · c tối đa 1.000 · d tối đa 300 · e m ≥ 299). Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (4,25%; trong phạm vi 3,97%). Tính power ở mức 5 điểm khi n = 859 (~0,64). |
| TV1 | Kiểm tay câu e và DE; điền mọi dấu `?` trong `pilot_plan.yaml`, ghi D1 + D2 vào phần chú thích đầu file. Ít nhất 3 luật dừng (an toàn, chi phí, mức sử dụng) đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, có người có quyền dừng. |
| TV3 | Viết 5 câu D2 "tách được tác động". Chạy hai lệnh tự kiểm tra: `yaml.safe_load` và `grep` không còn `?`. |
| TV4 | Điền mục 5 (bảng lỗi) và mục 6 (pilot plan) của hồ sơ. |

### CP5 · E — Chỉ số, rủi ro, hồ sơ (16:36–17:00)
| TV | Việc |
| -- | ---- |
| TV2 | Tính 3 chỉ số (chính 82,83% · dùng 27,12% · an toàn 4,25%). |
| TV3 | Viết `chi_so.md`: đặc tả 3 chỉ số + 1 chỉ số dùng + 1 chỉ số an toàn tự đề xuất; ≥ 6 event có `trace_id`; ánh xạ chỉ số → event. |
| TV1 | Viết ≥ 2 dòng rủi ro kinh tế trong `chi_so.md`, lấy số từ bảng độ nhạy, có nhãn `simulated` và người phụ trách. |
| TV4 | Chốt `ho_so_launch_v0.md`: 7 mục, mỗi mục có con số chính, trạng thái (Xong, có bằng chứng · Chưa · Giả lập), người phụ trách là một vai trò. Dòng cuối: **Go / Go có điều kiện / No-go**, nêu cả con số bất lợi (power 0,64, xem lại 100% ≈ 0,98–1,03×) và cách xử lý. **17:00 gửi cho nhóm hội đồng.** |

### 17:00 – Duyệt chéo Gate 2a (45 phút)
- **TV4 + TV1:** trình hồ sơ nhóm mình (1 phút) và trả lời câu hỏi hội đồng (1 phút). Chuẩn bị sẵn 3 câu hay bị hỏi: xem lại 100% thì chi phí bao nhiêu; có ≥ 20 cụm mỗi nhóm không; ngưỡng an toàn có làm pilot dừng ngay tuần đầu không.
- **TV3 + TV2:** làm hội đồng chấm nhóm n + 1 theo thang C6–C8, ghi `phieu_cham.md` (điểm, quyết định, lý do, 1 câu hỏi).

### 17:45 – Đóng gói và nộp
| TV | Việc |
| -- | ---- |
| TV4 | `group_report.md`, hoàn thiện bảng đóng góp trong `TEAM.md`. |
| TV3 | Chạy checklist [SUBMISSION.md](SUBMISSION.md): `grep -rni production report/team` không in gì, nhãn `simulated` đủ, đề xuất đúng 1 trong 3. |
| TV1 | Chạy `cd src && python lab13.py` trên **máy khác máy TV2** → 3 phép thử ĐẠT. |
| TV2 | Gộp commit cuối, push `main`, gửi link repo cho cả nhóm. |
| **Cả 4** | Mỗi người copy `report/team/MSSV_HoTen.md` thành file riêng (vd. `report/team/20241234_NguyenVanAn.md`), ghi phần việc, bằng chứng (commit, file), công cụ AI đã dùng và cách tự kiểm tra. **Mỗi người tự nộp link repo trên LMS trước 23h59.** |

## 3. Quy tắc làm việc chung

- **Mỗi file chỉ một người sửa** (theo bảng mục 1) để tránh conflict. Ai cần thêm nội dung vào file người khác thì nhắn cho chủ file.
- `src/lab13.py` chỉ một người cầm tại một thời điểm; bàn giao bằng commit + push trước khi người kia pull.
- `git pull` trước khi sửa, commit nhỏ, message rõ (vd. `CP1: mo_hinh + bang A2`). Không force-push.
- Không sửa hai file CSV, không commit `.venv/` hay `.env`.
- Mọi con số lấy từ `lab13.py` hoặc tính tay có ghi cách tính; số từ cột `_simulated` luôn có nhãn `simulated`.
- Mỗi câu trả lời ≤ 3 dòng và có ít nhất một con số. Không dùng từ "production".
- Đối chiếu ngay khi slide chữa hiện lên; lệch quá 2% thì sửa trước khi sang checkpoint sau.
