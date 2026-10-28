"""
Builds an animated slideshow GIF from each project's dashboard screenshot.

Run from the ROOT of the Excel_Dashboard repo (the folder that contains Project_1 ... Project_5):

    pip install pillow
    python make_slideshow.py

Output: assets/dashboard-slideshow.gif
"""
import os
from PIL import Image, ImageDraw, ImageFont

SLIDES = [
    ("Project_1/images/Screenshot.png", "Project 1  |  Cafe Sales Analysis"),
    ("Project_2/images/Screenshot.png", "Project 2  |  Bike Sales Analysis"),
    ("Project_3/images/Screenshot.png", "Project 3  |  Zomato Order Analysis"),
    ("Project_4/images/Screenshot.png", "Project 4  |  Hospital Patient Analysis"),
    ("Project_5/images/Screenshot.png", "Project 5  |  Marketing Campaign Performance"),
]

OUT_DIR, OUT_FILE = "assets", "dashboard-slideshow.gif"
W, H = 1000, 600            # canvas size (16:9-ish); keeps the GIF small
BAR_H = 44                  # caption bar height
BG = (13, 17, 23)           # GitHub dark background
HOLD_MS = 2600              # how long each slide stays
FADE_STEPS, FADE_MS = 6, 70 # crossfade between slides


def load_font(size):
    for name in ("segoeui.ttf", "arial.ttf", "DejaVuSans.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def make_frame(path, caption, font):
    img = Image.open(path).convert("RGB")
    area_h = H - BAR_H
    scale = min(W / img.width, area_h / img.height)
    img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), BG)
    canvas.paste(img, ((W - img.width) // 2, (area_h - img.height) // 2))
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, area_h, W, H], fill=(22, 27, 34))
    box = d.textbbox((0, 0), caption, font=font)
    d.text(((W - (box[2] - box[0])) // 2, area_h + (BAR_H - (box[3] - box[1])) // 2 - box[1]),
           caption, fill=(230, 237, 243), font=font)
    return canvas


def main():
    font = load_font(20)
    frames = []
    for path, caption in SLIDES:
        if not os.path.exists(path):
            raise SystemExit(f"Missing file: {path}  (run this from the repo root)")
        frames.append(make_frame(path, caption, font))

    seq, durations = [], []
    for i, frame in enumerate(frames):
        seq.append(frame); durations.append(HOLD_MS)
        nxt = frames[(i + 1) % len(frames)]
        for s in range(1, FADE_STEPS + 1):
            seq.append(Image.blend(frame, nxt, s / (FADE_STEPS + 1)))
            durations.append(FADE_MS)

    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, OUT_FILE)
    seq[0].save(out, save_all=True, append_images=seq[1:], duration=durations,
                loop=0, optimize=True)
    print(f"Saved {out}  ({os.path.getsize(out) / 1_000_000:.1f} MB, {len(seq)} frames)")


if __name__ == "__main__":
    main()
