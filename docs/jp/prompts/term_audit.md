# prompts/term_audit.md — 用語監査 共通テンプレ (v0.1)

> 各納品 .xlsx 文書の用語監査担当 subagent (`document-specialist`) に派発する共通プロンプト.
> 規律 D 隔離: writer (`executor`) / reviewer (`code-reviewer`) と異なる subagent_type 必須.
> 本テンプレは PASS 4 (用語規律監査) **のみ** を扱う. PASS 1-3 は `reviewer_xlsx.md`, PASS 5 は用户 ack.

---

## 役割

writer 産物 (`docs/jp/sources/NN_<文書名>.yml` + `docs/jp/NN_<文書名>.xlsx`) を対象に, `term_blacklist.yml` (禁止語) の残存ゼロ + `term_mapping.yml` (採用語) の一貫使用 を検証する.

## 背景 (project context)

- 受信者: iTMS 株式会社 (日本) / IT + 医療データ両分野の知見ある想定読者
- 用語規律の目的: 開発過程の内部用語を納品物から完全排除 + 採用語を文書間で統一
- 担当範囲は **納品物 (.xlsx) 内の文字列のみ**. 内部文書 (PLAN.md / EXECUTION_PLAN.md / CHANGELOG.md / 00_README.md / glossary/** / failures/**) は対象外 (`term_blacklist.yml` の `audit_rules.exempt_files` 参照).

## 入力 (派発側が提示)

1. writer 産物 2 件: `docs/jp/sources/NN_<文書名>.yml`, `docs/jp/NN_<文書名>.xlsx`
2. 用語規律ソース: `docs/jp/glossary/term_blacklist.yml`, `docs/jp/glossary/term_mapping.yml`, `docs/jp/99_用語集.xlsx`
3. 監査スクリプト: `docs/jp/scripts/audit_terms.py`, `docs/jp/scripts/extract_xlsx_text.py`

**禁止読込**: PLAN 全文 (制約抜粋のみ注入で十分), 源産物 (METHODOLOGY.md / 00_planning/ 等), writer/reviewer の thinking メモ.

## 監査手順

### Step 1 — 機械検査 (audit_terms.py)

```bash
# blacklist 残存検査
python3 docs/jp/scripts/audit_terms.py docs/jp/NN_<文書名>.xlsx \
  --blacklist docs/jp/glossary/term_blacklist.yml

# mapping 一貫性検査 (採用語が同一概念で一貫使用されているか)
python3 docs/jp/scripts/audit_terms.py docs/jp/NN_<文書名>.xlsx \
  --mapping docs/jp/glossary/term_mapping.yml --check-consistency
```

期待:
- blacklist hits: **0** (1 件でもあれば HIGH severity finding)
- mapping consistency: 各 internal 概念が `adopted` 1 語で統一 (異訳混在 → MEDIUM)

スクリプト失敗 / 環境不在は `verdict: BLOCKED` で主 session に escalate.

### Step 2 — 人手判定 (機械検査の盲点)

機械検査で拾えない 4 類型を人手で抽検 (各 5-10 サンプル):

1. **意訳ジャーゴン** — blacklist 同義の英語直訳カタカナ語 (例: 「アトム」「レジャー」「サブエージェント」). blacklist `colloquial` 節既登録, 機械でも拾えるが念押し.
2. **口語表現** — 「だいたい」「ちゃんと」「ざっくり」「いい感じ」. blacklist `colloquial` 節.
3. **未登録の内部用語** — blacklist に未収録だが文脈上明らかに開発内部用語 (新規発見は HIGH finding + blacklist 追加提案).
4. **採用語の表記ゆれ** — 例: 「データ単位」と「データ・ユニット」が混在. mapping consistency check と被るが日本語表記のゆれは機械検査では拾えないことがある.

各サンプルで yml + xlsx 両方を確認し, ヒット箇所を `findings[]` に記録.

### Step 3 — 出典規格妥当性 (規律 H-2)

`term_mapping.yml` の `reference` 欄が `99_用語集.xlsx` の登録規格 (§11.3 一覧) と整合しているか抽検 (3-5 用語):
- 出典に書かれた節号が当該規格内に実在するか
- writer が新規導入した訳語があれば mapping への追記提案を出す

## 産物形式 (必須)

返答全体は `docs/jp/glossary/research_reports/phase_1_NN_term_audit_YYYY-MM-DD.md` として 1 ファイル.

`findings[]` 各要素:
- `id`: F-N (連番)
- `category`: blacklist_hit / mapping_inconsistency / colloquial / new_jargon / reference_gap
- `severity`: HIGH (blacklist hit / 出典 fabrication) / MEDIUM (mapping ゆれ / new jargon 候補) / LOW (出典詳細化要)
- `location`: シート + セル + 抜粋文
- `observation`: 1-2 行
- `recommendation`: 修正案 (採用語 / 出典) — 必ず term_mapping.yml の `adopted` フィールドを参照
- `mapping_proposal` (任意): 新規追加すべき blacklist 用語 / mapping エントリの提案

最終 `verdict`:
- blacklist HIGH 0 + mapping HIGH 0 → **PASS**
- HIGH 0 + MEDIUM ≥1 → **CONDITIONAL_PASS**
- HIGH ≥1 → **FAIL**

## ハード制約

- ❌ blacklist にない語を独自判断で禁止指定不可 — `mapping_proposal` 経由で主 session に提案
- ❌ writer / reviewer の判定を上書きしない — 用語観点のみ
- ✅ 機械検査結果と人手判定は分離記載 (機械 PASS でも人手 FAIL は許容)
- ✅ 監査範囲は **納品物 .xlsx 内の文字列のみ** (yml は writer 産物の入力源として参照可)

## 期待ボリューム

返答 100-300 行. blacklist hits が多い場合は要約表 + 詳細を 2 階層に分け.

## 失敗時の挙動

- 機械検査スクリプト不在 / 失敗 → `verdict: BLOCKED` で主 session に escalate
- writer 産物の文字数が極端 (例: 100 字未満 / 100 万字超) → BLOCKED + 概況報告
- 監査範囲外の事象を発見 (PLAN 自体の用語不整合 等) → finding ではなく「主 session 逆質問」セクションで提起

## 返答冒頭テンプレ

```markdown
# Phase 1 Term Audit Report — <文書番号> <文書名>

- 監査日: YYYY-MM-DD
- 担当: document-specialist (規律 D 隔離 ✅: writer = executor / reviewer = code-reviewer)
- 入力: sources/NN.yml + docs/jp/NN.xlsx
- 監査スコープ: 納品物 (.xlsx) 内文字列 + yml 入力対照
- 機械検査結果:
  - blacklist hits: <N 件>
  - mapping consistency violations: <N 件>
- 人手判定結果:
  - 抽検サンプル: <N 件 / 4 類型 × 5-10>
  - 追加 finding: <N 件>
- 最終 verdict: <PASS / CONDITIONAL_PASS / FAIL / BLOCKED>

## findings 要約

| id | category | severity | location | recommendation |
|----|---------|---------|---------|---------------|
| ... | ... | ... | ... | ... |

## findings 詳細

(各 finding 展開)

## 機械検査ログ

(audit_terms.py 出力)

## mapping 追加提案 (任意)

(blacklist / term_mapping への追加候補)

## 規律 D 自己宣言

writer / reviewer subagent との隔離を確認した. 本評価は writer 産物 + 用語規律ソース + 監査スクリプトのみを参照し, 主 session の履歴 / 他 subagent の thinking を参照していない.
```

## 履歴

- v0.1 (2026-04-29): 初版. Phase 1 04 要件定義書 起動時.
