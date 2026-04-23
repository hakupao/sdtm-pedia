# Gemini Gems — Q1 GF EGFR 变异 (R2 smoke v4.0, v6-post-A1 system prompt)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/e05b51ebe93f2775
> **题类**: Q1 (A1 v3.4 新域 GF)
> **R1 baseline**: PASS (见 smoke_v4_answers/Q1_answer.md, 5 Req + GFORRES+GFDTC+GFSTAT/GFTCAT 混 Exp/Perm)

## Prompt (v4.0 原题, 同 R1)

某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 **5 个 Core=Req 变量** 和 **3 个 Core=Exp 变量** (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.

## Raw 回答 (DOM 原文)

**1. 归域建议**: 该场景应记录在 **GF (Genomics Findings)** 域. 原 PGx 相关发现已迁移至 GF 域. 同时采血记 BE, 样本测量记 BS, 通过 RELSPEC 建立关联.

**2. 关键变量清单 (GF 域)**:
- **5 Core=Req**: STUDYID / DOMAIN ("GF") / USUBJID / GFSEQ / GFTESTCD / GFTEST (Topic)
- **3 Core=Exp**: **GFGENE** (Gene Name, "EGFR") / GFORRES (L858R) / GFSTRESC

**3. 场景具体映射 (按 CO-4 硬锚)**:
- (a) **Exon 19 → GFGENSR** (Genetic Sub-Region, Core=Perm) ✓
- (b) **dbSNP rs121913444 → GFPVRID** (Published Variant ID, Core=Perm) ✓
- (c) **GRCh38.p13 → GFGENREF** (Genome Reference, Core=Perm) ✓
- (d) **遗传性 → GFINHERT** (Inheritability, Core=Perm, CT=**C181177**) ✓ + 注 Term 值 (GERMLINE/SOMATIC) 查 NCI EVS

**4. 专家纠错与 AHP 预警 (CO-5)**:
- 弃用提示: 严禁存 PF (已 deprecated, AHP-V3 migration → GF)
- 变量名校验: 请勿用 GFLOC / GFVARIANT, 应用 GFGENSR / GFPVRID / GFGENREF
- **注 [主 session 观察]**: 自身在 Exp 清单用了 **GFGENE** (CO-4 禁止臆造清单第 4 项), 但末尾预警只列 GFLOC/GFVARIANT, **self-contradiction**

**源路径**: knowledge_base/domains/GF/spec.md + ch04_general_assumptions.md + 04_business_scenarios §4

## Self-score verdict

**PARTIAL (0.5)** — **REGRESSION vs R1 PASS**

- 域 ✓ (GF 正确 + 主动识别 PF→GF deprecated migration, 额外加分)
- 5 Req ✓ (STUDYID/DOMAIN/USUBJID/GFSEQ/GFTESTCD/GFTEST 6 个)
- (a)(b)(c)(d) 全对 ✓ (包括 C181177 精确 + NCI EVS 外链合规)
- Req+4 子问答 → core facts 满足 PASS 判据大部分
- **FAIL 判据触发**: Exp 清单用 **GFGENE** — SMOKE_V4.md L455 明文 "臆造变量如 GFGENE / GFVARIANT" = FAIL
- v6 自己的 CO-4 §GF 禁止臆造清单 L102 列 **GFGENE**, Gemini v6 自己违反自己的规则
- 末尾"变量名校验"警告 GFLOC/GFVARIANT 但漏 GFGENE → self-contradictory output (同 R1 AHP3 末尾讽刺 irony 模式)
- Exp 3 个里只 2 个 valid (GFORRES + GFSTRESC), GFGENE 臆造 → 不满足"3 个 Exp"要求

**R1 vs R2 对比**: R1 PASS (GFORRES + GFDTC 2 clear Exp + GFSTAT/GFTCAT 边缘); R2 PARTIAL (GFGENE 臆造 + GFORRES + GFSTRESC, 虽然 GFSTRESC 可以算但 GFGENE 是新 defect). v6 CO-5 新增 AHP-V3 锚 deprecated 提醒生效 (主动加 PF→GF 纠错), 但 CO-4 Req/Exp 清单层面 hallucination **未改善反而 regression**.

**Rule D 14th reviewer 争议点**: 可能把 Q1 判 PASS (abcd + 域 + Req 全对, Exp 只是 1 个小瑕). 本评分取严格, 因 v6 CO-4 明文禁止 GFGENE 仍被 v6 自己违反, 这恰是 v6 要修的错.
