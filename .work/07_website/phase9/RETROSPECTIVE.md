# Phase 9 retrospective — Pre-Public-Release Polish + QA Bundle

> **Closed**: 2026-04-30
> **Tier**: 3
> **Daisy ack**: Option D (B + C combined) 2026-04-30 + Lighthouse baseline 91/73/100 "还可以" + 9.14 fix bundle scope F-1+F-3+F-4+F-5
> **Outcome**: effective PASS post 9.14 fix bundle (CONDITIONAL_PASS H=1 M=4 L=4 → PASS)

This is the Rule C-mandated retrospective. Three sections (保留下来的做法 / 必须补上的缺口 / 关键决策复盘) per `~/.claude/CLAUDE.md` rule C.

---

## §1 保留下来的做法 (R-P9-*)

- **R-P9-1 Pre-flight archeology saves a half-day of redundant work.** Phase 8→9 handoff named "Phase 9 = Downloads Pipeline" but `git log --follow web/scripts/build-bundles.sh` + `gh release view v1.0` revealed `2de87c4` (4-28 Phase 8.1+8.2 = build-bundles.sh + RELEASE.md + downloads.json) and `8e7bd83` (4-28 Phase 8.3 = GH Release `v1.0` LIVE + DownloadsSection feature flag flipped) already shipped. Without this archeology, Phase 9 would have either re-cut the immutable v1.0 tag (catastrophic) or written redundant code. Pattern locked: **open-phase pre-flight should always include "what's already shipped" archeology when the handoff names a specific master plan section**. C-P8-7 process improvement materialized.

- **R-P9-2 Same-edit-family bundle commit cadence.** 12 cheap polish tasks (9.1-9.12) combined into 1 commit `e89da8a` rather than per-task commits (Phase 6 had 5, Phase 7 had 4, Phase 8 had 2). Reasoning: tasks were small (~5-30 LOC each), independent, tested in same vitest+e2e lane. Commit message lists all 12 tasks + carryover IDs absorbed for git-archeology. **Pattern: scope-driven commit cadence — 1 commit when changes are small + independent + tested in same lane; multiple commits when changes are sequential or risk-isolated.**

- **R-P9-3 Reviewer brief D-dimension structure carries forward across 3 phases.** Phase 7 R-P7-1 → Phase 8 R-P8-1 → Phase 9 R-P9-3: structured `task_N_M_reviewer_prompt.md` with explicit D1-D7 stress dimensions adapted to phase surface. Phase 9's D2 ("SearchOverlay a11y completeness") explicitly asked about new i18n strings — reviewer's F-1 HIGH (English "1 results" pluralization) was caught BECAUSE the brief asked for it. **Brief structure is doing real work, not ceremony.**

- **R-P9-4 Rule A spot-check materialized as concrete pattern.** Phase 7 G-P7-7 said "Rule A rubric expansion for translation work" was a process gap; Phase 9 reviewer concretely applied it: "6 new strings × 3 langs spot-checked: zh ✓ / ja ✓ / en F-1 = 1/6 = 17% error rate". The 17% rate proves Rule A spot-check warranted on this surface. **Pattern: when a phase adds ≥3 new translatable strings, the reviewer brief should EXPLICITLY ask for Rule A semantic spot-check on the new keys (not just key parity).**

- **R-P9-5 Tool-automatable / tool-unavailable QA split.** Lighthouse via chrome-devtools MCP `lighthouse_audit` ran in main session (real numbers 91/73/100, evidence preserved at `web/qa/`). Safari/Firefox cross-browser left as Daisy manual checklist (browsers not Playwright-installed; ~250MB install cost vs 10-min manual sweep). **Pattern: tool-automatable subset auto-runs; tool-unavailable subset → checklist for manual operator + carryover ID.**

- **R-P9-6 Same-phase fix bundle pattern (N.5-style) repeated cleanly.** Phase 6.4 / Phase 7.5 / Phase 8.5 / Phase 9.14 all follow: reviewer CONDITIONAL_PASS → main session applies HIGH + cheap MEDIUM fixes → effective PASS in same phase. **Rule for the future locked: when reviewer surfaces HIGH + cheap MEDIUM with documented small-fix paths, fix in same phase via N.14 commit.**

- **R-P9-7 `Astro.site` derivation via `new URL(target.slice(1), Astro.site).toString()`** (D-P9-7). Reviewer suggested `${Astro.site}${target.slice(1)}` (string concat), but `Astro.site` is a URL object that toString's WITH trailing slash, so concat produces double-slash. `new URL()` constructor handles base+path normalization correctly. **Lesson: when concatenating Astro globals, prefer `new URL()` over template literals if the global is URL-typed.**

---

## §2 必须补上的缺口 (G-P9-*)

