# SDTM ナレッジベース — Release v1.2 変更履歴 (日本語)

> タグ: `v1.2-company-release` (リリース: 2026-05-19)
> 前バージョン: `v1.1-company-release` (2026-05-15)
> 動機: SMOKE_V4 R3 (2026-05-19) の Gemini v7.1 リグレッション → v8.1 system prompt 修正

## 概要

v1.2 は v1.1 の **Gemini 専用 system prompt 刷新**です. ナレッジベース / 4 プラットフォーム uploads / 全メタ文書 / 他 3 プラットフォーム (Claude / ChatGPT / NotebookLM) の system prompt はすべて v1.1 と同じ. **`self_deploy/gemini/system_prompt.md` のみを置換**しました (v7.1 → v8.1, 422 → 525 行, +24%).

## 動機: SMOKE_V4 R3 における Gemini リグレッション

v1.1 を 4 プラットフォームへデプロイ後, 2026-05-19 に完全リグレッションテスト (SMOKE_V4 R3) を実施. 4 プラットフォーム中 3 つが R1 ベースラインを維持:

- **Claude v2.6**: 17/17 (維持)
- **ChatGPT v2.2**: 17/17 (微増)
- **NotebookLM v2**: 15.5/17 (Q9 PUNT + Q11 PARTIAL は RAG アーキテクチャ制約, 想定内)
- **Gemini v7.1**: **13/17 (4 FAIL)** — R1 16/17 から後退

Gemini の 4 失敗:

| # | 題目 | v7.1 失敗モード |
|---|---|---|
| Q3 | BE / BS / RELSPEC 生体試料処理 | 話題ずれで AE / AESEV / AEGRPID を回答 (1,541 文字) |
| Q4 シナリオ A | 抗麻疹ウイルス IgG 価 | LB を IS の代わりに選択 (R2 修正のデグレード) |
| Q11 | Dataset-JSON v1.1 vs XPT v5 | 話題ずれで AE / CM を回答 (1,436 文字) |
| AHP1 | LBCLINSIG 変数幻覚プローブ | 話題ずれで CM 多剤併用 / MH を回答 (1,485 文字) |

