---
lang: ja
slug: changelog
order: 60
title: "変更履歴"
---

# SDTM ナレッジベース — Release v1.4 変更履歴 (日本語)

> タグ: `v1.4-company-release` (リリース: 2026-05-22)
> 前バージョン: `v1.3-company-release` (2026-05-20)
> 動機: Prompt フルスタックリファクタリング — 4 プラットフォーム v3/v9 clean rewrite (化石層除去 + KB グラウンディング default) + v1.3 からの minor carry 4 件 (C1-C4) + Claude bundle パイプラインアーキテクチャ修正. Gemini MAINTAINED_NO_SANITY_TEST (ユーザー 2026-05-22 決定).

## 概要

v1.4 は SDTM Pedia の **prompt-pass 級**リリースです — 維持中の 3 つの AI プラットフォーム (ChatGPT GPTs, Claude Projects, NotebookLM) が system prompt / instructions のフルスタック clean rewrite を完了し, v1.0-v1.3 の反復化石層を除去し, KB グラウンディングを主経路として再構築. Gemini Gems プラットフォームは v1.4 から「維持するが sanity テストは行わない」モードに移行 (ユーザー 2026-05-22 決定). v1.3 からの minor carry 4 件 (C1-C4) をマージ. C4 再構築中に検出された §N.N.N capture gap を Claude bundle パイプラインアーキテクチャ修正で解消 (Phase 6.5 reorg-A path regression).

## v1.4 (2026-05-22) — Prompt pass + Minor carries + パイプライン修正

**タイプ**: prompt-pass + minor carries (v1.3 の KB-pass に対して; 主作業は prompt 層に集中, KB 層は 1 ファイルのみ変更)

### Prompt 変更 (4 プラットフォーム system_prompt / instructions)

動機: v1.3 RETRO §二 8-carry リスト — 主軸は 4 プラットフォーム prompt フルスタックリファクタリング (Gemini v8.1 525 行に 17 件の CO-N 化石ルール + 他 3 プラットフォームの並行蓄積). v1.4 メイン carry は化石除去 + KB グラウンディング優先.

- **ChatGPT v3 system_prompt** (`self_deploy/chatgpt/system_prompt.md`): 120→119 行 + Method label anchor マッピング 4 行 (L77-80). v1.0-v1.3 反復注釈を除去, KB グラウンディングをデフォルト. A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
- **Claude v3 system_prompt** (`self_deploy/claude/system_prompt.md`): 125→133 行. 5 essential rules + regex ゲート CO-N + Files A-S 19-file table すべて保持 (critic レビュアーが attempt 1 の truncated 19→7 file table を発見 → attempt 2 で外科的修正により PASS_WITH_OBSERVATIONS).
- **NotebookLM v3 instructions** (`self_deploy/notebooklm/instructions.md`): 157→156 行. footer Sources citation はセマンティック等価で保持 (バイト完全ではないが挙動保存). v1.0-v1.3 反復化石層除去.
- **Gemini v9 system_prompt** (`self_deploy/gemini/system_prompt.md`): 525→292 行 (2026-05-22 増分の Method label anchor 含む). **MAINTAINED_NO_SANITY_TEST** — 最適化継続, テスト停止 (KNOWN_LIMITATIONS §0.A 参照).

### KB 変更 (1 ファイル修正)

- **PP/examples.md** — §6.3.5.9.3 に明示的 Method label マッピングテーブル 13 行追加 (A/B/C/D × IDVAR1+IDVAR2 4 行 + ヘッダー). KB + prompt 二重アンカーで v1.3 Q-S2 ChatGPT PARTIAL ラベルドリフトを解消 (C4).

### プラットフォーム別 bundle 変更

- **chatgpt**: `06_domain_examples_all.md` 再構築 (PP/examples §6.3.5.9.3 Method label table 含む); manifest 同期更新.
- **claude**: `09_examples_data_high.md` 再構築 (2922→3268 行, パイプライン修正後 A3.1 §N.N.N capture が初めて正常動作). Method label table + 新規 capture された 3 個の §N.N.N segment を含む.
- **notebooklm**: バケット 16 (`16_fnd_pharma_pc_pp.md`) 再構築 (Method label table 含む).
- **gemini**: bundle 変更が KB delta と同期 (gem は KB グラウンディング経由で自動取得).

### パイプライン / ビルドスクリプト修正 (重要)

