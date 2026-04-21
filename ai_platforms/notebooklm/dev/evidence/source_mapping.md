# Phase A A3: Source Mapping — concept cluster → ≤50 bucket

> **产出日期**: 2026-04-21
> **执行脚本**: `dev/scripts/cluster_req_variables.py`
> **Bucket 总数**: **42** (目标 ≤50, headroom 8 slot)
> **Coverage**: 295/295 knowledge_base md files
> **Domain Coverage**: 63/63
> **Req Coverage**: 176/176

---

## Bucket 01: `01_navigation_and_routing.md`

**Description**: 导航 + 路由提示 + Req 变量速查入口

**Files**: 2 | **Words**: 2,139 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `INDEX.md` | 1,481 |
| 2 | `ROUTING.md` | 658 |

---

## Bucket 02: `02_common_identifiers_and_timing.md`

**Description**: 9 通用 Req + 24 跨域变量详 (来自 VARIABLE_INDEX.md Section 一)

**Files**: 0 | **Words**: 0 | **Domains**: 0 | **Req vars covered**: 0

---

## Bucket 03: `03_sp_demographics_subject.md`

**Description**: DM (Special-Purpose) + SC (Findings, subject characteristics 归并)

**Files**: 6 | **Words**: 10,601 | **Domains**: 2 | **Req vars covered**: 10

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/DM/spec.md` | 1,954 |
| 2 | `domains/DM/assumptions.md` | 1,883 |
| 3 | `domains/DM/examples.md` | 4,616 |
| 4 | `domains/SC/spec.md` | 1,201 |
| 5 | `domains/SC/assumptions.md` | 141 |
| 6 | `domains/SC/examples.md` | 806 |

**Domains covered**: DM, SC

---

## Bucket 04: `04_sp_se_sm_sv_co.md`

**Description**: SE + SM + SV + CO (Special-Purpose 剩余 4)

**Files**: 12 | **Words**: 9,381 | **Domains**: 4 | **Req vars covered**: 11

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/SE/spec.md` | 647 |
| 2 | `domains/SE/assumptions.md` | 1,027 |
| 3 | `domains/SE/examples.md` | 1,431 |
| 4 | `domains/SM/spec.md` | 460 |
| 5 | `domains/SM/assumptions.md` | 305 |
| 6 | `domains/SM/examples.md` | 579 |
| 7 | `domains/SV/spec.md` | 742 |
| 8 | `domains/SV/assumptions.md` | 973 |
| 9 | `domains/SV/examples.md` | 1,589 |
| 10 | `domains/CO/spec.md` | 691 |
| 11 | `domains/CO/assumptions.md` | 412 |
| 12 | `domains/CO/examples.md` | 525 |

**Domains covered**: CO, SE, SM, SV

---

## Bucket 05: `05_int_exposure_ex_ec.md`

**Description**: Interventions: EX + EC (核心 exposure)

**Files**: 6 | **Words**: 14,408 | **Domains**: 2 | **Req vars covered**: 7

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/EX/spec.md` | 1,619 |
| 2 | `domains/EX/assumptions.md` | 876 |
| 3 | `domains/EX/examples.md` | 6,780 |
| 4 | `domains/EC/spec.md` | 2,005 |
| 5 | `domains/EC/assumptions.md` | 841 |
| 6 | `domains/EC/examples.md` | 2,287 |

**Domains covered**: EC, EX

---

## Bucket 06: `06_int_concomitant_cm_ag_ml.md`

**Description**: Interventions: CM + AG + ML

**Files**: 9 | **Words**: 11,043 | **Domains**: 3 | **Req vars covered**: 9

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/CM/spec.md` | 2,178 |
| 2 | `domains/CM/assumptions.md` | 679 |
| 3 | `domains/CM/examples.md` | 1,574 |
| 4 | `domains/AG/spec.md` | 2,105 |
| 5 | `domains/AG/assumptions.md` | 611 |
| 6 | `domains/AG/examples.md` | 1,075 |
| 7 | `domains/ML/spec.md` | 1,671 |
| 8 | `domains/ML/assumptions.md` | 215 |
| 9 | `domains/ML/examples.md` | 935 |

