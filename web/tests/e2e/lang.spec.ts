import { test, expect } from '@playwright/test';

test('root renders zh landing without a local redirect flash', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveURL('http://localhost:4321/');
  await expect(page.locator('main h1')).toContainText('SDTM 知识库');
  await expect(page.locator('text=Redirecting')).toHaveCount(0);
  await expect(page.locator('a[href="/zh/guide/user-guide/"]').first()).toBeVisible();
});
