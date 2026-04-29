# Research Report — 医療・製薬規格 (Session B)

> Phase 0.5 用語調研フェーズ 産物
> 派発: 2026-04-29 / 主 session → `oh-my-claudecode:document-specialist`
> 担当: 医療・製薬規格 5 件
> アクセス成功: **5/5** (有償規格は公式サマリ・プレビューで代替)

## 概要

厚労省 2 件 (ER/ES 指針 + CSV ガイドライン) は mhlw.go.jp で全文公開. GAMP 5 第 2 版は英語版 2022-07・日本語版 2025-04 発刊, 有償電子書籍のみ. ICH E6(R3) は 2025-01-06 Step 4 採択, **日本語通知未発出** (PMDA 予定中). ICH M11 は 2025-12-15 Step 5 採択, **日本語訳未公開**.

**重要発見**:
- **ICH E6(R3) 公式日本語通知 未発出** — PMDA 通知準備中
- **ICH M11 公式日本語訳 未公開**
- **GAMP 5 は有償電子書籍のみ** — 用語抜粋は公式概要レベル

---

## 1. ER/ES 指針 (厚労省, 2005)

- 正式名: 医薬品等の承認又は許可等に係る申請等における電磁的記録及び電子署名の利用について
- 通知番号: 薬食発第 0401022 号
- 公式 URL: https://www.mhlw.go.jp/web/t_doc?dataId=00ta8216&dataType=1&pageNo=1
- 入手可能性: 公開
- 構成: §2 用語定義 / §3 真正性・見読性・保存性要件
- 抜粋用語 (12):
  - 電磁的記録 / 電磁的記録媒体 / 電子署名 / デジタル署名 / クローズド・システム / オープン・システム / 監査証跡 (Audit Trail) / 真正性 / 見読性 / 保存性 / 識別・認証 / 完全性
- 備考: FDA 21 CFR Part 11 を参考に策定. 2005 年以降改訂なし, 現行有効.

## 2. コンピュータ化システム適正管理ガイドライン (厚労省, 2010)

- 通知番号: 薬食監麻発第 1021011 号
- 公式 URL: https://www.mhlw.go.jp/web/t_doc?dataId=00tb6573&dataType=1&pageNo=1
- Q&A: https://www.mhlw.go.jp/web/t_doc?dataId=00tb6574&dataType=1&pageNo=1
- 入手可能性: 公開
- 適用: 2012-04-01 開始
- 抜粋用語 (15):
  - コンピュータ化システム (§1.1/§10) / コンピュータシステム / システムライフサイクル / ソフトウェアカテゴリ / バリデーション計画書 / 要求仕様書 (URS) / 機能仕様書 (FS) / 設計仕様書 (DS) / 据付時適格性評価 (IQ) / 運転時適格性評価 (OQ) / 性能適格性評価 (PQ) / リスクアセスメント / 供給者アセスメント / 変更の管理 / システム台帳 / 廃棄計画書
- 備考: GMP 省令ベース CSV ガイドライン. FDA 21 CFR Part 11 + EU Annex 11 参照.

## 3. GAMP 5 (Second Edition, 2022) ★ 有償

- 正式名: ISPE GAMP 5: A Risk-Based Approach to Compliant GxP Computerized Systems / 日本語版: GAMPガイド: コンピュータ化システムのGxP適合へのリスクベースアプローチ
- 発行: 英語版 2022-07-29 (404 頁), 日本語版 2025-04 発行 (410 頁)
- 公式 URL (英): https://ispe.org/publications/guidance-documents/gamp-5-guide-2nd-edition
- 日本語版: https://guidance-docs.ispe.org/doi/book/10.1002/9781946964823
- TOC PDF (公開): https://ispe.org/sites/default/files/publications/guidance-documents/2022-TOC/ISPE-GAMP5-Ed2_TOC.pdf
- ISPE 日本本部: https://www.ispe.gr.jp/ISPE/07_public/07_01_19.htm
- 入手可能性: **有償** (会員 $395 / 非会員 $770 日本語版)
- 抜粋用語 (公式概要 + Pharmaceutical Engineering 誌より):
  - リスクベースアプローチ / GxP 適合 / ソフトウェアカテゴリ (1-5) / バリデーションライフサイクル / コンピュータソフトウェアアシュアランス (CSA) / データインテグリティ (ALCOA+) / サービスプロバイダ管理 / 反復的・アジャイル開発 / ブロックチェーン / AI/ML / クリティカルシンキング / オープンソースソフトウェア (OSS)