- **G-P9-1 Same-session blind spot in handoffs.** Phase 8 close session wrote the Phase 8→9 handoff naming "Phase 9 = Downloads Pipeline" without verifying that section's tasks weren't already shipped. Pattern lesson: **when a phase handoff names a specific master plan section as next-phase scope, the handoff should include a `git log --follow <indicative-file-from-target-section>` line to verify the section isn't already done.** R-P9-1 sister.

- **G-P9-2 Fixture matrix not enumerated in PLAN.** Phase 9.7 PLAN said "remark plugin throw fixture" but didn't enumerate the scenarios (throw / rewrite / changelog / anchor / drop-wrapper / absolute-URL). Reviewer F-3 caught CHANGELOG hash gap; F-9 caught dotslash form gap. Pattern lesson: **when writing fixture tests, enumerate the *scenarios* in the PLAN, not just the file. Future phase PLANs should include "fixture matrix" stubs for any new test files.**

- **G-P9-3 Canonical-derivation pattern not documented as project convention.** F-5 hardcoded `https://sdtm-pedia.pages.dev` was copy-paste from `dist/index.html` reference output without checking BaseLayout.astro convention. Phase 7 D-P7-3 trailing-slash canonical fix established but didn't document "canonical source = `Astro.site`". Captured as C-P9-16. Pattern lesson: **when adding new pages that emit canonical URLs, grep for existing canonical-emit sites and follow their derivation pattern.**

- **G-P9-4 Schema platform-key asymmetry on day-1.** Initial `web/src/data/schemas.ts` used `z.record(z.string(), z.string())` for `DimensionsSchema.values` while `DownloadsSchema.platform` used `z.enum([...])`. Test passed because actual data has correct keys. Reviewer caught the asymmetry. Pattern lesson: **when designing schemas with multiple "platform"-typed fields across schemas, factor a single-source enum first (`platformKeys`) and reuse across all schemas in the file.** Done in 9.14 fix; lesson locked.

- **G-P9-5 Half the deferred carryover absorbed; half still pending.** Phase 9 absorbed 8 of 12 deferred Phase 6/7 carryovers (C-P5-L2 + C-P6-4 + C-P6-6 + C-P6-7 + C-P7-6 + C-P8-1..5); 4 still pending (C-P6-5 / C-P5-M2 / C-P7-7 / C-P7-8). Phase 7 G-P7-5 + Phase 8 G-P8-5 lesson sustained: **deferring some carryover is OK if scope is bounded, but the deferred items should be explicitly re-prioritized in the next phase's PLAN.** Phase 10 PLAN should list which it absorbs (or explicitly mark "v1.1+ scope").

---

## §3 关键决策复盘 (D-P9-*)

- **D-P9-1 Scope = Option D (B+C combined).** Combine Phase 8 carryover absorption + master plan §"Phase 10 — QA + Polish" rather than scope-tight (one or the other). Tradeoff: more LOC at risk in single phase, but shipping pre-public-release polish in 1 phase is preferable to spreading polish across 2-3 phases when it's all the same edit-family + Daisy review-budget. Validated by: 1 commit `e89da8a` + 1 fix commit + 1 close = same commit count as Phase 8 (which was scope-tight at Search-only). **Decision held**: combining was the right call given Phase 9 surface heterogeneity didn't introduce risk.

- **D-P9-2 Reviewer = `feature-dev:code-architect`.** 2nd-burn feature-dev family but NEW agent (Phase 5 was code-reviewer). Architect lens for "is the design fit for purpose?" suited Phase 9's heterogeneous surface (e2e infra / a11y / data schemas / build pipeline / archeology). Reviewer caught F-1 (Rule A spot-check), F-3 (fixture coverage gap), F-4 (schema asymmetry), F-5 (architectural inconsistency) — all design-class findings consistent with the architect lens. **Decision held**: cross-agent rotation working as designed.

- **D-P9-3 9.14 fix bundle scope = F-1 HIGH + F-3+F-4+F-5 MEDIUM (4 of 9 findings).** F-2 (Escape stale closure) deferred because refactor non-trivial vs benefit; F-6/F-7/F-8/F-9 = LOW carryover. Same pattern as 6.4/7.5/8.5 — HIGH always fixes; cheap MEDIUM bundle when LOC small + same edit family; LOW always carryover unless trivially co-located. **Decision held**: ~14 LOC across 5 files (1 vitest test + 1 ts edit + 1 tsx edit + 2 astro edits) — small commit, surgical.

