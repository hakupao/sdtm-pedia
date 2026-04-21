# Phase A A4: Req 变量覆盖审计 (蕴含式 ∅ gap 结构级自证)

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
