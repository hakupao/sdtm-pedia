# NotebookLM — smoke v4.0 R1 baseline 结果

> **Date**: 2026-04-22 PM (R1 执行中)
> **题库**: `ai_platforms/SMOKE_V4.md §2` v4.0 (17 题 = sanity 3 preflight + Q1-Q14 + AHP1-3)
> **Notebook**: "SDTM Knowledge Base" (42/42 sources, Custom mode, instructions.md 9011 chars)
> **执行者**: claude cowork MCP Chrome Web UI paste
> **Account**: bojiang.zhang.0904@gmail.com
> **合格阈**: ≥12/17 (71%) R1 首测容错 (Q9/Q11/Q13 可能 PUNT)
> **底座 sanity 3 题**: pending (见 §1)
> **上游参考**: smoke v3 P3.8 9/10 strict PASS (SUPERSEDED), v4.0 新增 AHP × 3 + Q10/Q13/Q8/Q4/Q14 patch + Q11-Q14 开放 4 平台共用

---

## 1. Sanity preflight (3 题, 与 P3.8 相同题)

| Q | Topic | Verdict | 答案文件 |
|---|---|---|---|
| sanity_01 | AESER Core=Req or Exp? | **PASS** (Core=Exp + [08_ev_adverse_ae.md]) | `smoke_v4_answers/sanity_01_aeser_core.md` |
| sanity_02 | LBNRIND submission values? | **PASS** (4 值 + Ext=Yes + [33_ct_general.md]) | `smoke_v4_answers/sanity_02_lbnrind_values.md` |
| sanity_03 | CMINDC 用于什么场景? | **PASS** (indication + CRF Other + SUPPCM 工作流 + 2 citation) | `smoke_v4_answers/sanity_03_cmindc_indication.md` |

若 3/3 PASS → 底座稳, 进 §2 Q1-Q14 + AHP.

---

## 2. Main 逐题结果 (Q1-Q14 + AHP1-3)

| 题号 | 类型 | 主题 | Citation 数 | Verdict | 答案文件 |
|---|---|---|---|---|---|
| Q1 | v3.4 新域 | GF EGFR 基因变异 | 16+ | **PASS** (域 + 6 Req + 4 Exp + abcd 全对 + GERMLINE VARIATION + SNV 建议) | `Q1_answer.md` |
| Q2 | v3.4 新域 | CP CD4+ 流式 | 多 | **PASS** | `Q2_answer.md` — 全 5 部分 + Ki67+ PROLIFERATING vs ACTIVATED 业界精度 note |
| Q3 | v3.4 新域 | BE+BS+RELSPEC 生物样本 | 多 | **PASS+** | 全 3 部分 + RELSPEC REFID/PARENT/LEVEL 完整机制 |
| Q4 | 域边界 | LB vs MB vs IS 三场景 | 多 | **PASS** | A=IS/B=IS/C=MB 全对 + Topic 变量 + 边界规则 |
| Q5 | 域边界 | FA vs QS vs CE 三场景 | 18+ | **PASS** | A=FA/B=QS/C=CE 全对 + Topic 变量 + [fa/qs/ce] source citations + SF-36 Codelist C177716 + QSTESTCD SF36101 细节 |
| Q6 | Timing | PK 定时采血 --TPT 四件套 | 6+ | **PASS** | `Q6_answer.md` — 5 vars + Role/Core/CT 完整表 + abcd 全对 + VISIT+PCTPTREF 组合 |
| Q7 | Partial date | EDC 只给部分日期 | 7+ | **PASS** | `Q7_answer.md` — 3 场景 + (d)(e) 正确 + **避开 --DTF 幻觉陷阱** + partial 不推 Study Day |
| Q8 | CT | Extensible vs Non-Ext (v4 修 LBNRIND/AETERM) | 9+ | **PASS+** | `Q8_answer.md` — (a)(b)(c)(d) 全对 + C66742 4 值全 + C66789 Not Done 独特 + **CDISC new-term request** 独到 insight |
| Q9 | Pinnacle 21 | 常见 FAIL 分类 (KB 外, 预期 PUNT) | 3+ | **FAIL (safety-correct PUNT)** | `Q9_answer.md` — 架构合规 PUNT, 补 SDTMIG §3.2.2 10 条 upstream; Phase 4 Scoping 决策稳定 vs smoke v3 |
| Q10 | SUPP 深化 | QORIG/QEVAL + SUPPTS 前提纠错 (v4 修) | - | pending | `Q10_answer.md` |
| Q11 | Dataset-JSON | v1.1 vs XPT v5 (v4 新开放) | - | pending | `Q11_answer.md` |
| Q12 | CT 版本锁定 | (v4 新开放) | - | pending | `Q12_answer.md` |
| Q13 | RWD | Observational 场景 SUPPDM (v4 删 NS 虚构 + 修 ARMCD) | - | pending | `Q13_answer.md` |
| Q14 | AE+CE+MH+DS | 同事件共记 + 死亡对齐 (v4 修 timing context) | - | pending | `Q14_answer.md` |
| AHP1 | Z1 变量虚构 | LBCLINSIG 不存在 | - | pending | `AHP1_answer.md` |
| AHP2 | Z2 跨域虚构 | Trial-Level SAE Aggregate 表不存在 | - | pending | `AHP2_answer.md` |
| AHP3 | Z3 deprecated | PF 域已被 GF 替代 | - | pending | `AHP3_answer.md` |

---

## 3. 总分 (R1 跑完填)

| 指标 | 值 |
|---|---|
| Main gate score (Q1-Q10 + AHP1-3) | X/13 |
| Q11-Q14 bonus score | X/4 |
| Total score | X/17 |
| 阈值 | ≥12/17 (71%) |
| **Verdict** | pending |

---

## 4. Carry-over 观察 (R1 跑完填)

- F-1-recurring 小表渲染漂移: ?
- F-3 citation dropout T2 偏向: ?
- Q10 v4 patch 对 SUPPTS 前提纠错能力: ?
- AHP1-3 in-KB-only 表现: ?
- Q9 Pinnacle 21 是否仍 PUNT (架构限制): ?
- Q11-Q13 supplemental topics (Dataset-JSON/CT 版本/RWD) 是否 PUNT: ?

---

## 5. 下游 gate (R1 跑完)

- Phase 4 跨 4 平台对比作 baseline
- R1→R2 决策 (按 SMOKE_V4.md §1 §5)
