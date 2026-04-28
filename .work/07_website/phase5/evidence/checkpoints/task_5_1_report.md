# Task 5.1 — DocsLayout + 3 components — checkpoint report

**Date**: 2026-04-28
**Subagent**: `oh-my-claudecode:executor` (opus), agentId `af6be6191ad2e5537`
**Plan**: §5.1 lines 2012-2155
**Status**: PASS

## Files created (verbatim from plan)

| File | Lines |
|---|---|
| `web/src/components/astro/DocsSidebar.astro` | 32 |
| `web/src/components/astro/DocsTOC.astro` | 33 |
| `web/src/components/astro/PrevNextNav.astro` | 23 |
| `web/src/layouts/DocsLayout.astro` | 22 |
| **Total** | **110 insertions** |

## Verification

- **tsc**: `npx tsc --noEmit` → 0 errors
- **vitest**: `npm test -- --run` → 7 files / **29/29 passed** (existing baseline preserved)
- **build**: `npm run build` → 3 lang landing pages emitted, pagefind indexed 3 langs / 3 pages / 540 words, finished cleanly. New components are unused leaves until Task 5.3 wires the catchall route.

## Commit

`496ae6f36bc7e1e58b37118cf60dccaff2b2e4df`
> 07 Website Phase 5.1 — DocsLayout 3-col + Sidebar (mobile drawer) + TOC scroll-spy + PrevNext

## Divergence

None. All 4 existing patterns probed by the main session before dispatch (Lang type import, BaseLayout/TopNav prop shapes, content collection schema, Tailwind class set) matched plan code expectations exactly.

## Notes for Task 5.3

- Components are runtime-untested — they only execute when the catchall route renders a doc page. Task 5.3 e2e (`docs reader renders user-guide in zh`) will be the first execution.
- `getCollection('guide', filter)` returns objects with `data.slug` populated only if the markdown file's frontmatter has `slug:`; the catchall must derive slug from `entry.id` if `data.slug` missing. All 12 existing release v1.0 docs have explicit `slug:` so this is not an immediate risk, but worth noting.
- `DocsSidebar` filters by `lang`, but `DEMO_QUESTIONS.md` no longer has `lang:` (decision 2). The sidebar will NOT show DEMO_QUESTIONS in any lang's sidebar with the current filter `(e) => e.data.lang === lang`. Task 5.3 must either (a) include lang-undefined entries in all sidebars, or (b) accept that DEMO_QUESTIONS is reachable only via TopNav/HeroSection CTAs, not via sidebar. **Decision needed in Task 5.3.**
