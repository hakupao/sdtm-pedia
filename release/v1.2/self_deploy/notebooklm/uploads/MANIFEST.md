# SDTM Knowledge Base — NotebookLM 上传 MANIFEST (v2)

> **产出日期**: 2026-04-21 (P3.1 merge 后更新)
> **执行脚本**: `dev/scripts/merge_sources.py` (words/chars 从实际合成文件取, 非 bucket_config 估算)
> **上传文件数**: **42** (Pro 300 cap 的 14.0%)
> **总 words**: 1,582,085
> **最大 bucket words**: 302,027 (NotebookLM per-source cap 500K, headroom 40%)
> **Notebook**: `SDTM Knowledge Base` (单 notebook, ABC 三场景分享档位切换)
> **Chat mode**: Custom (instructions.md, ≤10K char)

## 上传清单

| # | Source name | Merged files | Words | Concept |
|---|------------|--------------|-------|---------|
| 01 | `01_navigation_and_routing.md` | 2 | 2,145 | 导航 + 路由提示 + Req 变量速查入口 |
| 02 | `02_common_identifiers_and_timing.md` | 0 | 1,080 | 9 通用 Req + 24 跨域变量详 (来自 VARIABLE_INDEX.md Section 一) |
| 03 | `03_sp_demographics_subject.md` | 6 | 10,619 | DM (Special-Purpose) + SC (Findings, subject characteristics 归并) |
| 04 | `04_sp_se_sm_sv_co.md` | 12 | 9,417 | SE + SM + SV + CO (Special-Purpose 剩余 4) |
| 05 | `05_int_exposure_ex_ec.md` | 6 | 14,426 | Interventions: EX + EC (核心 exposure) |
| 06 | `06_int_concomitant_cm_ag_ml.md` | 9 | 11,070 | Interventions: CM + AG + ML |
| 07 | `07_int_procedures_pr_su.md` | 6 | 6,168 | Interventions: PR + SU |
| 08 | `08_ev_adverse_ae.md` | 3 | 7,354 | Events: AE (单独 — 重要域, 单独 slot 提高精度) |
| 09 | `09_ev_disposition_ds_dv_ce.md` | 9 | 13,732 | Events: DS + DV + CE |
| 10 | `10_ev_history_mh_ho_be.md` | 9 | 11,141 | Events: MH + HO + BE |
| 11 | `11_fnd_lab_lb.md` | 3 | 5,863 | Findings: LB (lab, 单独 slot) |
| 12 | `12_fnd_vitals_vs_eg.md` | 6 | 9,238 | Findings: VS + EG (生命体征 + ECG) |
| 13 | `13_fnd_physical_exam_pe.md` | 3 | 2,147 | Findings: PE (physical exam) |
| 14 | `14_fnd_questionnaire_qs_ie.md` | 6 | 5,033 | Findings: QS + IE (questionnaires + inclusion/exclusion) |
| 15 | `15_fnd_biomarkers_mb_mi_ms_mk.md` | 12 | 19,585 | Findings specialized: MB (microbiology) + MI (microscopic imaging) + MS (mass spec) + MK (biomarker) |
| 16 | `16_fnd_pharma_pc_pp.md` | 6 | 18,039 | Findings: PC + PP (PK concentrations + parameters) |
| 17 | `17_fnd_oncology_tr_tu_rs_oe.md` | 12 | 22,769 | Findings: TR (tumor response) + TU (tumor ID) + RS (response) + OE (ophtalm exam) |
| 18 | `18_fnd_device_da_dd_gf_is.md` | 12 | 22,622 | Findings: DA (drug accountability) + DD (death details) + GF (genomic findings) + IS (immunogen) |
| 19 | `19_fnd_morphology_bs_cp_cv.md` | 9 | 16,007 | Findings: BS (biospecimens) + CP (clinical endpoint) + CV (cardiovascular) |
| 20 | `20_fnd_about_fa_sr.md` | 6 | 10,739 | Findings About: FA + SR (2 domains) |
| 21 | `21_fnd_other_nv_re_rp.md` | 9 | 10,817 | Findings 其他: NV + RE + RP |
| 22 | `22_fnd_other_ss_ur_ft.md` | 9 | 7,649 | Findings 其他: SS + UR + FT |
| 23 | `23_td_arms_ta_tv.md` | 6 | 9,078 | Trial Design: TA + TV (arms + visits) |
| 24 | `24_td_elements_te_tm_td.md` | 9 | 5,656 | Trial Design: TE + TM + TD (elements + milestones + durations) |
| 25 | `25_td_meta_ti_ts_oi.md` | 9 | 7,498 | Trial Design: TI + TS + OI (inclusion + summary + organism) |
| 26 | `26_rel_relrec_relspec_relsub.md` | 9 | 3,627 | Relationships: RELREC + RELSPEC + RELSUB |
| 27 | `27_rel_suppqual.md` | 3 | 1,835 | Supplemental: SUPPQUAL |
| 28 | `28_ig_ch01_ch02_ch03.md` | 3 | 6,751 | IG: ch01 intro + ch02 fundamentals + ch03 submitting data |
| 29 | `29_ig_ch04_general_assumptions.md` | 1 | 20,315 | IG: ch04 general assumptions (20K words 单独 slot, 关键规则源) |
| 30 | `30_ig_ch08_ch10.md` | 2 | 12,933 | IG: ch08 relationships + ch10 appendices |
| 31 | `31_model_obs_classes.md` | 2 | 6,596 | Model: observation classes + special purpose domains |
| 32 | `32_model_concepts_study_rel.md` | 4 | 5,801 | Model: concepts + associated persons + study-level + relationship datasets |
| 33 | `33_ct_general.md` | 5 | 98,051 | CT core: general codelists (~130K words) |
| 34 | `34_ct_lb.md` | 4 | 129,606 | CT core: lab codelists (~180K words, 单 slot 内) |
| 35 | `35_ct_findings_eg_qs_vs_mi_ae_dispo.md` | 9 | 83,907 | CT core: ECG + QS + VS + MI + AE + disposition + findings_about |
| 36 | `36_ct_specialized_micro_oncology_pk_is_cp.md` | 13 | 162,073 | CT core: microbiology + oncology + PK + is_domain + cp |
| 37 | `37_ct_misc_int_dm_sp_td_gf_oi_other.md` | 11 | 88,232 | CT core: interventions + dm + special_purpose + trial_design + gf + oi + other_part1-5 |
| 38 | `38_ct_questionnaires_part1_22.md` | 22 | 302,027 | CT questionnaires part 1-22 (22 files) |
| 39 | `39_ct_questionnaires_part23_43.md` | 21 | 291,941 | CT questionnaires part 23-43 (21 files) |
| 40 | `40_ct_supplementary.md` | 6 | 75,907 | CT supplementary (6 files) |
| 41 | `41_variable_index.md` | 1 | 27,758 | VARIABLE_INDEX.md 全集 (27K words) |
| 42 | `42_req_variable_coverage_audit.md` | 0 | 4,833 | 元 source: Req 变量全覆盖审计 (A4 产物 + 176 Req 变量全名单) |

## Req 变量覆盖声明 (Q1 红线 结构级自证)

✅ **∀ req ∈ req_vars_full_set (176), ∃ bucket ∈ uploads, 使 req ∈ bucket.covered_req_set**

**Q1 红线自证: 零漏集 (∅ gap)**. 63 domains 全覆盖, 176 独立 Req 变量全覆盖. 详见 bucket 42 (`42_req_variable_coverage_audit.md`) + 原审计 `dev/evidence/req_vars_coverage_audit.md`.

## 后续

- **P3.2**: 用户登 notebooklm.google.com → 新建 `SDTM Knowledge Base` → 拖拽本目录全部 42 个 md → 等 indexing 完成
- **P3.3**: Chat → Configure → Custom mode, 贴 `../instructions.md` 全文 (≤10K char)
- **P3.4**: Indexing smoke N=10 (每 source 预览 + 10 题 citation 精确回指)
- **P3.4.5**: Req 变量业务问答 N=10 (Q1 红线语义级自证, 规则 A 正本)
