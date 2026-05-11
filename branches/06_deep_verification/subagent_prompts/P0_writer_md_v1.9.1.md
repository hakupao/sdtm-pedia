# P0 Writer MD — 原子化 prompt v1.9.1

> Version: v1.9.1 (2026-05-05, post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT 30/30 = 100% strict PASS)
> Cut trigger: B-02 9 batches CLOSED, 19 candidate codifications backlog (1 CRITICAL + 2 HIGH + 2 MEDIUM + 1 NEW + 13 LOW); FALLBACK path sustained 7 batches 1,331 atoms 0 writer defect; 3 连续 batch 06/07/08 kickoff drift DEFUSED at batch 09 INAUGURAL clean
> 基于 v1.9 (2026-04-29) + B-02 cycle evidence (`evidence/checkpoints/cumulative_audit_post_B02.md` + `multi_session/P2_B-02_RETROSPECTIVE.md`)
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.9.1 变更 over v1.9: 8 NEW D-rules (D-1..D-8) consolidating 19 candidate stack. **Backward compatible** with v1.9 atoms (ch04 pilot a001-a218 v1.8-style + B-01/B-02 v1.9-style). v1.9 archived `archive/v1.9_final_2026-05-05/`.

## 角色硬约束 (v1.7/v1.8/v1.9 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` §角色硬约束 全文.
参 `archive/v1.9_final_2026-05-05/P0_writer_md_v1.9.md` §C-1..C-8 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.1 NEW PATCHES (D-1..D-8, B-02 cycle 实证驱动)
═══════════════════════════════════════════════════════════════════

### §D-1 Hook 22b NEW pre-DONE kickoff numeric claim grep checksum (CRITICAL)

**Background**: B-02 batch 06/07/08 3 连续 kickoff doc internal arithmetic drift (L117 `### 3.2.2` typo 实际 source `## 3.2.2` h_lvl=2 / "5 表" arithmetic 实际 4 表 / "62 fragment rows" off-by-one 实际 61). Writer correctly Rule-B'd preserve source byte-exact 每次, 但浪费 dispatch + Rule A grading 周期. Batch 09 kickoff §0.5 grep checksum 11/11 verified → INAUGURAL clean实战.

**Orchestrator rule (kickoff doc writer = main session)**: kickoff §0.5 (NEW MANDATORY block) "kickoff numeric claim grep checksum" — 写 kickoff 时, 任何 numeric claim 必须 grep-verified against source byte-exact:

```
### §0.5 Kickoff numeric claim grep checksum (MANDATORY for B-03+ kickoffs)

| Claim | Source verify command | Match? |
|---|---|---|
| ch08 = 439 lines | `wc -l knowledge_base/chapters/ch08_relationships.md` | ✓ 439 |
| 9 H2 headers | `grep -c "^## " ch08` | ✓ 9 |
| 19 H3 headers | `grep -c "^### " ch08` | ✓ 19 |
| 17 bold-caption | `grep -cE "^\*\*[A-Z][^*]*\*\*" ch08` | ✓ 17 |
| ... | ... | ✓ |
```

未通过 checksum 的 numeric claim 必须修正 OR 删除 OR 标 `(estimated)`.

**Hook 22b for writer (pre-DONE pattern check)**: 当 kickoff §2.2 含 "kickoff §0.5 verified N/M=100% byte-exact" 声明, writer 信任 kickoff numeric claims 用作 boundary detection. 当 kickoff §0.5 absent or partial, writer 须独立 grep-verify boundary numeric claims (e.g., total atom count 估, H2 count) against source 自己 — 不靠 kickoff `(estimated)` numbers 做 hard halt decisions.

**Rule B precedence**: source 永远 trump kickoff. Writer 永不 fabricate match — 即使 kickoff 与 source 不一致, emit source byte-exact + 在 batch report flag `kickoff_doc_drift_detected: <count>`.

**B-03 entry**: 所有 B-03+ kickoff template 强制 §0.5 checksum block, 每 kickoff 须含; 缺 §0.5 = orchestrator preflight FAIL.

### §D-2 D7 NEW NOTE blockquote-prefix bold-Note carve-out extension (HIGH)

**v1.9 NOTE carve-out** (源 inline `^**Note:**` / `^**Exception:**`) **扩到** blockquote variant `^>\s+\*\*(Note|Exception):\*\*\s+...`.

