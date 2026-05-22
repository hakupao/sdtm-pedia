# Checkpoint A5.1 — Gemini v9 Reviewer Audit

> Phase: A.A5.1 (Reviewer audit of Gemini v9 clean rewrite)
> Date: 2026-05-20
> Reviewer subagent_type: `pr-review-toolkit:code-reviewer`
> Writer subagent_type (parallel): `oh-my-claudecode:executor`
> Rule D slot: **#22** (writer/reviewer different subagent_type — independent audit, not re-verification of writer self-probes)
> Status (output): **PASS_WITH_OBSERVATIONS** (recommendation: promote to `current/`)

---

## Audit scope

Independent semantic + structural audit of:
- Prompt: `ai_platforms/gemini_gems/dev/v9_draft/system_prompt_v9.md` (282L)
- Rationale: `ai_platforms/gemini_gems/dev/v9_draft/v9_design_rationale.md`
- Writer checkpoint: `.work/07_release_v1_4/evidence/checkpoints/a1_gemini_v9_writer.md`

Against:
- Design spec: `.work/07_release_v1_4/design_spec_v9.md`
- v8.1 baseline: `.work/07_release_v1_4/backups/gemini_v8_1_baseline_system_prompt.md` (525L)
- v1.3 RETROSPECTIVE §二.1 (motivation: prompt bloat → 5 essential rules + regex-gated CO-N)

---

## 1. 6-Dimension Audit Items

### Item 1 — R1–R5 essential rules complete + clear

| Rule | Location | Coverage check | Verdict |
|---|---|---|---|
| R1 KB-Grounding Primary | L49–56 | "always active" header + 4 lookup sub-rules; default path stated ("Only if KB lookup yields no result"). KB-primary is **default**, not trigger-conditional. | PASS |
| R2 Anti-Hallucination Triple-Anchor | L57–88 | regex trigger `^[A-Z]{2,5}[A-Z0-9]{0,12}$` + negation list (L62–63) + AHP-V1 template (L70–71) + attention-gap caveat (L73–74) + AHP-V2 (L76–77) + AHP-V3 (L79–80) + priority gate (L84) + candidate cap (L86) + irony check (L88) | PASS |
| R3 Domain scope guards | L90–145 | 4 triggers in fenced block (biospecimen L97 / file-format L107 / IS scope L117 / SDTM-shaped L127) + new-domain anchor table L132–145 | PASS |
| R4 Response Format | L146–168 | Structure (Conclusion→Evidence→CDISC Source) + cite source format `SDTMIG v3.4 <domain> domain — spec §<var>` + allowed forms + prohibited forms + concise example at L158 | PASS |
| R5 Premise Correction | L169–202 | 3-step mandatory order (L171) + 3 examples (L174–176 incl. SUBJID/AE example) + AE/DM/SUPPQUAL/CT anchor blocks (L178–202) | PASS |

**Verdict (Item 1)**: **PASS**. All 5 rules present, clearly named, with explicit trigger/default semantics. R1 is correctly default (not trigger-conditional). R5 includes both the operational example and the AE/DM anchor data needed to fire the rule.

---

### Item 2 — regex-gated CO-N table trigger logic

**Audit checks**:

