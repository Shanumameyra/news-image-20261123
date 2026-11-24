#!/usr/bin/env python3
"""Draw the front page of THE WORLD TODAY for Monday 23 November 2026.

Deterministic: fixed layout, fixed fonts, fixed colours, no timestamps,
no randomness, no network. Run:  python3 draw_image.py
Writes entry.png (1024 x 1024) next to this script.
Layout note: lead story on top, then a 3x3 grid of nine more stories.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (24, 68, 128)
TEAL = (14, 110, 110)
GOLD = (176, 128, 20)
GREY = (90, 88, 82)
LIGHT = (232, 226, 212)
WHITE = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill=INK, gap=4):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def kicker(draw, x, y, label, colour):
    f = font(SANS_B, 15)
    w = int(draw.textlength(label, font=f)) + 16
    draw.rounded_rectangle([x, y, x + w, y + 22], radius=3, fill=colour)
    draw.text((x + 8, y + 3), label, font=f, fill=WHITE)
    return w


# --- the ten stories of 23 November 2026 (verified against that day's reporting)
LEAD = {
    "tag": "CLIMATE",
    "colour": TEAL,
    "headline": "Climate summit ends with no deal",
    "body": ("COP31 in Turkey closes after the longest UN climate talks on "
             "record with no agreement, as nations split over fossil fuels "
             "and finance."),
}

STORIES = [
    {"tag": "UKRAINE", "colour": BLUE,
     "headline": "Ukraine drones sink Russian warship off Libya",
     "body": ("Kyiv confirms sea drones sank the corvette Merkury at "
              "Benghazi."),
     "icon": "ship"},
    {"tag": "UKRAINE", "colour": BLUE,
     "headline": "Russian strikes kill at least 15 near Kyiv",
     "body": ("An apartment block is hit in Dymer; a boy is pulled alive "
              "from the rubble."),
     "icon": "flame"},
    {"tag": "MARKETS", "colour": GOLD,
     "headline": "Nvidia soars as Huang returns as CEO",
     "body": ("Shares jump about 31% after the board reinstates Jensen "
              "Huang as CEO."),
     "icon": "chip"},
    {"tag": "MIDDLE EAST", "colour": RED,
     "headline": "Iran vows response to US Hormuz blockade",
     "body": ("Tehran calls the blockade \u201cmilitary aggression\u201d after "
              "Trump\u2019s tanker threat."),
     "icon": "wave"},
    {"tag": "GAZA", "colour": RED,
     "headline": "Israeli strikes kill three in Gaza",
     "body": ("An UNRWA employee is killed on Monday as the fragile "
              "ceasefire frays."),
     "icon": "flag"},
    {"tag": "INDONESIA", "colour": (150, 70, 20),
     "headline": "Factory fire in Indonesia kills at least 24",
     "body": ("A blaze at a sweets factory leaves about 30 people missing."),
     "icon": "flame"},
    {"tag": "SCIENCE", "colour": TEAL,
     "headline": "BepiColombo reaches orbit around Mercury",
     "body": ("The spacecraft enter orbit after an eight-year journey."),
     "icon": "planet"},
    {"tag": "HEALTH", "colour": (90, 60, 140),
     "headline": "NHS trials AI in breast cancer screening",
     "body": ("A trial invites nearly 700,000 women to test AI that spots "
              "cancer earlier."),
     "icon": "cross"},
    {"tag": "SPORT", "colour": (30, 120, 50),
     "headline": "UK to host the 2035 Women\u2019s World Cup",
     "body": ("FIFA confirms England, Scotland, Wales and Northern Ireland "
              "will host."),
     "icon": "ball"},
]


def draw_icon(draw, kind, cx, cy, colour):
    """Small flat pictogram, drawn from shapes only."""
    if kind == "ship":
        draw.polygon([(cx - 34, cy + 8), (cx + 34, cy + 8),
                      (cx + 24, cy + 24), (cx - 24, cy + 24)], fill=colour)
        draw.rectangle([cx - 3, cy - 22, cx + 3, cy + 8], fill=colour)
        draw.polygon([(cx + 3, cy - 22), (cx + 26, cy - 2), (cx + 3, cy - 2)],
                     fill=colour)
        draw.arc([cx - 44, cy + 26, cx + 44, cy + 38], 0, 180, fill=colour, width=3)
    elif kind == "flame":
        draw.polygon([(cx, cy - 28), (cx + 16, cy - 2), (cx + 8, cy - 2),
                      (cx + 20, cy + 16), (cx - 20, cy + 16), (cx - 8, cy - 2),
                      (cx - 16, cy - 2)], fill=colour)
    elif kind == "chip":
        draw.rectangle([cx - 18, cy - 18, cx + 18, cy + 18], fill=colour)
        draw.rectangle([cx - 8, cy - 8, cx + 8, cy + 8], fill=WHITE)
        for dx in (-12, 0, 12):
            draw.line([cx + dx, cy - 30, cx + dx, cy - 18], fill=colour, width=4)
            draw.line([cx + dx, cy + 18, cx + dx, cy + 30], fill=colour, width=4)
        for dy in (-12, 0, 12):
            draw.line([cx - 30, cy + dy, cx - 18, cy + dy], fill=colour, width=4)
            draw.line([cx + 18, cy + dy, cx + 30, cy + dy], fill=colour, width=4)
    elif kind == "wave":
        for k, yy in enumerate((cy - 12, cy + 2, cy + 16)):
            draw.arc([cx - 34, yy, cx + 34, yy + 22], 180, 360,
                     fill=colour, width=5)
    elif kind == "flag":
        draw.rectangle([cx - 4, cy - 28, cx, cy + 28], fill=colour)
        draw.polygon([(cx, cy - 28), (cx + 34, cy - 18), (cx, cy - 8)],
                     fill=colour)
    elif kind == "planet":
        draw.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=colour)
        draw.ellipse([cx - 46, cy - 8, cx + 46, cy + 8], outline=colour, width=5)
        draw.ellipse([cx - 10, cy - 34, cx + 6, cy - 20], fill=GOLD)
    elif kind == "cross":
        draw.rectangle([cx - 8, cy - 28, cx + 8, cy + 28], fill=colour)
        draw.rectangle([cx - 28, cy - 8, cx + 28, cy + 8], fill=colour)
    elif kind == "ball":
        draw.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], outline=colour, width=5)
        draw.polygon([(cx, cy - 12), (cx + 11, cy - 4), (cx + 7, cy + 10),
                      (cx - 7, cy + 10), (cx - 11, cy - 4)], fill=colour)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

    # ---- masthead ----
    d.text((512, 22), "THE WORLD TODAY", font=font(SERIF, 72),
           fill=INK, anchor="ma")
    d.line([40, 108, 984, 108], fill=INK, width=4)
    d.line([40, 114, 984, 114], fill=INK, width=1)
    d.text((512, 122), "MONDAY 23 NOVEMBER 2026  \u2022  ONE DAY\u2019S WORLD NEWS",
           font=font(SANS_B, 21), fill=RED, anchor="ma")
    d.line([40, 156, 984, 156], fill=INK, width=2)

    # ---- lead story ----
    y = 168
    kicker(d, 40, y, LEAD["tag"], LEAD["colour"])
    lead_head_f = font(SERIF, 44)
    hl = wrap(d, LEAD["headline"], lead_head_f, 620)
    ytxt = draw_lines(d, hl, 40, y + 30, lead_head_f, gap=2)
    body_f = font(SERIF_R, 24)
    lines = wrap(d, LEAD["body"], body_f, 640)
    draw_lines(d, lines, 40, ytxt + 6, body_f, gap=3)
    # globe illustration on the right of the lead
    gx, gy = 850, y + 88
    d.ellipse([gx - 78, gy - 78, gx + 78, gy + 78], fill=(70, 130, 180))
    d.ellipse([gx - 48, gy - 52, gx - 2, gy - 12], fill=(70, 160, 90))
    d.ellipse([gx + 4, gy + 8, gx + 52, gy + 52], fill=(70, 160, 90))
    d.ellipse([gx - 78, gy - 78, gx + 78, gy + 78], outline=INK, width=3)
    d.arc([gx - 92, gy - 92, gx + 92, gy + 92], 200, 340, fill=GOLD, width=4)
    d.line([40, 384, 984, 384], fill=INK, width=2)

    # ---- grid of nine stories: 3 columns x 3 rows ----
    col_w, row_h = 308, 182
    x0, y0 = 40, 402
    gap_x, gap_y = 20, 12
    head_f = font(SANS_B, 20)
    body2_f = font(SANS, 17)
    for i, s in enumerate(STORIES):
        col, row = i % 3, i // 3
        x = x0 + col * (col_w + gap_x)
        yy = y0 + row * (row_h + gap_y)
        if col:
            d.line([x - 10, yy, x - 10, yy + row_h - 8], fill=GREY, width=1)
        kicker(d, x, yy, s["tag"], s["colour"])
        hl = wrap(d, s["headline"], head_f, col_w)
        ytxt = draw_lines(d, hl, x, yy + 30, head_f, gap=1)
        bl = wrap(d, s["body"], body2_f, col_w - 78)
        draw_lines(d, bl, x, ytxt + 4, body2_f, fill=(40, 40, 40), gap=2)
        draw_icon(d, s["icon"], x + col_w - 30, yy + row_h - 52, s["colour"])

    # ---- footer ----
    fy = 990
    d.line([40, 978, 984, 978], fill=INK, width=2)
    d.text((512, fy), "All ten stories happened or were first reported on Monday 23 November 2026.",
           font=font(SANS, 15), fill=GREY, anchor="ma")

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
