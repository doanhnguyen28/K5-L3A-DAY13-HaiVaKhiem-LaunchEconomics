# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: HaiVaKhiem · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); trong phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 40 triệu/tháng thành 4.599 đ ở 45.000 yc/tháng, 5.784 đ nếu khối lượng còn một nửa [simulated]. Nguồn: `bang_chi_phi.md` A2, A4 | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ±51,8% (×2 → 6.787 đ) · 2. Tỉ lệ xem lại ±40,7% (×2 → 6.292 đ) · 3. Lương +23,1% khi tăng 25%; giá token chỉ +5,6% khi gấp đôi [simulated]. Nguồn: B1, B2 | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ (đã cộng 222 ca nhân viên làm thay). Theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88×. **Bất lợi:** xem lại 100% tốn 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated]. Nguồn: A2, A3, B4 | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số chính trong đợt chạy thử là 82,83% (994/1.200), chưa so được với baseline 0,70 vì không có đối chứng · Bỏ qua gợi ý 27,12% (48/177) · Mở lại 7 ngày 4,25% (51/1.200), trong phạm vi 3,97%. 10 event có `trace_id`. Nguồn: `chi_so.md` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca theo 5 loại PAIR (4 · 5 · 4 · 4 · 3); nhãn theo bảng tham khảo, **chưa gắn độc lập** (đã ghi rõ trong file). 5 cách khắc phục có event, ngưỡng, vai trò; lỗi nặng nhất: hoàn trùng (ca 20) và báo "đã hoàn" khi sổ cái lỗi (ca 7). Nguồn: `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; mde 6 điểm, 859/nhóm, DE 6,96, m ≥ 299 yc/người. **Bất lợi:** không đủ mẫu cho 5 điểm (tối đa 1.000 < 1.251), power 0,64 nếu tác động thật là 5 điểm. 4 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ; quyết định 2027-01-05. Nguồn: `pilot_plan.yaml` | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%); xem lại 100% kéo dài → 0,98–1,03×, hoà vốn khi xem lại ≤ 5,1 phút; khối lượng còn một nửa → cố định +2.370 đ/việc [simulated]. Mỗi rủi ro có dấu hiệu, ngưỡng, hành động. Nguồn: `chi_so.md` E2 | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho pilot **chỉ noi_dia và hang_nang** (loại quoc_te 1,88×, thành công 27,3%; loại doi_tac 0,85×). Chi phí cả hệ thống 0,49× của 12.000 đ [simulated] cho thấy đáng chạy thử, nhưng lợi thế này mất hết nếu phải xem lại 100% (0,98–1,03×) và pilot chỉ đủ mẫu cho mức chênh 6 điểm. Các điều kiện, pilot chỉ bắt đầu ngày 2026-12-01 (theo `pilot_plan.yaml`) khi cả bốn điều kiện đã đạt:

- Sửa khoá chống trùng (`idempotency_key`) và chỉ báo "đã hoàn" khi sổ cái trả ok (ca 7, 20); đối soát mỗi giờ ra 0 ca trong 3 ngày thử. Phụ trách: Kỹ sư trưởng agent · Kiểm tra: 2026-11-27.
- Giám đốc vận hành ký chấp nhận mde 6 điểm (power 0,64 nếu tác động thật là 5 điểm). Phụ trách: Giám đốc vận hành LogiX-VN · Kiểm tra: 2026-11-28.
- Bật đủ 10 event có `trace_id`; sau tuần 1 thay phút xem lại và làm lại simulated bằng phút đo thật rồi tính lại chi phí mỗi việc thành công. Phụ trách: PM trợ lý hoàn phí · Kiểm tra: 2026-11-28 (bật event) và 2026-12-08 (số đo thật).
- Có kế hoạch giảm xem lại theo bậc 100% → 50% → 20% khi tỉ lệ sửa + bỏ < 15% trong 1 tuần, mục tiêu mỗi lần xem lại ≤ 5 phút (B4). Phụ trách: Trưởng nhóm CSKH · Kiểm tra: 2026-11-28.
