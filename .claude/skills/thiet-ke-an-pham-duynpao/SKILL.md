---
name: thiet-ke-an-pham-duynpao
description: Dùng khi Duyên nhờ thiết kế ấn phẩm hoặc ảnh cho Duynpao hay BNI: đề can tủ hấp, poster, ảnh bìa fanpage, thiệp sinh nhật, mã QR liên hệ, hình nền, video ngắn; xuất PNG/JPG/PDF để in hoặc đăng.
---

# Thiết kế ấn phẩm (PNG/PDF/video)

## Cách dựng
- Viết HTML/CSS, chụp bằng Playwright (chromium có sẵn, `deviceScaleFactor: 2`) ra PNG hoặc PDF (`page.pdf` với kích thước mm thật).
- **Luôn tự xem lại** ảnh bằng Read trước khi gửi bằng SendUserFile. PDF thì chuyển ra ảnh bằng `pdftoppm` để soát font tiếng Việt.
- Font Google: **Be Vietnam Pro** (chữ thường), **Baloo 2** (tiêu đề), Playfair Display (thiệp).
- Màu Duynpao:
  - Bộ cam vàng (đề can, poster): `--or:#F7931E; --or2:#E2620D; --red:#C4161C; --red2:#8F0F12; --yel:#FFD23F; --cream:#FFF6E6; --brown:#5A1E0E`.
  - Bộ đỏ đô (trang đặt hàng, ảnh bìa): `#c0392b` / `#8e2a1f`, nền `#faf6f1`.
- Lưu vào repo (thư mục theo loại: `cover/`, `thiep/`, `qr/`, …) rồi commit và push, vì scratchpad sẽ mất khi session kết thúc. Bản cuối thì tải lên Drive.
- Drive `create_file` chỉ nhận khoảng 3MB. File lớn hơn thì nén bằng Ghostscript (`-dPDFSETTINGS=/ebook` hoặc `/printer`) để xem, và dặn chị giữ file gốc để mang đi in.
- Thư mục Drive chỉ giữ bản mới nhất; bản cũ chuyển vào thùng rác sau khi chị duyệt.

## Kích thước chuẩn đã dùng
| Ấn phẩm | Kích thước | Ghi chú |
|---|---|---|
| Đề can tủ hấp | 108×50 cm = 3 mặt 36×50 | tông cam vàng, không ghi giá; Drive thư mục `13NeqDiKw5f32ezGpGiPEFHKiQEVi-ceq` |
| Poster tuyển đại lý | A3 297×420 mm + bản JPG | Drive thư mục `1MK6GE5eQHdHqY_v1q4Psir7cbHyVitLw` |
| Ảnh bìa fanpage | 3280×1248 px | chữ ở giữa, chừa góc trái dưới cho ảnh đại diện |
| Thiệp sinh nhật BNI | 1080×1350 px | màu đỏ + logo BNI, khung tròn cho ảnh, kèm .txt nội dung bài; danh sách thành viên ở sheet `1LLiVLMIzULtWWJSS4W5ZiQBNrBuYRloemdFFO5V-VGM` |
| Video TikTok | 9:16 dọc | PIL dựng chữ + ffmpeg ghép; xuất contact-sheet khung hình để soát |
| Hình nền điện thoại có QR | theo máy | mã đặt ở nửa trên, chừa 1/4 dưới cho nút đèn pin, không đè lên ảnh |

## Quy tắc của chị
- Ảnh sản phẩm giữ nguyên gốc. Chỉ làm sáng chiếc bánh khi chị yêu cầu.
- Ấn phẩm không ghi giá (trừ bảng giá sỉ, xem skill catalog).
- Gửi 1–2 phương án, chị chọn rồi mới làm chi tiết. Sửa đúng chỗ chị nói, giữ nguyên phần còn lại.

## Mã QR
- vCard hoặc link: rút gọn URL (bỏ `www`), mức sửa lỗi L để mã thưa và dễ quét. Thêm logo vào giữa thì dùng mức H.
- Sau khi tạo, **tự quét thử** bằng `zxingcpp` ở các mức thu nhỏ 0.5/0.35/0.25 và có làm mờ.
- Không dùng link Claude/artifact hay `file:///` làm QR.
- Việc còn treo: chị muốn quét ra thấy ảnh đại diện → phương án là trang liên hệ (GitHub Pages) với ảnh đại diện, QR trỏ tới trang đó. Chờ chị chọn ảnh.

## Cách làm tốt hơn khi in
- Thêm bleed 3 mm (đề can khổ lớn 5 mm), chữ cách mép tối thiểu 5 mm. Nói với nhà in là file RGB, hoặc xuất PDF/X CMYK nếu họ yêu cầu.
- Độ phân giải ảnh tại kích thước thật: ≥150 DPI cho đề can xem cách 1 m, ≥300 DPI cho poster A3.
- Đề can tủ hấp: dùng loại chịu nhiệt, có cán màng. In thử một mặt trước rồi mới in cả bộ.
- QR in tối thiểu 3×3 cm, có vùng trắng 4 ô quanh mã. Nên dùng QR trỏ tới một link mình kiểm soát được, để sau này đổi thông tin mà không phải in lại.