- 備考: 業界ガイド (法的拘束力なし). 第 1 版 2008 年.

## 4. ICH E6(R3) GCP ★ 公式日本語通知未発出

- 正式名: ICH Guideline for Good Clinical Practice E6(R3)
- 採択: 2025-01-06 Step 4 (Principles + Annex 1). Annex 2 は 2025 後半 Step 3 完了
- 公式 URL (英): https://database.ich.org/sites/default/files/ICH_E6(R3)_Step4_FinalGuideline_2025_0106.pdf
- FDA: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e6r3-good-clinical-practice-gcp
- EMA: https://www.ema.europa.eu/en/ich-e6-good-clinical-practice-scientific-guideline
- PMDA: https://www.pmda.go.jp/int-activities/int-harmony/ich/0028.html
- 日本語訳: **未発出** (PMDA「今後通知として発出予定」)
- 地域実施: EMA 2025-07-23 発効, FDA 2025-09 連邦官報, 日本通知準備中
- 抜粋用語 (英語版より, 仮訳併記):
  - 治験責任医師 (Investigator) / 依頼者 (Sponsor) / 被験者・試験参加者 (Trial Participant; E6(R3) で Subject から変更) / インフォームド・コンセント / 監査証跡 (Audit Trail; 新規定義) / モニタリング (RBM 包含) / 症例報告書 (CRF/eCRF) / 原資料・原記録 / 治験実施計画書 (Protocol) / 治験審査委員会 (IRB/IEC) / 有害事象 / SUSAR (新規) / メタデータ (新規) / 署名 (新規) / 同意 Assent (新規, 小児向け) / サービスプロバイダ (新規, CRO 上位概念) / データインテグリティ
- 備考: 構造変更 — 単一文書 → 原則 + Annex 1 + Annex 2 の 3 部構成. ICH M11 と整合.

## 5. ICH M11 (CeSHarP, Step 5 採択 2025-12-15) ★ 日本語訳未公開

- 正式名: ICH M11 Guideline on Clinical Electronic Structured Harmonised Protocol
- 採択: 2025-12-15 Step 5 (シンガポール ICH Assembly)
- 構成: ガイドライン + テンプレート + テクニカルスペシフィケーション (3 文書セット)
- 公式 URL (EMA): https://www.ema.europa.eu/en/ich-m11-guideline-clinical-study-protocol-template-technical-specifications-scientific-guideline
- ガイドライン PDF: https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/ich-m11-guideline-clinical-electronic-structured-harmonised-protocol-cesharp-step-5_en.pdf
- テンプレート PDF: https://database.ich.org/sites/default/files/ICH_Step4_M11_Final_Template_2025_1119.pdf
- FDA: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m11-technical-specification-clinical-electronic-structured-harmonised-protocol
- PMDA: https://www.pmda.go.jp/int-activities/int-harmony/ich/0095.html
- 日本語訳: **未公開** (Step 5 採択直後, MHLW/PMDA 通知準備中)
- 抜粋用語: CeSHarP / 臨床試験実施計画書 (Protocol) / ハーモナイズド・テンプレート / テクニカルスペシフィケーション / 介入的臨床試験 / 構造化データ交換 / 適格性基準 / エンドポイント / 推定対象 (Estimand; ICH E9(R1) 準拠) / 無作為化スキーマ / マスタープロトコル / 改訂・修正 (Amendment) / 適合性・基数 (Conformance / Cardinality)
- 備考: ICH E6(R3) + ICH E9(R1) (Estimand) + CDISC (CDASH/SDTM) と整合明示.

---

## アクセス制約

| 文書 | 制約 | 代替対応 |
|------|------|---------|
| PMDA ER/ES PDF | バイナリ抽出不可 | mhlw.go.jp HTML で代替 |
| EMA E6(R3) Step 5 PDF | バイナリ | ICH database PDF + 解説サイト |
| ICH M11 template PDF | バイナリ | EMA HTML + FDA + 解説 |
| ISPE 日本語版直販 | HTTP 403 | ispe.gr.jp + 業界ブログ |

## 追記: ICH E6(R3) / M11 日本語訳ギャップ

本プロジェクトの納品先 iTMS 様は 2026-04-29 時点で:
- E6(R3) の公式日本語訳は入手不能
- M11 の公式日本語訳は入手不能

→ term_mapping.yml では **公式日本語訳なし** と明示し, 業界慣用 / 旧版 E6(R2) からの推定継承で当面しのぐ判断要.
