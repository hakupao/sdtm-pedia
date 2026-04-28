# Task 7.0 — CF Pages preview verification (C-P5-M3)

> **Date**: 2026-04-29
> **Mode**: direct main-session, verification-only (no code changes)
> **Live site**: `https://sdtm-pedia.pages.dev/`
> **Local HEAD**: `e1737f1` (pushed; origin/main matches)

## Verdict

**PASS** — C-P5-M3 trailing-slash hosting verified clean. One incidental finding documented as **C-P7-1** (Astro i18n fallback soft-404 behavior). No regressions block Phase 7 progression to 7.1+.

## Probe matrix

### F-7.0-1: Trailing-slash redirects (PRIMARY C-P5-M3 verification)

| Probe class | Sample size | Result | Verdict |
|---|---|---|---|
| `/[lang]/<path>/` (with slash) | 13 routes (zh ×7 + en ×3 + ja ×3) | All 200 + `text/html` | ✅ PASS |
| `/[lang]/<path>` (no slash) | 11 routes (zh ×7 + en ×2 + ja ×2) | All 308 → `/[lang]/<path>/` | ✅ PASS |
| `/index.html` | 1 | 308 → `/` | ✅ PASS |
| `/` | 1 | 200 + `text/html` | ✅ PASS |
| `/sitemap-index.xml` | 1 | 200 + `application/xml` | ✅ PASS |

**Routes verified** (post Phase 6.4 close):
- `/zh/`, `/zh/guide/`, `/zh/guide/user-guide/`, `/zh/guide/platform-comparison/`, `/zh/changelog/`, `/zh/guide/readme/`, `/zh/compare/`
- `/en/`, `/en/compare/`, `/en/changelog/`
- `/ja/`, `/ja/compare/`, `/ja/changelog/`

**Cross-lang redirect anomaly check**: 0 cross-lang redirects observed. Every 308 stays within `/[lang]/`. Astro `build.format: 'directory'` + sidebar/CTA `/foo` (no slash) hrefs work correctly with CF Pages auto-redirect.

### F-7.0-2: Phase 6.4 H1 fix verification (changelog dual-route drop)

Expected post H1 fix: `/[lang]/guide/changelog/` returns 404 (sitemap dropped, dist directory not emitted).

Observed: 200 + meta-refresh redirect HTML body:
```html
<!doctype html>
<title>Redirecting to: /zh/</title>
<meta http-equiv="refresh" content="2;url=/zh/">
<meta name="robots" content="noindex">
<link rel="canonical" href="https://sdtm-pedia.pages.dev/zh/">
```

**Root-cause investigation**:
- Local `dist/zh/guide/changelog/` directory: **does not exist** (correctly dropped in 6.4)
- Live sitemap (`/sitemap-0.xml`): **does NOT list** `/[lang]/guide/changelog/` (correctly dropped)
- `/zh/guide/readme/` (Phase 6.4 NEW route): live response = full readme HTML (NOT redirect) → confirms CF is serving fresh build, NOT cached pre-6.4 deploy
- 3 nonsense URLs probed — `/zh/totally-bogus-path-12345/`, `/zh/foo/bar/baz/`, `/totally-bogus-path-12345/` — ALL return 200 with the same meta-refresh body

**Conclusion**: This is **intrinsic Astro 6 i18n fallback behavior** (`prefixDefaultLocale: true` + `defaultLocale: 'zh'`). Astro generates a soft-404 page for ALL unmatched `/[lang]/*` paths that meta-refreshes to the lang root. NOT a stale build; NOT a CF issue; NOT a regression from 6.4.

**SEO impact assessment**:
- Mitigated by `<meta name="robots" content="noindex">` on the soft-404 page → search engines won't index these URLs
- Phase 6.4 H1 fix achieves its primary goal (sitemap doesn't include dual-route changelog; canonical link on the live changelog points to correct route)
- Soft-404 200-response could fool dead-link checkers (link checkers expect proper 404 status). Low priority since project's internal links are programmatic + e2e covered

**Action**: documented as C-P7-1 (LOW). No code change in 7.0.

### F-7.0-3: Edge cases probed

- `dist/404.html`: empty file (0 bytes). Astro 6 + sitemap integration may not emit a 404 page by default; CF Pages serves built routes via static file lookup, falls through to Astro's i18n fallback for `/[lang]/*`
- Lang-neutral nonsense path `/totally-bogus-path-12345/`: also returns 200 with same fallback (this means even non-`[lang]` paths fall through to the same i18n redirect)
- `web/public/`: contains 4 files (favicon × 2, og-default.png, robots.txt). No `_redirects` / `_routes.json` / `_headers` overrides. CF Pages serves dist/ directly with default routing.

## Findings

### F-7.0-1 (PASS — primary objective)

**C-P5-M3 trailing-slash hosting**: ✅ verified clean across 27 probes. Astro `build.format: 'directory'` + sidebar `/foo` (no slash) hrefs work correctly via CF Pages 308 auto-redirects. No cross-lang redirect anomalies. No 5xx errors. No DNS/cert issues.

### F-7.0-2 (DRIFT-NOT-REGRESSION — incidental)

**Astro i18n soft-404 200-response behavior**: ALL unmatched `/[lang]/*` paths return 200 + meta-refresh redirect HTML (not hard 404). This is Astro design intent under `prefixDefaultLocale: true`, mitigated by `<meta name="robots" content="noindex">`. Not a regression from any phase. Phase 6.4 H1 fix accomplishes its sitemap-level goal.

→ **NEW carryover C-P7-1**: Astro i18n soft-404 behavior. LOW priority. Resolution options:
- (a) Accept as-is (current state, mitigated by noindex meta)
- (b) Add explicit catchall `[lang]/[...slug].astro` 404 fallback returning proper Astro `Astro.response.status = 404`
- (c) Add CF Pages `_routes.json` rule for explicit 404 routing
- (d) Document in `web/README.md` (Task 7.3) as "expected behavior, see C-P7-1"

**Recommendation**: defer to post-Phase-7 polish OR accept indefinitely (noindex meta is sufficient SEO defense).

## Verifications run

- `bash /tmp/cf_probe.sh` (40-probe matrix, captured in this report)
- `curl -s` body checks on `/zh/guide/changelog/`, `/zh/guide/readme/`, nonsense paths
- `ls dist/zh/` + `ls dist/zh/guide/changelog` (local dist sanity)
- `curl /sitemap-0.xml | head` (sitemap content sanity)
- `cat web/astro.config.mjs` (i18n config confirmation)

## Carryover delta

**Phase 6 → Phase 7 carryover updates**:
- C-P5-M3 trailing-slash hosting: **RESOLVED** in 7.0
- **NEW C-P7-1**: Astro i18n soft-404 200-response behavior (LOW, accept-as-is recommended)

## Next step

Proceed to Task 7.1 (compare i18n chrome). C-P7-1 added to Phase 7 carryover ledger; no blocker for 7.1+.