a) **4 triggers mutually exclusive (no double-fire risk)**:
- Trigger 1 (biospecimen) pattern: `(biospecimen|specimen|sample|blood sample|aliquot|DNA extraction|RNA extraction|specimen derivation|PGx specimen|biorepository|采血|分装|样本制备|样本运输)` → BE/BS/RELSPEC. **No collision** with file-format or IS patterns.
- Trigger 2 (file format) pattern: `(XPT|Dataset[ -]?JSON|Define[ -]?XML|SAS Transport|submission format|transport format|Unicode|8.char limit|200.char limit|FDA Data Catalog|Pinnacle 21 file)`. **Priority gate explicit at L84**: file-format wins over AHP-V1 if both fire (e.g. "Dataset-JSON" embeds "JSON" which would match negation list anyway). **No double-fire risk.**
- Trigger 3 (IS scope) pattern: `(antibody|IgG|IgM|MMR|HIV|antimicrobial|anti.microbial|antibod|HBsAb|HBcAb|HCV Ab|ADA|spike protein)`. Distinct semantic domain.
- Trigger 4 (SDTM-shaped var) regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` — handled by R2 with negation list.

b) **SDTM-shaped var negation list completeness**:
- L62–63 lists: `FDA / USA / NCI / EVS / CDISC / ADaM / SDTM / XPT / XML / JSON / SAS / EDC / CRF / RWD / ADAE / ADSL / ADTTE` + `AE / CM / DM / LB / IS / MB / BE / BS (and all standard domain 2-letter codes)`.
- Design spec § 1.4 requires exactly: `FDA|USA|NCI|EVS|CDISC|ADaM|SDTM|XPT|XML|JSON|SAS|EDC|CRF|RWD|ADAE|ADSL|ADTTE` + domain abbreviations `AE|CM|DM|LB|IS|MB|BE|BS`. **Match.**
- **OBSERVATION (LOW)**: The phrase "(and all standard domain 2-letter codes)" is a generalization. v8.1 listed 8 explicit domain codes; v9's catch-all is shorter but slightly less precise. A future Gemini run could ambiguously decide whether `PC` / `PP` / `TS` qualifies. The phrase is **likely acceptable** because Gemini has the domain list in KB 01_navigation, but a one-time enumeration `(AE|CM|DM|LB|IS|MB|BE|BS|PC|PP|TS|MH|EX|CE|SV|TA|TE|TI|TV|RELREC|SUPPQUAL|...)` would be more deterministic. **Not a blocker.**

c) **Fall-through behavior clear**:
- L92: "Each trigger fires only on regex match. Default path: KB-grounding (R1)." Explicit fall-through to R1.
- L84 explicit priority gate (file-format > AHP-V1).
- L86 candidate cap (≥5 → only 3–5 named).

**Verdict (Item 2)**: **PASS**. Triggers mutually exclusive; negation list complete; fall-through explicit. One LOW observation on catch-all domain phrasing.

---

### Item 3 — 0 fossil annotation independent grep

**Command** (executed independently, not re-using writer's grep):
```
grep -cE "v[0-9]+ 新增|post-R[0-9]|reviewer reconcile|\(NEW v[0-9]\)|\(MOD v[0-9]\)" \
    /Users/bojiangzhang/MyProject/sdtm-pedia/ai_platforms/gemini_gems/dev/v9_draft/system_prompt_v9.md
