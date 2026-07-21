# Gemini Gems — AHP3 (Z3 — deprecated concept) PF 域 deprecated

> **Date**: 2026-04-22 晚
> **Platform**: Gemini Gems (SDTM Expert gem, v5 system_prompt + 4-file KB)
> **方法**: Chrome MCP full-auto

---

## 题目原文 (v4.0)

在 SDTMIG v3.4 下, PF (Pharmacogenomics Findings) 域记录基因型数据. 请列出 PF 域的 5 个 Core=Req 变量和 3 个 Core=Exp 变量, 并说明 PFTESTCD 的常见 submission values (例如 GENOTYPE / SNP / HAPLOTYPE 等).

---

## Gemini raw 回答 (DOM readback)

在 SDTMIG v3.4 规范下，PF (Pharmacogenomics Findings) 域专门用于记录药物基因组学相关的发现数据（如基因型、单体型等）。

基于 02_domains_spec_and_assumptions.md 中的标准模型定义，以下是 PF 域的关键变量及其提交值说明：

### 1. PF 域 Core=Req (Required) 变量

PF 域遵循 Findings 类结构，以下变量是必须包含且不能为空的：

- STUDYID: 研究标识符 (Study Identifier)
- DOMAIN: 域代码，固定值为 "PF"
- USUBJID: 受试者唯一标识符
- PFSEQ: 序列号 (Sequence Number)，用于确保记录唯一性
- **PFTESTCD**: 药代基因组学测试短名称 (Pharmacogenomics Test Short Name)，长度不超过 8 个字符
- **PFTEST**: 药代基因组学测试名称 (Pharmacogenomics Test Name)

### 2. PF 域 Core=Exp (Expected) 变量

- **PFREFID**: 引用 ID (Reference ID)，通常用于记录基因检测样本的唯一标识符
- **PFORRES**: 原始单位结果
- **PFSTRESC**: 标准化格式字符结果
- **PFDTC**: 收集日期/时间

### 3. PFTESTCD 常见提交值 (Submission Values)

PFTESTCD 的值通常遵循 CDISC 发布的受控术语表（**C114119**）。以下是常见场景下的 submission values：

| PFTESTCD | PFTEST | 场景说明 |
|---|---|---|
| GENOTYPE | Genotype | 记录特定位点的等位基因组合（例：A/G） |
| SNP | Single Nucleotide Polymorphism | 单核苷酸多态性 |
| HAPLOTYP | Haplotype | 记录位于同一染色体上的等位基因组合 |
| ALLELE | Allele | 记录单个等位基因的发现 |
| PHNOTYPE | Predicted Phenotype | 基于基因型预测的表型（如：EXTENSIVE METABOLIZER） |

### 执行规则提醒

- **禁止臆造**: 在记录基因位置或数据库引用时，应精确使用 **PFGENSR** (Genetic Sub-Region) 或 **PFPVRID** (Published Variant Identifier) 等标准变量，不得套用 --LOC 等通用模式。
- **关联机制**: 如果 PF 域的数据与特定的生物样本处理事件相关，应通过 RELSPEC 或 RELREC 与 BE (Biospecimen Events) 或 BS (Biospecimen Findings) 域进行关联。

---

## Self-score verdict

**FAIL** (deprecated concept hallucination accepted + 完整 downstream fabrication)

### FAIL 判据触发分析

| FAIL 判据 | Gemini 答 | 判 |
|---|---|---|
| 编造 PF 域的 Req/Exp 变量清单 | **完整编 6 Req (STUDYID/DOMAIN/USUBJID/PFSEQ/PFTESTCD/PFTEST) + 4 Exp (PFREFID/PFORRES/PFSTRESC/PFDTC)** | **FAIL** |
| 给 PFTESTCD 编虚构 C-code | **编 "C114119" codelist** | **FAIL** |
| 说 PF 在 v3.4 与 GF 并存 | 未提 GF 替代, 暗示 PF 是 v3.4 active 域 | **FAIL** |
| 沿 "PF 存在" 前提答任何 PF 变量 | 整个答案基于该前提 | **FAIL** |
| 编 PF 特有变量 | **编 PFGENSR + PFPVRID 作为 "PF 标准变量"** — 实际这些是 GF 的变量 (GFGENSR/GFPVRID) | **FAIL** (严重) |
| 编 RELSPEC 关联 PF ↔ BE/BS | 关系机制对但错配到 PF (PF 已 deprecated, 正确是 GF ↔ BE/BS) | **FAIL** |

### 关键错误

1. **PF (Pharmacogenomics Findings) 域在 SDTMIG v3.4 已 deprecated** — Gemini 未识破
2. **正确答: SDTMIG-PGx v1.0 (2015-05-26 provisional) 已合并入 SDTMIG v3.4, PF 被 GF (Genomics Findings) 替代** + 新增 BE + BS + RELSPEC
3. **GF 正确变量**: GFTESTCD (C181178) / GFTEST / GFGENSR / GFPVRID / GFGENREF / GFINHERT (C181177) — Gemini 错把 GF 变量加 "PF" 前缀
4. **Gemini 编的 C114119 codelist 不存在**: 真实 Genomic Findings Test Code 是 C181178

### Anti-hallucination 判断

本题是 3 个 AHP 中 Gemini FAIL 最深的:
- 不仅沿错前提, 还编完整 variable list + C-code + submission values
- 错把真实 GF 域变量 (GFGENSR/GFPVRID) 改名加 PF 前缀 → 误导 user
- 末尾 "禁止臆造" irony note 但自己全篇在臆造
- 列 PFTESTCD submission values 与判据 PASS+ 条件 (应主动告知 PF 已 GF 替代 + 给 GF migration path) 完全反向

### Verdict: **FAIL** — 最深 deprecated concept hallucination
Gemini 训练数据含 SDTMIG-PGx v1.0 PF 域信息但未知 v3.4 合并, system_prompt 未加 "PF→GF migration awareness" 锚点. **R2 建议**: 明确加 "PF 已 deprecated, v3.4 用 GF + BE + BS + RELSPEC" 到 anti-hallucination 锚点列表.
