"""Render the Bodugola signature-product hero video from Lyre's own photography.

Style reference: short premium AI product ad (macro push-ins, light sweep,
kinetic serif type, logo end card). Everything is built from the real
restaurant photo in assets/img/bodugola.webp -- no generated food imagery.

Usage:  python3 tools/render_signature_video.py [landscape|portrait|all]
Needs:  pillow, numpy, imageio-ffmpeg; Playfair Display + Titillium Web TTFs
        in assets/fonts/ (Google Fonts, OFL).
"""
import math
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets/img"
FONTS = ROOT / "assets/fonts"
OUT = ROOT / "assets/video"
FPS = 30
DUR = 14.0

RED = (235, 30, 61)
WINE = (106, 27, 49)
CREAM = (250, 243, 232)
INK = (30, 26, 29)


def font(name, size, variation=None):
    f = ImageFont.truetype(str(FONTS / name), size)
    if variation:
        f.set_variation_by_name(variation)
    return f


def ease(t):  # easeOutCubic, clamped
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def ease_io(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


SRC = Image.open(IMG / "bodugola.webp").convert("RGB")
# crop away the "2KG" overlay text baked into the top-right of the post
SRC = SRC.crop((0, 18, SRC.width, SRC.height))
LOGO = Image.open(IMG / "logo-white.png").convert("RGBA")


def cover_crop(cx, cy, cw, W, H):
    """Crop a W:H window of width cw centred on (cx,cy) in SRC, scaled to W×H."""
    ch = cw * H / W
    if ch > SRC.height:
        ch = SRC.height
        cw = ch * W / H
    x0 = min(max(cx - cw / 2, 0), SRC.width - cw)
    y0 = min(max(cy - ch / 2, 0), SRC.height - ch)
    im = SRC.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))
    return im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))


def vignette(W, H, strength=0.65):
    y, x = np.ogrid[:H, :W]
    d = np.sqrt(((x - W / 2) / (W / 2)) ** 2 + ((y - H / 2) / (H / 2)) ** 2) / math.sqrt(2)
    m = 1 - strength * np.clip(d, 0, 1) ** 1.8
    return m[..., None]


def grade(im, vig):
    a = np.asarray(im).astype(np.float32)
    a = a * vig
    # warm, slightly lifted contrast
    a = (a - 128) * 1.06 + 128
    a[..., 0] *= 1.03
    a[..., 2] *= 0.96
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def grain(im, rng, amt=7):
    a = np.asarray(im).astype(np.int16)
    n = rng.integers(-amt, amt + 1, size=a.shape[:2], dtype=np.int16)[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))


def text_layer(W, H):
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def draw_rise(layer, xy, txt, fnt, fill, t, dist=40, anchor="ls"):
    """Draw text rising into place with fade; t in 0..1."""
    e = ease(t)
    if e <= 0:
        return
    tmp = text_layer(*layer.size)
    d = ImageDraw.Draw(tmp)
    x, y = xy
    d.text((x, y + dist * (1 - e)), txt, font=fnt, fill=fill + (int(255 * e),), anchor=anchor)
    layer.alpha_composite(tmp)


