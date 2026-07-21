<!-- chain: F (深度验证旁枝链 v2)
  修改本文件后, 必须检查:
  → _progress.json                       (程序化进度)
  → evidence/checkpoints/                (每 phase 快照)
  → ../../.work/03_verification/issues_found.md   (问题回流, Issue 5+)
  → ../../.work/meta/worklog/phase06_deep_verification.md
-->

# P6 Triage + Repair — Sub-Plan

> 创建: 2026-05-12
> 状态: DRAFT v0.1
> 前置条件: P5 ALL PASS (10,435 MD 原子 reverse_verdict, 0 HALLUCINATED, 2026-05-12)
> Tier: 3 (多 session, 高 stakes)

---

## 0. 进入条件 (已满足)

| 条件 | 状态 |
|---|---|
| P5 Gate ALL PASS | ✅ 2026-05-12 |
| coverage_ledger.jsonl 完整 | ✅ 12,487 atoms |
| section_coverage.jsonl 完整 | ✅ 399 sections |
| reverse_ledger.jsonl 完整 | ✅ 10,435 atoms |
| _progress.json current_phase = P6_triage | ✅ |

---

## 1. 当前数字快照 (P6 启动时)

### 1.1 覆盖率

| 指标 | 值 |
|---|---|
| 总 PDF 原子 (含 INTENTIONAL_EXCLUDE) | 12,487 |
| INTENTIONAL_EXCLUDE (已批准) | 394 |
| 调整后分母 | 12,093 |
| 已覆盖 (EXACT + EQUIVALENT + PARTIAL + MISPLACED) | 9,498 |
| **当前覆盖率** | **78.5%** |
| MISSING | 2,502 |
| ERROR | 93 |
| **99% 目标允余 MISSING+ERROR** | **≤ 120** |
| **P6 须关闭 gap** | **2,475 atoms** |

### 1.2 MISSING 来源分布

| Source | MISSING 数量 | 处理路径 |
|---|---|---|
| sv20 (SDTM v2.0) | 363 | 大部分 VERSION_MISMATCH/INTENTIONAL_EXCLUDE |
| ig34 (SDTMIG v3.4) | 2,139 | 分层: spec table IE + real repair |

### 1.3 section_coverage.jsonl 分布

| Verdict | 数量 | P6 行动 |
|---|---|---|
| FULL_COVERAGE | 101 | 无需处理 |
| MOSTLY_COMPLETE | 42 | 抽检 shall/must (§9.2 gate) |
| CONTENT_TRUNCATED | 110 | MEDIUM Issue, 分批修复 |
| SIBLING_DROPPED | 56 | HIGH Issue, 修复 |
| SKELETON_ONLY | 67 | 18 real HIGH Issue; 49 IE 申请 |
| STRUCTURE_DRIFTED | 23 | HIGH Issue, 修复 |

### 1.4 UNSOURCED_CANDIDATE

| 指标 | 值 |
|---|---|
| 总量 | 926 |
| 已 Rule A 抽查 30: 27/30 = P4a false negative | ~89% 预计可升为 SOURCED |
| HALLUCINATED (P5 rule_a 结论) | 0 |

---

## 2. P6 工作分解 (Work Breakdown)

P6 分为 5 个子任务 (T1-T5), 按优先级顺序执行:

```
T1 → T2 → T3 (并行 T2/T3) → T4 → T5 (Gate)
```

### T1: MISSING 原子分层脚本 (无 agent, 纯 Python)

**目的**: 产 `evidence/checkpoints/p6_missing_stratification.json` — 把 2,502 MISSING 分到 5 个 bucket:

| Bucket | 判定规则 | 预期数量 | 行动 |
|---|---|---|---|
| `IE_version_mismatch` | `pdf_atom_id` 前缀 `sv20_` AND section 在 sv20 superseded list | ~300 | 批量 INTENTIONAL_EXCLUDE |
| `IE_spec_table` | 所在 parent_section 是 `*_Specification` 且 domain spec 已有 spec.md | ~150 | 批量 INTENTIONAL_EXCLUDE |
| `IE_editorial` | parent_section 含 editorial 关键词 (Appendix A, SDS Team 等) | ~50 | 批量 INTENTIONAL_EXCLUDE |
| `HIGH_content_gap` | SKELETON_ONLY 或 STRUCTURE_DRIFTED 节 + atom_type ∈ {SENTENCE, LIST_ITEM, NOTE} | ~600 | 开 Issue 5+, T4 修复 |
| `MEDIUM_partial` | 其余 MISSING (CONTENT_TRUNCATED 节, 散落 MISSING) | ~1400 | Issue MEDIUM, 分批修复 |

