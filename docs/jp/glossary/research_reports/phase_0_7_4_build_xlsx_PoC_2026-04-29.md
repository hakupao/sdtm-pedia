# Phase 0.7 Step 0.7.4 — build_xlsx.py PoC 作成サマリ

> 作成日: 2026-04-29
> 担当: executor (Phase 0.7.4)
> 上流文書: `docs/jp/PLAN.md` §3, `docs/jp/EXECUTION_PLAN.md` §3 Phase 0.7

---

## 1. スクリプト構成 (_styles.py / build_xlsx.py の責務分離)

`_styles.py` は配色 9 種 (`COLORS` / `COLOR_*`)、フォント定数 (`FONTS`)、サイズ定数、行高定数、およびセル書式ヘルパ関数群 (`THIN_BORDER`, `HEADER_FILL`, `ZEBRA_FILL`, `ACCENT_FILL`, `SOLID_FILL`, `WHITE_FILL`, `apply_print_settings`, `make_header_row`, `make_freeze_top_row`, `make_body_cell`, `make_title_cell`) を 1 ファイルに集約する。PLAN §3.1 の配色・フォント仕様の単一責任源として機能し、`build_xlsx.py` および将来の `audit_terms.py` / `extract_xlsx_text.py` / `check_links.py` から import 可能である。

`build_xlsx.py` は yml 読込・シート生成ロジック・出力パス解決の責務のみを持つ。表示に関する定数はすべて `_styles` 経由で参照し、直接 HEX 値やフォント名を埋め込まない設計とした。

---

## 2. yml schema 仕様 (PoC 段階)

最小フィールド構成は `document` (name / number / recipient / author / created / updated / version / output) / `revisions` (配列) / `sheets` (配列: type = text | table | links の 3 種) / `approval` (enabled フラグ) である。`sheets[].type` の分岐により、テキスト段落・表形式データ・参照資料リンクの 3 種類の本文シートを生成する。出力パスはリポジトリルート相対で指定し、スクリプト内で絶対パスに解決する。

---

## 3. 既存スクリプトへの修正影響 (最小化)

`generate_style_guide.py` および `generate_cover_template.py` の修正範囲は import 追加とハードコード定数の `_styles` 参照への置換のみである。シート生成関数・ヘルパ関数の実装は一切変更していない。両スクリプトの再実行結果をバックアップと意味論的に比較 (全シート全セル値) した結果、完全一致を確認した (バイナリ差異は openpyxl の ZIP タイムスタンプに起因する既知の挙動であり、生成内容に差異はない)。

---

## 4. PoC 動作確認結果

- 生成ファイル: `docs/jp/templates/sample_demo.xlsx`
- シート数: 7 (1_表紙 / 2_改訂履歴 / 3_目次 / 1_概要 / 2_項目一覧 / 3_参考資料 / 4_承認欄)
- ファイルサイズ: 13,144 bytes
- 表紙 placeholder 置換: 全 6 フィールド (文書名 / 文書番号 / 受信者 / 作成者 / 作成日 / 版数) 正常置換済
- 目次ハイパーリンク: 6 件自動生成 (表紙 / 改訂履歴 / 本文 3 シート / 承認欄)
- blacklist 検査: 33 語を対象に検査、ヒット 0 件 (PASS)

---

## 5. Phase 1 以降への引継ぎ事項

yml schema は拡張余地を残している。`sheets[].type` に `image` (assets/ 内 PNG 挿入) や `conditional_table` (条件付き書式付き表) を追加する場合は `build_xlsx.py` の `type_handlers` 辞書に対応関数を追加するだけでよく、既存シート種別への影響はない。7 文書の writer が `docs/jp/sources/NN.yml` を整備し `python3 docs/jp/scripts/build_xlsx.py docs/jp/sources/NN.yml` を実行するだけで PLAN §3 形式約定 100% 準拠の xlsx を得られる体制が整った。
