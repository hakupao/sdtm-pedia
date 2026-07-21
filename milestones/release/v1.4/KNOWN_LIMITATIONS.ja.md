---
lang: ja
slug: known-limitations
order: 50
title: "既知の制限事項"
release: v1.4
---

# 既知の制限事項

本ページは v1.4 の利用境界を説明します. 単なる不具合一覧ではなく, どの質問を直接確認でき, どの質問を公式ソースまたは内部手順で確認すべきかを判断するためのものです.

## 0. v1.4 監査範囲 (2026-05-22 更新)

v1.4 は SDTM Pedia の **prompt-pass 級**リリースです — 維持中の 3 つの AI プラットフォーム (ChatGPT GPTs, Claude Projects, NotebookLM) を対象に system prompt / instructions のフルスタック clean rewrite を実施し, 反復ラウンドで蓄積された化石レイヤーを除去し, KB グラウンディングを主経路として再構築しました. 同時に v1.3 からの minor carry 4 件をマージしています.

**重要な変更 — Gemini Gems プラットフォームは v1.4 から「維持するが sanity テストは行わない」モードに移行します**, 詳細は下記 §0.A.

### 0.A. Gemini Gems プラットフォーム — MAINTAINED_NO_SANITY_TEST (v1.4 onwards)

v1.4 から, **SDTM Pedia は Gemini Gems に対して sanity / R4 リグレッションテストを実施しません**が, **best-effort のメンテナンスは継続します**:

- **決定日**: 2026-05-22 (ユーザー口頭 clarification)
- **トリガー**: v1.4 フェーズ B B1 ライト sanity において, Gemini v9 prompt が PP RELREC Method A/B/C/D 問題で完全に幻覚 (4/4 マッピングすべて誤り) することが判明. 加えて Gemini Pro クォータ制約 (5h ローリングウィンドウあたり約 4 問) が 17 問 R4 全量を長期にわたり阻害. 総合判断として **テストは継続しない** (クォータ浪費の回避); **最適化は継続する** (KB delta + 重要 prompt 修正).
- **v1.4 の Gemini 配信物**:
  - v9 system_prompt に Method label anchor 段落を追加 (ChatGPT v3 L77-80 と並行): A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
  - v1.4 KB delta (PP/examples §6.3.5.9.3 マッピングテーブル) は KB グラウンディング経由で Gemini gem の挙動に伝播 (bundle 再アップロードなしでも, 改訂された prompt によって gem の推論はこのテーブルを参照).
- **メンテナンス境界**:
  - **継続 ✅**: KB delta が Gemini gem instructions に流入 (release/ に Gemini bundle 差分を含む); 重要な prompt 修正 (anchor / 誤マッピング等の明示的 KB グラウンディング修).
  - **停止 ❌**: sanity 問題セット実行 (B1 4 問 × Gemini, R4 17 問 Gemini Pro 全量リグレッション, smoke プローブ検証); ロックステップダッシュボード (R3+ 維持期のダッシュボードはダウングレード; Phase 0-5 ゲートは履歴参照として保持); ユーザーレベル検証はセルフデプロイユーザーに委譲.
- **保持**: `release/v1.3/self_deploy/gemini/` を最後の sanity 検証済みベースラインとして保持 (v8.1 LIVE, 16/17 R3 PASS). v1.4 Gemini gem はこのベースライン上に v9 refactor + Method label anchor を加えますが, **sanity 覆盖なし**, ユーザー自検.

### 0.B. v1.4 配信内容 (3 プラットフォームを対象)

- **フェーズ A — Prompt clean rewrite** (3 プラットフォーム system prompt / instructions の clean rewrite, 独立 Rule D レビュアー監査済み):
  - **ChatGPT v3 system_prompt** (120→119 行 + 明示的 Method label anchor マッピング 4 行): v1.0-v1.3 反復注釈を除去, KB グラウンディングをデフォルト経路に, A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
  - **Claude v3 system_prompt** (125→133 行; critic レビュアーが attempt 1 の truncated 19→7 file table を発見 → attempt 2 で外科的修正により PASS_WITH_OBSERVATIONS 取得): 5 essential rules + regex ゲート CO-N + Files A-S テーブルすべて保持.
  - **NotebookLM v3 instructions** (157→156 行): footer Sources citation はセマンティック等価で保持 (バイト完全ではないが挙動保存); v1.0-v1.3 反復化石レイヤー除去.
  - **A3.1 Claude bundle パイプラインアーキテクチャ修正** (`extract_examples_data.py` SECTION_HDR_RE capture): v1.3 Phase D verifier が見つけた `## §N.N.N` heading が capture されないパイプラインギャップを修正. B1 UI sanity Q-S2 Claude で実戦命中 (paper PARTIAL → UI PASS+).

