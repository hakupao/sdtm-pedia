import { test, expect, type Locator } from '@playwright/test';

async function computedFontSizePx(locator: Locator) {
  const value = await locator.evaluate((el) => window.getComputedStyle(el).fontSize);
  return Number.parseFloat(value);
}

test('font-size tiers enlarge UI text without resizing containers or markdown prose', async ({ page }) => {
  await page.setViewportSize({ width: 1254, height: 720 });
  await page.goto('/zh/');

  const heroInner = page.locator('main section').first().locator('> div');
  const cta = page.locator('main a[href="/zh/guide/user-guide/"]').first();
  const fontSizeNav = page.getByRole('navigation', { name: '字号' });
  const defaultWidth = await heroInner.evaluate((el) => (el as HTMLElement).offsetWidth);
  await expect(fontSizeNav.getByRole('button', { name: '中' })).toHaveAttribute('aria-pressed', 'true');

  for (const [label, expected] of [
    ['小', 12.625],
    ['中', 14],
    ['大', 15.375],
    ['特大', 16.75],
  ] as const) {
    await fontSizeNav.getByRole('button', { name: label, exact: true }).click();
    await expect(computedFontSizePx(cta)).resolves.toBeCloseTo(expected, 1);
  }

  const xlWidth = await heroInner.evaluate((el) => (el as HTMLElement).offsetWidth);
  expect(xlWidth).toBe(defaultWidth);
  const wrappedTopNavItems = await page.locator('#mobile-nav-content a, #mobile-nav-content button').evaluateAll((els) => (
    els
      .map((el) => {
        const rect = el.getBoundingClientRect();
        return {
          text: (el.textContent || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' '),
          height: rect.height,
          whiteSpace: window.getComputedStyle(el).whiteSpace,
        };
      })
      .filter((item) => ['平台', '演示', '下载', '文档', '搜索'].includes(item.text))
      .filter((item) => item.height > 36 || item.whiteSpace !== 'nowrap')
  ));
  expect(wrappedTopNavItems).toEqual([]);

  await page.goto('/zh/guide/user-guide/');
  const proseHeading = page.locator('.prose-doc h1').first();
  await expect(computedFontSizePx(proseHeading)).resolves.toBeCloseTo(36, 1);
});
