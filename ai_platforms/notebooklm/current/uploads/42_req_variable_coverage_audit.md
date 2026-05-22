# 42_req_variable_coverage_audit

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `42`
> - **Concept**: 元 source: Req 变量全覆盖审计 (A4 产物 + 176 Req 变量全名单)
> - **Merged files**: 0
> - **Words**: 4,833
> - **Chars**: 24,612
> - **Auto source**: `req_coverage_audit` (merge_sources.py 合并 dev/evidence/req_vars_coverage_audit.md + dev/evidence/req_vars_full_set.md (前者给结构自证, 后者给完整 Req 名单作 NotebookLM RAG 召回锚). 不从 knowledge_base 合并.)

---
## Part A — Req 变量覆盖审计 (结构级 ∅ gap 自证)

> **产出日期**: 2026-04-21
> **执行脚本**: `dev/scripts/cluster_req_variables.py`
> **基线**: `dev/evidence/req_vars_full_set.md` (176 独立 Req 变量)
> **Bucket config**: `dev/scripts/bucket_config.json` (42 bucket, v1 initial)

## 断言 (H2 fix: 蕴含式, 非集合等式)

- **PASS condition**: `∀ req ∈ req_vars_full_set, ∃ bucket ∈ uploads, 使 req.variable ∈ bucket.covered_req_set`
- **FAIL condition**: `∃ req ∈ full_set, ∀ bucket, req.variable ∉ bucket.covered_req_set` (即漏集)

## ✅ PASS — 零漏集 (∅ gap)

**结构级 Q1 红线自证**: 176 独立 Req 变量全部被 42 bucket 覆盖.

- 通用 Req (9 vars) 全在 Section 一, 所有域范围, bucket 08/09/10/11+ 覆盖
- 领域专属 Req (167 vars) 按 63 domains 分布, 每 domain 全 3 files (spec+assumptions+examples) 都在某 bucket

## Domain coverage detail

