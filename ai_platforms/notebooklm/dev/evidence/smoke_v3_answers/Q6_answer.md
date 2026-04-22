# Q6 (C1 — Timing 深化) PK 定时采血 --TPT 四件套

> Date: 2026-04-22 / Account: bojiang.zhang.0904@gmail.com / Fresh chat

---

## 题

某 PK 研究的访视日安排: 受试者上午 8:00 服用研究药物 (A-001), 之后 15 min / 1 h / 4 h / 8 h 各采一次血样用于 PK. 一周后再来同样做一次 (两周期). 请说明 PK 域 (PC 域) 里, 对"服药后 4 小时采血"那一条记录, 下列 5 个 Timing 变量应怎么填:

PCTPT / PCTPTNUM / PCTPTREF / PCELTM / PCRFTDTC

并解释: (a) PCTPT vs PCTPTNUM 关系; (b) PCTPTREF 指什么; (c) PCELTM 是 ISO 什么格式; (d) 同一受试者两周期记录用什么区分.

## NotebookLM 答 (full text)

在 PC (Pharmacokinetics Concentrations) 域中, 针对"第一周期服药 (上午 8:00) 后 4 小时采血"的这一条记录, 这 5 个 Timing 变量的填写示例如下 (假设第一周期给药日期为 YYYY-MM-DD) [16_fnd_pharma_pc_pp.md]:

- `PCTPT`: `4h post` (或方案中定义的等效文本, 如 `4 HOURS POST-DOSE`)
- `PCTPTNUM`: `4` (用于表明该点在采血序列中的逻辑顺序, 通常 15 min 为 1, 1 h 为 2, 4 h 为 3 或 4 等)
- `PCTPTREF`: `Day 1 Dose` (或 `PREVIOUS DOSE`, 定义此相对时间参照点的名称)
- `PCELTM`: `PT4H`
- `PCRFTDTC`: `YYYY-MM-DDT08:00` (受试者实际服药的参考时间点)

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| PCTPT | Char | Timing | Perm |  | [16_fnd_pharma_pc_pp.md] |
| PCTPTNUM | Num | Timing | Perm |  | [16_fnd_pharma_pc_pp.md] |
| PCTPTREF | Char | Timing | Perm |  | [16_fnd_pharma_pc_pp.md] |
| PCELTM | Char | Timing | Perm | ISO 8601 duration | [16_fnd_pharma_pc_pp.md] |
| PCRFTDTC | Char | Timing | Perm | ISO 8601 datetime or interval | [16_fnd_pharma_pc_pp.md] |

详细解释:

**(a) PCTPT vs PCTPTNUM 关系**: PCTPT (Planned Time Point Name) 是计划时间点的文本描述, 而 PCTPTNUM (Planned Time Point Number) 是其对应的数值版本, 专门用于排序 (Numerical version of PCTPT to aid in sorting) [16_fnd_pharma_pc_pp.md]。因为若单纯使用文本排序, "10 HOURS" 会被排在 "2 HOURS" 之前, 所以必须借助 PCTPTNUM 来保证时间点在数据集中能呈现正确的发生先后顺序 [29_ig_ch04_general_assumptions.md]。

**(b) PCTPTREF 指什么**: PCTPTREF (Time Point Reference) 描述的是一个固定的"参考时间点"的名称 [16_fnd_pharma_pc_pp.md]。它是 PCTPT、PCTPTNUM 以及 PCELTM 所依赖的"锚点"(例如在 PK 采血中通常指向 `PREVIOUS DOSE` 或 `Day 1 Dose` 等具体给药事件) [16, 29_ig_ch04_general_assumptions.md]。

**(c) PCELTM 是 ISO 什么格式**: PCELTM (Planned Elapsed Time from Time Point Ref) 必须使用 **ISO 8601 duration** 格式 [16_fnd_pharma_pc_pp.md]。根据规则, 表示持续时间的格式必须以字母 "P" 开头, 表示时间部分 (小时、分钟、秒) 之前必须加 "T" [29_ig_ch04_general_assumptions.md]。因此, 计划给药后 4 小时的流逝时间应严格写为 `PT4H` [16_fnd_pharma_pc_pp.md]。

**(d) 同一受试者两周期记录用什么区分**: 在包含多个给药周期的交叉试验中, 仅仅依靠时间点变量无法区分两周期的记录, 主要依靠以下两个维度进行区分:
- **访视变量 (VISIT / VISITNUM)**: 使用 VISITNUM 来指定受试者所处的不同周期 (例如 Period 1 对应一组 VISITNUM, Period 2 对应另一组) [29_ig_ch04_general_assumptions.md]。
- **参考点及基准时间 (PCTPTREF / PCRFTDTC)**: 在 PCTPTREF 中定义不同的周期锚点文本 (如第一周期为 `Day 1 Dose`, 第二周期为 `Day 8 Dose`), 并使用该周期实际的给药日期时间来填充 PCRFTDTC [16_fnd_pharma_pc_pp.md]。

通过 **VISITNUM + PCTPTREF + PCRFTDTC** 的组合, 即可唯一区分并锚定不同周期的同一相对时间点 [29_ig_ch04_general_assumptions.md]。

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| PCTPT 文字时间点 | "4 hours post dose" 类 | `4h post` / `4 HOURS POST-DOSE` | ✅ |
| PCTPTNUM 数值排序 | 数字 | `4` + 排序解释 (10h vs 2h 文本排序坑) | ✅ |
| PCTPTREF 锚点名 | "DOSE" / "PREVIOUS DOSE" 类名字 | `Day 1 Dose` / `PREVIOUS DOSE` | ✅ |
| PCELTM ISO 8601 duration | `PT4H` | `PT4H` + P/T 前缀解释 | ✅ |
| PCRFTDTC ISO datetime | 实际服药 datetime | `YYYY-MM-DDT08:00` | ✅ |
| (a) 文字 vs 数值排序关系 | 关系明确 | 文字描述 vs 数值排序, 含 10h/2h 排序坑解释 | ✅ |
| (b) PCTPTREF = name 不是 datetime | name | "固定的参考时间点的名称" 明文 | ✅ |
| (c) PCELTM ISO duration | duration P/PT | duration + PT4H + P/T 规则 | ✅ |
| (d) 两周期区分 (VISITNUM/EPOCH) | VISITNUM 或 EPOCH | `VISITNUM + PCTPTREF + PCRFTDTC` 三元 (Day 1 vs Day 8 锚点) | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 9 项判据全中。5 个 Timing 变量值全对 + 4 个解释 (a)(b)(c)(d) 全中。加分: PCTPTNUM 排序坑明文 (10 HOURS vs 2 HOURS 文本排序) + PCELTM ISO 8601 P/T 规则解释 + 两周期 VISITNUM + PCTPTREF + PCRFTDTC 三元组合。无 FAIL 触发 (PCELTM 没写成 "4 hours"/"04:00:00", PCTPTREF 没写 datetime, 没用 VISITDY 区分周期)。
