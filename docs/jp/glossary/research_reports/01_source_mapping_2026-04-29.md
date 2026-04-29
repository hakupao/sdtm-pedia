# 01 基本設計書 引用源マッピング

> 作成日: 2026-04-29
> 用途: writer subagent への入力資料. 各シート content をどの源節 / 行 / 頁から起こすかの一次設計.
> 参照先: `docs/jp/sources/01_基本設計書.yml` (本マッピングを充填する yml 骨格)
> 上位文書: `docs/jp/04_要件定義書.xlsx` (本書は 04 §3 機能要件 + §4 非機能要件 + §5 制約条件 を実現する設計を提示する位置付け)

---

## 0. 引用源 一覧 (実在性検証済 2026-04-29)

| ID | パス | 用途 |
|----|------|------|
| S-1 | `METHODOLOGY.md` | シート 1 (システム目的) / シート 4 (CDISC 一次資料) |
| S-2 | `docs/DESIGN_RAG_KG.md` | シート 2 §2.5 / シート 3 §3.5 §3.6 / シート 4 §4.4 / シート 5 (Out of Scope) — Phase 7 設計仕様 |
| S-3 | `.work/06_deep_verification/schema/atom_schema.json` | シート 3 §3.3 — 検証 atom データモデル (frozen v1.2) |
| S-4 | `.work/06_deep_verification/schema/ledger_schema.json` | シート 3 §3.4 — 検証 ledger データモデル (frozen v1.2) |
| S-5 | `.work/00_planning/restructure_plan.md` | シート 2 §2.2 — 知識ベース 構造方針 |
| S-6 | `.work/00_planning/source_relationship.md` | シート 4 §4.1 — CDISC 4 種公式刊行物関係 |
| S-7 | `docs/jp/04_要件定義書.xlsx` | 全シート — 上位根拠章 (機能要件 / 非機能要件 / 制約条件 を引用) |
| S-8 | `docs/jp/sources/04_要件定義書.yml` | 04 yml content の節番号特定用 (writer 補助) |
| S-9 | `knowledge_base/INDEX.md` | シート 2 §2.2 — 知識ベース 索引文書 |
| S-10 | `knowledge_base/ROUTING.md` | シート 2 §2.2 + シート 4 §4.4 — 経路層文書 |
| S-11 | `ai_platforms/release/v1.0/` | シート 2 §2.4 + シート 4 §4.3 — 4 平台展開最終版 (Phase 6.5 完了) |
| S-12 | `docs/jp/PLAN.md` | シート 5 — 本納品物自身の制約 (規律 H 系) |
| S-13 | `ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md` | シート 5 — 既知の限界 |
| S-14 | `DISCLAIMER.md` | シート 5 — 著作権 |

writer は派発時に各 S-X を `test -f` (ディレクトリは `test -d`) で実在確認すること.

---

## 1. シート別 引用源対応

### シート 1 (1_概要)

| 小節 | 源 | 抜粋ヒント | 文体目標 |
|------|-----|-----------|---------|
| 1.1 本書の目的 | S-7 §1.5 + S-1 Purpose | 「本書は 04 要件定義書が定めた機能要件 (FR-01〜FR-11) および非機能要件 (NFR-01〜NFR-06) を実現する基本設計を提示する」 | 1-2 文. 04 との上下関係を明示 |
| 1.2 設計対象システムの範囲 | S-1 §2 (7 工程) + S-11 + S-2 §1 | 設計対象は知識ベース本体 + 検証パイプライン + AI 平台展開 + Phase 7 RAG+KG 計画の 4 サブシステム. 前 3 つは現行運用中, Phase 7 は設計済 / 未実装. | 「設計済 / 実装済 / 運用中」の状態区分を明記 |
| 1.3 想定読者 | S-7 §1.3 引用 | 「IT + 医療データ両分野の知見ある実務担当者」 | 04 と同一表現で統一 |
| 1.4 関連文書 | S-7 §1.4 + 本納品物 7 文書 + 99 用語集 | 04 (上位根拠) / 02 (運用) / 03 (試験) / 05 (詳細設計) / 06 (追跡可能性) との接続を箇条書き | 各 1 行で接続関係を述べる |
| 1.5 設計方針 (中核理念) | S-1 §3 + §5 + S-2 §1.4 | 「字面追跡可能性」+「リスク主導検証」+「ローカル先行 / プロバイダー非依存」+「読取専用源 + 派生著作物」 | 本書全体を貫く 4 設計理念を 1 文ずつ |

