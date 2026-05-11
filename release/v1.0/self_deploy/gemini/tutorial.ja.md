# Gemini Gem 作成チュートリアル — SDTM ナレッジベース公開版

> ゼロから CDISC SDTM 標準 (63 ドメイン + chapters + ビジネスシナリオ集) を検索できる Custom Gem を構築します。
> このチュートリアルを読み終えると、SDTM 変数定義 / ビジネスシナリオマッピング / クロスドメイン関連付けに精確に回答でき、よくある虚構の前提を見破る (3 つのアンチハルシネーションアンカー (anti-hallucination guard)) Gemini Gem が完成します。
> 所要時間の目安: **20〜40 分** (Gemini のインデックス作成は ChatGPT より大幅に高速です)。

---

## 0. 前提要件

- [ ] **Google アカウント** (13 歳以上)。**Gem の作成自体は 2025 年から Free アカウントでも可能**になりました。ただし **Knowledge ファイルのアップロード・他者への共有・大容量 instructions** を利用するには **Google AI Plus / Pro / Ultra / Workspace プランのいずれか**が必要です。本チュートリアルは Knowledge をフル活用するため **Pro 以上を推奨**。

  | プラン | Gem 作成 | Knowledge | 共有 |
  |--------|----------|-----------|------|
  | Free | 可 | 制限あり | 不可 |
  | Google AI Plus / Pro / Ultra | 可 | フル機能 | 可 |
  | Google Workspace (Business Standard 以上) | 可 | フル機能 (管理者制御下) | 可 |