**Domains covered**: AG, CM, ML

---

## Bucket 07: `07_int_procedures_pr_su.md`

**Description**: Interventions: PR + SU

**Files**: 6 | **Words**: 6,150 | **Domains**: 2 | **Req vars covered**: 7

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/PR/spec.md` | 2,006 |
| 2 | `domains/PR/assumptions.md` | 441 |
| 3 | `domains/PR/examples.md` | 626 |
| 4 | `domains/SU/spec.md` | 1,965 |
| 5 | `domains/SU/assumptions.md` | 454 |
| 6 | `domains/SU/examples.md` | 658 |

**Domains covered**: PR, SU

---

## Bucket 08: `08_ev_adverse_ae.md`

**Description**: Events: AE (单独 — 重要域, 单独 slot 提高精度)

**Files**: 3 | **Words**: 7,345 | **Domains**: 1 | **Req vars covered**: 6

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/AE/spec.md` | 3,369 |
| 2 | `domains/AE/assumptions.md` | 1,815 |
| 3 | `domains/AE/examples.md` | 2,161 |

**Domains covered**: AE

---

## Bucket 09: `09_ev_disposition_ds_dv_ce.md`

**Description**: Events: DS + DV + CE

**Files**: 9 | **Words**: 13,705 | **Domains**: 3 | **Req vars covered**: 10

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/DS/spec.md` | 828 |
| 2 | `domains/DS/assumptions.md` | 952 |
| 3 | `domains/DS/examples.md` | 6,358 |
| 4 | `domains/DV/spec.md` | 705 |
| 5 | `domains/DV/assumptions.md` | 205 |
| 6 | `domains/DV/examples.md` | 222 |
| 7 | `domains/CE/spec.md` | 1,665 |
| 8 | `domains/CE/assumptions.md` | 558 |
| 9 | `domains/CE/examples.md` | 2,212 |

**Domains covered**: CE, DS, DV

---

## Bucket 10: `10_ev_history_mh_ho_be.md`

**Description**: Events: MH + HO + BE

**Files**: 9 | **Words**: 11,114 | **Domains**: 3 | **Req vars covered**: 9

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/MH/spec.md` | 1,388 |
| 2 | `domains/MH/assumptions.md` | 1,240 |
| 3 | `domains/MH/examples.md` | 2,087 |
| 4 | `domains/HO/spec.md` | 1,327 |
| 5 | `domains/HO/assumptions.md` | 252 |
| 6 | `domains/HO/examples.md` | 1,021 |
| 7 | `domains/BE/spec.md` | 1,125 |
| 8 | `domains/BE/assumptions.md` | 383 |
| 9 | `domains/BE/examples.md` | 2,291 |

**Domains covered**: BE, HO, MH

---

## Bucket 11: `11_fnd_lab_lb.md`

**Description**: Findings: LB (lab, 单独 slot)

**Files**: 3 | **Words**: 5,854 | **Domains**: 1 | **Req vars covered**: 6

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/LB/spec.md` | 3,495 |
| 2 | `domains/LB/assumptions.md` | 507 |
| 3 | `domains/LB/examples.md` | 1,852 |

**Domains covered**: LB

---

## Bucket 12: `12_fnd_vitals_vs_eg.md`

**Description**: Findings: VS + EG (生命体征 + ECG)

**Files**: 6 | **Words**: 9,220 | **Domains**: 2 | **Req vars covered**: 9

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/VS/spec.md` | 2,030 |
| 2 | `domains/VS/assumptions.md` | 188 |
| 3 | `domains/VS/examples.md` | 782 |
| 4 | `domains/EG/spec.md` | 2,447 |
| 5 | `domains/EG/assumptions.md` | 467 |
| 6 | `domains/EG/examples.md` | 3,306 |

