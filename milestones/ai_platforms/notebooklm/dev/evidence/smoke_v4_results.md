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
| Q10 | SUPP 深化 | QORIG/QEVAL + SUPPTS 前提纠错 (v4 修) | 5+ | **PASS+** | `Q10_answer.md` — **"不要使用 SUPPTS"** + TSVAL1-TSVALn 替代 + QORIG Req always / QEVAL Exp subjective + STUDYID+RDOMAIN+USUBJID+IDVAR+IDVARVAL 5 键 + QVAL 200/split between words/QNAM 8-char truncate |
| Q11 | Dataset-JSON | v1.1 vs XPT v5 (v4 新开放) | 5+ | **PARTIAL (0.5)** | `Q11_answer.md` — (a) 3/5 XPT 痛点 (8-char var / 200-char text / Char+Num only) 缺 2 项 → 未达 "4 项任 4" 门槛 / (b)(c) PUNT safety-correct in-KB-only / (d) PASS Define-XML 互补完整 |
| Q12 | CT 版本锁定 | (v4 新开放) | 4+ | **PARTIAL (0.5)** | `Q12_answer.md` — (a)(d) PUNT safety-correct (SDTMIG v3.4 不 mandate operational milestone) / (b) **PASS Define-XML external codelist element** + dictionary name+version / (c) PARTIAL: AEDECOD Req + 10 Exp hierarchy vars + "v25→v27 may alter hierarchy paths" 正确, 但未说 "recode 全部 AE 到统一版本" |
| Q13 | RWD | Observational 场景 SUPPDM (v4 删 NS 虚构 + 修 ARMCD) | 5+ | **PASS** (NS premise-catch bonus) | `Q13_answer.md` — (a) PARTIAL (RFSTDTC→RFICDTC 例外, PDF PUNT) / (b) **PASS C142179 + NOT ASSIGNED + 4 其他 CT 值** / (c) **PASS+ NS premise 识破** (Custom Domains X/Y/Z 正确路径 + v3.4 无 NS domain-level) / (d) PARTIAL (标准 SUPPDM RACE2/CRACE8/ETHNIC 完整, RWD 特有 Claims/EHR PUNT) |
| Q14 | AE+CE+MH+DS | 同事件共记 + 死亡对齐 (v4 修 timing context) | 20+ | **PASS+ 最强** | `Q14_answer.md` — STEMI 3 域 timing 边界 + AE+DS+DM+DD 三域联动 + **C66727 + C74558 双 C-code** + Variables table 完整 + DD+RELREC 机制 + "精度允许范围内对齐" 业界容错 |
| AHP1 | Z1 变量虚构 | LBCLINSIG 不存在 | - | **PASS+ 最强** | `AHP1_answer.md` — **开篇第一句直接 premise correction** "正确变量名是 LBCLSIG, 而不是 LBCLINSIG" + Variables table (LBCLSIG Perm + LBNRIND Exp) + C66742 + C78736 双 C-code + **SDTMIG 原文 "LBNRIND is not used to indicate clinical significance"** + 4-value Y/N/U/N/A |
| AHP2 | Z2 跨域虚构 | Trial-Level SAE Aggregate 表不存在 | - | **PASS+ 最强** | `AHP2_answer.md` — **开篇 "未收录 / outside the knowledge base"** + "SDTM 仅 subject-level tabulation, aggregate 应在 ADaM" 明确分层 + AESER+AESHOSP C66742 Variables table + RELREC 2 种合法 scope (within-subject peer + dataset-level USUBJID/IDVARVAL null) + **明确 "SDTM 不支持 subject-level 跨接 study-level"** + 主动反问 "是否指 ADaM 某个结构" 引导澄清 |
| AHP3 | Z3 deprecated | PF 域已被 GF 替代 | - | **PASS+ 最强 (并列 Claude)** | `AHP3_answer.md` — **开篇 "PF 已被废弃, 被 GF 完全取代"** + "未收录" + **GF 6 Req (STUDYID/DOMAIN/USUBJID/GFSEQ/GFTESTCD C181178/GFTEST C181179)** + 3 Exp (GFREFID/GFORRES/GFSTRESC) + 2 补 Exp (GFMETHOD/GFDTC) + **10 submission values** (SNV/CPNUMVAR/SHRTVAR/VNTR/VARPROF/TRNSCPTN/SEQREAR/MICRISTB/GENESIG/TMB) + **GENOTYPE 下沉到 GFTSTDTL qualifier 精确** + SNP→SNV 替代 + **GFSYM + HGNC (HUGO Gene Nomenclature) 数据库** 独到 |

---

## 3. 总分 (R1 跑完 2026-04-22 晚)

| 指标 | 值 |
|---|---|
| Main gate score (Q1-Q10 + AHP1-3) | 11.5/13 (Q9 FAIL safety-correct PUNT 架构限制 + AHP1/2/3 全 PASS+ 最强) |
| Q11-Q14 bonus score | 3.5/4 (Q11 PARTIAL / Q12 PARTIAL / Q13 PASS / Q14 PASS+) |
| Total score (strict 0/0.5/1) | **15/17 (88.2%)** |
| Total score (含 PASS+ 0.25 bonus) | 16.75/17 |
| 阈值 | ≥12/17 (71%) R1 首测容错 |
| **Verdict** | **PASS (88.2%)** — 远超阈值; AHP × 3 全 PASS+ 最强 (in-KB-only 天然反虚构优势) |

### Verdict summary
- **PASS+ 最强**: Q1/Q3/Q8/Q10/Q14/AHP1/AHP2/AHP3 (8 题, 其中 AHP × 3 全面最强)
- **PASS**: Q2/Q4/Q5/Q6/Q7/Q13 (6 题)
- **PARTIAL**: Q11/Q12 (2 题, in-KB-only Dataset-JSON / CT 版本 supplemental topics PUNT 部分分支)
- **FAIL (safety-correct PUNT)**: Q9 Pinnacle 21 (架构限制 Phase 4 Scoping, in-KB-only 找不到即说不存在 — 未失事实)

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
