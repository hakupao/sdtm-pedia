# Q6 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/97bbcb182bdc7643
> Mode: Pro
> Run: 2026-04-21
> Note: First submit attempt landed empty (ngModel sync race); retried by separating JS paste from UI click and succeeded on second attempt.

## 原题
解释 DM 域的 ARMCD (Arm Code, 分组代号) 和 ARM (Arm Description, 分组描述) 的关系 (哪个是短代号, 哪个是 human-readable). 如果受试者因盲态问题在 Week 4 从 Arm A 转到 Arm B, 这个信息应该记录在 DM / SE / TA 哪个域? 分别说明各自的职责.

## 答案全文

在 SDTM 标准中，处理受试者分组（Arms）和转换（Transitions）涉及 Trial Design 域与 Subject 域的协同。以下是针对您问题的详细解答：

### 1. DM 域中 ARMCD 与 ARM 的关系

在 DM (Demographics) 域中，这两个变量共同描述受试者被分配到的试验组别：

**ARMCD (Arm Code)**:
- 定义：分组代号（短代号）。
- 属性：字符型，长度不超过 20 个字符。
- 特点：用于编程处理的唯一标识，通常不含空格（如 "ARM_A"）。
- Core：Req (Required)。

**ARM (Description of Arm)**:
- 定义：分组描述（Human-readable）。
- 属性：字符型，长度可达 200 个字符。
- 特点：完整的、具有业务意义的描述性名称（如 "Placebo Group"）。
- Core：Req (Required)。

**关系**：两者必须一一对应。每一个唯一的 ARMCD 必须对应一个唯一的 ARM 描述。

**源路径**: knowledge_base/domains/DM/spec.md §ARMCD & §ARM

### 2. 受试者从 Arm A 转到 Arm B 的记录位置与职责

当受试者在 Week 4 发生组别转换时，SDTM 通过以下三个域协同表达这一动态过程：

**A. TA (Trial Arms) — 定义规则**
- 职责：定义试验中所有合法的组别及其包含的 Element（元素）序列。
- 本场景：如果"从 A 转到 B"是方案（Protocol）预设的交叉（Cross-over）设计，TA 会定义一个包含 A 段和 B 段的 Arm。如果这是非计划的转换（由于盲态错误等），TA 域通常保持不变（除非方案修订增加了这种路径）。
- 源路径：knowledge_base/domains/TA/spec.md

**B. SE (Subject Elements) — 记录事实**
- 职责：记录受试者实际经历的时间段（Elements）。
- 本场景：这是记录转换的核心位置。
  - 记录 1：受试者处于 Element A（由 SESTDTC 到 Week 4 转换日期）。
  - 记录 2：受试者处于 Element B（由转换日期到结束）。
- SE 能够通过 ETCD (Element Code) 的变化，精确反映受试者在什么时间点离开了 A 对应的 Element 并进入了 B 对应的 Element。
- 源路径：knowledge_base/domains/SE/spec.md

**C. DM (Demographics) — 计划归属**
- 职责：记录受试者计划 (Planned) 被分配到的组别。
- 本场景：
  - 如果受试者最初被随机化到 Arm A，尽管后来发生了非计划转换，在 DM 中通常仍记录 ARMCD = "A"。
  - SDTMIG 规定 DM.ARM 反映的是随机化时的计划组别。对于实际接受的治疗与计划不符，应通过 ADaM 的 TRTP/TRTA 变量或 SDTM 的 EX 域（暴露）来区分。
  - 注意：如果该转换是方案允许的（如交叉设计），DM.ARM 应指向 TA 中定义的那个完整的交叉组别代码。
- 源路径：knowledge_base/domains/DM/assumptions.md 第 4 条 (Planned vs Actual)

### 总结建议

| 维度 | 记录方式 | 说明 |
|------|---------|------|
| DM | ARMCD = "A" | 保持随机化时的计划组别 (Planned Arm) |
| SE | 拆分为两条记录 | 分别记录 Element A 和 Element B 的起止时间 (Actual Path) |
| TA | 预定义的组别结构 | 描述 Arm A 和 Arm B 分别由哪些 Element 构成 |

**源路径引用**:
- knowledge_base/domains/DM/spec.md (变量定义)
- knowledge_base/domains/SE/spec.md (受试者实际经历记录)
- knowledge_base/chapters/ch04_general_assumptions.md §4.1.2 (Trial Design Model 逻辑)
