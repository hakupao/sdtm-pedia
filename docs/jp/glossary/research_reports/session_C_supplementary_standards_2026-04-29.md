# Research Report — 補助規格 (Session C)

> Phase 0.5 用語調研フェーズ 産物
> 派発: 2026-04-29 / 主 session → `oh-my-claudecode:document-specialist`
> 担当: 補助規格 4 件 (CDISC CJUG / JIS T 14971 / JIS Z 8301 / 公用文)
> アクセス成功: **4/4** (但 JIS 有償規格本文は商用購入要; CJUG 日本語訳も CDISC ログイン必須)

## 概要

CJUG は SDTMIG v3.2 / SDTM v1.4 の公式日本語訳を発行済み (cdisc.org ログイン必須). 業界慣用語 (ドメイン / 変数 / 被験者 / 来院 等) は複数の官民文書で確認可. JIS T 14971:2020 は ISO 14971:2019 IDT 訳, 主要リスク用語完備. JIS Z 8301:2019 は規格票作成ルール体系化, 文書形式語が揃う. 公用文作成の考え方 (2022 文化審議会建議) は文体 / 句読点 / 外来語の基準として公開 PDF.

**重要発見**:
- **CJUG SDTMIG 日本語訳は v3.2 まで** (本プロジェクト KB は v3.4 → ギャップ)
- **CDISC ログイン必須** で実訳語ファイル取得は別工程必要

---

## 1. CDISC 公式日本語訳 (CJUG) ★ 本プロジェクト核心

- 翻訳協力: 国立病院機構 名古屋医療センター / CJUG SDTM チーム / TRI
- 公式 URL: https://www.cdisc.org/translations/japanese
- CJUG: https://www.cdisc.org/user-network/asia/cdisc-japan-user-group-cjug
- CJUG Wiki: https://wiki.cdisc.org/display/J3C/What+CJUG
- SDTMIG v3.2: https://www.cdisc.org/standards/foundational/sdtmig/sdtmig-v3-2 (ログイン必須)
- 入手可能性: **限定** (CDISC 無償アカウント登録後ダウンロード)
- 連絡: CJUG-SDTM-OFFICE@umin.ac.jp / CJUG-OFFICE@umin.ac.jp

### 抜粋用語 (業界慣用 + CDASH 公式日本語版で確認)

| 用語 | 出典 |
|------|------|
| ドメイン (Domain) | 業界慣用 (JPMA / Certara JP 複数文書) |
| 変数 (Variable) | 業界慣用 (JPMA 2021) |
| 被験者 (Subject) | 業界慣用 |
| 来院 (Visit) | 業界慣用 |
| 観察クラス (Observation Class) | 業界慣用 |
| 介入 (Interventions) | CDASH v1.0 日本語版 §2 |
| 事象 (Events) | CDASH v1.0 日本語版 §2 |
| 所見 (Findings) | CDASH v1.0 日本語版 §2 |
| レコード (Record) | 業界慣用 |
| データセット (Dataset) | 業界慣用 |

### ★ 重要なギャップ

- 本プロジェクト KB は **SDTMIG v3.4** ベース
- CJUG 公式日本語訳は **v3.2 まで**
- → v3.3/v3.4 で追加された用語は **公式日本語訳が存在しない**
- term_mapping.yml では「v3.2 訳を一次拠所 + v3.3/v3.4 差分は英語原文 + 仮訳」と明示要

### 推奨次アクション (term_mapping.yml 起草前)

1. cdisc.org に無償アカウント作成
2. translations ページから SDTMIG v3.2 日本語版 PDF 取得
3. PDF 用語集 / 略語集セクションから訳語抽出
4. JPMA / PMDA 文書と照合

## 2. JIS T 14971:2020 — 医療機器リスクマネジメント (参考程度)

- 公式 URL: https://webdesk.jsa.or.jp/books/W11M0090/index/?bunsyo_id=JIS+T+14971:2020
- パブコメ草案 (e-Gov): https://public-comment.e-gov.go.jp/pcm/download?seqNo=0000202022
- kikakurui.com: https://kikakurui.com/t1/T14971-2020-01.html
- 入手可能性: **有償** (¥4,730 税込, 42 頁; パブコメ版で抜粋確認可能)
- 対応国際規格: ISO 14971:2019 IDT
- 抜粋用語 (10):

| 用語 | § |
|------|---|
| 危害 (Harm) | §3.3 |
| ハザード (Hazard) | §3.4 |
| リスク (Risk) | §3.18 |
| 重大さ (Severity) | §3.27 |
| リスクマネジメント | §3.24 |
| リスク分析 | §3.19 |
| リスク評価 | §3.23 |
| リスクコントロール | §3.21 |
| 残留リスク | §3.17 |
| ベネフィット | §3.2 |

