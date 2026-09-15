# DM1 Step 0 Attempt 1 — 失败归档 (基线命令漏 --structured-lookup)

> 2026-09-15 13:46. CDISC v3 140 题跑出 80.0%, 与历史基线 95.71% 不符.
> 技术判定: FAIL (命令与生产配置不等价) · 业务判定: 作废, 不作基线.

## 1. 输入
`eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid` (缺 `--structured-lookup`)
## 2. 产物
`evidence/failures/dm1_step0_attempt1_no_s1_flag.json` (保留, 可作 S1 关闭时的对照)
## 3. 原因
run_eval 的 S1 是显式开关, 生产 settings.structured_lookup_enabled=True; 历史命令见 `evidence/checkpoints/cdisc_gold_section_granularity.md`.
## 4. 对下一 attempt 的输入
PLAN §5 命令已补 `--structured-lookup`; attempt 2 复跑.
