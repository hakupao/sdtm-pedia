# Phase 5 end-of-phase reviewer — verdict + remediation log

**Date**: 2026-04-28
**Reviewer**: `feature-dev:code-reviewer`, agentId `a9a0cf22ddee7e31a`
**Rule D isolation**: cross-family from `pr-review-toolkit:code-reviewer` (used Phase 1, 2, 3.6, 4) — fresh family, no prior collision in 4 prior reviewer slots
**Scope**: commits `496ae6f` (5.1) + `43d7445` (5.2) + `56a18f7` (5.3) cumulative diff vs `8e7bd83`

## Verdict (initial): CONDITIONAL_PASS — H=3 M=3 L=2

## Final verdict (post-remediation): PASS

All 3 HIGH + 1 MEDIUM (M1) fixed in commit `ae05afd` (Phase 5.4 reviewer-fix bundle). Other 2 MEDIUM + 2 LOW deferred to Phase 5→6 carryover with rationale.

## HIGH findings — all fixed in `ae05afd`

### H1 — `PrevNextNav` filter excludes lang-neutral docs

- **File**: `web/src/components/astro/PrevNextNav.astro:6`
- **Bite**: Filter `e.data.lang === lang` (strict) excluded `lang === undefined` entries (DEMO_QUESTIONS), so `findIndex(d.data.slug === currentSlug)` returned `-1` on the DEMO page → prev/next always null. Adjacent docs in the sidebar got wrong neighbors (skipped over DEMO).
- **Fix**: Filter changed to `e.data.lang === lang || e.data.lang === undefined` to match `DocsSidebar`.
- **Verification**: e2e link-resolution + docs-reader test both pass; build emits `prev`/`next` links correctly across the lang-neutral DEMO_QUESTIONS entry.

### H2 — `changelog.astro` serves English source to zh/ja routes with no banner

- **File**: `web/src/pages/[lang]/changelog.astro:12-14`
- **Bite**: `all.find(d => d.data.slug === 'changelog')` ignored lang. CHANGELOG has `lang: en`, so zh/ja visitors at `/zh/changelog` and `/ja/changelog` got the English document body silently with no "translation pending" banner — bypassing the catchall's `fallback: true` logic.
- **Fix**: Added `const fallback = entry.data.lang !== undefined && entry.data.lang !== lang;` and conditional banner render. Footer link target `/${lang}/changelog` (NOT `/${lang}/guide/changelog`) preserved — dedicated route stays, gains correct fallback.
- **Verification**: build green; banner conditionally renders. (Visual confirmation deferred until human eyeballs the page; e2e link-resolution doesn't assert visible banner.)

### H3 — Schema says `slug.optional()` but `generateId` throws on missing slug

- **File**: `web/src/content.config.ts:27`
- **Bite**: Latent build-bomb. Schema let docs without `slug:` pass validation; runtime then threw with a generic error and silently failed the entire `guide` collection. Next doc added without `slug:` would break all 21 routes.
- **Fix**: Schema changed `slug: z.string().optional()` → `slug: z.string()` (required). Generic generateId throw retained as defense-in-depth. Schema validation now produces a clearer error before runtime.
- **Verification**: build green (all 7 release v1.0 top-level docs already have `slug:` — confirmed empirically before fix).

## MEDIUM findings

### M1 — e2e link-resolution skips `/en/` and `/ja/` (FIXED)

- **File**: `web/tests/e2e/smoke.spec.ts:29`
- **Fix**: Routes array extended to `['/zh/', '/en/', '/ja/', '/zh/guide/user-guide', '/zh/changelog']`. Now exercises lang-switcher targets across all 3 langs.
- **Verification**: e2e run shows 6/6 passed including link-resolution covering 5 routes.

### M2 — `DocsSidebar` mobile drawer JS = new instance of TopNav-M2 pattern (DEFERRED)

- **File**: `web/src/components/astro/DocsSidebar.astro:26`
- **Why deferred**: View Transitions not enabled in any phase yet. Net-new M2 instance; identical fix pattern to TopNav M2 carryover. Address as part of a single VT-enablement bundle when Phase 5+ enables `<ViewTransitions />`.
- **Carryover ID**: C-P5-M2.

### M3 — `TopNav` link `/${lang}/guide/` (trailing slash) may 404 on certain hosts (DEFERRED)

- **File**: `web/src/components/astro/TopNav.astro:15`
- **Why deferred**: Hosting-config dependent. Astro static build emits `index.html` files which most static hosts serve correctly for both `/${lang}/guide` and `/${lang}/guide/`. Will be checked during Cloudflare Pages deploy smoke (Phase 9). e2e link-resolution covers it in dev mode (passes).
- **Carryover ID**: C-P5-M3.

## LOW findings — deferred

### L1 — Fallback banner copy hard-coded English

- **Files**: `web/src/pages/[lang]/guide/[...slug].astro:40` + `web/src/pages/[lang]/changelog.astro` (banner block added in H2 fix)
- **Why deferred**: Cosmetic. Banner appears only on en→zh/ja fallback pages where the body itself is English. Localizing the banner line to zh/ja is i18n-debt, not a Phase 5 blocker. Add an i18n key `'fallback.banner'` when next touching `i18n/ui.{zh,en,ja}.json`.
- **Carryover ID**: C-P5-L1.

### L2 — `DocsTOC` renders empty `<aside>` for headings-less docs

- **File**: `web/src/components/astro/DocsTOC.astro`
- **Why deferred**: Cosmetic, xl-screen only. All 7 release v1.0 docs have multiple h2/h3 — never zero. Add `{filtered.length > 0 && <aside>...</aside>}` guard when next touching the file.
- **Carryover ID**: C-P5-L2.

## Phase 5 close metrics

| Metric | Before Phase 5 (`8e7bd83`) | After Phase 5 (`ae05afd`) |
|---|---|---|
| `.astro` files in `web/src/` | (existing 11) | +6 (DocsLayout + 3 components + 3 pages + 1 stub) — net 17 |
| Vitest tests | 29/29 | 29/29 (no new vitest in Phase 5; layout components covered by e2e) |
| Playwright e2e tests | 4/4 | **6/6** (+ docs-reader + link-resolution) |
| Pagefind indexed pages | 3 | (stays 3 for landing; docs pages indexed when crawled — not exercised in build smoke) |
| TS clean | yes | yes |
| Build green | yes | yes |
| HIGH integration risks open | 4 (per Phase 4 reviewer) | 0 (3 fixed in Phase 5 + H2 from Phase 4 fixed pre-Phase-5 by Phase 8.x) |

## Reviewer behavior assessment

The `feature-dev:code-reviewer` slot was the right Rule D pick: cross-family from `pr-review-toolkit` (used 4 times), produced 3 HIGH findings none of which the per-task reviewer or the build smoke could have caught (filter mismatch + silent lang bypass + schema/runtime contract drift). All 3 HIGH directly affect end-user experience or carry latent build risk. Family pool now: pr-review-toolkit 4×, feature-dev 1× (this), Phase 6 reviewer should pick fresh — candidates `oh-my-claudecode:code-reviewer`, `oh-my-claudecode:critic`, `oh-my-claudecode:verifier`.
