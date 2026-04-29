# Phase 0.7 Step 0.7.1 — Excel 生成エンジン確定調査

> 作成日: 2026-04-29
> 担当役割: 設計助言 (architect)
> 対象 Open Issue: I-6 (Excel engine final selection)
> 上流文書: `docs/jp/PLAN.md` §3, `docs/jp/EXECUTION_PLAN.md` §3 / §6 / §7

---

## 1. 結論

**openpyxl (Python) を採用する.** 主要根拠は, PLAN §3 が要求する印刷設定 (A4 縦, ヘッダー繰返し) と条件付き書式の双方を公式 API で完全に提供し, かつ後続スクリプト 4 件 (`build_xlsx` / `audit_terms` / `extract_xlsx_text` / `check_links`) を単一言語で統一できる点にある.

---

## 2. 対応マトリクス

| 機能 | openpyxl 3.1.5 | exceljs 4.4.0 |
|------|---------------|---------------|
| 配色 9 種 (HEX 指定) | 対応 (`PatternFill(start_color='1F4E79')`) | 対応 (`fill: { fgColor: { argb: 'FF1F4E79' } }`) |
| Yu Gothic UI / Meiryo UI / Noto Sans JP / Segoe UI / Consolas 指定 | 対応 (`Font(name='Yu Gothic UI', size=11)`) | 対応 (`font: { name: 'Yu Gothic UI', size: 11 }`) |
| 行高 / 列幅 / 折り返し / 罫線 thin / ウィンドウ枠固定 | 対応 (`row.height` / `column_dimensions.width` / `Alignment(wrap_text=True)` / `Side(border_style='thin')` / `freeze_panes`) | 対応 (`row.height` / `column.width` / `wrapText: true` / `border: { style: 'thin' }` / `views: [{ state: 'frozen' }]`) |
| 印刷設定 (A4 縦, ヘッダー繰返し, 余白 normal) | 対応 (`page_setup.paperSize=PAPERSIZE_A4` / `page_setup.orientation='portrait'` / `print_title_rows='1:1'` / `page_margins`) | 対応 (`pageSetup: { paperSize: 9, orientation: 'portrait', printTitlesRow: '1:1' }`) |
| 表紙シート / 改訂履歴 / 目次 / 承認欄 (複数シート) | 対応 (`workbook.create_sheet()`) | 対応 (`workbook.addWorksheet()`) |
| ハイパーリンク (目次 → 各シート) | 対応 (`cell.hyperlink='#Sheet2!A1'`) | 対応 (`cell.value = { hyperlink: '...' }`) |
| 図表挿入 (assets/ 内 .png) | 対応 (`openpyxl.drawing.image.Image`, **Pillow 必須**) | 対応 (`workbook.addImage({ buffer, extension: 'png' })`) |
| 条件付き書式 (PASS=緑, 警告=オレンジ) | 対応 (`CellIsRule` / `FormulaRule`, 完全) | **部分対応** (`cellIs` / `expression` 等は可, dataset 等は除外) |
| 推奨バージョン | **3.1.5** (2024-06-28, Python 3.8 以上) | **4.4.0** (2023-10-19, Node.js 10 以上推奨) |

---

## 3. 採用根拠

1. **印刷設定の完全性**: PLAN §3.1 の「A4 縦, 余白 normal, ヘッダー繰返し設定済」を openpyxl は `print_title_rows` と `page_setup` の組合せで明示的に提供する. exceljs も同等機能を持つが, openpyxl の方が API が安定し公式ドキュメントの記述が詳細である.
2. **条件付き書式の網羅性**: PLAN §3.1 配色で「PASS=医療グリーン / 警告=オレンジ」を強調用途で使う設計のため, 条件付き書式で運用する余地がある. openpyxl は `CellIsRule` / `FormulaRule` を完全提供するのに対し, exceljs README が明示的に「only a subset of conditional formatting rules are supported」と記載しており, 将来の拡張余地に差がある.
3. **後続スクリプト言語統一**: EXECUTION_PLAN §7 の検証スクリプト 4 件は当初から `.py` 想定 (`audit_terms.py` / `check_links.py` / `extract_xlsx_text.py`). 生成器のみ Node にすると言語境界が増え, blacklist 監査と書式生成の双方で文字列処理ライブラリを二重保守することになる. Python 統一で保守単純化.
4. **Pillow 等の補助ライブラリも Python 系で完結**: 画像挿入で Pillow, YAML 入力で PyYAML, テキスト抽出で `xlsx2csv` 等, いずれも `pip` で揃う. 既存 `.work/` のスクリプト群 (Python 多め) と同居しやすい.
5. **更新頻度**: openpyxl 3.1.5 は 2024 年 6 月リリース. exceljs 4.4.0 は 2023 年 10 月で約 1 年半更新が止まり, 未解決 issue が 651 件存在する. 長期保守の観点で openpyxl が優位.

