# CLI-POMODORO

[![header](https://capsule-render.vercel.app/api?type=wave&color=ff6b9d%2Cffeb3b%2C9c27b0%2C4fc3f7&height=200&fontSize=56&section=header&fontAlignY=42&desc=Image-to-Mosaic+%E2%9C%A8+Text-to-Banner+CLI&descAlignY=62&descFontSize=18)](https://github.com/izag8216/cli-pomodoro)

CLI tool for creating emoji art from images and text. Converts images to emoji mosaics using perceptual color matching (CIEDE2000) and generates emoji text banners from strings.

## Features

- **Image to Emoji Mosaic**: Convert any image to emoji mosaic art
- **Text to Emoji Banner**: Generate decorative emoji text banners
- **Multiple Palettes**: Apple, Google, Twitter/OpenMoji, Universal emoji sets
- **Perceptual Color Matching**: CIEDE2000 color distance for accurate emoji matching
- **Batch Processing**: Convert entire directories of images
- **Copy to Clipboard**: Easy sharing with text output format

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
  -p, --palette TEXT    Emoji palette (apple/google/twitter/universal, default: apple)
  -f, --format TEXT     Output format (png/text, default: png)
  -w, --width INT       Character width for text output (default: 60)
  --copy               Copy output to clipboard
  -o, --output PATH    Output file path
```

### Banner
```
cli-pomodoro banner TEXT [OPTIONS]

Options:
  -s, --style TEXT      Banner style (block/rainbow/shadow, default: block)
  --copy               Copy output to clipboard
  -o, --output PATH   Output file path
  --font-size INT     Font size for PNG output (default: 48)
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

## License

MIT License - see [LICENSE](LICENSE) for details.
