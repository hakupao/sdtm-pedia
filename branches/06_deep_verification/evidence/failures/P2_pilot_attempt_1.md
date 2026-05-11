# P2 Pilot Attempt 1 — Rule B 失败归档

> Date: 2026-04-29 (P1 CLOSURE 当天)
> Phase: P2 Pilot
> Attempt: 1 (初次)
> Status: **FAILED** (Rule A scientist 19/30 = 63.3% PASS, 远低于 ≥90% gate)
> Rule B 强制归档 — 不删, 留作下一 attempt 的输入参考

---

## 1. 输入 (派发 spec)

- **Sub-plan**: `plans/P2_md_atomization.md` v1.0 (2026-04-29 user ack'd)
- **Kickoff**: `evidence/checkpoints/p2_pilot_kickoff.md` (2-type alternation: executor + writer)
- **Writer 池**: 2-type alternation lock (3-type 设想被 document-specialist 无 Write tool 否决)
- **Writer prompt**: `subagent_prompts/P0_writer_md_v1.8.md` (paired-sync v1.8 baseline 2026-04-30)
- **Schema**: `schema/atom_schema.json` v1.2 frozen
- **5 Target**:

| ID | 文件 | 行数 | Writer slot |
|---|---|---|---|
| T1' | `knowledge_base/model/01_concepts_and_terms.md` | 102 (full) | A — `oh-my-claudecode:executor` |
| T-baseline | `knowledge_base/model/04_associated_persons.md` | 38 (full) | A — executor |
| T3a' | `knowledge_base/domains/CM/assumptions.md` | 19 (full) | A — executor |
| T2' | `knowledge_base/chapters/ch04_general_assumptions.md` | 行 1-300 (slice of 1395) | B — `oh-my-claudecode:writer` |
| T3b' | `knowledge_base/domains/CM/examples.md` | 103 (full) | B — `oh-my-claudecode:writer` |

---

## 2. 产物 (5 JSONL 落地)

合计 **383 atoms**, 文件保留作历史层 (不删, 用于 v1.9 codification 抽样源):

- `evidence/checkpoints/p2_pilot_T1_md_atoms.jsonl` (71 atoms, executor)
- `evidence/checkpoints/p2_pilot_baseline_md_atoms.jsonl` (26 atoms, executor)
- `evidence/checkpoints/p2_pilot_T3a_md_atoms.jsonl` (14 atoms, executor)
- `evidence/checkpoints/p2_pilot_T2_md_atoms.jsonl` (186 atoms, writer) — 含已知缺陷
- `evidence/checkpoints/p2_pilot_T3b_md_atoms.jsonl` (86 atoms, writer) — 含已知缺陷
- `evidence/checkpoints/p2_pilot_md_atoms_combined.jsonl` (合并 383 atoms)
- `evidence/checkpoints/p2_pilot_rule_a_verdicts.jsonl` (scientist 30-atom verdicts)
- `evidence/checkpoints/p2_pilot_rule_a_summary.md` (scientist 报告)
- `evidence/checkpoints/p2_pilot_review_report.md` (code-reviewer 报告)

---

## 3. 技术判定 (Rule A scientist 抽检结果)

**Rule A scientist (oh-my-claudecode:scientist) 30-atom 分层抽检**:
- PASS rate: **19/30 = 63.3%** (gate ≥90% → **FAIL**)
- PASS+PARTIAL: 25/30 = 83.3%
- 缺陷分布:
  - PASS: 19
  - PARTIAL: 6
  - FAIL_VERBATIM: 2
  - FAIL_LINE_RANGE: 2
  - FAIL_ATOM_TYPE: 1

### 3.1 三类系统性 Writer B 缺陷 (全部源自 `oh-my-claudecode:writer`, executor 0 缺陷)

#### F-P2P-DEFECT-001 TABLE_HEADER `line_end` 越界
- **影响**: Writer B 13/13 TABLE_HEADER atoms = **100% 缺陷率**
- **症状**: `line_end` 指向整张表的最后一行而非 header+separator 行 (应该是 2 行)
- **后果**: 与后续 TABLE_ROW atoms line range 重叠, 破坏 atom 层不重叠假设
- **executor 对照**: 3/3 TABLE_HEADER atoms 全 OK (line_end = header+separator 行末)

#### F-P2P-DEFECT-002 bold text `**foo**` 被当 HEADING (附编 heading_level)
- **影响**: 14 atoms (Writer B 输出, ch04 + CM/examples)
- **症状**: 如 `**cm.xpt**` / `**relrec.xpt**` 等 dataset-label captions 被 emit 为 `atom_type: HEADING + heading_level: N`
- **应该**: SENTENCE 或 NOTE (markdown bold 不是 heading 语法)
- **executor 对照**: 0 此类缺陷

#### F-P2P-DEFECT-003 LIST_ITEM verbatim 截断 + 前缀剥除
- **影响**: ch04 系统性 (具体计数 TBD, scientist 抽样命中即 fail)
- **症状**: 多句 list item 只保留首句; bullet (`- `) 或 numbered (`10. `) 前缀被剥
- **后果**: verbatim 不字面忠实 → 违反 IR5 + IR8 + Rule B 不可生成原则
- **executor 对照** (CM/assumptions): 完整 multi-sentence 项目 + 前缀保留, 0 缺陷

### 3.2 F-P2P-001 切片指令二义性 (CONFIRMED BLOCKING)

- **症状**: Writer B 在 line 214 (---separator 前) 收手, 实际只覆盖 71% slice scope
- **缺失**: §4.2 General Variable Assumptions / §4.2.1 Variable-Naming Conventions / §4.2.1.1-3 / §4.2.2 = 估 30-50 atoms 不在 ledger
- **Writer self-claim**: "stopped at semantic boundary" — 与 task spec "lines 1-300 hard" 不一致
- **根因**: dispatch prompt 措辞 "lines 1-300" + writer-side 解释自由度大; v1.8 prompt 也无 hard-line-range 强制

### 3.3 F-P2P-002 + F-P2P-003 parent_section 约定 (PARTIAL)

- F-P2P-002: T-baseline 用 `§4.1 [OVERVIEW]` 给 unnumbered `## Overview`. 内部一致但 N27 (chapter-short-bracket) 未明确允许 invented numbering.
- F-P2P-003: CM 域用 `§CM [...]` (domain-prefix) + `§CM.0..§CM.4` (0-indexed). 0-indexed 不规范, 应 §CM.1 起.

---

## 4. 业务判定

### 4.1 Pilot Gate 8 条 (sub-plan §A.3)

| # | 条件 | 状态 |
|---|---|---|
| a | 4 target 全产 atom | ✅ PASS (5 jsonl, 383 atoms) |
| b | 切片测试 sibling_index 0-N 连续 | ⚠️ PARTIAL (内部连续但 scope 71%) |
| c | 9-enum atom_type ≥7 种 | ✅ PASS (9/9 全命中) |
| d | schema 合规 100% | ✅ PASS (uniqueness OK, 18 hooks self-claim PASS) |
| e | Rule A scientist ≥90% | ❌ **FAIL** (63.3%) |
| f | Rule D code-reviewer PASS | ⚠️ CONDITIONAL_PASS |
| g | drift cal ≥80% | 未派发 (因 e FAIL halt) |
| h | 用户 ack | 待 |

**整体**: e 单条 FAIL → 整体 FAIL (gate 是 AND 关系).

### 4.2 N21 MD-side 扩展证据 (核心业务发现)

- **P1 round 10**: PDF-side N21 EMERGENCY-CRITICAL ban writer-family 全家 (round 10 cut, 后续 4 轮 1877 atoms 0 hallucination)
- **P1 round 14 H_C 假说**: writer-direction RELIABLE on `narrative_chapter_with_grouped_list_bullets` content (drift cal sv20 p.72 16/16 byte-exact)
- **P2 Pilot 实证**: writer-family 在 MD-side **narrative + table + list** 内容上有 3 类系统缺陷 + 切片不忠 — **直接挑战 H_C 假说在 MD-side 的成立**
- **结论**: N21 应外推到 MD-side. v1.9 候选 `D-MS-NEW-14-5 content-conditional N21 refinement` 应反向推为 `N21 全 ban writer-family 含 MD-side`. 推翻 H_C "MD-side narrative 可信" 简化模型.

### 4.3 H_C 假说证据修正

- 旧 H_C: "writer 在 narrative 内容可信, 仅 TABLE_ROW 不可信"
- 新证据: writer 在 MD narrative + LIST_ITEM (CM/examples) 也截断 verbatim + 错分 atom_type. **不是仅 TABLE 问题**
- 修正: H_C 假说 **REJECTED**. writer-family blanket ban 适用 PDF + MD 双 side.

---

## 5. 下一 attempt (P2 Pilot Attempt 2) 输入

### 5.1 关键调整

1. **Writer 池缩到 1-type**: 仅 `oh-my-claudecode:executor`. 写 5 target 全 executor 单 dispatch (放弃 2-type alternation; 与 P1 round 10+ N21 全 ban 路径一致).
2. **Rule D 满足**: writer (executor) ≠ Rule A reviewer (scientist) ≠ Rule D reviewer (code-reviewer) — 3 distinct subagent_type, 仍合规 (Rule D 不强求 writer 池 ≥2 种, 只要 writer ≠ reviewer).
3. **切片指令措辞强化**: dispatch prompt 含 "**HARD line range** [N, M] inclusive — every atom MUST have line_start ≥ N AND line_end ≤ M; if last semantic unit ends before line M, emit final atom with `truncation_at_boundary: true` flag and report final line_end. **DO NOT stop at semantic boundary for convenience**." — 同时在 final report 要求 writer 显式声明 actual coverage 覆盖到 line N.
4. **3 类缺陷 awareness**: dispatch prompt 显式列出 3 个 defect 模式作 anti-pattern, 让 executor 在 self-validate 阶段额外查这 3 类 (虽然 executor 在 attempt 1 没有这 3 缺陷, 但显式 reinforce 防回归).
5. **Output 路径**: per-target JSONL 加 `_v2` 后缀 (preserve attempt 1 输出作历史层).

### 5.2 Attempt 2 dispatch 规格 (1 executor 单派发)

| ID | 文件 | 行数 | 输出 |
|---|---|---|---|
| T1' | `knowledge_base/model/01_concepts_and_terms.md` | 102 (full) | `p2_pilot_T1_md_atoms_v2.jsonl` |
| T-baseline | `knowledge_base/model/04_associated_persons.md` | 38 (full) | `p2_pilot_baseline_md_atoms_v2.jsonl` |
| T3a' | `knowledge_base/domains/CM/assumptions.md` | 19 (full) | `p2_pilot_T3a_md_atoms_v2.jsonl` |
| T2' | `knowledge_base/chapters/ch04_general_assumptions.md` | **行 1-300 HARD** | `p2_pilot_T2_md_atoms_v2.jsonl` |
| T3b' | `knowledge_base/domains/CM/examples.md` | 103 (full) | `p2_pilot_T3b_md_atoms_v2.jsonl` |

### 5.3 Attempt 2 PASS gate (复用 sub-plan §A.3 + 强化)

- Rule A scientist 30-atom 分层 ≥**90%** (与 attempt 1 同 reviewer subagent_type 但 fresh dispatch; 抽样种子换)
- 切片测试: T2' last atom line_end ≥ 295 (允许 ≤5 行边界 buffer)
- 9/9 atom_type 仍命中
- F-P2P-002/003 parent_section 决议: scientist + code-reviewer attempt 2 阶段给出 OK 或 NEEDS_FIX verdict

---

## 6. v1.9 codification 候选 (post P2 Pilot Attempt 1)

加到 v1.9 候选堆 (post-P1 已累 22 个, 加 P2 Pilot 新增):

1. **N21 全 ban writer-family 扩到 MD-side** (HIGH, 推翻 H_C; 改 N21 scope from PDF-side-only to PDF+MD all-side)
2. **R-MD-Slice-Hard rule** (HIGH): 切片任务 line range 默认 hard; soft semantic-boundary 须显式 opt-in 字段 `slice_mode: "soft"` (默认 hard)
3. **Hook 22 NEW**: pre-DONE 校验 last atom.line_end ≥ slice_end (若 hard mode); fail → halt writer
4. **TABLE_HEADER line_end rule**: 显式定义 = header row + separator row 行末 (不是表末行)
5. **bold text 非 HEADING 显式 ban**: markdown `**...**` 不是 heading; emit SENTENCE 或 NOTE
6. **LIST_ITEM verbatim 完整性 hook**: pre-DONE 校验 verbatim 含原 bullet/number prefix + 不截断多句
7. **§CM.0 0-indexed 改 §CM.1 1-indexed** (LOW): domain section 编号统一 1-based
8. **F-P2P-002 unnumbered heading parent_section 约定**: 待 reviewer 决议; 倾向用 `§N [PARENT-CHAPTER-TITLE]` 不自创 sub-numbering

---

## 7. Rule B 完结声明

本 attempt 1 **FAILED**, 输入/产物/技术判定/业务判定/下一 attempt 输入全部归档. Attempt 2 dispatch 立即跟进同 session.

attempt 1 的 5 个 jsonl 文件 + scientist verdicts + code-reviewer report 全保留 (不删), 作:
- v1.9 codification 抽样源
- attempt 2 vs attempt 1 diff 校准基线
- N21 MD-side 扩展的实证依据

---

*Filed 2026-04-29 post P1 CLOSURE same day. Attempt 2 dispatch immediate.*
