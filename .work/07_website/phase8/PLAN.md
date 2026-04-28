# Website Phase 8 — Search (Pagefind) (Tier 3 plan trace)

> **Date opened**: 2026-04-29
> **Master plan**: `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` §"Phase 7 — Search (Pagefind)" lines 2483+ (annotated 2026-04-29 with renumber-to-Phase-8 deviation note)
> **Predecessor handoff**: `.work/meta/website_phase7_to_phase8_handoff_2026-04-29.md`
> **Branch**: `main` (HEAD = `fbc2ccd` post Phase 7 close + handoff sync; production live at `https://sdtm-pedia.pages.dev/`)

## Scope

Pagefind verify (Task 8.1) + SearchOverlay React island (Task 8.2 — Cmd+K open, Esc close, dynamic Pagefind import, stripHtml excerpt) + reviewer pass (Task 8.3). Tight scope per Phase 7 G-P7-5 lesson ("do one job per phase"). All deferred Phase 6/7 carryovers (C-P6-4/5/6/7 + C-P5-L1/L2/M2 + C-P7-6/7/8/10) stay deferred to a separate Phase 9-or-10 polish bundle.

## Plan deviation flag

**NONE expected.** Phase 8 follows master plan §"Phase 7 — Search (Pagefind)" verbatim except where reviewer surfaces issues. Two minor spec-drift notes (NOT deviations) flagged at session start:

1. **Pagefind output naming drift**: master plan Step 1 (line 2496) says expect `*.pf_index` files. Pagefind 1.5.2 actually emits `index/` + `fragment/` subdirs + `pagefind.{lang}_{hash}.pf_meta` per-lang metadata + `wasm.{lang|unknown}.pagefind` engine binaries. Same artifacts, different file layout. Task 8.1 verification adapted accordingly. Functionally equivalent — search runtime resolves all paths via `pagefind.js`.
2. **4 redirect pages indexing warnings**: build output `4 pages found without an <html> element` matches Phase 7 C-P7-6 (build noise). Correct behavior — redirect pages should NOT be indexed (the canonical content page IS indexed). Pagefind correctly skips them.

## Pre-flight decisions acked at session start (2026-04-29)

1. **Scope = Pagefind only** — Y. Defer C-P6-4/5/6/7 + C-P5-L1/L2/M2 + C-P7-6/7/8/10 to Phase 9-or-10 polish bundle. (Phase 7 G-P7-5 "do one job per phase" lesson.)
2. **Reviewer slot = `pr-review-toolkit:silent-failure-hunter`** — Y. Substituted from initial proposal `superpowers:silent-failure-hunter` (does not exist as a registered agent in this environment — superpowers family only has `code-reviewer`). pr-family 5th-burn but DIFFERENT agent (silent-failure-hunter vs code-reviewer), so Rule D isolation still holds (different prompt + different lens). Cross-family from Phase 7's `superpowers:code-reviewer`. Lens is the exact match for the silent-failure risk class of a search-index introduction phase (build green but index empty / UI renders but URLs broken / dev works but production breaks).
3. **Plan deviation flag = NONE expected** — Y. Master plan §"Phase 7 — Search" followed verbatim.

## Task breakdown

| Task | Mode | Spec | Owner |
|---|---|---|---|
| 8.1 — Verify Pagefind index builds | direct (verification only) | `npm run build` + `ls dist/pagefind/` + capture index stats | main session |
| 8.2 — SearchOverlay React island + tests | subagent dispatch | `SearchOverlay.tsx` (Cmd+K open / Esc close / Pagefind dynamic import / `stripHtml` excerpt) + `.test.tsx` ×2 + `TopNav.astro` mount + ⌘K hint + `e2e/search.spec.ts` | `oh-my-claudecode:executor` opus |
| 8.3 (gate) — End-of-Phase reviewer | reviewer subagent | full Phase 8 commit range | `pr-review-toolkit:silent-failure-hunter` |

## Task 8.1 detail (verify Pagefind builds)

