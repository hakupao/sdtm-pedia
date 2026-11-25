# P0 Writer MD — 原子化 prompt v1.9

> Version: v1.9 (2026-04-29, post P2 Pilot 2-attempt cycle)
> Cut trigger: P2 Pilot Attempt 1 FAIL Rule A 63.3% (Writer-family 3 systematic defects + slicing 71% coverage); Attempt 2 80% strict / 30/30 functional surfaced 8 NEW codification candidates
> 基于 v1.8 (2026-04-30) + P2 Pilot evidence (`evidence/failures/P2_pilot_attempt_1.md` + `evidence/checkpoints/p2_pilot_report.md`)
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.9 变更 over v1.8: 8 NEW patches C-1..C-8, 大部分由 P2 Pilot 实证驱动. **N21 全 ban writer-family 扩到 MD-side** 是核心业务发现 (推翻 round 14 H_C 假说). v1.8 archived `archive/v1.8_final_2026-04-29/`. NOT 行为兼容 — writer-family agents 物理禁止用作 writer.

## 角色硬约束 (v1.7/v1.8 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` §角色硬约束 全文.

═══════════════════════════════════════════════════════════════════
## v1.9 NEW PATCHES (C-1..C-8, P2 Pilot 实证驱动)
═══════════════════════════════════════════════════════════════════

### §C-1 SENTENCE sub-line atomization 显式允许 (HIGH)

**Rule**: 当 markdown 单物理行 (line_start == line_end) 含 ≥2 句独立语义时, writer **应** emit 多个 SENTENCE atoms, 每个 atom 的 verbatim = 该行的一个 byte-exact substring (单句). 多 atom 共享同 line_start/line_end, atom_id 提供唯一性.

**例**: ch04 line 53 = "SDTM datasets are normally named to be consistent with the domain code; for example, the Demographics dataset (DM) is named dm.xpt. (See the SDTM Domain Abbreviation codelist, ...) Exceptions to this rule are described in Section 4.1.7, Splitting Domains."

emit:
- a042 SENTENCE line 53 verbatim="SDTM datasets are normally named to be consistent with the domain code; for example, the Demographics dataset (DM) is named dm.xpt."
- a043 SENTENCE line 53 verbatim="(See the SDTM Domain Abbreviation codelist, C66734, in CDISC Controlled Terminology at https://...)"
- a044 SENTENCE line 53 verbatim="Exceptions to this rule are described in Section 4.1.7, Splitting Domains."

**与 IR2 一致** (semantic atom 是最小单元, 非 paragraph). **与 IR5 一致** (verbatim byte-exact substring 仍 byte-exact). **服务 P4a matcher 1-PDF-sentence ↔ 1-MD-sentence 匹配粒度**.

**Reviewer 注意**: 多 atom 同 line_start/line_end 是 FEATURE, 非 defect. FAIL_VERBATIM 不应基于 "verbatim ≠ full line" 判定.

### §C-2 N21 全 ban writer-family 扩到 MD-side (HIGH)

**v1.7 N21 (PDF-side ONLY)** → **v1.9 N21 (PDF + MD all-side)**.

**触发**: P2 Pilot Attempt 1 实证 `oh-my-claudecode:writer` 在 MD-side narrative + table + list 内容上有 3 类系统缺陷:
- TABLE_HEADER `line_end` 100% 越界
- bold text `**foo**` 14 atoms 误为 HEADING
- LIST_ITEM verbatim 截断 + 前缀剥除

**结论**: round 14 H_C 假说 "writer-direction RELIABLE on narrative content" **REJECTED**. writer-family 在 PDF + MD 全场景不可信.

**v1.9 N21 final**: writer-family (`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`) 全 ban 作 writer (PDF-side carry-forward + MD-side NEW). **唯一 writer pool**: `oh-my-claudecode:executor` 单 type.

### §C-3 R-MD-Slice-Hard: 切片默认 hard line range (HIGH)

**Rule**: 当 dispatch 指令含 "lines N-M" 类切片 scope, **默认 hard line range** — writer MUST emit atoms 满足 `line_start ≥ N AND line_end ≤ M`, **不得**在 N..M 内提前停止.

- `---` separator / 章节边界 / paragraph break **不是** 自动停止信号; writer push through 直到 line M.
- 若多句段最后一原子 line_end < M-5 (5 行 buffer): coverage failure → STOP + report (不得 fabricate).
- soft semantic-boundary mode: 须 dispatch 显式声明 `slice_mode: "soft"` (默认 hard).

**触发**: P2 Pilot Attempt 1 F-P2P-001 — `oh-my-claudecode:writer` 在 ch04 line 214 (---separator) 自停, 71% 覆盖, 漏 §4.2 整段.

### §C-4 Hook 22 NEW pre-DONE: last_atom.line_end ≥ slice_end (hard mode)

**Hook 22**: writer DONE 前自校验 — 若 dispatch 是 hard slice mode 且 last atom `line_end < slice_end - 5`, FAIL the hook + halt + report. 防 §C-3 silent shortfall.

**Hook 22 仅适用 hard slice mode**; full-file dispatch 不触发.

### §C-5 TABLE_HEADER `line_end - line_start ≤ 1` 显式 (MEDIUM)

**Rule**: TABLE_HEADER atom = column-name 行 + separator 行 (典型 markdown 表头 2 行). emit 时 `line_end - line_start ≤ 1` 必须成立. **不得**指向最后一 data row.

**对照**: TABLE_ROW atoms each 1 row, 1 行 = 1 atom.

**触发**: F-P2P-DEFECT-001 — Writer B 13/13 = 100% TABLE_HEADER 越界缺陷.