独立レビュアー (`oh-my-claudecode:scientist`, Rule D #15) は一致を確認し, 根本原因を Gemini v7.1 system prompt の 4 つのアンカーカバレッジ欠落と特定:

1. **Q3** — biospecimen キーワードのエントリーガード不在, Gemini が高頻度 SDTM ドメイン (AE / CM) にフォールバック.
2. **Q4 A** — v3.3 → v3.4 の IS スコープシフトの sticky anchor 不在; R2 修正がデグレード.
3. **Q11** — ファイル形式の ground rule 不在; Gemini がファイル形式の質問に SDTM ドメインの内容を代入.
4. **AHP1** — 反幻覚アンカーは題文に reflection scaffold がある時のみ発火. 単純な事実プローブでは未発火.

## v8.1 の変更内容

### 4-prong fix

- **CO-4 入口ガード (NEW)**: 題文に biospecimen 関連キーワード (中英 13 パターン) を含む場合, BE / BS / RELSPEC へ強制アンカー, AE / CM フォールバック禁止.
- **CO-2f ファイル形式 ground rule (NEW)**: 題文が XPT / Dataset-JSON / Define-XML / submission format に関する場合, 回答を CDISC 公開仕様に ground. 回答末尾の off-topic ガード含む.
- **CO-1e IS スコープシフト v3.3 → v3.4 (NEW)**: anti-microbial antibody 測定 (麻疹 / HBsAb / HCV / COVID / ADA, タイミング問わず) は IS, LB / MB ではない. HIV Ag / Ab combo は例外で MB (KB IS Assumption 5). ISTSTOPO 三層構造は Assumption 8.
- **CO-5 デフォルトリフレクション (MOD)**: 題文中で SDTM-shaped regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` に一致する識別子は, 題文フレージングに依存せず主回答前に必ず KB ダブルチェック. KB 未命中なら AHP-V1 否認テンプレート発火. 否定リスト + CO-2f 優先ゲートで過剰発火防止.

### 6 レビュアー駆動修正 (Rule D #16 reconcile)

- **H1**: HIV Ag / Ab combination → MB (LB ではない), KB IS Assumption 5.
- **H2**: CO-2f ファイル形式アンカーが CO-5 regex 変数幻覚パスに優先.
- **M1**: regex 否定リスト — 一般的な非 SDTM 略語 (`FDA` / `CDISC` / `XPT` / `JSON` 等) と SDTM ドメイン略号は KB ダブルチェックをスキップ.
- **M2**: 候補が 5 個以上の場合, 題文で明示的に言及された 3-5 個のみダブルチェック.
- **L1**: ISTSTOPO の出典を IS Assumption 8 に修正 (以前は誤って 7a と記載).
- **L2**: BECAT 例 `"EXTRACTION"` は sponsor-extensible と注記 (KB BE / spec L111 は 3 つの標準例のみ inline).

## Dry-run 検証 (Gemini 3.1 Pro, 2026-05-19 16:35-16:40 PM)

Pro クォータリセット直後に v7.1 の 4 失敗題を R3 ベースラインと同じ model で再テスト. 4/4 PASS:

| # | v7.1 R3 | v8.1 dry-run | Prong + Fix 検証 |
|---|---|---|---|
| Q3 | FAIL (AE 話題ずれ) | PASS (1,439c, 47.6s) | Prong 1 + L2 |
| Q4 | FAIL (A=LB) | PASS (1,763c, 52.7s) | Prong 3 + H1 + L1 |
| Q11 | FAIL (AE/CM 話題ずれ) | PASS (3,768c, 30.6s) | Prong 2 + H2 |
| AHP1 | FAIL (CM/MH 話題ずれ) | PASS (694c, 46.6s) | Prong 4 + M1 — 7/7 AHP-V1 要素発火 |

独立 Rule D #17 レビュアー (`oh-my-claudecode:verifier`) が KB 出典と照合して 4/4 PASS を確認, APPROVE 0 ブロッカー.

## プラットフォーム別パッケージ変更

### Gemini Gems (`self_deploy/gemini/`)

- **system_prompt.md**: 置換 (v7.1 → v8.1, 422 → 525 行).
- **uploads/*.md**: **不変** (v1.1 と完全一致; KB は v1.1 以降未変更).
- **tutorial.{en,zh,ja}.md**: 不変.

### Claude Projects / ChatGPT GPTs / NotebookLM

- 全ファイル byte-identical で v1.1 を継承. KB rebuild なし, prompt 変更なし.

## v1.1 から不変

- 全ナレッジベース内容.
- 4 プラットフォーム全 uploads bundles.
- 全メタ文書 (METHODOLOGY / USER_GUIDE / PLATFORM_COMPARISON / DEMO_QUESTIONS / GLOSSARY / README の en/zh/ja).
- Claude / ChatGPT / NotebookLM の全 system prompts および tutorials.

## 検証

- v8.1 dry-run: 4/4 PASS, Gemini 3.1 Pro (R3 ベースラインと同 model).
- Rule D #16 (`pr-review-toolkit:code-reviewer`): PASS_WITH_OBSERVATIONS, 6 件の reconcile fix を適用.
- Rule D #17 (`oh-my-claudecode:verifier`): PASS_WITH_OBSERVATIONS — APPROVE 0 ブロッカー.
- 完全な audit evidence: `ai_platforms/gemini_gems/dev/v8_draft/dry_run_2026-05-19/`.

## 既知 caveat (v1.2 post-cut に延期)

- **R4 17 題完全リグレッション**: v7.1 の 4 失敗題のみ再テスト, 13 道の v7.1 PASS 題は v8.1 下で未テスト. CO-5 デフォルトリフレクション regex と候補数キャップは多変数題で未独立検証. v1.2 post-cut で実施予定.
- **BECAT EXTRACTION KB-prompt 注記**: v8.1 prompt L272 で `"EXTRACTION"` を BECAT 例に含めたが, KB BE / spec L111 は 3 つの標準例のみ inline. 回答は sponsor-extensible と注記済み, 将来の prompt 改訂で明示的な出典引用を追加可能.
- **M2 候補数キャップ**: 4 題の dry-run では候補数 < 5, threshold が真に発火せず. R4 の多変数題で検証予定.

## v1.1 → v1.2 アップグレード手順

セルフホストユーザー向け:

1. Gemini Gem instructions フィールドの内容を `self_deploy/gemini/system_prompt.md` (525 行) で置換.
2. **他の操作は不要**. Uploads / 他プラットフォームの prompts / tutorials / メタ文書はすべて不変.
3. Gemini Gem の既存 chat セッションは次のメッセージ時に自動的に新 prompt を使用.