**Domains covered**: EG, VS

---

## Bucket 13: `13_fnd_physical_exam_pe.md`

**Description**: Findings: PE (physical exam)

**Files**: 3 | **Words**: 2,138 | **Domains**: 1 | **Req vars covered**: 6

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/PE/spec.md` | 1,571 |
| 2 | `domains/PE/assumptions.md` | 221 |
| 3 | `domains/PE/examples.md` | 346 |

**Domains covered**: PE

---

## Bucket 14: `14_fnd_questionnaire_qs_ie.md`

**Description**: Findings: QS + IE (questionnaires + inclusion/exclusion)

**Files**: 6 | **Words**: 5,015 | **Domains**: 2 | **Req vars covered**: 13

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/QS/spec.md` | 1,989 |
| 2 | `domains/QS/assumptions.md` | 1,233 |
| 3 | `domains/QS/examples.md` | 433 |
| 4 | `domains/IE/spec.md` | 894 |
| 5 | `domains/IE/assumptions.md` | 227 |
| 6 | `domains/IE/examples.md` | 239 |

**Domains covered**: IE, QS

---

## Bucket 15: `15_fnd_biomarkers_mb_mi_ms_mk.md`

**Description**: Findings specialized: MB (microbiology) + MI (microscopic imaging) + MS (mass spec) + MK (biomarker)

**Files**: 12 | **Words**: 19,549 | **Domains**: 4 | **Req vars covered**: 16

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/MB/spec.md` | 2,440 |
| 2 | `domains/MB/assumptions.md` | 458 |
| 3 | `domains/MB/examples.md` | 3,783 |
| 4 | `domains/MI/spec.md` | 1,860 |
| 5 | `domains/MI/assumptions.md` | 164 |
| 6 | `domains/MI/examples.md` | 1,034 |
| 7 | `domains/MS/spec.md` | 3,207 |
| 8 | `domains/MS/assumptions.md` | 467 |
| 9 | `domains/MS/examples.md` | 1,897 |
| 10 | `domains/MK/spec.md` | 2,069 |
| 11 | `domains/MK/assumptions.md` | 114 |
| 12 | `domains/MK/examples.md` | 2,056 |

**Domains covered**: MB, MI, MK, MS

---

## Bucket 16: `16_fnd_pharma_pc_pp.md`

**Description**: Findings: PC + PP (PK concentrations + parameters)

**Files**: 6 | **Words**: 18,021 | **Domains**: 2 | **Req vars covered**: 9

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/PC/spec.md` | 2,080 |
| 2 | `domains/PC/assumptions.md` | 65 |
| 3 | `domains/PC/examples.md` | 10,654 |
| 4 | `domains/PP/spec.md` | 1,482 |
| 5 | `domains/PP/assumptions.md` | 201 |
| 6 | `domains/PP/examples.md` | 3,539 |

**Domains covered**: PC, PP

---

## Bucket 17: `17_fnd_oncology_tr_tu_rs_oe.md`

**Description**: Findings: TR (tumor response) + TU (tumor ID) + RS (response) + OE (ophtalm exam)