def light_sweep(im, t, W, H):
    """Diagonal specular sweep across the frame, t in 0..1."""
    if t <= 0 or t >= 1:
        return im
    y, x = np.ogrid[:H, :W]
    pos = -0.3 * W + t * 1.6 * W
    d = (x + 0.45 * y) - pos
    band = np.exp(-(d / (0.07 * W)) ** 2) * 0.28
    a = np.asarray(im).astype(np.float32)
    a = a + (255 - a) * band[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


class Renderer:
    def __init__(self, W, H):
        self.W, self.H = W, H
        s = min(W, H * 1.6) / 1280  # type scale
        self.s = s
        big = int(150 * s) if W > H else int(120 * W / 720)
        self.f_big = font("PlayfairDisplay[wght].ttf", big, "Black")
        self.f_mid = font("PlayfairDisplay[wght].ttf", int(big * 0.52), "Black")
        self.f_it = font("PlayfairDisplay-Italic[wght].ttf", int(big * 0.3), "Bold Italic")
        self.f_cap = font("TitilliumWeb-Bold.ttf", max(16, int(22 * s * (1 if W > H else 1.25))))
        self.vig = vignette(W, H)
        self.vig_soft = vignette(W, H, 0.35)
        self.rng = np.random.default_rng(7)
        lw = int((210 if W > H else 220) * s * (1 if W > H else 1.3))
        self.logo = LOGO.resize((lw, int(lw * LOGO.height / LOGO.width)), Image.LANCZOS)

    def label(self, layer, n, txt, t, on_red=False):
        W, H, s = self.W, self.H, self.s
        pill, num = (CREAM, RED) if on_red else (RED, CREAM)
        e = ease(t)
        d = ImageDraw.Draw(layer)
        x, y = int(48 * s), int(56 * s)
        a = int(255 * e)
        d.rounded_rectangle((x, y - int(20 * s), x + int(36 * s), y + int(12 * s)), radius=int(16 * s), fill=pill + (a,))
        d.text((x + int(18 * s), y - 4 * s), n, font=self.f_cap, fill=num + (a,), anchor="mm")
        d.text((x + int(50 * s), y - 4 * s), txt, font=self.f_cap, fill=CREAM + (a,), anchor="lm")

    # --- shots -----------------------------------------------------------
    def shot_cheese(self, t, lt):
        W, H, s = self.W, self.H, self.s
        p = t / 3.0
        cw = (560 - 110 * ease_io(p)) if W > H else (380 - 80 * ease_io(p))
        im = cover_crop(300 + 30 * p, 420, cw, W, H)
        im = grade(im, self.vig)
        lay = text_layer(W, H)
        self.label(lay, "01", "LYRE SIGNATURE", (t - 0.2) / 0.5)
        x = int(56 * s)
        yb = H - int(70 * s)
        draw_rise(lay, (x, yb - self.f_big.size * 0.95), "TWO", self.f_big, CREAM, (t - 0.35) / 0.6)
        draw_rise(lay, (x, yb), "KILOS.", self.f_big, CREAM, (t - 0.55) / 0.6)
        return im, lay

    def shot_fries(self, t, lt):
        W, H, s = self.W, self.H, self.s
        p = lt / 2.6
        if W > H:
            im = cover_crop(360 + 160 * ease_io(p), 600, 540, W, H)
        else:
            im = cover_crop(420 + 120 * ease_io(p), 560, 360, W, H)
        im = grade(im, self.vig)
        lay = text_layer(W, H)
        self.label(lay, "02", "BEEF · CHEESE · FRIES", (lt - 0.1) / 0.5)
        x = int(56 * s)
        yb = H - int(70 * s)
        draw_rise(lay, (x, yb - self.f_big.size * 0.95), "ONE", self.f_big, CREAM, (lt - 0.2) / 0.6)
        draw_rise(lay, (x, yb), "BURGER.", self.f_big, CREAM, (lt - 0.4) / 0.6)
        return im, lay

    def shot_split(self, t, lt):
        W, H, s = self.W, self.H, self.s
        base = Image.new("RGB", (W, H), RED)
        landscape = W > H
        if landscape:
            ph = H
            z = 1.0 + 0.06 * ease_io(lt / 4.0)
            pw = int(ph * SRC.width / SRC.height * z)
            phz = int(ph * z)
            pic = SRC.resize((pw, phz), Image.LANCZOS)
            px = W - pw + int((pw - W * 0.56) * 0.0)
            px = int(W * 0.44) - (pw - int(W * 0.56)) // 2
            base.paste(pic, (px, (H - phz) // 2))
            panel_w = int(W * 0.46)
        else:
            z = 1.0 + 0.06 * ease_io(lt / 4.0)
            pw = int(W * z)
            phz = int(pw * SRC.height / SRC.width)
            pic = SRC.resize((pw, phz), Image.LANCZOS)
            base.paste(pic, ((W - pw) // 2, H - phz + int(40 * s)))
            panel_w = W
        base = light_sweep(base, (lt - 1.2) / 1.6, W, H)
        base = grade(base, self.vig_soft)
        lay = text_layer(W, H)
        d = ImageDraw.Draw(lay)
        # red panel wipes in
        wipe = ease(lt / 0.6)
        if landscape:
            d.rectangle((0, 0, int(panel_w * wipe), H), fill=RED + (255,))
            # jagged stamp edge on the panel
            ex = int(panel_w * wipe)
            step = int(18 * s)
            pts = [(ex, 0)]
            for i, yy in enumerate(range(0, H + step, step)):
                pts.append((ex + (int(9 * s) if i % 2 else 0), yy))
            pts.append((ex, H))
            d.polygon(pts, fill=RED + (255,))
            x0 = int(56 * s)
            cy = H // 2
        else:
            d.rectangle((0, 0, W, int(H * 0.34 * wipe)), fill=RED + (255,))
            x0 = int(40 * s)
            cy = int(H * 0.15)
        self.label(lay, "03", "PRE-ORDER ONLY", (lt - 0.3) / 0.5, on_red=True)
        fb = self.f_mid if landscape else self.f_mid
        draw_rise(lay, (x0, cy - int(10 * s)), "BODUGOLA", fb, CREAM, (lt - 0.45) / 0.6, anchor="ls")
        draw_rise(lay, (x0, cy + int(44 * s)), "a.k.a. The Giant Burger", self.f_it, CREAM, (lt - 0.7) / 0.6, anchor="ls")
        draw_rise(lay, (x0, cy + int(100 * s)), "2 KG BEEF · FRIES · SALAD", self.f_cap, CREAM, (lt - 0.9) / 0.6, anchor="ls")
        return base, lay

    def shot_price(self, t, lt):
        W, H, s = self.W, self.H, self.s
        base = Image.new("RGB", (W, H), WINE)
        # radial glow
        y, x = np.ogrid[:H, :W]
        g = np.exp(-(((x - W / 2) / (W * 0.45)) ** 2 + ((y - H * 0.55) / (H * 0.55)) ** 2))
        a = np.asarray(base).astype(np.float32)
        a = a + (np.array(RED, dtype=np.float32) - a) * g[..., None] * 0.9
        base = Image.fromarray(a.astype(np.uint8))
        z = 1.2 - 0.2 * ease(lt / 1.6)
        land = W > H
        ph = int(H * (0.86 if land else 0.56) * z)
        pw = int(ph * 0.78)
        # arch-framed photo (echoes the arch motif used on the site)
        crop_h = SRC.width / 0.78
        y0 = max(0, (SRC.height - crop_h) / 2)
        pic = SRC.resize((pw, ph), Image.LANCZOS, box=(0, y0, SRC.width, min(SRC.height, y0 + crop_h)))
        m = Image.new("L", (pw, ph), 0)
        md = ImageDraw.Draw(m)
        md.ellipse((0, 0, pw - 1, pw - 1), fill=255)
        md.rectangle((0, pw // 2, pw - 1, ph - 1), fill=255)
        cx = W // 2
        top = (H - ph) // 2 + int(H * (0.04 if land else -0.06))
        sh = Image.new("L", (W, H), 0)
        sh.paste(m, (cx - pw // 2 + int(10 * s), top + int(24 * s)))
        sh = sh.filter(ImageFilter.GaussianBlur(int(26 * s)))
        base = Image.composite(Image.new("RGB", (W, H), (40, 8, 18)), base, sh.point(lambda v: int(v * 0.55)))
        base.paste(pic, (cx - pw // 2, top), m)
        base = grade(base, self.vig_soft)
        lay = text_layer(W, H)
        self.label(lay, "04", "SERVES THE CREW", (lt - 0.1) / 0.5)
        if W > H:
            draw_rise(lay, (int(56 * s), H - int(70 * s)), "MVR 500", self.f_mid, CREAM, (lt - 0.5) / 0.6)
            draw_rise(lay, (W - int(56 * s), H - int(78 * s)), "Order ahead. Bring backup.", self.f_it, CREAM, (lt - 0.8) / 0.6, anchor="rs")
        else:
            draw_rise(lay, (W // 2, H - int(140 * s)), "MVR 500", self.f_mid, CREAM, (lt - 0.5) / 0.6, anchor="ms")
            draw_rise(lay, (W // 2, H - int(64 * s)), "Order ahead. Bring backup.", self.f_it, CREAM, (lt - 0.8) / 0.6, anchor="ms")
        return base, lay

    def shot_end(self, t, lt):
        W, H, s = self.W, self.H, self.s
        base = Image.new("RGB", (W, H), RED)
        lay = text_layer(W, H)
        e = ease(lt / 0.8)
        lg = self.logo
        sc = 0.88 + 0.12 * e
        lgs = lg.resize((max(1, int(lg.width * sc)), max(1, int(lg.height * sc))), Image.LANCZOS)
        alpha = lgs.getchannel("A").point(lambda v: int(v * e))
        lgs.putalpha(alpha)
        lay.alpha_composite(lgs, ((W - lgs.width) // 2, int(H * 0.42) - lgs.height // 2))
        draw_rise(lay, (W // 2, int(H * 0.42) + lg.height // 2 + int(64 * s)), "is the place to be!", self.f_it, CREAM, (lt - 0.5) / 0.7, anchor="ms")
        draw_rise(lay, (W // 2, H - int(56 * s)), "BEACH ROAD · HULHUMALÉ", self.f_cap, CREAM, (lt - 0.9) / 0.6, anchor="ms", dist=16)
        return base, lay

    SHOTS = [(0.0, 3.0, "shot_cheese"), (3.0, 5.6, "shot_fries"), (5.6, 9.6, "shot_split"),
             (9.6, 12.0, "shot_price"), (12.0, 14.0, "shot_end")]
    XF = 0.3  # crossfade seconds

    def frame(self, t):
        out = None
        for i, (a, b, name) in enumerate(self.SHOTS):
            if a - (self.XF if i else 0) <= t < b:
                im, lay = getattr(self, name)(t, t - a)
                im = im.convert("RGBA")
                im.alpha_composite(lay)
                im = im.convert("RGB")
                if out is None:
                    out = im
                else:
                    k = ease_io((t - (a - self.XF)) / self.XF)
                    out = Image.blend(out, im, k)
        # fade the end card back to black-ish then into shot 1 for a seamless loop
        if t > DUR - 0.35:
            first, lay = self.shot_cheese(0.0, 0.0)
            k = ease_io((t - (DUR - 0.35)) / 0.35)
            out = Image.blend(out, first, k)
        return grain(out, self.rng, 5)


def render(kind):
    W, H = (1280, 720) if kind == "landscape" else (720, 900)
    r = Renderer(W, H)
    OUT.mkdir(parents=True, exist_ok=True)
    stem = OUT / f"bodugola-signature-{kind}"
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    n = int(DUR * FPS)
    common = ["-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"]
    procs = [
        subprocess.Popen([ff, "-y", "-loglevel", "error", *common, "-c:v", "libx264", "-preset", "slow",
                          "-crf", "24", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an",
                          f"{stem}.mp4"], stdin=subprocess.PIPE),
    ]
    for i in range(n):
        t = i / FPS
        fr = r.frame(t)
        if abs(t - 7.4) < 0.5 / FPS:
            fr.save(f"{stem}-poster.jpg", quality=82, optimize=True, progressive=True)
        b = fr.tobytes()
        for p in procs:
            p.stdin.write(b)
    for p in procs:
        p.stdin.close()
        p.wait()
    print("wrote", stem)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for k in (["landscape", "portrait"] if which == "all" else [which]):
        render(k)
