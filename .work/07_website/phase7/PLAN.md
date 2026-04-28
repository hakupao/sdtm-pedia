# Website Phase 7 — Pre-Public-Release Bundle (Tier 3 plan trace)

> **Date opened**: 2026-04-29
> **Master plan**: `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` §"Phase 7 — Search (Pagefind)" lines 2483+
> **Predecessor handoff**: `.work/meta/website_phase6_to_phase7_handoff_2026-04-28.md`
> **Branch**: `main` (HEAD = `e1737f1` post Phase 6 close + index sync; production live at `https://sdtm-pedia.pages.dev/`)

## Scope

Bundle 3 Phase 6 carryovers (C-P6-1 compare i18n chrome + C-P6-3 canonical site-wide + C-P6-8 build:fresh + web/README) as Phase 7 entry, prefaced by C-P5-M3 CF Pages preview verification. All four are public-release prerequisites: distribution-readiness (canonical SEO, i18n parity, contributor docs, hosting smoke-test) before adding more user-facing surface (Pagefind in §7.1/7.2).

## ⚠️ Plan deviation flag

Master plan §"Phase 7" specifies **Search (Pagefind)** as Phase 7 scope (line 2483 + Task 7.1/7.2). **REJECT this for this Phase 7**. Reasons:

1. Phase 6 reviewer surfaced **8 carryovers C-P6-1..8** explicitly framed as "before public release". Pagefind is additive UX; canonical/i18n/CF-preview are distribution gates.
2. Phase 6 close metric: **27 build pages green**, but `<link rel="canonical">` is missing on every route + compare page chrome is hardcoded English on `/zh/compare` and `/ja/compare`. Both visible to first-touch users.
3. C-P5-M3 CF Pages preview deploy was committed as a Phase 6 verify-during item in PLAN.md but never executed (handoff §"Inherited build noise" + reviewer report). Cheap to verify now; risk grows the more pages land.
4. Master-plan §"Phase 7" is renumbered to **Phase 8 (deferred)** under this deviation. Pagefind moves down one slot; current Phase 8 (Downloads Pipeline) and Phase 9 (Deploy) shift to Phase 9/10. Updates to master plan deferred to Phase 7 close.

**Override**: Phase 7 = release-readiness bundle (4 tasks). Pagefind work re-numbered to subsequent phase, planned in next handoff.

## Pre-flight decisions acked at session start (2026-04-29)

1. **CF Pages preview verify first** — Y. C-P5-M3 trailing-slash hosting smoke-test before adding more pages.
2. **Bundle C-P6-1 + C-P6-3 + C-P6-8 as Phase 7 entry, defer master plan §"Phase 7" Pagefind** — Y. Plan deviation flag above.
3. **Reviewer slot = `superpowers:code-reviewer`** — Y. 3rd-family inaugural (after pr-review-toolkit ×4 + feature-dev ×1 + oh-my-claudecode ×1).

## Fact correction noted at session start

Handoff G-P6-3 + C-P6-8 say "no `web/README.md`". Actual: `web/README.md` exists (43 lines) but contains the default Astro starter template ("Astro Starter Kit: Minimal" boilerplate, never customized). C-P6-8 deliverable = **replace placeholder** (not create new). Same scope, accurate framing.

## Task breakdown

| Task | Mode | Spec | Owner |
|---|---|---|---|
| 7.0 — CF Pages preview verify (C-P5-M3) | direct (verification only) | live-site smoke + trailing-slash audit | main session |
| 7.1 — Compare page i18n chrome (C-P6-1) | direct (mechanical) | 4 keys × 3 langs in `ui.{zh,en,ja}.json` + plumb into `[lang]/compare.astro` + `CompareFilter.tsx` | main session |
| 7.2 — Site-wide `<link rel="canonical">` (C-P6-3) | direct (1 file) | edit `BaseLayout.astro` to emit canonical via `Astro.url.pathname` + `Astro.site` | main session |
| 7.3 — `build:fresh` script + `web/README.md` content (C-P6-8) | direct (2 files) | `package.json` script + replace placeholder README with project content (dev/build/test + tribal knowledge) | main session |
| 7.4 (gate) — End-of-Phase-7 reviewer | reviewer subagent | full Phase 7 commit range | `superpowers:code-reviewer` (recommended; 3rd-family inaugural) |

## Task 7.0 detail (C-P5-M3 CF preview verification)

