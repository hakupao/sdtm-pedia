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

test('docs reader renders user-guide in zh', async ({ page }) => {
  await page.goto('/zh/guide/user-guide');
  await expect(page.locator('article h1')).toBeVisible();
  await expect(page.locator('aside').first()).toBeVisible();
});

test('link-resolution: every <a> in main resolves ≠404 across landing + guide + changelog', async ({ page, request }) => {
  const routes = ['/zh/', '/en/', '/ja/', '/zh/guide/user-guide', '/zh/changelog'];
  const seen = new Set<string>();
  for (const route of routes) {
    await page.goto(route);
    const hrefs = await page.locator('main a[href], article a[href]').evaluateAll(
      (els) => els.map((e) => (e as HTMLAnchorElement).getAttribute('href') || '')
    );
    for (const href of hrefs) {
      if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('http')) continue;
      const url = href.startsWith('/') ? href : new URL(href, `http://localhost:4321${route}`).pathname;
      if (seen.has(url)) continue;
      seen.add(url);
      const resp = await request.get(url);
      expect(resp.status(), `dead link: ${url} (from ${route})`).toBeLessThan(400);
    }
  }
  expect(seen.size).toBeGreaterThan(0);
});
