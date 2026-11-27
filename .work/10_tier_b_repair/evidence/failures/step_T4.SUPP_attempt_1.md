# T4.1 补检 attempt 1 — PRE_EXISTING 层不通过 (规则 B 归档)

<!-- chain: E (plans) -->
> 状态: **不通过, 已触发 Q9 升级; 待主人裁定后进入 attempt 2** (2026-11-27). 失败数据全部保留, 未删未改.

- **输入**: HEAD `d46f8af` 的 KB (树 `63f857774a42cfaa71798705ad40ab51bc5e378a`) 与台账 (md5 `60729f7b64b7c1dfaf2174e394f6dd9c`); 样本 `work/t4/supp/supp_sample.jsonl` (203 条, md5 `0fb5799b821c5a4dc900b39fbf86bf86`), 包 `work/t4/supp/supp_pack_{1..8}.md`; brief `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (判定口径与后果条款派发前写死).
- **产物**: 审查者 (`oh-my-claudecode:tracer` × 8) 原始结果 `evidence/t4_supp_raw/pack_{1..8}.md`; 汇总 `evidence/checkpoints/t4_supp_fullcheck.md`; 逐条机读 `work/t4/supp/verdicts.json`.
- **技术判定**: 203 条 = HOLDS 171 / HOLDS_AS_EQUIV 30 / **NOT_HOLD 2** / UNVERIFIABLE 0. NOT_HOLD = `sv20_p0069_a001`、`sv20_p0069_a003` (PRE_EXISTING 层, 旧 EXACT): SDTM v2.0 §6.6 APRELSUB 表 APID / RDEVID 行的 Notes 文字 KB 本表没有, 旧匹配器跨表配到 §4 AP 表. 其余 10 个非空层全部通过.
- **业务判定**: 按写死条款 "层通过 = NOT_HOLD 0 且 UNVERIFIABLE 0" → PRE_EXISTING 层**不通过**; "PRE_EXISTING 层 NOT_HOLD ≥ 1 → 触发 PLAN Q9 升级, 主控上报并另定扩检方案, 不自行结案". 不是 KB 内容错 (v2.0 变量表只收精简列 = T1.4 R1 已裁定), 是 06 旧标签错.
- **已做的后续 (同日)**: Q9 扩检 192 条 (`evidence/t4_q9_raw/pack_{1..8}.md`): SDTM v2.0 旧 EQUIVALENT 127 条全检 → 51 条不成立 (49 条同类变量表行 / 表头 + 2 条目录条目跨文档误配); SDTMIG 旧 EQUIVALENT 2207 条抽 65 条 → 0 错.
- **下一 attempt 输入** (都要主人先定, 见 `evidence/checkpoints/t4_owner_decisions_round2.md`): ① `t4_relabel_pending.md` 的 57 条改标是否按建议执行 (认 IE / 改 PDF_TYPO), 或选 "把列补进 KB"; ② SDTMIG 旧 EQUIVALENT 抽样是否够, 还是全检 2207 条; 定后走 writer (`oh-my-claudecode:executor`) → reviewer 改台账, 重跑 `t0_mutation_head.sh --make-baseline` + 变异、`t4_coverage_decomp.py`、`t4_ack_lists.py`, 再对改过的原子复审.
