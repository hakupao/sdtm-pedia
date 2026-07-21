# Stage v2.6 — terminology tail rebalance (core+supp uncovered)

> Completed: 2026-04-20T01:30:55Z
> Batch script: extract_terminology_terms.py --tier tail

## Inputs
- stage: `v2.6` (batch 6)
- expected output file: `13a_terminology_tail_core.md`
- target cumulative tokens: 1,500,000

## Batch script result
- extract_terminology_terms.py OK, produced 13a_terminology_tail_core.md.

## Token tally (output_v2/*.md)
- files: 32
- total tokens: 1,336,360

| file | tokens |
|------|-------:|
| 00_routing.md | 2,657 |
| 01_index.md | 1,562 |
| 02_chapters.md | 60,716 |
| 03_model.md | 17,689 |
| 04_variable_index.md | 14,938 |
| 05_mega_spec.md | 65,993 |
| 06_assumptions.md | 17,509 |
| 07_examples_catalog.md | 4,295 |
| 08_terminology_map.md | 20,536 |
| 09_examples_data_high.md | 112,697 |
| 10_examples_data_others.md | 48,897 |
| 11a_terminology_high_core.md | 68,559 |
| 11b_terminology_high_questionnaires.md | 256,336 |
| 11c_terminology_high_supp.md | 26,857 |
| 12a_terminology_mid_core.md | 129,963 |
| 12b_terminology_mid_questionnaires.md | 224,659 |
| 12c_terminology_mid_supp.md | 23,317 |
| 13a_terminology_tail_core.md | 145,787 |
| 13c_terminology_tail_supp.md | 43,194 |
| CHECKPOINT_V2.1_HANDOFF.md | 3,796 |
| CHECKPOINT_V2.2_HANDOFF.md | 2,623 |
| CHECKPOINT_V2.3_HANDOFF.md | 2,558 |
| CHECKPOINT_V2.4_HANDOFF.md | 3,918 |
| CHECKPOINT_V2.5_HANDOFF.md | 5,276 |
| STAGE_V2.1_AB_REPORT.md | 5,671 |
| STAGE_V2.2_AB_REPORT.md | 3,290 |
| STAGE_V2.3_AB_REPORT.md | 5,145 |
| STAGE_V2.4_AB_REPORT.md | 4,673 |
| rag_decay_curve.md | 3,135 |
| system_prompt_v2.md | 3,002 |
| test_results_v2.md | 6,710 |
| upload_manifest_v2.md | 402 |

## Meta updates
- system_prompt_v2.md: appended
- upload_manifest_v2.md: appended

## Next
- 参照 PLAN_V2.md 对应 checkpoint 决定是否进入下一阶段.
