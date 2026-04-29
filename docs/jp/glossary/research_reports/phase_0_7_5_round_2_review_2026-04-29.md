# Phase 0.7 Step 0.7.5 — Round 2 視覚 QA 審査
> 審査日: 2026-04-29
> 担当: code-reviewer (Rule D 異 type, Round 2)
> Round 1 判定: CONDITIONAL_PASS (HIGH 0 / MEDIUM 3 / LOW 4)
> 本ラウンド範囲: M-1 + M-3 (M-2 / LOW 4 件は範囲外)
> 最終判定: **PASS**

---

## 0. 検証実行環境

- 実行ディレクトリ: `/Users/bojiangzhang/MyProject/SDTM-compare`
- 実行日時: 2026-04-29
- Python: `python3` (システム既定 / openpyxl 3.1.5 使用)
- 検査対象 build_xlsx.py: 33,156 bytes / 754 行 (Apr 29 15:11)

---

## 1. 検証サマリ

| 項目 | 結果 |
|------|------|
| M-1 schema 検証 4 ガード (+追加 2 ケース) | 6/6 PASS |
| M-3 docstring 8 関数 | 8/8 PASS (内部用語ヒット 0 / です・ます混在 0) |
| 回帰検証 (cell-level diff) | diff=0 (全 7 シート完全一致) |
| 副作用検査 (関連 4 ファイル sha256 不変) | 4/4 PASS |
| Round 1 機械検証 6 項目の再走 | 6/6 PASS (回帰なし) |
| 新規指摘 (HIGH/MEDIUM/LOW) | 0 件 |

---

## 2. 機械検証ログ

### 2.1 M-1 schema 検証 4 ガードの実証

`/tmp/r2_review/case_{a..f}.yml` を作成し `build_xlsx.py` で実行. 終了後一時ファイルは全削除済.

| # | ケース | 期待動作 | 実測 stderr | rc | 判定 |
|---|--------|---------|-------------|----|------|
| a | `document` キー欠落 | rc=1 + 必須メッセージ | `[エラー] yml に 'document' が必須.` | 1 | PASS |
| b | `document.output` 欠落 | rc=1 + 必須メッセージ | `[エラー] yml に 'document.output' が必須.` | 1 | PASS |
| c | `sheets[].name = "1_表紙"` (予約名衝突) | rc=1 + 候補名表示 | `[エラー] 予約シート名 '1_表紙' は本文シートに使用できない. 候補 → '本文_表紙'.` | 1 | PASS |
| d | `sheets[].name` 重複 (`1_概要` × 2) | rc=1 + 重複メッセージ | `[エラー] sheets[].name '1_概要' が重複している.` | 1 | PASS |
| e | `sheets[].name` 空白のみ (`"   "`) | rc=1 + 空文字メッセージ | `[エラー] sheets[].name に空文字または空白のみの値は使用できない.` | 1 | PASS |
| f | `sheets` キー欠落 | rc=1 + 必須メッセージ | `[エラー] yml に 'sheets' が必須.` | 1 | PASS |

**検出範囲が executor 主張 (4 ケース) を超えて 6 ケース全て発火することを確認.** いずれも `[エラー]` プレフィックス付きで `sys.stderr` に出力, rc=1 で終了する.

### 2.2 M-3 docstring 完備の実証

`ast.parse` で全関数を走査し docstring 有無を判定:

```
=== target 8 functions check ===
  _sheet_cover:    docstring_present=True (16 行)
  _sheet_revision: docstring_present=True (18 行)
  _sheet_toc:      docstring_present=True (17 行)
  _sheet_text:     docstring_present=True (13 行)
  _sheet_table:    docstring_present=True (15 行)
  _sheet_links:    docstring_present=True (15 行)
  _sheet_approval: docstring_present=True (11 行)
  main:            docstring_present=True (12 行)
```

加えて `_validate_schema` (13 行) / `build` (11 行) も完備. 8/8 全て期待要素 (機能 / 必須キー / 任意キー / 失敗時挙動) を含む.

**docstring 内部用語スキャン** (33 語 blacklist 全件, 単語境界付き正規表現):

```
blacklist term count: 33
== total blacklist hits in target docstrings: 0
```

**docstring 文体 (です・ます混在検出)**:

```
== total です/ます violations: 0
```

(平仮名 + `です|ます` の正規表現でスキャン. 全 docstring が「である調」で統一されている.)

### 2.3 回帰検証 (cell-level diff)

`python3 docs/jp/scripts/build_xlsx.py docs/jp/sources/sample_demo.yml` 実行 → rc=0, 13,143 bytes, 7 シート.

`load_workbook` で再生成版とバックアップ (`.backup/sample_demo.xlsx.before_round2`) を全シート全セル比較:

```
sheet names new: ['1_表紙','2_改訂履歴','3_目次','1_概要','2_項目一覧','3_参考資料','4_承認欄']
sheet names old: ['1_表紙','2_改訂履歴','3_目次','1_概要','2_項目一覧','3_参考資料','4_承認欄']
== total cell-value diff: 0 ==
```

