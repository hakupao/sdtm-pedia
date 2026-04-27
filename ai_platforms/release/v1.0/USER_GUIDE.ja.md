# SDTM AI ナレッジベース — ユーザーマニュアル v1.0

## 1. これは何ですか (プロジェクト背景)

CDISC 臨床試験データ集計標準 (SDTM) の変数定義 / Core 属性 / codelist を確認する際、SDTMIG v3.4 PDF と NCI EVS Browser を参照すると 10 分以上かかることがよくあります。本プロジェクトはこれらの資料を整理し、4 つの AI プラットフォーム (Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM) に展開しました。自然言語で質問するだけで、**spec 引用付きの回答を 1 分以内に取得できます**。

技術背景: SDTM (Study Data Tabulation Model) は 63 ドメイン + 数千の変数 + 大量の CT (Controlled Terminology) を含みます。CDISC SDTMIG v3.4 + v2.0 model + CDISC CT を 295 個の Markdown ソースに整理し、プロンプトエンジニアリングを加えて 4 プラットフォームに投入しました。RAG / system prompt / Core (Req/Exp/Perm) / Extensible / アンチハルシネーション探針 などの用語が不明な場合は [`./GLOSSARY.ja.md`](./GLOSSARY.ja.md) (1 ページ早見表) をご参照ください。

## 2. 成果概要 (技術ハイライト)

各プラットフォームに 17 問の代表的な SDTM 問題で完全評価を実施しました。3 問は『誤った前提を含むアンチハルシネーション探針』で、AI が誤前提を見破るかどうかをテストします。4 プラットフォームのスコアは以下の通りです:

| プラットフォーム | 17 問スコア | バージョン | 強み |
|---|:---:|:---:|---|
| Claude Projects | 17/17 (100%) | v2.6 | 変数精度 + 多段階推論 |
| ChatGPT GPTs | 16.5/17 (97%) | v2.2 LIVE | 全量対応 + チーム/Store 共有可能 |
| Gemini Gems | 16/17 (94%) | v7.1 LIVE | 長コンテキスト + 広範囲な探索 |
| NotebookLM | 15/17 (88%) | Custom mode | in-KB-only によるアンチハルシネーション |

ハイライト: v3.4 新ドメイン (GF / CP / BE / BS) + Timing + CT Extensible + SUPPQUAL scope + クロスドメイン死亡日レベル整合 + アンチハルシネーション問題 3 問 (LBCLINSIG / Trial-Level SAE Aggregate / PF 廃止ドメイン)。全工程で内部 4 つの品質規則 + 累計 28 名の独立 reviewer による検証を実施しています。参照元: `./CHANGELOG.md` + `../../SMOKE_V4.md` §3。用語集: [`./GLOSSARY.ja.md`](./GLOSSARY.ja.md)

## 3. どのプラットフォームを使うべきですか? (判断ツリー)

| 目的 | 推奨プラットフォーム | 理由 |
|---|---|---|
| 変数の精度重視 + 多段階推論 (Core + C-code + クロスドメイン変数) | **Claude Projects** | 1.29M tokens フル搭載、smoke 満点 |
| チーム / 部門内共有、または GPT Store 公開 | **ChatGPT GPTs** | 組織内共有は審査不要、Store は OpenAI review が必要 |
| 長コンテキスト + 一度に広範囲を探索 / クロスドメインパターン比較 | **Gemini Gems** | 1M ウィンドウ、4 ファイル深度マージ |
| 100% アンチハルシネーション (回答拒否は捏造より望ましいです) + 強力な citation | **NotebookLM** | in-KB-only、42 sources に含まれない質問は PUNT |

簡単な選び方: どれを選べばよいか分からない → Claude Projects。同僚と一緒に使いたい → ChatGPT GPTs。ハルシネーションが心配 → NotebookLM。詳細な比較は `../README.md` の「4 プラットフォーム役割分担」表をご参照ください。

## 4. 4 プラットフォームへのアクセス

### 4.1 Claude Projects (入門におすすめ)

- **アクセス方法**: Daisy から organization への招待をお待ちください。メールのリンクから参加できます。
- **URL**: claude.ai → Projects → "SDTM Knowledge Base" (具体的な URL は Daisy から個別にお送りします)。
- **プラン要件**: Claude Pro / Team / Enterprise。
- **適したシナリオ**: 変数の Core + CT バインド精度が必要な場合 / クロスドメイン変数推論 (PCTPT 5 点セット) / 誤った前提の訂正 (SUPPTS)。
- **適さないシナリオ**: リアルタイムでの FDA / Pinnacle 21 情報取得 (cdisc.org での手動確認が必要)、超大量ドメインの一括比較。

### 4.2 ChatGPT GPTs

- **アクセス方法**: Daisy が Custom GPT を organization に共有します。「自分の GPTs に追加」してください。
- **URL**: chatgpt.com → 上部ドロップダウン → "SDTM Knowledge Base"。
- **プラン要件**: ChatGPT Plus / Team / Enterprise (Free プランは不可)。
- **適したシナリオ**: 全ドメインの照会 / チーム共有 / GPT Store への OpenAI review 経由での公開。
- **適さないシナリオ**: 多段階推論は Claude よりやや劣ります。Free アカウントでは入口が見つかりません。

### 4.3 Gemini Gems

- **アクセス方法**: Daisy が共有 (Workspace 経由) するか、個人で自己展開します。
- **URL**: gemini.google.com → Gems → "SDTM Knowledge Base"。
- **プラン要件**: Gemini Advanced 個人 / Google Workspace。
- **適したシナリオ**: 大量のコンテキストを一度に扱う場合 / クロスドメインパターン比較 / 長いセッション。
- **適さないシナリオ**: 個人アカウントではチーム直接共有ができません (Workspace が必要です)。

