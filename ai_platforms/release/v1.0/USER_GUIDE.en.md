# SDTM AI Knowledge Base — User Guide v1.0

## 1. What This Is (Project Background)

If you need to look up CDISC SDTM variable definitions / Core / codelist, flipping through SDTMIG v3.4 PDF + NCI EVS Browser usually takes 10+ minutes. This project organizes all that material and deploys it to 4 AI platforms (Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM). You just ask in natural language and **get answers with spec citations in 1 minute**.

Technical background: SDTM (Study Data Tabulation Model) covers 63 domains + thousands of variables + extensive CT (Controlled Terminology). We organized CDISC SDTMIG v3.4 + v2.0 model + CDISC CT into 295 Markdown sources, then fed them to 4 AI platforms with prompt engineering. New to terms like RAG / system prompt / Core (Req/Exp/Perm) / Extensible / anti-hallucination probe? See [`./GLOSSARY.en.md`](./GLOSSARY.en.md) (1-page lookup).

## 2. What We Built (Technical Highlights)

We tested each platform with 17 representative SDTM questions, including 3 "deliberately wrong premise" anti-hallucination probes (testing whether the AI catches false premises rather than playing along). The 4-platform scorecard:

| Platform | 17-Q score | Version | Strengths |
|---|:---:|:---:|---|
| Claude Projects | 17/17 (100%) | v2.6 | Precise variables + multi-step reasoning |
| ChatGPT GPTs | 16.5/17 (97%) | v2.2 LIVE | Full coverage + shareable within teams / GPT Store |
| Gemini Gems | 16/17 (94%) | v7.1 LIVE | Long context + broad exploratory queries |
| NotebookLM | 15/17 (88%) | Custom mode | in-KB-only anti-hallucination |

Highlights: v3.4 new domains (GF / CP / BE / BS), Timing rules, CT Extensible handling, SUPPQUAL scope, cross-domain death-date alignment, and 3 anti-hallucination questions (LBCLINSIG / Trial-Level SAE Aggregate / PF deprecated domain). Throughout, quality was enforced with 4 internal quality rules + 28 independent reviewers cumulative. Sources: `./CHANGELOG.md` and `../../SMOKE_V4.md` §3. Glossary: [`./GLOSSARY.en.md`](./GLOSSARY.en.md)

## 3. Which Platform Should I Use? (Decision Tree)

| What you want to do | Recommended platform | Why |
|---|---|---|
| Precise variables + multi-step reasoning (Core + C-code + cross-variable) | **Claude Projects** | 1.29M tokens full coverage, perfect smoke score |
| Share with your team or department, or publish to GPT Store | **ChatGPT GPTs** | Org-internal sharing requires no review; GPT Store goes through OpenAI review |
| Large context + one-shot broad exploration / cross-domain pattern queries | **Gemini Gems** | 1M context window, 4-file deep merge |
| Maximum anti-hallucination (decline to answer rather than fabricate) + strong citation | **NotebookLM** | in-KB-only; if it's not in the 42 sources, it will PUNT rather than guess |

Short version: Not sure which to pick? Start with Claude Projects. Bringing colleagues along? Use ChatGPT GPTs. Worried about hallucinations? Use NotebookLM. For a detailed comparison see the "Four-Platform Roles" table in `../README.md`.

## 4. Access Links for All 4 Platforms

### 4.1 Claude Projects (Recommended Starting Point)

- **Access**: Wait for Daisy to add you to the organization — join via the email invite link.
- **URL**: claude.ai → Projects → "SDTM Knowledge Base" (Daisy will send the specific URL directly).
- **Subscription required**: Claude Pro / Team / Enterprise.
- **Best for**: Precise variable Core + CT lookups, cross-variable reasoning (e.g., the PCTPT five-variable set), correcting wrong premises (e.g., SUPPTS).
- **Not ideal for**: Real-time lookups on FDA / Pinnacle 21 (verify manually at cdisc.org); very large batch domain comparisons.

### 4.2 ChatGPT GPTs

- **Access**: Daisy shares the Custom GPT to your organization; click "Add to My GPTs".
- **URL**: chatgpt.com → top dropdown → "SDTM Knowledge Base".
- **Subscription required**: ChatGPT Plus / Team / Enterprise (Free tier is not supported).
- **Best for**: Full domain queries, team sharing, publishing to GPT Store via OpenAI review.
- **Not ideal for**: Multi-step reasoning (slightly weaker than Claude Projects); Free-tier accounts cannot access the GPT.

### 4.3 Gemini Gems

- **Access**: Daisy shares via Google Workspace, or you can self-deploy (personal account).
- **URL**: gemini.google.com → Gems → "SDTM Knowledge Base".
- **Subscription required**: Gemini Advanced (personal) / Google Workspace.
- **Best for**: Loading large amounts of context at once, cross-domain pattern comparisons, long sessions.
- **Not ideal for**: Personal accounts cannot share directly with a team (requires Google Workspace).

