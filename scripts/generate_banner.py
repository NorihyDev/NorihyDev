"""Rebuild the original banner: python scripts/generate_banner.py (requires Pillow)."""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
WIDTH, HEIGHT = 1200, 370
INK, MUTED, CYAN, VIOLET = "#edf5ff", "#a6b5cc", "#6ee7f7", "#b4a1ff"


def font(size: int, *, bold: bool = False, mono: bool = False):
    if mono:
        candidates = ["C:/Windows/Fonts/consola.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"]
    elif bold:
        candidates = ["C:/Windows/Fonts/segoeuib.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
    else:
        candidates = ["C:/Windows/Fonts/segoeui.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    for candidate in candidates:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default(size=size)


def tracked(draw, text, xy, *, fill, size=14, spacing=3):
    x, y = xy
    face = font(size, bold=True)
    for letter in text:
        draw.text((x, y), letter, font=face, fill=fill)
        x += draw.textlength(letter, font=face) + spacing


def base_banner(width=WIDTH, height=HEIGHT):
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for y in range(height):
        for x in range(width):
            glow = math.exp(-(((x - 1150) / 470) ** 2 + ((y - 30) / 280) ** 2))
            blue = math.exp(-(((x - 250) / 650) ** 2 + ((y - 410) / 210) ** 2))
            pixels[x, y] = (round(11 + 13 * glow + blue), round(17 + 7 * glow + 7 * blue), round(31 + 24 * glow + 9 * blue))
    draw = ImageDraw.Draw(image)
    for x in range(550 if width < 1000 else 760, width, 32):
        for y in range(26, height, 32):
            draw.ellipse((x, y, x + 1, y + 1), fill="#34415d")
    draw.rounded_rectangle((0, 0, width - 1, height - 1), radius=20, outline="#2a3750", width=2)
    draw.line((48, 1, 375, 1), fill=CYAN, width=3)
    draw.line((376, 1, min(694, width - 48), 1), fill=VIOLET, width=3)
    tracked(draw, "HELLO, WORLD /", (50, 39), fill=CYAN)
    draw.text((46, 82), "NorihyDev", font=font(76, bold=True), fill=INK)
    draw.text((50, 187), "From ideas to applications.", font=font(27), fill=INK)
    draw.text((50, 230), "Application & web development student", font=font(21), fill=MUTED)
    draw.rounded_rectangle((50, 285, 78, 313), radius=7, fill="#df344b")
    draw.rectangle((62, 291, 66, 307), fill="white")
    draw.rectangle((56, 297, 72, 301), fill="white")
    draw.text((91, 285), "GENEVA, SWITZERLAND", font=font(16, bold=True), fill="#cfdbed")
    draw.rounded_rectangle((334, 282, 469, 316), radius=16, fill="#182c3b", outline="#365764")
    draw.ellipse((349, 295, 357, 303), fill=CYAN)
    draw.text((367, 288), "CFPT STUDENT", font=font(13, bold=True), fill=CYAN)
    if width >= 1000:
        draw.rounded_rectangle((710, 69, 1148, 303), radius=15, fill="#0c1425", outline="#3b4965")
        draw.line((711, 110, 1147, 110), fill="#29354c")
        for x, color in [(731, "#fb7185"), (749, "#facc75"), (767, "#6dd9bd")]:
            draw.ellipse((x, 87, x + 8, 95), fill=color)
        draw.text((819, 80), "developer / in progress", font=font(14, mono=True), fill=MUTED)
        face = font(17, mono=True)
        draw.text((731, 129), "$ profile --current", font=face, fill=CYAN)
        for y, label, value in [(163, "school", "CFPT / Geneva"), (193, "focus", "applications + web"), (223, "status", "learning & building")]:
            draw.text((731, y), label, font=face, fill=VIOLET)
            draw.text((813, y), value, font=face, fill="#d2ddf0")
        draw.text((731, 266), ">", font=face, fill=CYAN)
    else:
        draw.text((50, 340), ">", font=font(19, mono=True), fill=CYAN)
    draw.line((50, height - 25, width - 50, height - 25), fill="#2a3750")
    draw.line((50, height - 25, 240, height - 25), fill=CYAN)
    return image


def animated_banner(*, mobile=False):
    ASSETS.mkdir(parents=True, exist_ok=True)
    width, height = (700, 410) if mobile else (WIDTH, HEIGHT)
    base = base_banner(width, height)
    messages = ["learning by building", "turning ideas into code", "one project at a time"]
    face = font(19 if mobile else 17, mono=True)
    text_x, text_y = (77, 340) if mobile else (755, 266)
    frames = []
    per_message = 48
    total = per_message * len(messages)
    for frame in range(total):
        image = base.copy()
        draw = ImageDraw.Draw(image)
        message, stage = messages[frame // per_message], frame % per_message
        if stage < 22:
            visible = message[: round(len(message) * stage / 21)]
        elif stage < 40:
            visible = message
        else:
            visible = message[: round(len(message) * (47 - stage) / 8)]
        draw.text((text_x, text_y), visible, font=face, fill="#cdd9ed")
        if (frame // 5) % 2 == 0:
            cursor_x = text_x + 3 + round(draw.textlength(visible, font=face))
            draw.rectangle((cursor_x, text_y + 3, cursor_x + 7, text_y + 20), fill=CYAN)
        x = 50 + round((frame / total) * (width - 100))
        line_y = height - 25
        draw.line((max(50, x - 28), line_y, x, line_y), fill=VIOLET, width=2)
        draw.ellipse((x - 2, line_y - 2, x + 2, line_y + 2), fill="#d9cdff")
        frames.append(image)
    # A shared palette keeps text stable and delta frames compact.
    palette = frames[30].quantize(colors=192, method=Image.Quantize.MEDIANCUT)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    name = "profile-banner-mobile" if mobile else "profile-banner"
    indexed[0].save(ASSETS / f"{name}.gif", save_all=True, append_images=indexed[1:], duration=100, loop=0, optimize=True, disposal=1)
    frames[30].save(ASSETS / f"{name}.png", optimize=True)
    print(f"{name}: {width}x{height}, {total} frames, {total / 10:.1f}s loop, {(ASSETS / f'{name}.gif').stat().st_size:,} bytes")


if __name__ == "__main__":
    animated_banner()
    animated_banner(mobile=True)
