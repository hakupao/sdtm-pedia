# P2 Pilot — Main-Session Kickoff

> 创建: 2026-04-29 (P1 CLOSURE 当天, post user ack of `plans/P2_md_atomization.md` v0.1)
> 父 sub-plan: `.work/06_deep_verification/plans/P2_md_atomization.md` v1.0 (升 v0.1 → v1.0 post user ack)
> 父 PLAN: `.work/06_deep_verification/PLAN.md` v0.6 (P1 CLOSURE)
> 状态: **dispatch_pending** (writers A/B/C 即将派发)

---

## 1. Pilot Targets (4 文件 + 1 baseline 重做)

| ID | 文件 | 行数 | 类别 | Writer slot |
|---|---|---|---|---|
| **T1'** | `knowledge_base/model/01_concepts_and_terms.md` | 102 (full) | model/ | A — `oh-my-claudecode:executor` |
| **T-baseline** | `knowledge_base/model/04_associated_persons.md` | 38 (full, P0 重做) | model/ baseline calibration | A — `oh-my-claudecode:executor` (与 T1' 同 batch) |
| **T2'** | `knowledge_base/chapters/ch04_general_assumptions.md` | 行 1-300 (of 1395) | chapters/ — **切片测试** | B — `oh-my-claudecode:writer` |
| **T3a'** | `knowledge_base/domains/CM/assumptions.md` | 19 (full) | assumptions/ | A — `oh-my-claudecode:executor` (与 T1' + T-baseline 同 batch) |
| **T3b'** | `knowledge_base/domains/CM/examples.md` | 103 (full) | examples/ | B — `oh-my-claudecode:writer` (与 T2' 同 batch) |

**总 scope**: ~560 行 MD, 估 400-600 atoms.

**Writer 池修正 (2026-04-29 dispatch 前发现)**: 原 sub-plan v0.1 设想 3-type rotation (含 `document-specialist`), 但 document-specialist Tools field = "All tools except Write, Edit" — **物理无 Write tool 不能落 JSONL**. 与 P1 §0 ban 同 carry-forward, 改 **2-type alternation lock** (executor + writer). Drift cal <80% fallback `general-purpose` 当 tiebreaker.

---

## 2. Writer 派发 (2 subagent_type 并行, foreground; 修正 from 3-type)

