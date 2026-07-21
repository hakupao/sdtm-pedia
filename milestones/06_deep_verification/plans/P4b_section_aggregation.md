<!-- chain: F (深度验证旁枝链 v2)
  修改本文件后, 必须检查:
  → ../_progress.json                       (phases.P4b_section_aggregation 字段)
  → ../evidence/checkpoints/                (P4b 产物快照)
  → ../PLAN.md §5                           (phase 状态更新)
  → ../audit_matrix.md                      (P4b section 新增)
  → ../trace.jsonl                          (phase_report 追加)
-->

# P4b — Section 聚合 Sub-Plan

> Version: **v1.0 (2026-05-12, post P4a gate ALL PASS)**
> 父 PLAN: `branches/06_deep_verification/PLAN.md` v0.6
> 前置: P4a ✅ ALL PASS (coverage_ledger.jsonl 12,487 条 forward entries)
> 目标: 按 HEADING 树归并, 产 `section_coverage.jsonl`, 检测三类失效
> Tier 3 (高 stakes) / 预估 **0.5 session**
> 脚本: `scripts/p4b_section_aggregate.py`

---

## 0. 输入 / 输出契约

| 项 | 值 |
|---|---|
| 输入 1 | `coverage_ledger.jsonl` (12,487 行 forward verdicts from P4a) |
| 输入 2 | `pdf_atoms.jsonl` (12,487 atoms; HEADING 876 个含 heading_level + sibling_index) |
| 输入 3 | `md_atoms.jsonl` (10,435 atoms; file 字段用于 md_target_files) |
| 主产物 | `section_coverage.jsonl` (一行/section) |
| 格式 | 父 PLAN §4.5 `section_coverage.jsonl` schema |
| 消费方 | P6 Triage + Repair 读 section_coverage 找高风险节 |

---

## 1. 数据概况 (P4a 实测)

| 指标 | 值 |
|---|---|
| 总 PDF 原子数 | 12,487 |
| HEADING 原子数 | 876 (7.0%) |
| 唯一 parent_section 值 (section 数) | 399 (398 distinct + 1 sv20 overlap §0 [Cover]) |
| ig34 sections | 340 |
| sv20 sections | 59 (SDTM v2.0; systematic low coverage, KB built from ig34) |
| coverage_ledger 有效行 | 12,476 (11 atoms not in ledger → default MISSING) |

**Section 格式分布**:

| 格式 | 数量 | 示例 |
|---|---|---|
| §-numbered | 356 | `§4.2.7 [Submitting Free Text]` |
| Domain (X – Y) | 87 | `FA – Assumptions`, `SR – Examples` |
| Other (Appendix/Cover) | 10 | `Appendix A: CDISC SDS Team` |

---

## 2. 聚合算法 (实现: scripts/p4b_section_aggregate.py)

### 2.1 Grouping

- Key = (source, parent_section): source 由 atom_id 前缀判定 (sv20_ / ig34_)
- sv20/ig34 各自独立成组 (防 §0 [Cover] 混合)

### 2.2 Per-section 统计

```
pdf_atom_count    = |content_atoms| (non-HEADING)
matched           = EXACT + EQUIVALENT verdicts
partial           = PARTIAL verdicts
coverage_density  = matched / pdf_atom_count  (None if pdf_atom_count=0)
misplaced_rate    = MISPLACED / pdf_atom_count
```

### 2.3 Child Sections (仅 §-numbered)

- 按 section number 层级寻找直接子节 (parent_num + "." + one level suffix)
- 子节状态: MATCHED (density ≥ 0.80) | CONTENT_TRUNCATED (0.20-0.80) | SKELETON_ONLY (<0.20) | MISSING (pdf_atom_count=0)

### 2.4 HEADING_MISSING 检测

- 对 §X.Y.Z 节: 在父节 §X.Y 的 HEADING 原子中匹配 verbatim = 本节 title
- 若该 HEADING 原子 verdict = MISSING → heading_missing_detected = true

### 2.5 Keyword 检测 (Level 1 / Level 2)

- MISSING 原子 verbatim 扫描 shall/must/required 等 → keyword_flag = "level1"
- MOSTLY_COMPLETE + level1 keyword → 强制 CONTENT_TRUNCATED 升级 (父 PLAN v0.4 NF-2)

### 2.6 aggregate_verdict 优先级 (来自父 PLAN §4.5)

```
STRUCTURE_DRIFTED > HEADING_MISSING > SKELETON_ONLY > SIBLING_DROPPED >
CONTENT_TRUNCATED > MOSTLY_COMPLETE > FULL_COVERAGE
```

---

## 3. 脚本输出 (2026-05-12 实测)

```
Total sections: 399
```