**Files**: 12 | **Words**: 22,733 | **Domains**: 4 | **Req vars covered**: 15

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/TR/spec.md` | 1,641 |
| 2 | `domains/TR/assumptions.md` | 926 |
| 3 | `domains/TR/examples.md` | 3,118 |
| 4 | `domains/TU/spec.md` | 1,650 |
| 5 | `domains/TU/assumptions.md` | 2,175 |
| 6 | `domains/TU/examples.md` | 1,678 |
| 7 | `domains/RS/spec.md` | 2,628 |
| 8 | `domains/RS/assumptions.md` | 1,559 |
| 9 | `domains/RS/examples.md` | 2,032 |
| 10 | `domains/OE/spec.md` | 2,671 |
| 11 | `domains/OE/assumptions.md` | 205 |
| 12 | `domains/OE/examples.md` | 2,450 |

**Domains covered**: OE, RS, TR, TU

---

## Bucket 18: `18_fnd_device_da_dd_gf_is.md`

**Description**: Findings: DA (drug accountability) + DD (death details) + GF (genomic findings) + IS (immunogen)

**Files**: 12 | **Words**: 22,586 | **Domains**: 4 | **Req vars covered**: 15

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/DA/spec.md` | 1,322 |
| 2 | `domains/DA/assumptions.md` | 148 |
| 3 | `domains/DA/examples.md` | 877 |
| 4 | `domains/DD/spec.md` | 667 |
| 5 | `domains/DD/assumptions.md` | 222 |
| 6 | `domains/DD/examples.md` | 706 |
| 7 | `domains/GF/spec.md` | 2,735 |
| 8 | `domains/GF/assumptions.md` | 556 |
| 9 | `domains/GF/examples.md` | 4,288 |
| 10 | `domains/IS/spec.md` | 2,909 |
| 11 | `domains/IS/assumptions.md` | 676 |
| 12 | `domains/IS/examples.md` | 7,480 |

**Domains covered**: DA, DD, GF, IS

---

## Bucket 19: `19_fnd_morphology_bs_cp_cv.md`

**Description**: Findings: BS (biospecimens) + CP (clinical endpoint) + CV (cardiovascular)

**Files**: 9 | **Words**: 15,980 | **Domains**: 3 | **Req vars covered**: 12

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/BS/spec.md` | 1,630 |
| 2 | `domains/BS/assumptions.md` | 169 |
| 3 | `domains/BS/examples.md` | 375 |
| 4 | `domains/CP/spec.md` | 4,141 |
| 5 | `domains/CP/assumptions.md` | 2,093 |
| 6 | `domains/CP/examples.md` | 4,709 |
| 7 | `domains/CV/spec.md` | 2,078 |
| 8 | `domains/CV/assumptions.md` | 73 |
| 9 | `domains/CV/examples.md` | 712 |

**Domains covered**: BS, CP, CV

---

## Bucket 20: `20_fnd_about_fa_sr.md`

**Description**: Findings About: FA + SR (2 domains)

**Files**: 6 | **Words**: 10,721 | **Domains**: 2 | **Req vars covered**: 11

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/FA/spec.md` | 1,657 |
| 2 | `domains/FA/assumptions.md` | 266 |
| 3 | `domains/FA/examples.md` | 4,544 |
| 4 | `domains/SR/spec.md` | 1,918 |
| 5 | `domains/SR/assumptions.md` | 171 |
| 6 | `domains/SR/examples.md` | 2,165 |

**Domains covered**: FA, SR

---

## Bucket 21: `21_fnd_other_nv_re_rp.md`

**Description**: Findings 其他: NV + RE + RP

**Files**: 9 | **Words**: 10,790 | **Domains**: 3 | **Req vars covered**: 12

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/NV/spec.md` | 2,164 |
| 2 | `domains/NV/assumptions.md` | 55 |
| 3 | `domains/NV/examples.md` | 2,076 |
| 4 | `domains/RE/spec.md` | 2,337 |
| 5 | `domains/RE/assumptions.md` | 126 |
| 6 | `domains/RE/examples.md` | 1,192 |
| 7 | `domains/RP/spec.md` | 1,862 |
| 8 | `domains/RP/assumptions.md` | 117 |
| 9 | `domains/RP/examples.md` | 861 |

**Domains covered**: NV, RE, RP

---

## Bucket 22: `22_fnd_other_ss_ur_ft.md`

**Description**: Findings 其他: SS + UR + FT

**Files**: 9 | **Words**: 7,622 | **Domains**: 3 | **Req vars covered**: 13

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/SS/spec.md` | 1,098 |
| 2 | `domains/SS/assumptions.md` | 181 |
| 3 | `domains/SS/examples.md` | 17 |
| 4 | `domains/UR/spec.md` | 2,051 |
| 5 | `domains/UR/assumptions.md` | 45 |
| 6 | `domains/UR/examples.md` | 568 |
| 7 | `domains/FT/spec.md` | 1,911 |
| 8 | `domains/FT/assumptions.md` | 1,311 |
| 9 | `domains/FT/examples.md` | 440 |

