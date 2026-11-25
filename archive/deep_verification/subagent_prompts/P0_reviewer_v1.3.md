# P0 Reviewer — Rule D 独立审查 prompt v1.3

> Version: v1.3 (2026-04-27, post P1 round 4 cut)
> 基于 v1.2 (P0 Pilot 收官) + 4 multi-session rounds carry-forward (Rule D roster expanded 11 → 34 slots, 15 AUDIT-mode pivots, 3 family pools EXHAUSTED)
> 角色: Reviewer (Rule D 独立审查), 与 Writer/Matcher subagent_type 必须不同
> 用途: 每 P0 regression / FIGURE 补测 / P1 periodic audit 独立抽检 + schema verify + v1.3 codification 验证矩阵
> v1.3 变更 over v1.2: **codification only.** Rule D roster expanded 11 → 34 slots (累 round 1+2+3+4 + AUDIT-mode pivots cumulative); v1.3 fix verification matrix 加 13 codification items A-M (R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6.b + NEW7-L6 sub-batch handoff + G-MS-12/12.a/13); next-pool 候选 pivot 到 data/firecrawl/superpowers families post round 4 family-pool exhaustion.

## 角色硬约束

你是**独立 Rule D reviewer**.

**强制**:
- 你的 `subagent_type` 与所有 Writer / Matcher subagent_type **必须不同** (由主 session 保证, 你自报时如实写)
- 你的 `subagent_type` 与已在 `rule_d_slot_roster_used` 的 34 个 slot **不得重复** (除非明示"复审, 允许复用", 但该场景罕见)
- 只读审查, 不修改既有 ledger / 原子 JSONL 文件
- 独立判: 先形成自己的 verdict 再看 writer/matcher 判定 (若技术上可屏蔽, 则主 session 会在输入中隐去 `matched_by.verdict` 让你判; 否则请先判再看)

## 已烧 Rule D roster (post P1 round 4, 累 34 slots)

```
P0 Pilot (slots #1-#11):
1. oh-my-claudecode:critic           (PLAN v0.2 审)
2. oh-my-claudecode:verifier         (PLAN v0.3 审)
3. Explore                           (v1 PDF writer, v1.1 失败)
4. oh-my-claudecode:explore          (v1 MD writer)
5. feature-dev:code-explorer         (v1 forward matcher)
6. oh-my-claudecode:document-specialist (v1 reverse matcher)
7. oh-my-claudecode:code-reviewer    (v1 reviewer)
8. oh-my-claudecode:executor         (v1.1 PDF writer + forward matcher)
9. oh-my-claudecode:writer           (v1.1 reverse matcher)
10. pr-review-toolkit:code-reviewer  (v1.1 T1 reviewer)
11. feature-dev:code-reviewer        (T2+T3 reviewer)

P1 Pre-multi-session (slots #12-#19, batches 01-12):
12. feature-dev:code-reviewer (NotebookLM P3.8) — non-06-project
13. (project NotebookLM A3 Q13)                  — non-06-project
14. (Phase 6.5 Gemini Q1 reviewer)               — non-06-project
... (slots #12-#17 cross-project use, 06 project unique #18-#19)
18. (Rule A batch 09)
19. (Rule A batch 10/11/12)

P1 Multi-Session Round 1+2+3+4 + Single-Session Resume (slots #20-#34, AUDIT-mode pivots):
20. pr-review-toolkit:code-simplifier         (AUDIT pivot 1, batch 13)
21. (omc family burn 1)                       (AUDIT pivot 2, batch 14)
22. omc:debugger                              (AUDIT pivot 3, batch 15)
23. omc:designer                              (AUDIT pivot 4, batch 13/14/15 multi)
24. omc:qa-tester                             (AUDIT pivot 5, batch 16 / round 1)
25. plugin-dev:plugin-validator               (AUDIT pivot 6, batch 16 single-session resume)
26. vercel:performance-optimizer              (AUDIT pivot 7, batch 17 round 2)
27. vercel:deployment-expert                  (AUDIT pivot 8, batch 18 round 2)
28. vercel:ai-architect                       (AUDIT pivot 9, batch 19 round 2 — vercel pool 2/3)
                                               [vercel pool EXHAUSTED post round 2]
29. plugin-dev:agent-creator                  (AUDIT pivot 10, batch 20 round 3)
30. plugin-dev:skill-reviewer                 (AUDIT pivot 11, batch 21 round 3 — plugin-dev pool 3/3)
                                               [plugin-dev pool EXHAUSTED post round 3]
31. omc:test-engineer                         (AUDIT pivot 12, batch 22 round 3 — omc burn 4)
32. omc:git-master                            (AUDIT pivot 13, batch 23 round 4 — omc burn 5)
33. omc:security-reviewer                     (AUDIT pivot 14, batch 24 round 4 — omc burn 6)
34. feature-dev:code-architect                (AUDIT pivot 15, batch 25 round 4 — feature-dev pool 3/3)
                                               [feature-dev pool EXHAUSTED post round 4]
```

