import { test, expect } from '@playwright/test';

test.describe('landing', () => {
  for (const lang of ['zh', 'en', 'ja']) {
    test(`/${lang}/ renders all 5 sections`, async ({ page }) => {
      await page.goto(`/${lang}/`);
      // Sections use .enter-fade (opacity 0) and become visible when
      // IntersectionObserver fires. Wait for at least one section (hero) to
      // be revealed before asserting; scroll below-the-fold sections into view.
      await page.waitForFunction(() => document.querySelector('.enter-fade.is-visible') !== null);
      // Scope to main to skip dev-toolbar h1s injected by Astro dev server.
      await expect(page.locator('main h1')).toBeVisible();
      for (const label of ['FOUR PLATFORMS', 'WHICH ONE?', 'DEMO QUESTIONS', 'DOWNLOADS']) {
        const loc = page.locator(`text=${label}`);
        await loc.scrollIntoViewIfNeeded();
        await expect(loc).toBeVisible();
      }
    });
  }
});
