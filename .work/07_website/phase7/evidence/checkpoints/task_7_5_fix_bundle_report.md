# Task 7.5 — Fix bundle (F-1 + F-2 + F-3 + F-4 + F-8) — CONDITIONAL_PASS → PASS

> **Date**: 2026-04-29
> **Mode**: direct main-session, mechanical fixes per reviewer recommendations
> **Trigger**: Phase 7 reviewer (`superpowers:code-reviewer`) verdict CONDITIONAL_PASS with 5-minute fix bundle path to PASS
> **Files touched**: 4

## Verdict

**PASS** — All 5 reviewer recommendations applied, verified, tests green. Phase 7 verdict upgrades from CONDITIONAL_PASS → **PASS**.

## Files modified

| File | Δ | Fix | Severity |
|---|---|---|---|
| `web/src/pages/[lang]/guide/index.astro` | 1 char | F-1 — added trailing slash to `Astro.redirect` target | HIGH |
| `web/src/i18n/ui.ja.json` | 3 lines | F-2 (`. ` → `。`) + F-3 (placeholder noun-form) + F-4 (label noun-form) | MEDIUM ×3 |
| `web/package.json` | 1 line | F-8 — `build:fresh` composes `npm run build` instead of duplicating | LOW |
| `web/src/components/react/CompareFilter.test.tsx` | 2 lines | sync test fixtures to F-3/F-4 ja string updates | (test sync) |

## F-1 fix detail (HIGH)

**Root cause**: redirect at `[lang]/guide/index.astro` emitted `Astro.redirect(\`/${lang}/guide/user-guide\`)` (no trailing slash). The redirect's auto-generated `<link rel="canonical">` then pointed to the no-slash URL, which itself 308-redirects to the with-slash content URL. Canonical-points-at-redirect chain.

**Fix**:
```diff
- return Astro.redirect(`/${lang}/guide/user-guide`);
+ return Astro.redirect(`/${lang}/guide/user-guide/`);
```

**Verification post-build**:
| Lang | Redirect canonical | Content canonical | Match? |
|---|---|---|---|
| zh | `https://sdtm-pedia.pages.dev/zh/guide/user-guide/` | `https://sdtm-pedia.pages.dev/zh/guide/user-guide/` | ✓ |
| en | `https://sdtm-pedia.pages.dev/en/guide/user-guide/` | `https://sdtm-pedia.pages.dev/en/guide/user-guide/` | ✓ |
| ja | `https://sdtm-pedia.pages.dev/ja/guide/user-guide/` | `https://sdtm-pedia.pages.dev/ja/guide/user-guide/` | ✓ |

(Reviewer's report listed `/` as a 4th affected route but Phase 7.2 verification showed `dist/index.html` already had with-slash canonical `https://sdtm-pedia.pages.dev/zh/`. So F-1 affected 3 routes, all from one source file edit.)

## F-2/F-3/F-4 fix detail (MEDIUM ×3)

**Root cause**: Phase 7.1 ja translations drifted from existing `ui.ja.json` conventions. Reviewer's Rule A coverage gap (lexical-only rubric) missed punctuation + grammatical-form drift.

**Fixes**:
```diff
- "compare.subhead": "4 プラットフォーム横並び. 次元キーワードで絞り込み.",
+ "compare.subhead": "4 プラットフォーム横並び。次元キーワードで絞り込み。",

- "compare.filter.placeholder": "次元を絞り込み...",
+ "compare.filter.placeholder": "次元の絞り込み...",

- "compare.filter.label": "次元を絞り込む"
+ "compare.filter.label": "次元の絞り込み"
```

**Convention alignment**:
- F-2 「。」 matches all 5 other ja sentence-terminating positions in `ui.ja.json`
- F-3 noun-form `次元の絞り込み...` matches `search.placeholder.ja` `ドキュメント検索...` (noun + ellipsis)
- F-4 noun-form `次元の絞り込み` matches a11y label convention (screen-readers expect noun-phrase descriptions, not finite verbs)

**Test fixture sync**: `CompareFilter.test.tsx` ja branch updated to assert new strings. Old strings no longer exist anywhere in dist (verified `grep -c '次元を絞り込み\\.\\.\\.' dist/ja/compare/index.html` = 0; `grep -c '次元を絞り込む' dist/ja/compare/index.html` = 0).

## F-8 fix detail (LOW)

**Root cause**: `build:fresh` script duplicated `astro build && pagefind --site dist` instead of composing `npm run build`. Future edits to `build` would silently bypass `build:fresh`.

**Fix**:
```diff
- "build:fresh": "rm -rf .astro node_modules/.astro dist && astro build && pagefind --site dist",
+ "build:fresh": "rm -rf .astro node_modules/.astro dist && npm run build",
```

**Verification**: `npm run build:fresh` post-edit produces 31 HTML pages identical to pre-edit (verified by full e2e suite passing post-fresh-build).

## Verifications

| Check | Result |
|---|---|
| `npx tsc --noEmit` | TSC_PASS — 0 errors |
| `npm test -- --run` | 32/32 (test fixture sync absorbed cleanly) |
| `npm run build:fresh` | green, 27 indexed pages, 31 HTML emitted |
| `grep` 3 redirect canonical hrefs in dist | all 3 match content-page canonicals (with trailing slash) |
| `grep` ja compare new strings in dist | all 3 new strings present |
| `grep -c` ja compare OLD strings in dist | 0 / 0 (removed cleanly) |
| `npx playwright test` | 6/6 passed |

## Carryover delta

- C-P7-2 redirect-canonical chain (F-1): **RESOLVED** in 7.5
- C-P7-3 ja convention drift (F-2/F-3/F-4): **RESOLVED** in 7.5
- C-P7-9 build:fresh composability (F-8): **RESOLVED** in 7.5

Remaining C-P7-* carryover for Phase 8:
- C-P7-1 Astro i18n soft-404 (LOW, accept-as-is, documented in README) — no action
- C-P7-4 C-P6-2 WCAG analysis (MEDIUM, audit-trail thinness) — to be addressed in Phase 7 close handoff (write the deferral rationale)
- C-P7-5 master plan §"Phase 7" not yet annotated (LOW) — to be addressed in Phase 7 close
- C-P7-6 build noise 4 redirect routes (LOW) — defer
- C-P7-7 Rule A rubric expansion (LOW, process improvement) — Phase 8+ adoption
- C-P7-8 README CF auto-deploy claim verification (LOW) — verify-or-amend before external announcement
- C-P7-10 CF preview probe checklist (LOW, process artifact) — Phase 9 deploy phase

## Reviewer verdict upgrade

Pre-fix: CONDITIONAL_PASS (1 HIGH + 4 MEDIUM + 5 LOW)
Post-fix: **PASS** (0 HIGH + 1 MEDIUM remaining [C-P7-4 audit-trail, addressed in handoff] + 7 LOW remaining [all carryover-acceptable])

## Commit

```
git commit -m "07 Website Phase 7.5 — reviewer fix bundle (F-1 HIGH + F-2/3/4 MEDIUM ×3 + F-8 LOW): redirect canonical trailing-slash + ja i18n convention + build:fresh composability"
```