### シート 2 (2_全体構成)

| 小節 | 源 | 抜粋ヒント | 文体目標 |
|------|-----|-----------|---------|
| 2.1 システム全体像 | S-1 §2 全体 + S-2 §2 + S-11 + S-9 | 4 サブシステム (知識ベース本体 / 検証パイプライン / AI 平台展開 / Phase 7 RAG+KG) の関係を構造図的に文章で記述. 表形式または箇条書き | 状態 (運用中 / 設計済) を各サブシステムに付記 |
| 2.2 知識ベース本体 | S-9 + S-5 §四 + S-1 §3 | 構成 = 63 ドメイン (`knowledge_base/domains/`) + 6 章 (`chapters/`) + 6 モデル (`model/`) + 受控用語 3 階層 (`terminology/`) + 索引 2 件 (INDEX.md / VARIABLE_INDEX.md). ROUTING.md は経路層文書 | 数値はそのまま (63 / 6 / 6 / 受控用語 1,005 codelist 37,939 用語 — S-7 §2.2 から) |
| 2.3 検証パイプライン (06 Deep Verification) | S-3 + S-4 + S-7 §3 FR-11 | 字面級確認の独立工程. atom 抽出 (PDF 9 種 + MD 9 種) → ledger 突合 (forward 9 verdict + reverse 5 verdict) → reviewer 二次審査 (規律 D). 本書執筆時点で 97% 範囲完了, 進行中. | 工程図的に 3 段階を文章化. 数値 (97% / 9 enum / 5 enum) は schema から正確に転記 |
| 2.4 AI 平台展開 (Phase 6.5) | S-11 (release v1.0) | 4 平台 (ChatGPT GPTs / Gemini Gems / NotebookLM / Claude Projects) 完成版. 各平台向けに容量制約 + 機能制約に整合させた配布物として再パッケージ済. tag `v1.0-company-release` 付与済. | 完成日 + 平台別の主用途を 1 文で |
| 2.5 Phase 7 RAG+KG (設計済 / 未実装) | S-2 §2 + §7 | 二段階ロードマップ. Phase 1 = RAG + データセット検証 (Chroma + LiteLLM + Streamlit). Phase 2 = KG + 混合経路 (Neo4j + Cypher). 現状 = 設計確定, 実装未着手. | 「設計済 / 未実装」を明示. 本書での扱いは設計書面のみで, 実装到達は別工程と注記 |
| 2.6 サブシステム間の関係 | S-1 §3 + S-2 §1.4 | 知識ベース本体 = 共通読取源. 検証パイプラインは知識ベースを入力, 検証結果を `.work/06_deep_verification/` 配下に保管. AI 平台展開は知識ベースを再パッケージしたもの. Phase 7 RAG+KG は知識ベースを入力源とする予定 | 1 図相当の文章. 入力 / 出力関係を主語明示 |

### シート 3 (3_データモデル)