- **`ai_platforms/claude_projects/dev/scripts/extract_examples_data.py`** parents[3]→parents[4] パスバグ修正: Phase 6.5 reorg-A で導入された path regression (スクリプトが 1 階層深く移動したが parents[] インデックスが同期されなかった). 影響: 全 28 domains が誤って missing 報告, A3.1 smoke は別の working config 起因で見落とし (smoke は dev/ で実行, 本番パスは異なる). C4 再構築時に実戦発火 → 修正 → 3 bundle 再構築成功 + 3268 行 examples bundle (§N.N.N capture 含む).

### 検証

- **B1 UI sanity** (Chrome MCP fire-and-forget): 4 問 × 3 プラットフォーム = 12 セル = **10 PASS+ + 2 PASS + 0 PARTIAL + 0 FAIL = 100% PASS** (Gemini 4 セルは §0.A により除外).
  - Q-S1 BECAT EXTRACTION: 3/3 PASS
  - Q-S2 PP RELREC Method (v1.3→v1.4 メイントリガー): 3/3 PASS+ (Claude paper PARTIAL → A3.1 パイプライン修正後 UI PASS+)
  - Q-S3 TR TRSTRESN/TRSTRESU typo: 3/3 PASS
  - Q-S4 DI ドメイン (NotebookLM バケット 25): 3/3 PASS
- **B2 R4 17 問全量リグレッション** (元 Gemini 専用スコープ): **N/A** — Gemini sanity テスト停止 (§0.A 参照; 最適化継続, テスト不継続).
- **Q-S2 再構築後 sanity 再テスト**: ユーザー指示で SKIPPED (grep レベルのコンテンツ検証で十分と判断).
- **C2 UNSOURCED N=80 サンプリング**: 75 RI + 0 XLSX + 0 HALLUCINATED + 5 NEEDS_REVIEW (累計 N=80; v1.3 N=40 HIGH + v1.4 +40 LOW; HIGH プールは v1.3 で枯渇).
- **C1 section_coverage**: P4b 決定的部分の再実行完了 — FULL_COVERAGE 101→137, SKELETON 67→46. md_atoms は pre-v1.3 状態のまま (LLM パイプライン再実行は v1.5 に C1-bis として延期).

### 既知の問題 (v1.5 へ延期 — KNOWN_LIMITATIONS §0 参照)

- **C1-bis フルパイプライン LLM 再実行**: P2 増分 + P4a 順方向マッチング + P4b (決定的部分は C1 で完了).
- **C1-ter post-P6 Makefile gate**: section_coverage 安定性 gate.
- **C2 KB_INTERNAL_CROSSREF 新分類カテゴリ**: N=80 サンプリングが現行 4 クラス分類器を超える新カテゴリの必要性を明らかに.
- **C2 3 件の deep paraphrase atoms manual review**: 5 件の NEEDS_HUMAN_REVIEW のうち 3 件は deep paraphrase で人的判断待ち.
- **C3 NotebookLM screenshot チュートリアル (Chrome MCP)**: v1.4 DEPLOY_GUIDE はテキストレベルのリマインダー; screenshot キャプチャは延期.
- **Tier B 156 セクション + 全 437 UNSOURCED + Phase 7 RAG+KG**: すべて v1.3 §二 からの carry.

### v1.3 → v1.4 アップグレード手順

セルフホストユーザー向け:

1. **sanity 覆盖 3 プラットフォーム (ChatGPT / Claude / NotebookLM)**: プラットフォームの system prompt を `self_deploy/<platform>/system_prompt.md` (または `instructions.md`) で置き換え; uploads を `self_deploy/<platform>/uploads/` の対応する bundle ファイルで置き換え. 詳細手順は `.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md`.
2. **Gemini**: ユーザー自検. v1.4 は v9 system_prompt + Method label anchor + KB delta 増分を提供しますが, 本プラットフォームは **sanity テスト覆盖なし** — 回答正確性はユーザー自身で検証, 高正確性シナリオでは他 3 プラットフォームを推奨.
3. **NotebookLM バケット 25** (v1.3 carry): 既存デプロイに古いソース `25_td_meta_ti_ts_oi.md` が残っている場合, `25_td_meta_ti_ts_oi_di.md` をアップロード後 **古いソースを手動削除** してください (43 → 42). v1.4 DEPLOY_GUIDE に目立つリマインダー.

**タグ**: `v1.4-company-release`

---

# SDTM ナレッジベース — Release v1.3 変更履歴 (日本語)

> タグ: `v1.3-company-release` (リリース: 2026-05-20)
> 前バージョン: `v1.2-company-release` (2026-05-19)
> 動機: KB pass — PP RELREC OA-4 欠落 + BECAT EXTRACTION prompt-KB 乖離 + Tier B 部分修復 + 4 プラットフォーム再構築 + ライト sanity 14-15/16 PASS

