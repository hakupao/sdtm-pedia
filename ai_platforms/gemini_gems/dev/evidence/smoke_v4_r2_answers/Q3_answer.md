# Gemini Gems — Q3 BE + BS + RELSPEC 生物样本链 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/94b9e11ebf24910e
> **题类**: Q3 (A3 v3.4 新域 BE + BS + RELSPEC)
> **R1 baseline**: PASS

## Raw 回答 (DOM 原文)

**(a) 行为阶段 → BE 域** (Biospecimen Events):
- 采血 → BECAT="COLLECTION"
- 运输 → BECAT="TRANSPORT"
- DNA 提取 → BECAT="EXTRACTION" 或 "PREPARATION"

**(b) 测量值 → BS 域** (Biospecimen Findings):
- 体积 5 mL: BSTESTCD="VOLUME", BSTEST="Volume"
- RIN 9.2: BSTESTCD="RIN", BSTEST="RNA Integrity Number"
- CT: C124300

**(c) BS-001 → DNA-001 派生关系 → RELSPEC** (Relationship Between Specimens, 非 RELREC):
- REFID 字段建立父子样本 ID 关联
- RELREC 用途: 不同 observation class 间的通用关联
- RELSPEC 用途: 专门描述样本派生/层级关系 (v3.4 PGx 合并后新)

**总结表**: BE (BETERM Topic + BECAT Category) / BS (BSTESTCD / BSTEST Topic) / RELSPEC.

**双域并行注**: 采血动作记 BE + 采血量测量记 BS (两者并行不互斥).

**Deprecated 提醒 (CO-5 AHP-V3 主动)**: 请勿记入 PF 域, PF 在 v3.4 已废弃, GF/BE/BS 替代.

**源路径**: knowledge_base/domains/BE/spec.md + BS/spec.md (C124300) + 04_business_scenarios_and_cross_domain.md §BE vs BS 边界硬锚

## Self-score verdict

**PASS+** — (a) 三段均 BE ✓ + BECAT 三值 ✓ / (b) BS + BSTESTCD + C124300 ✓ / (c) RELSPEC 正确 (避开 RELREC pit) + 双域并行声明 ✓ + AHP-V3 PF deprecation 主动锚 ✓

**R1 vs R2 对比**: 对齐 PASS. R2 加分: (1) BETERM 在总结表显式列 Topic 身份 (R1 可能 implicit); (2) C124300 CT 码显式; (3) 主动 AHP-V3 PF 识破 (v6 CO-5 工作). 无 regression.
