# Website Build — Phase 9 → Phase 10 Handoff

> **Date**: 2026-04-30
> **Outgoing session**: Phase 9 (Pre-Public-Release Polish + QA Bundle)
> **Incoming session**: Phase 10 (TBD — Daisy decides post-handoff scope)
> **Branch**: `main`. HEAD = (post 9.15 close commit, pending). Prior: `e89da8a` (9.1-9.12 polish bundle) + 9.14 fix bundle commit (pending) + this handoff's commit (pending).

## What's done — Phase 9

| Commit | Subject |
|---|---|
| `e89da8a` | 07 Website Phase 9.1-9.12 — Tier 3 polish bundle pre-public-release |
| (pending) | 07 Website Phase 9.14 — reviewer fix bundle (F-1 HIGH + F-3/4/5 MEDIUM ×3) |
| (pending) | 07 Website Phase 9 close — handoff + master plan annotation + index sync |

(Phase 9.13 reviewer pass = no source change — report committed alongside 9.14 evidence.)

## End-of-Phase-9 reviewer verdict

`feature-dev:code-architect` (2nd-burn feature-dev family — NEW agent vs Phase 5 `feature-dev:code-reviewer`; cross-family from Phase 8 `pr-review-toolkit:silent-failure-hunter`). Initial **CONDITIONAL_PASS H=1 M=4 L=4** (report 280 lines at `.work/07_website/phase9/evidence/checkpoints/phase_9_reviewer_report.md`). The HIGH (F-1 English "1 results" pluralization in aria live region) was caught via Rule A semantic spot-check on 6 new i18n strings — 1/6 = 17% error rate confirms Rule A spot-check warranted. zh + ja count-neutral suffix forms correct; only English failed.

**Phase 9.14 fix bundle applied** (commit pending, 5 files / +14 LOC): F-1 + F-3 + F-4 + F-5. Verified via vitest 47/47 (+1 CHANGELOG hash fixture from F-3) + dist HTML grep verifying F-5 redirect canonicals derived from `Astro.site`. Reviewer brief upgrade path satisfied → **effective PASS** for Phase 10 entry. Remaining LOW findings (F-2/F-6/F-7/F-8/F-9) deferred to Phase 10 polish bundle as C-P9-10 + C-P9-12..15.

## Pre-flight decisions made at Phase 9 start (Daisy ack 2026-04-30)

1. **Scope = Option D (B + C combined)** — Y. Combine Phase 8 carryover C-P8-1..5 + selective Phase 6/7 deferred polish + master plan §"Phase 10 — QA + Polish".
2. **Reviewer slot = `feature-dev:code-architect`** — Y. 2nd-burn feature-dev family, NEW agent within family. Cross-family vs Phase 8 pr-family.
3. **Plan deviation flag = NONE expected** — Y. Master plan §"Phase 10" followed; archeology finding §0 documents that master plan §"Phase 8 Downloads" + §"Phase 9 CF Deploy" + §"Phase 10.4 README" already shipped (4-28 / 4-28 / Phase 7.3). Phase 9-of-execution = renumbered §"Phase 10 — QA + Polish".

## §1 Retrospective — what went well (Rule C R-P9-*)