- **D-P9-4 Lighthouse baseline acceptance: a11y 91 / Best Practices 73 / SEO 100 (Daisy ack "还可以").** Master plan target ≥ 95 unmet. Tradeoff: pursuing 95/95/95 in Phase 9 would extend phase duration ~half-day (focus contrast remediation + label-aria fix + target-size mobile audit) for marginal user-facing benefit on Company Release Internal scope. **Decision held**: documented as v1.1 polish target via C-P9-2 + C-P9-5..8.

- **D-P9-5 Cross-browser scope: Chrome auto + Safari/Firefox manual checklist.** Playwright `webkit`/`firefox` not installed (~250MB install cost). Decision: 7-flow × 2-browser ~10 min Daisy manual cheaper than 250MB install + 3-browser maintenance burden for v1.0. **Decision held**: tool-automatable / tool-unavailable QA split is the right pattern.

- **D-P9-6 Pluralization fix Option B (inline conditional in TSX) over Option A (hyphenated `result(s)` in i18n).** Option A is grammatically ugly; Option B keeps i18n files clean and only branches the affected language. **Decision held**: 2 LOC inline guard appropriate for the surface.

- **D-P9-7 `Astro.site` derivation pattern via `new URL()` over `${Astro.site}${path}`.** `Astro.site` is URL object; toString includes trailing slash; concat would double-slash. `new URL(target.slice(1), Astro.site).toString()` correct. **Decision held**: lesson should propagate to BaseLayout-style canonical derivations IF they ever needed retrofit (they don't currently — BaseLayout uses different pattern via `Astro.url`).

- **D-P9-8 Subagent_prompts/ trace dir committed at Phase close** (D-P6-6 → D-P7-* → D-P8-* → D-P9-8 carryforward). Cleaner chronological commit; reviewer prompt + report co-located. **Pattern locked across 4 phases.**

---

## Rule A/B/C/D/E compliance

- **Rule A** semantic spot-check: 6 new strings × 3 langs = effectively 18 surface points. Reviewer applied N=6 (one per key per lang) full-coverage spot-check; found F-1 (1/6 = 17%). Spot-check **WARRANTED + EFFECTIVE**.
- **Rule B** failures archive: no failures encountered (no halt states, no abandoned attempts). 0 entries in `evidence/failures/`. Compliant.
- **Rule C** retrospective: this file. Three-section structure (R / G / D) per template. Compliant.
- **Rule D** writer/reviewer isolation: writer = main session opus / reviewer = `feature-dev:code-architect` (different agent + different context + different lens). Cross-family vs Phase 8 (pr-family) + Phase 7 (superpowers) + Phase 6 (omc). Compliant.
- **Rule E** cross-platform learning: not applicable (website-only scope).

## Phase-spanning patterns (Rule E candidates from Phase 9)

- **R-P9-1 (archeology before scoping)**: candidate for `~/.claude/CLAUDE.md` `personal_operating_principles` rule addition: "Open-phase pre-flight: when handoff names a specific master plan section as next-phase scope, run `git log --follow <indicative-file>` + `gh release list` (if release-relevant) to verify section isn't already done." Daisy decides whether to add at session-end retro absorption.

- **R-P9-4 (Rule A applies to NEW translatable strings, not just translations)**: Rule A skill original framing is "compression rate / rewrite rate >50%". Phase 9 evidence: 17% error rate on adding 6 NEW strings is high enough to warrant explicit spot-check. Candidate addition to `~/.claude/CLAUDE.md`: extend Rule A trigger to include "≥3 new translatable strings added in a phase that ships to multiple-lang viewers" — N=1-2 spot-check per lang per key.

- **R-P9-5 (tool-automatable / tool-unavailable QA split)**: candidate skill template for any phase that touches QA-like tasks (Lighthouse / cross-browser / a11y scan / performance trace).

These are CANDIDATES for Rule E absorption; final decision Daisy's at v1.1 / cross-platform retro.

---

## Phase 9 close metrics

- tsc 0 errors / vitest **47/47** in 11 files / e2e **7/7** strict against `npm run preview` / build **31** HTML pages / Pagefind **0** `<html>`-missing warnings (was 4) / dist/pagefind 17 artifacts / 4 GH URLs HTTP/2 302 ✓ / production landing HTTP/2 200 ✓ / pagefind.js HTTP/2 200 ✓ / Lighthouse 91/73/100 (Daisy ack baseline) / canonical URLs derived from `Astro.site` ✓ trailing slashes preserved per Phase 7.5
- 21 files / +8491 / -55 LOC in `e89da8a` (most volume = Lighthouse JSON + HTML reports)
- 5 files / +14 / -? LOC in 9.14 fix commit
- Family pool state at close: pr-family 5× / feature-dev 2× (NEW agent in 2nd burn) / omc 1× / superpowers 1× = 4 active families on website lane
- Ready for: Phase 10 (TBD scope — see handoff §"How the Phase 10 session should start")
