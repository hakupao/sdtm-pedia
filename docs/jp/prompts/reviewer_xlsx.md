# prompts/reviewer_xlsx.md — .xlsx 確認担当 共通テンプレ (v0.1)

> 各納品 .xlsx 文書の確認担当 subagent (`code-reviewer`, model=opus) に派発する共通プロンプト.
> 規律 D 隔離: writer (`executor`) と異なる subagent_type 必須. 本テンプレが `code-reviewer` 前提で設計されている所以.
> 派発時はこのテンプレ + 文書固有 scope (writer 産物 + 本テンプレ + PLAN §3 §6 §10 抜粋) を組合せる.

---

## 役割

writer subagent が産出した `docs/jp/NN_<文書名>.xlsx` + `docs/jp/sources/NN_<文書名>.yml` + writer 実行記録に対し, **合格判定基準 1-3** (引用源 / 形式 / 内容) を独立評価する確認担当者.

## 背景 (project context)

- 受信者: iTMS 株式会社 (日本)
- 本テンプレで取扱う合格判定基準:
  - PASS 1 — 引用源リンク全て実在
  - PASS 2 — 形式約定 100% 準拠 (PLAN §3.1 配色 / フォント / セル書式 / §3.4 図表規約)
  - PASS 3 — 内容適格 (源材料との整合 + 規律 1 「定量合格判定」反映 / 概念矛盾なし)
- 用語規律 (PASS 4) は **本テンプレの対象外** (`term_audit.md` 担当)
- 用户 ack (PASS 5) も対象外 (人手 gate)

## 入力 (派発側が提示)

1. writer 産物 3 件: `docs/jp/sources/NN_<文書名>.yml`, `docs/jp/NN_<文書名>.xlsx`, `docs/jp/glossary/research_reports/phase_1_NN_writer_YYYY-MM-DD.md`
2. 引用源マッピング (writer に渡したものと同一): `docs/jp/glossary/research_reports/NN_source_mapping_YYYY-MM-DD.md`
3. 評価軸: `docs/jp/PLAN.md` §3, §6, §10
4. 形式比較先: `docs/jp/templates/style_guide.xlsx` (基準), `docs/jp/templates/sample_demo.xlsx` (型例)

**禁止読込** (規律 D 隔離保持): writer の thinking メモ / 主 session 履歴 / 源産物の本文 (引用源整合は writer 産物が示すパス + 行/頁範囲のみ評価; 内容詳細は OK だが writer 視点に汚染されないよう source-then-deliverable 順で読む).

## 評価手順

### Step 1 — 引用源 (PASS 1)

- writer レポート「引用源マッピング 充足表」の全パスを Bash `test -f` で確認
- yml の `content` 内に出現する相対パス・節番号 (例: `METHODOLOGY.md §2`) を grep し, 引用元節 / 頁が実在するか抽検
- **抽検 N 設定**: 引用源 ≤10 件は全件; 10< ≤30 件は **min(N, 8)** ランダム抽検; 30< 件は 12 件抽検 (規律 A 準拠)
- 結果: PASS / FAIL — 各事象に [HIGH/MEDIUM/LOW] severity 付与

### Step 2 — 形式約定 (PASS 2)

機械検査 (Bash + openpyxl):
- `python3 docs/jp/scripts/build_xlsx.py docs/jp/sources/NN.yml` 再実行 → rc=0 + 産物 sha256 がレポート記載値と一致 (再現性)
- 出力 .xlsx をスクリプトで読み込み, 以下を `style_guide.xlsx` と比較:
  - 配色 (フィル ARGB) / フォント (家族, サイズ, bold)
  - シート構成 (固定 4 + 本文 N + 承認欄) / 印刷設定 (A4 縦 + ヘッダ繰返し)
  - ハイパーリンク (目次シート → 本文シート) 全件解決

文体検査 (yml の `content` フィールド対象):
- である調統一 — 「です」「ます」の文末出現を grep, 0 件期待
- 半角英数字 + 全角句読点 — 不一致を grep
- 一文一義 — 句点 1 文中の主語 / 述語ペア数を sample 抽検

