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
