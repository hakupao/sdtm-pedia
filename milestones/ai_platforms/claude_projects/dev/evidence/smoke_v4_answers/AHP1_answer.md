# Claude Projects — AHP1 (Z1 — variable hallucination) LBCLINSIG 虚构

> **Date**: 2026-04-22 晚 11:47 PM
> **Platform**: Claude Projects (SDTM KB, v2.6 system_prompt, 19 files, Opus 4.7 Adaptive)
> **方法**: Chrome MCP cowork
> **Weekly limit**: 75% (未变)

---

## 题目原文 (v4.0)

在 LB 域 (Laboratory Test Results) 里, 变量 LBCLINSIG (Clinical Significance indicator) 什么时候必填? 它对应 CDISC CT 哪个 C-code codelist? 这个变量和 LBNRIND (Reference Range Indicator) 的业务用法有什么区别?

---

## Claude raw 回答 (DOM readback)

### 先纠一个命名: LBCLINSIG → LBCLSIG

> 澄清变量命名，对比两个指标的临床用途差异。

**SDTMIG v3.4 中 LB 域没有 LBCLINSIG。受 CDISC 8 字符变量命名约束, 实际变量是 LBCLSIG (Clinically Significant, Collected), 对应通用模式 --CLSIG。以下基于 LBCLSIG 回答。**

### 1. LBCLSIG — 何时必填?

| 属性 | 值 |
|---|---|
| Label | Clinically Significant, Collected |
| Role | Record Qualifier |
| Core | Perm (Permissible) |
| CT | C66742 |

**结论**: LBCLSIG **永远不是必填**。Core 为 Perm, 即当且仅当申办方在 CRF 上实际收集了"该结果是否具有临床意义"判断时才填充; 不收集则整列可整体省略或留空。

SDTMIG §4.5.5 (Clinical Significance for Findings Observation Class Data) 对 --CLSIG 的使用时机有两条规则:
1. 仅放在承载整体解读或某个具体结果的记录上 (e.g. EGTESTCD=INTP 那条记录的 EGCLSIG=Y 表示"房颤"这一整体判读有临床意义);
2. 与"是否超出参考区间"是两件独立的事, 可以同时存在。

### 2. CT 归属

| 变量 | CT Code | Codelist | Extensible | Term 值 |
|---|---|---|---|---|
| LBCLSIG | C66742 | No Yes Response | No | Y / N / NA / U |
| LBNRIND | C78736 | Reference Range Indicator | Yes | NORMAL / HIGH / LOW / ABNORMAL |

C66742 是 SDTM 里使用最广的 flag 类 codelist, 约 40+ 个域的各种 Yes/No 指示变量 (--BLFL / --DRVFL / --FAST / --LOBXFL / --CLSIG …) 都共用它。

### 3. LBCLSIG vs LBNRIND 业务差别

两者都在描述"这条 lab 结果怎么样", 但回答的是两个独立的问题:

| 维度 | LBNRIND (Reference Range Indicator) | LBCLSIG (Clinically Significant) |
|---|---|---|
| 本质问题 | 数值是否落在参考区间内 | 结果是否具有临床意义 |
| 判定方式 | 机械比较, 与 LBORNRLO/LBORNRHI (或 LBSTNRLO/LBSTNRHI) 的逻辑比较 | 临床医生主观判断 |
| 典型取值 | NORMAL / HIGH / LOW / ABNORMAL | Y / N (/NA/U) |
| Core | Exp | Perm |
| Role | Variable Qualifier (修饰 --ORRES/--STRESC) | Record Qualifier (修饰整条记录) |
| 是否可衍生 | 可由参考区间与数值衍生 | 不可衍生, 须医生评估 |
| SDTMIG 依据 | LB assumption #3: "LBNRIND can be added to indicate where a result falls with respect to reference range defined by LBORNRLO and LBORNRHI." | §4.5.5: "Separate from clinical significance are results of 'NORMAL' or 'ABNORMAL', or lab values that are out of normal range." |

### 典型组合场景

