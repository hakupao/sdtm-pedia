# Task 6.1 Evidence Report

> Subagent: `oh-my-claudecode:executor` (opus, 1M)
> Branch: `main` (parent SHA `b25b834`)
> Date: 2026-04-28

## 1. Files touched

| Filename | Change | Lines |
|---|---|---|
| `web/src/components/react/CompareFilter.tsx` | CREATE | +66 |
| `web/src/components/react/CompareFilter.test.tsx` | CREATE | +35 |
| `web/src/pages/[lang]/compare.astro` | OVERWRITE (Phase 5 stub → real page) | -19 / +25 (net +6) |
| `.work/07_website/phase6/evidence/checkpoints/task_6_1_report.md` | CREATE | (this file) |

No other source files touched. `compare-dimensions.json` and `ComparePreviewSection.astro` deferred to Task 6.2 per brief §"Files NOT to touch".

## 2. Plan-deviation confirmation

The OVERWRITE follows the PLAN.md `⚠️ Plan deviation flag`: path-based i18n via `Astro.params.lang` (NOT root `compare.astro` + `?lang=` query). Verbatim file body of the new `web/src/pages/[lang]/compare.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import TopNav from '../../components/astro/TopNav.astro';
import { CompareFilter } from '../../components/react/CompareFilter';
import dims from '../../data/compare-dimensions.json';
import { type Lang } from '../../i18n/helpers';

export function getStaticPaths() {
  return [
    { params: { lang: 'zh' } },
    { params: { lang: 'en' } },
    { params: { lang: 'ja' } },
  ];
}

const lang = Astro.params.lang as Lang;
const pathname = Astro.url.pathname;
---
<BaseLayout title="Platform Comparison" lang={lang}>
  <TopNav lang={lang} pathname={pathname} />
  <main class="px-7 py-8 max-w-screen-xl mx-auto">
    <h1 class="font-display text-4xl font-bold mb-2">Multi-dimensional Comparison</h1>
    <p class="font-serif text-ink-mute mb-8">
      Side-by-side across 4 platforms. Filter by dimension keyword.
    </p>
    <CompareFilter client:load dims={dims} lang={lang} />
  </main>
</BaseLayout>
```

Confirmation points (per PLAN.md plan-deviation rationale):
- `getStaticPaths()` returns 3 lang params (`zh`, `en`, `ja`) — generates `/zh/compare/`, `/en/compare/`, `/ja/compare/`.
- Lang sourced from `Astro.params.lang as Lang` — NOT `Astro.url.searchParams.get('lang')`.
- `<TopNav lang={lang} pathname={pathname} />` mounts inside `<BaseLayout>` per existing `[lang]/changelog.astro` pattern; layout does not inject nav itself.
- `client:load` directive on `<CompareFilter>` because `useState` lives in the React island — `client:idle`/`client:visible` would paint-flash the input.

This is the artifact for "plan deviation followed".

## 3. vitest output (verbatim tail)

```
 RUN  v4.1.5 /Users/bojiangzhang/MyProject/SDTM-compare/web

 Test Files  8 passed (8)
      Tests  31 passed (31)
   Start at  11:08:52
   Duration  1.11s (transform 418ms, setup 816ms, import 353ms, tests 226ms, environment 5.34s)
```

Delta: was 29 → now 31 (= 29 prior + 2 new in `CompareFilter.test.tsx`).

The 2 new tests:
- `<CompareFilter> > renders all rows by default` — asserts both `最强场景` and `容量上限` rendered when `q=''`.
- `<CompareFilter> > filters rows by search input` — types `容量`, asserts `最强场景` removed, `容量上限` retained.

## 4. Build output

`npm run build` finished in 0.411 seconds with 0 errors. Pre-existing warnings (4 routes "no <html> element": `/`, `/zh/guide/`, `/en/guide/`, `/ja/guide/`) are inherited from prior phases and unrelated to Task 6.1.

`/compare/` lang variants verified:
```
dist/en/compare/index.html
dist/ja/compare/index.html
dist/zh/compare/index.html
```

All three exist (one per `getStaticPaths()` entry).

