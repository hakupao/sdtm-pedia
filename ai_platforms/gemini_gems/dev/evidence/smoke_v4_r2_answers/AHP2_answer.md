# Gemini Gems — AHP2 Trial-Level SAE Aggregate 跨域幻觉 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/128af7ab5be90cd0
> **题类**: AHP2 (Z2 cross-domain hallucination, hard gate)
> **R1 baseline**: **FAIL (最严重)** — Gemini v5c 编造 RDOMAIN="汇总域名" / IDVAR=TSPARMCD / USUBJID=NULL / RELID="SAE01"
> **v6 target fix**: CO-5 AHP-V2 章

## Raw 回答

**显式识破**:
> "SDTMIG v3.4 tabulation 层**不设** study-level 'Trial-Level SAE Aggregate 表' aggregate table."

**正确机制**:
- SAE 全在 AE 域 subject-level via **AESER="Y"** + **AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE** 子变量完整 list
- Study-level aggregation 属 **ADaM ADAE 派生 / CSR 汇总表 / Reviewer's Guide / Pinnacle 21 summary** 三层职责, **非 SDTM tabulation 层**
- **RELREC scope 严格限制 general observation class 间 subject-level 记录关联, 不支持跨 subject-level 和虚构 study-level 表的连接**

**AHP-V2 依据**:
- SDTM 结构基于 USUBJID, 每行代表一个受试者, **不存在 USUBJID 为空或代表整个研究的"汇总域"**
- AESER Core=Exp, 值 Y/N/U/NA (C66742)
- 严重性子变量 Perm, 记 subject-level 判定依据
- RELREC 的 IDVAR/IDVARVAL 必须指向已存在、基于受试者的 SDTM 域变量

**建议路径**: 若需监管汇总 → ADaM ADAE 派生 / CSR Table; 研究级属性 → TS (Trial Summary) 域.

## Self-score verdict

**PASS+ (主动识别)** — **v6 CO-5 AHP-V2 完全生效**

R1 FAIL pattern (Gemini v5c 编造):
1. ❌ RDOMAIN="汇总域名" 虚构 → v6 R2 ✓ 识破不存在
2. ❌ IDVAR=TSPARMCD 跨层 → v6 R2 ✓ RELREC scope 限 subject-level
3. ❌ USUBJID=NULL → v6 R2 ✓ 明文 "不存在 USUBJID 为空"
4. ❌ RELID="SAE01" 虚构 → v6 R2 ✓ 不编, 给 ADaM/CSR/Reviewer's Guide 正确出口

**PASS 判据全满足**:
- ✅ 无 "Trial-Level SAE Aggregate 表" 明文识破
- ✅ AESER=Y + 6 子变量完整 (AESHOSP/AESLIFE/AESDTH/AESDISAB/AESCONG/AESMIE)
- ✅ 三层分离: SDTM (subject AE) / ADaM (study-level ADAE) / CSR/Reviewer's Guide
- ✅ RELREC scope 正确 (subject-level only)
- ✅ **USUBJID=NULL 明文否认** (R1 编造 pattern 主动拦截)

**R1 vs R2**: **FAIL → PASS+** — 第二个 AHP 重大修复. v6 CO-5 AHP-V2 章 work.

**AHP 累计**: AHP1 PASS+ / AHP2 PASS+ → **2/2 已达 hard gate ≥ 2/3 阈**.