**Domains covered**: FT, SS, UR

---

## Bucket 23: `23_td_arms_ta_tv.md`

**Description**: Trial Design: TA + TV (arms + visits)

**Files**: 6 | **Words**: 9,060 | **Domains**: 2 | **Req vars covered**: 4

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/TA/spec.md` | 582 |
| 2 | `domains/TA/assumptions.md` | 837 |
| 3 | `domains/TA/examples.md` | 5,550 |
| 4 | `domains/TV/spec.md` | 524 |
| 5 | `domains/TV/assumptions.md` | 536 |
| 6 | `domains/TV/examples.md` | 1,031 |

**Domains covered**: TA, TV

---

## Bucket 24: `24_td_elements_te_tm_td.md`

**Description**: Trial Design: TE + TM + TD (elements + milestones + durations)

**Files**: 9 | **Words**: 5,629 | **Domains**: 3 | **Req vars covered**: 14

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/TE/spec.md` | 353 |
| 2 | `domains/TE/assumptions.md` | 909 |
| 3 | `domains/TE/examples.md` | 1,263 |
| 4 | `domains/TM/spec.md` | 255 |
| 5 | `domains/TM/assumptions.md` | 103 |
| 6 | `domains/TM/examples.md` | 179 |
| 7 | `domains/TD/spec.md` | 555 |
| 8 | `domains/TD/assumptions.md` | 522 |
| 9 | `domains/TD/examples.md` | 1,490 |

**Domains covered**: TD, TE, TM

---

## Bucket 25: `25_td_meta_ti_ts_oi.md`

**Description**: Trial Design: TI + TS + OI (inclusion + summary + organism)

**Files**: 9 | **Words**: 7,471 | **Domains**: 3 | **Req vars covered**: 12

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/TI/spec.md` | 437 |
| 2 | `domains/TI/assumptions.md` | 361 |
| 3 | `domains/TI/examples.md` | 183 |
| 4 | `domains/TS/spec.md` | 615 |
| 5 | `domains/TS/assumptions.md` | 1,718 |
| 6 | `domains/TS/examples.md` | 2,915 |
| 7 | `domains/OI/spec.md` | 369 |
| 8 | `domains/OI/assumptions.md` | 449 |
| 9 | `domains/OI/examples.md` | 424 |

**Domains covered**: OI, TI, TS

---

## Bucket 26: `26_rel_relrec_relspec_relsub.md`

**Description**: Relationships: RELREC + RELSPEC + RELSUB

**Files**: 9 | **Words**: 3,600 | **Domains**: 3 | **Req vars covered**: 8

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/RELREC/spec.md` | 412 |
| 2 | `domains/RELREC/assumptions.md` | 741 |
| 3 | `domains/RELREC/examples.md` | 735 |
| 4 | `domains/RELSPEC/spec.md` | 305 |
| 5 | `domains/RELSPEC/assumptions.md` | 136 |
| 6 | `domains/RELSPEC/examples.md` | 227 |
| 7 | `domains/RELSUB/spec.md` | 322 |
| 8 | `domains/RELSUB/assumptions.md` | 460 |
| 9 | `domains/RELSUB/examples.md` | 262 |

**Domains covered**: RELREC, RELSPEC, RELSUB

---

## Bucket 27: `27_rel_suppqual.md`

**Description**: Supplemental: SUPPQUAL

