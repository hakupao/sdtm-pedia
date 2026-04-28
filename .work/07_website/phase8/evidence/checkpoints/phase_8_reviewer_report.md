# Phase 8 — End-of-Phase Reviewer Report

> **Reviewer**: `pr-review-toolkit:silent-failure-hunter` (substituted at session-time from handoff's `superpowers:silent-failure-hunter` — that agent does not exist as a registered subagent in this environment; pr-family 5th-burn but FIRST burn of `silent-failure-hunter` agent within pr-family — prior 4 pr-family burns were all `code-reviewer`. Cross-family from Phase 7's `superpowers:code-reviewer`.)
> **Date**: 2026-04-29
> **Scope**: Phase 8 = Pagefind search introduction, 1 commit `4206203` (4 files, +160 LOC)
> **Mode**: read-only adversarial silent-failure-focused review
> **Branch**: `main` (HEAD = `4206203`, +1 commit ahead of `origin/main`)

---

## Verdict

**CONDITIONAL_PASS** → upgrades to **PASS** if F-1 (HIGH) is addressed in a small Phase 8.5 fix bundle (~6 LOC across 2 files: pass `lang` prop into `<SearchOverlay />`, replace 2 hardcoded English strings with i18n lookups). The fix path is mechanical and absorbs F-2 + F-3 in the same edit.

If Daisy elects to defer F-1 to Phase 9, **PASS-with-carryover** is acceptable for soft launch — the search overlay is functional in all 3 langs (Pagefind correctly auto-detects `<html lang>` and returns lang-scoped results), only the chrome (placeholder + aria-label) is English. JP/ZH-native users will see Chinese/Japanese results behind an English placeholder, which is the exact "looks fine until production" failure class silent-failure-hunter exists to catch — and the i18n keys are *already defined* (`search.placeholder` and `search.shortcut` in `ui.{zh,en,ja}.json`), so the omission is unambiguously a regression rather than a deferred translation task.

| Severity | Count | Items |
|---|---|---|
| **HIGH** | 1 | F-1 SearchOverlay hardcodes English chrome despite i18n keys already defined in all 3 langs |
| **MEDIUM** | 4 | F-2 ⌘K hint button text not localized (uses literal `⌘K` instead of `t['search.shortcut']`); F-3 SearchOverlay aria-label hardcoded English; F-4 `.catch(() => {})` swallows ALL dynamic-import failures including legitimate runtime errors; F-5 e2e Adj-2 button-click bypass hides keyboard-shortcut breakage class |
| **LOW** | 5 | F-6 No focus-return on close; F-7 No keyboard equivalent for backdrop-click close (covered by Esc, fine); F-8 No ARIA live region for results announcement; F-9 No retry / bounded backoff if Pagefind init fails partway; F-10 ⌘K hint button visible only on `md:` breakpoint |

---

## What Phase 8 did well (acknowledge first)

- **Plan adherence is strong**: 3 of 3 spec adjustments (Adj-1/2/3 in `task_8_2_report.md`) are individually defensible — Adj-1 (vite-ignore indirection) IS necessary, verified by inspecting the built bundle which emits `import("/pagefind/pagefind.js")` as a runtime call (vite would have rejected the literal-form static analysis on at least vitest startup); Adj-3 (aria-label addition) is good defensive a11y.
- **The `stripHtml` excerpt approach is correct**: never passes Pagefind's `<mark>...</mark>` excerpts through any HTML-injection prop. React renders `{stripHtml(r.excerpt)}` as text content. Zero XSS surface from search results — the strict approach.
- **Pagefind is correctly indexed**: 17 artifacts under `dist/pagefind/`, 3 langs (zh/en/ja) auto-detected from `<html lang>`, 27 pages / 6454 words. Verified `pagefind-entry.json` lists all 3 langs with `page_count: 9` each.
- **The dynamic import path resolves under preview**: `curl -sI http://localhost:4321/pagefind/pagefind.js` → `HTTP/1.1 200 OK / Content-Type: text/javascript` (verified during this review). CF Pages serves `dist/` as publish root — same path will resolve in production.
- **Test layering is sound**: vitest covers the document-listener wiring + Escape close (no Pagefind dep, runs in jsdom), playwright e2e covers the hydrated island + real Pagefind index. The two layers don't overlap, which is the right design.
- **SSR shape correct**: built HTML shows `<astro-island ... component-export="SearchOverlay" client="load">` with no inner SSR markup (correct, since `if (!open) return null`). No `await-children` flash; no FOUC.
- **Tsc + vitest verified independently**: `npx tsc --noEmit` exits 0, `npm test -- --run` reports `Test Files 9 passed (9) / Tests 34 passed (34)` (verified during this review).

