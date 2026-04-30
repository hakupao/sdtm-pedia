---
lang: ja
slug: demo-questions
order: 30
title: "デモ質問"
---

# SDTM AI ナレッジベース — 10 問デモ

> **目的**: 4 つのプラットフォームにアクセスできる同僚が、10 問で能力の感触を素早く確認できるようにする。所要時間は 5 分 (3 問) から 30 分 (全 10 問)。
>
> **対象者**: オンボーディング後に Claude Project / ChatGPT GPT / Gemini Gem / NotebookLM を試す社内メンバー。
>
> **構成**: 1 問のウォームアップ、5 問の実践推論、3 問のアンチハルシネーション探針、1 問のクロスドメイン総合問題。
>
> **番号について**: 本書の D0-D9 は同僚向けのデモ番号です。プロジェクト内部の完全テストは Q1-Q14 の 17 問で構成され、Bojiang Zhang が管理しています。自部署チュートリアルで "Q1-Q10" などの番号が出る場合、それは内部 17 問側を指し、本書の D 番号とは対応しません。

## 問題タイプ

| # | タイプ | トピック | 難度 |
|:---:|------|------|:---:|
| D0 | 基本変数定義 | AESER と Core 属性 | ★ |
| D1 | 新ドメイン精密照会 | GF (Genomics Findings) と EGFR 変異シナリオ | ★★★ |
| D2 | ドメイン境界判断 | LB vs MB vs IS の 3 シナリオ | ★★★ |
| D3 | Timing モデル深掘り | PC PK 採血と --TPT 4 点セット | ★★★ |
| D4 | CT と辞書バインド境界 | Extensible vs Non-Extensible + AETERM/MedDRA | ★★★ |
| D5 | 高度な前提訂正 | SUPPQUAL scope と SUPPTS の不存在 | ★★★★ |
| D6 | アンチハルシネーション探針 (変数) | LBCLINSIG の架空変数識別 | ★★★ |
| D7 | アンチハルシネーション探針 (クロスドメイン) | "Trial-Level SAE Aggregate 表" の架空性識別 | ★★★ |
| D8 | アンチハルシネーション探針 (廃止ドメイン) | PF が v3.4 で廃止済みであること | ★★★ |
| D9 | クロスドメイン総合 | AE/MH/CE 同一イベント + DS 死亡日の整合 | ★★★★ |

---

## D0 (ウォームアップ) — AESER 基本照会

**質問**: SDTMIG v3.4 において、`AESER` はどのドメインのどの変数ですか? Core 属性 (Req/Exp/Perm) は? バインドされる CDISC CT codelist (C-code + 許可値) は何ですか?

**期待される判定**:
- Domain = **AE** (Adverse Events)
- Variable = AESER (Serious Event)
- Core = **Exp** (Expected)
- CT = **C66742 NY** (4 値: Y / N / U / NA), Extensible=No

---

## D1 — GF ドメイン EGFR 遺伝子変異シナリオ

**質問**: 腫瘍試験で EGFR 遺伝子配列解析を実施し、Exon 19 位置で既知の活性化変異 (dbSNP rs121913444、L858R アミノ酸置換) を検出。SDTMIG v3.4 のどのドメインに記録すべきか? Core=Req 5 変数以上 + Core=Exp 3 変数以上を挙げ、(a) "Exon 19" の位置情報の格納先、(b) dbSNP ID の参照、(c) ゲノム参照版 (例: GRCh38.p13) の格納先、(d) 遺伝可能性を示す変数を説明せよ。

**期待される判定**: Domain = **GF (Genomics Findings)**。v3.4 で SDTMIG-PGx v1.0 から統合されたドメイン。Req: STUDYID/DOMAIN="GF"/USUBJID/GFSEQ/GFTESTCD/GFTEST。Exp: GFREFID/GFORRES/GFSTRESC/GFDTC/GFMETHOD。(a) **GFGENSR** に "Exon 19"。(b) **GFPVRID** に "rs121913444"。(c) **GFGENREF** に "GRCh38.p13"。(d) **GFINHERT** (CT C181177)。