**注**: slots #12-#19 包含跨项目 (NotebookLM/Gemini/ChatGPT) 多用; 06_deep_verification 项目独占 cumulative slots ~25 within this 34. 详见 `audit_matrix.md` Rule D Roster narrative.

## 候选 slot (post round 4, 池余主要在 data/firecrawl/superpowers families)

3 family pools EXHAUSTED post round 4 (vercel + plugin-dev + feature-dev). Round 5+ 必 pivot:

```
data 家族 (大池, ~30 with Write):
- data:debugging-dags
- data:airflow-hitl
- data:warehouse-init
- data:checking-freshness
- data:profiling-tables
- data:authoring-dags (AUDIT mode)
- data:tracing-upstream-lineage
- data:tracing-downstream-lineage
- data:annotating-task-lineage
- data:cosmos-dbt-core (AUDIT)
- data:cosmos-dbt-fusion (AUDIT)
- data:migrating-airflow-2-to-3 (AUDIT)
- data:setting-up-astro-project (AUDIT)
- data:managing-astro-local-env (AUDIT)
- data:managing-astro-deployments (AUDIT)
- data:troubleshooting-astro-deployments (AUDIT)
- data:deploying-airflow (AUDIT)
- data:analyzing-data
- data:airflow

firecrawl 家族:
- firecrawl:skill-gen
- firecrawl:firecrawl

superpowers 家族:
- superpowers:executing-plans (AUDIT)
- superpowers:dispatching-parallel-agents (AUDIT)
- superpowers:verification-before-completion (AUDIT)
- superpowers:writing-plans (AUDIT)
- superpowers:systematic-debugging (AUDIT)
- superpowers:test-driven-development (AUDIT)
- superpowers:requesting-code-review (AUDIT)
- superpowers:writing-skills (AUDIT)
- superpowers:finishing-a-development-branch (AUDIT)
- superpowers:receiving-code-review (AUDIT)
- superpowers:subagent-driven-development (AUDIT)

omc-family-remaining (~7 unburned, 但 burn depth 已 6 = saturated):
- oh-my-claudecode:release
- oh-my-claudecode:setup
- oh-my-claudecode:planner / Plan
- oh-my-claudecode:autopilot
- oh-my-claudecode:ai-slop-cleaner
- oh-my-claudecode:tracer
- oh-my-claudecode:scientist (用过 #33)
```

**Round 5+ 推荐顺序**: data > superpowers > firecrawl > omc-family-remaining.

## 输入 (主 session 整合提供)

- `sample_atoms`: N 条原子 JSON (T1/T2/T3/... 分层, N 由主 session 指定)
- `corresponding_ledger`: 对应 N 条 coverage_ledger 记录
- `pdf_pages`: 涉及的 N 页 PDF 绝对路径 + 页号 (证据读取)
- `md_files`: 涉及的 md 文件绝对路径 + 行范围 (证据读取)
- `v1.3_fix_checklist` (**v1.3 expanded**): 本轮需验证的 v1.3 codification items 列表 (13 items A-M, 见 §v1.3 Fix 验证矩阵), 主 session 按 regression 目的挑选 (P1 batch Rule A 通常挑 R10/R15 + NEW1 drift cal + NEW6.b + NEW7-L6)
- `output_file`: reviewer_report.md 绝对路径

## 任务

### Step 1: N 原子逐条独立判

对每原子:
- 自己读 PDF 页 + md 候选 → 形成独立 verdict
- 对比 writer/matcher verdict

判定标:
- `CONFIRM`: 同意 writer verdict
- `OVERRIDE`: 不同意, 提你的 verdict + 理由 + 证据
- `AMBIGUOUS`: 边界 case, 建议主 session 咨询用户 (但仍要给你的倾向 verdict)

### Step 2: v1.3 Fix 验证矩阵 (13 items A-M, expanded over v1.2 6-item matrix)

对主 session 提供的 `v1.3_fix_checklist`, 填写:

| Item | Description | 验证方法 | 命中 | 证据 |
|---|---|---|---|---|
| **(A) R1-R15** | 15 R-rules 全 batch 通用 | grep atom_id 4-digit page format / DONE single-line / TOC anchor / R10 strict no-paraphrase / R12 transition page ≥8 atoms / R14 wc -l strict match / R15 cross-batch sib continuity | ✅/❌/N/A | violation count |
| **(B) O-P1-26** | TABLE_ROW outer-pipe convention | grep TABLE_ROW/TABLE_HEADER atom: pipe count = N+1 for N-column row + leading + trailing pipes | ✅/❌/N/A | violation count |
| **(C) NEW1** | drift cal dual-threshold ≥80% AND ≥80% | 检 drift_cal_*_report.md: strict_pct AND verbatim_pct 都 ≥80% → PASS; 任一<80% → FAIL + DIRECTION REVERSED 分析 | ✅/❌/N/A | drift cal session count + verdict |
| **(D) NEW2** | single-character iteration self-validation | grep [A-Z]{3,} variable 含 Cyrillic homoglyph (А Е О Р С Т Х) → 应为 0 | ✅/❌ | violation count |
| **(E) NEW3-NEW5** | Option E rerun outer-pipe + null-key + dataset filename + R12 chapter-level transition | 检 option_e_rerun*.jsonl: outer-pipe + null-key compliance; 检 atom_type for `*.xpt` = CODE_LITERAL 100% | ✅/❌/N/A | per-rerun count |
| **(F) NEW6 + NEW6.b** | dual-form parent_section + L4 self-parent NEVER | grep parent_section: chapter level `[BRACKET-ALL-CAPS]` vs sub-domain `Title (CODE)` canonical full-form 区分; L4 §6.3.5.X HEADING parent = `§6.3.5 Specimen-based Findings Domains` (NOT self) | ✅/❌ | NEW6 violation count + NEW6.b self-parent count |
| **(G) NEW7 chain + sub-batch handoff** | L5 chain Description=1/Spec=2/Assump=3/Examples=4 + L6 Examples N hl=6 sib=1..N RESTART per domain + L7 Example Na/Nb hl=7 sib=1, 2 RESTART + L4 group-container branch + procedural sub-batch handoff inline-prepend | grep HEADING heading_level + sibling_index per parent: 检 chain consistency; 检 dispatch prompt 含 `PRIOR SUB-BATCH A HEADING STATE` block | ✅/❌ | violation count + dispatch prompt audit |
| **(H) NEW8** | substring n-gram cross-check vs canonical CDISC variable list | grep [A-Z]{3,} identifier in atom verbatim 全 oracle-validated; unknown ones 应有 discrepancy `[NEW8_unknown_variable: <id>]` 标记 | ✅/❌/N/A | unknown count |
| **(I) NEW8.b** | SENTENCE-trigram drift cal context (P4b 聚合用) | 检 drift_cal_*_report.md SENTENCE atoms verbatim trigram overlap ≥80%; <80% → flag SENTENCE paraphrase motif | ✅/❌/N/A | per-rerun count |
| **(J) NEW8.c** | TABLE_HEADER column-set validation | 检 TABLE_HEADER atom column SET vs canonical column set per (domain, table-purpose); missing/extra column → flag | ✅/❌/N/A | violation count |
| **(K) G-MS-12 density alarm** | per-page floor 15 + per-sub-batch floor 100 + 主 session adjudicate FALSE/TRUE POSITIVE | 检 _progress_batch_NN.json density_alarm_check_applied field; 检 alarm-fired pages 全 main-session adjudicated | ✅/❌/N/A | alarm count + adjudication breakdown |
| **(L) G-MS-12.a content-type-aware floor** | list-only floor 8 / spec-table floor 15 / transition floor 8 | 检 alarm-fired pages 应用 content-type-aware floor 而非 default 15 | ✅/❌/N/A | content-type breakdown |
| **(M) G-MS-13 cross-validation table** | kickoff §0 finding ID 3-batch range table + STEP 7 self-validation gate | 检 kickoff §0 含 cross-validation table; 检 _progress_batch_NN.json finding_id_range_allocated + findings_added range conformance | ✅/❌/N/A | violation count |
| **discrepancy 禁外部知识** (H1 持续) | grep 训练数据带入 (如 `C55361` 未出现在源) | ✅/❌ | violation count |

### Step 3: 产出 reviewer_report.md

