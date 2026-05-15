# SDTM ナレッジベース — Release v1.1 変更履歴 (日本語)

> タグ: `v1.1-company-release` (リリース: 2026-05-15)
> 前バージョン: `v1.0-company-release` (2026-04-27)
> 動機: `06_deep_verification` 支線の修正反映 (収束 2026-05-12)

## 概要

v1.1 は v1.0 会社リリース版の**コンテンツ刷新**です. 方法論 / system prompt / チュートリアル / 用語集 / Demo 問題 / プラットフォーム比較文書はいずれも変更なし. **4 つの AI プラットフォーム配信パッケージ `self_deploy/*/uploads/` のみを 06 検証後の `knowledge_base/` から再ビルド**しました.

## ナレッジベースの変更点 (本リリースの源)

`06_deep_verification` 支線で原子レベルの監査 + 修復を実施. `knowledge_base/` 純影響: **43 ファイル変更, +1,405 / -234 行**.

主な内容:

- **新 domain 追加: DI (Device Identifiers, SDTMIG-MD)** — 医療機器研究の study reference dataset. KB は現在 **64 domain** をカバー (旧 63).
- **PC/assumptions.md** — §6.3.5.9 "Relating PP Records to PC Records" (RELREC) 節を追加. PC と PP の連結 4 方法 (A/B/C/D) を含む (+118 行).
- **TA/assumptions.md** — 大幅拡充 (+175 行).
- **chapters/{ch02_fundamentals, ch04_general_assumptions, ch08_relationships, ch10_appendices}** — 原子レベルカバレッジ監査によるコンテンツ補強.
- **TI / TS / TU / TV / SC / NV** 等 — セクションレベルのギャップを充填 (P6 T4 Tier A 修復).
- 修復後カバレッジ率: **99.02%** (調整後分母); 幻覚原子 0.

完全な振り返り: `branches/06_deep_verification/RETROSPECTIVE.md`.

## プラットフォーム別パッケージ変更

### Claude Projects (`self_deploy/claude/uploads/`)

19 ファイル. 06 修正を反映した刷新パッケージ:
- `02_chapters.md` — 章全文再抽出
- `05_mega_spec.md` — 64 domain spec (DI に spec なしで 63 段のまま)
- `06_assumptions.md` — 64 domain assumption (DI 含む)
- `07_examples_catalog.md` — examples カタログ (PC RELREC 追加)
- `09_examples_data_high.md` + `10_examples_data_others.md` — examples テーブル刷新
- `03_model.md` — model 刷新 (observation_classes に変更あり)

不変: `00_routing.md`, `01_index.md`, `04_variable_index.md`, `08_terminology_map.md`, `11/12/13` terminology パッケージ.

### ChatGPT GPTs (`self_deploy/chatgpt/uploads/`)

9 ファイル. 刷新:
- `02_chapters_all.md` (+12.4 KB)
- `03_model_all.md` (小規模刷新)
- `05_domain_assumptions_all.md` (+74.2 KB — DI 追加, 64 段)
- `06_domain_examples_all.md` (+18.5 KB — PC RELREC 等)

不変: `01_navigation.md`, `04_domain_specs_all.md`, `07/08/09` terminology.

### Gemini Gems (`self_deploy/gemini/uploads/`)

KB 派生 3 ファイル (4 番目の `04_business_scenarios_and_cross_domain.md` は writer 執筆で不変). 3 ファイル全刷新:
- `01_navigation_and_quick_reference.md` (+13.9 KB — chapters/model/索引)
- `02_domains_spec_and_assumptions.md` (+74.2 KB — DI 追加)
- `03_domains_examples.md` (+18.5 KB — PC RELREC 等)

### NotebookLM (`self_deploy/notebooklm/uploads/`)

42 buckets. **22 buckets を刷新** (06 で変更された KB ファイルを含む全 buckets):
- `03_sp_demographics_subject`, `04_sp_se_sm_sv_co`, `06_int_concomitant_cm_ag_ml`,
- `09_ev_disposition_ds_dv_ce`, `10_ev_history_mh_ho_be`,
- `11_fnd_lab_lb`, `13_fnd_physical_exam_pe`, `15_fnd_biomarkers_mb_mi_ms_mk`,
- `16_fnd_pharma_pc_pp` (注目: PC §6.3.5.9 RELREC 追加),
- `17_fnd_oncology_tr_tu_rs_oe`, `21_fnd_other_nv_re_rp`,
- `25_td_meta_ti_ts_oi` (DI 追加 — bucket 名は DI を含むよう更新; SDTMIG-MD 医療機器 domain)

NotebookLM 総単語数: 1,599,397 (旧 1,599,332; DI から +65 語).

## v1.0 から不変

- 全メタ文書: `METHODOLOGY.{en,zh,ja}.md`, `USER_GUIDE.{en,zh,ja}.md`, `KNOWN_LIMITATIONS.{en,zh,ja}.md`, `PLATFORM_COMPARISON.{en,zh,ja}.md`, `DEMO_QUESTIONS.{en,zh,ja}.md`, `GLOSSARY.{en,zh,ja}.md`, `README.{en,zh,ja}.md`.
- 全 system prompts およびチュートリアル.

## v1.0 → v1.1 移行手順

セルフホストユーザー向け:
1. `self_deploy/<platform>/uploads/*.md` をデプロイ済みインスタンスに再アップロード.
2. system prompts / チュートリアル / メタ文書は**変更不要**.
3. 各プラットフォームの既存セッションは再インデックス後に新内容が反映されます.
