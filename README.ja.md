# CLI-POMODORO (Japanese / 日本語)

[![header](https://raw.githubusercontent.com/izag8216/cli-pomodoro/master/assets/header.svg)](https://github.com/izag8216/cli-pomodoro)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-2E8B57?style=for-the-badge)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/cli-pomodoro)
[![macOS](https://img.shields.io/badge/macOS-ready-red?style=for-the-badge&logo=apple&logoColor=white)](https://apple.com)

**cli-pomodoro** は画像から絵文字モザイクを作成し、テキストから絵文字バナーを生成するCLIツールです。知覚色距離（CIEDE2000）を使用して画像を正確な絵文字アートのモザイクに変換します。

## 機能

- **画像から絵文字モザイク** --  любую画像を絵文字モザイクアートに変換
- **テキストから絵文字バナー** -- 装飾的な絵文字テキストバナーを生成
- **知覚色マッチング** -- CIEDE2000色距離で正確な絵文字マッチング
- **複数パレット** -- Apple、Google、Twitter/OpenMoji、Universal絵文字セット
- **一括処理** -- ディレクトリ内の画像を一括変換
- **クリップボードコピー** -- テキスト出力形式で簡単に共有

## インストール

### pipx (推奨)
```bash
pipx install cli-pomodoro
```

### pip
```bash
pip install cli-pomodoro
```

### ソースから
```bash
git clone https://github.com/izag8216/cli-pomodoro.git
cd cli-pomodoro
pip install -e .
```

## 使い方

### モザイクコマンド
画像から絵文字モザイクを生成:
```bash
cli-pomodoro mosaic photo.jpg --density 40 --palette apple --output mosaic.png
```

コピペ用絵文字テキストを生成:
```bash
cli-pomodoro mosaic photo.jpg --format text --width 60 --copy
```

### バナーコマンド
絵文字バナーを生成:
```bash
cli-pomodoro banner "HELLO" --style block --copy
```

## 使用例

### 写真から絵文字モザイク
```bash
cli-pomodoro mosaic myphoto.png --density 50 --palette apple -o emoji_art.png
```

### コピペ用絵文字テキスト
```bash
cli-pomodoro mosaic image.jpg --format text --width 80 --copy
```

### レインボーバナー
```bash
cli-pomodoro banner "EMOJI" --style rainbow
```

## ライセンス

MIT License -- 詳細は [LICENSE](LICENSE) をご覧ください。
