---
name: nhap-nguyen-lieu-chi-phi-duynpao
description: Dùng khi Duyên báo mua nguyên liệu/bao bì ("Phô mai 50 kg", "Mỡ 205k", log Zalo nhân viên, sổ mẹ mua hộ) hoặc chi phí điện/nước/gas, để ghi sổ Nhập nguyên liệu và Chi phí tháng Duynpao.
---

# Nhập nguyên liệu & chi phí Duynpao

## File
- **Nguyên liệu & Sản lượng Duynpao** `13YCASlhmd2kN_TYKaRsnTpDTlaQE2yIR7xTK4kNGos0`, tab "Nhập nguyên liệu".
- **Đơn sỉ Duynpao** `1zwbhIyKhNFw5Le41XbUJ_IFdeZWBq-yPTNOSN8tsZl4`, tab "Nguyên liệu" (cột E = giá cố định dùng tính giá vốn, chốt 16/11/2026) và tab "Chi phí tháng".

## Tab "Nhập nguyên liệu"
- Dữ liệu bắt đầu từ dòng 5; tìm dòng trống cuối cùng trước khi ghi.
- Ô nhập tay (vàng): A Ngày (số serial, ví dụ 46350 = 24/11/2026), B Tên (phải trùng danh mục L), C Số lượng, D Thành tiền, E Nơi mua/ghi chú.
- Ô tự tính (xám), không ghi: F Đơn vị, G Nhóm, H Đơn giá, I Tháng, J Giá/kg.
- Danh mục L:O: L Tên, M Đơn vị, N Nhóm (Nguyên liệu / Bao bì / Khác), O Quy đổi. Món mới thì thêm vào dòng trống tiếp theo của L, đồng thời thêm vào tab "Nguyên liệu" bên file Đơn sỉ.
- Tổng tháng P:T: P Tháng, Q Nguyên liệu, R Bao bì, S Khác, T Tổng (dòng 6 = 2026-11).

## Đọc tin của chị
- Số tiền: "205 k" = 205.000; "6.210.000"; "2,5tr" = 2.500.000; "Hành tây 20 kg 200" = 20 kg, 200.000đ.
- Quy đổi: 1 tạ = 100 kg; 1 hộp thịt nướng = 10 gói; hộp H53 = hộp 4 bánh (600 cái = 570k); cốt dừa lon: 1 thùng = 24 lon.
- Log Zalo "[dd/mm hh:mm] Tên: …": Phạm Hồng Tuoi = Tươi, Vjtmập = anh Việt.
- Sổ "mẹ mua hộ" ghi ngày âm lịch → đổi sang dương. Chỉ lấy từ tháng 10 dương lịch trở đi.
- Không có ngày → ghi ngày hôm nay. Thiếu số cân → để trống C, ghi "Chưa có số cân".
- Tin gõ dở rồi gõ lại (ví dụ "Tạ đường 6 triệu 210.000" rồi "Tạ đường 6.210.000") → chỉ ghi một dòng.

## Quy trình
1. Đọc khoảng 30 dòng cuối: tìm dòng trống, và **kiểm tra trùng** (cùng tên + cùng tiền trong ±30 ngày). Nếu nghi trùng, hỏi một lần duy nhất, rõ ràng: "Đây là lần mua mới hay thanh toán cho lần dd/mm?"
2. `update_values` A:E, rồi đọc lại A:J.
3. So đơn giá H với giá cố định (tab Nguyên liệu file Đơn sỉ). Lệch > 10% → báo chị, **không tự sửa giá cố định**.
4. Đọc P6:T6 (tháng hiện tại) và báo: bảng Ngày | Tên | SL | Tiền | Đơn giá, tổng chi tháng, các điểm cần xác nhận.

## Chi phí tháng (điện, nước, gas, khác)
- Tab "Chi phí tháng" file Đơn sỉ: A Tháng (dòng 2 = 2026-10, dòng 3 = 2026-11), B Lương thợ (IMPORTRANGE H2 tab "Lương YYYY-MM"), C Điện-nước-gas, D Bao bì (tự kéo), E Chi phí khác, F Tổng, G Ghi chú.
- Ghi C bằng `update_formulas` dạng `=415779+7178236` để còn thấy từng khoản. Ghi chú vào G, ví dụ "Tiền nước … + tiền điện … (TT 22/11/2026)".
- Ghi vào tháng thanh toán. Nếu hóa đơn thuộc tháng trước thì hỏi chị.
- "Thanh toán tiền nước …" nghĩa là ghi sổ, Claude không chuyển tiền.
- Việc còn treo: tiền gas mẹ trả (chờ chị gửi số tiền và ngày), ghi vào C với chú thích "Mẹ trả".

## Cách làm tốt hơn
- Đầu mỗi tháng, so giá hóa đơn trung bình tháng trước với giá cố định; liệt kê các món lệch > 10% để chị chốt giá mới (ví dụ gói ướp thịt nướng 13.500đ so với 7.750đ).
- Đề xuất thêm cột "Người trả" (Chị/Mẹ/Việt/Tươi) để đối soát tiền ứng. Hỏi chị trước khi thêm cột.
- Cột E "Chi phí khác" của Chi phí tháng chưa kéo nhóm "Khác" từ sổ nhập; hỏi chị có muốn nối không.
- Mẫu tin gợi ý cho chị: `dd/mm Tên SL đơn-vị Tiền [nơi mua]`.
