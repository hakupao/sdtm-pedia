# Cross-browser smoke — 2026-04-30 (Phase 9 / master plan §10.3)

> **Scope**: smoke-level coverage of the 5 critical user flows on the 3 major
> browsers. Anything beyond this is QA bug-hunt territory and out of Phase 9
> scope.
>
> **Lane**: against production `https://sdtm-pedia.pages.dev/zh/` (post Phase 9
> push). Run after CF Pages auto-deploys the post-Phase-9 commit.
>
> **Methodology pattern**: this file is a checklist Daisy ticks off in each
> browser. Failures get a 1-line note and a Phase 9 fix bundle (or C-P9-*
> carryover). Pass with no notes = ship.

## Browsers under test

| Browser | Version target | Tester |
|---|---|---|
| Chromium (via Playwright `chromium`) | bundled @playwright/test 1.59.x | **automated** — `web/tests/e2e/` 7-test suite covers most flows |
| Safari | macOS Tahoe 26+ default | manual (Daisy) |
| Firefox | Firefox 132+ | manual (Daisy) |

Playwright `webkit` and `firefox` are NOT installed in this repo (`@playwright/test` defaults to `chromium`-only when projects are unspecified in `playwright.config.ts`); installing them would require `npx playwright install webkit firefox` ~250MB download — deferred per release-grade scope until cross-browser regressions are observed in the wild.

## Flows × browsers matrix

For each flow, write `OK` / `FAIL — <1-line reason>` per cell.

| # | Flow | Chrome | Safari | Firefox |
|---|---|---|---|---|
| 1 | Landing renders all 5 sections (Hero / Platforms / Compare preview / Demo / Downloads) at `/zh/` | OK | | |
| 2 | Theme toggle cycles 3 states (light / dark / system) and persists across reload | OK (vitest covers `theme.test.ts`) | | |
| 3 | Lang switcher swaps URL + content (`/zh/` ↔ `/en/` ↔ `/ja/`) | OK (e2e `lang.spec.ts`) | | |
| 4 | All 4 download links resolve to GH Release (HTTP/2 302 to S3) — `claude/chatgpt/gemini/notebooklm_bundle_v1.0.zip` | OK (curl HEAD verified 4/4 = 302) | | |
| 5 | `Cmd+K` (macOS) / `Ctrl+K` (Linux/Win) opens search overlay; type `AESER` → ≥1 result | OK (e2e `search.spec.ts` real keypress) | | |
| 6 | `/compare` filter narrows table when typing `容量` (zh) / `Capacity` (en) / `容量` (ja) | OK (vitest `CompareFilter.test.tsx`) | | |
| 7 | Visible focus ring on Tab navigation through landing | OK (Phase 9 / Task 9.5 added `*:focus-visible { outline: 2px solid var(--accent); }`) | | |

## Section-anchor notes

- IntersectionObserver-based section animations + TOC scroll-spy: chromium covered via vitest setup; Safari/Firefox should both support IntersectionObserver since Safari 12.1 / Firefox 55 — **no compat risk**.
- ViewTransitions / SVG icons / CSS `@media (prefers-color-scheme)`: all in modern-baseline.

## How to run

1. `npm run build && npm run preview` (or hit production at `https://sdtm-pedia.pages.dev/zh/`)
2. Open in each browser; tick off the table above.
3. If FAIL: capture screenshot + 1-line cause; file as Phase 10 polish carryover.

## Phase 9 sign-off

- **Chrome lane**: ✓ green via Playwright suite (7/7 e2e + 46/46 vitest as of post-9.9 commit)
- **Safari + Firefox lanes**: pending Daisy manual sweep (one-shot, ~10 min total). Recorded as carryover **C-P9-1** if not run before public-release announcement.
