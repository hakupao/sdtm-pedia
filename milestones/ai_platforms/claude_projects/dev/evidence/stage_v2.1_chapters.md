# Stage v2.1 — chapters 全展开

> Completed: 2026-04-18T13:32:01Z
> Batch script: rebuild_chapters_full.py 

## Inputs
- stage: `v2.1` (batch 1)
- expected output file: `02_chapters.md`
- target cumulative tokens: 270,000

## Batch script result
- rebuild_chapters_full.py OK, produced 02_chapters.md.

## Token tally (output_v2/*.md)
- files: 13
- total tokens: 209,620

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
| rag_decay_curve.md | 451 |
| system_prompt_v2.md | 2,140 |
| test_results_v2.md | 899 |
| upload_manifest_v2.md | 235 |

## Meta updates
- system_prompt_v2.md: replaced
- upload_manifest_v2.md: skipped

## Next
- 参照 PLAN_V2.md 对应 checkpoint 决定是否进入下一阶段.