**产物**: `scripts/p6_stratify_missing.py` + `evidence/checkpoints/p6_missing_stratification.json`

**Rule D**: 纯脚本 + 脚本自检, 无独立 reviewer 要求 (T1 是工具步, 不是 AI 判断步); T2 批量 IE 扩充时用户 ack 作 approval gate.

---

### T2: INTENTIONAL_EXCLUDE 批量扩充

**输入**: T1 的 IE bucket (`IE_version_mismatch` + `IE_spec_table` + `IE_editorial`)

**步骤**:
1. 脚本生成 IE 候选列表 (atom_id + category + exclusion_reason)
2. 主 session 汇总统计展示给用户 (分 category 列表, ≤20 行摘要)
3. 用户一次性 ack (或逐 category ack)
4. 脚本写入 `intentional_exclude_whitelist.md` + 更新 `coverage_ledger.jsonl` verdict → `INTENTIONAL_EXCLUDE`
5. 重算覆盖率, 写入 `evidence/checkpoints/p6_post_ie_coverage.md`

**预期效果**: 新增 ~500 INTENTIONAL_EXCLUDE → 调整覆盖率预计升至 **~86-88%**

**Gate**: 用户明确 ack + 脚本完整性校验 (无 orphan atom)

---

### T3: UNSOURCED_CANDIDATE 批分类 (并行 T2)

**输入**: `reverse_ledger.jsonl` 中 926 个 `UNSOURCED_CANDIDATE` 原子

**分类算法 (脚本优先)**:

```
Step 1: 重跑 fuzzy lookup (lower threshold 0.55 — 比 P5 更宽松)
        → 命中: 升为 SOURCED_P4A_MISSED_T3
Step 2: 检查 atom_type:
        HEADING / TABLE_HEADER / CROSS_REF → auto: SYNTHESIZED
Step 3: 检查文件路径:
        VARIABLE_INDEX / INDEX / ROUTING → already handled by P5, re-check
Step 4: 剩余 → agent 批处理 (每 50 atoms = 1 batch, subagent_type: oh-my-claudecode:scientist)
        每 batch: agent 看 verbatim + parent_section + source_file → verdict:
        SOURCED | SYNTHESIZED | UNSOURCED (合理编辑添加) | HALLUCINATED
```

**Rule D**: writer = `oh-my-claudecode:scientist`, reviewer = `oh-my-claudecode:verifier` 抽查 20%

**产物**: `evidence/checkpoints/p6_unsourced_classified.jsonl` + 更新 `reverse_ledger.jsonl`

**Gate**: HALLUCINATED = 0 (若发现 → 立即开 HIGH Issue + 停止 T3)

---

### T4: 节级修复 (Issue 开+修)

**范围** (按优先级):

**Tier A — HIGH (18 real SKELETON_ONLY + 23 STRUCTURE_DRIFTED)**:

处理流程:
1. 对每个 section: 读 PDF 原文 (P1 已有 atoms) + 读现有 KB md
2. writer agent (oh-my-claudecode:executor, model=opus) 补写/修正 KB md
3. 独立 reviewer agent (不同 subagent_type) 审改动
4. 通过 → 更新 coverage_ledger 相关 atom verdict
5. 开 Issue 5+ (或若 section 完全补写 → 开 + 立即 close)

**Tier B — HIGH/MEDIUM (56 SIBLING_DROPPED + 110 CONTENT_TRUNCATED)**:

处理方式:
- 先脚本聚合: 哪些 SIBLING_DROPPED/CONTENT_TRUNCATED 节实际上已有足够覆盖 (PARTIAL 原子多) → 有些可升级
- 剩余真实 gap → 开 Issue, 按优先级分批修复
- 含 shall/must 关键词丢失的 CONTENT_TRUNCATED → HIGH Issue
- 其余 → MEDIUM Issue, 允许 P7 前关闭

**subagent 分配原则**:
- 每节 = 1 writer subagent (独立 session) + 1 reviewer subagent (不同 type)
- 每 5 节组成 1 batch 并行派发
- Tier A batch 轮换 writer_type: executor → writer → executor (交替)

---

### T5: 覆盖率验证 + Gate

**步骤**:
1. 重跑 coverage 计算脚本 (T1 脚本扩展版)
2. 验证: 覆盖率 ≥ 99% (adjusted) 或 MISSING+ERROR ≤ 120
3. 验证: 0 SKELETON_ONLY 无 IE 或 closed Issue
4. 验证: 0 STRUCTURE_DRIFTED unresolved
5. 验证: UNSOURCED_CANDIDATE all classified (0 残留)
6. Rule D 独立 gate reviewer (subagent_type: `oh-my-claudecode:critic`)
7. 写 `evidence/checkpoints/p6_exit_gate_report.md`
8. trace.jsonl 写 `phase_report` 事件

---

## 3. Exit Gate (P6)

| Gate | 条件 | 阈值 |
|---|---|---|
| G1 | 覆盖率 ≥ 99% (adjusted, excl IE) | ≥ 99% |
| G2 | SKELETON_ONLY 全部有 IE 登记或 Issue closed | 0 unresolved |
| G3 | STRUCTURE_DRIFTED 全部有 Issue closed | 0 unresolved |
| G4 | UNSOURCED_CANDIDATE 全部分类完毕 | 0 残留 |
| G5 | HALLUCINATED = 0 (或已开 HIGH Issue + 修复完成) | 0 unresolved |
| G6 | Rule D reviewer PASS | 独立 subagent PASS |
| G7 | trace.jsonl P6 phase_report ≥ 1 | ≥ 1 |

---

## 4. Issue 5+ 编号规划

当前 Issue 1-4 已在 `.work/03_verification/issues_found.md`.

P6 新 Issue 编号:
- **Issue 5**: 第一个 SKELETON_ONLY real section (待定)
- **Issue 6**: 第二个 SKELETON_ONLY real section
- ... (顺序以 T4 执行顺序决定)
- STRUCTURE_DRIFTED issues 接续 SKELETON_ONLY 之后

---

## 5. 工作量估算

| 子任务 | 预估 session 数 | 并行度 |
|---|---|---|
| T1 (stratification 脚本) | 0.5 | 串行 |
| T2 (IE 批扩) | 0.5 (含用户 ack) | 串行 |
| T3 (UNSOURCED 分类) | 1 | 并行 T2 后半段 |
| T4 Tier A (41 HIGH sections) | 3-4 | 5 节/batch 并行 |
| T4 Tier B (166 MEDIUM sections) | 4-6 | 10 节/batch 并行 |
| T5 (Gate) | 0.5 | 串行 |
| **合计** | **~10-13 sessions** | |

---

## 6. Rule D Slot 规划 (接续 P5 roster)

P5 已烧 slots 见 `audit_matrix.md`. P6 新分配:

| T | Writer 候选 | Reviewer 候选 |
|---|---|---|
| T3 | `oh-my-claudecode:scientist` | `oh-my-claudecode:verifier` |
| T4-Tier A (奇 batch) | `oh-my-claudecode:executor` (model=opus) | `oh-my-claudecode:code-reviewer` |
| T4-Tier A (偶 batch) | `executor` (model=opus) | `oh-my-claudecode:critic` |
| T4-Tier B | `executor` | `feature-dev:code-reviewer` |
| T5 Gate | — | `oh-my-claudecode:critic` |

---

## 7. 第一步执行 (本 session 可立即启动)

**T1 脚本**: `scripts/p6_stratify_missing.py`

立即派 executor agent 编写该脚本, 运行产出分层报告, 然后主 session 向用户展示摘要请求 ack.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-05-12 | Initial DRAFT — 基于 P5 ALL PASS 数据启动 |