| Domain | In bucket | Req count |
|--------|-----------|-----------|
| AE | `08_ev_adverse_ae.md` | 6 |
| AG | `06_int_concomitant_cm_ag_ml.md` | 5 |
| BE | `10_ev_history_mh_ho_be.md` | 5 |
| BS | `19_fnd_morphology_bs_cp_cv.md` | 6 |
| CE | `09_ev_disposition_ds_dv_ce.md` | 5 |
| CM | `06_int_concomitant_cm_ag_ml.md` | 5 |
| CO | `04_sp_se_sm_sv_co.md` | 6 |
| CP | `19_fnd_morphology_bs_cp_cv.md` | 6 |
| CV | `19_fnd_morphology_bs_cp_cv.md` | 6 |
| DA | `18_fnd_device_da_dd_gf_is.md` | 6 |
| DD | `18_fnd_device_da_dd_gf_is.md` | 6 |
| DM | `03_sp_demographics_subject.md` | 7 |
| DS | `09_ev_disposition_ds_dv_ce.md` | 6 |
| DV | `09_ev_disposition_ds_dv_ce.md` | 5 |
| EC | `05_int_exposure_ex_ec.md` | 5 |
| EG | `12_fnd_vitals_vs_eg.md` | 6 |
| EX | `05_int_exposure_ex_ec.md` | 5 |
| FA | `20_fnd_about_fa_sr.md` | 7 |
| FT | `22_fnd_other_ss_ur_ft.md` | 7 |
| GF | `18_fnd_device_da_dd_gf_is.md` | 6 |
| HO | `10_ev_history_mh_ho_be.md` | 5 |
| IE | `14_fnd_questionnaire_qs_ie.md` | 9 |
| IS | `18_fnd_device_da_dd_gf_is.md` | 6 |
| LB | `11_fnd_lab_lb.md` | 6 |
| MB | `15_fnd_biomarkers_mb_mi_ms_mk.md` | 6 |
| MH | `10_ev_history_mh_ho_be.md` | 5 |
| MI | `15_fnd_biomarkers_mb_mi_ms_mk.md` | 7 |
| MK | `15_fnd_biomarkers_mb_mi_ms_mk.md` | 6 |
| ML | `06_int_concomitant_cm_ag_ml.md` | 5 |
| MS | `15_fnd_biomarkers_mb_mi_ms_mk.md` | 6 |
| NV | `21_fnd_other_nv_re_rp.md` | 6 |
| OE | `17_fnd_oncology_tr_tu_rs_oe.md` | 6 |
| OI | `25_td_meta_ti_ts_oi.md` | 6 |
| PC | `16_fnd_pharma_pc_pp.md` | 6 |
| PE | `13_fnd_physical_exam_pe.md` | 6 |
| PP | `16_fnd_pharma_pc_pp.md` | 6 |
| PR | `07_int_procedures_pr_su.md` | 5 |
| QS | `14_fnd_questionnaire_qs_ie.md` | 7 |
| RE | `21_fnd_other_nv_re_rp.md` | 6 |
| RELREC | `26_rel_relrec_relspec_relsub.md` | 4 |
| RELSPEC | `26_rel_relrec_relspec_relsub.md` | 4 |
| RELSUB | `26_rel_relrec_relspec_relsub.md` | 4 |
| RP | `21_fnd_other_nv_re_rp.md` | 6 |
| RS | `17_fnd_oncology_tr_tu_rs_oe.md` | 6 |
| SC | `03_sp_demographics_subject.md` | 6 |
| SE | `04_sp_se_sm_sv_co.md` | 6 |
| SM | `04_sp_se_sm_sv_co.md` | 5 |
| SR | `20_fnd_about_fa_sr.md` | 7 |
| SS | `22_fnd_other_ss_ur_ft.md` | 6 |
| SU | `07_int_procedures_pr_su.md` | 5 |
| SUPPQUAL | `27_rel_suppqual.md` | 7 |
| SV | `04_sp_se_sm_sv_co.md` | 3 |
| TA | `23_td_arms_ta_tv.md` | 3 |
| TD | `24_td_elements_te_tm_td.md` | 9 |
| TE | `24_td_elements_te_tm_td.md` | 4 |
| TI | `25_td_meta_ti_ts_oi.md` | 5 |
| TM | `24_td_elements_te_tm_td.md` | 5 |
| TR | `17_fnd_oncology_tr_tu_rs_oe.md` | 6 |
| TS | `25_td_meta_ti_ts_oi.md` | 5 |
| TU | `17_fnd_oncology_tr_tu_rs_oe.md` | 6 |
| TV | `23_td_arms_ta_tv.md` | 3 |
| UR | `22_fnd_other_ss_ur_ft.md` | 6 |
| VS | `12_fnd_vitals_vs_eg.md` | 6 |

## 下游 hook

- **Phase 3 P3.4.5 (M1 fix, 语义级自证)**: 本结构级自证 PASS 后, Phase 3 对 10 个随机 Req 变量做**业务问答**测试, 验证 NotebookLM RAG 能语义召回这些变量, 非仅结构级 ∈.
- **Rule A 触发说明**: 压缩率 ~83% (295→42 files), 必 N=10 抽检. 本步仅结构抽样, 语义抽检 Phase 3 P3.4.5 执行.


---

## Part B — Req 变量全集清单 (176 独立变量, 9 通用 + 167 领域专属)

> **产出日期**: 2026-04-21
> **执行脚本**: `dev/scripts/extract_req_vars.py`
> **源文件**: `knowledge_base/VARIABLE_INDEX.md`
> **目的**: 权威清单, 供 A3 cluster bucket 设计 + A4 结构级覆盖断言 + P3.4.5 语义级抽检 使用

## 统计

| 指标 | 数 |
|------|-----|
| 通用 Req 变量 (出现在 2+ 域) | **9** |
| 领域专属 Req 变量记录 (by domain) | **167** |
| **Req 记录总数** (通用 + 领域专属) | **176** |
| **去重独立 Req 变量名数** | **176** |

