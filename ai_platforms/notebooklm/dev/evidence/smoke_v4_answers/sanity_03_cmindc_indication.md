# NotebookLM — sanity_03 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM
> **执行者**: Bojiang + claude cowork MCP Chrome (fill tool via uid)
> **会话 URL**: https://notebooklm.google.com/notebook/3f87a93e-9a65-407e-8292-c28706fc6287
> **题类**: sanity preflight

## 发送 prompt

CMINDC (Concomitant Medication Indication) 这个变量在 SDTMIG v3.4 的 CM 域下用于什么业务场景? 请简短说明 + 引用 KB 源.

## Raw 回答

在 SDTMIG v3.4 的 CM (Concomitant/Prior Medications) 域下，变量 CMINDC 的属性与业务场景如下:

- Label: Indication
- Type: Char
- Role: Record Qualifier
- Core: Perm
- CT: 无 (未指定标准 Codelist)

业务场景 (Purpose): CMINDC 用于记录受试者服用或被给予该合并用药/治疗的原因（例如: "NAUSEA", "HYPERTENSION") [06_int_concomitant_cm_ag_ml.md]。在数据收集场景中，它可以用来承载 CRF 上收集的适应症信息; 如果是勾选了 "Other, specify" 产生的自由文本 (如 "BROKEN ARM")，通常也存入此变量。若申办方需要对适应症进行编码，可以将编码后的标准词填入 CMINDC，而将原始文本存入 SUPPCM [29_ig_ch04_general_assumptions.md]。

引用来源: [06_int_concomitant_cm_ag_ml.md], [29_ig_ch04_general_assumptions.md]。

**Citation 数**: 2 条 (bucket 06 CM + bucket 29 ch04 assumptions)

## Verdict: **PASS**

- 业务场景清晰 ✓ (indication of con-med)
- 具体示例 "NAUSEA", "HYPERTENSION" ✓
- CRF "Other, specify" 处理规则 ✓
- SUPPCM 编码/原文分离工作流 ✓
- 2 citation (跨 domain 文件 + ch04 assumptions) ✓
