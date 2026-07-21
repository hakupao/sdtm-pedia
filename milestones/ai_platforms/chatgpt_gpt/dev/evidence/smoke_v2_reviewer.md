# Phase 6.5 ChatGPT GPTs · Node 4 Smoke v2 — Reviewer Report

> **Reviewer**: oh-my-claudecode:tracer (Rule D 第 14 种 subagent_type, 独立链)
> **Method**: 只读, Evidence-driven tracing; 10 题逐题独立判定 (盲判, 后对比 scorer); KB 源核查
> **Date**: 2026-04-21
> **Scope**: ChatGPT smoke v2 10 题 (9/10 PASS scorer) + 5 batch 2 uploads 合规性 + Phase 4 gate 决策

## Review Verdict
**ADJUST (partial)** — confidence 82%

**Phase 4 gate 决定 = CONFIRM** (9 PASS + 1 FAIL 过 ≥8/10 阈值, 进 Phase 4 合规).
**Evidence 卫生 + Q3 remediation 方向 = ADJUST** (scorer Q3 FAIL 理由注入了 critical factual error, 会毒化 Phase 4 remediation).

## Independent Scoring Matrix (盲判, KB-grounded)

| Q | Topic | Scorer | 独立 | 一致? | 判据命中 | FAIL 命中? | 说明 |
|---|---|:-:|:-:|:-:|:-:|:-:|---|
| Q1 | CM 2 条 + Core=Req | PASS | PASS | ✅ | 7/7 | N | 5 个 Req 全对 (比 SMOKE 判据更严格) |
| Q2 | AE SAE 7 子 Y/N | PASS | PASS | ✅ | 8/8 | N | AE spec L248/338-398 全对应 |
| Q3 | LB HbA1c + LBNRIND | FAIL | FAIL | ✅ | 7/8 | **Y** | **verdict 对, 但 scorer 的 SDTM 事实理由硬错** (见 HIGH H1) |
| Q4 | AESEV + CTCAE + Grade 5 | PASS | PASS | ✅ | 5/5 | N | MILD/MODERATE/SEVERE + Grade 5→FATAL, `ae.md` L36/43-51 佐证 |
| Q5 | PC LLOQ ≠ 0 | PASS | PASS | ✅ | 5/5 | N | 典范 PASS |
| Q6 | ARMCD/ARM + 换组 | PASS | PASS | ✅ | 8/8 | N | **显式提 ACTARMCD/ACTARM** (跨平台差异点, Gemini 漏) |
| Q7 | MH+CM + ONGOING | PASS | PASS (borderline) | ✅ | 8/10 | N | **CMINDC 变量名未显式命名** (scorer L53 承认小扣分) |
| Q8 | ISO 8601 + AESTDY Day 1 | PASS | PASS | ✅ | 6/6 | N | 教科书级 PASS |
| Q9 | SUPPAE + QNAM 8 字符 | PASS | PASS | ✅ | 7/7 | N | AESOSP 6 字符合规 + 非标定义准确 |
| Q10 | RELREC vs SUPP | PASS | PASS | ✅ | 7/7 | N | RELREC 7 字段全对 vs `model/06_relationship_datasets.md` L32-40 |

**独立总分**: 严格 9/10 PASS (与 scorer 一致), 或 Q7 严判 PARTIAL 则 8.5/10. 两档均过阈.

## Findings

### HIGH — 影响 Phase 4 remediation (必读)

**H1. Scorer 对 LBNRIND codelist C78736 的事实断言本身错**

- Scorer L89: "C78736 明确是 H/N/L 单字符短码, 非 HIGH/LOW/NORMAL 全写"
- **KB 源 (唯一真源)** `knowledge_base/terminology/core/general_part4.md` L63-72:
  - `C78802 → ABNORMAL`
  - `C78800 → HIGH`
  - `C78801 → LOW`
  - `C78727 → NORMAL`
- KB `LB/spec.md` L264 CDISC Notes Examples 亦明文 "NORMAL, ABNORMAL, HIGH, LOW" (全写)

