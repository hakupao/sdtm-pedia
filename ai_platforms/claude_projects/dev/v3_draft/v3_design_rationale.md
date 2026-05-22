# Claude Project system_prompt v3 — Design Rationale (Attempt 2, post A5.3 critic revision)

> Writer attempt 1: oh-my-claudecode:executor (writer subagent, Rule D isolated)
> Writer attempt 2: main session (surgical revision per A5.3 critic NEEDS_REVISION findings)
> Date: 2026-05-20
> Task: Phase A.A3 clean rewrite v2.6 → v3
> Design spec: `.work/07_release_v1_4/design_spec_v9.md`
> Attempt 1 archive: `.work/07_release_v1_4/evidence/failures/a3_claude_attempt_1.md`

---

## 1. Line Count Comparison

| Metric | v2.6 baseline | v3 attempt 1 | v3 attempt 2 (current) |
|--------|--------------|--------------|------------------------|
| Total lines | 126 | 120 | 133 |
| Δ vs baseline | — | -4.8% | +5.6% |
| Sections | 8 | 6 | 7 |

**Attempt 2 design rationale**: 133L > design spec § 2.3 target (~80-100L) due to restored 19-file KB Structure table (+11 rows) and named-archive Coverage Notes per A5.3 critic findings C-1/C-2/C-3/M-3. Critic prioritized correctness of file table over line count target. Trade-off accepted: +13L over attempt 1 (120→133) to fix 3 CRITICAL + 1 MAJOR regression.

---

## 2. Structural Diff Summary (vs v2.6 baseline)

| Section | v2.6 | v3 attempt 2 | Action |
|---------|------|-----|--------|
| Header / role preamble | 15L with inline history refs | 12L clean header + role block | Rewritten; fossil annotations removed |
| KB file index | 11L (9 files listed; baseline was stale, true count = 19) | 22L (**19 files — all uploaded files in Project**) | Corrected vs both baseline AND attempt 1 (which truncated to 7) |
| Routing table (7 types) | 18L inline routing prose | 12L table, primary/secondary updated per actual 19-file layout (rows 4/5/6 now name 09/10/11a-13c/08) | Condensed; logic preserved; archive routing restored |
| Hard constraints / CO-N stack | ~30L prose rules (v1/v2/v2.x era) | 5 essential rules R1-R5 (L46/50/61/77/85) + regex CO-N inline table (L65-75) | Replaced fossil CO-N with spec-compliant 5 rules per design spec § 1.3-1.4 |
| Response format | 22L scattered across sections | Consolidated in R4 (L77-83) | Merged; duplicate guidance removed |
| Boundary templates | 20L (4 templates) | 14L (4 templates condensed) | Preserved all 4; text tightened |
| KB coverage notes | 15L (named archive files in tier descriptions) | 12L (archive files re-named per v2.6 model — attempt 1 had dropped names) | Restored named anchors per A5.3 critic M-3 |

---

## 3. Essential Rules (R1-R5) — Position in v3 attempt 2

| Rule | Name | Line in attempt 2 |
|------|------|------|
| R1 | KB-Grounding Primary | 46 |
| R2 | Anti-Hallucination (AHP-V1/V2/V3) | 50 |
| R3 | Domain Scope Guards (regex-gated) | 61 |
| R4 | Response Format | 77 |
| R5 | Premise Correction | 85 |

Verified by `grep -n "^### R[1-5]" system_prompt_v3.md`. All 5 rules present. R2 + R3 consolidate v2.6's scattered hallucination guards and domain-scope prose into structured, regex-gated logic per design spec § 1.3.

---

## 4. Regex-Gated CO-N Table — Position in v3 attempt 2

Located under R3 (lines 65-75), the inline code block lists all 4 required triggers:

| Trigger # | Pattern (verified line) | Action |
|-----------|--------|--------|
| 1 | biospecimen (L67) | BE/BS/RELSPEC priority; prohibit AE/CM fallback |
| 2 | file format (L69) | ground to CDISC format spec |
| 3 | IS scope shift (L71) | IS Assumption 2/5/8; HIV Ag/Ab combo → MB exemption |
| 4 | SDTM-shaped var (L73) | KB double-check (AHP-V1/V2/V3); negation list applies |

All 4 triggers from design spec § 1.4 are present byte-exact. Negation list at L57 inline in R2 (also applies to R3 trigger 4).

---

## 5. Fossil Annotation Self-Check

```
grep -cE "v[0-9]+ 新增|post-R[0-9]|reviewer reconcile|\(NEW v[0-9]\)|\(MOD v[0-9]\)" \
  ai_platforms/claude_projects/dev/v3_draft/system_prompt_v3.md
```

**Result: 0 matches.** Verified post-attempt-2. The version header line contains `v3` as the current version identifier only — not as iteration history. The `Replaces v2.6` line is explicitly permitted per design spec § 1.5.

---

## 6. Claude-Specific Carry-Over Verification

Per design spec § 2.3:

