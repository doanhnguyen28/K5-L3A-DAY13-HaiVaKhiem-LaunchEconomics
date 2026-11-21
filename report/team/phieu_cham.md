# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ...
- Nhóm được chấm: Stech (L3A) · repo `K5-L3A-DAY13-Stech-LaunchEconomics`, commit `4da8720`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | "Go có điều kiện" khớp với số của nhóm. Chi phí mỗi việc thành công là 4.472 đ, gấp 16,3× hoá đơn token; trong phạm vi pilot, có cộng chi phí cố định, là 4.599 đ = 0,38× [simulated]. Đề xuất nêu rõ ba con số bất lợi và cách xử lý từng số. (1) Xem lại 100% đẩy chi phí lên 11.743–12.415 đ (0,98–1,03×) → giữ thời gian mỗi lần xem lại dưới mức hoà vốn 4,8–5,1 phút. (2) Power chỉ còn ~0,64 nếu tác động thật là 5 điểm → Giám đốc vận hành ghi nhận đánh đổi trước ngày quyết định. (3) Chi phí cố định tăng lên 2.370 đ/việc khi khối lượng giảm một nửa → không mở rộng rollout. Mỗi điều kiện có người phụ trách. Lưu ý: hồ sơ đặt giới hạn 2 lần chạy ngay từ đầu, còn `pilot_plan.yaml` chỉ dùng giới hạn này khi chi phí vượt 8.000 đ; hai file cần thống nhất. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 8 | Phạm vi được thu hẹp về noi_dia và hang_nang, có lý do bằng số: 0,22× và 0,69× so với 12.000 đ; loại quoc_te (1,88×, thành công 27,3%, chạy lại không giúp: lần 1 đúng 30% → lần 2 11,4% → lần 3 2,2%) và doi_tac (0,85×). Hầu hết số giả lập đều có nhãn [simulated], kể cả ngưỡng dừng 8.000 đ trong YAML. Trừ 2 điểm vì vẫn còn số giả lập chưa gắn nhãn: dòng 6 của hồ sơ ("loại quoc_te 1,88×, doi_tac 0,85×") và trường `scope` trong `pilot_plan.yaml` (phần "1,88x / 0,85x" nằm ngoài cụm có chữ simulated). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Pilot chia ngẫu nhiên theo nhân viên, 20 + 20, nghĩa là mỗi nhóm có đủ 20 cụm. Có seed ghi trước, phân tầng theo depot, đối chứng chạy cùng lúc. Nhóm tính đủ 5 câu D1 (1.251 · 3.103 → cần 42 người mỗi nhóm · trần 1.000 · trần 300 · m ≥ 299) và chọn mức chênh 6 điểm, n = 859, DE = 6,96, có ghi rõ đánh đổi. Ngưỡng an toàn đặt dựa trên tỉ lệ mở lại hiện tại 3,97%: cao hơn đối chứng 2 điểm hoặc vượt trần 6%. Ba luật dừng đều có ngưỡng, thời hạn (3 ngày / 2 tuần / 1 tuần) và người có quyền dừng (Giám đốc vận hành, PM, Trưởng nhóm CSKH). Góp ý: chưa có ngày bắt đầu nên chưa kiểm được mỗi nhân viên kịp đạt 299 yêu cầu trước 2027-01-05 (cần khoảng 10 ngày làm việc ở bước 0.50); hoàn tiền trùng nên dừng ngay, không đợi "3 ngày liên tiếp". |
| **Tổng** | | | | **28 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Trong phạm vi noi_dia + hang_nang, chi phí kể cả chi phí cố định là 4.599 đ = 0,38× so với nhân viên tự làm, và vẫn chỉ 5.784 đ = 0,48× nếu khối lượng giảm một nửa [simulated]. Thiết kế pilot tách được tác động của trợ lý, và nhóm đã nêu thẳng các con số bất lợi. Hội đồng giữ các điều kiện của nhóm và thêm năm điều kiện:
1. Thống nhất giới hạn số lần chạy (2 hay 3 lần) giữa hồ sơ và `pilot_plan.yaml`. Người phụ trách: PM trợ lý hoàn phí.
2. Ghi ngày bắt đầu pilot và tỉ lệ xem lại ban đầu. Nếu tuần đầu phải xem lại 100% thì chi phí là 11.743 đ, vượt ngưỡng 8.000 đ, nên luật dừng 2 sẽ kích hoạt ngay. Người phụ trách: Giám đốc vận hành LogiX-VN.
3. Thay phút xem lại và phút làm lại simulated bằng số đo thật sau tuần 1. Người phụ trách: PM trợ lý hoàn phí.
4. Dừng ngay khi có ca hoàn tiền trùng đầu tiên. Người phụ trách: Kỹ sư trưởng agent.
5. Bổ sung nhãn [simulated] ở dòng 6 hồ sơ và trường `scope` của YAML.

**Một câu hỏi cho đội trình:** "Nếu 2 tuần đầu pilot phải xem lại 100% các ca, chi phí mỗi việc thành công lên 11.743 đ [simulated], vượt ngưỡng dừng 8.000 đ của nhóm. Lúc đó pilot có tự thu hẹp về noi_dia không, và nhóm sẽ sửa luật dừng hay kế hoạch giảm xem lại thế nào để pilot vẫn ra được quyết định trước 2027-01-05?"