## 概要

v1.3 は**ナレッジベース pass 級**リリースです — v1.0 以来最大規模のコンテンツ更新. 本バージョンは KB を直接修正し, 更新されたソースから 4 プラットフォーム全バンドルを再構築して, 4 つのデプロイ済み AI プラットフォームでエンドツーエンドの配信を検証しています. Gemini system prompt (v8.1, 525 行) は v1.2 から**変更なし**; v1.4 の prompt フルスタックリファクタリングは延期.

## v1.3 (2026-05-20) — KB pass + 4 プラットフォーム再構築 + ライト sanity

**タイプ**: ナレッジベース pass (v1.0 以来最大のコンテンツ変更; prompt のみの刷新ではない)

### KB 変更 (11 ファイル修正)

- **PP/examples.md** — §6.3.5.9.3 RELREC Method クイックリファレンスを追加 (Method A/B/C/D テーブル + Method C の省略形 relrec.xpt 1 件). 06 Deep Verification プロジェクトから引き継いだ OA-4 欠落を解消. (バンドルで +2,620 行)
- **BE/spec.md** — L111: CDISC 標準例 COLLECTION / PREPARATION / TRANSPORT の隣に `EXTRACTION` をスポンサー拡張可能な第 4 の例として追加. KB と Gemini v8.1 prompt L272 の表現を揃える.
- **TR/spec.md** (§6.3.12.2) — 列ヘッダー typo を修正: TR 結果表示テーブルの `TRSTRESN` → `TRSTRESU`.
- **Tier B 修復 (その他 8 ファイル)** — 高密度 shall/must セクション 10 件を修復: §2.7 SDTM 変数規則, §6.4.2 FA 命名, §7.2.1 Trial Arms Example 4, §7.3.2/§7.3.3 TD/TM, §4.5.1.2 Tests Not Done, §6.4.3 FA --OBJ, §7.2.1.1 TA Distinguishing, §4.3.5.

### プラットフォーム別バンドル変更

- **chatgpt**: 3 ファイル更新 — `04_specs_and_context.md` (+284), `05_domain_assumptions.md` (+333), `06_domain_examples_all.md` (+5,432)
- **gemini**: 3 ファイル更新 — `01_navigation_and_routing.md` (+3,103), `02_specs_and_assumptions.md` (+617), `03_domains_examples.md` (+5,432)
- **notebooklm**: 7 ファイル更新 + 1 ファイルリネーム (`25_td_meta_ti_ts_oi.md` → `25_td_meta_ti_ts_oi_di.md`, バケット名に DI を反映)
- **claude**: 5 ファイル更新 — `02_chapters.md`, `03_model_structure.md`, `06_assumptions_all.md`, `09_examples_data_high.md` (+592), `10_examples_data_others.md`

### ビルドスクリプト変更 (防御的強化)

- ChatGPT `merge_for_chatgpt.py`: `expected_segments` をハードコードの `63/64/63` から動的 `len(_collect_domain_assumptions())` に変更. セグメント数リグレッションなし; delta >5% 時は warn (fail ではない).
- NotebookLM 新規 `validate_bucket_coverage.py`: 190/190 KB ファイルがバケットに到達, 陳腐化参照 0 件, 未ルーティングドメイン 0 件.

### 検証

- **フェーズ B クロスプラットフォーム delta oracle**: 4 つのバイト完全等式 PASS (ChatGPT 04 delta = NotebookLM バケット 10 delta = Gemini 02 部分 delta (BE/spec 変更等)). サイレントロス 0 件.
- **フェーズ C ライト sanity (4 問 × 4 プラットフォーム = 16 セル)**: 14-15/16 PASS.
  - Q-S1 BECAT EXTRACTION: 4/4 PASS (2 PASS+)
  - Q-S2 PP RELREC 4 メソッド: Claude PASS+, NotebookLM PASS+, ChatGPT PARTIAL (IDVAR 組み合わせ正確, Method ラベルずれ), Gemini FAIL (prompt bloat — v1.4 継続)
  - Q-S3 TR TRSTRESN/TRSTRESU typo: 4/4 PASS (2 PASS+)
  - Q-S4 DI ドメイン / バケット 25 リネーム: NotebookLM PASS+ (フッターで `25_td_meta_ti_ts_oi_di.md` 引用), Claude PASS+, Gemini PASS, ChatGPT PASS 推定