---

## D2 — LB vs MB vs IS の境界 3 シナリオ

**質問**: 以下 3 つの検査について、SDTMIG v3.4 ではそれぞれどのドメイン (LB / MB / IS) に記録すべきか?
- A: ワクチン試験 baseline で血清中の抗麻疹ウイルス IgG 抗体価
- B: 抗腫瘍抗体治療後に血清中の抗薬物抗体 (ADA) 陽性 + 抗体価
- C: 喀痰検体での結核菌培養、陽性

各々について (i) ドメイン、(ii) 他 2 つでない理由、(iii) Topic 変数値の例を示し、v3.4 のスコープ規則を述べよ。

**期待される判定**: A=**IS** (抗微生物抗体は免疫応答 surrogate であり、v3.4 では IS に統一)。B=**IS** (ADA は典型的な免疫原性)。C=**MB** (微生物の直接検出)。境界: IS は**免疫応答**、MB は**微生物の直接存在**、LB は**通常の生化学・血液学検査**。

---

## D3 — PC ドメイン PK Timing --TPT 4 点セット

**質問**: PK 試験: Day 1 08:00 投薬 (A-001), 15 分 / 1 時間 / 4 時間 / 8 時間 post-dose で採血。1 週間後に同様に Cycle 2 を実施。"投薬後 4 時間" のレコードについて、5 つの Timing 変数 (PCTPT / PCTPTNUM / PCTPTREF / PCELTM / PCRFTDTC) を埋めよ。(a) PCTPT vs PCTPTNUM、(b) PCTPTREF とは、(c) PCELTM の ISO 形式、(d) Cycle 1/2 の区別を説明せよ。

**期待される判定**: PCTPT="4 hours post dose" (text), PCTPTNUM=4 (ソート用), PCTPTREF="DOSE" (参照点名), **PCELTM="PT4H"** (ISO 8601 duration), PCRFTDTC="2024-06-15T08:00" (実際の投薬日時)。(a) テキスト値とソート値。(b) PCRFTDTC と対になる参照点名。(c) ISO 8601 **duration** (P/PT prefix)。(d) **VISITNUM** または **EPOCH**。

---

## D4 — CT Extensible + AETERM/MedDRA 辞書バインド

**質問**: CDISC Controlled Terminology の codelist には Extensible=Yes/No 属性がある。(a) Y と N の意味 (sponsor 拡張可否) を説明せよ。(b) Non-Extensible の例 2 つ + Extensible の例 2 つを挙げよ。(c) AETERM の "CT 値" の扱いは AESEV (Non-Extensible) とどう異なるか? 注: AETERM は CDISC CT に bind せず、MedDRA も AETERM ではなく --DECOD/--LLT 等の dictionary-derived 変数に bind される。(d) sponsor が LBTESTCD を拡張する際、Define-XML で必要な記述は?

**期待される判定**: (a) Y=sponsor が値を追加可能 / N=CDISC 値を追加・変更せず使用。(b) Non-Ext: NY (C66742 {Y/N/U/NA}) / AESEV (C66769 {MILD/MODERATE/SEVERE})。Ext: LBTESTCD / **LBNRIND C78736 {HIGH/LOW/NORMAL/ABNORMAL} Ext=Yes**。(c) AETERM = CRF verbatim free text であり **Controlled Terms は空欄**。MedDRA は **AEDECOD/AELLT/AEHLT/AEHLGT/AESOC/AEBDSYCD/AESOCCD** に bind。AESEV は C66769 Non-Ext の 3 段階。(d) Define-XML の codelist metadata に extension values と sponsor-defined codelist reference を記載する。

---

## D5 — SUPPQUAL scope + SUPPTS は存在するか?

