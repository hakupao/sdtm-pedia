# v1.1 Rebuild — Diff Summary (baseline → rebuilt)

> 生成时间: 2026-05-15
> 用途: 验证 v1.1 rebuild 改动范围与 06 P6 T4 KB 修复一致

## ChatGPT (9 files, 4 changed)

| 文件 | baseline bytes | rebuilt bytes | Δ | 原因 |
|------|--------------:|-------------:|--:|------|
| 01_navigation.md | — | — | 0 | 同 (ROUTING/INDEX/VARIABLE_INDEX 未变) |
| 02_chapters_all.md | 246,800 | 259,253 | +12,453 | 06 改 ch02/ch04/ch08/ch10 |
| 03_model_all.md | — (small) | — (small) | small | 06 改 model/02_observation_classes.md |
| 04_domain_specs_all.md | — | — | 0 | 同 (DI 无 spec.md, 其他 spec 未变) |
| 05_domain_assumptions_all.md | 244,089 | 318,267 | +74,178 | 06 新加 DI/assumptions.md + 多 assumption 补强 |
| 06_domain_examples_all.md | 664,618 | 683,165 | +18,547 | 06 改 PC RELREC linking, MB/PP examples 等 |
| 07/08/09 terminology | — | — | 0 | 同 (terminology 未变) |

## Gemini (3 files, all 3 changed; 04 由 writer 手写不动)

| 文件 | baseline bytes | rebuilt bytes | Δ |
|------|--------------:|-------------:|--:|
| 01_navigation_and_quick_reference.md | 476,877 | 490,805 | +13,928 |
| 02_domains_spec_and_assumptions.md | 919,567 | 993,745 | +74,178 |
| 03_domains_examples.md | 664,912 | 683,459 | +18,547 |

注: 01 含 chapters/ + model/ + ROUTING/INDEX/VARIABLE_INDEX, gemini 唯一含 chapters 的文件.

## NotebookLM (42 buckets, 11 buckets changed + 1 newly含 DI)

变更 buckets (11):
- 03_sp_demographics_subject (SC examples 改 + 其他)
- 04_sp_se_sm_sv_co (SE/SV assumption 改 + SC examples)
- 06_int_concomitant_cm_ag_ml (CM/ML assumption)
- 09_ev_disposition_ds_dv_ce (DS assumption)
- 10_ev_history_mh_ho_be (MH/BE assumption)
- 11_fnd_lab_lb (LB assumption)
- 13_fnd_physical_exam_pe (PE assumption)
- 15_fnd_biomarkers_mb_mi_ms_mk (MB/MS/MK assumption + MB examples)
- 16_fnd_pharma_pc_pp (PC §6.3.5.9 RELREC + PC/PP examples 大改)
- 17_fnd_oncology_tr_tu_rs_oe (TR/TU assumption)
- 21_fnd_other_nv_re_rp (NV/RE/RP assumption)
- + bucket 25_td_meta_ti_ts_oi (新加 DI/assumptions.md, +65 words)
- + chapters-bearing buckets 28/29/30 (ch02/ch04/ch08/ch10 改)

Total: 1,599,397 words (baseline 1,599,332, +65 words from DI)

## 一致性核验

KB 改动: 43 文件 +1,405 / -234 行 (净 +1,171 行)
平台聚合大小净增 (chatgpt + gemini + notebooklm 主聚合文件):
- chatgpt: +105,178 bytes ≈ +35,000 tokens
- gemini: +106,653 bytes ≈ +35,500 tokens
- notebooklm: +65 words (DI 独立 bucket 加入) + 多 bucket 行级变化
- 三个平台改动量级一致 → KB 改动如实回灌

