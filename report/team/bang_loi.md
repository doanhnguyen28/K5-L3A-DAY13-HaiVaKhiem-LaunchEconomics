# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Doanh · Người gắn nhãn 2: không thực hiện

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất (theo bảng tham khảo) |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | — | — | — |
| 2 | Hệ thống | — | — | — |
| 3 | Ngữ cảnh | — | — | — |
| 4 | Giới hạn hệ thống | — | — | — |
| 5 | Ngầm | — | — | — |
| 6 | Do người dùng | — | — | — |
| 7 | Hệ thống | — | — | — |
| 8 | Hệ thống | — | — | — |
| 9 | Do người dùng | — | — | — |
| 10 | Ngữ cảnh | — | — | — |
| 11 | Giới hạn hệ thống | — | — | — |
| 12 | Ngầm | — | — | — |
| 13 | Giới hạn hệ thống | — | — | — |
| 14 | Do người dùng | — | — | — |
| 15 | Hệ thống | — | — | — |
| 16 | Ngữ cảnh | — | — | — |
| 17 | Ngầm | — | — | — |
| 18 | Ngữ cảnh | — | — | — |
| 19 | Giới hạn hệ thống | — | — | — |
| 20 | Hệ thống | — | — | — |

Tổng theo loại: Do người dùng 4 (1, 6, 9, 14) · Hệ thống 5 (2, 7, 8, 15, 20) · Ngữ cảnh 4 (3, 10, 16, 18) · Giới hạn hệ thống 4 (4, 11, 13, 19) · Ngầm 3 (5, 12, 17).

**Tỉ lệ đồng thuận:** không áp dụng (không có hai bộ nhãn độc lập).

## Quy tắc phân biệt cho các ca không trùng

Không có ca không trùng vì không gắn độc lập. Nhóm ghi lại quy tắc cho các ca dễ lẫn (theo tài liệu tham khảo):

- Ca 6, 9 là do người dùng, không phải hệ thống: gốc lỗi là khách chọn sai mục hoặc nhập sai mã; việc trợ lý không gợi ý thuộc cột khắc phục.
- Ca 13 là giới hạn hệ thống: ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.
- Ca 8, 15 là hệ thống, không phải ngầm: sai đã lộ ra (trích dẫn nhìn thấy được, nhân viên bắt được). Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- Ca 18 là ngữ cảnh: số tiền đúng chính sách, chỉ giả định "khách hiểu cách tính" là không khớp.
- Ca 12 là ngầm: kết quả đúng nhưng chi phí token gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" có thể là sai về chi phí.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". Tên event khớp với danh sách event trong `chi_so.md`.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 6 | Do người dùng | Tỉ lệ `ticket_reopened` có reason khác với loại yêu cầu ban đầu (vd. chọn "giao trễ" nhưng mở lại vì "hàng vỡ"), theo dõi hằng ngày; cảnh báo khi > 1% số yêu cầu/ngày | Trợ lý đối chiếu mục khách chọn với nội dung mô tả; nếu lệch (từ khoá "vỡ", "hỏng" trong luồng giao trễ) thì hỏi lại khách chọn đúng mục trước khi xử lý | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: đếm `refund_ledger_write` có ket_qua = ok trùng request_id; ngưỡng 0 ca, có ca là cảnh báo ngay | Bắt buộc `idempotency_key` theo request_id cho mọi lệnh hoàn; sổ cái từ chối lệnh thứ hai cùng khoá; khách gửi lại thì trả trạng thái của lệnh đang chạy | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Số phản ánh "làm phiền" hoặc `ticket_reopened` có reason = thoi_gian_thong_bao theo tuần; tỉ lệ tin nhắn gửi trong 22:00–7:00 trên tổng tin nhắn, ngưỡng > 5% | Đổi thiết kế: tin hoàn tiền trong 22:00–7:00 được hoàn tất trong hệ thống nhưng hẹn gửi Zalo lúc 7:00; khách có thể chọn nhận ngay | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Event `handoff_to_staff` có reason = dau_vao_khong_doc_duoc, theo dõi tỉ lệ theo tuần và theo kênh; cảnh báo khi > 3% số yêu cầu | Khi nhận tin thoại, nói rõ trợ lý chưa đọc được âm thanh, đưa sẵn mẫu 3 trường (mã vận đơn, lý do, số tiền) để khách nhập nhanh, hoặc chuyển nhân viên kèm file âm thanh | PM trợ lý hoàn phí |
| 12 | Ngầm | Báo cáo hằng ngày chi phí token + tool mỗi yêu cầu theo depot từ `agent_run_completed`; cảnh báo khi một depot > 1,5 lần trung vị các depot trong 2 ngày liên tiếp | Kiểm tra schema đầu ra của tool tra đơn (thiếu trường thì báo lỗi ngay thay vì để agent gọi lại); sửa tool của D05; giới hạn 2 lần chạy | Kỹ sư trưởng agent |