- **R-P9-1** Pre-flight archeology (commits log + `gh release view v1.0` + `git ls-remote --tags origin`) caught the Phase 8→9 handoff's wrong premise BEFORE any redundant work was scheduled. The handoff said "Phase 9 = Downloads Pipeline" but Downloads Pipeline already shipped 4-28. Saved ~half-day of duplicate work + protected an immutable `v1.0` tag from accidental re-cut. **Pattern locked**: open-phase pre-flight should always include a "what's already shipped" archeology pass when the handoff names a specific master plan section. C-P8-7 process improvement applied.
- **R-P9-2** Same-edit-family bundle (12 cheap polish tasks combined into 1 commit `e89da8a`) instead of per-task commits. Phase 6 had 5 commits + close, Phase 7 had 4 + close, Phase 8 had 2 + close — Phase 9 had 1 + 1 fix + 1 close. Reasoning: tasks were small (~5-30 LOC each), independent, and tests covered each via vitest/e2e. The bundle commit message lists all 12 tasks + carryover IDs absorbed for git-archeology. Pattern: scope-driven commit cadence — 1 commit when changes are small + independent + tested in same lane; multiple commits when changes are sequential or risk-isolated.
- **R-P9-3** Subagent reviewer brief (R-P7-1 / R-P8-1 carryforward as `task_9_13_reviewer_prompt.md`) explicitly enumerated D1-D7 stress dimensions adapted to Phase 9 surface (e2e infra / SearchOverlay a11y / plugin fixture / zod schema / redirect HTML / focus-visible CSS / archeology + scope). The reviewer caught F-1 specifically because D2 asked about new i18n strings — the brief structure is doing real work. Same brief pattern locked for future phases.
- **R-P9-4** Reviewer's Rule A spot-check explicitly enumerated as a process artifact (zh ✓ / ja ✓ / en F-1 = 1/6 = 17% error rate confirms warranted). Pattern: when a phase adds 3+ new translatable strings, the reviewer brief should EXPLICITLY ask for Rule A spot-check on the new keys (not just "i18n parity" which only checks key existence). C-P7-7 process improvement (Rule A rubric expansion) effectively materialized via this concrete pattern.
- **R-P9-5** Lighthouse + cross-browser scope decisions made the right tradeoff — Lighthouse audit ran via chrome-devtools MCP (got real numbers 91/73/100 vs deferring entirely); Safari/Firefox left as Daisy manual checklist (browsers not Playwright-installed, ~250MB install cost vs 10-min manual sweep). Daisy ack "还可以" on Lighthouse baseline 91/73/100 + 6 fail items as carryover C-P9-4..9. The "tool-automatable subset auto-runs; tool-unavailable subset becomes Daisy manual checklist" split is the right pattern for QA-style phases.
- **R-P9-6** Phase 8.5 same-phase fix bundle pattern repeated cleanly in Phase 9.14 (F-1 HIGH + 3 cheap MEDIUMs / +14 LOC / 1 commit). HIGH always fixes in same phase if path is mechanical. Locked rule sustained.
- **R-P9-7** Tier 3 trace artifacts (PLAN.md 199 lines + _progress.json + 4 evidence reports + 1 reviewer brief + 1 reviewer report + cross-browser template + Lighthouse evidence) all preserved and committed. Phase archeology can be reconstructed from `git log --follow .work/07_website/phase9/`. Same pattern as Phase 7/8 sustained.

## §2 Gaps (Rule C G-P9-*)

- **G-P9-1** Phase 8→9 handoff (`.work/meta/website_phase8_to_phase9_handoff_2026-04-29.md`) stated "Phase 9 = master plan §'Phase 8 — Downloads Pipeline'" without verifying that section's tasks weren't already shipped. The handoff WAS written by the Phase 8 close session — same-session blind spot. Pattern lesson: when a phase handoff names a specific master plan section as next-phase scope, the handoff should include a `git log --follow <indicative-file-from-target-section>` line to verify the section isn't already done. R-P9-1 sister.
- **G-P9-2** Phase 9 PLAN.md §"task 9.7" mentioned `web/remark-md-link-rewrite.test.mjs` but didn't list which fixture cases would be written ahead of time. Reviewer F-3 caught the CHANGELOG hash gap; F-9 caught the dotslash form gap. Pattern lesson: when writing fixture tests, enumerate the **scenarios** in the PLAN, not just the file. Future phase PLANs should include "fixture matrix" stubs for any new test files.
- **G-P9-3** F-5 hardcoded domain in 2 redirect files was a copy-paste from `dist/index.html` reference output (Phase 7.5 fix evidence) without checking if BaseLayout.astro uses derived `Astro.site`. The Phase 7 D-P7-3 trailing-slash canonical fix established the convention but wasn't documented as "canonical source = Astro.site". Pattern lesson: when adding new pages that emit canonical URLs, grep for existing canonical-emit sites and follow their derivation pattern. Captured as C-P9-16 process improvement.
- **G-P9-4** F-4 `DimensionsSchema.values` typo-blind gap survived from initial schema design — schemas.ts day-1 wrote `z.record(z.string(), z.string())` and the test passed because actual data has correct keys. Reviewer caught the asymmetry vs `DownloadsSchema.platform`. Pattern lesson: when designing schemas with multiple "platform"-typed fields across schemas, enforce single-source enum first (`platformKeys`) and reuse across all schemas in the file. Done in 9.14 fix; lesson locked.
- **G-P9-5** Phase 9 absorbed 8 of the 12 deferred Phase 6/7 carryovers (C-P5-L2 + C-P6-4 + C-P6-6 + C-P6-7 + C-P7-6 + 4 from Phase 8 C-P8-1..4 + C-P8-5 — 8 tasks); 4 still deferred (C-P6-5 / C-P5-M2 / C-P7-7 / C-P7-8). Plus 2 Phase 8 LOW (F-7 already-resolved + F-9 deferred). Phase 7 G-P7-5 + Phase 8 G-P8-5 lesson sustained: deferring some carryover is OK if scope is bounded, but the deferred items should be explicitly re-prioritized in the next phase's PLAN. Phase 10 PLAN should list which it absorbs.