**Goal**: confirm the build pipeline produces a usable Pagefind index that the SearchOverlay (Task 8.2) can dynamic-import. This is the gate before writing Task 8.2 — if build is broken, fix build first.

**Probes**:
- `cd web && npm run build` exits 0
- `ls dist/pagefind/` shows: `pagefind.js`, `pagefind-ui.js`, `pagefind-component-ui.js`, `*.pf_meta` (per-lang), `wasm.*.pagefind`, `index/`, `fragment/` subdirs, `pagefind-entry.json`
- Build output reports ≥3 langs indexed + ≥27 pages indexed (matches Phase 7 close baseline)
- `cat dist/pagefind/pagefind-entry.json` shows valid JSON with `languages` array

**Verification**:
- Build green
- `dist/pagefind/` populated with ≥10 artifacts
- 3 langs indexed (zh/en/ja)
- ≥27 pages indexed (matches Phase 7 close `27 content pages` baseline)
- 4 redirect-page warnings expected (C-P7-6 known noise, not blocking)

**Evidence**: `.work/07_website/phase8/evidence/checkpoints/task_8_1_report.md`

**No commit** (verification-only). Findings feed into Task 8.2 planning OR generate new C-P8-* if regressions surface.

## Task 8.2 detail (SearchOverlay React island)

**Files**:
- Create: `web/src/components/react/SearchOverlay.tsx`
- Create: `web/src/components/react/SearchOverlay.test.tsx`
- Modify: `web/src/components/astro/TopNav.astro` (mount overlay + add ⌘K hint button)
- Create: `web/tests/e2e/search.spec.ts`

**Spec** (verbatim from master plan §"Phase 7 — Search" Task 7.2 lines 2531-2606, with minor adjustments noted in evidence report):

```tsx
// SearchOverlay.tsx — keyboard-driven search overlay
// - Cmd+K (or Ctrl+K) opens, Escape closes
// - Pagefind loaded via dynamic import on first open (no eager bundle cost)
// - Excerpts stripped of HTML before render (no inner-HTML injection, no XSS surface)
// - Results limited to top 10 per query
```

Key design points:
- Pagefind import path: `/pagefind/pagefind.js` (resolved at runtime from public dist root, NOT a Vite import)
- Use `@vite-ignore` comment on the dynamic import to suppress Vite warnings
- Excerpt rendering: `r.excerpt` may contain `<mark>` tags; strip them with regex before render. Use only React's plain text-content render path (`{stripHtml(r.excerpt)}`), never any HTML-injection prop.
- Modal overlay closes on backdrop click (per master plan onClick handler) AND Escape

**Tests** (vitest):
1. `opens on Cmd+K` — render, no searchbox initially, dispatch keydown Cmd+K, searchbox appears
2. `closes on Escape` — render, open with Cmd+K, dispatch Escape, searchbox gone

**TopNav mount**: `<SearchOverlay client:load />` placed alongside ThemeToggle / LangSwitcher. ⌘K hint button dispatches keydown event (cosmetic — Cmd+K still works without it).

**E2E** (playwright):
- `test('search opens with Cmd+K and finds AESER')` — preview server (build first), navigate `/zh/guide/user-guide`, press Cmd+K, fill 'AESER', verify result visible
- Note: requires `npm run build && npm run preview` not just dev (Pagefind index built only on build)

**Verification**:
- `npx tsc --noEmit` 0 errors
- `npm test -- --run` ≥34/34 (was 32 post Phase 7, +2 SearchOverlay tests)
- `npm run build:fresh` green; dist/pagefind/ still populated
- `npm run test:e2e` includes search.spec.ts and passes (CI-equivalent: build → preview → test)

**Commit**:
```bash
git commit -m "07 Website Phase 8.2 — SearchOverlay (Cmd+K, Pagefind dynamic import, plain-text excerpt, 2 tests + e2e)"
```

## Task 8.3 detail (reviewer pass)

