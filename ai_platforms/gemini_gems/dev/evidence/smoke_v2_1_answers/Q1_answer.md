# Q1 Answer — 合并用药 CM 域拆分

- URL: https://gemini.google.com/u/1/gem/3b572e310813/c15d655937375ff8
- 模式: Pro
- Date: 2026-04-21

## 题目

受试者在同一天开始服用两种降压药 (氯沙坦 50 mg/日 + 氨氯地平 5 mg/日), 计划持续服用整个试验期, 目的是控制高血压. 请问在 SDTM CM 域里应该拆成几条记录? 每条记录至少要填哪些 Core=Req 变量? 简要说明字段含义 (不需要给具体 NCI Code).

## 答案全文

根据 CDISC SDTMIG v3.4 的规定，针对您描述的业务场景，映射建议如下：

### 1. 结论
在 SDTM CM 域中应该拆分为 **2 条** 记录。

### 2. 依据与逻辑
- **拆分原则**：根据 CM 域的标准结构（One record per constant dosing interval per medication per subject），每种不同的药物（活性成分或申报名称）应作为独立的记录录入。
- **业务场景应用**：虽然氯沙坦和氨氯地平是在同一天开始服用，且目的相同，但它们是两种不同的化学实体。除非该药物本身是以"固定剂量复方制剂"（Fixed-dose Combination, FDC）的单一商品名购买并记录的，否则在 SDTM 中必须按 CMTRT 分别列出，以便后续进行药理分类编码（CMDECOD）。

### 3. 核心变量 (Core=Req) 列表及含义
根据 CM 域的 Spec，每条记录至少需要填写以下 **5 个** 必须（Required）变量：

| 变量名 | 变量标签 | 字段含义说明 |
|-------|---------|-------------|
| STUDYID | Study Identifier | 注册方案的唯一研究编号。|
| DOMAIN | Domain Abbreviation | 领域缩写，固定为 "CM"。|
| USUBJID | Unique Subject Identifier | 唯一受试者识别号，用于跨研究/跨域追踪受试者。|
| CMSEQ | Sequence Number | 域内记录流水号。同一受试者第一条为 1，第二条为 2，以此类推。|
| CMTRT | Reported Name of Drug, Med, or Therapy | 受试者服用的药物名称原文（如："LOSARTAN" 或 "AMLODIPINE"）。|

注：尽管 CMSTDTC (开始日期) 和 CMINDC (适应症) 在本场景中非常重要，但它们在 CM 域中的 Core 属性为 **Exp** (Expected)，而非 Req (Required)。

### 4. 记录展示示意
- 记录 1：CMTRT = "LOSARTAN 50 mg", CMSEQ = 1
- 记录 2：CMTRT = "AMLODIPINE 5 mg", CMSEQ = 2

**源路径**:
- knowledge_base/domains/CM/spec.md 段落: §CMTRT, §CMSEQ 及 Core 属性定义
- knowledge_base/domains/CM/assumptions.md 段落: Assumption 1 (One record per medication per subject)

## 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| 两条 CM 记录 (每个药各一条, 不能合并) | ✅ 答 2 条 |
| 列出 CM Core=Req: STUDYID / DOMAIN (="CM") / USUBJID / CMTRT — 必含 4 个 | ✅ 全列 + CMSEQ |
| 至少提到 CMSEQ (序列号) / CMSTDTC (开始日) / CMINDC (指征) | ✅ CMSEQ 列 Req, CMSTDTC+CMINDC 明确列为 Exp |
| 指征都是高血压 | ⚠️ 未明列指征值, 但业务场景"控制高血压"被引述 |

| FAIL 判据 | 结果 |
|----------|------|
| 合并成一条记录 | ✅ 未触 |
| 错列 Req 变量 | ✅ 未触 |
| 臆造不存在的变量名 | ✅ 未触 |

## Verdict: **PASS** (1.0 分)

正确拆分 2 条 + 5 个 Core=Req 变量全正确 (STUDYID/DOMAIN/USUBJID/CMSEQ/CMTRT) + CMSTDTC/CMINDC 的 Exp 属性解释准确 + FDC 边界说明合理 + 源路径 CO-3 合规.