## §3 Decisions (Rule C D-P9-*)

- **D-P9-1** **Plan deviation: NONE.** Master plan §"Phase 10 — QA + Polish" Tasks 10.1 + 10.2 + 10.3 + 10.5 all addressed (10.4 already-done from Phase 7.3). Two non-deviation observations: (a) renumbering archeology — master plan §"Phase 8 Downloads" + §"Phase 9 CF Deploy" + §"Phase 10.4 README" already shipped 4-28/4-28/Phase 7.3 — annotation in Task 9.15; (b) Lighthouse Performance category not measured (chrome-devtools MCP `lighthouse_audit` excludes performance by design — requires separate `performance_start_trace` tool, deferred as C-P9-4).
- **D-P9-2** **Reviewer = `feature-dev:code-architect`.** Daisy ack 2026-04-30 entry decision b. 2nd-burn feature-dev family but NEW agent within family (Phase 5 used `code-reviewer`). Cross-family vs Phase 8 pr-family + Phase 7 superpowers + Phase 6 omc-critic. Architect lens (vs code-quality lens) suited Phase 9's heterogeneous surface (e2e infrastructure / a11y / data schemas / build pipeline / archeology). Substituted (vs handoff's recommendation backup) when verified registered.
- **D-P9-3** **Phase 9.14 fix bundle scope = F-1 HIGH + F-3 + F-4 + F-5 MEDIUM (4 of 9 findings).** Reviewer recommended F-3 + F-4 + F-5 alongside F-1 because: F-3 fixture gap is co-located test edit, F-4 schema asymmetry is co-located edit, F-5 hardcoded domain is `Astro.site` 1-line refactor (verified `Astro.site` defined in `astro.config.mjs:9`). F-2 (Escape stale closure) deferred because the refactor is non-trivial vs benefit; F-6/F-7/F-8/F-9 = LOW carryover. Same pattern as Phase 7.5 + Phase 8.5 fix bundles — HIGH always fixes; cheap MEDIUM bundle when LOC is small + same edit family; LOW always carryover unless trivially co-located. Locked.
- **D-P9-4** **Lighthouse baseline acceptance: a11y 91 / Best Practices 73 / SEO 100.** Daisy ack "还可以" 2026-04-30. Performance not measured (tool limitation). 6 fail items (color-contrast / label-content-name-mismatch / target-size / errors-in-console / inspector-issues / third-party-cookies) recorded as C-P9-5..9. third-party-cookies (CF Pages baseline) ACCEPTED indefinitely.
- **D-P9-5** **Cross-browser scope: Chrome auto via Playwright + Safari/Firefox manual checklist.** Playwright `webkit`/`firefox` browser binaries not installed (~250MB install cost). 7-flow × 2-browser sweep is ~10 min Daisy manual; cheaper than installing browsers + maintaining 3-browser test matrix for v1.0. Pattern: tool-automatable subset auto-runs; tool-unavailable subset → Daisy manual.
- **D-P9-6** **Pluralization fix Option B (inline conditional in `SearchOverlay.tsx`) chosen over Option A (1-line `ui.en.json` change).** Option A `"results"` → `"result(s)"` is grammatically ugly; Option B keeps i18n files clean and only branches the affected language. ~2 LOC inline guard.
- **D-P9-7** **`Astro.site` derivation pattern via `new URL(target.slice(1), Astro.site).toString()`** chosen for redirect canonicals. Reviewer suggested `${Astro.site}${target.slice(1)}` (string concat) but `Astro.site` is a URL object that toString's WITH trailing slash, so concat would double-slash. `new URL()` constructor handles base+path normalization correctly. ~2 LOC × 2 files.
- **D-P9-8** **`subagent_prompts/` trace dir committed at Phase close** (D-P6-6 carryforward) — sustained pattern for Phase 7+/8/9.