**Files**: 3 | **Words**: 1,826 | **Domains**: 1 | **Req vars covered**: 7

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `domains/SUPPQUAL/spec.md` | 598 |
| 2 | `domains/SUPPQUAL/assumptions.md` | 812 |
| 3 | `domains/SUPPQUAL/examples.md` | 416 |

**Domains covered**: SUPPQUAL

---

## Bucket 28: `28_ig_ch01_ch02_ch03.md`

**Description**: IG: ch01 intro + ch02 fundamentals + ch03 submitting data

**Files**: 3 | **Words**: 6,742 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `chapters/ch01_introduction.md` | 1,651 |
| 2 | `chapters/ch02_fundamentals.md` | 1,905 |
| 3 | `chapters/ch03_submitting_data.md` | 3,186 |

---

## Bucket 29: `29_ig_ch04_general_assumptions.md`

**Description**: IG: ch04 general assumptions (20K words 单独 slot, 关键规则源)

**Files**: 1 | **Words**: 20,312 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `chapters/ch04_general_assumptions.md` | 20,312 |

---

## Bucket 30: `30_ig_ch08_ch10.md`

**Description**: IG: ch08 relationships + ch10 appendices

**Files**: 2 | **Words**: 12,927 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `chapters/ch08_relationships.md` | 8,149 |
| 2 | `chapters/ch10_appendices.md` | 4,778 |

---

## Bucket 31: `31_model_obs_classes.md`

**Description**: Model: observation classes + special purpose domains

**Files**: 2 | **Words**: 6,590 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `model/02_observation_classes.md` | 4,260 |
| 2 | `model/03_special_purpose_domains.md` | 2,330 |

---

## Bucket 32: `32_model_concepts_study_rel.md`

**Description**: Model: concepts + associated persons + study-level + relationship datasets

**Files**: 4 | **Words**: 5,789 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `model/01_concepts_and_terms.md` | 1,168 |
| 2 | `model/04_associated_persons.md` | 612 |
| 3 | `model/05_study_level_data.md` | 2,504 |
| 4 | `model/06_relationship_datasets.md` | 1,505 |

---

## Bucket 33: `33_ct_general.md`

**Description**: CT core: general codelists (~130K words)

**Files**: 5 | **Words**: 98,036 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `terminology/core/general_part1.md` | 39,561 |
| 2 | `terminology/core/general_part2.md` | 5,496 |
| 3 | `terminology/core/general_part3.md` | 17,632 |
| 4 | `terminology/core/general_part4.md` | 9,177 |
| 5 | `terminology/core/general_part5.md` | 26,170 |

---

## Bucket 34: `34_ct_lb.md`

**Description**: CT core: lab codelists (~180K words, 单 slot 内)

**Files**: 4 | **Words**: 129,594 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `terminology/core/lb_part1.md` | 1,655 |
| 2 | `terminology/core/lb_part2.md` | 61,853 |
| 3 | `terminology/core/lb_part3.md` | 65,822 |
| 4 | `terminology/core/lb_part4.md` | 264 |

---

## Bucket 35: `35_ct_findings_eg_qs_vs_mi_ae_dispo.md`

**Description**: CT core: ECG + QS + VS + MI + AE + disposition + findings_about

**Files**: 9 | **Words**: 83,880 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `terminology/core/eg_part1.md` | 11,262 |
| 2 | `terminology/core/eg_part2.md` | 11,892 |
| 3 | `terminology/core/eg_part3.md` | 10,782 |
| 4 | `terminology/core/qs_part1.md` | 20,210 |
| 5 | `terminology/core/vs.md` | 4,721 |
| 6 | `terminology/core/mi.md` | 10,870 |
| 7 | `terminology/core/ae.md` | 642 |
| 8 | `terminology/core/disposition.md` | 1,622 |
| 9 | `terminology/core/findings_about.md` | 11,879 |

---

## Bucket 36: `36_ct_specialized_micro_oncology_pk_is_cp.md`

