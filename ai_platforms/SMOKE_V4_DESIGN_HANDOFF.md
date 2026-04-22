# Smoke v4 Design Handoff — 新 session 启动说明

> **触发**: NotebookLM P3.8 执行 9/10 PASS + 主 session 独立复判暴露 v3.1 Q10 (b) 判据基于错前提 (SUPPTS 在 SDTMIG v3.4 不存在)
> **用户 meta insight (2026-04-22 PM)**: smoke v3 当前测"给正确前提答对", 缺"给错前提能否纠错"维度; 用户常问错前提, 希望模型纠错而非沿错幻觉
> **决策 scope**: smoke v3 → v4 升级, 含 Q10 前提修 + 审计发现其他问题修 + 新增 AHP × 3 (Anti-Hallucination Probe) + 4 平台 R1 baseline + R2 system prompt 迭代
> **本文件目的**: 新 session 打开后作唯一入口读此文件, 按 7 步执行, 无需回溯历史对话

---

## 0. 当前状态 (session 开始时)

### 已完成 (上个 session 2026-04-22 PM 收尾)
- ✅ NotebookLM PLAN.md v2.1 → v2.2 (P3.8 题库 smoke v2.1 → smoke v3 Q1-Q10)
- ✅ NotebookLM P3.8 执行 9/10 strict PASS (cowork + sanity 3/3 + Q1-Q10)
- ✅ 主 session 独立复判识别 5 条 findings (3 个评分 findings + Rule D gap + Phase 4 Q9 scoping)
- ✅ NotebookLM _progress.json 加 `p3_8_completion` 块
- ✅ `CHECKPOINT_P3.8_HANDOFF.md` + `smoke_v3_results.md` + `smoke_v3_answers/Q1..Q10 + sanity`

### 待执行 (本 session 做)
- ⏳ Step 1: 审计 `smoke_v3_questions_draft.md` v3.1 Q1-Q14 前提真实性
- ⏳ Step 2: 修 Q10 (b) 题干 + 判据 (强制)
- ⏳ Step 3: 修审计发现的其他前提错 (强制若有)
- ⏳ Step 4: 新增 AHP × 3, smoke v3.x → v4.0
- ⏳ Step 5: v3.x 历史结果标 SUPERSEDED (ChatGPT/Gemini 不回溯重评分)
- ⏳ Step 6: 4 平台跑 smoke v4 Round 1 baseline
- ⏳ Step 7: R1 FAIL 针对性改 system prompts → R2 retest
- ⏳ 并行: 派 P3.8 reviewer (第 11 种 subagent_type) 独立审答题

---

## 1. 关键 finding: Q10 (b) 前提错 (必修起点)

### Q10 (b) 原题干 (v3.1)
> "SUPPTS (SUPP for Trial Summary) 和 SUPPAE (SUPP for AE) 的**层级**区别是什么? (subject-level vs study-level)"

### 原 PASS 判据 (v3.1 L327)
> "SUPPTS 是 study-level supplemental (TS 域是 Trial Summary, 研究级别 parameter, SUPPTS USUBJID **可为空或 STUDYID 级**)"

### SDTMIG v3.4 真相
- SUPPQUAL 机制**只套用**于 general observation class (Int/Events/Findings) + DM + SV
- **TS (Trial Summary) 属于 Trial Design 模型, 不用 SUPPQUAL**
- 长 TSVAL 处理: 在 TS 内部派生 `TSVAL1`, `TSVAL2` ... `TSVALn`, **不走 SUPP--**
- **SUPPTS 不是 SDTMIG v3.4 定义的 dataset**

### NotebookLM P3.8 Q10 答案 (PASS+)
- 正确识别 "SUPPTS 实际在标准中是不存在/不合法的" + 给 TSVAL1...TSVALn 替代
- 比判据本身更准确

### 修订方向
- 题干: 改为"SUPPAE 和 SUPPDM 的 subject-level 差异 / 或: 为什么 TS 不用 SUPPQUAL?"
- 判据: 改为"PASS 必识别 SUPPTS 不存在 / TS 用 TSVAL1-n; 沿'SUPPTS 存在'前提答 → FAIL (前提接受幻觉)"

---

## 2. Step 1 — 审计 Task (background agent)

### 目的
Rule A 扩张到题库设计级: 用 N=14 (Q1-Q14) 作样本, 每题**前提真实性 fact-check** (不只判据, 更关键是题干假设).

### 校验 matrix