> **说明**: 去重独立变量数计的是唯一变量名集合基数. 通用变量在 N 个域出现仍记 1 个独立变量;
> 领域专属变量若同名在多域出现也只记 1 个独立变量 (如 `--SEQ` pattern 但 VARIABLE_INDEX 按域列)

---

## 一、通用 Req 变量 (出现在 2+ 域) — 9 个

| 变量名 | Core | Label | Type | Role | 出现的域 |
|--------|------|-------|------|------|---------|
| DOMAIN | Req | Domain Abbreviation | Char | Identifier | 除 RELREC, RELSPEC, RELSUB, SUPPQUAL 外所有域 |
| ETCD | Req | Element Code | Char | Topic* | SE, TA, TE |
| IECAT | Req | Inclusion/Exclusion Category | Char | Grouping Qualifier | IE, TI |
| IETEST | Req | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | IE, TI |
| IETESTCD | Req | Inclusion/Exclusion Criterion Short Name | Char | Topic | IE, TI |
| MIDSTYPE | Req | Disease Milestone Type | Char | Record Qualifier* | SM, TM |
| RDOMAIN | Req* | Related Domain Abbreviation | Char | Record Qualifier* | CO, RELREC, SUPPQUAL |
| STUDYID | Req | Study Identifier | Char | Identifier | 所有域 |
| USUBJID | Req* | Unique Subject Identifier | Char | Identifier | 除 OI, TA, TD, TE, TI, TM, TS, TV 外所有域 |

---

## 二、领域专属 Req 变量 (by domain) — 60 域 × 平均 ~2.8 Req/域

### AE (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| AEDECOD | Req | Dictionary-Derived Term | Char | Synonym Qualifier | MedDRA |
| AESEQ | Req | Sequence Number | Num | Identifier | — |
| AETERM | Req | Reported Term for the Adverse Event | Char | Topic | — |

### AG (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| AGSEQ | Req | Sequence Number | Num | Identifier | — |
| AGTRT | Req | Reported Agent Name | Char | Topic | — |

### BE (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| BESEQ | Req | Sequence Number | Num | Identifier | — |
| BETERM | Req | Reported Term for the Biospecimen Event | Char | Topic | — |

### BS (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| BSSEQ | Req | Sequence Number | Num | Identifier | — |
| BSTEST | Req | Biospecimen Test Name | Char | Synonym Qualifier | C124299 |
| BSTESTCD | Req | Biospecimen Test Short Name | Char | Topic | C124300 |

### CE (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| CESEQ | Req | Sequence Number | Num | Identifier | — |
| CETERM | Req | Reported Term for the Clinical Event | Char | Topic | — |

### CM (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| CMSEQ | Req | Sequence Number | Num | Identifier | — |
| CMTRT | Req | Reported Name of Drug, Med, or Therapy | Char | Topic | — |

### CO (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| COSEQ | Req | Sequence Number | Num | Identifier | — |
| COVAL | Req | Comment | Char | Topic | — |

### CP (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| CPSEQ | Req | Sequence Number | Num | Identifier | — |
| CPTEST | Req | Name of Measurement, Test or Examination | Char | Synonym Qualifier | C181174 |
| CPTESTCD | Req | Test or Examination Short Name | Char | Topic | C181173 |

### CV (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| CVSEQ | Req | Sequence Number | Num | Identifier | — |
| CVTEST | Req | Name of Cardiovascular Test | Char | Synonym Qualifier | C101846 |
| CVTESTCD | Req | Short Name of Cardiovascular Test | Char | Topic | C101847 |

### DA (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| DASEQ | Req | Sequence Number | Num | Identifier | — |
| DATEST | Req | Name of Accountability Assessment | Char | Synonym Qualifier | C78731 |
| DATESTCD | Req | Short Name of Accountability Assessment | Char | Topic | C78732 |

### DD (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| DDSEQ | Req | Sequence Number | Num | Identifier | — |
| DDTEST | Req | Death Detail Assessment Name | Char | Synonym Qualifier | C116107 |
| DDTESTCD | Req | Death Detail Assessment Short Name | Char | Topic | C116108 |

