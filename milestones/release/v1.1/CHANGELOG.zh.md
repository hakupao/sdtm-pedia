# SDTM 知识库 — Release v1.1 变更说明 (中文)

> Tag: `v1.1-company-release` (发布: 2026-05-15)
> 上一版: `v1.0-company-release` (2026-04-27)
> 触发: 回灌 `06_deep_verification` 旁枝修复 (收尾 2026-05-12)

## 概要

v1.1 是 v1.0 公司发布版的**内容刷新**. 方法论 / system prompt / 教程 / 术语表 / Demo 题 / 平台对比文档**全部不变**. **仅 4 个 AI 平台上传包 `self_deploy/*/uploads/` 用 06 验证后的 `knowledge_base/` 重建**.

## 知识库改动 (本次发布的源)

`06_deep_verification` 旁枝对知识库做了原子级审计 + 修复. 净影响: **43 文件改动, +1,405 / -234 行**.

要点:

- **新增 domain DI** (Device Identifiers, SDTMIG-MD) — 医疗器械研究参考数据集. KB 现覆盖 **64 个 domain** (原 63).
- **PC/assumptions.md** — 新增 §6.3.5.9 "Relating PP Records to PC Records" (RELREC) 节, 含 4 种链接方法 A/B/C/D (+118 行).
- **TA/assumptions.md** — 大幅扩充 (+175 行).
- **chapters/{ch02_fundamentals, ch04_general_assumptions, ch08_relationships, ch10_appendices}** — 原子级覆盖审计后内容补强.
- **TI / TS / TU / TV / SC / NV** 等 — 节级缺口填充 (P6 T4 Tier A 修复).
- 修复后覆盖率: **99.02%** (调整分母); 0 幻觉原子.

完整反思: `branches/06_deep_verification/RETROSPECTIVE.md`.

## 各平台包变更

### Claude Projects (`self_deploy/claude/uploads/`)

19 文件. 重建包:
- `02_chapters.md` — 章节全文重抽
- `05_mega_spec.md` — 64 域 spec (DI 无 spec, 仍 63 段)
- `06_assumptions.md` — 64 域 assumption (含 DI)
- `07_examples_catalog.md` — examples 目录 (PC RELREC examples 新加)
- `09_examples_data_high.md` + `10_examples_data_others.md` — examples 数据表刷新
- `03_model.md` — model 刷新 (observation_classes 改)

不变: `00_routing.md`, `01_index.md`, `04_variable_index.md`, `08_terminology_map.md`, `11/12/13` terminology 包.

### ChatGPT GPTs (`self_deploy/chatgpt/uploads/`)

9 文件. 刷新:
- `02_chapters_all.md` (+12.4 KB)
- `03_model_all.md` (小幅)
- `05_domain_assumptions_all.md` (+74.2 KB — DI 加入, 64 段)
- `06_domain_examples_all.md` (+18.5 KB — PC RELREC 等)

不变: `01_navigation.md`, `04_domain_specs_all.md`, `07/08/09` terminology.

### Gemini Gems (`self_deploy/gemini/uploads/`)

3 个 KB 派生文件 (第 4 个 `04_business_scenarios_and_cross_domain.md` 是 writer 手写, 不变). 3 个全刷新:
- `01_navigation_and_quick_reference.md` (+13.9 KB — chapters/model/索引)
- `02_domains_spec_and_assumptions.md` (+74.2 KB — DI 加入)
- `03_domains_examples.md` (+18.5 KB — PC RELREC 等)

### NotebookLM (`self_deploy/notebooklm/uploads/`)

42 个 buckets. **22 个 buckets 刷新** (含 06 改动 KB 的全部 buckets):
- `03_sp_demographics_subject`, `04_sp_se_sm_sv_co`, `06_int_concomitant_cm_ag_ml`
- `09_ev_disposition_ds_dv_ce`, `10_ev_history_mh_ho_be`
- `11_fnd_lab_lb`, `13_fnd_physical_exam_pe`, `15_fnd_biomarkers_mb_mi_ms_mk`
- `16_fnd_pharma_pc_pp` (重要: PC §6.3.5.9 RELREC 加入)
- `17_fnd_oncology_tr_tu_rs_oe`, `21_fnd_other_nv_re_rp`
- `25_td_meta_ti_ts_oi` (DI 加入 — bucket 改名含 DI; SDTMIG-MD 设备识别 domain)

NotebookLM 总词数: 1,599,397 (原 1,599,332; +65 词来自 DI).

## v1.0 不变项

- 全部元文档: `METHODOLOGY.{en,zh,ja}.md`, `USER_GUIDE.{en,zh,ja}.md`, `KNOWN_LIMITATIONS.{en,zh,ja}.md`, `PLATFORM_COMPARISON.{en,zh,ja}.md`, `DEMO_QUESTIONS.{en,zh,ja}.md`, `GLOSSARY.{en,zh,ja}.md`, `README.{en,zh,ja}.md`.
- 全部 system prompts 和 tutorials.

## 验证

- 每平台 rebuild 与 v1.0 baseline 做 diff, delta 与 06 旁枝改动范围一致.
- Rule D 独立 reviewer (subagent_type ≠ 主 session) APPROVE 本次 rebuild.

## v1.0 → v1.1 升级方法

自部署用户:
1. 把 `self_deploy/<platform>/uploads/*.md` 重新上传到部署实例.
2. system prompts / tutorials / 元文档**不需要**变更.
3. 每平台已存在的对话 session 重新索引后生效.