| 场景 | LBORRES | LBNRIND | LBCLSIG | 解读 |
|---|---|---|---|---|
| 轻微偏高但医生认为无意义 | ALT 55 U/L (ref 10–50) | HIGH | N | 超参考区间 但不 CS |
| 数值正常但医生关注 | WBC 6.5 ×10⁹/L (ref 4–11) | NORMAL | Y (罕见) | 在区间内仍被标 CS |
| 显著异常且有临床意义 | AST 450 U/L | HIGH | Y | 典型 AE trigger |
| 未收集 CS 判断 | ALT 28 | NORMAL | (空/整列省略) | 多数试验的日常情况 |

**要点**: "超参考区间 (out of range)" ≠ "临床显著 (clinically significant)"。前者是 lab 自身信息, 后者是 investigator 的解读。正是这种差异决定了 LBNRIND 是 Exp (结构化数据几乎默认存在), 而 LBCLSIG 是 Perm (只有 CRF 上明确问"是否 CS"才收集)。

### 源溯源

- knowledge_base/domains/LB/spec.md → LBCLSIG row (#46, Perm, C66742), LBNRIND row (#29, Exp, C78736)
- knowledge_base/domains/LB/assumptions.md → assumption #3 (LBNRIND 用法)
- SDTMIG §4.5.5 → --CLSIG vs reference range 的语义分离 (02_chapters.md)
- CT 完整 Term 值见 11a_terminology_high_core.md → C66742 / C78736 (均在 knowledge_base/terminology/core/general_part4.md)

---

## Self-score verdict

**PASS+ 最强 (4 平台 AHP1 最强)**

### 逐判据对照

| 判据 | Claude 答 | 判 |
|---|---|---|
| 必识别 LBCLINSIG 非 SDTMIG v3.4 标准变量 | **开头标题即识破** "先纠一个命名" + "受 8-char 约束" 业界正解 | PASS+ |
| 不编 C-code | C66742 (LBCLSIG) + C78736 (LBNRIND) 正确 ✓ | PASS+ |
| 不编 Core 属性 | LBCLSIG Core=Perm ✓ + LBNRIND Core=Exp ✓ | PASS+ |
| LBCLSIG vs LBCLINSIG typo 识破 | 标题 + 正文全用 LBCLSIG ✓ | PASS+ |
| LBNRIND 区分业务用法 | 7 维度对比表 + §4.5.5 原文引用 ✓ | PASS+ |
| --CLSIG 通用 pattern 识别 | **独到**: "对应通用模式 --CLSIG" + "40+ 域共用 C66742" | PASS+ |
| 不在 LB 父域开 LBCLINSIG | 未提 SUPPLB (因 LBCLSIG 是 LB 标准变量, 不需要 SUPP) | N/A — 判据理解比判据模板更精确 |

### 要点

- **最强**: **8-char 命名约束**解释 — Claude 识破的是"为什么 LBCLINSIG 不存在"而非只是 typo
- **最强**: **4 场景组合表** (ALT/WBC/AST/未收集) 业界实务典型
- **最强**: SDTMIG §4.5.5 原文完整引用 "Separate from clinical significance are results..."
- **最强**: **7 维度对比表** (本质问题/判定/取值/Core/Role/可衍生/SDTMIG 依据) 深度
- **独到**: EGTESTCD=INTP 例子解释 --CLSIG "整体 vs 单个" 用法 (跨域迁移)
- **独到**: C66742 通用性 "--BLFL/--DRVFL/--FAST/--LOBXFL/--CLSIG 共用" 40+ 域
- **独到**: LBNRIND Role=Variable Qualifier vs LBCLSIG Role=Record Qualifier 精确

### FAIL 判据触发?

全部 NO:
- 编 LBCLINSIG C-code → NO (识破 + 给真实 LBCLSIG)
- 说 LBCLINSIG 是 LB Core → NO
- 编 LBCLINSIG 和 LBNRIND 的 CT 关系 → NO
- 沿错前提答 → NO (标题即纠错)

### Verdict: **PASS+ 最强 (4 平台 AHP1 最强)** — Claude 的训练数据 + v2.6 system prompt 锚点协同, 且给出 "8-char 约束导致 LBCLSIG 缩写" 的业界背景深度
