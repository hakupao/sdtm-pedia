# ChatGPT GPTs — V5C Regression Results (Q4-Q10, v2.2 LIVE)

> **Purpose**: 消化 Phase 5 retro §2 G5-4 "Q4-Q10 v5c 等价 10/10 假设未实测" 缺口; 双 reviewer #24 M-2 / #25 MED-1 独立交叉 flag 要求的 verification task.
> **Execution time**: 2026-04-24 (Chrome MCP full-auto)
> **System prompt live**: v2.2 (post Q1 GFINHERT 精确校验 patch applied 2026-04-24)
> **Scope**: Q4-Q10 共 7 题 (N5.4 原推论 "v5c 改 CO-4 只影响 Q1/Q2/Q3 v3.4 新域题, 不碰 Q4-Q10")
> **Prior R1 baseline preserved**: `smoke_v4_answers/Q{4-10}_answer_r1_pre_v2.2.md` (Rule B)
> **Full V5C plan**: `ai_platforms/V5C_REGRESSION_PLAN.md`

---

## 1. 逐题 Verdict 表

| Q | 题类 | Verdict | 关键命中点 |
|---|---|---|---|
| Q4 | B1 LB/MB/IS 边界 | **PASS** | A=IS/B=IS/C=MB; Host vs Pathogen + Ag/Ab combo 例外; ISBDAGNT + ISTSTOPO SCREEN/CONFIRM/QUANTIFY 深度 |
| Q5 | B2 FA/QS/CE 边界 | **PASS** | A=FA (RELREC 关联 MH bonus) / B=QS (SF36312-319 8 维度 QSTESTCD 精确) / C=CE (CEDUR=PT30S ISO duration bonus) |
| Q6 | C1 PC Timing 4-件套 | **PASS** | PCTPT=4H / PCTPTNUM=3 / PCTPTREF=PERIOD 1 DOSE / PCELTM=PT4H / PCRFTDTC ISO datetime; 两周期完整示例表 |
| Q7 | C2 Partial date + ADaM imputation | **PASS** | A=2024-06 / B=2024 / C=null; SDTM 不 imputation, ADaM 派生 ASTDT; 相对 timing CMSTRTPT/AEENRTPT (非 SUPP) |
| Q8 | D1 CT Extensible + MedDRA | **PASS+** equivalent | Ext Yes/No 精确; AEDECOD 绑 MedDRA 非 AETERM (PASS+ bonus); "very bad headache" 业务示例; LBLOINC external codelist |
| Q9 | E1 Pinnacle 21 FAIL 分类 | **PASS** | 6 类 FAIL (结构/Required/CT/日期/Key/跨域); cSDRG 6 字段模板; "不为 0 FAIL 改坏数据" 原则; EPOCH/partial date anti-pattern |
| Q10 | H1 SUPP + SUPPTS premise trap | **PASS+** equivalent | **SUPPTS premise caught** + TSVAL1-TSVALn canonical; QORIG Req/QEVAL Exp 精确 Core; AEACNOTH→AEACNOT1/2 §4.5.3.2 8-char 拆分示例 |

**总分 (strict)**: **7/7 (100%)** (2 PASS+ equivalent: Q8 AEDECOD 绑定精度 + Q10 SUPPTS AHP premise catch)

---

## 2. 对比 R1 Baseline 差异

| Q | R1 (v2.1) baseline 结论 | V5C (v2.2) 差异 | 判断 |
|---|---|---|---|
| Q4 | PASS | PASS, 深度持平或增 (ISTSTOPO SCREEN/CONFIRM/QUANTIFY) | No regression, slight enrich |
| Q5 | PASS | PASS, RELREC 关联 MH 为 bonus (R1 未明确提) | No regression, 小强化 |
| Q6 | PASS | PASS, 两周期 crossover 示例表为 bonus | No regression |
| Q7 | PASS | PASS, 相对 timing 变量清单 (CMSTRTPT/AEENRTPT) 为 bonus | No regression |
| Q8 | PASS+ | PASS+ equivalent, AEDECOD 绑 MedDRA 非 AETERM 显式 | No regression, 同或持 bonus |
| Q9 | PASS+ | PASS, cSDRG 6 字段模板 + anti-pattern 深度 | No regression |
| Q10 | PASS+ (SUPPTS 主 gate) | PASS+ equivalent, SUPPTS premise catch + §4.5.3.2 8-char 精确 | No regression |

**结论**: **N5.4 推论 "v5c 改 CO-4 只影响 Q1/Q2/Q3, 不影响 Q4-Q10" 成立** — v2.1→v2.2 bullet 加 (v3.4 新域变量名精确校验) 未污染 Q4-Q10.

---

## 3. 总分 + 判定

| 指标 | 值 |
|---|---|
| Q4-Q10 总题数 | 7 |
| PASS | 5 (Q4/Q5/Q6/Q7/Q9) |
| PASS+ equivalent | 2 (Q8 + Q10) |
| PARTIAL | 0 |
| FAIL | 0 |
| Strict score | **7/7 (100%)** |
| 主阈值 (§3.1) | 7/7 |
| **Gate** | **PASS (strict 7/7)** ✓ |

---

## 4. 跨题 v2.2 patch 持续性观察

- v2.2 "v3.4 新域变量名精确校验" bullet 主测目标是 Q1 GFINHERT — 本 regression (Q4-Q10) 不触, 无旁题副作用
- Extended thinking planning 行为 (如 Q1 "我会按 SDTMIG v3.4 新 GF 域核对变量表重点确认...") 在 Q4-Q10 仍触发 ("我会按 SDTMIG 的域定义...") — UI Extended 模式开启正常
- `<!-- source: knowledge_base/... -->` 溯源注释格式 (CO-3 等效) 全部 7 题均引 ✓

---

## 5. Rule B / C / D / E 合规

- **Rule B (失败归档)**: 无 FAIL, 无需 failures/ 归档. R1 原档保留 `Q{4-10}_answer_r1_pre_v2.2.md`.
- **Rule C (Retro 强制)**: Tier 2 retro 非强制 (per V5C plan §5.3), 结果回灌 `PHASE5_RETROSPECTIVE.md §2 G5-4` 闭合记录.
- **Rule D (审阅隔离)**: self-score 完成; **待** 15th R2-line reviewer 独立复核 (候选 `superpowers:code-reviewer` / `oh-my-claudecode:critic`)
- **Rule E (跨平台 cross-check)**: 双平台同题直接对比 (本文件 × `gemini_gems/.../smoke_v4_v7_regression_results.md`); 跨平台观察见 `gemini_gems/.../smoke_v4_v7_regression_results.md §5`

---

## 6. 主结论

1. ✅ **G5-4 闭合**: v5c→v2.2 Q4-Q10 等价假设 **成立** (7/7 strict PASS); 双 Phase 4 reviewer MED flag 已消化
2. ✅ **v2.2 patch 隔离性**: GFINHERT bullet 修 Q1 MINOR 未污染 Q4-Q10
3. ✅ **ChatGPT v2.2 LIVE 健壮**: 7/7 strict + 2 PASS+ equivalent (Q8 AEDECOD 绑定 + Q10 SUPPTS premise) 说明 v2.1→v2.2 base 稳, 无旁题 regression
4. **Rule D 待跟进**: 15th R2-line reviewer 独立复核本 verdict, 2 PASS+ 判断是否正确
