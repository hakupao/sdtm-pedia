# Rule A Batch 09 Review — slot #18 pr-review-toolkit:pr-test-analyzer

> Date: 2026-04-25
> Sample: 10 atoms (1 per page p.81-90)
> Seed: 20260450
> Coverage: HEADING / CODE_LITERAL / TABLE_HEADER / NOTE / LIST_ITEM (×2) / TABLE_ROW (×3) / SENTENCE — 6/9 atom_types exercised (no CROSS_REF/FIGURE/[none] in batch 09 sample)
> PDF path: `/Users/bojiangzhang/MyProject/SDTM-compare/source/SDTMIG v3.4 (no header footer).pdf`
> Batch scope: §5.3 Subject Elements (SE) p.79-83 / §5.4 Subject Disease Milestones (SM) p.84-85 / §5.5 Subject Visits (SV) p.86-91
> Ground truth source: CLAUDE.md TOC anchor (p.4-5), NOT topic guess

## Verdict summary

| metric | count |
|---|---|
| PASS | 8 / 10 |
| PARTIAL | 1 / 10 |
| FAIL | 1 / 10 |
| Pass rate (PASS-only) | 80% |
| Pass rate (PASS + PARTIAL) | 90% |
| Threshold | ≥90% |
| Verdict (strict PASS-only) | **FAIL** at 80% |
| Verdict (PASS+PARTIAL pooled) | **PASS** at 90% (boundary) |

**Recommended batch verdict:** **CONDITIONAL_PASS** — strict threshold ≥90% is met only when PARTIAL is pooled with PASS (90.0% exactly at floor). The single FAIL (F-B09-RA-1 below) is HIGH severity and merits an inline fix before batch close. PARTIAL F-B09-RA-2 is LOW and may be accepted with schema-level note.

## Findings

### F-B09-RA-1 (ig34_p0087_a001) — SVCNTMOD controlled-terms hallucination
- **Severity:** HIGH
- **Issue:** TABLE_ROW atom's Controlled Terms cell reads `C\(NCI\)GCD` but PDF p.87 clearly shows `(CNTMODE)` (hyperlinked CT codelist name). `C(NCI)GCD` is not a valid NCI codelist identifier and appears to be a mangled or hallucinated token. The correct codelist name for SVCNTMOD (Contact Mode) is **CNTMODE**.
- **Evidence:** PDF p.87 row 1 — `SVCNTMOD | Contact Mode | Char | (CNTMODE) | Record Qualifier | The way in which the visit was conducted. Examples: "IN PERSON", "TELEPHONE CALL", "IVRS". | Perm` vs atom verbatim — `SVCNTMOD | Contact Mode | Char | C\(NCI\)GCD | Record Qualifier | ...`
- **Hypothesis:** Possible OCR/PDF-text artifact where hyperlink anchor text was conflated with surrounding parentheses/NCI tokens, or writer attempted to generalize "(CNTMODE)" into "C(NCI)GCD" (nonsense expansion). Either way it corrupts a semantically load-bearing field used by downstream CT validation.
- **Action:** `escalate_HIGH` — inline fix required. Replace `C\(NCI\)GCD` with `(CNTMODE)`. Also recommend batch-wide sweep for similar CT-cell corruption in SV/related domains (check SVEPCHGI `(NY)`, SVPRESP `(NY)`, SVOCCUR `(NY)` integrity).

### F-B09-RA-2 (ig34_p0090_a001) — ds.xpt row 5 empty-cell representation ambiguity
- **Severity:** LOW
- **Issue:** TABLE_ROW for ds.xpt row 5 renders as 13 pipe-delimited fields matching the header column count, so structurally correct. However, the empty DSSCAT cell is represented implicitly by `PROTOCOL MILESTONE | SCREENING` without a visible `| |` marker — reading the raw string makes it hard to distinguish "empty DSSCAT" from "missing DSSCAT column". Pipe-count math resolves correctly, but a reader scanning verbatim values could mis-map DSCAT/DSSCAT/EPOCH.
- **Evidence:** PDF p.90 row 5 — DSCAT=PROTOCOL MILESTONE, DSSCAT=(empty), EPOCH=SCREENING. Atom verbatim: `...PROTOCOL MILESTONE | SCREENING...` (empty cell collapses to single `|` separator).
- **Action:** `inline_fix_suggest` — adopt consistent empty-intermediate-cell marker across all TABLE_ROW atoms (e.g. `| |` or explicit empty-string token). Non-blocking for this batch but recommend P1 prompt v1.3 addition.

### F-B09-RA-3 (ig34_p0088_a001) — figure_ref vs cross_ref field misuse (INFO)
- **Severity:** INFO (not a rubric FAIL dim)
- **Issue:** Atom populates `figure_ref: ["§4.4.5"]` but §4.4.5 is a section cross-reference, not a figure. The same reference is correctly populated in `cross_refs: ["§4.4.5", "Clinical Encounters and Visits"]`, so the figure_ref duplicate is schema-incorrect.
- **Action:** `inline_fix_suggest` — set `figure_ref: null`. Not a rubric FAIL because figure_ref is not among the 4 tracked verdict dimensions, but schema-wise it's incorrect.

