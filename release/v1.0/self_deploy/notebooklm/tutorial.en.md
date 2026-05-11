# NotebookLM Deployment Tutorial — SDTM Knowledge Base Release v1.0

> Release v1.0 self-deployment tutorial (NotebookLM 1 notebook × 42 sources + Custom mode).
> After completing this tutorial: 30–60 minutes to get a working NotebookLM notebook, in-KB-only natural anti-hallucination, complete 17-question test 15/17 PASS (88%) baseline.
> Source files: project repository `./` (instructions.md + uploads/ × 42).
>
> ℹ️ All `../../../../notebooklm/dev/evidence/...` paths referenced in this document point to internal QA artifacts retained by Bojiang Zhang and are NOT included in this release pack. Contact Bojiang Zhang for access if needed.

---

## 0. Prerequisites

- [ ] **Google account and NotebookLM plan** ([notebooklm.google.com](https://notebooklm.google.com)): **NotebookLM plan tiers as of 2026 (Free / Plus / Pro)**:

| Tier | Plan name | Notebooks/user | Sources/notebook | Chats/day |
|------|-----------|---------------|------------------|-----------|
| Free (Standard) | (personal Google account) | 100 | **50** | 50 |
| Plus | Google One AI Premium (personal) | 200 | 100 | 200 |
| Pro | Workspace Enterprise / Education | 500 | 300 | 500 |

  This release uses **42 sources** — fits within **Free tier** (84% of 50 cap). **Plus / Pro provide ample headroom**.
  Words/source limit: **500,000 words or 200 MB/file** (same across Free / Plus / Pro).
  Largest bucket in this release: 302K words < 500K → safe on all plans.
- [ ] **Google account** (personal Gmail or Workspace): one account manages all notebooks; if you plan to do team sharing in the future, using a Workspace account is recommended
- [ ] **Web browser access** to [notebooklm.google.com](https://notebooklm.google.com): this tutorial is entirely Web UI operations (NotebookLM has no consumer GA API)
- [ ] **Local clone of this repository**: you need to upload the **42 source files** under `./uploads/*.md` and paste `./instructions.md` into the Chat Custom mode

**On "capability vs. capacity"**:
- This release uses **42 sources** — Free 50 cap (84%) / Plus 100 cap (42%) / Pro 300 cap (14%). **Accommodated on all plans**; Plus or higher recommended for stability
- Total words: **1,582,085** (largest bucket 302K < 500K/source cap; 0 over-cap / 0 missing)
- Chat Custom mode instructions.md: **8,925 Unicode chars — confirmed working in practice (as of 2026-04); recommend staying within 10K chars as a safe guideline**
- **Coverage**: 63/63 domains fully covered / 176/176 Req variables ∅ gap (structural-level + semantic-level dual-anchor closure) / 295 md files fully ingested across 42 concept buckets

---

## Deployment flow at a glance

The actual NotebookLM UI flow (as of 2026) dictates this order, which this tutorial follows:

```
§1 Create the notebook (Name only)
       ↓
§2 Upload 42 sources           ← required first
       ↓
§3 Wait for indexing
       ↓
§4 Configure Custom Mode instructions   ← only operable after sources are in the notebook
       ↓
§5 Smoke test
```

> **Important**: Custom mode (§4) cannot be activated before sources are uploaded. The old "create notebook → paste prompt immediately" flow does not work in the current UI. Always finish §2 first.

---

## 1. Create Notebook

1. Log in to [notebooklm.google.com](https://notebooklm.google.com) with your Google account
2. Click "**Create new notebook**" (current official label)
3. **Recommended name**: `SDTM Knowledge Base` or `CDISC SDTM Expert`
4. **Sharing level** (default Restricted; see §7 for details on two-tier toggle): start with Restricted, switch to a wider level after smoke test passes as needed

> **Note**: The current (2026) UI has **no Description field**. Only the Name is editable. The old tutorial's "Description" step has been removed.

---

## 2. Upload 42 Sources

1. In the "**Sources**" panel on the left side of the notebook, click "**Add**" (no + symbol) → choose your upload method from the popup (**Upload files / Google Drive / URL / audio file / paste text**)
2. Select "**Upload files**" (or drag and drop)
3. **Batch-select** all **42 files** from `./uploads/*.md` (01–42 numbered buckets; do not include MANIFEST.md — MANIFEST is a source inventory document, not a source itself)
4. **Wait for the upload to complete**: all 42 files will queue together; the Web UI supports a single batch. In practice this takes roughly 2–5 minutes for all files to finish

### Key: preventing "indexing silent fail"

NotebookLM officially acknowledges a very small probability of indexing silent fail (a file is uploaded but never truly indexed). Safeguards:

- **UI tile-level spot check**: after uploading, scan through every source tile and check whether the thumbnail + word-count estimate looks reasonable. If any tile shows "0 words" or an error state → **delete and re-upload**
- **All 42 tiles present**: none can be missing. Every tile must show a green "Indexed" status
- **Open a few sources and preview**: spot-check 5–10 sources (first source_01 + last source_42 + a few random ones) by clicking them and reading the opening paragraph, to guard against "uploaded successfully but content is garbled"

On upload, this release was measured 42/42 indexed with 0 silent fail (upload log: `../../../../notebooklm/dev/evidence/p3_2_upload_log.md`).

---

## 3. Wait for Indexing

- NotebookLM indexing is much faster than Claude; 42 sources typically all turn green "Indexed" within **2–10 minutes**
- In the Sources panel, each file has a status icon:
  - 🟡 Spinning = indexing in progress, chat is not yet available
  - ✅ Green checkmark = indexed, chat is available
  - **Note**: Official documentation does not specify exact icon appearance (🟡/✅) — the above is based on observed UI behavior and may change with UI updates
- Proceed to §5 smoke test only after all files show ✅
- If any file is still yellow after >30 minutes, it likely experienced a silent fail → re-upload per §2
- **You can do this in parallel**: paste the §4 Custom Mode Instructions (foreground operation) while indexing runs in the background

---

## 4. Configure Custom Mode Instructions

NotebookLM has **no System Prompt** — the only prompt-engineering entry point is the Chat **Custom mode**. This release provides `./instructions.md` (8,925 Unicode chars, 89.25% utilization), which already contains the SDTM expert prompt + 13 behavior rules + anchors.

> **Prerequisite**: sources must already be uploaded in §2. The Custom mode entry under Chat only becomes operable once the notebook contains sources.

### Steps

1. Open the notebook you created, and confirm that the 42 sources are visible in the Sources panel
2. Click the **gear icon** in the Chat panel → open "**Configure Chat**" menu → select "**Custom**" mode (default is "Default"; "Learning Guide" is also available)
   > **Note**: As of the 2025/10 update, the Custom mode entry point was unified under "Configure Chat"
3. **Copy the entire content** of `./instructions.md` (do not truncate)
4. Paste it into the Custom goals box
5. Click **Save**

### Why instructions.md is so dense

The release instructions.md contains:
- **13 behavior rules** — priority / citation enforcement / boundary honesty / no fabrication
- **SDTM anchors** (high-frequency error-prone points): AESER Core=Exp (not Req) / LBNRIND 4 values Y/N/U/NA written in full / NY C66742 / ISO 8601 datetime / C-code literal citation / Day 1 with no Day 0 / RELREC+RELSPEC+RELSUB triple set / SUPP-- structure
- **Authoritative layer priority**: `spec > ch04 > CT > assumptions > examples` (use this priority order to resolve conflicts when the same variable appears in multiple sources)

**No official character limit is documented** (the old "10K char limit" has disappeared from official docs). The 8,925 Unicode chars in this instructions.md are confirmed working in practice (as of 2026-04). **Recommend staying within 10K chars** as a safe guideline; the ~1,000 char headroom can accommodate 3–5 additional anchors you define.

### Custom mode is per-chat switchable, doesn't lock the whole notebook

Each chat session can independently switch between Default / Learning Guide / Custom (at the UI level). It does not lock the entire notebook. To verify this yourself:
1. Open a chat, switch to "Learning Guide", ask about AE domain rules → you will get a Socratic teaching-style answer
2. Switch back to "Custom" and ask the same question → you will get a structured SDTM expert answer
3. Same source set, different output style

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
- Answer has no citation → Custom mode is not active; return to §4 and re-paste instructions.md
- Answer says variable is not in the KB (but it should be) → a source is missing or indexing failed; return to §2 and re-upload the corresponding source
- Answer content is wrong (e.g., AESER=Req) → instructions.md was pasted incompletely; return to §4 and verify character count is 8,925

### Release v1.0 complete demo

In addition to the 3 sanity questions in this tutorial, release v1.0 provides a 10-question full demo at [../../DEMO_QUESTIONS.en.md](../../DEMO_QUESTIONS.en.md). Note: NotebookLM is an in-KB-only design — supplemental topic questions like Q11/Q12 will result in a PUNT (refusal to answer). This is **correct anti-hallucination behavior, not a bug**; see [../../KNOWN_LIMITATIONS.en.md](../../KNOWN_LIMITATIONS.en.md) §L4-NB5.

---

## 6. Full Regression Testing (Optional, 17 Questions, ~30 minutes)

Complete test of 17-question suite (including 3 anti-hallucination questions): 15/17 PASS (88.2%), all 3 anti-hallucination questions caught — tied for strongest among the 4 platforms (NotebookLM in-KB-only architecture is naturally anti-hallucination). You can re-run these 17 questions to verify your own deployed notebook is equally stable.

- **Question bank**: [`../../../../SMOKE_V4.md`](../../../../SMOKE_V4.md) §2
- **Per-question answers + verdicts**: `../../../../notebooklm/dev/evidence/smoke_v4_answers/*.md`
- **Summary report**: `../../../../notebooklm/dev/evidence/smoke_v4_results.md`
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
- all 3 anti-hallucination questions caught (strongest tier) — NotebookLM architecture has a natural anti-hallucination advantage

---

## 7. Sharing Level Toggle (2 tiers) + Featured Notebooks

NotebookLM supports dynamically switching the same notebook between sharing levels without needing to create multiple notebooks. The share level toggle drill was VERIFIED + deepened on 2026-04-23 (`../../../../notebooklm/dev/evidence/share_level_toggle_drill.md`).

### Two-tier semantics

| Level | Access rule | Use case |
|-------|-------------|----------|
| **Restricted** (default) | Owner only + Google accounts on the invite list | Personal use / small team |
| **Anyone with a link** | Any Google-account user who has the link can access | Targeted distribution / team-wide announcement |

> "Public" is not a user-selectable sharing level in the current UI. The old tutorial's "Public level" entry has been removed.

### Toggle steps

1. Click the "**Share**" button in the upper-right of the notebook → open the share panel
2. Select the desired level and click "**Copy link**" to generate an access link
3. Switching back to Restricted **immediately revokes** the previous link (live-tested PASS; no caching residuals)

### Featured Notebooks (public gallery)

- A curated list (researchers / publishers / nonprofits etc.) selected by Google — general users cannot apply
- **Featured Notebooks is not available on Workspace Enterprise / Education accounts**
- The old tutorial's "Public level" concept was closest to Featured Notebooks, but it is not a user-switchable option

### Free tier 50-cap only applies to Restricted + Invite scenario

- If the notebook is Restricted and you invite a Free tier Gmail account, that invitee **may only see the first 50 sources**
- This release has 42 sources ≤ 50, so **no impact**
- If you later expand to ≥51 sources and need Free tier viewer access, conduct A/B/C interpretation testing (see PLAN §3.3)

---

## 8. Troubleshooting Guide

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| Answer has no citation | Custom mode not active | Return to §4, re-paste instructions.md, confirm green Save checkmark |
| Answer says variable is not in KB (but it should be) | Source indexing silent fail | In §2, find the corresponding source tile and check its status; if yellow loading times out → delete and re-upload |
| Answer gets AESER wrong (says Req) | instructions.md was pasted truncated | Original text is 8,925 chars; if character count is significantly lower after pasting → re-paste |
| 17-Q Q9 FAIL (architecture limit) | **Expected** in-KB-only architectural limitation, safety-correct PUNT | Do not modify instructions.md to add "allow extrapolation" — doing so will degrade the anti-hallucination advantage |
| AHP1–3 shows fabrication (e.g., answers that LBCLINSIG exists) | instructions.md "boundary honesty" anchor not taking effect | Return to §4 and verify instructions.md is complete; or switch Chat mode away from Custom and switch back to refresh |
| Pro viewer cannot see all sources under **Anyone with a link** | Should not happen; this sharing level does not apply the Free tier cap | Check Google account login state; regenerate the share link |
| Table rendering drift (single-row misalignment) | F-1-recurring known behavior; does not deduct semantic score | Re-sending the same question usually refreshes it; retry idempotency is not enforced |
| Citation dropout (on scenario questions) | F-3 systemic weakness (T2 question-type bias) | Answer content is usually correct; citations occasionally drop; does not deduct semantic score |
| "Configure Chat" menu in Custom mode is missing / not clickable | §2 source upload not yet complete | Verify that the 42 sources are visible in the Sources panel; if not, finish §2 first |

---

## 9. Upgrade / Maintenance

### Scaling up (42 → N sources)

- Pro cap is 300 sources; current usage is 14%, leaving 8-slot + 258 Pro cap headroom
- To expand the KB (e.g., adding SDTMIG next version v3.5 / new domains), add bucket 43+ to `../../../../notebooklm/dev/scripts/bucket_config.json` → run `merge_sources.py` → upload the new source incrementally
- Note: ≥51 sources will trigger the Free tier viewer 50-cap; re-run Free tier testing

### Free tier compatibility (no change needed)

- Free tier limits: 100 notebooks × 50 sources × 500K words/source × 50 chats/day × 3 audio/day
- **This release works as-is on Free tier**: 42 sources ≤ 50 cap, largest bucket 302K < 500K/source cap → **no bucket re-splitting required**
- No re-splitting or re-upload is needed. Deployment steps are identical across Free / Plus / Pro.

### instructions.md fine-tuning

- **No official character limit is documented** (the old "10K char limit" has disappeared from official docs). The 8,925 chars in instructions.md are confirmed working in practice (as of 2026-04). **Recommend staying within 10K chars** as a safe guideline (~1,075 chars headroom = 3–5 additional anchors)
- When adding anchors, update CLAUDE.md + RETROSPECTIVE.md R-NBL-3 at the same time
- Run `wc -m` before pasting to check character count

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

**Studio panel (2025/7 redesign) — 4 tile layout** retained in PLAN §10:
- **Audio Overviews** × N episodes (SAFETY / EFFICACY / PK Deep Dive podcast, 30–45 min each)
- **Video Overviews** (new in 2025/7, video version of Audio)
- **Mind Maps**: 63-domain cross-domain relationships + RELREC/SUPPQUAL coverage
- **Reports** (old Study Guide is now integrated under this Reports tile): AE / LB / CM Socratic guided learning

Trigger condition: you explicitly request "refine the Studio 4-tile set later." Not triggering this does not affect the main retro or the FINAL status of this tutorial.

### 10.4 Related documentation

| Document | Path | Purpose |
|----------|------|---------|
| **RETROSPECTIVE (this platform)** | `../../../../notebooklm/docs/RETROSPECTIVE.md` | Rule C three-section + pivot case + _template/ patches |
| **Cross-4-platform Phase 5 retro** | `../../../../retrospectives/PHASE5_RETROSPECTIVE.md` | v1.0 FINAL 2026-04-24 Bojiang Zhang-acknowledged 4-platform sign-off |
| **PLAN** | `../../../../notebooklm/docs/PLAN.md` | 662-line v2.2 (complete plan after architecture pivot) |
| **Complete 17-Q test results** | `../../../../notebooklm/dev/evidence/smoke_v4_results.md` + `smoke_v4_answers/` | Per-question verdict for all 17 questions |
| **Share level toggle evidence (2 tiers)** | `../../../../notebooklm/dev/evidence/share_level_toggle_drill.md` | v1.0 FINAL 6 sub-steps + verification that "Public" is not a user-selectable tier |
| **v1→v2 architecture pivot record** | `../../../../notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` | Key lesson: writer narrative synthesis pseudo-constraint |
| **Reviewer report** | `../../../../notebooklm/dev/evidence/phase5_retrospective_reviewer.md` | v0.2 post-fix independent audit 10 action items |

---

## Appendix: Post-Deployment Self-Check Checklist

After deployment, run through the following checklist (order matches the real UI flow):

- [ ] Notebook created and named `SDTM Knowledge Base`
- [ ] 42 sources uploaded + all ✅ Indexed
- [ ] Chat Custom mode has the full instructions.md content pasted (8,925 chars)
- [ ] Smoke 3 questions (AESER Core / LBNRIND 4 values / CMINDC scenario) 3/3 PASS
- [ ] (Optional) complete 17-question test ≥12/17 PASS
- [ ] Sharing level toggle verified for ≥2 levels (at minimum Restricted and Anyone with a link)
- [ ] Shared notebook URL with team (when distributing via Anyone with a link)
- [ ] Read §10.2 Known Limitations; do not push Pinnacle 21 or similar requirements to NotebookLM

---

*v1.2 — 2026-05-11 — Deployment steps corrected to match the real UI flow (Upload → Indexing → Custom mode order; no Description field). v1.1 (UI terminology 2026 sync) is rolled in.*
*Platform-specific retro: ../../../../notebooklm/docs/RETROSPECTIVE.md ; Release v1.0 overview: ../README.en.md*
