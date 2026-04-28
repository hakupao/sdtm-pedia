# Task 8.5 — Reviewer Fix Bundle (F-1 HIGH + F-2/3/4/5 MEDIUM)

> **Status**: PASS — Phase 8 reviewer verdict CONDITIONAL_PASS → effective PASS
> **Date**: 2026-04-29
> **Mode**: direct main session, post-reviewer fix bundle (mirrors Phase 7.5 pattern)
> **Commit**: `b00b63c` (4 files changed, +25 / -11)
> **Trigger**: Phase 8.3 reviewer (`pr-review-toolkit:silent-failure-hunter`) returned CONDITIONAL_PASS H=1 M=4 L=5 with documented small fix path

## Findings addressed

| Finding | Severity | Class | Fix locus | LOC |
|---|---|---|---|---|
| **F-1** | HIGH | silent i18n regression | SearchOverlay.tsx + TopNav.astro | +6 / -2 |
| **F-2** | MEDIUM | unlocalized ⌘K button text | TopNav.astro | +1 / -1 |
| **F-3** | MEDIUM | aria-label hardcoded English | SearchOverlay.tsx | folded into F-1 |
| **F-4** | MEDIUM | `.catch(() => {})` silent error swallow | SearchOverlay.tsx | +5 / -3 |
| **F-5** | MEDIUM | e2e test name lies about trigger | search.spec.ts | +8 / -1 |

LOW findings F-6..10 deferred per reviewer §"Recommendations for Phase 8 → Phase 9 handoff" (carryover IDs C-P8-*).

## Files changed

```
web/src/components/astro/TopNav.astro           |  4 ++--
web/src/components/react/SearchOverlay.test.tsx |  4 ++--
web/src/components/react/SearchOverlay.tsx      | 19 +++++++++++++------
web/tests/e2e/search.spec.ts                    |  9 ++++++++-
4 files changed, 25 insertions(+), 11 deletions(-)
```

## Detail

### F-1 [HIGH] — SearchOverlay i18n wiring

**Root cause**: keys `search.placeholder` (zh: `搜索文档...` / ja: `ドキュメント検索...` / en: `Search docs...`) and `search.shortcut` (`Cmd K` all 3 langs) existed pre-Phase 8 in `web/src/i18n/ui.{zh,en,ja}.json:18-19`. Phase 8 introduced the SearchOverlay but didn't consume them. JP/ZH-native users would see English chrome behind a localized page = silent regression.

**Fix** (SearchOverlay.tsx):

```diff
-import { useEffect, useRef, useState } from 'react';
+import { useEffect, useRef, useState } from 'react';
+import { getUIStrings, type Lang } from '../../i18n/helpers';

-export function SearchOverlay() {
+export function SearchOverlay({ lang = 'en' }: { lang?: Lang } = {}) {
+  const t = getUIStrings(lang);
   const [open, setOpen] = useState(false);
   ...
```

```diff
-          placeholder="Search docs..."
-          aria-label="Search docs"
+          placeholder={t['search.placeholder']}
+          aria-label={t['search.placeholder']}
```

`lang` defaults to `'en'` so existing standalone test mounts (`render(<SearchOverlay />)`) and any unforeseen mounting context still type-check + run safely.

**Fix** (TopNav.astro):

```diff
-<SearchOverlay client:load />
+<SearchOverlay client:load lang={lang} />
```

`TopNav.astro` already had `lang: Lang` in props + `t = getUIStrings(lang)` in scope; the prop just needed forwarding.

**Verification**:
- `dist/ja/guide/user-guide/index.html` shows `<astro-island ... component-export="SearchOverlay" ... props="{&quot;lang&quot;:[0,&quot;ja&quot;]}" ...>` — lang prop wired through
- SearchOverlay returns `null` from SSR when closed, so the `placeholder` text is set client-side post-hydration. Vitest `<SearchOverlay lang="en" />` confirms hook chain works under jsdom.

