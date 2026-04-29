# Phase 0.7 Round 2 Remediation 報告書
> 作成日: 2026-04-29
> 担当: executor (Phase 0.7 Round 2)
> 対象ファイル: `docs/jp/scripts/build_xlsx.py`
> 修正内容: M-1 スキーマ検証強化 + M-3 内部関数 docstring 補完

---

## 1. 修正概要

### M-1: スキーマ検証強化

`build()` の冒頭で `_validate_schema(data)` を呼び出す構造に変更した.
`_validate_schema()` は以下の 4 種の違反を `ValueError` で検出する:

1. `document` キー欠落または None
2. `document.output` キー欠落または None
3. `sheets[].name` が予約シート名 (`1_表紙` / `2_改訂履歴` / `3_目次` / `4_承認欄`) と衝突
4. `sheets[].name` の重複・空文字・空白のみ

`main()` 側で `ValueError` を catch し、stderr に `[エラー]` プレフィックス付きで出力後 `sys.exit(1)` する.

### M-3: 内部関数 docstring 補完

以下 8 関数に NumPy スタイル (既存 `build()` と統一) の docstring を追加した:
`_sheet_cover` / `_sheet_revision` / `_sheet_toc` / `_sheet_text` / `_sheet_table` / `_sheet_links` / `_sheet_approval` / `main`.
各 docstring に「機能 1 行」「yml 上の必須キー / 任意キー一覧」「失敗時挙動」を記述.
`main` のみ CLI 引数 / 終了コード仕様を追記.

---

## 2. 実装方針

- `_validate_schema(data: dict) -> None` を `_sheet_cover` の直前に配置 (内部ヘルパブロック内).
- `build()` の `yaml.safe_load()` 直後に `_validate_schema(data)` を 1 行追加.
- `main()` の `build()` 呼び出しを `try / except ValueError` でラップ.
- 標準ライブラリ追加なし. `_styles.py` / yml / xlsx 群は無変更.
- docstring スタイルは既存 `build()` の NumPy 形式に準拠 (Parameters / Returns 見出し使用).

---

## 3. 失敗系 4 ケース実行ログ

| # | ケース | stderr 出力 | 終了コード | 判定 |
|---|--------|------------|------------|------|
| a | `document` キー無 | `[エラー] yml に 'document' が必須.` | 1 | PASS |
| b | `document.output` 無 | `[エラー] yml に 'document.output' が必須.` | 1 | PASS |
| c | `sheets[].name = "1_表紙"` | `[エラー] 予約シート名 '1_表紙' は本文シートに使用できない. 候補 → '本文_表紙'.` | 1 | PASS |
| d | `sheets[].name` 重複 | `[エラー] sheets[].name '1_概要' が重複している.` | 1 | PASS |

一時 yml ファイルは `/tmp/test_{a,b,c,d}.yml` に作成後、テスト完了後に削除済.

---

## 4. 回帰テスト結果

```
python3 docs/jp/scripts/build_xlsx.py docs/jp/sources/sample_demo.yml
→ 生成完了: .../docs/jp/templates/sample_demo.xlsx
→ ファイルサイズ: 13,142 bytes
→ シート数: 7 (1_表紙 / 2_改訂履歴 / 3_目次 / 1_概要 / 2_項目一覧 / 3_参考資料 / 4_承認欄)
→ EXIT:0
```

セル値 diff (openpyxl load_workbook による全セル比較):

```
diff = 0 (セル値完全一致)
```

バックアップ: `docs/jp/templates/.backup/sample_demo.xlsx.before_round2`

---

## 5. 影響範囲

| 項目 | 詳細 |
|------|------|
| 変更ファイル | `docs/jp/scripts/build_xlsx.py` のみ |
| 行数 | 563 行 → 754 行 (+191 行; docstring + _validate_schema 関数) |
| 公開 API 変更 | なし (`build()` / `main()` のシグネチャ不変) |
| 新規依存 | なし (標準ライブラリのみ) |
| 正常系挙動変化 | なし (sample_demo.yml → セル値 diff = 0 確認済) |

---

## 6. M-2 / L-1〜L-4 への波及確認

| 指摘 | 波及 | 根拠 |
|------|------|------|
| M-2 (監査スコープ仕様書外の表記揺れ) | なし | `audit_terms.py` / `term_blacklist.yml` は本修正で未変更 |
| L-1 (重複ヘルパ関数) | なし | `_thin_border` / `_medium_border` 等のローカルヘルパは既存のまま保持 |
| L-2 (`__placeholders` シート) | なし | `generate_cover_template.py` は未変更 |
| L-3 (図表番号自動採番欠如) | なし | `_sheet_table` の生成ロジックは変更なし |
| L-4 (generate_style_guide.py 肥大) | なし | 対象外ファイル |

blacklist 残存確認 (納品スコープ `docs/jp/scripts/build_xlsx.py`):

```
grep -nE 'atom|ledger|round|batch|Rule D|subagent|...' docs/jp/scripts/build_xlsx.py
→ hits: 0
```

---

## 7. 結論

M-1 / M-3 の修正を最小差分で実施した. 失敗系 4/4 PASS, 回帰 diff = 0, blacklist 0 hits.
Phase 0.7 Round 2 reviewer による無条件 PASS 審査に向けて提出する.