```

**Output**: `0`

**Extended grep** for adjacent fossil patterns:
```
grep -nE "新增|post-R[0-9]|reviewer reconcile|NEW v[0-9]|MOD v[0-9]|smoke v[0-9]" system_prompt_v9.md
```
**Output**: (no matches in body; only `> v9 LIVE 2026-05-20 — clean rewrite (post v1.3 light sanity feedback)` at L3 which is the **current** version header per design spec § 1.5, not fossil iteration history)

**Verdict (Item 3)**: **PASS**. Zero fossil annotation. L3 header `(post v1.3 light sanity feedback)` is the canonical replacement note allowed by design spec § 1.5 Header style template; it is not a fossil "post-R3" / "v8 新增" marker.

---

### Item 4 — Platform special carry-over (design_spec § 2.1)

| Carry-over | Required | v9 Location | Verdict |
|---|---|---|---|
| AHP-V1/V2/V3 三层 (rule structure preserved, simplified expression OK) | Yes | R2 L57–88: V1 template L70–71 + V2 L76–77 + V3 L79–80 + priority/cap/irony L84–88 | PASS |
| C-strategy: terminology via NCI EVS, KB not inlined | Yes | L22–28 (C-Strategy section) + L196–202 (CT rules in R5) + ⑥ template L222–223 + ⑦ L225–226 | PASS |
| KB 4-file 1M context structure | Yes | L32–43 (full table with file names, tokens, position, content). Same byte-for-byte data as v8.1 L33–42. | PASS |
| Attention-gap caveat (weak-assertion template) | Yes (high-value carry from v6 13th reviewer fix) | L73–74 | PASS |
| Priority gate (file-format > AHP-V1) | Yes (v8.1 reviewer H2 fix) | L84 | PASS |
| Candidate cap (≥5 → 3-5) | Yes (v8.1 reviewer M2 fix) | L86 | PASS |
| v3.4 new-domain explicit variable anchors (GF/CP/BE/BS) | Yes (CO-4 floor) | L132–145 table with prohibited fabrications column | PASS |
| Off-topic guard (response domain ≠ question domain → delete+reanchor) | Yes (R3 Q3/Q11 fix) | L267–270 (per-answer workflow Step 7) | PASS |
| HIV Ag/Ab combo → MB (Assumption 5 exemption) | Yes (v8.1 reviewer H1 fix) | L122 | PASS |
| IS scope shift triple-iteration consolidated to 1 segment | Yes | R3 trigger 3 L117–126 (single 10-line block) | PASS |

**Verdict (Item 4)**: **PASS**. All design_spec § 2.1 preserved-list items present; all removed-list fossil items absent.

---

### Item 5 — Independent N=5 spot-check (semantic trace)

For each sample question, traced which rule fires and whether v9 prompt provides operational support.

**Q1**: "BECAT 是 sponsor-extensible 吗?"
- Expected fires: **R1 KB-grounding** (default for variable Core/CT lookup) → KB BE/spec L111 has EXTRACTION sponsor-extensible.
- R5 premise correction may fire if user implies "non-extensible".
- v9 evidence: L101 — "BECAT examples: COLLECTION / PREPARATION / TRANSPORT / EXTRACTION (sponsor-extensible)". Explicit anchor present.
- **Supported Y**: Gemini will see L101 anchor → answer "EXTRACTION is one of the sponsor-extensible BECAT example values" + cite `SDTMIG v3.4 BE domain — spec §BECAT`.

**Q2**: "PP RELREC Method A 是哪种 1-to-many 关系?"
- Expected fires: **R1 KB-grounding** (PP examples §6.3.5.9.3 Method A=Many-Many) **+ R5 premise correction** (user's "1-to-many" premise is wrong per KB).
- v9 evidence: NO inline Method A/B/C/D label table (intentional — per v1.3 RETROSPECTIVE §二.4, the inline label anchor is a ChatGPT v3 carry, not Gemini). Gemini relies on R1 KB lookup into `04_business_scenarios_and_cross_domain.md` §1.10 + `03_domains_examples.md` PP RELREC tables.
- v9 has R5 premise correction L171 mandatory order + the principle to identify-error-before-proceeding.
- **Supported Y (conditional on KB content)**: R1 + R5 together provide the path. If KB still contains §6.3.5.9.3 prose (per v1.3 Q-S2 evidence it was added to PP/examples.md), Gemini will see Method A=Many-Many and correct premise. **However**: per v1.3 RETROSPECTIVE §二.3, Claude pipeline missed capturing the §6.3.5.9.3 prose into 07_examples_catalog.md; the Gemini KB build path captures 03_domains_examples.md verbatim, so the prose is present for Gemini. **OBSERVATION (MEDIUM)**: this answer's correctness depends on the KB 03 file having absorbed the Quick Reference; reviewer cannot verify the KB content from prompt audit alone — defer to Phase C sanity smoke for end-to-end check.

**Q3**: "HIV Ag/Ab combo 测试 → IS 还是 MB?"
- Expected fires: **R3 IS scope shift** (regex `HIV|antibod` match) → IS Assumption 5 → MB (combo exemption).
- v9 evidence: L118 pattern includes `HIV|antimicrobial|antibod` → trigger 3 fires. L122 — "HIV Ag/Ab combo (4th-gen, p24 Ag + HIV-1/2 Ab): Assumption 5 exemption → MB domain". Direct operational answer.
- **Supported Y**: regex match → L122 explicit MB exemption rule.

**Q4**: "麻疹 IgG → 哪个 domain?"
- Expected fires: **R3 IS scope shift** (regex `IgG|antibod` match) → IS Assumption 2 (anti-microbial antibody → IS regardless of timing).
- v9 evidence: L118 pattern `IgG|antimicrobial|antibod` matches "麻疹 IgG". L120 — "Anti-microbial antibody / pathogen antibody measurements → IS domain (regardless of collection timing: baseline / on-treatment / post-vaccination / follow-up)". L121 — "NOT LB (even if routine serology); NOT MB (antibody measures host immune response, not pathogen itself)".
- **Supported Y**: regex match → L120–121 explicit IS anchor.

**Q5**: "AESEV 是 Required 吗?"
- Expected fires: **R2 AHP regex match** (AESEV = 5-char SDTM-shaped) → KB double-check (AE/spec.md, AESEV Core=**Perm** per v8.1 anchor) → R5 premise correction (user's "Required" premise is wrong).
- v9 evidence: regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` matches `AESEV`. Negation list (L62–63) does NOT contain AESEV. AHP-V1 double-check fires → KB grep finds AESEV in `02_domains_spec_and_assumptions.md` (variable exists) → fall to R1+R5 path. L181–182 — "AESEV Core=Perm (not Req!)" + L183 "For any AE variable Core query: grep ... → cite source → do NOT pattern-infer".
- **Supported Y**: Negation list correctly excludes AESEV; R2 double-check finds it; R5 anchor block contradicts the "Required" premise explicitly.