## Carryover for Phase 10 (consolidated, IDs C-P9-*)

### Phase 9.14 already RESOLVED (no carryover)

- C-P9-(F-1) "1 results" English pluralization — fixed
- C-P9-(F-3) CHANGELOG hash fixture — fixed
- C-P9-(F-4) DimensionsSchema values typo-blind — fixed
- C-P9-(F-5) hardcoded domain in redirect canonicals — fixed

### Phase 10 carryover (numbered)

- **C-P9-1** Safari + Firefox cross-browser sweep (Daisy manual ~10 min, before public-release announcement). Source: 9.11.
- **C-P9-2** Lighthouse remediation pass to 95/95/95 (cheap fixes for 5 of 6 fail items per `lighthouse-evidence-2026-04-30.md`). OPTIONAL — Daisy ack baseline 91/73/100 acceptable.
- **C-P9-3** axe DevTools manual scan per master plan §10.2 step 1 (Daisy manual ~10 min).
- **C-P9-4** Lighthouse Performance trace via `chrome-devtools__performance_start_trace` (separate tool not used in 9.10).
- **C-P9-5** color-contrast remediation (likely fine-text + `--ink-faint` 0.4 alpha).
- **C-P9-6** label-content-name-mismatch on ⌘K hint button (aria-label vs visible text WCAG 2.5.3).
- **C-P9-7** target-size mobile audit + bump dense flex spacing.
- **C-P9-8** errors-in-console triage (Pagefind warn intentional? or gate to DEV?).
- **C-P9-9** third-party-cookies — ACCEPTED indefinitely (CF Pages baseline). NOT a carryover; documented for future auditors.
- **C-P9-10** SearchOverlay Escape branch reads stale `open` closure (F-2) — non-trivial refactor.
- **C-P9-11** ~~Astro.site derivation~~ RESOLVED in 9.14 (F-5).
- **C-P9-12** playwright webServer stdout swallowed on build fail (F-6).
- **C-P9-13** CI env var comment misleading for CF Pages (F-7) — 1 LOC.
- **C-P9-14** Remove redundant `role="searchbox"` (F-8) — 1 LOC.
- **C-P9-15** Plugin fixture missing `./UPPERCASE.md` form (F-9) — 1 fixture.
- **C-P9-16** [Process improvement] Canonical-derivation grep before adding new pages that emit `<link rel=canonical>`. G-P9-3 sister.

### Pre-existing Phase 6/7/8 carryover NOT touched in Phase 9

- **C-P7-1** Astro i18n soft-404 200 — ACCEPTED indefinitely (documented in `web/README.md`)
- **C-P7-7** Rule A rubric expansion for translation work — DEFER process improvement (R-P9-4 partial materialization)
- **C-P7-8** README "auto-deploys from main" verify — DEFER (Daisy manual CF dashboard)
- **C-P8-6** Mobile UX (⌘K hint md:+ breakpoint only) — DEFER (no UX direction)
- **C-P6-5** `/guide/platform-comparison` vs `/compare` redundancy — DEFER design decision
- **C-P5-M2** DocsSidebar drawer ViewTransitions — DEFER (no VT enabled)

## Working state — Phase 9 close

