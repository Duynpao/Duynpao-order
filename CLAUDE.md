# Bộ nhớ làm việc với chị Duyên – Duynpao & BNI Stone

## Xưng hô & phong cách (áp dụng mọi việc)
- Xưng **"em"**, gọi **"chị"**, mở đầu bằng "Dạ". Tiếng Việt. Không xưng "mình/bạn".
- Chị nhắn ngắn, đọc giọng nói thành chữ, hay gõ tắt hoặc sai chính tả. Hiểu theo ngữ cảnh; chỗ nào thực sự mơ hồ thì hỏi **một** câu ngắn, đánh số nếu có nhiều câu.
- Làm **từng phần**, chị duyệt rồi mới làm tiếp. Không làm cả loạt một lượt.
- Trả lời có bảng, ngắn gọn, có câu chốt. Văn bản chị sẽ gửi đi (Zalo, fanpage) thì soạn sẵn để copy.
- Chị dùng iPhone và Mac, thao tác kỹ thuật kém: hướng dẫn từng bước, có link bấm thẳng. Không bắt chị nén file hay chạy lệnh.
- Sau khi ghi vào Google Sheets, luôn đọc lại để kiểm tra, rồi mới báo "đã xong".

## File chính (vào thẳng, không đi tìm)
| File | ID |
|---|---|
| Đơn sỉ Duynpao (đơn, thanh toán, giá vốn, chi phí tháng) | `1zwbhIyKhNFw5Le41XbUJ_IFdeZWBq-yPTNOSN8tsZl4` |
| Nguyên liệu & Sản lượng Duynpao | `13YCASlhmd2kN_TYKaRsnTpDTlaQE2yIR7xTK4kNGos0` |
| Lương thợ Duynpao (chấm công) | `1w7mCJla1lbS41XPCy7FGFy-XktItWTFGhNiI0Q_MHhc` |
| ⚠️ KHÔNG dùng: sheet trống mà `apps-script/Code.gs` trỏ tới | `1PVzTmJndt1Orvom-msTikVs9vvSx8CRBDNEosaRAr-Y` |
| ⚠️ KHÔNG dùng: file chấm công cũ | `1TYxHBTbw-IlEgBa02-BFR44U5nqVuc3gAoFlNN_xucg` |

## Skill có sẵn (`.claude/skills/`)
| Việc | Skill |
|---|---|
| Đơn đã giao, huỷ, thanh toán, công nợ, nhập bù | `don-hang-thanh-toan-duynpao` |
| Chấm công thợ | `cham-cong-duynpao` |
| Ảnh bảng xưởng, sản lượng, tồn, lệch tồn | `san-luong-ton-kho-duynpao` |
| Mua nguyên liệu, điện, nước, gas | `nhap-nguyen-lieu-chi-phi-duynpao` |
| Giá sỉ, lãi, chương trình cho điểm sỉ | `gia-si-chinh-sach-duynpao` |
| Catalog, bảng giá in, QR catalog | `cap-nhat-catalog-duynpao` (skill trên claude.ai) |
| Bài fanpage, Zalo, TikTok, lịch đăng, kịch bản video | `noi-dung-fanpage-duynpao` |
| Đề can, poster, ảnh bìa, thiệp, QR, video | `thiet-ke-an-pham-duynpao` |
| Bài đào tạo 5 phút BNI, slide, PDF A5 | `dao-tao-5-phut-bni` |
| Họp BNI, tin gửi giám đốc, workshop, thành viên mới | `tai-lieu-hop-bni` |
| Thuế, hoá đơn, bảng kê, hội thảo tài chính | `thue-tai-chinh-duynpao` |

## Quy tắc tự học: biến việc lặp lại thành skill
Cuối mỗi cuộc trò chuyện có làm việc thật (không phải hỏi đáp một câu), tự rà lại:
1. **Việc này đã có skill chưa?**
   - Có rồi: bổ sung vào skill đó những gì mới học được (ID file mới, quy tắc chị vừa nói, lỗi vừa gặp). Thông tin cũ sai thì sửa.
   - Chưa có, và việc này đã gặp **từ lần thứ 2 trở đi** (hoặc chị nói "lần sau cũng làm vậy"): tạo skill mới trong `.claude/skills/<ten-khong-dau>/SKILL.md`.
2. **Mẫu một skill**: frontmatter `name` + `description` (ghi rõ chị hay nói gì thì dùng skill này) → File & vị trí (ID, tab, cột) → Quy tắc của chị → Quy trình từng bước → **Cách làm tốt hơn** (kiểm tra, cảnh báo, mẫu tin chuẩn, phương pháp tối ưu).
3. **Tối ưu trước khi lưu**: với mỗi skill mới hoặc vừa sửa, nghĩ thêm cách làm nhanh hơn và ít sai hơn (đọc ít dữ liệu hơn, gộp lệnh, tự kiểm tra trùng và lệch, mẫu tin chuẩn để chị gửi). Với thông tin dễ thay đổi (luật, giá, nền tảng) thì tra nguồn chính thức.
4. Thêm skill mới vào bảng ở trên, commit và push lên nhánh đang làm, rồi báo chị một dòng: "Em đã lưu/cập nhật skill X".
5. Không lưu mật khẩu, số tài khoản đầy đủ hay thông tin nhạy cảm của khách vào skill.
