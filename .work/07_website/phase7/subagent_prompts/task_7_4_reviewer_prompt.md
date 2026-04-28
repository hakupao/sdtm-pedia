# Task 7.4 — End-of-Phase-7 Reviewer Brief

> **Reviewer**: `superpowers:code-reviewer`
> **Date dispatched**: 2026-04-29
> **Phase scope**: Phase 7 = pre-public-release bundle (3 commits)
> **Branch**: `main`. Commit range: `e1737f1..a1ad23e` (3 new commits since Phase 6 close)
> **Working directory**: `/Users/bojiangzhang/MyProject/SDTM-compare`

## Adversarial framing

This is a **pseudo-infrastructure phase** (release-readiness chrome before public distribution). Per Phase 6 D-P6-4 + R-P6-5 lesson, infrastructure-class phases deserve adversarial review. Find what would embarrass the team after public distribution:
- SEO regressions invisible during dev but live on prod
- i18n key drift / parity / typography mistakes (especially JP)
- Documentation that's accurate at write-time but rots on first commit
- Plan deviation that wasn't justified strongly enough
- Anything that would force a Phase 7.5 fix bundle

If you can't find anything, say so explicitly. Don't manufacture findings.

## Phase 7 scope (3 commits)

```
3c151de 07 Website Phase 7.1 — compare page i18n chrome (4 keys × 3 langs, C-P6-1 absorbed) + Phase 7 Tier 3 trace open + Task 7.0 PASS
4047b85 07 Website Phase 7.2 — site-wide canonical link via BaseLayout (C-P6-3 absorbed)
a1ad23e 07 Website Phase 7.3 — build:fresh script + replace web/README.md placeholder with project content (C-P6-8 absorbed)
```

## Plan deviation (challenge if weak)

PLAN.md §"Plan deviation flag" rejects master plan §"Phase 7" Pagefind in favor of release-readiness bundle (CF preview + i18n + canonical + README). 4 reasons given. Re-read those reasons critically — is "release readiness" actually more pressing than search? Could you make a case for the opposite? Phase 6's plan deviation (D-P6-1) survived adversarial review; this one needs the same scrutiny.

## D1-D5 review dimensions

### D1: i18n key parity + correctness (Phase 7.1 / commit `3c151de`)

**Files**: `web/src/i18n/ui.{zh,en,ja}.json`, `web/src/components/react/CompareFilter.tsx`, `web/src/pages/[lang]/compare.astro`, `web/src/components/react/CompareFilter.test.tsx`

**Stress**:
- 4 new keys × 3 langs = 12 strings. Are translations idiomatic? Specifically the JP — `compare.title.ja` = "多次元プラットフォーム比較" (ZH-influenced compound vs natural JP); `compare.filter.label.ja` = "次元を絞り込む" (verb form for an aria-label, not noun form `次元の絞り込み`). The 7.1 report flagged the verb-form as "minor polish" but didn't fix. Adversarial: is this a deferred bug?
- Did `helpers.test.ts` actually cover the new keys via key parity? Verify by grep, not by trust.
- Are placeholder strings consistent with the convention? Check `search.placeholder` style: `搜索文档...` / `Search docs...` / `ドキュメント検索...` — all noun-phrase + ellipsis. New `compare.filter.placeholder.ja` = `次元を絞り込み...` is gerund + ellipsis. Consistency drift?
- Is there ANY hardcoded English UI chrome left on `/[lang]/compare` page? Grep dist HTML for English-looking strings on the ja variant.
- Was `BaseLayout title=` plumbed correctly through the new i18n key? Verify `<title>` in dist HTML matches the lang.

### D2: canonical URL correctness (Phase 7.2 / commit `4047b85`)

**File**: `web/src/layouts/BaseLayout.astro`

**Stress**:
- 31/31 dist HTML pages have canonical per the report. Spot-check 3 random pages — does the href actually match the pathname for each?
- Trailing-slash format: does `Astro.url.pathname` consistently produce `/zh/compare/` (with slash) or could it produce `/zh/compare` (without)? Build with `build.format: 'directory'` — verify the format on a nested route + a top-level route + the lang root.
- The 4 redirect routes (`/`, `/zh/guide/`, `/en/guide/`, `/ja/guide/`) DON'T extend BaseLayout (no `<html>` element warning). They retain Astro's built-in canonical pointing to lang-root. Is this actually correct SEO? Or should the redirect's canonical point to the page where the redirect target lives (e.g. `/zh/guide/` redirect → canonical to `/zh/`)? Walk through search-engine consolidation logic.
- `og:url` added alongside canonical — both use the same href. Is this strictly necessary? Is there a case where they should diverge? (Hint: look up canonical-vs-og:url best practices.)
- `Astro.site` fallback path: if `astro.config.mjs` `site:` is removed, the fallback returns `Astro.url.pathname` only (no protocol/host). Is this a usable canonical? Or is it actively misleading? Should the fallback throw instead?

### D3: README content-vs-tribal-knowledge accuracy (Phase 7.3 / commit `a1ad23e`)

**File**: `web/README.md` (113 lines, 5,513 bytes)

