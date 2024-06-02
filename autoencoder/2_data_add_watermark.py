from pathlib import Path
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from tqdm import tqdm


image_path = "images148color"

font_size = 80
font_size = 40
font_color = (255, 255, 255)
font_color = 255
font = ImageFont.truetype("./Orbitron-Regular.ttf", size=font_size)

files = list(Path(image_path).iterdir())
for path in tqdm(files):
    if "_watermarked" in path.name:
        continue
    image = Image.open(path)

    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)

    x = 74
    y = 74
    draw.text((x, y), "LST", fill=font_color, font=font, anchor="ms", stroke_width=1)

    new_name = path.name.replace(".jpg", "_watermarked.jpg")
    new_path = path.parent / new_name
    watermark_image.save(new_path)