| 小節 | 源 | 抜粋ヒント | 文体目標 |
|------|-----|-----------|---------|
| 3.1 知識ベース三件パターン (ドメイン) | S-1 §3 第 1 段落 + S-7 §3 FR-08 | 各ドメイン (例: `knowledge_base/domains/AE/`) に **spec.md / assumptions.md / examples.md** の 3 件構成. spec = 変数仕様 / Core 区分, assumptions = 業務上の前提, examples = 実装例 | 1 ドメイン = 3 件の固定パターンを述べる |
| 3.2 章節文書および モデル文書 | S-9 + S-1 §2 Phase 4 | `chapters/` = 6 章 (`ch01_introduction.md` 〜 `ch10_appendices.md`). `model/` = 6 文書 (観察クラス / 概念). 章節文書は頁範囲を頭付付与で SDTMIG 目次と直接対応. | ファイル名のうち代表 1-2 件を例示 (実数値) |
| 3.3 受控用語データ構造 | S-1 §3 第 3 段落 + S-7 §3 FR-10 | `knowledge_base/terminology/` 配下にコードリスト文書群. 各文書に CDISC 割当の C 符号 (例: C66731) を保持し NCI EVS Browser と相互参照可能. | 「コードリスト」「C 符号」「NCI EVS Browser」を初出時に正式定義 |
| 3.4 検証 atom データモデル | S-3 全体 | atom_schema v1.2 (frozen 2026-04-24). PDF 原子 + MD 原子 共存型 (oneOf), 9 値硬列挙型 atom_type (HEADING / SENTENCE / LIST_ITEM / TABLE_HEADER / TABLE_ROW / CODE_LITERAL / CROSS_REF / FIGURE / NOTE). PDF 原子 ID 形式 `<source>_p<NNN>_a<NNN>` (例 ig34_p0425_a012). MD 原子 ID 形式 `md_<file_stem>_a<NNN>`. | schema 仕様の代表値 (9 値 / id pattern / oneOf 構造) を正確に転記. 実装上の重要規則 (CODE_LITERAL の dataset 文件名硬規則 等) を 1 文程度補足 |
| 3.5 検証 ledger データモデル | S-4 全体 | ledger_schema v1.2 (frozen 2026-04-24). 1 行 JSONL = 1 突合決定. forward (PDF→MD) verdict 9 値 + reverse (MD→PDF) verdict 5 値. 必須フィールド = verdict / similarity_score (0.0-1.0) / matched_by. 規律 D の reviewer 独立審査記録 audited_by を任意配列で蓄積. | forward 9 値 + reverse 5 値の代表値を列挙. 数値 gate (PARTIAL ≥ 0.50 / SOURCED ≥ 0.50) も明記 |
| 3.6 RAG チャンク メタデータ (Phase 7 設計) | S-2 §3.2 | Phase 7 RAG ベクトル検索向けに各チャンクへ構造化メタデータ (source / domain / class / file_type / section / chunk_index) を付与. ドメイン絞込検索 + 意味類似度の 2 段検索を可能とする設計. 現状未実装. | 「設計済 / 未実装」明示. 列挙 6 項目 |
| 3.7 知識グラフ ノード / リレーション (Phase 7 設計) | S-2 §5.2 | Phase 7 第 2 段ロードマップ. ノード 6 種 (Domain / Variable / Codelist / Term / Class / Chapter). リレーション 7 種 (HAS_VARIABLE / BELONGS_TO / USES_CT / CONTAINS_TERM / RELATED_TO / DESCRIBED_IN / SHARED_VARIABLE). データソース = `meta.yaml` (P3 構造化メタデータ, 未実装). | 数値 (6 / 7) と代表値を転記. 「未実装」明示 |

### シート 4 (4_外部IF)

| 小節 | 源 | 抜粋ヒント | 文体目標 |
|------|-----|-----------|---------|
| 4.1 CDISC 一次資料 | S-1 §1 Table + S-6 §一 | 4 種公式刊行物 (SDTMIG v3.4 PDF / SDTM Model v2.0 PDF / SDTMIG xlsx v3.4 / Controlled Terminology xlsx 2024 年版). 入手は CDISC Library 経由. 本知識ベースはこれら一次資料の派生著作物として位置付ける. | 04 §2.2 + §6 P-01 と整合. 数値 (461 頁 / 74 頁 / 1,917 変数 / 1,005 codelist / 37,939 用語) 転記 |
| 4.2 NCI EVS Browser | S-1 §3 第 3 段落 | 米国国立がん研究所 提供の C 符号照合インタフェース. 受控用語の C 符号 (例 C66731) を入力に外部 web 検索が可能. 本知識ベースは C 符号を保持することで本 IF への接続を可能とする. | 公式名 (NCI EVS Browser) を初出 |
| 4.3 AI 平台 (Phase 6.5 完了) | S-11 + 04 §3 FR-07 | 4 平台 = ChatGPT GPTs / Google Gemini Gems / Google NotebookLM / Anthropic Claude Projects. 本知識ベースは各平台向けに容量制約 + 機能制約に整合させた配布物として再パッケージ済. リリース版 v1.0. | 各平台 1 文ずつ用途差別化 |
| 4.4 LLM プロバイダー (Phase 7 設計) | S-2 §3.6 + §5.5 | LiteLLM 抽象層により Claude / GPT / DeepSeek 他 多供給者を非依存に呼出. ベクトル化は OpenAI text-embedding-3-small 等. ベクトル DB は Chroma (ローカル). KG は Neo4j (ローカル). 全て Docker Compose ベースのローカル実行を前提. 現状未実装. | 「設計済 / 未実装」明示 |
| 4.5 本納品物生成基盤 | S-12 §3.1 + 既知 docs/jp/scripts/ | 本納品物 (.xlsx 7 文書 + 用語集) の生成基盤として openpyxl 3.1.5 (Python) + 内製 build_xlsx.py / audit_terms.py を使用. テンプレート (style_guide.xlsx + cover_template.xlsx) で表紙 / 改訂履歴 / 承認欄を統一. | 「本納品物」自身の生成 IF の意味で 1 段落. 詳細は 05 詳細設計書に委譲する旨注記 |

