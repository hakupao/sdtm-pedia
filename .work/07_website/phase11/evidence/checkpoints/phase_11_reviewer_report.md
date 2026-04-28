# Phase 11 Reviewer Report — oh-my-claudecode:code-reviewer

> **Reviewer**: `oh-my-claudecode:code-reviewer` (3rd-burn omc-family NEW agent — Phase 6 critic / Phase 10 verifier / Phase 11 code-reviewer)
> **Date**: 2026-04-30
> **Scope**: Phase 11 commits `e36354c` → `6c92b05` (5 implementation commits, HEAD = `6c92b05`, baseline = `cdd8f8e`)
> **Mode**: read-only static review + test re-run

## Verdict

**PASS**

## Summary

Phase 11 ships 5 user-driven UX polish items (TopNav/Footer max-w wrap, ⌘K → 搜索 明文, utilities divider, DocsLayout Footer mount, v1.2 font-size 4-tier adjuster). All 5 commits map 1:1 to PLAN §2 scope; zero files outside expected directory tree; zero C-P9-* / C-P10-* carryover silently absorbed.

Code quality is high throughout: the FontSizeToggle component faithfully mirrors the ThemeToggle pattern (correct WAI-ARIA `aria-pressed` toggle semantic, not `aria-current`), the localStorage default-as-absent-attribute trick avoids CSS specificity drift, the BaseLayout flash-prevention script extends cleanly to handle both `theme` and `fontsize` keys behind one shared try/catch, the percentage-based `--fs-base` (87.5%/100%/112.5%/125%) is the right choice for browser-zoom-respecting a11y, and the i18n parity tests (helpers.test.ts) automatically guard the +18 new keys via vitest's full-key sort comparison.

All 4 verification gates pass at the same numerical baseline the PLAN predicted: tsc 0 / vitest 57/57 (+6 over Phase 10's 51/51, exactly matching FontSizeToggle.test.tsx's 6-spec count) / e2e 7/7 (search spec was correctly updated to assert the new i18n-localized "搜索" label) / build 31 pages + Pagefind 27 indexed / 6457 words.

No HIGH or MEDIUM findings. Two LOW observations below are stylistic / process notes carried forward to Phase 12 as `C-P11-1` and `C-P11-2`; neither blocks phase close, and a fix-bundle commit is **not** recommended.

## Stress dimensions D1-D7

### D1 — TopNav + Footer max-w-screen-xl wrap (11.1) — PASS

Outer `<header class="border-b border-rule">` and `<footer class="bg-ink text-bg">` keep their full-width chrome strip (border + bg respectively). Inner `<div class="max-w-screen-xl mx-auto px-7 py-N flex justify-between items-center">` wraps content. The flex/justify/items classes correctly migrated from outer header to inner div; mobile `px-7` 28px parity preserved; pattern matches Phase 10.2 LandingLayout convention. DocsLayout's existing `<div class="flex max-w-screen-xl mx-auto flex-col lg:flex-row">` confirms the same design token is sustained across landing/docs/chrome.

### D2 — ⌘K hint Option A (11.2) — PASS

`grep -rn "search.shortcut|⌘K|<kbd>" web/src/` returns 0 matches outside the new `search.label`. Per-locale strings landed (zh "搜索" / en "Search" / ja "検索"). Button text + aria-label both reference `t['search.label']` (TopNav.astro:27,29). The `onclick="document.dispatchEvent(new KeyboardEvent('keydown', {key:'k', metaKey:true}))"` Cmd+K dispatch is preserved — the keyboard listener inside SearchOverlay is unaffected. Search e2e spec (search.spec.ts:14) was correctly updated to assert `getByLabel('搜索')` against the `/zh/` route — passes.

### D3 — TopNav utilities visual divider (11.3 + 11.5 5th group) — PASS

