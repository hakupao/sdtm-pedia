# Website Build — Phase 1 → Phase 2 Handoff

> **Date**: 2026-04-27
> **Outgoing session**: completed Phase 1 (7 tasks, Astro scaffolding) + 3 plan-doc commits
> **Incoming session**: should start Phase 2 (Design System, 5 tasks)

## What's done — Phase 1

12 commits landed on `main` and pushed to `origin/main`. Commit chain (oldest → newest):

| Commit | Subject |
|---|---|
| `2c3e9c5` | 07 Website Phase 1.1 — Astro minimal scaffold (web/) |
| `abf2527` | 07 Website Phase 1.2 — install Astro + React + Tailwind v4 + Pagefind + test deps |
| `2d36ac9` | 07 Website Phase 1.2 fixup — switch to @tailwindcss/vite (Astro v6 compat); drop unused PostCSS deps |
| `72bc1c0` | 07 Website plan erratum — Astro v6 + Tailwind v4 use @tailwindcss/vite (Phase 1 §1.2/§1.3/§1.4 + Phase 2 §2.1 directives) |
| `f00fae8` | 07 Website plan nit — pin tailwindcss@^4 (drop @next dist-tag drift risk) |
| `1192725` | 07 Website Phase 1.3 — astro.config: react + tailwind + sitemap + i18n (zh default, prefixDefaultLocale) |
| `26cbfbc` | 07 Website Phase 1.4 — Tailwind v4 CSS entry stub (@import tailwindcss; full theme deferred to §2.1) |
| `9f206ed` | 07 Website Phase 1.5 — dir scaffold + favicon + og-default + robots |
| `222a8dc` | 07 Website Phase 1.6 — Vitest config + npm scripts (dev/build/test/test:e2e) |
| `bfd7d29` | 07 Website plan nit — vitest test script needs --passWithNoTests (Vitest v4 default exits 1 on empty) |
| `083e45a` | 07 Website Phase 1.7 — Playwright config (chromium, reuse dev server) |

(Note: `eda792b` — "06 Deep Verification round 8" — sits between `abf2527` and `2d36ac9`. Unrelated parallel-lane commit; ignore for website-build purposes.)

## Three architectural deviations vs original plan

The original plan was written before testing whether `@astrojs/tailwind` (v3-era) works with Astro 6 + Tailwind v4. It doesn't. The plan was patched mid-Phase-1 (Daisy chose Option A: canonical 2026 path):

1. **`@astrojs/tailwind` → `@tailwindcss/vite`** (Astro 6 peer dep refused legacy integration). Plan §1.2/§1.3/§1.4 + §2.1 directives revised. Vite plugin registered via `vite: { plugins: [tailwindcss()] }` in `astro.config.mjs`. No more `tailwind.config.mjs` or `postcss.config.mjs` — Tailwind v4 is CSS-first.
2. **`tailwindcss@next` → `tailwindcss@^4`** (remove dist-tag drift risk for plan re-runs).
3. **`vitest run` → `vitest run --passWithNoTests`** (Vitest v4 changed default: empty test suite exits 1).

## Working state — Phase 1 complete

- **Branch**: `main`. Pushed to `origin/main` at end of Phase 1 (HEAD = `083e45a` at push time).
- **`web/` tree** is fully scaffolded: Astro 6.1.9, React 19, Tailwind v4 + `@tailwindcss/vite`, Vitest 4, Playwright 1.59 + chromium 1217 cached, sitemap, pagefind, fontsource (8 files imported in §2.1).
- **Smoke-tests passed during Phase 1**: `npm run dev` starts clean (Task 1.3); `npm test` exit 0 with 0 tests (Task 1.6); `npx playwright test --list` semantically reports 0 tests (Task 1.7 — Playwright 1.59 returns exit 1 on empty `--list`, version quirk, self-resolves once Phase 4+ adds specs).
- **Untracked at start of new session**: `.work/06_deep_verification/...` files (parallel batch-35/36/37 verification lane; **do not stage, do not modify** — that's a different work stream). Specifically a fresh `.bak` (`pdf_atoms.jsonl.pre-v1.5-retroactive.bak`) and a modified `pdf_atoms.jsonl` may show — leave alone.

## What's next — Phase 2 (5 tasks)

Per plan §"Phase 2 — Design System" (lines 596–937 in the plan file):

- **2.1 CSS tokens (light/dark)** — overwrite `web/src/styles/global.css` (currently the 2-line stub from Task 1.4) with the full token set: 8 fontsource imports, `@import "tailwindcss";`, light/dark CSS variables (`--bg --bg-alt --ink --ink-mute --ink-faint --accent --rule`), `prefers-color-scheme` fallback, body baseline, reduced-motion guard.
- **2.2 Theme persistence library + tests** — `web/src/lib/theme.ts` + `theme.test.ts`. TDD applies. Functions: `getStoredTheme`, `setStoredTheme`, `applyTheme`, `resolveEffectiveTheme`. localStorage persistence; 'system' default.
- **2.3 Theme toggle React island + tests** — `web/src/components/react/ThemeToggle.tsx` + `.test.tsx`. TDD applies. Three-state toggle (light/dark/system).
- **2.4 SectionLabel ritual component** — `web/src/components/astro/SectionLabel.astro`. Pure visual `.astro`, no tests.
- **2.5 BaseLayout** — `web/src/layouts/BaseLayout.astro`. Imports `../styles/global.css`. Foundation for landing + docs layouts in Phases 3–4.

**Phase 2 takes ~45-60 min.** Heavier than Phase 1 because 2.2 and 2.3 are TDD with real tests. 2.4/2.5 are mechanical visual components.

## Forward-looking concerns from Phase 1 review (non-blocking)

1. **§2.1 may be missing a `@theme inline {}` block for Tailwind utility class generation.** Tailwind v4 needs `@theme inline { --color-bg: var(--bg); ... }` for utility classes like `bg-bg`, `text-ink` to exist. The plan §2.1 only defines `:root` CSS variables, not the `@theme` block. **If Phase 2.5 BaseLayout (or later phases) actually use `bg-bg`/`text-ink`/`border-rule` Tailwind utilities, §2.1 needs an `@theme inline {}` mapping**. Verify when implementing 2.1; if utilities aren't used (raw `var(--bg)` everywhere), no patch needed.
2. **`prefixDefaultLocale: true` means `/` 404s** until Phase 4 adds `src/pages/index.astro` (root → `/zh/` redirect). Phase 2 doesn't yet add E2E tests that hit `/`, so non-blocking now.
3. **`site: 'https://sdtm-pedia.pages.dev'` in `astro.config.mjs` is a placeholder.** Phase 9 swaps for custom domain; sitemap embeds it from Phase 7 onward.

## Execution mode

Same as Phase 1: `superpowers:subagent-driven-development` skill. Each task = 1 implementer subagent + spec + quality reviews (or direct-verify for 1-3-line trivial tasks).

For 2.2 / 2.3 (TDD with real tests): the implementer should follow `superpowers:test-driven-development` — write failing tests first, then implement, then green.

Sonnet model usually suffices. Bump to opus for any task where the implementer hits real architectural choices.

## How the new session should start

Read this handoff file FIRST, then read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` Phase 2 section (lines 596–937). Skip Phases 0 + 1 (done). Then dispatch Task 2.1 implementer.

Do NOT match the SDTM-compare project's `CLAUDE.md` "Multi-Session Parallel Protocol" routing patterns (those are for batch 35/36/37 verification work — `.work/06_deep_verification/multi_session/`). The website work goes through `superpowers:subagent-driven-development` skill executing the plan.
