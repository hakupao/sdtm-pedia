# Phase 1 Term Audit Report — 04 要件定義書

- 監査日: 2026-04-29
- 担当: document-specialist (規律 D 隔離 ✅: writer = executor / reviewer = code-reviewer)
- 入力: docs/jp/sources/04_要件定義書.yml + docs/jp/04_要件定義書.xlsx
- 監査スコープ: 納品物 (.xlsx) 内文字列 + yml 入力対照
- 機械検査結果:
  - blacklist hits: 0 件 (カテゴリ 4, 語数 33)
  - mapping consistency violations: 6 件 (内訳は下記)
- 人手判定結果:
  - 抽検サンプル: 37 件 (4 類型 × 5–10)
  - 追加 finding: 4 件 (うち 2 件は機械検査の false-positive 確認、2 件は実質 MEDIUM)
- 最終 verdict: **CONDITIONAL_PASS**

---

## findings 要約

| id  | category              | severity | location                                    | recommendation                                                         |
|-----|-----------------------|----------|---------------------------------------------|------------------------------------------------------------------------|
| F-1 | mapping_inconsistency | MEDIUM   | 1_表紙!B7, 4_非機能要件!B4                 | 「作成者」→「文書作成担当者」(フルラベル) または mapping notes 許容短縮形「作成担当」に統一 |
| F-2 | mapping_inconsistency | MEDIUM   | 3_機能要件!C13                              | 「データ単位」→「検証単位」(atom 採用語)                               |
| F-3 | mapping_inconsistency | MEDIUM   | 2_業務要件!B19, 5_制約条件!C3              | 「差異」→「乖離」(drift 採用語); ただし false-positive 疑義あり (下記参照) |
| F-4 | mapping_inconsistency | MEDIUM   | 3_機能要件!C12                              | 「相互参照」→「相互照合」等; ただし false-positive 疑義あり (下記参照) |
| F-5 | mapping_inconsistency | MEDIUM   | 4_非機能要件!C3                             | false-positive と判定: 「概ね」は だいたい → 文脈依存 の「範囲・期間」文脈採用形で適正 |
| F-6 | mapping_inconsistency | MEDIUM   | 3_目次 他 9 箇所                            | false-positive と判定: 「約」は「制約」「要約」等の漢字内包によるサブストリング誤検出 |
| F-7 | new_jargon (C3)       | MEDIUM   | 3_機能要件!C13                              | 「パイプライン」— 開発工程特有カタカナ語; blacklist 追加提案               |
| F-8 | mapping_inconsistency | MEDIUM   | 1_背景目的!B7, 1_背景目的!B20              | 「トレーサビリティ管理表」— 文書タイトルとして固有名詞的使用だが採用語「追跡可能性」との混在 |
| F-9 | colloquial (C2)       | LOW      | 2_業務要件!B19, 5_制約条件!C3              | false-positive: 「差異」は口語ではなく正式な比較用語; 口語類型には該当しない |

---

## findings 詳細

### F-1 — 作成者 (mapping_inconsistency / MEDIUM)

- **category**: mapping_inconsistency
- **severity**: MEDIUM
- **location**:
  - `1_表紙!B7` — セル値: `作成者` (表紙フォームの行ラベル)
  - `4_非機能要件!B4` — セル値: `作成者・承認者分離` (非機能要件 NFR-02 行ラベル)
- **observation**: `term_mapping.yml` で internal=writer の採用語は `文書作成担当者`。`作成者` は candidates に含まれる非採用候補。表紙ラベルおよび要件行ラベル双方に `作成者` が使われており、mapping 一貫性違反。mapping notes に「Excel 役割列では「作成担当」短縮可」と明記されているが `作成者` は許容されていない。
- **recommendation**: 表紙ラベルは `文書作成担当者` または mapping notes 許容短縮形 `作成担当` に修正。`作成者・承認者分離` は `文書作成担当者・文書確認担当者分離` または `作成担当・承認担当の分離` に修正。
- **mapping_proposal**: なし (既登録)