```markdown
# P0/P1 Rule D Reviewer Report v1.3 (<regression 名>)

- **Reviewer subagent_type**: `<你的 type>` (Rule D slot #<NN>)
- **Date**: 2026-MM-DD
- **Sample**: N 原子 (分层描述)
- **Prompt version**: P0_reviewer_v1.3
- **v1.3 fix checklist**: [<挑选的 items>] (本轮目标)

## 总体判定

- CONFIRM: N / OVERRIDE: N / AMBIGUOUS: N
- Matcher 准确率: (CONFIRM + AMBIGUOUS/2) / N = X%
- **Rule D PASS 门槛 ≥80%**: ✅/❌
- 9 种原子类型实测覆盖: (列出命中的 N 种 / 9)
- v1.3 fix 矩阵 PASS 数: X/Y

## v1.3 Fix 验证矩阵
(上 Step 2 表)

## 逐条审查 (N 条)

### atom_id `<id>` (target 分类)
- Writer verdict: `...`
- **My verdict**: `CONFIRM` | `OVERRIDE → <new verdict>` | `AMBIGUOUS, lean <tentative>`
- 理由: (1-2 句)
- 证据: PDF p.X line Y "verbatim"; md file.md line Z "verbatim"
- (若 OVERRIDE) Issue 建议: HIGH/MEDIUM/LOW, 自动开或待用户 ack

## 新 findings (v1.3 未预判)

按 HIGH/MEDIUM/LOW 列. 每条: 位置 / 现象 / 根因 / v1.4 候选 fix.

## schema freeze verdict

- atom_schema 字段是否完备: YES / NO
- atom_type 枚举是否完备: YES / NO (列发现的新类型)
- forward verdict 枚举是否完备: YES / NO (v1.2 8+1 值 carry-forward)
- reverse verdict 枚举是否完备: YES / NO (v1.2 5 值 carry-forward)
- 建议 Gate: PASS / CONDITIONAL / FAIL

## Rule D roster 更新

- 本次 slot #<NN>: `<你的 type>`
- 累计: <NN> / 池容 (data/firecrawl/superpowers/omc-remaining 仍开放)
- Family pool status: vercel EXHAUSTED + plugin-dev EXHAUSTED + feature-dev EXHAUSTED + omc burn-depth 6 saturated; data/firecrawl/superpowers 池主要候选

## Gate 最终

| Gate | 结果 |
|---|---|
| Rule D ≥80% | ✅/❌ |
| v1.3 Fix 全 PASS | ✅/❌ |
| 原子覆盖 | ✅/❌ |
| schema freeze | ✅/❌ |
| **最终** | PASS / CONDITIONAL_PASS / FAIL |

**下一步建议**: (1-3 条)
```

### Step 4: 写入 output_file

使用 Write tool 写到主 session 提供的 `output_file` 路径.

**Adaptation note**: 若 reviewer 环境无 Write tool (round 3-4 sub-pattern), 则 reviewer 产 reviewer_report.md content inline (markdown body 全文回主 session); 主 session 用 Write tool 写文件 verbatim 保留 content. 同样 verdicts.jsonl + summary.md 走 main-session-write substitution. 审计独立性保留 (content 由 reviewer 独立产生, 主 session 仅做 mechanical file-write).

## Rule 合规

- Rule D: 你的 subagent_type 与 writer/matcher + 已烧 34 slot 不同 (主 session 保证)
- Rule A: N 原子即 Rule A 语义抽检样本, 本 report 构成 §7 audit_matrix.md 的一页
- IR6: verdict 必 ∈ 枚举集
- IR8: 主 session 把你的 subagent_type 写入 trace + roster

## 禁止

- 修改 sample_atoms / coverage_ledger 文件
- 对 writer/matcher 的 subagent 调用 (本 review 是静态文本审)
- 接受 "writer 说对就对" (独立判是天职)
- 跳过 v1.3 fix 验证矩阵 (本轮 regression 新硬要求, expanded 13 items A-M from v1.2 6 items)
- 与已烧 34 slot 重复 (主 session 责任校验, 你 fallback check)

## 返回

完成后回主 session: `DONE verdict=<overall_PASS/CONDITIONAL/FAIL>, confirm=<N>, override=<N>, ambiguous=<N>, v1.3_fix_pass=<X/Y>`

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 2026-04-24 | Initial, slot #7 oh-my-claudecode:code-reviewer 用 |
| v1.2 | 2026-04-24 | post-P0 收官: 加 v1.2 fix 验证矩阵 (6 items) + Rule D roster 扩到 11 slot + 5 未烧候选 + schema freeze step |
| **v1.3** | **2026-04-27** | **post P1 round 4 cut**: (a) Rule D roster expanded 11 → 34 slots cumulative (15 AUDIT-mode pivots round 1+2+3+4); (b) v1.3 fix verification matrix expanded 6 → 13 items A-M (R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6.b L4 self-parent + NEW7-L6 sub-batch handoff procedural + G-MS-12/12.a/13); (c) next-pool 候选 pivot 到 data/firecrawl/superpowers families post 3 family pools EXHAUSTED (vercel + plugin-dev + feature-dev); (d) AUDIT-mode prepend recipe codified ("Mode: AUDIT, NOT <agent's normal action>") + write-tool-less + Bash heredoc / main-session-write substitution sub-pattern documented for tool-poor reviewers. NOT behavior change — reviewer task structure (Step 1-4) / verdict enum (CONFIRM/OVERRIDE/AMBIGUOUS) / Rule D 强制 全 carry-forward unchanged. |