## Pass list (brief)

- **ig34_p0081_a012** — HEADING "SE – Examples" level 3 sibling 3, verbatim match, §5.3 SE correct per TOC.
- **ig34_p0082_a009** — CODE_LITERAL "se.xpt" dataset filename label, verbatim match, §5.3 SE correct.
- **ig34_p0083_a010** — TABLE_HEADER for SE Example 2 (9 cols Row..EPOCH), verbatim match, §5.3 SE correct.
- **ig34_p0084_a018** — NOTE footnote ¹ about asterisk CT marker, verbatim match including superscript ¹, §5.4 SM correct (p.84 is §5.4 opener).
- **ig34_p0085_a001** — LIST_ITEM Assumption 2.b MIDS sequence number, verbatim match, §5.4 SM correct.
- **ig34_p0086_a018** — TABLE_ROW STUDYID in sv.xpt spec, verbatim match (7 fields), §5.5 SV correct.
- **ig34_p0088_a001** — LIST_ITEM continuation of Assumption 6 (VISITNUM + §4.4.5 ref), verbatim match, §5.5 SV correct; INFO-level schema note on figure_ref field misuse.
- **ig34_p0089_a003** — SENTENCE SV Examples Example 1 intro, verbatim match, §5.5 SV correct.

## Partial list (brief)

- **ig34_p0090_a001** — TABLE_ROW ds.xpt row 5 INFORMED CONSENT OBTAINED for subject 101. Structurally correct (13 fields, empty DSSCAT resolves via pipe-count), but empty-cell representation ambiguous. MINOR drift, non-blocking.

## Fail list (brief)

- **ig34_p0087_a001** — TABLE_ROW SVCNTMOD CT cell corrupted `(CNTMODE)` → `C\(NCI\)GCD`. HIGH severity, requires inline fix before batch close.

## Ground-truth anchor check (anti-"§5.2=CO" bug)

Per CLAUDE.md TOC anchor (authoritative p.4-5 reading):

- §5.1 Comments (CO) — p.60-61 ✓
- §5.2 Demographics (DM) — p.62-78 ✓
- §5.3 Subject Elements (SE) — p.79-83 ✓ (atoms 1/2/3 parent_section §5.3 SE correct)
- §5.4 Subject Disease Milestones (SM) — p.84-85 ✓ (atoms 4/5 parent_section §5.4 SM correct)
- §5.5 Subject Visits (SV) — p.86-91 ✓ (atoms 6/7/8/9/10 parent_section §5.5 SV correct)

No §5.X inversion bug detected in batch 09. All 10 atoms have parent_section matching PDF page-location ground truth.

## Dimension-level statistics

| Dimension | correct | drift/paraphrase | wrong | n/a |
|---|---|---|---|---|
| verbatim | 8 | 2 (1 drift + 1 paraphrase) | 0 | 0 |
| atom_type | 10 | 0 | 0 | 0 |
| parent_section | 10 | 0 | 0 | 0 |
| heading_fields | 1 correct | 0 | 0 | 9 n/a |

- `parent_section` is 10/10 correct — strong signal that TOC-anchor discipline is holding in batch 09.
- `atom_type` is 10/10 correct — no type misclassification across 6 exercised enum values.
- `verbatim` has 2 issues (1 HIGH CT hallucination + 1 LOW empty-cell ambiguity) — concentrated in TABLE_ROW atoms.
- `heading_fields` n/a for 9/10 (only 1 HEADING in sample); that single one fully correct.

## Recommendations to main session

1. **Inline fix F-B09-RA-1 before batch close** — SVCNTMOD CT cell `C\(NCI\)GCD` → `(CNTMODE)`. HIGH.
2. **Sweep-check CT cells in SV p.86-88 batch atoms** — verify `(NY)` / `(CNTMODE)` not similarly corrupted. Same executor session may have systematic CT-token issue.
3. **Prompt v1.3 candidate (LOW)** — formalize empty-intermediate-cell marker in TABLE_ROW verbatim (explicit `| |` vs implicit collapse).
4. **Schema lint candidate (INFO)** — flag atoms where figure_ref and cross_refs both contain the same `§X.Y` token — figure_ref should only hold Figure N.M / Figure N-M tokens.

## Rule A compliance statement (slot #18)

- Sample size N=10 per PLAN §E.2 v1.1 per-batch Rule A cadence ✓
- Independent verification — reviewer is distinct subagent_type `pr-review-toolkit:pr-test-analyzer` (Rule D slot #18, not same as executor `oh-my-claudecode:executor` or writer `oh-my-claudecode:writer` that produced atoms) ✓
- Each atom verified against 1 dedicated PDF page read ✓ (10 pages × 1 read each, no cross-page reuse)
- Ground truth TOC anchored, no topic-guess chapter mapping ✓
- Evidence archived inline (pdf_quote per atom + verdict JSONL + this MD summary) ✓
- Failed atoms NOT deleted (Rule B) — F-B09-RA-1 HIGH flagged for inline fix, original atom preserved pending main-session action ✓

---

*End of Rule A batch 09 review. Slot #18 sign-off: CONDITIONAL_PASS pending inline fix of F-B09-RA-1.*
