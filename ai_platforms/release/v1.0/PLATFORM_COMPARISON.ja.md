---
lang: ja
slug: compare
order: 20
title: "4 プラットフォーム多次元比較"
---

# 4 プラットフォーム多次元比較

> 4 プラットフォームを 9 つの次元で横断比較します。データスナップショット: 2026-04-27 v1.0.

## 1. 評価スコア (smoke v4 / 17 問)

| プラットフォーム | スコア | バージョン | 主な失点 |
|---|:---:|:---:|---|
| Claude Projects | 17/17 (100%) | v2.6 | なし |
| ChatGPT GPTs | 16.5/17 (97%) | v2.2 LIVE | Q1 GFINHERT スペル (v2.2 適用後に修正済み); 長尾 chunk のテーブル中段が miss される場合あり |
| Gemini Gems | 16/17 (94%) | v7.1 LIVE | Q10 SUPP-- Core anchor (v7.1 適用後に修正済み); R1 65% → R2 94% (v6→v7 アップグレード) |
| NotebookLM | 15/17 (88%) | v1.0 / Custom mode | Q9 Pinnacle 21 / Q11 Dataset-JSON / Q12 CT version の 3 問が PUNT (in-KB-only アーキテクチャ上の制限、安全動作でありバグではありません) |

## 2. 容量上限

| プラットフォーム | 容量上限 | 現在の使用量 | 余裕 |
|---|---|---|---|
| Claude Projects | 1.29M tokens (Pro ソフトリミット付近) | 19 ファイル / 77% | 約 23%、新規ファイル追加時は低優先度ファイルのダウングレードが必要 |
| ChatGPT GPTs | 20 ファイルのハード上限 | 9 ファイル (マージ後、例: 04_domain_specs_all.md) | 11 ファイルの headroom |
| Gemini Gems | 1M tokens コンテキストウィンドウ | 4 ファイル (最も積極的なマージ) | ウィンドウ余裕は十分、コールドスタート時の最初の token はやや遅い |
| NotebookLM | 50 source ハード上限 (Pro プラン) | 42 source | 8 source headroom |

## 3. チーム共有方式

| プラットフォーム | 共有方式 | 審査の要否 |
|---|---|---|
| Claude Projects | Organization / Project 招待 (Team / Enterprise プランで Project を共有; Pro ユーザーは各自が再デプロイが必要) | 該当なし (内部直接招待) |
| ChatGPT GPTs | Custom GPT を organization に共有 (審査不要) または GPT Store 公開 (OpenAI review が必要) | Store 公開のみ審査あり |
| Gemini Gems | Workspace プラン: Daisy が直接共有; 個人アカウント: 同僚が各自でセルフデプロイ (完全な v7.1 system prompt を貼り付け) | 該当なし |
| NotebookLM | メール招待で notebook に参加 (Pro / Workspace)、または同僚が自己構築 (50-source cap) | 該当なし |

## 4. サブスクリプション要件

| プラットフォーム | 対応プラン | Free プランで利用可能か |
|---|---|:---:|
| Claude Projects | Claude Pro / Team / Enterprise | 否 |
| ChatGPT GPTs | ChatGPT Plus / Team / Enterprise | 否 |
| Gemini Gems | Gemini Advanced 個人 / Google Workspace | 否 |
| NotebookLM | NotebookLM Pro / Google Workspace | 否 (50-source cap は Pro / Workspace プランのみ) |

## 5. インターネット接続

| プラットフォーム | インターネット接続 | デフォルト状態 |
|---|---|---|
| Claude Projects | 手動で web search を有効化可能 | デフォルト OFF、必要に応じて切替 |
| ChatGPT GPTs | 手動で web browsing を有効化可能 | デフォルト OFF、必要に応じて切替 |
| Gemini Gems | 手動で有効化可能 (Google Search 統合) | デフォルト OFF、必要に応じて切替 |
| NotebookLM | 厳格な in-KB-only (42 source 内のみ、インターネット接続なし) | 設計上の仕様であり、バグではありません; KB 外の質問は積極的に PUNT |

## 6. アンチハルシネーション傾向

| プラットフォーム | アンチハルシネーション強度 | メカニズム |
|---|:---:|---|
| Claude Projects | 強い | 多段階推論 + system prompt anti-fabrication anchor + Stage 6 Deferred Stub ルール |
| ChatGPT GPTs | 中 | system prompt 誘導 + v2.2 適用後の GFINHERT 精確変数検証; 長尾 chunk で miss される場合あり |
| Gemini Gems | やや強い (v7.1 以降) | v6→v7 アップグレードで AHP guardrail 追加、R1→R2 スコアが 65% から 94% に向上; 同僚デプロイ時は完全な v7.1 system prompt の貼り付けが必要 |
| NotebookLM | 非常に強い | in-KB-only アーキテクチャが天然のアンチハルシネーション; 42 source 外の質問は捏造より拒答を優先; inline citation による逆引き確認 |

## 7. ファイル数制限

| プラットフォーム | ファイル数制限 | 現在のファイル数 |
|---|---|:---:|
| Claude Projects | token 容量によるソフト上限 (~77% 使用済み / 1.29M tokens) | 19 |
| ChatGPT GPTs | 20 ファイルのハード上限 | 9 |
| Gemini Gems | 明示的なファイル数制限なし (1M token ウィンドウによる制約) | 4 |
| NotebookLM | 50 source ハード上限 (Pro) — §2 参照 | 42 |

## 8. 最も得意なシナリオ

| プラットフォーム | 最も得意なシナリオ |
|---|---|
| Claude Projects | 精確な変数 + 多段階推論 (Core + C-code + クロスドメイン変数、例: PCTPT 5 点セット); 誤った前提の訂正 (SUPPTS); ドメイン境界の判定 |
| ChatGPT GPTs | 全ドメイン照会; チーム共有 / GPT Store 公開; 組織内共有は審査不要 |
| Gemini Gems | 大量コンテキストの一括入力 / クロスドメインパターン比較; 長いセッション; 広範囲の探索; 4 ファイルの深度マージ |
| NotebookLM | 強いアンチハルシネーション (監査 / コンプライアンス); inline citation による逆引き確認; 捏造より拒答を優先; クロスドメイン死亡日レベル整合と v3.4 新ドメイン PASS+ |

## 9. 最も苦手なシナリオ

| プラットフォーム | 最も苦手なシナリオ |
|---|---|
| Claude Projects | リアルタイムのインターネット接続 (FDA / Pinnacle 21 は cdisc.org での手動確認が必要); 超大量ドメインの一括比較; 容量が 77% で Pro ソフトリミットに近い |
| ChatGPT GPTs | 多段階推論は Claude よりやや劣る; Free アカウントでは入口が見つからない; 長尾 chunk のテーブル中段が miss される場合あり |
| Gemini Gems | 個人アカウントではチームへの直接共有ができない (Workspace が必要); 同僚がセルフデプロイする際は完全な v7.1 system prompt を貼り付けないと AHP guardrail が失われる |
| NotebookLM | 42 source 外の質問 (リアルタイムの Pinnacle 21 / 最新ニュース / Dataset-JSON v1.1 / CT version locking + MedDRA) は積極的に PUNT — 設計上の仕様であり、バグではありません |

---
*v1.0 — 2026-04-27 — メンテナー: Daisy*
