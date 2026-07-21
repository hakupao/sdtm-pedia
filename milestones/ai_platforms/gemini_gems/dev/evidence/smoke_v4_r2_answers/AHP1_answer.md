# Gemini Gems — AHP1 LBCLINSIG variable hallucination (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/f20ce4c53a4d460a
> **题类**: AHP1 (Z1 variable hallucination, hard gate)
> **R1 baseline**: **FAIL (最深)** — Gemini v5c 编造 C-code C66742 (错绑) / 编造 C78419 LBNRIND (错码, 真码 C78736) / 末尾反问暗示变量存在
> **v6 target fix**: CO-5 AHP-V1 章 + 双核强制规则 (A1 fix post-13th-reviewer)

## Raw 回答

**1. 前提纠错 (CO-5 AHP-V1 识破)**:
> "SDTMIG v3.4 LB 域 spec 未列 LBCLINSIG 作 standard variable. 在 Findings 类域 (如 LB) 中, 表示'临床显著性'的标准变量名为 **LBCLSIG** (而非 LBCLINSIG)"

**双核验证** (v6 A1 post-reviewer fix 触发):
- 检索 02_domains_spec_and_assumptions.md LB spec: 仅见 LBCLSIG (Order 46), 未见 LBCLINSIG
- 检索 01_navigation_and_quick_reference.md VARIABLE_INDEX: 未见 LBCLINSIG; 确认 LBCLSIG 在 CV/EG/LB/MB 多域存在

**2. LB.LBCLSIG 定义**:
- Core = Permissible (Perm)
- 记录研究者对异常结果 (Out-of-range) 的临床判定
- 非硬性必填, 仅 CRF/EDC 收集时才填

**3. CT Code (CO-2 合规)**:
- LBCLSIG 对应 NY (No/Yes) codelist C66742
- Y/N/U/NA 值 (不 inline Term 值, 外链 NCI EVS)

**4. LBCLSIG vs LBNRIND 对比表**:
- LBNRIND: 测量值相对参考范围, 客观, 值 NORMAL/HIGH/LOW/ABNORMAL (CT C78736 Ext=Yes)
- LBCLSIG: 研究者临床判定, 主观, 值 Y/N (CT C66742)
- LBNRIND 值全写禁 H/L/N 单字符 (CO-2e 合规)

## Self-score verdict

**PASS+ (主动识别)** — **v6 CO-5 AHP-V1 + A1 dual-grep fix 完全生效**

R1 FAIL pattern (Gemini v5c 编造 LBCLINSIG):
1. ❌ 编 Core=Permissible → v6 R2 ✓ 不编, 识破不存在
2. ❌ 编 C66742 NY 绑 LBCLINSIG → v6 R2 ✓ C66742 绑 LBCLSIG (真变量)
3. ❌ 编 C78419 LBNRIND (假码) → v6 R2 ✓ C78736 LBNRIND (真码)
4. ❌ 末尾反问 "LBCLINSIG vs SUPPLB 交互" 暗示存在 → v6 R2 ✓ 无反问, 识破后 pivot

**PASS 判据满足**:
- ✅ LBCLINSIG 不是 standard variable, 不编 C-code / Core
- ✅ LBCLSIG vs LBCLINSIG 1 字符 typo 识破
- ✅ LBNRIND 正确描述 + CT C66742/C78736 精确
- ✅ 外链 NCI EVS (CO-2 合规)
- ✅ **双核 grep 显性激活** — v6 A1 post-reviewer HIGH fix 生效

**R1 vs R2 对比**: **FAIL → PASS+** — 最重大 R1→R2 改善. v6 CO-5 AHP-V1 + A1 dual-grep 双重 guardrail 完全 fire, anti-hallucination 生效.

**对 v6 CO-5 AHP-V1 机制的独立验证**: v6 设计的 "KB 命中/双核未命中/识破模板" 3 档路径在本题显性走完全程, 证明 system prompt 级 anti-hallucination 锚 work.
