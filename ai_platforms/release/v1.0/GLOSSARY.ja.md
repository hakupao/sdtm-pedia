---
lang: ja
slug: glossary
order: 40
title: "用語集"
---

# 用語集 — SDTM AI ナレッジベース

> 1 ページの早見表です。不明な用語があればこちらに戻ってご確認ください。SDTM 業界 / AI プラットフォーム / プロジェクト内部の 3 カテゴリに分類しています。

## 1. SDTM 業界用語

| 用語 | 日本語 | 説明 |
|---|---|---|
| **SDTM** | 臨床試験データ表記モデル | Study Data Tabulation Model。CDISC 標準のひとつで、臨床試験データをどのように表（ドメイン / 変数 / コードリスト）として整理するかを定めています。 |
| **SDTMIG v3.4** | SDTM 実装ガイド v3.4 | SDTM Implementation Guide。SDTM モデルを「どのドメインにどの変数があり、それぞれの Core 属性は何か」という形で具体化した仕様書です。本プロジェクトで使用している v3.4 は 2021 年版の主流仕様です。 |
| **CDISC** | 臨床データ交換標準協会 | Clinical Data Interchange Standards Consortium。SDTM / ADaM / CDASH などの一連の標準を管理しており、FDA への提出には必須の組織です。 |
| **Domain（ドメイン）** | ドメイン（領域） | SDTM では臨床データをテーマ別に 63 のドメインに分類しています。例：AE（Adverse Events）/ DM（Demographics）/ LB（Lab）/ EX（Exposure）。各ドメインは 1 枚のテーブルに対応します。 |
| **Variable（変数）** | 変数 | ドメイン内の 1 列を指します。例：AE ドメインには AESER（Serious Event フラグ）/ AETERM（報告原文）/ AEDECOD（MedDRA デコード）などがあります。 |
| **Core 属性** | Req / Exp / Perm | 各変数の「入力必須レベル」を表します。**Req**（Required、必須）/ **Exp**（Expected、原則記載、欠損時は注記が必要）/ **Perm**（Permissible、任意）。例：USUBJID Core=Req、AESER Core=Exp、AESEV Core=Perm。 |
| **CT（Controlled Terminology）** | 規制用語 / 制御用語集 | CDISC が定める「その変数に入力できる値の一覧」です。例：AESER には Y/N/U/NA の 4 値のみ使用可能で、"yes" や "はい" は使えません。 |
| **C-code** | NCI 用語コード | 各コードリストを一意に識別する NCI EVS の C-code です。例：NY コードリスト = C66742、AESEV コードリスト = C66769。これらの C-code は SDTMIG / NCI EVS Browser / Pinnacle 21 など各所で共通して使われます。 |
| **Extensible** | 拡張可能 | コードリストにスポンサー独自の値を追加できるかどうかを示すフラグです。**Extensible=Yes**（例：LBNRIND は 4 標準値 + スポンサー追加可）対 **Non-Extensible**（例：NY は Y/N/U/NA の厳格な 4 値のみで追加不可）。 |
| **Codelist** | コードリスト（コード表） | 名前付きの値セットです。例：LBNRIND コードリストには {HIGH/LOW/NORMAL/ABNORMAL} の 4 標準値があります。「CT」と同義で使われます。 |
| **SUPPQUAL / SUPP--** | 補足ドメイン | SDTM の標準変数では収まりきらないデータを格納する際に使用します。SUPPQUAL ドメインに IDVAR / IDVARVAL / QNAM / QVAL の 4 点セットで補足します。各標準ドメインに対応する SUPP-- が存在します（例：AE ↔ SUPPAE / LB ↔ SUPPLB）。 |
| **NSV** | 非標準変数 | Non-Standard Variable。主ドメインには収録できず、SUPPQUAL にのみ格納する変数を指します。SUPP-- は NSV を格納するためのコンテナです。 |
| **RELREC / RELSPEC / RELSUB** | 関係ドメイン 3 点セット | SDTM のドメイン間関連付けの仕組みです。RELREC = レコードレベル（例：1 件の AE と 1 件の EX を関連付け）/ RELSPEC = 検体レベル / RELSUB = 被験者レベル。 |
| **MedDRA** | 医薬品規制活動のための医療用語集 | 国際的に使われる医学用語辞書です。AE ドメインの AEDECOD / AEHLT / AEHLGT などの変数は MedDRA に準拠しています。CDISC CT には属しませんが、AE ドメインでは強く依存しています。 |
| **NCI EVS** | NCI エンタープライズ語彙サービス | National Cancer Institute Enterprise Vocabulary Services。CDISC CT の公式公開サイトで、[browser.evs.nci.nih.gov](https://browser.evs.nci.nih.gov) からアクセスできます。マイナーなコードリストはここでリアルタイムに確認できます。 |
| **Pinnacle 21** | 標準準拠チェックツール | SDTM データセットと標準仕様の適合を自動チェックする業界標準ツールで、「SDTM 向けのリンター」のようなものです。本プロジェクトは Pinnacle 21 に直接接続しておらず、実際の検証には cdisc.org または対応ツールでの確認が必要です。 |
| **ISO 8601** | 日付・時刻の国際標準 | 国際標準の日付・時刻フォーマットです（例：`2026-04-27T13:45Z`、`2026-04-27`、`--MM-DD`）。SDTM のすべての --DTC 変数には ISO 8601 形式での入力が必須です。 |

## 2. AI プラットフォーム / RAG 用語

| 用語 | 日本語 | 説明 |
|---|---|---|
| **System Prompt / Instructions** | システムプロンプト / インストラクション | AI に渡す「操作マニュアル」で、役割 / 優先順位 / ガードルール / アンカーなどを定義します。ChatGPT では Instructions / Custom Instructions、Claude では System Prompt、Gemini では Gem instructions、NotebookLM では Custom mode と呼ばれます。 |
| **Custom mode** | NotebookLM カスタムモード | NotebookLM Chat の 3 モードのひとつ（Default / Learning Guide / Custom）。システムプロンプトを設定できる唯一の入口で、上限は 10K 文字です。本デプロイでは Custom mode に instructions.md を設定しています。 |
| **RAG** | 検索拡張生成 | Retrieval-Augmented Generation。AI は質問を受けると、まずナレッジベースから関連する断片を検索し、その断片に基づいて回答を生成します。「記憶頼み」ではありません。4 つのプラットフォームすべてが RAG を使用しており、NotebookLM は最も厳格な in-KB-only RAG を採用しています。 |
| **Indexing** | インデックス化 | ナレッジベースをアップロードすると、AI がまず「全体を読み込んでチャンクに分割しベクトルインデックスを構築」します。この処理が完了して初めてチャットが可能になります。処理時間はプラットフォームにより異なります（Gemini 約 1〜3 分 / ChatGPT 約 5〜15 分 / Claude / NotebookLM 約 2〜10 分）。 |
| **in-KB-only** | ナレッジベース内に限定 | NotebookLM の設計原則で、回答はアップロードされたソースのみから生成されます。Web 検索やパラメータによる推測回答は行いません。ナレッジベース外の質問は回答を拒否します（PUNT）。 |
| **PUNT** | 回答拒否 | NotebookLM の用語で「わかりません、アップロードされたソースに情報がありません」を意味します。**PUNT はバグではなくフィーチャーです** — 情報を捏造するよりも誠実な応答です。 |
| **Hallucination / 幻覚 / 虚構** | AI による捏造（ハルシネーション） | AI が知識の空白部分に、もっともらしく見えるが実際には誤った情報を作り出すことです。本プロジェクトが重点的に防いでいる問題です。 |
| **Anti-hallucination Probe（AHP）/ 反虚構プローブ** | 「意図的に誤りを含む」テスト問題 | 評価問題に意図的に誤った前提を含めます（例：「PF ドメインにはどのような変数がありますか？」と聞くが、PF はすでに廃止済み）。AI が誤った前提に乗らず主体的に識別できるかを確認します。本プロジェクトでは各プラットフォームに 3 問の AHP を使用しています。 |
| **PASS+** | 誤前提を主体的に指摘した場合の加点 | 評価用語です。PASS = 核心的な事実に正答 / PASS+ = 正答 + 問題中の誤った前提を主体的に指摘。AHP 問題では PASS+ を最も重視します。 |
| **Smoke test** | スモークテスト（煙テスト） | 「電源を入れて基本的な動作を確認する」類の予備テストです。完全なカバレッジは求めず、主要機能が正常に動作することだけを確認します。本プロジェクトではデプロイ後に D0/D1/D5 の 3 問を実施することをスモークテスト通過の基準とします。 |
| **token** | LLM の処理単位（トークン） | LLM が内部でテキストを分割する単位です（日本語 1 文字 ≒ 0.5〜1 トークン、英語 1 単語 ≒ 1〜2 トークン）。Claude Project の容量は約 3〜4M トークン、Gemini は 1M コンテキストウィンドウです。 |
| **Context window** | コンテキストウィンドウ | LLM が一度に「記憶」できるトークンの最大数です。超過した場合は古い内容が失われます。Gemini の 1M は約 1,000 ページを一度に処理できることを意味し、Claude は約 200K〜1M です。 |

## 3. プロジェクト内部用語

| 用語 | 意味 |
|---|---|
| **17 問 / 内部完全問題集** | 各プラットフォームの評価に使用する SDTM 問題セットです。共通問題 14 問 + 反虚構プローブ 3 問で構成されています。`../../SMOKE_V4.md` §2 をご参照ください。 |
| **D0〜D9 / Demo** | 同僚向けの 10 問クイックデモセットです。本ディレクトリの `./DEMO_QUESTIONS.md` にあります。内部の 17 問とは別物であり、問題番号に対応関係はありません。 |
| **4 条の品質ルール** | プロジェクト内部の成果物・レビュープロセスに関する規律です（例：「改変率 50% 超は独立サンプリングレビュー必須」「失敗記録は削除しない」「最終稿には必ず振り返りを記載」「レビューは自己審査禁止」）。同僚は詳細まで把握する必要はありません。 |
| **LIVE** | プラットフォームのデプロイ完了 + 完全な 17 問実施済み + 品質ゲート通過済み、実際に使用可能な状態です。現在 4 つのプラットフォームすべてが LIVE です。 |
| **baseline** | プロジェクト内部で公式に測定した「そのプラットフォームでこの問題セットを実施した場合に期待されるスコア」です。自分でデプロイして同じ問題を実施した場合、同様のスコアが再現できるはずです（±2 点の誤差は許容範囲です）。 |

---

## さらに詳しく知りたい場合

| テーマ | パス |
|---|---|
| 完全なテスト問題集 + 各プラットフォームの問題別回答 | `../../SMOKE_V4.md` + 各プラットフォームの `dev/evidence/smoke_v4_answers/` |
| 完全な制限事項一覧 | [`./KNOWN_LIMITATIONS.en.md`](./KNOWN_LIMITATIONS.en.md) |
| プロジェクト方法論 | `../../claude_projects/docs/RETROSPECTIVE_V2.md`（Claude v2 最終状態の振り返り）+ `../../notebooklm/docs/RETROSPECTIVE.md`（NotebookLM 振り返り） |
| 4 プラットフォームの横断的振り返り | `../../retrospectives/PHASE5_RETROSPECTIVE.md`（v1.0 FINAL） |

> ⚠️ 注記: 本節における `../../...` または `dev/evidence/...` 形式のパスは、プロジェクト内部の成果物 (Bojiang Zhang が保管) を指しており、本 release パックには含まれていません。詳細が必要な場合は Bojiang Zhang までご連絡ください。

---
*v1.1 — 2026-04-27 — メンテナー: Bojiang Zhang*
