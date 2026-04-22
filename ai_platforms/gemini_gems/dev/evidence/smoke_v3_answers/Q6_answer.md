# Q6 — Gemini SDTM Expert 回答 (C1 — PK Timing --TPT 四件套)

> 期望核心: PCTPT="4 hours post dose" + PCTPTNUM=4 + PCTPTREF="DOSE" + PCELTM="PT4H" (ISO 8601 Duration) + PCRFTDTC=实际服药时间 + TPT/TPTNUM 排序 + Duration 格式 + VISITNUM/EPOCH 区分周期
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/9494390b30efb45a
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

这是一个非常经典的 PK (药代动力学) 数据映射场景。在 SDTM 的 PC (Pharmacokinetics Concentrations) 域中，精准地表达计划的时间点 (Planned Time) 以及它与参考事件 (Reference Event) 的关系至关重要。

针对您提到的"服药后 4 小时采血"这一记录，以下是变量的推荐填法以及对背后逻辑的详细解释：

### 1. 变量填法 (示例)

假设患者在 2026-04-22 的 08:00 服药。对于 4 小时后的那次采血记录：

| 变量 | 值示例 | 含义说明 |
|------|--------|----------|
| PCTPT | "4 h" 或 "4 HOURS POST-DOSE" | 计划时间点的字符描述 (Protocol/CRF 上的用词) |
| PCTPTNUM | 4 | 计划时间点的数值，用于排序 |
| PCTPTREF | "DOSE" 或 "STUDY DRUG ADMINISTRATION" | 锚定参考点，即 4 小时是相对什么而言的 |
| PCELTM | "PT4H" | 从参考点到计划采血点的计划流逝时间 (ISO 8601 Duration 格式) |
| PCRFTDTC | "2026-04-22T08:00" | 锚定参考点 (即服药) 的实际发生日期/时间 |

### 2. 详细解释 (a - d)

(a) **PCTPT vs PCTPTNUM 的关系**
- PCTPT (Planned Time Point Name) 是文本型 (Char)，通常直接照搬 Protocol 或 CRF 上设计的访视点名称
- PCTPTNUM (Planned Time Point Number) 是对应的数值型 (Num)
- 核心区别: 文本型排序往往不符合时间逻辑（例如 "15 min" 字符排序可能在 "1 h" 前后）。PCTPTNUM 专为分析或审查时按时间先后顺序正确排序

(b) **PCTPTREF 指什么？**
- PCTPTREF (Time Point Reference) 指"计划时间点"所依赖的基准事件 (Anchor/Reference point)
- 在本例中，所有采血时间都相对于服药发生，PCTPTREF 填 "DOSE" 或协议定义术语

(c) **PCELTM 是什么 ISO 格式？**
- PCELTM (Planned Elapsed Time from Time Point Ref) 遵循 **ISO 8601 Duration** 格式
- 格式: P (Period) 开头，时间以 T (Time) 前缀：PT4H = 4 小时; PT15M = 15 分钟; PT1H30M = 1 小时 30 分钟

(d) **同一受试者两周期记录用什么区分？**
- **VISIT / VISITNUM**：基础区分，周期 1 VISIT="PERIOD 1"，周期 2 VISIT="PERIOD 2"
- **EPOCH**：高度推荐，明确划分数据阶段（如 "TREATMENT PERIOD 1" / "TREATMENT PERIOD 2"），跨域一致
- 补充: PCTPTREF 也可带入周期信息（如 "DOSE 1", "DOSE 2"），但 VISIT/EPOCH 更规范

### 源路径

- knowledge_base/domains/PC/spec.md §PCTPT, §PCTPTNUM, §PCTPTREF, §PCELTM, §PCRFTDTC
- knowledge_base/chapters/ch04_general_assumptions.md §4.1.4.10 (EPOCH) 及 §4.1.4.3 (ISO 8601 Duration)

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| PCTPT 文字 | "4 hours post dose" | "4 h" 或 "4 HOURS POST-DOSE" | ✅ |
| PCTPTNUM 数字 | 4 | 4 | ✅ |
| PCTPTREF 名字 | "DOSE" / "STUDY DRUG DOSE" | "DOSE" / "STUDY DRUG ADMINISTRATION" | ✅ |
| PCELTM ISO 8601 Duration | "PT4H" | "PT4H" | ✅ |
| PCRFTDTC ISO datetime | 实际服药时间 | "2026-04-22T08:00" | ✅ |
| (a) TPT vs TPTNUM | 文字标识 vs 数字排序 | 文字型 vs 数字型 + 排序 chronological 详述 | ✅ |
| (b) PCTPTREF 指 | 名字 (reference point name) | 锚定参考点 / 基准事件 | ✅ |
| (c) PCELTM 格式 | ISO 8601 Duration | ISO 8601 Duration + P/PT 前缀 + PT4H/PT15M/PT1H30M 示例 | ✅ |
| (d) 两周期区分 | VISITNUM / EPOCH | VISIT/VISITNUM + EPOCH (推荐) + PCTPTREF DOSE1/DOSE2 补充 | ✅ |

## Verdict

**PASS** — 5 Timing 变量 + 4 解释 (a/b/c/d) 全部精准命中. PT4H 格式 + TPT vs TPTNUM 排序意图 + PCTPTREF 锚定事件 + VISITNUM/EPOCH 两周期区分均完整. ISO 8601 Duration 举 PT4H/PT15M/PT1H30M 三例加分. 表格表达清晰. 典型 generalization + v3.4 Timing 变量深度理解 同时达标.

- 04 引用: 1 次 (ch04 §4.1.4.10 EPOCH + §4.1.4.3 ISO 8601 Duration); 非 04 业务弹药包命中 (04 §4.3 Timing 基础而本题要求深入 --TPT 四件套, Gemini 引正确 ch04 §4.1.4.3 Duration 专有条款)
- CO-2 触发: 无
- Score: 1 / 1
