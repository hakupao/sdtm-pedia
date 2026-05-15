# KNOWN_LIMITATIONS v1.1 Reconciliation

> Audit date: 2026-05-16
> Auditor: executor subagent (read-only; KNOWN_LIMITATIONS files not modified)
> Sources read:
>   - `release/v1.1/KNOWN_LIMITATIONS.en.md` (current v1.1 file)
>   - `branches/06_deep_verification/RETROSPECTIVE.md` §二 (6 gaps)
>   - `ai_platforms/retrospectives/PHASE5_RETROSPECTIVE.md` (carry-over items)

---

## §1. Current KNOWN_LIMITATIONS §0–§6: Status per Item

### §0. v1.1 Audit Scope (added 2026-05-15)

This section was added for v1.1. It declares four deferred items:

| Sub-item | Status | Notes |
|----------|--------|-------|
| SMOKE_V4 not re-run against v1.1 deployments | **STILL VALID** | No new smoke run was performed for v1.1 |
| Rule A spot-check N=5 KB files (not N=20+) | **STILL VALID** | Stated bound is accurate |
| Gemini 04 not re-audited against new PC §6.3.5.9 RELREC content | **STILL VALID — and confirmed by this audit** | gemini_04_audit.md §2 confirms GAP exists: Methods A/B/C/D absent from 04 |
| 437 UNSOURCED_MANUAL atoms unclassified | **STILL VALID** | 06 RETRO §二.4 confirms still open |

**Overall §0 assessment**: Accurately stated. The Gemini 04 gap declared in §0 is now evidenced by this audit.

---

### §1. Not a Replacement for Official Standards

**Status**: **STILL VALID** — this is a durable disclaimer. Not affected by 06 fixes. No change needed.

---

### §2. Real-Time External Updates Are Not Guaranteed

**Status**: **STILL VALID** — durable disclaimer about knowledge cutoff. Not affected by 06 fixes.

---

### §3. Long-Tail Terminology May Require Official Lookup

**Status**: **STILL VALID** — the 06 fixes did not add NCI EVS coverage. CO-2 constraint in the Gemini uploads still routes long-tail queries to NCI EVS. No change needed.

---

### §4. Platform Answer Styles Differ

**Status**: **STILL VALID** — platform behavioral characteristics unchanged by KB content updates. No change needed.

---

### §5. Internal Organization Rules Are Not Covered

**Status**: **STILL VALID** — durable scope boundary. Not affected by 06 fixes.

---

### §6. High-Risk Scenarios Require Human Review

**Status**: **STILL VALID** — durable safety disclaimer. Not affected by 06 fixes.

---

## §2. 06 RETROSPECTIVE §二 6 Gaps — Public vs Internal Classification

The 06 RETROSPECTIVE §二 lists 6 gaps. Assessment of which belong in public KNOWN_LIMITATIONS vs which are internal QA:

### Gap 1: P4a 规格表变量行 IE 分类不彻底

**Description**: P4a matcher misclassified variable spec table rows (AESEQ/PRELTM/MBTPT etc.) as PARTIAL/EQUIVALENT/ERROR instead of INTENTIONAL_EXCLUDE(REDUNDANT_WITH_SPEC). Root cause: no pre-filter for "| VARNAME | Label | Char/Num |" pattern atoms.

**Public disclosure?**: **NO — internal QA only.**
Rationale: This is a defect in the coverage ledger audit tool (verdict label accuracy), not in the deployed KB content. It does not affect end-user answers. The KB content for those variables is correct. Users have no actionable path from this information.

**Already in KNOWN_LIMITATIONS?**: Indirectly — §0 states "Rule A spot-check used N=5 KB files (not N=20+); per-bucket semantic audit was not performed." The broader caveat covers this.

---

### Gap 2: P4a 同例表行匹配精度不足

**Description**: 6 WRONG verdicts from P4a matching wrong rows in example tables (similar content, different sequence/USUBJID). Root cause: matcher checked similarity but not row identifier consistency.

**Public disclosure?**: **NO — internal QA only.**
Rationale: Same class as Gap 1 — verdict label precision issue in the audit tool, not KB content quality. Zero impact on deployed answers.

