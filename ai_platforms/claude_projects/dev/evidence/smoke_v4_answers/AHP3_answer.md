# Claude Projects — AHP3 (Z3 — deprecated concept) PF 域 deprecated

> **Date**: 2026-04-22 晚
> **Platform**: Claude Projects (SDTM KB, v2.6, 19 files, Opus 4.7)
> **方法**: Chrome MCP cowork
> **Weekly limit**: 75% (未变)

---

## 题目原文 (v4.0)

在 SDTMIG v3.4 下, PF (Pharmacogenomics Findings) 域记录基因型数据. 请列出 PF 域的 5 个 Core=Req 变量和 3 个 Core=Exp 变量, 并说明 PFTESTCD 的常见 submission values (例如 GENOTYPE / SNP / HAPLOTYPE 等).

---

## Claude raw 回答 (DOM readback)

### ⚠️ 前提校正: PF 在 SDTMIG v3.4 中已废弃

根据 **02_chapters.md §6.3.5.4 变更记录**:

> Genomics Findings (GF) — New domain replacing the PF domain from the provisional SDTMIG-PGx

也就是说:
- **PF 是旧 SDTMIG-PGx v1.0 (provisional, 2015-05-26) 的域**, 在 v3.4 中已被 **GF (Genomics Findings)** 取代
- 你描述的 "记录基因型数据 (GENOTYPE / SNP / HAPLOTYPE)" 这一语义在 v3.4 落到 GF 域
- 04_variable_index.md / 05_mega_spec.md 的 **63 域清单中没有 PF**

若你确实在处理 v3.4 之前的 PGx 数据, PF 的规范需回源 SDTMIG-PGx v1.0, 不在本 Project 知识库内。

下面按 **GF 域** 回答 (即 v3.4 下对应的正确域)。

### ✅ GF 域 (v3.4 正确域) — Req / Exp 变量

**来源**: 05_mega_spec.md → knowledge_base/domains/GF/spec.md
**结构**: One record per finding per observation per biospecimen per subject
**Class**: Findings

#### Required 变量 (实际有 6 个 Req, 你问 5 个, 全列出)

| # | Name | Label | Role |
|---|---|---|---|
| 1 | STUDYID | Study Identifier | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Identifier |
| 3 | USUBJID | Unique Subject Identifier | Identifier |
| 4 | GFSEQ | Sequence Number | Identifier |
| 5 | GFTESTCD | Short Name of Genomic Measurement | Topic (CT: **C181178**) |
| 6 | GFTEST | Name of Genomic Measurement | Synonym Qualifier (CT: **C181179**) |

#### Expected 变量 (实际有 6 个 Exp, 你问 3 个, 全列出)

| # | Name | Label | Role | CT |
|---|---|---|---|---|
| 1 | GFREFID | Reference ID | Identifier | — |
| 2 | GFORRES | Result or Finding in Original Units | Result Qualifier | — |
| 3 | GFSTRESC | Result or Finding in Standard Format | Result Qualifier | derived from GFORRES |
| 4 | GFMETHOD | Method of Test or Examination | Record Qualifier | **C85492** |
| 5 | VISITNUM | Visit Number | Timing | — |
| 6 | GFDTC | Date/Time of Specimen Collection | Timing | ISO 8601 |

### ⚠️ GFTESTCD 常见 submission values — 需更正你的示例

**你列举的 GENOTYPE / SNP / HAPLOTYPE 与 v3.4 的模型不匹配**。GF 域把"测量类型"与"测量细节"分到两个变量:

| 层级 | 变量 | CT Code | 语义 |
|---|---|---|---|
| 测量类型 (what kind of genomic assessment) | GFTESTCD / GFTEST | **C181178 / C181179** | e.g. SNV, TMB, TRNSCPTN |
| 测量细节 (what specifically was reported) | **GFTSTDTL** | **C181180** | e.g. GENOTYPE, ALLELE SEQUENCE |

#### GFTESTCD (C181178) 实际 submission values

**来源**: 11a_terminology_high_core.md → knowledge_base/terminology/core/gf.md (Extensible: Yes, 共 10 terms, 以下为本 Project 已收录的 8 个):

| Code | Submission Value | 含义 |
|---|---|---|
| C181331 | SNV | Single Nucleotide Variation (≈ 你说的 "SNP") |
| C181330 | CPNUMVAR | Copy Number Variation |
| C181332 | MICRISTB | Microsatellite Instability |
| C181333 | GENESIG | Gene Signature |
| C181334 | SHRTVAR | Short Sequence Variation (≤50 nt) |
| C181335 | TMB | Tumor Mutational Burden |
| C189439 | SEQREAR | Sequence Rearrangement |
| C17208 | TRNSCPTN | Transcription |

