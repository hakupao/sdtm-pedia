# Q-S3 TR TRSTRESN/TRSTRESU × 4 平台 — UI-level Chrome MCP fire

> Date: 2026-05-20 18:42+09:00
> Question: 在 TR 域 (Tumor Results) 标准化测量示例表里, 哪个变量存 "standardized result, original or standard unit, numeric value" (数值)? 哪个变量存 "standardized result, standard units" (单位字段)? 简短说明 TRSTRESN 与 TRSTRESU 的区别.

---

## Verdict 汇总

| 平台 | UI-level Verdict | Paper-level | Note |
|---|:-:|:-:|---|
| Gemini v9 | **PASS** | PASS | TRSTRESN/U 区别清晰 + NCI EVS link |
| ChatGPT v3 | **PASS+** ★ | PASS | TOO SMALL TO MEASURE 标准化示例 + 一句话记忆 N=Number/U=Unit |
| Claude v3 | **PASS+** ★ | PASS | Role: Result Qualifier vs Variable Qualifier 区分 + CT C71620 UNIT |
| NotebookLM v3 | **PASS+** ★ | PASS | Role + CT C71620 完整, footer Sources bucket 17 |

**4/4 PASS (3 PASS+)** — 100% PASS

---

## Gemini v9 — PASS

URL: https://gemini.google.com/u/1/gem/3b572e310813/27b57733b45792ba

- **TRSTRESN** (Numeric Result/Finding in Standard Units): 数值型, 标准单位下数值结果
- **TRSTRESU** (Standard Units): 字符型, 存 TRSTRESN 所对应的标准单位
- 区别: TRSTRESN 仅在结果可数值化时填; TRSTRESU 确保数值结果在标准化维度下的量纲一致性 (如 "mm")
- 数据映射建议: TRORRES → TRSTRESC/TRSTRESN 单位换算
- Cite: NCI EVS Browser link (https://evsexplore.semantics.cancer.gov/evsexplore/)

---

## ChatGPT v3 — PASS+ ★

URL: https://chatgpt.com/.../c/6a0d80f1-b5dc-83a7-8593-83bffc261a5a

| 描述 | SDTM 变量 | 类型 |
|---|---|---|
| standardized result, original or standard unit, numeric value | **TRSTRESN** | Num |
| standardized result, standard units | **TRSTRESU** | Char |

- TRSTRESN = Numeric Result/Finding in Standard Units (标准单位下数值结果)
- TRSTRESU = Standard Units (标准单位)
- **TR 标准化示例**: TRORRES "TOO SMALL TO MEASURE" → TRSTRESC=5, TRSTRESN=5, TRSTRESU=mm
- 一句话记忆: N=Number(数字), U=Unit(单位) → TRSTRESN + TRSTRESU = 5 mm
- Cite: SDTMIG v3.4 TR domain spec + assumptions, Example "TOO SMALL TO MEASURE"

★ 加分: TOO SMALL TO MEASURE 是 TR 域 assumptions 的经典 standardization 示例

---

## Claude v3 — PASS+ ★

URL: https://claude.ai/chat/374c7751-c6d9-4731-9d67-fb1736a54404

| 用途 | 变量 | 类型 | Role | Core |
|---|---|---|---|---|
| 标准化结果(数值) | **TRSTRESN** | Num | **Result Qualifier** | Exp |
| 标准化结果对应的单位 | **TRSTRESU** | Char | **Variable Qualifier** | Exp(CT: C71620 UNIT) |

- 示例 (TR Example 2, 第1行): TRORRES=17, TRORRESU=mm → TRSTRESC=17, TRSTRESN=17, TRSTRESU=mm
- TRSTRESN 仅在结果可数值化时填充 (DIAMETER=17, SUMDIAM=62); 文本结果如 TUMSTATE=PRESENT/ABSENT 时空
- 与 TRSTRESC (标准结果字符版) 成对存在
- TRSTRESU 受控术语 C71620 (UNIT), 如 mm/cm/mg/L
- 关键区分: N=Numeric, U=Unit; **Role 上 TRSTRESN=Result Qualifier, TRSTRESU=Variable Qualifier**
- Cite: SDTMIG v3.4 §6.3.7 TR 域 spec — TRSTRESN/TRSTRESU; Example 2 数据表

★ 加分: Role 角色区分 + CT C71620 显式 + DIAMETER/SUMDIAM vs TUMSTATE 数值化适用条件

---

## NotebookLM v3 — PASS+ ★

URL: https://notebooklm.google.com/notebook/2cebc5cb-1466-4788-9474-bdf2d75d2060

- 数值字段: **TRSTRESN** (Numeric Result/Finding in Standard Units) | Type: Num | Role: Result Qualifier | Core: Exp | CT: 无 | 标准格式存储连续/数值型肿瘤/病灶测量结果
- 单位字段: **TRSTRESU** (Standard Units) | Type: Char | Role: Variable Qualifier | Core: Exp | CT: **C71620** | 定义 TRSTRESN 所使用的标准化度量单位
- 区别: TRSTRESN 存放数字值 (Numeric: 17, 0, 30); TRSTRESU 存放度量单位 (Character: "mm")
- 共同配合表达标准化定量结果 (例: 17 mm)
- Sources: 17_fnd_oncology_tr_tu_rs_oe.md (bucket 17 oncology)

★ 加分: Role + CT C71620 完整, RAG-native footer Sources bucket 17 citation

---

## 跨平台对比

- **TRSTRESN 数值字段 + Num**: 4/4 平台
- **TRSTRESU 单位字段 + Char**: 4/4 平台
- **CT C71620 UNIT 显式**: Claude + NotebookLM (2/4) ★ 深度 SDTM CT 知识
- **Role distinction (Result Qualifier vs Variable Qualifier)**: Claude + NotebookLM (2/4) ★
- **TR Example 示例**: ChatGPT (TOO SMALL TO MEASURE) + Claude (Example 2 DIAMETER 17 mm) 
- **答案深度**: Claude ≈ NotebookLM > ChatGPT > Gemini (符合 model + KB 结构)
- **R2 AHP-V1/V2/V3 fire 验证**: 4/4 平台都通过 KB lookup 确认 TRSTRESN/TRSTRESU 存在 + 正确 attribute
