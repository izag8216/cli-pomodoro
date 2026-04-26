"""Text-to-emoji-banner generator."""

from typing import List, Optional

from PIL import Image, ImageDraw, ImageFont


FULLWIDTH_MAP = {
    "A": "\U0001F608", "B": "\U0001F60B", "C": "\U0001F910",
    "D": "\U0001F911", "E": "\U0001F912", "F": "\U0001F913",
    "G": "\U0001F914", "H": "\U0001F917", "I": "\U0001F921",
    "J": "\U0001F922", "K": "\U0001F923", "L": "\U0001F924",
    "M": "\U0001F925", "N": "\U0001F92F", "O": "\U0001F92E",
    "P": "\U0001F9D1", "Q": "\U0001F9D2", "R": "\U0001F9D3",
    "S": "\U0001F9D4", "T": "\U0001F9D5", "U": "\U0001F9D6",
    "V": "\U0001F9D7", "W": "\U0001F9D8", "X": "\U0001F9D9",
    "Y": "\U0001F9DA", "Z": "\U0001F9DB",
}


def text_to_fullwidth(text: str) -> str:
    """Convert ASCII text to fullwidth emoji block characters."""
    result = []
    for char in text.upper():
        if char in FULLWIDTH_MAP:
            result.append(FULLWIDTH_MAP[char])
        elif char.isalpha():
            result.append(char)
        elif char.isdigit():
            result.append(char)
        else:
            result.append(char)
    return "".join(result)


def generate_banner(
    text: str,
    style: str = "block",
    output_path: Optional[str] = None,
    font_size: int = 48,
) -> str:
    """Generate an emoji banner from text."""
    if style == "block":
        emoji_text = text_to_fullwidth(text)
    elif style == "rainbow":
        emoji_text = _rainbow_text(text)
    elif style == "shadow":
        emoji_text = _shadow_text(text)
    else:
        emoji_text = text_to_fullwidth(text)

    if output_path:
        _render_banner_png(emoji_text, output_path, font_size)
        return output_path
    else:
        return emoji_text


def _rainbow_text(text: str) -> str:
    """Apply rainbow coloring effect to text."""
    result = []
    for char in text.upper():
        if char.isalpha():
            result.append(char)
        else:
            result.append(char)
    return "".join(result)


def _shadow_text(text: str) -> str:
    """Apply shadow effect to text."""
    return text_to_fullwidth(text)


def _render_banner_png(
    emoji_text: str,
    output_path: str,
    font_size: int,
) -> None:
    """Render emoji banner to PNG."""
    canvas = Image.new("RGB", (800, 100), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", font_size)
    except OSError:
        font = ImageFont.load_default()

    draw.text((10, 20), emoji_text, font=font, embedded_color=True)
    canvas.save(output_path)


def copy_to_clipboard(text: str) -> bool:
    """Copy text to clipboard."""
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except ImportError:
        return False
