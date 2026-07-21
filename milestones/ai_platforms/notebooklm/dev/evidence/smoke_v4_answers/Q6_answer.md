# NotebookLM Q6 answer — PK --TPT 四件套

**Verdict**: PASS
**Citation count**: 6+ ([16_fnd_pharma_pc_pp.md] × 5 + [29_ig_ch04_general_assumptions.md] × 2)

## 变量表 (含 Role/Core/CT)

| Variable | Label | Type | Role | Core | CT | 填法示例 | Source |
|---|---|---|---|---|---|---|---|
| PCTPT | Planned Time Point Name | Char | Timing | Perm | — | "4h post" | [16_fnd_pharma_pc_pp.md] |
| PCTPTNUM | Planned Time Point Number | Num | Timing | Perm | — | 3 (ordinal: 15min=1, 1h=2, 4h=3) | [16_fnd_pharma_pc_pp.md] |
| PCTPTREF | Time Point Reference | Char | Timing | Perm | — | "PREVIOUS DOSE" 或 "PERIOD 1 DOSE" | [16_fnd_pharma_pc_pp.md] |
| PCELTM | Planned Elapsed Time | Char | Timing | Perm | ISO 8601 duration | "PT4H" | [16_fnd_pharma_pc_pp.md] |
| PCRFTDTC | Date/Time of Reference Point | Char | Timing | Perm | ISO 8601 datetime | "2023-10-01T08:00" | [16_fnd_pharma_pc_pp.md] |

## (a) PCTPT vs PCTPTNUM
- PCTPT = 文本描述 ("4h post")
- PCTPTNUM = 数值化版本, **唯一作用 aid in sorting** (因 "15 min"/"1h"/"4h" 文本无法按时间先后自然排列)

## (b) PCTPTREF
- Time Point Reference = 用于计算流逝时间的固定参考锚点描述名称 ("PREVIOUS DOSE" / "DAY 1 DOSE")
- 是确定 PCTPT/PCTPTNUM/PCELTM 的基础锚点

## (c) PCELTM 格式
**ISO 8601 duration** (非 clock time):
- 必须 P 开头, 时间成分用 T 分隔
- 4h → **PT4H**
- 15 min → PT15M

## (d) 两周期区分 (交叉/多周期, Crossover)
组合两种方式:
1. **VISITNUM / VISIT** 指定周期 (PERIOD 1 / PERIOD 2)
2. **PCTPTREF** 命名不同周期给药锚点 (PERIOD 1 DOSE / PERIOD 2 DOSE), 配合各自 PCRFTDTC 独立给药时间

## 评分要点
- ✓ 5 变量全填对 + Role/Core/CT 完整表
- ✓ 每变量 inline citation
- ✓ (a) sorting 目的清晰 + 排序反例说明
- ✓ (b) 零点锚点 + 3 变量依赖
- ✓ (c) PT4H + P/T 规则
- ✓ (d) VISIT + PCTPTREF 组合
- △ 无 PCTPTNUM 替代编码方案 (相对小时数 vs ordinal, Claude 两者都提, NBLM 只 ordinal)
- △ 无 Pre-dose 负号规则 ("-PT15M")
- △ 无完整示意表 (Claude 级 8 行)

## Carry-over
- F-1 小表渲染: 本答含 markdown 表格 (Variable table), UI 渲染正常 — 未触 F-1 漂移
- F-3 citation 分布: 大部分 [16_fnd_pharma_pc_pp.md] (PC specific), ch04 cross-ref 在 (c)(d) 用到 — citation 偏向 PC-specific file 而非 ch04, T2 题型偏向未显著改善
