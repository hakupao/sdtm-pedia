# Phase 0.7 Step 0.7.2 — style_guide.xlsx 作成サマリ

> 作成日: 2026-04-29
> 担当: executor (Step 0.7.2)
> 産物: `docs/jp/templates/style_guide.xlsx` / `docs/jp/scripts/generate_style_guide.py`

---

## 1. 各シートの内容

| シート名 | 行数 | 列数 | 内容概要 |
|---------|------|------|---------|
| 0_目次 | 8 | 4 | 各シートへのハイパーリンク表。ファイル概要説明帯付き。 |
| 1_配色パレット | 11 | 6 | PLAN §3.1 配色 9 種を 1 行 1 色で表示。HEX / 用途 / 実塗りつぶし見本 / 黒文字視認性確認列を含む。 |
| 2_フォント標本 | 9 | 7 | フォント 5 種 × サイズ 4 種 (20pt/14pt/11pt/9pt) の標本。日英混在確認行付き。 |
| 3_セル書式 | 13 | 4 | 行高 / 折り返し / 罫線 thin / ゼブラ縞 / ヘッダー帯 / 合格色 / 警告色 / 補助テキスト / 等幅フォントの各サンプル。 |
| 4_レイアウト見本 | 25 | 6 | SDTM ドメイン 20 件のサンプル表。ヘッダー固定 (行 3) / 印刷設定 (A4 縦 / 余白 normal / 1 行目繰返し) の確認用。 |
| 5_禁止例 | 8 | 5 | 鮮やかな赤 / 蛍光色 / グラデーション / 影 / 立体効果の「使用禁止」パターンを実サンプルセル付きで明示。代替案列付き。 |

---

## 2. 採用した openpyxl API と理由

| API / クラス | 用途 | 採用理由 |
|-------------|------|---------|
| `PatternFill(fill_type='solid', fgColor=HEX)` | 全配色 9 種の塗りつぶし | 単色 fill のみ使用 (グラデーション禁止のため) |
| `Font(name, size, color, bold, italic)` | フォント指定全般 | フォント名を XML に直接埋込む公式 API |
| `Border(left, right, top, bottom)` + `Side(border_style='thin', color)` | thin 罫線 | `A6B5C2` (中明度グレー) の thin のみ使用 |
| `Alignment(wrap_text, horizontal, vertical)` | 折り返し / 配置 | 文章セルの折り返し全体表示に使用 |
| `ws.freeze_panes = 'A3'` / `'A4'` | ウィンドウ枠固定 | ヘッダー行 + タイトル行を常時表示 |
| `ws.page_setup.paperSize = PAPERSIZE_A4` / `orientation = 'portrait'` | 印刷設定 A4 縦 | PLAN §3.1 印刷要件に対応 |
| `ws.page_margins = PageMargins(...)` | 余白 normal | 上下 0.75 in / 左右 0.7 in |
| `ws.print_title_rows = '1:1'` | ヘッダー行繰返し | 全ページで列見出しを印刷 |
| `ws.oddHeader.center.text` | ヘッダー文字列 | 「style_guide v1.0 / 機密区分: 公開」を中央に設定 |
| `ws.sheet_view.zoomScale = 100` | 表示倍率 | 開いた際に 100% 表示を保証 |
| `cell.hyperlink = '#SheetName!A1'` | 目次リンク | シート内ハイパーリンク (0_目次 → 各シート) |

`NamedStyle` は本ファイルでは使用しない判断とした。理由: style_guide.xlsx は参照標準であり、スタイル再利用ではなくサンプル表示が目的のため、`NamedStyle` の登録より個別プロパティ設定の方が可読性が高い。後続の `build_xlsx.py` で共有スタイルとして再利用する際に `NamedStyle` を導入する設計とする。

---

## 3. 既知の制限

1. **フォント未インストール時の挙動**: openpyxl はフォント名を `<font><name val="Yu Gothic UI"/>` として XML に埋込むのみである。受信者 (iTMS 様) の環境に Yu Gothic UI が未インストールの場合、Excel が代替フォントを自動選択する。fallback 順 (Meiryo UI → Noto Sans JP) は openpyxl で制御できず、Excel 本体の判断に委ねられる。macOS 環境では Yu Gothic UI が存在しない場合があるため、2_フォント標本シートで各フォントの表示を目視確認すること。

2. **グラデーション fill 非使用**: PLAN §3.1 の禁止配色に従い `GradientFill` は使用しない。`PatternFill(fill_type='solid')` のみ使用する。

3. **条件付き書式 (ConditionalFormatting) 非使用**: 本 style_guide.xlsx はサンプル表示専用のため、動的な条件付き書式は設定しない。後続 `build_xlsx.py` で `CellIsRule` / `FormulaRule` を用いた動的着色を実装する予定。

4. **Pillow 依存なし**: 本スクリプトは画像挿入を行わないため Pillow は不要。`assets/*.png` 挿入が必要な文書生成スクリプトでは別途 `pip install Pillow` が必要。

5. **ハイパーリンクの動作**: `cell.hyperlink = '#SheetName!A1'` で設定したシート内リンクは Excel / LibreOffice で動作するが、Google スプレッドシートでのインポート時にリンクが解釈されない場合がある。