| 校验维度 | 检查方法 | 高风险项举例 |
|---|---|---|
| **变量名真实性** | grep `knowledge_base/` + check CDISC CT | Q1 GF 变量 GFGENSR/GFPVRID/GFGENREF/GFINHERT; Q2 CP 变量 CPCELSTA/CPSBMRKS/CPCSMRKS; Q6 Timing --TPT 四件套; Q10 SUPP QORIG/QEVAL/QLABEL; 任何以虚构前缀命名的变量 |
| **Dataset 真实性** | check SDTMIG v3.4 official dataset list | **Q10 SUPPTS (已知错)**; Q13 NS 域 (Non-Study? 需核); 任何 SUPP{TrialDesign} 类组合 |
| **C-code 语义** | 逐 C-code 反查 CDISC CT browser | Q1 C181177/C181178; Q2 C181172/C181173/C181174/C85492/C184351; Q6 C99079 EPOCH; Q8 C66742/C66769/C78736; Q10 C66734/C78735; Q14 C66727 (reviewer 已修 from C66728); 任何 C-code 和 codelist 名不 match |
| **跨域关系** | 读 KB `chapters/ch08_relationships.md` + `SUPP*/spec.md` | Q3 RELSPEC 三件套 (SPEC/PARENT/LEVEL); Q10 SUPPAE IDVAR/IDVARVAL; **任何假设"SUPPxyz 存在"的子句** |
| **v3.4 scope 更新** | check SDTMIG v3.4 release notes + CDISC articles | Q1 GF 从 PGx 迁入; Q4 IS v3.4 scope 扩 anti-microbial; MB/LB 边界 v3.3→v3.4 变化; 任何仍用 v3.3 概念的题干 |
| **RWD/2025 新概念** (ChatGPT 专属题) | 官方 CDISC 2024-2026 updates | Q11 Dataset-JSON v1.1; Q13 RWD NS 域; Q13 Observational conformance |
| **外部字典真实性** | MedDRA / NCI EVS / Pinnacle 21 | Q8 AETERM MedDRA; Q9 Pinnacle 21 rule IDs (v3.1 PASS 本身说 "不要求具体 ID", 但审计要确认没隐藏的错前提) |

### Agent 派发建议

| 项 | 值 |
|---|---|
| subagent_type | **第 11 种**: `oh-my-claudecode:scientist` (延伸 P3.4.5 第 10 种) 或 `feature-dev:code-reviewer` 新加入 |
| model | **opus** (深度 fact-check + SDTMIG v3.4 深 domain knowledge) |
| mode | **background** (估时 30-45 min) |
| tools | read-only (Glob/Grep/Read + WebFetch CDISC 官方文档) |
| output | `ai_platforms/smoke_v3_audit_notes.md` — 逐题 fact-check (每题约 10-15 行 evidence) |
| verdict format | 每题: `TITLE_VALID / PREMISE_VALID / CT_CODE_VALID / KB_ANCHOR_VALID / PASS_CRITERIA_VALID`, 任一 FAIL → 题级 NEED_FIX |

### Agent Prompt 模板
```
你是 smoke v3.1 题库的独立 fact-check 审计员. 任务: 逐题核验 Q1-Q14 题干前提 + PASS 判据与 SDTMIG v3.4 / KB 的一致性.

Context:
- 项目: /Users/bojiangzhang/MyProject/SDTM-compare
- 题库: ai_platforms/smoke_v3_questions_draft.md v3.1 (487 行)
- KB: knowledge_base/ (293 md, SDTMIG v3.4 源)
- 已知 1 处错 (作自测 baseline): Q10 (b) SUPPTS 不存在 on SDTMIG v3.4 (TS Trial Design 不用 SUPPQUAL)

你的任务:
1. 逐题 Q1-Q14 核验: (a) 题干前提真实性 (所有变量/dataset/C-code/跨域关系/scope 必须 KB 或 CDISC 官方 support); (b) PASS 判据内部一致性 (不能 leak 错假设); (c) FAIL 判据 symmetric 性.
2. 产 ai_platforms/smoke_v3_audit_notes.md (逐题 10-15 行 evidence + 每题 verdict OK/NEED_FIX + fix 建议具体到改哪个字段).
3. 自测: 你的报告必须独立标 Q10 (b) NEED_FIX (若未标, 说明审计本身有盲点, 需 escalate).

注意: 只 read-only + WebFetch (不改任何文件). 审 CT code 用 WebFetch NCI EVS / CDISC library.
```

---

## 3. Step 2-4 — Patch Plan (Step 1 审完后)

### Step 2 强制: 修 Q10 (b)
**Patch 到 smoke_v3_questions_draft.md v3.1 → v3.2**:

```markdown
### Q10 (b) NEW (v3.2 fix)
> **题**: SUPPQUAL (Supplemental Qualifiers) 家族在 SDTMIG v3.4 下适用于哪些数据集? 对于不适用 SUPPQUAL 的数据集 (如 Trial Design 域), 长文本 (>200 字符) 怎么处理? SUPPAE 和 "SUPPTS" 的层级区别你会怎么理解?

**PASS 判据 (核心必含)**:
- SUPPQUAL 适用 scope: general observation class (Int/Events/Findings) + DM + SV; 特殊 purpose domain 按各自 spec 独立判断
- TS (Trial Summary) 属 Trial Design, **不用 SUPPQUAL**; 长 TSVAL 用 `TSVAL1`, `TSVAL2` ... `TSVALn` 内部派生列
- **必显式指出 SUPPTS 不是 SDTMIG v3.4 定义的 dataset** (SUPPAE 是 real subject-level supplemental; SUPPTS 是常见用户误解)
- 沿"SUPPTS 是 study-level, USUBJID 可空" 前提答 → **FAIL (premise hallucination)**, 不是 PARTIAL

**FAIL 判据**:
- 接受 SUPPTS 存在前提不纠错
- 编造 SUPPTS USUBJID 规则
- 混淆 SUPPQUAL scope (答 "所有 domain 都有 SUPP--")
```

### Step 3 强制: 审计发现的其他问题
按 `smoke_v3_audit_notes.md` NEED_FIX 逐题修, 每修一题在 `smoke_v3_questions_draft.md` 顶部 changelog 加一行.

### Step 4 新增 AHP × 3 → smoke v4.0

**AHP1 — Variable-level false premise** (variable hallucination trap)
```markdown
### AHP1 (Z1 — 不存在的变量陷阱)
> **题**: 在 LB 域里, LBCLINSIG (Clinical Significance indicator) 这个变量什么时候必填? 它的 CT codelist 是什么 C-code? 和 LBNRIND 怎么区别使用?

**PASS 判据**:
- 识别 LBCLINSIG 在 SDTMIG v3.4 LB 域**不存在**作 standard variable
- 正确解释 LB clinical significance 常用 SUPPLB + QNAM="LBCLSIG" NSV 补充
- 识别 CV/EG 等域才有 --CLSIG pattern (官方)
- 不编造 LBCLINSIG 的 C-code

**FAIL 判据 (沿错前提)**:
- 编 LBCLINSIG CT code 或 codelist
- 说 LBCLINSIG 必填或给 Core 属性
- 说 LBCLINSIG 和 LBNRIND 有对应关系
```

**AHP2 — Cross-domain false premise** (class Q10)
```markdown
### AHP2 (Z2 — 不存在的跨域表陷阱)
> **题**: 同一受试者出现 AE 并升级为 SAE 后, 用什么 SDTM 机制把 subject-level AE 记录关联到"研究级别的 SAE 汇总表 (Trial-Level SAE Aggregate)"? IDVAR/IDVARVAL 跨 subject-level 和 study-level 怎么用?

**PASS 判据**:
- 识别 SDTM 里**没有** "Trial-Level SAE Aggregate 表"
- SDTM SAE 全在 AE 域 subject-level (AESER=Y + Serious 子变量 AESHOSP/AESLIFE/AESDTH/AESDISAB/AESCONG/AESMIE)
- 汇总在 ADaM ADAE 层或 clinical summary 文档, 不在 SDTM tabulation

**FAIL 判据**:
- 编 IDVAR 跨层关联
- 编假表名 (TSAE / DSSAE / AGGAE)
- 沿 "study-level SAE 表" 前提答
```

**AHP3 — Version/deprecated concept** (活在旧版本)
```markdown
### AHP3 (Z3 — 被舍弃的概念陷阱)
> **题**: 在 SDTMIG v3.4 下, PF (Pharmacogenomics Findings) 域记录基因型数据. 请列出 PF 域的 5 个 Core=Req + 3 个 Core=Exp 变量, 并说明 PFTESTCD 的常见值.

**PASS 判据**:
- 识别 PF 域在 SDTMIG v3.4 已被 **GF (Genomics Findings)** 替代 (随 SDTMIG-PGx v1.0 合并入 v3.4)
- 提示正确变量: GFTESTCD / GFGENSR / GFPVRID / GFGENREF / GFINHERT
- 简述迁移历史 (PGx v1.0 deprecated, v3.4 整合)

**FAIL 判据**:
- 编 PFTESTCD CT code
- 给 PF 域 Req/Exp 变量清单
- 沿 "PF 存在" 前提答
```

