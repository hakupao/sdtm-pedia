# Website Build — Phase 2 → Phase 3 Handoff

> **Date**: 2026-04-27 (evening)
> **Outgoing session**: completed Phase 2 (5 tasks + 1 fixup + 3 closure = 9 commits, all on `main` and pushed to `origin/main`)
> **Incoming session**: should start Phase 3 (Content Collections + i18n, 5 tasks)

## What's done — Phase 2

9 commits landed on `main`. Commit chain (oldest → newest):

| Commit | Subject |
|---|---|
| `2772d46` | 07 Website Phase 2.1 — global.css: tokens light+dark, font imports, reduced-motion guard |
| `65b4326` | 07 Website Phase 2.2 — theme.ts: localStorage + system + applyTheme (5 tests) |
| `2ad3aa8` | 07 Website Phase 2.3 — ThemeToggle island (4-state cycle, 2 tests) |
| `bcb7d0f` | 07 Website Phase 2.1.1 — @theme inline mapping for Tailwind accent/bg/ink utilities (used in 2.3 + 2.4) |
| `d3d841f` | 07 Website Phase 2.4 — SectionLabel.astro (§NN / LABEL ritual) |
| `33e840c` | 07 Website Phase 2.5 — BaseLayout.astro (theme flash guard, og meta, lang attr) |
| `3bcd13c` | 07 Website Phase 2.6 — drop unavailable @fontsource/source-serif-pro/500.css import |
| `4fd216a` | 07 Website Phase 2.7 — pin Vite ^7 via package overrides (Astro 6 / Tailwind v4 vite8 conflict) |
| `9cc3762` | 07 Website Phase 2.8 — try/catch around BaseLayout theme flash-guard IIFE (Safari private mode safety) |

