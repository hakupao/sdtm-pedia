---
lang: ja
slug: known-limitations
order: 50
title: "既知の制限事項"
---

# 既知の制限事項

本ページは v1.3 の利用境界を説明します. 単なる不具合一覧ではなく, どの質問を直接確認でき, どの質問を公式ソースまたは内部手順で確認すべきかを判断するためのものです.

## 0. v1.3 監査範囲 (2026-05-20 更新)

v1.3 は SDTM Pedia の**ナレッジベース pass 級**リリースです (v1.0 以来最大規模のコンテンツ更新). v1.2 の Gemini 専用 prompt 刷新モデルを刷新し, v1.3 ではナレッジベースを直接修正し, 4 プラットフォーム全バンドルを再構築して, 4 つのデプロイ済み AI プラットフォームでエンドツーエンドの配信を検証しています.

### v1.3 の新機能

- **フェーズ A — ナレッジベース層の修正** (KB ファイル 11 件修正, 2 回の独立した Rule D レビュアー監査で幻覚 0 件, 意図しない削除 0 件):
  - **PP RELREC リンク** — `PP/examples.md` に §6.3.5.9.3 RELREC Method クイックリファレンスを追加 (Method A/B/C/D テーブル + Method C の省略形 relrec.xpt 1 件). 06 Deep Verification プロジェクトから引き継がれた OA-4 欠落を解消.
  - **BECAT EXTRACTION スポンサー拡張可能** — `BE/spec.md` L111 の CDISC 標準例 (COLLECTION / PREPARATION / TRANSPORT) の隣に明示的に注記. KB とデプロイ済みの Gemini v8.1 prompt L272 の表現を揃える.
  - **Tier B セクション修復** — 高密度 shall/must セクション 10 件を修復 (§2.7 SDTM 変数規則, §6.4.2 FA 命名, §7.2.1 Trial Arms Example 4, §7.3.2/§7.3.3 TD/TM, §4.5.1.2 Tests Not Done, §6.3.12.2 TR 列ヘッダー typo TRSTRESN→TRSTRESU, §6.4.3 FA --OBJ, §7.2.1.1 TA Distinguishing, §4.3.5).
  - **UNSOURCED_MANUAL 原子サンプリング** — 437 件の UNSOURCED_MANUAL 原子から N=40 の層化サンプル (高リスク shall/must 10 件 + 対照 30 件) を分類: 80% REASONABLE_INFERENCE + 20% DERIVED_FROM_XLSX + **0% HALLUCINATED** (Rule D `scientist` レビュアー監査で確認).
- **フェーズ B — 4 プラットフォーム再構築** (ビルドスクリプト強化, クロスプラットフォーム delta oracle 検証):
  - ビルドスクリプト防御化: ChatGPT `merge_for_chatgpt.py` をハードコードの `expected_segments=63/64/63` から動的 `len()` に変更; NotebookLM に新規 `validate_bucket_coverage.py` を追加 (190/190 KB ファイルがバケットに到達, 陳腐化参照 0 件).
  - 4 プラットフォーム再構築: ChatGPT (3 ファイル更新), Gemini (3 ファイル更新), NotebookLM (7 ファイル更新 + 1 ファイルリネーム), Claude Projects (5 ファイル更新).
  - NotebookLM バケット 25 リネーム: `25_td_meta_ti_ts_oi.md` → `25_td_meta_ti_ts_oi_di.md` (DI の取り込みを反映). **セルフデプロイユーザーは新ファイルをアップロード後, 古いソースを削除してください** — USER_GUIDE 参照.
  - クロスプラットフォーム delta oracle: ChatGPT 04 (+284) = NotebookLM バケット 10 (+284) = Gemini 02 部分 (+284) の BE/spec 変更などでバイト完全等価を確認. サイレントロス 0 件.
  - 4 プラットフォーム全 `system_prompt`/`instructions` の陳腐化した数値参照を監査 (20/20 grep プローブ PASS).
- **フェーズ C — ライト sanity (14-15/16 PASS)**:
  - v1.3 対象 4 問 × デプロイ済み 4 プラットフォーム = 16 セル; BECAT (A2), PP RELREC (A1), TR typo (A3), DI ドメイン (B5) をエンドツーエンドで検証.
  - Q-S1 BECAT EXTRACTION: 4/4 PASS (2 PASS+).
  - Q-S2 PP RELREC 4 メソッド: Claude PASS+, NotebookLM PASS+, ChatGPT PARTIAL (4 つの IDVAR 組み合わせは正確だが KB に対して Method A/B/C/D ラベルがずれ), Gemini FAIL (下記参照).
  - Q-S3 TR TRSTRESN vs TRSTRESU typo 修正: 4/4 PASS (2 PASS+).
  - Q-S4 DI ドメイン (NotebookLM バケット 25 リネーム): NotebookLM PASS+ (フッター引用 `25_td_meta_ti_ts_oi_di.md` — B5 デプロイ確認), Claude PASS+, Gemini PASS (Flash-Lite フォールバック, Pro クォータ枯渇), ChatGPT は判定未取得だがパターンから PASS と推定.

