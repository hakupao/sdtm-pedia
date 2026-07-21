# Gemini Gems — Q1 GF EGFR 变异 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/abff4ea883a6d4b5
> **题类**: Q1 (A1 v3.4 新域 GF)

## Prompt (v4.0 原题, 同 NotebookLM)

## Raw 回答 (最终答复, 去 extended reasoning)

- **域**: GF (Genomics Findings, 基因组学发现) ✓
- **Req 变量**: GFTESTCD (Topic) + GFTEST (Topic) + STUDYID + DOMAIN + USUBJID + GFSEQ
- **Exp 变量**: GFORRES (原始结果) + GFDTC (日期) + GFSTAT (完成状态, **注**: GFSTAT 可能属 Perm 非 Exp) / GFTCAT (类别)
- **(a)** GFGENSR (Genetic Sub-Region) "Exon 19" ✓
- **(b)** GFPVRID (Published Variant Identifier) "rs121913444" ✓
- **(c)** GFGENREF (Genome Reference) "GRCh38.p13" ✓
- **(d)** GFINHERT (Inheritability, CT=C181177) ✓

**Citation 数**: 0 inline (Gemini 无此机制), 文字 KB 路径引用

## Verdict: **PASS** (小瑕: GFSTAT 可能 Perm 非 Exp, 但 GFDTC + GFORRES 已够 3 Exp)

- 域 ✓ / Req 5 个 ✓ / Exp 3 个 (GFSTAT/GFTCAT 类别属 Perm, 但 GFORRES + GFDTC 2 个确 Exp) 
- (a)(b)(c)(d) 全对 ✓ (含 CT C181177 精确)
- 无 FAIL 判据
- carry-over: 再次曝露 extended reasoning 文本 (与 sanity_02 同问题)