### シート 5 (5_制約事項)

| 小節 | 源 | 抜粋ヒント | 文体目標 |
|------|-----|-----------|---------|
| 5.1 04 要件定義書 §5 制約条件の継承 | S-7 §5 (C-01〜C-05) | 全 5 件 (規格優先性 / 規制範囲外 / 著作権 / 機能限界 / 機密区分) を本書でも有効として再掲 + 設計レベルで具体化. C-01 規格優先性 = 設計意思決定が CDISC 公式刊行物と矛盾する場合は公式刊行物を優先. C-04 機能限界 = S-13 KNOWN_LIMITATIONS に列挙の 4 項目を踏襲. | 各 1-2 行. 04 §5 とは別 ID 体系 (例 D-01〜D-05) で管理 |
| 5.2 設計レベル制約 | S-2 §1.4 + S-12 §10 | (1) ローカル先行 — Docker Compose ローカル実行を前提とし, クラウド展開は本範囲外. (2) プロバイダー非依存 — 特定 LLM 供給者に固定しない. (3) 読取専用源 — `knowledge_base/` は変更不可. 本書記述の改修は派生著作物側に限定. (4) 範囲外 — `ai_platforms/` 配下文書の日本語化, リアルタイム同期, 法務契約は本納品物の範囲外. | 4 件. 各 1 行 |
| 5.3 設計凍結状態 | S-3 + S-4 frozen 注記 | atom_schema および ledger_schema は v1.2 (frozen 2026-04-24) に固定. P0 Pilot 完了をもって以後変更を禁ずる旨を schema 自体に明記済. 本書の §3.4 §3.5 はこの凍結に依拠する. | 凍結 = 変更不可. 凍結根拠ファイル名を引用 |
| 5.4 著作権 | S-14 + S-7 §5 C-03 | CDISC が SDTM / SDTMIG / 受控用語の各規格および原刊行物の著作権を保持. 本リポジトリは原刊行物そのものを再配布せず, 派生著作物のみを CC BY 4.0 ライセンスで配布. | 04 C-03 と同一文言で統一 |
| 5.5 範囲外 (Out of Scope) | S-2 §8 + S-12 §0.3 | (1) クラウド展開 / 認証 / マルチテナント (Phase 7 設計時点では deferred). (2) 知識ベースの自動連続更新 (rebuild pipeline). (3) 複数 SDTM 版数管理 (現状 v3.4 のみ). (4) `ai_platforms/` 配下の日本語化. (5) 法務契約書 (NDA / SOW). | DESIGN_RAG_KG §8 + PLAN §0.3 から 5 項目集約 |

### シート 6 (6_参考資料)