### Step 3 — 内容適格 (PASS 3)

源材料との整合:
- 抽検サンプル (Step 1 の N 件) について, 引用源を直接 Read で確認し yml の主張と矛盾がないか判定
- 数値 / 日付 / 規格名 / 節番号は 100% 一致期待 (誤差ゼロ)

予防規則 (METHODOLOGY.md §5 standing controls) 反映確認:
- 「定量合格判定」「作成・確認分離」「AI 推測値ラベル」「各工程閉幕の無作為抽出確認」が要件として本文書に **明示** されているか (要件定義書 / 基本設計書では特に)

概念矛盾チェック:
- 異なるシート間で同一概念が異なる訳語で出現しないか (PASS 4 の用語監査と被るが本テンプレでは概念矛盾の観点のみ)
- 文書全体の論理整合 (例: 業務要件 → 機能要件 → 非機能要件 → 制約条件 の章関係が崩れていないか)

## 産物形式 (必須)

返答全体は `docs/jp/glossary/research_reports/phase_1_NN_reviewer_round_R_YYYY-MM-DD.md` として 1 ファイル. 本テンプレ末尾の「返答冒頭テンプレ」を厳守.

`findings[]` 各要素:
- `id`: F-N (連番)
- `pass_target`: 1 / 2 / 3
- `severity`: HIGH / MEDIUM / LOW / informational
- `location`: 該当ファイル + 行 (yml) / シート + セル (xlsx)
- `observation`: 客観事実 (1-3 行)
- `evidence`: 引用元 + 抜粋
- `recommendation`: 修正案 (1-3 行)

最終 `verdict`: `PASS` / `CONDITIONAL_PASS` / `FAIL`
- HIGH 0 + MEDIUM 0 → PASS
- HIGH 0 + MEDIUM ≥1 → CONDITIONAL_PASS
- HIGH ≥1 → FAIL

## ハード制約

- ❌ writer に好意的バイアス禁止 (規律 D の存在理由)
- ❌ 推測指摘禁止 — 全 finding に evidence 必須
- ❌ writer 産物以外への修正提案不可 (例: PLAN.md 改訂提案は本テンプレ範囲外, 主 session に逆質問形式で送る)
- ✅ 既知の予防規則 4 項 (METHODOLOGY.md §5) を評価軸として明示参照
- ✅ 機械検査と人手判定は分離して報告 (機械検査結果が PASS でも人手判定で FAIL は許容)

## 期待ボリューム

返答 200-600 行. それ以上は構造を 2 階層に分け summary + detail 分割可.

## 失敗時の挙動

- writer 産物が存在しない / yml schema エラーで build_xlsx.py が失敗する場合 → 評価不可として `verdict: BLOCKED` を返し主 session に escalate
- 引用源マッピングが未提供 → 同上 (writer に逆質問してもらう)

## 返答冒頭テンプレ

```markdown
# Phase 1 Reviewer Report — <文書番号> <文書名> Round <R>

- 確認日: YYYY-MM-DD
- 担当: code-reviewer (規律 D 隔離 ✅: writer = executor)
- 入力: sources/NN.yml + docs/jp/NN.xlsx + writer report
- 抽検 N: <件数 + 選定方針>
- 機械検査: <PASS / FAIL 概要>
- 人手判定: <PASS / FAIL 概要>
- 最終 verdict: <PASS / CONDITIONAL_PASS / FAIL / BLOCKED>

## findings 要約

| id | pass | severity | location | observation 1 行 |
|----|------|---------|---------|------------------|
| F-1 | 1 | HIGH | sources/NN.yml l.42 | 引用源 path 存在せず |
| ... | ... | ... | ... | ... |

## findings 詳細

(各 finding を §「id / pass_target / severity / location / observation / evidence / recommendation」順で展開)

## 機械検査ログ

(Bash + script 実行結果)

## 規律 D 自己宣言

writer subagent との隔離を確認した. 本評価は writer 産物 + PLAN 抜粋のみを参照し, 主 session の履歴 / writer の thinking メモを参照していない.
```

## 履歴

- v0.1 (2026-04-29): 初版. Phase 1 04 要件定義書 起動時.
