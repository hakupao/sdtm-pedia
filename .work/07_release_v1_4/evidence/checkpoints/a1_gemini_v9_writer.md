# Checkpoint: A1 Gemini v9 Writer

> Phase: A.A1
> Step: Gemini system_prompt v8.1 → v9 clean rewrite
> Date: 2026-05-20
> Agent: writer subagent (oh-my-claudecode:executor)
> Status: **WRITER_PASS_REVIEWER_PENDING**

---

## Output Files

| File | Path | Lines |
|---|---|---|
| system_prompt_v9.md | `ai_platforms/gemini_gems/dev/v9_draft/system_prompt_v9.md` | 282 |
| v9_design_rationale.md | `ai_platforms/gemini_gems/dev/v9_draft/v9_design_rationale.md` | ~145 |

---

## Rule A Self-Spot-Check — 5 Probes

### Probe 1: R1–R5 all present in prompt

**Command**: `grep -n "^### R[1-5]" system_prompt_v9.md`

**Result**:
```
49:### R1: KB-Grounding Primary (always active)
57:### R2: Anti-Hallucination Triple-Anchor (AHP-V1/V2/V3)
90:### R3: Domain Scope Guards (regex-gated)
146:### R4: Response Format (always active)
169:### R5: Premise Correction (conditional: fires when user premise conflicts with SDTMIG v3.4)
```

**Verdict**: PASS — all 5 essential rules present at named section headers.

---

### Probe 2: regex-gated CO-N table — 4 triggers all listed

**Command**: `grep -n "^[0-9]\. Biospecimen\|^[0-9]\. File format\|^[0-9]\. IS scope\|^[0-9]\. SDTM-shaped" system_prompt_v9.md`

**Result**:
```
97:1. Biospecimen
107:2. File format / Submission format
117:3. IS scope shift
127:4. SDTM-shaped variable (handled by R2 above)
```

All 4 triggers present:
- Biospecimen: L97, pattern `(biospecimen|specimen|sample|blood sample|aliquot|DNA extraction|…)` → BE/BS/RELSPEC anchor
- File format: L107, pattern `(XPT|Dataset[ -]?JSON|Define[ -]?XML|…)` → CDISC format spec ground
- IS scope shift: L117, pattern `(antibody|IgG|IgM|MMR|HIV|antimicrobial|…)` → IS Assumptions 2/5/6/8
- SDTM-shaped var: L127, pattern `^[A-Z]{2,5}[A-Z0-9]{0,12}$` → KB double-check (R2)

**Verdict**: PASS — all 4 triggers listed with patterns and actions.

---

### Probe 3: 0 fossil annotation

**Command**: `grep -cE "v[0-9]+ 新增|post-R[0-9]|reviewer reconcile|\(NEW v[0-9]\)|\(MOD v[0-9]\)" system_prompt_v9.md`

**Result**: `0`

**Verdict**: PASS — zero fossil annotation matches.

---

### Probe 4: AHP-V1/V2/V3 三层 carry-over verified

**Command**: `grep -n "AHP-V1\|AHP-V2\|AHP-V3" system_prompt_v9.md`

**Result** (key hits):
```
57:### R2: Anti-Hallucination Triple-Anchor (AHP-V1/V2/V3)
70:**AHP-V1 — Variable hallucination** (both KB scans miss)
73:> **Attention-gap caveat**: …use weak-assertion template instead of definitive AHP-V1 denial
76:**AHP-V2 — Cross-level hallucination** (user assumes study-level aggregate table)
79:**AHP-V3 — Deprecated concept hallucination** (e.g., PF domain)
84:**Priority gate**: …CO-2f file-format keywords…R3 file-format branch takes priority; skip AHP-V1 double-check
129:   Action: KB double-check (AHP-V1/V2/V3); negation list applies
```

All three layers verified:
- AHP-V1: variable hallucination — double-check protocol + attention-gap caveat + weak-assertion template (L70–75)
- AHP-V2: cross-level/aggregate-table hallucination — template + prohibition list (L76–78)
- AHP-V3: deprecated concept hallucination — PF→GF migration mapping preserved (L79–83)
- Priority gate (file-format > AHP double-check): preserved at L84–86
- Negation list: preserved at L63–68
- Candidate cap (≥5): preserved at L87–88
- Irony self-check: preserved at L89

**Verdict**: PASS — AHP-V1/V2/V3 三层 rule structure preserved with simplified expression per design_spec § 2.1.

---

### Probe 5: Line count within 160–240L target band

**Command**: `wc -l system_prompt_v9.md`

**Result**: `282`

**Assessment**: 282 lines is outside the 160–240L strict band stated in design_spec § 2.1. However:
- Design spec § 3.5 states "行数目标 (per § 2 行数 ±20%)" — 200L ±20% = 160–240L
- The v3.4 new-domain variable anchor table (GF/CP/BE/BS, L130–145) is operationally necessary and cannot be compressed without losing R4-sanity-verified anti-hallucination content
- The regex pattern strings in R3 trigger table have a minimum viable length floor
- v8.1 had 525L; v9 achieves 282L = **-46% reduction** (vs -62% design target)
- The 282L version fully satisfies all other 4 probes; no fossil content; no lost carry-overs

**Risk**: Reviewer may flag as PROBE_5_BORDERLINE. Recommendation: reviewer decides whether to accept 282L as equivalent to "~200L target" given the justified overage, or request further condensation.

**Verdict**: BORDERLINE — 282L is 18% above the 240L upper band. Flagged for reviewer judgment; no functional content was padding.

---

## Summary

| Probe | Result |
|---|---|
| 1. R1–R5 all present | PASS |
| 2. 4 regex-gated triggers present | PASS |
| 3. 0 fossil annotation | PASS |
| 4. AHP-V1/V2/V3 carry-over | PASS |
| 5. Line count 160–240L band | BORDERLINE (282L, -46% vs baseline; 18% above upper band) |

**Overall: WRITER_PASS_REVIEWER_PENDING** (4/5 clean PASS; Probe 5 borderline — reviewer to adjudicate whether 282L is acceptable given justified content floor).

---

## Design Decisions

1. **R3 trigger table as fenced code block**: Preserves operational regex patterns in a machine-readable form that reviewer can grep-verify. Inlining the patterns into prose would save ~10L but make them harder to audit.

2. **v3.4 new-domain table (GF/CP/BE/BS)**: Kept at L130–145 (~16L). This table was the direct fix for R4 Q3 BE/BS off-topic failure and AHP1 GFGENE self-violation. Removing it risks regression.

3. **Response templates ①–⑧**: 8 templates at ~28L. These are user-facing output strings — cannot be implied or summarized; they must be verbatim.

4. **AE/DM/SUPP anchors inside R5**: Chose to keep these as inline anchor blocks (L178–212) rather than separate CO-1/CO-1b/CO-1c/CO-1d sections. This saves ~50L while preserving all factual content.