| Carry-Over Item | Present in v3 attempt 2? | Location |
|----------------|---------------|---------|
| Claude Project KB structure (actual upload count) | **Yes (19 files, corrected from attempt 1's incorrect 7)** | KB Structure section, lines 20-39 (19 rows: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11a, 11b, 11c, 12a, 12b, 12c, 13a, 13c) |
| Claude artifact-friendly response style | Yes | R4 (markdown lists/tables, conclusion-first, no greeting preamble) |
| v2.6 7-type routing table | Yes | Routing section, lines 95-103 — Rows 4/5/6 updated to reflect 19-file layout (09/10 archives for examples, 11a-13c tiers for terminology, 09 cross-reference for PP RELREC Quick Reference) |
| 4 boundary templates | Yes | Boundary Templates section, lines 107-118 |
| Internal routing notes (not user-visible) | Yes | KB Coverage Notes section, lines 122-130 — archive files named per v2.6 baseline §119-125 model |

**Attempt 1 → 2 correction**: attempt 1 truncated the file table from 19 to 7, claiming "7 compressed files" in header + table. This was a regression vs v2.6 (which said "9", also wrong but closer). Attempt 2 restores ground-truth 19-file table verified by `ls ai_platforms/claude_projects/current/uploads/` = 19 files.

---

## 7. v2.6 → v3 Decisions

**Removed:**
- "v2.x 改动" iteration history annotations in section headers
- Redundant CO-N-style prose scattered across multiple sections (replaced by R1-R5)
- Duplicate response format guidance (was in both "回答规范" and "格式化约定" sections)
- "工作流程 (每次回答)" enumerated workflow (consolidated into routing table + R1)

**Preserved (and corrected in attempt 2):**
- All 4 boundary templates (examples data / terminology values / Notes detail / unknown domain)
- Internal KB routing priority order (high > low > catalog for examples; high > mid > tail > 08 for CT)
- AHP-V1/V2/V3 three-layer anti-hallucination mechanism (v8.1 R4 sanity 5/5 validated)
- CDISC public citation style (SDTMIG v3.4 §N.N.N; NCI EVS Cxxxxx)
- "Do not expose internal file names" rule
- **Full 19-file KB table** (attempt 2 fix; attempt 1 had truncated to 7)
- **Named-archive anchors in Coverage Notes** (attempt 2 fix; attempt 1 had only "high tier / mid tier / tail tier" without file names)

**Restructured:**
- 19-file KB table moved to second section for immediate orientation
- Essential rules named R1-R5 per design spec § 1.3
- Regex table formatted as code block per design spec § 1.4 template
- Routing row 6 (Cross-domain linking) now adds `09_examples_data_high.md` secondary hint — anchors the A3.1 pipeline fix (PP §6.3.5.9.3 RELREC Method Quick Reference now reachable in 09 bundle after rebuild)

---

## 8. Attempt 1 → Attempt 2 Revision Log (post A5.3 critic findings)

A5.3 reviewer (oh-my-claudecode:critic, Rule D slot #24) returned NEEDS_REVISION verdict with 3 CRITICAL + 3 MAJOR findings. All 6 addressed in attempt 2:

| Finding | Severity | Fix in attempt 2 |
|---|---|---|
| C-1 | CRITICAL | Header L18: "7 compressed files" → "19 compressed files (~190K tokens)". KB Structure table expanded from 8 rows (00-07) to 19 rows (00-13c) |
| C-2 | CRITICAL | Routing row 5 now consistent with KB table; 08_terminology_map.md is row 9 in expanded table + named as fallback in Routing #5 |
| C-3 | CRITICAL | KB Coverage Notes lines 124-128 now name all archive files: 09 (high examples), 10 (low examples), 11a/11b/11c (high terminology tier), 12a/12b/12c (mid tier), 13a/13c (tail tier). MedDRA codelist C65047/C67154 reference now anchored in 13a context |
| M-1 | MAJOR | Line count rationale corrected: 100L claim was wrong (attempt 1 was 120L). Attempt 2 actual = 133L (verified `wc -l`). Trade-off acknowledged in § 1 above |
| M-2 | MAJOR | R1-R5 positions corrected in § 3: now 46/50/61/77/85 (verified `grep -n "^### R"`). Previously claimed 50/56/70/82/92 was off by ~14 lines |
| M-3 | MAJOR | Named-file routing restored in §6 and Routing rows 4/5: 09_examples_data_high.md / 10_examples_data_others.md / 11a-13c terminology archives now named in routing destinations |

**Open Question deferred**: Method label anchor for PP §6.3.5.9.3 (A=Many-Many / B=One-Many / C=Many-One / D=One-One). Per design spec § 2.3, this is ChatGPT-only carry. Critic open question whether Claude needs same anchor — deferred to Phase C sanity verify (if Claude Q-S2 in Phase C shows drift, add anchor in v1.5; if not, no action).

**A3.1 pipeline fix critical review** (separate from prompt review): critic APPROVED with reservations (regex correct, 0 cross-ref regression, no double-emission). Phase B oracle suggested: `grep -c "#### §" output_v2/09_examples_data_high.md` expecting 2 (PP + MB; PC may go to 10 depending on D1 domain list).
