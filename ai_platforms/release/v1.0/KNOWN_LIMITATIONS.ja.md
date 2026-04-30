---
lang: ja
slug: known-limitations
order: 50
title: "既知の制約"
---

# 既知の制約 — SDTM AI ナレッジベース v1.0

> 本ページは現在版の制約をまとめたものです。各制約について、影響するプラットフォーム、証拠/再現方法、推奨回避策を記載します。

## プラットフォーム横断の制約

### L1 — Questionnaires (QS) codelist のカバレッジが不完全

**影響**: 4 プラットフォームすべて。Claude Projects v2.6 で最も顕著。
**詳細**: 296 個の長尾 QS codelist (PROMIS / EORTC item-bank 系) は容量制約により、いずれのデプロイでも完全展開されていません。Claude Projects は QS codelist の約 55.8% をカバーし、残りは NCI EVS Browser リンクへのフォールバックです。
**回避策**: カバー範囲外の QS codelist を照会する場合は、AI に NCI EVS Browser URL を示させてください。AI は stub しか保持していないことを認識する必要があります。Phase 7 の self-hosted RAG でこのギャップを解消予定です。

### L2 — 巨大 codelist (LB / MedDRA 級) は完全 term 一覧ではなく stub として返される

**影響**: 4 プラットフォームすべて。
**詳細**: LB Test Code C65047 (2,536 terms) など 6 つの巨大 codelist は、全 term を列挙せず stub-with-pointer として保持しています。"C65047 の全 terms を列挙して" と聞いた場合、stub 宣言 + NCI EVS Browser リンクを返すべきであり、term list を捏造してはいけません。
**回避策**: この挙動は許容されます。ここで platform が terms を捏造する場合は、system prompt の Stage 6 Deferred Stub ルール (Claude) または同等の anti-fabrication anchor を再確認してください。

### L3 — リアルタイム Web 照会 (FDA / Pinnacle 21 / dbSNP / NCI EVS) は埋め込まれていない

**影響**: NotebookLM (in-KB-only アーキテクチャ)。ChatGPT/Gemini/Claude は、Web search が有効であれば検索可能。
**詳細**: Dataset-JSON catalog status や Pinnacle 21 rule release notes など変化する標準情報について、KB 内容は 2026-04-22 baseline 時点を反映しています。
**回避策**: 時間依存の回答は CDISC.org / FDA.gov / standards.pinnacle21.certara.net で手動確認してください。AI は通常ソースを引用しますが、引用が 6 か月以上古い場合は再確認が必要です。

## プラットフォーム別制約

### Claude Projects (v2.6)

- **L4-Cl1**: 容量は約 77% (1.29M tokens / 19 files)。paid-tier soft cap に近づいています。さらに内容を追加するには、既存の低優先度ファイルを削除する必要があります (UPLOAD_TUTORIAL §8 downgrade path を参照)。
- **L4-Cl2**: Indexing indicator は信頼性が低いです。UI に "Indexing" と表示されていても、新しい内容にクエリがヒットする場合があります。待たずに smoke questions で直接テストしてください。
- **L4-Cl3**: 公開共有リンクはありません。Team/Enterprise plan メンバーは同じ Project を共有できますが、Pro plan ユーザーは個別に再デプロイする必要があります。

### ChatGPT GPTs (v2.2 LIVE)

- **L4-CG1**: 20-file hard limit。現在のデプロイは 9 files を使用しており、拡張余地があります。ソースファイルは統合済みで、例として 63 domain specs は `04_domain_specs_all.md` に統合されています。
- **L4-CG2**: File search RAG chunk strategy はユーザー設定できません。長尾 terminology query は、表の中ほどに埋もれている場合 miss chunks になる可能性があります。
- **L4-CG3**: GPT Store 公開には OpenAI review が必要です。Custom GPT は org/team に review なしで共有できるため、社内利用ではこちらを推奨します。

### Gemini Gems (v7.1 LIVE)

- **L4-GE1**: アップロードファイルは 4 個のみで、最も積極的に統合されています。大きな context window で補えますが、cold session では first-token latency が遅くなる場合があります。
- **L4-GE2**: 個人アカウントに紐づきます。Gem は標準ではチーム共有できません (Workspace plan では一部共有機能があります)。各同僚が self-deploy します。
- **L4-GE3**: Claude/NotebookLM と比べ、反ハルシネーション baseline は弱めです。R1→R2 upgrade (v6→v7 system prompt) により 65% から 94% に改善しました。**同僚がデプロイする場合は、v7.1 system prompt を逐語的に使用する必要があります**。

### NotebookLM

- **L4-NB1**: 50-source hard cap (Pro plan)。現在は 42/50 で、8 source の余裕があります。
- **L4-NB2**: 設計上 in-KB-only です。42 sources に含まれない内容、例えばデプロイ日以降の breaking news には回答できません。一方で、自然な anti-hallucination protection が得られます。
- **L4-NB3**: Q9 (Pinnacle 21 categories) は PUNT。NotebookLM は Pinnacle 21 Webpage から推測せず、「この knowledge base にはない」と安全に宣言します。これは**正しい安全挙動**であり、bug ではありません。
- **L4-NB4**: Sources panel ≠ Chat。質問は Chat (mat-input-0) に入力し、"Discover sources" search には入力しません。
- **L4-NB5**: Q11 (Dataset-JSON v1.1) と Q12 (CT version locking + MedDRA) は PARTIAL。42 sources の範囲外の補足テーマです。PUNT が安全な回答であり、platform が自信を持って答える場合は注意してください。

## 問題タイプ別パフォーマンス参考

SMOKE_V4 R1+R2 結果 (2026-04-22 から 2026-04-24) に基づきます:

| 問題タイプ | Claude | ChatGPT | Gemini (R2) | NotebookLM |
|---|:---:|:---:|:---:|:---:|
| 新ドメイン (GF/CP/BE/BS) | PASS+ | PASS | PASS | PASS+ |
| ドメイン境界 (LB/MB/IS) | PASS+ | PASS | PASS+ | PASS |
| Timing model (--TPT) | PASS | PASS | PASS | PASS |
| CT mechanism (Ext + dictionary) | PASS+ | PARTIAL→PASS (post v2.2) | PASS | PASS+ |
| 前提訂正 (SUPPTS) | PASS+ | PASS | PASS+ (post v7.1) | PASS+ |
| anti-hallucination (LBCLINSIG) | PASS+ | PASS | PASS+ (post v7) | PASS+ (in-KB-only) |
| anti-hallucination (SAE Aggregate) | PASS | PASS | PASS+ | PASS+ |
| deprecated PF | PASS+ | PASS | PASS+ | PASS+ |
| クロスドメイン死亡時刻 | PASS+ | PASS | PASS | PASS |
| リアルタイム / 補足テーマ (Q11/Q12) | PASS | PASS | PARTIAL | PUNT (正しい) |

## 新しい制約の報告

本ページにないハルシネーション、事実誤り、または scope gap を発見した場合:
1. 完全な質問 + AI 回答を保存してください (スクリーンショット + テキスト)。
2. プラットフォーム + バージョンを記録してください。例: "ChatGPT GPT v2.2 LIVE 2026-04-24"。
3. Bojiang Zhang にメールするか、project tracker issue を作成して上記を添付してください。
4. expected vs actual を含め、SDTMIG v3.4 spec section または CDISC CT C-code を引用してください。

これらは次の minor release に向けて `./CHANGELOG.md` で追跡します。