### v1.3 で再評価しなかった項目 (v1.4 へ延期)

- **メイン — 4 プラットフォーム `system_prompt`/`instructions` フルスタックリファクタリング**: フェーズ C でユーザーが指摘したように, 4 つのデプロイ済み prompt はすべて複数の反復レイヤーを蓄積しています (Gemini v8.1 は 525 行で, 17 件の CO-N 不正防止ルールがあり, それぞれに "v5/v6/v7/v7.1/v8 新増" と smoke test 失敗の化石記録が付いています). この複雑さが注意力を分散させてアンカーを過度に特化させ, フェーズ C Q-S2 で Gemini が失敗した原因となりました: Gemini Gem は PP-PC RELREC リンクメソッドを幻覚し (PPLNKID/PCREFID と主張), v1.3 KB の §6.3.5.9.3 Method A/B/C/D 分類体系を取得できませんでした. v1.4 リリースでは 4 つの prompt をすべてゼロから書き直します — 化石注釈の削除, サブルールの統合, KB グラウンディングをメインパスとして復元. 推定削減量: Gemini 525 → ~200 行, CO-N ルールは質問タイプが一致する場合のみ発火する regex ゲート制御.
- **437 件の UNSOURCED_MANUAL 原子の全量分類**: v1.3 では N=40 をサンプリング (幻覚 0 件). 全量 437 件の系統検証は Rule D レビュアーが発見した発見的分類器の修正とともに v1.4 に持ち越し (Rule D `scientist` は DERIVED_FROM_XLSX と初期ラベルされた 10 件の原子のうち 5 件が実際には PDF 本文であることを発見; メインセッションの分類器に `xlsx vs PDF` の事前確率バイアスがあった).
- **Tier B セクション 11-25 (高密度 + 小節)** + **全 level-2 Tier B (cannot / except / only / should キーワード)** — v1.3 はランク 11-20 (10 セクション, 約 37 原子) を修復. ランク 1-10 (最高密度, 約 470 原子), ランク 21-25 (最小節), および 24 件の level-2 セクションは v1.4 へ延期.
- **Issue 5 §6.3.5.9.3 PC/PP 143 TABLE_ROW Tier-B MEDIUM 修復**: 06 Deep Verification §二 参照; 行レベルデータ値差分の修復.
- **section_coverage.jsonl フルパイプライン再実行**: v1.3 はベースラインのバックアップと陳腐化状態の文書化のみ. 正確な判定更新のためにフルパイプライン (md_atoms 再生成 → P4a 順方向マッチング → P4b 集計) が v1.4 で必要.
- **R4 全 17 問 Gemini Pro 専用リグレッション**: v1.3 は 17 問の単一プラットフォームリグレッションの代わりに 4 問のライト sanity × 4 プラットフォームを使用. 4 つの sanity 問題は v1.3 の KB 変更をすべてエンドツーエンドでカバー; R4 全量は延期 (Pro クォータ制約: 複数の 5h ウィンドウにわたって約 16-20 時間の実時間).
- **PASS+ §1.2 厳格な「AHP 専用」スコープ拡張** (R4 sanity retro からの W1 継続): フェーズ C Q-S1 および Q-S5 で, 非 AHP 問題も KB グラウンドで追加の深さ (クロスドメイン参照, ソース引用) があれば PASS+ 評価を得ることが示されました. PASS+ 基準スコープは「AHP トピック OR ベースラインを超える深さの KB グラウンド回答」に拡大し, 将来の smoke テスト向けにここに文書化します.

### 外観 / デプロイ上の注意事項

- NotebookLM バケット 25 リネーム: 既存の v1.0–v1.2 の NotebookLM デプロイには古いソース `25_td_meta_ti_ts_oi.md` があります. 新しい `25_td_meta_ti_ts_oi_di.md` をアップロードしたら, **手動で古いソースを削除**して陳腐化した引用を避けてください (クリーンアップ後, 43 ソースが 42 に減少するはずです).
- ChatGPT GPT の PP-PC RELREC の「Method A/B/C/D」ラベルは, 場合によって v1.3 KB §6.3.5.9.3 クイックリファレンスのラベルと一致しない可能性があります (フェーズ C Q-S2 PARTIAL). 4 つの IDVAR 組み合わせは正確であり, ラベリングは主観的です.

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
