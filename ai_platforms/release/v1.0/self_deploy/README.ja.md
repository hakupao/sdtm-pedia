# セルフデプロイガイド — SDTM AI ナレッジベース v1.0

> 自分で環境を構築したい方向けです。4 プラットフォームはそれぞれ独立してデプロイでき、30〜60 分で公開できます。

## 1. どのプラットフォームでデプロイすべきですか?

| プラットフォーム | デプロイ時間 | プラン要件 | チーム共有方式 |
|---|:---:|---|---|
| **NotebookLM** | ~30 min | Pro / Workspace | notebook 招待 (50-source cap) |
| **Gemini Gems** | ~30 min | Advanced / Workspace | 個人では直接共有不可、Workspace が必要 |
| **ChatGPT GPTs** | ~45 min | Plus / Team / Enterprise | organization 内は審査不要、GPT Store は review が必要 |
| **Claude Projects** | ~60 min | Pro / Team / Enterprise | Team/Enterprise で共有可、Pro は各自で再デプロイ |

判断ツリー (USER_GUIDE.ja.md §3 と同一): 最速を求める場合 (~30 min) → NotebookLM または Gemini; 最も深い RAG を求める場合 → Claude Projects; チーム共有を求める場合 → ChatGPT GPTs; 最強の anti-hallucination を求める場合 → NotebookLM.

## 2. 4 プラットフォーム デプロイチュートリアル (独立, 1 つ選んで実行)

- **Claude Projects** → [./claude_tutorial.ja.md](./claude_tutorial.ja.md) (19 ファイル + system_prompt + 24 題 smoke)
- **ChatGPT GPTs** → [./chatgpt_tutorial.ja.md](./chatgpt_tutorial.ja.md) (Custom GPT + 9 ファイル + v2.2 system prompt + 17 題 smoke)
- **Gemini Gems** → [./gemini_tutorial.ja.md](./gemini_tutorial.ja.md) (Gem + 4 統合ファイル + v7.1 system prompt + AHP 検収)
- **NotebookLM** → [./notebooklm_tutorial.ja.md](./notebooklm_tutorial.ja.md) (notebook + 42 sources + Custom mode 9011 chars + 3 段階共有)

## 3. 共通の前提準備

1. 本リポジトリを `git clone` してローカルに展開し、ルートディレクトリに移動します。
2. 対象プラットフォームの `ai_platforms/{claude_projects,chatgpt_gpt,gemini_gems,notebooklm}/current/` を参照してください (dev/ や archive/ からはコピーしないでください)。
3. §1 の表に従い、アカウントとプランを準備します。
4. §2 の該当 tutorial を開き、章の順序を**厳守して**実行してください (手順をスキップすると system_prompt のゲートルールが失われます)。

## 4. デプロイ後の検証 (smoke test)

デプロイ完了後、`../DEMO_QUESTIONS.md` の D0・D1・D5 の 3 問で簡易検収を行います (所要時間 約 5 分):

- **D0**: AESER 基本クエリ (AE / Exp / C66742 NY) — 基本 RAG の検証。
- **D1**: GF ドメイン EGFR シナリオ (GFGENSR / GFPVRID / GFGENREF / GFINHERT) — 新ドメイン + 多変数推論の検証。
- **D5**: SUPPTS 前提誤り訂正 — anti-hallucination ゲートの検証 (能動的に誤りを検出し → TSVAL1-n を返すこと)。

3 問すべて PASS = デプロイ成功。1 問でも PASS しない場合は `../KNOWN_LIMITATIONS.en.md` でトラブルシューティングしてください。優先確認事項: (a) system_prompt.md が完全にペーストされ途中で切れていないか、(b) uploads/ のファイル数とサイズがチュートリアルの一覧と合致しているか。

## 5. アップグレード / メンテナンス

ソースリポジトリは今後も更新されます: minor release (`../CHANGELOG.md` に v1.1 / v1.2 と記載) または SDTMIG 新版 (v3.5+) のタイミングです。再アップロード手順: `git pull` → `current/` に移動 → 旧 uploads を削除して再アップロード → **新しい system_prompt.md を完全にコピー&ペースト** (途中で切断すると AHP ゲートルールが失われます。例: Gemini v7.1 CO-1d SUPPQUAL ハードアンカー + ChatGPT v2.2 v3.4 新ドメイン変数名検証)。ロールバック: 各プラットフォームの `dev/archive/drafts/` に過去バージョンが保存されています。

## 6. フィードバック

誤りや幻覚を発見した場合: (1) スクリーンショットを撮り、質問の原文と AI の回答を保存します; (2) プラットフォーム + バージョン (例: "ChatGPT GPT v2.2 LIVE 2026-04-24") + 期待される回答 (SDTMIG v3.4 章番号または CDISC CT C-code を引用) + セルフデプロイバージョン番号 + smoke スコアを添付します; (3) メールで Daisy に連絡 / issue tracker / 部門グループチャットで @Daisy。内容は `../CHANGELOG.md` に集約し、次の minor release で対応します。