**意味着**:
1. CDISC C78736 官方 Submission Value 是 **HIGH/LOW/NORMAL 全写**, 没有 "H/N/L" 单字符
2. ChatGPT 答 "HIGH/LOW/NORMAL" 实际上**符合 KB 源 + CDISC 官方** codelist
3. SMOKE_QUESTIONS_V2.md Q3 PASS 判据 (L73 "LBNRIND = H") + FAIL 判据 (L76 "写 HIGH/LOW 而非 H/L") **本身和 KB 冲突**
4. Q3 FAIL verdict 在"按判据当时样子评分刚性"层面仍成立; 但 **Phase 4 remediation 不能按 scorer 建议 "在 02/03 补 H/N/L 硬规则"** — 那会把和 KB 矛盾的错知识注入 system_prompt

**Phase 4 remediation 方向翻转**: 不补 H/N/L 规则, 而是**先校准 SMOKE_QUESTIONS_V2.md Q3 判据** (放宽接受 "HIGH/LOW/NORMAL" 为 PASS), 再决定是否 system_prompt 补什么.

### HIGH — 题目设计缺陷

**H2. SMOKE_QUESTIONS_V2.md Q3 判据与自家 KB 源冲突**

L73 / L76 写的 "H/L/N" 短码在 KB 三处 (general_part4.md / LB/spec.md / model/02_observation_classes.md) 全无支撑. 题目设计阶段用了实验室 CRF 惯用写法, 未对齐 CDISC CT 官方 submission values. Gemini 按 CO-2 拒答反而误打误撞回避了这个坑.

### MEDIUM

**M1. Q7 CMINDC 变量名缺失** — PASS 判据明文 "CMINDC (指征=高血压)", 答案仅隐含未显式命名. scorer L53 承认但未扣分. 严判可 PARTIAL (0.5), 对总分无影响.

**M2. Q4 "AESEV vs AESER 区分" 未显式对比** — PASS 判据 L92 "说明 AESEV 不等于 Serious (AESER)", 答案 Q4_answer.md L11 隐含未显式对比. scorer 承认. borderline PASS.

### LOW

- **L1. Q1 CMDECOD 是否 Core=Req** — 答案自认未查 CM spec 原文, 认识论谦虚可嘉, 评分未受影响.
- **L2. Q9 "AESOSP" 非标性独立核查** — 不在 AE 标准变量表 L248-398, 合"非标"定义, 无臆造.
- **L3. Q8 AESTDY 规则** — 与 Gemini 同日独立答案交叉 PASS, 证据强.

## SDTM 事实抽检 (KB 源 vs 答案)

| # | 事实 | ChatGPT 答 | KB 源 | 一致? |
|---|---|---|---|:-:|
| 1 | CM Core=Req 变量集 | STUDYID/DOMAIN/USUBJID/CMSEQ/CMTRT | CM spec L11/20/29/38/65 | ✅ |
| 2 | AESER Core | 隐含 Y=Exp | AE spec L254 Core: Exp | ✅ |
| 3 | 6 SAE 子 Core | 隐含 Perm | AE spec L344/353/362/371/380/398 | ✅ |
| 4 | AESEV codelist | C66769 | `terminology/core/ae.md` L43 | ✅ |
| 5 | FATAL = Grade 5 | AEOUT=FATAL | `terminology/core/ae.md` L36 C48275 | ✅ |
| 6 | LBNRIND codelist | C78736 | LB spec L261 + `general_part4.md` L63 | ✅ |
| 7 | **LBNRIND CT 值** | **HIGH/LOW/NORMAL** | **general_part4.md L69-72: HIGH/LOW/NORMAL/ABNORMAL** | **✅ (真实数据) / ❌ (按错判据)** |
| 8 | RELREC 7 字段 | 全列 | `model/06_relationship_datasets.md` L32-40 | ✅ |

**关键**: 事实 #7 是 scorer L89 断言 "C78736 是 H/N/L" 的事实层颠覆 — ChatGPT 按 KB 源答"HIGH/LOW/NORMAL"是**正确的**.

## Q3 FAIL vs PARTIAL 独立裁决

**意见**: **FAIL (严格判)**, 不改 PARTIAL.

**理由**:
1. 题目 FAIL 判据 L76 明文 "写 HIGH/LOW 而非 H/L = FAIL", 按 L212 "FAIL 判据命中 = FAIL" OR 逻辑硬命中
2. Scorer 自己 Q3_answer.md L56 提了备选 PARTIAL 但最终选 FAIL, 判定公允
3. 翻 PARTIAL 会开口子, 破坏评分刚性