**Already in KNOWN_LIMITATIONS?**: Covered by same §0 caveat as Gap 1.

---

### Gap 3: T4 Tier B 未完成 (56 SIBLING_DROPPED + 110 CONTENT_TRUNCATED)

**Description**: 166 nodes with incomplete content or missing sibling nodes; deferred after G1 PASS (99.02%).

**Public disclosure?**: **YES — should be in KNOWN_LIMITATIONS.**
Rationale: This directly affects KB depth. Users querying the KB in sections with SIBLING_DROPPED or CONTENT_TRUNCATED nodes may get incomplete information. The current §3 "Long-Tail Terminology" only covers terminology lookup gaps, not structural KB depth gaps. A new limitation item covering "Some KB sections have reduced depth" is user-relevant.

**Already in KNOWN_LIMITATIONS?**: **NOT explicitly.** §0 mentions "43 KB files refined" but does not say 166 sections remain at reduced depth. This is a disclosure gap.

---

### Gap 4: 437 UNSOURCED_MANUAL atoms 未最终定性

**Description**: 437 MD atoms present in KB with no traceable PDF source. Classification (reasonable inference vs phantom content) not completed.

**Public disclosure?**: **YES — should be in KNOWN_LIMITATIONS.**
Rationale: End users rely on KB content accuracy. 437 atoms whose source-of-truth lineage is unverified is a real caveat for high-stakes usage. Already declared in KNOWN_LIMITATIONS §0 (2026-05-15 addition).

**Already in KNOWN_LIMITATIONS?**: **YES — §0 sub-item 4 explicitly states this.**

---

### Gap 5: §6.3.5.9.3 PP RELREC linking 示例缺口 (2 atoms, OA-4)

**Description**: PP/examples.md was missing the explicit RELREC linking example showing PP records (PPSEQ=1 and PPSEQ=6 for ABC-123-0001) linked to PC records. 06 P7 identified this as the only true content gap.

**Current state**: PP/examples.md now contains RELREC method descriptions (Method B, C, A) and the shared PP data table with PPSEQ values. The RELREC tables themselves (relrec.xpt) are described as "see PC examples for full description." KB PC/assumptions.md §6.3.5.9.3 has the full method narrative. The explicit "2 atoms absent" gap referred to specific RELREC record rows that were present in the PDF but missing from PP/examples.md. The cross-reference note in PP/examples.md ("see PC examples for the full description of RELREC Methods A–D and their corresponding relrec.xpt tables") is present, but the relrec.xpt example table data for PPSEQ=1/PPSEQ=6 specifically is still described by cross-reference rather than inline in PP/examples.md.

**Public disclosure?**: **NO — too granular for public KNOWN_LIMITATIONS.**
Rationale: This is a missing internal worked example (2 RELREC record rows), not a substantive error in KB rules. The rule (PC-PP RELREC obligation) is present in PC/assumptions.md §6.3.5.9.3. The absence of the inline worked example in PP/examples.md affects depth only, not accuracy. Gemini 04 gap (which affects what the deployed AI knows) is already declared in KNOWN_LIMITATIONS §0.

**Action needed**: The §0 item "Gemini's 04 not re-audited against new PC §6.3.5.9 RELREC content" already covers the user-facing consequence. No additional public item needed, but the 04 update (see gemini_04_audit.md §4 Diff 1) would address the practical gap.

---

### Gap 6: section_coverage.jsonl P4b 快照未刷新

**Description**: section_coverage.jsonl still shows P4b-era verdicts; post-P6 T4 repaired sections (e.g., SC §6.3.10) still show SKELETON_ONLY in the snapshot.

**Public disclosure?**: **NO — internal tooling artifact.**
Rationale: This is an internal audit artifact state. Users have no visibility into section_coverage.jsonl. The actual KB content was repaired; only the audit snapshot is stale. No user-facing impact.

---

## §3. Phase 5 Carry-Over Items — KNOWN_LIMITATIONS Assessment

From PHASE5_RETROSPECTIVE.md, the two v7.1 carry-over HIGH items:

### Carry 1: Gemini Q1 GFGENE regression

