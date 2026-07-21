# Q9 — SUPPAE 边界 + QNAM/QLABEL/QVAL 示例 (v2.1)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e741ef-08ac-83a4-8775-d76366805f06
**Date**: 2026-04-21
**Thought for**: 3m 4s

## 原题

SUPPAE (Supplemental Qualifiers for AE) 的作用是什么? 什么情况下应该走 SUPPAE 而不是直接加 AE 域变量? 请举一个典型例子, 给出 QNAM / QLABEL / QVAL 三字段的完整示例 (场景自选, 无需 NCI Code).

## ChatGPT 答案 (完整)

**结论**:

**SUPPAE 的作用**: 把同一条 AE 记录上的非标准补充字段 (non-standard variables, NSVs) 单独存成一条或多条 supplemental qualifier 记录, 再通过父记录键值回连到 AE. SDTM 明确说**不能在标准域里随意新增 sponsor-defined 变量**; 这类补充信息要放进 SUPP--, 并用 **QNAM / QLABEL / QVAL** 来表达变量名、标签和值. SUPP-- 记录还带 QORIG / QEVAL, 并通过 STUDYID / RDOMAIN / USUBJID / IDVAR / IDVARVAL 关联到父记录.

### 什么时候走 SUPPAE, 而不是直接往 AE 加变量

1. **如果 SDTM/AE 已有标准变量能装, 就用标准变量, 不用 SUPPAE**.
   例如 AESEV, AESER, AEREL, AEACN, AESTDTC 这类, 属于标准 AE 变量; Permissible 变量只要研究里确实采集了, 也应直接放进 AE, 而不是绕到 SUPPAE.

2. **如果没有标准变量, 但它只是"这条 AE 的补充限定信息", 就用 SUPPAE**.
   典型就是 CRF 上的 "Other, specify" 自由文本, 用来补充某个标准非结果型 qualifier. SDTMIG 明确说, 这类 free-text specify 应放进 SUPP--.

3. **如果它其实是"另一条观察", 就不要用 SUPPAE**.
   SUPP-- 只适合"补充限定信息", 不能拿来替代独立观察. 指南明确写了: 如果数据代表单独观察, 就应作为单独观察建模.

### 典型的 AE 场景

**场景**: CRF 里有 AESMIE (Other medically important serious event?) = Y, 并且还收了一个自由文本说明: "为什么它算 medically important serious AE?"

- AESMIE 这个标准判断标志, 应放在 AE.AESMIE
- 但那段补充说明文本, AE 里没有标准变量可装
- 所以这段文本应走 SUPPAE

**SUPPAE 记录示例**:

| 字段 | 示例值 |
|------|-------|
| STUDYID | ABC123 |
| RDOMAIN | AE |
| USUBJID | ABC123-001 |
| IDVAR | AESEQ |
| IDVARVAL | 7 |
| **QNAM** | **AESMDESC** |
| **QLABEL** | **Other MIE Description** |
| **QVAL** | **HIGH RISK OF AIRWAY OBSTRUCTION** |
| QORIG | CRF |
| QEVAL | |

**核心 3 字段 (判据要求)**:
- **QNAM = AESMDESC**
- **QLABEL = Other MIE Description**
- **QVAL = HIGH RISK OF AIRWAY OBSTRUCTION**

### 为什么这个例子应该走 SUPPAE

- 它不是新的 AE 事件
- 也不是 AE 现有标准变量能承载的内容
- 它只是对这条 AE 的一个补充说明, 所以属于 supplemental qualifier

这和 SDTMIG 对 AE 的说明一致: 当收集了 "Other medically important serious adverse event" 的描述时, 应放到 SUPPAE, 而不是在 AE 里自定义一列.

### 一句话判断法

1. AE 里已有标准变量吗? 有, 就放 AE.
2. 没有标准变量, 但只是补充说明 / 补充限定吗? 是, 就放 SUPPAE.
3. 其实是另一条观察或另一时点的信息吗? 是, 就建新 AE 记录或用 FA/其他合适域, 不要放 SUPPAE.

### 源溯源

- `knowledge_base/domains/SUPPQUAL/assumptions.md`
- `knowledge_base/chapters/ch04_general_assumptions.md`
- `knowledge_base/domains/AE/assumptions.md`

## 判据对齐 (v2.1)

- ✅ SUPPAE 存放**标准 AE 域未定义的补充变量** (NSV 核心定义)
- ✅ "标准 AE 变量能放下的不走 SUPPAE" (避免重复, 已点出)
- ✅ 典型例子合格: QNAM = AESMDESC / QLABEL = Other MIE Description / QVAL = HIGH RISK OF AIRWAY OBSTRUCTION (SDTMIG AE "Other MIE" 经典场景, 完美命中 PASS 判据第二种类型)
- ✅ QNAM / QLABEL / QVAL 三字段完整 + 语义对 (short name / label / 实际值)
- ✅ RDOMAIN / USUBJID / IDVAR / IDVARVAL 内部结构变量列出 (加分, 体现 SUPP-- 连接机制)
- ✅ QORIG / QEVAL 也列 (完整度超出判据基线)
- ✅ "一句话判断法" 3 步决策树 (加分, 实务价值高)
- ✅ 拒绝"独立观察"用 SUPP-- (SDTMIG 原文边界命中)
- ✅ 引 3 源 (SUPPQUAL/assumptions + ch04 + AE/assumptions)

## Verdict: **PASS** (1/1)

## 归因

系统 prompt v2.1 + SUPPQUAL + AE knowledge 命中: SUPPAE 作用完整定义 + "何时用 SUPPAE" 三条判断准则 + "Other MIE Description" 经典示例完整 (QNAM/QLABEL/QVAL 三字段无误) + 完整 SUPPAE 记录结构 (STUDYID/RDOMAIN/USUBJID/IDVAR/IDVARVAL/QORIG/QEVAL) + "独立观察不走 SUPPAE" 边界 + 一句话判断法决策树. 3 源溯源完整.