**Stress**:
- 5 tribal-knowledge sections claim accuracy against current project state. Verify each:
  - "Cache invalidation requires `build:fresh`" — does running plain `npm run build` after a remark plugin edit ACTUALLY produce stale output? Or did Phase 6.4 just have an unrelated cache-corruption issue? Test it: edit the plugin trivially, run plain `npm run build`, check dist diff.
  - "Playwright `reuseExistingServer: true`" — confirm by reading `web/playwright.config.ts`.
  - "Lang-neutral entries throw on `.md` cross-refs" — confirm by reading `web/remark-md-link-rewrite.mjs`.
  - "Adding a new doc — 4-step recipe" — does the catchall route `[lang]/guide/[...slug]/` actually pick up files added to `ai_platforms/release/v1.0/`? Or does it require additional config?
  - "Soft-404 200 + meta-refresh" — Task 7.0 verified with 3 nonsense URLs. Acceptable.
- Is `npm run build:fresh` script actually equivalent to `rm -rf` + `npm run build`? Or did the script subtly diverge (e.g. forgot a cache directory)? Compare:
  - PLAN spec: `rm -rf .astro node_modules/.astro dist && npm run build`
  - Actual `package.json`: `rm -rf .astro node_modules/.astro dist && astro build && pagefind --site dist`
  - These are equivalent IF and ONLY IF `npm run build` = `astro build && pagefind --site dist`. Verify.
- README links: every `[X](URL)` — do they resolve? Specifically the external links (Astro / React / Tailwind / Vitest / Testing Library / Playwright / Pagefind).
- README claims "Cloudflare Pages auto-deploys from `main`" — is this actually true? (You can't verify without CF dashboard access, but flag if unverifiable.)

### D4: Task 7.0 CF preview verification completeness

**File**: `.work/07_website/phase7/evidence/checkpoints/task_7_0_report.md`

**Stress**:
- 27 probes is enough? Or did we miss a class? Things NOT probed:
  - Sub-language tags (e.g. `/zh-cn/` redirect handling — none expected, but if a user types it, what happens?)
  - Trailing-slash on `/sitemap-index.xml` and `/sitemap-0.xml` and `/robots.txt` (lang-neutral resources)
  - Routes with embedded query strings (`/zh/?lang=en` — does CF preserve query through the 308?)
  - HEAD vs GET method differences (curl -I uses HEAD; some routes might 404 on HEAD but 200 on GET)
- C-P7-1 (Astro i18n soft-404) recommendation = "accept indefinitely OR document". Adversarial: dead-link checkers WILL be misled. Should this be MEDIUM not LOW? When the project gets external links from somewhere, broken inbound links will return 200, masking the rot.
- The H1 fix verification on the live site is incomplete because the live serves Astro's i18n fallback for `/zh/guide/changelog/` (200 + meta-refresh, not 404). Did Phase 6.4 H1 actually achieve its goal, or did it just move the SEO duplicate problem to a different place? Sitemap is clean (good), but external links to `/zh/guide/changelog/` would still resolve to a 200-status page.

### D5: plan deviation soundness + Phase 7 carryover handling

**Files**: `.work/07_website/phase7/PLAN.md`, `.work/07_website/phase7/_progress.json`

**Stress**:
- PLAN.md §"Plan deviation flag" gives 4 reasons. Each reason — is it strong, adequate, or hand-wavey?
- 8 carryovers from Phase 6 (C-P6-1..8). 4 absorbed (1, 3, 8 + C-P5-M3 in 7.0). 4 deferred (2, 5, 6, 7) + 1 partial (4). Is the deferral pattern justified, or is the team kicking real problems down the road?
  - C-P6-2 color-only winner signaling = WCAG 1.4.1 violation. Pre-public-release. Why is this deferred?
  - C-P6-7 no schema validation on `compare-dimensions.json` = runtime React explosion risk if a future contributor adds malformed entry. Pre-public-release. Why deferred?
- Is `superpowers:code-reviewer` actually a sound 3rd-family Rule D pick? Verify it's a different family from prior 6 reviewers.
- Was Rule A spot-check (N=3 of 12 strings) sufficient? Per CLAUDE.md "规则 A 强制" — N must be in PLAN.md. PLAN.md says N=3. Is 3/12 = 25% sample rate adequate for translation work, or should it have been higher?

## Verification artifacts to consult

- `.work/07_website/phase7/PLAN.md` — Tier 3 plan trace
- `.work/07_website/phase7/_progress.json` — task verdicts + carryover ledger
- `.work/07_website/phase7/evidence/checkpoints/task_7_{0,1,2,3}_report.md` — per-task evidence
- `.work/meta/website_phase6_to_phase7_handoff_2026-04-28.md` — predecessor retro
- `web/dist/` — fresh build output for spot-checking dist HTML

## Output format

Standard `superpowers:code-reviewer` output. Verdict + per-finding severity (HIGH / MEDIUM / LOW) + section §"Recommendations for Phase 7 → Phase 8 handoff" with carryover IDs (use `C-P7-N` namespace, continuing from C-P7-1 already established by Task 7.0).

If you find any HIGH that requires a 7.5 fix bundle before declaring Phase 7 done, flag explicitly with what to fix + how. If all HIGH/MEDIUM can defer, say so.

## Pass criteria

- 0 HIGH findings UNLESS the finding is fixable in a small post-review patch and you'd recommend doing so before declaring Phase 7 done
- M-level + L-level findings deferred OK with carryover IDs

## Constraint

Read-only. Do not edit any files. Output your review report to: `.work/07_website/phase7/evidence/checkpoints/phase_7_reviewer_report.md`
