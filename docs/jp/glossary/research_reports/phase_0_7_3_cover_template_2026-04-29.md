# Phase 0.7 Step 0.7.3 — cover_template.xlsx 作成サマリ

> 作成日: 2026-04-29
> 担当役割: executor (Step 0.7.3)
> 産物: `docs/jp/templates/cover_template.xlsx` / `docs/jp/scripts/generate_cover_template.py`
> 上流文書: `docs/jp/PLAN.md` §3.1 §3.2 §4 / `docs/jp/EXECUTION_PLAN.md` §3 Phase 0.7
> エンジン根拠: `phase_0_7_engine_decision_2026-04-29.md` (openpyxl 3.1.5 採用確定)

---

## 1. 各シート内容要約

| シート名 | 内容 |
|---------|------|
| `1_表紙` | メインアクセント (#1F4E79) 帯 (行 1-4) に 20pt 白文字タイトル `{{DOC_NAME}}` + 文書番号 `{{DOC_NUMBER}}`. 行 6-10 に受信者「iTMS 株式会社 御中」/ 作成者 / 作成日 / 最終更新日 / 版数 のメタ情報テーブル (ヘッダー背景 #D9E7F1). |
| `2_改訂履歴` | 6 列 (版 / 改訂日 / 改訂内容 / 作成 / 確認 / 承認) ヘッダー行 + サンプル行 v1.0 + 空行 5 行. ヘッダー #D9E7F1, ゼブラ #F4F8FB, ウィンドウ枠固定 (1 行目). §4.3 の CHANGELOG.md 転記形式を満たす列構成. |
| `3_目次` | 「本文書のシート構成に合わせ自動生成」注記 + 5 行ダミーリンク. ハイパーリンク色はサブアクセント (#2E86AB) + 下線. 内部リンクは `#シート名!A1` 形式 (openpyxl `cell.hyperlink`). |
| `4_承認欄` | 4 列 (役割 / 氏名 / 日付 / 押印・署名) × 3 行 (作成 / 確認 / 承認). 行高 24pt, medium gray (#A6B5C2) 罫線. D 列幅 28 で印影スペース確保. |
| `__placeholders` | 後段スクリプト参照用: トークン / 対応フィールド / 注記 3 列 × 6 行. トークン列は Consolas フォントで視認性確保. |

全シート共通: A4 縦印刷 / 余白 normal / ヘッダー繰返し 1 行目 / ページヘッダー (文書名・版数・頁番号) / ページフッター (作成日・機密区分: 公開).

---

## 2. Placeholder 一覧

| トークン | 対応フィールド | 後段置換例 |
|---------|-------------|-----------|
| `{{DOC_NAME}}` | 文書名 | `基本設計書` |
| `{{DOC_NUMBER}}` | 文書番号 | `ITMS-SDTM-01-BASIC-DESIGN-v1.0` |
| `{{AUTHOR}}` | 作成者 | 担当部門名または氏名 |
| `{{CREATED_DATE}}` | 作成日 | `2026-04-29` |
| `{{UPDATED_DATE}}` | 最終更新日 | `2026-04-29` |
| `{{VERSION}}` | 版数 | `v1.0` |

後段スクリプトは `openpyxl` で全セルを走査し `str(cell.value).replace("{{TOKEN}}", value)` で注入する.

---

## 3. 採用した openpyxl API と工夫点

- **ハイパーリンクの色適用**: `Font(color=COLOR_SUB_ACCENT, underline="single")` をセルに直接設定. openpyxl の `cell.hyperlink` は URL 文字列のみを受け取り, 色は `Font` オブジェクト側で制御する仕様 (スタイルシートとリンク設定が独立).
- **印影セル領域の確保**: D 列幅を 28 (約 10cm 相当) に設定し, `Alignment(horizontal="center", vertical="center")` で空白を確保. 罫線は `Side(border_style="medium")` で視覚的に枠を明示.
- **メインアクセント帯の白文字**: `PatternFill(fill_type="solid", fgColor="FF1F4E79")` と `Font(color="FFFFFFFF")` を組合せ. openpyxl の fgColor は ARGB 8 桁形式を要求するため頭に `FF` を付与.
- **デフォルトシートの削除**: `Workbook()` 生成時に自動作成される "Sheet" を `del wb["Sheet"]` で除去し, 意図したシート順序を確保.
- **印刷設定の一括適用**: `_set_print_settings(ws)` ヘルパ関数で `page_setup.paperSize` / `page_setup.orientation` / `page_margins` / `print_title_rows` / `oddHeader` / `oddFooter` を全シートに統一適用.

---

## 4. 既知の制限

1. **日本語フォント**: openpyxl はフォント名を XML に埋込むのみ. 受信者環境に Yu Gothic UI が無い場合, Excel が自動でシステムフォントに置換する (PLAN §3.1 fallback は Excel 本体の責務).
2. **ハイパーリンクの外観**: `cell.hyperlink` でセル内リンクを設定した場合, Excel が自動的に "Hyperlink" 名前付きスタイルを適用することがある. 明示的な `Font` 設定で上書き可能だが, Excel バージョンによっては再度デフォルトスタイルに戻る場合がある.
3. **`__placeholders` シートの印刷ヘッダー**: ページヘッダーに `{{DOC_NAME}}` / `{{VERSION}}` を埋込んでいるため, 後段で置換しない限りプレースホルダー文字列がそのまま印刷される. 参照専用シートとして印刷対象外 (非表示化) を推奨.
4. **条件付き書式**: 本テンプレでは未実装. PASS/警告セル装飾が必要な本文シートでは `CellIsRule` / `FormulaRule` を追加する (openpyxl 完全対応済み, build_xlsx.py で実装予定).
