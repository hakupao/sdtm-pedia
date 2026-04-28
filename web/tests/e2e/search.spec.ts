import { test, expect } from '@playwright/test';

// Phase 9 / C-P8-2: real keypress — playwright webServer is now `npm run build
// && npm run preview` (C-P8-1) so Pagefind index exists and chromium runs
// against built assets that include the SearchOverlay islanded as expected.
// Control+k chosen over Meta+k for cross-platform CI (Linux runner has no Meta
// key); SearchOverlay listener accepts either ctrlKey or metaKey + 'k'.
test('search opens via Cmd/Ctrl+K and finds AESER', async ({ page }) => {
  await page.goto('/zh/guide/user-guide/');
  // Hydration completion proxy: wait for the ⌘K hint button (rendered by
  // Astro at SSR, hydrated by React island wiring the document keydown listener).
  await expect(page.getByLabel('Open search')).toBeVisible();
  // Click body first to ensure document focus (not browser chrome). Without
  // this, headless chromium routes the keypress to the chrome and the React
  // document listener never sees it.
  await page.locator('body').click();
  await page.keyboard.press('Control+k');
  const input = page.getByRole('searchbox');
  await expect(input).toBeVisible();
  await input.fill('AESER');
  await expect(page.locator('text=AESER').first()).toBeVisible({ timeout: 5000 });
});
