# Q5 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/638763801f4535a7
> Mode: Pro
> Run: 2026-04-21

## 原题
药代动力学 (PK) 研究中, 采样点的血药浓度检测值低于实验室定量下限 (LLOQ). 按 SDTMIG v3.4 PC 域 assumptions, 应该如何填写 PCORRES (原始结果) / PCSTRESN (标准数值) / PCSTRESC (标准字符) / PCLLOQ (定量下限)? 为什么不能直接写 0?

## 答案全文

在药代动力学（PK）研究中，处理低于定量下限（Below the Lower Limit of Quantitation, BLQ 或 BQL）的数据是 SDTM PC 域映射的经典场景。根据 SDTMIG v3.4 PC 域 Assumptions 以及 Findings 观测类的通用规则，映射逻辑如下：

### 1. 变量填写规则

- **PCORRES (Original Result)**: 填写原始报告中的值。如果原始实验报告单上写的是 "< 0.1" 或 "BQL"，则照实填写。
- **PCSTRESC (Standard Character Result)**: 填写标准格式的字符结果。通常与 PCORRES 保持一致或进行标准化处理（如 "< 0.1"）。
- **PCSTRESN (Standard Numeric Result)**: 必须保持为空（Null）。
  - 注：根据 SDTMIG 规定，当结果无法以数值形式表示（如包含 "<" 符号或非数值字符）时，PCSTRESN 无法存储该信息。
- **PCLLOQ (Lower Limit of Quantitation)**: 填写该检测方法的定量下限数值（例如 0.1）。这是 PC 域特有的变量，用于明确说明定量的边界。

### 2. 为什么不能直接写 0？

在 SDTM 数据标准化中，"0" 也是一个具体的观测数值。以下是不能写 0 的核心原因：

- **真实性（Accuracy）**：BQL 并不意味着血药浓度绝对为 0，而是意味着浓度处于 0 到 LLOQ 之间的某个位置，只是目前的分析方法无法精确测量。填 0 属于臆造数据。
- **避免偏倚（Bias）**：如果在 SDTM 层级将其强制设为 0，会直接影响后续药代动力学参数（如 Cmax、AUC）的计算。
- **分析假设归属于 ADaM**：如何处理 BQL 数据（是填 0、填 1/2 LLOQ 还是填 LLOQ）属于统计分析策略。根据 CDISC 原则，这类"衍生/填充（Imputation）"逻辑应在 ADaM (ADPC) 域中处理，而不是在 SDTM 原始域中。SDTM 必须保留原始观测的特质。

### 依据与溯源

- PC Assumption 1：指明了当 PCSTRESC 包含 "<" 符号时，PCSTRESN 应当为 Null。
- PC Assumption 5：提到了 PCLLOQ 变量的应用，用于记录定量的下限值。
- PC Domain Spec：明确了 PCLLOQ 的 Core 属性（Permissible，但在 PK 研究中通常作为关键信息收集）。

**源路径**: knowledge_base/domains/PC/assumptions.md
**段落**: §Assumption 1, §Assumption 5
**相关参考**: 如果样本未采集或由于实验原因无结果（非 BQL），应使用 PCSTAT = 'NOT DONE' 和 PCREASND。但 BQL 属于已完成检测但结果低于量程，因此 PCSTAT 仍应保持为空。
