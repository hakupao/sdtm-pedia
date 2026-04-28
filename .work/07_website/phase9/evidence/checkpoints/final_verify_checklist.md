# Final verify checklist — Phase 9 / master plan §10.5 Step 3

> **Date**: 2026-04-30 (post Phase 9 polish bundle, pre-reviewer)
> **Production URL**: `https://sdtm-pedia.pages.dev/`
> **Commit anchor**: post Phase 9 polish (HEAD pending). 4-28 archeology pre-existing: `2de87c4` (build-bundles+RELEASE.md+downloads.json), `8e7bd83` (GH Release v1.0 cut + DownloadsSection flag flip).

Master plan §10.5 Step 3 lists 8 verify items. Each row = an automated probe + verdict.

| # | Master plan check | Probe | Verdict |
|---|---|---|---|
| 1 | CF Pages production build green | `curl -sI https://sdtm-pedia.pages.dev/zh/` → HTTP/2 200 | ✅ HTTP/2 200 (verified 2026-04-30 05:56) |
| 2 | `https://sdtm-pedia.pages.dev/zh/` renders | `curl -sI ... \| head -3` → 200 + content-type: text/html | ✅ verified |
| 3 | All 4 download links resolve to GH Release (302 to S3) | `curl -sI https://github.com/hakupao/sdtm-pedia/releases/download/v1.0/{claude,chatgpt,gemini,notebooklm}_bundle_v1.0.zip` → all HTTP/2 302 | ✅ 4/4 = HTTP/2 302 (claude 0.8 MB / chatgpt 1.5 MB / gemini 0.5 MB / notebooklm 1.5 MB) |
| 4 | `/compare` filter works (type "容量" in zh, table shrinks) | vitest `CompareFilter.test.tsx` (2 cases) + dist HTML smoke | ✅ vitest 46/46 / dist `/zh/compare/index.html` shows 9-dim table |
| 5 | Cmd+K search opens + finds known string (`AESER`) | playwright `search.spec.ts` real keypress test (post Phase 9 / C-P8-2) | ✅ e2e search.spec.ts green against `npm run preview` (Phase 9 / C-P8-1+C-P8-2) |
| 6 | Theme toggle cycles + persists across reload | vitest `theme.test.ts` + `ThemeToggle.test.tsx` | ✅ vitest covered |
| 7 | Lang switcher swaps URL + content | playwright `lang.spec.ts` + vitest `LangSwitcher.test.tsx` | ✅ e2e + vitest covered |
| 8 | Lighthouse all categories ≥ 95 | Daisy manual via Chrome DevTools → Lighthouse on `https://sdtm-pedia.pages.dev/zh/` | ⏳ **Manual lane** — recorded as **C-P9-2** pending Daisy sweep before public-release announcement |

## Aggregate metrics (post Phase 9)

| Metric | Value | Δ vs Phase 8 close |
|---|---|---|
| tsc errors | 0 | unchanged |
| vitest tests | 46 / 46 in 11 files | +12 / +2 files |
| e2e tests | 7 / 7 against `npm run preview` lane | +0 (lane changed dev→preview, real keypress promoted) |
| build pages | 31 (27 indexed, 4 redirects with `data-pagefind-ignore`) | unchanged page count, redirect HTML structure improved |
| Pagefind warnings (no `<html>` element) | **0** | -4 (C-P7-6 resolved by 9.9) |
| dist/pagefind/ | 17 artifacts / 932K / 27 pages / 6454 words / 3 langs | unchanged |
| GH Release v1.0 | 4 assets live since 2026-04-28T00:42:36Z | unchanged |
| `*:focus-visible` keyboard ring | added (Task 9.5) | NEW |
| zod schema validators for json data | DownloadsSchema + DimensionsSchema (Task 9.8) | NEW |
| remark plugin throw-guard fixture | 6 vitest cases (Task 9.7 / C-P6-6) | NEW |

## Outstanding manual items (Daisy lane)

- **C-P9-1** Safari + Firefox cross-browser sweep per `web/qa/cross-browser-2026-04-30.md` (~10 min)
- **C-P9-2** Lighthouse manual run on `https://sdtm-pedia.pages.dev/zh/` per master plan §10.1 (~5 min)
- **C-P9-3** axe DevTools scan per master plan §10.2 (~10 min)

These three are sequential one-shots Daisy can knock off in a single browser session before announcing v1.0 publicly.

## Sign-off recommendation

✅ All automation-coverable verify items green. The 3 manual sweeps are explicitly carryover (C-P9-1..3) per Phase 9 close handoff. Phase 9 reviewer (Task 9.13 = `feature-dev:code-architect`) gates final-PASS.
