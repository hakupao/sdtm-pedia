# ChatGPT GPTs — Q1 GF EGFR 变异 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8a045-163c-83ab-9e9b-67af11039862
> **题类**: Q1 (A1 v3.4 新域 GF)

## Prompt (v4.0 原题, 同 NotebookLM)

## Raw 回答

- **域**: GF (Genomics Findings) ✓ (非 LB/MS 理由明确)
- **Req** (6): GFTESTCD (Topic, e.g. SNV) + GFTEST (Single Nucleotide Variation) + STUDYID + DOMAIN + USUBJID + GFSEQ
- **Exp** (3+): GFORRES + GFSTRESC + VISITNUM (Findings 通则)
- **(a)** GFGENSR = "Exon 19" ✓ + GFGENLOC (精确坐标)
- **(b)** GFPVRID = "rs121913444" ✓
- **(c)** GFGENREF = GRCh38.p13 ✓
- **(d)** **GFINHERTG** = "GERMLINE" ✗ (**变量名拼错, 正确应 GFINHERT**)
- **临床纠错 bonus**: 识破 "Exon 19 + L858R" 不一致 (L858R 经典是 Exon 21; Exon 19 常见的是 deletion 如 ΔE746-A750), SDTM 忠实记录不矫正生物学 ✓

**Citation 数**: 文字 KB 源路径引用 3 个 (GF/spec.md + GF/examples.md + MS/assumptions.md)

## Verdict: **PARTIAL (0.5)**

- 域 ✓ / 5 Req ✓ / 3 Exp ✓
- (a)(b)(c) ✓
- **(d) 变量名 GFINHERTG 拼错** (应 GFINHERT per KB + SMOKE_V4.md §2 判据) — 单字母差, 触及 variable identity awareness 缺陷, 按 v4.0 FAIL 判据 "臆造变量" 严 FAIL, 但 GERMLINE 值正确 + 语义对 → **PARTIAL**
- **临床纠错加分**: L858R Exon 21 识破展示 ChatGPT 非 SDTM 领域强; **主动识破错前提** 虽非 AHP 题但体现纠错能力
- F-3 carry-over: ChatGPT 推理暴露 (Extended 模式, ~3 min 思考)
