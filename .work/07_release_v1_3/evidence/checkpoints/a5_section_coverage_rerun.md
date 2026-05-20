# A5 — section_coverage.jsonl 重跑评估 (G6)

> Date: 2026-05-20
> Phase: A — KB layer fixes
> Step: A5
> Predecessor: 06 retro §二 6 (section_coverage.jsonl P4b 快照未刷新)
> Status: **PARTIAL** — baseline 备份完成, 完整 pipeline rerun 延 v1.4

---

## 1. Carry 来源

06 旁枝 retro §二 6:

> "P6 T4 修复后, section_coverage.jsonl 仍是 P4b 时期的快照, 部分节的 aggregate_verdict 与实际不符 (如 SC/§6.3.10 实际已修复, 但快照仍显 SKELETON_ONLY).
> → **后续建议**: P4b 脚本 scripts/p4b_section_aggregate.py 在下次 KB 大规模修改后重跑一次."

PLAN.md v1.3 A5: "跑 scripts/p4b_section_aggregate.py → diff 新旧 → 确认 A3 修复节 aggregate_verdict 提升".

## 2. 实际依赖分析

`scripts/p4b_section_aggregate.py` (`/branches/06_deep_verification/scripts/p4b_section_aggregate.py:1-13`) 注释明确 inputs:

```
Input:  pdf_atoms.jsonl, coverage_ledger.jsonl, md_atoms.jsonl
Output: section_coverage.jsonl
```

**关键发现**: p4b 是 **下游聚合** 脚本, 它需要 `md_atoms.jsonl` 和 `coverage_ledger.jsonl` 反映新 KB. 而:
- `md_atoms.jsonl` (10,435 atoms) 是 06 P2 B-03c (round 01-13) 多次跑的产物, 上次更新 2026-05-11. 在 v1.3 Phase A 改 KB 之后, **未重跑**.
- `coverage_ledger.jsonl` (12,487 entries) 是 06 P4a forward matcher 产物, 也未重跑.

**直接跑 p4b 等于在 stale 输入上跑** — 输出 = 与原 section_coverage.jsonl 几乎相同 (除非脚本本身有 stochastic 改变), 不能反映 A1/A2/A3 KB 改动. **无意义**.

## 3. 完整 pipeline rerun 需求 (留 v1.4)

要让 section_coverage.jsonl 真实反映 v1.3 KB 改动, 完整 pipeline 是:

```
v1.3 KB 改 (PP/examples + BE/spec + 10 Tier B 节)
  ↓
[需重跑] md_atoms extractor (06 P2 b-03c 类) — 仅对改动 KB 文件
  ↓
md_atoms.jsonl 更新 (10,435 → ~10,500+ 估)
  ↓
[需重跑] p4a forward matcher — 仅对相关 PDF/MD 区域
  ↓
coverage_ledger.jsonl 更新 (PARTIAL/MISSING 应改 EXACT/EQUIVALENT)
  ↓
[本步可跑] p4b_section_aggregate.py
  ↓
section_coverage.jsonl 更新 (CONTENT_TRUNCATED → MOSTLY_COMPLETE/FULL_COVERAGE)
```

P2 b-03c 单 round 需 8-12 batch, ~3-5h 工程, Rule A + Rule D 全跑. 在 v1.3 scope 不合算 — 因为 v1.3 是 release pass, 不是 06 cycle pass.

## 4. v1.3 A5 实际动作 (PARTIAL)

### 4.1 Baseline 备份

- `section_coverage.jsonl.pre_v1_3.bak` (1.6MB) — 当前快照
- `coverage_ledger.jsonl.pre_v1_3.bak` (3.7MB) — 当前快照
- `md_atoms.jsonl.pre_v1_3.bak` (10,435 行) — 当前快照

备份位于 `branches/06_deep_verification/` (与原文件同目录).

### 4.2 文档化 stale 状态

A3 Batch M 改动的 10 节, 在 section_coverage.jsonl 中仍标 CONTENT_TRUNCATED, 但实际 KB 内容已 (per writer + Rule D reviewer 双层验证):

