# Task 8.2 Executor Subagent Prompt

> **Agent**: `oh-my-claudecode:executor` (opus)
> **Phase**: 07 Website Phase 8 — Search (Pagefind)
> **Task**: 8.2 SearchOverlay React island + tests + e2e
> **Date dispatched**: 2026-04-29
> **Repo**: `/Users/bojiangzhang/MyProject/SDTM-compare`
> **Branch**: `main` (HEAD = `fbc2ccd` at dispatch)

## Goal

Implement the SearchOverlay React island per master plan spec, add vitest unit tests + playwright e2e, mount into TopNav with a Cmd+K hint button, commit. Single commit. ~150 LOC across 4 files.

## Pre-flight context (already verified — DO NOT redo)

- Pagefind 1.5.2 build pipeline is healthy. Task 8.1 already confirmed:
  - `web/package.json` build script `astro build && pagefind --site dist` works
  - `dist/pagefind/` produces 17 artifacts (`pagefind.js`, `pagefind-ui.js`, `pagefind-component-ui.js`, `index/`, `fragment/`, `pagefind-entry.json`, 3 `*.pf_meta`, `wasm.{en,unknown}.pagefind`, etc.)
  - 3 langs indexed (zh/en/ja), 27 pages, 6454 words
  - 4 redirect-page warnings are pre-existing C-P7-6 (correct behavior, ignore)
- Site uses `build.format: 'directory'` so all canonical content URLs end with trailing slash (e.g. `/zh/guide/user-guide/`)
- Phase 7 baseline at HEAD: tsc 0, vitest 32/32, e2e 6/6 strict, 31 build pages

## Files to create

### 1. `web/src/components/react/SearchOverlay.tsx`

Per master plan `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` lines 2531-2606, with these adjustments:

- **No HTML-injection prop allowed.** `r.excerpt` from Pagefind contains `<mark>...</mark>` highlight tags. Strip them with `stripHtml()` (regex `/<[^>]*>/g` → '') and render the plain string via React's normal text-node path: `{stripHtml(r.excerpt)}`. Never use any prop that injects raw HTML.
- Cmd+K (or Ctrl+K) opens; Escape closes; backdrop click closes
- Pagefind loaded via dynamic import on first open: `import(/* @vite-ignore */ '/pagefind/pagefind.js')`. The `@vite-ignore` comment IS required to suppress Vite warnings about runtime-resolved imports.
- Top 10 results
- Tailwind classes per master plan spec (use existing project tokens: `bg-bg`, `border-rule`, `text-accent`, `text-ink-mute`, `font-mono`, `font-serif`)

### 2. `web/src/components/react/SearchOverlay.test.tsx`

Two vitest tests using `@testing-library/react` (already a dep — see existing `CompareFilter.test.tsx`):

1. **opens on Cmd+K**: render, assert `queryByRole('searchbox')` not in document, dispatch `keydown { key: 'k', metaKey: true }` on document, assert `getByRole('searchbox')` in document.
2. **closes on Escape**: render, open via Cmd+K, dispatch `keydown { key: 'Escape' }`, assert searchbox gone.

Mirror the existing `CompareFilter.test.tsx` test structure conventions (jsdom, `import { describe, it, expect } from 'vitest'`).

### 3. `web/tests/e2e/search.spec.ts`

```typescript
import { test, expect } from '@playwright/test';

test('search opens with Cmd+K and finds AESER', async ({ page }) => {
  // Note: requires a built site (pagefind index built only on `npm run build`, not dev)
  // playwright.config.ts already runs `npm run preview` as webServer per Phase 6.4 README tribal-knowledge
  await page.goto('/zh/guide/user-guide');
  await page.keyboard.press('Meta+k');
  const input = page.getByRole('searchbox');
  await expect(input).toBeVisible();
  await input.fill('AESER');
  await expect(page.locator('text=AESER').first()).toBeVisible({ timeout: 5000 });
});
```

**IMPORTANT**: Check `web/playwright.config.ts` — if its `webServer.command` is `npm run dev`, the e2e WILL FAIL because dev server doesn't have Pagefind index. Two options:
- (preferred) check if Phase 5/6/7 already configured `webServer.command` to use `npm run preview` or build-then-preview. If so, just verify the test passes.
- If not configured for build/preview: do NOT modify `playwright.config.ts` — instead document in evidence report that e2e needs `npm run build && npm run preview` first, then run the test manually with the preview server up.

