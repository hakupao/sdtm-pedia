---
lang: ja
slug: readme
order: 0
title: "README"
---

# SDTM AI ナレッジベース v1.0 — 社内公開版

> 2026-04-27 / 4 AI プラットフォーム LIVE / ユーザーマニュアル + セルフデプロイチュートリアル完備

## ドキュメントナビゲーション

- [USER_GUIDE.ja.md](./USER_GUIDE.ja.md) — 利用者向けメインマニュアル (背景 / デシジョンツリー / 入口 / 制限事項 / フィードバック)、初回利用時は必読です
- [DEMO_QUESTIONS.md](./DEMO_QUESTIONS.md) — デモ用 10 題パック (3 言語の設問 + 英語判定基準)
- [KNOWN_LIMITATIONS.en.md](./KNOWN_LIMITATIONS.en.md) — 既知の制限事項完全版 (L1-L3 クロスプラットフォーム + L4 各プラットフォーム)
- [CHANGELOG.md](./CHANGELOG.md) — バージョン履歴 + smoke v4 ベースライン (Claude 17/17 / ChatGPT 16.5/17 / Gemini 16/17 / NotebookLM 15/17)
- [self_deploy/](./self_deploy/) — 4 プラットフォーム個別デプロイチュートリアル
- 多言語切替の詳細: 下記セクション参照

## 多言語切替

中国語 (zh) / 英語 (en) / 日本語 (ja) の 3 言語に対応しています。3 言語完備のドキュメント: トップレベル README / USER_GUIDE / self_deploy/README + 4 プラットフォームチュートリアル。英語のみのドキュメント: DEMO_QUESTIONS.md (設問は 3 言語埋め込み、判定基準は英語の SDTM 用語をそのまま使用) / KNOWN_LIMITATIONS.en.md / CHANGELOG.md。ファイル名のサフィックスで言語を識別します: `*.zh.md` / `*.en.md` / `*.ja.md`。

## クイックスタート (60 秒)

1. [USER_GUIDE.ja.md](./USER_GUIDE.ja.md) §3 のデシジョンツリーでプラットフォームを選択してください (どれを選ぶか迷う場合 → Claude Projects をお勧めします)。
2. [DEMO_QUESTIONS.md](./DEMO_QUESTIONS.md) から任意の 3 題を試してください (D0 + D1 + D5 を推奨)。
3. フィードバックを Bojiang Zhang へお送りください。

## セルフデプロイ

ご自身で環境を構築される場合は [self_deploy/README.ja.md](./self_deploy/README.ja.md) をご参照ください。各プラットフォームの独立したチュートリアルが掲載されています。
