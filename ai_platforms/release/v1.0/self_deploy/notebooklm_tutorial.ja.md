# NotebookLM デプロイチュートリアル — SDTM ナレッジベース公開版 v1.0

> release v1.0 セルフデプロイチュートリアル (NotebookLM 1 notebook × 42 sources + Custom mode).
> 本チュートリアルを完了すると、30〜60 分で NotebookLM notebook が立ち上がります。in-KB-only による天然のハルシネーション対策を備え、完全 17 問テスト 15/17 PASS (88%) ベースラインを達成しています。
> 情報源: プロジェクトリポジトリ ai_platforms/notebooklm/current/ (instructions.md + uploads/ × 42).

---

## 0. 前提要件

- [ ] **Google AI Pro サブスクリプション** ([ai.google.com](https://ai.google.com)): 本デプロイは 42 sources を使用し、Pro プラン上限内に十分収まります (Pro 上限は本プロジェクトの使用量を大幅に超えています)。Free tier 50-source 上限はちょうど収まり動作可能ですが、Pro の方が安定します。詳細な各種 cap (notebooks / sources / words / chat / audio) は [`../../notebooklm/docs/PLAN.md`](../../notebooklm/docs/PLAN.md) §A をご参照ください。
- [ ] **Google アカウント** (個人 Gmail または Workspace): 1 つのアカウントですべての notebooks を管理します。将来チーム共有を行う場合は Workspace アカウントに統一することを推奨します
- [ ] **ウェブアクセス** [notebooklm.google.com](https://notebooklm.google.com): 本チュートリアルはすべて Web UI で操作します (NotebookLM には consumer GA API がありません)
- [ ] **本リポジトリをローカルに clone**: `../../notebooklm/current/uploads/*.md` 配下の **42 個の source ファイル**のアップロードと、`../../notebooklm/current/instructions.md` の Chat Custom mode への貼り付けが必要です

**「機能 vs 容量」について**:
- 公開版は **42/300 = 14%** の Pro source slot を使用します (cap を大きく下回り、8 slot headroom で将来の拡張にも対応可能です)
- 総 words 数 **1,582,085** (最大 bucket 302K < 500K/source cap、0 over-cap / 0 missing)
- Chat Custom mode instructions.md **8,925 Unicode chars / 10,000 char limit = 10.75% headroom**
- **カバレッジ**: 63/63 domains 全カバー / 176/176 Req 変数 ∅ gap (構造レベル + 意味レベル両アンカー閉鎖) / 295 md を全件収録し 42 concept bucket に分類

---

## 1. Notebook を作成

1. [notebooklm.google.com](https://notebooklm.google.com) に Pro サブスクリプションの Google アカウントでログインします
2. 左上の "**+ New notebook**" または "**Create new**" をクリックします
3. **命名推奨**: `SDTM Knowledge Base` または `CDISC SDTM Expert`
4. **Description** (任意、notebook の設定から入力可能): `SDTM (Study Data Tabulation Model) knowledge base from CDISC standards v3.4 IG. 42 concept-clustered sources covering 63 domains + 176 Req variables + chapters + terminology + examples. Answers variable definitions, Core attributes, codelist terms, cross-domain relationships, SUPPQUAL mechanics.`
5. **共有レベル** (デフォルトは Restricted。§8 で 3 段階切替を詳しく説明します): まず Restricted のまま開始し、smoke test 通過後に用途に応じて切り替えてください

---

## 2. Custom Mode Instructions を設定

NotebookLM には **System Prompt がありません**。prompt engineering できる唯一の入口は Chat の **Custom mode** (10K char limit) です。本公開版では `../../notebooklm/current/instructions.md` (8,925 Unicode chars、89.25% 使用) を提供しており、SDTM エキスパート prompt・13 条の behavior rules・アンカーポイントがすべて記述済みです。

### 操作手順

1. 作成した notebook を開きます
2. 右上の Chat エリアにある "**Configure**" またはギアアイコン → "**Custom**" mode を選択します (デフォルトは "Default"。他に "Learning Guide" があります)
3. `../../notebooklm/current/instructions.md` の内容を**すべてコピー**します (途中で切らないでください)
4. Custom goals の入力欄に貼り付けます
5. **Save** します

### instructions.md が密な理由

公開版の instructions.md には以下が含まれています:
- **13 条の behavior rules** — 優先順位 / citation 強制 / 境界に関する誠実さ / 推測しない
- **SDTM アンカーポイント** (頻出エラー箇所): AESER Core=Exp (Req ではない) / LBNRIND 4 値 Y/N/U/NA 全記載 / NY C66742 / ISO 8601 datetime / C-code のリテラル引用 / Day 1 は存在するが Day 0 は存在しない / RELREC+RELSPEC+RELSUB の 3 点セット / SUPP-- 構造
- **Authoritative layer の優先順位**: `spec > ch04 > CT > assumptions > examples` (同一変数で複数ソース間に矛盾が生じた場合、この優先順位で判断します)

**10.75% headroom** はその後の微調整用に確保されています (~1,000 chars で独自アンカーを 3〜5 個追加できます)。10K を超えると NotebookLM に切り捨てられますので、超過しないようにご注意ください。

### Custom mode は chat 単位で動的切替、notebook 全体をロックしません

Chat session ごとに Default / Learning Guide / Custom を独立して切り替えられます (UI レベル)。notebook 全体にロックされることはありません。確認したい場合:
1. 1 回の chat で "Learning Guide" に切り替え、AE ドメインのルールを質問 → Socratic 教育的な回答が返ってきます
2. "Custom" に戻して同じ質問 → 構造化された SDTM エキスパートの回答が返ってきます
3. 同一の source セットで、出力スタイルが異なることが確認できます

---

## 3. 42 sources をアップロード

1. notebook 左側の "**Sources**" パネルで "**+ Add**" をクリックします
2. "**Upload**" を選択します (ドラッグ&ドロップも可能です)
3. `../../notebooklm/current/uploads/*.md` から **42 個のファイル** (01〜42 番の bucket、MANIFEST.md は除く — MANIFEST は source 一覧ドキュメントであり source 本体ではありません) を**一括選択**します
4. **アップロード完了を待ちます**: 42 個のファイルが一括キューに入ります。Web UI は単一バッチをサポートしており、実測で約 2〜5 分ですべて転送が完了します

### 重要: "indexing silent fail" の防止

NotebookLM は公式に、ごく稀に indexing silent fail (ファイルがアップロードされたにもかかわらず実際には index されない) が発生する可能性を認めています。防御策は以下のとおりです:

- **UI tile レベルのスポットチェック**: アップロード完了後、各 source tile を一通り確認し、サムネイル + 文字数の推定値が妥当かどうか確認します。"0 words" や error 状態の tile があれば → **削除して再アップロード**してください
- **42 tile がすべて揃っていること**: 1 つも欠けてはいけません。すべての tile が "Indexed" の緑ステータスである必要があります
- **いくつかの source をクリックしてプレビュー**: 5〜10 個の source を抽出 (最初の source_01 + 最後の source_42 + 任意のいくつか) して開き、先頭の文章を確認します。「アップロード成功したが内容が文字化け」を防ぐためです

本リリース版アップロード時に 42/42 indexed、0 silent fail を測定済 (アップロードログ: `../../notebooklm/dev/evidence/p3_2_upload_log.md`)

---

## 4. Indexing を待つ

- NotebookLM の indexing は Claude よりも高速です。42 sources は通常 **2〜10 分**ですべて "Indexed" の緑ステータスになります
- UI の Sources パネルでは、各ファイルの横にステータスアイコンが表示されます:
  - 🟡 ぐるぐるマーク = indexing 中。この間は chat できません
  - ✅ 緑チェック = indexed 完了。chat 可能です
- すべて ✅ になってから §5 の smoke test に進んでください
- 30 分以上経っても黄色の loading が残っている場合、その source が silent fail している可能性が高いです → §3 の手順に従って再アップロードしてください
- **この間に並行してできること**: §2 の instructions.md の貼り付け (フォアグラウンド操作)。indexing はバックグラウンドで実行されるため、両作業を並行して行えます

---

## 5. Smoke Test

基本的な 3 問で notebook の基盤が安定していることを確認します。1 問でも FAIL した場合は次に進まないでください。

| # | 質問 | 期待される回答 | 確認ポイント |
|---|---|---|---|
| 1 | `AESER の Core 属性は Req か Exp か?` | **Exp (Req ではない)** | 最も頻出のエラーポイント。回答には `[08_ev_adverse_ae.md]` 類の citation が必須です |
| 2 | `LBNRIND の submission values をすべて挙げてください` | **Y / N / U / NA** (4 値すべて記載、LOW/HIGH/WITHIN REF は記載しない) | Extensible=Yes + `[33_ct_general.md]` citation を含むこと |
| 3 | `CMINDC はどのような場面で使いますか？CMTRT との関係は?` | **CMINDC = concomitant med の indication/reason。CRF の "Other, specify" は SUPPCM ワークフローで処理。CMTRT と統合しない** | citation 必須 + SUPPCM への言及 |

**3/3 PASS** → §6 の任意の完全回帰に進んでください。

**1 問 FAIL** の場合のトラブルシューティング:
- 回答に citation がない → Custom mode が有効になっていません。§2 に戻って instructions.md を再貼り付けしてください
- 回答で変数が KB に存在しないと言われる (実際には存在するはずの変数) → source の漏れまたは indexing fail です。§3 に戻り該当 source を再アップロードしてください
- 回答内容が誤っている (例: AESER=Req と回答) → instructions.md が途中で切り取られています。§2 に戻り文字数が 8,925 であることを確認してください

### Release v1.0 完全デモ
本チュートリアルの sanity 3 問に加え、release v1.0 では 10 問の完全デモも提供しています。詳細は [../DEMO_QUESTIONS.md](../DEMO_QUESTIONS.md) をご参照ください。NotebookLM は in-KB-only 設計のため、Q11/Q12 のような supplemental topics は PUNT (回答拒否) となります。これは**正しいハルシネーション対策の挙動であり、バグではありません**。詳細は [../KNOWN_LIMITATIONS.en.md](../KNOWN_LIMITATIONS.en.md) §L4-NB5 をご参照ください。

---

## 6. 完全回帰

本リリース版は 17 問完全題庫 (3 問のアンチハルシネーション問題を含む) を完全テスト済です。実測 **15/17 PASS (88.2%)**、3 問のアンチハルシネーション問題すべてを見破り、4 プラットフォームの中で並列最強です (NotebookLM の in-KB-only アーキテクチャは構造的にアンチハルシネーションです)。これら 17 問を再実行して、ご自身でデプロイした notebook が同様に安定していることを検証できます。

- **題庫**: [`../../../SMOKE_V4.md`](../../../SMOKE_V4.md) §2
- **問ごとの回答 + verdict**: `../../notebooklm/dev/evidence/smoke_v4_answers/*.md`
- **集計レポート**: `../../notebooklm/dev/evidence/smoke_v4_results.md`
- **合格基準**: ≥12/17 (71%) — R1 初回テストの許容範囲

### 17 問の内訳

| カテゴリ | 問番号 | テスト内容 |
|----------|--------|-----------|
| Sanity | sanity_01-03 | 基盤の安定性確認 (§5 と同じ) |
| v3.4 新ドメイン | Q1-Q3 | GF / CP / BE+BS+RELSPEC |
| ドメイン境界 | Q4-Q5 | LB/MB/IS / FA/QS/CE |
| Timing | Q6-Q7 | PK 採血 4 点セット / Partial date |
| CT | Q8 | Extensible vs Non-Extensible |
| Pinnacle 21 | Q9 | 一般的な FAIL 分類 (NotebookLM は safety-correct PUNT が予想されます) |
| SUPP 詳細 | Q10 | QORIG/QEVAL + SUPPTS 前提の誤り指摘 |
| Bonus | Q11-Q14 | Dataset-JSON / CT バージョン / RWD / AE+CE+MH+DS の連携 |
| **AHP (anti-hallucination)** | AHP1-3 | **変数の虚構 / クロスドメインの虚構 / deprecated 虚構** — in-KB-only による天然優位性のテスト |

### 予想される結果

- Q1〜Q8 / Q10 / Q14 / AHP1〜3 は PASS が期待されます (90%+)
- Q9 は **FAIL が予想されます** (safety-correct PUNT。in-KB-only アーキテクチャでは Pinnacle 21 の外部ドキュメントに自然にアクセスできないためです — 能力の FAIL ではありません)
- Q11〜Q12 は **PARTIAL が予想されます** (supplemental topics であり in-KB のカバレッジが不完全です)
- 3 問のアンチハルシネーション問題すべてで PASS+ が期待されます — NotebookLM のアーキテクチャはハルシネーション対策に天然の優位性があります

---

## 7. 3 段階共有レベル切替

NotebookLM は同一の notebook 内で 3 段階の共有レベルを動的に切り替えられます。複数の notebook を作成する必要はありません。3 段階切替の実測は 2026-04-23 に VERIFIED + 詳細確認済みです (`../../notebooklm/dev/evidence/share_level_toggle_drill.md`)。

### 3 段階の意味

| レベル | アクセス規則 | 適用場面 | 50-cap 規則 |
|--------|-------------|---------|-------------|
| **Restricted** (デフォルト) | owner + 招待リストに登録された Google アカウントのみ | 個人利用 / 小規模チーム | **Free tier の invitee には 50 source cap が適用されます** (Pro の owner は制限なし) |
| **Anyone with link** | リンクを持つ任意の Google アカウントでログインすれば閲覧可能 | 限定的な外部配布 / 社内広報 | Free tier cap は適用されません |
| **Public** | リンクを誰とでも共有できます (Google へのログインは引き続き必要です) | オープンなナレッジベース | Free tier cap は適用されません |

### 切替手順

1. notebook 右上の "**Share**" ボタン → Share パネルを開きます
2. 希望のレベルを選択し、"**Copy link**" でアクセスリンクを生成します
3. Restricted に戻すと、以前のリンクが**即座に revoke** されます (実測 PASS、キャッシュの残留なし)

### 重要: Public レベル ≠ 自動広報 (実測の新発見)

- Public レベルとは「**リンクを持つ人なら誰でもログイン不要でアクセス可能**」という意味であり、NotebookLM の公開ギャラリーに自動掲載されるわけではありません
- NotebookLM の公開ギャラリー (Featured) は**キュレーションされたリスト**であり、自動掲載ではありません。Public レベルにしても**自動的に公開されることはありません**
- **プライバシー保護の観点**では ChatGPT GPT Store の "Public = 全世界に公開" という意味合いよりも保守的です
- 適している場面: 小規模な社内共有 + 限定的な外部配布の組み合わせ

### Free tier 50-cap は Restricted + 招待の場面にのみ適用

- Restricted レベル + Free tier Gmail のサブアカウントを招待した場合、そのサブアカウントは**前 50 source しか閲覧できない可能性があります**
- 本公開版は 42 sources ≤ 50 であり、**影響はありません**
- 将来 ≥ 51 sources に拡張し、かつ Free tier viewer のアクセスが必要な場合は、A/B/C の解釈で実測が必要です (PLAN §3.3 参照)

---

## 8. トラブルシューティングガイド

| 症状 | 診断 | 対処 |
|------|------|------|
| 回答に citation がない | Custom mode が有効になっていない | §2 に戻り instructions.md を再貼り付けして、Save の緑チェックを確認してください |
| 回答で変数が KB に存在しないと言われる (実際には存在するはずの変数) | source の indexing silent fail | §3 で該当 source tile のステータスを確認し、黄色の loading がタイムアウトしていれば削除して再アップロードしてください |
| AESER を Req と回答する | instructions.md が途中で切り取られている | 原文の文字数は wc -m で 8925。貼り付け後の文字数が著しく少ない場合は再貼り付けしてください |
| 17 問 Q9 FAIL (アーキテクチャ制限) | **予想どおりの動作** — in-KB-only アーキテクチャの制限による safety-correct PUNT です | instructions.md に「外部推論を許可する」を追加しないでください。3 問のアンチハルシネーション問題すべて見破りの優位性が低下します |
| AHP1〜3 で虚構が発生する (例: LBCLINSIG が存在すると回答) | instructions.md の「境界に関する誠実さ」アンカーが機能していない | §2 に戻り instructions.md が完全であるか確認します。または Chat mode を切り替えてから Custom に戻してリフレッシュしてください |
| Anyone-with-link レベルの Pro viewer が source を全件閲覧できない | 本来ならあり得ません。このレベルには Free tier cap は適用されません | Google アカウントのログイン状態を確認し、share link を再生成してください |
| 小テーブルのレンダリングがずれる (単一行のズレ) | F-1-recurring として認識されている既知の現象。意味的なスコアには影響しません | 同じ質問を再度送信すると通常は改善されます。retry の冪等性は保証されていません |
| citation が欠落する (実務場面の質問) | F-3 システム的な弱点 (T2 問題タイプの偏り) | 回答内容は通常正確です。citation が稀に欠落しますが、意味的なスコアには影響しません |

---

## 9. アップグレード / メンテナンス

### 拡張 (42 → N sources)

- Pro cap は 300 source。現在 14% 使用中で、8 slot + 258 Pro cap headroom があります
- KB を拡張する場合 (例: SDTMIG 次バージョン v3.5 / 新ドメイン追加)、`../../notebooklm/dev/scripts/bucket_config.json` に bucket 43 以降を追加 → `merge_sources.py` を実行 → 新しい source を差分アップロードしてください
- 注意: ≥ 51 sources になると Free tier viewer の 50-cap が適用されます。Free tier 実測をやり直す必要があります

### ダウングレード (42 → Free tier 対応)

- Free tier 上限: 50 notebooks × 50 sources × 150K words/source × 50 chat/day × 3 audio/day
- **本公開版は Free tier では words cap を超過します**: 最大 bucket 302K > 150K/source Free cap → bucket の再分割が必要です (細粒度に分割し、各 bucket を < 150K にします)
- 再分割の手順: `../../notebooklm/dev/scripts/` で新しい config を作成し、80〜100 bucket にパックして再アップロードします
- 作業時間の見積もり: 1〜2 日

### instructions.md の微調整

- 10K char 制限があり、10.75% headroom (~1,075 chars、独自アンカーを 3〜5 個追加可能)
- アンカーを追加する際は CLAUDE.md + RETROSPECTIVE.md R-NBL-3 も合わせて更新してください
- 10K を超えると切り捨てられます。貼り付け前に wc -m で確認してください

---

## 10. 今後のパス

### 10.1 すぐに使えること

- 任意の SDTM 変数の定義 / Core 属性 / codelist 値を質問できます
- ドメイン境界を質問できます (LB vs MB vs IS / FA vs QS vs CE)
- Timing (--TPT 4 点セット / Partial date) を質問できます
- SUPPQUAL のメカニズム / RELREC の 3 点セットを質問できます
- **誤った前提を与えて** NotebookLM に誤り指摘をさせる使い方 (AHP の得意分野)

### 10.2 既知の制限 (in-KB-only アーキテクチャ)

NotebookLM は sources からのみ回答するという強い制約があり、学習データやウェブにはアクセスしません。**これは優位性 (AHP) でもあり制限でもあります**:

- Pinnacle 21 レポートの分類 → **PUNT**
- Dataset-JSON / XPT v5 の比較 → supplemental topic PUNT (一部の分岐)
- RWD (Claims / EHR) 固有の SUPP フィールド → PUNT
- CT バージョンの operational milestones へのロック → 一部の分岐で PUNT

これらが必要な場合は、Claude / ChatGPT / Gemini の各プラットフォームを補完的に活用してください (本プロジェクトでは同時に複数プラットフォームへのデプロイを行っています)。

### 10.3 ICEBOX (post-project optional)

PLAN §10 に保留されている Studio の 3 点セット:
- **Audio Overview** × 3 回 (SAFETY / EFFICACY / PK Deep Dive ポッドキャスト、各 30〜45 分)
- **Mind Map**: 63 domain のクロスドメイン関係 + RELREC/SUPPQUAL のカバレッジ
- **Study Guide**: AE / LB / CM の Socratic ガイド形式

実行条件: ユーザーが「Studio の 3 点セットをあとで精製したい」と申し出た場合。申し出がない場合はメインの retro + 本チュートリアルの FINAL に影響しません。

### 10.4 関連ドキュメント

| ドキュメント | パス | 用途 |
|-------------|------|------|
| **RETROSPECTIVE (本プラットフォーム)** | `../../notebooklm/docs/RETROSPECTIVE.md` | Rule C の 3 段構成 + pivot 事例 + _template/ パッチ |
| **4 プラットフォーム横断 Phase 5 retro** | `../../retrospectives/PHASE5_RETROSPECTIVE.md` | v1.0 FINAL 2026-04-24 Daisy 承認済み 4 プラットフォーム sign-off |
| **PLAN** | `../../notebooklm/docs/PLAN.md` | 662 行 v2.2 (アーキテクチャ pivot 後の完全 plan) |
| **完全 17 問テスト結果** | `../../notebooklm/dev/evidence/smoke_v4_results.md` + `smoke_v4_answers/` | 17 問の問ごとの verdict |
| **3 段階切替 evidence** | `../../notebooklm/dev/evidence/share_level_toggle_drill.md` | v1.0 FINAL 6 サブステップ + Public 意味論の詳細確認 |
| **v1→v2 アーキテクチャ pivot 記録** | `../../notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` | 重要な教訓: Writer の叙述合成における疑似制約 |
| **reviewer レポート** | `../../notebooklm/dev/evidence/phase5_retrospective_reviewer.md` | v0.2 post-fix 独立審査 10 アクションアイテム |

---

## 付録: デプロイ後セルフチェックリスト

デプロイ完了後、以下のチェックリストを一通り確認してください:

- [ ] notebook を新規作成し、`SDTM Knowledge Base` と命名した
- [ ] Chat Custom mode に instructions.md の全文を貼り付けた (8,925 chars)
- [ ] 42 個の source をアップロードし、すべて ✅ Indexed になった
- [ ] Smoke 3 問 (AESER Core / LBNRIND 4 値 / CMINDC 場面) が 3/3 PASS した
- [ ] (任意) 完全 17 問テストで ≥ 12/17 PASS した
- [ ] 3 段階切替を ≥ 2 レベル確認した (少なくとも Restricted と Anyone with link)
- [ ] notebook URL をチームに共有した (Anyone-with-link / Public レベルのみ)
- [ ] 本チュートリアル §10.2 の既知の制限を読み、Pinnacle 21 などの要件を NotebookLM に無理に求めないようにした

---

*v1.0 — 2026-04-27 — 社内公開版*
*本プラットフォーム独立 retro: ../../notebooklm/docs/RETROSPECTIVE.md ; release v1.0 概要: ../README.ja.md*