The 5th utility group (FontSizeToggle) was added in 11.5 *after* 11.3 committed; the divider pattern was sustained correctly:
- search button: `border-l border-rule pl-4 pr-4`
- LangSwitcher wrapper: `border-l border-rule pl-4 pr-4 flex items-center`
- ThemeToggle wrapper: `border-l border-rule pl-4 pr-4 flex items-center`
- FontSizeToggle wrapper: `border-l border-rule pl-4 flex items-center` (no `pr-4` — intentional, last group)

Internal consistency holds. Parent span uses `flex items-center ml-2` (no `gap-3` — gaps now provided by per-child `pl-4 pr-4`).

### D4 — DocsLayout Footer mount (11.4) — PASS

`<Footer lang={lang} />` mounts after the flex container `</div>` and before `</BaseLayout>` in DocsLayout.astro:23. The flex container (DocsSidebar + article + DocsTOC) closes cleanly before Footer; DocsTOC's `sticky top-0 self-start max-h-screen overflow-y-auto` constrains stickiness to its own column, not page-level — no overlap risk with the post-flex Footer strip. LandingLayout vs DocsLayout structural parity now holds: both mount `<TopNav>` → content → `<Footer>` inside `<BaseLayout>`. Note: LandingLayout still has `<EnterFadeScript />` that DocsLayout lacks — pre-existing intentional asymmetry (no scroll-fade on docs reader), not a Phase 11 regression.

### D5 — v1.2 font-size 4-tier adjuster (11.5) — PASS

**Lib (fontSize.ts)** — 22 LOC, fully type-safe. Mirrors theme.ts API surface exactly except for the validation array (`VALID: FontSize[]`) replacing the `||` chain. `applyFontSize('md')` correctly uses `removeAttribute` so the default tier maps to "no attribute" → `:root { --fs-base: 100% }` cascades cleanly with no CSS specificity drift.

