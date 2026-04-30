import { test, expect } from '@playwright/test';

test.describe('landing', () => {
  const sectionLabels = {
    zh: ['NO. 02 / 四个平台', 'NO. 03 / 怎么选?', 'NO. 04 / 演示问题', 'NO. 05 / 下载'],
    en: ['NO. 02 / FOUR PLATFORMS', 'NO. 03 / WHICH ONE?', 'NO. 04 / DEMO QUESTIONS', 'NO. 05 / DOWNLOADS'],
    ja: ['NO. 02 / 4 プラットフォーム', 'NO. 03 / 選び方', 'NO. 04 / デモ質問', 'NO. 05 / ダウンロード'],
  } as const;

  for (const lang of ['zh', 'en', 'ja'] as const) {
    test(`/${lang}/ renders all 5 sections`, async ({ page }) => {
      await page.goto(`/${lang}/`);
      // Sections use .enter-fade (opacity 0) and become visible when
      // IntersectionObserver fires. Wait for at least one section (hero) to
      // be revealed before asserting; scroll below-the-fold sections into view.
      await page.waitForFunction(() => document.querySelector('.enter-fade.is-visible') !== null);
      // Scope to main to skip dev-toolbar h1s injected by Astro dev server.
      await expect(page.locator('main h1')).toBeVisible();
      for (const label of sectionLabels[lang]) {
        const loc = page.getByText(label, { exact: true });
        await loc.scrollIntoViewIfNeeded();
        await expect(loc).toBeVisible();
      }
      // Pin the landing comparison preview to its 4-dim shape; if a contributor
      // expands LANDING_PREVIEW_KEYS or reorders the JSON, this trips loud.
      const whichOne = page.locator('section').filter({ hasText: sectionLabels[lang][1] });
      await expect(whichOne.locator('tbody tr')).toHaveCount(4);
      await expect(page.locator(`a[href="/${lang}/guide/"]`)).toHaveCount(0);
      await expect(page.locator(`a[href="/${lang}/guide/user-guide/"]`).first()).toBeVisible();
    });
  }
});

test('ja landing and demo guide do not expose known Chinese-source strings', async ({ page }) => {
  await page.goto('/ja/');
  await expect(page.locator('main')).not.toContainText('精确变量+推理');
  await expect(page.locator('main')).not.toContainText('团队共享');
  await expect(page.locator('main')).not.toContainText('20 file 硬限');
  await expect(page.locator('main')).not.toContainText('默认开');

  await page.goto('/ja/guide/demo-questions/');
  await expect(page.locator('article')).toContainText('SDTM AI ナレッジベース');
  await expect(page.locator('article')).not.toContainText('同事拿到');
  await expect(page.locator('article')).not.toContainText('题型分布');
  await expect(page.locator('article')).not.toContainText('核心事实必中');
  await expect(page.locator('article')).not.toContainText('主动识破');
});

test('guide release docs have first-class zh/en/ja versions instead of fallback banners', async ({ page }) => {
  const routes = [
    ['/zh/guide/demo-questions/', 'SDTM AI 知识库'],
    ['/en/guide/demo-questions/', 'SDTM AI Knowledge Base'],
    ['/ja/guide/demo-questions/', 'SDTM AI ナレッジベース'],
    ['/zh/guide/known-limitations/', '已知限制'],
    ['/en/guide/known-limitations/', 'Known Limitations'],
    ['/ja/guide/known-limitations/', '既知の制約'],
    ['/zh/changelog/', '更新日志'],
    ['/en/changelog/', 'CHANGELOG'],
    ['/ja/changelog/', '変更履歴'],
  ] as const;

  for (const [route, heading] of routes) {
    await page.goto(route);
    await expect(page.locator('article h1')).toContainText(heading);
    await expect(page.locator('article')).not.toContainText('translation pending');
    await expect(page.locator('article')).not.toContainText('翻译待补');
    await expect(page.locator('article')).not.toContainText('翻訳準備中');
  }
});

test('docs reader renders user-guide in zh', async ({ page }) => {
  await page.goto('/zh/guide/user-guide');
  await expect(page.locator('article h1')).toBeVisible();
  await expect(page.locator('aside').first()).toBeVisible();
});

test('link-resolution: every <a> in main resolves ≠404 across landing + guide + changelog', async ({ page, request }) => {
  const routes = [
    '/zh/', '/en/', '/ja/',
    '/zh/guide/user-guide', '/zh/changelog',
    // README pages in all 3 langs — these contain the non-.md relative refs
    // (./self_deploy/) that must be dropped by the rewrite plugin.
    '/zh/guide/readme', '/en/guide/readme', '/ja/guide/readme',
  ];
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
