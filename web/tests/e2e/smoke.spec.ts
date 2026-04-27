import { test, expect } from '@playwright/test';

test.describe('landing', () => {
  for (const lang of ['zh', 'en', 'ja']) {
    test(`/${lang}/ renders all 5 sections`, async ({ page }) => {
      await page.goto(`/${lang}/`);
      await expect(page.locator('h1')).toBeVisible();
      await expect(page.locator('text=FOUR PLATFORMS')).toBeVisible();
      await expect(page.locator('text=WHICH ONE?')).toBeVisible();
      await expect(page.locator('text=DEMO QUESTIONS')).toBeVisible();
      await expect(page.locator('text=DOWNLOADS')).toBeVisible();
    });
  }
});
