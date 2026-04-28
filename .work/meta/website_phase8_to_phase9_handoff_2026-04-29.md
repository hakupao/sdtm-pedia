# Website Build — Phase 8 → Phase 9 Handoff

> **Date**: 2026-04-29
> **Outgoing session**: Phase 8 (Search — Pagefind) — 2 commits on `main` (post Phase 7 close)
> **Incoming session**: Phase 9 (Downloads Pipeline — original master plan §"Phase 8" pre-renumber)
> **Branch**: `main`. HEAD = `b00b63c`. Plus this handoff's index-sync commit pending.

## What's done — Phase 8

| Commit | Subject |
|---|---|
| `4206203` | 07 Website Phase 8.2 — SearchOverlay (Cmd+K, Pagefind dynamic import, plain-text excerpt, 2 tests + e2e) |
| `b00b63c` | 07 Website Phase 8.5 — reviewer fix bundle (F-1 HIGH + F-2/3/4/5 MEDIUM ×4): SearchOverlay i18n + ⌘K hint i18n + safer dynamic-import .catch + e2e test name honesty |

(Phase 8.1 = verification-only, no commit — Pagefind 1.5.2 build pipeline pre-existed; output naming spec drift `*.pf_index` → `index/`+`fragment/` subdirs documented in PLAN.md as non-deviation.)
(Phase 8.3 reviewer pass = no source change — report committed alongside 8.5 evidence.)
(Phase 8.4 not used — Phase 8 jumped from 8.3 to 8.5 fix bundle mirroring Phase 7's 7.4→7.5 numbering.)

Note on parent: `4206203` parents `dd67cee` (06 Deep Verification round 11 reconciler closure committed by parallel session during this Phase 8 work). Zero cross-lane contamination — Phase 8 commits only touch `web/` paths, deep-verification reconciler only touched `.work/06_deep_verification/`.

## End-of-Phase-8 reviewer verdict

`pr-review-toolkit:silent-failure-hunter` (substituted at session-time from handoff's `superpowers:silent-failure-hunter` — that agent does not exist as registered in this environment; pr-family 5th burn but FIRST burn of `silent-failure-hunter` agent within pr-family — prior 4 pr-family burns were all `code-reviewer`. Cross-family from Phase 7's `superpowers:code-reviewer`). Initial **CONDITIONAL_PASS H=1 M=4 L=5** (report 453 lines at `.work/07_website/phase8/evidence/checkpoints/phase_8_reviewer_report.md`). The HIGH (F-1 silent i18n regression — search overlay hardcoded English chrome despite `search.placeholder` keys already defined in all 3 locale files pre-Phase-8) was the exact "feature shipped without consuming pre-existing locale infrastructure" failure class Phase 7 reviewer caught on `compare.subhead.ja` — second cumulative instance.

**Phase 8.5 fix bundle applied** (commit `b00b63c`, 4 files / +25 -11 LOC): F-1 + F-2 + F-3 + F-4 + F-5. Verified via dist HTML grep (`<astro-island ... props="{lang:[0,ja]}" ...>` on JA route + ⌘K button text rendered from `t['search.shortcut']`) + e2e 7/7 against `npm run preview`. Reviewer brief upgrade path satisfied → **effective PASS** for Phase 9 entry. Remaining LOW findings (F-6/F-8/F-9/F-10) deferred to Phase 9 polish bundle as C-P8-3..6.

## Pre-flight decisions made at Phase 8 start (carryover from Phase 7 handoff)

1. **Scope = Pagefind only (defer C-P6-* + C-P7-* polish to Phase 9-or-10)** — Y. Phase 7 G-P7-5 "do one job per phase" lesson applied; carryover absorption deferred to dedicated phase.
2. **Reviewer slot = `pr-review-toolkit:silent-failure-hunter`** — Y. Substituted from handoff's recommended `superpowers:silent-failure-hunter` (does not exist as registered; superpowers family only has `code-reviewer`). pr-family 5th burn but FIRST burn of `silent-failure-hunter` agent (prior 4 pr-family burns all `code-reviewer`) — different agent + different prompt + complementary silent-failure lens. Daisy ack: "好的走a".
3. **Plan deviation flag = NONE expected** — Y. Master plan §"Phase 7 — Search" followed verbatim. Two minor spec-drift notes (NOT deviations): (i) Pagefind 1.5.2 output naming uses `index/`+`fragment/` subdirs + `*.pf_meta` instead of `*.pf_index` per master plan Step 1; (ii) 4 redirect pages "no `<html>` element" warnings = pre-existing C-P7-6 expected behavior (correct: redirect pages should not be indexed).

## §1 Retrospective — what went well (Rule C R-P8-*)

- **R-P8-1** Phase 7's structured-brief reviewer prompt pattern (R-P7-1) carried forward as `phase8/subagent_prompts/task_8_3_reviewer_prompt.md` (5 stress dimensions D1-D5: silent index failures / broken result URLs / dynamic import path correctness / a11y / plan adherence). Result: 1 HIGH + 4 MEDIUM + 5 LOW = 10 findings, same yield-per-LOC as Phase 7's 11 findings on a larger surface. Brief structure proved repeatable and *adversarially calibrated* (silent-failure-hunter caught a class of bug code-reviewer might have missed: "feature shipped without consuming infrastructure that already exists").
- **R-P8-2** Subagent dispatch for Task 8.2 (oh-my-claudecode:executor opus, ~150 LOC across 4 files) returned commit `4206203` with 3 well-justified spec adjustments (Adj-1 vite-ignore indirection / Adj-2 e2e button-click proxy / Adj-3 a11y parity) plus 2 informational blockers (B-1 playwright webServer config / B-2 astro-island await-children). Brief-side constraint "STOP if e2e needs config change" honored cleanly — executor flagged B-1 as C-P8-1 candidate rather than scope-creep into playwright.config.ts. Pattern locked: subagent for substantial work (~150 LOC threshold), main-session for verify + reviewer dispatch + close.
- **R-P8-3** Pre-flight verification (Task 8.1) PASS gated Task 8.2 dispatch cheaply — `npm run build` + `ls dist/pagefind/` + parse `pagefind-entry.json` gave 100% confidence the SearchOverlay's dynamic import target would exist before any LOC was written. Same pattern as Phase 7 R-P7-3 ("CF Pages preview probe with control probes") — verify the surface the new feature depends on, before building the new feature.
- **R-P8-4** Reviewer F-1 root cause = "feature shipped without consuming pre-existing locale infrastructure". The keys (`search.placeholder` + `search.shortcut`) were defined in `ui.{zh,en,ja}.json:18-19` BEFORE Phase 8 — someone anticipated the search overlay. Phase 8 PLAN.md mistakenly said "Phase 8 introduces no new translated strings (search overlay placeholder = 'Search docs...' kept English-only per master plan spec)". The reviewer's discovery exposed the PLAN's premise as wrong + caught the silent regression in same pass. Pattern lesson: when a phase introduces a feature that touches an infrastructure-providing module (i18n, canonical, sitemap, etc.), grep the infrastructure FIRST for matching keys/registrations, not LAST. Captured as C-P8-7 process improvement.
- **R-P8-5** F-5 root cause = "test name claims raw Cmd+K trigger but actually clicks ⌘K hint button". Adj-2 in Task 8.2 documented WHY (headless chromium keyboard delivery quirk) but the test name still lied. Reviewer caught the inconsistency in a single read. Pattern: test name MUST reflect what the test actually does, not what we wished it did. The Adj-2 workaround is fine; the misnamed test was a separate sin. C-P8-2 tracks the eventual real-keypress test once C-P8-1 unblocks it.
- **R-P8-6** Phase 7.5 fix bundle pattern (CONDITIONAL_PASS → PASS in same phase via small mechanical fixes) repeated cleanly in Phase 8.5 (5 fixes / +25 LOC / single commit). Carryover bookkeeping for HIGH findings avoided. Rule for the future locked: when reviewer surfaces HIGH + cheap MEDIUM with a documented small fix path, fix in same phase via N.5 commit.
- **R-P8-7** Tier 3 trace artifacts (PLAN.md 244 lines + _progress.json + 8.1/8.2/8.5 task evidence reports + reviewer report 453 lines + 2 subagent prompts) all preserved and committed. Future archeology can reconstruct the full decision chain from `git log --follow .work/07_website/phase8/`. Same pattern as Phase 7 R-P7-7 sustained.

## §2 Gaps (Rule C G-P8-*)

- **G-P8-1** Handoff recommended reviewer agent (`superpowers:silent-failure-hunter`) doesn't exist in this environment. The handoff was written by Phase 7 close session without verifying agent registration. Pattern lesson: when the handoff pre-allocates a Rule D reviewer slot, verify the agent IS registered (or note the substitution path explicitly). Captured: future phase handoffs should include `(verified registered N/A 2026-04-29)` annotation OR a tested-substitute list. Process improvement R-P8-2 carryforward candidate.
- **G-P8-2** Phase 8 PLAN.md §"Rule A semantic spot-check" said "Phase 8 introduces no new translated strings" + "If Daisy wants the placeholder localized, add 3 keys × 3 langs". This was wrong — the keys ALREADY EXISTED. The PLAN was written without grepping `ui.{zh,en,ja}.json` for `search.*`. The mistake didn't cost much because the F-1 reviewer caught + 8.5 fixed it, but future Phase PLANs should grep infrastructure for matching keys at write-time. R-P8-4 sister.
- **G-P8-3** Phase 7's `superpowers:silent-failure-hunter` recommendation was based on the assumption that `superpowers` package mirrors `pr-review-toolkit`'s agent set. It does not — `superpowers` family ships only `code-reviewer`, `requesting-code-review`, etc. but NOT `silent-failure-hunter`. The Rule D pre-allocation logic should not assume agent-name parity across families. Pattern lesson: family-rotation Rule D logic needs an explicit "agent of family X with lens Y" lookup, not name-parity guessing.
- **G-P8-4** F-4 fix uses `import.meta.env.PROD` to gate the `console.warn`. This is a Vite primitive that's been around since Vite 2 (verified — `pagefind` and `astro` both use it internally). However: if Astro ever migrates off Vite (unlikely but documented), this guard breaks silently. No alternative checked. Pattern: `import.meta.env.*` is fine for now; if the Vite assumption is ever revisited project-wide, audit for this guard.
- **G-P8-5** Phase 8 absorbed 0 of the deferred Phase 6/7 carryovers (C-P6-4/5/6/7 + C-P5-L1/L2/M2 + C-P7-6/7/8/10). All deferred to Phase 9-or-10 polish bundle. Phase 7 G-P7-5 lesson (deferring half the carryover is OK if scope is sequence-driven, but the deferred items should be re-prioritized in Phase N+1 PLAN) applies again. Phase 9 PLAN should explicitly state which it absorbs.

## §3 Decisions (Rule C D-P8-*)

- **D-P8-1** **Plan deviation: NONE.** Master plan §"Phase 7 — Search (Pagefind)" Tasks 7.1+7.2 followed verbatim except for: (a) spec drift on Pagefind output naming (documented as non-deviation in PLAN.md); (b) Adj-1/2/3 implementation adjustments documented in 8.2 evidence; (c) reviewer agent substitution documented in 8.3 evidence. None of these are scope/intent deviations — all are mechanical responses to environment realities. Pattern locked: spec-drift documentation as non-deviation flag is acceptable form.
- **D-P8-2** **Reviewer = `pr-review-toolkit:silent-failure-hunter` substituted from `superpowers:silent-failure-hunter`** when the latter discovered not-registered. Substitution presented to Daisy with 4 options A/B/C/D + tradeoffs; Daisy chose A. The substitution maintains Rule D isolation (different prompt + different lens + cross-family from Phase 7) and is the *better-fit* lens for Phase 8's risk profile (silent index failures = literally what the agent's prompt is built for). Process artifact: when handoff-recommended agent unavailable, present substitute options with Rule D tradeoffs to user, don't unilaterally swap.
- **D-P8-3** **Phase 8.5 fix bundle scope = ALL 5 findings (F-1 HIGH + F-2/3/4/5 MEDIUM)**. User pre-authorized "全做(F-1+2+3+4+5)" + LOW findings F-6..F-10 deferred. Same pattern as Phase 6.4 + Phase 7.5 — HIGH always fixes in same phase if path is mechanical; MEDIUM bundle when LOC is small + same edit family; LOW always carryover unless trivially co-located. Locked.
- **D-P8-4** **Search overlay placeholder localization decision: localize using PRE-EXISTING `search.placeholder` keys in `ui.{zh,en,ja}.json`**, not adding new keys (PLAN.md's premise). Confirmed correct after F-1 surfaced the pre-existing keys. The locale values (zh: `搜索文档...` / ja: `ドキュメント検索...` / en: `Search docs...`) were reasonable as-is — no Rule A spot-check needed beyond the dist HTML grep verification (existing translations, not new ones).
- **D-P8-5** **Search overlay aria-label decision: reuse `t['search.placeholder']` for both `placeholder` and `aria-label`** instead of adding a separate `search.aria` key. The placeholder string is a valid noun-phrase in all 3 langs that works as both label + placeholder text. Scope minimization. If accessibility audit requires a more specific aria pattern (e.g. "Search documentation, results appear below"), add the key then.
- **D-P8-6** **TopNav button aria-label `"Open search"` left English-only.** F-1 reviewer flagged the visible `⌘K` text (F-2) and the SearchOverlay input aria-label (F-3) but NOT the TopNav button's `aria-label="Open search"`. Decision: defer to a future a11y review pass — adding it now would expand i18n surface beyond reviewer findings. If user demand surfaces, add `nav.search.button.aria` key cluster (would need 3 langs × 1 key = 3 strings + Rule A N=3).
- **D-P8-7** **F-4 .catch console.warn gated by `import.meta.env.PROD`.** Chosen for: vitest jsdom + dev server stay quiet (no test noise), production gets DevTools-visible signal of unexpected runtime failures. Trade-off: Astro might migrate off Vite eventually, which would break this guard silently. Acceptable risk — Vite is locked-in for the foreseeable future + the failure mode (no warning logged) is itself silent so the regression is bounded to the diagnostic surface we just added.
- **D-P8-8** **F-5 e2e test rename over rewrite.** Considered: (option a) rename test to honest description + comment block + C-P8-2 carryover for real-keypress promotion when C-P8-1 lands, vs (option b) add real `body.focus() + page.keyboard.press('Control+k')` fallback now. Chose (a) for: (i) playwright config change required for option b is exactly what C-P8-1 tracks (don't double-fix); (ii) renaming + commenting captures the WHY for future me; (iii) vitest still covers the raw-keydown wiring layer separately. Locked. C-P8-2 explicit graduation criterion documented in test header comment.

## Carryover for Phase 9 (consolidated, IDs C-P8-*)

### Phase 8.5 already RESOLVED (no carryover)

- C-P8-(F-1) silent i18n regression — fixed
- C-P8-(F-2) ⌘K hint i18n — fixed
- C-P8-(F-3) aria-label English — fixed
- C-P8-(F-4) `.catch(()=>{})` silent swallow — fixed (PROD-only console.warn)
- C-P8-(F-5) e2e test name lies — fixed (rename + comment)

### Phase 9 carryover (numbered)

- **C-P8-1** Switch playwright `webServer.command` from `npm run dev` to `npm run build && npm run preview`. Required for `search.spec.ts` to run in CI green out-of-the-box (Pagefind index built only on `npm run build`). Cost: ~2-3s slowdown per e2e run. Defer to Phase 9 polish OR Phase 10 (Deploy) PLAN as a pre-flight check. Source: F-7 LOW + Task 8.2 B-1.
- **C-P8-2** Promote `search.spec.ts` from synthetic-keydown via ⌘K button click → real `page.keyboard.press('Control+k')` once C-P8-1 lands. Investigate why headless chromium doesn't deliver Meta+k to the React document listener without focus (likely browser-chrome consumes the shortcut). Source: F-5 fix comment.
- **C-P8-3** No focus-return on overlay close (Esc / backdrop click). Pattern: store `document.activeElement` on open, restore focus on close. ~5 LOC in `SearchOverlay.tsx`. Source: F-6 LOW.
- **C-P8-4** No ARIA live region for results announcement. Screen reader users get no notification when results populate. Add `<div role="status" aria-live="polite" class="sr-only">` summarizing result count. ~3 LOC. Source: F-8 LOW.
- **C-P8-5** No retry / bounded backoff if Pagefind init fails partway. Currently `.catch` warns once and search returns 0 results forever. Could add 1-2 retries with 500ms / 1500ms backoff. Rare prod case but cheap to harden. Source: F-9 LOW.
- **C-P8-6** ⌘K hint button visible only on `md:` breakpoint (mobile users have no visual affordance for the keyboard shortcut, though Cmd+K still works). Mobile UX: either hide on mobile (current state, defensible) or show a tappable search icon instead. Defer pending mobile UX direction. Source: F-10 LOW.
- **C-P8-7** [Process improvement] Pre-PLAN infrastructure grep: when a phase introduces a new feature that touches an infrastructure module (i18n keys, canonical infrastructure, sitemap, etc.), grep the infrastructure for matching keys/registrations BEFORE writing the PLAN. Phase 8 PLAN.md mistakenly said "no new translated strings" without grepping `search.*` in `ui.{zh,en,ja}.json:18-19`. R-P8-4 sister. Update CLAUDE.md `personal_operating_principles` Rule A or `_template/03_research.md` checklist.
- **C-P8-8** [Process improvement] Pre-allocated reviewer agent verification: when handoff pre-allocates a Rule D reviewer slot, verify the agent IS registered before the next-phase session opens. Phase 7 close handoff's `superpowers:silent-failure-hunter` recommendation cost a session-time substitution discussion. Future handoffs: include `(verified registered 2026-MM-DD)` annotation OR provide tested-substitute list. G-P8-1 + G-P8-3 capture.

### Pre-existing Phase 6/7 carryover NOT touched in Phase 8

- **C-P7-1** Astro i18n soft-404 200 — ACCEPTED indefinitely (documented in `web/README.md`)
- **C-P7-4** C-P6-2 WCAG 1.4.1 deferral rationale — RESOLVED in Phase 7 close (not a violation)
- **C-P7-5** Master plan annotation — RESOLVED in Phase 7 close + extended in this Phase 8 close
- **C-P7-6** 4 redirect "no `<html>` element" warnings — DEFER to Phase 9-or-10 polish (still visible in Phase 8 build noise, no impact)
- **C-P7-7** Rule A rubric expansion for translation work — DEFER process improvement
- **C-P7-8** README "auto-deploys from main" verify — DEFER (verify-before-external-announcement)
- **C-P7-10** CF preview probe checklist — DEFER to Phase 10 (Deploy) PLAN
- **C-P6-2** color-only winner signaling — RESOLVED via C-P7-4
- **C-P6-4** playwright `reuseExistingServer: true` — DEFER (related but distinct from C-P8-1)
- **C-P6-5** `/[lang]/guide/platform-comparison` vs `/[lang]/compare` redundancy — DEFER design decision
- **C-P6-6** No vitest for plugin lang-neutral throw guard — DEFER fixture test
- **C-P6-7** No `compare-dimensions.json` schema validation — DEFER defensive
- **C-P5-M2** DocsSidebar drawer ViewTransitions — DEFER (no VT enabled)
- **C-P5-L1** Fallback banner i18n — DEFER (banner not on Phase 8 surface)
- **C-P5-L2** Empty TOC `<aside>` guard — DEFER cosmetic

## Working state — Phase 8 close

- **Branch**: `main`. HEAD = `b00b63c` (post 8.5 fix bundle). Plus this handoff's index-sync commit pending.
- **`web/` tree** (post Phase 8):
  - `web/src/components/react/SearchOverlay.tsx` (NEW, 105 LOC post 8.5) — Cmd+K open, Esc close, Pagefind dynamic import via `pagefindUrl` const + `/* @vite-ignore */`, `stripHtml(r.excerpt)` plain-text render, top 10 results, `lang` prop default 'en', `t['search.placeholder']` for placeholder + aria-label, `import.meta.env.PROD`-gated console.warn on dynamic-import failure.
  - `web/src/components/react/SearchOverlay.test.tsx` (NEW, 21 LOC) — 2 vitest cases (open on Cmd+K + close on Escape), `<SearchOverlay lang="en" />` fixtures.
  - `web/tests/e2e/search.spec.ts` (NEW, 35 LOC post 8.5) — 1 playwright e2e via ⌘K hint button click (synthetic keydown), preview-server lane documented in header + comment block tying to C-P8-2 promotion criterion.
  - `web/src/components/astro/TopNav.astro` (MODIFIED, +10 LOC) — imports SearchOverlay, mounts `<SearchOverlay client:load lang={lang} />` + ⌘K hint button rendering `{t['search.shortcut']}`.
  - `dist/pagefind/` (BUILD ARTIFACT, 17 files / 932K) — 3 langs / 27 pages / 6454 words indexed.
- **Test status**: tsc 0 errors / vitest 34/34 (was 32, +2 SearchOverlay tests) / e2e 7/7 strict against `npm run preview` (was 6/6, +1 search.spec.ts) / build 31 HTML pages green / Pagefind 27 pages indexed.
- **Evidence preserved**: `.work/07_website/phase8/{PLAN.md (244 lines), _progress.json (final state), evidence/checkpoints/{task_8_1, task_8_2, task_8_5_fix_bundle, phase_8_reviewer}_report.md, subagent_prompts/{task_8_2_executor, task_8_3_reviewer}_prompt.md}` — full Tier 3 trace.

## How the Phase 9 session should start

1. Read this handoff first.
2. Read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` §"Phase 8 — Downloads Pipeline" lines 2649+ — this is THE master-plan Phase 9 spec post-renumber. Note the Phase 7+8 close annotations at the top of §"Phase 7 — Search" (added in Phase 7 close + extended in this Phase 8 close).
3. Read `.work/07_website/phase8/evidence/checkpoints/phase_8_reviewer_report.md` §"Recommendations for Phase 8 → Phase 9 handoff" — for C-P8-* status detail and Phase 9 entry recommendations.
4. Decisions to make BEFORE Phase 9 entry tasks:
   - a. **Phase 9 scope**: stick with master-plan §"Phase 8 — Downloads Pipeline" Tasks 8.1 + 8.2 + 8.3 (build-bundles.sh + RELEASE.md + cut v1.0 GH Release), OR bundle Phase 6/7/8 carryovers (C-P8-1..6 + C-P7-* + C-P6-*)? Recommend: KEEP TIGHT (Downloads Pipeline only) — this is the release-critical path; carryovers are polish/UX best handled in a dedicated Phase 10-or-11 polish bundle AFTER deploy. Phase 7 G-P7-5 + Phase 8 G-P8-5 lessons.
   - b. **Phase 9 reviewer slot pre-allocation** (verify agent IS registered, per C-P8-8 lesson). Cross-family options remaining post Phase 8: `oh-my-claudecode:code-reviewer` / `verifier` (2nd-burn omc-family), `pr-review-toolkit:type-design-analyzer` (6th-burn pr-family, different agent), `superpowers:requesting-code-review` (2nd-burn superpowers, different agent), or 4th-family inaugural (`feature-dev:code-architect` for the bash script + release pipeline architecture lens? would be good fit). Recommend: `feature-dev:code-architect` — Phase 9 introduces shell-script tooling + release-pipeline integration; architecture lens (vs code-reviewer's quality lens) better matches "is the design fit for purpose?" failure class. Backup: `oh-my-claudecode:verifier` for evidence-based verification of GH Release URL resolution.
   - c. **Phase 9 PLAN.md plan deviation flag**: NONE expected. Master plan §"Phase 8 — Downloads Pipeline" should be followed verbatim. Document deviation flag if introduced.
5. Same execution mode as Phases 6/7/8: subagent-driven dev for non-trivial tasks (Task 8.1 build-bundles.sh = small bash, direct OK; Task 8.3 cut GH Release = NETWORK-SIDE-EFFECT, needs human-in-loop OR explicit ack), direct-verify for trivial, end-of-phase reviewer cross-family before declaring done. Tier 3 trace mandatory.

Family pool state at Phase 8 close: `pr-review-toolkit` ×5 (Phases 1, 2, 3.6, 4 = code-reviewer + Phase 8 = silent-failure-hunter), `feature-dev` ×1 (Phase 5), `oh-my-claudecode` ×1 (Phase 6 critic), `superpowers` ×1 (Phase 7 code-reviewer). Phase 9 candidates: `feature-dev:code-architect` (2nd-burn feature-dev, different agent — RECOMMENDED for Phase 9 spec fit), `oh-my-claudecode:code-reviewer`/`verifier` (2nd-burn omc), `superpowers:requesting-code-review` (2nd-burn superpowers), `pr-review-toolkit:type-design-analyzer`/`pr-test-analyzer` (6th-burn pr, different agents).

## Push state at Phase 8 close

`origin/main` = `dd67cee` at session start (06 Deep Verification round 11 reconciler closure, NOT Phase 7 close — `dd67cee` parents `fbc2ccd` Phase 7 close in the cumulative log, but `dd67cee` is the latest origin/main HEAD because the deep-verification reconciler pushed during this Phase 8 work). Phase 8 commits (`4206203`, `b00b63c`) + this handoff's index-sync commit pending push. Phase 8 close push commit will publish Phase 8 to CF Pages.

After push, CF Pages will auto-rebuild, picking up:
- SearchOverlay React island reachable site-wide via Cmd+K (mounted in TopNav)
- Pagefind 27-page index served at `/pagefind/*`
- ⌘K hint button in nav (md:+ breakpoint)
- F-1 i18n fix (search overlay localized chrome on /ja and /zh routes)
- F-4 PROD-only `console.warn` if Pagefind init fails (DevTools telemetry)

Verify CF re-deploy ~5 minutes post-push:
- `curl -sI https://sdtm-pedia.pages.dev/pagefind/pagefind.js` → expect HTTP 200 + `Content-Type: text/javascript`
- Browser open `https://sdtm-pedia.pages.dev/zh/guide/user-guide/`, press Cmd+K, observe `搜索文档...` placeholder (NOT `Search docs...`)
- Browser open `https://sdtm-pedia.pages.dev/ja/guide/user-guide/`, press Cmd+K, observe `ドキュメント検索...` placeholder
- Search "AESER" should return ≥1 hit pointing at `/zh/guide/user-guide/` or sibling routes
