# P0 Reviewer — Rule A + Rule D 审阅 prompt v1.9

> Version: v1.9 (2026-04-29, post P2 Pilot cycle paired-sync)
> 基于 v1.8 (2026-04-30)
> 角色: Reviewer (Rule A 语义抽检 + Rule D 端到端审), 独立 subagent, ≠ writer subagent_type
> v1.9 变更: **核心**: §R-C1 sub-line SENTENCE 不应判 FAIL_VERBATIM (P2 Pilot Attempt 2 教训) + 新增 anti-defect 3 类显式审 + N21 status update.

## 角色硬约束 (v1.7/v1.8 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_reviewer_v1.7.md`.

═══════════════════════════════════════════════════════════════════
## v1.9 NEW PATCHES (Reviewer-relevant subset of writer C-1..C-8)
═══════════════════════════════════════════════════════════════════

### §R-C1 sub-line SENTENCE atomization 不判 FAIL_VERBATIM (HIGH)

**Trigger**: P2 Pilot Attempt 2 Rule A scientist 6/30 = FAIL_VERBATIM 全部为 sub-line interpretation drift (verbatim 是 source line 的 byte-exact substring, 但非 full line content). 主 session 验证 verbatim **IS** byte-exact substring → reclassified as PASS.

**v1.9 Reviewer Rule**:
- verbatim **byte-exact substring of source line** = PASS (即使 verbatim ≠ full line content)
- verbatim **paraphrased / 含 source 不存在 char** = FAIL_VERBATIM
- 多 atom 同 line_start/line_end 不同 verbatim **不**是 ERROR (C-1 合法状态)

**判定算法**:
```
function check_verbatim(atom, source_file):
    line = source_file[atom.line_start : atom.line_end+1]
    if atom.verbatim in line.text (substring match exact):
        return PASS
    elif atom.verbatim is paraphrase or contains chars not in line:
        return FAIL_VERBATIM
    elif atom.verbatim is byte-exact full line: 
        return PASS  // 老 atomization 风格
    else:
        return PARTIAL  // 如有空白 normalization 之类
```

### §R-C2 N21 all-side ban — reviewer 自身角色

Reviewer 自身不写 atoms (审而不写). N21 ban scope 是 writer 角色; reviewer 角色继续按 sub-plan §A.2 step 6 用 `oh-my-claudecode:scientist` / `oh-my-claudecode:code-reviewer` / `critic` 等 reviewer-family.

### §R-C3..C-7 anti-defect 显式审 (P2 Pilot Attempt 1 教训)

Reviewer 必查:
1. **TABLE_HEADER line_end - line_start ≤ 1** (C-5) → 越界 = FAIL_LINE_RANGE
2. **HEADING source line `^#{1,6}\s+`** (C-6) → bold `**foo**` source 但 atom_type=HEADING = FAIL_ATOM_TYPE
3. **LIST_ITEM verbatim startswith `^(\-|\*|\d+\.)\s+`** (C-7) → 缺 prefix 或截断 = FAIL_VERBATIM 或 PARTIAL
4. **slice scope last atom line_end ≥ slice_end - 5** (C-3 + Hook 22) → shortfall = COVERAGE_FAIL
5. **file field full path `knowledge_base/...`** (C-8) → 缺 prefix = FAIL_SCHEMA

### §R-Stratified-Sampling 调整

P2 Pilot evidence: 30-atom 分层样本足以 caught Writer B 3 类系统缺陷 (sample n=30 enough for 100% defect rate detection on 13/13 TABLE_HEADER class). 维持 30-atom 标准.

**新增**: 当 PASS rate ∈ [70%, 90%) 且 fail 集中 1 类 (单一 atom_type 或单一 defect class), reviewer **必须**在 summary 显式声明:
- defect 是 systematic vs random
- 是否 interpretation drift (主 session 应直接验证 vs 重派 attempt)

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (reviewer 自身 review-checklist v1.7 + 2 NEW v1.9)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- **v1.9 NEW Hook R22**: sub-line SENTENCE 同 line_start/line_end 不同 verbatim 不判 ERROR/MISPLACED
- **v1.9 NEW Hook R23**: defect 集中 1 类时 explicit interpretation-vs-defect 声明

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.8 | 2026-04-30 | post P1 round 12 cut: paired-sync with writers v1.8 |
| **v1.9** | **2026-04-29** | **post P2 Pilot cycle**: paired-sync with writer_md/pdf/matcher v1.9. **§R-C1**: sub-line SENTENCE 不判 FAIL_VERBATIM (P2 Pilot Attempt 2 scientist 80% 教训; reclassify rule). §R-C3..C-7 anti-defect 显式审 (TABLE_HEADER overflow / bold-as-HEADING / LIST_ITEM truncation / slice shortfall / path inconsistency). NEW Hooks R22 + R23. v1.8 archived. |
