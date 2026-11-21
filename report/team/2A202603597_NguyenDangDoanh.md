# Báo cáo cá nhân — NguyenDangDoanh-2A202603597

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đăng Doanh
- MSSV: 2A202603597
- Email:
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người gắn nhãn 1 (TV3); trong buổi làm nhận thêm phần code và các file hồ sơ còn trống

## 2. Phần việc phụ trách

- Theo phân công ban đầu (`chiaviec.md`): người gắn nhãn 1, chủ các file `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/phieu_cham.md`; viết câu trả lời A2, A3, B3, B4 và năm câu D2; soát checklist nộp bài.
- Nhận thêm trong buổi: `src/lab13.py`, các bảng trong `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- `src/lab13.py`: ba hàm A1, `mo_hinh`, A3, A4, bảng độ nhạy B1–B4, cỡ mẫu D1, ba chỉ số E1; chạy từ đầu đến cuối, ba phép thử in ĐẠT.
- `bang_chi_phi.md`: bảng A1–A4, B1–B3 và các câu trả lời, mọi số giả lập có nhãn `simulated`.
- `chi_so.md`: ba chỉ số tính thử (82,83% · 27,12% · 4,25%), hai chỉ số tự đề xuất, 10 event có `trace_id`, kiểm tra chéo chỉ số – event, ba dòng rủi ro kinh tế.
- `pilot_plan.yaml`: D1, D2, đánh đổi mức chênh 6 điểm, 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- `bang_loi.md`: bảng khắc phục 5 ca (6, 20, 16, 11, 12) có event, ngưỡng, vai trò phụ trách. Nhãn 20 ca lấy theo bảng tham khảo của tài liệu, **không phải bộ nhãn tôi gắn độc lập**; đã ghi rõ trong file.
- `ho_so_launch_v0.md`, `group_report.md`: hồ sơ bảy mục với đề xuất Go có điều kiện, báo cáo nhóm.

## 4. Bằng chứng

- Output `cd src && python lab13.py`: "Ba phép thử đáp án biết trước: ĐẠT"; chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn; D1: 1.251 · 3.103 · 1.000 · 300 · m ≥ 299; power 0,64.
- `yaml.safe_load` đọc được `pilot_plan.yaml`, nhận 4 luật dừng; không còn dấu `?` ngoài chú thích; lệnh grep trong checklist (từ cấm theo quy tắc 5) không in gì.
- Commit: (điền hash commit sau khi push)

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Opus)**, dùng cho phần lớn bài làm: chia việc cho nhóm, viết `src/lab13.py`, tính và điền số vào các file hồ sơ, viết bảng khắc phục, hồ sơ launch và báo cáo nhóm. Nhãn 20 ca ở nhiệm vụ C không do AI gắn mà lấy từ bảng tham khảo của tài liệu.
- **Cách tự kiểm tra:** chạy `lab13.py` và so từng con số với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%); đối chiếu A2 bằng một script đọc CSV thuần Python độc lập, kết quả trùng; kiểm tra quy tắc "giảm một nửa = nửa mức tăng gấp đôi" ở B1 và "cặp = tổng hai tác động" ở B2; chạy `yaml.safe_load` và các lệnh `grep` trong checklist nộp bài.

## 6. Tự đánh giá

- Hiểu và giải thích được: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công; vì sao chạy lại không giúp quoc_te; vì sao số cụm, không phải tổng số yêu cầu, giới hạn cỡ mẫu hiệu dụng (tối đa c / ICC).
- Hạn chế: phần lớn code và văn bản do AI viết, tôi chủ yếu điều phối và kiểm tra số; không thực hiện bước gắn nhãn độc lập ở nhiệm vụ C nên nhóm mất điểm đồng thuận. Lần sau cần tự gắn nhãn trước và tự viết ít nhất một hàm tính chi phí.
