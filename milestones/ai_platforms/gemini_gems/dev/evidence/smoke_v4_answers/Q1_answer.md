# Gemini Gems — Q1 GF EGFR 变异 (post-apply smoke, v7 live)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q1)
> **执行时间**: 2026-04-24 (post v7 apply to Gem UI)
> **执行者**: Bojiang + claude cowork Chrome MCP (full-auto)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/5e0402af8a7d6917
> **题类**: Q1 (A1 — GF 域, v3.4 新域) / **post-apply 验证 v7 CO-4 "§GF 正向清单双锚" patch**
> **System prompt live**: v7 (v6-post-A1 + CO-1c ARMCD null rule + CO-4 §GF 正向清单双锚)

---

## 题目原文 (复制自 SMOKE_V4.md §2 Q1)

某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 **5 个 Core=Req 变量** 和 **3 个 Core=Exp 变量** (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.

## 发送给模型的 prompt (实际粘贴文本)

同上 (原题 verbatim, 无包装; Chrome MCP fill)

---

## 模型 raw 回答 (DOM readback 原文)

根据您提供的场景（肿瘤受试者血样 EGFR 基因测序、特定外显子突变、dbSNP 引用及遗传性），该数据应记录在 SDTMIG v3.4 新引入的 **GF (Genomics Findings)** 域。

### 1. 归域建议

- **归域**: GF (Genomics Findings)
- **理由**: GF 域专门用于存储人类受试者的基因组发现数据。虽然该数据来自血样（涉及 BE/BS 域的样本采集和测量），但具体的基因变异结果（突变类型、位置、数据库引用）属于 GF 域的范畴。

### 2. 关键变量清单 (基于 GF 正向清单双锚)

根据 SDTMIG v3.4 GF 域 spec (CO-4 硬约束)，该记录的变量示例如下：

#### Core = Req (必须提供的变量)

- **STUDYID**: Study Identifier
- **DOMAIN**: Domain Abbreviation (值为 "GF")
- **USUBJID**: Unique Subject Identifier
- **GFSEQ**: Sequence Number
- **GFTESTCD**: Genomics Test Short Name (例如 "EGFRMUT")
- **GFTEST**: Genomics Test Name (例如 "EGFR Gene Mutation Analysis")

#### Core = Exp (期望提供的变量，Findings 类标配)

- **GFORRES**: Original Result (例如 "L858R" 或 "POSITIVE")
- **GFSTRESC**: Standardized Character Result (与 GFORRES 对应)
- **GFDTC**: Date/Time of Finding (记录测序或结果生成的日期)

### 3. 特定场景处理说明

根据 **CO-4 (GF 域变量硬锚)**，具体的映射方式如下：

- **(a) 如何记录 "Exon 19" 位置信息**: 使用变量 **GFGENSR** (Genetic Sub-Region)。该变量用于记录基因内的特定位置或区域。
- **(b) 如何引用 dbSNP ID (rs121913444)**: 使用变量 **GFPVRID** (Published Variant Identifier)。该变量专门用于存储外部已知变异数据库（如 dbSNP, COSMIC）的唯一标识符。
- **(c) 基因组参考版本 (GRCh38.p13) 存哪**: 使用变量 **GFGENREF** (Genome Reference)。用于记录分析时参考的基因组程序集版本。
- **(d) 变异可遗传性 (Inheritability)**: 使用变量 **GFINHERT** (Inheritability)。该变量关联 Controlled Terminology **C181177**，用于标识变异是生殖系 (Germline) 还是体细胞 (Somatic) 来源。

### ⚠️ 专家纠错与提示 (CO-4/CO-5)

- **禁止臆造变量**: 在 SDTMIG v3.4 中 **不存在** GFGENE、GFLOC 或 GFVARIANT 变量。请勿将基因名或突变位置套用这些虚构名称。基因名称应体现在 GFTEST/GFTESTCD 中，具体亚区位置使用 GFGENSR。
- **CT 查询**: 关于 GFINHERT 的具体 Term 值（如 "GERMLINE"），请查阅 NCI EVS Browser (C181177)。

**源路径**:
- `knowledge_base/domains/GF/spec.md` (GF 域变量定义与 Core 属性)
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.4.11 (Disease Milestones/Genomics 相关)
- `04_business_scenarios_and_cross_domain.md` §4 (跨域规则)

**段落**: GF Spec Section - Variable Qualifiers

**Citation 数**: 3 条 (3 source paths)

---

## Self-score verdict

- **Verdict**: **PASS** (primary main gate); **PASS+ equivalent** on anti-hallucination (自发列禁止臆造变量 clause)
- **理由** (对照 SMOKE_V4.md §2 Q1 PASS 判据逐条):
  - 域: **GF (Genomics Findings)** ✓
  - Core Req: STUDYID / DOMAIN / USUBJID / GFSEQ / GFTESTCD / GFTEST (6/5) ✓
  - Core Exp: GFORRES / GFSTRESC / GFDTC (3/3) ✓
  - (a) **GFGENSR** "Exon 19" ✓ — **R2 GFGENE regression HIGH 未复发**
  - (b) **GFPVRID** rs121913444 ✓
  - (c) **GFGENREF** GRCh38.p13 ✓
  - (d) **GFINHERT** + CT **C181177** + Germline/Somatic ✓
- **触发 FAIL 判据?** 无 (未答 LB/PF; 未臆造 GFGENE/GFVARIANT; GFCHROM vs GFGENSR 未混淆 — 实际未提 GFCHROM)
- **Bonus (v7 CO-4 patch 主测目标)**:
  - ✅ **R2 Q1 HIGH regression (GFGENE 幻觉) 彻底修复** — v7 CO-4 正向清单双锚生效, 答中显式列 "不存在 GFGENE / GFLOC / GFVARIANT" 作专家纠错
  - ✅ 自发引 "CO-4 硬约束" 和 "CO-5 AHP" 作推理锚点, 表明 system prompt 规则被 Gem 内化使用
  - ✅ 源路径 3 条 citation, CO-3 强制生效
- **F-* carry-over 观察**:
  - ✅ **v7 CO-4 patch 主目标 §GF 正向清单双锚生效** — R1+R2 Q1 GFGENE 系统性 gap 修完
  - ⚠️ Core Exp 只列 3 个 (GFORRES/GFSTRESC/GFDTC), 未包含 GFMETHOD / GFREFID — 达标但不如 ChatGPT v2.2 厚度 (5 个), carry-over LOW
  - ✅ CO-5 anti-hallucination 引用链 (CO-4/CO-5 明确标注) 表明 v7 patch 已融入 Gem 推理流程

**v7 apply status**: ✅ EFFECTIVE (Q1 核心 "§GF 正向清单双锚" patch 生效, R2 HIGH regression 彻底解除)