**Component (FontSizeToggle.tsx)** — 45 LOC. Clean ThemeToggle mirror:
- `aria-pressed={t === size}` boolean per button — correct WAI-ARIA toggle semantic (not `aria-current`, which would be wrong for a setting-applier rather than a navigation-current).
- `aria-label={labels[t]}` + `title={labels[t]}` from i18n props.
- `style={{ fontSize: TIER_PX[t] }}` — 9px/11px/13px/15px visual scaling on the button glyph "A" itself, communicating the tier visually. Inline style is the only sustainable way to express per-button variable typography; acceptable departure from Tailwind-only convention.
- `<nav aria-label={navLabel}>` correctly wraps the 4 buttons (verified by spec #6 in tests).
- `useEffect` reads stored value on mount + applies + sets state. Single source of truth.

**CSS (global.css)** — 4 lines. Percentage-based scale `87.5% / 100% / 112.5% / 125%` is the a11y-correct choice (respects browser-level zoom default). `html { font-size: var(--fs-base); }` causes Tailwind rem-relative tokens (text-base / text-lg / prose / sidebar / TOC) to scale automatically; chrome `text-[10px]` arbitrary classes stay fixed by design (preserves data-density typography intent — TopNav identifier, SectionLabel, Footer date strip).

**Flash prevention (BaseLayout.astro:26-39)** — single inline `is:inline` script with one shared try/catch wraps both `theme` and `fontsize` localStorage reads. The fontsize check `f === 'sm' || f === 'lg' || f === 'xl'` deliberately omits `'md'` (since md = default = no attribute). Mirrors theme's `t === 'light' || t === 'dark'` pattern (omits `'system'` for the same reason). Sustained design.

**Caller wiring (TopNav.astro:45-56)** — `<FontSizeToggle client:load navLabel + labels />` passes 5 i18n strings as expected. `client:load` matches ThemeToggle's hydration directive — no SSR mismatch concerns since the component initializes with `'md'` state, useEffect adjusts post-hydration.

**Tests (FontSizeToggle.test.tsx)** — 6 specs, all green:
1. Renders 4 inline buttons with i18n aria-labels
2. Marks "Medium" as pressed by default (no stored choice)
3. Click Small persists "sm" + applies data-fontsize + flips aria-pressed
4. Click X-Large persists "xl" + applies data-fontsize
5. Click Medium after Large removes data-fontsize + persists "md" (explicitly covers the `removeAttribute` branch)
6. Uses nav with passed aria-label

`beforeEach` clears localStorage + removes data-fontsize attribute → no test pollution.

### D6 — No regressions — PASS

| Gate | Result | PLAN target |
|---|---|---|
| `npx tsc --noEmit` | 0 errors | 0 |
| `npm run test` | **57/57** (12 files, 1.65s) | 57/57 (+6 vs Phase 10's 51/51) |
| `npm run test:e2e` | **7/7** (7.9s) | 7/7 |
| `npm run build` | **31 pages** | 31 |
| Pagefind | **27 indexed / 6457 words** | 27 indexed (Phase 11 changes affect chrome + new feature, not body content — confirmed) |

Search spec adapted to localized aria-label correctly (search.spec.ts:14).

### D7 — Plan deviation flag — NONE

`git diff cdd8f8e..6c92b05 --name-only | grep -vE "^(\.work/07_website/phase11/|web/src/components/(astro|react)/|web/src/i18n/|web/src/layouts/|web/src/lib/|web/src/styles/|web/tests/e2e/)"` returns 0 lines. All 14 changed files (2 PLAN/progress + 12 web) fall inside the expected directory whitelist. No carryover silently absorbed.

## Findings

### F-1 [LOW] — `getStoredFontSize` validation drift between lib and inline flash-prevention script

**File**: `web/src/layouts/BaseLayout.astro` (lines 34-37) + `web/src/lib/fontSize.ts` (line 4)
**Issue**: `fontSize.ts` declares `VALID: FontSize[] = ['sm', 'md', 'lg', 'xl']` and validates `getStoredFontSize` via `VALID.includes(...)`. The inline flash-prevention script duplicates the valid-set check inline as `f === 'sm' || f === 'lg' || f === 'xl'` (deliberately omitting `'md'` because md = default = no attribute). If the `VALID` set ever expands (e.g. future xxl tier), the inline script must be updated in lockstep — there is no shared constant.
**Fix**: None required for v1.2; the duplication is bounded and intentional. **Decision**: carryover to Phase 12 as **C-P11-1** [process] — if a 5th tier is ever added, audit the BaseLayout inline script. Mirrors the same condition that already exists for theme (`'light' || 'dark'` literal). Not a fix-in-bundle item.

### F-2 [LOW] — FontSizeToggle nav classes diverge from ThemeToggle in tracking/text-size tokens

**File**: `web/src/components/react/FontSizeToggle.tsx:28`
**Issue**: ThemeToggle's `<nav>` uses `className="flex gap-2 font-mono text-[10px] tracking-wider"`. FontSizeToggle's `<nav>` uses `className="flex items-baseline gap-2 font-mono"` — drops `text-[10px] tracking-wider`. The drop is functionally correct (per-button `style={{ fontSize: TIER_PX[t] }}` overrides the parent text-[10px] anyway, and tracking is irrelevant for single-letter "A" buttons) but the className diverges from the established mirror pattern, which can confuse future maintainers reading "FontSizeToggle should look like ThemeToggle".
**Fix**: Optional cosmetic — could add `tracking-wider` back for token consistency, but no visual difference. **Decision**: carryover to Phase 12 as **C-P11-2** [cosmetic]. Not a fix-in-bundle item.

## Rule A spot-check (N=18)

18 new i18n strings = 1 `search.label` × 3 langs + 5 `fontsize.*` × 3 langs.

| Key | zh | en | ja | Verdict |
|---|---|---|---|---|
| search.label | 搜索 | Search | 検索 | natural across all 3 |
| fontsize.label | 字号 | Font size | 文字サイズ | canonical UI terms |
| fontsize.sm | 小 | Small | 小 | natural |
| fontsize.md | 中 | Medium | 中 | natural |
| fontsize.lg | 大 | Large | 大 | natural |
| fontsize.xl | 特大 | X-Large | 特大 | natural; see note |

**Note on ja "特大"**: kanji "特大" is the standard Japanese rendering for "extra-large" in size contexts (matches the CSS font-size keyword `x-large` ≈ Japanese 特大). Cross-family vs `theme.system` "システム" / `theme.dark` "ダーク" / `theme.light` "ライト" (all katakana loanwords) reflects an *appropriate* domain split: theme names are loanwords, size grades are native kanji. No flag.

## Test re-run results

```
$ cd web && npx tsc --noEmit
[exit 0, no output]

$ cd web && npm run test
Test Files  12 passed (12)
     Tests  57 passed (57)
  Duration  1.65s

$ cd web && npm run test:e2e
Running 7 tests using 3 workers
✓ 1 lang.spec.ts › root redirects to /zh/ (250ms)
✓ 3 search.spec.ts › search opens via Cmd/Ctrl+K and finds AESER (365ms)
✓ 2 smoke.spec.ts › landing /zh/ renders all 5 sections (805ms)
✓ 4 smoke.spec.ts › landing /en/ renders all 5 sections (1.1s)
✓ 5 smoke.spec.ts › landing /ja/ renders all 5 sections (1.1s)
✓ 6 smoke.spec.ts › docs reader renders user-guide in zh (101ms)
✓ 7 smoke.spec.ts › link-resolution: every <a> in main resolves ≠404 (560ms)
7 passed (7.9s)

$ cd web && npm run build
[build] 31 page(s) built in 937ms
[Pagefind] Indexed 27 pages / 6457 words / 3 languages
```

## Plan deviation flag

**NONE.** All 14 changed files (`git diff cdd8f8e..6c92b05 --name-only`) fall within: `.work/07_website/phase11/` (2) + `web/src/components/{astro,react}/` (3) + `web/src/i18n/` (3) + `web/src/layouts/` (2) + `web/src/lib/` (1) + `web/src/styles/` (1) + `web/tests/e2e/` (1) + 1 docs metadata. Zero C-P9-1..16 / C-P10-1..5 / pre-existing carryover silently absorbed. Daisy's "把这次就当作 1.2" 5-item scope discipline held.

## Positive observations

- **Pattern reuse over invention**: FontSizeToggle is a near-perfect mirror of ThemeToggle (same useState/useEffect/switchTo/nav-with-aria-label/aria-pressed shape). Reduces cognitive load for future maintainers.
- **Default-as-absent-attribute trick**: Both `theme.ts` and `fontSize.ts` use `removeAttribute` for the default tier. This avoids CSS-specificity drift if a future stylesheet ever overrides at the `:root` level — the data attribute selector simply doesn't match. Sustained micro-architectural consistency.
- **Shared flash-prevention script**: BaseLayout extends one IIFE with one try/catch to handle both keys. Avoids two separate inline scripts and two parse passes. Idiomatic.
- **i18n key parity test**: helpers.test.ts's full-key-sort comparison automatically guarded the +18 new keys without any test additions — the seed-dictionary-as-source-of-truth pattern paid off.
- **Per-button visual tier communication**: The "A" glyph at 9/11/13/15px self-documents the size choice without relying on the user reading the label. Strong progressive enhancement for keyboard/screen-reader-light users while remaining accessible.
- **Search e2e spec migration**: search.spec.ts:14 was updated to assert the new i18n label `getByLabel('搜索')` — the test author understood that locale-scoped DOM queries strengthen the test (it now also asserts the zh route gets the zh label, which catches future i18n regressions).

## Recommendation

No fix-bundle commit needed before phase close. Both LOW findings are carryover to Phase 12 (`C-P11-1` process / `C-P11-2` cosmetic). Proceed to Task 11.7 (close + handoff + index sync + push).

---

**Reviewer signature**: oh-my-claudecode:code-reviewer (3rd-burn omc-family NEW agent)
**Total findings**: H=0 / M=0 / L=2
**Verdict**: **PASS**
