# Q7 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/466f26cb2a8a3f56
> Mode: Pro
> Run: 2026-04-21

## 原题
EDC 系统里某字段值为 "病史: 高血压 10 年, 目前仍在服用氨氯地平 5 mg/日". 映射到 SDTM 时这条信息应该拆成哪些域的记录? 只进 MH? 只进 CM? 还是两域都要? 简要说明 MH 和 CM 的分工.

## 答案全文

根据 SDTMIG v3.4 的一般假设与域映射规则，这条 EDC 信息包含两个截然不同的临床概念：疾病状况（Condition）与干预措施（Intervention）。因此，必须将这条信息拆分并映射到 MH 和 CM 两个域。

### 1. 结论：建议拆分方案

这条记录应拆分为两部分进行映射：

**MH (Medical History): 记录"高血压"**
- MHTERM: "高血压"
- MHSTDTC: 映射 10 年前的时间（如已知具体年份则记录，否则按 partial date 处理）
- MHENRTP: "ONGOING" (因为目前仍在治疗)

**CM (Concomitant Medications): 记录"氨氯地平"**
- CMTRT: "氨氯地平"
- CMDOSE: 5
- CMDOSU: "mg"
- CMDOSFRQ: "每日" (需映射至对应的 CT，如 QD)
- CMONGO: "Y"

### 2. MH 与 CM 的分工说明

根据 SDTM 观测类的定义（Findings/Events/Interventions）：

**MH (Medical History) —— 属于 Events 类**
- 分工：记录受试者在研究开始前已经存在的疾病、症状或医学状况。它回答的是"受试者患有什么病？"
- 逻辑：即使该疾病目前正在被治疗，疾病本身作为一个"事件/状况"应保留在 MH 中。

**CM (Concomitant Medications) —— 属于 Interventions 类**
- 分工：记录受试者接受的药物治疗或非药物干预。它回答的是"受试者为了治疗（或预防）目的使用了什么药？"
- 逻辑：用于治疗既往病史的药物，属于"合并用药"，应在 CM 域中详细记录其剂量、频率和持续时间。

### 3. 跨域关联（RELREC）

如果研究方案要求明确两者的因果或治疗关系（即"氨氯地平是为了治疗这条高血压病史"），可使用 RELREC (Related Records) 域将 MH 的 MHSEQ 与 CM 的 CMSEQ 进行关联。

**源路径**:
- knowledge_base/domains/MH/assumptions.md §General Assumptions (Medical History covers conditions/events)
- knowledge_base/domains/CM/assumptions.md §General Assumptions (Concomitant Medications covers treatments/interventions)
- knowledge_base/chapters/ch04_general_assumptions.md §4.1.2 (Events vs Interventions classes)