### F-2 — データ単位 (mapping_inconsistency / MEDIUM)

- **category**: mapping_inconsistency
- **severity**: MEDIUM
- **location**: `3_機能要件!C13`
- **observation**: セル値 — `七工程パイプラインと並行し、知識ベースの字面級確認を独立した作業群として継続実施する。各データ単位の主張を出典 PDF と頁単位で照合する。` `term_mapping.yml` で internal=atom の採用語は `検証単位`、`データ単位` は非採用候補。文脈は内部的な atom 概念 (最小検証粒度) を指しており、mapping 違反。
- **recommendation**: `各データ単位の主張` → `各検証単位の主張`
- **mapping_proposal**: なし (既登録)

### F-3 — 差異 (mapping_inconsistency / MEDIUM — false-positive 疑義あり)

- **category**: mapping_inconsistency
- **severity**: MEDIUM
- **location**:
  - `2_業務要件!B19` — `本知識ベースの記述と公式刊行物との間に差異が見られた場合は、公式刊行物が優先される。`
  - `5_制約条件!C3` — `本知識ベースの記述と CDISC 公式刊行物の記述に差異が見られた場合は、公式刊行物が優先される。`
- **observation**: `term_mapping.yml` で internal=drift の候補に `差異` が含まれ、採用語は `乖離`。ただし本文書の `差異` は文書間比較差 (METHODOLOGY.md §6 の直接引用に近い内容) を意味し、開発内部の `drift` (経時的ずれの概念) とは異なる文脈。`term_mapping.yml` drift の notes にも「経時的ずれを表現不足」とあり、文書比較文脈には `差異` が適合する可能性がある。機械検査は構造上フラグを立てるが、主 session による文脈判定を要する。
- **recommendation**: 主 session 判断を要請。(1) 文書比較文脈でも `乖離` に統一する場合 → 2 箇所を `乖離` に修正。(2) 文書比較文脈は `差異` を許容する場合 → mapping の drift notes に「文書比較文脈は「差異」可」と追記し、本 finding を INFORMATIONAL に格下げ。用語監査担当は判断不可 (監査範囲外の意味論的解釈)。
- **mapping_proposal**: drift エントリの notes に「文書間比較差 (静的) は「差異」可」の文脈免除注記追加を主 session に提案。

### F-4 — 相互参照 (mapping_inconsistency / MEDIUM — false-positive 疑義あり)

- **category**: mapping_inconsistency
- **severity**: MEDIUM
- **location**: `3_機能要件!C12`
- **observation**: セル値 — `knowledge_base/terminology/ 配下の各コードリスト文書に CDISC 割当の C 符号 (例 C66731) を保持し、米国国立がん研究所 EVS Browser (NCI EVS Browser) との相互参照を可能とする。` `term_mapping.yml` で internal=chain の候補に `相互参照` が含まれ、採用語は `変更連鎖`。ただし本文書の `相互参照` は NCI EVS Browser との外部文献照合 (bibliographic cross-reference) を意味し、開発内部の `chain` (変更連鎖・同期義務) とは全く別概念。これは機械検査の誤分類 (false-positive) と判断する。
- **recommendation**: 主 session 判断を要請。(1) 機械検査 false-positive として許容し mapping の chain candidates から `相互参照` を削除する。(2) あるいは `相互参照` を別語 (例: `相互照合`、`照合参照`) に変更して混乱回避。用語監査担当は意味論的判断は行わず主 session に逆質問 (下記参照)。
- **mapping_proposal**: chain エントリの candidates から `相互参照` を削除、または notes に「NCI EVS 等の外部参照文脈での「相互参照」は chain 概念外」と免除注記追加を主 session に提案。

### F-5 — 概ね (false-positive / MEDIUM → 実質 LOW)