シート構成・セル値ともに完全一致 (7 シート × 全セル).

### 2.4 副作用検査

#### 2.4.1 関連 .py ファイル sha256 不変

| ファイル | sha256 (現行) | 判定 |
|---------|--------------|------|
| `docs/jp/scripts/_styles.py` | `e9e9acb71a1ded13563acd2457375de064e84c07fad3620420ee16d1fbbc19fc` | 変更なし (Apr 29 14:26) |
| `docs/jp/scripts/generate_style_guide.py` | `761582cd6210b5ae6558b39710c3b9801a3e1f2abd0489c00e7e20825d554c82` | 変更なし (Apr 29 14:27) |
| `docs/jp/scripts/generate_cover_template.py` | `33a579e99cbea4e4077554263bbdff7988e58ba8b515bccebbf5e60efc8182de` | 変更なし (Apr 29 14:27) |

mtime も Round 1 (Apr 29 14:30 以前) のままで, Round 2 (Apr 29 15:11) 以降の編集は build_xlsx.py のみ.

#### 2.4.2 既生成 .xlsx ファイル sha256

`style_guide.xlsx` / `cover_template.xlsx` は再生成されておらず (Apr 29 14:34 のまま), Round 2 で執行された python 処理は sample_demo.xlsx 1 件のみ. `.backup/` 内の baseline 群とは Round 1 段階で取られたバックアップのため hash 差分があるが, これは Round 2 の責任範囲外.

### 2.5 Round 1 機械検証 6 項目の再走 (回帰なし確認)

再生成 `sample_demo.xlsx` に対して:

```
item 1 (color/font): fonts in use = ['Calibri','Consolas','Yu Gothic UI']
item 3 (sheet structure): 7 sheets — 期待通り
item 4 (blacklist scan, xlsx): 0 hits
item 5 (print settings): 7/7 paperSize=9 portrait
item 6 (cell-level diff): 0 (§2.3 と同)
freeze_panes / merge sanity:
  1_表紙: merged=8 (帯 + メタ)
  2_改訂履歴: freeze='A2'
  3_目次: freeze='A5' merged=2
  2_項目一覧: freeze='A3'
  3_参考資料: freeze='A3'
  4_承認欄: merged=1
```

Round 1 で PASS した 6 項目すべて回帰ゼロ. (`Calibri` は openpyxl が未指定セルに付与する既定値であり, build_xlsx.py が明示設定したセルは全て `Yu Gothic UI` / `Consolas` で指定済. Round 1 と同条件.)

---

## 3. 指摘事項 (新規のみ)

新規指摘なし.

(既存 LOW 4 件 / M-2 は本ラウンド範囲外として持ち越し, Phase 1 着手時に処理.)

---

## 4. 最終判定根拠

**判定: PASS (無条件)**

**根拠**:

1. **M-1 完全閉鎖**: executor が主張した 4 ケースに加え, reviewer が独自に追加した「空白のみ sheet 名」「sheets キー欠落」を含む 6/6 全ケースで `ValueError` → `[エラー]` プレフィックス + rc=1 を確認. メッセージは違反内容 + 候補名を含み, Phase 1 writer の品質ゲートとして十分.
2. **M-3 完全閉鎖**: 対象 8 関数すべて docstring 完備 (11-18 行). 機能 / 必須キー / 任意キー / 失敗時挙動の 4 要素が網羅される. 内部用語ヒット 0 / です・ます混在 0 で「である調」+ blacklist 規律も適合.
3. **回帰ゼロ**: sample_demo.xlsx 全 7 シート × 全セル diff = 0. シート構成・セル値・freeze_panes・merge 構造に変化なし.
4. **副作用ゼロ**: `_styles.py` / `generate_style_guide.py` / `generate_cover_template.py` の sha256 変化なし. `style_guide.xlsx` / `cover_template.xlsx` は再生成されていない.
5. **Round 1 機械検証 6 項目すべて回帰なし**: 配色 / フォント / シート構成 / blacklist (33 語) / 印刷設定 / 回帰検証.
6. **HIGH / 新規 MEDIUM 指摘ゼロ**: 新たな品質低下要素は検出されず.

**Phase 0.7 final close への申送り**:

- M-1 / M-3 はクローズ. Round 1 残課題 7 件のうち 2 件 (M-1, M-3) を本ラウンドで閉鎖.
- 持越し課題 5 件 (M-2 / L-1〜L-4) は Phase 1 開始時に着手:
  - M-2 (blacklist 25→33 語ドリフト) → Phase 1 で `audit_terms.py` 設計時に解消.
  - L-1 (重複ヘルパ整理) → 任意, Phase 1 と並行で構わない.
  - L-2 (`__placeholders` シート可視性) → 納品時 (build_xlsx.py 経由生成) では発生しないため Phase 1 緊急度は低い.
  - L-3 (図表番号自動採番) → Phase 1 で yml schema 拡張時に検討.
  - L-4 (generate_style_guide.py 肥大) → 将来課題.
- **Phase 0.7 final close 可能**.
