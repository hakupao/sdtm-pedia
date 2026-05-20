# R4 Sanity Q1 — GF EGFR variant (Gemini v8.1 LIVE)

**Date**: 2026-05-20 AM
**Platform**: Gemini Gem v8.1 LIVE (SDTM Knowledge Base Gem; `ai_platforms/gemini_gems/current/system_prompt.md` 525 行)
**Question source**: `ai_platforms/SMOKE_V4.md:440-466`
**Execution**: Chrome DevTools MCP, fully automated (no human paste-in-between)
**Conversation URL**: https://gemini.google.com/u/1/gem/3b572e310813/313d77842ceec238

---

## 题目

> 某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 **5 个 Core=Req 变量** 和 **3 个 Core=Exp 变量** (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.

---

## Gemini v8.1 答案 (从 a11y snapshot 完整抽取)

**结论**: 这条 EGFR 激活突变的测序结果应该记录在 **GF (Genomics Findings) 域**。虽然业务场景涉及"外周血样", 其实际的采血和制备行为应记录在 **BE (Biospecimen Events) 域**, 但基因测序的发现与测量结果必须归入 GF 域。

**核心变量清单** (依据 GF 域规范, 优先展示 Topic 变量):

Core=Req 变量:
- **GFTESTCD** (Genomics Test Short Name, Topic 变量)
- **GFTEST** (Genomics Test Name, Topic 变量)
- STUDYID (Study Identifier)
- DOMAIN (Domain Abbreviation, 值为 "GF")
- USUBJID (Unique Subject Identifier)
- **GFSEQ** (Sequence Number)

Core=Exp 变量:
- **GFORRES** (Original Result, 用于记录突变结果)
- **GFSTRESC** (Standardized Character Result)
- **GFDTC** (Date/Time of Finding)

**具体场景映射 (a-d)**:
- (a) "Exon 19" 位置信息: **GFGENSR** (Genetic Sub-Region, Core=Perm). 禁止臆造 GFLOC.
- (b) dbSNP ID (rs121913444): **GFPVRID** (Published Variant Identifier, Core=Perm). 禁止臆造 GFVARIANT.
- (c) 基因组参考版本 (GRCh38.p13): **GFGENREF** (Genome Reference, Core=Perm). 禁止臆造 GFREFVER.
- (d) 遗传性标识: **GFINHERT** (Inheritability, Core=Perm), 受控于 CT Code `C181177`. 禁止臆造 GFSTYPE.

**依据**: 在 SDTMIG v3.4 中, 旧版的 PF (Pharmacogenomics Findings) 域已被完全废弃 (deprecated), 基因发现数据由 GF 域替代承载。此外, 本场景中的基因名称 (EGFR) 属于业务语义的 Topic 层, 应通过 GFTESTCD/GFTEST 承载, 绝不允许将其映射为不存在的 GFGENE 变量。

**CDISC 来源**: SDTMIG v3.4 GF domain — spec

---

## Strict 判据 evaluation

| 项 | 判据 | v8.1 答案 | 命中 |
|---|---|---|:---:|
| 1 | 识别域为 GF (Genomics Findings), 不是 LB/PGx/PF | ✅ "GF (Genomics Findings) 域" + 主动说 PF deprecated | ✓ |
| 2 | Core Req ≥ 5: STUDYID/DOMAIN/USUBJID/GFSEQ/GFTESTCD/GFTEST | ✅ 6 个全部列 (GFTESTCD/GFTEST 列首位标 Topic) | ✓ |
| 3 | Core Exp ≥ 3: GFREFID/GFORRES/GFSTRESC/GFDTC/GFMETHOD/VISITNUM | ✅ GFORRES + GFSTRESC + GFDTC | ✓ |
| 4 | (a) GFGENSR 存 "Exon 19" | ✅ "GFGENSR (Genetic Sub-Region, Core=Perm)" | ✓ |
| 5 | (b) GFPVRID 存 "rs121913444" | ✅ "GFPVRID (Published Variant Identifier, Core=Perm)" | ✓ |
| 6 | (c) GFGENREF 存 "GRCh38.p13" | ✅ "GFGENREF (Genome Reference, Core=Perm)" | ✓ |
| 7 | (d) GFINHERT (Inheritability, CT C181177) | ✅ "GFINHERT" + 引用 CT `C181177` | ✓ |
| 8 | FAIL: 答成 LB/PGx/PF? | ✅ 无, 主动 PF deprecated | ✓ |
| 9 | FAIL: 臆造 GFGENE/GFVARIANT? | ✅ 主动 5 禁忌: GFGENE/GFVARIANT/GFLOC/GFREFVER/GFSTYPE | ✓ |
| 10 | FAIL: GFCHROM 和 GFGENSR 弄混? | ✅ 无, 只用 GFGENSR | ✓ |

**10/10 命中, 0 FAIL**

---

## PASS+ upgrade evidence (vs R3 v7.1 baseline PASS)

R3 v7.1 答案是 PASS (无 +). R4 v8.1 升级到 PASS+, 升级点:

1. **主动列 5 个 anti-hallucination 禁忌变量** (GFGENE/GFVARIANT/GFLOC/GFREFVER/GFSTYPE) — v8.1 CO-5 default reflection 体现, 无 reflection prompt 自动触发"禁止臆造"对照
2. **主动跨域提 BE (Biospecimen Events)** — v8.1 4-prong CO-1 体现 (BE/BS/RELSPEC sticky anchor); 题目仅说"外周血样"未要求列 BE, v8.1 主动补"采血/制备 → BE 域"
3. **主动引用 CT Code `C181177`** — 超出判据要求, KB grounded 精确度
4. **主动声明 PF deprecated** — 判据只要求"不答成 PF", v8.1 主动给出"PF 已废" + "GF 替代承载"对照
5. **KB citation 锚点多处** (snapshot 中多个 "View source details" 按钮) — KB grounded 强信号

---

## Watch findings (v8.1 reviewer audit Rule D #17, 4 项 LOW/MED)

| Watch | 该题观察 | 风险 |
|---|---|---|
| M2 候选数限 (Q2 多变量题特别注意) | Q1 不适用 (单变量答案) | — |
| PASS+ §1.2 strict 应 "AHP 专属" | Q1 非 AHP, 但 v8.1 给 PASS+ 级答案 → 反证 strict 不仅限 AHP, 一般题 PASS+ 也合理 | LOW (caveat) |
| CO-5 default reflection (Q6/Q14 timing/跨域看) | Q1 已展现 default reflection (主动 anti-hallucination), 无过度自我修正 | ✓ no risk |
| CO-2f 文件格式 gate (Q5 边界判别) | Q1 非文件格式题, gate 没误触 | ✓ no risk |

---

## Conclusion

**Verdict: PASS+** (R3 baseline PASS, v8.1 升级, **不退化, 反而升级**)

**Regression status**: ✅ 无回归. v8.1 在 Q1 上比 v7.1 表现更强 (4-prong + default reflection 都触发, 主动补深度).

**Next**: Q2 (CP CD4+ T 细胞, multi-variable, watch M2 候选数限).