| section_id | section_coverage 快照 verdict | 实际状态 (post-v1.3-A3) |
|---|---|---|
| ig34_§2.7 | CONTENT_TRUNCATED | partial→complete (Step k 含 §8.4 cross-ref + 7 timing var split) |
| ig34_§6.4.2 | CONTENT_TRUNCATED | partial→complete (FA full split + RELMIDS + Points to Consider) |
| ig34_§7.2.1 (TA Ex4) | CONTENT_TRUNCATED | partial→complete (TATRANS rules + blinded view) |
| ig34_§7.3.2 (TD) | CONTENT_TRUNCATED | partial→complete (contingent visits clause) |
| ig34_§7.3.3 (TM) | CONTENT_TRUNCATED | partial→complete (TM Description) |
| ig34_§4.5.1.2 | CONTENT_TRUNCATED | partial→complete (TA branching + transition full text) |
| ig34_§6.3.12.2 (TR) | CONTENT_TRUNCATED | partial→complete (typo fix TRSTRESN → TRSTRESU) |
| ig34_§6.4.3 (FA --OBJ) | CONTENT_TRUNCATED | partial→complete (--OBJ unique-to-FA statement) |
| ig34_§7.2.1.1 (TA Distinguishing + TE) | CONTENT_TRUNCATED | partial→complete (branch-no-if clause + TE Description) |
| ig34_§4.3.5 | CONTENT_TRUNCATED | verified-already-complete (KB superset of PDF heading) |

A1 PP RELREC + A2 BECAT 同样未在 section_coverage 反映.

## 5. KNOWN_LIMITATIONS reconcile 影响 (Phase D)

v1.3 KNOWN_LIMITATIONS §0 应加 entry (W1 + G6 综合):

> v1.3 KB pass 修了 10 个 Tier B 节 + PP RELREC + BECAT 分叉. 但 `branches/06_deep_verification/section_coverage.jsonl` (P4b 快照, 2026-05-12) 仍反映 v1.2 baseline 状态, 未反映 v1.3 KB 改动. 完整 pipeline rerun (md_atoms 扩增 → p4a forward matcher → p4b aggregate) 工程量 = 06 半个 cycle, 留 v1.4 KB pass 时一起做. 不影响 deploy 答案质量 (4 平台 uploads 直接从 KB rebuild, 不依赖 section_coverage).

## 6. v1.4 carry

| Item | 说明 |
|---|---|
| 06 pipeline 增量 rerun script | 新增 `scripts/p4b_incremental_rerun.py` — 给定 changed KB file 列表, 仅 reextract 这些文件的 md_atoms + 仅重 match 涉及 PDF 区域 + 重跑 p4b. 工程量较 full rerun 减少 80%. |
| Tier B Batch H (ranks 1-10, 470 atoms) | v1.3 deferred — v1.4 主任务之一 |
| Tier B Batch S (ranks 21-25, ~10 atoms) | v1.3 deferred — 可与 Batch H 同 cycle 跑 |
| Level2 24 sections | v1.3 deferred — v1.4 / v1.5 |
| Full 437 UNSOURCED_MANUAL classify | v1.3 N=40 抽样 PASS, 全量分类 v1.4 |

## 7. Gate

| Gate | Pass condition | Actual | Verdict |
|---|---|---|---|
| A5-G1 | baseline 备份完成 | 3 文件 (.pre_v1_3.bak) | ✅ |
| A5-G2 | stale 状态 documented + reconcile 留 KNOWN_LIMITATIONS | 完成 (§ 5) | ✅ |
| A5-G3 | 完整 pipeline rerun (md_atoms + coverage_ledger + p4b) | 留 v1.4 | ⏸ deferred |

**A5 verdict**: PARTIAL — 满足 v1.3 release scope (备份 + 文档化), 完整 rerun 留 v1.4.

## 8. Carry status

- 06 retro §二 6: **PARTIALLY RESOLVED** — baseline 备份 + 文档化, 完整 rerun v1.4
- PLAN.md A5 Gate: 修订为 PARTIAL (rationale ref § 2-3 实际依赖分析)
