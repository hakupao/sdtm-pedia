# Phase 1-04: audit_terms 実装報告

> 作成日: 2026-04-29
> 担当: executor (oh-my-claudecode:executor)
> 規律: H-2 + Phase 0.7 deferred M-2 対応 / 規律 D 隔離 (実装専任)

---

## 産物一覧

| ファイル | 行数 | 役割 |
|---|---|---|
| `docs/jp/scripts/extract_xlsx_text.py` | 164 行 | .xlsx → 全文 plain text 抽出 (公開 API: `extract_cells`) |
| `docs/jp/scripts/audit_terms.py` | 538 行 | 用語規律監査 (blacklist + mapping consistency) |

---

## A. extract_xlsx_text.py — 主要関数 / 公開 API

### 公開関数

| 関数 | シグネチャ | 説明 |
|---|---|---|
| `extract_cells` | `(xlsx_path: str) -> Iterator[dict]` | .xlsx の非空セルを順次 yield. audit_terms.py が import して使用 |

### 内部関数

| 関数 | 説明 |
|---|---|
| `_format_jsonl(cells, out)` | jsonl 形式出力 |
| `_format_raw(cells, out)` | raw テキスト形式出力 |
| `main()` | CLI エントリポイント |

### extract_cells の出力フィールド

```json
{
  "sheet": "1_用語対照表",
  "row": 4,
  "col": 1,
  "coord": "A4",
  "value": "round",
  "hyperlink": null
}
```

### 実装上の判断

- `MergedCell` インスタンスは `isinstance` チェックでスキップ (左上セルのみ取得)
- `data_only=True` で数式セルの計算済み値を取得 (キャッシュなしは None → スキップ)
- xlsx 不在 → exit 2, stderr にエラーメッセージ

---

## B. audit_terms.py — 主要関数 / 公開 API

### 公開関数

| 関数 | シグネチャ | 説明 |
|---|---|---|
| `load_blacklist` | `(yml_path: str) -> dict` | term_blacklist.yml 読込 + schema 検証 |
| `load_mapping` | `(yml_path: str) -> list` | term_mapping.yml 読込 + schema 検証 |
| `scan_blacklist` | `(cells: list, blacklist_data: dict) -> list` | blacklist 全 term を全セルに照合 |
| `scan_mapping` | `(cells: list, entries: list) -> list` | mapping consistency 検査 |
| `format_output` | `(xlsx_path, blacklist_result, mapping_result) -> dict` | JSON 出力整形 |

### 内部関数

| 関数 | 説明 |
|---|---|
| `_is_ascii_only(term)` | term が全 ASCII かを判定 |
| `_build_pattern(term, case_sensitive, match_whole_word)` | re パターン構築 |
| `_print_human_summary(result)` | 人間可読サマリを stderr 出力 |
| `main()` | CLI エントリポイント |

### マッチングロジック詳細

`match_whole_word: true` の解釈:

| term の種別 | 判定方法 | 例 |
|---|---|---|
| 全 ASCII (半角英数字のみ) | `\b` 単語境界 + `re.IGNORECASE` | `atom`, `round`, `cut` |
| 日本語 / カタカナ / 漢字含む | 部分一致 (`re.escape` のみ) | `ちゃんと`, `アトム`, `だいたい` |
| 1 文字 term | 検出続行 + stderr 警告 | (現 yml に該当なし) |

### mapping consistency 仕様

- `adopted` が `文脈依存` または `公開不要 (内部分類)` の場合: candidates 全語を未採用候補扱い
- `adopted` がそれ以外: candidates から adopted を除いた語が未採用候補
- 未採用候補語が xlsx 内に出現 → inconsistency として記録 (occurrences + first_location 付き)

### 終了コード

| コード | 条件 |
|---|---|
| 0 | PASS: blacklist_hit = 0 かつ mapping_inconsistency = 0 |
| 1 | FAIL: いずれか > 0 |
| 2 | 引数エラー / ファイル不在 / yml schema 不正 |

---

## 動作検証 A-E 結果

### A. extract_xlsx_text.py — 99_用語集.xlsx jsonl 抽出

