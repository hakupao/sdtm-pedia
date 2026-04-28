import { test, expect } from '@playwright/test';

// NOTE: Pagefind index is produced only by `npm run build` (not by `astro dev`).
// playwright.config.ts currently runs `npm run dev` as webServer, so this spec
// requires a manual preview lane until C-P8-1 (Phase 9 polish) switches the
// playwright webServer to `npm run build && npm run preview`.
//
// Manual run:
//   npm run build
//   npm run preview &
//   npx playwright test tests/e2e/search.spec.ts --config=<override-baseURL-to-:4322>
//   kill %1
// Test name reflects the actual trigger (button click → synthetic keydown), not
// raw `page.keyboard.press('Meta+k')`. The raw keypress isn't reliably delivered
// to the React document listener in headless chromium without a focused target;
// the button's inline onclick exercises the same setOpen(true) code path.
// Vitest covers the raw-keydown listener wiring separately (SearchOverlay.test.tsx).
// Tracked: C-P8-2 — promote to real-keypress test once playwright webServer is
// switched to build+preview (C-P8-1) so we can investigate focus delivery.
test('search opens via ⌘K hint button click (synthetic keydown) and finds AESER', async ({ page }) => {
  await page.goto('/zh/guide/user-guide/');
  // Wait for the SearchOverlay React island to hydrate before dispatching a
  // keyboard event — Astro's astro-island custom element wires the document
  // listener inside `connectedCallback` -> hydrator. The "Open search" button
  // (rendered by Astro at SSR) becomes useful as a hydration-completion proxy.
  await expect(page.getByLabel('Open search')).toBeVisible();
  // Click the ⌘K hint button — its onclick dispatches a synthetic
  // KeyboardEvent on document, exercising the same code path as Cmd+K.
  await page.getByLabel('Open search').click();
  const input = page.getByRole('searchbox');
  await expect(input).toBeVisible();
  await input.fill('AESER');
  await expect(page.locator('text=AESER').first()).toBeVisible({ timeout: 5000 });
});