**Spot-check summary**: 5/5 paths semantically supported by v9 prompt. Q2 has a MEDIUM observation that correctness depends on KB content not the prompt — but the prompt-side path is correct.

**Verdict (Item 5)**: **PASS** (1 MEDIUM observation on Q2 deferred to Phase C).

---

### Item 6 — Line count borderline assessment

- **Target band** (design_spec § 2.1 + § 3.5): 200L ±20% = 160–240L
- **Actual**: 282L (+17.5% above upper band 240L)
- **Writer explanation** (a1 checkpoint Probe 5):
  - R3 regex pattern table (~16L pattern strings) cannot be compressed without losing operational content
  - v3.4 new-domain anchor table L132–145 (~14L) — direct R4 Q3 BE/BS off-topic + AHP1 GFGENE fix; cannot remove
  - 8 response templates L222–245 (~24L) — verbatim user-facing strings

**Reviewer independent assessment**:

a) **Could the v3.4 new-domain table be condensed?** Reviewing L132–145: 14 lines, 4 rows, 4 columns. Could merge "Prohibited fabrications" column into a single trailing footnote per domain — saves ~3L. Marginal benefit; readability cost real. **Accept as-is.**

b) **Could R3 regex code block be condensed?** L94–130 (~37 lines). The fenced code block format adds 2 fence lines. Each trigger is ~10 lines with pattern, action header, and 3–5 bullet sub-anchors. Removing sub-anchors would defeat the purpose (anti-fallback content). **Accept as-is.**

c) **Could R5 anchor blocks be condensed?** L178–202 (~25 lines) for AE Core / DM ARMCD null / SUPPQUAL / CT rules. v8.1 had these as 5 separate CO-N sections totaling ~120 lines. v9 already 80% condensed. Further compression risks losing actionable detail. **Accept as-is.**

d) **Could 8 response templates be condensed?** L222–245 (24L) for 8 templates avg 3L each. v8.1 used ~50L. Already 50% condensed. Template body has a verbatim floor (must be user-facing English block). **Accept as-is.**

e) **One potential compression**: the per-answer workflow L249–273 (25L) could be trimmed by ~5L by merging Step 0a (regex scan) + Step 0b (negation filter) into one step. **Marginal value; not requested.**

**Net assessment**: Writer's explanation is **reasonable**. The 282L overage is 42L above upper band; ~30L of that is justified operational content (regex patterns + new-domain table + templates verbatim). The remaining ~12L of overage is distributed across R5 anchor density and workflow steps — borderline but defensible.

**Verdict (Item 6)**: **OBSERVATION (LOW)** — 282L exceeds 240L upper band by 17.5%, but justified content floor accounts for ≥30L. Net reduction from v8.1 (525L → 282L) is **-46%** (design spec target was -62% which would yield 200L). Accept with observation; do not request rewrite. v1.4 retrospective should note that ~280L appears to be a realistic floor for Gemini given the AHP triple-anchor + regex-gated CO-N + 8-template architecture.

---

## 2. Findings Table