**Description**: CT core: microbiology + oncology + PK + is_domain + cp

**Files**: 13 | **Words**: 162,034 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `terminology/core/microbiology_part1.md` | 2,382 |
| 2 | `terminology/core/microbiology_part2.md` | 13,878 |
| 3 | `terminology/core/microbiology_part3.md` | 15,178 |
| 4 | `terminology/core/oncology_part1.md` | 13,650 |
| 5 | `terminology/core/oncology_part2.md` | 7,520 |
| 6 | `terminology/core/pk_part1.md` | 14,830 |
| 7 | `terminology/core/pk_part2.md` | 12,843 |
| 8 | `terminology/core/pk_part3.md` | 12,069 |
| 9 | `terminology/core/pk_part4.md` | 1,883 |
| 10 | `terminology/core/is_domain_part1.md` | 7,073 |
| 11 | `terminology/core/is_domain_part2.md` | 38,934 |
| 12 | `terminology/core/cp_part1.md` | 10,489 |
| 13 | `terminology/core/cp_part2.md` | 11,305 |

---

## Bucket 37: `37_ct_misc_int_dm_sp_td_gf_oi_other.md`

**Description**: CT core: interventions + dm + special_purpose + trial_design + gf + oi + other_part1-5

**Files**: 11 | **Words**: 88,199 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `terminology/core/interventions.md` | 15,557 |
| 2 | `terminology/core/dm.md` | 809 |
| 3 | `terminology/core/special_purpose.md` | 161 |
| 4 | `terminology/core/trial_design.md` | 7,998 |
| 5 | `terminology/core/gf.md` | 2,616 |
| 6 | `terminology/core/oi.md` | 823 |
| 7 | `terminology/core/other_part1.md` | 14,408 |
| 8 | `terminology/core/other_part2.md` | 10,772 |
| 9 | `terminology/core/other_part3.md` | 16,097 |
| 10 | `terminology/core/other_part4.md` | 15,496 |
| 11 | `terminology/core/other_part5.md` | 3,462 |

---

## Bucket 38: `38_ct_questionnaires_part1_22.md`

**Description**: CT questionnaires part 1-22 (22 files)

**Files**: 22 | **Words**: 301,961 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `terminology/questionnaires/questionnaires_part1.md` | 10,915 |
| 2 | `terminology/questionnaires/questionnaires_part2.md` | 12,249 |
| 3 | `terminology/questionnaires/questionnaires_part3.md` | 14,151 |
| 4 | `terminology/questionnaires/questionnaires_part4.md` | 14,000 |
| 5 | `terminology/questionnaires/questionnaires_part5.md` | 13,857 |
| 6 | `terminology/questionnaires/questionnaires_part6.md` | 12,510 |
| 7 | `terminology/questionnaires/questionnaires_part7.md` | 11,463 |
| 8 | `terminology/questionnaires/questionnaires_part8.md` | 13,617 |
| 9 | `terminology/questionnaires/questionnaires_part9.md` | 8,931 |
| 10 | `terminology/questionnaires/questionnaires_part10.md` | 14,168 |
| 11 | `terminology/questionnaires/questionnaires_part11.md` | 13,516 |
| 12 | `terminology/questionnaires/questionnaires_part12.md` | 14,254 |
| 13 | `terminology/questionnaires/questionnaires_part13.md` | 13,253 |
| 14 | `terminology/questionnaires/questionnaires_part14.md` | 14,306 |
| 15 | `terminology/questionnaires/questionnaires_part15.md` | 14,585 |
| 16 | `terminology/questionnaires/questionnaires_part16.md` | 11,845 |
| 17 | `terminology/questionnaires/questionnaires_part17.md` | 9,932 |
| 18 | `terminology/questionnaires/questionnaires_part18.md` | 19,923 |
| 19 | `terminology/questionnaires/questionnaires_part19.md` | 22,562 |
| 20 | `terminology/questionnaires/questionnaires_part20.md` | 13,066 |
| 21 | `terminology/questionnaires/questionnaires_part21.md` | 14,633 |
| 22 | `terminology/questionnaires/questionnaires_part22.md` | 14,225 |

