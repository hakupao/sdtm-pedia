# Phase 9 reviewer report — `feature-dev:code-architect` (Task 9.13)

> **Subagent**: `feature-dev:code-architect` (2nd-burn feature-dev family — NEW agent vs Phase 5 `feature-dev:code-reviewer`; cross-family from Phase 8 `pr-review-toolkit:silent-failure-hunter`)
> **Commit reviewed**: `e89da8a` (Phase 9.1-9.12 polish bundle, 21 files / +8491/-55 LOC)
> **Brief**: `.work/07_website/phase9/subagent_prompts/task_9_13_reviewer_prompt.md`
> **Stress dims applied**: D1-D7 (e2e infrastructure / SearchOverlay a11y / plugin fixture / zod schema / redirect HTML / focus-visible CSS / archeology + scope)
> **Verdict**: **CONDITIONAL_PASS** → upgrades to PASS post 9.14 fix bundle

## Reviewer verdict

**CONDITIONAL_PASS**: H=1 / M=4 / L=4 = 9 findings. F-1 HIGH is fixable in ~2 LOC; per pass criteria triggers CONDITIONAL_PASS with mandatory 9.14 fix bundle. F-3 + F-4 recommended as same-phase cheap fixes (co-located edits). F-2 + F-5 borderline (F-5 pending `Astro.site` verification by writer). F-6/F-7/F-8/F-9 = LOW carryover.

## Findings

### F-1 [HIGH] — English "1 results" pluralization bug in aria live region
- **Where**: `web/src/i18n/ui.en.json:21` + `web/src/components/react/SearchOverlay.tsx:97`
- **What**: live region message `\`${results.length} ${t['search.results.label']}\`` produces "1 results" for single-result English queries. zh ("个结果") + ja ("件の結果") are count-neutral suffixes, correct as-is. Only English fails.
- **Why it matters**: aria-live read aloud verbatim by screen readers; "1 results found" common real-world outcome for specific SDTM variable queries (e.g. "AESER" → 1-2 hits).
- **Fix path**: same-phase ~2 LOC inline conditional in SearchOverlay.tsx.

### F-2 [MEDIUM] — Escape branch reads stale `open` closure (correctness fine, design smell)
- **Where**: `SearchOverlay.tsx:27-36`
- **What**: Escape handler fires `setOpen(false)` even when `open` already false (no-op re-render). The 'race' the brief asks about resolves correctly because `previousFocusRef` is a synchronous ref, not state. Code is correct by accident — concern is design clarity.
- **Why it matters**: low correctness impact. Test fidelity gap: jsdom `fireEvent.keyDown` fires synchronously and skips the React batching path. Production risk minimal.
- **Fix path**: carryover C-P9-10 (non-trivial refactor — `open` is stale closure inside listener; would require ref-tracking to guard).

### F-3 [MEDIUM] — Plugin fixture lacks CHANGELOG hash-preservation case
- **Where**: `web/remark-md-link-rewrite.test.mjs:36-41` + plugin `web/remark-md-link-rewrite.mjs:60-62`
- **What**: 6 fixtures cover non-CHANGELOG hash preservation (`USER_GUIDE.md#install` → `/ja/guide/user-guide#install`) but not the CHANGELOG branch. If `${hash}` interpolation ever drops on the changelog path, no test catches it.
- **Why it matters**: changelog files conventionally have per-version anchors (`CHANGELOG.md#v1.0`); silent dropping would 404-style anchor navigation.
- **Fix path**: same-phase ~6 LOC (1 new fixture). Vitest 46 → 47.

### F-4 [MEDIUM] — `DimensionsSchema.values` allows any string key (typo-blind)
- **Where**: `web/src/data/schemas.ts:33`
- **What**: `z.record(z.string(), z.string())` permits `"cladue"` (typo) silently. `DownloadsSchema.platform` already uses `z.enum([...])`; values should match.
- **Why it matters**: typo in `compare-dimensions.json` values key passes schema validation, renders blank table cell on live site, no test failure.
- **Fix path**: same-phase ~3 LOC; tighten to `z.record(z.enum(['claude','chatgpt','gemini','notebooklm']), z.string())`.

### F-5 [MEDIUM] — Hardcoded `https://sdtm-pedia.pages.dev` in 2 redirect files
- **Where**: `web/src/pages/index.astro:16` + `web/src/pages/[lang]/guide/index.astro:19`
- **What**: noindex+data-pagefind-ignore mitigates SEO impact, but architectural inconsistency vs BaseLayout (which uses derived canonical per Phase 7 Task 7.2).
- **Why it matters**: domain rename requires hunting hardcoded strings separately. CF Pages preview deploys would point canonical at production domain.
- **Fix path**: same-phase IF `Astro.site` defined in `astro.config.mjs` (writer verify). Replace ~2 LOC. Else carryover C-P9-11.

### F-6 [LOW] — playwright stdout: 'ignore' swallows build errors
- **Where**: `playwright.config.ts:13`
- **What**: `npm run build && npm run preview` — if build fails non-zero, preview never starts, playwright times out at 120s with "server did not start". Real build error invisible.
- **Fix path**: carryover C-P9-12 (DX fix).

### F-7 [LOW] — `process.env.CI` comment misleading for CF Pages
- **Where**: `playwright.config.ts:19`
- **What**: comment "CI: always fresh" accurate for GitHub Actions; CF Pages uses `CF_PAGES=1` not `CI`.
- **Fix path**: carryover C-P9-13 (1 LOC comment fix).

### F-8 [LOW] — `role="searchbox"` redundant on `<input type="search">`
- **Where**: `SearchOverlay.tsx:110`
- **What**: implicit ARIA role from `type="search"` makes explicit `role="searchbox"` redundant. Not harmful.
- **Fix path**: carryover C-P9-14.

### F-9 [LOW] — Plugin fixture missing `./UPPERCASE.md` form
- **Where**: `remark-md-link-rewrite.test.mjs`
- **What**: `SHAPE` regex handles dotslash prefix; no fixture covers it.
- **Fix path**: carryover C-P9-15 (1 fixture).

## Recommendations for 9.14 fix bundle

**Include** (HIGH + cheap MEDIUM, ~14 LOC across 3-4 files):
1. F-1 HIGH — pluralization (~2 LOC `SearchOverlay.tsx`)
2. F-3 MEDIUM — CHANGELOG hash fixture (~6 LOC `remark-md-link-rewrite.test.mjs`)
3. F-4 MEDIUM — tighten `values` schema (~3 LOC `schemas.ts`)
4. F-5 MEDIUM — `Astro.site` derivation (~2 LOC × 2 files = 4 LOC) **pending writer verification of `Astro.site` availability**

**Defer** (carryover):
- F-2 → C-P9-10
- F-6 → C-P9-12
- F-7 → C-P9-13
- F-8 → C-P9-14
- F-9 → C-P9-15

## Process notes

- **Rule D**: writer = main session opus / reviewer = feature-dev:code-architect ✓ (different agent + context + lens; cross-family vs Phase 8)
- **Rule A**: 6 new i18n strings spot-checked. zh ✓ / ja ✓ / en F-1 (1/6 = 17% error rate — Rule A spot-check **warranted + caught the bug**).
- **Rule B**: no failures archived (none expected); compliant.
- **Rule C**: retro pending in 9.15 close handoff (correct sequencing).

## Pass-criteria check

- ✗ "0 HIGH findings UNLESS fixable in small post-review patch" — F-1 fixable in ~2 LOC → CONDITIONAL_PASS triggered.
- → Upgrades to **effective PASS** post 9.14 fix bundle (F-1 required; F-3 + F-4 + F-5 recommended).