---

## Findings

### F-1 [HIGH] SearchOverlay hardcodes English chrome (`placeholder` + `aria-label`) despite i18n keys defined in all 3 langs

**Class**: silent i18n regression — feature works but the wrong language; the regression is invisible because there are no negative tests for "this string is not English on /ja".
**File**: `web/src/components/react/SearchOverlay.tsx:78-79`
**Phase 8 attribution**: introduced by commit `4206203`.

**Concrete evidence**:

`web/src/components/react/SearchOverlay.tsx:74-82`:
```tsx
<input
  ref={inputRef}
  type="search"
  role="searchbox"
  placeholder="Search docs..."
  aria-label="Search docs"
  onChange={onChange}
  className="w-full px-4 py-3 font-mono text-sm border-b border-rule bg-bg"
/>
```

But `web/src/i18n/ui.zh.json:18-19`:
```json
"search.placeholder": "搜索文档...",
"search.shortcut": "Cmd K",
```

`web/src/i18n/ui.ja.json:18-19`:
```json
"search.placeholder": "ドキュメント検索...",
"search.shortcut": "Cmd K",
```

`web/src/i18n/ui.en.json:18-19`:
```json
"search.placeholder": "Search docs...",
"search.shortcut": "Cmd K",
```

The `search.placeholder` and `search.shortcut` keys *already exist* in all three locale files — pre-Phase-8, the previous owner anticipated this overlay would consume them. Phase 8 omits the wiring.

`web/src/components/astro/TopNav.astro:8`:
```astro
const t = getUIStrings(lang);
```

The TopNav has `t` in scope. It does not pass it to the overlay.

`web/src/components/astro/TopNav.astro:34`:
```astro
<SearchOverlay client:load />
```

No props; no `lang`; no localized strings.

**Why it's HIGH not MEDIUM**:
1. The keys are *already defined* in zh/ja with correct translations. This is not a "need to translate" task — it's "wire up the strings that exist." The work was already done by a previous translation pass; Phase 8 ignored it.
2. JP-native and ZH-native users land on `/ja/guide/user-guide/` and `/zh/guide/user-guide/`, the entire page chrome around them is in their language, they hit ⌘K, and a search box opens with **English** placeholder + aria-label. This is an across-language seam, audible to JP screen-reader users immediately ("Search docs" read in `en-US` voice, breaking the JP language context).
3. The ⌘K hint button shows literal `⌘K` (line 27 of TopNav.astro, see F-2). A JP user has no signal that "Cmd K" is the i18n term for that shortcut in their locale.
4. There is no test that catches this — `helpers.test.ts` enforces *key parity* across locale files but not *consumption*. The test infrastructure is silent.
5. Phase 7 reviewer specifically called this exact failure class out (F-2/F-3/F-4 on `compare.subhead.ja`, etc.) and Phase 7.5 fix bundle resolved them. Phase 8 ships a fresh instance of the same failure class.

**Hidden errors this masks**: Any future locale addition (e.g., `ko`, `de`) will need to add the `search.*` keys, but the overlay won't consume them. The key-parity test will pass. The overlay will show "Search docs..." on the new locale. The bug recurs every time we add a language.

**Fix** (~6 LOC across 2 files):

`TopNav.astro` line 34:
```astro
<SearchOverlay client:load lang={lang} />
```

`SearchOverlay.tsx`:
```tsx
import { getUIStrings, type Lang } from '../../i18n/helpers';

export function SearchOverlay({ lang }: { lang: Lang }) {
  const t = getUIStrings(lang);
  // ... existing logic ...
  <input
    placeholder={t['search.placeholder']}
    aria-label={t['search.placeholder']}  // or a separate t['search.aria'] key
    ...
  />
}
```

If a `<button aria-label="Search docs"...>` test exists in `SearchOverlay.test.tsx`, also pass a stub `lang="en"` in render: `render(<SearchOverlay lang="en" />)`.

---

