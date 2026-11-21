# Tạo hình nền có mã QR ở góc. Chạy sau tao_qr.py: python3 qr/tao_hinh_nen.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans"
RED, DARK, CREAM = (192, 57, 43), (142, 42, 31), (250, 246, 241)
code = Image.open(os.path.join(HERE, "duynpao-qr-chi-ma.png")).convert("RGB")

def bun(d, cx, cy, r, col):
    # bánh bao cách điệu: thân tròn dẹt + nếp xoắn trên đỉnh
    d.ellipse([cx-r, cy-r*0.75, cx+r, cy+r*0.75], outline=col, width=max(3, r//12))
    for k in range(-2, 3):
        a = k * 0.35
        d.arc([cx-r*0.55+k*r*0.12, cy-r*0.75, cx+r*0.55+k*r*0.12, cy+r*0.2],
              200+k*8, 340+k*8, fill=col, width=max(2, r//16))

def make(W, H, qr_size, corner, title_y, name, bottom_gap=0):
    img = Image.new("RGB", (W, H), CREAM)
    # nền chuyển màu nhẹ
    grad = Image.new("RGB", (1, H))
    for y in range(H):
        t = y / H
        grad.putpixel((0, y), tuple(int(CREAM[i]*(1-t*0.35) + (243, 214, 200)[i]*t*0.35) for i in range(3)))
    img = grad.resize((W, H))
    # họa tiết bánh bao mờ
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    step = int(min(W, H) / 4.5); r = step // 4
    for j, y in enumerate(range(-step//2, H + step, step)):
        for x in range(-step//2 + (step//2 if j % 2 else 0), W + step, step):
            bun(d, x, y, r, (192, 57, 43, 28))
    img.paste(layer, (0, 0), layer)
    d = ImageDraw.Draw(img)
    # tiêu đề
    s = min(W, H)
    ft = ImageFont.truetype(F + "-Bold.ttf", int(s * 0.12))
    fs = ImageFont.truetype(F + ".ttf", int(s * 0.035))
    def center(y, t, f, c):
        d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=c)
    center(title_y, "DUYNPAO", ft, RED)
    center(title_y + int(s*0.15), "Bánh bao nhà làm", fs, DARK)
    # thẻ QR ở góc
    pad, m = int(qr_size*0.07), int(s*0.04)
    fl = ImageFont.truetype(F + "-Bold.ttf", int(qr_size*0.075))
    cap = "Quét để liên hệ"
    cw, ch = qr_size + 2*pad, qr_size + 2*pad + int(qr_size*0.13)
    x0 = W - cw - m if "r" in corner else m
    y0 = H - ch - m - bottom_gap if "b" in corner else m
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0+6, y0+10, x0+cw+6, y0+ch+10], radius=pad*2, fill=(80, 20, 10, 70))
    sh = sh.filter(ImageFilter.GaussianBlur(14)); img.paste(sh, (0, 0), sh)
    d.rounded_rectangle([x0, y0, x0+cw, y0+ch], radius=pad*2, fill="white", outline=RED, width=max(3, pad//4))
    img.paste(code.resize((qr_size, qr_size), Image.NEAREST), (x0+pad, y0+pad))
    d.text((x0 + (cw - d.textlength(cap, font=fl))/2, y0 + pad + qr_size + int(qr_size*0.02)), cap, font=fl, fill=DARK)
    img.save(os.path.join(HERE, name))
    print(name, img.size)

make(2560, 1440, 560, "br", 420, "hinh-nen-may-tinh.png", bottom_gap=60)     # máy tính, QR góc phải dưới
make(1170, 2532, 600, "br", 700, "hinh-nen-dien-thoai.png", bottom_gap=260)   # điện thoại, QR góc phải dưới
