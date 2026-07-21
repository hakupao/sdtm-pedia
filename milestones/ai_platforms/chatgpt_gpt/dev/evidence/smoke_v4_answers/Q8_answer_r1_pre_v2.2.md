# ChatGPT Q8 answer — CT Extensible + MedDRA binding

**Verdict**: PASS+

## (a) Extensible=Yes vs No
- **Ext=No**: submission values 封闭, sponsor 不能加新值, 完全按 CDISC/NCI 发布值集用
- **Ext=Yes**: 优先 CDISC 标准值, 不够时 sponsor 可扩, study-specific permissible set 在 Define-XML 说明

## (b) 例子
**Non-Extensible** (必按 CDISC 用):
- AE.AESEV → **C66769** Severity/Intensity (MILD/MODERATE/SEVERE)
- AE.AEOUT → **C66768** Outcome of Event (RECOVERED/RESOLVED, FATAL, UNKNOWN...)
- 可补 AE.AEACN → C66767

**Extensible** (允许扩):
- AE.AEACNDEV → **C111110** Device Events Action Taken
- Treatment Intent → **C124307**
- 补: Marital Status Response → C76348

## (c) AETERM vs AESEV — 不是同类 CT 值

| 变量 | Role | Core | Controlled Terms | 来源 |
|---|---|---|---|---|
| AE.AETERM | Topic | Req | **空白** | verbatim, 研究者/站点原话 |
| AE.AEDECOD | Synonym Qualifier | — | **MedDRA** | 字典派生 preferred term |
| AE.AELLT/AEPTCD | — | — | MedDRA | 字典 hierarchy |
| AE.AESEV | Record Qualifier | Perm | **C66769** | CDISC CT coded |

**关键**: AETERM 不绑任何 CT, MedDRA 绑的是 AEDECOD/AELLT/AEPTCD 等字典派生变量.

### General Assumption 结构支持
- Events: topic = --TERM (verbatim)
- Findings: topic = --TESTCD (用 CT)
- Interventions/Events verbatim 若编码修改 → --MODIFY
- 字典编码结果 → --DECOD

**用户 prompt 里"AETERM 实际用 MedDRA"更精确应是**: "AE 是用 MedDRA 编码, 但 verbatim 在 AETERM, MedDRA 派生值在 AEDECOD/AELLT/AEPTCD" — ChatGPT 正确纠偏.

## (d) Sponsor 扩 LBTESTCD 时 Define-XML 要做什么

### 背景
- LB.LBTESTCD (Topic, Req) 绑 **C65047**, ≤8 字符
- LB.LBTEST (Synonym Qualifier, Req) 绑 **C67154**, ≤40 字符

### Define-XML 要求
1. 为 LBTESTCD 定义 study-specific codelist (含标准 CDISC + sponsor 新增)
2. 每个 sponsor-added LBTESTCD 给对应 LBTEST (成对一致)
3. 只列 study 计划允许的值 (不塞整个 codelist)
4. metadata 说明 origin / 定义
5. 若同一变量 collected + derived 混用 → value-level metadata 区分

### 建模提醒
- **"Other, specify" 不能直接把 verbatim 丢进 LBTESTCD**: 要先编码 (e.g. verbatim "Prothrombin time" → LBTESTCD="PT", LBTEST="Prothrombin Time")
- **不要把过多属性塞 LBTESTCD**: 不推荐 location/method/laterality/machine 揉进 code, 用 generic test code + qualifier variables 表达

## 源溯源
- ch04_general_assumptions.md (Controlled terminology / Define-XML 通则)
- AE/spec.md (AE 变量定义)
- AE/assumptions.md (AE 业务规则)
- terminology/core/ae.md (AE codelists)
- LB/spec.md (LB 变量定义)
- terminology/questionnaires/questionnaires_part1.md (Ext 例子)

## 评分要点
- ✓ (a) Ext=No / Yes 语义完整 + Define-XML 机制
- ✓ (b) 2+2 例子 C-code 全对 (C66769/C66768, C111110/C124307)
- ✓ (c) **AETERM 不绑任何 CT** 关键判断正确 + 精确纠用户 prompt "AETERM 用 MedDRA" 错误描述
- ✓ (c) MedDRA 绑 AEDECOD/AELLT/AEPTCD 明确
- ✓ (d) Define-XML 5 条 + 2 条建模提醒 (Other specify 必编码, 不塞属性)
- ✓ C65047 + C67154 + 长度限制