### DM (4 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| COUNTRY | Req | Country | Char | Record Qualifier | — |
| SEX | Req | Sex | Char | Record Qualifier | C66731 |
| SITEID | Req | Study Site Identifier | Char | Record Qualifier | — |
| SUBJID | Req | Subject Identifier for the Study | Char | Topic | — |

### DS (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| DSDECOD | Req | Standardized Disposition Term | Char | Synonym Qualifier | C66727; C114118; C150811 |
| DSSEQ | Req | Sequence Number | Num | Identifier | — |
| DSTERM | Req | Reported Term for the Disposition Event | Char | Topic | — |

### DV (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| DVSEQ | Req | Sequence Number | Num | Identifier | — |
| DVTERM | Req | Protocol Deviation Term | Char | Topic | — |

### EC (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| ECSEQ | Req | Sequence Number | Num | Identifier | — |
| ECTRT | Req | Name of Treatment | Char | Topic | — |

### EG (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| EGSEQ | Req | Sequence Number | Num | Identifier | — |
| EGTEST | Req | ECG Test or Examination Name | Char | Synonym Qualifier | C71152; C120524 |
| EGTESTCD | Req | ECG Test or Examination Short Name | Char | Topic | C71153; C120523 |

### EX (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| EXSEQ | Req | Sequence Number | Num | Identifier | — |
| EXTRT | Req | Name of Treatment | Char | Topic | — |

### FA (4 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| FAOBJ | Req | Object of the Observation | Char | Record Qualifier | — |
| FASEQ | Req | Sequence Number | Num | Identifier | — |
| FATEST | Req | Findings About Test Name | Char | Synonym Qualifier | C101833 |
| FATESTCD | Req | Findings About Test Short Name | Char | Topic | C101832 |

### FT (4 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| FTCAT | Req | Category | Char | Grouping Qualifier | C115304 |
| FTSEQ | Req | Sequence Number | Num | Identifier | — |
| FTTEST | Req | Name of Test | Char | Synonym Qualifier | — |
| FTTESTCD | Req | Short Name of Test | Char | Topic | — |

### GF (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| GFSEQ | Req | Sequence Number | Num | Identifier | — |
| GFTEST | Req | Name of Genomic Measurement | Char | Synonym Qualifier | C181179 |
| GFTESTCD | Req | Short Name of Genomic Measurement | Char | Topic | C181178 |

### HO (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| HOSEQ | Req | Sequence Number | Num | Identifier | — |
| HOTERM | Req | Healthcare Encounter Term | Char | Topic | — |

### IE (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| IEORRES | Req | I/E Criterion Original Result | Char | Result Qualifier | C66742 |
| IESEQ | Req | Sequence Number | Num | Identifier | — |
| IESTRESC | Req | I/E Criterion Result in Std Format | Char | Result Qualifier | C66742 |

### IS (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| ISSEQ | Req | Sequence Number | Num | Identifier | — |
| ISTEST | Req | Immunogenicity Test or Examination Name | Char | Synonym Qualifier | C120526 |
| ISTESTCD | Req | Immunogenicity Test/Exam Short Name | Char | Topic | C120525 |

### LB (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| LBSEQ | Req | Sequence Number | Num | Identifier | — |
| LBTEST | Req | Lab Test or Examination Name | Char | Synonym Qualifier | C67154 |
| LBTESTCD | Req | Lab Test or Examination Short Name | Char | Topic | C65047 |

### MB (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| MBSEQ | Req | Sequence Number | Num | Identifier | — |
| MBTEST | Req | Microbiology Test or Finding Name | Char | Synonym Qualifier | C120528 |
| MBTESTCD | Req | Microbiology Test or Finding Short Name | Char | Topic | C120527 |

### MH (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| MHSEQ | Req | Sequence Number | Num | Identifier | — |
| MHTERM | Req | Reported Term for the Medical History | Char | Topic | — |

### MI (4 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| MISEQ | Req | Sequence Number | Num | Identifier | — |
| MISPEC | Req | Specimen Material Type | Char | Record Qualifier | C78734 |
| MITEST | Req | Microscopic Examination Name | Char | Synonym Qualifier | C132262 |
| MITESTCD | Req | Microscopic Examination Short Name | Char | Topic | C132263 |

