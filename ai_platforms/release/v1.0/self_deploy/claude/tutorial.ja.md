# Claude Project 作成チュートリアル — SDTM ナレッジベース公開版 v1.1

> release v1.0 セルフデプロイチュートリアル (ゼロから CDISC SDTM を照会できる Claude Project を構築します).
> 本チュートリアルを完了すると、30〜60 分で完全に使用可能な Claude Project が得られます (indexing 待機時間はバックグラウンドで進行)。19 ファイル 1.29M tokens、完全 24 問テスト全 PASS ベースライン。
> 情報源: プロジェクトリポジトリ `./` (system_prompt.md + uploads/ × 19).

---

## 0. 前提要件

- [ ] **Claude Pro ($18/月) / Max ($100 または $200/月、Pro の 5x/20x usage) / Team / Enterprise いずれかのプラン。** Max は 2025 年に追加された新プランで、Pro より上位 / Enterprise より下位の位置付け。Free プランは Projects 5 件まで作成可能ですが、本 KB の 1.29M tokens を読み込むには Pro 以上が必須。
- [ ] **Web アクセス** [claude.ai](https://claude.ai): 本チュートリアルは全工程 Web UI 上で操作します。
- [ ] **本リポジトリをローカルにクローン済み**: `./uploads/` 配下の 19 ファイルと `./system_prompt.md` を参照する必要があります。

**「能力 vs 容量」について**:
- カバレッジ範囲: core codelist 99.3% / supp codelist 100% / questionnaires codelist 55.8% / 63 ドメイン examples 100% / 6 章 chapters 全展開
- 30 MB/file 上限 (2025 年に 1 MB から大幅拡大) のため、本 KB の最大ファイル 11b (~890 KB) を含む全ファイルに余裕があります。

---

## 1. Project を作成

1. [claude.ai](https://claude.ai) にログインします。
2. 左サイドバーの "**Projects**" → 右上の "**+ New Project**" (または中央の "**Create Project**") をクリックします。
3. **命名例**: `SDTM Knowledge Base` または `CDISC SDTM Expert`
4. **Description** (任意): `SDTM (Study Data Tabulation Model) knowledge base from CDISC standards. Answers variable definitions, codelist terms, example datasets, cross-domain references.`
5. **アクセス権限** (現在の UI では 2 択のみ):
   - "**Keep it private**": 個人利用 (デフォルト)
   - "**Share with your broader organization**": Team / Enterprise プランで利用可能。共有時の権限は "Can use" / "Can edit" の 2 段階
   - 注意: "Public" 選択肢は **2026 年現在の UI からは廃止済み**。個別の "公開共有リンク" は引き続きサポートされていません。

---

## 2. System Prompt を設定 (Set project instructions)

System Prompt は Project の「役割と動作仕様書」であり、モデルがクエリをどのようにルーティングし、ソースを引用し、境界を処理するかを定義します。

### 操作手順

1. 作成した Project を開き、右上の "**Edit project**" をクリックします。
2. "**Set project instructions**" ボタン (または "**Project instructions**" フィールド) を探します。※ 2025 年に UI ラベルが "Custom instructions" から "Set project instructions" に変更されました。
3. `./system_prompt.md` の内容を**完全にコピー**します (切り捨てないでください)。
4. フィールドに貼り付けます。
5. **保存**します。

### System Prompt が長い理由

公開版の System Prompt は約 **4〜6K tokens** あり、6 段階の累積指示が含まれています。
- Stage 1 段: 章の完全展開使用ルール
- Stage 2 段: examples 高頻度ドメインデータ照会の優先度
- Stage 3 段: examples 残りドメインのフォールバック戦略
- Stage 4 段: terminology 高頻度 codelist (`11*`) 優先、`08_terminology_map` へのフォールバック
- Stage 5 段: terminology 中頻度 codelist (`12*`) を CT 照会チェーンに追加
- Stage 6 段: terminology 末尾 + 6 つの MedDRA 級 giant codelist の Deferred stub 宣言

各段は一つのカバレッジ層であり、合わせると「全ファイルへの照会ルーティング戦略」になります。いずれかの段が欠けると、Claude が `11*` を参照して CT Code を検索できなくなります。

---

## 3. ナレッジベース 19 ファイルをアップロード

### 操作手順

1. "Edit project" 画面のまま、"**Project Knowledge**" パネルを探します。
2. `./uploads/` ディレクトリ配下の **全 19 個の `.md` ファイル**を一括選択します。
3. Knowledge パネルにドラッグ&ドロップします (または "Add files" ボタンから選択)。
4. Claude がアップロードを開始します (~1〜2 分) → その後 Indexing に移行します。

### ファイル一覧 (19 ファイル、合計 1,286,161 tokens)

順序は問いません。`./uploads/` ディレクトリ配下の全 19 個の `.md` ファイルをアップロードしてください。

**重要な概念**:
- ファイル名のプレフィックス `00-13c` は照会優先度のシグナルです (System Prompt 内でこれらのプレフィックスをルーティングに使用しています)。
- **いかなるファイルもリネームしないでください** — Project Knowledge のファイル名は Claude が引用元を特定するためのアンカーです。
- **ファイルを分割・結合しないでください** — 特に 11b (~890 KB、最大単一ファイル) は 30 MB 上限に対して余裕で収まるため、分割不要です。

### よくある質問

**Q: UI に「File is too large」と表示される**
A: 単一プロジェクトファイルの上限は **30 MB** (2025 年に 1 MB から大幅拡大) です。本 KB の最大ファイル 11b (~890 KB) は余裕で収まります。BOM または CRLF が付加されていないか確認してください。※ 旧来の 1 MB / 256K tokens 制限は過去のものです。現在は問題ありません。
ファイル数は無制限 (コンテキストウィンドウに収まる範囲) です。

**Q: 一部ファイルだけアップロードして試したい**
A: 推奨しません。T1〜T22 と優先度検証の 24/24 PASS ベースラインは**全 19 ファイル**に基づくものです。ファイルが不足すると品質が低下します。

**Q: アップロードの進行が 90% で止まったまま**
A: 一般的にネットワークの問題です。ページをリロードしてください。Claude はアップロード済みのファイルを保持していますので、残りのファイルを継続してアップロードできます。

---

## 4. Indexing を待つ (重要: 実際には待つ必要はありません)

アップロード完了後、UI に "**Indexing**" インジケーターが表示される場合があります。所要時間は **30〜60 分**、場合によってはそれ以上になります。

### Indexing の完了を実際に待たないでください

実測の観察結果:
- Indexing インジケーターは**信頼性が低い**です: 表示中であっても、すぐに質問すれば新しいコンテンツにヒットします。
- 実際に待つ場合は 60 分以上かかり、indexing 失敗として再試行を促すメッセージが表示されることもあります。
- デプロイフローの正しい確認方法は**1〜2 問直接質問すること** (次のステップ) であり、ヒットすれば利用可能です。

**Indexing の進捗表示の有無は公式ドキュメントに明記なし** — 2026 年現在の UI ではインジケーターが表示されない場合もあります。実用上は §5 smoke test で動作確認する方が確実です。

アップロードが完了したら、そのまま §5 smoke test に進んでください。

---

## 5. Smoke Test (3 問、約 5 分)

Project 内に新しいチャットを作成し、以下の 3 問を順番に質問して、各回答を期待値と照合してください。

### T1: 変数定義照会 (最も基本的)

**質問**: `AE.AEDECOD の Core 属性は何ですか？ どの章を引用していますか？`

**期待値**:
- Core = **Required** (または Req)
- 引用元 `05_mega_spec.md §AE` + `04_variable_index.md (Sy/R)` + `02_chapters.md §4.3.6` (三元構造 AETERM/AEMODIFY/AEDECOD)
- AEPTCD の配套変数への言及があること

Claude が Core=Permissible と回答したり章番号を答えられない場合は、Indexing がまだ反映されていない可能性があります。5〜10 分待ってから再試行してください。

### T17: Codelist Term 表照会 (RAG 深度)

**質問**: `C66742 codelist の全 Term 値は何ですか？`

**期待値**:
- 4 つの Term: **C49487 N / C48660 NA / C17998 U / C49488 Y**
- Extensible: **No**
- 41 の Related Domains (AE/AG/BS/CE/...) が列挙されていること
- 引用元 `11a_terminology_high_core.md` + `02_chapters.md §4.3.7`

Y/N/U/NA は返答されるが C-code が含まれない場合は、RAG が 11a を取得できていません。11a が正常にアップロードされているか確認してください。

### T22: Giant Codelist 境界識別 (stub 検証)

**質問**: `C65047 codelist にはどのような Term 値がありますか？`

**期待値** (最も重要な境界テストです):
- Claude は「C65047 は Laboratory Test Code であり、2,536 terms を含む超大規模 codelist のため、Project 内には全 Term 値が完全には収録されていません」と**宣言**すること
- 引用元 `13a_terminology_tail_core.md` (stub 定義) + `../../../knowledge_base/terminology/core/lb_part*.md` (ソースファイル) + NCI EVS Browser へのリンク
- **ハルシネーションなし**: 具体的な term 値を提示しないこと (Claude が term を列挙した場合は幻覚であり、トラブルシューティングが必要です)

Claude が term を列挙しようとしたり「わかりません」と回答した場合は、System Prompt 内の Stage 6 Deferred stub ルールが機能していません。System Prompt 内の Stage 6 (内部バージョン v2.6 で確定した Deferred stub ルール) が含まれているか再確認してください。

### Release v1.0 完全 demo
上記 T1/T17/T22 に加え、release v1.0 では anti-hallucination probe を含む 10 問の完全 demo を提供しています。[../../DEMO_QUESTIONS.ja.md](../../DEMO_QUESTIONS.ja.md) をご参照ください。ユーザーのオンボーディングには、まず D0 + D1 + D6 の 3 問 (5 分) から始めることを推奨します。

---

## 6. 完全回帰テスト (任意、24 問、約 40 分)

「自分のデプロイしたプロジェクトがプロジェクトのベースラインと同等かどうか」を確認したい場合:

1. リポジトリから `../../claude_projects/dev/test_results.md` を開きます。
2. T1 → T22 + T-core-reb + T-supp-reb (計 24 問) を順番に質問します。
3. Claude の回答をマトリックスに記録されている v2.6 終態の回答と照合します。
4. 全て一致 = デプロイ PASS; 差異がある場合 = A/B 差異を記録します。新しいアップロードや indexing の状態差異による可能性があります。

推奨事項:
- **1 問につき新しいチャット** (コンテキスト汚染を避けるため)
- 各問、最初の token が返るまで約 20〜30 秒お待ちください。60 秒無応答の場合はレート制限に引っかかっている可能性があります。1 分待ってから再試行してください。
- **T3** (クロスバッチ RELREC) と **T7/T17** (C66742 原文ヒット) に特に注目してください — これらの問題は RAG がファイル横断で召回できるかを検証します。

---

## 7. トラブルシューティングガイド

| 症状 | 考えられる原因 | 対処 |
|------|--------------|------|
| 全ての照会で「わかりません」と回答される | System Prompt が完全に貼り付けられていない | Set project instructions に全 6 段 stage が含まれているか確認する。特に Stage 6 を確認すること |
| 章番号が誤っている (例: §4.3.6 と表示されるが実際は §4.3.7) | 02_chapters.md がアップロードされていないか切り捨てられている | 02_chapters.md を再アップロードし、ファイルサイズ > 200KB であることを確認する |
| T22 で C65047 の具体的な term 値が列挙される (幻覚) | Stage 6 Deferred stub ルールが機能していない | System Prompt Stage 6 段を確認し、13a_terminology_tail_core.md がアップロードされているか確認する |
| CT code の照会で 11*/12*/13* ではなく 08 のみが返される | CT 照会優先度ルールが欠けている | System Prompt 末尾に `CT 照会優先度 11*>12*>13*>08` が含まれているか確認する |
| Capacity 警告が表示される | Claude Projects のポリシー変更 — **公式に "X% capacity" UI の記載は現在ありません**。実機 UI で表示がある場合のみ参考に | 削除の優先順位: 13c > 12c > 12b > 11c (11a/11b/09/05/02 のコアは保持する) |
| 特定の問への回答が非常に遅い / 頻繁にレート制限が発生する | Pro プランの RAG レート制限 | 30〜60 秒待ってから再試行する。継続する場合は Team/Enterprise へのアップグレードを検討する |
| questionnaires (quest) codelist の約 44% に回答できない | 公開版は quest の 55.8% のみカバー (設計上の決定) | 正常な動作です。quest の長尾 296 codelist は後続の Phase 7 自家製 RAG での処理対象です |

---

## 8. アップグレード / ダウングレードパス

現在 30 MB/file 上限のため、本 KB はダウングレードの必要なし (全 19 ファイルが余裕で収まります)。以下は容量制限の厳しい旧環境向けの参考情報です。

### カバレッジを向上させたい場合 (任意、デフォルトでは実施しません)

- quest カバレッジを 55.8% から ~80% に引き上げる場合: quest tail extraction を追加する必要があります (+~180K tokens)。
- 6 つの giant (MedDRA 級 codelist) を Deferred stub からインライン展開に変更する場合: +500K tokens が必要となります。推奨しません。

### ダウングレードしたい場合 (旧環境で容量が不足している場合)

削除の優先順位 (最も有用なものを保持します):
1. まず `13c_terminology_tail_supp.md` を削除 (43K、supp 長尾)
2. 次に `13a_terminology_tail_core.md` を削除 (146K。ただし 6 giants stub を含むため、削除すると T22 が FAIL になります)
3. 次に `12c_terminology_mid_supp.md` を削除 (23K)
4. 次に `12b_terminology_mid_questionnaires.md` を削除 (225K)
5. 最後に `12a_terminology_mid_core.md` を削除 (130K)

保持の最低ライン: `11a/b/c_terminology_high_*` + `09/10_examples_data_*` + `00-08` コア構造 = 約 800K tokens。

---

## 9. チーム協業

- Claude Projects の Knowledge アップロードは **Project ごと** に管理されており、Project 間での共有はできません。
- Team/Enterprise プランでは、メンバーが Project を共有できますが、各自が参照するのは同一の Knowledge です (フォークではありません)。
- チームメンバーが System Prompt を変更したりファイルを削除した場合、**全員**に影響が及びます。編集権限は 1〜2 名に限定することを推奨します。
- 「公開リンクへの公開」には対応していません。外部ユーザーに提供する場合は、各自が本チュートリアルに従って個別にセットアップする必要があります。

---

## 10. 今後のパス

- 本公開版はすでに**完全な終態**であり、短期的な容量拡張の予定はありません。
- 長尾 302 codelist (296 quest + 6 giants) は後続の Phase 7 自家製 RAG (設計ドキュメント: 本プロジェクト `../../claude_projects/docs/`) での処理対象です。
- Claude は 2025 年に Projects に **RAG (Retrieval-Augmented Generation)** を有料プラン向けに自動導入しました — コンテキストウィンドウ 200K を超える KB でも自動的に RAG モードに切り替わり、本 KB の 1.29M tokens を扱えます。Enterprise の一部モデルでは 500K context window が利用可能。
- 公開版の使用中にナレッジベースのコンテンツに欠落や誤りを発見した場合は、プロジェクトの issue tracker にフィードバックしてください。ナレッジベースの更新後、公開版を再ビルドします。

---

## 付録: 検証チェックリスト (デプロイ後セルフチェック)

- [ ] Claude Pro 以上のプランが有効になっている
- [ ] Project が作成済みであり、名称が明確である
- [ ] Set project instructions に完全な System Prompt (全 6 段 stage を含む) が貼り付けられている
- [ ] Project Knowledge パネルに 19 ファイルのアップロードが表示されている
- [ ] T1 AEDECOD Core 照会 PASS (Req と回答し、§4.3.6/§4.3.5 を引用している)
- [ ] T17 C66742 Term 表照会 PASS (4 term + 41 related domains)
- [ ] T22 C65047 giant 境界照会 PASS (stub を宣言し、ハルシネーションなし)
- [ ] UI capacity 表示 (もし表示される場合) ~77%

全て ☑ = デプロイ成功。通常利用を開始できます。

---

*v1.1 — 2026-05-11 — UI 用語を 2026 年公式仕様に同期 (Custom instructions → Set project instructions / 30MB 上限 / Max プラン)*
*方法論詳細: ../../claude_projects/docs/ ; release v1.0 概要: ../README.ja.md*