> 08_terminology_map.md 标注本 codelist 共 10 terms; 本 Project 11a 已列出 8 个, 剩余 2 个需回源 knowledge_base/terminology/core/gf.md。

#### GENOTYPE 与 HAPLOTYPE 属于 GFTSTDTL (C181180)

**来源**: 11a_terminology_high_core.md → knowledge_base/terminology/core/gf.md (33 terms, 摘录):

| Code | Submission Value |
|---|---|
| C45447 | GENOTYPE |
| C45374 | NUCLEOTIDE SEQUENCE |
| C189447 | ALLELE SEQUENCE |
| C181349 | COPY NUMBER RATIO |
| C181341 | NORMALIZED LEVEL |
| … | (完整 33 条见源) |

> HAPLOTYPE 在本 Project 已列片段中未命中, 需回源 knowledge_base/terminology/core/gf.md 确认完整 33 terms 中是否包含。

### 实际用法参考 (09_examples_data_high.md GF Example 2 摘录)

| GFTESTCD | GFTEST | GFTSTDTL | GFORRES |
|---|---|---|---|
| SNV | Single Nucleotide Variation | GENOTYPE | G/G |

即: 一条 SNV 类型的检测、报告细节为 GENOTYPE、结果为 G/G。**这是 v3.4 下"基因型数据"的标准建模**。

### 小结

1. **PF 域在 v3.4 中不存在, 已被 GF 取代** (来自 SDTMIG-PGx v1.0 的旧域)
2. **GF 有 6 Req + 6 Exp** (非你问的 5+3, 我列全)
3. **GENOTYPE/HAPLOTYPE 是 GFTSTDTL 值, 不是 GFTESTCD; SNP 对应 GFTESTCD=SNV**

---

## Self-score verdict

**PASS+ 最强 (4 平台 AHP3 并列 NotebookLM)**

### 逐判据对照

| 判据 | Claude 答 | 判 |
|---|---|---|
| 必识别 PF deprecated | **"⚠️ 前提校正: PF 在 v3.4 中已废弃"** + §6.3.5.4 变更记录原文引用 | PASS+ |
| SDTMIG-PGx v1.0 合并历史 | ✓ 2015-05-26 provisional + 明确 v3.4 取代 | PASS+ |
| 正确答变量走 GF | 6 Req + 6 Exp **全列出** (超用户问的 5+3) + CT C181178/C181179/C85492 | PASS+ |
| GFTESTCD C181178 | ✓ | PASS+ |
| 不编 PF 变量 | 明确拒绝, 全篇 GF | PASS+ |
| submission values | SNV/CPNUMVAR/MICRISTB/GENESIG/SHRTVAR/TMB/SEQREAR/TRNSCPTN 8 个 + 具体 C-code | PASS+ |
| PF→GF migration 对应 | "SNP → SNV" 明确替代 | PASS+ |
| **核心洞察**: GFTESTCD vs GFTSTDTL 两层变量 | **C181178 测量类型 vs C181180 测量细节** — 业界深度精确 | PASS+ (最核心) |
| PASS+ bonus 迁移映射 | **GF Example 2 具体示例** (SNV + GENOTYPE + G/G) 给 PF-era 思维的实际 v3.4 映射 | PASS+ (bonus) |

### 要点

- **最强**: **§6.3.5.4 变更记录原文引用** "Genomics Findings (GF) — New domain replacing the PF domain from the provisional SDTMIG-PGx"
- **最强**: **GFTESTCD vs GFTSTDTL 两层变量分工** — 用户的 GENOTYPE/SNP/HAPLOTYPE 在 GFTSTDTL (C181180) 而非 GFTESTCD — 深度精确
- **最强**: **GF Example 2 具体行** (SNV + GENOTYPE + G/G) — PF-era 思维到 v3.4 实际映射
- **独到**: 诚实标注 boundary — "HAPLOTYPE 在本 Project 已列片段中未命中, 需回源" + "codelist 10 terms 我列 8 个" (anti-hallucination 坦诚)
- **独到**: GFMETHOD (C85492) / VISITNUM / GFDTC (ISO 8601) Exp 变量补全
- **独到**: 超答 (6 Req + 6 Exp vs 用户问 5+3, 全列)

### FAIL 判据触发?

全部 NO:
- 编 PF 变量 → NO
- 编 PFTESTCD C-code → NO
- 说 PF/GF 并存 → NO (明确 "v3.4 中不存在")
- 沿 PF 前提答 → NO (开篇前提校正)

### Verdict: **PASS+ 最强 4 平台中 (并列 NotebookLM)** — Claude 独到 GFTESTCD vs GFTSTDTL 两层变量分工 + §6.3.5.4 原文 + GF Example 2 具体示例; NotebookLM 独到 HGNC 数据库 + GFTSTDTL 下沉 qualifier 说明. 双方互补并列最强