If you decide the e2e needs the playwright config switched to a build+preview server (which would slow CI), STOP and report instead — the user wants minimal scope creep.

## Files to modify

### 4. `web/src/components/astro/TopNav.astro`

- Add: `import SearchOverlay from '../react/SearchOverlay'` at top
- Mount: `<SearchOverlay client:load />` somewhere inside the nav (placement doesn't matter — it's a fixed-position modal)
- Add the ⌘K hint button next to existing controls (alongside `ThemeToggle` / `LangSwitcher`):

```astro
<button
  class="font-mono text-[10px] text-ink-mute hover:text-accent"
  onclick="document.dispatchEvent(new KeyboardEvent('keydown', {key:'k', metaKey:true}))"
  aria-label="Open search"
>
  ⌘K
</button>
```

The button is cosmetic — Cmd+K works without it. Placement: same `<span>`/wrapper as the other nav controls. Match existing nav tokenization style.

## Verification gates (ALL must pass before commit)

Run from `/Users/bojiangzhang/MyProject/SDTM-compare/web`:

```
npx tsc --noEmit
npm test -- --run
npm run build
ls dist/pagefind/                    # still populated
```

Expected after Task 8.2:
- tsc: 0 errors
- vitest: 34/34 (was 32; +2 SearchOverlay tests)
- build: 31 pages green
- dist/pagefind/ still populated (17 artifacts)

For the e2e test, run separately ONCE BUILD IS GREEN:
```
npm run build
npm run preview &           # background it
sleep 3
npx playwright test tests/e2e/search.spec.ts
kill %1                     # stop preview
```

If e2e passes, record in evidence. If e2e fails due to playwright.config.ts not running build+preview, document the gap (don't modify config) and let the user decide.

## Commit

ONE commit only. Stage these 4 files:
```
git add web/src/components/react/SearchOverlay.tsx \
        web/src/components/react/SearchOverlay.test.tsx \
        web/src/components/astro/TopNav.astro \
        web/tests/e2e/search.spec.ts
git commit -m "$(cat <<'EOF'
07 Website Phase 8.2 — SearchOverlay (Cmd+K, Pagefind dynamic import, plain-text excerpt, 2 tests + e2e)

Master plan §"Phase 7 — Search (Pagefind)" Task 7.2 (renumbered to Phase 8 per
Phase 7 close handoff `.work/meta/website_phase7_to_phase8_handoff_2026-04-29.md`).
Cmd+K / Ctrl+K opens overlay, Esc or backdrop click closes. Pagefind loaded via
runtime dynamic import (no eager bundle cost). Excerpts pass through stripHtml
(no HTML-injection prop) — Pagefind <mark> highlight tags rendered as plain
text. Top 10 results. Vitest: 32 -> 34. E2E: search.spec.ts added.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

## Evidence to write

Write the report to `/Users/bojiangzhang/MyProject/SDTM-compare/.work/07_website/phase8/evidence/checkpoints/task_8_2_report.md`. Include:

- Files created + LOC counts
- Verification results (tsc / vitest / build / e2e — actual numbers)
- Any spec adjustments + reason (e.g. if you changed the Tailwind class palette to match existing tokens)
- Any blockers (e.g. e2e needed config change you stopped to flag)
- Commit hash

Also update `/Users/bojiangzhang/MyProject/SDTM-compare/.work/07_website/phase8/_progress.json` `tasks.8.2_searchoverlay_react_island.status` from `pending` to `completed` with `commit` filled in and `verdict: "PASS"`. Preserve other fields.

## Constraints

- **Do not** modify `playwright.config.ts` (per scope minimization). Flag if e2e gating needs a config change instead of doing it.
- **Do not** touch any file under `.work/06_deep_verification/` — three other sessions are running parallel batches there.
- **Do not** add new dependencies — `@testing-library/react` and `vitest` are already deps; `pagefind` is a dep + dynamic-imported at runtime (not bundled).
- **Do not** localize the search placeholder — Phase 8 explicitly defers i18n of the search overlay (see PLAN.md "Rule A semantic spot-check"). Keep `placeholder="Search docs..."` English-only per master plan spec.
- **Do not** push. The user runs the close + push at end of phase.

## What "done" looks like

- 1 commit on `main` (HEAD ahead of `fbc2ccd` by 1)
- `task_8_2_report.md` written with verification numbers
- `_progress.json` updated: 8.2 status `completed`, commit hash recorded
- A short summary back to the user covering: LOC, vitest delta, e2e status, any blockers