## 5. Stub-replacement check

```
$ grep -l "PHASE 6 PENDING" dist/zh/compare/index.html && echo "FAIL: stub still present" || echo "OK: stub gone"
OK: stub gone

$ grep -c '<table' dist/zh/compare/index.html
1

$ grep -c 'role="searchbox"' dist/zh/compare/index.html
0
```

The `role="searchbox"` literal-grep returned 0 — **but this is correct, not a failure**. `<input type="search">` carries the `searchbox` ARIA role *implicitly*; React/Astro renders only the explicit `type="search"` attribute, not a redundant `role=` attribute. The test `screen.getByRole('searchbox')` works on the implicit role. Semantic equivalent verification:

```
$ grep -c 'type="search"' dist/zh/compare/index.html
1

$ grep -c 'aria-label="Filter dimensions"' dist/zh/compare/index.html
1

$ grep -o 'type="search"[^>]*' dist/zh/compare/index.html | head -1
type="search" placeholder="Filter dimensions..." aria-label="Filter dimensions" class="font-mono text-sm px-3 py-2 border border-rule bg-bg w-64 mb-6" value=""/
```

Input element renders with `type="search"` (implicit searchbox role) + a11y `aria-label`. Comparison table is server-rendered (1 `<table>`).

## 6. e2e (verbatim tail)

```
Running 6 tests using 2 workers

  ✓  2 tests/e2e/lang.spec.ts:3:1 › root redirects to /zh/ (665ms)
  ✓  1 tests/e2e/smoke.spec.ts:5:5 › landing › /zh/ renders all 5 sections (1.2s)
  ✓  3 tests/e2e/smoke.spec.ts:5:5 › landing › /en/ renders all 5 sections (1.1s)
  ✓  4 tests/e2e/smoke.spec.ts:5:5 › landing › /ja/ renders all 5 sections (1.1s)
  ✓  5 tests/e2e/smoke.spec.ts:22:1 › docs reader renders user-guide in zh (176ms)
  ✓  6 tests/e2e/smoke.spec.ts:28:1 › link-resolution: every <a> in main resolves ≠404 across landing + guide + changelog (1.6s)

  6 passed (7.8s)
```

6/6 PASS. No stale `astro dev` on :4321 — pre-emptive `lsof -ti:4321 | xargs -r kill` returned no PIDs.

## 7. Open questions / surprises

1. **`role="searchbox"` literal grep ≠ implicit ARIA role** — The brief's verification step 4 expected `grep -c 'role="searchbox"' ≥ 1`. The HTML spec rule is that `<input type="search">` carries the `searchbox` role implicitly without an explicit `role=` attribute being serialized. So the literal grep returns 0, but the testing-library `getByRole('searchbox')` query (which honors implicit roles) works — and the unit test for `getByRole('searchbox')` in `CompareFilter.test.tsx` PASSES (one of the 31/31). I did NOT add an explicit `role="searchbox"` attribute to the input because (a) it would be redundant per WAI-ARIA "first rule of ARIA use" (don't add ARIA when native HTML provides the same semantics), (b) it would diverge from the plan template, and (c) the underlying intent (a searchbox is rendered) is satisfied. I substituted a semantic-equivalent grep (`type="search"` + `aria-label="Filter dimensions"`) for evidence — both return 1. **Recommend reviewer 6.3 update PLAN §6.1 verification step to use `grep -c 'type="search"'` instead.**

2. **No other surprises.** All other steps green first-attempt. No retries, no Rule B failure-archive entries.

## Rule A/B/C/D/E compliance

- **Rule A (semantic spot-check)**: not applicable — no AI rewrite/compress operation in this task.
- **Rule B (failure archive)**: no abandoned attempts; no `failures/task_6_1_attempt_*.md` written.
- **Rule C (retro)**: deferred to Task 6.3 reviewer + Phase-6 retro (Tier 3 project-level).
- **Rule D (writer ≠ reviewer)**: this report is the writer artifact only. Reviewer is Task 6.3 (`oh-my-claudecode:critic`).
- **Rule E (cross-platform)**: not applicable — single-task scope.
