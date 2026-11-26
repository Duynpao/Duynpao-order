---
name: san-luong-ton-kho-duynpao
description: Dùng khi Duyên gửi ảnh bảng viết tay ở xưởng (số bánh làm trong ngày, TỒN, bánh hỏng) hoặc hỏi báo cáo xưởng, lệch tồn, tồn kho thành phẩm Duynpao.
---

# Sản lượng & tồn kho xưởng Duynpao

## File
**Nguyên liệu & Sản lượng Duynpao** `13YCASlhmd2kN_TYKaRsnTpDTlaQE2yIR7xTK4kNGos0`. Các tab: Sản lượng ngày, Tồn kho ngày, Xuất hàng ngày, Đối chiếu tồn, Sản lượng tháng (và Nhập nguyên liệu, xem skill khác).

**Dòng theo ngày: dòng = 5 + (ngày − 01/10/2026)**. Ví dụ 01/10 = dòng 5, 16/11 = dòng 51, 24/11 = dòng 59. Luôn đọc cột A của dòng đó để kiểm tra ngày trước khi ghi (đã từng ghi nhầm 15 sang 16).

### Tab "Sản lượng ngày" (ghi C:U)
C Thịt 1 trứng · D Thịt 2 trứng · E Xúc xích phomai · F Bò ngô phomai · G Gà nấm phomai · H Xá xíu phomai · I Cốm dừa · J Đậu dừa · K Kimsa trứng muối · L Thịt hành mini · M Chay sữa · N Chay sữa túi 500gr · O Gạo lứt · P Nguyên cám · Q Cốm mini · R Mini mix vị phomai · S TỔNG (công thức, không ghi) · T Bánh hỏng/huỷ · U Ghi chú.

### Tab "Tồn kho ngày" (ghi D:Z, bỏ qua C, M, S vì là công thức)
Cùng các cột sản phẩm như trên. C = V+W+X, M = Y+Z. T = Chay cân (kg), U = Ghi chú, V = T (thịt 1 trứng mẻ mới), W = T5, X = T6 (các mẻ cũ), Y = Chay trắng, Z = Chay xanh.

### Viết tắt trên bảng xưởng
T/T5/T6 = Thịt 1 trứng theo mẻ · Cám = Nguyên cám · Lứt = Gạo lứt · Xíu = Xá xíu · XX = Xúc xích · Bò · Gà · Kimsa · Chay cân tính bằng kg (5 kg = 10 túi 500gr).

### Tab khác
- "Xuất hàng ngày": C5 lấy IMPORTRANGE từ tab ẩn `_Xuất ngày` của file Đơn sỉ (`1zwbhIyKhNFw5Le41XbUJ_IFdeZWBq-yPTNOSN8tsZl4`). **Không nhập tay.** Xuất được cộng theo NGÀY NHẬN; đơn Huỷ không tính, đơn "Chờ xác nhận" vẫn tính; cộng thêm tab "Xuất khác".
- "Đối chiếu tồn": mỗi ngày một khối 13 dòng, bắt đầu dòng 6. Cột A Ngày, B Loại, C Tồn đầu, D Làm, E Xuất, F Tồn cuối HT, G NV báo, H Lệch (tô đỏ). C3 = ngày tồn đầu kỳ (15/11/2026). Tồn đầu = tồn NV báo hôm trước, nếu trống thì lấy tồn HT hôm trước.

## Quy tắc của chị
- **Bỏ qua số tổng thợ ghi trên bảng.** Chỉ cộng từng loại.
- Ghi chú dạng "Theo ảnh bảng dd/mm", nêu rõ số mờ hoặc ô trống. Số viết sát nhau, không chắc (ví dụ 390 hay 39) thì hỏi lại.
- Bánh hỏng đã bán hoặc bỏ phải ghi thêm vào tab "Xuất khác" của file Đơn sỉ.

## Quy trình
1. Đọc ảnh, lập bảng số theo từng loại và trình bày lại cho chị nếu có số không chắc.
2. Kiểm tra cột A, rồi `update_values` `'Sản lượng ngày'!C{r}:U{r}` và `'Tồn kho ngày'!D{r}:Z{r}`.
3. `get_values` khối Đối chiếu tồn của ngày đó.
4. Soạn tin Zalo dán được ngay:
```
BÁO CÁO XƯỞNG dd/mm (Tx)
SẢN LƯỢNG LÀM: tổng N bánh
- Loại: số (xếp giảm dần)
TỒN NHÂN VIÊN BÁO: …
LỆCH TỒN (NV – hệ thống): Loại +/−n … ; Khớp: …
CẦN KIỂM TRA: …
```

## Cách làm tốt hơn
- Gắn cờ: một loại lệch ±30% so với trung bình 7 ngày; |lệch tồn| > 20 bánh hoặc > 10%; lệch âm 3 ngày liền (từng gặp với xúc xích, kimsa); bánh hỏng > 2% sản lượng. Những ngày đó nêu nguyên nhân hay gặp: đơn chưa lên sheet, bánh biếu hoặc ăn thử chưa ghi Xuất khác, đếm nhầm mẻ.
- Thiếu ảnh ngày nào thì báo ngay, vì Đối chiếu tồn sẽ lệch dây chuyền.
- Mỗi tuần gửi chị tóm tắt: tổng sản lượng, top lệch, loại sắp hết (tồn < nhu cầu 2 ngày) để lên kế hoạch làm.
