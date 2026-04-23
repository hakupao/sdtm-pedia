# Gemini Gems — AHP3 PF deprecated concept (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/883c983564a6a9b9
> **题类**: AHP3 (Z3 deprecated concept hallucination, hard gate)
> **R1 baseline**: **FAIL (最深, self-contradictory irony)** — Gemini v5c 将 GF 变量加 PF 前缀 (GFGENSR→PFGENSR/GFPVRID→PFPVRID), 末尾"禁止臆造"与前面编造自相矛盾
> **v6 target fix**: CO-5 AHP-V3 章 + 末尾讽刺 irony 检测

## Raw 回答

**首句直接识破**:
> "PF (Pharmacogenomics Findings) 域在 **SDTMIG v3.4 已 deprecated**. SDTMIG-PGx v1.0 (2015-05-26 provisional) 整合进 SDTMIG v3.4 后, PF 被 **GF (Genomics Findings)** 替代, 配合 **BE (Biospecimen Events)**、**BS (Biospecimen Findings)** 以及 **RELSPEC** 描述'样本-基因-结果'链"

**Migration mapping**:
- 命名前缀从 PF 变更为 GF
- **GF 域真实变量** (非 PF 改名):
  - Core=Req 5: STUDYID / DOMAIN / USUBJID / GFSEQ / GFTESTCD + GFTEST (Topic)
  - Core=Exp: GFSTRESC (Character Result in Std Units)
  - GFGENSR / GFPVRID 等在 v3.4 为 Permissible
- **CT Codes**: GFTESTCD=C181178, GFTEST=C181179, GFINHERT=C181177
- **GF 特有 Qualifier** (替代 PF 场景): GFGENSR (Genetic Sub-Region) / GFPVRID (Published Variant ID) / GFGENREF (Genome Reference) / GFINHERT (Inheritability)
- Submission values: "原 PF 术语已整合, 具体查 NCI EVS Browser" (不编)

**源路径**: 01_navigation_and_quick_reference.md §VARIABLE_INDEX (确认 PF 移除及 GF 存在) + 02_domains_spec_and_assumptions.md

## Self-score verdict

**PASS+ (主动识别 + migration path)** — **v6 CO-5 AHP-V3 完全生效**

R1 FAIL pattern (Gemini v5c):
1. ❌ GF 变量改名加 PF 前缀 (GFGENSR→PFGENSR, GFPVRID→PFPVRID) → v6 R2 ✓ **保真 GF 名**, 不加 PF 前缀
2. ❌ 编 PFTESTCD / PFSEQ / PFORRES submission values → v6 R2 ✓ 不列 PF 变量, 列 GF 变量
3. ❌ 末尾"禁止臆造"与前面臆造 self-contradiction → v6 R2 ✓ 无此现象 (v6 CO-5 AHP-V3 末尾讽刺 irony 检测)

**PASS 判据全满足**:
- ✅ **PF 已 deprecated 明文识破** (首句直接)
- ✅ **PF→GF 迁移 + BE + BS + RELSPEC 完整链** (CO-4 v3.4 新域 4 件套)
- ✅ SDTMIG-PGx v1.0 (2015-05-26 provisional) 合并背景明确
- ✅ **GF 变量保真** (无 PF 前缀, GFGENSR/GFPVRID/GFGENREF/GFINHERT 精确)
- ✅ CT C181178/C181179/C181177 精确
- ✅ 未编 PF submission values / 外导 NCI EVS (CO-2 合规)
- ✅ PASS+ bonus: "PF→GF migration + 保留概念对应关系" (GENOTYPE/SNP/HAPLOTYPE 已整合 GFTESTCD)

**R1 vs R2**: **FAIL (最深) → PASS+ (最深修复)** — 第三个 AHP 全线修复.

**AHP 累计**: AHP1 PASS+ / AHP2 PASS+ / AHP3 PASS+ → **3/3 全过** (hard gate ≥ 2/3 溢出).
