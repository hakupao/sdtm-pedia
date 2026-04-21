# Q6 — DM.ARMCD vs DM.ARM + 中途换组 (v2.1)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e73d3d-a88c-83a4-be4b-5a41777b5785
**Date**: 2026-04-21
**Thought for**: 1m 28s

## 原题

解释 DM 域的 ARMCD (Arm Code, 分组代号) 和 ARM (Arm Description, 分组描述) 的关系 (哪个是短代号, 哪个是 human-readable). 如果受试者因盲态问题在 Week 4 从 Arm A 转到 Arm B, 这个信息应该记录在 DM / SE / TA 哪个域? 分别说明各自的职责.

## ChatGPT 答案 (完整)

**结论先说**:

- **DM.ARMCD** 是短代号 / code, 更偏机器可处理; **DM.ARM** 是给人看的分组描述 / human-readable description. 二者在 TA 中是**一一对应**关系, 这个一一对应必须在 DM 里保持.
- 受试者在 Week 4 因盲态问题从 Arm A 转到 Arm B, 这个"实际走过的路径"**主要记在 SE**; DM 只保留受试者级摘要 (计划 arm / 实际 arm 总结); TA 不记录单个受试者的偏离, 除非 A→B 本来就是方案设计的一条 planned arm.

### 1) ARMCD 和 ARM 的关系

在 DM 里:
- **DM.ARMCD** — Planned Arm Code, Role = Record Qualifier, 是计划分组的短代码.
- **DM.ARM** — Description of Planned Arm, Role = Synonym Qualifier, 是这个 code 的可读描述.

可以把它理解成:
- ARMCD = "A" → 短代号
- ARM = "Drug A" → 人能直接读懂的描述

SDTM 明确要求: TA 里 ARMCD 和 ARM 是 **one-to-one relationship**, 这个对应关系在 DM.ARMCD/ARM 以及 DM.ACTARMCD/ACTARM 中都要保持.

模型层面: ARMCD 在 TA 里是 arm 的"主题变量" (topic), 但在 DM 里只是描述该受试者记录的一个 qualifier. 这说明了 **TA 定义设计, DM 摘要受试者**.

### 2) Week 4 从 Arm A 转到 Arm B, 放 DM / SE / TA 哪个域?

**SE: 记录"实际发生了什么"** (最核心的落点)

SE 的职责是记录受试者实际经过的 subject elements 时间线, 即"这个人实际走了哪些 element、从什么时候到什么时候". SDTM 明说: SE 用来提交"the trial elements a subject actually passed through".

对你这个场景:
- 需要在 SE 里体现 Week 4 的切换时间
- 用 SESTDTC / SEENDTC 表示 element 起止
- SESEQ 按真实时间顺序排列

如果这个 Week 4 的切换不能用原计划中的 element 合理表示, 则应建 **unplanned element**:
- ETCD = "UNPLAN"
- SEUPDES 填写对该非计划 element 的描述
- 这类记录的 TAETORD 不填

SDTM 还专门举了"给错药"的例子: 受试者本来在 blinded treatment A, 却一段时间实际上拿到了 drug B; 在 SE 里就用 UNPLAN + SEUPDES 表达这个非计划经历.

**DM: 记录"计划 arm / 实际 arm 的受试者级摘要"**

DM 只有一条受试者记录, 不是时间线. 它负责总结:
- **ARMCD / ARM** = 计划分到哪一组
- **ACTARMCD / ACTARM** = 实际走成了哪一组 (仅当实际路径能对应到 TA 中某个 planned arm)

对你的场景, 通常应这样理解:
- ARMCD/ARM 仍然表示原先被分配的 Arm A
- 是否能把 ACTARMCD/ACTARM 填成 Arm B, 要看整个实际经历是否恰好对应 TA 中某个已计划 arm

关键规则:
- 如果实际路径符合 TA 中某个已计划 arm, 则 ACTARMCD/ACTARM 可填该 arm;
- 如果实际路径不符合任何 planned arm (比如前 4 周 A, 后面因盲态问题转 B, 这在平行设计里通常不是任何一个计划 arm), 则:
  - ACTARMCD = null
  - ACTARM = null
  - **ARMNRS = "UNPLANNED TREATMENT"**
  - **ACTARMUD** 说明实际发生了什么