---

## Bucket 39: `39_ct_questionnaires_part23_43.md`

**Description**: CT questionnaires part 23-43 (21 files)

**Files**: 21 | **Words**: 291,878 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `terminology/questionnaires/questionnaires_part23.md` | 12,881 |
| 2 | `terminology/questionnaires/questionnaires_part24.md` | 14,344 |
| 3 | `terminology/questionnaires/questionnaires_part25.md` | 13,278 |
| 4 | `terminology/questionnaires/questionnaires_part26.md` | 14,544 |
| 5 | `terminology/questionnaires/questionnaires_part27.md` | 14,136 |
| 6 | `terminology/questionnaires/questionnaires_part28.md` | 14,366 |
| 7 | `terminology/questionnaires/questionnaires_part29.md` | 13,969 |
| 8 | `terminology/questionnaires/questionnaires_part30.md` | 16,467 |
| 9 | `terminology/questionnaires/questionnaires_part31.md` | 17,070 |
| 10 | `terminology/questionnaires/questionnaires_part32.md` | 15,890 |
| 11 | `terminology/questionnaires/questionnaires_part33.md` | 14,099 |
| 12 | `terminology/questionnaires/questionnaires_part34.md` | 15,370 |
| 13 | `terminology/questionnaires/questionnaires_part35.md` | 15,003 |
| 14 | `terminology/questionnaires/questionnaires_part36.md` | 15,007 |
| 15 | `terminology/questionnaires/questionnaires_part37.md` | 14,507 |
| 16 | `terminology/questionnaires/questionnaires_part38.md` | 15,078 |
| 17 | `terminology/questionnaires/questionnaires_part39.md` | 13,733 |
| 18 | `terminology/questionnaires/questionnaires_part40.md` | 12,846 |
| 19 | `terminology/questionnaires/questionnaires_part41.md` | 13,669 |
| 20 | `terminology/questionnaires/questionnaires_part42.md` | 13,788 |
| 21 | `terminology/questionnaires/questionnaires_part43.md` | 1,833 |

---

## Bucket 40: `40_ct_supplementary.md`

**Description**: CT supplementary (6 files)

**Files**: 6 | **Words**: 75,889 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `terminology/supplementary/supplementary_part1.md` | 13,284 |
| 2 | `terminology/supplementary/supplementary_part2.md` | 13,576 |
| 3 | `terminology/supplementary/supplementary_part3.md` | 14,762 |
| 4 | `terminology/supplementary/supplementary_part4.md` | 15,144 |
| 5 | `terminology/supplementary/supplementary_part5.md` | 14,834 |
| 6 | `terminology/supplementary/supplementary_part6.md` | 4,289 |

---

## Bucket 41: `41_variable_index.md`

**Description**: VARIABLE_INDEX.md 全集 (27K words)

**Files**: 1 | **Words**: 27,755 | **Domains**: 0 | **Req vars covered**: 0

**Files list**:

| # | File (relative to knowledge_base/) | Words |
|---|------------------------------------|-------|
| 1 | `VARIABLE_INDEX.md` | 27,755 |

---

## Bucket 42: `42_req_variable_coverage_audit.md`

**Description**: 元 source: Req 变量全覆盖审计元信息 (A4 产物写入)

**Files**: 0 | **Words**: 0 | **Domains**: 0 | **Req vars covered**: 0

> **Auto-generated bucket** — 不从 knowledge_base 合并, 由其他 pipeline 产物填充.

## Global Coverage Summary

- **File coverage**: 295 / 295 (✅ FULL)
- **Domain coverage**: 63 / 63 (✅ FULL)
- **Req variable coverage**: 176 / 176 (✅ FULL ∅ gap)
