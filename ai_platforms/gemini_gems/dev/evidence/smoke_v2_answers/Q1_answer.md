# Q1 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/0c1ab80ef7914247
> Mode: Pro
> Run: 2026-04-21

## 原题
受试者在同一天开始服用两种降压药 (氯沙坦 50 mg/日 + 氨氯地平 5 mg/日), 计划持续服用整个试验期, 目的是控制高血压. 请问在 SDTM CM 域里应该拆成几条记录? 每条记录至少要填哪些 Core=Req 变量? 简要说明字段含义 (不需要给具体 NCI Code).

## 答案全文

在 SDTM CM (Concomitant Medications) 域中，针对您描述的场景，处理建议如下：

### 1. 应该拆成几条记录？

**结论：应该拆分为 2 条记录。**

依据与逻辑：根据 SDTMIG 中 Interventions（干预类）观察类别的基本原则，每条记录通常代表受试者接受的一种特定药物、剂量、频率或治疗周期的变化。

- **原因**：虽然两种药（氯沙坦和氨氯地平）是同日开始服用的，但它们是不同的化学成分且具有不同的剂量。为了准确记录每种药物的剂量、单位和可能的编码（CMDECOD），必须分别录入。
- **扩展**：即使是复方制剂（如一颗药里含有两种成分），如果 EDC 是分开采集的，通常也建议在 CM 中拆分记录，除非该复方制剂有唯一的官方名称。但在本案中，它们显然是作为两种独立药物被处方的。

### 2. 每条记录至少要填哪些 Core=Req 变量？

根据 SDTMIG v3.4，CM 域共有 **5 个必须填写（Core=Req）的变量**：

| 变量名 | 标签 (Label) | 含义简述 |
|---|---|---|
| STUDYID | Study Identifier | 研究编号，唯一标识一个临床试验。 |
| DOMAIN | Domain Abbreviation | 域缩写，CM 域固定填 "CM"。 |
| USUBJID | Unique Subject Identifier | 受试者唯一标识符，跨域唯一。 |
| CMSEQ | Sequence Number | 记录序列号，用于在受试者内唯一标识一条 CM 记录（通常为 1, 2, ...）。 |
| CMTRT | Reported Name of Drug, Med, or Therapy | 药物名称的原始记录（如"氯沙坦"或"氨氯地平"）。 |

注：虽然 CMDECOD (Standardized Term) 和 CMSPID (Sponsor-Defined Identifier) 等变量在实际业务中非常重要，但根据 SDTMIG v3.4 规范，它们的 Core 属性分别为 Exp (Expected) 或 Perm (Permissible)，并非技术上的 Req。

### 3. 字段含义简要说明 (针对本场景)

为了完整描述您的业务场景，除了上述 Req 变量外，通常还需涉及以下关键字段：

- CMTRT (Req): 填入原始药名，记录 1 为 "LOSARTAN", 记录 2 为 "AMLODIPINE"。
- CMDOSE: 填入剂量数值（如 50 或 5）。
- CMDOSU: 填入剂量单位（如 mg）。
- CMINDC: 填入用药指征（如 "HYPERTENSION"）。
- CMSTDTC: 填入开始用药日期。
- CMENRTP: 填入 "ONGOING" (若试验结束时仍在服用) 或对应的结束时间变量。

**源路径**: knowledge_base/domains/CM/spec.md
**段落**: §CM Spec (Core Attributes) & Interventions Class General Assumptions