### F-2 [MEDIUM] ⌘K hint button shows literal `⌘K` instead of `t['search.shortcut']`

**Class**: i18n consistency / sibling to F-1
**File**: `web/src/components/astro/TopNav.astro:27`
**Phase 8 attribution**: introduced by commit `4206203`.

**Concrete evidence**:
```astro
<button
  type="button"
  class="font-mono text-[10px] tracking-wider text-ink-mute hover:text-accent"
  onclick="document.dispatchEvent(new KeyboardEvent('keydown', {key:'k', metaKey:true}))"
  aria-label="Open search"
>
  ⌘K
</button>
```

The button text and the `aria-label` are both English-hardcoded. `t['search.shortcut']` is defined as `"Cmd K"` in all 3 langs (currently same string but explicit i18n decoupling is the point — JP could become `"⌘ K"` or `"検索: Cmd+K"` later without code changes). The `aria-label="Open search"` has no `search.aria.open` key in `ui.{zh,en,ja}.json` — that's a missing key (would need to add 3 keys × 3 langs).

**Why MEDIUM not HIGH**: the button text is a Unicode keyboard glyph (`⌘`) which is locale-agnostic. The `aria-label="Open search"` is the screen-reader-impacting half — that's MEDIUM-level but absorbed in F-1 fix scope.

**Fix** (folds into F-1 fix bundle): use `{t['search.shortcut']}` for button text, add `search.aria.open` key × 3 langs, use `t['search.aria.open']` for aria-label. Total ~5 LOC.

---

### F-3 [MEDIUM] SearchOverlay `aria-label="Search docs"` hardcoded — sibling to F-1