- **Branch**: `main`. HEAD = (post 9.15 close commit, pending). Prior: `e89da8a` + 9.14 fix bundle (pending).
- **Test status**: tsc 0 errors / vitest **47/47** in 11 files (+13 / +2 vs Phase 8) / e2e **7/7** strict against `npm run preview` lane / build **31** HTML pages green / **0** Pagefind no-`<html>` warnings (was 4) / dist/pagefind/ 17 artifacts unchanged.
- **GH Release v1.0**: 4 assets LIVE since 2026-04-28T00:42:36Z (`https://github.com/hakupao/sdtm-pedia/releases/tag/v1.0`). All 4 download URLs HTTP/2 302 ✓.
- **Production**: `https://sdtm-pedia.pages.dev/` live; landing HTTP/2 200; pagefind.js HTTP/2 200.
- **Lighthouse**: a11y 91 / Best Practices 73 / SEO 100 (Performance not measured). Baseline ack'd by Daisy.
- **Evidence preserved**: `.work/07_website/phase9/{PLAN.md (199 lines), _progress.json, evidence/checkpoints/{final_verify_checklist, lighthouse-evidence, phase_9_reviewer_report}-2026-04-30.md, subagent_prompts/task_9_13_reviewer_prompt.md, RETROSPECTIVE.md (forthcoming)}` + `web/qa/{lighthouse-zh-landing, cross-browser}-2026-04-30.{html,json,md}`.

## How the Phase 10 session should start

1. Read this handoff first.
2. **Decide Phase 10 scope**: master plan has no §"Phase 11" — Phase 10 was QA + Polish. Phase 10 is THE LAST master plan section. Phase 10-of-execution candidates:
   - **A**: v1.1 polish bundle absorbing C-P9-* carryover (cheap cleanup pass, ~half day)
   - **B**: Daisy public-release announcement (Slack / blog post / email — out of code scope, just trigger work)
   - **C**: New feature work (e.g. server-side search, auth, custom domain) — out of v1.0 scope
   - **D**: Migration/upgrade work (Astro 7 watch, etc.) — out of v1.0 scope
   - **E**: STOP — declare v1.0 complete, archive `web/` lane until next iteration
3. Read `.work/07_website/phase9/evidence/checkpoints/phase_9_reviewer_report.md` for full C-P9-* status.
4. Reviewer slot for Phase 10 (if A): cross-family options remaining post Phase 9: `oh-my-claudecode:code-reviewer` / `verifier` (2nd-burn omc), `pr-review-toolkit:type-design-analyzer` / `pr-test-analyzer` (6th-burn pr-family, NEW agent), `superpowers:requesting-code-review` (2nd-burn superpowers), `feature-dev:code-reviewer` (3rd-burn feature-dev). Recommend: `oh-my-claudecode:verifier` for evidence-based "is the polish actually polished" verification on the LIVE production site.

Family pool state at Phase 9 close: `pr-review-toolkit` ×5 (Phases 1, 2, 3.6, 4 = code-reviewer + Phase 8 = silent-failure-hunter), `feature-dev` ×2 (Phase 5 = code-reviewer + Phase 9 = code-architect), `oh-my-claudecode` ×1 (Phase 6 critic), `superpowers` ×1 (Phase 7 code-reviewer). Phase 10 candidates expand the families used so far.

## Push state at Phase 9 close

`origin/main` = `0e682a7` at session start. Phase 9 commits (`e89da8a` 9.1-9.12, pending 9.14 fix bundle, pending 9.15 close handoff) + this handoff's index-sync commit pending push.

After push, CF Pages will auto-rebuild, picking up:
- Phase 9 polish (focus-visible / SearchOverlay focus-return + aria live + 1-retry / TOC empty guard)
- Redirect HTML wrapper with `<html lang>` + `data-pagefind-ignore` (Pagefind cleanups)
- 9.14 fix: English "1 result" pluralization + Astro.site-derived redirect canonicals + tighter DimensionsSchema

Verify CF re-deploy ~5 minutes post-push:
- `curl -sI https://sdtm-pedia.pages.dev/` should still resolve to `/zh/` redirect (HTTP/2 200 + `<meta http-equiv=refresh>` immediate)
- `curl -s https://sdtm-pedia.pages.dev/zh/guide/ | grep canonical` should show `<link rel="canonical" href="https://sdtm-pedia.pages.dev/zh/guide/user-guide/">` (Astro.site-derived)
- `curl -s https://sdtm-pedia.pages.dev/pagefind/pagefind-entry.json` should still report 27 indexed pages
- Browser open `https://sdtm-pedia.pages.dev/zh/guide/user-guide/`, press Cmd+K, type any query that returns 1 hit, screen reader should announce "1 result" (NOT "1 results") in EN session
