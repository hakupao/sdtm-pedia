# Gemini Gems — Q14 (I1 — AE+CE+MH 同事件 + DS 死亡跨域对齐)

> **Date**: 2026-04-22 晚
> **Platform**: Gemini Gems (SDTM Expert gem, v5 system_prompt + 4-file KB)
> **Mode**: Gemini 3.1 Pro
> **方法**: Chrome MCP full-auto (ClipboardEvent paste + Enter)
> **生成时间**: ~1 min

---

## 题目原文 (v4.0)

受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答:
(a) 这一系列事件里, 心梗本身可以同时记在哪些域 (AE / CE / MH)? 各自的业务边界什么?
(b) "死亡" 这个 terminal event 同时应该记 AE 和 DS 还是只一个?
(c) DS 域的 DSDECOD vs DSCAT 在"死亡"场景下值各是什么?
(d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?

---

## Gemini raw 回答 (DOM readback)

对于这一涉及多个SDTM域（AE, CE, MH, DS, DM）且包含死亡终点事件的复杂业务场景，详细解答如下：

### (a) 心梗（STEMI）记录的域及业务边界

心梗本身可以记在以下三个域，取决于其发生的时机和研究方案的定义：

- **AE (Adverse Events)**：
  - 业务边界：受试者在签署知情同意书（ICD）后、试验结束前发生的任何不良医疗事件。在本场景中，Visit 5 突发的 STEMI 属于典型的 AE。
  - 严重性判定：因 STEMI 导致住院 3 天，该 AE 必须判定为 Serious (AESER="Y")，且需勾选 AESHOSP="Y"（住院/延长住院）。

- **CE (Clinical Events)**：
  - 业务边界：用于记录方案预先定义为"临床关注事件"或"疗效终点事件"的事件。
  - 场景应用：如果该研究是一项以心血管事件（MACE）为主要终点的试验，STEMI 可能既是 AE 也是疗效终点。此时心梗记录在 CE 中以便进行终点评价，通常会通过 RELREC 与 AE 域的记录关联。

- **MH (Medical History)**：
  - 业务边界：记录受试者在**入组前（通常指 ICD 签署前）**已经存在的医疗情况或诊断。
  - 场景应用：如果该受试者在入组前就有心梗史，记在 MH。Visit 5 发生的事件属于研究期间的新发事件，不应记在 MH 中。

源路径：knowledge_base/domains/AE/spec.md §AESER, knowledge_base/domains/CE/assumptions.md §1, knowledge_base/domains/MH/spec.md §MHTERM。

### (b) "死亡"事件的记录方式

"死亡"作为一个终点事件（Terminal Event），必须在多个域中同时体现，而不是只记一个：

- **DS (Disposition)**：必须记录。这是受试者退出研究的最权威来源，DSCAT 标记为 "DISPOSITION EVENT"，表示受试者因死亡而中止了研究或治疗。
- **AE (Adverse Events)**：必须记录。导致死亡的心衰是一个 AE。需设置 AESDTH="Y"（结果导致死亡）和 AEOUT="FATAL"。
- **DM (Demographics)**：必须体现。通过 DTHFL="Y" 和 DTHDTC 来声明受试者的死亡状态和日期。

源路径：knowledge_base/domains/DS/assumptions.md §1, knowledge_base/domains/AE/spec.md §AESDTH, knowledge_base/domains/DM/spec.md §DTHFL。

### (c) DS 域死亡场景下的变量值

在因心衰死亡导致研究中止的场景下，DS 域的核心变量建议取值如下：

- **DSTERM** (Reported Term)："DEATH" 或 "CONGESTIVE HEART FAILURE"（按 CRF 原始收集词）。
- **DSDECOD** (Standardized Term)："DEATH"。
- **DSCAT** (Category)："DISPOSITION EVENT"。
- **DSSCAT** (Subcategory)："STUDY PARTICIPATION"（表示因死亡导致的整个研究参与的中止）。

源路径：knowledge_base/domains/DS/spec.md §DSDECOD, §DSCAT, §DSSCAT。

### (d) 死亡时间（ISO 8601）跨域对齐规则

为了保证数据一致性，不同域中的死亡相关日期必须按以下逻辑对齐：

- **DM.DTHDTC**：受试者的死亡日期时间，作为全库的"死亡基准日期"。
- **DS.DSSTDTC**：因死亡导致中止的处治日期。该日期必须等于 DM.DTHDTC。
- **AE.AESTDTC**（针对心衰事件）：导致死亡的 AE 的开始时间。心衰可能在死亡前已发生（日期早于或等于死亡日）。
- **AE.AEENDTC**（针对心衰事件）：必须等于 DM.DTHDTC。

总结对齐公式：**DS.DSSTDTC = DM.DTHDTC = AE.AEENDTC**（针对直接死因 AE）。

源路径：knowledge_base/chapters/ch04_general_assumptions.md §4.4.4 (ISO 8601), knowledge_base/domains/DM/spec.md §DTHDTC。

---

## Self-score verdict

**PASS+** (bonus track, 4-file KB 容错)

### 逐判据对照

| 判据 | Gemini 答 | 判 |
|---|---|---|
| (a) AE 识别 on-study SAE | "STEMI 属于典型 AE, AESER=Y + AESHOSP=Y" ✓ | PASS |
| (a) AE/MH/CE timing 边界 | ICD 前=MH / study 期=AE / CE=方案预定义终点. MH 例外 "若入组前心梗史" 精确 ✓ | PASS |
| (a) 本题心梗是 AE 不跨 MH/CE | "Visit 5 新发事件不记 MH" + "CE 仅当 MACE 终点" ✓ | PASS |
| (b) DS 必记 + AE.AESDTH=Y 非互斥 | 全中, 且补 DM.DTHFL/DTHDTC 三域 | PASS+ |
| (c) DSDECOD=DEATH | ✓ | PASS |
| (c) DSCAT=DISPOSITION EVENT | ✓ + DSSCAT bonus | PASS |
| (c) CDISC CT C66727 codelist | **未提 C66727 C-code** | MINOR gap |
| (d) 日级对齐 DM.DTHDTC=DS.DSSTDTC=AE.AEENDTC | 总结公式精确 ✓ | PASS |
| (d) time-level offset 可接受 | **未提 time-level offset, AEENDTC 写 "必须等于"** | MINOR gap (判据过严但方向对) |

### 要点

- **最强**: (a) CE 解释为 "MACE 预定义疗效终点 + RELREC 与 AE 关联" 超出基础判据
- **独到**: AEOUT="FATAL" + DM.DTHFL 补充 (判据未列但业界必要)
- **缺**: C66727 Completion/Reason codelist C-code; time-level offset 容错 + csdrg 文档化说明
- **4 部分全中核心判据, 无 FAIL 触发**

### FAIL 判据触发?

- "AE/CE/MH 三个都记同一事件" → NO (明确分 timing 边界)
- "AE/MH/CE 绝对互斥" → NO (给入组前 MH 例外)
- 死亡只记 AE 不记 DS → NO (DS 必记)
- DSDECOD 自定义 term → NO (用 DEATH)
- 日期不一致无 SDRG → NO (给对齐公式)
- 要求 time-level 严格等 → **minor 触发** (写 "必须等于" 而非日级)
