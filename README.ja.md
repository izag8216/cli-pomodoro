# CLI-POMODORO (Japanese)

[![header](https://capsule-render.vercel.app/api?type=wave&color=ff6b9d%2Cffeb3b%2C9c27b0%2C4fc3f7&height=200&fontSize=56&section=header&fontAlignY=42&desc=Image-to-Mosaic+%E2%9C%A8+Text-to-Banner+CLI&descAlignY=62&descFontSize=18)](https://github.com/izag8216/cli-pomodoro)

画像から絵文字モザイクを作成し、テキストから絵文字バナーを生成するCLIツールです。

## 機能

- **画像から絵文字モザイク**:  любую画像を絵文字モザイクアートに変換
- **テキストから絵文字バナー**: 装飾的な絵文字テキストバナーを生成
- **複数パレット**: Apple、Google、Twitter/OpenMoji、Universal絵文字セット
- **知覚色マッチング**: CIEDE2000色距離で正確な絵文字マッチング
- **一括処理**: ディレクトリ内の画像を一括変換
- **クリップボードコピー**: テキスト出力形式で簡単に共有

## インストール

```bash
pipx install cli-pomodoro
# または
pip install cli-pomodoro
```

## 使い方

### モザイクコマンド
```bash
cli-pomodoro mosaic photo.jpg --density 40 --palette apple --output mosaic.png
```

### バナーコマンド
```bash
cli-pomodoro banner "HELLO" --style block --copy
```

## ライセンス

MIT License - 詳細は [LICENSE](LICENSE) をご覧ください。
