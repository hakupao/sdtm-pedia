# Website Build — Phase 4 → Phase 5 Handoff

> **Date**: 2026-04-28
> **Outgoing session**: completed Phase 3.6 (end-of-Phase-3 gate, conditional PASS) + Phase 4 (8 tasks + 1 .gitignore + 1 reviewer-fix = 10 commits, all on `main`)
> **Incoming session**: Phase 5 — Docs Reader (5+ tasks, plan §"Phase 5" lines 2010-2312)

## What's done — Phase 3.6 + Phase 4

Phase 3.6 = end-of-Phase-3 integration gate per the Phase 2→3 handoff §"End-of-Phase-3 gate" requirement. Dispatched `pr-review-toolkit:code-reviewer` against commits `92b91f3..6903060`. Verdict: **Conditional PASS for Phase 4 entry** with 4 carryover findings (see §"Carryover" below). Build green, 17/17 vitest, tsc clean.

Phase 4 = Landing Page. 10 commits on `main` (oldest → newest):

| Commit | Subject |
|---|---|
| `991b0f5` | 07 Website Phase 4.1 — LandingLayout + TopNav (mobile drawer) + Footer |
| `f8c8c4f` | 07 Website Phase 4.2 — HeroSection.astro |
| `3ee3ae5` | 07 Website Phase 4.3 — §02 PlatformsSection (count-up island, 8 tests, JSON data) |
| `3a88c9f` | 07 Website Phase 4.4 — §03 ComparePreviewSection (4-dim preview, x-scroll, accent winners) |
| `071cd23` | 07 Website Phase 4.5 — §04 DemoSection (3 demos D0/D1/D5 trilingual) |
| `c3eb6d4` | 07 Website Phase 4.6 — §05 DownloadsSection (4-bundle grid, GH URL builder, 2 tests) |
| `46afbe5` | 07 Website Phase 4.7 — landing page wired (3 langs × 5 sections, e2e smoke 4/4) |
| `f566da3` | 07 Website Phase 4.8 — section enter-fade animation (IO + prefers-reduced-motion guard) |
| `ecf9049` | 07 Website .gitignore — exclude Playwright test-results/ and playwright-report/ |
| _(this commit)_ | 07 Website Phase 4.9 — reviewer-fix bundle (H1 + H3 + H4 + key parity test) |

## End-of-Phase-4 review verdict

Dispatched `pr-review-toolkit:code-reviewer` against `6903060..f566da3`. Verdict: **PASSES structural gate, 4 HIGH integration risks** that per-task structural review could not catch (the Phase 2 lesson again). Of the 4 HIGH:

- **H1 fixed in Phase 4.9**: HeroSection status line was hard-coded `CLAUDE 17/17 · GPT 16.5 · GEMINI 16 · NBLM 15` — 3 of 4 platforms missing `/17` denominator. Now data-driven from `platforms.json` so future score updates flow through one source.
- **H3 fixed in Phase 4.9**: `getUIStrings` return type tightened from `Record<string, string>` to `Record<UIKey, string>` where `UIKey = keyof typeof zh`. TS now flags typo'd keys at compile time. Plus 2 new vitest parity tests assert en/ja share the exact key set with zh — catches translation drift the moment a key is added/removed.
- **H4 fixed in Phase 4.9**: ComparePreviewSection `<a href="/compare">` was the only nav link bypassing i18n; would 404 even at the root level. Now `/${lang}/compare` consistent with all other future-route CTAs.
- **H2 NOT fixed — Phase 5 dependency** (see below).

## Carryover — what Phase 5 must address before public deploy

### **HARD-BLOCKER for any external/Daisy walkthrough — must land in Phase 5 or be explicitly gated by a feature flag**

#### H2 (carryover) — Download bundle .zips do not exist
- **Evidence**: `find ai_platforms/release/v1.0 -name '*.zip'` → zero hits. `self_deploy/{claude,chatgpt,gemini,notebooklm}/` exist as directories with file counts/sizes matching `web/src/data/downloads.json` (19/9/4/43 files, 4.6/9.3/2.2/9.4 MB), but no zips have been built or published to a GitHub release tagged `v1.0`.
- **Bite**: every download link on the landing page returns 404 at first paint. Reviewer flagged this as the textbook structural-PASS-vs-semantic-PASS miss.
- **Phase 5/9 task options**:
  1. Build the 4 zips from the existing `self_deploy/` dirs and publish a `v1.0` GitHub release before any public link goes out. Plan §Phase 8 ("Downloads Pipeline", lines 2647-2793) is the right home for the zip-build script.
  2. Until then, gate `DownloadsSection` behind a feature flag (`if (import.meta.env.PUBLIC_RELEASE_PUBLISHED) ...`) or replace the section with a "release pending" placeholder.
- **Don't ship `/zh/` to anyone (even internally) without one of the above.**

#### M1 (carryover) — 6 dead CTA links to non-existent routes
The landing page advertises navigation to:
- `/${lang}/guide/` (TopNav "GUIDE", Footer "GUIDE", HeroSection primary CTA "READ THE GUIDE") — **lands in Phase 5** (Docs Reader)
- `/${lang}/changelog` (Footer "CHANGELOG") — **lands in Phase 5** as a special-cased doc page
- `/${lang}/guide/demo-questions` (TopNav "DEMO", DemoSection "ALL TEN QUESTIONS") — **lands in Phase 5** as a guide entry
- `/${lang}/compare` (ComparePreviewSection "FULL COMPARISON") — **lands in Phase 6** (Multi-dim Comparison Page)

