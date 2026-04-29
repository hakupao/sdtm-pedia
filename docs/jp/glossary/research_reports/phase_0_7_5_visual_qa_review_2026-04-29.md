# Phase 0.7 Step 0.7.5 — Excel 基盤 視覚 QA 審査
> 審査日: 2026-04-29
> 担当: code-reviewer (Rule D 異 type, executor とは別 subagent)
> 上流仕様: `docs/jp/PLAN.md` §3 / §11.1, `docs/jp/EXECUTION_PLAN.md` §3 Phase 0.7
> 審査対象: 4 スクリプト (`_styles.py` / `generate_style_guide.py` / `generate_cover_template.py` / `build_xlsx.py`) + 3 .xlsx (style_guide / cover_template / sample_demo) + 1 yml (sample_demo.yml) + 4 レポート MD
> 最終判定: **CONDITIONAL_PASS**

---

## 0. 審査サマリ

| 区分 | 件数 |
|------|------|
| HIGH 指摘  | 0 |
| MEDIUM 指摘 | 3 |
| LOW 指摘 | 4 |
| 機械検証項目 | 6 全項 PASS |
| 評価項目 | 12 (PASS 9 / CONDITIONAL 3 / FAIL 0) |

CRITICAL/HIGH ゼロのため Phase 0.7 は閉じる方向で問題ないが, 3 件の MEDIUM は Phase 1 着手前にスクリプトへ補強を入れることを推奨する.

---

## 1. 12 項目チェックリスト判定

| # | 観点 | 判定 | 指摘 |
|---|------|------|------|
| 1 | 配色 HEX 完全一致 (9 種) | PASS | _styles.COLORS 9 種 / ARGB 8 桁版 9 種 すべて PLAN §3.1 と一致. 全 18 項抽検済 (規律 A 100%). |
| 2 | フォント名一致 (PLAN §3.1) | PASS | _styles.FONTS は Yu Gothic UI / Meiryo UI / Noto Sans JP / Segoe UI / Consolas を保持. PLAN §3.1 の選択肢「Segoe UI **または** Arial」「Consolas **または** Yu Gothic UI Mono」は第一候補のみ採用で仕様適合. なお style_guide.xlsx 「2_フォント標本」の代替候補列に Arial / Yu Gothic UI Mono を文字列として明記済 (受信者環境への提示意図確保). |
| 3 | 生成 .xlsx シート構成 | PASS | style_guide=6 / cover_template=5 / sample_demo=7, 計 18 シート. 各 .xlsx の主張通り. |
| 4 | blacklist 残存ゼロ (xlsx + py + yml + 4 MD) | PASS | xlsx 0 / yml 0 / py 0. MD 1 hit (M-2 参照: "writer" — 内部レポートで規律対象外, 監査範囲は `audit_rules.scope=deliverables_only`). |
| 5 | 印刷設定 (A4 縦 / portrait / print_title_rows) | PASS | 全 18 シートで paperSize=9, orientation=portrait, print_title_rows='$1:$1'. |
| 6 | 回帰検証 (cell-level diff) | PASS | generate_style_guide.py / generate_cover_template.py 再実行後, バックアップとのセル値完全一致 (差異 0). 意味論的同一性確保. |
| 7 | 責務分離 (_styles.py の副作用) | PASS | 副作用ゼロ. top-level 文 18 個全て定数代入. import 時に副作用なし. 関数は全て純粋関数 (引数依存のみ). |
| 8 | 型 + docstring (公開 API) | CONDITIONAL | _styles.py 公開関数 13/13 に docstring 完備. 一方 build_xlsx.py の公開 main() に docstring 無, 内部 _sheet_* 関数群もドキュメンテーション無 (M-3 参照). |
| 9 | エラー処理 (yml schema 違反 / 名衝突) | CONDITIONAL | 未対応 sheet type=`diagram` は警告 stderr 出して continue (健全). 一方 (a) 必須 key 完全欠如 (`document` 自体無し) でも rc=0 で空 xlsx 生成, (b) sheets[].name=`1_表紙` のような fixed sheet 名衝突を openpyxl の自動 rename (`1_表紙1`) に放置している. M-1 参照. |
| 10 | CLI 健全性 (使用法表示) | PASS | build_xlsx.py 引数無 → rc=1 + 「使用方法」stderr 出力. ファイル不在 → rc=1 + 明示エラー. generate_*.py は --help 引数を無視して即実行する (引数不要 script として割切り設計, 単独実行でも害はない). |
| 11 | PLAN §3.2 必須要素 (表紙 / 改訂履歴 / 目次 / 承認欄) | PASS | cover_template.xlsx 4 種揃, sample_demo.xlsx 4 種揃. 改訂履歴 ヘッダーは 6 列 (版 / 改訂日 / 改訂内容 / 作成 / 確認 / 承認) で PLAN §3.2 完全一致. 承認欄は 4 列 (役割 / 氏名 / 日付 / 押印・署名) × 3 行 (作成 / 確認 / 承認) で PLAN §3.2 「3 行構成」と整合. |
| 12 | §3.3 文体 (である調) + §3.4 図表番号 | CONDITIONAL | sample_demo.yml 本文 "である調" 確認済 (です・ます混在ゼロ). 一方 (a) §3.4 図表番号「図N-N / 表N-N」採番欄が table sheet ヘッダー定義に未組込み, (b) sample_demo.yml 表ヘッダーが「項目 / 説明 / 判定」のみで図表番号列無. PLAN §3.4 は図表に番号必須の記述だが build_xlsx.py PoC 段階では Phase 1 writer の責務に委ねる構造. L-3 参照. |