| 区分 | 内容 | 出典 |
|------|------|------|
| 上位根拠 | 04 要件定義書 (本納品物 §3 §4 §5 引用元) | `docs/jp/04_要件定義書.xlsx` |
| 内部設計仕様 | RAG + KG 設計仕様 (Phase 7) | `docs/DESIGN_RAG_KG.md` |
| 内部設計仕様 | atom データ schema v1.2 (frozen 2026-04-24) | `.work/06_deep_verification/schema/atom_schema.json` |
| 内部設計仕様 | ledger データ schema v1.2 (frozen 2026-04-24) | `.work/06_deep_verification/schema/ledger_schema.json` |
| 内部計画 | 知識ベース 構造方針 | `.work/00_planning/restructure_plan.md` |
| 内部計画 | CDISC 4 種公式刊行物関係 | `.work/00_planning/source_relationship.md` |
| 知識ベース 入口 | 索引 | `knowledge_base/INDEX.md` |
| 知識ベース 経路層 | 経路層文書 | `knowledge_base/ROUTING.md` |
| Phase 6.5 リリース | AI 平台展開 v1.0 | `ai_platforms/release/v1.0/` |
| Phase 6.5 既知の限界 | 既知の限界 | `ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md` |
| 公式刊行物 | SDTMIG v3.4 (2021 年 11 月) 461 頁 | CDISC Library |
| 公式刊行物 | SDTM Model v2.0 Final (2021 年 11 月) 74 頁 | CDISC Library |
| 公式刊行物 | SDTMIG xlsx v3.4 (1,917 変数) | CDISC Library |
| 公式刊行物 | Controlled Terminology xlsx 2024 年版 (1,005 codelist / 37,939 用語) | CDISC Library |
| 規格 | GAMP 5 (ISPE 2nd Edition 2022) | ISPE |
| 規格 | ICH E6(R3) GCP | ICH |
| 規格 | ALCOA+ データ完全性原則 | (一般) |
| 規格 | 21 CFR Part 11 (米国) | FDA |
| 規格 | PMDA ER/ES 指針 | PMDA |
| 配布許諾 | CC BY 4.0 (派生著作物) | `DISCLAIMER.md` |

writer 注: 本シートは links 型または table 型で記述. 内部パスは相対パス (リポジトリルート起点) で記載.

---

## 2. 用語規律ヒント (writer 派発前 注入)

writer は本マッピング + `term_mapping.yml` v0.5 を併読し以下を厳守:

| 源原文 (英語) / 候補 | 採用語 (term_mapping.yml) | 出典規格 | 注 |
|---------------------|--------------------------|----------|----|
| evidence | 証跡 | 業界慣行 (規律 H-1) | 04 で確立 |
| atom (内部用語) | 検証単位 | (mapping 参照) | 但し本書 §3.4 では schema 仕様としての固有名「atom_schema」「PDF 原子 / MD 原子」は構造名としてそのまま使用可 (term_mapping.yml notes に整合). 文中で工程的な言及は「検証単位」 |
| ledger (内部用語) | 管理表 | (mapping 参照) | schema 固有名「ledger_schema」は §3.5 でそのまま使用可. 工程的言及は「突合管理表」 |
| traceability | 追跡可能性 | JIS X 0160 | 04 NFR-05 と統一 |
| placeholder | 占位マーカー | (規律 H-1) | 04 NFR-01 と統一 |
| coverage ratio | 覆盖率 | (mapping 参照) | 04 で確立 |
| pipeline | パイプライン | IPA システム開発関連ガイド (§Phase 3 用語集登録予定) | 04 用語監査 round 1 で採用 |
| forward / reverse (突合方向) | 順方向 / 逆方向 | (新規) | §3.5 で初出. mapping 追加提案候補 |
| chunk (RAG) | チャンク | (新規) | §3.6 で初出. JIS X 0160 用語に登録なし → カタカナ標準語 |
| node / relationship (KG) | ノード / リレーション | (新規) | §3.7 で初出. 情報処理用語として標準 |
| Local-first | ローカル先行 | (新規) | §1.5 §5.2 で初出 |

**注意**: writer が新規導入する訳語 (forward / reverse / chunk / node / relationship / Local-first 等) は term_audit subagent への提案として記録 (本書 §3 mapping 提案候補).

---

## 3. mapping 提案候補 (writer → audit に申送り想定)