**Goal**: confirm `https://sdtm-pedia.pages.dev/` serves all 27 build pages correctly with `build.format: 'directory'` + sidebar/CTA `/foo` (no slash) hrefs. Catches trailing-slash regressions before more pages land.

**Probes**:
- `curl -sI https://sdtm-pedia.pages.dev/zh/compare` (no trailing slash) — expect 308 redirect to `/zh/compare/` OR direct 200
- `curl -sI https://sdtm-pedia.pages.dev/zh/compare/` — expect 200
- Same probe for: `/zh/`, `/zh/guide/`, `/zh/guide/user-guide/`, `/zh/guide/platform-comparison/`, `/zh/changelog/`, `/zh/guide/readme/` (post Phase 6.4 routes)
- Same probe for `/en/*` and `/ja/*` variants (sample, not exhaustive)
- Probe `/zh/guide/changelog/` — expect 404 (Phase 6.4 H1 fix dropped this catchall variant)
- Probe `/zh/guide/changelog` — expect 404 too (no redirect either)

**Verification**:
- Build green-equivalent on production
- No 5xx on any `[lang]/` route
- `Location` header on 308 redirects sticks within `/[lang]/` (no cross-lang redirect anomaly)
- `/zh/guide/changelog/` 404s cleanly (proves H1 fix landed in production)

**Evidence**: `.work/07_website/phase7/evidence/checkpoints/task_7_0_report.md` — curl matrix + verdicts

**No commit** (verification-only). Findings + verdicts feed into 7.1+ planning OR generate new C-P7-* if regressions surface.

## Task 7.1 detail (C-P6-1 compare i18n chrome)

**Files**:
- Modify: `web/src/i18n/ui.zh.json` — append 4 keys
- Modify: `web/src/i18n/ui.en.json` — append 4 keys (parity)
- Modify: `web/src/i18n/ui.ja.json` — append 4 keys (parity)
- Modify: `web/src/pages/[lang]/compare.astro` — replace hardcoded h1 + subhead with `getUIStrings(lang)['compare.title']` + `['compare.subhead']`; pass `BaseLayout title={...}` from same key
- Modify: `web/src/components/react/CompareFilter.tsx` — accept new prop `t: { placeholder: string; label: string }` (or take `lang` and call `getUIStrings(lang)` directly — but island = client side, simpler to pass strings as props from server)
- Modify: `web/src/components/react/CompareFilter.test.tsx` — pass test fixtures for new props

**4 keys + translations**:

| Key | zh | en | ja |
|---|---|---|---|
| `compare.title` | 多维平台对比 | Multi-dimensional Comparison | 多次元比較 |
| `compare.subhead` | 四平台横向对比. 按维度关键字过滤. | Side-by-side across 4 platforms. Filter by dimension keyword. | 4 プラットフォーム横並び. 次元キーワードで絞り込み. |
| `compare.filter.placeholder` | 过滤维度... | Filter dimensions... | 次元を絞り込み... |
| `compare.filter.label` | 过滤维度 | Filter dimensions | 次元を絞り込む |