### F-2 [MEDIUM] — ⌘K hint button literal → i18n

**Fix** (TopNav.astro):

```diff
-        ⌘K
+        {t['search.shortcut']}
```

All 3 langs currently resolve to `Cmd K` (the i18n key gives a future hook for locale-specific notation if needed without re-deploying code). Verified in dist:

```html
<button ... aria-label="Open search"> Cmd K </button>
```

(rendered identically across en/zh/ja routes since the JSON values match).

### F-3 [MEDIUM] — aria-label hardcoded English

**Fix**: folded into F-1 — `aria-label={t['search.placeholder']}`. Reused `search.placeholder` (which reads as a noun-phrase in all 3 langs and works as both label + placeholder text) instead of adding a new i18n key (scope minimization).

### F-4 [MEDIUM] — `.catch(() => {})` swallows all errors

**Root cause**: a single empty catch buried at least 5 distinct failure modes (404 dev/test = expected; CORS, MIME mismatch, WASM init failure, network drop, malformed entry.json = unexpected). In production a runtime failure here is genuinely surprising (CF Pages serves `dist/` as publish root with the Pagefind index alongside) so silent failure ⇒ "search broken, no signal".

**Fix** (SearchOverlay.tsx):

```diff
-        .catch(() => {
-          // Pagefind index missing (e.g. dev server, jsdom test, or build skipped).
-          // Search will simply return no results — no need to surface a runtime error.
-        });
+        .catch((err) => {
+          // Pagefind index missing (e.g. dev server, jsdom test, build skipped).
+          // Search returns no results in that case. In production a runtime
+          // failure here is genuinely unexpected (CF Pages serves dist/ root)
+          // so we surface it via console.warn for telemetry / DevTools triage.
+          if (import.meta.env.PROD) {
+            console.warn('[SearchOverlay] Pagefind init failed:', err);
+          }
+        });
```

`import.meta.env.PROD` evaluates to `false` under vitest jsdom + dev server, `true` only under Astro production build. Test logs stay clean; production gets a DevTools warning if the init breaks.

### F-5 [MEDIUM] — e2e test name honesty