```
コマンド: python3 docs/jp/scripts/extract_xlsx_text.py docs/jp/99_用語集.xlsx --format jsonl
```

| 項目 | 値 |
|---|---|
| 抽出行数 | **405 行** |
| シート一覧 | `1_用語対照表`, `1_表紙`, `2_採用根拠`, `2_改訂履歴`, `3_候補参考`, `3_目次`, `4_承認欄` |
| exit code | 0 |

raw format 先頭出力 (確認):

```
=== 1_表紙 ===
用語集
文書番号: ITMS-SDTM-99-GLOSSARY-v0.1
受信者
iTMS 株式会社 御中
...
```

### B. audit_terms.py — 99_用語集.xlsx (blacklist + mapping 一括)

```
コマンド: python3 docs/jp/scripts/audit_terms.py docs/jp/99_用語集.xlsx \
  --blacklist docs/jp/glossary/term_blacklist.yml \
  --mapping docs/jp/glossary/term_mapping.yml --check-consistency --human
```

| 項目 | 値 |
|---|---|
| blacklist hit_count | **126** |
| mapping inconsistency_count | **92** |
| verdict | **FAIL** |
| exit code | 1 |

**観察**: 99_用語集.xlsx は用語集ドキュメント自体であり、`1_用語対照表` シートの「英 (内部用語)」列に `round`/`batch`/`atom` 等の禁止語を一覧として掲載している。また `2_採用根拠` / `3_候補参考` シートの採用候補列に未採用語が含まれる。これは仕様どおりの正検出。

**ユーザー向け注記 (主 session へ逆質問)**: `term_blacklist.yml` の `audit_rules.exempt_files` に `glossary/**` が列挙されているが、スクリプトは現在 `exempt_files` を参照せず全ファイルを均等検査する。`99_用語集.xlsx` は用語集ドキュメントのため、監査対象から除外する運用 (呼び出し側が対象ファイルを選定する) か、スクリプトに exempt_files 判定を追加するかを確認されたい。Phase 0.5.8 で「blacklist_scan: 0 hits 既確認」とされた根拠と矛盾しないか確認要。

### C. audit_terms.py — templates/sample_demo.xlsx

```
コマンド: python3 docs/jp/scripts/audit_terms.py docs/jp/templates/sample_demo.xlsx \
  --blacklist docs/jp/glossary/term_blacklist.yml \
  --mapping docs/jp/glossary/term_mapping.yml --check-consistency --human
```

| 項目 | 値 |
|---|---|
| blacklist hit_count | **0** |
| mapping inconsistency_count | **2** |
| verdict | **FAIL** |
| exit code | 1 |

**観察**: blacklist は 0 hits でクリア。mapping inconsistency として以下が検出された:

| found_alt | adopted | 場所 | 箇所数 |
|---|---|---|---|
| `作成者` | `文書作成担当者` | `1_表紙!B7` | 1 |
| `確認` | `承認` | `1_表紙!B2` | 8 |

`確認` は承認欄 / 目次シートのラベルに多数出現。`term_mapping.yml` では `ack` の adopted が `承認`、candidates に `確認` が含まれるため、標準テンプレートの「確認」列ラベルが不整合として検出される。

**ユーザー向け注記**: `確認` は `ack` (内部用語 "了承/ack") の未採用候補として mapping に登録されているが、日本語文書の一般的な「確認」列ラベルとは別概念。mapping 設計の観点から `確認` を candidates に含めることの妥当性、または mapping consistency チェックの適用範囲 (一般用語との衝突回避) を主 session に確認されたい。

### D. 故意不正検査 — /tmp/test_fail.xlsx (atom + ちゃんと)

```
コマンド: python3 docs/jp/scripts/audit_terms.py /tmp/test_fail.xlsx \
  --blacklist docs/jp/glossary/term_blacklist.yml \
  --mapping docs/jp/glossary/term_mapping.yml --check-consistency --human
```

| 項目 | 値 |
|---|---|
| blacklist hit_count | **2** (atom @ Sheet1!A1, ちゃんと @ Sheet1!B1) |
| mapping inconsistency_count | 0 |
| verdict | **FAIL** |
| exit code | **1** |

