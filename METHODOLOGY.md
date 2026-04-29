# Methodology — How This Knowledge Base Was Built and Why You Can Trust It

> Last updated: 2026-04-29 · Maintained alongside the build itself, not as marketing copy.

The natural first reaction to an AI-extracted SDTM knowledge base is *"did it hallucinate, did it skip pages, did anyone actually verify this?"* This page is the answer. It documents what was done, what is traceable, what was found wrong along the way, and how you can audit any specific answer yourself.

If you only read one section, read [§4 — Verification and known issues](#4-verification-and-known-issues).

---

## 1. Sources of truth

Every artifact in `knowledge_base/` traces back to one of four official CDISC publications. Nothing in this repository is generated from third-party summaries or paraphrased standards.

| Source | Version | Scope |
|---|---|---|
| SDTM Implementation Guide PDF | v3.4 (2021-11-29) | 461 pages — domain specs, assumptions, examples |
| SDTM Model PDF | v2.0 Final (2021-11-29) | 74 pages — conceptual model |
| SDTMIG xlsx | v3.4 | 1,917 variables across 63 domains |
| CDISC Controlled Terminology xlsx | 2024 release | 1,005 codelists / 37,939 terms |

The originals are not redistributed in this repository (CDISC copyright). See [DISCLAIMER.md](DISCLAIMER.md).

## 2. How it was built

A seven-phase pipeline. Each phase has its own plan, execution log, and verification record under `.work/` — they are part of the repository, not a separate documentation site.

| Phase | What happened | Primary output |
|---|---|---|
| 1 | xlsx → Markdown via Python | 63 `spec.md` files + terminology |
| 2 | PDF page indexing (programmatic, not visual) | `.work/02_indexing/page_index.json` |
| 3 | AI-assisted extraction from PDF, in 11 batches | per-domain `assumptions.md` + `examples.md` |
| 4 | Supplementary content extraction | 6 model files + 6 chapter files |
| 5 | Full validation pass + master index | `INDEX.md` + verification reports |
| 6 | Retrieval optimization (routing, reverse index) | `ROUTING.md` + `VARIABLE_INDEX.md` (1,523 variables) |
| 6.5 | AI platform deployment | 4-platform release bundle (`ai_platforms/release/v1.0/`) |

A separate **literal-level deep verification audit** runs as an ongoing track (`.work/06_deep_verification/`). It compares every atomic claim in the knowledge base against the source PDF, page by page. As of 2026-04-29 the audit has reached **97% coverage of the in-scope pages** and is still running.

## 3. Traceability — how to audit any single answer

The repository is deliberately structured so that a reader can spot-check the knowledge base against the PDF in seconds. There is no "trust me" layer.

**To verify a domain-level answer:**

1. Note the domain code in the answer (`AE`, `LB`, `DM`, …).
2. Open `knowledge_base/domains/<DOMAIN>/`:
   - `spec.md` — variable-level specification (sourced from xlsx, Core / type / codelist binding)
   - `assumptions.md` — domain-specific business rules (sourced from PDF)
   - `examples.md` — implementation examples (sourced from PDF)
3. Each file's header references the relevant PDF page range. Cross-check against the SDTMIG v3.4 PDF.
4. For variable Core / codelist binding, verify against the SDTMIG xlsx if you have it.

**For a chapter-level answer:** open `knowledge_base/chapters/chXX_*.md`. The page range and section numbers match the PDF table of contents directly.

**For a terminology answer:** every codelist file in `knowledge_base/terminology/` carries the CDISC C-code (e.g. `C66731`) so it can be cross-checked against the NCI EVS Browser.

The full source-to-output map is at [`docs/TRACEABILITY.md`](docs/TRACEABILITY.md).

## 4. Verification and known issues

Two systemic issues were caught during the validation phase and are publicly documented. They are not hidden because they are the most useful evidence that the verification process actually works.

### Issue 1 — Page index drift (2026-04-15, resolved)

The first pass at PDF image and figure indexing relied on AI agents visually identifying page numbers. Spot-checking by a domain expert revealed that the page references for the TD example were off by 4 pages, and similar drift (±2–4 pages) was distributed across roughly 60 figures.

**Root cause:** AI agents reading a PDF cannot reliably observe page boundaries — they estimate. The pipeline did not distinguish "exact value" from "estimated value."

**Fix:** the page index was rebuilt programmatically — `page_index.json` is now the single authoritative source, all downstream files reference it, and any AI-produced page estimate is now labelled `(estimated)` rather than written into the index.

**Full investigation:** [`.work/03_verification/issue1_investigation.md`](.work/03_verification/issue1_investigation.md)

### Issue 2 — Skeleton-only content marked as PASS (2026-04-15, resolved)

`ch04_general_assumptions.md` was marked PASS in the first validation pass even though approximately 30% of its subsections contained only one or two sentences of placeholder text with `<!-- 待补全 -->` markers. The PDF contains 38 pages of detailed rules; the file at the time contained roughly 9 lines per page. The post-fix version contains roughly 17 lines per page.

**Root cause:** the PASS criterion accepted *"missing content has been clearly marked as missing"* as a substitute for *"content is complete."* In addition, the same agent both wrote and approved the file — there was no independent reviewer reading the PDF.

**Fix:** every flagged subsection was rebuilt from the source PDF. The PASS criterion was rewritten to require quantitative coverage (lines-per-page ratio against a baseline, zero placeholder markers, ≥95% point coverage). From then on, the agent that writes a file cannot be the same context that approves it.

**Full record:** [`.work/03_verification/issues_found.md`](.work/03_verification/issues_found.md)

### Standing limitations

Some limitations cannot be fully resolved within the AI-platform deployment (giant codelists stored as stubs, real-time external lookups not embedded, etc.). They are tracked separately and acknowledged in the deployment artifacts: [`ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md`](ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md).

## 5. Independent review process

The two issues above produced four standing rules. They are enforced for every phase of every track in this repository.

1. **Quantitative PASS criteria.** Coverage ratios, lines-per-page ratios, zero placeholder markers — not subjective "looks right."
2. **Author and reviewer must be separate.** The agent or process that writes a file cannot be the one that approves it. Reviewer agents read the source PDF independently and produce a structured coverage report.
3. **AI estimates must be labelled.** Anything an AI cannot programmatically confirm is marked `(estimated)` rather than written into an authoritative index.
4. **Human spot-check is part of the workflow.** A random sample is reviewed against the source PDF at every phase close — not as a one-time afterthought.

The four rules and the failure cases that produced them are documented at [`.work/meta/retrospective.md`](.work/meta/retrospective.md).

In addition, the verification track itself is iterative — the deep-verification audit (§2) has been through 14 review rounds at the time of writing, with each round documented under `.work/06_deep_verification/evidence/checkpoints/` and discrepancies pushed back into the knowledge base.

## 6. What this means for you

- **Skepticism is welcome.** Locate the source page in seconds; if a number feels off, you can confirm or refute it directly against the PDF.
- **Discrepancies should be reported.** If the deep-verification audit missed something, please open a GitHub issue. The audit track is open-ended.
- **Not a regulatory substitute.** This knowledge base is an aid for engineers, programmers, and reviewers working with SDTM. For regulatory submissions, always defer to the official CDISC publications.

---

**Repository:** https://github.com/hakupao/sdtm-pedia
**Live site:** https://sdtm-pedia.pages.dev
**License:** CC BY 4.0 — see [LICENSE](LICENSE) and [DISCLAIMER.md](DISCLAIMER.md).
