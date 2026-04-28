# Task 7.1 — Compare page i18n chrome (C-P6-1)

> **Date**: 2026-04-29
> **Mode**: direct main-session, mechanical
> **Carryover absorbed**: C-P6-1
> **Files touched**: 6

## Verdict

**PASS** — 4 keys × 3 langs added with parity, dist HTML emits correct localized strings on all 3 lang variants, vitest 32/32 (was 31, +1), tsc 0 errors, no regression on changelog catchall drop.

## Files modified

| File | Δ | Purpose |
|---|---|---|
| `web/src/i18n/ui.zh.json` | +4 | 4 new keys (compare.title / compare.subhead / compare.filter.placeholder / compare.filter.label) |
| `web/src/i18n/ui.en.json` | +4 | parity (English source) |
| `web/src/i18n/ui.ja.json` | +4 | parity (Japanese translations) |
| `web/src/components/react/CompareFilter.tsx` | ~3 | import `getUIStrings` + plumb `t['compare.filter.placeholder']` + `t['compare.filter.label']` into input |
| `web/src/components/react/CompareFilter.test.tsx` | +11 | new test "localizes filter input placeholder + aria-label per lang" covering zh/en/ja |
| `web/src/pages/[lang]/compare.astro` | ~6 | replace hardcoded h1 + subhead with `t['compare.title']` + `t['compare.subhead']`; pass localized title to BaseLayout for HTML <title> SEO consistency |

## 4 new keys × 3 langs

| Key | zh | en | ja |
|---|---|---|---|
| `compare.title` | 多维平台对比 | Multi-dimensional Comparison | 多次元プラットフォーム比較 |
| `compare.subhead` | 四平台横向对比. 按维度关键字过滤. | Side-by-side across 4 platforms. Filter by dimension keyword. | 4 プラットフォーム横並び. 次元キーワードで絞り込み. |
| `compare.filter.placeholder` | 过滤维度... | Filter dimensions... | 次元を絞り込み... |
| `compare.filter.label` | 过滤维度 | Filter dimensions | 次元を絞り込む |

## Implementation choice

Decided to have `CompareFilter` call `getUIStrings(lang)` **internally** rather than pass placeholder/label as props from the .astro caller. Reasons:

1. Keeps existing `<CompareFilter dims={dims} lang="zh" />` API unchanged → existing 2 tests pass without signature edits
2. Vitest jsdom env handles `import zh from './ui.zh.json'` natively (Vite ESM JSON)
3. Bundle cost: ui.{zh,en,ja}.json + helpers.ts are already imported elsewhere in the client bundle (TopNav etc.); marginal added bytes ≈ 0
4. Risk: client bundle pulls all 3 lang dictionaries even when only 1 is used. Acceptable: 3 × ~20 keys × ~30 bytes ≈ 2KB raw. Not worth the prop-plumbing complexity for this scale.

## Verifications

| Check | Cmd | Result |
|---|---|---|
| TypeScript | `npx tsc --noEmit` | 0 errors |
| Unit tests | `npm test -- --run` | 32/32 passed (was 31; +1 new i18n localization test) |
| Key parity (zh = en = ja keys) | within `helpers.test.ts` | PASS automatically (4 new keys in all 3 dicts) |
| Fresh build (cache clear) | `rm -rf .astro node_modules/.astro dist && npm run build` | 31 HTML pages emitted (27 indexed by pagefind + 4 redirect routes — consistent with Phase 6 close) |
| zh/compare i18n strings in dist | `grep -oE '多维平台对比\|过滤维度' dist/zh/compare/index.html` | found `多维平台对比`, `过滤维度` |
| en/compare i18n strings in dist | `grep -oE 'Multi-dimensional Comparison\|Filter dimensions' dist/en/compare/index.html` | found both |
| ja/compare i18n strings in dist | `grep -oE '多次元プラットフォーム比較\|次元を絞り込み\|次元を絞り込む' dist/ja/compare/index.html` | found `多次元プラットフォーム比較`, `次元を絞り込み` |
| H1 fix not regressed | `ls dist/zh/guide/changelog` | OK: dropped (Phase 6.4 H1 still effective) |

## Rule A spot-check (N=3 of 12 strings)

Per PLAN.md §"Rule A semantic spot-check" — 12 translated strings (4 keys × 3 langs), pick 3 randomly:

| Sample | Source (en) | Target (lang) | Verdict |
|---|---|---|---|
| `compare.subhead.ja` | "Side-by-side across 4 platforms. Filter by dimension keyword." | "4 プラットフォーム横並び. 次元キーワードで絞り込み." | **PASS** — 横並び (side-by-side) is idiomatic Japanese for tabular comparison; プラットフォーム loanword consistent with rest of ja dict; 次元 (dimension) is correct technical JP usage |
| `compare.filter.label.ja` | "Filter dimensions" | "次元を絞り込む" | **PASS with minor polish suggestion** — verb-form (`絞り込む`) reads as "to filter dimensions" (imperative). Idiomatically natural for a screen-reader action description. Could be `次元の絞り込み` (noun-form) for stricter label convention; not blocking. Defer to optional polish if Daisy's JP ear prefers |
| `compare.title.zh` | "Multi-dimensional Comparison" | "多维平台对比" | **PASS** — 多维 (multi-dimensional) is technical; 平台 (platform) explicit makes it more discoverable than dropping platform; 对比 (comparison) is formal/SEO-friendly |

**Spot-check result**: 3/3 semantic PASS. 0 SDTM term drift (none expected — these are UI chrome). 0 fabrication. 1 optional polish on `compare.filter.label.ja` deferred.

## Carryover delta

- C-P6-1 hardcoded English compare chrome: **RESOLVED** in 7.1
- C-P5-L1 fallback banner i18n: not touched in 7.1 (banner not on compare page); **PROBE deferred to next i18n surface touch**

## Commit

```
git commit -m "07 Website Phase 7.1 — compare page i18n chrome (4 keys × 3 langs, C-P6-1 absorbed)"
```
