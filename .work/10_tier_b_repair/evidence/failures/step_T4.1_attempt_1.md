# T4.1 总闸 attempt 1 — 不通过 (CONDITIONAL) 指针

<!-- chain: E (plans) -->
> 状态: CONDITIONAL, 等用户裁定 (2026-11-27). 本文件只做规则 B 的索引, 正文不复制.

- **输入**: 抽样脚本 `scripts/t4/t4_sample.py` (seed 20261127, 正式 72 + 补充 12); brief `subagent_prompts/t4_gate_reviewer_v1.0.md`; 全部 T0-T3 证据.
- **产物**: `evidence/checkpoints/t4_gate_review.md`; 审查原文 `evidence/t4_gate_raw/{pack1..4,evidence_layer}.md`; 样本包 `work/t4/gate_pack_{1..4}.md`.
- **技术判定**: 样本 84/84 HOLDS (样本层无失败).
- **业务判定**: 证据层不能 PASS — G-TB1/2 NOT_MET (残留 `ig34_p0056_a006` + 三类无用户 ack), G-TB3 字面 NOT_MET (strict 96.0741%; mapped 99.3578% 无用户认可).
- **下一 attempt 输入**: `evidence/checkpoints/t4_user_decisions.md` §00 U-1~U-5 的用户裁定 (+ U-2/U-8 的 ledger 改动, 走 writer→reviewer); 证据层建议的补强 (pre_existing 58、C7 38 条、FIG 11、C3 结案清单) 视 U-5. attempt 2 用同一审查角色的新实例.