**Rule**: 当 markdown 行匹配 `^>\s+\*\*(Note|Exception):\*\*\s+...`, atom_type=**NOTE** (NOT SENTENCE, NOT TABLE_ROW). verbatim 含 `> ` blockquote prefix + `**Note:**` 或 `**Exception:**` bold markers byte-exact.

**例**: ch08 L389 `> **Note:** BE, BS, and RELSPEC are not...`

emit:
- aN NOTE line 389 verbatim=`> **Note:** BE, BS, and RELSPEC are not subject to the SUPP-- model.`

12-byte prefix hex: `3e 20 2a 2a 4e 6f 74 65 3a 2a 2a 20` (`> **Note:** `).

**触发**: B-02 batch 09 ch08 L389 D7 NEW codify (1 实例首现 chapter-files). 模式 likely 在 domains/ B-03 cycle 出现 multiple instances.

**Reviewer 注意**: hex-dump verify byte-exact `>` + space + `**` + Note/Exception + `:` + `**` + space prefix; 不允许任何 bold marker missing 或 trailing space dropped.

### §D-3 D5 markdown-uniform numbered Heading dual-constraint (HIGH)

**Rule**: 当 markdown source 中数字 numbering 与文档 semantic hierarchy 不一致 (e.g., source `## 3.2.2 Conformance` h_lvl=2, semantic 应是 §3.2 sub of §3 — markdown markup 与 semantic chain 错开 1 层), 应 dual-constraint emit:

- `h_lvl` = source markdown 实际 byte-exact (`## 3.2.2` → h_lvl=2, NOT 3; 不修正)
- `parent_section` = semantic parent — 按 source 出现位置在 chain 中的 logical parent (`§3.2 [Submitting Data]` 或 chapter root 视 source structure 而定)

**Children atoms**: parent_section follow same logical chain — children of `## 3.2.2` (h_lvl=2 但 semantic §3.2.2) inherit closest semantic-correct H2 parent (e.g., `§3.2 [...]`).

**触发**: B-02 batch 06 ch03 L117 — kickoff doc 误标 h_lvl=3 (`### 3.2.2`), 实际 source `## 3.2.2 Conformance`. Writer Rule-B 强制 emit h_lvl=2 + dual-constraint parent_section.

**KB cleanup deferred (LOW per §D-7.9)**: ch03 L117 source MD 一致化 (`## 3.2.2` → `### 3.2.2`) 推荐 source-side fix (NOT writer 行为). Defer to B-04 source curation pass.

### §D-4 D8 NEW numberless `## Overview` H2 chapter root inherit (NEW)

**Rule**: 当 markdown 含 numberless `## Overview` H2 (前置 chapter narrative section, 不是 numbered §N.0), it shares **sib chain** with numbered H2 in same chapter (positional sib_index by source order; numberless `## Overview` sib=1, numbered §N.1 sib=2, ..., §N.K sib=K+1).

**Children atoms** (LIST_ITEM/SENTENCE/TABLE_*/NOTE/etc) under `## Overview` inherit **chapter root** parent_section (`§N [Chapter Title]`), NOT sub-namespace `§N.0 [Overview]` 或 `§N.Overview [Overview]`.

**例**: ch08 L5 `## Overview` (sib=1) 与 numbered §8.1-§8.8 (sib=2..9) 共 sib chain. L5 children L7/L9-16/L18/L20-22 emit:
- parent_section=`§8 [Representing Relationships and Data]` (chapter root inherit)
- NOT `§8.0 [Overview]` (non-canonical N27 per pilot F-P2P-002)

**触发**: pilot F-P2P-002 实证 sub-namespace `§N.0 [Overview]` 是 N27 non-canonical convention (P2 Pilot v2 修正 ch04 a001-a218 已 applied). B-02 batch 09 ch08 D8 INAUGURAL standalone codify post-pilot.

**Edge case**: 当 chapter 含 numbered `## N.0 Overview` (有 number 显式), 沿用普通 numbered H2 模式 — children inherit `§N.0 [Overview]` sub-namespace. D8 仅 apply to numberless `## Overview` (无 number prefix).

### §D-5 bold-caption SENTENCE retention rule formal codify (MEDIUM)

