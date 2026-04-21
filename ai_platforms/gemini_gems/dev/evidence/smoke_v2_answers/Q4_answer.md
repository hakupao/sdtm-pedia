# Q4 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/4ccf7e3a6135571d
> Mode: Pro
> Run: 2026-04-21

## 原题
SDTMIG v3.4 中, AE 域的 AESEV (Severity) 变量有几档取值? 和肿瘤试验常用的 CTCAE Grade 1-5 如何对应? 如果 EDC 里只收到 Investigator 填的 CTCAE Grade, AESEV 该怎么填? Grade 5 对应什么特殊处理?

## 答案全文

针对您提出的关于 AE.AESEV 取值、CTCAE 对应关系以及业务填报的具体问题，以下是基于 SDTMIG v3.4 的详细解析：

### 1. AESEV (Severity) 的取值档位

AE.AESEV（Severity/Intensity，Core: Perm）用于表示不良事件的严重程度（临床强度）。

- **取值档位**：它受控于外部字典 AESEV Codelist（CT Code C66769）。
- 在大多数非肿瘤临床试验中，标准的三档取值为 MILD, MODERATE, SEVERE（轻度、中度、重度）。
- **字典查询**：CT Code C66769 在本 Gem §3.1 索引未列详细 Term 值。具体 Term 值请查 NCI EVS Browser: https://evsexplore.semantics.cancer.gov/evsexplore/ 搜索 C66769。本 Gem 不 inline CT Term 以保业务场景完整覆盖。

### 2. AESEV 与 CTCAE Grade 1-5 的对应关系

在 SDTM 标准中，Severity (严重程度) 和 Toxicity Grade (毒性分级) 是两个独立的概念，分别对应不同的变量：

- Severity 使用 **AE.AESEV** (Core: Perm)。
- Toxicity Grade 使用 **AE.AETOXGR** (Standard Toxicity Grade, Core: Perm)。

CTCAE（Common Terminology Criteria for Adverse Events）是一套毒性分级标准（Grade 1 到 Grade 5）。在业务逻辑上，虽然 Grade 1-3 在字面上常被描述为 Mild / Moderate / Severe，但 Grade 4 (Life-threatening) 和 Grade 5 (Death) 已经超出了单纯的"临床强度"范畴，混入了"严重性 (Seriousness)"和"结果 (Outcome)"的概念。因此，SDTM 不推荐将它们强行视为同一个变量。

### 3. 如果 EDC 只收到 Investigator 填的 CTCAE Grade，AESEV 该怎么填？

**结论：不应推算，AESEV 留空，将收集到的 Grade 填入 AE.AETOXGR。**

业务处理原则：SDTM 的核心原则是"如实反映收集的数据（Tabulation）"。如果 CRF/EDC 设计中只收集了 CTCAE Grade 而没有独立收集 Severity，那么在 SDTM 映射时：

- 将 EDC 中的分级值映射至 AE.AETOXGR（例如："1", "2", "3"）。
- AE.AESEV 作为 Permitted 变量，直接留空 (Null)。
- 切勿擅自衍生（例如不要写 hardcode 规则把 Grade 1 强行转成 MILD 填入 AESEV），除非 Protocol 或 Data Management Plan (DMP) 中有明确且书面的 1:1 映射规定。

### 4. CTCAE Grade 5 的特殊处理

在 CTCAE 标准中，Grade 5 明确代表"因该不良事件导致死亡"。这会触发跨变量的连锁反应：

- 毒性分级：AE.AETOXGR = "5"。
- 不良事件结果：因为患者死亡，应在结果变量 AE.AEOUT (Outcome of Adverse Event, Core: Perm) 填入对应 Fatal 的标准词（受控于 OUT Codelist，通常为 "FATAL"）。
- 严重性标准 (Seriousness)：死亡属于法规定义的严重不良事件标准，因此：
  - AE.AESER (Serious Event, Core: Exp) 必须为 "Y"。
  - AE.AESDTH (Results in Death, Core: Perm) 必须为 "Y"。

**关于 AE 域 Core 属性的提示 (CO-1)**：AE 域 Core 属性不规则：STUDYID/DOMAIN/USUBJID/AESEQ/AETERM/AEDECOD (6 个) Req；AESER/AEREL/AEACN/AELLT* (10 左右) Exp；其余 (AESEV/AESHOSP/AESLIFE/AESDTH/AETOXGR/AEOUT 等) Perm。逐变量查 02 spec。本例中 AESEV 和 AETOXGR 均为 Perm。

**源路径**:
knowledge_base/domains/AE/spec.md §AESEV, §AETOXGR, §AEOUT, §AESDTH, §AESER
knowledge_base/chapters/ch04_general_assumptions.md (关于不轻易衍生未收集数据的基本假设)