**Reviewer**: `pr-review-toolkit:silent-failure-hunter` — pr-family 5th burn but FIRST burn of `silent-failure-hunter` agent within the family (prior 4 burns all `code-reviewer`). Cross-agent within family + cross-family from Phase 7's `superpowers:code-reviewer`. Substituted at session-time from the handoff's recommended `superpowers:silent-failure-hunter` because that agent does not exist as registered in this environment.

**Why this lens**: Pagefind has a high silent-failure surface — build can succeed but index can be empty (no `<html>` in pages, wrong root selector, language detection fails). Search UI can render but result URLs can be broken (Pagefind base path mismatch, dist served from wrong root). Dynamic import path can be wrong but only fail at runtime in production. These are the failure modes silent-failure-hunter is built to surface.

**Brief dimensions** (structured per Phase 6 R-P6-1 + Phase 7 R-P7-1 lesson):
- **D1** Silent index failures: build green, index actually empty? Pagefind warnings ignored?
- **D2** Broken result URLs: Pagefind result `r.url` paths resolve to live pages? Trailing-slash matches `build.format: 'directory'`?
- **D3** Dynamic import path correctness: `/pagefind/pagefind.js` resolves in production hosting (CF Pages)? Asset path consistent across dev/preview/prod?
- **D4** A11y of search overlay: searchbox role, focus management, Escape semantics, label coverage
- **D5** Plan adherence to master plan §"Phase 7 — Search": any drift from spec? Justified?

**Pass criteria**:
- All Phase 8 commits diffed against PLAN.md
- 0 HIGH findings OR all HIGH fixed in 8.4 fix bundle (mirror Phase 7.5 pattern)
- M-level findings deferred OK (carryover IDs C-P8-*)

**Evidence**: `.work/07_website/phase8/evidence/checkpoints/phase_8_reviewer_report.md`
**Subagent prompt**: `.work/07_website/phase8/subagent_prompts/task_8_3_reviewer_prompt.md`

## Reviewer slot pre-allocation (Rule D)

Reviewer family hot list post Phase 7:
- Phase 1, 2, 3.6, 4: `pr-review-toolkit:code-reviewer` (×4)
- Phase 5: `feature-dev:code-reviewer`
- Phase 6: `oh-my-claudecode:critic`
- Phase 7: `superpowers:code-reviewer`

**Phase 8 reviewer slot = `pr-review-toolkit:silent-failure-hunter`** — pr-family 5th-burn but FIRST burn of `silent-failure-hunter` agent (prior pr-family burns all `code-reviewer`). Different agent + complementary lens to Phase 7's `superpowers:code-reviewer`. Originally planned `superpowers:silent-failure-hunter` per handoff, swapped at session-time when the agent was discovered not to be registered.

## Evidence layout

```
.work/07_website/phase8/
├── PLAN.md                              ← this file
├── _progress.json                       ← step verdicts
├── evidence/
│   ├── checkpoints/
│   │   ├── task_8_1_report.md
│   │   ├── task_8_2_report.md
│   │   └── phase_8_reviewer_report.md
│   └── failures/                        ← Rule B: archived not deleted
└── subagent_prompts/                    ← Rule C support
    ├── task_8_2_executor_prompt.md
    └── task_8_3_reviewer_prompt.md
```

## Carryover from Phase 7 to Phase 8 (status mapping)