**Rule**: bold-caption 模式 atom_type=**SENTENCE** (NOT NOTE, NOT HEADING):
- `**Rows N-M:**` / `**Row N:**`
- `**Example N:**` / `**Example.**` / `**Example: ...**`
- `**Definitions:**`
- `**Figure N. ...**` / `**Figure.**`
- `**Steps:**` / `**Step N:**`
- 类似 `**[Caption Label]:**` 模式

bold markers `**` preserved verbatim byte-exact.

**与 NOTE carve-out 区分** (§D-2 + v1.9 inline `^**Note:**`):
- **NOTE carve-out**: `^**Note:**` / `^**Exception:**` / `^> **Note:**` / `^> **Exception:**` (semantically separate aside, author 强调 cautionary remark)
- **SENTENCE caption**: `**Rows ...:**` / `**Example ...:**` / `**Definitions:**` / `**Figure ...**` / `**Steps:**` / etc (caption inline w/ paragraph flow, normal narrative reading)

**关键测试**: 若 caption 后面 same line 或后续 paragraph 继续 narrative flow 且无 "this is an aside" semantics → SENTENCE. 若 caption 启动一段 cautionary aside (`Note: WARNING blah`), → NOTE carve-out.

**触发**: B-02 batch 06 codify (`**Definitions:**` `**Example:**`) + validated batches 07/08/09 (17 instances ch08 batch 09). pre-v1.9.1 已 implicit 应用; v1.9.1 显式 codify.

### §D-6 TABLE_HEADER style 兼容 (writer 2-row sustained, matcher 1-row legacy accept) (MEDIUM)

**Writer rule (sustained from v1.9 §C-5)**: TABLE_HEADER atom **应** include header row + alignment row, `line_end - line_start ≤ 1` (典型 2-row markdown table header). v1.9 baseline 不变.

**Backward compat NOTE**: ch04 pilot a001-a218 是 v1.8 prompt era atoms, TABLE_HEADER `line_end == line_start` (single-row, alignment row missing). 不 re-emit (low ROI per G-B02-5).

**Matcher v1.9.1 §M-D6** 显式 accept 两种 style; **Reviewer v1.9.1 §R-D6** 不 emit FAIL_LINE_RANGE for ch04 atom_id < a219 (pilot legacy).

**Writer for B-03+**: 沿用 §C-5 2-row standard. 不 emit single-row TABLE_HEADER.

### §D-7 LOW codifications group (consolidated)

**§D-7.1 mixed sib chain handling** (numbered + numberless H3 共 H2 parent): sib_index 按 source positional order (NOT numbered-only counted index). 例: ch08 §8.4 下 5 H3 chain — §8.4.1 sib=1 + numberless `### Key Rules` sib=2 + §8.4.2 sib=3 + §8.4.3 sib=4 + §8.4.4 sib=5. Children inherit closest H2/H3 parent_section per D8 模式 extension.

**§D-7.2 Axis 5 ordered LIST_ITEM STRONGLY VALIDATED promote**: numbered list `^N\.\s+...` (含 bold-prefix variant `N. **Term.**`) atom_type=**LIST_ITEM** (NOT SENTENCE). pre-v1.9 codify P1 round 14 + B-02 9 batches sustained 0 violation = STRONGLY VALIDATED status. v1.9.1 baseline 不变.

**§D-7.3 S-01 inline cross_ref distinction**: inline cross-reference (e.g., `(see §X.Y)` / `Section 4.1.7`) emit 在 atom 的 `cross_refs` field (附属 atom). CROSS_REF atom_type 仅用作 dedicated cross-reference blocks (e.g., ch04 a892 — first cumulative CROSS_REF atom; "See also: ..." standalone block).

**§D-7.4 S-02 numberless H3 sib chain under numbered H2**: numberless H3 chain 各 numbered H2 parent 内 restart sib=1, NOT 跨 H2 cumulative count. validated 7+ instances batches 05/07/08/09.

**§D-7.5 S-03 sub-line cross_refs placement**: 同 line 含 sub-line SENTENCE atoms 时, cross_refs field assign to specific sub-line atom (the one containing the cross-ref text), NOT all sub-line peers.

**§D-7.6 S-04 trailing-narrative parent attachment**: section 末尾 narrative atoms (post all numbered subsections) 仍 inherit closest H2/H3 parent_section (NOT escalate to chapter root unless source structure 明示 chapter-level narrative).

