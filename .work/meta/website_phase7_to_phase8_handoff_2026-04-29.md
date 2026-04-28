# Website Build — Phase 7 → Phase 8 Handoff

> **Date**: 2026-04-29
> **Outgoing session**: Phase 7 (Pre-Public-Release Bundle) — 4 commits on `main`
> **Incoming session**: Phase 8 (Pagefind / Search — original master plan §"Phase 7" pre-renumber)
> **Branch**: `main`. HEAD = `e7e64c0`. Pushed: pending Phase 7 close commit.

## What's done — Phase 7

| Commit | Subject |
|---|---|
| `3c151de` | 07 Website Phase 7.1 — compare page i18n chrome (4 keys × 3 langs, C-P6-1 absorbed) + Phase 7 Tier 3 trace open + Task 7.0 PASS |
| `4047b85` | 07 Website Phase 7.2 — site-wide canonical link via BaseLayout (C-P6-3 absorbed) |
| `a1ad23e` | 07 Website Phase 7.3 — build:fresh script + replace web/README.md placeholder with project content (C-P6-8 absorbed) |
| `e7e64c0` | 07 Website Phase 7.5 — reviewer fix bundle (F-1 HIGH + F-2/3/4 MEDIUM ×3 + F-8 LOW): redirect canonical trailing-slash + ja i18n convention + build:fresh composability |

(Phase 7.0 = verification-only, no commit — embedded into 7.1 commit.)
(Phase 7.4 reviewer pass = no source change — report committed in 7.5.)

## End-of-Phase-7 reviewer verdict

`superpowers:code-reviewer` (Rule D 3rd-family inaugural after `pr-review-toolkit` ×4 + `feature-dev` ×1 + `oh-my-claudecode` ×1): initial **CONDITIONAL_PASS H=1 M=4 L=5** (report 453 lines at `.work/07_website/phase7/evidence/checkpoints/phase_7_reviewer_report.md`). The HIGH (F-1 redirect-canonical chain) was a pre-existing bug that Phase 7's new canonical infrastructure illuminated — exact "infrastructure-phase-finds-latent-bugs" pattern Phase 6 D-P6-4 + R-P6-5 lessons predicted.

**Phase 7.5 fix bundle applied** (commit `e7e64c0`, ~10 LOC across 4 files): F-1 + F-2 + F-3 + F-4 + F-8. Verified directly via dist HTML grep (3 redirect canonicals match content canonicals; 3 ja string updates present, 0 old strings remaining; build:fresh composes `npm run build`). Reviewer brief upgrade path satisfied → **effective PASS** for Phase 8 entry. Remaining M-level (F-5 WCAG audit-trail thinness) addressed via documented analysis below; remaining L-level + 1 process MEDIUM (F-10 Rule A rubric) deferred per reviewer recommendation.

## Pre-flight decisions made at Phase 7 start (carryover from Phase 6 handoff)

