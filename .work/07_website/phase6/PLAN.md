# Website Phase 6 — Multi-dim Comparison Page (Tier 3 plan trace)

> **Date opened**: 2026-04-28
> **Master plan**: `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` §"Phase 6" lines 2313-2480
> **Predecessor handoff**: `.work/meta/website_phase5_to_phase6_handoff_2026-04-28.md`
> **Branch**: `main` (HEAD = `3d00a96` post Phase 5 close + 9.1 CF Pages config; production live at `https://sdtm-pedia.pages.dev/zh/`)

## Scope

Replace the Phase 5 `/compare` placeholder with the real multi-dimensional comparison page (9 dims × 4 platforms with search filter), absorb 2 Phase 5 carryovers (C-P5-1 markdown cross-link rewrite + C-P5-2 PLATFORM_COMPARISON slug rename) at Phase 6 entry to clear technical debt before adding new surface.

## ⚠️ Plan deviation flag (must apply during Task 6.1)

Plan §6.1 Step 3 specifies `web/src/pages/compare.astro` (root, no lang prefix) with URL query string `?lang=en` for language detection. **REJECT this**. Reasons:

1. Phase 4 `ComparePreviewSection.astro` links to `/${lang}/compare` (path-based).
2. Phase 5 stub lives at `web/src/pages/[lang]/compare.astro` (path-based).
3. The whole project uses path-based i18n (`astro.config.mjs` `prefixDefaultLocale: true`).
4. Plan-verbatim would break the existing CTA + force a redirect or dead link.

**Override**: overwrite `web/src/pages/[lang]/compare.astro` (same path as the Phase 5 stub) with the real page. Use `Astro.params.lang` (NOT `?lang=`) for language detection, same pattern as `[lang]/changelog.astro`. The `getStaticPaths()` returns `[{lang:'zh'},{lang:'en'},{lang:'ja'}]` like the stub already does.

## Task breakdown

| Task | Mode | Spec | Owner |
|---|---|---|---|
| 6.0 — `.md` cross-ref remark plugin + slug rename + e2e strict | subagent (executor opus) | C-P5-1 + C-P5-2 absorbed | TBD |
| 6.1 — CompareFilter island + overwrite stub `[lang]/compare.astro` | subagent (executor opus) | plan §6.1 lines 2315-2441 + plan deviation above | TBD |
| 6.2 — Expand `compare-dimensions.json` 4 → 9 dims + landing slice(0, 4) | direct (trivial) | plan §6.2 lines 2443-2479 | main session |
| 6.3 (gate) — End-of-Phase-6 reviewer | reviewer subagent | full Phase 6 commit range | `oh-my-claudecode:critic` (recommended) |

## Task 6.0 detail (NEW, carryover absorption)

**Files to create/modify**:
- Create: `web/remark-md-link-rewrite.mjs` (or place in `web/src/lib/`)
- Modify: `web/astro.config.mjs` — register the plugin
- Modify: `ai_platforms/release/v1.0/PLATFORM_COMPARISON.{zh,en,ja}.md` — `slug: compare` → `slug: platform-comparison`
- Modify: `web/tests/e2e/smoke.spec.ts` — remove the `/\.md(?:#|$)/` skip in link-resolution test
- Modify: `web/src/pages/[lang]/guide/[...slug].astro` if any path consumes the old `compare` slug (likely not)

**Plugin spec**:
- Receives a markdown AST link node with `node.url` like `GLOSSARY.zh.md` or `USER_GUIDE.zh.md#section`
- Rewrites `/^([A-Z_]+)(?:\.(zh|en|ja))?\.md(#.*)?$/` → `/${currentLang}/guide/${name.toLowerCase()}${hash || ''}`
- For PLATFORM_COMPARISON specifically (post-rename): name = `platform-comparison` (lowercase, hyphenated)
- For DEMO_QUESTIONS (lang-neutral): same rule applies (slug `demo-questions`)
- Currentlang = the rendering page's lang (passed via remark plugin options or read from frontmatter)
- Skip non-markdown URLs (http/https/mailto, anchors only)

**Verification**:
- `npm run build` green; check a built guide HTML for an `<a href>` matching `/zh/guide/glossary` (rewritten from `GLOSSARY.zh.md`)
- `npm run test:e2e` link-resolution test runs WITHOUT the `.md` skip and still passes (means all 30 cross-refs resolve cleanly)
- `git grep -F 'GLOSSARY.zh.md' ai_platforms/release/v1.0/` to count source occurrences for sanity baseline

**Commit**:
```bash
git commit -m "07 Website Phase 6.0 — remark plugin for .md cross-refs + PLATFORM_COMPARISON slug rename + e2e link-resolution strict (C-P5-1 + C-P5-2 absorbed)"
```

## Task 6.1 detail

**Files**:
- Create: `web/src/components/react/CompareFilter.tsx` (plan lines 2352-2407)
- Create: `web/src/components/react/CompareFilter.test.tsx` (plan lines 2324-2347, 2 vitest)
- **Overwrite** (NOT create): `web/src/pages/[lang]/compare.astro` (was Phase 5 stub; real page now)

**[lang]/compare.astro shape** (per plan deviation):
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import TopNav from '../../components/astro/TopNav.astro';
import { CompareFilter } from '../../components/react/CompareFilter';
import dims from '../../data/compare-dimensions.json';
import { type Lang } from '../../i18n/helpers';
export function getStaticPaths() {
  return [{ params: { lang: 'zh' } }, { params: { lang: 'en' } }, { params: { lang: 'ja' } }];
}
const lang = Astro.params.lang as Lang;
const pathname = Astro.url.pathname;
---
<BaseLayout title="Platform Comparison" lang={lang}>
  <TopNav lang={lang} pathname={pathname} />
  <main class="px-7 py-8 max-w-screen-xl mx-auto">
    <h1 class="font-display text-4xl font-bold mb-2">Multi-dimensional Comparison</h1>
    <p class="font-serif text-ink-mute mb-8">Side-by-side across 4 platforms. Filter by dimension keyword.</p>
    <CompareFilter client:load dims={dims} lang={lang} />
  </main>
