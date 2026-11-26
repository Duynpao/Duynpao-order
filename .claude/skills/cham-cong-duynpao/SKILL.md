---
name: cham-cong-duynpao
description: Dùng khi Duyên báo chấm công thợ xưởng Duynpao (tin nhắn kiểu "Mai Thủy Bảy Tươi Hồng đủ công, TC 4 tiếng", ảnh chụp tin, nghỉ P/K/H) để ghi vào sheet Lương thợ và báo lại bảng Người × Ngày.
---

# Chấm công thợ Duynpao

## File & vị trí (vào thẳng, không đi tìm file)
- **Lương thợ Duynpao**: `1w7mCJla1lbS41XPCy7FGFy-XktItWTFGhNiI0Q_MHhc`. Tab "Hướng dẫn lương", "Cài đặt lương", "Lương YYYY-MM" (hiện tại "Lương 2026-11").
- KHÔNG dùng file chấm công cũ `1TYxHBTbw-IlEgBa02-BFR44U5nqVuc3gAoFlNN_xucg`.
- Tab tháng: B2 = tháng, H2 = TỔNG LƯƠNG THÁNG. Dòng 5 = số ngày. **Cột ngày d = cột I + (d−1)** (1→I, 15→W, 22→AD, 24→AF, 31→AM).
- Dòng nhân viên (dòng ngay dưới mỗi người = "↳ Tăng ca (giờ)"):
  | Dòng | Người | Việc |
  |---|---|---|
  | 6 | Đoàn Văn Bẩy | bếp |
  | 8 | Đoàn Văn Mai | gói bánh |
  | 10 | Đoàn Thị Thuỷ | làm bột |
  | 12 (TC: 13) | Phạm Hồng Tươi | ủ hấp, quản lý |
  | 14 | Nguyễn Văn Việt | QL sản xuất, giao hàng |
  | 16 | Hồng | lên đơn, quay chụp (thử việc) |

## Ký hiệu
X = đủ 8 tiếng · NH = nửa ngày, chủ cho nghỉ nửa còn lại · N = nửa ngày, thợ xin nghỉ · H = chủ cho nghỉ cả ngày (70%) · số giờ (vd 6) = làm 6 tiếng · "6H" = làm 6 tiếng, 2 tiếng chủ cho nghỉ · L = làm ngày lễ (200%) · T = thử việc (85%) · P = phép · K = không phép · trống = không làm.
Tăng ca 25.000đ/giờ; đơn giá công = lương tháng/28; chuyên cần 200k; xăng = 200k × công/28.

## Quy tắc mặc định của chị
- Việt mặc định X mỗi ngày. Hồng ghi **T** đến khi chị báo hết thử việc.
- Tăng ca chỉ ghi cho **Tươi** (dòng 13), đúng số "TC" trong tin, không tự trừ giờ ăn.
- Không ghi giờ vào/ra. Ô đã có K thì giữ và hỏi lại.
- Tin không ghi ngày → lấy ngày ngay sau ngày cuối đã điền, và nói rõ giả định đó.
- "H" đứng lẻ, không rõ là ai → hỏi lại chị chứ không đoán.

## Quy trình
1. `get_values` `'Lương YYYY-MM'!I5:AM16` để biết các ngày đã điền và tránh ghi đè.
2. Mỗi ngày ghi một khối dọc dòng 6–16 bằng `update_values`, ví dụ `[["X"],[null],["X"],[null],["X"],[null],["X"],[4],["X"],[null],["T"]]`. Gộp nhiều ngày vào một lần gọi (một khối chữ nhật nhiều cột).
3. Đọc lại khối vừa ghi rồi báo chị bằng bảng nhỏ Người × Ngày, kèm các điểm cần xác nhận (tối đa 1–2 câu hỏi).

## Sang tháng mới
Nhân bản tab tháng trước, đặt tên "Lương YYYY-MM", sửa B2, xoá I6:AM45. Tab "Chi phí tháng" bên file Đơn sỉ tự kéo H2 qua IMPORTRANGE theo tên tab, nên tên phải đúng định dạng.

## Cách làm tốt hơn
- Cảnh báo khi: tăng ca > 5 giờ/ngày, ô đã có số bị ghi đè, có người trống quá 2 ngày liền mà không có P/K.
- Mẫu tin gợi ý cho chị: `dd/mm: đủ công [trừ …]; Tươi TC x; nghỉ: tên (P/K/H)`.
- Cuối tháng đọc H2 và từng dòng tổng để gửi chị bảng lương tóm tắt trước ngày trả lương.
