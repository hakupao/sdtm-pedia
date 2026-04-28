import { test, expect, type Locator } from '@playwright/test';

async function computedFontSizePx(locator: Locator) {
  const value = await locator.evaluate((el) => window.getComputedStyle(el).fontSize);
  return Number.parseFloat(value);
}

test('font-size tiers enlarge UI text without resizing containers or markdown prose', async ({ page }) => {
  await page.goto('/zh/');

  const heroInner = page.locator('main section').first().locator('> div');
  const cta = page.locator('main a[href="/zh/guide/user-guide/"]').first();
  const defaultWidth = await heroInner.evaluate((el) => (el as HTMLElement).offsetWidth);

  for (const [tier, expected] of [
    ['sm', 12.625],
    ['md', 14],
    ['lg', 15.375],
    ['xl', 16.75],
  ] as const) {
    await page.evaluate((nextTier) => {
      if (nextTier === 'md') {
        document.documentElement.removeAttribute('data-fontsize');
      } else {
        document.documentElement.dataset.fontsize = nextTier;
      }
    }, tier);
    await expect(computedFontSizePx(cta)).resolves.toBeCloseTo(expected, 1);
  }

  const xlWidth = await heroInner.evaluate((el) => (el as HTMLElement).offsetWidth);
  expect(xlWidth).toBe(defaultWidth);

  await page.goto('/zh/guide/user-guide/');
  const proseHeading = page.locator('.prose-doc h1').first();
  await expect(computedFontSizePx(proseHeading)).resolves.toBeCloseTo(36, 1);
});