---

## 2. 機械検証ログ (項目 1-6)

### 項目 1: 配色 HEX
```
COLORS dict 9 種 + ARGB 8 桁 9 種 完全一致 — PASS
main_accent: #1F4E79 OK / sub_accent: #2E86AB OK / header_bg: #D9E7F1 OK
zebra_odd: #F4F8FB OK / border_line: #A6B5C2 OK / pass_green: #4D8B7C OK
warn_orange: #C97B5C OK / bg_white: #FFFFFF OK / caption_gray: #5A6B7A OK
ARGB: COLOR_MAIN_ACCENT=FF1F4E79 ... 9 種全 OK + COLOR_TEXT_WHITE=FFFFFFFF
```

### 項目 2: フォント
```
_styles.FONTS keys: jp_primary='Yu Gothic UI', jp_fallback='Meiryo UI',
jp_fallback2='Noto Sans JP', en_primary='Segoe UI', mono='Consolas'
PLAN §3.1 第一候補 5 種すべて存在.
PLAN §3.1 fallback 候補 (Arial / Yu Gothic UI Mono) は generate_style_guide.py の表示用文字列で受信者に提示.
```

### 項目 3: シート構成
```
style_guide.xlsx (6 sheets):
  0_目次, 1_配色パレット, 2_フォント標本, 3_セル書式, 4_レイアウト見本, 5_禁止例

cover_template.xlsx (5 sheets):
  1_表紙, 2_改訂履歴, 3_目次, 4_承認欄, __placeholders

sample_demo.xlsx (7 sheets):
  1_表紙, 2_改訂履歴, 3_目次, 1_概要, 2_項目一覧, 3_参考資料, 4_承認欄

合計 18 シート (executor 主張通り).
```

### 項目 4: blacklist 残存
```
スコープ毎の hit 数:
  xlsx (3 ファイル, 18 シート): 0 hits  ← 納品候補, MUST 0 → 達成
  sources/sample_demo.yml:      0 hits  ← deliverable feed, MUST 0 → 達成
  scripts/*.py (4 ファイル):    0 hits  ← 内部, INFORMATIONAL → 達成
  research_reports/*.md (4 ファイル): 1 hit (writer @ 0_7_4 PoC, 内部レポート)
  → audit_rules.scope=deliverables_only に従い MD は対象外, FAIL 不要.

検査ロジック: 全 33 blacklist 用語に対し
  pattern: (?<![A-Za-z0-9_])TERM(?![A-Za-z0-9_]), case_insensitive=True
  注: 仕様書では blacklist 25 語と記述があるが実際は 33 語 (term_blacklist.yml 全件).
```

### 項目 5: 印刷設定
```
全 18 シート (6+5+7) で:
  ws.page_setup.paperSize == 9 (= openpyxl PAPERSIZE_A4)
  ws.page_setup.orientation == 'portrait'
  ws.print_title_rows == '$1:$1'
PLAN §3.1 印刷要件 100% 適合.
```

### 項目 6: 回帰検証 (cell-level diff)
```
generate_style_guide.py 再実行 → 旧版とのセル値差異: 0
generate_cover_template.py 再実行 → 旧版とのセル値差異: 0
意味論的同一性確認. _styles.py 抽出による副作用なし.
```

---

## 3. 指摘事項詳細