**Class**: a11y / i18n parity
**File**: `web/src/components/react/SearchOverlay.tsx:79`
**Phase 8 attribution**: introduced by commit `4206203` (Adj-3 explicitly added this for "parity with CompareFilter" — but didn't notice CompareFilter takes `lang` prop and uses i18n).

**Concrete evidence**:
```tsx
aria-label="Search docs"
```

vs `web/src/components/react/CompareFilter.tsx:30` (the parity reference):
```tsx
aria-label={t['compare.filter.label']}
```

CompareFilter:
- accepts `lang: Lang` as a prop
- calls `const t = getUIStrings(lang);`
- uses `t['compare.filter.label']` for aria-label

SearchOverlay does none of this. Adj-3 in `task_8_2_report.md` says "kept consistent" with CompareFilter — but only at the structural level (added an aria-label attribute), not at the i18n level (route the value through `t[]`). This is a partial-parity that *looks* done but isn't.

**Why MEDIUM not HIGH**: subsumed into the F-1 fix scope. Mechanical alongside F-1.

**Fix** (folds into F-1 fix bundle): see F-1.

---

### F-4 [MEDIUM] `.catch(() => {})` silently swallows ALL dynamic-import failures including legitimate runtime errors

**Class**: silent failure / classic anti-pattern
**File**: `web/src/components/react/SearchOverlay.tsx:42-49`
**Phase 8 attribution**: introduced by commit `4206203`. The `task_8_2_report.md` Adj-1 documents "Eliminates 2 noisy unhandled-rejections from vitest output without affecting production behavior — search just returns 0 results when the index is unreachable."

**Concrete evidence**:
```tsx
import(/* @vite-ignore */ pagefindUrl)
  .then((m) => {
    pagefindRef.current = m;
  })
  .catch(() => {
    // Pagefind index missing (e.g. dev server, jsdom test, or build skipped).
    // Search will simply return no results — no need to surface a runtime error.
  });
```

**The empty catch lumps together at least 5 distinct failure modes**:
1. **404** — `/pagefind/pagefind.js` not built (dev server, jsdom). EXPECTED.
2. **CORS error** — if the site is reverse-proxied through a CDN that strips `/pagefind/*` for some reason. UNEXPECTED.
3. **MIME type mismatch** — if a future CF Pages config or worker rewrites `.js` to `text/html`. UNEXPECTED.
4. **WASM init failure** — `pagefind.js` loads but `init_pagefind()` chokes on a corrupted `wasm.{lang}.pagefind`. UNEXPECTED.
5. **Network timeout / connection drop** mid-fetch. UNEXPECTED.
6. **Pagefind module loads but `entry_response.json` returns malformed JSON** (cache poisoning / partial deploy). UNEXPECTED.

For modes 2-6, the user types a query, sees zero results, and concludes "search is broken" or "no docs match." There is no log, no telemetry, no retry, no banner. The user cannot distinguish "no results for AESER" from "Pagefind didn't load." The dev / on-call cannot debug from logs because there are no logs.

**Why MEDIUM not HIGH**: the most likely failure mode (404 in dev) is correctly silent. Production failure modes 2-6 are individually low-probability for a static site on CF Pages. But the *class* of "no signal when search infrastructure breaks" is exactly the silent-failure class the brief asked for.

**Recommendation**:
```tsx
import(/* @vite-ignore */ pagefindUrl)
  .then((m) => {
    pagefindRef.current = m;
  })
  .catch((err) => {
    // 404 in dev / test is expected; everything else should surface.
    if (import.meta.env.PROD) {
      // eslint-disable-next-line no-console
      console.warn('[SearchOverlay] Pagefind unavailable:', err);
    }
  });
```

Or, more disciplined: track an `error` state and render a single-line banner inside the overlay ("Search index unavailable — refresh or visit /sitemap.xml"). This is more work than the F-1 fix but materially better for a search feature that ships to public users.

**Defer-acceptable** if the team commits to monitoring via a different channel (e.g., synthetic check on `/pagefind/pagefind-entry.json` content-type after each deploy). Track as **C-P8-1** if deferred.

---

### F-5 [MEDIUM] e2e bypasses keyboard-shortcut delivery via button-click — hides a real failure class

**Class**: test coverage gap masquerading as test pass
**File**: `web/tests/e2e/search.spec.ts:22`
**Phase 8 attribution**: introduced by commit `4206203` (Adj-2 documents this explicitly).

**Concrete evidence** (`search.spec.ts:13-27`):
```ts
test('search opens with Cmd+K and finds AESER', async ({ page }) => {
  await page.goto('/zh/guide/user-guide/');
  await expect(page.getByLabel('Open search')).toBeVisible();
  // Click the ⌘K hint button — its onclick dispatches a synthetic
  // KeyboardEvent on document, exercising the same code path as Cmd+K.
  await page.getByLabel('Open search').click();
  ...
});
```

The test name SAYS "search opens with Cmd+K" but the test actually clicks a button that synthesizes a keyboard event. These are NOT equivalent code paths in production:

- **Production user**: presses physical Cmd+K. Browser dispatches keydown to document. React listener fires. Overlay opens.
- **Test**: clicks the hint button. Inline `onclick` constructs `new KeyboardEvent('keydown', {key:'k', metaKey:true})` and dispatches it. React listener fires. Overlay opens.

The test exercises the React listener wiring + overlay render. It does NOT exercise:
- whether headless chromium delivers Cmd+K to the document at all (Adj-2 explicitly notes: "neither `Meta+k` nor `Control+k` causes the React `keydown` listener to fire when no element is focused")
- whether the page steals focus / blocks key delivery
- whether browser chrome consumes the shortcut (reported as the actual issue in Adj-2)

**Adversarial reading**: if the hint button's inline `onclick` ever changes (e.g., team decides "let's just call a function instead of dispatching a synthetic event"), the test will still pass against the new direct-call path — but the *user's actual Cmd+K* might silently break. The test's name lies about what it covers.

**Adj-2 rationale** ("`Meta+k` not delivered to the document in headless chromium when no element is focused") is plausible but the right fix is `await page.locator('body').focus()` then `page.keyboard.press('Meta+k')`, not redirect-to-button-click. The button-click path *also* exists as a separate user code path (mobile users tap the button) so it deserves its own test — but the keyboard shortcut deserves a real test.

**Why MEDIUM not HIGH**: vitest layer covers the React listener directly via `fireEvent.keyDown(document, ...)`. So the listener wiring IS tested at unit level. The e2e gap is "browser-level keyboard event delivery to a React document listener" — a real failure class but covered indirectly. Acceptable as long as the test name is honest.

**Fix options**:
- **(A)** Rename test: `'search opens via ⌘K hint button'` so the name doesn't lie.
- **(B)** Add a second test that does `await page.locator('body').focus(); await page.keyboard.press('Control+k');` and accept it might be flaky on some browsers (allowed via `test.fail()` annotation).
- **(C)** Carry as **C-P8-2** for Phase 9 hardening.

---

### F-6 [LOW] No focus-return on Esc-close

**Class**: a11y / focus management
**File**: `web/src/components/react/SearchOverlay.tsx:26-27, 64`

When Escape closes the overlay, focus disappears (was on the input, input is now unmounted). A keyboard-only user has to Tab from `<body>` start to find their previous position. Best-practice modal pattern: capture `document.activeElement` on open, restore on close.

**Why LOW**: standard Tab behavior recovers; not a blocker for users; relevant only to keyboard-power-users. Pre-public release polish.

**Fix**: ~6 LOC — capture activeElement in the open useEffect, restore in the close path.

---

### F-7 [LOW] Backdrop click closes — keyboard equivalent IS Esc (covered)

**Class**: a11y verification (this is NOT a finding, included for completeness per brief D4)
**Verification**: Esc closes (line 26-27). Backdrop-click (line 68 `onClick={() => setOpen(false)}`) is mouse-only by definition — no keyboard equivalent needed because Esc serves that purpose. ✓ Not a finding.

---

### F-8 [LOW] No ARIA live region for results — screen reader hears nothing when results populate

**Class**: a11y / screen-reader announcement
**File**: `web/src/components/react/SearchOverlay.tsx:83-96`

```tsx
<ul className="max-h-96 overflow-y-auto">
  {results.map((r, i) => (
    <li key={i} ...
```

The `<ul>` has no `aria-live`, `role="status"`, `role="region"`, or `aria-label`. When a screen-reader user types into the input and 5 results populate, NVDA/VoiceOver/JAWS hear nothing. They have to manually navigate (Tab or arrow) to discover results exist.

**Best practice**: `<div aria-live="polite" aria-atomic="false">` wrapping the `<ul>`, or add `<span class="sr-only" aria-live="polite">{results.length > 0 ? `${results.length} result${results.length === 1 ? '' : 's'}` : ''}</span>`.

**Why LOW for Phase 8**: small affected user fraction; deferred is acceptable; sequence after F-1 a11y wave.

**Fix**: ~3 LOC.

---

### F-9 [LOW] No retry / bounded backoff if Pagefind initial load fails partway

**Class**: resilience / degraded-mode UX
**File**: `web/src/components/react/SearchOverlay.tsx:32-51`

If the dynamic import succeeds but the WASM fetch times out (Pagefind init is multi-step: load entry.json → load wasm → load index chunks per query), `pagefindRef.current` is set but subsequent `.search(q)` calls may throw asynchronously. The `onChange` handler does `await pagefindRef.current.search(q)` without try/catch — an unhandled promise rejection bubbles to React's error boundary (none defined) → React logs to console + the input becomes unresponsive.

**Why LOW**: low-probability path on a production CDN. Still worth a try/catch around the search call.

**Fix**: ~4 LOC — wrap the `await pagefindRef.current.search(q)` in try/catch, set an error state, optionally re-init on next open.

---

### F-10 [LOW] ⌘K hint button hidden on mobile (`md:hidden` class on parent nav)

**Class**: discoverability / mobile UX
**File**: `web/src/components/astro/TopNav.astro:15`

```astro
<nav id="mobile-nav-content" class="hidden md:flex items-center gap-4 ...">
```

The nav containing the ⌘K button is `hidden md:flex` — so on `<md` viewports (default Tailwind breakpoint = 768px), the only entry to search is via the mobile menu (☰ button, line 14). After tapping ☰, the user sees `⌘K` button — but a mobile user typically doesn't have a ⌘ key. Tapping the button DOES dispatch the synthetic KeyboardEvent and DOES open the overlay (the test verifies this) — so it works, but the affordance is misleading on touch.

**Why LOW**: search IS reachable on mobile (via tap). The button label mismatches the input modality but doesn't break functionality. Phase 9 polish bundle candidate: split the button — desktop shows `⌘K`, mobile shows magnifying-glass icon or `Search`.

**Fix**: ~10 LOC for responsive variant. Defer-acceptable.

---

## D-by-D summary (per brief stress dimensions)

### D1 — Silent index failures
- **Build green + index actually built**: ✓ verified — `pagefind-entry.json` shows 3 langs × 9 pages each = 27 indexed pages.
- **Pagefind warnings**: 4 redirect-page "no `<html>` element" warnings present — pre-existing C-P7-6, correctly classified, redirect canonicals already trailing-slash-fixed in Phase 7.5 (verified `dist/zh/guide/index.html` has `<link rel="canonical" href="https://sdtm-pedia.pages.dev/zh/guide/user-guide/">` with trailing slash).
- **Language detection**: ✓ Pagefind reads `<html lang="zh|en|ja">` per page; verified all 3 produce correct langs in `pagefind-entry.json`.
- **Root selector**: Pagefind defaults to `<body>`. The TopNav header and `<SearchOverlay client:load />` mount-point sit *inside* `<body>` — so Pagefind WILL index nav text (e.g., "ドキュメント", "4 平台", "Demo") into the search corpus. This is acceptable but worth noting: searches for "Guide" might surface every page since "Guide" appears in nav. NOT a finding because (a) Pagefind ranks by frequency-relative-to-page-length so nav text gets low weight and (b) the team has not reported false positives. **Possible C-P8-3 if signal-to-noise becomes a complaint** (defer).
- **Index scope**: ✓ build runs `pagefind --site dist`, indexes only `dist/`. No leakage from `src/`, `node_modules/`, or other sibling dirs.
- **Index NOT empty**: 6454 words indexed / 27 pages = ~239 words/page. Plausible for a docs site.

### D2 — Broken result URLs
- **`r.url` resolves to live page**: I cannot run live search end-to-end without the executor's preview lane, but: Pagefind result URLs come from the `<html>` page paths it indexes. The 27 indexed pages all live at `dist/<lang>/<path>/index.html`. Pagefind emits URLs like `/zh/guide/user-guide/` (with trailing slash, matching `build.format: 'directory'`). The SearchOverlay renders `<a href={r.url}>` directly. ✓ should resolve.
- **Cross-lang results**: Pagefind auto-detects from `<html lang>` and **only returns same-language results** (since each lang has its own index hash). So a search on `/zh/...` will NOT surface `/en/...` results. ✓ Verified by `pagefind-entry.json` showing 3 separate language indexes.
- **Hash anchors / encoded chars**: Pagefind preserves anchors via `calculate_sub_results` (visible in pagefind.js source). Excerpt anchors are URL-encoded by Pagefind itself. Not a Phase 8 finding.

### D3 — Dynamic import path correctness
- **Vite static analysis**: ✓ Adj-1's variable indirection works — built bundle (`dist/_astro/SearchOverlay.BzFhClcG.js`) emits `import("/pagefind/pagefind.js")` literally, runtime resolves it.
- **Dev / preview / prod path consistency**: ✓ verified `curl -sI http://localhost:4321/pagefind/pagefind.js` → `200 OK / Content-Type: text/javascript` against `npm run preview`. Production CF Pages serves identical paths from `dist/` publish root. Confidence high — would still "verify in production after first deploy" to be safe (C-P8-4 candidate for the deploy-day checklist).
- **`.catch(() => {})` swallowing**: F-4 above.
- **API surface**: ✓ `pagefind.js` top-level `export{search, ...}`. SearchOverlay calls `pagefindRef.current.search(q)` — works because `m.search` is the exported top-level function.
- **`r.data()`**: ✓ verified in `pagefind.js` — search results have `data: async () => await this.loadFragment(...)` per result. The SearchOverlay's `r.data()` call is the documented Pagefind API.

### D4 — A11y of search overlay
- **`role="searchbox"` on `type="search"`**: redundant but harmless. Per ARIA spec, `<input type="search">` already has implicit `role="searchbox"`. The explicit role doesn't hurt and supports older AT.
- **Focus on input on open**: ✓ `inputRef.current?.focus()` in line 34.
- **Focus return on close**: ✗ F-6 above.
- **Tab trap**: ✗ no focus trap inside overlay. Tab from input cycles through page nav (focus escapes overlay). Standard modal a11y prescribes a focus trap. **Possible C-P8-5** (defer or fix).
- **Backdrop click + Esc**: ✓ Esc closes; backdrop click closes; mouse + keyboard both covered.
- **`<ul>` + `<li>` + `<a>` semantics**: ✓ correct list pattern.
- **Live region**: ✗ F-8 above.
- **⌘K hint aria-label**: F-2/F-3 above (i18n).
- **Placeholder English-only "deferred"**: claimed in PLAN.md but the keys ARE defined — F-1 contradicts the deferral rationale.

### D5 — Plan adherence
- **Adj-1 (vite-ignore indirection)**: ✓ necessary, verified by inspecting built bundle.
- **Adj-2 (e2e button click)**: ⚠ F-5 — works but bypasses real keyboard delivery test.
- **Adj-3 (aria-label addition)**: ⚠ F-3 — added the attribute but hardcoded the string, defeating the parity rationale.

### D6 — Free-form
- F-9 (try/catch around search call)
- F-10 (mobile UX)
- The `pagefindRef` is `useRef<any>` — typed as `any`. A typed `interface PagefindModule { search(q: string): Promise<{results: PagefindResult[]}>; }` would catch API drift across Pagefind versions. LOW; not raised as a finding because TypeScript strictness here is a polish concern.

---

## Recommendations for Phase 8 → Phase 9 handoff

### Recommended 8.5 fix bundle (F-1 + F-2 + F-3 in one edit, ~10 LOC across 4 files)

1. **F-1 / F-2 / F-3 fix**: pass `lang` prop into `<SearchOverlay />`, replace 3 hardcoded English strings with `t['search.placeholder']` / `t['search.shortcut']`. Adds 1 missing key `search.aria.open` × 3 langs (or reuse existing keys). Update `SearchOverlay.test.tsx` to pass `lang="en"` in render.

If 8.5 is not run, these land as Phase 9 carryover:

### Carryover IDs for Phase 9 (continuing C-P8-* namespace)

- **C-P8-1 [HIGH if F-1 deferred / N/A if 8.5 fixes]** — SearchOverlay i18n wiring (F-1 + F-2 + F-3). Mechanical, ~10 LOC.
- **C-P8-2 [MEDIUM]** — `.catch(() => {})` should distinguish dev-404 from production-runtime-error (F-4). Add `import.meta.env.PROD` guard + `console.warn`, OR add an error-state banner to the overlay.
- **C-P8-3 [LOW]** — playwright `webServer.command` switch to `npm run build && npm run preview` so `search.spec.ts` runs green out-of-the-box (B-1 in `task_8_2_report.md`). Affects CI integration.
- **C-P8-4 [MEDIUM]** — e2e renaming or real keyboard test (F-5). Test name should not lie.
- **C-P8-5 [LOW]** — Focus management on overlay close (F-6 + F-7).
- **C-P8-6 [LOW]** — Focus trap inside overlay (D4).
- **C-P8-7 [LOW]** — ARIA live region for results announcement (F-8).
- **C-P8-8 [LOW]** — Try/catch around `search()` call (F-9).
- **C-P8-9 [LOW]** — Mobile ⌘K affordance (F-10) — split desktop/mobile button text.
- **C-P8-10 [INFO]** — Post-deploy verification: `curl -sI https://sdtm-pedia.pages.dev/pagefind/pagefind.js` should return `200 + text/javascript` after Phase 8 push (D3). Add to Phase 9 deploy checklist.
- **C-P8-11 [INFO]** — Possible nav-text noise in Pagefind results (D1 root selector). Monitor for SNR complaints.

### Phase 9 entry recommendations

When Phase 9 starts:

1. **First action**: read `.work/07_website/phase8/_progress.json` carryover + this report's C-P8-* list. Confirm whether 8.5 was run.
2. **Pre-flight**: do a real production smoke against `https://sdtm-pedia.pages.dev/zh/guide/user-guide/` after Phase 8 push lands. Real `Cmd+K` in real Chrome with real screen reader. Confirm F-1/F-4/F-5 are either fixed or accepted-with-known-limitations.
3. **Reviewer slot for Phase 9**: 5th-family inaugural candidate. Phase 7 = `superpowers`, Phase 8 = `pr-review-toolkit:silent-failure-hunter` (NEW agent within pr-family). Phase 9 candidates: `feature-dev:silent-failure-hunter` or `oh-my-claudecode:critic` or `claude-code-guide:*` — fresh-family preferred for Rule D depth.

---

## Process notes (Rule D + Rule A audit trail)

- **Rule D (writer-reviewer isolation)**: writer = `oh-my-claudecode:executor` opus (Task 8.2); reviewer = `pr-review-toolkit:silent-failure-hunter` (this report). Cross-family ✓ (omc vs pr-family). Cross-AGENT within pr-family ✓ (silent-failure-hunter vs prior 4 code-reviewer burns). Cross-family vs Phase 7's `superpowers:code-reviewer` ✓.
- **Rule A (semantic spot-check)**: PLAN.md says N=0 (no new translated strings). Phase 7 reviewer F-10 already flagged Rule A rubric coverage gaps for translation work; Phase 8 doesn't add translation surface. F-1 finding here exposes a *related* but distinct gap: Rule A doesn't currently audit "i18n keys defined but not consumed." Recommend adding to Phase 9+ rubric: when adding a new component that mounts in a localized layout, verify it consumes available i18n keys for its strings.
- **Rule B (failures archive)**: PLAN.md says "none expected"; none archived; no obvious failures hidden ✓.
- **Rule C (retro)**: pending in Phase 8 close handoff doc per PLAN.md exit criterion #7.

---

## Pass-criteria check

- ✗ "0 HIGH findings UNLESS the finding is fixable in a small post-review patch and you'd recommend doing so before declaring Phase 8 done" — F-1 IS HIGH, IS fixable in ~10 LOC across 4 files, IS recommended.

→ **CONDITIONAL_PASS** (upgrades to PASS when F-1 is fixed in 8.5 fix bundle, OR Daisy elects PASS-with-carryover and absorbs into Phase 9).

If Daisy prefers ship-now-fix-later: PASS-with-carryover is acceptable. The search feature is *functional* in all 3 langs — Pagefind correctly returns lang-scoped results based on `<html lang>`. The bug is chrome-only, not function. JP/ZH-native users experience an English-labeled box that returns Japanese/Chinese results. That's an acceptable degraded state for soft launch but should be fixed before any external announcement.

---

## Summary

Phase 8 ships a working, dynamic-imported, XSS-safe Pagefind search overlay with ⌘K shortcut, real Pagefind integration, and layered test coverage. The core engineering is clean — the dynamic-import path resolves under preview, the API surface (`m.search` + per-result `r.data()`) matches the runtime module, the SSR shape is correct (no FOUC), and `stripHtml` removes the XSS surface for `<mark>`-tagged excerpts.

The failure mode this review surfaces is **not a Pagefind issue** — it's a **silent i18n regression**. The `search.placeholder` and `search.shortcut` keys exist in `ui.zh.json` / `ui.en.json` / `ui.ja.json` and were defined by a prior translation pass anticipating exactly this overlay. Phase 8 mounted the overlay without wiring the keys. The omission is invisible to the existing test suite (no test asserts "the placeholder on `/ja` is not English"). It will be invisible until a JP-native user opens the search box.

This is the canonical silent-failure pattern: **the work upstream was done, the work downstream was done, and the wiring between them was forgotten**. The fix is ~10 LOC and absorbs F-2 + F-3 in the same edit.

Phase 8 is fundamentally **PASS-class**. The 1 HIGH finding (F-1) is a 5-minute fix that materially improves multilingual UX. The 4 MEDIUM findings cluster around F-1 (i18n) and the silent-catch / e2e bypass patterns that are easy to defer to Phase 9 hardening. The 5 LOW findings are pre-public-release polish.

**Recommendation**: 5-minute 8.5 fix bundle (F-1 + F-2 + F-3 in one edit), then ship.

---

## Verification commands run during this review (read-only)

```bash
git show 4206203 --stat                                 # 4 files, +160 LOC ✓
cd web && npx tsc --noEmit                              # exit 0 ✓
cd web && npm test -- --run                             # 34/34 PASS, 9 files ✓
cd web && cat dist/pagefind/pagefind-entry.json         # 3 langs × 9 pages, valid JSON ✓
cd web && grep canonical dist/zh/guide/index.html       # trailing-slash matched (post-7.5) ✓
cd web && head dist/_astro/SearchOverlay.*.js           # built bundle inspects: import("/pagefind/pagefind.js") emitted literally ✓
cd web && tail dist/pagefind/pagefind.js                # export{createInstance, ..., search}; ✓
cd web && (npm run preview &) && curl -sI :4321/pagefind/pagefind.js  # 200 OK, text/javascript ✓
cd web && grep '<html lang' dist/{zh,en,ja}/guide/user-guide/index.html  # lang attr correct per locale ✓
```

End of report.
