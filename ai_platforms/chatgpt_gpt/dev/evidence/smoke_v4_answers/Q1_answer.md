# ChatGPT GPTs — Q1 GF EGFR 变异 (post-apply smoke, v2.2 live)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q1)
> **执行时间**: 2026-04-24 (post v2.2 apply to GPT Builder UI)
> **执行者**: Bojiang + claude cowork Chrome MCP (full-auto)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69eacdad-8b74-83a7-b990-8557d014bd8f
> **题类**: Q1 (A1 — GF 域, v3.4 新域) / **post-apply 验证 v2.2 patch "v3.4 新域变量名精确校验"**
> **System prompt live**: v2.2 (GFINHERT 7 字母 / 禁 GFINHERTG / CP 三 marker 8 字母 / BE+BS 短名)

---

## 题目原文 (复制自 SMOKE_V4.md §2 Q1)

某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 **5 个 Core=Req 变量** 和 **3 个 Core=Exp 变量** (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.

## 发送给模型的 prompt (实际粘贴文本)

同上 (原题 verbatim, 无包装; Chrome MCP fill)

---

## 模型 raw 回答 (DOM readback 原文)

**Sub-message 1 (planning)**:

> 我会按 SDTMIG v3.4 的新 Genomics Findings（GF）域核对变量表，重点确认 GF 位点、外部数据库、参考基因组和遗传性变量的精确变量名。

**Sub-message 2 (final answer, Thought for 1m 1s)**:

结论：这条记录应放在 **GF — Genomics Findings** 域。GF 是 SDTMIG v3.4 新增的基因组发现域，用于核酸层面的变异、转录等发现，也可包括由核酸结果推断出的蛋白/氨基酸信息；其结构是 "one record per finding per observation per biospecimen per subject"。

另：你给的组合里 **"Exon 19" 与 "L858R"** 在科学含义上看起来不一致；L858R 通常对应 EGFR exon 21。SDTM 映射时不要自行改写原始报告，但应发 data query 或在 reviewer guide/metadata 说明来源。

### 推荐记录思路 (Core=Req 变量表)

| 变量 | Role / Core | 建议值或说明 |
|---|---|---|
| STUDYID | Identifier / Req | 研究编号 |
| DOMAIN | Identifier / Req | GF |
| USUBJID | Identifier / Req | 受试者唯一标识 |
| GFSEQ | Identifier / Req | 受试者内 GF 记录序号 |
| GFTESTCD | Topic / Req | 若报告为单碱基变异，可用 SNV；若更泛化为短变异，可用 SHRTVAR，两者均在 GFTESTCD CT 中出现。 |
| GFTEST | Synonym Qualifier / Req | 如 Single Nucleotide Variation 或 Short Variation；与 GFTESTCD 配套。 |

### 至少 3 个 Core=Exp 变量

| 变量 | Role / Core | 建议值或说明 |
|---|---|---|
| GFORRES | Result Qualifier / Exp | 原始报告结果，例如 L858R、c.2573T>G、EGFR L858R |
| GFSTRESC | Result Qualifier / Exp | 标准化结果；从 GFORRES 复制或派生 |
| GFMETHOD | Record Qualifier / Exp | 测定方法，如 sequencing / NGS；GF cross reference 指向 Method codelist C85492 |
| GFDTC | Timing / Exp | 外周血样本采集日期/时间 |
| GFREFID | Identifier / Exp | 实验室报告号、样本报告 ID 或外部结果引用号 |

### 四个具体问题

**(a) "Exon 19" 位置信息放哪？**
放在 **GFGENSR (Genetic Sub-Region, Core: Perm)**，值可为 Exon 19。GFGENSR 的说明就是变异所在的 locus 子区域，示例包括 Exon 15、Kinase domain。
如果还有更精确坐标，则用 **GFGENLOC (Genetic Location, Core: Perm)** 记录序列内位置。

**(b) dbSNP ID 怎么引用？**
用 **GFPVRID (Published Variant Identifier, Core: Perm)**，值填 **rs121913444**。

**(c) 基因组参考版本 GRCh38.p13 存哪？**
用 **GFGENREF (Genome Reference, Core: Perm)**，值填 **GRCh38.p13**。GFGENREF 的 CDISC notes 明确给出 Genome Reference Consortium Human Build 38 patch release 13 可表示为 GRCh38.p13。

**(d) 如果该变异可遗传给下一代，走哪个变量？**
用 **GFINHERT (Inheritability, Core: Perm, CT: C181177)**。若判断为可遗传/生殖系来源，按该 codelist 选择相应受控术语值，例如 GF example 里有 GFINHERT = **GERMLINE** 的用法。

源溯源：`<!-- source: knowledge_base/domains/GF/spec.md -->`；CT 源：`<!-- source: knowledge_base/terminology/core/gf.md -->`.

**Citation 数**: 2 条 (GF/spec.md + terminology/core/gf.md, 均为源路径注释格式)

---

## Self-score verdict

- **Verdict**: **PASS** (no PASS+ because main gate, not AHP)
- **理由** (对照 SMOKE_V4.md §2 Q1 PASS 判据逐条):
  - 域: **GF (Genomics Findings)** ✓ (正确识别为 v3.4 新域, 不是 PF 旧域)
  - Core Req: STUDYID / DOMAIN / USUBJID / GFSEQ / GFTESTCD / GFTEST (6/5) ✓
  - Core Exp: GFORRES / GFSTRESC / GFMETHOD / GFDTC / GFREFID (5/3) ✓
  - (a) **GFGENSR** "Exon 19" ✓
  - (b) **GFPVRID** rs121913444 ✓ — **v2.2 patch primary target: 未写成 GFINHERTG / GFPVRIDS / 任何 8 字母化形**, 全部精确变量名
  - (c) **GFGENREF** GRCh38.p13 ✓
  - (d) **GFINHERT** (7 字母) + CT **C181177** + GERMLINE 示例值 ✓ — **关键 v2.2 patch 生效: GFINHERT 未再写成 GFINHERTG (R1 regression 修)**
- **触发 FAIL 判据?** 无 (未答 LB/PF 旧域, 未臆造 GFGENE/GFVARIANT, 未混淆 GFCHROM vs GFGENSR)
- **Bonus (v2.2 patch 主测目标)**:
  - ✓ GFINHERT 7 字母精确 (非 8 字母 GFINHERTG) — **v2.2 Q1 MINOR 修生效**
  - ✓ 额外科学 sanity check: 主动标记 "Exon 19 + L858R" 组合不一致 (L858R 实为 Exon 21) — 超出题目要求, 额外 anti-hallucination 加分, PASS+ 级 bonus (仅记录, 不计入主 gate 分)
- **观察**:
  - 答中出现 `GFGENLOC` (Genetic Location) 变量, 不在 v7 CO-4 禁止臆造清单 (GFLOC/GFREFVER/GFSTYPE/GFGENE/GFVARIANT/GFVALGRP), 但需 KB spec 验证是否 v3.4 真实变量 — carry-over LOW (不影响主答案 PASS)
- **F-* carry-over 观察**:
  - ✅ **v2.2 patch 主目标 GFINHERT 精确命名生效** — R1 GFINHERTG PARTIAL MINOR 未再出现
  - ✅ 2.2 extended thinking 模式触发"先核对变量表"的 planning 行为, 有助精确性
  - ⚠️ GFGENLOC 需后续 KB 核定
  - ✅ L858R/Exon 19 不一致科学 sanity catch, 超预期 anti-hallucination

**v2.2 apply status**: ✅ EFFECTIVE (Q1 核心 "v3.4 新域变量名精确校验" bullet 生效)