- [ ] ウェブブラウザで [gemini.google.com](https://gemini.google.com) にアクセスできること
- [ ] **本リポジトリをローカルに clone 済み**: `./` 配下の `system_prompt.md` (約 29.9 KB) と `uploads/` 配下の 4 つの .md ファイルを参照するために必要です

**プランと共有について**:
- 個人 Google AI Pro / Ultra で Gem を作成・共有できます。**2025 年以降、Gem の共有機能が解放**され、Google Drive と同じ UI で Viewer/Editor 権限を設定できます (§9 参照)。

---

## 1. Gem を新規作成

1. [gemini.google.com](https://gemini.google.com) に Google アカウントでログインします
2. サイドバー → "**Gems**" → "**Explore Gems**" → "**New Gem**" ボタン (記号 + なし)
3. **Name**: `SDTM Expert` または `CDISC SDTM Knowledge` を推奨します
4. **Description**: `CDISC SDTMIG v3.4 + SDTM v2.0 Expert — Variable definitions, rule reasoning, business scenario mapping, cross-domain.`

---

## 2. Instructions を設定 (system_prompt.md)

1. Gem の編集画面で "**Instructions**" または "**Custom Instructions**" フィールドを見つけます
2. `./system_prompt.md` (v7.1 LIVE、29,919 chars) の内容を**すべてコピー**して貼り付けます
3. **重要**: Gemini Gems は長い Instructions を受け付けます。**公式の文字数上限は明記されていません**が、本 v7.1 LIVE の 29,919 chars は実測で動作確認済みです (2026-04 時点)。**過度に長い Instructions は Knowledge ファイル参照を弱めるという報告もある**ため、必要最小限に保つことを推奨。ChatGPT の 8K 上限に慣れているために手動で切り詰めないでください。切り詰めるとアンチハルシネーションのアンカーが失われます

**v7.1 LIVE の主要パッチ (貼り付け後に必ず保持すること)**:
- **§CO-1d SUPPQUAL Core + scope ハードアンカー**: QORIG Core=Req / QEVAL Core=Exp / CT C78735; SUPPQUAL は Trial Design (TS/TA/TE/TI/TV) には適用されません
- **§CO-1c ARM/ARMCD/ARMNRS** 5 値 (NOT APPLICABLE を含む) Extensible=Yes
- **§CO-5 AHP-V1/V2/V3** 3 段階アンチハルシネーションガード (変数レベル / クロスドメインレベル / deprecated レベル)

---

## 3. ナレッジベース 4 ファイルをアップロード

1. Gem の編集画面 → "**Knowledge**" パネル → "**Upload files**" またはドラッグ＆ドロップ
2. `./uploads/` 配下の **4 つの .md ファイルをすべて**選択します。順序は以下のとおりです:
   - `01_navigation_and_quick_reference.md` (~124K tokens)
   - `02_domains_spec_and_assumptions.md` (~240K tokens、63 ドメイン仕様 + assumptions をドメイン内で交互配置)
   - `03_domains_examples.md` (~220K tokens、63 ドメインの examples)
   - `04_business_scenarios_and_cross_domain.md` (~30K tokens、26 ビジネスシナリオ + FAQ)
3. **ファイル名の変更や分割・統合は行わないでください**

Gemini Knowledge には **10 ファイルのハード上限**があります。現在 4/10 (6 ファイルの余裕あり)。合計 ~616K tokens は 1M コンテキストウィンドウの約 62% を占め、~38% のレスポンスバッファが確保されています。

**追記**: **1 ファイルあたり 100 MB が一般的な上限** (動画は 2 GB)。**Google Drive ファイルを直接参照することも可能** (常に最新版が参照され、変更時の差し替えが不要)。

---

## 4. Indexing を待つ (RAG 処理)

**2026 年現在、Gemini Gems は RAG (Retrieval-Augmented Generation、セマンティック チャンク検索) を採用**しています。アップロード後、Knowledge ファイルはチャンク分割・ベクトル化され、クエリごとに**意味的類似度の高いチャンクのみ**が動的に注入されます。Instructions は毎ターン全文注入されますが、Knowledge ファイルは類似度ヒット時のみ呼ばれます。

通常 1〜3 分以内にファイルのステータスが "Ready" に変わり、チャットを開始できます。

**注意**: RAG パイプラインの安定性は時折変動します (2026/1 にファイル参照退行バグ報告あり)。citation が出ない / 期待した内容がヒットしない場合は、新規 chat で再試行するか §7 トラブルシューティングを参照してください。

---

## 5. Smoke Test (3 問、~5 分)

**Preview** で 1 問につき新しいチャットを開いて質問します:

| # | 質問 | 期待される回答のポイント | 検証観点 |
|---|------|---------|------|
| T1 | `AESER の Core 属性は Req ですか、Exp ですか？` | Core = **Exp** (Req ではない) | CO-1 高頻度の誤りやすいアンカー |
| T2 | `LB / MB / IS の 3 ドメインはどう区別しますか？微生物培養結果はどのドメインに入りますか？` | LB = 臨床検査 (化学/血液/尿); MB = 微生物 (培養/薬剤感受性); IS = 免疫 (抗体/ワクチン) | ドメイン境界の識別 |
| T3 | `PF ドメイン (Pharmacogenomics Findings) の変数リストは？` (PF は deprecated) | Gem は**見破るべき**: PF は v3.4 で廃止済み。現在は GF (Genomics Findings) / BE (Biospecimen Events) / BS (Biospecimen Findings) + RELSPEC を使用 | AHP3 deprecated アンチハルシネーション (R1→R2 アップグレードのコア閉合点 (closure point)) |

**3/3 PASS** = デプロイ成功。いずれかが FAIL の場合 → §7 トラブルシューティングを参照してください。

**Knowledge ファイルが RAG でヒットしているか確認するため、Gem が回答内に source citation を含めることを期待値に追加**してください。

---

## 6. 完全回帰 (10 問、オプション ~30 分)

`../../DEMO_QUESTIONS.ja.md` を開き、D0-D9 (10 問の demo) を順に質問します。**1 問につき新しいチャット**を使用してください。プロジェクト内部完全 17 問ベースライン 16/17 (94.1%)、3 問のアンチハルシネーション問題すべて見破り。あなたがデプロイした Gem がこの 10 問を >= 8/10 で通過すれば、ベースライン同等です。

---

## 7. トラブルシューティングガイド (Gemini 固有)

| 症状 | 考えられる原因 | 対処方法 |
|------|---------|------|
| ARM 回答時に ARMCD / ARMNRS が混在する | §CO-1c アンカーが無効 | system_prompt §CO-1c を再確認 (ARM の 5 値をすべて列挙 + Extensible=Yes) |
| SUPPQUAL Core の回答が誤り (QORIG=Exp / QEVAL=Req) | §CO-1d v7.1 アンカーが有効でない | system_prompt の全文を貼り直し、§CO-1d セクションが含まれていることを確認 |
| PF / PGx ドメインの変数を回答 (deprecated の虚構) | §CO-5 AHP-V3 アンカーが無効 | §CO-5 + §回答規範 ⑧ Deprecated concept セクションを再確認 |
| LBCLINSIG を回答 (変数の虚構) | §CO-5 AHP-V1 アンカーが無効 | §CO-5 デュアルコアワークフロー step 0 + AHP-V1 識別テンプレートを再確認 |
| 最初のトークンが遅い (>10 秒) | コールドスタートの正常な動作 | 以降のクエリは速くなります。30 秒以上続く場合は Google AI のステータスを確認してください |
| 回答に引用 / ソースパスがない | §CO-3 アンカーが無効 | system_prompt §三条硬約束 + §回答規範 を貼り直してください |
| Knowledge ファイルのステータスが "Processing" のまま | ファイルが想定外に大きい (本公開版は最大 ~919 KB) / エンコード異常 | 02 ファイル (~919 KB、最大) を確認し、UTF-8 LF / BOM なしであることを確認してください |

---

## 8. アップグレード / ダウングレードパス

**アップグレード (KB 拡張)**:
- 現在 4/10 ファイル、6 ファイルの余裕あり
- terminology のロングテール (questionnaires) は 05 ファイルとして追加可能; SDTMIG v3.5 の新ドメインは 06 ファイルとして追加可能
- **ダウングレード不要**: 現在の合計 token は 1M ウィンドウの 62%、38% のバッファで十分です

**ダウングレード (容量警告時、通常不要)**:
1. まず `04_business_scenarios_and_cross_domain.md` を削除 (ビジネスシナリオ集ですが、R2 アップグレードの重要ファイルです)
2. 次に `03_domains_examples.md` を削除 (examples)

最低限保持するファイル: `01 + 02` (ナビゲーション + spec/assumptions) = 365K tokens。

---

## 9. チーム協業

**Gemini Gem は 2025 年から共有可能になりました** (旧来の "共有不可" 制約は解除)。

- **共有方法**: Gem Manager で対象 Gem の横の "**Share**" → Google Drive と同じ UI で Viewer / Editor 権限を選択 → メールアドレス指定で招待
- **Workspace 管理者制御**: Admin Console → Generative AI → Gemini app → Gem sharing でオン/オフ切替可能
- **受信側の挙動**: 共有された Gem は受信者の Gem Manager に自動追加されません。受信者が開いて使用してから "My Gems" に追加される仕組み
- **注意**: Free アカウントは共有機能を利用できません。送信側・受信側ともに Pro / Ultra / Workspace が必要
- **公開ギャラリーについて**: GPT Store のような公開マーケットプレイスは存在しません。Google が用意した "premade Gems" は Gems Manager 内に表示されますが、ユーザーが Gem を公開ストアに掲載する機能はありません

---

## 10. 今後のパス

- 本公開版はすでに**完全な最終形態**であり、短期間での容量拡張は予定していません
- ロングテールの terminology + Studio 機能 (NotebookLM の Audio Overviews / Video Overviews / Mind Maps / Reports) は今後の Phase 7 / NotebookLM での補完に委ねています
- ナレッジベースのコンテンツに誤りや不足がある場合は、プロジェクトの issue tracker にフィードバックをお寄せください

---

## 付録: 検証チェックリスト

- [ ] Google AI Pro 以上のプランが有効になっている
- [ ] Custom Gem が作成済みで、名前が明確に設定されている
- [ ] Instructions に system_prompt.md の全文が貼り付けられている (v7.1 LIVE、29,919 chars)
- [ ] Knowledge パネルに 4 ファイルすべてが Ready 状態で表示されている
- [ ] T1 AESER Core=Exp PASS
- [ ] T2 LB/MB/IS ドメイン境界 PASS
- [ ] T3 PF deprecated アンチハルシネーション識別 PASS

すべて ☑ = デプロイ成功。日常利用を開始できます。

---

*v1.1 — 2026-05-11 — UI 用語を 2026 年公式仕様に同期 (RAG 採用 / Gem 共有解放 / Free 作成可)*