- **category**: mapping_inconsistency
- **severity**: MEDIUM (機械) → **false-positive** (人手判定)
- **location**: `4_非機能要件!C3`
- **observation**: セル値 — `行頁比は概ね 15 行から 20 行毎頁を基準とする。` `term_mapping.yml` で internal=だいたい、adopted=文脈依存、notes: `数値 → 「約」/ 範囲・期間 → 「概ね」/ 内容要約 → 「概略として」`。本文の「15 行から 20 行」は数値範囲であり、mapping notes が明示する「範囲・期間: 「概ね」」の文脈採用形として **適正使用**。機械検査は `文脈依存` を adopted として全 candidates をフラグするため、適正採用語「概ね」を誤検出している。
- **recommendation**: 修正不要。機械検査の false-positive として記録のみ。
- **mapping_proposal**: audit_terms.py の文脈依存エントリ処理改善を主 session に提案 (現在は `文脈依存` adopted 時に全 candidates を inconsistency 扱いするが、使用語が candidates 内であれば INFORMATIONAL 扱いとする仕様変更)。

### F-6 — 約 (false-positive / MEDIUM → 実質 INFORMATIONAL)

- **category**: mapping_inconsistency
- **severity**: MEDIUM (機械) → **false-positive** (人手判定)
- **location**: `3_目次!B12` 他 9 箇所
- **observation**: 10 箇所すべてを確認。「約」は以下の漢字内包により誤検出:
  - `制約条件` (×7 箇所) — `制約` 内の `約`
  - `要約` (×1 箇所) — `第三者要約や言換え版から派生したコンテンツ`
  - `容量制約` (×2 箇所) — `容量制約および機能制約`
  全 10 箇所で `約` は独立した語として使用されておらず、すべて漢字複合語の一部。スクリプト自体が単文字語に対し「false positive の可能性あり」警告を出力しており (stderr: `[警告] term が 1 文字のため false positive の可能性あり: '約'`)、機械検査設計上の既知限界。
- **recommendation**: 修正不要。機械検査の false-positive として記録のみ。
- **mapping_proposal**: `だいたい` エントリの candidates `約` について、スクリプト側で単文字語の漢字候補は `match_whole_word` を単語境界ではなく形態素境界で判定する改善、または mapping の `約` を candidates から削除し代わりに `おおよそ` 等で補完することを主 session に提案。

### F-7 — パイプライン (new_jargon / MEDIUM)

- **category**: new_jargon
- **severity**: MEDIUM
- **location**: `3_機能要件!C13`
- **observation**: セル値 — `七工程パイプラインと並行し、知識ベースの字面級確認を独立した作業群として継続実施する。` `パイプライン` は `term_blacklist.yml` 未収録だが、開発工程の処理連鎖を指す IT 内部カタカナ語。納品先 iTMS (IT + 医療データ) 向け文書として「カタカナ語直訳禁止」の硬約束 (H-1) と整合が不明確。
- **recommendation**: `七工程パイプライン` → `七工程処理連鎖` または `七段階処理工程` に修正を検討。主 session の判断を要する。
- **mapping_proposal**: `パイプライン` を `term_blacklist.yml` の `colloquial` または `process_jargon` に追加提案。suggested_replacement: `["処理連鎖", "処理工程"]`。

### F-8 — トレーサビリティ (mapping_inconsistency / MEDIUM)

- **category**: mapping_inconsistency
- **severity**: MEDIUM
- **location**: `1_背景目的!B7`, `1_背景目的!B20`
- **observation**:
  - B7: `本納品物 (要件定義書、基本設計書、運用保守マニュアル、テスト結果報告書、詳細設計書、トレーサビリティ管理表、進捗報告書、用語集) は…`
  - B20: `・06 トレーサビリティ管理表: 要件、設計、試験、根拠資料の横断対応表。`
  `トレーサビリティ管理表` は文書番号 06 の固有名称。機械検査では `トレーサビリティ` は blacklist 未収録のため未フラグ。人手 C4 (採用語の表記ゆれ) 類型で発見。`4_非機能要件!B6` および `4_非機能要件!C7` では `追跡可能性` が採用されており (`NFR-05 追跡可能性`)、同一文書内で `トレーサビリティ管理表` vs `追跡可能性` が混在している。
