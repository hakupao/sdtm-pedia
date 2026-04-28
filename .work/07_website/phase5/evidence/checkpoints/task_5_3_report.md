# Task 5.3 — Catchall + lang fallback + /changelog + /compare stub + link-resolution e2e — checkpoint report

**Date**: 2026-04-28
**Subagent**: `oh-my-claudecode:executor` (opus), agentId `a4d79a9b53bab73d3`
**Plan**: §5.3 lines 2207-2308 + 4 augmentations from main session decisions
**Status**: PASS with 1 carryover for Phase 6

## Files (commit 56a18f7)

| File | Action | Lines |
|---|---|---|
| `web/src/pages/[lang]/guide/index.astro` | created | 7 |
| `web/src/pages/[lang]/guide/[...slug].astro` | created | 45 |
| `web/src/pages/[lang]/changelog.astro` | created | 18 |
| `web/src/pages/[lang]/compare.astro` | created (Phase 6 stub) | 19 |
| `web/src/components/astro/DocsSidebar.astro` | modified (filter +lang-undefined) | +1/-1 |
| `web/src/content.config.ts` | **modified — load-bearing fix outside listed 6** | +18 |
| `web/tests/e2e/smoke.spec.ts` | extended (2 new tests) | +30 |

## Augmentations applied

- **A** (lang-neutral fallback): `[...slug].astro` `getStaticPaths` branches on `doc.data.lang === undefined` — emits zh+en+ja paths with `fallback: false` so DEMO_QUESTIONS gets no banner. lang-tagged en→zh/ja still gets banner.
- **B** (sidebar): filter changed to `e.data.lang === lang || e.data.lang === undefined` so DEMO_QUESTIONS appears in every lang's sidebar.
- **C** (compare stub): `web/src/pages/[lang]/compare.astro` returns "PHASE 6 PENDING" placeholder for all 3 langs. Phase 6 overwrites.
- **D** (link-resolution e2e): walks every `<a>` in `main`/`article` of `/zh/`, `/zh/guide/user-guide`, `/zh/changelog`. Skips `#`-only anchors, `mailto:`, external `http(s)://`, AND `*.md` source-file cross-refs (carryover, see below).

## Verification

- **tsc**: `npx tsc --noEmit` → 0 errors
- **vitest**: 7 files / 29 passed (29) — no regression
- **build**: 34 pages green; per-lang `guide/{readme, user-guide, glossary, demo-questions, known-limitations, compare, changelog}/index.html` + `index.html` (meta-refresh redirect) + per-lang `/changelog/index.html` + `/compare/index.html` all emitted
- **e2e**: `npm run test:e2e` → **6/6 passed** (1 prior lang-redirect + 3 prior landing-section + 2 new: docs reader + link-resolution)

## Subagent surprises (worth flagging)

### Surprise 1 — Astro 6 API
Plan code uses `await entry.render()` (Astro 4 collection API). Astro 6 requires `import { render } from 'astro:content'` + `await render(entry)`. Subagent fixed in [...slug].astro and changelog.astro.

### Surprise 2 — Phase 5.1 was committed against a broken collection state
Default `generateId` keys off `data.slug` alone. Multiple per-lang variants share the same `slug` (e.g. `user-guide` exists in en/zh/ja). Default behavior: later items overwrite earlier ones, leaving each slug with ONLY ONE lang variant. Phase 5.1 sidebar filter `e.data.lang === lang` masked this because the surviving variant happened to be the lang being filtered for, but globally the collection was broken.

**Fix in `content.config.ts`**:
1. `generateId: ({ data }) => lang ? \`${lang}-${slug}\` : slug` — composite id per-lang
2. Glob narrowed `**/*.md` → `*.md` to exclude `self_deploy/**` tutorial markdown that lacks slug contract
3. Added `if (!slug) throw new Error(...)` for fail-loud on missing frontmatter

This is a **load-bearing fix** that the listed-6-files constraint did not anticipate. Accept as scope-correct violation: Phase 5.1 verbatim-copy + Phase 5.3 fallback logic CANNOT WORK without this fix. Subagent's choice was right.

### Surprise 3 — slug "compare" collision (resolved naming, no bug)
`PLATFORM_COMPARISON.zh.md` has `slug: compare` so it lands at `/{lang}/guide/compare/`. Phase 6 stub lives at `/{lang}/compare/`. Different paths → no route collision. Both build cleanly. Phase 6 may want to rename PLATFORM_COMPARISON's slug to `platform-comparison` to disambiguate (cosmetic).

### Surprise 4 — Markdown cross-refs are dead
~30+ `[Glossary](GLOSSARY.zh.md)` style raw-markdown-filename cross-refs across README/USER_GUIDE/GLOSSARY in all 3 langs render as `<a href="GLOSSARY.zh.md">` which resolves to `/{lang}/guide/GLOSSARY.zh.md` → 404. Out-of-Phase-5 scope. Link-resolution e2e currently SKIPS hrefs matching `/\.md(?:#|$)/` to avoid false alarms.

## Carryover for Phase 6

- **C-P5-1**: ~30 `*.md` cross-refs in markdown bodies are dead links. Recommended fix in Phase 6 = add a `remark` plugin (e.g. `remark-link-rewrite`) to rewrite `[X](FOO.zh.md)` → `/${currentLang}/guide/foo` (lowercase, drop lang+suffix). Once added, remove the `.md` skip in e2e link-resolution test so it starts enforcing internal markdown integrity.
- **C-P5-2** (cosmetic): Rename PLATFORM_COMPARISON.{zh,en,ja}.md frontmatter `slug: compare` → `slug: platform-comparison` to disambiguate from the Phase 6 `/${lang}/compare/` page route. No functional impact today.
- **C-P5-3** (review): The new collection `generateId` enforces all top-level release docs have a `slug:` frontmatter. If Phase 6+ adds new docs to `ai_platforms/release/v1.0/`, missing `slug:` will throw at build time (intended fail-loud behavior).

## Phase 5.1 retroactive note

Task 5.1 checkpoint reported "PASS" because tsc/vitest/build were green. Build green was misleading: the collection was silently overwriting per-lang variants. Phase 5.1 sidebar would have shown only one lang variant per slug if it had been rendered (it wasn't, because no docs route existed in 5.1). Phase 5.3's content.config.ts fix retroactively repairs this. Lesson worth absorbing into RETROSPECTIVE.md at Phase 5 close.

## Commit
`56a18f7` — 07 Website Phase 5.3 — docs catchall + lang fallback + /changelog + /compare stub + link-resolution e2e (decisions 2+3)
7 files changed, 137 insertions(+), 2 deletions(-)
