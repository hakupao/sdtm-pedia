# ChatGPT GPT 作成チュートリアル — SDTM ナレッジベース公開版

> ゼロから CDISC SDTM 標準 (63 ドメイン + terminology + chapters) を検索できる Custom GPT を構築します。
> このチュートリアルを完了すると、SDTM 変数定義 / codelist / examples / クロスドメイン関連を正確に回答でき、よくある虚構前提 (LBCLINSIG / SUPPTS / PF deprecated など) を見破ることができる ChatGPT GPT が得られます。
> 総所要時間: **30〜60 分** (indexing 待機時間を含む)。

---

## 0. 前提要件

- [ ] **ChatGPT Plus / Team / Enterprise** プラン (無料プランでは Custom GPT を作成できません)
- [ ] **Web アクセス** [chatgpt.com](https://chatgpt.com): 本チュートリアルはすべて Web UI での操作です
- [ ] **本リポジトリをローカルに clone**: `../../chatgpt_gpt/current/` 配下の `system_prompt.md` (約 8.6KB) および `uploads/` 配下の 9 個の .md ファイルが必要です

**「チーム共有 vs GPT Store 公開」について**:
- Org/Team プラン内ではメンバーを直接 email で招待でき、**審査なし**で共有できます
- GPT Store での公開は OpenAI の審査が必要です (通常 1〜3 営業日)。すべての ChatGPT ユーザーがアクセスできるようになります

---

## 1. Custom GPT を新規作成

1. [chatgpt.com](https://chatgpt.com) にログインします
2. 左下の "**Explore GPTs**" をクリック → 右上の "**+ Create**" をクリックします
3. **Configure** タブに移動します (Create タブの会話モードではありません)
4. **Name**: `SDTM Expert` または `CDISC SDTM Knowledge` を推奨します
5. **Description** (英語で 1 文、約 130 文字): `CDISC SDTMIG v3.4 + SDTM v2.0 Expert — Variable definitions, rule reasoning, controlled terminology, cross-domain linking.`
6. **Capabilities**: **Web Search / Code Interpreter / DALL-E** をすべてオフにします (この GPT は純粋な知識検索用であり、これらを有効にするとハルシネーションのリスクが高まります)

---

## 2. Instructions (System Prompt) を設定

1. 引き続き Configure タブで、"**Instructions**" フィールドを見つけます
2. `../../chatgpt_gpt/current/system_prompt.md` の全文を**完全にコピー**して貼り付けます (v2.2 LIVE、8,582 chars)
3. **途中で切断しないでください**: ChatGPT UI の文字数インジケーターは 8000 chars と表示されますが、実測では 8,582 chars まで受け付けます (verified、デプロイ済みで動作中)。ChatGPT UI が受け付けない場合は、§Conversation Starters セクション (非コア部分) を優先的に削除してください
4. **保存**します

**v2.2 LIVE の主要機能** (貼り付け後は変更しないでください):
- GFINHERT 7 文字の正確なスペル (R1 での GFINHERTG extra-G スペルドリフトを修正)
- L858R / Exon 19 科学的一貫性の能動的識別 (anti-hallucination ボーナス)
- AHP × 3 反ハルシネーションアンカー (変数レベル / クロスドメインレベル / deprecated レベル)

---

## 3. ナレッジベース 9 ファイルをアップロード

1. Configure タブで "**Knowledge**" パネルを見つけ、"**Upload files**" をクリックするかドラッグ＆ドロップします
2. `../../chatgpt_gpt/current/uploads/` 配下の **9 個の .md ファイルすべて**を選択します。順序は `01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09` です
3. **ファイル名を変更したり、分割・結合したりしないでください**: ファイル名のプレフィックスは System Prompt のルーティングアンカーです

**ファイル一覧 (9 ファイル、合計 ~2.5M tokens)**:
- `01_navigation.md` (~46K) — ROUTING + INDEX + VARIABLE_INDEX
- `02_chapters_all.md` (~60K) — SDTMIG ch01/02/03/04/08/10
- `03_model_all.md` (~17K) — SDTM v2.0 Model 6 セクション
- `04_domain_specs_all.md` (~185K) — 63 ドメイン spec 全量フラット
- `05_domain_assumptions_all.md` (~54K) — 63 ドメイン assumptions
- `06_domain_examples_all.md` (~220K) — 63 ドメイン examples
- `07_terminology_core_high_freq.md` (~200K) — core 高頻度 15 codelist
- `08_terminology_quest_and_supp.md` (~1M) — questionnaires + supplemental
- `09_terminology_core_mid_tail.md` (~698K) — core 中〜低頻度

ChatGPT GPT Builder Knowledge には **20 ファイルのハード制限**があります。現在 9/20 (11 ファイルの空き)。

**よくある Q**:
- "File too large" → ファイルがエディタにより BOM / CRLF が追加されていないか確認してください。UTF-8 LF で保存し直してください
- アップロードが 90% で止まる → ネットワークの問題です。ページを更新してください (アップロード済みのファイルは保持され、残りを続けてアップロードできます)

---

## 4. Indexing を待つ

ChatGPT File Search RAG の indexing は通常 **5〜15 分**かかります。UI 上で各ファイルのステータスが "Processing..." から "Ready" に変わります。すべてが Ready になってから §5 に進んでください。

実際には「全ファイルの indexing 完了」を示す明確なインジケーターはありません。個別ファイルが Ready になった時点で使用可能と見なします。

---

## 5. Smoke Test (3 問、~5 分)

**右上の Preview** から、1 問ずつ新しい chat で質問してください:

| # | 質問 | 期待されるポイント | 検証内容 |
|---|------|---------|------|
| T1 | `AESER の Core 属性は何ですか？NY codelist (C66742) のすべての term 値を列挙してください。` | Core = **Exp** (Req ではない)；4 term: **Y / N / U / NA** + C-code | 最高頻度の誤りやすい項目 + 高頻度 codelist の命中 |
| T2 | `GFINHERT はどのような変数ですか？どのドメインに属しますか？` | GF (Genomics Findings、v3.4 新ドメイン)；INHERT のフルネームは Inherited；7 文字の正確なスペル (GFINHERTG ではない) | v3.4 新ドメイン識別 + v2.2 スペル修正 |
| T3 | `LBCLINSIG はどの codelist にありますか？` (虚構の変数) | GPT は**見破るべき**: LBCLINSIG は LB ドメイン v3.4 spec に存在しない；LBNRIND / LBSTRESC の使用を推奨 | AHP1 anti-hallucination |

**3/3 PASS** = デプロイ成功。いずれかが FAIL の場合 → §7 トラブルシューティングガイドを参照してください。

---

## 6. 完全回帰 (10 問、オプション ~30 分)

`../DEMO_QUESTIONS.md` を開き、Q1〜Q10 を順番に質問します。**1 問ごとに新しい chat** を使用してコンテキスト汚染を避けてください。スコア ≥ 8/10 = ベースラインリリース版と同等。

---

## 7. トラブルシューティングガイド

| 症状 | 考えられる原因 | 対処方法 |
|------|---------|------|
| GFINHERTG (extra G) と回答する | Instructions が v2.2 LIVE でない | system_prompt.md 末尾の "v3.4 新域変量名精確校驗" セクションが含まれているか確認する |
| PF ドメインの変数リストを回答する (PF deprecated) | AHP3 アンカーが有効でない | system_prompt §CO-5 AHP-V3 + 反ハルシネーションセクションを再確認する |
| "SUPPTS はデータセット" と回答する | SUPP scope セクションが欠如 | system_prompt §SUPP scope が完全かどうか確認する (SUPPQUAL は Trial Design には非対応) |
| File Search が誤ったセクションを召喚する | ファイルのセグメンテーション失敗 | system_prompt §P13 TableAware プロンプトが含まれているか確認する；問題のファイルを再アップロードする |
| "AESER Core = Req" と回答する | 04_domain_specs_all.md が未アップロードまたは途中切断 | 再アップロードする；ファイルサイズが ≥ 180KB であることを確認する |
| 20 ファイル以上のアップロード警告 | GPT Builder のハード制限に達した | ダウングレードパス §8 に従いファイルを削除する |
| 最初のトークンが遅い / 頻繁にレート制限 | Plus プランの RAG レート制限 | 30〜60 秒待ってから再試行する；継続する場合は Team/Enterprise へ移行する |

---

## 8. アップグレード / ダウングレードパス

**アップグレード (KB 拡張)**:
- 現在 9/20 ファイル、11 ファイルの空きあり
- v3.5 SDTMIG 新ドメイン / questionnaires の長尾を追加する場合は、`dev/scripts/` に bucket を追加 → merge → 増分アップロードします

**ダウングレード (容量警告時)**:
削除の優先順位 (最も有用なものを保持):
1. まず `09_terminology_core_mid_tail.md` を削除 (中〜低頻度)
2. 次に `08_terminology_quest_and_supp.md` を削除 (questionnaires 長尾)
3. 次に `06_domain_examples_all.md` を削除 (examples)

最低限保持するファイル: `01-05 + 07` (ナビゲーション + chapters + model + spec + assumptions + 高頻度 CT) = 6 ファイルのコア。

---

## 9. チーム協業 / GPT Store 公開

**Org/Team チーム共有**:
- 審査なし、email で直接招待できます
- メンバーには**同一の GPT** が表示され、Instructions の変更は全員に即時反映されます
- 誤った変更を防ぐため、編集権限は 1〜2 名に制限することを推奨します

**GPT Store 公開**:
- OpenAI の審査が必要です (目安 1〜3 営業日)
- 全世界からアクセス可能になり、オープンなナレッジベースに適しています
- 名称 / Description に機密キーワードや社内コードを含めないよう注意してください

---

## 10. 今後のパス

- 本リリース版はすでに**完全な最終状態**であり、短期間での容量拡張予定はありません
- 長尾の questionnaires + 6 つの MedDRA レベルの大規模 codelist は、今後の Phase 7 自作 RAG に委ねます
- ナレッジベースの内容に誤りや欠落がある場合は、プロジェクトの issue tracker にフィードバックしてください。修正後、リリース版を再ビルドして配布します

---

## 付録: 検証チェックリスト

- [ ] ChatGPT Plus / Team / Enterprise プランが有効になっている
- [ ] Custom GPT を作成し、名称が明確に設定されている
- [ ] Instructions に system_prompt.md の全文が貼り付けられている (v2.2 LIVE、8,582 chars)
- [ ] Knowledge パネルに 9 ファイルすべてが Ready と表示されている
- [ ] T1 AESER + C66742 smoke PASS
- [ ] T2 GFINHERT の正確なスペル PASS (GFINHERTG ではない)
- [ ] T3 LBCLINSIG 反ハルシネーション識別 PASS

すべて ☑ = デプロイ成功。日常利用を開始できます。

---

*v1.0 — 2026-04-27 — 社内公開版*
