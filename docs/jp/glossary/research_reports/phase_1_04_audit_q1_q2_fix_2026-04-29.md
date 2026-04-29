# Phase 1 用語監査スクリプト修正報告 (Q1 + Q2)

作成日: 2026-04-29
担当: executor (規律 D 隔離 — writer/reviewer/用語監査と兼務禁止)
対象ファイル:
- `docs/jp/scripts/audit_terms.py`
- `docs/jp/glossary/term_mapping.yml`
- `docs/jp/glossary/term_blacklist.yml`
- `docs/jp/CHANGELOG.md`

---

## 修正 1: audit_terms.py — exempt_files 自動除外機能追加

### 変更内容

| 箇所 | 変更前行数 | 変更後行数 | 内容 |
|------|-----------|-----------|------|
| imports | 23-29 | 23-31 | `fnmatch`, `Path`, `PurePath` 追加 |
| 新関数 `_resolve_repo_root()` | (なし) | 追加 +15 行 | blacklist yml 親 4 階層からリポジトリルートを動的判定 |
| 新関数 `_to_relative_path()` | (なし) | 追加 +10 行 | xlsx パスをリポジトリルート起点相対パスに正規化 |
| 新関数 `check_exempt()` | (なし) | 追加 +42 行 | exempt_files glob 照合 (PurePath.match + fnmatch 二段) |
| `format_output()` | 298-365 | 更新 | `exempt_info` 引数追加, verdict を exempt 時 "INFORMATIONAL" に上書き |
| `_print_human_summary()` | 368-419 | 更新 | exempt 表示ブロック追加 |
| `main()` | 486-534 | 更新 | exempt 判定ブロック追加, `bl_data` ロードを exempt 判定と共用, exit 条件に "INFORMATIONAL" 追加 |

合計追加: +約 75 行 (既存 538 行 → 613 行)

### 設計決定事項

- **リポジトリルート判定**: `docs/jp/glossary/term_blacklist.yml` から親 4 階層 (glossary → jp → docs → repo_root) で動的解決. ハードコードは不使用.
- **glob 照合二段戦略**:
  1. `PurePath(rel_path).match(pattern)` — パスパターン (`glossary/**`, `failures/**` 等)
  2. `fnmatch.fnmatch(filename, pattern)` — ファイル名単純パターン (`PLAN.md`, `*用語集*.xlsx` 等)
- **スキャン継続**: exempt 時も通常スキャンは実行する (hits は JSON に記録される). verdict のみ INFORMATIONAL に固定.
- **`bl_data` ロード共用**: exempt 判定と blacklist スキャンで同一 `bl_data` オブジェクトを再利用 (二重ロード禁止).

### term_blacklist.yml への追記

`*用語集*.xlsx` パターンを `audit_rules.exempt_files` に追加. 理由: `99_用語集.xlsx` は用語集ファイル自身であり、blacklist 掲載語 (round / atom 等) を内部用語対照表として合法的に保有する。

---

## 修正 2: term_mapping.yml ack エントリ candidates から「確認」削除

### 変更内容 (diff サマリ)

```diff
  - internal: ack
-   candidates: ["承認", "確認", "了承"]
+   candidates: ["承認", "了承"]
    adopted: "承認"
    reason: |
-     「確認」は事実認知を指し意思決定意味なし. 「了承」は商慣行的, 公文書では「承認」優先.
+     「了承」は商慣行的, 公文書では「承認」優先.
      「承認」は CSV ガイドライン §6.6 変更管理 + IPA モデル契約書 §承認欄 で標準語.
+     「確認」は日本語汎用語で承認欄列ラベル等に頻出. candidates 化は誤検出が多発するため除外. adopted の「承認」強制で規律目的は達成される.
```

`ack` エントリは維持, `adopted: "承認"` は維持. candidates から「確認」のみ除外.
version フィールドは v0.3 のまま (CHANGELOG にて v0.4 として記録).

---

## 動作検証 4 項

### A. 99_用語集.xlsx — INFORMATIONAL / exit 0

```
コマンド: python3 docs/jp/scripts/audit_terms.py docs/jp/99_用語集.xlsx
         --blacklist docs/jp/glossary/term_blacklist.yml
         --mapping docs/jp/glossary/term_mapping.yml --check-consistency
```

結果:
```
verdict: INFORMATIONAL
exempt.matched: True
exempt.matched_pattern: *用語集*.xlsx
input_relative_path: docs/jp/99_用語集.xlsx
EXIT_CODE: 0
```

判定: **PASS** (INFORMATIONAL, exit 0, exempt.matched true, matched_pattern 返却)

### B. sample_demo.xlsx — 確認 hits ゼロ確認

```
コマンド: python3 docs/jp/scripts/audit_terms.py docs/jp/templates/sample_demo.xlsx
         --blacklist docs/jp/glossary/term_blacklist.yml
         --mapping docs/jp/glossary/term_mapping.yml --check-consistency
```

結果:
```
verdict: FAIL
blacklist_hit_count: 0
mapping_inconsistency_count: 1  (writer/作成者 — 本修正範囲外の既存 issue)
確認 hits: 0  (修正前 2 件 → 修正後 0 件)
EXIT_CODE: 1
```

補足: `mapping_inconsistency_count: 0` の期待値は「確認」による 2 件がゼロになること。
残存 1 件は `writer → 作成者` (sample_demo.xlsx B7 の既存不整合) で本修正と無関係。
「確認」hits は確実に消失しており、修正目的は達成。
EXIT_CODE は FAIL (既存不整合残存) のため 1 — 期待どおり。

判定: **PASS** (確認 hits ゼロ達成)

### C. /tmp/test_fail.xlsx — FAIL / exit 1 / hit_count >= 2

```
作成: openpyxl で cell A1="atom", B1="ちゃんと"
コマンド: python3 docs/jp/scripts/audit_terms.py /tmp/test_fail.xlsx
         --blacklist docs/jp/glossary/term_blacklist.yml
         --mapping docs/jp/glossary/term_mapping.yml --check-consistency
```

結果:
```
verdict: FAIL
blacklist_hit_count: 2  (atom @ A1, ちゃんと @ B1)
EXIT_CODE: 1
```

判定: **PASS** (FAIL, exit 1, hit_count >= 2)

### D. term_mapping.yml — ack エントリ検証

```python
ack['internal'] == 'ack'          # True
ack['adopted'] == '承認'           # True
'確認' in ack['candidates']        # False
'承認' in ack['candidates']        # True (adopted は candidates に残る)
'日本語汎用語で承認欄列ラベル等に頻出' in ack['reason']  # True
```

判定: **PASS** (ack エントリ存在, 確認消失, 承認維持, reason 新追記含有)

---

## 残存懸念

**Q3 category 名統一 (本修正範囲外)**

`scan_mapping` 関数が返す inconsistency の `internal` フィールドは term_mapping.yml の `internal` キー値であり、
category (process_jargon / artifact_jargon 等) の名称は現在 JSON 出力に含まれない。
Q3 として挙げられた「category 名統一」問題 (blacklist と mapping で category 命名規則が異なる) は
本修正の scope 外。必要であれば別チケットで対応すること。

**sample_demo.xlsx の writer/作成者 不整合**

`docs/jp/templates/sample_demo.xlsx` の 1_表紙 B7 に「作成者」が残存。
term_mapping.yml では `writer → 文書作成担当者` が採用語で「作成者」は未採用候補。
テンプレートファイルの修正は本修正範囲外。
