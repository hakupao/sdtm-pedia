# Gemini Gem Creation Tutorial — SDTM Knowledge Base Release

> Build from scratch a Custom Gem that can look up CDISC SDTM standards (63 domains + chapters + business scenario ammunition pack).
> After completing this tutorial you will have: a working Gemini Gem that can precisely answer SDTM variable definitions / business scenario mapping / cross-domain associations, and can detect common fabricated premises (3 anti-hallucination anchors (anti-hallucination guard)).
> Total time: **20-40 minutes** (Gemini indexing is much faster than ChatGPT).

---

## 0. Prerequisites

- [ ] **Google AI Pro subscription** (personal plan is sufficient) — free Gemini has no Custom Gem editing access
- [ ] Web access to [gemini.google.com](https://gemini.google.com)
- [ ] **Local clone of this repository**: you need to read `system_prompt.md` (~29.9 KB) and the 4 `.md` files under `uploads/` from `./`

**About plans and team sharing**:
- A personal Google AI Pro subscription can create a Gem, but **does not support team sharing** (Gem is bound to your personal account)
- Workspace plans have Gem sharing capability, but the semantics differ from personal — having colleagues **each deploy separately is the safest path**
- Gemini has no publicly browsable gallery like a "GPT Store" — sharing is link-only

---

## 1. Create a New Custom Gem

1. Sign in to [gemini.google.com](https://gemini.google.com) (using the Google account with your Pro subscription)
2. Left navigation → "**Gems**" → top right "**+ New Gem**" or "**Create a new Gem**"
3. **Name**: recommended `SDTM Expert` or `CDISC SDTM Knowledge`
4. **Description**: `CDISC SDTMIG v3.4 + SDTM v2.0 Expert — Variable definitions, rule reasoning, business scenario mapping, cross-domain.`

---

## 2. Configure Instructions (system_prompt.md)

1. In the Gem Edit interface, locate the "**Instructions**" or "**Custom Instructions**" field
2. **Copy the entire contents** of `./system_prompt.md` (v7.1 LIVE, 29,919 chars) and paste it in
3. **Important**: Gemini accepts instructions **far exceeding 8K characters** (tested up to 30K accepted). Do not manually truncate out of habit from ChatGPT's 8K limit — truncation will drop the anti-hallucination anchors

**v7.1 LIVE key patches (must be preserved after pasting)**:
- **§CO-1d SUPPQUAL Core + scope hard anchor**: QORIG Core=Req / QEVAL Core=Exp / CT C78735; SUPPQUAL does not apply to Trial Design (TS/TA/TE/TI/TV)
- **§CO-1c ARM/ARMCD/ARMNRS** 5 values including NOT APPLICABLE Extensible=Yes
- **§CO-5 AHP-V1/V2/V3** three-tier anti-hallucination guard (variable-level / cross-domain-level / deprecated-level)

---

## 3. Upload 4 Knowledge Base Files

1. Gem Edit → "**Knowledge**" panel → "**Upload files**" or drag and drop
2. Select **all 4 `.md` files** under `./uploads/`, in this order:
   - `01_navigation_and_quick_reference.md` (~124K tokens)
   - `02_domains_spec_and_assumptions.md` (~240K tokens, 63 domain specs + assumptions interleaved within domains)
   - `03_domains_examples.md` (~220K tokens, 63 domain examples)
   - `04_business_scenarios_and_cross_domain.md` (~30K tokens, 26 business scenarios + FAQ)
3. **Do not rename / do not split or merge the files**

Gemini Knowledge has a **10-file hard limit**; the current count is 4/10 (6 files of headroom). Total ~616K tokens occupies approximately 62% of the 1M context window, leaving ~38% response buffer.

---

## 4. Wait for Indexing

Gemini Gem has **no RAG / no chunk retrieval** — after uploading, files are **ready within seconds**, with the full text always in context. File status generally changes to "Ready" within 1-3 minutes, after which you can start chatting.

ChatGPT uses RAG retrieval; Gemini uses full injection — the two have fundamentally different underlying architectures. Do not apply your ChatGPT indexing wait experience here.

---

## 5. Smoke Test (3 Questions, ~5 min)

**Preview** — one new chat per question:

| # | Question | Expected Key Points | Validation Focus |
|---|----------|---------------------|-----------------|
| T1 | `Is the Core attribute of AESER Req or Exp?` | Core = **Exp** (not Req) | CO-1 high-frequency error-prone anchor |
| T2 | `How do the LB / MB / IS domains differ? Where do microbiology culture results belong?` | LB = clinical laboratory (chemistry/blood/urine); MB = microbiology (culture/susceptibility); IS = immunology (antibody/vaccine) | Domain boundary identification |
| T3 | `What is the variable list for the PF domain (Pharmacogenomics Findings)?` (PF is deprecated) | Gem should **detect**: PF was deprecated in v3.4; the current domains are GF (Genomics Findings) / BE (Biospecimen Events) / BS (Biospecimen Findings) + RELSPEC | AHP3 deprecated anti-hallucination (core closure point of R1→R2 upgrade) |

**3/3 PASS** = deployment successful; any FAIL → see §7 Troubleshooting.

---

## 6. Full Regression (10 Questions, ~30 min, Optional)

Open `../DEMO_QUESTIONS.md` and ask questions D0-D9 (10 demo questions). **One new chat per question**. Internal complete 17-question baseline 16/17 (94.1%), all 3 anti-hallucination questions caught; your Gem scoring ≥ 8/10 on these 10 = equivalent baseline.

---

## 7. Troubleshooting Guide (Gemini-specific)

| Symptom | Possible Cause | Resolution |
|---------|---------------|------------|
| ARM answers mix up ARMCD / ARMNRS | §CO-1c anchor not effective | Re-check system_prompt §CO-1c (ARM 5 values listed in full + Extensible=Yes) |
| SUPPQUAL Core answered incorrectly (QORIG=Exp / QEVAL=Req) | §CO-1d v7.1 anchor not active | Re-paste the full system_prompt, confirm §CO-1d section is present |
| Answers with PF / PGx domain variables (deprecated hallucination) | §CO-5 AHP-V3 anchor not effective | Re-check §CO-5 + §Response Spec ⑧ Deprecated concept section |
| Answers with LBCLINSIG (hallucinated variable) | §CO-5 AHP-V1 anchor not effective | Re-check §CO-5 dual-core workflow step 0 + AHP-V1 detection template |
| Slow first token (>10 seconds) | Normal cold-start behavior | Subsequent queries will be faster; if sustained >30 seconds check Google AI status |
| Answers lack citations / source paths | §CO-3 anchor not effective | Re-paste system_prompt §Three Hard Constraints + §Response Spec |
| Knowledge file status stuck at "Processing" | File exceeds 5 MB / encoding issue | Check file 02 (~919 KB, largest); confirm UTF-8 LF without BOM |

---

## 8. Upgrade / Downgrade Path

**Upgrade (expand KB)**:
- Currently 4/10 files, 6 files of headroom
- Terminology long tail (questionnaires) can be added as file 05; SDTMIG v3.5 new domains can be added as file 06
- **No need to downgrade**: current total tokens occupy 62% of the 1M window, with 38% buffer — ample room

**Downgrade (capacity warning, generally not needed)**:
1. First remove `04_business_scenarios_and_cross_domain.md` (business ammunition, but critical for R2 upgrade)
2. Then remove `03_domains_examples.md` (examples)

Minimum retained: `01 + 02` (navigation + spec/assumptions) = 365K tokens.

---

## 9. Team Collaboration

**Gemini Gem does not support team sharing** (unlike ChatGPT GPT):
- A Gem is bound to the personal Google account and cannot be shared by inviting colleagues to the same Gem
- Colleagues each follow this tutorial to deploy their own copy and maintain it independently
- Workspace plans have Gem sharing capability, but the actual semantics are complex — **each person deploying separately is the safest path**
- There is no "Gemini Gem Store" public publishing path — sharing is link-only

---

## 10. Future Paths

- This release is already a **complete final state** and will not be expanded further in the near term
- Long-tail terminology + the Studio trio (Audio Overview / Mind Map / Study Guide) are deferred to the subsequent Phase 7 / NotebookLM complementary track
- If there are errors or omissions in the knowledge base content, report them to the project issue tracker

---

## Appendix: Verification Checklist

- [ ] Google AI Pro subscription is active
- [ ] Custom Gem created with a clear name
- [ ] Instructions field contains the full system_prompt.md (v7.1 LIVE, 29,919 chars)
- [ ] Knowledge panel shows all 4 files as Ready
- [ ] T1 AESER Core=Exp PASS
- [ ] T2 LB/MB/IS domain boundary PASS
- [ ] T3 PF deprecated anti-hallucination detection PASS

All ☑ = deployment successful, ready for daily use.

---

*v1.0 — 2026-04-27 — Company Release*