**Root cause**: the test was named `'search opens with Cmd+K and finds AESER'` but actually clicked the ⌘K hint button (whose inline onclick dispatches a synthetic `keydown`). Adj-2 in Task 8.2 documented why (headless chromium doesn't deliver Meta+k to the document listener without focus) but the test name still claimed Cmd+K. If the inline `onclick` is ever changed to a direct function call, the test passes while real Cmd+K silently breaks.

**Fix** (search.spec.ts):

```diff
+// Test name reflects the actual trigger (button click → synthetic keydown), not
+// raw `page.keyboard.press('Meta+k')`. The raw keypress isn't reliably delivered
+// to the React document listener in headless chromium without a focused target;
+// the button's inline onclick exercises the same setOpen(true) code path.
+// Vitest covers the raw-keydown listener wiring separately (SearchOverlay.test.tsx).
+// Tracked: C-P8-2 — promote to real-keypress test once playwright webServer is
+// switched to build+preview (C-P8-1) so we can investigate focus delivery.
-test('search opens with Cmd+K and finds AESER', async ({ page }) => {
+test('search opens via ⌘K hint button click (synthetic keydown) and finds AESER', async ({ page }) => {
```

Body unchanged. Trade-off: test name is uglier but no longer lies. The "C-P8-2 promote" comment clarifies why the workaround exists + what unblocks the real-keypress test.

## Test fixture sync

`SearchOverlay.test.tsx`: both `render(<SearchOverlay />)` calls became `render(<SearchOverlay lang="en" />)`. tsc would have caught this (the prop is required if you don't use the default), but explicit pass is more readable in tests.

## Verification gates

| Gate | Command | Expected | Actual |
|---|---|---|---|
| **tsc** | `npx tsc --noEmit` | 0 errors | **0 errors** |
| **vitest** | `npm test -- --run` | 34/34 (no count change) | **34/34 PASS** (9 files, 1.13s) |
| **build** | `npm run build` | 31 pages + Pagefind | **31 pages built**; Pagefind 27 pages / 3 langs / 6454 words / 17 artifacts |
| **dist HTML** | `grep` ja route | lang prop on astro-island; "Cmd K" in button | **VERIFIED** — `props="{&quot;lang&quot;:[0,&quot;ja&quot;]}"` + `> Cmd K <` rendered |
| **e2e (search only)** | `npx playwright test tests/e2e/search.spec.ts` | 1 PASS against preview | **1 PASS in 368ms** |
| **e2e (full suite)** | `npx playwright test` | 7/7 (search + smoke + lang + link-resolution) | **7/7 PASS in 4.3s** |

Pre-existing warnings unchanged (4 redirect-page `<html>`-missing notes = C-P7-6 expected; ja/zh stemming notes = informational).

## Verdict upgrade

Phase 8.3 reviewer initial verdict **CONDITIONAL_PASS H=1 M=4 L=5** → post-8.5 **PASS** (HIGH + 4 MEDIUM resolved per reviewer's recommended fix path; LOW deferred).

## Carryover for Phase 9 (preliminary IDs, finalized in handoff)

| ID | Source | Description | Status |
|---|---|---|---|
| C-P8-1 | reviewer F-7 (LOW) + Task 8.2 B-1 | playwright `webServer.command` uses `npm run dev`; switch to `npm run build && npm run preview` for CI-green search.spec.ts | DEFER to Phase 9 polish |
| C-P8-2 | F-5 fix comment | Promote search.spec.ts to real `page.keyboard.press('Control+k')` once C-P8-1 lands (investigate focus delivery in headless chromium) | DEFER to Phase 9 |
| C-P8-3 | F-6 LOW | No focus-return on overlay close | DEFER (a11y polish) |
| C-P8-4 | F-8 LOW | No ARIA live region for results announcement | DEFER (a11y polish) |
| C-P8-5 | F-9 LOW | No retry / bounded backoff if Pagefind init fails partway | DEFER (rare prod case) |
| C-P8-6 | F-10 LOW | ⌘K hint button visible only on `md:` breakpoint | DEFER (mobile UX) |

Detailed reviewer write-up at `.work/07_website/phase8/evidence/checkpoints/phase_8_reviewer_report.md`.

## Cumulative metrics post Phase 8.5

| Metric | Phase 7 close | Task 8.2 | Task 8.5 | Delta vs Phase 7 |
|---|---|---|---|---|
| tsc errors | 0 | 0 | 0 | 0 |
| vitest | 32/32 | 34/34 | 34/34 | +2 |
| e2e (against preview) | 6/6 | 7/7 | 7/7 | +1 (search.spec.ts) |
| build pages | 31 | 31 | 31 | 0 |
| dist/pagefind/ artifacts | 0 (Phase 7 didn't index) | 17 | 17 | +17 (search shipped) |
| HEAD | `fbc2ccd` | `4206203` | `b00b63c` | +2 commits |

## Pattern observation (Rule C carry-forward to Phase 8 → 9 handoff)

Phase 8 ships the same failure pattern Phase 7 lessons predicted: when a phase introduces a new feature surface that touches existing infrastructure (search overlay touching pre-existing i18n key infrastructure), it can silently fail to consume that infrastructure. Phase 7 caught 3 instances on `compare.subhead.ja` etc; Phase 8 caught 1 fresh instance on `search.placeholder`. Two cumulative instances of "feature shipped without consuming pre-existing locale keys" — the helpers.test.ts key parity test catches *missing* keys but not *unconsumed* keys. Process improvement candidate for Phase 9 carryover: add a static-analysis pass (lint rule or post-build grep) for "i18n key defined but never imported by a component", or per-locale visual regression test that fails when an /ja route shows English chrome.
