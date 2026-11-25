# Q1 (A1 — GF 域) EGFR 基因变异场景

> Date: 2026-04-22
> Account: bojiang.zhang.0904@gmail.com
> Notebook: SDTM Knowledge Base (42/42 sources, Chat Custom mode, fresh chat)

---

## 题

某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 5 个 Core=Req 变量 和 3 个 Core=Exp 变量 (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.

## NotebookLM 答 (full text)

该测序结果属于基因组变异发现, 应当记录在 **GF (Genomics Findings, 基因组学发现)** 域 [18_fnd_device_da_dd_gf_is.md, 41_variable_index.md]。

涉及的变量 (按 Topic 变量优先排序, 以下列出 6 个 Core=Req 变量和 4 个 Core=Exp 变量):

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| GFTESTCD | Char | Topic | Req | C181178 | [18_fnd_device_da_dd_gf_is.md] |
| GFTEST | Char | Synonym Qualifier | Req | C181179 | [18_fnd_device_da_dd_gf_is.md] |
| STUDYID | Char | Identifier | Req |  | [18_fnd_device_da_dd_gf_is.md] |
| DOMAIN | Char | Identifier | Req |  | [18_fnd_device_da_dd_gf_is.md] |
| USUBJID | Char | Identifier | Req |  | [18_fnd_device_da_dd_gf_is.md] |
| GFSEQ | Num | Identifier | Req |  | [18_fnd_device_da_dd_gf_is.md] |
| GFORRES | Char | Result Qualifier | Exp |  | [18_fnd_device_da_dd_gf_is.md] |
| GFSTRESC | Char | Result Qualifier | Exp |  | [18_fnd_device_da_dd_gf_is.md] |
| GFREFID | Char | Identifier | Exp |  | [18_fnd_device_da_dd_gf_is.md] |
| GFMETHOD | Char | Record Qualifier | Exp | C85492 | [18_fnd_device_da_dd_gf_is.md] |

针对该条特定结果的记录说明:

- **(a) 如何记录 "Exon 19" 位置信息**: 应当记录在 `GFGENSR` (Genetic Sub-Region) 变量中 [18_fnd_device_da_dd_gf_is.md]。该变量 (Core=Perm, Role=Variable Qualifier) 用于记录发现变异所在的基因座子区域 (SDTM 标准示例中明确包含了 "Exon 15" 等外显子信息) [18_fnd_device_da_dd_gf_is.md]。
- **(b) 如何引用 dbSNP ID (如 rs121913444)**: 应当记录在 `GFPVRID` (Published Variant Identifier) 变量中 [18_fnd_device_da_dd_gf_is.md]。该变量 (Core=Perm, Role=Variable Qualifier) 专门用于记录在外部数据库中已公开表征的变异的唯一标识符 (指南示例包括 "rs121913227", "COSM41596") [18_fnd_device_da_dd_gf_is.md]。
- **(c) 基因组参考版本 (例如 GRCh38.p13) 存哪**: 应当记录在 `GFGENREF` (Genome Reference) 变量中 [18_fnd_device_da_dd_gf_is.md]。该变量 (Core=Perm, Role=Variable Qualifier) 用于记录生成该报告结果时所参照的基因组参考版本 (指南给出的示例即为 "GRCh38.p13") [18_fnd_device_da_dd_gf_is.md]。
- **(d) 如果该变异可遗传给下一代, 走哪个变量**: 应当记录在 `GFINHERT` (Inheritability) 变量中 [18_fnd_device_da_dd_gf_is.md]。该变量用于标识变异是否能传递给下一代。当变异属于可遗传的生殖细胞系变异时, 必须使用受控术语 (Codelist: C181177) 中的完整规范值 `GERMLINE VARIATION` [37_ct_misc_int_dm_sp_td_gf_oi_other.md]。

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| Domain = GF (not LB/PF) | GF | GF (Genomics Findings) | ✅ |
| ≥5 Req vars | STUDYID/DOMAIN=GF/USUBJID/GFSEQ/GFTESTCD/GFTEST | All 6 listed | ✅ |
| ≥3 Exp vars | GFREFID/GFORRES/GFSTRESC/GFDTC/GFMETHOD/VISITNUM | GFORRES, GFSTRESC, GFREFID, GFMETHOD (4) | ✅ |
| (a) Exon 19 → GFGENSR | GFGENSR | GFGENSR + 示例 "Exon 15" | ✅ |
| (b) dbSNP → GFPVRID | GFPVRID | GFPVRID + 示例 rs121913227 | ✅ |
| (c) GRCh38.p13 → GFGENREF | GFGENREF | GFGENREF + 示例 GRCh38.p13 | ✅ |
| (d) Inheritability → GFINHERT | GFINHERT | GFINHERT + GERMLINE VARIATION + C181177 | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 全 7 项判据命中 + 加分: Codelist C181177 GERMLINE VARIATION 规范值 + GFMETHOD CT C85492 + GFTESTCD CT C181178 全部对。无任何 FAIL 触发。