| ID | Description | Status |
|---|---|---|
| C-P7-1 | Astro i18n soft-404 200 | ACCEPTED indefinitely (documented in `web/README.md`) |
| C-P7-4 | C-P6-2 WCAG 1.4.1 deferral rationale | RESOLVED (handoff §"C-P6-2 deferral rationale") — not a violation |
| C-P7-5 | Master plan annotation | RESOLVED (annotated in Phase 7 close commit `fbc2ccd`) |
| C-P7-6 | 4 redirect "no `<html>` element" warnings | DEFER to Phase 9-or-10 polish — visible in Task 8.1 build noise too, no impact |
| C-P7-7 | Rule A rubric expansion for translation | DEFER process improvement (no new translation in Phase 8) |
| C-P7-8 | README "auto-deploys from main" verify | DEFER — verify-before-external-announcement |
| C-P7-10 | CF preview probe checklist | DEFER to Phase 9 (Deploy) PLAN |
| C-P6-2 | Color-only winner signaling | RESOLVED via C-P7-4 (not a violation) |
| C-P6-4 | playwright `reuseExistingServer: true` | DEFER to polish bundle |
| C-P6-5 | platform-comparison vs compare redundancy | DEFER design decision |
| C-P6-6 | No vitest for plugin lang-neutral throw | DEFER fixture test |
| C-P6-7 | No `compare-dimensions.json` schema validation | DEFER defensive |
| C-P5-M2 | DocsSidebar drawer ViewTransitions | DEFER (no VT enabled) |
| C-P5-L1 | Fallback banner i18n | DEFER (banner not on Phase 8 surface) |
| C-P5-L2 | Empty TOC `<aside>` guard | DEFER cosmetic |

## Exit criteria

1. tsc 0 errors
2. vitest ≥34 (≥2 SearchOverlay tests added)
3. e2e includes search.spec.ts and passes
4. `npm run build:fresh` green; `dist/pagefind/` still populated; SearchOverlay reachable from any page via Cmd+K
5. Manual probe: open `/zh/guide/user-guide`, press Cmd+K, search 'AESER', click result, lands on correct page
6. `pr-review-toolkit:silent-failure-hunter` reviewer verdict ≥ CONDITIONAL_PASS, all HIGH fixed
7. Phase 8 → Phase 9 handoff doc at `.work/meta/website_phase8_to_phase9_handoff_2026-04-29.md`
8. Index sync (CLAUDE.md Key Paths + MANIFEST + worklog + PROGRESS.md) committed in Phase 8 close

## Rule A semantic spot-check

Phase 8 introduces no new translated strings (search overlay placeholder = "Search docs..." kept English-only per master plan spec; localizing the placeholder is a Phase 9-or-10 polish item if user-facing demand surfaces). N=0 translation surface → Rule A spot-check **N/A** for Phase 8. If Daisy wants the placeholder localized, add 3 keys × 3 langs to `ui.{zh,en,ja}.json` and apply Rule A N=3 (per Phase 7 R-P7-6 + C-P7-7 expanded rubric).

## Rule B / C / D applied

- **B**: failed attempts archive in `evidence/failures/` (none expected for verification + spec-driven implementation).
- **C**: retro at Phase 8 close = handoff doc.
- **D**: writer = `oh-my-claudecode:executor` opus (Task 8.2); reviewer = `pr-review-toolkit:silent-failure-hunter` (different family from Phase 7's superpowers + different agent within pr-family from prior 4 code-reviewer burns + complementary silent-failure lens). Task 8.1 + 8.3 directly handled in main session (verification + dispatch).

## How a fresh session should start Phase 8

1. Read `.work/meta/website_phase7_to_phase8_handoff_2026-04-29.md` (predecessor retro).
2. Read this PLAN.md.
3. Read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` lines 2483+ for the master plan §"Phase 7 — Search" content (Pagefind), then ack plan deviation = NONE.
4. Confirm 3 entry decisions:
   a. Scope = Pagefind only (defer C-P6-* + C-P7-* polish to Phase 9-or-10) — Y/N
   b. Reviewer slot = `pr-review-toolkit:silent-failure-hunter` (substituted from handoff's `superpowers:silent-failure-hunter` because that agent isn't registered) — Y/N
   c. Plan deviation flag = NONE expected — Y/N
5. Execute tasks 8.1 → 8.2 → 8.3 with TaskCreate/TaskUpdate or _progress.json tracking.
6. Phase 8 close: handoff doc + index sync (CLAUDE.md Key Paths + MANIFEST + worklog + PROGRESS.md) + commit + push.
