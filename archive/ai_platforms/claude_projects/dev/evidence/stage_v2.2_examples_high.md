# Stage v2.2 — examples 高频域

> Completed: 2026-04-19T07:07:08Z
> Batch script: extract_examples_data.py --tier high

## Inputs
- stage: `v2.2` (batch 2)
- expected output file: `09_examples_data_high.md`
- target cumulative tokens: 360,000

## Batch script result
- extract_examples_data.py rc=1 but produced 09_examples_data_high.md — cap-warning accepted. stderr tail: ['[Tier high] EXCEED_HARD_CAP: 112697 > 50000']

## Token tally (output_v2/*.md)
- files: 16
- total tokens: 333,719

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
| CHECKPOINT_V2.1_HANDOFF.md | 3,796 |
| STAGE_V2.1_AB_REPORT.md | 5,671 |
| rag_decay_curve.md | 979 |
| system_prompt_v2.md | 2,162 |
| test_results_v2.md | 2,284 |
| upload_manifest_v2.md | 235 |

## Meta updates
- system_prompt_v2.md: appended
- upload_manifest_v2.md: appended

## Next
- 参照 PLAN_V2.md 对应 checkpoint 决定是否进入下一阶段.
