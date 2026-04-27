# Known Limitations — SDTM AI Knowledge Base v1.0

> Maintained as a single English file. Each limitation lists: which platform(s) it affects, the evidence/reproduction, and the recommended workaround.

## Cross-Platform Limitations

### L1 — Questionnaires (QS) codelist coverage incomplete

**Affects**: All 4 platforms (most pronounced on Claude Projects v2.6).
**Detail**: 296 long-tail QS codelists (PROMIS / EORTC item-bank style) are not fully expanded in any deployment due to capacity constraints. Claude Projects covers ~55.8% of QS codelists; the rest fall back to NCI EVS Browser links.
**Workaround**: For QS codelist queries beyond the covered subset, ask the AI to point you to the NCI EVS Browser URL (the AI will recognize it has only a stub). Phase 7 self-hosted RAG will close this gap.

### L2 — Giant codelists (LB / MedDRA-tier) returned as stubs, not full term lists

**Affects**: All 4 platforms.
**Detail**: 6 giant codelists (e.g. LB Test Code C65047 with 2,536 terms) are stored as stub-with-pointer rather than enumerated. Asking "list all terms of C65047" should return a stub declaration + NCI EVS Browser link, NOT a fabricated term list.
**Workaround**: Acceptable behavior. If a platform fabricates terms here, it's a hallucination — re-check the system prompt's Stage 6 Deferred Stub rules (Claude) or equivalent anti-fabrication anchor.

### L3 — Real-Time Web Lookup (FDA / Pinnacle 21 / dbSNP / NCI EVS) not embedded

**Affects**: NotebookLM (in-KB-only architecture); ChatGPT/Gemini/Claude can web-search if enabled.
**Detail**: For breaking standards updates (e.g. Dataset-JSON catalog status, Pinnacle 21 rule release notes), the in-KB content reflects state as of 2026-04-22 baseline.
**Workaround**: Cross-check time-sensitive answers on CDISC.org / FDA.gov / standards.pinnacle21.certara.net manually. The AI will normally cite its source; if the citation is older than 6 months, double-check.

## Per-Platform Limitations

### Claude Projects (v2.6)

- **L4-Cl1**: Capacity at ~77% (1.29M tokens / 19 files). Approaching paid-tier soft cap. Adding more content requires removing existing low-priority files (see UPLOAD_TUTORIAL §8 降级路径).
- **L4-Cl2**: Indexing indicator unreliable. Even when UI shows "Indexing", queries can hit new content. Don't wait — test directly with smoke questions.
- **L4-Cl3**: No public sharing link. Team/Enterprise plan members share the same Project; Pro plan users must re-deploy individually.

### ChatGPT GPTs (v2.2 LIVE)

- **L4-CG1**: 20-file hard limit. Current deployment uses 9 files (room to grow). Source files are merged (e.g. all 63 domain specs into one `04_domain_specs_all.md`).
- **L4-CG2**: File search RAG chunk strategy not user-configurable. Some long-tail terminology queries may miss chunks if buried mid-table.
- **L4-CG3**: GPT Store publication requires OpenAI review. Custom GPT can be shared to org/team without review (recommended for company-internal use).

### Gemini Gems (v7.1 LIVE)

- **L4-GE1**: Only 4 uploaded files (most aggressive merge). Larger context window compensates but may slow first-token latency on cold sessions.
- **L4-GE2**: Personal-account binding. Gem cannot be shared to a team out of the box (Workspace plan offers some sharing). Each colleague self-deploys.
- **L4-GE3**: Lower baseline anti-hallucination strictness vs. Claude/NotebookLM. R1→R2 upgrade (v6→v7 system prompt) brought it from 65% to 94%; **all colleagues deploying must use the v7.1 system prompt verbatim** to inherit the AHP guardrail.

### NotebookLM

- **L4-NB1**: 50-source hard cap (Pro plan). Current deployment 42/50, 8 source headroom.
- **L4-NB2**: In-KB-only by design. Cannot answer questions about content NOT in the 42 sources (e.g., breaking news after deployment date). On the upside, this gives natural anti-hallucination protection.
- **L4-NB3**: Q9 (Pinnacle 21 categories) PUNT — NotebookLM safely declares "not in this knowledge base" rather than answering from Pinnacle 21 webpages. This is **correct safety behavior**, not a bug.
- **L4-NB4**: Sources panel ≠ Chat. Questions go in Chat (mat-input-0), not in "Discover sources" search.
- **L4-NB5**: Q11 (Dataset-JSON v1.1) and Q12 (CT version locking + MedDRA) are PARTIAL — supplemental topics outside the 42 sources' scope. PUNT is the safe answer; if the platform attempts a confident answer here, treat with caution.

## Question-Type Performance Reference

Based on SMOKE_V4 R1+R2 results (2026-04-22 to 2026-04-24):

| Question Type | Claude | ChatGPT | Gemini (R2) | NotebookLM |
|---|:---:|:---:|:---:|:---:|
| New domain (GF/CP/BE/BS) | PASS+ | PASS | PASS | PASS+ |
| Domain boundary (LB/MB/IS) | PASS+ | PASS | PASS+ | PASS |
| Timing model (--TPT) | PASS | PASS | PASS | PASS |
| CT mechanism (Ext + dictionary) | PASS+ | PARTIAL→PASS (post v2.2) | PASS | PASS+ |
| Premise correction (SUPPTS) | PASS+ | PASS | PASS+ (post v7.1) | PASS+ |
| Anti-hallucination (LBCLINSIG) | PASS+ | PASS | PASS+ (post v7) | PASS+ (in-KB-only) |
| Anti-hallucination (SAE Aggregate) | PASS | PASS | PASS+ | PASS+ |
| Deprecated PF | PASS+ | PASS | PASS+ | PASS+ |
| Cross-domain death timing | PASS+ | PASS | PASS | PASS |
| Real-time / supplemental (Q11/Q12) | PASS | PASS | PARTIAL | PUNT (correct) |

## Reporting New Limitations

If you encounter a hallucination, factual error, or scope gap not covered above:
1. Save the full question + AI response (screenshot + text).
2. Note which platform + version (e.g., "ChatGPT GPT v2.2 LIVE 2026-04-24").
3. Email Daisy / open a project tracker issue with the above attached.
4. Include expected vs actual: cite the SDTMIG v3.4 spec section or CDISC CT C-code.

We track these in `ai_platforms/release/v1.0/CHANGELOG.md` for the next minor release.
