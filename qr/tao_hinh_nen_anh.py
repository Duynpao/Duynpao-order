# Hình nền từ ảnh minh hoạ của chị, chèn mã QR vào góc. Chạy: python3 qr/tao_hinh_nen_anh.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
HERE = os.path.dirname(os.path.abspath(__file__))
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans"
RED, DARK, CREAM = (192, 57, 43), (142, 42, 31), (253, 241, 226)
art = Image.open(os.path.join(HERE, "anh-chi-duyen.webp")).convert("RGB")
code = Image.open(os.path.join(HERE, "duynpao-qr-chi-ma.png")).convert("RGB")

def feather(size, f):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rectangle([f, f, size[0]-f, size[1]-f], fill=255)
    return m.filter(ImageFilter.GaussianBlur(f / 2))

def qr_card(img, x0, y0, qr_size):
    d = ImageDraw.Draw(img); W, H = img.size
    pad = int(qr_size * 0.07)
    fl = ImageFont.truetype(F + "-Bold.ttf", int(qr_size * 0.075))
    cap = "Quét để liên hệ"
    cw, ch = qr_size + 2*pad, qr_size + 2*pad + int(qr_size * 0.13)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0+6, y0+10, x0+cw+6, y0+ch+10], radius=pad*2, fill=(90, 50, 20, 60))
    sh = sh.filter(ImageFilter.GaussianBlur(14)); img.paste(sh, (0, 0), sh)
    d.rounded_rectangle([x0, y0, x0+cw, y0+ch], radius=pad*2, fill="white", outline=RED, width=max(3, pad//4))
    img.paste(code.resize((qr_size, qr_size), Image.NEAREST), (x0+pad, y0+pad))
    d.text((x0 + (cw - d.textlength(cap, font=fl))/2, y0 + pad + qr_size + int(qr_size*0.02)), cap, font=fl, fill=DARK)
    return cw, ch

def place(bg, size, xy, f):
    a = art.resize(size, Image.LANCZOS)
    bg.paste(a, xy, feather(size, f))

# Máy tính 2560x1440: ảnh ở giữa-trái, QR bên trái trên nền kem
W, H = 2560, 1440
img = Image.new("RGB", (W, H), CREAM)
place(img, (1440, 1440), (W - 1440 - 380, 0), 90)
qs = 460; cw = qs + 2*int(qs*0.07); ch = qs + 2*int(qs*0.07) + int(qs*0.13)
qr_card(img, 70, H - ch - 220, qs)
img.save(os.path.join(HERE, "hinh-nen-anh-may-tinh.png"))

# Điện thoại 1170x2532: ảnh ở giữa, QR bên trái
W, H = 1170, 2532
img = Image.new("RGB", (W, H), CREAM)
place(img, (1120, 1120), (25, 230), 70)
qs = 510; cw = qs + 2*int(qs*0.07); ch = qs + 2*int(qs*0.07) + int(qs*0.13)
qr_card(img, 60, 1370, qs)
img.save(os.path.join(HERE, "hinh-nen-anh-dien-thoai.png"))
print("xong")