- **フェーズ B — ライト sanity (3 プラットフォーム 12/12 PASS, Gemini 4 セルは drop により除外)**:
  - B1 UI レベル (Chrome MCP fire-and-forget): 4 問 × 3 プラットフォーム = 12 セル = **10 PASS+ + 2 PASS + 0 PARTIAL + 0 FAIL = 100% PASS**.
  - 問題セット: Q-S1 BECAT EXTRACTION (v1.3 carry), Q-S2 PP RELREC Method (v1.3 → v1.4 メインリファクタリングのトリガー), Q-S3 TR TRSTRESN/TRSTRESU typo, Q-S4 DI ドメイン (NotebookLM バケット 25 リネーム).
  - B2 R4 17 問全量リグレッション (元 Gemini 専用スコープ): **N/A — Gemini sanity テストは停止** (詳細 §0.A; 最適化は継続, テストは継続せず).

- **フェーズ C — Minor carries (4 件)**:
  - **C1 section_coverage.jsonl 全量パイプライン再実行** — v1.3 A5 baseline stale carry をクローズ. P4b 決定的部分の再実行完了 (FULL_COVERAGE 101→137, SKELETON 67→46); フル LLM パイプライン再実行 (P2 増分 + P4a 順方向マッチング) は v1.5 に C1-bis として延期.
  - **C2 UNSOURCED 発見的分類器修正 + N=80 サンプリング** — Rule D `scientist` (v1.3) が発見した DERIVED_FROM_XLSX→REASONABLE_INFERENCE バイアスを修正; N=40 (v1.3 HIGH stratum) + 40 (v1.4 LOW stratum) に拡張. 結果: 75 RI + 0 XLSX + 0 HALLUCINATED + 5 NEEDS_HUMAN_REVIEW (累計 N=80); Rule A 10/10 PASS; バイアス修が HIGH から LOW stratum まで拡大.
  - **C3 NotebookLM バケット 25 UX チュートリアル + screenshot** — v1.3 実運用でユーザーが古いソースの削除を忘れる事象が発生 (43 → 本来 42); v1.4 `.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md` に目立つリマインダー追加; Chrome MCP screenshot チュートリアルは v1.5 に延期.
  - **C4 ChatGPT PP RELREC Method label KB anchor** — `PP/examples.md §6.3.5.9.3` に明示的 4 行マッピングテーブル追加, v1.3 Q-S2 ChatGPT PARTIAL ラベルドリフトを解消 (KB + prompt 二重アンカー). 3 プラットフォーム bundle 再構築 + Gemini v9 system_prompt anchor 同期 (2026-05-22 ユーザー clarification 後).

### 0.C. v1.3 §0 項目の reconcile

| v1.3 §0 項目 | v1.4 状況 |
|---|---|
| 4 プラットフォーム system_prompt/instructions フルスタックリファクタリング (メインライン) | **resolved** — 4 プラットフォーム (ChatGPT/Claude/NotebookLM/Gemini) すべて v3/v9 clean rewrite 完了; Gemini v9 に Method label anchor を追加 (Phase A 本体 + 2026-05-22 増分); Gemini sanity テストのみ停止 (詳細 §0.A) |
| 437 件 UNSOURCED_MANUAL 全量分類 | **部分的に resolved** — 発見的バイアス修正 + N=80 サンプリング完了; 全 437 件の逐次レビューは v1.5 に延期 |
| Tier B セクション 11-25 + 全 level-2 (約 156 セクション) | **defer to v1.5** — v1.4 規模を超える (約 5-7 営業日の独立 KB pass サイクル), 独立リリースとして実施 |
| Issue 5 §6.3.5.9.3 PC/PP 143 TABLE_ROW Tier-B MEDIUM 修復 | **defer to v1.5** — 06 Deep Verification §二 参照; Tier B 全量と同時期に処理 |
| section_coverage.jsonl 全量パイプライン再実行 | **部分的に resolved** — P4b 決定的部分完了 (C1); フル LLM パイプライン再実行 (C1-bis) は v1.5 に延期 |
| R4 全 17 問 Gemini Pro リグレッション | **N/A — Gemini sanity テスト停止** (Pro クォータ制約 + テスト停止; 最適化は継続) |
| PASS+ §1.2 厳格 "AHP 専用" スコープ拡張 | **acknowledged** — 拡張定義 (KB グラウンディング + ベースラインを超える深さ = PASS+) が v1.4 sanity でも継続適用; 将来の smoke 設計で正式組み込み |

### 0.D. v1.4 で未実施の項目 (v1.5+ に延期)

