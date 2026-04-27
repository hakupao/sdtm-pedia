# Claude Project 作成チュートリアル — SDTM ナレッジベース公開版 v1.0

> release v1.0 セルフデプロイチュートリアル (ゼロから CDISC SDTM を照会できる Claude Project を構築します).
> 本チュートリアルを完了すると、30〜60 分で完全に使用可能な Claude Project が得られます (indexing 待機時間はバックグラウンドで進行)。容量 ~77%、19 ファイル 1.29M tokens、完全 24 問テスト全 PASS ベースライン。
> 情報源: プロジェクトリポジトリ `./` (system_prompt.md + uploads/ × 19).

---

## 0. 前提要件

- [ ] **Claude Pro サブスクリプション** (または Team/Enterprise): 公開版の総 token 量は 1.29M であり、無料プランの上限を超えています。Pro 以上のプランでは Claude Projects の RAG 分割が自動的に有効になります。
- [ ] **Web アクセス** [claude.ai](https://claude.ai): 本チュートリアルは全工程 Web UI 上で操作します。
- [ ] **本リポジトリをローカルにクローン済み**: `./uploads/` 配下の 19 ファイルと `./system_prompt.md` を参照する必要があります。

**「能力 vs 容量」について**:
- 公開版の実測では Claude Projects の容量を約 **77% capacity** (UI 表示) 使用します。
- まだ余裕はありますが、有料プランのソフト上限に近づいています。今後 Anthropic が容量を変更した場合は再評価が必要になる場合があります。
- カバレッジ範囲: core codelist 99.3% / supp codelist 100% / questionnaires codelist 55.8% / 63 ドメイン examples 100% / 6 章 chapters 全展開

---

## 1. Project を作成

1. [claude.ai](https://claude.ai) にログインします。
2. 左サイドバーの "**Projects**" → "**Create Project**" をクリックします。
3. **命名例**: `SDTM Knowledge Base` または `CDISC SDTM Expert`
4. **Description** (任意): `SDTM (Study Data Tabulation Model) knowledge base from CDISC standards. Answers variable definitions, codelist terms, example datasets, cross-domain references.`
5. **アクセス権限**:
   - 個人利用: **Private**
   - チーム利用: 所属 organization を選択 (Team/Enterprise プランのみ対応)
   - 注意: Claude Projects は現時点で**公開共有リンクの生成を支援しておりません**。organization 内共有のみ可能です。

---

## 2. System Prompt を設定 (Custom Instructions)

System Prompt は Project の「役割と動作仕様書」であり、モデルがクエリをどのようにルーティングし、ソースを引用し、境界を処理するかを定義します。

### 操作手順

1. 作成した Project を開き、右上の "**Edit project**" をクリックします。
2. "**Custom instructions**" または "**Project instructions**" フィールドを探します。
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
- **ファイルを分割・結合しないでください** — 特に 11b (256K tokens、最大単一ファイル) は実測で召回に問題はありませんでしたが、加工すると RAG 分割が破損する可能性があります。

### よくある質問

**Q: UI に「File is too large」と表示される**
A: 単一ファイルの上限は ~1MB (約 256K tokens) です。11b がちょうど 256K を超えると発生する場合があります。対処方法:
- エディタが BOM または CRLF を付加していないか確認してください。
- 解決しない場合は 11b を 11b-a/11b-b の 2 分割にすることも可能ですが、A/B テストの再実施が必要になります。

**Q: 一部ファイルだけアップロードして試したい**
A: 推奨しません。T1〜T22 と優先度検証の 24/24 PASS ベースラインは**全 19 ファイル**に基づくものです。ファイルが不足すると品質が低下します。

**Q: アップロードの進行が 90% で止まったまま**
A: 一般的にネットワークの問題です。ページをリロードしてください。Claude はアップロード済みのファイルを保持していますので、残りのファイルを継続してアップロードできます。

---

## 4. Indexing を待つ (重要: 実際には待つ必要はありません)

アップロード完了後、UI に "**Indexing**" インジケーターが表示されます。所要時間は **30〜60 分**、場合によってはそれ以上になります。

### Indexing の完了を実際に待たないでください

実測の観察結果:
- Indexing インジケーターは**信頼性が低い**です: 表示中であっても、すぐに質問すれば新しいコンテンツにヒットします。
- 実際に待つ場合は 60 分以上かかり、indexing 失敗として再試行を促すメッセージが表示されることもあります。
- デプロイフローの正しい確認方法は**1〜2 問直接質問すること** (次のステップ) であり、ヒットすれば利用可能です。

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

Claude が term を列挙しようとしたり「わかりません」と回答した場合は、System Prompt 内の Stage 6 Deferred stub ルールが機能していません。System Prompt に v2.6 段が含まれているか再確認してください。

### Release v1.0 完全 demo
上記 T1/T17/T22 に加え、release v1.0 では anti-hallucination probe を含む 10 問の完全 demo を提供しています。[../DEMO_QUESTIONS.md](../DEMO_QUESTIONS.md) をご参照ください。社内同僚のオンボーディングには、まず D0 + D1 + D6 の 3 問 (5 分) から始めることを推奨します。

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
| 全ての照会で「わかりません」と回答される | System Prompt が完全に貼り付けられていない | Custom Instructions に全 6 段 stage が含まれているか確認する。特に Stage 6 を確認すること |
| 章番号が誤っている (例: §4.3.6 と表示されるが実際は §4.3.7) | 02_chapters.md がアップロードされていないか切り捨てられている | 02_chapters.md を再アップロードし、ファイルサイズ > 200KB であることを確認する |
| T22 で C65047 の具体的な term 値が列挙される (幻覚) | Stage 6 Deferred stub ルールが機能していない | System Prompt Stage 6 段を確認し、13a_terminology_tail_core.md がアップロードされているか確認する |
| CT code の照会で 11*/12*/13* ではなく 08 のみが返される | CT 照会優先度ルールが欠けている | System Prompt 末尾に `CT 照会優先度 11*>12*>13*>08` が含まれているか確認する |
| Capacity UI が 85% を超えて警告が表示される | Claude Projects のポリシー変更 | 削除の優先順位: 13c > 12c > 12b > 11c (11a/11b/09/05/02 のコアは保持する) |
| 特定の問への回答が非常に遅い / 頻繁にレート制限が発生する | Pro プランの RAG レート制限 | 30〜60 秒待ってから再試行する。継続する場合は Team/Enterprise へのアップグレードを検討する |
| questionnaires (quest) codelist の約 44% に回答できない | 公開版は quest の 55.8% のみカバー (設計上の決定) | 正常な動作です。quest の長尾 296 codelist は後続の Phase 7 自家製 RAG での処理対象です |

---

## 8. アップグレード / ダウングレードパス

### カバレッジを向上させたい場合 (任意、デフォルトでは実施しません)

- quest カバレッジを 55.8% から ~80% に引き上げる場合: quest tail extraction を追加する必要があります (+~180K tokens)。予想 capacity は ~85% になります。
- 6 つの giant (MedDRA 級 codelist) を Deferred stub からインライン展開に変更する場合: +500K tokens が必要となり、C12 のハード上限に直接抵触します。推奨しません。

### ダウングレードしたい場合 (容量が不足している場合)

削除の優先順位 (最も有用なものを保持します):
1. まず `13c_terminology_tail_supp.md` を削除 (43K、supp 長尾)
2. 次に `13a_terminology_tail_core.md` を削除 (146K。ただし 6 giants stub を含むため、削除すると T22 が FAIL になります)
3. 次に `12c_terminology_mid_supp.md` を削除 (23K)
4. 次に `12b_terminology_mid_questionnaires.md` を削除 (225K)
5. 最後に `12a_terminology_mid_core.md` を削除 (130K)

保持の最低ライン: `11a/b/c_terminology_high_*` + `09/10_examples_data_*` + `00-08` コア構造 = 約 800K tokens / ~50% capacity。

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
- Anthropic が新しいプランやより大きな capacity をリリースした場合は、85〜90% への拡張を再評価することができます。
- 公開版の使用中にナレッジベースのコンテンツに欠落や誤りを発見した場合は、プロジェクトの issue tracker にフィードバックしてください。ナレッジベースの更新後、公開版を再ビルドします。

---

## 付録: 検証チェックリスト (デプロイ後セルフチェック)

- [ ] Claude Pro 以上のプランが有効になっている
- [ ] Project が作成済みであり、名称が明確である
- [ ] Custom Instructions に完全な System Prompt (全 6 段 stage を含む) が貼り付けられている
- [ ] Project Knowledge パネルに 19 ファイルのアップロードが表示されている
- [ ] T1 AEDECOD Core 照会 PASS (Req と回答し、§4.3.6/§4.3.5 を引用している)
- [ ] T17 C66742 Term 表照会 PASS (4 term + 41 related domains)
- [ ] T22 C65047 giant 境界照会 PASS (stub を宣言し、ハルシネーションなし)
- [ ] UI capacity 表示が ~77% (正常範囲)

全て ☑ = デプロイ成功。通常利用を開始できます。

---

*v1.0 — 2026-04-27 — 社内公開版*
*方法論詳細: ../../claude_projects/docs/ ; release v1.0 概要: ../README.ja.md*
