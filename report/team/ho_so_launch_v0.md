# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Gate 2a duyệt kế hoạch pilot. Chi phí dùng phút xem lại/làm lại giả lập được ghi `simulated`; các điều kiện dưới đây là việc cần làm, chưa phải bằng chứng đã triển khai.

Nhóm: HaiVaKhiem · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); trong phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 40 triệu/tháng thành 4.599 đ ở 45.000 yc/tháng, 5.784 đ nếu khối lượng còn một nửa [simulated]. Nguồn: `bang_chi_phi.md` A2, A4 | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại ×2: +51,8% (6.787 đ), ÷2: −25,9% · 2. Xem lại ×2: +40,7% (6.292 đ), ÷2: −20,3% · 3. Lương +23,1% khi tăng 25%; giá token chỉ +5,6% khi gấp đôi [simulated]. Nguồn: B1, B2 | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Trên toàn bộ 1.200 yêu cầu: cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ, gồm 222 ca nhân viên làm thay, chưa cộng cố định. Theo loại (chi phí mỗi việc trợ lý làm thành công): noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88×. **Bất lợi:** xem lại 100% tốn 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated]. Nguồn: A2, A3, B4 | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số chính trong đợt chạy thử là 82,83% (994/1.200), chưa so được với baseline 0,70 vì không có đối chứng · Bỏ qua gợi ý 27,12% (48/177) · Mở lại 7 ngày 4,25% (51/1.200), trong phạm vi 3,97%. 10 event có `trace_id`. Nguồn: `chi_so.md` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca theo 5 loại PAIR (4 · 5 · 4 · 4 · 3); nhãn theo bảng tham khảo, **chưa gắn độc lập** (đã ghi rõ trong file). Đã có 5 cách khắc phục và bảng AI rà soát 20 ca có lý do; vẫn thiếu hai bộ nhãn độc lập và tỉ lệ đồng thuận. Hai lỗi cần kiểm soát trước pilot: hoàn trùng (ca 20) và báo "đã hoàn" khi sổ cái lỗi (ca 7). Nguồn: `bang_loi.md` | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Dự kiến chia ngẫu nhiên 20 + 20 nhân viên, phân tầng theo depot; MDE 6 điểm, 859 mẫu hiệu dụng/nhóm, DE 6,96; cần ≥ 299 yc/người = 5.980 yc thực tế/nhóm. **Bất lợi:** không đủ mẫu cho 5 điểm (tối đa 1.000 < 1.251), power 0,64 nếu tác động thật là 5 điểm. YAML có 4 luật dừng; cần TV2 chốt seed và tách luật hoàn trùng để dừng ngay. Dự kiến quyết định 2027-01-05, sau khi đủ mẫu và theo dõi 7 ngày. Nguồn: `pilot_plan.yaml` | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%); xem lại 100% kéo dài → 0,98–1,03×, hoà vốn khi xem lại ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút); khối lượng còn một nửa → cố định +2.370 đ/việc [simulated]. Mỗi rủi ro có dấu hiệu, ngưỡng, hành động. Nguồn: `chi_so.md` E2 | Giả lập | PM trợ lý hoàn phí |

**Bốn điều kiện trước ngày bắt đầu dự kiến 2026-12-01** (mọi mốc theo GMT+7; chưa đạt thì lùi ngày bắt đầu):

- **An toàn:** sửa khoá chống trùng và chỉ báo “đã hoàn” khi sổ cái trả ok (ca 7, 20); đối soát 0 ca hoàn trùng/báo hoàn sai trạng thái trong 3 ngày thử. TV2 cập nhật luật hoàn trùng thành dừng ngay khi phát hiện ≥ 1 ca. Phụ trách: Kỹ sư trưởng agent; kiểm tra 2026-11-27.
- **Thiết kế pilot:** ghi seed, cách phân tầng và số mẫu thực tế trong kế hoạch; ký chấp nhận MDE 6 điểm, power khoảng 0,64 nếu tác động thật là 5 điểm. Phụ trách: Giám đốc vận hành LogiX-VN; kiểm tra 2026-11-28.
- **Đo lường:** đặc tả đủ 10 event có `trace_id`, thời điểm tạo yêu cầu, nối được các lần chạy; mẫu số việc thành công phải loại ca mở lại/sai tiền. Bật và thử luồng ghi event trước pilot. Phụ trách: PM trợ lý hoàn phí; kiểm tra 2026-11-28.
- **Xem lại:** có kế hoạch 100% → 50% → 20%; chỉ giảm khi sửa + bỏ < 15% trong 1 tuần và chỉ số an toàn không vượt ngưỡng. Đo phút thật, đối chiếu cả hai mốc hoà vốn 5,1/4,8 phút [simulated]. Phụ trách: Trưởng nhóm CSKH; kiểm tra 2026-11-28.

**Sau tuần 1:** PM tính lại chi phí bằng phút đo thật vào 2026-12-08 nếu bắt đầu đúng lịch; đây là mốc theo dõi sau khởi động. Nếu chưa đủ 5.980 yêu cầu/nhóm hoặc chưa theo dõi đủ 7 ngày, Giám đốc vận hành lùi quyết định hiệu quả, vẫn giám sát an toàn.

**Đề xuất: Go có điều kiện** cho pilot chỉ **noi_dia + hang_nang**; loại quoc_te (1,88×, thành công 27,3%) và doi_tac (0,85×, điều khoản riêng) [simulated đối với chi phí]. Cơ sở là chi phí toàn hệ thống 0,49× [simulated, chưa cố định]; rủi ro là xem lại 100% tốn 0,98–1,03× [simulated] và power chỉ 0,64 cho mức 5 điểm. Chỉ bắt đầu khi đủ bốn điều kiện trên; nhiệm vụ gắn nhãn độc lập vẫn chưa hoàn tất.
