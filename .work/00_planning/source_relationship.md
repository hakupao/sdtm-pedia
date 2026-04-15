# 源文件关系梳理

> 创建日期：2026-04-13
> 状态：**已完成** (2026-04-13)

---

## 一、源文件清单

| 文件 | 格式 | 内容概述 |
|------|------|----------|
| `SDTMIG v3.4 (no header footer).pdf` | PDF, 461页 | SDTM 实施指南 v3.4 全文（章节叙述 + 变量表 + assumptions + examples） |
| `SDTMIG_v3.4.xlsx` | Excel | SDTMIG 3.4 的变量元数据，结构化表格（1917 行变量，63 个 domain） |
| `SDTM_v2.0.pdf` | PDF | SDTM 数据模型标准 v2.0（概念、模型结构、observation class 定义） |
| `SDTM Terminology.xlsx` | Excel | CDISC 受控术语（约 1000 个 codelist，约 39000 条术语） |

---

## 二、PDF 与 xlsx 的关系（关键发现）

### xlsx 是 PDF 的子集

`SDTMIG_v3.4.xlsx` 的内容**完全包含在** `SDTMIG v3.4.pdf` 之中。

PDF 的第 5、6、7 章围绕 domain 展开，每个 domain 的介绍由**三部分**组成：

| 部分 | 内容 | 与 xlsx 的关系 |
|------|------|----------------|
| **Specification** | 变量定义表（Variable Name, Label, Type, Controlled Terms, Role, CDISC Notes, Core） | **= xlsx 的内容**，且 xlsx 质量更高（结构化、无 PDF 提取噪音、有 Variable Order 列） |
| **Assumptions** | 叙述性业务规则、变量使用指导、编码规范、边界情况说明 | **xlsx 中没有**，仅存在于 PDF |
| **Examples** | 示例数据表（展示 .xpt 数据集的真实场景数据行） | **xlsx 中没有**，仅存在于 PDF |

### 以 AE domain 为例（PDF p133-142）

- **Specification**（p134-137）：60 个变量的定义表 → 与 xlsx Variables sheet 中 Domain=AE 的行一致
- **Assumptions**（p137-140）：12 条详细指导（采集范围、编码规则、严重程度变量、时间变量等）
- **Examples**（p140-142）：6 个示例数据集，展示不同场景下的 ae.xpt 数据

### xlsx 的优势

xlsx `Variables` sheet 结构：
```
Version | Variable Order | Class | Domain | Variable Name | Label | Type | Controlled Terms | Role | CDISC Notes | Core
```

相比 PDF 提取的表格：
- 有明确的 `Variable Order` 排序编号
- `Controlled Terms` 字段更干净
- 无 PDF→文本 转换的格式噪音
- 结构化程度更高，适合程序化处理

### 结论

> **Specification 应以 xlsx 为权威来源，Assumptions 和 Examples 应从 PDF 提取。**

---

## 三、PDF 的章节结构

```
第 1 章  Introduction（p7-10）
第 2 章  Fundamentals of the SDTM（p11-16）
第 3 章  Submitting Data in Standard Format（p17-21）
第 4 章  Assumptions for Domain Models（p22-59）— 通用假设，适用于所有 domain
第 5 章  Models for Special-Purpose Domains（p60-91）
         - CO, DM, SE, SM, SV（每个 domain: Spec + Assumptions + Examples）
第 6 章  Domain Models Based on General Observation Classes（p92-381）
         6.1 Interventions: AG, CM, EC/EX, ML, PR, SU
         6.2 Events: AE, BE, CE, DS, DV, HO, MH
         6.3 Findings: DA, DD, EG, IE, BS/CP/GF/IS/LB/MB/MI/MK/MS/NV/OE/PC/PE/PP/QS/RE/RP/RS/SC/SS/TR/TU/UR/VS
         6.4 Findings About: FA, SR
第 7 章  Trial Design Model Datasets（p382-426）
         - TA, TD, TE, TI, TM, TS, TV
第 8 章  Representing Relationships and Data（p427-440）
         - RELREC, SUPPQUAL, RELSPEC, RELSUB 等
第 9 章  Study References（p441-443）
         - DI, OI
第 10 章 Appendices（p444+）
```

---

## 四、待继续梳理

- [ ] 现有输出物（project_knowledge_base）的重叠与缺失分析
- [ ] 重构方案设计
- [ ] SDTM_v2.0.pdf 与 SDTMIG v3.4 的关系
- [ ] SDTM Terminology.xlsx 的处理策略
