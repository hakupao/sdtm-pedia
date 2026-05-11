# P0 Reviewer — Rule A + Rule D 审阅 prompt v1.9.1

> Version: v1.9.1 (2026-05-05, post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT 30/30 = 100% strict PASS)
> 基于 v1.9 (2026-04-29) + B-02 cycle evidence
> 角色: Reviewer (Rule A 语义抽检 + Rule D 端到端审), 独立 subagent, ≠ writer subagent_type
> v1.9.1 变更: paired-sync with writer + matcher v1.9.1 §D-1..D-8. **核心**: 6 NEW anti-flag rules — reviewer 不应 emit FAIL for codified canonical patterns + 1 CRITICAL kickoff drift handling rule (verify writer Rule-B'd correctly, 不 fault writer for kickoff doc drift).

## 角色硬约束 (v1.7/v1.8/v1.9 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_reviewer_v1.7.md`.
参 `archive/v1.9_final_2026-05-05/P0_reviewer_v1.9.md` §R-C1..C-7 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.1 NEW PATCHES (Reviewer-relevant subset of writer §D-1..D-8)
═══════════════════════════════════════════════════════════════════

### §R-D1 Hook 22b kickoff drift handling — verify writer Rule-B'd correctly (CRITICAL)

**Background**: B-02 batch 06/07/08 3 连续 kickoff doc drift (L117 typo / "5 表" arithmetic / 62→61 fragment rows). Writer correctly Rule-B'd preserve source byte-exact 每次. Reviewer 应 distinguish "kickoff doc drift" (orchestrator-side) vs "writer atom error" (writer-side).

**Reviewer rule**:
1. atom verbatim 与 source byte-exact match = PASS (即使 与 kickoff §2.2 numeric claim 不一致)
2. 当 batch report 含 `kickoff_doc_drift_detected: <count>` flag, reviewer **不**应 mark atoms FAIL based on kickoff drift; verify atoms vs source 是真权威
3. Reviewer 在 summary 含独立段 `Kickoff drift verification`:
   - 若 batch report flag 表示 kickoff drift, reviewer 独立 grep verify source 一致 writer atoms
   - 若 reviewer发现 writer atoms 与 source mismatch (writer fabricated to match kickoff), 这是 HIGH severity defect (违反 Rule B)
   - 若 reviewer发现 kickoff drift 但 writer atoms 与 source 一致, INFO log 不 fault writer

**Hook R24** NEW: kickoff drift report routing — kickoff doc drift instances 应 route 到 orchestrator (主 session) batch-level report, NOT writer-level FAIL.

### §R-D2 D7 NOTE blockquote-prefix bold-Note 接受 (HIGH)

**Rule**: 当 atom_type=NOTE + verbatim startswith `> **Note:** ` 或 `> **Exception:** ` byte-exact (12-byte hex prefix `3e 20 2a 2a 4e 6f 74 65 3a 2a 2a 20` for Note variant), reviewer **接受**为 canonical. 不 emit FAIL_ATOM_TYPE.

**Hex-dump verify** (mandatory for D7 instances): reviewer Bash 用 `od -c` 或 `xxd` 跨 atom verbatim 验证 byte-exact prefix. Trailing space byte (`0x20`) 不允许 dropped.

### §R-D3 D5 markdown-uniform numbered Heading dual-constraint 接受 (HIGH)

**Rule**: 当 atom h_lvl 与 atom parent_section semantic-suggested h_lvl 不一致 (e.g., source `## 3.2.2 Conformance` h_lvl=2 但 semantic 应 §3.2 sub of §3 h_lvl=3), reviewer **接受**为 D5 dual-constraint canonical. 不 emit FAIL_H_LVL.

**Verify**: reviewer 独立 read source 该 line, 验证 h_lvl 是 source byte-exact (Rule B); parent_section 是 semantic-correct (sib chain 中 logical parent).

### §R-D4 D8 numberless `## Overview` chapter root inherit 接受 (NEW)

**Rule**: 当 children atoms (LIST_ITEM/SENTENCE/etc) parent_section = chapter root (`§N [Chapter Title]`) 且 source structure 父 H2 是 numberless `## Overview`, reviewer **接受**为 canonical. 不 emit `parent_section_should_be_subsection`.

**Verify**: reviewer read source 该 atom 所在 H2 source line, 验证 是 numberless `## Overview` (无 numbering prefix). 若 是 numbered `## N.0 Overview`, reviewer enforce sub-namespace `§N.0 [Overview]` (D8 仅 apply to numberless variant).

### §R-D5 bold-caption SENTENCE 接受 (MEDIUM)

**Rule**: 当 atom_type=SENTENCE + verbatim 匹配 `^\*\*[A-Z][^*]+(:|\.)\*\*\s+...` (bold-caption pattern, non-Note/Exception) 或 `**Figure ...**` / `**Steps:**` / etc, reviewer **接受**为 canonical SENTENCE caption. 不 emit `should_be_HEADING` 或 `should_be_NOTE`.

**与 NOTE carve-out 严格区分**:
- NOTE 仅当 caption text 是 `Note` 或 `Exception` 字面: `^\*\*(Note|Exception)\b` 或 `^>\s+\*\*(Note|Exception)\b`
- 其他 (`Rows`/`Row`/`Example`/`Definitions`/`Figure`/`Steps`/`Where:`/etc) = SENTENCE

### §R-D6 TABLE_HEADER style 兼容 v1.8 pilot legacy 1-row 接受 (CRITICAL anti-flag)

**Rule**: TABLE_HEADER atom 接受两种 style:
- v1.9 standard: `line_end - line_start == 1` (header + alignment row)
- v1.8 pilot legacy: `line_end - line_start == 0` (header row only, ch04 atom_id < a219)

**判别**: 当 atom 来自 ch04 + atom_id `< a219` (pilot atom_id range), reviewer **不**应 emit FAIL_LINE_RANGE for `line_end - line_start == 0`. 其他范围 (ch04 a219+ 或 B-01 model 或 B-02 chapters/ ch01/02/03/08/10 或 B-03+ domains) 应满足 v1.9 standard 2-row, 否则 FAIL_LINE_RANGE.

**Reviewer 在 summary 显式声明 style 分类**: e.g., `30 atoms sampled: 18 v1.9 standard 2-row + 12 v1.8 pilot 1-row legacy (ch04 a001-a218); 0 FAIL_LINE_RANGE post-classification`.

### §R-D7 LOW codifications reviewer 影响

- **§R-D7.1 mixed sib chain**: reviewer 接受 mixed numbered + numberless H3 sib chain positional sib_index. 不 emit `sib_index_should_be_X`
- **§R-D7.2 Axis 5 LIST_ITEM 接受**: ordered list `^N\.\s+` atom_type=LIST_ITEM canonical
- **§R-D7.3 cross_refs field 接受**: inline cross-reference (e.g., `(see §X.Y)`) 在 atom 的 `cross_refs` field; 不需要单独 CROSS_REF atom
- **§R-D7.4 numberless H3 sib restart per H2**: 各 H2 parent 内 H3 sib=1 restart canonical
- **§R-D7.5 sub-line cross_refs 单 atom 归属**: cross_refs assign to specific sub-line atom, not all peers
- **§R-D7.6 trailing-narrative parent attachment**: 接受 inherit closest H2/H3 parent_section (NOT escalate chapter root)
- **§R-D7.7 D6 letter-prefix appendix-style H2**: 接受 `§10.A [...]` bracketed parent_section
- **§R-D7.8 schema v1.2.1 atom_id `\d{3,}`**: 接受 atom_id ≥ 1000 padded
- **§R-D7.13 writer DONE >999 atom_id**: 接受 writer 报告 N atoms ≥ 1000

### §R-D8 FALLBACK pool peer-alternative — reviewer 自身 status

Reviewer subagent_type 选择 peer-alternative pool (per writer v1.9.1 §D-8):
- OMC reviewer family preferred (scientist/code-reviewer/critic)
- pr-review-toolkit:code-reviewer peer-alternative (B-02 sustained 7-batch 100% PASS empirical)
- feature-dev:code-reviewer peer-alternative for cumulative inter-cycle audit
- Rule D 隔离硬约束 unchanged: reviewer subagent_type ≠ writer subagent_type per batch

### §R-Stratified-Sampling 调整 (v1.9.1)

- 维持 30-atom inter-cycle stratified standard (B-01 + B-02 evidence)
- per-batch Rule A audit 维持 8 boundary + 3-7 stratified = 11-16 verdict rows
- **NEW (v1.9.1 +)**: 当 batch 含 D-codified anomaly 实例 (NOTE-BQ / D5 dual-constraint / D8 chapter-root / bold-caption SENTENCE / mixed sib chain), reviewer 应 stratified sample include ≥1 anomaly instance verify byte-exact preservation + canonical pattern adherence

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (reviewer v1.7 18 + v1.9 2 + v1.9.1 6)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 NEW Hook R22 carry-forward (sub-line SENTENCE 同 line_range 多 atom 不 ERROR/MISPLACED)
- v1.9 NEW Hook R23 carry-forward (defect 集中 1 类时 explicit interpretation-vs-defect 声明)
- **v1.9.1 NEW Hook R24**: kickoff drift report routing — kickoff doc drift instances route 到 orchestrator level, NOT writer FAIL
- **v1.9.1 NEW Hook R-D2**: NOTE atom hex-dump verify byte-exact prefix `> **Note:** ` 或 `**Note:** ` (mandatory for D7 instances)
- **v1.9.1 NEW Hook R-D3**: D5 dual-constraint h_lvl/parent_section divergence 接受 (verify h_lvl byte-exact source + parent_section semantic-correct)
- **v1.9.1 NEW Hook R-D4**: D8 chapter root inherit 接受 (verify 父 H2 是 numberless `## Overview` source line)
- **v1.9.1 NEW Hook R-D5**: bold-caption SENTENCE 接受 (非 Note/Exception caption ≠ HEADING/NOTE)
- **v1.9.1 NEW Hook R-D6**: TABLE_HEADER pilot legacy 1-row 接受 for ch04 atom_id < a219 (style 显式分类 in summary)

**Reviewer hook 总数**: 18 (v1.7) + 2 (v1.9) + 6 (v1.9.1) = **26 hooks**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.1 sync with B-02 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **30-atom inter-cycle stratified standard**: SUSTAINED status (B-01 28/30 = 93.3% + B-02 30/30 = 100% = 2 cumulative cycles validated)
- **B-02 cycle 100% strict PASS**: NEW STATUS — 0 HIGH/MEDIUM/LOW NEW findings post 30-atom cumulative audit; preventive layers (Hook A4 + D5/D6/D7/D8 codify + CRITICAL kickoff self-consistency rule) effectively prevented systemic drift
- **Rule D 隔离硬约束 STRONGLY VALIDATED EXTENDED**: B-01 + B-02 13 batches sustained writer ≠ reviewer subagent_type 0 violation
- **FALLBACK reviewer pool peer-alternative**: NEW STATUS (pr-review-toolkit:code-reviewer + feature-dev:code-reviewer 等同 OMC reviewer-family priority)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.8 | 2026-04-30 | post P1 round 12 cut: paired-sync with writers v1.8 |
| v1.9 | 2026-04-29 | post P2 Pilot cycle: §R-C1 sub-line SENTENCE 不判 FAIL_VERBATIM. §R-C3..C-7 anti-defect 显式审. NEW Hooks R22 + R23. |
| **v1.9.1** | **2026-05-05** | **post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT**: paired-sync with writer_md/pdf/matcher v1.9.1. 7 NEW anti-flag/handling rules §R-D1..D-8 (kickoff drift handling CRITICAL / NOTE-BQ accept HIGH / D5 dual-constraint accept HIGH / D8 chapter root inherit accept NEW / bold-caption SENTENCE accept MEDIUM / TABLE_HEADER 1-row pilot legacy accept CRITICAL anti-flag / LOW group consolidated). 6 NEW hooks R24/R-D2/R-D3/R-D4/R-D5/R-D6. Reviewer hooks 20 → 26. v1.9 archived. **Backward compatible** — handles v1.8 pilot + v1.9 baseline + v1.9.1 codified atoms uniformly. |
