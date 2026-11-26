---
name: don-hang-thanh-toan-duynpao
description: Dùng khi Duyên báo đơn đã giao, huỷ đơn, đổi ngày nhận, khách thanh toán hoặc còn nợ, nhập bù đơn cũ từ ảnh hay log Zalo, hoặc hỏi về đơn hàng, công nợ của Duynpao.
---

# Đơn hàng & thanh toán Duynpao

## File (vào thẳng file này)
**Đơn sỉ Duynpao** `1zwbhIyKhNFw5Le41XbUJ_IFdeZWBq-yPTNOSN8tsZl4`.
⚠️ KHÔNG dùng `1PVzTmJndt1Orvom-msTikVs9vvSx8CRBDNEosaRAr-Y`: đó là file mà `apps-script/Code.gs` trỏ tới, file này trống.

### Tab "Đơn hàng" (sheetId 0). Mỗi loại bánh một dòng.
A Thời gian (serial) · B Tháng "YYYY-MM" (**tính theo ngày nhận**) · C Mã đơn · D Khách · E SĐT (ghi kèm `'` đứng đầu) · F Địa chỉ · G Ngày nhận (ghi dạng chữ "d/m/yyyy") · H Đóng gói ("Đóng túi 6 bánh" / "Đóng hộp 4 bánh" / "Khách lẻ · Giao tận nơi") · I Loại bánh · J SL · K Đơn vị ("bánh" / "túi 500gr") · L Đơn giá · M Thành tiền · N Số bánh · O Ghi chú · P Trạng thái · Q Nguồn khách · R Mã khách · S Nguồn tính thưởng · T Biết Duynpao qua.
- Mã đơn: `DPyyMMdd-xxxxx` là đơn sỉ, `LEyyMMdd-xxxxx` là đơn lẻ. Đơn nhập bù lấy ngày nhập làm mã với 5 số ngẫu nhiên, và phải kiểm tra không trùng mã có sẵn.
- Trạng thái chỉ có 3 giá trị: **"Chờ xác nhận"**, **"Đã giao"**, **"Huỷ"** (viết "Huỷ", không viết "Hủy").

### Tab "Thanh toán". Mỗi đơn một dòng, đơn mới ở trên.
A Mã đơn · B Ngày đặt · C Tháng · D Khách · E SĐT · F Loại (Sỉ/Lẻ) · G Số bánh · H Tổng tiền · I Giao hàng (**sửa tay cho khớp cột P bên Đơn hàng**) · J Đã thanh toán (TRUE/FALSE) · K Đã trả trước · L Còn nợ · M Ngày thanh toán dd/mm/yyyy · N Ghi chú.
- Trả đủ: J=TRUE, L=0, M=ngày, N="Chị Duyên báo dd/mm: …".
- Trả thiếu: J=FALSE, K=số đã trả, L=phần còn nợ, M=ngày, N="Chị Duyên báo dd/mm: X đã trả …, còn nợ …". Kiểm tra K + L = H.
- Chị không nói ngày thì ghi ngày hôm nay và báo cho chị biết.

### Tab báo cáo
"Lợi nhuận", "Công nợ", "Tổng hợp tháng" là số dán cứng. Chị phải bấm menu **Duynpao → cập nhật** thì số mới đổi. Cuối mỗi lượt sửa, nhắc chị bấm.

## Quy tắc của chị
- Huỷ đơn: đổi P thành "Huỷ", **không xoá dòng**. Chỉ xoá khi chị xác nhận là trùng. Hai đơn cùng khách, cùng ngày, cùng số lượng thì coi là trùng.
- Giao sớm: sửa G thành ngày giao thật, O ghi "Khách hẹn nhận 26/11, đã giao sớm 24/11".
- Đơn nhập bù: P="Đã giao", O="đơn nhập bù · Đã giao dd/mm/yyyy (theo ngày khách báo)", G = ngày khách báo, B = tháng của ngày nhận.
- Hàng giao thiếu khách báo lại thì không tính. Bánh tặng để giá 0đ. Dừa sợi không cho vào đơn.
- Viết tắt: h = hộp 4 bánh; t/túi = túi 6 bánh; "thịt" = Thịt 1 trứng; chay xanh/trắng = Chay sữa (ghi màu vào ghi chú); chay nút = Gạo lứt; chay cám = Nguyên cám; 1kg chay = 2 túi Chay sữa túi 500gr.
- Giá sỉ/bánh: xem skill `gia-si-chinh-sach-duynpao`.
- Tên Zalo đổi sang tên khách: Dũng An→Đức; Quang Minh→Yến; Hương Nam→Hương; Thanh Tâm→Cô Tâm; Minh Nguyễn→Cô Minh; Lanh Lê→Lanh; Phạm Tâm→Tâm Phạm; Thuỷ Bình→Bình; Phươngthuy→Bằng lăng; Huyền→Thành Nam 06; Vườn Xinh→Vân Anh; Nguyễn Bảo Ngọc→Hà Thu Hường.
- Phạm Hồng Tươi và Vjtmập (anh Việt) là người đặt hộ: đơn tính cho khách mà họ đặt hộ. Đơn "Xuân Khiêm" mặc định của Trung Thu. Ngọc Ánh, Thư con dê vàng và Linh Vy là một nhà. Thanh và Mai ở Dê Vàng là 2 khách khác nhau.
- SĐT không phải của khách: 0981094473 (anh Việt nhập hộ), 0975392409 (chị đặt hộ).

## Quy trình
1. Đọc theo cột (C:D, G, P), không đọc cả A1:T. Tìm khách theo tên, không phân biệt hoa thường hay dấu, kết hợp ngày nhận. Gom các dòng theo mã đơn.
2. Tìm dòng theo mã đơn **ngay lúc sửa**, không dùng lại số dòng cũ, vì xoá dòng làm số dòng bị lùi.
3. Sửa bằng `update_values`. Nhiều vùng rời nhau thì dùng một lệnh `update_spreadsheet`. Đổi P thì đồng bộ luôn cột I bên tab Thanh toán.
4. Trước khi ghi đè cột nào, xem đó có phải công thức không bằng `get_spreadsheet` (userEnteredValue). Chưa chắc chắn: Q, R, S và cột L của Thanh toán.
5. Đọc lại các ô vừa sửa, rồi báo chị bằng bảng: mã đơn | khách | tổng | đã sửa gì. Câu hỏi thì đánh số.
6. Nhập bù nhiều đơn: dựng bảng xem trước, chị duyệt "nhập đi" rồi mới `append_values`.

## Cách làm tốt hơn
- Kiểm tra trước khi ghi: trạng thái thuộc 3 giá trị cho phép, mã đơn chưa có, không trùng (khách, ngày nhận, loại, SL).
- Khi chị hỏi công nợ: lọc tab Thanh toán L>0, xếp theo số ngày nợ, gắn cờ nợ quá 7 ngày.
- Cuối tuần đề xuất danh sách đơn "Chờ xác nhận" có ngày nhận đã qua, để chị xác nhận giao hay huỷ.