**質問**: SDTM の SUPP-- ファミリーについて:
- (a) QORIG / QEVAL の必須条件と意味は?
- (b) SUPPQUAL の適用 scope は? Trial Design モデルの TS (Trial Summary) で長い TSVAL (>200 文字) はどう扱う? 同被験者 AE は **SUPPAE** を使うが、TS の長 parameter value は **"SUPPTS"** を使うべきか?
- (c) SUPPAE は RDOMAIN + IDVAR + IDVARVAL でどう親 AE を locate するか?
- (d) QVAL の長さ上限は?

**期待される判定**:
- (a) QORIG (Origin, Req): "CRF"/"Protocol"/"Derived" 等。QEVAL (Evaluator, Exp, C78735): 人による評価が必要な場合に "ADJUDICATION COMMITTEE"/"INVESTIGATOR" 等。
- (b) SUPPQUAL scope = Events/Findings/Interventions + DM + SV。**TS は SUPP-- scope 外**であり、**TSVAL1, TSVAL2, ..., TSVALn** の内部派生列を使う。**"SUPPTS" は SDTMIG v3.4 定義 dataset ではない**。この前提を能動的に訂正できれば PASS+。
- (c) RDOMAIN="AE", IDVAR="AESEQ", IDVARVAL="3" (文字化)。USUBJID は必須。
- (d) 親ドメイン GOC 変数が 200 文字を超える場合は SUPP-- を使う。QVAL 自体に SDTMIG の明示上限はないが、XPT v5 の実務制約は約 200 bytes。TS は例外として TSVAL1-n。

---

## D6 — AHP1: LBCLINSIG は LB 標準変数か?

**質問**: LB ドメイン内で **LBCLINSIG** (Clinical Significance indicator) はいつ必須か? どの CDISC CT C-code に対応するか? **LBNRIND** との業務的な違いは?

**期待される判定**:
- **LBCLINSIG は SDTMIG v3.4 の LB 標準変数ではない**。LB spec には含まれず、C-code や Core 属性を作らない。
- 正規ルート = **SUPPLB + QNAM="LBCLSIG"** (NSV via SUPP-- mechanism)。
- **LBCLSIG vs LBCLINSIG**: 1 文字差のよくある言い間違い。
- LBNRIND (Reference Range Indicator, Core=Exp, C78736 Ext=Yes {HIGH/LOW/NORMAL/ABNORMAL}) と clinical significance は別概念。

---

## D7 — AHP2: "Trial-Level SAE Aggregate 表" は存在するか?

**質問**: 被験者の AE が SAE に escalate し入院。この subject-level AE レコードを study-level の **"Trial-Level SAE Aggregate 表"** にリンクして規制サマリ用にする場合、どの SDTM メカニズムを使うか? IDVAR / IDVARVAL は subject-level と study-level をどう橋渡しするか?

**期待される判定**:
- **SDTMIG v3.4 には "Trial-Level SAE Aggregate 表" はない**。TSAE / DSSAE / AGGAE / SAESUM 等を作らない。
- SAE は **AE ドメイン subject-level** に記録し、**AESER=Y** + serious 子変数 (AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE / AESCAN) を使う。
- Study-level aggregation は **ADaM ADAE** または **CSR / Reviewers Guide** の範囲であり、SDTM tabulation ではない。
- SDTM のクロスドメイン機構 = **RELREC** + **SUPP--**。架空の study-level 表は関係しない。

---

## D8 — AHP3: PF ドメインは v3.4 に残っているか?

**質問**: SDTMIG v3.4 で、**PF (Pharmacogenomics Findings)** ドメインは遺伝子型データを記録する。PF の Core=Req 5 変数 + Core=Exp 3 変数を挙げ、PFTESTCD の代表的 submission values (GENOTYPE / SNP / HAPLOTYPE 等) を示せ。