**§D-7.7 D6 letter-prefix appendix-style H2 chain**: appendix-style H2 (无数字编号, letter prefix) 用 letter-prefix bracketed parent_section 形式 (e.g., `§10.A [CDISC SDS Team]`). H3 chain 各 H2 parent 内 restart sib=1 per S-02.

**§D-7.8 schema v1.2.1 sustained**: atom_id pattern `\d{3,}` (3-or-more digits, 完全向后兼容) sustained 9 batches 0 issue in B-02. v1.9.1 baseline schema = v1.2.1 unchanged. v1.3 promote pending B-04 retro validation 4000+ atoms cumulative.

**§D-7.9 KB cleanup ch03 L117 deferred**: source MD `## 3.2.2 Conformance` → `### 3.2.2 Conformance` 推荐 source-side fix (NOT writer 行为). Defer to B-04 source curation pass.

**§D-7.10 ch04 pilot re-emit deferred**: a001-a218 v1.8 style preserved. matcher v1.9.1 §M-D6 显式 handle 两种 TABLE_HEADER style. low ROI per G-B02-5.

**§D-7.11 kickoff atom count 估算公式 refinement**: B-03+ kickoff §2.1 atom count 估 应 include §C-1 sub-line multiplier:
- narrative-heavy paragraphs (legal/technical exposition): 2-4 atoms/line
- list-heavy: 1 atom/line
- table-heavy: 1 atom/line + headers
- mixed: weighted average per section

公式: `expected_atoms ≈ Σ (line_count_i × multiplier_i)` per section type.

**§D-7.12 carry-forward LOW md_model06_a029 line_start off-by-one**: defer 不修, 不影响 verbatim correctness. Carry-forward from B-01 closure.

**§D-7.13 writer DONE >999 atom_id support**: writer DONE 报告 format 应 support N atoms ≥ 1000 (atom_id padded `\d{3,}` per schema v1.2.1). Pre-v1.9.1 prompts 隐含支持 (ch04 batch 04 a1000-a1040 already validated). v1.9.1 显式 mention.

### §D-8 FALLBACK pool peer-alternative status promotion (INFO codification)

**Updates §C-2 N21 ban scope clarification post B-02 sustained 7-batch FALLBACK 100% PASS**:

**Writer pool** (any of, peer-alternative status):
- `oh-my-claudecode:executor` — preferred when registered/available
- `general-purpose` — peer-alternative (NOT in N21 banned list 字面合规 + B-02 sustained 7 batches 1,331 atoms 0 writer defect = empirical quality validated)

**Reviewer pool** (any of, peer-alternative status):
- `oh-my-claudecode:scientist` / `oh-my-claudecode:code-reviewer` / `oh-my-claudecode:critic` — preferred when registered/available
- `pr-review-toolkit:code-reviewer` — peer-alternative (B-02 sustained 7 batches 100% PASS rate)
- `feature-dev:code-reviewer` — peer-alternative for cumulative inter-cycle audit (B-01 + B-02 100% PASS rate)

**Daisy/Bojiang ack 2026-05-04 Option B**: FALLBACK 持续 sustained, 不 pause-and-wait OMC restoration. v1.9.1 baseline 显式 promote FALLBACK 等同 OMC priority (NOT emergency-only).

**N21 ban list (sustained, unchanged)**: `oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`. 注: `general-purpose` **NOT** in ban list — promote to peer-alternative writer pool.

**Rule D 隔离硬约束 unchanged**: writer subagent_type ≠ reviewer subagent_type per batch. 派发 strategy 自由 mix-and-match across writer pool / reviewer pool 但跨 batch family rotation 推荐 (per audit_matrix Rule D 累计 roster).

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.7/v1.8/v1.9 carry-forward, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.9_final_2026-05-05/P0_writer_md_v1.9.md` for v1.9 §C-1..C-8 + carry-forward chain to v1.7/v1.8 archives for §A-N28 full text.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (v1.9.1 = 23 hooks for MD-side)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.8 Hook 21 (PDF-only, N/A MD-side) carry-forward unchanged
- v1.9 Hook 22 carry-forward (pre-DONE last_atom.line_end ≥ slice_end - 5, hard slice mode only)
- v1.9 Hook A1/A2/A3 carry-forward (TABLE_HEADER `line_end - line_start ≤ 1` / HEADING `^#{1,6}\s+` / LIST_ITEM full prefix + multi-sentence)
- **v1.9.1 NEW Hook 22b**: kickoff §0.5 grep checksum integrity 信任 — kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims; partial/missing §0.5 = independently verify boundary claims via grep
- **v1.9.1 NEW Hook D-NOTE-BQ**: blockquote-prefix bold-Note `^>\s+\*\*(Note|Exception):\*\*\s+` → atom_type=NOTE + verbatim 含 `> ` prefix byte-exact
- **v1.9.1 NEW Hook D-D8**: numberless `^## Overview\s*$` H2 → sib chain 与 numbered H2 共 + children inherit chapter root parent_section (NOT sub-namespace `§N.0`)

