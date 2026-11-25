# Q2 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/598a34d0c35117ca
> Mode: Pro
> Run: 2026-04-21
> Note: Conversation has auto-acknowledgment as turn 1 (gem auto-greet); Q2 is turn 2 user

## 原题
一位受试者服药后出现严重皮疹并因此住院 3 天治疗. Investigator 判断为药物相关的严重不良事件. 请问 SDTM AE 域中, 该如何记录这条事件的严重性相关变量 (AESER 及其子变量)? 请列出需要填写的 SAE 判定类变量 (AESER / AESCONG / AESDISAB / AESHOSP / AESLIFE / AESDTH / AESMIE) 各自的含义和本例取值, "Y" 还是 "N"?

## 答案全文

在此案例中，受试者因"严重皮疹"住院治疗，研究者判定为"严重不良事件 (SAE)"。根据 SDTMIG v3.4 和 SDTM v2.0 的规定，AE 域中的严重性相关变量应按以下逻辑记录：

### 1. 核心结论：本例变量取值表

| 变量名 | 标签 (Label) | 本例取值 | 含义 / 判定依据 | Core 属性 |
|---|---|:---:|---|:---:|
| AESER | Serious Event | Y | 严重不良事件标志。由于研究者已判定为 SAE，此项必须为 "Y"。 | Exp |
| AESHOSP | Requires Hospitalization | Y | 导致住院或延长住院时间。受试者住院 3 天治疗，符合此项。 | Perm |
| AESDTH | Results in Death | N | 导致死亡。本例受试者未死亡。 | Perm |
| AESLIFE | Is Life Threatening | N | 威胁生命。指事件发生时即面临死亡风险（如心跳骤停），住院本身不自动等同于威胁生命。 | Perm |
| AESDISAB | Persist or Signif Disability | N | 导致持久或显著的躯体功能障碍/能力丧失。本例未提及。 | Perm |
| AESCONG | Congenital Anomaly or Birth Defect | N | 先天性畸形或出生缺陷。本例为服药后的皮疹，不属于此类。 | Perm |
| AESMIE | Other Medically Important Event | N | 其他重要医学事件。当不符合上述任何具体标准，但根据医学判断属于严重状态时使用。本例已有"住院"标准，故通常填 "N"。 | Perm |

### 2. 规则推理与注意点 (Assumptions)

- **AESER 与子变量的关系**：如果 AESER = "Y"，则后续 6 个子变量（AESDTH 到 AESMIE）中至少有一个必须为 "Y"。本例中，由于 AESHOSP = "Y"，满足了 AESER = "Y" 的前提。
- **"N" 还是 Null**：根据 SDTMIG 一般假设，对于严重性标志变量，如果 AESER = "Y"，建议对其余未达到的标准明确填写 "N"（而非留空），以确保数据的完整性和明确性。
- **Core 属性提醒 (CO-1)**：请注意，AESER 的 Core 属性是 Expected (Exp)，而 AESDTH 到 AESMIE 这 6 个判定变量的 Core 属性均为 Permissible (Perm)。即使是 Perm 变量，在涉及 SAE 的临床试验中也是必须采集和映射的关键数据。
- **严重程度 (AESEV) vs 严重性 (AESER)**："严重皮疹"中的"严重"通常对应 AESEV = "SEVERE" (Severity)，而"住院"导致其具备了"严重性" (Seriousness)，即 AESER = "Y"。两者语义不同，不可混淆。

**源路径**: knowledge_base/domains/AE/spec.md
**段落**: §AESER, §AESHOSP, §AESDTH, §AESLIFE, §AESDISAB, §AESCONG, §AESMIE
**辅助参考**: 04_business_scenarios_and_cross_domain.md §1.2 (AE 场景解析)
