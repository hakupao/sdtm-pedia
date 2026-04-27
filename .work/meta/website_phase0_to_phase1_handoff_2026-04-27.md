# Website Build — Phase 0 → Phase 1 Handoff

> **Date**: 2026-04-27
> **Outgoing session**: completed Phase 0 (5 tasks, content + assets)
> **Incoming session**: should start Phase 1 (Astro scaffolding, 7 tasks)

## What's done

- **Spec**: `docs/superpowers/specs/2026-04-27-sdtm-release-website-design.md` (committed `33788a8`)
- **Plan**: `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` (committed `81b7eb2`, 3056 lines, 11 phases ~50 tasks)
- **Phase 0 complete** — 6 commits on main, 8 ahead of origin/main:
  | Task | Status | File | Commits |
  |---|---|---|---|
  | 0.1 PLATFORM_COMPARISON.zh.md | ✅ | `ai_platforms/release/v1.0/PLATFORM_COMPARISON.zh.md` 94 lines | `a14d414` + `0e745db` |
  | 0.2 PLATFORM_COMPARISON.en.md | ✅ | `ai_platforms/release/v1.0/PLATFORM_COMPARISON.en.md` 94 lines | `8e79d21` + `53341f0` |
  | 0.3 PLATFORM_COMPARISON.ja.md | ✅ | `ai_platforms/release/v1.0/PLATFORM_COMPARISON.ja.md` 94 lines | `31b80d1` + `03b800c` |
  | 0.4 favicon.svg | ✅ | `assets/favicon.svg` 329 bytes (cobalt + serif italic S) | uncommitted (defer to 1.5) |
  | 0.5 og-default.png | ✅ | `assets/og-default.png` 1200×630 RGBA 54KB | uncommitted (defer to 1.5) |

## Working state

- **Branch**: `main`
- **Untracked**: `assets/` (favicon.svg + og-default.png — staying there until Task 1.5 moves them to `web/public/`)
- **Untracked also**: `package.json` + `node_modules/` (created by Phase 0.5 sharp install — root `node_modules/` and `package-lock.json` already in `.gitignore`)
- **Push status**: 8 commits ahead of `origin/main`. **Push status TBD by user** — see resume prompt below.

## What's next (Phase 1, 7 tasks)

Per plan §"Phase 1 — Astro Scaffolding":
- 1.1 `npm create astro@latest web -- --template minimal --no-install --no-git --typescript strict`
- 1.2 install deps (Astro + React + Tailwind v4 + @fontsource/* + Vitest + Playwright + Pagefind, ~30 packages)
- 1.3 configure `astro.config.mjs` with i18n (zh default) + react + tailwind + sitemap
- 1.4 Tailwind v4 config + postcss
- 1.5 dir scaffold + move `assets/favicon.svg` + `assets/og-default.png` → `web/public/` + add `web/public/robots.txt` + commit
- 1.6 Vitest config + npm scripts (dev/build/test/test:e2e)
- 1.7 Playwright config + chromium install (`npx playwright install --with-deps chromium` will download ~150MB)

**Phase 1 takes ~30-45 min. Heavy ops**: `npm install` (2-5 min), Playwright Chromium download (large).

## Execution mode

User chose **subagent-driven-development** (each task = 1 implementer subagent + 1 spec reviewer + 1 quality reviewer per skill `superpowers:subagent-driven-development`).

For mechanical Phase 1 tasks: sonnet/haiku models suffice. Reviews can be quick combined passes (these are config files, not domain content).

## Known non-blocking observations from Phase 0

- OG image used librsvg fallback fonts (DejaVu Serif, system mono — Playfair Display + JetBrains Mono not installed system-wide). Visual still editorial. Can re-render in Docker / @vercel/og post-v1.0 if pixel-perfect typography matters.
- §3 NotebookLM "审核" cell wording is slightly inconsistent with ChatGPT row (NBLM says "不适用 (内部直接邀请)", CG says "仅 Store 发布需审核"). Acceptable, not flagged for fix.

## How the new session should start

Read this handoff file FIRST, then read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` Phase 1 section. Skip Phase 0 (done). Then dispatch Task 1.1 implementer.

Do NOT match the SDTM-compare project's `CLAUDE.md` "Multi-Session Parallel Protocol" routing patterns (those are for batch 35/36/37 verification work, NOT this website work). The website work goes through `superpowers:subagent-driven-development` skill executing the plan.