### M-1 [MEDIUM] build_xlsx.py のスキーマ違反検証が緩い
- 場所: `docs/jp/scripts/build_xlsx.py` `build()` 関数 (行 469-534)
- 事象 1: `document` キーがまったく無い yml を渡しても rc=0 で空 xlsx を生成する (3 シートのみのファイルが出力される). 致命的でないが Phase 1 で writer が yml を破壊した場合に発覚が遅れる.
- 事象 2: `sheets[].name` がプログラム固定の `1_表紙` / `2_改訂履歴` / `3_目次` / `4_承認欄` と衝突する場合, openpyxl が自動で `1_表紙1` に rename する. 警告も例外も出ない. 監査は通るが目次のリンク切れと内容不整合が静かに発生する.
- 事象 3: `document.output` も `revisions` も `sheets` も空でファイル生成が成功する → 仕様適合とは言えないファイルが「PASS」扱いになる.
- 修正案 (Phase 1 着手前):
  - `build()` の冒頭に必須キー検査 (`if not data.get("document"): raise ValueError("yml に 'document' 節が必須.")`).
  - 固定シート名 `{"1_表紙", "2_改訂履歴", "3_目次", "4_承認欄"}` と user sheet 名の衝突検査. 衝突時は `ValueError` で停止し具体的シート名を表示.
  - 必須 sheet 名空文字 / 重複検査 (sheets[].name の重複).
- 参照: PoC レポート §2 「最小フィールド構成」, EXECUTION_PLAN.md §5 「失敗ケース」.

### M-2 [MEDIUM] 監査スコープ仕様書外の表記揺れ
- 場所: 本人プロンプト / `term_blacklist.yml` / `audit_rules`
- 事象: 本タスク指示は blacklist 「25 語」の grep を要求しているが, 実 yml は 33 語 (新たに `kickoff` / `handoff` / `cut` / `multi-session` / `reconciler` / 口語俗語 4 語等を追加). 機械検査は 33 語全件で実施した (規律 A 100% 達成) が, 後続 reviewer/writer が 25 語前提で動作すると差分 8 語を見落とす恐れ.
- 修正案: `audit_terms.py` (Phase 1 で作成) は `term_blacklist.yml` を単一ソースとし, スクリプト内ハードコード禁止. 本タスク仕様書 (Phase 0.7.5 prompt) も次回更新時に「33 語 (term_blacklist.yml に従う)」へ訂正.

### M-3 [MEDIUM] build_xlsx.py 内部関数の docstring 欠落
- 場所: `docs/jp/scripts/build_xlsx.py` `_sheet_cover` / `_sheet_revision` / `_sheet_toc` / `_sheet_text` / `_sheet_table` / `_sheet_links` / `_sheet_approval` / `main`
- 事象: 公開 `build()` には NumPy スタイルの docstring があるが, シート生成 `_sheet_*` 関数 7 件と CLI エントリ `main()` には docstring 無. _styles.py は公開関数 13/13 に docstring 完備で, 同等水準を期待. Phase 1 で writer が yml schema 拡張する際に各 `_sheet_*` の入力契約 (yml の必須キー / 任意キー) が不可視.
- 修正案: 各 `_sheet_*(wb, doc, sheet_def)` に「sheet_def に期待するキー」「列構成」「失敗時挙動」を 1 段落で記述. `main()` には CLI 仕様 (引数 / 終了コード) を記述.

### L-1 [LOW] 重複ヘルパ関数 (_styles.py 抽出後の置去り)
- 場所: `generate_style_guide.py` 行 55-116, `generate_cover_template.py` 行 82-117, `build_xlsx.py` 行 43-50
- 事象: `_styles.py` に共通化済の `THIN_BORDER` / `HEADER_FILL` / `SOLID_FILL` 等が, 各スクリプトで再定義 (`thin_border` / `header_fill` / `solid_fill` 等) されている. PoC レポート §3 は「import 追加とハードコード定数の `_styles` 参照への置換のみ」と主張するが, ヘルパ関数は古い実装が残置. _styles.COLORS への置換だけで関数共有は未完了.
- 影響: 動作上の害なし (同一実装) だが今後 `THIN_BORDER` の挙動を変更しても 3 箇所のローカル `thin_border()` には反映されない. DRY 違反.
- 修正案: 各スクリプトのローカル `thin_border` / `header_fill` / `solid_fill` 等を削除し `_styles.THIN_BORDER()` / `_styles.HEADER_FILL()` / `_styles.SOLID_FILL()` に置換. Phase 1 着手前 (急ぎではない) の整理項目.

