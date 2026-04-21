# Q10 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/cf10a3d03d44ed44
> Mode: Pro
> Run: 2026-04-21

## 原题
一位受试者的某次 AE (头晕) 被 Investigator 判定和某合并用药 (复方降压药) 引起的血压下降有关. 这种"AE 由 CM 引起"的关联, 应该用 RELREC (Related Records) 记录, 还是用 SUPPAE / SUPPCM 存储? 解释两者的差异 (RELREC 负责什么 / SUPPAE/SUPPCM 负责什么), 说明本场景的选择理由.

## 答案全文

### 结论

在这种"AE 由 CM 引起"的关联场景中，应当使用 **RELREC (Related Records) 记录**，而不是使用 SUPPAE 或 SUPPCM。

### 差异解释与选择理由

#### 1. RELREC 与 SUPP-- 的功能差异

**RELREC (Related Records)**:
- 核心功能：负责描述记录与记录之间 (Record-to-Record) 的关系。
- 机制：它通过 IDVAR (标识变量名，如 "AESEQ") 和 IDVARVAL (标识变量值，如 "1")，将一个域中的某条记录与另一个域中的某条记录（或多条记录）关联起来。
- 适用场景：两个或多个已存在于标准域中的记录之间存在临床逻辑关联（如：AE 与 CM 的因果关系、LB 与记录干预的关联等）。

**SUPPAE / SUPPCM (Supplemental Qualifiers)**:
- 核心功能：负责存储非标准变量 (Non-Standard Variables, NSVs)。
- 机制：它是对单体记录属性的水平扩展。如果某个属性在标准域 spec 中没有对应的变量，则放入 SUPP--。
- 适用场景：记录某条 AE 的额外信息（如：AE 的具体发生部位，若标准域无空间存储），而不是用来链接另一条独立的记录。

#### 2. 本场景的选择理由

- **记录的独立性**："头晕" 已经在 AE 域有一条记录，"复方降压药" 已经在 CM 域有一条记录。该业务问题的核心是建立这两条既有记录之间的映射/链接。
- **SDTMIG 规定**：根据 SDTMIG v3.4 章节 §4.1.8.1 的通用假设，RELREC 域专门用于标识两个或多个域中相关记录之间的关系。
- **避免冗余**：虽然可以在 SUPPAE 中通过非标准变量记录 CM 的名称，但这会导致数据冗余且无法实现程序上的自动追溯。通过 RELREC 指向 CMSEQ 是 CDISC 推荐的标准做法。

### 业务映射建议

在 RELREC 中，您需要创建一条记录：

- 指向 AE 记录：IDVAR = "AESEQ", IDVARVAL = [该 AE 的序列号]
- 指向 CM 记录：IDVAR = "CMSEQ", IDVARVAL = [该 CM 的序列号]
- 定义关系类型：RELTYPE 可填入类似 "CAUSAL" 或根据试验要求定义的术语。

**源路径**:
- knowledge_base/chapters/ch04_general_assumptions.md §8.1 Related Records (RELREC)
- knowledge_base/business_scenarios/04_business_scenarios_and_cross_domain.md §1.10 (AE 与 CM 关联场景) 及 §4.1 (RELREC vs SUPP-- 决策树)
