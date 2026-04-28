import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  use: {
    baseURL: 'http://localhost:4321',
    trace: 'on-first-retry',
  },
  webServer: {
    // build+preview lane required: search.spec.ts depends on Pagefind index
    // produced only by `npm run build` (`astro dev` does NOT run pagefind).
    // Phase 8 carryover C-P8-1.
    command: 'npm run build && npm run preview',
    url: 'http://localhost:4321',
    // Local iteration: reuse a preview server started by hand (`npm run build &&
    // npm run preview &`) so e2e doesn't rebuild on every `npm run test:e2e`.
    // CI: always fresh — the build step IS the regression guard. Phase 6
    // carryover C-P6-4 (no longer unconditional reuse → no stale-dev false pass).
    reuseExistingServer: !process.env.CI,
    // build can take 30-60s on cold .astro cache; +a few seconds for preview
    // spin-up. 120s gives headroom without flaky timeouts.
    timeout: 120_000,
    stdout: 'ignore',
    stderr: 'pipe',
  },
});