1. **CF Pages preview verify first (Task 7.0)** — Y. C-P5-M3 trailing-slash hosting smoke-tested before adding more pages.
2. **Bundle C-P6-1 + C-P6-3 + C-P6-8 + C-P5-M3 as Phase 7 entry, defer master plan §"Phase 7" Pagefind to Phase 8** — Y. Plan deviation flag in `phase7/PLAN.md` (4 reasons; 3 strong + 1 reason #4 admin-consequence-not-justification per F-9, accepted as written but flagged).
3. **Reviewer slot = `superpowers:code-reviewer`** — Y. 3rd-family inaugural confirmed.

## §1 Retrospective — what went well (Rule C R-P7-*)

- **R-P7-1** Phase 6 R-P6-1 lesson (structured reviewer brief with explicit dimensions + adversarial framing) carried forward as `phase7/subagent_prompts/task_7_4_reviewer_prompt.md`. Result: 1 HIGH + 4 MEDIUM + 5 LOW = 10 findings, vs Phase 6's 11 findings on a larger surface. Per-LOC review yield held; brief structure proved repeatable.
- **R-P7-2** Pre-flight fact-correction at session start (handoff said `web/README.md` missing; actual: existed but had Astro starter boilerplate) caught BEFORE Phase 7.3 work began. Saved ~5 min of "create vs replace" confusion. Pattern: explicitly verify handoff claims against current state at session open, even for trivial-looking statements.
- **R-P7-3** CF Pages preview verification (Task 7.0) caught C-P7-1 incidentally (Astro i18n soft-404 200-response on ALL unmatched paths). The probe matrix was sized for C-P5-M3 trailing-slash only; the 3-nonsense-URL probe added at the end was the discovery vector. Pattern: when running a verification matrix, add 1-2 "control" probes for adjacent failure modes — they're cheap and surface latent issues.
- **R-P7-4** All 3 main tasks (7.1/7.2/7.3) plus 7.5 fix bundle ran direct in main session (no subagent dispatch). Diff size 7 files / ~150 lines net additions. For mechanical work at this scale, subagent overhead would have cost more than it saved; main-session execution + tight verification loop (tsc + vitest + grep dist after each edit batch) was the right mode. Pattern locked: subagent for substantial work (Phase 6.0/6.1 each ~100+ LOC), direct for mechanical (Phase 6.2 + all of Phase 7).
- **R-P7-5** README written in 7.3 was verified accurate at write-time across 5 tribal-knowledge sections by the reviewer (each claim cross-checked against current code). The "tribal knowledge" pattern — pre-empting day-2 contributor pain points — proved valuable on a sample size of 5/5. Survival depends on future contributors not silently changing the patterns described.
- **R-P7-6** F-2/F-3/F-4 (ja i18n convention drift) were ALL the same root cause: Rule A rubric was lexical-only and missed punctuation + grammatical-form. Reviewer caught all 3 in one adversarial pass. Process improvement: C-P7-7 (rubric expansion) should adopt before next i18n phase.
- **R-P7-7** Tier 3 trace artifacts (PLAN.md 242 lines + _progress.json + 5 task evidence reports + reviewer report + reviewer prompt) all preserved and committed. Future archeology can reconstruct full decision chain from `git log --follow .work/07_website/phase7/`. Same pattern as Phase 6 R-P6-6 sustained.

## §2 Gaps (Rule C G-P7-*)

- **G-P7-1** Reason #4 of plan deviation (PLAN.md L19-20) is administrative-consequence not justification. F-9 LOW. Pattern lesson: when documenting plan deviation, every reason should answer "why this instead of master plan", not "what changes if we do this". Reasons #1/#2/#3 hit the bar; reason #4 is filler. Fix in next phase: drop or restate.
- **G-P7-2** Master plan §"Phase 7" not annotated for Pagefind renumber (C-P7-5). Exit criterion #8 in PLAN.md was set for Phase 7 close; addressed in this handoff via the master plan edit committed alongside (see C-P7-5 below). Pattern: when Phase N deviates from master plan, annotate master plan IN THE SAME PHASE N close commit, not deferred. This phase did defer; next one shouldn't.
- **G-P7-3** Rule A rubric was sample-size-3 lexical-only. F-10 LOW + F-2/F-3/F-4 MEDIUM are evidence the rubric undersized. Pattern: for translation work, increase N to ~50% of strings AND broaden rubric to include typography + grammatical-form-vs-role-fit checks. Captured as C-P7-7.
- **G-P7-4** F-1 HIGH was a pre-existing bug Phase 7 surface-illuminated. Phase 6 cookery for "infra phase finds latents" predicted this exactly (D-P6-4). The bug existed BEFORE Phase 7 — but the team didn't know about it because canonical wasn't a checked dimension. Pattern lesson sustained: when you introduce a checked dimension, expect to find latent bugs in adjacent code that the new check exposes. Phase 6 H1 + H2 → Phase 7 F-1 = 2 cumulative instances of this pattern; high confidence the pattern holds.
- **G-P7-5** Phase 7 absorbed 4 of 8 Phase 6 carryovers (C-P6-1/3/8 + C-P5-M3 from Phase 5 carryforward). 4 deferred to Phase 8 (C-P6-2/5/6/7) + 1 partial (C-P6-4 README documented but no code fix). Pattern: deferring half the carryover is OK if scope is sequence-driven, but the deferred items should be re-prioritized in Phase 8 PLAN; otherwise they age out of the radar. Phase 8 PLAN should explicitly state which it absorbs.

## §3 Decisions (Rule C D-P7-*)

- **D-P7-1** **Plan deviation: Phase 7 = release-readiness bundle, master plan §"Phase 7" Pagefind → Phase 8.** Confirmed correct (D5 reviewer pass + adversarial counter-argument considered). Trade-off: master plan numbering drifts by 1; documentation cost of annotation is small. Future plan deviations: state the deviation in PLAN.md AND annotate master plan in same close commit (G-P7-2 lesson).
- **D-P7-2** **CompareFilter calls `getUIStrings(lang)` internally** rather than receiving placeholder/label as props. Chose for: keeps existing test signature, vitest jsdom handles ESM JSON imports natively, marginal bundle cost (~2KB raw). Trade-off: client bundle pulls all 3 lang dictionaries even when only 1 used. Acceptable at this scale; revisit if compare island grows or if other islands need lang-specific strings (consider a build-time strings injector then).
- **D-P7-3** **`<link rel="canonical">` + `<meta property="og:url">` use the same href.** For static documentation, no divergence case. Reviewer D2 confirmed. If future requirements introduce social-card-targeted alt URLs, split then; do not pre-design.
- **D-P7-4** **Astro `Astro.site` fallback in BaseLayout returns pathname-only**, defensive but unreachable in production. Reviewer D2 confirmed not actively misleading (search engines treat relative canonical as relative-to-current-URL = self-referential). Keep defensive fallback.
- **D-P7-5** **Reviewer = `superpowers:code-reviewer` (Opus + adversarial)** — chose 3rd-family inaugural over 2nd-burn pr-family or omc-family. Pattern locked: prefer family rotation when possible to maintain Rule D cross-family isolation; same family is fine for incremental UX phases but infra phases benefit from fresh-family blast radius checks. Phase 8 candidates: 4th-family inaugural (`pr-review-toolkit:silent-failure-hunter`, `pr-review-toolkit:type-design-analyzer`, `oh-my-claudecode:code-reviewer` / `verifier`, `superpowers:silent-failure-hunter` / `requesting-code-review`).
- **D-P7-6** **Phase 7.5 fix bundle applied directly post-reviewer** (rather than deferring all to Phase 8). Cost: 4 files / ~10 LOC / 5 min total. Benefit: reviewer verdict CONDITIONAL_PASS → PASS in single phase, no carryover bookkeeping. Accepted; same pattern as Phase 6.4. Rule for the future: HIGH findings + cheap MEDIUM findings always go in same-phase fix bundle if the verdict path to PASS is well-defined; LOW findings always carryover unless trivially co-located.
- **D-P7-7** **C-P6-2 WCAG 1.4.1 deferred with documented analysis** (instead of carryover-without-rationale, F-5 audit-trail concern). See "C-P6-2 deferral rationale" below — `font-bold` IS a sufficient non-color cue per strict WCAG reading. Deferring is defensible; just needed the analysis stated.
- **D-P7-8** **Test fixture sync in 7.5** — when 7.5 changed ja translations, `CompareFilter.test.tsx` ja branch had to update too. Cleanly handled in same commit. Pattern: when fixing i18n strings post-test-creation, always check test fixtures for hardcoded references. Vitest 32/32 passing post-update confirms no other tests had matching references.

## C-P6-2 deferral rationale (resolves F-5 + C-P7-4)

**Issue**: Phase 6 reviewer flagged `text-accent font-bold` on winner cells as potential WCAG 1.4.1 violation (color-only conveyance).

**Phase 7 reviewer F-5 analysis** (verified): WCAG 1.4.1 requires info conveyed by color also be conveyed by another visual cue. The compare table uses BOTH:
- Color: `text-accent` (CSS variable, theme-dependent)
- Weight: `font-bold` (700 vs default ~400 for `font-serif` Source Serif Pro)

At rendered `text-sm` (14px), the 700-vs-400 weight delta IS perceptible. `font-bold` qualifies as a non-color cue per strict WCAG reading.

**Decision**: **DEFER indefinitely. Not a violation.** Phase 6 reviewer's M-class severity was conservatively-correct-at-flag-time but WCAG analysis confirms the design IS compliant. No code fix needed.

**If future requirements demand stricter conformance** (e.g., government-procurement audit, or color-blind user feedback): add a `★` glyph or `▶` marker to winner cells. ~3 LOC in `CompareFilter.tsx`. Until that requirement materializes, accept current state.

This rationale closes C-P6-2 (RESOLVED, not violation) AND C-P7-4 (audit-trail documented).

## Carryover for Phase 8 (consolidated, IDs C-P7-*)

### Phase 7.5 already RESOLVED (no carryover)

- C-P7-2 redirect canonical chain (F-1 HIGH) — fixed
- C-P7-3 ja convention drift (F-2/F-3/F-4 MEDIUM ×3) — fixed
- C-P7-9 build:fresh composability (F-8 LOW) — fixed

### Phase 8 carryover

- **C-P7-1** Astro i18n soft-404 200 + meta-refresh on unmatched `/[lang]/*` paths — accepted indefinitely; documented in `web/README.md` "Soft-404 on unmatched `/[lang]/*` paths" section. Mitigated by `<meta name="robots" content="noindex">`. No further action.
- **C-P7-4** C-P6-2 WCAG 1.4.1 deferral rationale — RESOLVED via this handoff §"C-P6-2 deferral rationale". `font-bold` is sufficient non-color cue per strict reading. Not a violation. Add visual marker only if future audit requirement materializes.
- **C-P7-5** Master plan §"Phase 7" annotated for Pagefind renumber — addressed in Phase 7 close commit (master plan edit alongside this handoff).
- **C-P7-6** Build noise (4 redirect "no `<html>` element" warnings) — DEFER indefinitely. Pre-existing Phase 6 inherited noise. Cosmetic; suppress by replacing `Astro.redirect()` with explicit `*.astro` wrappers if a future Phase needs to clean CI noise. Add to Phase 9 (Deploy) backlog.
- **C-P7-7** Rule A rubric expansion for translation work — process improvement. For Phase 8+ i18n work: (a) increase sample N to ~50% of translated strings (translation is high-rewrite low-volume; per-string review is cheap), (b) rubric items: lexical accuracy, punctuation matches surrounding dict, grammatical form matches role (placeholder=noun-phrase, label=noun-phrase, sentence=full sentence with terminal punctuation), tone matches voice. Update CLAUDE.md `personal_operating_principles` Rule A or `_template/03_research.md` checklist.
- **C-P7-8** README claim "Cloudflare Pages auto-deploys from `main`" — verify with CF dashboard before first external announcement. Verify-or-amend; cheap.
- **C-P7-10** CF preview probe checklist — process artifact for future infrastructure phases. Items to probe-class: query strings (`?lang=en`), HEAD-vs-GET differences, encoded characters / Unicode in URL paths, lang-neutral resources (sitemap, robots.txt). Add to Phase 9 (Deploy) PLAN as a pre-flight check.

### Pre-existing Phase 6 carryover NOT touched in Phase 7

- **C-P6-2** color-only winner signaling — RESOLVED via C-P7-4 analysis (not a violation)
- **C-P6-4** playwright `reuseExistingServer: true` — PARTIAL (README tribal-knowledge doc only, no code fix). Phase 8+ candidate: change to `!process.env.CI` OR add `pretest:e2e` script that kills port 4321
- **C-P6-5** `/[lang]/guide/platform-comparison` vs `/[lang]/compare` redundancy — DEFER. Design decision pending. Options: cross-link / drop one / merge content
- **C-P6-6** No vitest for plugin lang-neutral throw guard — DEFER. Fixture test before a future cross-ref breaks build at runtime
- **C-P6-7** No `compare-dimensions.json` schema validation — DEFER. zod or content-collection schema before runtime React explosion on malformed entry
- **C-P5-M2** DocsSidebar drawer ViewTransitions — DEFER (no VT enabled)
- **C-P5-L1** Fallback banner i18n — DEFER (banner not on Phase 7 surface; revisit when next i18n surface lands)
- **C-P5-L2** Empty TOC `<aside>` guard — DEFER cosmetic

## Working state — Phase 7 close

- **Branch**: `main`. HEAD = `e7e64c0` (post 7.5 fix bundle). Plus this handoff's index-sync commit pending.
- **`web/` tree** (post Phase 7):
  - 4 i18n keys added: `compare.title`, `compare.subhead`, `compare.filter.placeholder`, `compare.filter.label` × 3 langs (12 strings; 3 ja revised in 7.5 to noun-form + 「。」)
  - `BaseLayout.astro` emits `<link rel="canonical">` + `<meta property="og:url">` site-wide on 27 content pages; 4 redirect routes retain Astro built-in canonical now consistently pointing at content-page canonical (post 7.5 trailing-slash fix)
  - `[lang]/compare.astro` localized chrome (h1 + subhead + BaseLayout title, all from i18n keys)
  - `CompareFilter.tsx` localizes placeholder + aria-label via `getUIStrings(lang)` internal call
  - `package.json` adds `build:fresh` script (composable `npm run build` form)
  - `web/README.md` replaced with project-specific 113-line content (stack / scripts / architecture / 5 tribal-knowledge sections / hosting / release / phase trace)
  - `[lang]/guide/index.astro` redirect target now has trailing slash matching `build.format: 'directory'`
- **Test status**: tsc 0 errors / vitest 32/32 (was 31, +1 i18n test) / e2e 6/6 strict over 8 routes (Phase 6 close baseline preserved) / build 31 HTML pages green (27 content + 4 redirect) / pagefind 3 langs indexed
- **Evidence preserved**: `.work/07_website/phase7/{PLAN.md (242 lines), _progress.json (final state), evidence/checkpoints/{task_7_0..3, task_7_5, phase_7_reviewer}_report.md, subagent_prompts/task_7_4_reviewer_prompt.md}` — full Tier 3 trace.

## How the Phase 8 session should start

1. Read this handoff first.
2. Read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` §"Phase 7 — Search (Pagefind)" lines 2483+ — this is THE master-plan Phase 8 spec post-renumber. Note the Phase 7 annotation at the top (added in this Phase 7 close).
3. Read `.work/07_website/phase7/evidence/checkpoints/phase_7_reviewer_report.md` §"Recommendations for Phase 7 → Phase 8 handoff" — for C-P7-* status detail and Phase 8 entry recommendations.
4. Decisions to make BEFORE Phase 8 entry tasks:
   - a. **Pagefind scope**: stick with master-plan §"Phase 7 — Search (Pagefind)" Tasks 7.1 + 7.2 (Pagefind verify + SearchOverlay React island), OR bundle additional Phase 6/7 carryovers? Recommend: keep tight (Pagefind only), defer C-P6-* carryovers to a separate Phase 9 polish bundle. Phase 7 lesson: when one phase mixes infra + carryover, the carryover absorption rate gets stuck at ~50%. Do one job per phase.
   - b. **Phase 8 reviewer slot pre-allocation**. Cross-family options remaining post Phase 7: `superpowers:silent-failure-hunter` / `superpowers:requesting-code-review` (2nd-burn superpowers), `pr-review-toolkit:silent-failure-hunter` / `type-design-analyzer` (5th-burn pr-family), `oh-my-claudecode:code-reviewer` / `verifier` (2nd-burn omc-family), or fresh family entirely. Recommend: `superpowers:silent-failure-hunter` (2nd-burn superpowers, complementary lens to `code-reviewer`'s positive-finding-style for a search-index introduction phase where silent indexing failures are the failure class).
   - c. **Phase 8 PLAN.md plan deviation flag**: NONE expected. Master plan §"Phase 7 — Search" should be followed verbatim except where Phase 8 reviewer surfaces issues. Document deviation flag if introduced.
5. Same execution mode as Phases 6/7: subagent-driven dev for non-trivial tasks (Pagefind dynamic-import + SearchOverlay React island = ~150 LOC, borderline but reasonable for subagent), direct-verify for trivial, end-of-phase reviewer cross-family before declaring done. Tier 3 trace mandatory.

Family pool state at Phase 7 close: `pr-review-toolkit` ×4 (Phases 1, 2, 3.6, 4), `feature-dev` ×1 (Phase 5), `oh-my-claudecode` ×1 (Phase 6 critic), `superpowers` ×1 (Phase 7 code-reviewer). Phase 8 candidates: `superpowers:silent-failure-hunter` (2nd-burn within family — different agent, complementary lens), `pr-review-toolkit:silent-failure-hunter` (4th-burn pr-family), `oh-my-claudecode:code-reviewer` / `verifier` (2nd-burn omc-family), or 4th-family inaugural.

## Push state at Phase 7 close

`origin/main` = `e1737f1` at session start (Phase 6 close). Phase 7 commits (`3c151de`, `4047b85`, `a1ad23e`, `e7e64c0`) + this handoff's index-sync commit pending push. Phase 7 close push commit = first push to publish Phase 7 to CF Pages.

After push, CF Pages will auto-rebuild, picking up:
- Compare page i18n (zh/ja localized chrome)
- Site-wide canonical
- Redirect-canonical chain fix (the F-1 SEO improvement)
- New `web/README.md` (visible only to repo readers, but useful for future PR contributors)

Verify CF re-deploy via probe matrix from `.work/07_website/phase7/evidence/checkpoints/task_7_0_report.md` ~5 minutes post-push (CF Pages typical build time 2-3 minutes).