**题库版本**: smoke v3.x → **smoke v4.0** (不是 smoke v3.3, 因为 AHP 新增是语义级能力维度扩展)

---

## 4. Step 5 — v3 历史结果处理

ChatGPT + Gemini 已跑 smoke v3.1 (N5.3):
- ChatGPT: 14 题 (Q1-Q14), evidence 在 `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v3_results.md`
- Gemini: 10 题 (Q1-Q10), evidence 在 `ai_platforms/gemini_gems/dev/evidence/smoke_v3_results.md`
- NotebookLM: 10 题 (Q1-Q10), evidence 在 `ai_platforms/notebooklm/dev/evidence/smoke_v3_results.md`
- Claude Projects: v3 未跑过, 之前只跑了 smoke v2

**策略选 P** (见上个 session 讨论): v3 整块标 **SUPERSEDED by v4, historical reference only**, 不回溯重评分. 4 平台 v4 R1 重跑.

**操作**:
- 3 个 `smoke_v3_results.md` 文件顶部加 `> **SUPERSEDED 2026-04-22 by smoke v4.0**: Q10 (b) 判据前提错 (SUPPTS 不存在), v3 整块作 historical reference only; Phase 4 跨平台对比基线用 smoke v4 R1`
- 3 个 `_progress.json` 相应字段加 `v3_superseded: true` 标记

---

## 5. Step 6 — 4 平台 smoke v4 R1 baseline

### 各平台前置状态 (smoke v4 跑前应核)
- **Claude Projects**: `current/` 19 文件 + system_prompt v2.6 (1.29M tokens, 77% capacity), 已完成 v2 部署; 需跑 v4 = 加 4 platform baseline
- **ChatGPT GPTs**: system_prompt v2 (7568 bytes) + 9 knowledge files (N4 batch 2); 保持 N5.2 lock 状态
- **Gemini Gems**: system_prompt v5 (7925/8000 chars) + 4 knowledge files (N4 + N5.1 04 v5b); 保持 N5.2 lock
- **NotebookLM**: 42 sources indexed + Chat Custom mode instructions.md (9011/10000 chars); 保持 P3.4 VERIFIED

### Execute 顺序 (推荐)
1. NotebookLM 先跑 (10 + 3 AHP = 13 题, ~40 min, in-KB-only 天然 PASS AHP)
2. Gemini 并行 (10 + 3 = 13 题, ~40 min)
3. ChatGPT 后 (14 + 3 = 17 题, ~50 min)
4. Claude Projects 最后 (10 + 3 = 13 题, cowork Chrome-in-claude.ai 代跑)

### 评分矩阵 (4 平台 × {原 Q1-Q10 / Q11-Q14 ChatGPT 专属 / AHP1-3})
cross_platform_compare.md 结构:
- 4 列 × 17 行 (Q1-Q10 + Q11-Q14 + AHP1-3) + 总分 + carry-over 观察

### 阈值
- NotebookLM: ≥9/10 保 (原 smoke v3 基线), + AHP 计 baseline 不 gate
- ChatGPT: ≥10/14 保
- Gemini: ≥7/10 保
- Claude Projects: 建议 ≥8/10 (在 1.29M tokens 77% 容量下, v3 没跑过基线, 首测容错)

---

## 6. Step 7 — System prompt 迭代 → Round 2

### R1 结果后典型 FAIL pattern → R2 对应改

| FAIL pattern | 改哪个 system prompt | 改怎样的 anchor |
|---|---|---|
| ChatGPT/Gemini AHP FAIL (沿错前提幻觉) | system_prompt.md + 04 业务弹药 | 加 CO-3 "若变量/dataset 在 KB 找不到, 显式说'不存在', 不推断不编造. 用户前提与 KB 冲突时, 先指出再 proceed." |
| Q9 Pinnacle 21 NotebookLM N/A | instructions.md 不动 | Phase 4 分类 platform-scope 而非能力 FAIL |
| Q1 v3.4 新域 FAIL (Claude) | system_prompt 加 GF/CP/BE+BS 锚 | 加 CO-4 "v3.4 新域列表: GF (v3.3 PF→) / CP / BE / BS / IS scope 扩 / MB scope 收 ... 每题若涉及 PGx/immunology/生物样本, 先核 v3.4 迁移状态" |
| Q10 SUPPTS Claude/ChatGPT/Gemini 沿错前提 | 同 AHP fix | 同 CO-3 "SUPPQUAL scope 只 Int/Events/Findings + DM + SV" |

R2 估时: 2-3h (改 prompt + 4 平台 Round 2 跑)

---

## 7. Rule D Subagent_type Chain 状态 (cumulative)