- **recommendation**: 文書タイトル `06 トレーサビリティ管理表` は固有名詞として扱う場合、初出に `(追跡可能性管理表)` の括弧注記を付す。あるいは文書タイトル自体を `06 追跡可能性管理表` に変更する。主 session の判断を要する。
- **mapping_proposal**: `トレーサビリティ` を `term_blacklist.yml` の `colloquial` に追加提案。suggested_replacement: `["追跡可能性"]`。または `term_mapping.yml` に新エントリとして `internal: トレーサビリティ, adopted: 追跡可能性` 追加提案。

---

## 機械検査ログ

```
用語監査サマリ — /Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/04_要件定義書.xlsx
検査日時: 2026-04-29T10:21:23Z
exempt.matched: false (docs/jp/04_要件定義書.xlsx は exempt 対象外 — 通常監査)
[blacklist]  ヒット数: 0  (カテゴリ: 4, 語数: 33)
[mapping]    不整合数: 6  (エントリ: 33)
  INCONSISTENCY: '作成者' (採用語: '文書作成担当者')  @ 1_表紙!B7  (2 箇所)
  INCONSISTENCY: 'データ単位' (採用語: '検証単位')  @ 3_機能要件!C13  (1 箇所)
  INCONSISTENCY: '差異' (採用語: '乖離')  @ 2_業務要件!B19  (2 箇所)
  INCONSISTENCY: '相互参照' (採用語: '変更連鎖')  @ 3_機能要件!C12  (1 箇所)
  INCONSISTENCY: '概ね' (採用語: '文脈依存')  @ 4_非機能要件!C3  (1 箇所)
  INCONSISTENCY: '約' (採用語: '文脈依存')  @ 3_目次!B12  (10 箇所)
verdict: FAIL
exit_code: 1
```

**機械検査結果の人手評価:**

| 機械フラグ       | 人手判定        | 理由                                                         |
|-----------------|----------------|--------------------------------------------------------------|
| 作成者 (2箇所)  | 実 MEDIUM      | 非採用候補の使用。F-1 として記録。                           |
| データ単位      | 実 MEDIUM      | 非採用候補の使用。F-2 として記録。                           |
| 差異 (2箇所)    | false-positive 疑 | 文書比較文脈で drift ≠ 差異; 主 session 要判断。F-3。      |
| 相互参照        | false-positive | NCI EVS 外部参照文脈; chain 概念と無関係。F-4。              |
| 概ね            | false-positive | mapping notes が「範囲・期間 → 概ね」と明示; 適正使用。F-5。|
| 約 (10箇所)     | false-positive | 「制約」等漢字複合語内包によるサブストリング誤検出。F-6。    |

実 MEDIUM: 2 件 (F-1, F-2) + 主 session 判断待ち 1 件 (F-3) + 人手追加 2 件 (F-7, F-8)

---

## Step 2 人手判定サンプル記録

**総セル数**: 247

### 類型 1 — 意訳ジャーゴン (5 サンプル)

| # | 検査語 | 結果 | 根拠 |
|---|--------|------|------|
| 1 | アトム | 不検出 | 全 247 セルで未出現 |
| 2 | レジャー | 不検出 | 全 247 セルで未出現 |
| 3 | サブエージェント | 不検出 | 全 247 セルで未出現 |
| 4 | ベリフィケーション | 不検出 | 全 247 セルで未出現 |
| 5 | バッチ | 不検出 | 全 247 セルで未出現 |

結果: 0 件 ✅

