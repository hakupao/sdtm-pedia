# Q_sanity_4 — Gemini SDTM Expert 回答

> 题: Disease Milestones 实际发生记录在哪个域? TM 和 SM 什么关系?
> 期望: SM 域 (Subject Disease Milestones); TM 定义 + SM 记录实例 + 其他域用 `--MIDS` 引用 (MIDS 三角关系)
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/004a7f3a4d3d3030
> 时间: 2026-04-22
> 账号: bojiang.zhang.0904@gmail.com (Pro)
> Mode: Pro

## 完整回答

根据 SDTMIG v3.4 的规定，关于 Disease Milestones (疾病里程碑) 的记录域以及 TM (Trial Milestones) 与 SM (Subject Milestones) 的关系，解析如下：

### 1. Disease Milestones 实际发生记录在哪个域？

Disease Milestones 的实际发生通常记录在 **SM (Subject Milestones)** 域，或者通过 **MIDS (Milestone Identification)** 变量族在其他域中引用。

- **SM 域 (Subject Milestones)**:
  - 用途: 记录受试者层面特定里程碑事件的实际发生日期/时间。
  - 场景: 当疾病里程碑是一个独立的事件（如：受试者达到"首次缓解 First Remission"或"疾病进展 Progression"）时，该记录会出现在 SM 域。

- **MIDS 变量族引用**:
  - 机制: 在 Findings (如 RS, LB) 或 Events (如 AE) 域中，使用 `--MIDS` (Milestone Identifier), `--MIDSTYPE`, 和 `--RELMIDS` (Relationship to Milestone) 变量来关联 TM 域中定义的里程碑。
  - 意义: 这种方式允许数据使用者直接看到"这条记录（如 AE）是发生在哪个疾病里程碑（如第一次进展）之后"，而无需通过复杂的 RELREC 建立关联。

### 2. TM 和 SM 的关系

TM 和 SM 共同构成了 SDTM 的里程碑框架，分别代表"试验设计层"和"受试者执行层"：

| 特性 | TM (Trial Milestones) | SM (Subject Milestones) |
|------|----------------------|------------------------|
| 域类 (Class) | Special Purpose (Trial Design) | Events |
| 定义层面 | 试验级 (Trial Level) | 受试者级 (Subject Level) |
| 内容 | 定义整个研究计划中预设的里程碑（如：FPI, LPO, 或特定的疾病评估点） | 记录每个受试者实际达成这些里程碑的具体信息（如：该受试者实际随机化的日期） |
| 结构 | 每个试验里程碑一条记录 | 每个受试者每达成一个里程碑一条记录 |
| 核心变量 | `TMTERM` (里程碑名称) | `SMTERM` (里程碑名称), `SMSTDTC` (发生时间) |

### 关系总结

TM 域定义的项 (`TMTERM`) 通常是 SM 域记录 (`SMTERM`) 的来源。SM 记录了受试者何时 (Timing) 经历了 TM 中定义的那个事件 (Term)。在涉及疾病进展 (Disease Progress) 的复杂研究中，TM 会定义什么是 "Progression Milestone"，而 SM 则记录每个受试者具体在哪一天达到了该状态。

### 源路径

- `knowledge_base/chapters/ch04_general_assumptions.md` §4.4.11 (Disease Milestones)
- `knowledge_base/domains/TM/spec.md`
- `knowledge_base/domains/SM/spec.md`
- `knowledge_base/04_business_scenarios_and_cross_domain.md` §24.3 (MIDS 变量跨域扩散)

### 相关依据

"The Subject Milestones (SM) domain... contains the actual dates and times that milestones were achieved by subjects." (Ref: SM Assumptions)
"The Trial Milestones (TM) domain... describes planned trial-level milestones." (Ref: TM Spec)

## Verdict

**PASS** — SM 域 + TM/SM 试验级 vs 受试者级区分 + `--MIDS/--MIDSTYPE/--RELMIDS` 变量族三变量齐全 + 跨域引用机制; 完全命中期望 "SM 域 (Subject Disease Milestones); TM 定义 + SM 记录实例 + 其他域用 `--MIDS` 引用 (MIDS 三角关系)". 表格对比完整, 源路径 4 条 (含 ch04 §4.4.11 + 04 §24.3 + 两 spec.md) 均指认合理. §1.6 硬锚点 + MIDS 三角底座未回归.

## Step 2 sanity 4 题全结果

| # | 题 | 期望 | 实际 | Verdict |
|---|----|------|------|---------|
| 1 | AESER Core | Exp | Exp | PASS |
| 2 | LBNRIND values | HIGH/LOW/NORMAL/ABNORMAL | 4 值全写 + CO-2 子条款显式禁 H/L/N | PASS |
| 3 | ACTARMCD 域 + Core | DM / Exp | DM / Exp + ARMCD/ARM Req 对比 | PASS |
| 4 | Disease Milestones 域 + TM/SM | SM + MIDS 三角 | SM + MIDS 变量族 + 对比表 | PASS |

**4/4 sanity PASS → 底座 v5+v5b 仍 lock, 可进 Step 3 smoke v3 Q1-Q10.**
