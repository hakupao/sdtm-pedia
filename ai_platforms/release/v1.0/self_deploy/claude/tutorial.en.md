# Claude Project Creation Tutorial — SDTM Knowledge Base Release v1.0

> Release v1.0 self-deployment tutorial (set up a Claude Project capable of answering CDISC SDTM queries from scratch).
> After following this tutorial: 30–60 minutes to a complete working Claude Project (including indexing wait time which runs in background). Capacity ~77%, 19 files / 1.29M tokens, complete 24-question test all-pass baseline.
> Source: project repository `./` (system_prompt.md + uploads/ × 19).

---

## 0. Prerequisites

- [ ] **Claude Pro subscription** (or Team/Enterprise): the release build totals 1.29M tokens, exceeding the free-tier limit; Pro and above plans automatically enable RAG sharding for Claude Projects
- [ ] **Web browser access** to [claude.ai](https://claude.ai): this tutorial is performed entirely through the Web UI
- [ ] **Local clone of this repository**: you will need the 19 files under `./uploads/` and `./system_prompt.md`

**On "capability vs. capacity"**:
- The release build occupies approximately **77% capacity** of Claude Projects (as shown in the UI)
- Headroom remains, but this is already close to the soft ceiling of paid plans; if Anthropic adjusts capacity limits in the future a re-evaluation may be needed
- Coverage: core codelist 99.3% / supp codelist 100% / questionnaires codelist 55.8% / 63 domain examples 100% / 6 chapters fully expanded

---

## 1. Create Project

1. Log in to [claude.ai](https://claude.ai)
2. Click "**Projects**" in the left sidebar → "**Create Project**"
3. **Suggested name**: `SDTM Knowledge Base` or `CDISC SDTM Expert`
4. **Description** (optional): `SDTM (Study Data Tabulation Model) knowledge base from CDISC standards. Answers variable definitions, codelist terms, example datasets, cross-domain references.`
5. **Access permissions**:
   - Personal use: **Private**
   - Team use: select your organization (Team/Enterprise plans only)
   - Note: Claude Projects currently **does not support generating public share links**; sharing is limited to within an organization

---

## 2. Configure System Prompt (Custom Instructions)

The System Prompt is the Project's "role and behavior specification" — it defines how the model routes queries, cites sources, and handles scope boundaries.

### Steps

1. Open the newly created Project and click "**Edit project**" in the top-right corner
2. Locate the "**Custom instructions**" or "**Project instructions**" field
3. **Copy the entire contents** of `./system_prompt.md` (do not truncate)
4. Paste into the field
5. **Save**

### Why the System Prompt is so long

The release build System Prompt is approximately **4–6K tokens**, containing 6 accumulated instruction stages:
- Stage 1: full chapter expansion usage rules
- Stage 2: query priority for high-frequency domain data in examples
- Stage 3: fallback strategy for remaining domains in examples
- Stage 4: terminology high-frequency codelist (`11*`) takes priority; fallback to `08_terminology_map`
- Stage 5: terminology mid-frequency codelist (`12*`) added to the CT query chain
- Stage 6: terminology tail + 6 MedDRA-scale giant codelists handled via Deferred stub declarations

Each stage is a coverage layer; together they form the "query routing strategy across all files." Omitting any stage will cause Claude to not know to look in `11*` for CT Codes.

---

## 3. Upload 19 Knowledge Base Files

### Steps

1. Still in the "Edit project" interface, locate the "**Project Knowledge**" panel
2. Select **all 19 `.md` files** in the `./uploads/` directory at once
3. Drag them into the Knowledge panel (or click "Add files" to select)
4. Claude will begin uploading (~1–2 minutes) → then proceed to Indexing

### File list (19 files, 1,286,161 tokens total)

Order does not matter; upload all of them. The `./uploads/` directory contains all 19 `.md` files.

**Key concepts**:
- File name prefixes `00–13c` serve as query-priority signals (the System Prompt references these prefixes for routing)
- **Do not rename** any file — the file name in Project Knowledge is itself the anchor Claude uses for source citations
- **Do not split or merge** files — especially `11b` (256K tokens, the largest single file); testing confirmed it does not cause recall degradation, but custom modifications could break RAG chunking

### FAQ

**Q: The UI shows "File is too large" for a file**
A: The per-file limit is ~1 MB (~256K tokens); `11b` is right at 256K and may trigger this. If it does:
- Check whether your editor has appended a BOM or converted line endings to CRLF
- As a last resort, split `11b` into `11b-a` / `11b-b`, but A/B testing will need to be re-run

**Q: I only want to upload a subset to test**
A: Not recommended. The 24/24 PASS baseline for T1–T22 plus priority validation is the product of **all 19 files**. Uploading fewer will degrade results.

**Q: Upload progress is stuck at 90%**
A: This is typically a network issue. Refresh the page — Claude retains already-uploaded files and you can continue uploading the rest.

---

## 4. Wait for Indexing (Important: you don't actually need to wait)

After upload completes, the UI will show an "**Indexing**" indicator that can run for **30–60 minutes** or longer.

### Do not actually wait for Indexing to finish

Observed in practice:
- The Indexing indicator is **unreliable**: even while it shows as still indexing, querying immediately can already retrieve new content
- Waiting the full cycle means 60+ minutes, and the UI may even report an indexing failure requiring a retry
- The correct way to verify a deployment is to **ask 1–2 questions directly** (next step) — a successful hit means it's ready

So once the upload is complete, go straight to §5 Smoke Test.

---

## 5. Smoke Test (3 questions, ~5 minutes)

Open a new chat in the Project and ask the following 3 questions in order, checking each answer against the expected result.

### T1: Variable definition query (most basic)

**Question**: `What is the Core attribute of AE.AEDECOD? Which chapters does it reference?`

**Expected**:
- Core = **Required** (or Req)
- Source citations: `05_mega_spec.md §AE` + `04_variable_index.md (Sy/R)` + `02_chapters.md §4.3.6` (three-part structure AETERM/AEMODIFY/AEDECOD)
- Mention of AEPTCD as a companion variable

If Claude answers Core=Permissible or cannot cite a chapter number, Indexing has not yet taken effect — wait 5–10 minutes and try again.

### T17: Codelist term table query (RAG depth)

**Question**: `What are all the Term values for the C66742 codelist?`

**Expected**:
- 4 Terms: **C49487 N / C48660 NA / C17998 U / C49488 Y**
- Extensible: **No**
- Lists 41 Related Domains (AE/AG/BS/CE/...)
- Source tags: `11a_terminology_high_core.md` + `02_chapters.md §4.3.7`

If Claude gives Y/N/U/NA but not the C-codes, `11a` was not retrieved by RAG — verify that `11a` was uploaded successfully.

### T22: Giant codelist boundary recognition (stub verification)

**Question**: `What are the Term values for the C65047 codelist?`

**Expected** (this is the most critical boundary test):
- Claude should **declare** that "C65047 is a Laboratory Test Code containing 2,536 terms; at this scale the Project does not include a complete enumeration of all Term values"
- Source citations: `13a_terminology_tail_core.md` (stub definition) + `../../../knowledge_base/terminology/core/lb_part*.md` (source files) + NCI EVS Browser entry point
- **Zero hallucination**: no specific term values should be listed (if Claude does list terms, that is a hallucination and must be debugged)

If Claude attempts to list terms or says "I don't know," the Stage 6 Deferred stub rule in the System Prompt has not taken effect — re-verify that the System Prompt includes the v2.6 stage.

### Release v1.0 full demo
In addition to T1/T17/T22 above, release v1.0 provides a 10-question full demo (including anti-hallucination probes) at [../DEMO_QUESTIONS.md](../DEMO_QUESTIONS.md). For colleague onboarding, the recommended starting point is D0 + D1 + D6 (3 questions, ~5 minutes).

---

## 6. Full Regression Test (optional, 24 questions, ~40 minutes)

To confirm "my deployed Project is equivalent to the project baseline Project":

1. Open `../../claude_projects/dev/test_results.md` from the repository
2. Ask questions T1 → T22 + T-core-reb + T-supp-reb in order (24 questions total)
3. Compare Claude's answers against the v2.6 final-state answers recorded in the matrix
4. All consistent = deployment PASS; any deviation = log the A/B difference — likely caused by a fresh upload or indexing state variation

Recommendations:
- **One question per new chat** (avoids context contamination)
- Allow ~20–30 seconds for the first token per question; if there is no response after 60 seconds, rate limiting may have triggered — wait a minute and retry
- Pay particular attention to **T3** (cross-batch RELREC) and **T7/T17** (C66742 exact-text hit) — these two verify that RAG can retrieve across files

---

## 7. Troubleshooting Guide

| Symptom | Likely cause | Resolution |
|---------|-------------|------------|
| All queries answered with "I don't know" | System Prompt not fully pasted | Verify Custom Instructions contains all 6 Stage sections, especially Stage 6 |
| Wrong chapter numbers returned (e.g., §4.3.6 when §4.3.7 is correct) | `02_chapters.md` not uploaded or truncated | Re-upload `02_chapters.md`; verify file size > 200 KB |
| T22 C65047 lists specific term values (hallucination) | Stage 6 Deferred stub rule not active | Check System Prompt Stage 6 section + verify `13a_terminology_tail_core.md` is uploaded |
| CT code queries return only `08` instead of `11*`/`12*`/`13*` | CT query priority rule missing | Verify System Prompt tail contains `CT query priority 11*>12*>13*>08` |
| Capacity UI exceeds 85% with a warning | Anthropic policy change | Remove in this priority order: 13c > 12c > 12b > 11c (keep `11a`/`11b`/`09`/`05`/`02` core files) |
| Slow responses / frequent rate limiting | Pro plan RAG rate limiting | Wait 30–60 seconds and retry; if persistent, consider upgrading to Team/Enterprise |
| ~44% of questionnaires (quest) codelist queries unanswered | Release build covers only 55.8% of quest (by design) | Expected behavior; the long-tail 296 quest codelists are deferred to a future Phase 7 RAG pipeline |

---

## 8. Upgrade / Downgrade Path

### To increase coverage (optional, not done by default)

- Push quest coverage from 55.8% to ~80%: requires adding a batch of quest tail extractions (+~180K tokens), estimated capacity ~85%
- Replacing the 6 giants (MedDRA-scale codelists) from Deferred stub to inline: requires +500K tokens, which would directly hit the hard ceiling — not recommended

### To reduce footprint (when capacity is insufficient)

Remove in this priority order (retaining the most useful files):
1. First remove `13c_terminology_tail_supp.md` (43K, supp long-tail)
2. Then remove `13a_terminology_tail_core.md` (146K, but contains 6-giants stub — removing it will cause T22 to FAIL)
3. Then remove `12c_terminology_mid_supp.md` (23K)
4. Then remove `12b_terminology_mid_questionnaires.md` (225K)
5. Then remove `12a_terminology_mid_core.md` (130K)

Minimum viable baseline: `11a/b/c_terminology_high_*` + `09/10_examples_data_*` + `00–08` core structure = ~800K tokens / ~50% capacity.

---

## 9. Team Collaboration

- Knowledge uploads in Claude Projects are **per-Project** and cannot be shared across Projects
- Members within a Team/Enterprise plan share the same Project and see the same Knowledge (not individual forks)
- If a team member modifies the System Prompt or deletes a file, **everyone** is affected; it is recommended to restrict edit permissions to 1–2 people
- "Publish to a public link" is not supported: for external users, each person must follow this tutorial and set up their own copy

---

## 10. Future Paths

- This release build is the **complete final state**; no further capacity expansion is planned in the near term
- The long-tail 302 codelists (296 quest + 6 giants) are allocated to a future Phase 7 self-hosted RAG pipeline (design document: `../../claude_projects/docs/` in this repository)
- If Anthropic releases a new plan or larger capacity, re-evaluate whether pushing to 85–90% is worthwhile
- If knowledge base content gaps or errors are discovered during use of the release build, report them to the project issue tracker; the release build will be rebuilt after knowledge base updates

---

## Appendix: Deployment Verification Checklist

- [ ] Claude Pro or higher plan is active
- [ ] Project created with a clear name
- [ ] Custom Instructions contain the complete System Prompt (all 6 Stage sections)
- [ ] Project Knowledge panel shows 19 files uploaded
- [ ] T1 AEDECOD Core query PASS (answers Req + cites §4.3.6/§4.3.5)
- [ ] T17 C66742 term table query PASS (4 terms + 41 related domains)
- [ ] T22 C65047 giant boundary query PASS (declares stub, zero hallucination)
- [ ] UI capacity shows ~77% (normal range)

All boxes checked = deployment successful, ready for daily use.

---

*v1.0 — 2026-04-27 — Company Release*
*Methodology details: ../../claude_projects/docs/ ; Release v1.0 overview: ../README.en.md*
