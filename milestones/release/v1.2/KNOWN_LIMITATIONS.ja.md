---
lang: ja
slug: known-limitations
order: 50
title: "既知の制約"
---

# 既知の制約

本ページは v1.2 の利用境界を説明します. 単なる不具合一覧ではなく, どの質問を直接確認でき, どの質問を公式ソースまたは内部手順で確認すべきかを判断するためのものです.

## 0. v1.2 監査範囲 (2026-05-19 更新)

v1.2 は v1.1 の Gemini 専用 system prompt 刷新 (v7.1 → v8.1, 422 → 525 行) です. ナレッジベース / 4 プラットフォーム uploads / 全メタ文書 / Claude / ChatGPT / NotebookLM の prompt はすべて byte-identical で v1.1 を継承しています.

### v1.2 で検証済み

- **SMOKE_V4 R3 (2026-05-19)** — v1.1 デプロイ後の 4 プラットフォーム × 17 問完全リグレッションテスト. 結果: Claude 17/17, ChatGPT 17/17, NotebookLM 15.5/17 (Q9 PUNT と Q11 PARTIAL は RAG アーキテクチャ制約), **Gemini v7.1: 13/17, 4 件 FAIL** (Q3 BE/BS/RELSPEC が AE へ話題ずれ; Q4 シナリオ A が IS の代わりに LB へ; Q11 Dataset-JSON が AE/CM へ話題ずれ; AHP1 LBCLINSIG が CM/MH へ話題ずれ). 独立レビュアー (`oh-my-claudecode:scientist`, Rule D #15) が 68/68 セル一致を確認.
- **Gemini v8.1 による R3 の 4 失敗題の dry-run (2026-05-19 16:35-16:40 PM)** — 4 件すべて Gemini 3.1 Pro (R3 ベースラインと同 model) で PASS. Q3/Q4/Q11/AHP1 は Rule D #17 レビュアー (`oh-my-claudecode:verifier`) APPROVE, 0 ブロッカー.
- **Rule A カバレッジ拡張** — v1.1 抽検時は N=5 KB ファイル (v1.1 audit から延期). v1.1 post-cut audit (2026-05-16) で **N=20 KB ファイル × 4 プラットフォーム = 124 grep probes, 100% PASS** に拡大.

### v1.2 で再評価しなかった項目 (v1.2 post-cut へ延期)

- **Gemini v8.1 の R4 17 問完全リグレッション** — v7.1 の 4 失敗題のみ再テスト, Gemini の 13 道の v7.1 PASS 題は v8.1 下で未テスト. CO-5 デフォルトリフレクション regex と候補数キャップは多変数題で未独立検証. リスク: 低 (v8.1 変更は anchor 拡張で PASS 題の核心 rule に影響しない) だが完全確認には R4 が必要.
- **M2 候補数キャップ独立検証** — 4 題の dry-run では候補数 < 5, threshold が真に発火せず. R4 の多変数題で検証予定.
- **BECAT EXTRACTION KB-prompt 注記** — v8.1 prompt L272 で `"EXTRACTION"` を BECAT 例に含めたが, KB BE / spec L111 は 3 つの標準例 (`COLLECTION` / `PREPARATION` / `TRANSPORT`) のみ inline. デプロイ回答は sponsor-extensible と注記済みだが, 将来の prompt 改訂で明示的な出典引用を追加し prompt-KB 乖離を防ぐことが可能.
- **Gemini の `04_business_scenarios_and_cross_domain.md`** — writer 手書きで v1.2 不変. 2026-05-16 post-v1.1 audit pass で監査済み, 追加対応不要.
- **06 P5 段階の 437 個の `UNSOURCED_MANUAL` 原子** — 最終確定していない. デプロイ回答には影響しないが, KB 内で出典が未検証のコンテンツを表す.
- **166 KB セクション Tier B 延期** — 56 個は兄弟ノード欠落, 110 個は内容切り詰め. 06 ディープ検証はカバレッジ gate (99.02%) 達成時に Tier A 修復のみ完了. これらのセクションの回答は他の領域より不完全な可能性があります. Tier B 修復は将来の KB pass で計画されています.

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