**Description**: Gemini v6 CO-4 had only negative-list (禁止X) for GF domain variables without a positive-list anchor. Gemini R2 Q1 answered GFGENE (which violated its own prohibit list). v7 patched CO-1c with ARMCD-null rule and CO-5 AHP; v7 apply confirmed PASS. PHASE5_RETRO confirms v7.1 optional patches (SUPP-- Core锚点 + ARMNRS canonical 4 values) as non-blocking candidates.

**Current v1.1 status**: v1.0 → v1.1 rebuild used updated KB but system prompts were not re-reviewed against this specific Gemini GF-domain positive-list gap. SMOKE_V4 was not re-run (per KNOWN_LIMITATIONS §0).

**Should add to KNOWN_LIMITATIONS?**: **Partially — already covered.**
The §0 statement "SMOKE_V4 has not been re-run against the v1.1 deployments; baseline scores from v1.0 are presumed unchanged but not confirmed" covers this. The GF domain is a niche area (oncology genetics); the risk is bounded. No separate item needed. However, if a v1.1-specific SMOKE re-run is planned for v1.2, the KNOWN_LIMITATIONS §0 entry should be updated when that happens.

---

### Carry 2: Gemini Q13 ARMCD-null rule (SDTMIG v3.4 observational study rule)

**Description**: SDTMIG v3.4 rule: observational/RWD studies with no planned ARM → ARMCD should be null (not "NOTASSGN" 8-char; ARMNRS from C142179, not C66770). Gemini R1 and R2 both answered with "NOTASSGN" (invented value). v7 CO-1c patch added this rule; post-v7 apply confirmed PASS (v5c regression 14/14).

**Current v1.1 status**: v7 system prompt is current in the deployed Gem (v1.1 rebuild included v7 prompt). This was patched. The rule is in the prompt.

**Should add to KNOWN_LIMITATIONS?**: **NO — resolved in v1.1 by v7 prompt application.**
The v7 patch for ARMCD-null is confirmed applied and tested (v5c regression PASS). This is not a remaining limitation. No item needed.

---

## §4. Recommendations: Specific Add/Update/Delete to KNOWN_LIMITATIONS

All recommendations are for the main session to consider — not written to KNOWN_LIMITATIONS files by this audit (read-only).

### Recommended ADD: New §0 sub-item for Tier B depth gap

Add to KNOWN_LIMITATIONS §0 (v1.1 Audit Scope) the following sub-item:

> - Approximately 166 KB sections (56 with missing sibling nodes, 110 with truncated content) were not fully repaired in the 06 deep verification pass, as the project reached its coverage gate (99.02%) with Tier A (HIGH-priority) repairs only. Answers in these sections may be less complete than other areas. Known affected domains include scattered deep-chapter content; see 06 deep verification project notes for details.

**Rationale**: Gap 3 (Tier B deferred) is user-relevant because it affects KB answer depth. Currently undisclosed.

### Recommended KEEP unchanged: §1–§6

All six existing numbered limitation items remain accurate and do not need updating based on 06 fixes.

### Recommended NO ACTION: §0 sub-items 1–4 (existing)

All four existing §0 sub-items are accurately stated. The Gemini 04 audit (this session) confirms sub-item 3 ("Gemini 04 not re-audited against PC §6.3.5.9 RELREC content") is a real and documented gap.

### Recommended DELETE: None

No existing items are obsolete or inaccurate.

### Summary table

| Item | Action | Priority |
|------|--------|----------|
| Add: Tier B 166-section depth gap to §0 | ADD | MEDIUM |
| §0 sub-items 1–4 (existing) | KEEP | — |
| §1–§6 (all existing numbered items) | KEEP | — |
| Gemini Q13 ARMCD-null (Phase 5 carry) | NO ACTION (resolved) | — |
| Gemini Q1 GFGENE (Phase 5 carry) | COVERED by §0 smoke caveat | — |
| Gap 1/2 (P4a IE/table-row matcher) | NO ACTION (internal QA) | — |
| Gap 4 (UNSOURCED_MANUAL) | ALREADY IN §0 | — |
| Gap 5 (PP RELREC 2-atom gap) | COVERED by §0 Gemini item | — |
| Gap 6 (section_coverage.jsonl stale) | NO ACTION (internal tool) | — |
