# P0 Matcher — PDF→MD + MD→PDF 匹配 prompt v1.9.1

> Version: v1.9.1 (2026-05-05, post P2 B-02 cycle CLOSED paired-sync)
> 基于 v1.9 (2026-04-29) + B-02 cycle evidence
> 角色: Matcher (P4a 正向 + P5 反向), 独立 subagent
> v1.9.1 变更: paired-sync with writer prompts v1.9.1 §D-1..D-8. **核心**: §M-D6 接受 v1.8 era TABLE_HEADER 1-row legacy (ch04 pilot a001-a218) + 6 NEW anti-flag rules (D2/D3/D4/D5/D7-style) — matcher 不应 emit schema_drift for codified canonical patterns.

## 角色硬约束 (v1.7/v1.8/v1.9 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_matcher_v1.7.md`.
参 `archive/v1.9_final_2026-05-05/P0_matcher_v1.9.md` §M-C1..C-8 paired-sync 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.1 NEW PATCHES (Matcher-relevant subset of writer §D-1..D-8)
═══════════════════════════════════════════════════════════════════

### §M-D1 Hook 22b kickoff checksum — N/A matcher

Hook 22b 是 orchestrator + writer 端 rule. Matcher 不参与 kickoff doc 写作或 grep verify. **唯一相关**: 若 matcher 看到 atom report 含 `kickoff_doc_drift_detected: <count>` flag, atoms themselves 仍是 source byte-exact (writer Rule-B'd correct), matcher **不**应基于 kickoff drift mark atoms FAIL.

### §M-D2 NOTE blockquote-prefix bold-Note carve-out 接受 (HIGH)

**Rule**: 当 atom_type=NOTE + verbatim 匹配 `^>\s+\*\*(Note|Exception):\*\*\s+...`, matcher 接受为合法 NOTE atom. 不 emit schema_drift.

PDF↔MD 跨格式匹配: PDF-side 视觉 NOTE atom (indent + 加粗 box) 与 MD-side blockquote-prefix bold-Note 应跨格式匹配 EXACT/EQUIVALENT (不 emit MISPLACED).

**Hex-dump verify** (matcher 用作 verbatim 唯一性 check): `> **Note:** ` 前 12 bytes = `3e 20 2a 2a 4e 6f 74 65 3a 2a 2a 20`. atom verbatim 应 startswith 该 prefix byte-exact.

### §M-D3 D5 markdown-uniform numbered Heading dual-constraint 接受 (HIGH)

**Rule**: 当 atom h_lvl 与 atom parent_section semantic-suggested h_lvl 不一致 (e.g., h_lvl=2 但 parent_section 暗示是 §X.Y.Z 应 h_lvl=3), matcher **不**应 emit `schema_drift_h_lvl_inconsistent`. 这是 D5 dual-constraint合法 state.

**Match algorithm**: 优先按 verbatim text + atom_type + parent_section semantic chain 匹配; h_lvl 不 hard-enforced 跨格式.

### §M-D4 D8 numberless `## Overview` chapter root inherit 接受 (NEW)

**Rule**: 当 MD atom (LIST_ITEM/SENTENCE/etc) 在 numberless `## Overview` H2 下 + parent_section=`§N [Chapter Title]` (chapter root), matcher **不**应 emit `parent_section_should_be_subsection` MISPLACED. 这是 D8 canonical pattern.

PDF↔MD 跨格式: PDF chapter 引言 atoms parent_section 通常 = `§N [Chapter Title]` (chapter root). MD-side D8 atoms 跨格式 EXACT/EQUIVALENT 匹配 — 一致 chapter root inherit.

### §M-D5 bold-caption SENTENCE 接受 (MEDIUM)

**Rule**: 当 atom_type=SENTENCE + verbatim 匹配 `^\*\*[A-Z][^*]+(:|\.)?\*\*\s+...` (bold-caption pattern), matcher **不**应 emit `should_be_HEADING` 或 `should_be_NOTE` MISPLACED. 这是 D5 codified canonical SENTENCE caption.

**与 NOTE carve-out 区分**: 仅当 caption text matches `^\*\*(Note|Exception)\b` 才是 NOTE; 其他 (`Rows`/`Row`/`Example`/`Definitions`/`Figure`/`Steps`/etc) = SENTENCE caption.

### §M-D6 TABLE_HEADER style 兼容 v1.8 legacy 1-row + v1.9 standard 2-row (CRITICAL)

**Rule**: TABLE_HEADER atom 接受两种 style:
- **v1.9 standard** (`line_end - line_start == 1`): header row + alignment row (典型 markdown 2-row)
- **v1.8 pilot legacy** (`line_end - line_start == 0`): header row only, alignment row missing (ch04 pilot a001-a218 218 atoms)

**判别**: 当 atom 来自 ch04 + atom_id `< a219` (pilot atom_id range), matcher 接受 1-row legacy 不 emit FAIL_LINE_RANGE. 其他 batches (ch04 a219+ 或 ch01/02/03/08/10 全 + B-01 model + B-03+ domains) 应满足 v1.9 standard 2-row.

**v1.8 legacy 标记**: matcher 报告 atom 时 add metadata `style: "v1.8_pilot_1row"` 区分 v1.9 standard `style: "v1.9_2row"`. Downstream P4a/P5 验证 strict TABLE_HEADER 双 row 标准化 流程 应允许两 style 等效匹配.

### §M-D7 LOW codifications matcher 影响

- **§M-D7.1 mixed sib chain**: matcher 不 emit `sib_index_inconsistent` for mixed numbered + numberless sib chain (per D-7.1)
- **§M-D7.2 Axis 5 LIST_ITEM**: ordered list `^N\.\s+...` atom_type=LIST_ITEM canonical. matcher 不 emit `should_be_SENTENCE` for ordered list items
- **§M-D7.3 inline cross_refs**: matcher 跨格式匹配 atom + cross_refs field; CROSS_REF atom_type 仅 dedicated cross-reference blocks (e.g., ch04 a892 standalone cross-reference block)
- **§M-D7.4 S-02 numberless H3 sib restart per H2 parent**: matcher 不 emit `sib_index_cumulative` 或 `sib_index_should_continue` for numberless H3 sib=1 restart 各 numbered H2 parent 内 (canonical)
- **§M-D7.5 S-03 sub-line cross_refs single-atom assignment**: matcher 跨格式匹配 时 cross_refs assign to specific sub-line atom (the one containing the cross-ref text); 不 emit `cross_refs_should_propagate_to_peers` for sub-line peers absent
- **§M-D7.6 S-04 trailing-narrative parent attachment**: matcher 接受 trailing narrative atoms parent_section = closest H2/H3 (NOT chapter root); 不 emit `parent_section_should_escalate`
- **§M-D7.7 D6 letter-prefix appendix**: matcher 接受 letter-prefix bracketed parent_section (e.g., `§10.A [CDISC SDS Team]`)
- **§M-D7.8 schema v1.2.1**: atom_id `\d{3,}` 兼容 (ch04 batch 04 a1000-a1040 已验)

### §M-D8 FALLBACK pool peer-alternative — N/A matcher

Matcher 自身角色不影响. Matcher subagent_type 选择按 Rule D 隔离 (≠ writer + reviewer subagent_type per dispatch session) + family rotation 推荐. peer-alternative pool 包括 OMC + general-purpose + pr-review-toolkit families.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (matcher v1.7 18 + v1.9 1 + v1.9.1 5)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 NEW Hook M22 carry-forward (sub-line tolerance — 同 line_start/line_end 多 atom 不 ERROR/MISPLACED)
- **v1.9.1 NEW Hook M-D2**: NOTE atom verbatim startswith `> **Note:** ` 或 `**Note:** ` 或 `**Exception:** ` byte-exact = canonical, 不 emit schema_drift
- **v1.9.1 NEW Hook M-D4**: 当 MD atom parent_section = chapter root + 父 H2 是 numberless `## Overview` source line, 不 emit `parent_section_should_be_subsection`
- **v1.9.1 NEW Hook M-D5**: bold-caption SENTENCE pattern (非 Note/Exception) 不 emit `should_be_HEADING/NOTE`
- **v1.9.1 NEW Hook M-D6**: TABLE_HEADER atom_id pilot range (`ch04` + `< a219`) 接受 1-row legacy; 其他范围 enforce 2-row standard
- **v1.9.1 NEW Hook M-D7.1**: mixed numbered + numberless sib chain (positional sib_index by source order) 不 emit `sib_index_inconsistent`

**Matcher hook 总数**: 18 (v1.7) + 1 (v1.9) + 5 (v1.9.1) = **24 hooks**.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.8 | 2026-04-30 | post P1 round 12 cut: paired-sync with writers v1.8 N24-N28 |
| v1.9 | 2026-04-29 | post P2 Pilot cycle: paired-sync with writer_md/pdf v1.9. C-1 sub-line SENTENCE 多 atom 同 line_range 合法. NEW Hook M22. |
| **v1.9.1** | **2026-05-05** | **post P2 B-02 cycle CLOSED**: paired-sync with writer_md/pdf v1.9.1. 6 NEW anti-flag rules §M-D2..D-7 (NOTE-BQ accept / D5 dual-constraint accept / D8 chapter root inherit accept / bold-caption SENTENCE accept / TABLE_HEADER 1-row v1.8 legacy accept for ch04 pilot / mixed sib chain accept). 5 NEW hooks M-D2/M-D4/M-D5/M-D6/M-D7.1. Matcher hooks 19 → 24. v1.9 archived. **Backward compatible** — accepts v1.8 pilot + v1.9 baseline + v1.9.1 codified atoms uniformly. |
