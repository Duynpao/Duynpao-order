# Tạo mã QR danh thiếp (vCard) Duynpao. Chạy: python3 qr/tao_qr.py
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
VCARD = "\r\n".join([
    "BEGIN:VCARD", "VERSION:3.0",
    "N:;Duynpao;;;", "FN:Duynpao - Bánh bao",
    "TEL;TYPE=CELL:0975392409",
    "TEL;TYPE=CELL:0925983535",
    "URL:https://zalo.me/0975392409",
    "item1.URL:https://facebook.com/oduyen.412635",
    "item1.X-ABLabel:Facebook",
    "item2.URL:https://facebook.com/duynpao",
    "item2.X-ABLabel:Fanpage",
    "item3.URL:https://drive.google.com/file/d/18yF7zXvWLI34RQ8Q5gWO359D9-DyRhZ0/view",
    "item3.X-ABLabel:Catalog",
    "item4.URL:https://tiktok.com/@duynpao10",
    "item4.X-ABLabel:TikTok",
    "END:VCARD",
])

RED, DARK, BG = (192, 57, 43), (142, 42, 31), (250, 246, 241)
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)
qr.add_data(VCARD.encode("utf-8"))
qr.make(fit=True)
code = qr.make_image(fill_color=DARK, back_color="white").convert("RGB")

W = code.width + 160
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans"
f_title = ImageFont.truetype(F + "-Bold.ttf", 84)
f_sub = ImageFont.truetype(F + ".ttf", 40)
f_line = ImageFont.truetype(F + "-Bold.ttf", 44)
lines = ["SĐT / Zalo: 0975 392 409", "SĐT / Zalo: 0925 983 535", "Fanpage: fb.com/duynpao", "TikTok: @duynpao10"]
H = 200 + code.height + 90 + len(lines) * 66 + 70
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
def center(y, text, font, fill):
    w = d.textlength(text, font=font); d.text(((W - w) / 2, y), text, font=font, fill=fill)
center(50, "DUYNPAO", f_title, RED)
center(150, "Quét mã để lưu liên hệ", f_sub, DARK)
d.rounded_rectangle([60, 210, W - 60, 230 + code.height + 20], radius=30, fill="white", outline=RED, width=6)
img.paste(code, (80, 240))
y = 240 + code.height + 60
for t in lines:
    center(y, t, f_line, DARK); y += 66
img.save(os.path.join(HERE, "duynpao-qr-lien-he.png"), dpi=(300, 300))
code.save(os.path.join(HERE, "duynpao-qr-chi-ma.png"))
with open(os.path.join(HERE, "duynpao.vcf"), "w", encoding="utf-8") as fh: fh.write(VCARD)
print("Đã tạo xong", img.size)