| 用語 (英語 / 内部) | 本書での仮採用 | 候補別案 | 監査依頼内容 |
|--------------------|---------------|---------|-------------|
| forward (突合方向) | 順方向 | フォワード | JIS X 0160 / IPA 関連用語の確認要 |
| reverse (突合方向) | 逆方向 | リバース | 同上 |
| chunk (RAG 検索単位) | チャンク | データ片 / 断片 | IPA 検索エンジン関連用語の確認要. RAG 業界標準に沿う必要あり |
| node / relationship (KG) | ノード / リレーション | 節点 / 関係 | JIS X 0160 グラフ理論用語の確認要 |
| Local-first | ローカル先行 | ローカル優先 | IPA システム開発関連ガイドの用語確認要 |
| RAG / KG (略号) | 略号のまま (本書では「検索拡張生成 (RAG: Retrieval-Augmented Generation)」「知識グラフ (KG: Knowledge Graph)」と初出時に正式名併記) | — | 国際標準略号. mapping 追加要 |
| Cypher | Cypher (固有名) | — | 固有名のためそのまま. 99 用語集には登録要 |
| Docker Compose | Docker Compose (固有名) | — | 固有名のためそのまま. 99 用語集には登録要 |
| Streamlit / FastAPI / Chroma / Neo4j / LiteLLM | 固有名のまま | — | 各製品名. 99 用語集には初出時のみ登録 |

writer はこれら候補について audit subagent から指示が来る前提で yml 内に該当語を使う場合は仮採用語 1 候補に統一して記録. 04 で確立した「外来語の長音記号 case-by-case 規則」(D-7 決定事項) に従う.

---

## 4. 抜粋禁止事項

writer は以下を yml に転記しないこと:

- METHODOLOGY.md / DESIGN_RAG_KG.md 内の commit hash / GitHub URL / 著者名 / 内部 commit リンク
- `.work/06_deep_verification/_progress.json` / `docs/jp/_progress.json` の round 番号 / batch 番号 / 段階名 (内部用語規律違反)
- `.work/03_verification/issues_found.md` の Issue 番号や fix commit リンク
- 開発担当者の個人名 (規律 H-4: 作成者個人情報含めない)
- subagent_type / writer / reviewer / audit_record / audited_by 等 schema 内部の役割名 — schema 固有名としては §3.5 で言及可能だが, 工程的言及は禁止 (term_blacklist.yml 準拠)

ただし以下は OK:
- 公式刊行物の版番号 / 頁番号 / 規格名
- schema 固有名 (atom_schema / ledger_schema / atom_type / verdict / similarity_score / matched_by) — 構造名としての用途のみ
- 標準訳の用語 / 製品固有名 (Streamlit / FastAPI / Chroma / Neo4j / LiteLLM / openpyxl / Cypher / Docker Compose)

---

## 5. writer self-check 補強

writer は産物提出前に本マッピング §1 の各シート ID 行を逐行に対応させた充足表を実行記録に必須含める. 対応欠落あれば自己 FAIL.

加えて本書固有の self-check 観点:

| # | 観点 | 検証方法 |
|---|------|---------|
| 6 | Phase 7 RAG+KG が「設計済 / 未実装」と明示されているか | yml grep で「設計済」「未実装」の出現確認, 該当節 (2.5 / 3.6 / 3.7 / 4.4) すべてに 1 件以上 |
| 7 | atom / ledger schema 数値 (9 enum / 5 enum / similarity_score 0.0-1.0 / PARTIAL ≥0.50) が原文と一致 | S-3 / S-4 と yml 該当節を grep 比較 |
| 8 | 04 要件定義書との接続が §1.1 §5.1 に明示されているか | yml grep で「04」「要件定義書」言及確認 |
| 9 | knowledge_base 構造数値 (63 / 6 / 6 / 受控用語 1,005 codelist 37,939 用語) が S-9 / S-7 §2.2 と一致 | yml 該当節と源文 直接照合 |

---

## 6. 期待される本文ボリューム

各シート 800-1,500 字程度を目安. 04 要件定義書と同等水準. 表型シート (3_データモデル / 4_外部IF / 5_制約事項) は表 8-15 行 + 補足注記. text 型シート (1_概要 / 2_全体構成) は段落主体.

---

## 履歴

- v0.1 (2026-04-29): 初版. 01 基本設計書 writer 派発前.