### L-2 [LOW] 仕様書外の追加要素 `__placeholders` シート
- 場所: `cover_template.xlsx` シート 5
- 事象: PLAN §3.2 「各シート冒頭の必須要素」には placeholder 一覧シートは含まれない. cover_template.xlsx に `__placeholders` (placeholder 6 種を Consolas で表示) を追加するのは executor の独自判断. PoC レポート §4「3. `__placeholders` シートの印刷ヘッダー」自身が「参照専用シートとして印刷対象外 (非表示化) を推奨」と書くが, 現状非表示化 (`ws.sheet_state="hidden"`) は適用されていない.
- 影響: テンプレが受信者にそのまま渡ると placeholder 値 (`{{DOC_NAME}}` 等) が見える違和感. cover_template はあくまで内部ベースのため納品時 (build_xlsx.py 経由) は問題なし.
- 修正案: cover_template.xlsx は内部参照用と明示 (README 追記) または `ws.sheet_state="hidden"` で隠す.

### L-3 [LOW] 図表番号 (図N-N / 表N-N) の機械生成欠如
- 場所: `build_xlsx.py` `_sheet_table` (行 320-364)
- 事象: PLAN §3.4 「図番号 図N-N / 表番号 表N-N. キャプション必須, 図表下に配置」を build_xlsx.py の `table` type は実装していない. 表ヘッダーは yml の `headers` をそのまま採用するのみ. Phase 1 で writer が手で図表番号列を yml に書込む形になる.
- 影響: PoC 段階としては許容範囲. Phase 1 で 7 文書全てにこのルールを浸透させるのは負担.
- 修正案: `_sheet_table` に `figure_number` (任意) を追加し, 設定時はタイトル行の左に `表N-N: ` を自動挿入する設計を Phase 1 で検討.

### L-4 [LOW] generate_style_guide.py 1 ファイル肥大 (32KB)
- 場所: `docs/jp/scripts/generate_style_guide.py` 全 642 行
- 事象: 単一ファイルに 6 シート分の生成ロジックが直書き. シート毎の関数分離は済 (sheet_toc / sheet_palette / 他) だが「1 関数 50 行未満」の目安からは外れる (sheet_layout が 80 行超等). _styles.py 抽出後も `prohibited_items` のような大量データが直書き残置.
- 影響: 読込みは可能, 将来の禁止例追加で diff レビューが多少重い. 致命的問題なし.
- 修正案: `prohibited_items` のような巨大データは別 yml/json に外出しできる余地あり (将来課題).

---

## 4. 最終判定根拠

**判定: CONDITIONAL_PASS**

**根拠**:
1. CRITICAL/HIGH 指摘ゼロ. Phase 0.7 PASS 二条 (PLAN §3.1 デザイン基準 100% 準拠 + 視覚 ack 用意完了) の前段機械要件は満たした.
2. 配色 HEX 9 種 + ARGB 9 種, フォント 5 種 (PLAN 第一候補), シート 18 枚, 印刷設定 18/18, 回帰差異 0 — 機械検証 6 項全て PASS.
3. blacklist 33 語スキャン (xlsx 3 + yml 1 + py 4 + 1 hit @ 内部 MD のみ) — 納品スコープ (`deliverables_only`) で残存ゼロ.
4. PLAN §3.2 必須要素 (表紙 / 改訂履歴 / 目次 / 承認欄) は cover_template.xlsx と sample_demo.xlsx で完備. 改訂履歴 6 列 / 承認欄 3 役 PLAN 整合.

**残課題と Phase 0.6 (用户 ack) への引継ぎ条件**:
- M-1 (build_xlsx スキーマ検証強化) は Phase 1 着手前に修正推奨. 現状でも generate 自体は動作するが, 7 文書 writer が yml を組む際の品質ゲート不足.
- M-3 (build_xlsx 内部関数 docstring) は Phase 1 着手と並行で改善可.
- L-1 (重複ヘルパ整理) は時間ある時の整理.
- 図表番号自動採番 (L-3) は Phase 1 で 7 文書 writer 規律に組み込む.
- 用户視覚 ack (Phase 0.7.6) は本機械審査と独立に「3 .xlsx を Excel で実開いて見栄え確認」が必要 — 本 reviewer はそれ自体は実施できないため, 用户に Excel または LibreOffice での目視確認を依頼することで Phase 0.7 完了とする.

**Phase 0.7.6 (用户 ack) への申送り**:
- 3 ファイル (`style_guide.xlsx` / `cover_template.xlsx` / `sample_demo.xlsx`) を Excel で開き, 配色帯 (#1F4E79) の白文字視認性 / Yu Gothic UI のフォント適用 / ゼブラ縞 / 表紙アクセント帯 / 承認欄罫線 を目視確認.
- 印刷プレビュー (A4 縦 / ヘッダー繰返し) を 1 シートでも確認すれば Phase 0.7.5 機械要件 + Phase 0.7.6 視覚要件で Phase 0.7 全体クローズ可能.