- **UNSOURCED_MANUAL N=40 サンプル**: 0% HALLUCINATED (80% REASONABLE_INFERENCE + 20% DERIVED_FROM_XLSX). Rule D `scientist` レビュアーが確認.
- **system_prompt 監査**: 4 プラットフォーム全体で 20/20 grep プローブ PASS (陳腐化した数値参照 0 件).

### 既知の問題 (v1.4 へ延期 — KNOWN_LIMITATIONS §0 参照)

- **Gemini PP RELREC 取得の弱さ** (フェーズ C Q-S2 FAIL): Gemini v8.1 prompt bloat (525 行, 化石レイヤーとしての 17 件 CO-N ルール) が PP RELREC の KB グラウンディング失敗を引き起こす. v1.4 主要継続: 4 プラットフォーム全 prompt フルスタックリファクタリング (~200 行クリーン版, regex ゲート制御 CO-N ルール).
- **437 件 UNSOURCED_MANUAL 原子の全量分類**: v1.3 は N=40 のサンプリングのみ. 全量は延期.
- **Tier B セクション 11-25 + 全 level-2 Tier B**: v1.3 はランク 11-20 (10 セクション) を修復. 残り約 156 セクションは延期.
- **R4 全 17 問 Gemini リグレッション**: v1.3 はライト sanity 4 問 × 4 プラットフォームを使用; Pro 専用 R4 はクォータ制約により延期.
- **section_coverage.jsonl フルパイプライン再実行**: ベースラインはバックアップ済み; 完全再実行は v1.4 へ延期.

### v1.2 → v1.3 アップグレード手順

セルフホストユーザー向け:

1. **全 4 プラットフォーム**: `self_deploy/<platform>/uploads/` のファイルで uploads を置き換える.
2. **NotebookLM**: `25_td_meta_ti_ts_oi_di.md` をアップロードし, 古い `25_td_meta_ti_ts_oi.md` を NotebookLM のソースリストから**削除** (ソース数が 43 から 42 に減少するはず).
3. **System prompts / instructions**: 変更不要 (Gemini v8.1 + 他 3 プラットフォームの prompt は v1.2 から変更なし).

**タグ**: `v1.3-company-release`

---

## v1.2 (2026-05-19) — Gemini 専用 prompt 刷新 v7.1 → v8.1

> タグ: `v1.2-company-release` (リリース: 2026-05-19)
> 前バージョン: `v1.1-company-release` (2026-05-15)
> 動機: SMOKE_V4 R3 (2026-05-19) の Gemini v7.1 リグレッション → v8.1 system prompt 修正

v1.2 は v1.1 の **Gemini 専用 system prompt 刷新**です. ナレッジベース / 4 プラットフォーム uploads / 全メタ文書 / 他 3 プラットフォーム (Claude / ChatGPT / NotebookLM) の system prompt はすべて v1.1 と同じ. **`self_deploy/gemini/system_prompt.md` のみを置換**しました (v7.1 → v8.1, 422 → 525 行, +24%).

### 動機: SMOKE_V4 R3 における Gemini リグレッション

v1.1 を 4 プラットフォームへデプロイ後, 2026-05-19 に完全リグレッションテスト (SMOKE_V4 R3) を実施. 4 プラットフォーム中 3 つが R1 ベースラインを維持:

- **Claude v2.6**: 17/17 (維持)
- **ChatGPT v2.2**: 17/17 (微増)
- **NotebookLM v2**: 15.5/17 (Q9 PUNT + Q11 PARTIAL は RAG アーキテクチャ制約, 想定内)
- **Gemini v7.1**: **13/17 (4 FAIL)** — R1 16/17 から後退

### v8.1 変更概要

4-prong fix: CO-4 入口ガード (biospecimen キーワード) + CO-2f ファイル形式 ground rule + CO-1e IS スコープシフト v3.3→v3.4 + CO-5 デフォルトリフレクション (SDTM-regex KB ダブルチェック). 6 件のレビュアー駆動修正 (H1/H2/M1/M2/L1/L2). 詳細は完全版 CHANGELOG.ja.md 参照.

### 検証

- v8.1 dry-run: 4/4 PASS, Gemini 3.1 Pro (R3 ベースラインと同 model).
- Rule D #16 (`pr-review-toolkit:code-reviewer`): PASS_WITH_OBSERVATIONS, 6 件の reconcile fix を適用.
- Rule D #17 (`oh-my-claudecode:verifier`): APPROVE 0 ブロッカー.

**タグ**: `v1.2-company-release`
