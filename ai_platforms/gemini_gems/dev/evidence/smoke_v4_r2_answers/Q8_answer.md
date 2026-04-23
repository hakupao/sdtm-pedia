# Gemini Gems — Q8 CT Extensible vs Non-Ext + AETERM (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/5fc2d9552a608b6e
> **题类**: Q8 (D1 CT, R1 PARTIAL)
> **R1 baseline**: PARTIAL (NY 仅 Y/N + C66767 错 Ext=Yes + AETERM MedDRA 绑定位置错)
> **v6 target fix**: CO-2e 新增 (C66742 4 值 Y/N/U/NA + C66767 Non-Ext) + AETERM not CDISC CT 澄清

## Raw 回答

- **(a)** Ext=No 封闭 (不得 sponsor 加, 需向 CDISC 提变更); Ext=Yes 开放 (sponsor 可加, 不冲突现有)
- **(b)** Non-Ext 例: **AESER C66742 {Y, N, U, NA}** ✓ / **AEACN C66767** ✓ (DOSE NOT CHANGED etc); Ext 例: **LBTESTCD C65047** / **UNIT C71620**
- **(c)** AESEV: CDISC CT **C66769 Non-Ext** {MILD, MODERATE, SEVERE} 直接填 SDTM; AETERM: **不受 CDISC CT 约束**, 受**外部字典 MedDRA**, AETERM=reported term, 标准化术语在 **AEDECOD** (MedDRA Preferred Term). Define-XML: AEDECOD 指向 **ExternalCodeList** (MedDRA name/version/language), 非 CodeList
- **(d)** Define-XML 扩 LBTESTCD: CodeList 节点含 CDISC 标准术语 + 自定义 EnumeratedItem (通常无 NCI Code) + Extensible=Yes 属性 + LBTEST↔LBTESTCD 一致性 check

**源路径**: ch04 §4.1.2.10 + AE/spec §AESER/§AESEV/§AETERM + LB/spec §LBTESTCD + 04 §3.1

## Self-score verdict

**PASS+** — **R1 PARTIAL → R2 PASS+ 修复全线生效**

1. ✅ **v6 CO-2e 修 NY 4 值**: "仅 Y, N, U, NA" vs R1 "仅 Y/N" defect
2. ✅ **v6 CO-2e 修 C66767 Non-Ext**: 正确标 AEACN C66767 Non-Ext vs R1 错 Ext=Yes
3. ✅ **AETERM MedDRA 边界**: 明确 AETERM 不受 CDISC CT + AEDECOD 绑 MedDRA Preferred Term + ExternalCodeList Define-XML 机制
4. ✅ Define-XML CodeList + EnumeratedItem + Extensible=Yes 声明完整

**R1 vs R2**: PARTIAL → PASS+. **v6 Q8 micro-fix (CO-2e + AETERM 分层) 全线修复 R1 3 defects**.
