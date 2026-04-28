# Task 7.2 — Site-wide canonical link via BaseLayout (C-P6-3)

> **Date**: 2026-04-29
> **Mode**: direct main-session, 1 file
> **Carryover absorbed**: C-P6-3
> **Files touched**: 1

## Verdict

**PASS** — `<link rel="canonical">` emitted on 31/31 HTML pages with correct lang-specific URLs. `og:url` added alongside for social-sharing consistency. tsc 0 / vitest 32/32 / e2e 6/6 / fresh build green.

## Files modified

| File | Δ | Purpose |
|---|---|---|
| `web/src/layouts/BaseLayout.astro` | +5 -0 | compute `canonicalHref` from `Astro.site` + `Astro.url.pathname`; emit `<link rel="canonical">` + `<meta property="og:url">` in `<head>` |

`web/astro.config.mjs` already has `site: 'https://sdtm-pedia.pages.dev'` (verified Phase 7 pre-flight); no config change needed.

## Implementation

```astro
const canonicalHref = Astro.site
  ? new URL(Astro.url.pathname, Astro.site).href
  : Astro.url.pathname;
```

Then in `<head>`:
```astro
<link rel="canonical" href={canonicalHref} />
...
<meta property="og:url" content={canonicalHref} />
```

The `Astro.site` fallback path-only branch is unreachable in production (config sets `site:`), but defensive — preserves a usable canonical even if config drifts later.

## Verifications

| Check | Cmd | Result |
|---|---|---|
| TypeScript | `npx tsc --noEmit` | 0 errors |
| Unit tests | `npm test -- --run` | 32/32 passed (Phase 7.1 baseline preserved) |
| Fresh build | `rm -rf .astro node_modules/.astro dist && npm run build` | 31 HTML pages emitted |
| e2e | `npx playwright test` | 6/6 passed |
| Canonical coverage | `grep -lr 'rel="canonical"' dist --include='*.html' \| wc -l` | 31/31 (100%) |
| Sample compare zh | `dist/zh/compare/index.html` canonical | `https://sdtm-pedia.pages.dev/zh/compare/` |
| Sample compare en | `dist/en/compare/index.html` canonical | `https://sdtm-pedia.pages.dev/en/compare/` |
| Sample compare ja | `dist/ja/compare/index.html` canonical | `https://sdtm-pedia.pages.dev/ja/compare/` |
| Existing changelog route | `dist/zh/changelog/index.html` canonical | `https://sdtm-pedia.pages.dev/zh/changelog/` |
| Lang root | `dist/zh/index.html` canonical | `https://sdtm-pedia.pages.dev/zh/` |
| Site root (redirect-to-zh) | `dist/index.html` canonical | `https://sdtm-pedia.pages.dev/zh/` (Astro's built-in i18n redirect template, NOT BaseLayout — correct: soft-redirects canonical to redirect target) |

## Coverage breakdown

- **27 content pages** extending BaseLayout: get our new canonical pointing to themselves
- **4 redirect pages** (`/`, `/zh/guide/`, `/en/guide/`, `/ja/guide/`) NOT extending BaseLayout: retain Astro's built-in i18n redirect canonical pointing to their lang-root target

This is the correct SEO behavior:
- Real content pages have self-referential canonical → search engines treat the URL as authoritative
- Soft-redirect pages have canonical to the redirect destination → search engines consolidate signals on the destination

## Trailing-slash format check

`Astro.url.pathname` returns `/zh/compare/` (with trailing slash) for `dist/zh/compare/index.html`, matching `build.format: 'directory'`. No manual normalization needed.

## Carryover delta

- C-P6-3 site-wide canonical: **RESOLVED** in 7.2

## Commit

```
git commit -m "07 Website Phase 7.2 — site-wide canonical link via BaseLayout (C-P6-3 absorbed)"
```