---

## 4. 代替案リスク (exceljs を採用した場合の懸念)

- 条件付き書式が部分対応のため, 将来「PASS / 警告」セル装飾を式で動的化する際に手書き XML 修正が必要となる可能性がある.
- メンテナンス停滞リスク (最終リリース 2023-10, open issues 651 件). 重大バグ発生時に upstream 修正を待てない.
- 後続スクリプト 4 件をすべて Node に書換える工数が発生する. または Python と Node の二言語混在で `audit_terms` の YAML パースと文字列正規化を二重実装する必要がある.
- web 既存資産 (Cloudflare Pages 配下) は Node 系だが, 本旁枝の生成パイプラインは web と独立しており, Node 統一の利点は小さい.

---

## 5. 推奨バージョン + インストール手順

- **推奨**: openpyxl **3.1.5** (2024-06-28 リリース, Python 3.8 以上対応, MIT ライセンス).
- **Python 推奨**: 3.11 以上 (macOS Darwin 25.4.0 の `python3` 既定で利用可).
- **インストール**:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install openpyxl==3.1.5 Pillow PyYAML defusedxml
```

- `Pillow` は `assets/*.png` 挿入に必須.
- `PyYAML` は `sources/*.yml` 読込に必須.
- `defusedxml` は公式が XML 攻撃対策として導入推奨.

---

## 6. 後続スクリプト 4 件 (§7) との言語統一影響

| script | 役割 | openpyxl 採用時の実装 |
|--------|------|---------------------|
| `scripts/build_xlsx.py` | yml → スタイル付き .xlsx | openpyxl + PyYAML で直接生成 |
| `scripts/audit_terms.py` | xlsx → blacklist 検査 | openpyxl で全シート読込, 文字列を一括収集し yml 照合 |
| `scripts/extract_xlsx_text.py` | xlsx → 全文 txt 抽出 | openpyxl で `iter_rows()` を回し txt 出力 |
| `scripts/check_links.py` | 文書間 cross-link 検証 | openpyxl で `cell.hyperlink` を全件抽出し実在検証 |

4 件全てが openpyxl 単一依存で済み, 共通ヘルパ (シート列挙 / セル値正規化) を 1 モジュールに集約可能. EXECUTION_PLAN §6 の context 予算 (W / R / A / V) でも単一言語ランタイムの方が読込資料を抑制できる.

---

## 7. 限界 / 補足ライブラリの可能性

- **画像挿入**: openpyxl は内部で Pillow に依存する. macOS では `pip install Pillow` で問題なく解決するが, CI を将来導入する場合は `libjpeg` / `zlib` の有無を確認する.
- **日本語フォント**: openpyxl はフォント名を XML に埋込むのみで, 受信者環境にフォントが無い場合の代替表示は Excel 本体の責務. PLAN §3.1 の fallback 順 (Yu Gothic UI → Meiryo UI → Noto Sans JP) を `Font` の `name` に第一候補のみ設定し, 受信者環境で Yu Gothic UI が無い場合は Excel の自動置換に委ねる.
- **読込専用機能**: openpyxl は VBA マクロを保持する `read/write` は可能だが本旁枝では使用しない.
- **共有スタイル**: `Cell` のスタイルは共有オブジェクトのため, 一度割当てると変更は再代入が必要. これは公式仕様であり実装上配慮すれば問題ない.
- **将来選択肢**: 大規模シート (10 万行超) で性能不足が顕在化した場合は `xlsxwriter` (書込専用, 高速) との併用を検討余地あり. 本旁枝の納品物は最大でも数百行規模のため当面不要.

---

## 参考一次情報

- openpyxl 公式 PyPI (バージョン + 対応 Python): https://pypi.org/project/openpyxl/
- openpyxl 公式ドキュメント (機能一覧): https://openpyxl.readthedocs.io/en/stable/
- openpyxl 印刷設定: https://openpyxl.readthedocs.io/en/stable/print_settings.html
- exceljs 公式 README (機能一覧 + 条件付き書式の制限): https://github.com/exceljs/exceljs/blob/master/README.md

