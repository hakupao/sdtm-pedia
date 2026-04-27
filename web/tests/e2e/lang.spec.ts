import { test, expect } from '@playwright/test';

test('root redirects to /zh/', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveURL(/\/zh\//);
});