(Translations: zh from main session; en literal-preserves Phase 6 originals; ja conservative — `多次元比較` matches scientific JP usage, not `マルチディメンショナル`. If Daisy's JP ear prefers different phrasing, swap during 7.1 or as a polish pass.)

**Verification**:
- `npx tsc --noEmit` 0 errors
- `npm test -- --run` 31/31 (CompareFilter tests use new prop fixtures, helpers.test.ts key-parity passes — 4 new keys × 3 langs = 12 entries, all parity)
- `npm run build:fresh` green (use 7.3's new script if landed first; else `rm -rf .astro && npm run build`)
- Manual verify: `/zh/compare` shows "多维平台对比" h1, ja shows "多次元比較" h1, en unchanged

**Commit**:
```bash
git commit -m "07 Website Phase 7.1 — compare page i18n chrome (4 keys × 3 langs, C-P6-1 absorbed)"
```

## Task 7.2 detail (C-P6-3 canonical site-wide)

**Files**:
- Modify: `web/src/layouts/BaseLayout.astro` — emit `<link rel="canonical">` from `Astro.url.pathname` + `Astro.site`
- Possibly modify: `web/astro.config.mjs` — confirm `site:` is set (required for `Astro.site` to populate). If unset, set to `https://sdtm-pedia.pages.dev`.

**Spec**:
```astro
---
const canonicalHref = Astro.site
  ? new URL(Astro.url.pathname, Astro.site).href
  : Astro.url.pathname;  // fallback to pathname-only if site config missing
---
...
<head>
  ...
  <link rel="canonical" href={canonicalHref} />
</head>
```

**Verification**:
- `npm run build:fresh` green
- `grep -r 'rel="canonical"' dist/zh/compare/index.html` returns one match
- `grep -r 'rel="canonical"' dist/en/changelog/index.html` returns one match
- Spot-check 3 dist pages: each has one canonical pointing to its own URL with trailing slash matching `build.format: 'directory'`
- e2e 6/6 still green

**Commit**:
```bash
git commit -m "07 Website Phase 7.2 — site-wide canonical link via BaseLayout (C-P6-3 absorbed)"
```

## Task 7.3 detail (C-P6-8 build:fresh + README)

**Files**:
- Modify: `web/package.json` — add `"build:fresh": "rm -rf .astro node_modules/.astro dist && npm run build"` to scripts
- Modify: `web/README.md` — replace Astro starter boilerplate with project content

**README content outline** (~80-120 lines):
- Project tagline (1 line)
- Stack (Astro 6 + React 19 + Tailwind 4 + Vitest 4 + Playwright)
- `npm run dev` / `npm run build` / `npm run build:fresh` / `npm test` / `npm run test:e2e`
- Tribal knowledge box:
  - Cache invalidation: when editing `remark-md-link-rewrite.mjs` or any markdown processor, run `npm run build:fresh` (Astro content cache holds AST)
  - Stale dev server: `playwright.config.ts` has `reuseExistingServer: true`. If e2e returns confusing results, `lsof -ti:4321 | xargs kill` first
  - i18n is path-based (`prefixDefaultLocale: true`). All routes are `/[lang]/...`. Lang-neutral entry pages (e.g. `DEMO_QUESTIONS.md` no `.lang` suffix) require `lang:` frontmatter omitted; remark plugin throws if a lang-neutral entry has `.md` cross-refs (intentional fail-loud)
  - Adding a new doc: drop `*.md` (or `*.{zh,en,ja}.md`) into `ai_platforms/release/v1.0/`, ensure `slug:` frontmatter is set; catchall route `/[lang]/guide/[...slug]/` picks it up automatically

**Verification**:
- `npm run build:fresh` green (script works)
- `cat web/README.md | head -1` returns project header (not "Astro Starter Kit: Minimal")
- No edits leak outside `web/`

**Commit**:
```bash
git commit -m "07 Website Phase 7.3 — build:fresh script + replace web/README.md placeholder with project content (C-P6-8 absorbed)"
```

## Task 7.4 detail (reviewer pass)

**Reviewer**: `superpowers:code-reviewer` — 3rd-family inaugural (cross-family from pr-review-toolkit ×4 + feature-dev ×1 + oh-my-claudecode ×1).

**Brief**: structured per Phase 6 R-P6-1 lesson — explicit dimensions to stress (i18n key parity D1, canonical URL correctness D2, README content-vs-tribal-knowledge accuracy D3, CF preview findings completeness D4, plan-deviation justification soundness D5). Adversarial framing per Phase 6 R-P6-5 + D-P6-4 (release readiness = pseudo-infrastructure phase, deserves adversarial mode).

**Pass criteria**:
- All Phase 7 commits diffed against PLAN.md
- 0 HIGH findings OR all HIGH fixed in 7.5 fix bundle
- M-level findings deferred OK (carryover IDs C-P7-*)

**Evidence**: `.work/07_website/phase7/evidence/checkpoints/phase_7_reviewer_report.md`

## Reviewer slot pre-allocation (Rule D)

Reviewer family hot list post Phase 6:
- Phase 1, 2, 3.6, 4: `pr-review-toolkit:code-reviewer` (×4)
- Phase 5: `feature-dev:code-reviewer`
- Phase 6: `oh-my-claudecode:critic`

**Phase 7 reviewer slot = `superpowers:code-reviewer`** — cross-family (3rd inaugural family on website lane). Backup if dispatched: `pr-review-toolkit:silent-failure-hunter` or `oh-my-claudecode:code-reviewer`.

## Evidence layout

```
.work/07_website/phase7/
├── PLAN.md                              ← this file
├── _progress.json                       ← step verdicts
├── evidence/
│   ├── checkpoints/
│   │   ├── task_7_0_report.md
│   │   ├── task_7_1_report.md
│   │   ├── task_7_2_report.md
│   │   ├── task_7_3_report.md
│   │   └── phase_7_reviewer_report.md
│   └── failures/                        ← Rule B: archived not deleted
└── subagent_prompts/                    ← Rule C support (reviewer prompt only this phase, 7.0-7.3 are direct)
```

## Carryover from Phase 6 to Phase 7 (status mapping)

| ID | Description | Status |
|---|---|---|
| C-P6-1 | Hardcoded English UI chrome on `/[lang]/compare` | **absorbed into Task 7.1** |
| C-P6-2 | Color-only winner signaling WCAG 1.4.1 | DEFER — split into Phase 8 carryover or polish (not blocking release) |
| C-P6-3 | Missing site-wide `<link rel="canonical">` | **absorbed into Task 7.2** |
| C-P6-4 | playwright `reuseExistingServer: true` foot-gun | DEFER — covered by README tribal-knowledge box in 7.3, no code change |
| C-P6-5 | platform-comparison vs compare route redundancy | DEFER — design decision, not mechanical |
| C-P6-6 | No vitest for plugin lang-neutral throw guard | DEFER — fixture test, low ROI relative to release readiness |
| C-P6-7 | No schema validation on compare-dimensions.json | DEFER — defensive; would reject malformed entry but no current breakage |
| C-P6-8 | Astro content-cache invalidation undocumented | **absorbed into Task 7.3** (build:fresh script + README tribal-knowledge box) |
| C-P5-M3 | TopNav trailing-slash hosting | **absorbed into Task 7.0** (CF preview verify) |
| C-P5-M2 | DocsSidebar drawer ViewTransitions | DEFER (no VT enabled) |
| C-P5-L1 | Fallback banner i18n | RESOLVED transitively if 7.1 covers fallback banner key — verify during 7.1 |
| C-P5-L2 | Empty TOC `<aside>` guard | DEFER cosmetic |

## Exit criteria

1. tsc 0 errors
2. vitest ≥ 31 (key parity tests cover 4 new keys × 3 langs automatically)
3. e2e 6/6 still green
4. `npm run build:fresh` green; canonical present on every dist HTML; compare page i18n on `/zh/compare` + `/ja/compare`
5. CF Pages preview verification (Task 7.0) report shows 0 hosting regressions OR all regressions tracked as C-P7-*
6. `superpowers:code-reviewer` reviewer verdict ≥ CONDITIONAL_PASS, all HIGH fixed
7. Phase 7 → Phase 8 handoff doc at `.work/meta/website_phase7_to_phase8_handoff_*.md`
8. Master plan annotated with Phase-7-renumbered-Pagefind-to-Phase-8 deviation note (deferred to Phase 7 close)

## Rule A semantic spot-check

Phase 7 has 3 lang JP/ZH translations of 4 i18n keys (12 strings total). Per Rule A: 12 strings is N=12 sample, 0 compression but ~75% rewrite (English source → ZH/JA targets). Apply N=3 spot-check post-7.1: random pick 3 of 12 translated strings, verify (a) accurate semantic transfer, (b) no SDTM term drift (none expected since these are UI chrome not domain content), (c) tone matches existing ui.zh.json / ui.ja.json voice. Evidence in `task_7_1_report.md` § "Rule A spot-check".

## Rule B / C / D applied

- **B**: failed attempts archive in `evidence/failures/` (none expected for verification + mechanical i18n work).
- **C**: retro at Phase 7 close = handoff doc.
- **D**: writer = main session; reviewer = `superpowers:code-reviewer` (different family + different process). All 4 Phase 7 tasks done direct in main session per Phase 6 D-P6 precedent for trivial-mechanical work; no subagent dispatch except reviewer.

## How a fresh session should start Phase 7

1. Read `.work/meta/website_phase6_to_phase7_handoff_2026-04-28.md` (predecessor retro).
2. Read this PLAN.md.
3. Read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` lines 2483+ for the master plan §"Phase 7" content (Pagefind), then ack plan deviation above (Phase 7 = release bundle, Pagefind moves to Phase 8).
4. Confirm 3 entry decisions:
   a. CF Pages preview verify first (Task 7.0) — Y/N
   b. Bundle C-P6-1 + C-P6-3 + C-P6-8 + C-P5-M3 as Phase 7 (defer Pagefind to Phase 8) — Y/N
   c. Reviewer slot = `superpowers:code-reviewer` — Y/N
5. Execute tasks 7.0 → 7.1 → 7.2 → 7.3 → 7.4 with TaskCreate/TaskUpdate or _progress.json tracking.
6. Phase 7 close: handoff doc + index sync (CLAUDE.md Key Paths + MANIFEST + worklog + PROGRESS.md) + commit + push.