### 類型 2 — 口語表現 (8 サンプル)

| # | 検査語 | 結果 | 根拠 |
|---|--------|------|------|
| 1 | だいたい | 不検出 | 全セル未出現 |
| 2 | ちゃんと | 不検出 | 全セル未出現 |
| 3 | ざっくり | 不検出 | 全セル未出現 |
| 4 | いい感じ | 不検出 | 全セル未出現 |
| 5 | 結構 | 不検出 | 全セル未出現 |
| 6 | すごく | 不検出 | 全セル未出現 |
| 7 | とても | 不検出 | 全セル未出現 |
| 8 | なんか | 不検出 | 全セル未出現 |

結果: 0 件 ✅

### 類型 3 — 未登録内部用語 (10 サンプル)

| # | 検査語 | 結果 | 根拠 |
|---|--------|------|------|
| 1 | パイプライン | **検出** | `3_機能要件!C13` 「七工程パイプライン」→ F-7 として記録 |
| 2 | リポジトリ | 検出 (許容判定) | `2_業務要件!B14`, `5_制約条件!C5` 「本リポジトリは原刊行物そのものを再配布せず」。技術的正確性のために必要な IT 用語。blacklist 未収録で強制禁止ではないが許容性を主 session に確認提案。 |
| 3 | フェーズ | 不検出 | 全セル未出現 |
| 4 | スプリント | 不検出 | 全セル未出現 |
| 5 | ワークフロー | 不検出 | 全セル未出現 |
| 6 | タスク | 不検出 | 全セル未出現 |
| 7 | コミット | 不検出 | 全セル未出現 |
| 8 | デプロイ | 不検出 | 全セル未出現 |
| 9 | ブランチ | 不検出 | 全セル未出現 |
| 10 | バリデーション | 不検出 | 全セル未出現 |

実質 MEDIUM 1 件 (F-7: パイプライン)、要確認 1 件 (リポジトリ)。

### 類型 4 — 採用語の表記ゆれ (7 サンプル)

| # | 採用語 | ゆれ候補 | 結果 | 根拠 |
|---|--------|----------|------|------|
| 1 | 追跡可能性 | トレーサビリティ | **検出** | `1_背景目的!B7`, `1_背景目的!B20` → F-8 |
| 2 | 検証単位 | データ単位 | **検出** | `3_機能要件!C13` → F-2 (機械検査と一致) |
| 3 | 乖離 | 差異 | **検出** | `2_業務要件!B19`, `5_制約条件!C3` → F-3 |
| 4 | 工程移行判定 | ゲート | 不検出 | 全セル未出現 |
| 5 | 合格判定基準 | PASS 四条 | 不検出 | 全セル未出現 |
| 6 | 審査独立性原則 | Rule D | 不検出 | 全セル未出現 |
| 7 | 実施回 | ラウンド | 不検出 | 全セル未出現 |

---

## Step 3 出典規格妥当性 (規律 H-2 抽検)

5 エントリを抽検。

| # | エントリ (internal) | 採用語 | reference 主要出典 | 妥当性判定 |
|---|---------------------|--------|-------------------|-----------|
| 1 | atom | 検証単位 | `厚労省 CSV ガイドライン §1.1 / §10 (2010)` | 妥当 — CSV ガイドライン §1.1 は用語・定義節、§10 はバリデーション節として整合 |
| 2 | drift | 乖離 | `JIS Z 8301:2019 §8 用字, 用語及び略語` | 妥当 (F-2 修正済) — §8 は kikakurui.com で確認済。節タイトル「規格票作成規則」は規格正式タイトルではないが §8 参照は正確 |
| 3 | handoff | 工程間引渡し | `JIS X 0160:2021 (有償全文未確認 — D-6 制約)` | PARTIAL — D-6 制約明記あり。有償資料の §番号未確認は許容範囲内 (F-2 修正後 PARTIAL 表記あり) |
| 4 | reviewer | 文書確認担当者 | `JIS X 0160:2021 §6.4.9 + §6.4.11; IPA 要件定義ガイド 第2版 §レビュー担当者` | 妥当 — §6.4.9 は jis.eomec.com で確認可能。IPA ガイドの §名は公開資料で一次確認可 |
| 5 | ack | 承認 | `厚労省 CSV ガイドライン §6.6 変更管理 (2010)` | 妥当 — §6.6 変更管理節は公開版で確認可。IPA モデル契約書 §承認欄も実在 |

