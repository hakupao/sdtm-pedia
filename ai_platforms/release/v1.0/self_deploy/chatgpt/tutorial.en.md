# ChatGPT GPT Creation Tutorial — SDTM Knowledge Base Release

> Build from scratch a Custom GPT that can look up CDISC SDTM standards (63 domains + terminology + chapters).
> After completing this tutorial you will have: a working ChatGPT GPT that accurately answers SDTM variable definitions / codelists / examples / cross-domain associations, and can detect common fabricated premises (e.g. LBCLINSIG / SUPPTS / PF deprecated).
> Total time: **30–60 minutes** (including indexing wait).

---

## 0. Prerequisites

- [ ] **ChatGPT Plus / Team / Enterprise** subscription (free tier cannot create Custom GPTs)
- [ ] **Web access** to [chatgpt.com](https://chatgpt.com): this tutorial is entirely Web UI based
- [ ] **Local clone of this repository**: you need to read `./system_prompt.md` (~8.6 KB) and the 9 .md files under `./uploads/`

**About "team sharing vs. GPT Store public publishing"**:
- Org/Team subscriptions can invite members directly, **no review required**
- GPT Store public publishing requires OpenAI review (typically 1–3 business days); any ChatGPT user can then access it

---

## 1. Create Custom GPT

1. Log in to [chatgpt.com](https://chatgpt.com)
2. Click "**Explore GPTs**" in the bottom-left → click "**+ Create**" in the top-right
3. Go to the **Configure** tab (not the conversational Create tab)
4. **Name**: recommended `SDTM Expert` or `CDISC SDTM Knowledge`
5. **Description** (one English sentence, ~130 characters): `CDISC SDTMIG v3.4 + SDTM v2.0 Expert — Variable definitions, rule reasoning, controlled terminology, cross-domain linking.`
6. **Capabilities**: disable **Web Search / Code Interpreter / DALL-E** (this GPT is pure knowledge Q&A; enabling these expands the hallucination surface)

---

## 2. Configure Instructions (System Prompt)

1. Still on the Configure tab, locate the "**Instructions**" box
2. **Copy the full contents** of `./system_prompt.md` (v2.2 LIVE, 8,582 chars) and paste them in
3. **Do not truncate**: the ChatGPT UI character indicator shows an 8,000-char limit, but in practice it accepts 8,582 chars (verified, deployed and running). If your ChatGPT UI rejects it, first try removing the §Conversation Starters section (non-core)
4. **Save**

**v2.2 LIVE key capabilities** (preserve after pasting, do not edit):
- GFINHERT 7-letter exact spelling (fixes R1 GFINHERTG extra-G spelling drift)
- L858R / Exon 19 scientific consistency active detection (anti-hallucination bonus)
- 3 anti-hallucination anchors (variable-level / cross-domain / deprecated)

---

## 3. Upload 9 Knowledge Base Files

1. On the Configure tab, find the "**Knowledge**" panel and click "**Upload files**" or drag and drop
2. Select **all 9 .md files** under `./uploads/`, in order: `01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09`
3. **Do not rename / do not split or merge**: file name prefixes are routing anchors in the System Prompt

**File list (9 files, total ~2.5M tokens)**:
- `01_navigation.md` (~46K) — ROUTING + INDEX + VARIABLE_INDEX
- `02_chapters_all.md` (~60K) — SDTMIG ch01/02/03/04/08/10
- `03_model_all.md` (~17K) — SDTM v2.0 Model 6 sections
- `04_domain_specs_all.md` (~185K) — all 63 domain specs, equal weight
- `05_domain_assumptions_all.md` (~54K) — 63 domain assumptions
- `06_domain_examples_all.md` (~220K) — 63 domain examples
- `07_terminology_core_high_freq.md` (~200K) — core high-frequency 15 codelists
- `08_terminology_quest_and_supp.md` (~1M) — questionnaires + supplemental
- `09_terminology_core_mid_tail.md` (~698K) — core mid-to-tail segment

ChatGPT GPT Builder Knowledge has a **20-file hard limit**; current count is 9/20 (11 files headroom).

**Common questions**:
- "File too large" → check whether your editor accidentally added BOM / CRLF; re-save as UTF-8 LF
- Upload stuck at 90% → network issue; refresh the page (already-uploaded files are retained; resume uploading the remaining ones)

---

## 4. Wait for Indexing

ChatGPT File Search RAG indexing typically takes **5–15 minutes**. Each file's status in the UI transitions from "Processing..." to "Ready". Proceed to §5 only after all files show Ready.

Note: there is no explicit "all indexing complete" indicator; a single file showing Ready means that file is available.

---

## 5. Smoke Test (3 Questions, ~5 min)

Click **Preview** in the top-right. Ask each question in a **new chat**:

| # | Question | Expected key points | What is being verified |
|---|----------|---------------------|------------------------|
| T1 | `What is the Core attribute of AESER? List all term values in the NY codelist (C66742).` | Core = **Exp** (not Req); 4 terms: **Y / N / U / NA** + C-code | Most common mistake + high-frequency codelist hit |
| T2 | `What variable is GFINHERT? Which domain does it belong to?` | GF (Genomics Findings, v3.4 new domain); INHERT stands for Inherited; exactly 7 letters (not GFINHERTG) | v3.4 new domain recognition + v2.2 spelling fix |
| T3 | `Which codelist does LBCLINSIG belong to?` (fabricated variable) | GPT should **detect the fabrication**: LBCLINSIG does not exist in the LB domain v3.4 spec; suggest LBNRIND / LBSTRESC instead | AHP1 anti-hallucination |

**3/3 PASS** = deployment successful; any FAIL → see §7 Troubleshooting.

---

## 6. Full Regression (10 Questions, Optional ~30 min)

Open [`../DEMO_QUESTIONS.md`](../DEMO_QUESTIONS.md) and submit questions D0–D9 (10 demo questions) one by one. Use a **new chat per question** to avoid context contamination. Score ≥ 8/10 = equivalent to the baseline release version.

---

## 7. Troubleshooting Guide

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Answers GFINHERTG (extra G) | Instructions are not v2.2 LIVE | Check whether the "v3.4 new domain variable name exact validation" section is present at the end of system_prompt.md |
| Answers PF domain variable list (PF deprecated) | AHP3 anchor not effective | Re-check system_prompt §CO-5 AHP-V3 + anti-fabrication section |
| Answers "SUPPTS is a dataset" | SUPP scope section missing | Check that system_prompt §SUPP scope is complete (SUPPQUAL does not apply to Trial Design) |
| File Search recalls wrong passage | File segmentation failure | Check whether system_prompt §P13 TableAware hint is present; re-upload the problematic file |
| Answers "AESER Core = Req" | 04_domain_specs_all.md not uploaded / truncated | Re-upload; verify file size ≥ 180 KB |
| Warning about ≥ 20 files uploaded | GPT Builder hard limit triggered | Remove files following the downgrade path in §8 |
| Slow first token / frequent rate limiting | Plus subscription RAG rate limiting | Wait 30–60 seconds and retry; if persistent → upgrade to Team/Enterprise |

---

## 8. Upgrade / Downgrade Path

**Upgrade (expand KB)**:
- Current count: 9/20 files, 11 files headroom
- When adding v3.5 SDTMIG new domains / questionnaires long-tail content, add a bucket in `dev/scripts/` → merge → upload incrementally

**Downgrade (capacity warning)**:
Remove files in this priority order (most useful retained last):
1. Remove `09_terminology_core_mid_tail.md` first (mid-to-tail low-frequency)
2. Then remove `08_terminology_quest_and_supp.md` (questionnaires long-tail)
3. Then remove `06_domain_examples_all.md` (examples)

Minimum retained baseline: `01–05 + 07` (navigation + chapters + model + spec + assumptions + high-frequency CT) = 6 core files.

---

## 9. Team Collaboration / GPT Store Publishing

**Org/Team sharing**:
- No review required; invite members directly by email
- All members see **the same GPT**; changes to Instructions take effect for everyone immediately
- Recommend restricting edit permissions to 1–2 people to prevent accidental edits

**GPT Store public publishing**:
- Requires OpenAI review (~1–3 business days)
- Accessible to anyone on the internet; suitable for an open knowledge base
- Ensure the Name / Description does not contain sensitive keywords or internal company identifiers

---

## 10. Future Paths

- This release is already a **complete final state**; no capacity expansion is planned in the near term
- Long-tail questionnaires + 6 MedDRA-level giant codelists are deferred to a future Phase 7 self-built RAG
- If you find errors or gaps in the knowledge base, report them to the project issue tracker; the release build will be rebuilt after fixes

---

## Appendix: Verification Checklist

- [ ] ChatGPT Plus / Team / Enterprise subscription is active
- [ ] Custom GPT has been created with a clear name
- [ ] Instructions contain the complete system_prompt.md (v2.2 LIVE, 8,582 chars)
- [ ] Knowledge panel shows all 9 files as Ready
- [ ] T1 AESER + C66742 smoke PASS
- [ ] T2 GFINHERT exact spelling PASS (not GFINHERTG)
- [ ] T3 LBCLINSIG anti-fabrication detection PASS

All ☑ = deployment successful; you can begin daily use.

---

*v1.0 — 2026-04-27 — Company Release*