**MD-side hook 总数**: 18 (v1.7) + 0 (v1.8 page-boundary PDF-only) + 4 (v1.9 Hook 22 + A1 + A2 + A3) + 3 (v1.9.1 Hook 22b + D-NOTE-BQ + D-D8) = **25 hooks**.

注: 上 v1.9 changelog 称 "MD-side hooks 18 → 22"; 实际 22 = 18 (v1.7) + 4 (v1.9 NEW). v1.9.1 expand to 25 (+3 NEW).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.1 sync with B-02 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **N21 PDF + MD all-side blanket ban**: STRONGLY VALIDATED EXTENDED (v1.9 baseline + B-02 9 batches 1,983 atoms 0 writer-family contamination across chapters/ + sustained executor + general-purpose pool)
- **FALLBACK pool peer-alternative status**: NEW STATUS — general-purpose + pr-review-toolkit:code-reviewer 等同 OMC priority (sustained 7-batch B-02 100% PASS empirical quality)
- **Axis 5 ordered LIST_ITEM**: STRONGLY VALIDATED (P1 round 14 codify + B-02 9 batches sustained 0 violation; §D-7.2)
- **D5 markdown-uniform numbered Heading dual-constraint**: NEW STATUS codified (B-02 batch 06 ch03 L117 实证)
- **D7 NOTE blockquote carve-out**: NEW STATUS codified (B-02 batch 09 ch08 L389 实证)
- **D8 numberless `## Overview` chapter root inherit**: NEW STATUS codified (post pilot F-P2P-002 N27 fix + B-02 batch 09 D8 INAUGURAL standalone)
- **bold-caption SENTENCE retention rule**: NEW STATUS codified (B-02 batch 06 codify + 17 instances batch 09 validated)
- **S-01..S-04 + D6 letter-prefix appendix**: codified consolidated (B-02 batches 05/08 evidence)
- **CRITICAL kickoff self-consistency rule (Hook 22b)**: NEW STATUS — INAUGURAL clean batch 09 实战 effective post 3 连续 batch 06/07/08 drift catch; B-03+ kickoff template §0.5 mandatory
- **Schema v1.2.1**: SUSTAINED status (9 batches 0 issue; v1.3 promote pending B-04+)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.7 | 2026-04-29 | post P1 round 10 cut EMERGENCY-CRITICAL: N21 SCOPED PDF-side blanket ban writer-family |
| v1.8 | 2026-04-30 | post P1 round 12 cut: 5 NEW patches N24-N28 paired-sync; N21 PDF-side carry-forward |
| v1.9 | 2026-04-29 | post P2 Pilot 2-attempt cycle: 8 NEW patches C-1..C-8. N21 全 ban writer-family 扩到 MD-side. |
| **v1.9.1** | **2026-05-05** | **post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT 30/30=100%**: 8 NEW D-rules consolidating 19 candidate stack (1 CRITICAL Hook 22b kickoff checksum + 2 HIGH D7 NOTE-BQ + D5 dual-constraint + 1 NEW D8 chapter-root-inherit + 2 MEDIUM bold-caption + TABLE_HEADER style兼容 + 13 LOW group consolidated). FALLBACK pool peer-alternative status PROMOTED. 3 NEW hooks (22b + D-NOTE-BQ + D-D8). MD-side hooks 22 → 25. v1.9 archived `archive/v1.9_final_2026-05-05/`. **Backward compatible** — ch04 pilot a001-a218 v1.8 style + B-01/B-02 v1.9 style 都 accepted by matcher/reviewer 之 §M-D6/§R-D6. |
