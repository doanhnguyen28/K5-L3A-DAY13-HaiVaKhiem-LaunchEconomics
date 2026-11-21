# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Ba dòng đầu tính trên `src/logix_requests.csv` (1.200 yêu cầu, đọc với `keep_default_na=False`). Ba chỉ số này dùng các cột đo được (`dong_trong_24h`, `mo_lai_trong_7_ngay`, `duoc_xem_lai`, `quyet_dinh_xem_lai`), không dùng cột `_simulated`.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200); trong phạm vi noi_dia + hang_nang: 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177; sua 41, bo 7, giu 129) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi noi_dia + hang_nang: 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm dùng trợ lý được nhân viên mở gợi ý của trợ lý | Số `refund_request_created` (arm = tro_ly) có ít nhất một `agent_suggestion_shown` cùng `trace_id`, chia số `refund_request_created` (arm = tro_ly), theo tuần và theo `staff_id` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm, không chờ khách mở lại) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra trong tuần (100 đơn/tuần, chọn ngẫu nhiên) | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Con số này không so được với baseline 0,70 để kết luận về tác động, vì đợt chạy thử không có nhóm đối chứng và gồm cả quoc_te, doi_tac.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent (`logix_runs.csv`). `arm` là nhóm của pilot (`tro_ly` hoặc `doi_chung`).

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, depot, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (ok/loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | request_id, staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | request_id, staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | request_id, reason (thieu_du_lieu / ngoai_pham_vi / vuot_so_lan_chay / dau_vao_khong_doc_duoc), tom_tat, trace_id | Khi agent chuyển cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | request_id, idempotency_key, so_tien, ket_qua (ok/loi), ma_loi, trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `ticket_closed` | Hệ thống ticket | request_id, closed_at, kenh_xu_ly (tro_ly/nhan_vien), trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, 100 đơn chọn ngẫu nhiên |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính.

- Chính: `refund_request_created` (mẫu số, created_at) + `ticket_closed` (closed_at − created_at ≤ 24 giờ) + `ticket_reopened` (không có trong 7 ngày sau closed_at).
- Dùng, bỏ qua gợi ý: `staff_review_decision` (quyet_dinh là sua hoặc bo, chia tổng số event này).
- An toàn, lỗi lọt đến khách: `ticket_reopened` trong 7 ngày, chia `refund_request_created`.
- Dùng, tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` có arm = tro_ly, nối bằng `trace_id`.
- An toàn, tự đề xuất: `audit_sample_checked` (so_tien_da_hoan khác so_tien_dung).
- Chi phí mỗi việc thành công (dùng cho luật dừng chi phí): `agent_run_completed` (token, tool, mọi lần chạy) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai`, chia số `ticket_closed` có kenh_xu_ly = tro_ly. Phút xem lại và làm lại đo thật từ hai event này sẽ thay cho hai cột `_simulated`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công +51,8%, từ 4.472 đ lên 6.787 đ [simulated] (B1, yếu tố nhạy nhất) | Tỉ lệ `staff_rework_completed` / yêu cầu theo tuần > 7% (đợt chạy thử: 4,9%, 48/982 trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất để tìm nguyên nhân gốc trước khi sang bước rollout tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ với 9 phút làm lại; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4); hoà vốn khi mỗi lần xem lại ≤ 5,1 phút | % yêu cầu có `staff_review_decision` còn > 50% ở cuối bước rollout 0.25; `phut_xem_lai` đo thật trung bình > 5 phút | Giảm xem lại theo bậc (100% → 50% → 20%) khi tỉ lệ sửa + bỏ < 15% trong 1 tuần | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (tổng 4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (tổng 5.784 đ = 0,48×) [simulated] (A4) | Số `ticket_closed` có kenh_xu_ly = tro_ly theo tuần < 50% kế hoạch (kế hoạch: 33.750 việc thành công/tháng ở quy mô đầy đủ) | Không mở rộng pilot; xem lại hợp đồng chi phí cố định trước ngày quyết định | PM trợ lý hoàn phí |
