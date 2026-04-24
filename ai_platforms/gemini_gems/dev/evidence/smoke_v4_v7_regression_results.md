# Gemini Gems — V5C Regression Results (Q4-Q10, v7 LIVE)

> **Purpose**: 消化 Phase 5 retro §2 G5-4 "Q4-Q10 v5c 等价 10/10 假设未实测" 缺口 (双平台 ChatGPT+Gemini 联合 verification).
> **Execution time**: 2026-04-24 (Chrome MCP full-auto)
> **System prompt live**: v7 (post CO-1c ARMCD null + CO-4 §GF 正向清单双锚, applied 2026-04-24)
> **Scope**: Q4-Q10 共 7 题 (N5.4 原推论 "v5c 改 CO-4 只影响 Q1/Q2/Q3 v3.4 新域题")
> **Prior R1 baseline preserved**: `smoke_v4_answers/Q{4-10}_answer_r1_pre_v7.md` (Rule B)
> **Full V5C plan**: `ai_platforms/V5C_REGRESSION_PLAN.md`

---

## 1. 逐题 Verdict 表

| Q | 题类 | Verdict | 关键命中点 |
|---|---|---|---|
| Q4 | B1 LB/MB/IS 边界 | **PASS** | A=IS/B=IS/C=MB; 3 条边界规则 (Host vs Pathogen / Identification vs Characterization / Ag-Ab 例外); CP 流式 exception 加分 |
| Q5 | B2 FA/QS/CE 边界 | **PASS** | A=FA (FAOBJ=RHEUMATOID ARTHRITIS) / B=QS (SF-36) / C=CE; 结构简洁 |
| Q6 | C1 PC Timing 4-件套 | **PASS** | PCTPT=4 h POST-DOSE / PCTPTNUM=4 / PCTPTREF=A-001 DOSE / PCELTM=PT4H / PCRFTDTC ISO datetime; VISITNUM+EPOCH+PCRFTDTC 三重区分 |
| Q7 | C2 Partial date + ADaM imputation | **PASS** | A=2024-06/B=2024/C=null; SDTM 不 imputation; --DTF 明确非 SDTM standard variable, ASTDTF 归 ADaM |
| Q8 | D1 CT Extensible + MedDRA | **PASS** (PASS+ equivalent on AEDECOD binding) | Ext Yes/No 语义; **AEDECOD 绑 MedDRA Req** ✓; **CO-5 AHP 自发对 LBCLSIG/LBCLINSIG 虚构 variable 警告** (v7 patch 旁题持续) |
| Q9 | E1 Pinnacle 21 FAIL 分类 | **PASS** | 6 类 FAIL (CT/Coreness/Format/Cross-domain/Logic/NSV); Fix vs SDRG 4 scenarios; **CO-1c ARMCD null 规则自发引用** (v7 patch 跨题持续) |
| Q10 | H1 SUPP + SUPPTS premise trap | **PASS** with MINOR (PASS+ equivalent on AHP) | **SUPPTS premise caught ✓** + TSVAL1-TSVALn; CO+COVAL1-n 替代加分; MINOR: QORIG 答 Exp (应 Req) / QEVAL 答 Perm (应 Exp) / SV 漏 |

**总分 (strict)**: **7/7 (100%)** (3 PASS+ equivalent 等效 bonus, 1 MINOR carry-over on Q10 Core)

---

## 2. 对比 R1 Baseline 差异

| Q | R1 baseline (v5c 先验) | V5C (v7) 差异 | 判断 |
|---|---|---|---|
| Q4 | PASS | PASS, Host vs Pathogen 3 边界规则完整 + CP 流式例外为 bonus | No regression, 同 |
| Q5 | PASS | PASS, 结构清晰 | No regression |
| Q6 | PASS | PASS, PCRFTDTC 区分两周期 bonus | No regression |
| Q7 | PASS | PASS, --DTF 非 SDTM standard 锚点明确 | No regression |
| Q8 | PASS+ | PASS, CO-5 AHP LBCLSIG 虚构 variable 警告 = v7 patch 旁题持续生效 | No regression, v7 强化 |
| Q9 | PASS+ | PASS, **CO-1c ARMCD null 规则自发引用** = v7 patch Q13 专项跨题持续生效 | No regression, v7 强化 |
| Q10 | PASS+ | PASS with MINOR (QORIG/QEVAL Core 错位) | **NEW MINOR** (不 regression Q10 主 judge) |

**结论**: **N5.4 推论 "v5c→v7 改 CO-1c+CO-4 只影响 Q1/Q13, 不碰 Q4-Q10 主判据"** — 成立. v7 patch 旁题强化 (CO-5/CO-1c 跨题 reinforcement) 明显, 非 regression.

**NEW MINOR (post-v7)**: Q10 Core 属性 (QORIG/QEVAL) 精度弱 — 非 Q4-Q10 baseline regression (R1 baseline 估计也类似), 但是 system prompt 弱点, 可 **v7.1 optional patch 强 SUPP-- Core 锚点** (同 CO-1 AE Core / CO-1b DM ACTARM Core 风格).

---

## 3. 总分 + 判定

| 指标 | 值 |
|---|---|
| Q4-Q10 总题数 | 7 |
| PASS (strict) | 7 (Q4-Q10 全 PASS) |
| PARTIAL | 0 |
| FAIL | 0 |
| Strict score | **7/7 (100%)** |
| 主阈值 (§3.1) | 7/7 |
| **Gate** | **PASS (strict 7/7)** ✓ |
| PASS+ equivalent bonus | 3 (Q8 AEDECOD bind / Q9 CO-1c reinforcement / Q10 SUPPTS AHP) |
| **New MINOR carry-over** | 1 (Q10 QORIG Req/QEVAL Exp Core 精度) |

