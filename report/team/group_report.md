# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: HaiVaKhiem
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có chạy pilot hay không, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định. Cách tiếp cận: viết một mô hình chi phí duy nhất (`mo_hinh` trong `src/lab13.py`) rồi gọi lại cho mọi kịch bản, để mọi con số trong hồ sơ cùng một nguồn; tách số đo từ trace và số giả lập (cột `_simulated`, ghi nhãn `simulated`).

## 3. Giải pháp

- **A · Chi phí mỗi việc thành công** ([bang_chi_phi.md](bang_chi_phi.md)): tử số cộng token, tool của mọi lần chạy (kể cả lần lỗi) và tiền xem lại, làm lại; mẫu số chỉ đếm việc thành công. Tách theo 4 loại yêu cầu, cộng chi phí cố định cho phạm vi pilot.
- **B · Bảng độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): 9 kịch bản đổi từng yếu tố, 1 cặp, giới hạn 1/2/3 lần chạy tính cả phần nhân viên làm thay, kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): 20 ca theo 5 loại Google PAIR, 5 cách khắc phục có event, ngưỡng, vai trò phụ trách.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu cho ba cách chia trước khi chọn; chọn chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm; 4 luật dừng.
- **E · Chỉ số và hồ sơ** (`chi_so.md`, `ho_so_launch_v0.md`): 3 chỉ số tính thử + 2 chỉ số tự đề xuất, 10 event có `trace_id`, 3 dòng rủi ro kinh tế, hồ sơ một trang bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu; giờ nhân viên chiếm 92,5% chi phí [simulated].
- Trên toàn bộ mẫu, cả hệ thống **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated], đã cộng 222 ca nhân viên làm thay, chưa cộng cố định. quoc_te 1,88× và chạy lại không giúp (ok lần 1/2/3: 30% · 11,4% · 2,2%), nên phạm vi pilot chỉ noi_dia + hang_nang.
- Yếu tố nhạy nhất: số ca làm lại (+51,8% khi gấp đôi), không phải giá token (+5,6%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ cả hệ thống) [simulated].
- Con số bất lợi: xem lại 100% tốn 0,98–1,03× [simulated]; pilot 20 + 20 nhân viên chỉ đủ mẫu cho mức chênh 6 điểm (power 0,64 ở mức 5 điểm).
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- **Đề xuất cuối:** Go có điều kiện cho pilot noi_dia + hang_nang, 4 điều kiện trước ngày bắt đầu dự kiến 2026-12-01; mốc thay phút giả lập bằng phút đo thật là 2026-12-08, sau tuần 1 (xem [hồ sơ launch](ho_so_launch_v0.md)).
- **Chưa có kết quả duyệt chéo:** bổ sung tên nhóm hội đồng, điểm C6–C8, quyết định và phản hồi thực tế khi nhận được.

## 5. Khó khăn và cách xử lý

- Máy ban đầu chưa có pandas: tạo `src/.venv` và cài theo `src/requirements.txt`; trong lúc chờ, đối chiếu số A2 bằng script đọc CSV thuần Python, kết quả trùng với `lab13.py`.
- Terminal Windows báo lỗi font khi in tiếng Việt: chạy với `PYTHONIOENCODING=utf-8`; lệnh kiểm tra yaml cần `open(..., encoding='utf-8')` trên Windows.
- Nhiệm vụ C: nhóm không thực hiện bước hai người gắn nhãn độc lập. Nhãn trong `bang_loi.md` lấy theo bảng tham khảo của tài liệu và đã ghi rõ trong file; nhóm chấp nhận không nhận điểm phần đồng thuận.
- Ngưỡng an toàn: tỉ lệ mở lại hiện tại 4,25% (3,97% trong phạm vi), nên không dùng ngưỡng tuyệt đối 3% (pilot sẽ dừng ngay tuần đầu) mà so với nhóm đối chứng (+2 điểm) kèm trần 6%.

## 6. Tổng hợp đóng góp

TV1 Hoàng Gia Khiêm phụ trách mô hình chi phí và độ nhạy; TV2 Đặng Thanh Hải phụ trách phần tính toán ca 2; TV3 Nguyễn Đăng Doanh soạn chỉ số, bảng khắc phục và bản nháp hồ sơ/báo cáo. TV4 Đoàn Văn Tú rà soát và hoàn thiện hồ sơ, sửa độ nhạy, phân biệt mẫu hiệu dụng/thực tế, tách mốc trước/sau pilot và cập nhật thông tin cá nhân. Chi tiết: [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

- Tiền xem lại và làm lại (92,5% chi phí) dựa trên cột giả lập; phải thay bằng phút đo thật từ event `staff_review_decision` và `staff_rework_completed` sau tuần 1 pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chưa kết luận được tác động lên chỉ số chính; pilot chỉ đủ mẫu cho mức chênh 6 điểm.
- Mô hình chi phí cộng tuyến tính, chưa tính tương tác (ví dụ xem lại kỹ hơn làm giảm làm lại).
- Bảng lỗi có thêm rà soát 20 ca bằng Codex cho TV4, mỗi ca có nhãn và lý do. Chưa có hai bộ nhãn độc lập; đáp án đã được tham khảo nên bảng bổ sung không dùng tính đồng thuận giữa hai người.
- Trước khi chốt pilot, TV2 cần ghi seed và **5.980 yêu cầu thực tế/nhóm** (20 × 299; khoảng 859 mẫu hiệu dụng), tách luật hoàn trùng để dừng ngay, xác định thời gian đủ mẫu và theo dõi 7 ngày.
- TV3 cần làm rõ `created_at` và cách nối nhiều lần chạy; mẫu số chi phí mỗi việc thành công phải loại ca mở lại/sai tiền, không chỉ đếm ticket đã đóng. Hồ sơ ghi các điểm này thành điều kiện trước pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `NormalIndPower` (`statsmodels.stats.power`).
- Tài liệu lab: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
