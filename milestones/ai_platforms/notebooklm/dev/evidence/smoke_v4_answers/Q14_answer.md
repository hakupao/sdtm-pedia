# NotebookLM — Q14 (I1 — AE+CE+MH 同事件 + DS 死亡跨域对齐)

> **Date**: 2026-04-22 晚
> **Platform**: NotebookLM (SDTM Knowledge Base notebook, 42 sources + instructions.md Custom mode)
> **方法**: Chrome MCP cowork (delete chat history → setter paste → Submit → wait)
> **生成时间**: ~3 min

---

## 题目原文 (v4.0)

受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答:
(a) 这一系列事件里, 心梗本身可以同时记在哪些域 (AE / CE / MH)? 各自的业务边界什么?
(b) "死亡" 这个 terminal event 同时应该记 AE 和 DS 还是只一个?
(c) DS 域的 DSDECOD vs DSCAT 在"死亡"场景下值各是什么?
(d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?

---

## NotebookLM raw 回答 (DOM readback)

针对您描述的受试者突发心梗 (STEMI) 住院、随后因心衰死亡的场景，以下是基于 SDTMIG v3.4 规则的详细解答：

### (a) STEMI 的记录域与业务边界 (AE / CE / MH)

在这一系列事件中，STEMI **不会记录在 MH 中**，而是根据方案定义记录在 AE 或 CE 中 [1][2][3]。

- **MH (Medical History)**: 不适用 [3]。MH 域用于记录试验参考期开始前（通常是第一次给药前）的既往病史 [3]。由于 STEMI 发生在 Visit 5（试验期间），因此不能记入 MH [3]。
- **AE (Adverse Events)**: 适用 [1]。AE 域用于记录受试者在使用试验药物后发生的任何不良医学事件 [1]。在大多数常规试验中，突发的 STEMI 应作为严重不良事件 (SAE) 收集并记录在 AE 中 [1]。
- **CE (Clinical Events)**: 适用 [2]。CE 域用于记录方案预先定义、且不作为 AE 处理的临床关注事件 [2]。如果该研究是一项心血管结局试验，方案将心梗 (Myocardial Infarction) 定义为疗效终点 (Efficacy endpoint)，则该 STEMI 应记录在 CE 域，而不是 AE 域 [2]。

### (b) "死亡" 这个 terminal event 应该记在哪个域？

死亡本身不是一个事件，而是事件的结局 (Outcome) [4]。该场景下必须在 AE、DS 和 DM 多域联动记录，不能仅记录在一个域中 [5][6][7]：

- **AE 域**: 记录导致死亡的根本原因（心衰，Heart Failure）作为不良事件 (AETERM) [8]。该不良事件的结局变量 AEOUT 应设为 "FATAL" [5][9]，且导致死亡的标志 AESDTH 必须设为 "Y" [5]。
- **DS 域**: 记录受试者因死亡而终止研究或退出当前试验阶段的处置事件 [10][8]。
- **DM 域**: 必须更新受试者的死亡日期 DTHDTC 以及死亡标志 DTHFL 设为 "Y" [7]。
- **(可选) DD (Death Details) 域**: 如果收集了额外的死亡细节（例如首要死因、死亡地点），则记录在 DD 域，并通过 RELREC 与 DS 和 AE 关联 [4][6]。

### (c) DS 域在"死亡"场景下的 DSDECOD 与 DSCAT 值

当受试者因死亡结束研究参与时，DS 域的取值必须使用标准受控术语全拼，不能缩写：

- **DSCAT** (Category for Disposition Event): 必须为 **"DISPOSITION EVENT"** (Codelist **C74558**) [11][10]。
- **DSDECOD** (Standardized Disposition Term): 必须为 **"DEATH"** (Codelist **C66727 / NCOMPLT**) [12][8][6]。
- (此时 DSTERM 通常记录具体收集的死因文字，如 "Heart Failure" [8]。)

### (d) 死亡时间的 ISO 8601 跨域对齐逻辑

受试者的确切死亡时间必须以 ISO 8601 format (YYYY-MM-DDThh:mm:ss) 格式呈现，并在多个域的 Timing 变量中保持逻辑一致与对齐 [13][14][15][5]：

- **AE.AEENDTC**: 记录心衰这一致死性不良事件的结束时间。因为事件以死亡告终，此时间对应受试者的死亡时间 [14][5]。
- **DS.DSSTDTC**: 记录死亡这一受试者处置事件 (Disposition event) 的发生时间 [15][8]。
- **DM.DTHDTC**: 记录从临床数据库中捕获的受试者确切死亡时间 [13]。

**对齐规则**: 针对此次事件，**DM.DTHDTC = DS.DSSTDTC = AE.AEENDTC**。三个值在精度允许的范围内必须完全对齐 [8][5][7]。

### Variables involved

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| AETERM | Char | Topic | Req | | [16] |
| AEOUT | Char | Record Qualifier | Perm | C66768 | [17] |
| AESDTH | Char | Record Qualifier | Perm | C66742 | [18] |
| AESTDTC | Char | Timing | Exp | ISO 8601 | [19] |
| AEENDTC | Char | Timing | Exp | ISO 8601 | [14] |
| DSCAT | Char | Grouping Qualifier | Exp | C74558 | [11] |
| DSDECOD | Char | Synonym Qualifier | Req | C66727 | [12] |
| DSSTDTC | Char | Timing | Exp | ISO 8601 | [15] |
| DTHDTC | Char | Record Qualifier | Exp | ISO 8601 | [13] |
| DTHFL | Char | Record Qualifier | Exp | C66742 | [20] |

**Codelist Reference**:
- C66768 (Outcome of Event): FATAL / NOT RECOVERED/NOT RESOLVED / RECOVERED/RESOLVED WITH SEQUELAE / RECOVERED/RESOLVED / RECOVERING/RESOLVING / UNKNOWN [9]
- C66727 (Completion/Reason for Non-Completion): Includes DEATH [12][8]
- C74558 (Category of Disposition Event): Includes DISPOSITION EVENT [11][10]

**Boundary note**: AEOUT 和 AESDTH 的 Core 层级均为 Perm，但当不良事件导致死亡时，为了说明事件的 fatal 性质，通常会在提交时包含并填入 "FATAL" 和 "Y" [5]。DSDECOD 是 Req 变量，无论何种情况绝不能留空，发生死亡必须标准化映射为 "DEATH" [12][8]。

---

## Self-score verdict

**PASS+ 最强** (NotebookLM Q14 — 4 平台 baseline 对比预期最高)

### 逐判据对照

| 判据 | NotebookLM 答 | 判 |
|---|---|---|
| (a) AE 识别 on-study SAE | ✓ | PASS |
| (a) AE/MH/CE timing 边界 | ICD 前=MH / study 期内=AE / CE=方案预定义疗效终点 ✓ | PASS |
| (a) 本题 STEMI 归属 | on-study 排除 MH, AE 或 CE 按方案定义 ✓ (未直接下断言, 给方案条件分支) | PASS |
| (b) 死亡 AE+DS 非互斥 | **三域联动 AE+DS+DM + DD 可选 RELREC** 超判据 | PASS+ |
| (c) DSDECOD=DEATH + C66727 | **Codelist C66727 NCOMPLT 精确** | PASS+ |
| (c) DSCAT=DISPOSITION EVENT | ✓ + **Codelist C74558 精确给出** | PASS+ |
| (c) DSTERM 记 "Heart Failure" | **bonus 独到** (判据未列但业界精确) | PASS+ |
| (d) 日级对齐公式 | DM.DTHDTC=DS.DSSTDTC=AEENDTC ✓ + "精度允许范围内完全对齐" 业界准确 | PASS+ |

### 要点

- **最强**: (c) 两个 C-code (C66727 Completion + C74558 Category) 精确, 判据核心
- **最强**: Variables table 完整, 每个变量 Role/Core/CT 全给, 超出 4 平台基线
- **独到**: DD (Death Details) 域 + RELREC 连接 DS/AE (判据未列但业界 SDTMIG v3.4 正确)
- **独到**: DSTERM="Heart Failure" (原始收集词 vs DSDECOD 标准化) 精确区分
- **独到**: AEOUT/AESDTH Core=Perm 但死亡场景必填的 Boundary note
- **Citation 稠密**: 20+ inline [1]-[20] 源码引用

### FAIL 判据触发?

- "三域都记同一事件" → NO (明确 AE/MH 互斥 by timing, AE/CE 按方案)
- "AE/MH/CE 绝对互斥" → NO (明确 MH 排除仅因 on-study)
- 死亡只记 AE → NO (三域必联动)
- DSDECOD 自定义 term → NO (CDISC CT DEATH)
- 日期不一致 → NO (给对齐公式)
- time-level 严格相等 → **NO** (用 "精度允许范围内", 业界容错表达)

### Verdict: **PASS+ 最强** (Q14 判据全中 + 3 个 bonus + 2 个 C-code 精确 + Variables table + DD 域)