### §C-6 bold text `**foo**` is NOT HEADING (explicit ban) (MEDIUM)

**Rule**: markdown HEADING **仅** `^#{1,6}\s+` 形式 (必须 `#`/`##`/`###` 前缀 + 空格). 任何 `**bold**` text **不是** HEADING, atom_type 应 emit SENTENCE 或 NOTE (caption-style 用 NOTE).

**触发**: F-P2P-DEFECT-002 — Writer B 14 atoms 把 `**cm.xpt**` `**relrec.xpt**` 等 dataset-label captions 误 emit 为 HEADING 附 fake heading_level.

### §C-7 LIST_ITEM verbatim 含全 prefix + 全 sentences (MEDIUM)

**Rule**: LIST_ITEM atom verbatim **必须**:
1. 含 bullet/number prefix (`- `, `* `, `1. `, `10. ` 等) 字面
2. 含该 item 内**全部**句子, 直到下一 bullet 或空行 (不得截断多句)

**触发**: F-P2P-DEFECT-003 — Writer B 系统性截断多句 list items + 剥前缀. executor (CM/assumptions Attempt 1) 0 缺陷, 已合规.

### §C-8 file field 用 repo-relative full path 含 `knowledge_base/` 前缀 (LOW)

**Rule**: atom `file` 字段 = repo 根目录的 full repo-relative path. KB 文件 prefix 必须含 `knowledge_base/`.

- ✓ `knowledge_base/chapters/ch04_general_assumptions.md`
- ✗ `chapters/ch04_general_assumptions.md` (缺 `knowledge_base/` 前缀)
- ✓ `knowledge_base/domains/CM/assumptions.md`
- ✓ `knowledge_base/model/01_concepts_and_terms.md`

**触发**: F-P2P-DEFECT-005 — P2 Pilot Attempt 2 T2 (ch04 split 3 part agents) 218 atoms 漏 `knowledge_base/` 前缀, 与 model/CM atoms 不一致.

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.7/v1.8 carry-forward §A-N28, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.8_final_2026-04-29/P0_writer_md_v1.8.md` for v1.8 §N24-N28 + carry-forward to `archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` for §A-N23 full text.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (v1.9 = 21 hooks for MD-side)
═══════════════════════════════════════════════════════════════════

- Hooks 1-18 (v1.6 carry-forward unchanged)
- Hook 21 (v1.8 PDF-side NEW; **N/A MD-side** unchanged per N26)
- **Hook 22 NEW (v1.9)**: pre-DONE last_atom.line_end ≥ slice_end - 5 (hard slice mode only)
- **Hook A1 NEW (v1.9)**: TABLE_HEADER `line_end - line_start ≤ 1`
- **Hook A2 NEW (v1.9)**: HEADING source line matches `^#{1,6}\s+` (not bold)
- **Hook A3 NEW (v1.9)**: LIST_ITEM verbatim starts with `^(\-|\*|\d+\.)\s+` + full multi-sentence content

**MD-side hook 总数**: 18 (v1.7) + 0 (v1.8 page-boundary PDF-only) + 4 NEW (v1.9 Hook 22 + A1 + A2 + A3) = **22 hooks**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9 sync with PDF writer + P2 Pilot evidence)
═══════════════════════════════════════════════════════════════════

- **N21 PDF + MD all-side blanket ban**: STRONGLY VALIDATED based on P2 Pilot Attempt 1 evidence (writer-family 3 systematic defects on MD content reproduce PDF-side N21 trigger pattern)
- **H_C content-conditional reliability hypothesis**: **REJECTED** based on P2 Pilot Attempt 1 evidence
- **R-MD-Slice-Hard rule**: NEW STATUS post P2 Pilot Attempt 2 (Attempt 2 dispatch with explicit "HARD line range" + Hook A4 = 100% coverage; Attempt 1 without explicit rule = 71% coverage)
- **executor single-type writer pool**: STATUS PROMOTION post P2 Pilot Attempt 2 (Attempt 2 397 atoms 0 anti-defect across 3 NEW Hook A1+A2+A3)
- **multi-axis motif taxonomy (v1.8 N24)**: extends to MD-side per C-1..C-8 codification

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut: 9 NEW patches N1-N9 |
| v1.5 | 2026-04-28 | post P1 round 8 cut: 3 NEW patches N15-N17 sync |
| v1.6 | 2026-04-29 | post P1 round 9 cut EMERGENCY-CRITICAL: 3 NEW patches N18-N20 + hooks 15→18 |
| v1.7 | 2026-04-29 | post P1 round 10 cut EMERGENCY-CRITICAL: N21 SCOPED PDF-side ONLY |
| v1.8 | 2026-04-30 | post P1 round 12 cut: 5 NEW patches N24-N28 paired-sync; MD-side N21 carry-forward (still PDF-only) |
| **v1.9** | **2026-04-29** | **post P2 Pilot 2-attempt cycle**: 8 NEW patches C-1..C-8. **N21 全 ban writer-family 扩到 MD-side** (推翻 H_C 假说, P2 Pilot Attempt 1 实证). C-1 SENTENCE sub-line 显式允许 (服务 P4a matcher). C-3/C-4 R-MD-Slice-Hard + Hook 22. C-5/C-6/C-7 anti-defect (TABLE_HEADER line_end / bold-non-HEADING / LIST_ITEM full prefix). C-8 file field full path. v1.8 archived `archive/v1.8_final_2026-04-29/`. **行为不兼容** — writer-family 物理禁止. MD-side hooks 18 → 22. |