- 備考: SDTM は医療機器ではなく製薬データ標準のため **参考程度**. 関連ガイダンス TR T 24971:2020 もあり.

## 3. JIS Z 8301:2019 — 規格票の様式及び作成方法

- 公式 URL: https://webdesk.jsa.or.jp/books/W11M0090/index/?bunsyo_id=JIS+Z+8301:2019
- 概要解説 (無償): https://www.jsa.or.jp/datas/media/10000/md_7624.pdf
- 原案作成手引: https://webdesk.jsa.or.jp/pdf/dev/md_5652.pdf
- kikakurui.com: https://kikakurui.com/z8/Z8301-2019-01.html
- 入手可能性: **有償** (¥7,590 税込, 150 頁)
- 抜粋用語:

| 用語 | § |
|------|---|
| 箇条 (Clause) | §3, §6.1 |
| 細分箇条 (Subclause) | §6.1 |
| 見出し | §6.4 |
| 表 (Table) | §28 |
| 図 (Figure) | §29 |
| 用語及び定義 | §16 (2019 年版で必須化) |
| 優先用語 / 代替用語 / 推奨しない用語 | §16.5.4 |
| 追補 (Amendment) | §37, 附属書 I |
| 版 (Edition) | §3, 附属書 J |
| 附属書 (Annex) | §20 |

- 重要: 「章」は JIS Z 8301 では正式語ではない — **「箇条 (Clause)」が正式**. 日常語との混同注意.
- 「節」も同様 — **「細分箇条 (Subclause)」が正式**.
- 本プロジェクト .xlsx 文書を JIS 規格票として作成する場合に準拠推奨.

## 4. 公用文作成の考え方 (文化庁, 2022 建議)

- 公式 URL: https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/hokoku/93650001_01.html
- 解説 PDF (索引付): https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/hokoku/pdf/93651301_01.pdf
- プレスリリース: https://www.bunka.go.jp/koho_hodo_oshirase/hodohappyo/93650001.html
- 国語施策ポータル: https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/94336802.html
- 入手可能性: 公開
- 発行: 2022-01-07 建議, 2022-03-08 解説 PDF 改訂
- 抜粋用語:

| 用語 | 内容 |
|------|------|
| 公用文の分類 | 告示・通知 / 記録・公開資料 / 解説・広報 の 3 類型 |
| 横書きの読点 | 「、(テン)」を原則 (従来「，(コンマ)」を見直し) |
| 縦書きの句読点 | 「。」「、」を使用 |
| ですます体 (敬体) | 広報・解説では積極的に許容 |
| である体 (常体) | 法令・告示・通知の基本文体 |
| 専門用語の扱い | 言い換え・注記を加える |
| 外来語 (カタカナ語) | 日本語語感 vs 原語近似の 2 アプローチ |
| 漢字の使い方 | 常用漢字表に基づく |
| 送り仮名 | 「送り仮名の付け方」(内閣訓令) 準拠 |
| 用語の統一 | 同一文書内同一概念は同一表記 |

- 備考: 法的拘束力なし (建議・通知). 71 年ぶり全面改訂 (前身: 1951 年「公用文作成の要領」).
- **長音符問題**: 建議は長音符 (「ー」) 維持の立場 (例:「コンピューター」). JIS Z 8301 (ISO 訳語準拠で長音符なし) と不一致のケースあり, term_mapping.yml で採用基準明示要.
- **WebFetch 制約**: PDF 直接抽出不可. プレスリリース + 解説サイト経由で確認.

---

## 追記: CJUG 日本語訳の取得手続 (term_mapping.yml 起草前必須)

cdisc.org translations ページからの実訳語ファイル取得は本 research subagent では不可 (ログイン必須). Bojiang 側で:

1. cdisc.org 無償アカウント作成 (氏名 / メール / 所属で登録可能と推定)
2. translations ページで SDTMIG v3.2 日本語版 + SDTM v1.4 日本語版 + ADaMIG v1.0 日本語版 を取得
3. PDF を `docs/jp/glossary/research_reports/cjug_extracts/` に配置 (権利関係注意, 個人参照範囲のみ)
4. 用語集 / 略語集セクションをスクリーン抜粋して term_mapping.yml の `reference` 欄に明示

→ I-7 (日方 reviewer) と同様, 用户アクションが必要なオフライン依頼項目.
