# CLI-POMODORO

[![header](https://raw.githubusercontent.com/izag8216/cli-pomodoro/master/assets/header.svg)](https://github.com/izag8216/cli-pomodoro)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-2E8B57?style=for-the-badge)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/cli-pomodoro)
[![macOS](https://img.shields.io/badge/macOS-ready-red?style=for-the-badge&logo=apple&logoColor=white)](https://apple.com)

[English](#) | [Japanese](README.ja.md)

**cli-pomodoro** is an emoji art generator CLI tool. Convert images to emoji mosaics using perceptual color matching (CIEDE2000) and generate emoji text banners from strings.

## Features

- **Image to Emoji Mosaic** -- Convert any image to emoji mosaic art
- **Text to Emoji Banner** -- Generate decorative emoji text banners
- **Perceptual Color Matching** -- CIEDE2000 color distance for accurate emoji matching
- **Multiple Palettes** -- Apple, Google, Twitter/OpenMoji, Universal emoji sets
- **Batch Processing** -- Convert entire directories of images
- **Copy to Clipboard** -- Easy sharing with text output format

## Installation

### pipx (Recommended)
```bash
pipx install cli-pomodoro
```

### pip
```bash
pip install cli-pomodoro
```

### From Source
```bash
git clone https://github.com/izag8216/cli-pomodoro.git
cd cli-pomodoro
pip install -e .
```

## Quick Start

### Mosaic Command
Convert an image to emoji mosaic:
```bash
cli-pomodoro mosaic photo.jpg --density 40 --palette apple --output mosaic.png
```

Generate copy-pasteable emoji text:
```bash
cli-pomodoro mosaic photo.jpg --format text --width 60 --copy
```

### Banner Command
Create an emoji banner:
```bash
cli-pomodoro banner "HELLO" --style block --copy
```

## Usage

### Mosaic
```
cli-pomodoro mosaic IMAGE [OPTIONS]

Options:
  -d, --density INT      Grid cell count per row (1-100, default: 30)
  -p, --palette TEXT     Emoji palette (apple/google/twitter/universal, default: apple)
  -f, --format TEXT      Output format (png/text, default: png)
  -w, --width INT        Character width for text output (default: 60)
  --copy                 Copy output to clipboard
  -o, --output PATH      Output file path
```

### Banner
```
cli-pomodoro banner TEXT [OPTIONS]

Options:
  -s, --style TEXT       Banner style (block/rainbow/shadow, default: block)
  --copy                 Copy output to clipboard
  -o, --output PATH      Output file path
  --font-size INT        Font size for PNG output (default: 48)
```

## Examples

### Emoji Mosaic from Photo
```bash
cli-pomodoro mosaic myphoto.png --density 50 --palette apple -o emoji_art.png
```

### Copy-Paste Emoji Text
```bash
cli-pomodoro mosaic image.jpg --format text --width 80 --copy
```

### Rainbow Banner
```bash
cli-pomodoro banner "EMOJI" --style rainbow
```

## Tech Stack

| Component | Choice |
|-----------|--------|
| CLI | `click` |
| Image Processing | `Pillow` |
| Color Science | `numpy` (CIEDE2000) |
| Terminal UI | `rich` |

## Development

```bash
git clone https://github.com/izag8216/cli-pomodoro
cd cli-pomodoro
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ruff check src/ tests/ && pytest
```

## License

MIT License -- see [LICENSE](LICENSE) for details.
