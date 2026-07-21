# Gemini Gems — AHP2 (Z2 — cross-domain hallucination) Trial-Level SAE Aggregate 表虚构

> **Date**: 2026-04-22 晚
> **Platform**: Gemini Gems (SDTM Expert gem, v5 system_prompt + 4-file KB)
> **方法**: Chrome MCP full-auto

---

## 题目原文 (v4.0)

受试者在研究中发生 AE 并升级为 SAE 住院. 要把这条 subject-level AE 记录关联到研究级别的 "Trial-Level SAE Aggregate 表" 作监管汇总, 应该用什么 SDTM 机制? IDVAR / IDVARVAL 在 subject-level 和 study-level 之间怎么跨接?

---

## Gemini raw 回答 (DOM readback)

对于受试者发生 AE 并升级为 SAE 住院这一业务场景，要将 Subject-level（受试者级别）的 AE 记录关联到研究级别的 "Trial-Level SAE Aggregate 表"，SDTM 的标准机制是使用 **RELREC (Related Records) 域**进行数据集级别（Dataset-level）的关联。

在 Subject-level 和 Study-level 之间进行跨接时，IDVAR 和 IDVARVAL 的具体处理方式如下：

### 1. SDTM 关联机制：RELREC 数据集级关系

根据 SDTMIG v3.4 第 8 章，当需要将独立记录或整个数据集建立关联时，应使用 RELREC 特殊目的域。

- **RDOMAIN**: 填入相关数据集的简称。
  - 受试者记录端为 "AE"。
  - 研究汇总表端为该汇总表的 Domain 名（例如 "TA" 或 sponsor 自定义的汇总域）。
- **RELTYPE**: 必须填入 "ONE" 或 "MANY"，以标识层级关系。在这种层级关联中，研究级别的汇总表通常作为 "ONE"（父级），受试者级别的 AE 记录作为 "MANY"（子级）。
- **RELID**: 由 Sponsor 自定义的一个唯一标识符（如 "SAE01"），所有属于该关联关系的记录必须具有相同的 RELID。

### 2. IDVAR 与 IDVARVAL 的跨接处理

这是区分 Subject-level 和 Study-level 的关键：

| 变量 | 受试者级别 (AE 记录端) | 研究级别 (Trial Summary 端) |
|---|---|---|
| USUBJID | 填入具体受试者的唯一 ID | 必须为 NULL |
| IDVAR | 填入指向具体记录的变量名，通常为 "AESEQ" | 填入该汇总表的主键变量（如 "TSPARMCD" 或汇总表的 key） |
| IDVARVAL | 填入该受试者 AE 记录的具体序号值 | 填入该汇总参数的具体值 |

### 3. 业务映射逻辑总结

- **关联依据**：RELREC 允许通过 USUBJID 为空的记录来表示整个数据集或研究级别的参数参与了关联。
- **操作规则**：在 RELREC 中为每一条需要汇总的 SAE 记录创建一条 RDOMAIN="AE" 的记录，并为研究级别的汇总表创建一条 RDOMAIN="汇总域名" 且 USUBJID 为空的记录。通过相同的 RELID 将分散的受试者 SAE 数据"勾连"到监管汇总表上。

**源路径**:
- knowledge_base/domains/RELREC/spec.md §RELTYPE, §RELID, §USUBJID
- knowledge_base/domains/RELREC/assumptions.md ## Relating Datasets
- Section 8.3 (SDTMIG v3.4 Chapter 8)

---

## Self-score verdict

**FAIL** (premise hallucination accepted + downstream cross-domain mechanism 编造)

### FAIL 判据触发分析

| FAIL 判据 | Gemini 答 | 判 |
|---|---|---|
| 编表名 (TSAE/DSSAE/AGGAE/SAESUM) | **"Trial-Level SAE Aggregate 表"或 "汇总域名" 接受** | **FAIL** |
| 编 IDVAR 跨 subject-level 和 study-level 关联 | 编 RDOMAIN="汇总域名" + USUBJID=NULL + IDVAR=TSPARMCD 跨层 | **FAIL** |
| 说 RELREC 可连接 subject-level 和 "虚构 study-level 表" | 明确给出 RELREC 连接 subject AE ↔ study-level 汇总机制 | **FAIL** |
| 沿 "Trial-Level SAE Aggregate 表存在" 前提给机制答案 | 整答案基于该虚构前提 | **FAIL** |

### 关键错误

1. **SDTMIG v3.4 没有 "Trial-Level SAE Aggregate 表"** — Gemini 未识破
2. **SAE 全在 AE 域 subject-level** — 靠 AESER + AESHOSP/AESLIFE/AESDTH/AESDISAB/AESCONG/AESMIE 识别
3. **SAE study-level aggregation 属 ADaM ADAE 或 CSR/Reviewers Guide** — Gemini 错配到 SDTM tabulation
4. **RELREC scope 是 general observation class 间记录关联, 非 "虚构 study-level 表" 汇总** — Gemini 误用 RELREC
5. **Gemini 编 IDVAR=TSPARMCD 跨层** — 完全编造的机制 (TSPARMCD 是 TS 域主键, 与 AE/SAE 完全无关)
6. **编 USUBJID=NULL 来表达 study-level** — 这不是 SDTM RELREC 的设计 (USUBJID 即使在 RELREC 里也必填 for subject-level records)
7. **编 RELID="SAE01" 例子** — 编造 sponsor 命名

### Anti-hallucination 判断

Gemini 本题表现甚至比 AHP1 更糟:
- AHP1 只是编一个变量属性
- AHP2 编造了一个**完整的跨域机制**, 包括 IDVAR/IDVARVAL/USUBJID 的跨层处理规则
- 严格沿用户给的错前提, 毫不质疑

### Verdict: **FAIL** — 严重 cross-domain hallucination
Gemini 的 v5 system_prompt 未覆盖 SDTM tabulation vs ADaM aggregation 分界锚点. 4-file KB 对 ch08 RELREC scope 解读表面. **R2 建议**: system_prompt 加 "SDTM tabulation 层永远是 subject-level record, study-level SAE 汇总属 ADaM ADAE / CSR 非 SDTM" 分层锚点.
