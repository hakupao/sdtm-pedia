# Q1 — Gemini SDTM Expert 回答 (A1 — GF 域 EGFR 基因变异)

> 题: 某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 5 个 Core=Req 变量 和 3 个 Core=Exp 变量 (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.
> 期望核心: GF 域 + GFGENSR (a) + GFPVRID (b) + GFGENREF (c) + GFINHERT (d)
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/c8b8dc246289f2d6
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

根据 SDTMIG v3.4 规范及您提供的知识库信息，该外周血 EGFR 基因测序结果应记录在 **GF (Genetic Findings)** 域。

### 1. 映射建议与变量列表

建议域：GF (Genetic Findings)
该域用于记录受试者遗传物质（DNA/RNA）中的变异及相关发现。

**至少 5 个 Core=Req 变量**：

1. STUDYID (Study Identifier)
2. DOMAIN (Domain Abbreviation) - 固定值为 "GF"
3. USUBJID (Unique Subject Identifier)
4. GFSEQ (Sequence Number)
5. GFTESTCD (Genetic Test Short Name) - 如 "VARIDENT" (Variant Identification)
6. GFTEST (Genetic Test Name) - 如 "Variant Identification"

**至少 3 个 Core=Exp 变量 (Topic 变量优先)**：

1. **GFGENE** (Gene Name) - Topic 变量核心补充，记录 "EGFR"
2. **GFVARIANT** (Variant Name) - 记录 "L858R"
3. **GFSTRESC** (Character Result in Standard Format) - 记录变异结果，如 "PRESENT" 或具体的突变描述。

### 2. 具体业务场景说明

根据 GF 域规范与假设：

- **(a) 如何记录 "Exon 19" 位置信息**：
  应记录在 **GFLOC** (Location) 变量中。对于基因组位置，GFLOC 常用于存储外显子 (Exon) 或内含子 (Intron) 信息。

- **(b) 如何引用 dbSNP ID (rs121913444)**：
  应记录在 **GFREFID** (Reference Identifier) 变量中。该变量专门用于记录外部数据库（如 dbSNP, COSMIC）的参考 ID。

- **(c) 基因组参考版本 (GRCh38.p13) 存哪**：
  应记录在 **GFREFVER** (Reference Version) 变量中。它用于指明在识别变异时所参考的基因组组装版本。

- **(d) 如果该变异可遗传给下一代（生殖系变异），走哪个变量**：
  应记录在 **GFSTYPE** (Specimen Type) 或更具体的 **GFVALGRP** (Variant Grouping) 变量中，通过 Controlled Terminology 标注为 "GERMLINE" (生殖系) 或 "SOMATIC" (体细胞)。在 GF 域的典型实践中，区分遗传性还是获得性主要通过 GFSTYPE 或辅助变量。

### 3. 源路径引用

源路径: `knowledge_base/domains/GF/spec.md`
段落: §GF (Genetic Findings Domain Specification)

源路径: `knowledge_base/domains/GF/assumptions.md`
段落: Section 1, 2 (Genetic Findings Assumptions)

注意：
- 由于外周血（Peripheral Blood）是样本来源，其详细样本信息通常在 BS (Biospecimen Events) 域定义，并通过 GF.LNKID 或 RELREC 与 GF 记录关联。
- 关于具体的变异描述，建议参考 NCI EVS 映射相应的术语。具体 Term 值请查阅 NCI EVS Browser。

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| 域 | GF | GF (Genetic Findings) | ✅ |
| Core Req 5 | STUDYID/DOMAIN/USUBJID/GFSEQ/GFTESTCD/GFTEST | 列齐 6 个 | ✅ |
| Core Exp 3 | GFREFID/GFORRES/GFSTRESC/GFDTC/GFMETHOD | GFSTRESC 对, GFGENE+GFVARIANT 臆造 | ❌ |
| (a) Exon 19 → GFGENSR | GFGENSR | **GFLOC** (臆造) | ❌ |
| (b) dbSNP ID → GFPVRID | GFPVRID | **GFREFID** (臆造) | ❌ |
| (c) 基因组参考 → GFGENREF | GFGENREF | **GFREFVER** (臆造) | ❌ |
| (d) Inheritability → GFINHERT | GFINHERT (CT C181177) | **GFSTYPE / GFVALGRP / GERMLINE / SOMATIC** (完全错) | ❌ |

## Verdict

**FAIL** — 4/4 专门子问题 (a/b/c/d) 全部使用**臆造变量名** (GFLOC, GFREFID, GFREFVER, GFSTYPE/GFVALGRP), **不是** v3.4 GF 域真实的 GFGENSR / GFPVRID / GFGENREF / GFINHERT. 触 FAIL 判据 "臆造变量如 GFGENE / GFVARIANT (其实是 GFSYM / GFORRES)" + "说 GFINHERT 不存在". 虽识别域为 GF + Core Req 正确 + 源路径引用 KB 文件 (但实际未落实到变量级), 但专属 v3.4 新变量深度 **完全失守** — 典型 generalization 失败: Gemini 用 pre-train 记忆 (GF-like 通用命名如 GFGENE/GFLOC/GFREFID 像 XXREFID/XXLOC 通用模式) 覆盖 KB spec.md 真实新变量.

- 04 引用: 无 (pure generalization probe 合规)
- CO-2 触发: 无
- Score: 0 / 1
