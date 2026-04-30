---
lang: ja
slug: changelog
order: 60
title: "変更履歴"
---

# 変更履歴 — SDTM AI ナレッジベース リリース

## v1.0 — 2026-04-27 (社内リリース)

### 追加

- 4 プラットフォーム向けデプロイパッケージを公開:
  - Claude Projects v2.6
  - ChatGPT GPTs v2.2 LIVE
  - Gemini Gems v7.1 LIVE
  - NotebookLM Custom mode
- 3 言語の onboarding ドキュメントを公開:
  - `README`
  - `USER_GUIDE`
  - `PLATFORM_COMPARISON`
  - `DEMO_QUESTIONS`
  - `GLOSSARY`
  - `METHODOLOGY`
  - `KNOWN_LIMITATIONS`
- 同僚が短時間でデプロイ品質を確認できる 10 問 demo set (D0-D9) を公開。
- 各プラットフォームの self-deploy tutorial を公開し、ファイルアップロード、prompt 設定、smoke test 手順を整理。

### 品質ベースライン (17 問評価、R1+R2)

| プラットフォーム | スコア | 状態 |
|---|:---:|---|
| Claude Projects | 17/17 | LIVE |
| ChatGPT GPTs | 16.5/17 | LIVE |
| Gemini Gems | 16/17 | LIVE |
| NotebookLM | 15/17 | LIVE |

### 方法論リファレンス

- 完全な方法論と検証説明は `METHODOLOGY` を参照。
- 既知の制約と回避策は `KNOWN_LIMITATIONS` を参照。
- 各プラットフォームのデプロイ境界と適用シナリオは `PLATFORM_COMPARISON` を参照。

### ソース知識ベース

- ソース内容は CDISC SDTMIG v3.4、SDTM Model v2.0、CDISC Controlled Terminology に基づきます。
- リリースパッケージは CDISC 原資料を再配布しません。
- 知識ベース内容は repo 内で traceable に保たれ、`knowledge_base/` と検証記録まで監査可能です。

### リリース成果物

- 4 つの zip bundle は GitHub releases で配布。
- Web サイトは 3 言語の landing、ドキュメント、比較表、ダウンロード入口を提供。

### 既知の制約

- QS long-tail codelist は完全カバーではありません。
- 巨大 codelist は完全 term 展開ではなく stub + NCI EVS pointer を使用します。
- NotebookLM は in-KB-only アーキテクチャのため、リアルタイム Web 内容には PUNT します。

## プレリリース履歴 (概要)

- 知識ベース構築と検証を完了。
- 4 プラットフォームのデプロイを完了。
- 17 問 baseline テストを完了。
- v1.0 release package と同僚向け onboarding 文書を完了。
