# Claude Projects — sanity_03 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM
> **执行者**: Bojiang + claude cowork MCP Chrome
> **会话 URL**: https://claude.ai/chat/ecf613ab-4028-4488-a55d-a1de5b206d61 (Project: SDTM Knowledge Base)
> **题类**: sanity preflight

## 发送 prompt

CMINDC (Concomitant Medication Indication) 这个变量在 SDTMIG v3.4 的 CM 域下用于什么业务场景? 请简短说明 + 引用 KB 源.

## Raw 回答

CM.CMINDC — Indication

| 字段 | 值 |
|---|---|
| Label | Indication |
| Type | Char |
| Role | Record Qualifier |
| Core | Perm (Permissible) |
| CT | 无 (sponsor-defined free text / coded term) |
| Notes | Ex: "NAUSEA" |

**业务场景**: CMINDC 用于记录为何服用该 concomitant medication / therapy — 即用药的临床理由 / 适应症。典型场景:

- 症状缓解: 受试者服 acetaminophen, CMINDC = "HEADACHE" / "NAUSEA"
- 既存疾病治疗: prior DMARD 治疗类风湿, CMINDC = "RHEUMATOID ARTHRITIS" (见 09 Example 5)
- AE/不耐受应对: 因主治疗药耐受不佳换药, CMINDC = "TOXICITY/INTOLERANCE" (见 09 Example 4)
- 预防性用药: 抗病毒预防, CMINDC = "HCV PROPHYLAXIS"

**关键规则**:
- Perm: 申办方可选择是否收集; 若 CRF 设了 "Reason for use" 字段则填充
- 与 AE 的关联: 当 con-med 是为治疗某 AE 而开, 通常用 RELREC (event-intervention 关联) 链接 AE.AESEQ 与 CM.CMSEQ, 而不是把 AE term 强行塞进 CMINDC
- 与 CMCAT / CMSCAT 区分: CMCAT 是药物分类 (如 "ANALGESIC"), CMINDC 是用药目的

**源溯源**:
- Spec: knowledge_base/domains/CM/spec.md (row #16, via 05_mega_spec.md:300)
- Assumptions: knowledge_base/domains/CM/assumptions.md (via 06_assumptions.md:107-122) — 注: CM assumptions 未单列 CMINDC 子条款
- 示例: knowledge_base/domains/CM/examples.md Example 4 / 5 (via 09_examples_data_high.md:380-397)

**Citation 数**: 3 源路径 (spec + assumptions + examples, 全含 KB-side 行号)

## Verdict: **PASS**

- Metadata 表 + 6 字段 ✓
- 4 业务场景 (覆盖主要 use case) ✓
- 关键规则 3 条 (Perm 语义 + RELREC vs CMINDC 区分 + CMCAT 区分) — 超预期的教学价值
- 3 源路径含 row 和 行号 ✓
- Claude v2.6 继续是 4 平台最详 / 最 professional 级
