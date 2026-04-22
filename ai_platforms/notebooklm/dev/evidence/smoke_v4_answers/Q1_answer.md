# NotebookLM — Q1 GF EGFR 变异 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM
> **会话 URL**: https://notebooklm.google.com/notebook/3f87a93e-9a65-407e-8292-c28706fc6287 (同 sanity chat)
> **题类**: Q1 (A1 v3.4 新域 GF)

## Prompt (v4.0 原题)

某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 5 个 Core=Req 变量 和 3 个 Core=Exp 变量 (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.

## Raw 回答 (关键点)

- **域**: GF (Genomics Findings) ✓ [18_fnd_device_da_dd_gf_is.md]
- **Req** (6): GFTESTCD (Topic C181178) + GFTEST (C181179) + STUDYID + DOMAIN + USUBJID + GFSEQ
- **Exp** (4): GFORRES + GFSTRESC + GFMETHOD (C85492) + GFDTC (ISO 8601)
- **(a)** GFGENSR (Genetic Sub-Region) = "Exon 19" ✓
- **(b)** GFPVRID (Published Variant Identifier) = "rs121913444" ✓
- **(c)** GFGENREF (Genome Reference) = GRCh38.p13 ✓
- **(d)** GFINHERT (Inheritability, C181177) = "GERMLINE VARIATION" ✓ (+ SOMATIC VARIATION 边界)
- **Bonus**: GFTESTCD 建议填 "SNV" (单核苷酸变异) [36_ct_specialized...] + [37_ct_misc...]

**Citation 数**: 16+ inline citations, 主源 [18_fnd_device_da_dd_gf_is.md]

## Verdict: **PASS** (核心判据全中, 边界 note 加分)

- 域 ✓ / 5+ Req ✓ / 3+ Exp ✓
- (a)(b)(c)(d) 全对 ✓
- 无 FAIL 判据触发
- carry-over: 16+ citations 展示 NotebookLM inline citation 优势
