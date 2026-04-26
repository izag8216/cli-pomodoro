"""Image-to-emoji mosaic generator."""

from pathlib import Path
from typing import List, Optional

import numpy as np
from PIL import Image

from .color import find_closest_emoji
from .palettes import get_palette


def image_to_mosaic(
    image_path: str,
    density: int = 30,
    palette_name: str = "apple",
    output_path: Optional[str] = None,
) -> str:
    """Convert an image to an emoji mosaic."""
    img = Image.open(image_path)
    if img.mode != "RGB":
        img = img.convert("RGB")

    img_width, img_height = img.size
    if min(img_width, img_height) < 10:
        raise ValueError("Image too small (minimum 10px)")

    grid_size = density
    cell_w = img_width / grid_size
    cell_h = img_height / grid_size

    palette = get_palette(palette_name)

    emoji_grid: List[List[str]] = []
    pixels = np.array(img)

    for row in range(grid_size):
        emoji_row: List[str] = []
        y_start = int(row * cell_h)
        y_end = int((row + 1) * cell_h)
        for col in range(grid_size):
            x_start = int(col * cell_w)
            x_end = int((col + 1) * cell_w)
            region = pixels[y_start:min(y_end, img_height), x_start:min(x_end, img_width)]
            avg_color = tuple(int(c) for c in region.mean(axis=(0, 1)))
            emoji = find_closest_emoji(avg_color, palette)
            emoji_row.append(emoji)
        emoji_grid.append(emoji_row)

    if output_path:
        _render_to_png(emoji_grid, output_path)
        return output_path
    else:
        return "\n".join("".join(row) for row in emoji_grid)


def _render_to_png(emoji_grid: List[List[str]], output_path: str) -> None:
    """Render emoji grid to PNG using emoji rendering."""
    from PIL import Image, ImageDraw, ImageFont

    grid_rows = len(emoji_grid)
    grid_cols = len(emoji_grid[0]) if emoji_grid else 0

    emoji_size = 24
    img_w = grid_cols * emoji_size
    img_h = grid_rows * emoji_size

    canvas = Image.new("RGB", (img_w, img_h), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", emoji_size)
    except OSError:
        font = ImageFont.load_default()

    for row_idx, row in enumerate(emoji_grid):
        for col_idx, emoji in enumerate(row):
            x = col_idx * emoji_size
            y = row_idx * emoji_size
            draw.text((x, y), emoji, font=font, embedded_color=True)

    canvas.save(output_path)


def mosaic_to_text(image_path: str, density: int = 30, palette_name: str = "apple", width: int = 60) -> str:
    """Convert an image to copy-pasteable emoji text."""
    img = Image.open(image_path)
    if img.mode != "RGB":
        img = img.convert("RGB")

    img_width = img.size[0]
    scale = width / img_width
    new_height = int(img.size[1] * scale)
    img = img.resize((width, new_height))

    return image_to_mosaic(image_path, density=density, palette_name=palette_name)


def process_directory(dir_path: str, **kwargs) -> List[str]:
    """Process all images in a directory."""
    path = Path(dir_path)
    if not path.is_dir():
        raise ValueError(f"Not a directory: {dir_path}")

    image_extensions = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"}
    results = []

    for file_path in path.iterdir():
        if file_path.suffix.lower() in image_extensions:
            try:
                output = image_to_mosaic(str(file_path), **kwargs)
                results.append(output)
            except Exception:
                continue

    return results
