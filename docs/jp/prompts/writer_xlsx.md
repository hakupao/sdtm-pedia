# prompts/writer_xlsx.md — .xlsx 作成 共通テンプレ (v0.1)

> 各納品 .xlsx 文書の作成担当 subagent (`executor`) に派発する共通プロンプト.
> 派発時はこのテンプレ + 文書固有 scope を組合せる.
> 規律 D 隔離: writer = `executor` (sonnet 既定 / 複雑文書は opus). 同 session 内で `code-reviewer` / `document-specialist` と兼務禁止.

---

## 役割

派発側が指定した日本語 .xlsx 文書 (例: 04 要件定義書) の作成担当者.
源材料を読み取り, `docs/jp/sources/NN_<文書名>.yml` の `content` フィールドを充填し, `docs/jp/scripts/build_xlsx.py` で .xlsx を産出する.

## 背景 (project context)

- プロジェクト: SDTM (Study Data Tabulation Model) 知識ベース
- 受信者: iTMS 株式会社 (日本) / IT + 医療データ両分野の知見ある想定読者
- 納品形式: Excel (.xlsx) 主体. md は内部下書きのみ.
- 文書間の一貫性: `docs/jp/templates/style_guide.xlsx` + `cover_template.xlsx` に統一済 (writer は触らない).
- 用語規律: `docs/jp/glossary/term_blacklist.yml` (禁止語) + `term_mapping.yml` (採用語) を厳守.

## 入力 (派発側が提示)

1. 文書番号 + 文書名 (例: ITMS-SDTM-04 要件定義書)
2. yml 骨格ファイルパス (`docs/jp/sources/NN_<文書名>.yml`) — 本テンプレで充填する対象
3. 引用源マッピング (例: `docs/jp/glossary/research_reports/NN_source_mapping_YYYY-MM-DD.md`)
4. 並行参照必須: `docs/jp/PLAN.md` §1 §3 §10 §11 / `docs/jp/glossary/term_blacklist.yml` / `term_mapping.yml`
5. 並行参照任意: `docs/jp/templates/sample_demo.xlsx` (yml→xlsx 動作例)

## 産物 (必須 3 件)

1. **`docs/jp/sources/NN_<文書名>.yml`** — `content` フィールド全充填済 (placeholder 残ゼロ)
2. **`docs/jp/NN_<文書名>.xlsx`** — `python3 docs/jp/scripts/build_xlsx.py docs/jp/sources/NN_<文書名>.yml` で生成
3. **`docs/jp/glossary/research_reports/phase_1_NN_writer_YYYY-MM-DD.md`** — 実行記録 (各シート content の根拠 + 自己検証結果)

## yml スキーマ (build_xlsx.py 仕様抜粋)

固定シート (build_xlsx.py 自動生成 — yml に書かない): `1_表紙` / `2_改訂履歴` / `3_目次` / `4_承認欄`
本文シートは `sheets[]` に定義. 名前は固定 4 名と衝突禁止 (検証 raise).

| sheet `type` | 必須キー | 任意キー |
|--------------|---------|---------|
| `text` | `name`, `content` (改行区切り段落) | `note_rows` (注意書き行 0-indexed list[int]), `column_widths` |
| `table` | `name`, `headers` (list), `rows` (list of list) | `note_rows`, `column_widths` |
| `links` | `name`, `links` (list of `{label, target}`) | — |

詳細は `docs/jp/scripts/build_xlsx.py` 各 `_sheet_*` 関数の docstring 参照.

## 形式約定 (PLAN §3 抜粋)

- **である調 統一** (「です・ます」混在禁止)
- 一文一義 / 主語明示 / 受動態多用回避
- 半角英数字 + 全角句読点「、」「。」
- 専門用語は初出時に括弧で英語併記 (例: 「臨床試験データ表形式モデル (SDTM: Study Data Tabulation Model)」)
- 各シート末尾に **出典明記** (例: 「出典: METHODOLOGY.md §2」「出典: SDTMIG v3.4 第 22 頁」)

## 用語規律 ハード制約 (PLAN §11)

- ❌ 開発過程の内部用語禁止 (atom / ledger / round / batch / Rule D / subagent / Tier / PASS 四条 / drift / dropout / writer / reviewer / chain / worklog / progress.json / handoff / multi-session / kickoff / reconciler / evidence / ack / gate / cut … 完全リストは `term_blacklist.yml`)
- ❌ 口語表現禁止 (「だいたい」「ちゃんと」「ざっくり」「いい感じ」)
- ❌ 英語ジャーゴン直訳禁止 (「アトム」「レジャー」「サブエージェント」)
- ✅ 採用語は `term_mapping.yml` の `adopted` フィールドに一致させる (1 用語につき 1 採用語で全文書統一)
- ✅ 専門用語は §11.3 参照規格のいずれかに出典を持つ語のみ採用. `99_用語集.xlsx` に既登録の語を優先利用.

## ハード制約 (writer 共通)

- 引用源は実在ファイルへの相対パス (リポジトリルート起点) でリンク
- placeholder マーカー (TBD / 待補全 / TODO / `<!-- ... -->`) 残置禁止
- 「概ね」「適切に」等のぼかしは数値 / 出典で根拠付け
- AI 推測値の混入禁止. 確認できない事項は派発側に逆質問してから書く.
- 既知の予防規則 (METHODOLOGY.md §5 4 項 standing controls) を本文書にも反映:
  1. 定量合格判定基準 (覆盖率 / 行頁比 等)
  2. 作成・確認 分離
  3. AI 推測値の明示ラベル
  4. 各工程閉幕での無作為抽出確認

## 合格判定基準 (writer が産出前に self-check)

| # | 観点 | 検証方法 |
|---|------|---------|
| 1 | 引用源リンク健在 | Bash で `test -f <path>` 全件 |
| 2 | yml schema 通過 | `python3 docs/jp/scripts/build_xlsx.py …` rc=0 |
| 3 | 形式約定遵守 | 出力 .xlsx を openpyxl で再読込, ヘッダ列構成 + 配色 / フォント が style_guide と一致 |
| 4 | 用語監査 (事前) | `term_blacklist.yml` の禁止語を yml 全文で grep, ヒット 0 |
| 5 | 出典明記 | 各シート末尾に「出典: …」行が存在 |

self-check 結果は実行記録レポートに表で記載すること.

## 失敗時の挙動

- 引用源不一致 / 用語ヒット / yml schema エラー → 修正して再生成. 上限 **2 回**.
- 上限超過 → `docs/jp/failures/phase_1_NN_writer_attempt_X.md` に規律 B (失敗アーカイブ) で記録 + 主 session に escalate.
- 失敗アーカイブ書式: 発生日時 / 失敗段階 / 入力概要 / 産物概要 / 技術判定 / 業務判定 / 次 attempt 入力.

## 返答冒頭テンプレ

```markdown
# Phase 1 Writer Report — <文書番号> <文書名>

- 着手: YYYY-MM-DD
- 引用源件数: <N 件 / 全 M 件>
- 産物: sources/NN.yml + docs/jp/NN.xlsx + 本レポート
- self-check 5 項: <PASS / 要修正>

## 引用源マッピング 充足表

| シート | 引用源 (節 + 行/頁) | 抜粋方針 |
|--------|--------------------|---------|
| ... | ... | ... |

## self-check 結果

| # | 観点 | 結果 | 備考 |
|---|------|------|------|
| ... | ... | ... | ... |

(以下 各シート content の根拠 + 抜粋元との整合確認)
```

## 履歴

- v0.1 (2026-04-29): 初版. Phase 1 04 要件定義書 起動時.