这不是推断, 而是 SDTM 示例直接展示的处理方式: 受试者计划是 A, 但中途误用了 B; ARM/ARMCD 仍反映计划 treatment, ACTARM/ACTARMCD 置空, 因为整个实际经历不匹配任何 planned arm, 并用 ARMNRS="UNPLANNED TREATMENT" + ACTARMUD 描述.

**TA: 记录"方案设计里计划有哪些 arm"**

TA 是试验设计层数据集, 不是受试者实际执行数据. 它的结构是 **one record per planned element per arm**.

所以:
- 如果"Week 4 从 A 转到 B"只是某个受试者因为盲态问题发生的偏离, **不改 TA**
- 只有当"A→B"本身就是方案预先设计的一条 arm (比如 crossover / rescue / re-randomization 设计中的 planned sequence), 才应该在 TA 中定义那条 arm.

### 3) 这三个域各自的职责, 一句话版

| 域 | 职责 | 你的场景里怎么用 |
|----|------|-----------------|
| DM | 受试者级摘要 | 保留 ARMCD/ARM (计划 arm); 若实际路径不匹配任何 planned arm, 则 ACTARMCD/ACTARM 置空并用 ARMNRS/ACTARMUD 解释 |
| SE | 受试者实际经过的 element 时间线 | 主要记录 Week 4 切换; 必要时用 ETCD="UNPLAN"、SEUPDES 描述 |
| TA | 方案层的 planned arms | 不记录单个受试者偏离; 只有设计里本来就有 A→B 这条 arm 才在这里定义 |

### 4) 实务判断口诀

- 问"原来计划分哪组?" → 看 DM.ARMCD / DM.ARM
- 问"这个人实际上走了什么路径?" → 看 SE
- 问"研究设计里本来有哪些 arm?" → 看 TA
- 问"实际路径最后能不能概括成某个 planned arm?" → 决定 DM.ACTARMCD / ACTARM 是否可填; 不能概括就走 ARMNRS="UNPLANNED TREATMENT" + ACTARMUD.

### 源溯源

- `knowledge_base/domains/DM/spec.md`
- `knowledge_base/domains/DM/assumptions.md`
- `knowledge_base/domains/SE/assumptions.md`
- `knowledge_base/domains/SE/examples.md`
- `knowledge_base/model/01_concepts_and_terms.md`
- `knowledge_base/chapters/...` (TA 的 trial design 定位)

## 判据对齐 (v2.1)

- ✅ ARMCD = 短代号 (Planned Arm Code, Record Qualifier) — "A"/"PBO"
- ✅ ARM = Full description (Description of Planned Arm, Synonym Qualifier) — human-readable
- ✅ ARMCD 是 TA 的键; DM.ARMCD 必须匹配 TA.ARMCD (one-to-one)
- ✅ DM 只记**最终分组** (ACTARMCD / ACTARM); SE 记**实际经过的 element 序列**; TA 是**设计**非实际
- ✅ ACTARM / ACTARMCD vs ARM / ARMCD 清晰区分
- ✅ **加分**: ARMNRS="UNPLANNED TREATMENT" + ACTARMUD 处理实际不匹配任何 planned arm 场景 (SDTM 示例级知识)
- ✅ **加分**: ETCD="UNPLAN" + SEUPDES 处理 SE 非计划 element (SDTM 示例级知识)
- ✅ SDTM 示例"给错药"场景直接类比 (examples.md 命中)
- ✅ 引 6 源 (DM/spec + DM/assumptions + SE/assumptions + SE/examples + model/01 + chapters)

## Verdict: **PASS** (1/1)

## 归因

系统 prompt v2.1 + DM/SE/TA knowledge 全命中. ARMCD/ARM 短长描述正确, ACTARM 概念识别 + ARMNRS="UNPLANNED TREATMENT" 专业级处理 + ETCD="UNPLAN"/SEUPDES unplanned element 示例级知识, 均超判据基线. TA 设计 vs 实际清晰分工. 6 源溯源完整.