### 4.4 NotebookLM

- **Access**: Daisy invites you to the notebook, or you can create your own (50-source cap).
- **URL**: notebooklm.google.com → "SDTM Knowledge Base".
- **Subscription required**: NotebookLM Pro / Google Workspace.
- **Best for**: Strong anti-hallucination (audit / compliance use), inline citation lookups, preferring "I don't know" over making something up.
- **Not ideal for**: Questions outside the 42 sources (real-time Pinnacle 21, breaking news) — it will decline to answer by design, not a bug.

## 5. 5-Minute Quick Start (3 Warm-Up Questions)

Open your preferred platform (Claude Projects is a good first choice) and ask these 3 questions in order. Compare your answers against the Expected answers in `./DEMO_QUESTIONS.md`:

1. **D0 (Warm-up)**: "What domain and variable is AESER in SDTMIG v3.4? What is its Core attribute? Which CT C-code does it bind to?" Expected: AE domain / Serious Event / Exp / C66742 NY {Y/N/U/NA}.
2. **D1 (New domain)**: Copy the D1 question text from DEMO_QUESTIONS.md (EGFR / Exon 19 / dbSNP). Expected: Domain=GF; should return GFGENSR / GFPVRID / GFGENREF / GFINHERT.
3. **D5 (Wrong-premise correction)**: "What is SUPPTS in the SDTM standard? Is QORIG required?" Expected: The model proactively recognizes that "SUPPTS does not exist in SDTMIG v3.4" and redirects to TSVAL1-TSVALn = PASS+.

Grading: All core facts correct (domain / variable / Core / C-code) = PASS. Proactively catches the wrong premise = PASS+. Follows the wrong premise and fabricates = FAIL.

## 6. Full Demo Package (10 Questions)

The complete 10-question set is in `./DEMO_QUESTIONS.md` (questions in three languages + English grading criteria). 5-minute intro = D0 / D1 / D5; 30-minute full run = D0 through D9 (includes 3 AHP probes: D6 LBCLINSIG / D7 SAE Aggregate / D8 PF deprecated domain + the cross-domain ultimate challenge D9: AE/MH/CE + DS death-date alignment). After running, compare your results against the §2 baselines (17/17 / 16.5/17 / 16/17 / 15/17) to see how your instance performs.

## 7. Known Limitations (Frequently Asked Questions)

Full details are in `./KNOWN_LIMITATIONS.en.md`. Summary:

- **L1 — Incomplete QS codelist coverage**: 296 long-tail questionnaire codelists (PROMIS / EORTC) are not fully expanded due to capacity constraints (Claude ~55.8%); the remainder links out to NCI EVS Browser.
- **L2 — Large codelists stored as stubs**: LBTESTCD (2,536 terms) and 5 other large tables are stored as stubs with pointers only — the model will not fabricate individual terms.
- **L3 — No real-time web access**: NotebookLM is strictly in-KB-only; breaking news and the latest Pinnacle 21 updates are outside its knowledge (it will PUNT). The other 3 platforms can browse the web but require you to enable that manually.
- **Claude**: Capacity is at 77%, close to the Pro soft ceiling; adding new files requires first downgrading lower-priority content.
- **ChatGPT**: Hard 20-file limit (currently using 9); long-tail chunk tables may be partially missed mid-section.
- **Gemini**: Personal accounts cannot share directly with a team (requires Google Workspace); the v7.1 system prompt must be pasted in full.
- **NotebookLM**: 50-source cap (currently 42); Q9 / Q11 / Q12 proactively PUNT — this is **correct and safe behavior**, not a flaw.

## 8. Feedback

If you find an error, hallucination, or off-topic answer: (1) Take a screenshot and save the full original question and AI response. (2) Note the platform and version (e.g., "ChatGPT GPT v2.2 LIVE 2026-04-24") and the expected answer (citing the SDTMIG v3.4 section number or CDISC CT C-code). (3) Email Daisy, file in the company issue tracker, or @Daisy in the department group chat. Issues are consolidated in `./CHANGELOG.md` and addressed in the next minor release.

## 9. Road Map

**Short term (v1.0 maintenance)**: Collect feedback and fix SDTM content errors; quarterly v1.x minor releases. **Medium term (Phase 7 — self-hosted RAG)**: Break free of the 4-platform capacity constraints, enabling all 295 files at full resolution plus complete QS codelist expansion. **Long term**: Keep pace with SDTMIG v3.5+ and extend coverage to ADaM and Define-XML.

---
*v1.0 — 2026-04-27 — Maintained by Daisy*