- **Tier B 156 セクション** (Batch H ランク 1-10 約 470 atoms + Batch S 21-25 約 10 atoms + level-2 24 セクション約 600 atoms) — v1.4 規模を超える, 独立 KB pass サイクル.
- **437 件 UNSOURCED_MANUAL 全量逐次分類** — v1.4 は発見的修正 + N=80 サンプリングのみ; 全量精度パスは v1.5.
- **フェーズ 7 RAG + KG キックオフ** — prompt refactor と並行実施は非経済的, 独立フェーズとして実施 (設計は `docs/DESIGN_RAG_KG.md` で完了).
- **C1-bis フル LLM パイプライン再実行** — P2 増分 + P4a 順方向マッチング (決定的部分は C1 で完了).
- **C2 KB_INTERNAL_CROSSREF 新分類カテゴリ** — N=80 サンプリングの 5 件 NEEDS_HUMAN_REVIEW atoms が現行 4 クラス分類器の新カテゴリ追加必要性を明らかに.
- **C2 3 件の deep paraphrase atoms manual review** — N=80 carry (5 件の NEEDS_HUMAN_REVIEW のうち 3 件は deep paraphrase で人的判断待ち).
- **C3 NotebookLM screenshot チュートリアル (Chrome MCP)** — v1.4 DEPLOY_GUIDE にテキストレベルのリマインダー + スケルトン追加, screenshot キャプチャは次の sprint に延期.

### 0.E. 外観 / デプロイ上の注意事項

- **Gemini ユーザー**: v1.4 は Gemini gem 増分を提供します (system_prompt v9 clean rewrite + Method label anchor + KB delta). ただし本プラットフォームは **sanity テスト覆盖なし** であり, 回答正確性はユーザー自検をお願いします. 高い正確性が必要なシナリオでは ChatGPT / Claude / NotebookLM の使用を推奨します (本リリースで sanity 覆盖済み).
- **NotebookLM バケット 25** (v1.3 carry, v1.4 でチュートリアル強化): 既存の v1.0-v1.3 NotebookLM デプロイに古いソース `25_td_meta_ti_ts_oi.md` が残っている場合, `25_td_meta_ti_ts_oi_di.md` をアップロード後 **古いソースを手動削除** してください (クリーンアップ後 43 → 42). v1.4 `.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md` に目立つリマインダー (screenshot チュートリアルは v1.5 に延期).
- **ChatGPT PP RELREC Method label**: v1.4 KB + prompt 二重アンカーが対応済み (C4 resolved), v1.3 PARTIAL ドリフトは resolved 予定 (sanity 再テストはユーザー grep レベル検証に委譲).

## 1. 公式標準の代替ではありません

SDTM Pedia は参照支援ツールです。規制当局提出、標準解釈、用語バージョン確認、重要なマッピング判断では、CDISC 刊行物、NCI EVS、ライセンスされた MedDRA 資料、規制要件、内部 SOP を使用してください。

## 2. リアルタイムの外部更新は保証されません

本リリースは、公開時点で整理された知識範囲を反映しています。新しい CDISC バージョン、Pinnacle 21 ルール更新、Dataset-JSON の状況、外部データベース変更などは、該当する公式ソースを確認してください。

## 3. 長尾の統制用語は公式確認が必要な場合があります

非常に大きい codelist や長尾の questionnaire 用語は、すべてのプラットフォームで完全展開されているわけではありません。この場合、よい回答は境界を明示し、未確認の完全リストを生成するのではなく、NCI EVS などの権威あるソースに戻るよう案内します。

## 4. プラットフォームごとに回答スタイルが異なります

Claude、ChatGPT、Gemini、NotebookLM は、回答スタイル、引用表示、慎重さが異なります。NotebookLM はアップロード済み資料により近い回答をする傾向があります。他のプラットフォームは説明や要約に向きますが、人による判断は必要です。

## 5. 組織内部ルールは対象外です

スポンサー、CRO、データ標準チームには、内部マッピング規約、Define-XML 実務、Reviewers Guide の書き方、品質フローがある場合があります。SDTM Pedia は標準確認を支援しますが、これらの規約を置き換えません。

## 6. 人によるレビューが必要な場面

以下は人による確認を推奨します。

- 正式提出のデータ構造または変数マッピングに影響する判断。
- 医学コーディング、重篤な有害事象、死亡、中止など重要な臨床概念。
- プロジェクト固有の CRF、SAP、データ管理計画、スポンサー標準。
- 根拠が明確でない回答、またはチーム標準と矛盾する回答。

明らかな誤りや不足を見つけた場合は、質問、プラットフォーム、回答、期待される根拠を記録し、メンテナーに共有してください。