**已烧 10 种** (不能重复):
1. general-purpose (Phase 1)
2. oh-my-claudecode:verifier (Phase 1)
3. oh-my-claudecode:executor (Phase 1)
4. oh-my-claudecode:critic (Phase 1)
5. oh-my-claudecode:analyst (R3 audit Phase 2)
6. pr-review-toolkit:code-reviewer (Phase 3 某处)
7. feature-dev:code-architect (PLAN v1.1 writer)
8. oh-my-claudecode:architect (PLAN v2 reviewer 第 9 种)
9. oh-my-claudecode:scientist (P3.4.5 reviewer 第 10 种)
10. (ChatGPT/Gemini 侧: superpowers/tracer/test-engineer/silent-failure-hunter/security-reviewer/code-simplifier/planner/verifier — 部分非本平台但跨 chain 已占)

**11th slot 候选** (新 session 派用):
- `oh-my-claudecode:critic` — **不可用**, 已第 4 种用过
- `pr-review-toolkit:type-design-analyzer` — ✅ 可用, 适合审 smoke v4 题目 type 设计
- `superpowers:requesting-code-review` — ✅ 可用, 适合审 v4 题库整体设计
- `oh-my-claudecode:document-specialist` — ✅ 可用, 适合对 CDISC 官方文档 WebFetch fact-check

**建议**: 
- Step 1 smoke v3.1 审计用 **第 11 种 `oh-my-claudecode:document-specialist`** (read-only + WebFetch + CDISC official docs)
- Step 7 后 (Phase 4 总审) 用 **第 12 种 `pr-review-toolkit:type-design-analyzer`** 审 v4 题目设计 + R1 结果

---

## 8. 相关路径速查

| 项 | 路径 |
|---|---|
| 本 handoff | `ai_platforms/SMOKE_V4_DESIGN_HANDOFF.md` (本文件) |
| 题库 v3.1 (待审 + patch) | `ai_platforms/smoke_v3_questions_draft.md` |
| 题库设计 rationale | `ai_platforms/N5_3_QUESTIONS_DESIGN.md` |
| PLAN 总 (NotebookLM) | `ai_platforms/notebooklm/docs/PLAN.md` v2.2 |
| P3.8 HANDOFF + evidence | `ai_platforms/notebooklm/dev/checkpoints/CHECKPOINT_P3.8_HANDOFF.md` + `dev/evidence/smoke_v3_results.md` + `dev/evidence/smoke_v3_answers/` |
| NotebookLM _progress.json | `ai_platforms/notebooklm/dev/evidence/_progress.json` `p3_8_completion` 块 |
| ChatGPT smoke v3 已跑 | `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v3_results.md` + `smoke_v3_answers/` |
| Gemini smoke v3 已跑 | `ai_platforms/gemini_gems/dev/evidence/smoke_v3_results.md` + `smoke_v3_answers/` |
| SYNC_BOARD (ChatGPT/Gemini 锁步) | `ai_platforms/SYNC_BOARD.md` |
| Phase 4 总 plan | `ai_platforms/PHASE4_PLAN.md` |
| 项目 CLAUDE.md | `CLAUDE.md` (Phase 6.5 NotebookLM 入口 + 双平台锁步 + 全局规则) |
| 全局 CLAUDE.md (规则 A/B/C/D + Tier 1/2/3) | `~/.claude/CLAUDE.md` |

---

## 9. 执行前最终 checklist (新 session 开始时)

- [ ] 读 `ai_platforms/SMOKE_V4_DESIGN_HANDOFF.md` (本文件)
- [ ] 读 `ai_platforms/smoke_v3_questions_draft.md` v3.1 (487 行)
- [ ] 读 `ai_platforms/notebooklm/dev/evidence/_progress.json` `p3_8_completion` 块
- [ ] 读 `ai_platforms/notebooklm/dev/evidence/smoke_v3_results.md` (理解为什么要 v4)
- [ ] 扫 `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v3_results.md` + `gemini_gems/dev/evidence/smoke_v3_results.md` (理解两平台已跑什么题)
- [ ] 按 Step 1 派 background audit agent, 跑 `oh-my-claudecode:document-specialist` + opus + WebFetch
- [ ] 审计完 → 回报用户 → ack 后 Step 2-4 patch
- [ ] patch 完 → 用户 ack 后进 Step 5-6 (4 平台 R1)
- [ ] R1 跑完 → 用户 review → Step 7 iterate

**此 handoff 自足**: 新 session 开始时只需 read 本文件 + smoke_v3_questions_draft.md + p3_8_completion 块即可, 无需回溯历史对话.