Phase 4 e2e smoke does NOT click these links — it asserts only DOM presence + visibility. **Phase 5 should add a link-resolution e2e** that for each `<a>` in `main` performs a HEAD/GET and asserts non-404. Cheap insurance, catches the next M1 immediately.

### Soft (cheap insurance to add when you next touch the file)

#### M2 — TopNav drawer JS won't survive Astro view transitions
`web/src/components/astro/TopNav.astro:25-31` runs once at initial load via top-level `document.getElementById`. If/when Phase 5 enables `<ViewTransitions />` (planned per spec but not yet wired), soft-navigation back to `/zh/` will leave the drawer toggle dead. **Fix**: wrap in `document.addEventListener('astro:page-load', initDrawer)`. No-op when transitions are off.

#### M3 — `compare-dimensions.json` lookup swallows missing-platform errors
`ComparePreviewSection.astro:34` casts `p.key as keyof typeof d.values`. If `platforms.json` adds a 5th platform without parity in every dimension's `values`, the cell renders the literal string `undefined`. **Fix**: add `web/src/data/data.test.ts` asserting each dimension's `values` keys === `platforms.map(p => p.key)`.

#### M4 — `.enter-fade` no-JS = blank below-the-fold
With JS disabled (RSS readers, text browsers, no-JS scrapers), every section permanently sits at `opacity: 0`. Pagefind still indexes server-rendered HTML so search works, but a no-JS human visitor sees only the dev-toolbar shell. **Fix**: add `<noscript><style>.enter-fade { opacity: 1 !important; transform: none !important; }</style></noscript>` to `EnterFadeScript.astro`. 3 lines.

### Phase 3 carryover (still open at Phase 4 close)

- **H1 (Phase 3 reviewer)** — `replaceLangInPath` regex misses paths like `/zh?q=x` (no slash + query). Did NOT bite Phase 4 because `Astro.url.pathname` strips query before reaching `LangSwitcher`. **Phase 5 risk**: if any client-side code mutates `location.pathname` and feeds the result to `replaceLangInPath`, this surfaces. Tighten the regex when Phase 5 first uses LangSwitcher in a non-trivial path.
- **M3 (Phase 3 reviewer)** — `add-frontmatter.mjs` defaults `lang: en` for files without lang suffix → `DEMO_QUESTIONS.md` and `CHANGELOG.md` are tagged `lang: en` but DEMO_QUESTIONS is trilingual content. **Phase 5 must decide** before wiring `/${lang}/guide/demo-questions`: split into 3 lang variants OR set `lang: undefined` and have the docs reader treat as language-neutral.
- **L2 (Phase 2 deferred §1)** — `theme.ts` SSR asymmetry. Did NOT surface in Phase 4 (BaseLayout's `is:inline` IIFE runs in browser only). **Phase 5 risk**: if any `.astro` front-matter calls `applyTheme()` SSR-side, surface. Add JSDoc `@remarks Client-only` header to theme.ts now to prevent surprise.

## Working state — Phase 4 close

- **Branch**: `main`. HEAD = `<phase-4.9-reviewer-fix>`. Pushed once user approves.
- **`web/` tree** is fully scaffolded for Phase 5 docs reader to compose:
  - `LandingLayout.astro` is reusable for any landing-style page.
  - `BaseLayout.astro` is the SEO/font/lang/theme foundation Phase 5 should also wrap.
  - `TopNav` + `Footer` + `EnterFadeScript` are ready to be reused under any `[lang]/...` route.
  - `i18n/helpers.ts` `UIKey` type-safety means Phase 5 will get TS errors on typo'd `t['guide.toc']` etc.
  - `i18n/ui.{zh,en,ja}.json` will need new keys for guide/TOC/breadcrumb/prev-next nav. Adding to one file without the others = vitest fails (key parity test).
- **Test status**: 29/29 vitest, 4/4 e2e, tsc clean, build green (3 lang pages + redirect, Pagefind indexed 545 words across 3 langs).

## How the new session should start

Read this handoff file FIRST, then read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` Phase 5 section (lines 2010-2312). Skip Phases 0-4 (done).

Before dispatching Phase 5 Task 5.1, decide:
1. **DEMO_QUESTIONS lang attribution** (Phase 3 carryover M3) — split or keep language-neutral?
2. **Download-bundle gating** (Phase 4 carryover H2) — feature flag or build-the-zips first?
3. **Link-resolution e2e** (Phase 4 carryover M1) — add as Phase 5 entry task?

Same execution mode as Phases 1-4: subagent-driven dev for non-trivial tasks, direct-verify for trivial ones, end-of-phase integration reviewer + smoke probe before declaring done. The Phase 2 lesson keeps proving itself — Phase 4's reviewer caught H1/H2/H3/H4 + M1-M4 that 8 per-task structural reviews missed.

## Phase 4 deferred minors (LOW, defer indefinitely)

- L1: `replaceLangInPath` regex query edge case (Phase 3 carryover; not bitten).
- L2: `theme.ts` SSR asymmetry (Phase 2 deferred; not bitten).
- L3: `CountUp` rAF cleanup-return inside IO callback is dead code; cosmetic, ≤600ms RAF leak on unmount.
- L4-L6: cosmetic/non-issues per Phase 4 reviewer.
