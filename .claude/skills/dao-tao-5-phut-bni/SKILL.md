---
name: dao-tao-5-phut-bni
description: Dùng khi Duyên nhờ soạn bài đào tạo 5 phút (education moment) cho BNI Stone, gồm kịch bản, chuỗi bài theo tuần, slide minh hoạ hoạt hình và bản in PDF A5 cho diễn giả.
---

# Bài đào tạo 5 phút – BNI Stone

Đọc thêm bối cảnh chapter trong `../tai-lieu-hop-bni/boi-canh-bni.md`.

## Tài sản đã có
- Claude Doc "Kịch bản đào tạo 5 phút – Sự hiện diện": https://claude.ai/artifact/R2bxpHr2GschmtCFY4n5JB. Gồm bài nền và tuần 1–14.
  - Tuần 1–7: Hòn than, Quán mở cửa đúng giờ, Khi ăn thì ăn, Đàn ngỗng, Cây tre, Hoàng tử bé, Bó đũa.
  - Tuần 8–14: Mài rìu, Hải đăng, Căn phòng nói thay ta, Gandhi, Tăng Tử, Sao biển, Bình nứt.
  - **Không lặp lại chuyện đã dùng.**
- Google Slides: bài nền `1096hlnlgsqvHDwm48bP6_Oi5GcXtEiQgy_aWaZqSxBU`, tuần 10 `1sIjb4bVzTg8JzFb6Wt0RAAvrOjXmPLbj3b_5isL0v_w`. Nhân vật dùng chung: Thỏ Lan, Gấu Hưng, Cô Cú, Mèo Mi.
- Bộ slide "Ba câu hỏi" (Artifact Slides): https://claude.ai/artifact/CidTi9NtQChzqKhZw41m9s, kèm bản in Kich-ban-Ba-cau-hoi-A5.pdf.
- Tài liệu gốc BNI trên Drive, thư mục `1SFyPDhoPOjbWUQb0WCHLZ04umLjMgCxo` (Thẩm định.pdf, Brochure sau kết nạp.pdf). BNI Academy cần đăng nhập nên Claude không vào được; nhờ chị đối chiếu số liệu.

## Khung một bài (5 phút ≈ 650 từ)
1. **Mở đầu** (30–45 giây): câu hỏi, hoặc một hành động như úp điện thoại, hít thở.
2. **Câu chuyện** (~1:30): chuyện có thật hoặc chuyện đời thường. Không dùng cổ tích hay ngụ ngôn. Nhân vật minh hoạ phải ghi rõ là minh hoạ.
3. **Câu chuyện nói gì với chapter mình?** (~1:00): gắn với vấn đề thật của chapter, có ô [ ] để chị điền số liệu.
4. **Hành động tuần này** (~1:15): một việc cụ thể, đo được.
5. **Chốt** (30 giây): nhắc lại thông điệp, cam kết.
Đầu mỗi bài ghi các mục: Vấn đề · Thông điệp · Đạo cụ · Số từ.

## Quy trình (làm từng phần, chị duyệt rồi mới làm tiếp)
1. Gửi dàn ý hoặc bảng tổng quan chuỗi bài trước. **Không viết cả loạt một lượt**, chị đã từng ngắt "e từ từ".
2. Viết kịch bản vào Claude Doc, mỗi bài một lần gọi. Trong bài, Duyên xưng "tôi", gọi "anh chị".
3. Slide: làm thử 1 bài trước. Vẽ nhân vật SVG, render bằng Playwright, dựng bằng python-pptx, tải lên Drive (tự chuyển thành Google Slides). Hoặc dùng Artifact type Slides.
4. **Luôn xuất ngược** Google Slides ra PDF (`download_file_content`, exportMimeType pdf) rồi `pdftoppm` để soát font tiếng Việt và hình.
5. Bản in cho diễn giả: HTML `@page{size:A5}`, render PDF bằng Playwright. Gắn nhãn SLIDE n, thụt lề lời thoại, câu chốt trong ô nền kem, ghi chú "(Dừng 3–5 giây)", số trang n/N. Dặn chị in A5, **tỉ lệ 100% (Actual size)**.
6. Sắp slide theo đúng thứ tự chị đưa. Phần nào không có trong kịch bản của chị thì **ẩn** đi, không xoá.
7. Tự soát phần kết: có chỗ nào bỏ lửng không, rồi báo chị.

## Cách làm tốt hơn
- Đếm từ (130 từ/phút) và ghi thời lượng ước tính trong kịch bản.
- Mỗi bài 1 thông điệp và 1 lời kêu gọi gắn với chỉ số PALMS (tỷ lệ hiện diện, 1-2-1, khách mời). Tuần 7 và 14 so số liệu trước và sau.
- Slide tối đa 6–7 trang, mỗi trang một ý, chữ ≥ 28pt, lời nói để trong speaker notes.
- PDF A5: thân chữ 12–13pt, thêm vạch mốc thời gian bên lề, kiểm tra trang trắng thừa bằng `pdfinfo`.
- Lập thư mục Drive cố định "Đào tạo 5 phút", đặt tên file `Tuần NN – Tên bài`. Hỏi chị trước khi tạo.