</BaseLayout>
```

**Verification**:
- `npx tsc --noEmit` 0 errors
- `npm test -- --run` → 31/31 (was 29 + 2 CompareFilter tests)
- `npm run build` → `dist/{zh,en,ja}/compare/index.html` (real page, not "PHASE 6 PENDING" stub)
- `npm run test:e2e` → 6/6 still passes; manually verify `/zh/compare` shows table not stub

**Commit**:
```bash
git commit -m "07 Website Phase 6.1 — CompareFilter island + /[lang]/compare.astro real page (overwrites Phase 5 stub, path-based i18n per plan deviation)"
```

## Task 6.2 detail (trivial, direct)

Append 5 dims to `web/src/data/compare-dimensions.json` per plan lines 2452-2461 (score / subscription / internet / file-limit / worst-at).

Modify `web/src/components/astro/ComparePreviewSection.astro` to use `dims.slice(0, 4)` so landing keeps its 4-dim preview while `/compare` shows all 9.

**Verification**:
- `npm test -- --run` (existing landing tests should still pass — preview shows 4 dims after slice)
- Manually verify `/zh/compare` shows 9 rows in the table

**Commit**:
```bash
git commit -m "07 Website Phase 6.2 — expand compare-dimensions to 9 dims (preview shows first 4 via slice)"
```

## Reviewer slot pre-allocation (Rule D)

Reviewer family hot list post Phase 5:
- Phase 1, 2, 3.6, 4: `pr-review-toolkit:code-reviewer` (×4)
- Phase 5: `feature-dev:code-reviewer`

**Phase 6 reviewer slot = `oh-my-claudecode:critic`** — cross-family from both, Opus model = deep analysis. Backup if dispatched: `oh-my-claudecode:code-reviewer` or `oh-my-claudecode:verifier`.

## Evidence layout

```
.work/07_website/phase6/
├── PLAN.md                              ← this file
├── _progress.json                       ← step verdicts
├── evidence/
│   ├── checkpoints/
│   │   ├── task_6_0_report.md
│   │   ├── task_6_1_report.md
│   │   ├── task_6_2_report.md
│   │   └── phase_6_reviewer_report.md
│   └── failures/                        ← Rule B: archived not deleted
└── subagent_prompts/                    ← Rule C support
```

## Carryover from Phase 5 to Phase 6 (status mapping)

| ID | Description | Status |
|---|---|---|
| C-P5-1 | `.md` cross-refs need remark plugin | **absorbed into Task 6.0** |
| C-P5-2 | PLATFORM_COMPARISON `slug: compare` rename | **absorbed into Task 6.0** |
| C-P5-M2 | DocsSidebar drawer ViewTransitions | DEFER (no VT enabled) |
| C-P5-M3 | TopNav trailing-slash hosting | **CHECK during Phase 6 deploy smoke** (CF Pages live now, easy to verify) |
| C-P5-L1 | Fallback banner i18n | DEFER to next i18n touch |
| C-P5-L2 | Empty TOC `<aside>` guard | DEFER cosmetic |

## Exit criteria

1. tsc 0 errors
2. vitest ≥ 31 (added 2 for CompareFilter)
3. e2e 6/6 still green AFTER removing `.md` skip in link-resolution
4. build green; per-lang `/compare/index.html` shows real comparison table (NOT stub); per-lang `/guide/platform-comparison/index.html` exists (post-slug-rename)
5. `oh-my-claudecode:critic` reviewer verdict ≥ CONDITIONAL_PASS, all HIGH fixed
6. CF Pages preview deploy from a feature branch passes (verify path-based `/compare` works on real CF infra, catches C-P5-M3)
7. Phase 6 → Phase 7 handoff doc at `.work/meta/website_phase6_to_phase7_handoff_*.md`

## Rule A semantic spot-check

Phase 6 doesn't compress/rewrite content (data is static JSON + plugin is mechanical rewrite). Skip Rule A formal N-sample audit. **BUT** post-Task-6.0 manually spot-check 3 random rewritten links on the live site to confirm the plugin produces the right URLs (e.g., `[Glossary](GLOSSARY.zh.md)` in `USER_GUIDE.zh.md` should render as `<a href="/zh/guide/glossary">`).

## Rule B / C / D applied

- **B**: failed attempts archive in `evidence/failures/`.
- **C**: retro at Phase 6 close = handoff doc.
- **D**: writer = subagent executor; reviewer = `oh-my-claudecode:critic` (different family + different process).

## How a fresh session should start Phase 6

1. Read `.work/meta/website_phase5_to_phase6_handoff_2026-04-28.md` (predecessor retro).
2. Read this PLAN.md.
3. Read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` lines 2313-2480 (master Phase 6 spec).
4. Confirm 3 entry decisions:
   a. Task 6.0 absorbs C-P5-1 + C-P5-2 (recommended) — Y/N
   b. Plan deviation: `[lang]/compare.astro` instead of root `compare.astro` (recommended) — Y/N
   c. Reviewer slot = `oh-my-claudecode:critic` (recommended) — Y/N
5. Execute tasks 6.0 → 6.1 → 6.2 → 6.3 with TaskCreate/TaskUpdate tracking.
6. Post-Phase-6: optional CF Pages preview deploy from feature branch to verify before merge.
