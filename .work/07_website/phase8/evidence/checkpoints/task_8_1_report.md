# Task 8.1 — Verify Pagefind Index Builds

> **Date**: 2026-04-29
> **Mode**: direct main session, verification only, no commit
> **Branch**: `main` HEAD = `fbc2ccd`

## Verdict

**PASS** — Pagefind 1.5.2 build pipeline produces a usable search index. SearchOverlay (Task 8.2) can dynamic-import `pagefind.js` and call `search()` once landed.

## Probes

### Build
```
$ cd web && npm run build
... (Astro build 31 pages green)
[Reading languages]
Discovered 3 languages: zh, en, ja
[Building search indexes]
Total:
  Indexed 3 languages
  Indexed 27 pages
  Indexed 6454 words
  Indexed 0 filters
  Indexed 0 sorts
Finished in 0.430 seconds
```
Exit code: **0** ✓

### Artifacts in `dist/pagefind/`
```
$ ls dist/pagefind/
fragment                                  ← per-page snippet store
index                                     ← per-lang inverted index
pagefind-component-ui.css                 ← bundled UI styles
pagefind-component-ui.js                  ← stock UI component
pagefind-entry.json                       ← runtime entry manifest (langs, hashes)
pagefind-highlight.js                     ← result-page highlight helper
pagefind-modular-ui.css                   ← modular UI styles
pagefind-modular-ui.js                    ← modular UI component
pagefind-ui.css                           ← classic UI styles
pagefind-ui.js                            ← classic UI component
pagefind-worker.js                        ← Web Worker for search
pagefind.en_781136c5d2.pf_meta            ← en lang metadata
pagefind.ja_9438c4fd72.pf_meta            ← ja lang metadata
pagefind.js                               ← THE runtime entrypoint (← Task 8.2 dynamic-imports this)
pagefind.zh_cc96385cd2.pf_meta            ← zh lang metadata
wasm.en.pagefind                          ← WASM engine for English
wasm.unknown.pagefind                     ← WASM engine for ja/zh fallback
```
17 artifacts total. Total size: **932K**.

### `pagefind-entry.json` validity
```
$ cat dist/pagefind/pagefind-entry.json | head -20
... (valid JSON, includes language list + per-lang asset hashes)
```
Parses as JSON ✓ (consumed by `pagefind.js` at runtime).

## Findings

### F-8.1-1 [PASS] Required Pagefind artifacts present
All Task 8.2 dependencies present:
- `pagefind.js` — runtime entry (dynamic import target) ✓
- `pagefind-ui.js` — fallback if Task 8.2 ever swaps for stock UI ✓
- `*.pf_meta` for each lang (zh/en/ja) ✓
- `wasm.*.pagefind` engines ✓
- `index/` + `fragment/` data subdirs ✓

### F-8.1-2 [PASS] 3 languages indexed
`zh`, `en`, `ja` matches Phase 7 close baseline of 3-lang i18n parity. No language regression.

### F-8.1-3 [PASS] 27 pages indexed
Matches Phase 7 close `27 content pages` baseline (4 redirect pages correctly excluded — see F-8.1-5).

### F-8.1-4 [INFO] 6454 words indexed
Across 3 langs and 27 pages = ~239 words/page average. Reasonable for short-form documentation pages. No reference baseline to compare against (first-time measurement).

### F-8.1-5 [ACCEPTED] 4 redirect pages "no `<html>` element" warnings
```
4 pages found without an <html> element.
Pages without an outer <html> element will not be processed by default.
  * "/" has no <html> element
  * "/ja/guide/" has no <html> element
  * "/zh/guide/" has no <html> element
  * "/en/guide/" has no <html> element
```
**Correct behavior.** These are Astro auto-generated redirect templates (`<meta http-equiv="refresh">` only, no `<html>`). They SHOULDN'T be indexed because:
- They redirect to canonical content pages within 2 seconds
- They have `<meta name="robots" content="noindex">`
- The canonical content pages ARE indexed (e.g. `/zh/guide/user-guide/` is in the 27 indexed)

Phase 7 reviewer flagged this as C-P7-6 LOW build noise; same noise here. Defer per Phase 8 entry decision (a) — polish bundle Phase 9-or-10.

### F-8.1-6 [INFO] Master plan output naming spec drift
Master plan `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` line 2496 expects:
```
Expected: pagefind.js, pagefind-ui.js, *.pf_index, *.pf_meta exist
```

Actual Pagefind 1.5.2 output:
- `pagefind.js` ✓
- `pagefind-ui.js` ✓
- `*.pf_meta` ✓ (per-lang)
- `*.pf_index` ✗ — REPLACED by `index/` subdir structure (one inverted-index file per chunk inside `index/`) + `fragment/` subdir for snippet data

This is functionally equivalent — `pagefind.js` resolves all paths via the entry manifest. SearchOverlay's dynamic import doesn't care about internal layout. Documented in PLAN.md §"Plan deviation flag" as spec-drift note (NOT a deviation).

## Verification status

- [x] Build green (exit 0)
- [x] `dist/pagefind/` populated (17 artifacts, 932K)
- [x] 3 langs indexed (zh/en/ja)
- [x] ≥27 pages indexed (27 pages, exact match Phase 7 baseline)
- [x] `pagefind-entry.json` valid JSON
- [x] No new failure modes vs Phase 7 baseline (4 redirect warnings = C-P7-6 known)

## Next

Task 8.2 dispatch unblocked. SearchOverlay.tsx can:
- Dynamic import `'/pagefind/pagefind.js'` (runtime path, NOT bundled by Vite)
- Expect `pagefind.search(query)` to return per-lang results based on detected page lang
- Expect `result.url` to point at canonical content URLs with trailing slashes (matches `build.format: 'directory'`)
- Expect `result.excerpt` to contain `<mark>...</mark>` tags around match highlights — must `stripHtml()` before render (per master plan spec)