每个 writer 收到 self-contained prompt 含:
- 加载 `subagent_prompts/P0_writer_md_v1.8.md` (paired-sync v1.8 baseline 2026-04-30) + 必要时回链 `subagent_prompts/archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` 全文
- 加载 `schema/atom_schema.json` (frozen v1.2)
- 目标文件路径 (含 line range for T2')
- 输出 JSONL 路径 (per-writer checkpoint)
- atom_id 命名规则: `md_{kb_path_short}_a{NNN}` (如 `md_model01_a001`, `md_ch04_a001`, `md_dmCM_assn_a001`)
- sibling_index 起始 0; T2' (ch04 切片) 段间 sibling_index 续接 (pilot 只跑第 1 段, 起始 0)
- `extracted_by.subagent_type` + `extracted_by.prompt_version: "P0_writer_md_v1.8"` + `extracted_by.ts` (RFC3339)

**输出文件** (per-writer checkpoint, 不直接写 root `md_atoms.jsonl`):
- Writer A (executor) → `evidence/checkpoints/p2_pilot_T1_md_atoms.jsonl` (T1' atoms) + `p2_pilot_baseline_md_atoms.jsonl` (T-baseline atoms) + `p2_pilot_T3a_md_atoms.jsonl` (CM/assumptions)
- Writer B (writer) → `evidence/checkpoints/p2_pilot_T2_md_atoms.jsonl` (ch04 lines 1-300) + `p2_pilot_T3b_md_atoms.jsonl` (CM/examples)
- ~~Writer C (document-specialist)~~ — 废弃 (无 Write tool)

主 session 在 writer 全返回后做 §3 合并校验.

---

## 3. 主 session 合并 + 校验 (post writers)

1. cat 4 jsonl → `evidence/checkpoints/p2_pilot_md_atoms_combined.jsonl`
2. atom_id 唯一性校验 (jq dedup)
3. sibling_index 连续性校验 (T2' ch04 段内 + 各文件内)
4. parent_section §N [TITLE] 形式合规 (N27/N28)
5. atom_type 9-enum 命中数统计
6. 写 `evidence/checkpoints/p2_pilot_combined_summary.md` (atom 总数 + 9-enum 命中 + schema 合规)

---

## 4. Rule A + Rule D (post 合并)

### 4.1 Rule A scientist 抽检

- Reviewer slot: `oh-my-claudecode:scientist` (P1 round 14 已烧 #68; P2 重新 fresh dispatch 视为 P2 内 slot #1, P1 池外)
- Scope: 30 atom 分层 (HEADING/SENTENCE/LIST_ITEM/TABLE_ROW/CODE_LITERAL 各 ≥4)
- 输入: combined jsonl + 对应 KB md 原文路径
- Output: `evidence/checkpoints/p2_pilot_rule_a_verdicts.jsonl` + `p2_pilot_rule_a_summary.md`
- **门槛 ≥90% PASS**

### 4.2 Rule D end-to-end reviewer

- Reviewer slot: `oh-my-claudecode:code-reviewer` (P2 内 slot #2, 不同 type vs scientist)
- Scope: 端到端 schema + atom_type 分布 + sibling_index + P0 baseline diff (T-baseline vs P0 已存)
- Output: `evidence/checkpoints/p2_pilot_review_report.md`
- **门槛: PASS / CONDITIONAL_PASS** (任何 BLOCKING fail → halt)

### 4.3 Drift cal (P2 内首次)

- 选 T1' 10 个原子 (分层)
- 派 3 种 writer type 平行 re-atomize T1' 同 10 原子位置 (不看 baseline)
- 比 atom_type + verbatim hash 一致率
- **门槛 ≥80%**, <80% halt

---

## 5. Pilot Report (post Rule A/D/drift)

写 `evidence/checkpoints/p2_pilot_report.md` 含:

- 4 target 实测 atom 数 vs 估算
- 9-enum atom_type 实测覆盖
- 切片测试结果 (T2' sibling_index 段内连续 + parent_section L2 active-heading 持续)
- Rule A scientist 30-atom verdicts 一致率
- Rule D code-reviewer 综合 verdict
- drift cal 三 type 一致率 + 偏离 motif (如有)
- P0 baseline diff (T-baseline vs P0 已存 atoms 差异分析)
- 已发现 v1.8 prompt 缺陷 / v1.9 候选
- Pilot Gate 8 条逐条 PASS/FAIL

---

## 6. 8-条 Pilot Gate (sub-plan §A.3)

- [ ] 4 target 全产 atom (无文件 0 atoms)
- [ ] 切片测试: ch04 lines 1-300 sibling_index 0-N 连续无 gap, L1/L2 active-heading 跨段持续
- [ ] 9-enum atom_type 至少命中 7 种
- [ ] schema 合规 100% (atom_id 唯一 + verbatim 非空 + parent_section §N [TITLE] 形式)
- [ ] Rule A scientist 抽检 ≥90% PASS
- [ ] Rule D code-reviewer 独立 PASS
- [ ] drift 校准 ≥80%: 3 writer type 对 T1' 同 10 原子一致率
- [ ] 用户 ack "p2 pilot 看起来合理"

任一未 PASS → halt, Rule B 失败归档 + v1.9 cut session.

---

## 7. Rule D 隔离声明 (规则 D 强制)

- Writer pool (P2 pilot): `executor` / `writer` / `document-specialist` (3 distinct subagent_type)
- Rule A reviewer: `scientist` (≠ writer pool)
- Rule D reviewer: `code-reviewer` (≠ writer pool, ≠ Rule A reviewer)
- Drift cal 3 type: 复用 writer pool 同 3 type (drift cal 是 writer 重跑性质, 不审阅 — Rule D 不冲突)

**所有 dispatch 写入 `trace.jsonl` 含 `subagent_type` + `role` (writer/reviewer/drift) + `phase: "P2_pilot"` + `ts`.**

---

## 8. 失败回退 (Rule B)

任一 writer 产出 schema 不合规 / 含 FAILURE 标记 / 输出空:
- 归档 `evidence/failures/P2_pilot_attempt_<M>.md` 含输入/产物/技术判定/业务判定/下次输入
- 主 session 决定: 换 writer type 重派 / 拆更小段 / 调 prompt
- pilot 整体不 abort, 仅该 target 失败追踪

---

*Kickoff written 2026-04-29 post user ack. Pilot dispatch immediate. ETA pilot 完成 0.5-1 session.*