**但**: Q3 remediation 方向**必须翻转** (见 H1) — 不补 H/N/L 硬规则, 先校准 SMOKE 判据或 KB 源一致性.

## Convergence / Separation Notes

- **Q3 两平台同 FAIL 但失败模式结构性不同** — ChatGPT 答 HIGH (按 KB 正确), Gemini CO-2 拒答. 非同根因收敛.
- **Q6 ACTARM 两平台分离** — ChatGPT 正确识别 SDTM DM 域 ACTARM/ACTARMCD, Gemini 错层到 ADaM. 证明 ChatGPT batch 2 含 terminology + spec 全量的**架构优势**.
- **其他 8 题双平台双 PASS 收敛** — 独立证据强 (双平台独立答案一致 ≠ 巧合).

## Rule D / Rule E 合规

- **Rule D**: 第 14 种 subagent_type (tracer) 独立于 scorer + writer. 只读未改. ✅
- **Rule E Q1=C 陌生公开受众**: ChatGPT 答题多次展示 "未拿到原文逐项核对" / "检索没直接返回" 的谦虚表达 (Q1 L52 / Q3 L32 / Q5 L33) — 合 Rule E 精神.
- **Rule E Q2 (reviewer 独立于 writer)**: 盲判后对比, 合规.
- **Rule B (失败归档)**: 第一轮 type 丢字失败 + JS paste 恢复全记录 smoke_v2_results.md L13-34, 归档合规.

## 对 Phase 4 的 Actionable Recommendations

1. **[HIGH 必修]** 先核实 C78736 submission value 真相 (跑 `Grep -n "C78736" knowledge_base/terminology/` + 查 NCI EVS C78736 当前页面) → 若 KB 源和 CDISC 官方均为 HIGH/LOW/NORMAL, **翻转 SMOKE_QUESTIONS_V2.md Q3 L73/L76 判据**, 接受长写为 PASS.
2. **[HIGH 必修]** Phase 4 A/B 回归 Q3 之前, **绝不要**按 scorer L104-106 补 "LBNRIND=H/N/L" 硬规则 — 会注入和 KB 矛盾的错知识.
3. **[MEDIUM]** Q7 CMINDC 严苛化: 把"答题必显式命名 PASS 判据要求的变量名"写进 Phase 4 regression 标准.
4. **[MEDIUM]** 跨平台 Q6 ACTARM 差异归档到 SYNC_BOARD 作为 "ChatGPT batch 2 terminology 覆盖优于 Gemini C refactor" 的证据, 回流 `_template/`.
5. **[LOW]** Q3 可选路径: ChatGPT 也走 Gemini 式 CO-2 "对硬 CT codelist 值指向 NCI EVS" — 若愿意放弃部分 inline term recall 换可靠性.

## Uncertainty Notes

- **C78736 submission value 真相未跨源独立核实** — 仅 KB `general_part4.md` + `LB/spec.md` 两源 (都是同一 KB, 抽取自 CDISC xlsx). 建议 Phase 4 前查 NCI EVS 官方页面交叉确认.
- **Rule E Q1=C 在 system_prompt 中的强度** — 未直接测试源码, 仅从答题表现推断.

## 结论

**Phase 4 gate = CONFIRM** (≥8/10 过阈, 三方独立证据: scorer + tracer + Gemini 同日跑).

**ADJUST 三处**:
- **Q3 remediation 方向翻转** — 不补 H/N/L 硬规则, 先校准 SMOKE 判据或 KB 源一致性 (HIGH)
- **Q7 严判可 borderline PARTIAL** (MEDIUM, 对总分无影响)
- **跨平台 Q6 ACTARM 归档为 ChatGPT 架构优势证据** (MEDIUM)

**Critical Unknown**: C78736 当前 CDISC 官方 submission values 是 HIGH/LOW/NORMAL 还是 H/N/L (KB 源指前者, scorer 断言后者, 两者冲突 — Phase 4 前必解).

**Discriminating Probe**: 15 分钟内可收敛 (Grep KB + 查 NCI EVS), 决定 SMOKE Q3 判据是否翻转.