### 4.4 NotebookLM

- **アクセス方法**: Daisy から notebook への招待を受けるか、自己構築 (50 ソースの上限あり) します。
- **URL**: notebooklm.google.com → "SDTM Knowledge Base"。
- **プラン要件**: NotebookLM Pro / Google Workspace。
- **適したシナリオ**: 強いアンチハルシネーション性が必要な場合 (監査 / コンプライアンス) / inline citation による逆引き確認 / 回答拒否は捏造より望ましいです。
- **適さないシナリオ**: 42 ソースに含まれないトピック (リアルタイムの Pinnacle 21 情報 / 最新ニュース) については回答を拒否します。これは設計上の動作であり、バグではありません。

## 5. 5 分間クイックスタート (3 問ウォームアップ)

よく使うプラットフォームを開き (まず Claude Projects を推奨)、以下の 3 問を順番に質問してください。回答は `./DEMO_QUESTIONS.md` の Expected と照らし合わせてご確認ください。

1. **D0 (ウォームアップ)**: "AESER は SDTMIG v3.4 のどのドメインのどの変数ですか? Core は何ですか? バインドされている CT C-code は何ですか?" 期待回答: AE ドメイン / Serious Event / Exp / C66742 NY {Y/N/U/NA}。
2. **D1 (新ドメイン)**: DEMO_QUESTIONS.md の D1 の質問文をコピーして貼り付けてください (EGFR / Exon 19 / dbSNP に関する問題です)。期待回答: Domain=GF、GFGENSR / GFPVRID / GFGENREF / GFINHERT が答えられること。
3. **D5 (誤前提の訂正)**: "SUPPTS は SDTM 標準の何ですか? QORIG は必須ですか?" 期待回答: "SUPPTS は SDTMIG v3.4 に存在しない" と自発的に指摘し、TSVAL1-TSVALn に誘導すれば PASS+。

判定基準: 核心的な事実 (ドメイン / 変数 / Core / C-code) がすべて正確 = PASS。誤った前提を自発的に指摘 = PASS+。誤った前提を受け入れて回答を作成 = FAIL。

## 6. 完全 demo パッケージ (10 問)

10 問フルセットは `./DEMO_QUESTIONS.md` に収録されています (3 言語の質問文 + 英語の判定基準)。5 分間入門版 = D0 / D1 / D5。30 分間フル実施版 = D0 → D9 (AHP 3 問: D6 LBCLINSIG / D7 SAE Aggregate / D8 PF 廃止ドメイン + クロスドメイン最終問題 D9 AE/MH/CE + DS 死亡日レベル整合を含む)。実施後は §2 のベースライン (17/17 / 16.5/17 / 16/17 / 15/17) と照らし合わせ、各プラットフォームの精度をご確認ください。

## 7. 既知の制限 (よくある質問)

完全版は `./KNOWN_LIMITATIONS.en.md` をご覧ください。以下は日本語での要約です。

- **L1 — QS codelist の不完全収録**: 296 件の長尾 questionnaire codelist (PROMIS/EORTC 等) は容量制約により全展開できていません (Claude は約 55.8%)。それ以外は NCI EVS Browser へのリンクで対応しています。
- **L2 — 大規模 codelist は stub 形式**: LBTESTCD (2,536 term) など 6 テーブルは stub + ポインタのみを格納しており、term の生成はできません。
- **L3 — リアルタイム接続**: NotebookLM は厳密に in-KB-only のため、最新ニュースや最新の Pinnacle 21 情報は PUNT (回答拒否) となります。その他 3 プラットフォームはインターネット接続が可能ですが、手動で有効化が必要です。
- **Claude**: 容量 77% で Pro ソフトリミットに近づいています。新しいファイルを追加する際は、優先度の低いファイルをダウングレードする必要があります。
- **ChatGPT**: 20 ファイルのハード上限 (現在 9 ファイル) があります。長尾チャンクのテーブル中段が miss される場合があります。
- **Gemini**: 個人アカウントではチーム直接共有ができません (Workspace が必要です)。v7.1 の system prompt は必ず完全な形で貼り付けてください。
- **NotebookLM**: 50 ソースの上限 (現在 42 ソース)。Q9 / Q11 / Q12 の 3 問が自発的に PUNT するのは**正しい安全動作**です。

## 8. フィードバック

誤り / ハルシネーション / 意図しない回答を発見した場合: (1) スクリーンショットを撮り、質問の全文と AI の回答を保存してください。(2) プラットフォーム名とバージョン番号 (例: "ChatGPT GPT v2.2 LIVE 2026-04-24") + 期待される回答 (SDTMIG v3.4 の章番号または CDISC CT C-code を引用) を添えてください。(3) Daisy にメールするか、社内の issue tracker または部門グループチャットで @Daisy にご連絡ください。フィードバックは `./CHANGELOG.md` に集約され、次の minor release に反映されます。

## 9. ロードマップ

短期 (v1.0 メンテナンス): フィードバックを受けて SDTM の誤りを修正し、四半期ごとに v1.x minor リリースを行います。中期 (Phase 7 自社 RAG 構築): 4 プラットフォームの容量制約から脱却し、295 ファイルをフル搭載 + QS codelist の完全展開を目指します。長期: SDTMIG v3.5+ との同期 + ADaM / Define-XML 拡張。

---
*v1.0 — 2026-04-27 — メンテナー: Daisy*