### MK (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| MKSEQ | Req | Sequence Number | Num | Identifier | — |
| MKTEST | Req | Name of Musculoskeletal Test | Char | Synonym Qualifier | C127270 |
| MKTESTCD | Req | Short Name of Musculoskeletal Test | Char | Topic | C127269 |

### ML (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| MLSEQ | Req | Sequence Number | Num | Identifier | — |
| MLTRT | Req | Name of Meal | Char | Topic | — |

### MS (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| MSSEQ | Req | Sequence Number | Num | Identifier | — |
| MSTEST | Req | Name of Assessment | Char | Synonym Qualifier | C128687 |
| MSTESTCD | Req | Short Name of Assessment | Char | Topic | C128688 |

### NV (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| NVSEQ | Req | Sequence Number | Num | Identifier | — |
| NVTEST | Req | Name of Nervous System Test | Char | Synonym Qualifier | C116103 |
| NVTESTCD | Req | Short Name of Nervous System Test | Char | Topic | C116104 |

### OE (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| OESEQ | Req | Sequence Number | Num | Identifier | — |
| OETEST | Req | Name of Ophthalmic Test or Exam | Char | Synonym Qualifier | C117742 |
| OETESTCD | Req | Short Name of Ophthalmic Test or Exam | Char | Topic | C117743 |

### OI (4 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| OIPARM | Req | Non-host Organism ID Element Name | Char | Synonym Qualifier | C179590 |
| OIPARMCD | Req | Non-host Organism ID Element Short Name | Char | Topic | C179591 |
| OISEQ | Req | Sequence Number | Num | Identifier | — |
| OIVAL | Req | Non-host Organism ID Element Value | Char | Result Qualifier | — |

### PC (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| PCSEQ | Req | Sequence Number | Num | Identifier | — |
| PCTEST | Req | Pharmacokinetic Test Name | Char | Synonym Qualifier | — |
| PCTESTCD | Req | Pharmacokinetic Test Short Name | Char | Topic | — |

### PE (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| PESEQ | Req | Sequence Number | Num | Identifier | — |
| PETEST | Req | Body System Examined | Char | Synonym Qualifier | — |
| PETESTCD | Req | Body System Examined Short Name | Char | Topic | — |

### PP (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| PPSEQ | Req | Sequence Number | Num | Identifier | — |
| PPTEST | Req | Parameter Name | Char | Synonym Qualifier | C85493 |
| PPTESTCD | Req | Parameter Short Name | Char | Topic | C85839 |

### PR (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| PRSEQ | Req | Sequence Number | Num | Identifier | — |
| PRTRT | Req | Reported Name of Procedure | Char | Topic | — |

### QS (4 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| QSCAT | Req | Category of Question | Char | Grouping Qualifier | C100129 |
| QSSEQ | Req | Sequence Number | Num | Identifier | — |
| QSTEST | Req | Question Name | Char | Synonym Qualifier | — |
| QSTESTCD | Req | Question Short Name | Char | Topic | — |

### RE (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| RESEQ | Req | Sequence Number | Num | Identifier | — |
| RETEST | Req | Name of Respiratory Test | Char | Synonym Qualifier | C111107 |
| RETESTCD | Req | Short Name of Respiratory Test | Char | Topic | C111106 |

### RELREC (1 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| RELID | Req | Relationship Identifier | Char | Record Qualifier | — |

### RELSPEC (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| LEVEL | Req | Specimen Level | Num | Variable Qualifier | — |
| REFID | Req | Specimen ID | Char | Identifier | — |

### RELSUB (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| RSUBJID | Req | Related Subject or Pool Identifier | Char | Identifier | — |
| SREL | Req | Subject Relationship | Char | Record Qualifier | C100130 |

### RP (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| RPSEQ | Req | Sequence Number | Num | Identifier | — |
| RPTEST | Req | Name of Reproductive Test | Char | Synonym Qualifier | C106478 |
| RPTESTCD | Req | Short Name of Reproductive Test | Char | Topic | C106479 |