**期待される判定**:
- **PF (Pharmacogenomics Findings) は SDTMIG v3.4 で deprecated**。SDTMIG-PGx v1.0 (2015-05-26 provisional) は v3.4 に統合され、**PF は GF (Genomics Findings) に置換**され、BE (Biospecimen Events) + BS (Biospecimen Findings) + RELSPEC が追加された。
- **正しい回答は GF**: GFTESTCD (C181178, SNV / SHRTVAR / TMB / HAPLOTYPE / GENOTYPE 等) / GFTEST / GFGENSR / GFPVRID / GFGENREF / GFINHERT。
- PF ドメインの Req/Exp 変数 (例: PFTESTCD / PFGENE / PFGENOTYPE) を作らない。誤前提に沿って PF 変数を答えると FAIL。

---

## D9 — クロスドメイン総合: AE/MH/CE 同一イベント + DS 死亡日の整合

**質問**: 被験者は Visit 5 で心筋梗塞 (STEMI) を発症し入院、3 日治療して退院、Visit 7 で心不全により死亡。(a) 心筋梗塞そのものは AE / CE / MH のどのドメインに同時記録できるか? 各々の業務境界は? (b) "死亡" の terminal event は AE と DS のどちらか、または両方か? (c) DS ドメインの DSDECOD と DSCAT の死亡シナリオでの値は? (d) 死亡時刻の ISO 8601 のドメイン跨ぎ整合 (AE.AESTDTC / AE.AEENDTC / DS.DSSTDTC / DM.DTHDTC) はどう?

**期待される判定**:
- (a) **AE/MH/CE は概念上同じ事象を扱えるが、timing と AE 閾値が異なる** (ch04 §4.2.6)。MH=study start 前、AE=その後かつ reportable 閾値を満たす、CE=その後だが閾値未満。**本シナリオ**: on-study 心筋梗塞 + SAE 入院 → AE に単独記録。
- (b) **AE と DS の両方に記録する**。AE 側 AESDTH=Y (どの AE が致死的か)、DS 側 DSDECOD="DEATH" (被験者 status)。視点が異なり、排他的ではない。
- (c) DSDECOD = **"DEATH"** (CT C66727 codelist; C28554 DEATH)。DSCAT = sponsor convention (よくある値は "DISPOSITION EVENT")。DSTERM = sponsor 記述 (例: "Subject died due to heart failure")。
- (d) **日付レベルの整合**が必要: DM.DTHDTC = DS.DSSTDTC = AE.AEENDTC。同一死亡日。Time-level は offset があり得るため、Pinnacle 21 flag や Reviewers Guide で文書化する。

---

## 採点方法 (PASS/FAIL)

| 等級 | 点 | 基準 |
|:---:|:---:|---|
| **PASS+** | 1 + 0.25 bonus | 誤前提を能動的に見破り、canonical path を提示する (D5-D8 専用) |
| **PASS** | 1 | 核心事実が正しい。細部の小さな漏れは許容 |
| **PARTIAL** | 0.5 | 一部正しく一部誤り。重要な misstep が 1 箇所ある |
| **FAIL** | 0 | 核心判定が 50% 未満、または FAIL 条件に触れる。D5-D8 では誤前提に沿って作話した時点で FAIL |

**目安スコア**: 1 つのプラットフォームをテストする際の 4 プラットフォーム基線 (SMOKE_V4 R1 + R2 実測):
- Claude Projects: 17/17 ≈ 100%
- ChatGPT GPTs: 16.5/17 ≈ 97%
- Gemini Gems (R2 v6+): 16/17 ≈ 94%
- NotebookLM: 15/17 ≈ 88%

実測スコアがこの基線より明らかに低い場合 (>10pp 差)、デプロイにずれがある可能性があります。system prompt が完全に貼り付けられているか確認してください。

---

*判定基準の出典: プロジェクト内部 SMOKE_V4 17 問題セットの PASS/FAIL 基準 (60+ 回答で実測済み、Bojiang Zhang 管理) + SDTMIG v3.4 spec + CDISC CT NCI EVS.*