| aggregate_verdict | Count | % |
|---|---|---|
| FULL_COVERAGE | 101 | 25.3% |
| MOSTLY_COMPLETE | 42 | 10.5% |
| CONTENT_TRUNCATED | 110 | 27.6% |
| SIBLING_DROPPED | 56 | 14.0% |
| SKELETON_ONLY | 67 | 16.8% |
| STRUCTURE_DRIFTED | 23 | 5.8% |
| HEADING_MISSING | 0 | 0% |

**Failure pattern counts** (section 可多 pattern):

| Pattern | Count |
|---|---|
| CONTENT_TRUNCATED | 132 |
| SKELETON_ONLY | 80 |
| SIBLING_DROPPED | 76 |
| STRUCTURE_DRIFTED | 23 |

**Key counts**:
- SKELETON_ONLY sections: 67 (need triage)
- STRUCTURE_DRIFTED sections: 23 (≥10% MISPLACED)
- Level-1 keyword flag (shall/must in MISSING atoms): 43 sections
- HEADING_MISSING: 0 (all PDF section headings found in KB)

---

## 4. SKELETON_ONLY Triage (67 sections)

| Category | Count | Disposition |
|---|---|---|
| sv20 (SDTM v2.0 doc, KB built from ig34) | 20 | INTENTIONAL_EXCLUDE: `SDTM_V2_SYSTEMATIC_GAP` |
| EDITORIAL_META (§0 Cover, TOC) | 3 | INTENTIONAL_EXCLUDE: `EDITORIAL_META` |
| Domain "Specification" / "Description/Overview" stubs | 20 | INTENTIONAL_EXCLUDE: `REDUNDANT_WITH_SPEC` (out-of-scope per PLAN §0.2) |
| Small stubs (≤2 content atoms) | 6 | Low-priority, likely stub sections |
| **NEEDS INVESTIGATION (ig34, ≥3 atoms)** | **20** | → P6 Triage, open Issues |

**Top ig34 SKELETON_ONLY needing P6 investigation**:

| Section | Atoms | Density | Priority |
|---|---|---|---|
| §6.3.5.9.3 — Example 2/3/4 (each) | 50/84/88 | 0.0 | HIGH |
| §6.3.5.7.1 Microbiology Specimen (MB) | 89 | 0.169 | HIGH |
| §5 [General Observation Classes] | 28 | 0.0 | HIGH |
| §6.3.10 Subject Characteristics (SC) | 28 | 0.036 | HIGH |
| §6.4.1 When to Use Findings About Events | 25 | 0.0 | MEDIUM |
| §3.1.3 The Findings Observation Class | 101 | 0.218 | MEDIUM |
| Appendix A: CDISC SDS Team | 78 | 0.026 | LOW (team list, INTENTIONAL_EXCLUDE) |
| §7.1.x Trial Design concepts | ~15 each | 0-0.05 | MEDIUM |
| §8.6.2 Guidelines for Forming New Domains | 11 | 0.0 | MEDIUM |
| §4.4.4 Use of Study Day Variables | 11 | 0.091 | MEDIUM |

---

## 5. Exit Gate (P4b)

来自父 PLAN §5 + §9.1 P4b 行:

| Gate 条件 | 阈值 | 状态 |
|---|---|---|
| 每 PDF 节有 aggregate_verdict | 100% | ✅ (399/399) |
| 0 节 SKELETON_ONLY 未在白名单或 Issue | 0 未登记 | ⚠️ pending triage |
| 0 节 SKELETON_ONLY 未登记解释 | 0 | pending |
| Rule A 30-section 审查 | ≥95% 一致率 | 🔄 reviewer running |
| STRUCTURE_DRIFTED 节全有 Issue 或解释 | 23 sections | pending P6 |
| trace.jsonl P4b phase_report ≥1 | ≥1 | pending |

---

## 6. Writer / Reviewer 分配

P4b 为脚本主导 (0.5 session), 主 session 作 aggregator.

| Slot | Type | Role | 状态 |
|---|---|---|---|
| P4b-R1 | `oh-my-claudecode:scientist` | Rule A 30-section 独审 | 🔄 running (2026-05-12) |

P4b gate reviewer = `oh-my-claudecode:scientist` (项目首次用于 P4b; P4a-R1 预定 slot).

---

## 7. 下一步 (P4b → P6)

P4b 完成后:
1. **Rule A reviewer 结果** → 若 ≥95% 一致 → gate PASS
2. **SKELETON_ONLY 白名单** → 20 sv20 + 3 editorial + 20 domain spec → INTENTIONAL_EXCLUDE 登记
3. **真实缺口** → P6 Triage: 开 Issues 5+ for SKELETON_ONLY + STRUCTURE_DRIFTED
4. **P5 反向匹配** → 可与 P6 Triage 并行

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-05-12 | Initial, post P4a gate ALL PASS. Script run complete, reviewer dispatched. |