### RS (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| RSSEQ | Req | Sequence Number | Num | Identifier | — |
| RSTEST | Req | Assessment Name | Char | Synonym Qualifier | C96781 |
| RSTESTCD | Req | Assessment Short Name | Char | Topic | C96782 |

### SC (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| SCSEQ | Req | Sequence Number | Num | Identifier | — |
| SCTEST | Req | Subject Characteristic | Char | Synonym Qualifier | C103330 |
| SCTESTCD | Req | Subject Characteristic Short Name | Char | Topic | C74559 |

### SE (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| SESEQ | Req | Sequence Number | Num | Identifier | — |
| SESTDTC | Req | Start Date/Time of Element | Char | Timing | ISO 8601 datetime or interval |

### SM (1 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| SMSEQ | Req | Sequence Number | Num | Identifier | — |

### SR (4 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| SROBJ | Req | Object of the Observation | Char | Record Qualifier | — |
| SRSEQ | Req | Sequence Number | Num | Identifier | — |
| SRTEST | Req | Skin Response Test or Examination Name | Char | Synonym Qualifier | C112023 |
| SRTESTCD | Req | Skin Response Test or Exam Short Name | Char | Topic | C112024 |

### SS (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| SSSEQ | Req | Sequence Number | Num | Identifier | — |
| SSTEST | Req | Status Name | Char | Synonym Qualifier | C124306 |
| SSTESTCD | Req | Status Short Name | Char | Topic | C124305 |

### SU (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| SUSEQ | Req | Sequence Number | Num | Identifier | — |
| SUTRT | Req | Reported Name of Substance | Char | Topic | — |

### SUPPQUAL (4 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| QLABEL | Req | Qualifier Variable Label | Char | Synonym Qualifier | — |
| QNAM | Req | Qualifier Variable Name | Char | Topic | — |
| QORIG | Req | Origin | Char | Record Qualifier | — |
| QVAL | Req | Data Value | Char | Result Qualifier | — |

### TD (7 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| TDANCVAR | Req | Anchor Variable Name | Char | Timing | — |
| TDMAXPAI | Req | Planned Assessment Interval Maximum | Char | Timing | ISO 8601 duration |
| TDMINPAI | Req | Planned Assessment Interval Minimum | Char | Timing | ISO 8601 duration |
| TDNUMRPT | Req | Maximum Number of Actual Assessments | Num | Record Qualifier | — |
| TDORDER | Req | Sequence of Planned Assessment Schedule | Num | Timing | — |
| TDSTOFF | Req | Offset from the Anchor | Char | Timing | ISO 8601 duration |
| TDTGTPAI | Req | Planned Assessment Interval | Char | Timing | ISO 8601 duration |

### TE (1 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| TESTRL | Req | Rule for Start of Element | Char | Rule | — |

### TM (2 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| TMDEF | Req | Disease Milestone Definition | Char | Variable Qualifier | — |
| TMRPT | Req | Disease Milestone Repetition Indicator | Char | Record Qualifier | C66742 |

### TR (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| TRSEQ | Req | Sequence Number | Num | Identifier | — |
| TRTEST | Req | Tumor/Lesion Assessment Test Name | Char | Synonym Qualifier | C96778 |
| TRTESTCD | Req | Tumor/Lesion Assessment Short Name | Char | Topic | C96779 |

### TS (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| TSPARM | Req | Trial Summary Parameter | Char | Synonym Qualifier | C67152 |
| TSPARMCD | Req | Trial Summary Parameter Short Name | Char | Topic | C66738 |
| TSSEQ | Req | Sequence Number | Num | Identifier | — |

### TU (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| TUSEQ | Req | Sequence Number | Num | Identifier | — |
| TUTEST | Req | Tumor/Lesion ID Test Name | Char | Synonym Qualifier | C96783 |
| TUTESTCD | Req | Tumor/Lesion ID Short Name | Char | Topic | C96784 |