hit 一覧:

```json
{"term": "atom", "category": "artifact_jargon", "sheet": "Sheet1", "coord": "A1"}
{"term": "ちゃんと", "category": "colloquial", "sheet": "Sheet1", "coord": "B1"}
```

期待値 (FAIL, exit 1, hit_count ≥ 2) 全て充足。

### E. エラーケース検証

| シナリオ | コマンド抜粋 | stderr 出力 | exit code |
|---|---|---|---|
| yml 不在 | `--blacklist /tmp/nonexistent.yml` | `[エラー] blacklist yml が見つからない: ...` | **2** |
| xlsx 不在 | `audit_terms.py /tmp/nonexistent.xlsx` | `[エラー] xlsx ファイルが見つからない: ...` | **2** |
| extract_xlsx_text xlsx 不在 | `extract_xlsx_text.py /tmp/nonexistent.xlsx` | `[エラー] xlsx ファイルが見つからない: ...` | **2** |
| yml schema 不正 (YAML 構文エラー) | `--blacklist /tmp/bad_schema.yml` | `[エラー] blacklist yml YAML 構文エラー: ...` | **2** |

全ケース exit 2 + stderr メッセージ明示を確認。

---

## term_blacklist.yml / term_mapping.yml 読込時に発見した schema 不整合

### 発見 1: 99_用語集.xlsx が監査対象になる問題 (上記 B の観察参照)

`audit_rules.exempt_files` フィールドが yml に存在するが、スクリプトはこれを現在参照していない。呼び出し側で対象ファイルを制御する設計か、スクリプト内で除外するかを主 session に確認されたい。

### 発見 2: mapping consistency の `確認` 衝突 (上記 C の観察参照)

`ack` エントリの candidates に `確認` が含まれるため、標準テンプレートの「確認」「確認担当」等の一般的な列ラベルが全て inconsistency として検出される。mapping 設計の意図 (ack の文脈限定適用 vs. 全文スキャン) を確認されたい。

### 発見 3: term_mapping.yml の category 5 (katakana_aliases) が blacklist に未対応

`term_mapping.yml` には `katakana_aliases` カテゴリ (`アトム`, `レジャー`, `サブエージェント`) が存在するが、`term_blacklist.yml` の `categories` には `process_jargon` / `artifact_jargon` / `governance_jargon` / `colloquial` の 4 カテゴリのみ。カタカナエイリアスは `colloquial` として blacklist に含まれているが (`アトム`, `レジャー`, `サブエージェント` は colloquial 内に掲載)、term_mapping.yml 側と category 名が不一致。両 yml の category 構造を統一するかを主 session に確認されたい。

---

## 既存スクリプトとの style 整合確認

| 規則 | build_xlsx.py | 本実装 | 整合 |
|---|---|---|---|
| shebang + encoding 宣言 | `#!/usr/bin/env python3` + `# -*- coding: utf-8 -*-` | 同一 | OK |
| docstring 言語 | 日本語 | 日本語 | OK |
| section header | `# ─────` (em dash × 76) | 同一形式 | OK |
| PEP8 | import 順 (stdlib → third-party → local) | 同一 | OK |
| エラー出力 | `print(..., file=sys.stderr)` + `sys.exit(N)` | 同一 | OK |
| パス解決 | `os.path.isfile` / `os.path.abspath` | 同一 | OK |
| yml 読込 | `yaml.safe_load` | 同一 (yml_to_glossary.py 参照) | OK |
| 関数粒度 | 単一責任 + docstring | 同一 | OK |
| 日本語コメント | 処理の意図を日本語で記述 | 同一 | OK |

---

## 備考

- `extract_xlsx_text.py` は `audit_terms.py` から `import extract_cells` して使用 (重複実装なし)
- 標準依存以外: `openpyxl`, `PyYAML` のみ (仕様どおり)
- `sys.path.insert(0, os.path.dirname(__file__))` で同一ディレクトリの `extract_xlsx_text` を確実に import
