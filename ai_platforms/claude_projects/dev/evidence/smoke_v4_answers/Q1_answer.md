# Claude Projects — Q1 GF EGFR 变异 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM
> **会话 URL**: https://claude.ai/chat/ecf613ab-4028-4488-a55d-a1de5b206d61
> **题类**: Q1 (A1 v3.4 新域 GF)

## Prompt (v4.0 原题, 同 NotebookLM)

## Raw 回答 (摘要)

- **域**: GF (Genomics Findings) ✓ / Class: Findings / Structure: one-record-per-finding-per-observation
- **Req** (6, with row #): GFTESTCD (Topic, C181178, e.g. VARNT) + GFTEST (C181179) + STUDYID + DOMAIN + USUBJID + GFSEQ
- **Exp** (5): GFORRES ("EGFR p.L858R" verbatim) + GFSTRESC ("NM_005228:c.2573T>G:p.L858R" HGVS) + GFMETHOD ("NEXT GENERATION SEQUENCING" C85492) + GFDTC + GFREFID (lab accession)
- **(a)** GFGENSR = "Exon 19" + GFGENLOC (精细) + GFCHROM = "7" (EGFR 染色体) ✓
- **(b)** GFPVRID = "rs121913444" ✓
- **(c)** GFGENREF = "GRCh38.p13" ✓ + GFSEQID = "NM_005228" (RefSeq transcript) / GF assumption #7: 必含 patch level 不能只写 "GRCh38"
- **(d)** GFINHERT = "GERMLINE VARIATION" (C17666) ✓; 完整 CT C181177 表: GERMLINE (C17666) / SOMATIC (C18060) / MITOCHONDRIAL (C181352) — 3 terms Ext=Yes
- **补字段**: GFSYM = "EGFR" / GFSYMTYP (CT C181176) / GFSPEC = "BLOOD" (CT C111114) / GFANMETH (CT C181181)
- **临床纠错**: 同 ChatGPT 识破 L858R = Exon 21 (not 19), Exon 19 典型 deletion ΔE746-A750
- **源路径 3**: GF/spec.md (05_mega_spec.md:942-1006) + GF/assumptions.md #5 #7 (06_assumptions.md:402-419) + terminology/core/gf.md (13a:2864-2874)

## Verdict: **PASS+**

- 6 Req + 5 Exp ✓ (远超 5+3 要求)
- (a)(b)(c)(d) 全对 + 精确 CT code C17666 ✓
- Bonus: 完整 C181177 3-term 表 + GFSYM/GFSPEC/GFANMETH 补字段 + GF assumption #7 patch-level 规则 + 临床纠错
- Claude v2.6 对 v3.4 新域 GF 首测答得最专业, 接近 CDISC reviewer 水平
- 无 FAIL