### TV (1 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| TVSTRL | Req | Visit Start Rule | Char | Rule | — |

### UR (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| URSEQ | Req | Sequence Number | Num | Identifier | — |
| URTEST | Req | Name of Urinary Test | Char | Synonym Qualifier | C129941 |
| URTESTCD | Req | Short Name of Urinary Test | Char | Topic | C129942 |

### VS (3 Req)

| 变量名 | Core | Label | Type | Role | CT |
|--------|------|-------|------|------|----|
| VSSEQ | Req | Sequence Number | Num | Identifier | — |
| VSTEST | Req | Vital Signs Test Name | Char | Synonym Qualifier | C67153 |
| VSTESTCD | Req | Vital Signs Test Short Name | Char | Topic | C66741 |

---

## 三、去重独立 Req 变量名全集 (A4 / P3.4.5 audit 基线)

以下清单按字典序排列, A4 / P3.4.5 按此全集做蕴含式覆盖断言 (∀ req ∈ full_set, ∃ source, ...).

```
AEDECOD
AESEQ
AETERM
AGSEQ
AGTRT
BESEQ
BETERM
BSSEQ
BSTEST
BSTESTCD
CESEQ
CETERM
CMSEQ
CMTRT
COSEQ
COUNTRY
COVAL
CPSEQ
CPTEST
CPTESTCD
CVSEQ
CVTEST
CVTESTCD
DASEQ
DATEST
DATESTCD
DDSEQ
DDTEST
DDTESTCD
DOMAIN
DSDECOD
DSSEQ
DSTERM
DVSEQ
DVTERM
ECSEQ
ECTRT
EGSEQ
EGTEST
EGTESTCD
ETCD
EXSEQ
EXTRT
FAOBJ
FASEQ
FATEST
FATESTCD
FTCAT
FTSEQ
FTTEST
FTTESTCD
GFSEQ
GFTEST
GFTESTCD
HOSEQ
HOTERM
IECAT
IEORRES
IESEQ
IESTRESC
IETEST
IETESTCD
ISSEQ
ISTEST
ISTESTCD
LBSEQ
LBTEST
LBTESTCD
LEVEL
MBSEQ
MBTEST
MBTESTCD
MHSEQ
MHTERM
MIDSTYPE
MISEQ
MISPEC
MITEST
MITESTCD
MKSEQ
MKTEST
MKTESTCD
MLSEQ
MLTRT
MSSEQ
MSTEST
MSTESTCD
NVSEQ
NVTEST
NVTESTCD
OESEQ
OETEST
OETESTCD
OIPARM
OIPARMCD
OISEQ
OIVAL
PCSEQ
PCTEST
PCTESTCD
PESEQ
PETEST
PETESTCD
PPSEQ
PPTEST
PPTESTCD
PRSEQ
PRTRT
QLABEL
QNAM
QORIG
QSCAT
QSSEQ
QSTEST
QSTESTCD
QVAL
RDOMAIN
REFID
RELID
RESEQ
RETEST
RETESTCD
RPSEQ
RPTEST
RPTESTCD
RSSEQ
RSTEST
RSTESTCD
RSUBJID
SCSEQ
SCTEST
SCTESTCD
SESEQ
SESTDTC
SEX
SITEID
SMSEQ
SREL
SROBJ
SRSEQ
SRTEST
SRTESTCD
SSSEQ
SSTEST
SSTESTCD
STUDYID
SUBJID
SUSEQ
SUTRT
TDANCVAR
TDMAXPAI
TDMINPAI
TDNUMRPT
TDORDER
TDSTOFF
TDTGTPAI
TESTRL
TMDEF
TMRPT
TRSEQ
TRTEST
TRTESTCD
TSPARM
TSPARMCD
TSSEQ
TUSEQ
TUTEST
TUTESTCD
TVSTRL
URSEQ
URTEST
URTESTCD
USUBJID
VSSEQ
VSTEST
VSTESTCD
```

---

*脚本执行结束. 独立 Req 变量 176 个. Q1 红线零丢失审计基线 established.*