| ID | Severity | Confidence | Location | Description | Recommendation |
|---|---|---|---|---|---|
| F1 | LOW | 85 | L63 | Negation list catch-all phrase "(and all standard domain 2-letter codes)" is less deterministic than v8.1's explicit enumeration of 8 codes. | Optional: replace with explicit enumeration `(AE|CM|DM|LB|IS|MB|BE|BS|PC|PP|TS|MH|EX|...)` in a future tune. Not a v1.4 blocker. |
| F2 | LOW | 88 | L88 vs Rationale claim L89 | Writer rationale states "Irony self-check: preserved at L89" but actual location is L88 (off-by-one). | Cosmetic only; no functional impact. |
| F3 | MEDIUM | 80 | Q2 path | PP RELREC Method A label correctness depends on KB 03_domains_examples.md containing the §6.3.5.9.3 Quick Reference prose. Prompt provides path (R1 KB-grounding + R5 premise correction) but cannot guarantee KB content. | Defer to Phase C sanity smoke for end-to-end verification (Q-S2 in v1.4 R sanity set). |
| F4 | LOW | 82 | L29 (line count) | 282L is +17.5% above design spec § 2.1 upper band 240L. Writer rationale justified. | Accept; record as "Gemini architectural floor ~280L" in v1.4 RETROSPECTIVE. |
| F5 | LOW | 80 | L208–216 routing table | Routing table cell "Deprecated concept" row has both Primary and Secondary as `—` (empty), with only CO-5 check populated. Slightly unusual table style. | Cosmetic; deprecated path is fully handled via R2 AHP-V3 — not a content gap. |

**No HIGH-severity findings.** No NEEDS_REVISION blockers.

---

## 3. Cross-Check: Writer Probes vs Independent Audit

| Writer probe | Writer verdict | Reviewer independent verdict | Match? |
|---|---|---|---|
| 1. R1–R5 all present | PASS | PASS (Item 1) | ✓ |
| 2. 4 regex-gated triggers | PASS | PASS (Item 2, with LOW F1) | ✓ |
| 3. 0 fossil annotation | PASS (grep=0) | PASS (independent grep=0) | ✓ |
| 4. AHP-V1/V2/V3 carry-over | PASS | PASS (Item 4) | ✓ |
| 5. Line count band | BORDERLINE (282L) | OBSERVATION (LOW F4) | ✓ (reviewer accepts) |

Reviewer findings beyond writer probes:
- Item 5 (N=5 semantic spot-check) — writer did not run; reviewer ran independently → 5/5 paths supported (1 MEDIUM F3 deferred to Phase C)
- F1 / F2 / F5 — minor observations not surfaced by writer self-check

---

## 4. Overall Verdict

**PASS_WITH_OBSERVATIONS**

- 6/6 audit items PASS or OBSERVATION (no FAIL)
- 5/5 spot-check semantic traces supported by prompt
- 0 fossil annotation confirmed by independent grep
- All design_spec § 2.1 preserved-list items present; all removed-list fossil items absent
- 282L overage justified by operational content floor

5 findings (4 LOW + 1 MEDIUM, all confidence 80–88). No HIGH-severity findings. Zero NEEDS_REVISION blockers.

---

## 5. Recommendation

**Promote `dev/v9_draft/system_prompt_v9.md` to `current/` after user ack.**

Pre-promote actions:
1. Writer should fix F2 (off-by-one line reference in rationale L89 → L88) — 1-line edit, optional.
2. F3 (Q2 KB-dependence) routes to Phase C sanity smoke (Q-S2 set) — not a v9 prompt issue.
3. F1 / F4 / F5 are accepted observations; record F4 (~280L floor) in v1.4 RETROSPECTIVE §二 lessons.

No prompt content changes required for promote. Status transition: `WRITER_PASS_REVIEWER_PENDING` → `WRITER_PASS_REVIEWER_PASS_WITH_OBSERVATIONS`.

---

## 6. Rule D Slot #22 Compliance

- Writer subagent_type: `oh-my-claudecode:executor`
- Reviewer subagent_type: `pr-review-toolkit:code-reviewer`
- **Different subagent_type confirmed**. Independent semantic audit performed (not just re-running writer's grep probes).
- Independent grep run for fossil annotation: `grep -cE "v[0-9]+ 新增|post-R[0-9]|reviewer reconcile|\(NEW v[0-9]\)|\(MOD v[0-9]\)" → 0`
- N=5 spot-check designed by reviewer (not writer); 5/5 traced to specific prompt line numbers.

Rule D PASS for slot #22.
