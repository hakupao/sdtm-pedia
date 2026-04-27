# NotebookLM Deployment Tutorial — SDTM Knowledge Base Release v1.0

> Release v1.0 self-deployment tutorial (NotebookLM 1 notebook × 42 sources + Custom mode).
> After completing this tutorial: 30–60 minutes to get a working NotebookLM notebook, in-KB-only natural anti-hallucination, smoke v4 R1 15/17 (88%) baseline.
> Source files: project repository `ai_platforms/notebooklm/current/` (instructions.md + uploads/ × 42).

---

## 0. Prerequisites

- [ ] **Google AI Pro subscription** (subscription page [ai.google.com](https://ai.google.com)): NotebookLM Pro tier limits = 500 notebooks × 300 sources × 500K words/source × 500 chats/day × 20 audio/day; **Free tier limit is 50 sources** and applies under the Restricted sharing level — this deployment uses 42 sources, just under the Free tier boundary, but a Pro subscription is more stable
- [ ] **Google account** (personal Gmail or Workspace): one account manages all notebooks; if you plan to do team sharing in the future, using a Workspace account is recommended
- [ ] **Web browser access** to [notebooklm.google.com](https://notebooklm.google.com): this tutorial is entirely Web UI operations (NotebookLM has no consumer GA API)
- [ ] **Local clone of this repository**: you need to upload the **42 source files** under `../../notebooklm/current/uploads/*.md` and paste `../../notebooklm/current/instructions.md` into the Chat Custom mode

**On "capability vs. capacity"**:
- This release occupies **42/300 = 14%** of the Pro source slots (well below the cap; 8-slot headroom for future expansion)
- Total words: **1,582,085** (largest bucket 302K < 500K/source cap; 0 over-cap / 0 missing)
- Chat Custom mode instructions.md: **8,925 Unicode chars / 10,000 char limit = 10.75% headroom**
- **Coverage**: 63/63 domains fully covered / 176/176 Req variables ∅ gap (A4 structural-level + P3.4.5 semantic-level dual anchor closed) / 295 md files fully ingested across 42 concept buckets

---

## 1. Create Notebook

1. Log in to [notebooklm.google.com](https://notebooklm.google.com) (use the Google account with your Pro subscription)
2. Click "**+ New notebook**" or "**Create new**" in the upper-left corner
3. **Recommended name**: `SDTM Knowledge Base` or `CDISC SDTM Expert`
4. **Description** (optional, fill in the notebook settings): `SDTM (Study Data Tabulation Model) knowledge base from CDISC standards v3.4 IG. 42 concept-clustered sources covering 63 domains + 176 Req variables + chapters + terminology + examples. Answers variable definitions, Core attributes, codelist terms, cross-domain relationships, SUPPQUAL mechanics.`
5. **Sharing level** (default Restricted; see §9 for details on three-tier toggle): start with Restricted, switch to a wider level after smoke test passes as needed

---

## 2. Configure Custom Mode Instructions

NotebookLM has **no System Prompt** — the only prompt-engineering entry point is the Chat **Custom mode** (10K char limit). This release provides `../../notebooklm/current/instructions.md` (8,925 Unicode chars, 89.25% utilization), which already contains the SDTM expert prompt + 13 behavior rules + anchors.

### Steps

1. Open the notebook you just created
2. Find "**Configure**" or the gear icon in the upper-right Chat area → select "**Custom**" mode (the default is "Default"; "Learning Guide" is also available)
3. **Copy the entire content** of `../../notebooklm/current/instructions.md` (do not truncate)
4. Paste it into the Custom goals box
5. Click **Save**

### Why instructions.md is so dense

The release instructions.md contains:
- **13 behavior rules** — priority / citation enforcement / boundary honesty / no fabrication
- **SDTM anchors** (high-frequency error-prone points): AESER Core=Exp (not Req) / LBNRIND 4 values Y/N/U/NA written in full / NY C66742 / ISO 8601 datetime / C-code literal citation / Day 1 with no Day 0 / RELREC+RELSPEC+RELSUB triple set / SUPP-- structure
- **Authoritative layer priority**: `spec > ch04 > CT > assumptions > examples` (use this priority order to resolve conflicts when the same variable appears in multiple sources)

The **10.75% headroom** is reserved for your future fine-tuning (~1,000 chars can accommodate 3–5 additional anchors you define). Exceeding 10K will cause NotebookLM to truncate the content — do not paste more than that.

### H3 VERIFIED: Custom mode is dynamically switchable

Each chat session can independently switch between Default / Learning Guide / Custom (at the UI level). It does not lock the entire notebook. To verify this yourself:
1. Open a chat, switch to "Learning Guide", ask about AE domain rules → you will get a Socratic teaching-style answer
2. Switch back to "Custom" and ask the same question → you will get a structured SDTM expert answer
3. Same source set, different output style

---

## 3. Upload 42 Sources

1. In the "**Sources**" panel on the left side of the notebook, click "**+ Add**"
2. Select "**Upload**" (or drag and drop)
3. **Batch-select** all **42 files** from `../../notebooklm/current/uploads/*.md` (01–42 numbered buckets; do not include MANIFEST.md — MANIFEST is a source inventory document, not a source itself)
4. **Wait for the upload to complete**: all 42 files will queue together; the Web UI supports a single batch. In practice this takes roughly 2–5 minutes for all files to finish

### Key: preventing "indexing silent fail"

NotebookLM officially acknowledges a very small probability of indexing silent fail (a file is uploaded but never truly indexed). Safeguards:

- **UI tile-level spot check**: after uploading, scan through every source tile and check whether the thumbnail + word-count estimate looks reasonable. If any tile shows "0 words" or an error state → **delete and re-upload**
- **All 42 tiles present**: none can be missing. Every tile must show a green "Indexed" status
- **Open a few sources and preview**: spot-check 5–10 sources (first source_01 + last source_42 + a few random ones) by clicking them and reading the opening paragraph, to guard against "uploaded successfully but content is garbled"

In project Phase 3 P3.2 live testing, 42/42 indexed with 0 silent fails (`../../notebooklm/dev/evidence/p3_2_upload_log.md`).

---

## 4. Wait for Indexing

- NotebookLM indexing is much faster than Claude; 42 sources typically all turn green "Indexed" within **2–10 minutes**
- In the Sources panel, each file has a status icon:
  - 🟡 Spinning = indexing in progress, chat is not yet available
  - ✅ Green checkmark = indexed, chat is available
- Proceed to §5 smoke test only after all files show ✅
- If any file is still yellow after >30 minutes, it likely experienced a silent fail → re-upload per §3
- **You can do this in parallel**: paste the §2 instructions.md content (foreground operation) while indexing runs in the background

---

## 5. Smoke Test

Use 3 basic questions to verify the notebook foundation is stable. If any 1 question FAILS, do not continue.

| # | Question | Expected answer | What it validates |
|---|---|---|---|
| 1 | `What is the Core attribute of AESER — Req or Exp?` | **Exp (not Req)** | The highest-frequency error-prone point; answer must include a citation such as `[08_ev_adverse_ae.md]` |
| 2 | `What are all the submission values for LBNRIND?` | **Y / N / U / NA** (all 4 values written out, not LOW/HIGH/WITHIN REF) | Should include Extensible=Yes + a `[33_ct_general.md]` citation |
| 3 | `What is CMINDC used for? How does it relate to CMTRT?` | **CMINDC = indication/reason for concomitant med; CRF "Other, specify" goes through SUPPCM workflow; do not merge with CMTRT** | Must include a citation + mention of SUPPCM |

**3/3 PASS** → proceed to optional §6 full regression.

**Any 1 FAIL** → troubleshoot:
- Answer has no citation → Custom mode is not active; return to §2 and re-paste instructions.md
- Answer says variable is not in the KB (but it should be) → a source is missing or indexing failed; return to §3 and re-upload the corresponding source
- Answer content is wrong (e.g., AESER=Req) → instructions.md was pasted incompletely; return to §2 and verify character count is 8,925

### Release v1.0 complete demo

In addition to the 3 sanity questions in this tutorial, release v1.0 provides a 10-question full demo at [../DEMO_QUESTIONS.md](../DEMO_QUESTIONS.md). Note: NotebookLM is an in-KB-only design — supplemental topic questions like Q11/Q12 will result in a PUNT (refusal to answer). This is **correct anti-hallucination behavior, not a bug**; see [../KNOWN_LIMITATIONS.en.md](../KNOWN_LIMITATIONS.en.md) §L4-NB5.

---

## 6. Full Regression Testing (Optional, 17 Questions, ~30 minutes)

This release was tested against the full 17-question suite (Q1–Q14 + AHP1–3) during smoke v4 R1, achieving **15/17 strict PASS (88.2%)**, with AHP × 3 all PASS+ (strongest tier). You can re-run these to verify your own deployment reaches the same level of stability.

- **Question bank**: [`../../../SMOKE_V4.md`](../../../SMOKE_V4.md) §2
- **Per-question answers + verdicts**: `../../notebooklm/dev/evidence/smoke_v4_answers/*.md`
- **Summary report**: `../../notebooklm/dev/evidence/smoke_v4_results.md`
- **Pass threshold**: ≥12/17 (71%) for R1 first-run tolerance

### 17-question distribution

| Category | Questions | What it tests |
|----------|-----------|---------------|
| Sanity | sanity_01–03 | Foundation stability (same as §5) |
| v3.4 new domains | Q1–Q3 | GF / CP / BE+BS+RELSPEC |
| Domain boundaries | Q4–Q5 | LB/MB/IS / FA/QS/CE |
| Timing | Q6–Q7 | PK sampling four-item set / Partial date |
| CT | Q8 | Extensible vs Non-Extensible |
| Pinnacle 21 | Q9 | Common FAIL classifications (NotebookLM expected to PUNT safety-correct) |
| SUPP deep dive | Q10 | QORIG/QEVAL + SUPPTS premise correction |
| Bonus | Q11–Q14 | Dataset-JSON / CT version / RWD / AE+CE+MH+DS linkage |
| **AHP (anti-hallucination)** | AHP1–3 | **Variable fabrication / cross-domain fabrication / deprecated-version fabrication** — in-KB-only natural advantage test |

### Expected performance

- Q1–Q8 / Q10 / Q14 / AHP1–3 should PASS (90%+)
- Q9 **expected FAIL** (safety-correct PUNT; in-KB-only architecture naturally cannot reach Pinnacle 21 external documentation — this is an architectural limitation, not a capability failure)
- Q11–Q12 **expected PARTIAL** (supplemental topics; in-KB coverage incomplete)
- AHP × 3 should all PASS+ (strongest tier) — NotebookLM architecture has a natural anti-hallucination advantage

---

## 7. Troubleshooting Guide

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| Answer has no citation | Custom mode not active | Return to §2, re-paste instructions.md, confirm green Save checkmark |
| Answer says variable is not in KB (but it should be) | Source indexing silent fail | In §3, find the corresponding source tile and check its status; if yellow loading times out → delete and re-upload |
| Answer gets AESER wrong (says Req) | instructions.md was pasted truncated | Original text is 8,925 chars; if character count is significantly lower after pasting → re-paste |
| smoke v4 Q9 FAIL | **Expected** in-KB-only architectural limitation, safety-correct PUNT | Do not modify instructions.md to add "allow extrapolation" — doing so will degrade the AHP × 3 anti-hallucination advantage |
| AHP1–3 shows fabrication (e.g., answers that LBCLINSIG exists) | instructions.md "boundary honesty" anchor not taking effect | Return to §2 and verify instructions.md is complete; or switch Chat mode away from Custom and switch back to refresh |
| Pro viewer cannot see all sources under Anyone-with-link | Should not happen; this sharing level does not apply the Free tier cap | Check Google account login state; regenerate the share link |
| Table rendering drift (single-row misalignment) | F-1-recurring known behavior; does not deduct semantic score | Re-sending the same question usually refreshes it; retry idempotency is not enforced |
| Citation dropout (on scenario questions) | F-3 systemic weakness (T2 question-type bias) | Answer content is usually correct; citations occasionally drop; does not deduct semantic score |

---

## 8. Upgrade / Maintenance

### Scaling up (42 → N sources)

- Pro cap is 300 sources; current usage is 14%, leaving 8-slot + 258 Pro cap headroom
- To expand the KB (e.g., adding SDTMIG next version v3.5 / new domains), add bucket 43+ to `../../notebooklm/dev/scripts/bucket_config.json` → run `merge_sources.py` → upload the new source incrementally
- Note: ≥51 sources will trigger the Free tier viewer 50-cap; re-run P3.9 (f) Free tier testing

### Scaling down (42 → Free tier compatible)

- Free tier limits: 50 notebooks × 50 sources × 150K words/source × 50 chats/day × 3 audio/day
- **This release exceeds the Free tier words cap**: largest bucket 302K > 150K/source Free cap → bucket re-splitting is required (finer granularity, each < 150K)
- Re-splitting path: write a new config in `../../notebooklm/dev/scripts/`, pack into 80–100 buckets, re-upload
- Estimated effort: 1–2 days

### instructions.md fine-tuning

- 10K char limit; 10.75% headroom (~1,075 chars for 3–5 additional anchors)
- When adding anchors, update CLAUDE.md + RETROSPECTIVE.md R-NBL-3 at the same time
- Exceeding 10K causes truncation; run `wc -m` before pasting to check

---

## 9. Team Collaboration / Three-Tier Sharing Toggle

NotebookLM supports dynamically switching the same notebook among 3 sharing levels without needing to create multiple notebooks. The P3.9 three-tier toggle drill was VERIFIED + deepened on 2026-04-23 (`../../notebooklm/dev/evidence/share_level_toggle_drill.md`).

### Three-tier semantics

| Level | Access rule | Use case | 50-cap rule |
|-------|-------------|----------|-------------|
| **Restricted** (default) | Owner only + Google accounts on the invite list | Personal use / small team | **Free tier invitees subject to 50-source cap** (Pro owner not affected) |
| **Anyone with link** | Any Google-account user who has the link can access | Targeted external sharing / company-wide broadcast | Free tier cap does not apply |
| **Public** | Link can be shared with anyone (Google login still required) | Open knowledge base | Free tier cap does not apply |

### Toggle steps

1. Click the "**Share**" button in the upper-right of the notebook → open the share panel
2. Select the desired level and click "**Copy link**" to generate an access link
3. Switching back to Restricted **immediately revokes** the previous link (P3.9 (d) live-tested PASS; no caching residuals)

### Important: Public level ≠ automatic broadcast (P3.9 new finding)

- The Public level means "**any link holder can access without logging in**" — it does NOT auto-list the notebook in the NotebookLM public gallery
- The NotebookLM public gallery (Featured) is a **curated list**, not auto-listed; setting your notebook to Public does **not automatically expose it**
- **Privacy-friendlier** than ChatGPT GPT Store "Public = broadcast to the entire internet" semantics
- Suitable for: small internal team + targeted external sharing combined scenarios

### Free tier 50-cap only applies to Restricted + Invite scenario

- If the notebook is Restricted and you invite a Free tier Gmail account, that invitee **may only see the first 50 sources**
- This release has 42 sources ≤ 50, so **no impact**
- If you later expand to ≥51 sources and need Free tier viewer access, conduct A/B/C interpretation testing (see PLAN §3.3)

---

## 10. Future Paths

### 10.1 Ready to use immediately

- Query any SDTM variable definition / Core attribute / codelist value
- Query domain boundaries (LB vs MB vs IS / FA vs QS vs CE)
- Query Timing (--TPT four-item set / Partial date)
- Query SUPPQUAL mechanics / RELREC triple set
- **Provide a wrong premise** and expect NotebookLM to correct it (AHP strength)

### 10.2 Known limitations (in-KB-only architecture)

NotebookLM is strictly constrained to answer only from sources; it does not access training data or the web. **This is both an advantage (AHP) and a limitation**:

- Pinnacle 21 report classifications → **PUNT**
- Dataset-JSON / XPT v5 comparisons → supplemental topic PUNT (on some branches)
- RWD (Claims / EHR) SUPP fields specific to those domains → PUNT
- CT version-locked operational milestones → PUNT on some branches

If you need these, use Claude / ChatGPT / Gemini on any platform as a complement (all deployed in the same project release).

### 10.3 ICEBOX (post-project optional)

Studio three-piece set retained in PLAN §10:
- **Audio Overview** × 3 episodes (SAFETY / EFFICACY / PK Deep Dive podcast, 30–45 min each)
- **Mind Map**: 63-domain cross-domain relationships + RELREC/SUPPQUAL coverage
- **Study Guide**: AE / LB / CM Socratic guided learning

Trigger condition: you explicitly request "refine the Studio three-piece set later." Not triggering this does not affect the main retro or the FINAL status of this tutorial.

### 10.4 Related documentation

| Document | Path | Purpose |
|----------|------|---------|
| **RETROSPECTIVE (this platform)** | `../../notebooklm/docs/RETROSPECTIVE.md` | Rule C three-section + pivot case + _template/ patches |
| **Cross-4-platform Phase 5 retro** | `../../retrospectives/PHASE5_RETROSPECTIVE.md` | v1.0 FINAL 2026-04-24 Daisy-acknowledged 4-platform sign-off |
| **PLAN** | `../../notebooklm/docs/PLAN.md` | 662-line v2.2 (complete plan after architecture pivot) |
| **smoke v4 R1 results** | `../../notebooklm/dev/evidence/smoke_v4_results.md` + `smoke_v4_answers/` | Per-question verdict for all 17 questions |
| **P3.9 three-tier toggle evidence** | `../../notebooklm/dev/evidence/share_level_toggle_drill.md` | v1.0 FINAL 6 sub-steps + Public semantics deep-dive |
| **v1→v2 architecture pivot record** | `../../notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` | Key lesson: writer narrative synthesis pseudo-constraint |
| **Reviewer report** | `../../notebooklm/dev/evidence/phase5_retrospective_reviewer.md` | v0.2 post-fix independent audit 10 action items |

---

## Appendix: Post-Deployment Self-Check Checklist

After deployment, run through the following checklist:

- [ ] Notebook created and named `SDTM Knowledge Base`
- [ ] Chat Custom mode has the full instructions.md content pasted (8,925 chars)
- [ ] 42 sources uploaded + all ✅ Indexed
- [ ] Smoke 3 questions (AESER Core / LBNRIND 4 values / CMINDC scenario) 3/3 PASS
- [ ] (Optional) smoke v4 R1 17 questions ≥12/17 PASS
- [ ] Three-tier toggle verified for ≥2 levels (at minimum Restricted and Anyone with link)
- [ ] Notebook URL noted and shared with team (only under Anyone-with-link / Public level)
- [ ] Read §10.2 Known Limitations; do not push Pinnacle 21 or similar requirements to NotebookLM

---

*v1.0 — 2026-04-27 — Company Release*
*Platform-specific retro: ../../notebooklm/docs/RETROSPECTIVE.md ; Release v1.0 overview: ../README.en.md*