(Note: untracked `.work/06_deep_verification/...` files at end of session are parallel batch-38/39/40 verification lane; **do not stage, do not modify** — that's a different work stream.)

## Three architectural deviations vs original plan

The original plan was written before Phase 2 hit real Node 25 + vitest 4 + Tailwind v4 + Astro 6 integration realities. Three deviations were applied with Daisy's authorization mid-Phase-2:

1. **Task 2.3 — Option B 4-state cycle replaces broken static `NEXT` table.** Plan's `NEXT = { light: 'dark', dark: 'system', system: 'light' }` cannot satisfy the verbatim test, which requires state `'system'` to map to two different next states (`'dark'` on click 1, `'light'` on click 3 from initial). Daisy chose Option B: keep the test verbatim and rewrite impl as a 4-state alternating cycle (`system → dark → system → light → system → dark → ...`) using `useRef<'dark'|'light'>('dark')` for `nextFlip` direction. Matches GitHub/Vercel "sticky-neutral toggle" UX.
2. **Phase 2.1.1 fixup commit (`bcb7d0f`) — `@theme inline {}` block in `global.css`.** Phase 1 review (handoff §"Forward-looking concerns" #1) flagged this as "deferred until Tailwind utilities are first consumed". Tasks 2.3 (`hover:text-accent`) and 2.4 (`text-accent`, `bg-accent`) are the first consumers; without the mapping, Tailwind v4 silently no-ops these utilities (no built-in `accent` palette key). Fixup exposes 7 design tokens (`--color-bg`, `--color-bg-alt`, `--color-ink`, `--color-ink-mute`, `--color-ink-faint`, `--color-accent`, `--color-rule`) as Tailwind utilities sourcing from the `:root` CSS variables.
3. **Phase 2.7 expanded scope — `@vitejs/plugin-react` downgrade in addition to `vite ^7` override.** Astro 6 requires Vite 7; `@tailwindcss/vite@4.2.4` brings Vite 8 transitively. The documented Astro fix is `"overrides": { "vite": "^7" }` in `package.json`. But the existing devDep `@vitejs/plugin-react@^6.0.1` imports `vite/internal` which is a Vite 8-only export, so pinning vite ^7 alone broke the test runner. Implementer downgraded `@vitejs/plugin-react` to `^5.2.0` (peer-compat with vite 4-8 per its `peerDependencies`; was already transitively installed by `@astrojs/react`). Both files committed together (`package.json` + `package-lock.json`).

## Working state — Phase 2 complete

- **Branch**: `main`. HEAD = `9cc3762`. Pushed to `origin/main` at end of Phase 2.
- **`web/` tree** is fully scaffolded for the design system:
  - `web/src/styles/global.css` — fontsource imports (7, was 8 before 2.6 dropped 500.css), `@import "tailwindcss"`, `@theme inline {}` mapping, light/dark token blocks, OS-preference fallback, body baseline, reduced-motion guard.
  - `web/src/lib/theme.ts` — 4 functions (`getStoredTheme`, `setStoredTheme`, `applyTheme`, `resolveEffectiveTheme`), localStorage-persisted, 'system' default.
  - `web/src/lib/theme.test.ts` — 5 tests, all passing.
  - `web/src/test-setup-storage.ts` — Node 25 + jsdom + vitest 4 polyfill (`InMemoryStorage` for localStorage/sessionStorage + `matchMedia` stub). Idempotent guards. Will become dormant once Node fixes its native localStorage stub upstream.
  - `web/vitest.config.ts` — `setupFiles: ['./src/test-setup-storage.ts', './src/test-setup.ts']` (order matters — polyfill before jest-dom matchers). `environmentOptions.jsdom.url: 'http://localhost'`.
  - `web/src/components/react/ThemeToggle.tsx` — React 19 island, useRef-based 4-state cycle.
  - `web/src/components/react/ThemeToggle.test.tsx` — 2 tests, all passing.
  - `web/src/components/astro/SectionLabel.astro` — pure visual ritual `§ NN / LABEL`, 2 props.
  - `web/src/layouts/BaseLayout.astro` — foundation layout, lang/title/description/og meta, inline theme-flash guard with try/catch.
  - `web/package.json` — `"overrides": { "vite": "^7" }` + `@vitejs/plugin-react: ^5.2.0`.
- **Test status**: 7/7 green (`Test Files 2 passed (2) | Tests 7 passed (7)`).
- **TypeScript strict**: clean (`npx tsc --noEmit` exit 0).
- **`npm ls vite`**: uniformly `vite@7.3.2 deduped` everywhere (no v8 leakage).
- **Build**: `npm run build` green. **Verified end-to-end with smoke probe**: a temporary `web/src/pages/smoke-phase2.astro` (NOT committed) imports `BaseLayout` + `SectionLabel` + uses Tailwind utilities (`text-accent bg-bg-alt font-mono`); build succeeds, dist CSS contains `text-accent` rule + `Source Serif` `@font-face` + `--accent` values. Tailwind v4 `@theme inline` inlines `var(--accent)` directly rather than emitting `--color-accent` aliases — this is correct v4 behavior, not a bug.

## Process learning — 规则 A enforcement gate

**Per-task reviews PASSED structurally for tasks 2.1-2.5; final integration review caught 2 Critical Phase 3 blockers + 1 Important defensive gap that would have detonated on Phase 3's first real route commit.** Specifically:

- Critical #1: `@fontsource/source-serif-pro/500.css` does not exist in the package (only `200/300/400/600/700/900` ship). Plan §2.1 line 5 referenced it.
- Critical #2: Astro 6 / Tailwind v4 / Vite 7-vs-8 mismatch crashes the build the moment any route consumes `global.css`.
- Important #4: `BaseLayout.astro` flash-guard `localStorage.getItem` lacks try/catch; throws in Safari private browsing → halts head parsing.

Why per-task reviews missed all 3: **no task wired `BaseLayout`/`global.css` into a real (non-underscore) route**. Per-task green-lights were structural-only — file syntactically valid, tests pass on the file in isolation. The system never had to run as a system. This is exactly 规则 A from CLAUDE.md ("结构检查 ≠ 语义检查").

The 3 closure commits (2.6/2.7/2.8) absorbed all blockers. The smoke probe (a non-underscore route consuming `BaseLayout` + Tailwind utilities) is now the verified entry contract. **Phase 3 should add a smoke-probe gate at end-of-phase before declaring done.** Not just for Phase 3 — for any future phase that touches the build path (3, 4, 5, 7).

## Phase 2 deferred minors (not blocking, fix opportunistically)

These were flagged by per-task reviewers but deemed forward-looking; defer to Phase 3+ when their cost/value crosses the threshold:

1. **`theme.ts` SSR asymmetry** — `getStoredTheme` has `typeof localStorage === 'undefined'` SSR guard, but `setStoredTheme`, `applyTheme`, `resolveEffectiveTheme` don't. Today this is fine (only client-only ThemeToggle island consumes them). If Phase 4+ ever calls theme functions from a `.astro` front-matter (SSR context), guards will be needed. Add JSDoc `@remarks Client-only` header now to prevent surprise.
2. **`ThemeToggle` SSR placeholder icon flash** — useState('system') initial render shows `◐` until useEffect hydrates. The page background already won't flash (BaseLayout inline guard handles it), but the toggle icon will briefly mismatch. Acceptable Astro-island tradeoff; would need server-rendered cookie read to fully eliminate.
3. **`nextFlip` ref doesn't persist across page reloads** — refresh resets to `'dark'` initial direction regardless of session history. Cosmetic; acceptable simplification.
4. **`global.css` light-token block uses both `:root, [data-theme="light"]`** — equal-specificity tie resolved by source order. Works; subtly confusing to readers. Cleanup opportunity.
5. **`theme.test.ts` hardcodes `'theme'` localStorage key** — duplicates the `KEY` constant in `theme.ts:4`. Rename risk if key ever changes. Refactor to assert via `getStoredTheme()` instead of `localStorage.getItem('theme')` direct read.
6. **`ThemeToggle.test.tsx` doesn't test the 4th click (`light → system`)** — leaves alternation invariant partly uncovered. Add 4th click assertion if you want full cycle coverage.
7. **`InMemoryStorage` polyfill missing `Storage` proxy property-access semantics** — real browser supports `localStorage.foo = 'bar'`; polyfill doesn't. Tests don't use it today. Add a comment near the polyfill noting the limitation.
8. **`test-setup-storage.ts` is "tech debt by inertia" risk** — once Node fixes its native localStorage stub, the polyfill becomes dormant but won't auto-clean up. Add a comment near the guard reminding to delete this file when Node ≥X removes the broken stub.

None of these block Phase 3. Suggested handling: address #1 + #4 in Phase 3 (since 3.x will start consuming theme/tokens from `.astro` front-matter contexts and visual review may surface them); #5 + #6 + #8 next time touching the test files; #2 + #3 + #7 punt to Phase 10 polish.

## What's next — Phase 3 (5 tasks)

Per plan §"Phase 3 — Content Collections + i18n" (lines 938-1301 in `docs/superpowers/plans/2026-04-27-sdtm-release-website.md`):

- **3.1 Frontmatter + content collection schema** — write `web/scripts/add-frontmatter.mjs` (one-shot script), run it to prepend `lang/slug/order/title` frontmatter to `ai_platforms/release/v1.0/*.md` (~27 files), create `web/src/content/config.ts` with Astro content collection schema. **Note: this task crosses the `web/` boundary** (touches `ai_platforms/release/v1.0/*.md`). Plan splits into TWO commits per Step 4:
  - First commit: release doc frontmatter additions (`ai_platforms/release/v1.0/*.md`)
  - Second commit: web schema + script (`web/src/content/config.ts` + `web/scripts/add-frontmatter.mjs`)
  - **Important**: the `add-frontmatter.mjs` script has `if (body.startsWith('---')) continue;` — it's idempotent, won't double-add. Some release docs already have frontmatter from Phase 6.5 release work; verify before running. Don't accidentally clobber existing fields.
- **3.2 i18n UI strings** — 3 dictionary JSON files (`web/src/i18n/ui.{zh,en,ja}.json`). No tests. Pure static.
- **3.3 i18n helpers + tests** — `web/src/i18n/helpers.ts` + `helpers.test.ts`. **TDD applies.** Likely: `t(key, lang)` lookup + `getCurrentLang(url)` parsing + fallback chain.
- **3.4 LangSwitcher React island + tests** — `web/src/components/react/LangSwitcher.tsx` + `.test.tsx`. **TDD applies.** Switches between zh/en/ja via URL prefix manipulation.
- **3.5 Root redirect `/` → `/zh/`** — `web/src/pages/index.astro` (replaces stock starter) — meta-refresh or 308 redirect to `/zh/` (default locale per `astro.config.mjs`'s `prefixDefaultLocale: true`). Plan handoff §"Forward-looking concerns" #2 anticipated this would unblock the `/ → 404` situation.

**Phase 3 takes ~60-90 min.** Heavier than Phase 2 because 3.1 crosses repo boundaries, 3.3 + 3.4 are TDD with real tests, and 3.5 finally unblocks the root URL.

## Forward-looking concerns from Phase 2 review (non-blocking, Phase 3-relevant)

1. **`prefixDefaultLocale: true` + Task 3.5 redirect interaction**. Phase 3.5 adds `/` → `/zh/` redirect. Astro will then route `/zh/`, `/en/`, `/ja/`. But Phase 4 onward needs to verify deep links to `/zh/guide/...` work; the i18n routing config (`astro.config.mjs`) may need adjustment if pages don't get auto-prefixed.
2. **Smoke probe gate**. After Phase 3.5 redirect lands and unblocks root URL, run a smoke build (`npm run build`) and visit `/` in browser to confirm redirect works. Phase 2 closure already verified Tailwind + fonts work end-to-end; Phase 3 closure should re-verify i18n routing actually serves correct lang content.
3. **`@vitejs/plugin-react ^5` ceiling** — current pin is `^5.2.0`. If a future Astro upgrade re-bumps Vite or the plugin needs v6 features, revisit. Document the pin reason in commit body (already done in `4fd216a`) for future readers.
4. **Phase 2 deferred minors §1 + §4 above** — likely surface in Phase 3 visual review. Address opportunistically.

## Execution mode

Same as Phases 1-2: `superpowers:subagent-driven-development` skill. Each task = 1 implementer subagent + spec + quality reviews (or direct-verify for trivial tasks like 3.5).

For 3.3 / 3.4 (TDD with real tests): the implementer should follow `superpowers:test-driven-development` — write failing tests first, then implement.

**End-of-Phase-3 gate**: dispatch a final integration reviewer (`superpowers:code-reviewer`) for the entire Phase 3 commit chain, AND run a smoke probe (build + visit root in browser via dev server, confirm `/` redirects to `/zh/` and a Phase-4-style guide page renders). Don't repeat Phase 2's mistake of declaring done based on per-task structural PASS.

Sonnet model usually suffices. Bump to opus for any task where the implementer hits real architectural choices (e.g., 3.1 if the cross-boundary glob path resolution gets tricky).

## How the new session should start

Read this handoff file FIRST, then read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` Phase 3 section (lines 938-1301). Skip Phases 0 + 1 + 2 (done). Then dispatch Task 3.1 implementer.

Do NOT match the SDTM-compare project's `CLAUDE.md` "Multi-Session Parallel Protocol" routing patterns (those are for batch-38/39/40 verification work — `.work/06_deep_verification/multi_session/`). The website work goes through `superpowers:subagent-driven-development` skill executing the plan.

If you discover plan inconsistencies (like Phase 2.3's `NEXT` table vs test mismatch), **escalate to Daisy with concrete options** — don't guess. The Phase 2 Option B path (keep test verbatim, rewrite impl) was the right call but only because Daisy chose; in different cases Option A or C might be better.

If a per-task review passes but you suspect the system isn't actually wired together (no real route consumes the new code), **add a smoke probe step** before declaring done. Phase 2's lesson: structural PASS ≠ semantic PASS.
