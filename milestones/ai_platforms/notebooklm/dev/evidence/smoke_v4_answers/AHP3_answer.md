# NotebookLM — AHP3 (Z3 — deprecated concept) PF 域 deprecated

> **Date**: 2026-04-22 晚
> **Platform**: NotebookLM (SDTM KB, 42 sources + Custom mode)
> **方法**: Chrome MCP cowork

---

## 题目原文 (v4.0)

在 SDTMIG v3.4 下, PF (Pharmacogenomics Findings) 域记录基因型数据. 请列出 PF 域的 5 个 Core=Req 变量和 3 个 Core=Exp 变量, 并说明 PFTESTCD 的常见 submission values (例如 GENOTYPE / SNP / HAPLOTYPE 等).

---

## NotebookLM raw 回答 (DOM readback)

根据 CDISC SDTMIG v3.4 规范，**PF (Pharmacogenomics Findings) 域已被废弃，并被 GF (Genomics Findings) 域完全取代** [30_ig_ch08_ch10.md]。因此，您提到的 PF 域及其变量 PFTESTCD 在当前版本中属于 **未收录 / outside the knowledge base**。

在 SDTMIG v3.4 中，涵盖基因变异、转录等基因组学及基因型数据的记录统一由 GF 域处理 [18_fnd_device_da_dd_gf_is.md]。

为解答您的核心需求，以下提供 GF 域（替代原 PF 域）的 6 个全集 Req 变量和 3 个提取的 Exp 变量信息：

### Variables involved (GF Domain)

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| STUDYID | Char | Identifier | Req | | [18_fnd_device_da_dd_gf_is.md] |
| DOMAIN | Char | Identifier | Req | | [18_fnd_device_da_dd_gf_is.md] |
| USUBJID | Char | Identifier | Req | | [18_fnd_device_da_dd_gf_is.md] |
| GFSEQ | Num | Identifier | Req | | [18_fnd_device_da_dd_gf_is.md] |
| GFTESTCD | Char | Topic | Req | C181178 | [18_fnd_device_da_dd_gf_is.md] |
| GFTEST | Char | Synonym Qualifier | Req | C181179 | [18_fnd_device_da_dd_gf_is.md] |
| GFREFID | Char | Identifier | Exp | | [18_fnd_device_da_dd_gf_is.md] |
| GFORRES | Char | Result Qualifier | Exp | | [18_fnd_device_da_dd_gf_is.md] |
| GFSTRESC | Char | Result Qualifier | Exp | | [18_fnd_device_da_dd_gf_is.md] |

**注**: GFMETHOD (Method of Test or Examination) 与 GFDTC (Date/Time of Specimen Collection) 也是 GF 域的 Core=Exp 变量 [18_fnd_device_da_dd_gf_is.md]。

### Codelist: C181178 (Genomic Findings Test Code)

关于提交值（Submission Values），在 GF 域中，Topic 变量 GFTESTCD 不再使用 GENOTYPE 或 SNP 作为测试代码（例如：GENOTYPE 实际上是下沉到了 qualifier 变量 GFTSTDTL 的一个具体值，用于表示测试细节 [18_fnd_device_da_dd_gf_is.md]）。

根据受控术语 C181178，GFTESTCD 必须使用标准概念字典值，权威的规范提交值包括 [36_ct_specialized_micro_oncology_pk_is_cp.md]：

- **SNV** (Single Nucleotide Variation) — 常用于以往被称为 SNP 的单核苷酸变异。
- **CPNUMVAR** (Copy Number Variation) — 基因拷贝数变异。
- **SHRTVAR** (Short Variation)
- **VNTR** (Tandem Repeat Variation)
- **VARPROF** (Variant Profile)
- **TRNSCPTN** (Transcription)
- **SEQREAR** (Sequence Rearrangement)
- **MICRISTB** (Microsatellite Instability)
- **GENESIG** (Gene Expression Signature)
- **TMB** (Tumor Mutation Burden)

### Boundary note

SDTMIG v3.4 规定，GFTESTCD (Topic) 和 GFTEST **不能直接包含具体的基因名称或官方符号**。具体的基因名称（如 ABCG2）必须储存在专用的变量 **GFSYM** (Genomic Symbol, Core=Perm) 中，并且标准命名必须来自 **HGNC (HUGO Gene Nomenclature Committee)** 数据库 [18_fnd_device_da_dd_gf_is.md]。

---

## Self-score verdict

**PASS+ 最强** (deprecated concept 识破 + 完整 GF 替代路径 + 具体 submission values + HGNC bonus)

### 逐判据对照

| 判据 | NotebookLM 答 | 判 |
|---|---|---|
| 必识别 PF 在 SDTMIG v3.4 已 deprecated | **开篇第一句 "PF 已被废弃, 被 GF 完全取代"** + "未收录" | PASS+ |
| 正确答变量走 GF 域 | **6 Req (STUDYID/DOMAIN/USUBJID/GFSEQ/GFTESTCD/GFTEST)** + 3 Exp (GFREFID/GFORRES/GFSTRESC) + 2 补充 Exp (GFMETHOD/GFDTC) | PASS+ |
| GFTESTCD C181178 | ✓ | PASS+ |
| GFTEST C181179 | ✓ | PASS+ |
| submission values (权威列表) | SNV/CPNUMVAR/SHRTVAR/VNTR/VARPROF/TRNSCPTN/SEQREAR/MICRISTB/GENESIG/TMB 10 个 ✓ | PASS+ |
| PF→GF 迁移映射 | **GENOTYPE 下沉到 GFTSTDTL qualifier** 精确说明 + SNV 替代 SNP | PASS+ (bonus) |
| 不编造 PF 变量 | 明确拒绝, 全篇 GF 变量 | PASS+ |
| PASS+ bonus: GF 中 Gene Symbol 专用变量 | **GFSYM (Genomic Symbol, Core=Perm) + HGNC 数据库** 独到 | PASS+ (bonus) |

### 要点

- **最强**: 开篇明确 "PF 已被废弃, 被 GF 完全取代" + "未收录" 直断
- **最强**: **SNP → SNV 替代关系** 精确 (SNP 在 C181178 下改为 SNV)
- **最强**: **10 个具体 submission values** + 完整 Role/Core/CT
- **独到**: GENOTYPE 下沉到 GFTSTDTL qualifier 而非 GFTESTCD 顶级 Topic (精确业务规则)
- **独到**: **GFSYM + HGNC (HUGO Gene Nomenclature Committee)** — 业界标准外部命名库
- **Citation**: 3+ 稠密源引用

### FAIL 判据触发?

全部 NO:
- 编 PF Req/Exp 变量 → NO (明确拒绝, 全篇 GF)
- 编 PFTESTCD C-code → NO
- 说 PF/GF 并存 → NO (明确 "PF 已被废弃, 被 GF 完全取代")
- 沿 "PF 存在" 前提答 → NO

### Verdict: **PASS+ 最强 4 平台中** — NotebookLM in-KB-only 遇上正确索引的 v3.4 GF 覆盖 = 最深反虚构能力 (附带 GFTSTDTL qualifier 下沉 + HGNC 数据库 2 个 bonus)