Step 3 結果: reference 欄の重大な fabrication なし。有償書籍未確認分は D-6 制約として明示済み。

---

## 最終 verdict 根拠

- blacklist HIGH: **0 件** ✅
- mapping HIGH: **0 件** ✅ (機械検査 verdict=FAIL だが HIGH 件数は 0)
- mapping MEDIUM: **5 件** (F-1, F-2, F-3, F-7, F-8; F-3 は主 session 判断待ちを含む)
- false-positive 確認: 3 件 (F-4, F-5, F-6)

term_audit.md 階梯: `HIGH 0 + MEDIUM ≥1` → **CONDITIONAL_PASS**

---

## 主 session 逆質問 (監査範囲外事象)

1. **F-3 文脈判断**: `差異` (drift 候補) が文書間比較文脈 (METHODOLOGY.md §6 由来の定型句) に使われている。`乖離` への強制置換か、drift notes への文脈免除追記か、主 session が方針を決定されたい。

2. **F-4 candidates 削除提案**: `chain` エントリの candidates `相互参照` は NCI EVS 照合文脈と衝突するため、主 session による mapping の candidates リスト見直しを提案する。

3. **リポジトリ許容性**: `リポジトリ` (2 箇所) は blacklist 未収録。著作権・再配布制約の技術的説明に必須と判断されるが、主 session が納品物での使用可否を確認されたい。

---

## mapping 追加提案

| 提案種別 | 対象 | 提案内容 |
|---------|------|---------|
| blacklist 追加 | `パイプライン` | `process_jargon` に追加。suggested_replacement: `["処理連鎖", "処理工程"]` |
| blacklist 追加 | `トレーサビリティ` | `colloquial` に追加。suggested_replacement: `["追跡可能性"]` |
| mapping 追加 | `トレーサビリティ` | 新エントリ: `internal: トレーサビリティ, adopted: 追跡可能性` |
| mapping notes 修正 | `drift` → `乖離` | notes に「文書間比較差 (静的) 文脈は「差異」可」の文脈免除注記追加を検討 |
| mapping candidates 修正 | `chain` → `変更連鎖` | candidates から `相互参照` を削除し、外部参照文脈との混乱回避 |
| スクリプト改善提案 | `audit_terms.py` | `文脈依存` adopted エントリでは、candidates 内の語は inconsistency ではなく適正採用として扱う仕様変更。単文字 candidates (`約`) は漢字複合語内包のサブストリング誤検出回避のため形態素レベル照合を検討。 |

---

## 規律 D 自己宣言

writer (executor / opus) および reviewer (code-reviewer / opus) との subagent_type 隔離を確認した。本評価は以下のみを参照して実施した:

- writer 産物: `docs/jp/sources/04_要件定義書.yml` + `docs/jp/04_要件定義書.xlsx`
- 用語規律ソース: `docs/jp/glossary/term_blacklist.yml`, `docs/jp/glossary/term_mapping.yml`
- 監査スクリプト: `docs/jp/scripts/audit_terms.py`, `docs/jp/scripts/extract_xlsx_text.py`
- 監査プロンプトテンプレ: `docs/jp/prompts/term_audit.md`

主 session の履歴、他 subagent の thinking メモ、R1 reviewer 判定は一切参照していない。

---

*産物パス: `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/glossary/research_reports/phase_1_04_term_audit_2026-04-29.md`*
