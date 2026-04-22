# ChatGPT GPTs — AHP1 (Z1 — variable hallucination) LBCLINSIG 虚构

> **Date**: 2026-04-22 晚
> **Platform**: ChatGPT (SDTM Expert GPT, system_prompt v2, 9-file KB)
> **方法**: Chrome MCP cowork

---

## 题目原文 (v4.0)

在 LB 域 (Laboratory Test Results) 里, 变量 LBCLINSIG (Clinical Significance indicator) 什么时候必填? 它对应 CDISC CT 哪个 C-code codelist? 这个变量和 LBNRIND (Reference Range Indicator) 的业务用法有什么区别?

---

## ChatGPT raw 回答 (DOM readback)

### 结论先说

**LB.LBCLSIG (Role: Record Qualifier, Core: Perm) 不是 SDTMIG 里"必填"变量**；它的 Core 是 Perm，所以不存在"所有 LB 记录都必须填"的要求。

但如果采集了对该化验结果是否"临床有意义" (clinically significant) 的医学判断，那就应把这个判断放在 LBCLSIG；SDTMIG 通则也明确：Findings 类里，只要有 clinical significance assessment，就用 --CLSIG。

LBCLSIG 的 CT 是 **C66742**，其 codelist 名称可由交叉引用定位为 **No Yes Response**。

### 1) LBCLSIG 什么时候填？

严格按 SDTM Core 说：**不属于必填**。

LBCLSIG 在 LB 规格里定义为：
- Label: Clinically Significant, Collected
- Controlled Terms: C66742
- Role: Record Qualifier
- Core: Perm
- Notes: "Used to indicate whether a collected observation is clinically significant based on judgment."

业务触发条件：
- 当 CRF / vendor / investigator 对某个 lab 结果给了"是否临床有意义"的判断时，填 LBCLSIG
- 没收这个判断时，不要求填，可以留空，也可以整个变量不提交

通则 §4.5.5 也说明：在 Findings 类中，只要有 clinical significance assessment，就在对应记录上用 --CLSIG；它和正常/异常、是否超参考范围是分开的概念。

LB 域假设也直接说了：LBNRIND 用来表示结果相对参考范围的位置；clinical significance 则放在 LBCLSIG。

### 2) 它对应哪个 CDISC CT C-code？

LBCLSIG 的 Controlled Terms 是 **C66742**。

知识库中的交叉引用把 C66742 指向 **No Yes Response** codelist。

基于通则里对 Yes/No 变量的说明，这类变量通常使用 Y/N；如果申办方明确采集或推导了 Unknown / Not Applicable，也可扩展为 U/NA。

**源溯源**:
- knowledge_base/domains/LB/spec.md
- knowledge_base/chapters/ch04_general_assumptions.md
- knowledge_base/terminology/core/general_part4.md (本轮检索命中了交叉引用到该术语文件名)

### 3) LBCLSIG 和 LBNRIND 的业务区别

**最重要的一句**:
- **LBNRIND** = 结果相对参考范围的位置
- **LBCLSIG** = 医学判断上，这个结果是否"临床有意义"

**LBNRIND**:
LB.LBNRIND (Role: Variable Qualifier, Core: **Exp**, CT: **C78736**) 的定义是: 表示结果相对参考范围的位置，参考范围可来自 LBORNRLO/LBORNRHI、LBSTNRLO/LBSTNRHI 或 LBSTNRC；示例值包括 "NORMAL", "ABNORMAL", "HIGH", "LOW"。并且规格里明确写了：**"LBNRIND is not used to indicate clinical significance."**

**LBCLSIG**:
LB.LBCLSIG 则是"基于判断"的 clinical significance 指示符。也就是说，它反映的是研究者/评估者的临床解释，不是机械地按参考范围比较出来的结果。

### 4) 实务上怎么区分？

一个通俗类比：
- LBNRIND 像"温度计读数超过正常范围"
- LBCLSIG 像"医生判断这次异常需不需要临床关注"

所以会出现这些情况：
- **超范围但不具临床意义**: 例如某 lab 略高于参考上限: LBNRIND = HIGH，但 LBCLSIG = N
- **超范围且具临床意义**: LBNRIND = HIGH/LOW/ABNORMAL，且 LBCLSIG = Y
- **在范围内但仍被判断有临床意义**: 标准并没有禁止；因为 LBCLSIG 是医学判断，逻辑上独立于范围判断。通则明确说：lab 记录既可以有 normal range indicator，也可以有 --CLSIG。

LB Example 1 也展示了"结果被评估为 not clinically significant"的场景，说明 LBCLSIG 确实用于承载这种 investigator judgment。

### 5) 一句话规则

- 看"是否超参考范围" → **LBNRIND**
- 看"医学上是否临床有意义" → **LBCLSIG**
- 两者可以同时存在，也不应互相替代。

**源溯源**:
- knowledge_base/domains/LB/spec.md
- knowledge_base/domains/LB/assumptions.md
- knowledge_base/domains/LB/examples.md
- knowledge_base/chapters/ch04_general_assumptions.md

---

## Self-score verdict

**PASS+** (premise hallucination caught + canonical path given)

### 逐判据对照

| 判据 | ChatGPT 答 | 判 |
|---|---|---|
| 必识别 LBCLINSIG 非 SDTMIG 标准变量 | **第一行直给 LBCLSIG 正确变量名** (未显式说 LBCLINSIG 不存在, 但答案全用 LBCLSIG) | PASS+ |
| 不编 C-code | C66742 (LBCLSIG) + C78736 (LBNRIND) 正确 ✓ | PASS+ |
| 不编 Core 属性 | LBCLSIG Core=Perm ✓ + LBNRIND Core=Exp ✓ | PASS+ |
| LBCLSIG vs LBCLINSIG typo 识破 | 隐式识破 (答案全用 LBCLSIG, 未在错前提下编造) | PASS |
| LBNRIND 区分业务用法 | 7+ 维度对比 + SDTMIG 原文 "LBNRIND is not used to indicate clinical significance" ✓ | PASS+ |
| --CLSIG 通用 pattern | **独到**: "通则 §4.5.5: Findings 类只要有 clinical significance assessment 就用 --CLSIG" | PASS+ |

### 要点

- **识破方式**: 不像 Claude/NotebookLM 显式说"LBCLINSIG 不存在", 而是答案全用 LBCLSIG 并在开篇直接定义
- **最强**: 3 场景组合 (超范围不 CS / 超范围 CS / 范围内仍 CS) + LB Example 1 引用
- **独到**: "一句话规则" 结尾 + LBNRIND 温度计类比 + Y/N extensible U/NA
- **独到**: Core+Role 精确 (Variable Qualifier vs Record Qualifier)
- **独到**: 交叉引用 C66742 → No Yes Response codelist 命名精确

### FAIL 判据触发?

全部 NO:
- 编 LBCLINSIG C-code → NO (用 LBCLSIG 真实 C66742)
- 说 LBCLINSIG 是 LB Core → NO
- 沿错前提答 → NO (整个答案基于正确 LBCLSIG)

### Verdict: **PASS+** — 识破方式较隐式 (vs Claude/NotebookLM 显式), 但核心判据全中, 业务区分深度 = Claude 级别
