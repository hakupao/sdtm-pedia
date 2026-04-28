# Phase 9.13 reviewer prompt — `feature-dev:code-architect` (architectural design review)

> **You are dispatched as a Rule D adversarial reviewer**, NOT a designer. Your job is to find design flaws, scope errors, and architectural risks in the Phase 9 polish bundle that the writer (main session, opus) just shipped at commit `e89da8a`. The writer cannot review their own work — you are the second set of eyes.
>
> **Family rotation**: this is the 2nd burn of feature-dev family in the website lane (Phase 5 = `feature-dev:code-reviewer`); you (`code-architect`) are a NEW agent within the family. Cross-family vs Phase 8 (`pr-review-toolkit:silent-failure-hunter`) ✓.

## Context — required reading

Read in this order:

1. `/Users/bojiangzhang/MyProject/SDTM-compare/.work/07_website/phase9/PLAN.md` — full phase plan, 199 lines, includes archeology finding §0.
2. `/Users/bojiangzhang/MyProject/SDTM-compare/.work/07_website/phase9/_progress.json` — task table + metrics.
3. `/Users/bojiangzhang/MyProject/SDTM-compare/.work/meta/website_phase8_to_phase9_handoff_2026-04-29.md` — incoming carryover (C-P8-1..6 + C-P7/6/-* + C-P5-L2).
4. `git show --stat e89da8a` then `git show e89da8a -- web/` (the commit you're reviewing).
5. The 21 changed/new files in commit `e89da8a` (web/ + .work/07_website/phase9/).

## Scope of your review

Phase 9 is "pre-public-release polish + QA bundle". Daisy ack'd Option D = combine:
- (A) Phase 8 carryover C-P8-1..5 + C-P8-6 (mobile UX deferred)
- (B) selective Phase 6/7 deferred polish (C-P5-L2 / C-P6-6 / C-P6-7 / C-P7-6)
- (C) master plan §"Phase 10 — QA + Polish" (10.1 Lighthouse / 10.2 focus-visible CSS / 10.3 cross-browser / 10.5 final verify)

Plus Phase 9 archeology finding (master plan §"Phase 8 Downloads" + §"Phase 9 CF Deploy" already shipped 4-28).

## Stress dimensions D1-D7 (apply each with a "what could silently break in production?" lens)

### D1 — E2E infrastructure correctness (Tasks 9.1+9.2)
- Is `'npm run build && npm run preview'` as a single playwright `webServer.command` actually robust? What happens if `npm run build` fails — does playwright wait until timeout? Does the preview server hang on a stale port?
- `reuseExistingServer: !process.env.CI` — is `CI` env var the right gate? CF Pages doesn't set `CI`; only GitHub Actions / standard CI runners do. A user running `CI=1 npx playwright test` locally now skips reuse — is that expected friction or a regression?
- 9.2 promotes synthetic keydown to `page.keyboard.press('Control+k')` after `page.locator('body').click()`. Was the body-click necessary? Could the click itself dismiss any default-open modal/menu and create flake?
- The ⌘K hint button is the hydration proxy — does the test depend on its specific aria-label `"Open search"`? If a future i18n pass localizes that aria-label (currently English-only — covered by Phase 8 D-P8-6 deferral), does the e2e silently break?

### D2 — SearchOverlay a11y completeness (Tasks 9.3+9.4)
- Focus return: `previousFocusRef.current = document.activeElement` on Cmd+K open; is there a race where overlay close runs before the ref is set (e.g., user presses Esc while still in capture phase)? The ref is cleared after restoring — is null-check on subsequent close cycle correct?
- The aria live region uses `role="status"` + `aria-live="polite"` — is this WAI-ARIA compliant for "search results announcement"? Some recommendations specify `role="region"` + `aria-live="polite"` + `aria-atomic="true"`. Should we use the more verbose form?
- 1-retry backoff: `setTimeout(() => tryImport(1), 1000)` — does this leak across remount? If user closes overlay before the retry fires, the result still mutates `pagefindRef.current` after unmount. Is that a memory issue or just dead state?
- New i18n keys `search.results.label` (zh "个结果" / en "results" / ja "件の結果") — does the en form ("1 results") sound natural? Should it be "result(s)" to handle pluralization?

### D3 — remark plugin fixture coverage (Task 9.7)
- 6 fixtures: throw-on-no-lang, rewrite, changelog-route, anchor, drop-wrapper, absolute-URL. What's NOT covered? Bare anchor (`#foo`)? Mailto/tel links? Self-referential link to same file's own slug?
- The fixtures construct mdast nodes by hand — is the shape exactly what `unist-util-visit` expects? Specifically, does `index` need to be set on the parent's children array, or is it derived?
- Real-world cross-ref shape sample: any frontmatter-aware vs frontmatter-less cases I might be missing?

### D4 — zod schema design (Task 9.8)
- `DownloadsSchema.bundles.length(4)` — hardcoded count to 4 platforms. If we ever add a 5th (or remove notebook), the schema fails. Is this rigidity desired (catches accidental drops) or fragile (blocks legitimate scope changes)?
- `filename` regex `/_bundle_v\d+\.\d+(\.\d+)?\.zip$/` — does it tolerate `v1.0-rc1` or `v2.0.1-beta`? Should it?
- `compare-dimensions.json` schema has `values: z.record(z.string(), z.string())` — that allows any platform key. Should we constrain to the 4 platform enum like Downloads has?
- The migration strategy: schemas exist parallel-only, no consumers parse via schema yet. Is that the right balance, or should at least one consumer migrate to demonstrate the path?

### D5 — Redirect HTML wrapper (Task 9.9)
- `<meta http-equiv="refresh" content="0;url=...">` instead of `Astro.redirect()`. Is the behavioral difference benign? Astro.redirect sends Response with body — what status code? My investigation showed `dist/index.html` already uses meta-refresh-content-2 in built output, so the runtime Effect should match.
- `data-pagefind-ignore="all"` — is `="all"` the correct value for the attribute? Pagefind docs say bare `data-pagefind-ignore` (no value) suffices but accepts `"all"` as alias.
- Trailing-slash canonical preservation — verify `dist/index.html` post-9.9 emits `<link rel="canonical" href="https://sdtm-pedia.pages.dev/zh/">` (with trailing slash) per Phase 7.5 D-P7-3 fix. The new template uses `${target}` where `target = '/zh/'` — so trailing slash IS preserved.
- The `<a>` fallback for no-JS browsers ("Redirecting from `/` to `/zh/`") — is `<code>` semantic correct here?

### D6 — Focus-visible CSS scope (Task 9.5)
- `*:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }` — universal selector. Does Tailwind v4 reset `outline: 0` on `*:focus`? If so, our rule fires only when `:focus-visible` matches (keyboard nav), which is what we want.
- Dark mode: `--accent` is `#60a5fa` which on `--bg: #0d0c0a` has ratio ~7:1, comfortably AA. Light mode: `--accent: #1e40af` on `--bg: #f8f5ef` ~10:1. ✓
- Are there elements where the outline conflicts with existing borders (e.g., search input which already has `border-b border-rule`)? Visual smoke deferred to manual.

### D7 — Phase 9 archeology + scope decision (§0)
- The archeology finding pivots Phase 9 from "Downloads Pipeline" to "QA + Polish renumbered". Is the carryover absorption matrix in PLAN.md §5 accurate and complete?
- C-P9-* enumeration: are 9 IDs the right granularity? Some (C-P9-9 third-party-cookies) are explicitly ACCEPTED — these don't need to be numbered carryover. Should they be downgraded to "documented as accepted"?
- The Lighthouse 91/73/100 baseline acceptance — is this the right call for "release-grade" Phase 9 (Daisy ack "还可以"), or should at least the 1-2 cheapest fixes (label-content-name-mismatch on ⌘K button — likely 5 LOC) be done in this phase?

## Pass criteria

- 0 HIGH findings UNLESS the finding is fixable in a small post-review patch and you'd recommend doing so before declaring Phase 9 done (in which case → CONDITIONAL_PASS, fixable → upgrades to PASS post 9.14 fix bundle).
- MEDIUM findings: triage as same-phase fix (if cheap & co-located) OR carryover (C-P9-*).
- LOW findings: typically carryover.

Output structure:

```
## Reviewer verdict: PASS / CONDITIONAL_PASS / FAIL

## Findings (H/M/L count)

### F-1 [HIGH/MEDIUM/LOW] — short title
- Where: file:line
- What: 1-2 sentence description
- Why it matters: ...
- Fix path: same-phase patch (~N LOC) / carryover C-P9-N / accepted

### F-2 ...
...

## Recommendations for 9.14 fix bundle (if CONDITIONAL_PASS)
...

## Process notes (Rule A/B/C/D audit trail)
- Rule D: writer = main session opus / reviewer = feature-dev:code-architect (this report). Cross-family ✓ vs phase 8 pr-family. NEW agent within feature-dev family ✓.
- Rule A: any translation-style work? (Phase 9 added 6 strings — search.results.label + search.unavailable × 3 langs. Any semantic spot-check warranted?)
- Rule B: any failures archived? (None expected; if failures, report.)
- Rule C: retro pending in close handoff doc.

## Pass-criteria check
- ✓/✗ "0 HIGH findings UNLESS fixable in small patch"
```

## What you DON'T do

- Do NOT run `npm test` / `npm run build` / `npx playwright test` — you don't have Bash. Trust the metrics in PLAN.md / _progress.json / commit message as ground truth (writer reported tsc 0 / vitest 46/46 / e2e 7/7 against preview / build 31 pages / Pagefind 0 warnings / 4 GH URLs HTTP/2 302). If you suspect a metric is wrong, flag as a finding for the main session to verify; don't try to verify yourself.
- Do NOT fix any code yourself; this is a review pass.
- Do NOT extend Phase 9 scope beyond the 12 tasks listed; if you find issues outside scope (e.g. in the unrelated `M CLAUDE.md` 06-deep-verification round-12 prep state), flag and skip.

## What you DO

- Read carefully. Spot-check 2-3 files line-by-line for design flaws.
- Cross-reference PLAN.md decisions against actual implementation.
- Apply D1-D7 stress dimensions; document findings.
- Recommend a 9.14 fix bundle path IF appropriate (HIGH + small patch).
- Output verdict + structured findings.

Begin.