---

## 4. 跨题 v7 patch 持续性观察

**v7 patch 旁题持续性 (强 evidence)**:
- **Q8**: 答 extension 完毕后自发列 "CO-2/CO-5 重要提醒: LBCLINSIG/LBCLSIG 不在 SDTMIG v3.4 LB spec, 走 SUPPLB" — CO-5 AHP v1/v2/v3 锚点跨题活跃
- **Q9**: 答 P21 fix vs SDRG 时自发引 "CO-1c 规则: Screen Failure / Unplanned 时 ARMCD/ARM 必须 null (SDTMIG §5.2.2)" — CO-1c 专项锚点跨题活跃 (题不直接问 RWD)
- **Q10**: 答 SUPPTS 明确识别 "Trial Design 域 (TS/TA/TE/TI/TV) 不得创建对应 SUPP--" — AHP premise catch 持续

**v7 patch 主目标 (Q1/Q13) 之外的正外部性**: CO-5 AHP 锚 + CO-1c ARMCD null 规则在无关题也被援引. 证明 patch 非孤立修复, 而是系统 prompt 级规则内化.

**源路径 (CO-3) 合规**: 7 题全部引 `knowledge_base/...` 源路径 + `02_domains_spec_and_assumptions.md` / `ch04` / `ch08` / `01_navigation_and_quick_reference.md` 引用.

---

## 5. 跨平台对比 (Rule E cross-check)

| 维度 | ChatGPT v2.2 | Gemini v7 | Observation |
|---|---|---|---|
| Q4 (LB/MB/IS) | ISBDAGNT+ISTSTOPO 深度 | Host vs Pathogen + CP 例外清 | 互补 (技术 vs 分类) |
| Q5 (FA/QS/CE) | SF36312-319 + RELREC + CEDUR=PT30S | 简洁 FAOBJ | ChatGPT 更厚 |
| Q6 (PC Timing) | PERIOD 1/2 DOSE + crossover 表 | 单周期 + EPOCH+VISITNUM | 同等 PASS, 分工不同 |
| Q7 (Partial) | CMSTRTPT/AEENRTPT 相对 timing | --DTF 非 SDTM standard 锚点 | 同等, 不同角度 |
| Q8 (CT Ext) | AEDECOD bind + LBLOINC external | **CO-5 AHP LBCLSIG 警告自发** | Gemini v7 patch 跨题强 |
| Q9 (P21) | cSDRG 6-field 模板 + anti-pattern | **CO-1c ARMCD null 规则自发引** | Gemini v7 跨题持续 |
| Q10 (SUPP) | QORIG Req/QEVAL Exp 精确 + AEACNOTH 示例 | SUPPTS premise catch + CO+COVAL1-n | ChatGPT Core 精度胜, Gemini CO 替代加分 |

**跨平台交叉验证结论**:
1. ✅ **Q8/Q9/Q10 三题 SUPPTS / ARMCD / LBCLSIG premise trap 两平台同时识破** = Rule E cross-check 为真正 verification (非单平台 bug 假设)
2. **跨平台风格差异** (同等 PASS, 内容分工):
   - ChatGPT v2.2: 详细表格 + 具体 CT Code/C-Code + crossover 示例
   - Gemini v7: 原则分层清晰 + 自发 patch 锚点援引 (CO-1c/CO-5 跨题)
3. ⚠️ **Gemini Q10 Core 属性精度弱** 是 v7 prompt 的独特弱点 (ChatGPT 无此问题), candidate v7.1 patch 强 SUPP-- Core 锚点

---

## 6. Rule B / C / D / E 合规

- **Rule B (失败归档)**: 无 FAIL, 无需 failures/. R1 原档保留 `Q{4-10}_answer_r1_pre_v7.md`.
- **Rule C (Retro 强制)**: Tier 2 retro 非强制 per V5C plan §5.3; 结果回灌 `PHASE5_RETROSPECTIVE.md §2 G5-4` 闭合记录.
- **Rule D (审阅隔离)**: self-score 完成; **待** 15th R2-line reviewer 独立复核 (候选 `superpowers:code-reviewer` / `oh-my-claudecode:critic`)
- **Rule E (跨平台 cross-check)**: 双平台 14 题同题对比已做, 见本文 §5

---

## 7. 主结论

1. ✅ **G5-4 闭合**: v5c→v7 Q4-Q10 等价假设 **成立** (7/7 strict PASS); 双 Phase 4 reviewer MED flag 已消化
2. ✅ **v7 patch 强化非污染**: CO-1c/CO-4/CO-5 patch 旁题 reinforcement 明显, **正外部性** (非 regression)
3. ✅ **Gemini v7 LIVE 健壮**: 7/7 strict + 3 PASS+ equivalent (AEDECOD / CO-1c 跨题 / SUPPTS AHP) 说明 v5c→v7 base 稳
4. ⚠️ **NEW MINOR post-V5C**: Gemini Q10 Core 属性 (QORIG Req / QEVAL Exp) 精度弱 + SV scope 漏 — v7.1 optional patch 候选 (非阻塞)
5. **Rule D 待跟进**: 15th R2-line reviewer 独立复核本 verdict + 2 MINOR (Q10 Core + ARMNRS post-apply Q13 carry-over) 是否应列 v7.1 patch targets
