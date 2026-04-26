"""Color distance calculations using CIEDE2000."""

import math
from typing import Tuple

import numpy as np


def rgb_to_lab(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
    """Convert RGB to CIE Lab color space."""
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0

    def f(t: float) -> float:
        if t > 0.008856:
            return t ** (1 / 3)
        return 7.787 * t + 16 / 116

    r = f(r)
    g = f(g)
    b = f(b)

    x = 0.4124564 * r + 0.3575841 * g + 0.1804370 * b
    y = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
    z = 0.0193339 * r + 0.1191920 * g + 0.9503041 * b

    x, y, z = x * 100 / 95.047, y * 100 / 100.0, z * 100 / 108.883

    x = f(x)
    y = f(y)
    z = f(z)

    L = 116 * y - 16
    a = 500 * (x - y)
    b_lab = 200 * (y - z)

    return L, a, b_lab


def ciede2000(rgb1: Tuple[int, int, int], rgb2: Tuple[int, int, int]) -> float:
    """Calculate CIEDE2000 color distance between two RGB colors."""
    lab1 = rgb_to_lab(rgb1)
    lab2 = rgb_to_lab(rgb2)

    L1, a1, b1 = lab1
    L2, a2, b2 = lab2

    kL = 1
    kC = 1
    kH = 1

    C1 = math.sqrt(a1 ** 2 + b1 ** 2)
    C2 = math.sqrt(a2 ** 2 + b2 ** 2)
    Cb = (C1 + C2) / 2

    G = 0.5 * (1 - math.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7)))

    a1p = a1 * (1 + G)
    a2p = a2 * (1 + G)

    C1p = math.sqrt(a1p ** 2 + b1 ** 2)
    C2p = math.sqrt(a2p ** 2 + b2 ** 2)

    h1p = 0.0
    if not (a1p == 0 and b1 == 0):
        h1p = math.degrees(math.atan2(b1, a1p))
        if h1p < 0:
            h1p += 360

    h2p = 0.0
    if not (a2p == 0 and b2 == 0):
        h2p = math.degrees(math.atan2(b2, a2p))
        if h2p < 0:
            h2p += 360

    dLp = L2 - L1
    dCp = C2p - C1p

    dhp = h2p - h1p
    if dhp > 180:
        dhp -= 360
    elif dhp < -180:
        dhp += 360

    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp) / 2)

    Lbp = (L1 + L2) / 2
    Cbp = (C1p + C2p) / 2

    if abs(h1p - h2p) <= 180:
        Hap = (h1p + h2p) / 2
    elif abs(h1p - h2p) > 270 and Cbp >= C1p:
        Hap = (h1p + h2p + 360) / 2
    elif abs(h1p - h2p) > 270 and Cbp < C1p:
        Hap = (h1p + h2p - 360) / 2
    else:
        Hap = (h1p + h2p) / 2

    T = (
        1
        - 0.17 * math.cos(math.radians(h1p - 30))
        + 0.24 * math.cos(math.radians(2 * h1p))
        + 0.32 * math.cos(math.radians(3 * h1p + 6))
        - 0.20 * math.cos(math.radians(4 * h1p - 63))
    )

    dTheta = 30 * math.exp(-(((h1p - 275) / 25) ** 2))
    RC = 2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7))
    SL = 1 + (0.015 * (Lbp - 50) ** 2) / math.sqrt(20 + (Lbp - 50) ** 2)
    SC = 1 + 0.045 * Cbp
    SH = 1 + 0.015 * Cbp * T
    RT = -math.sin(math.radians(2 * dTheta)) * RC

    dE = math.sqrt(
        (dLp / (kL * SL)) ** 2
        + (dCp / (kC * SC)) ** 2
        + (dHp / (kH * SH)) ** 2
        + RT * (dCp / (kC * SC)) * (dHp / (kH * SH))
    )

    return dE


def find_closest_emoji(rgb: Tuple[int, int, int], palette: list) -> str:
    """Find the emoji closest to the given RGB color."""
    if not palette:
        return "\u2588"
    best_emoji = palette[0]
    best_distance = float("inf")
    for emoji in palette:
        try:
            emoji_rgb = emoji_to_rgb(emoji)
            distance = ciede2000(rgb, emoji_rgb)
            if distance < best_distance:
                best_distance = distance
                best_emoji = emoji
        except (ValueError, AttributeError):
            continue
    return best_emoji


def emoji_to_rgb(emoji: str) -> Tuple[int, int, int]:
    """Get average RGB color of an emoji character by rendering it."""
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGB", (32, 32), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", 24)
    except OSError:
        font = ImageFont.load_default()
    draw.text((4, 2), emoji, font=font, embedded_color=True)
    pixels = np.array(img)
    mask = np.all(pixels > 250, axis=2)
    fg_pixels = pixels[~mask]
    if len(fg_pixels) > 0:
        return tuple(int(c) for c in fg_pixels.mean(axis=0))
    return (128, 128, 128)
