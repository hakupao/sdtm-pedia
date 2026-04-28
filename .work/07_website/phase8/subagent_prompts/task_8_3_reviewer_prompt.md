# Task 8.3 Reviewer Subagent Prompt

> **Agent**: `pr-review-toolkit:silent-failure-hunter` (substituted from handoff's `superpowers:silent-failure-hunter` — that agent does not exist as registered; pr-review-toolkit's silent-failure-hunter is the equivalent lens)
> **Phase**: 07 Website Phase 8 — Search (Pagefind)
> **Task**: 8.3 End-of-Phase reviewer pass
> **Date**: 2026-04-29
> **Repo**: `/Users/bojiangzhang/MyProject/SDTM-compare`
> **Branch**: `main` (HEAD = `4206203`, +1 commit ahead of origin/main)

## Mode

Read-only adversarial review. **Do not** edit any source files. Write only the evidence report at the path below.

## Why your lens (silent-failure-hunter) for this phase

Pagefind has a high silent-failure surface. `code-reviewer` (Phase 7) catches positive issues — what's there but wrong. You catch what's missing or what fails *quietly*: build green but index empty, search UI renders but result URLs broken, dynamic import path wrong but only fails in production hosting, results returned but escapes mishandled. This is the failure class for a search-index introduction phase.

Phase 8 is the first phase to ship search. The risk is something works in dev/test but silently breaks in production. Find those.

## Scope

Single commit on `main` ahead of origin/main: **`4206203`** "07 Website Phase 8.2 — SearchOverlay".

Diff: `git show 4206203` (4 files, +160 LOC):
- `web/src/components/react/SearchOverlay.tsx` (NEW, 102 LOC) — the React island
- `web/src/components/react/SearchOverlay.test.tsx` (NEW, 21 LOC) — 2 vitest cases
- `web/tests/e2e/search.spec.ts` (NEW, 27 LOC) — 1 playwright e2e
- `web/src/components/astro/TopNav.astro` (MODIFIED, +9 LOC) — mount + ⌘K hint button

Pre-existing context (already verified):
- Pagefind 1.5.2 build pipeline produces 17 artifacts in `web/dist/pagefind/` (Task 8.1 PASS — see `.work/07_website/phase8/evidence/checkpoints/task_8_1_report.md`)
- All Phase 7 baselines preserved: tsc 0, vitest 32→34, e2e 6/6→7/7 (against `npm run preview`), build 31 pages
- Site uses `build.format: 'directory'` so canonical URLs end with trailing slash

## Required reading

In order (the brief is self-contained so you don't need conversation history):

1. `.work/07_website/phase8/PLAN.md` — Phase 8 Tier 3 plan trace (3 tasks, 3 entry decisions, exit criteria)
2. `.work/07_website/phase8/evidence/checkpoints/task_8_1_report.md` — Pagefind verify (passed)
3. `.work/07_website/phase8/evidence/checkpoints/task_8_2_report.md` — SearchOverlay implementation report (3 spec adjustments Adj-1/2/3 + 2 blockers B-1/B-2)
4. `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` lines 2483-2645 — master plan §"Phase 7 — Search (Pagefind)" Tasks 7.1+7.2 (the spec being implemented; renumbered to Phase 8)
5. The 4 changed files in commit `4206203`

For Phase 7 review patterns + lessons (informs your style — DO NOT mimic verdict though):
6. `.work/07_website/phase7/evidence/checkpoints/phase_7_reviewer_report.md` — Phase 7 reviewer's structured-brief format

## Stress dimensions (find issues here)

### D1 — Silent index failures
- Build green but Pagefind index actually empty?
- Pagefind warnings in build output ignored or downgraded?
- Language detection wrong (e.g. `lang="zh-CN"` vs `lang="zh"`)?
- Root selector wrong — Pagefind indexing nav/footer instead of content?
- Index built for wrong content scope (e.g. dist/some-other-dir)?
- What does `dist/pagefind/pagefind-entry.json` contain — does it match what `pagefind.js` will load at runtime?

### D2 — Broken result URLs
- Pagefind result `r.url` paths actually resolve to live pages?
- Trailing-slash matches `build.format: 'directory'` (or canonicalizes consistently)?
- `<a href={r.url}>` produces clickable links — what about cross-lang nav (a search on `/zh/...` returns `/en/...` results)?
- Hash anchors lost?
- Encoded characters?

### D3 — Dynamic import path correctness
- `/pagefind/pagefind.js` resolves under CF Pages production hosting? Asset path consistent dev/preview/prod?
- The dynamic import wrapper (`pagefindUrl` const + `/* @vite-ignore */`) — does Vite static analysis still trip on it under any condition (e.g. SSR pre-render)?
- The `.catch(() => {})` swallows ALL errors silently — is that the right call for "Pagefind missing" vs e.g. network error vs CORS vs MIME-type mismatch?
- Pagefind module shape — does `pagefindRef.current.search(q)` match the actual API surface the module exposes? (verify against built `dist/pagefind/pagefind.js` if needed)
- `r.data()` is `await`ed — does the module export `data()` per result, or per page?

### D4 — A11y of search overlay
- `role="searchbox"` on a `type="search"` input — redundant or correct?
- Focus management: input gets focus on open. Where does focus return on close (Esc)?
- Trap focus inside the overlay or not? Tab navigation behavior?
- Backdrop click closes — keyboard equivalent?
- Result list: `<li>` items inside `<ul>` — semantics OK? `<a>` inside `<li>` — pattern OK?
- Screen reader announcement: when results populate, is there a live region? Does the user hear "5 results" or just nothing?
- The ⌘K hint button: `aria-label="Open search"` — does this convey the keyboard shortcut?
- The `placeholder="Search docs..."` is English-only — accepted Phase 8 deferral, OK.

### D5 — Plan adherence to master plan §"Phase 7 — Search"
- 3 spec adjustments documented in `task_8_2_report.md` (Adj-1/2/3) — each justified?
- Adj-1: dynamic import indirection — necessary or paranoid? Did Vite actually fail on the literal form, or was it a different error?
- Adj-2: e2e via ⌘K button click instead of raw `page.keyboard.press('Meta+k')` — is this circumventing a real issue (headless chromium keyboard event delivery to React document listener) or hiding an actual bug?
- Adj-3: aria-label addition — pure parity, fine.

### D6 — Anything you find on inspection
silent-failure-hunter's job is finding what *isn't* checked. If you spot something none of D1-D5 covers, raise it.

## Verification you can run (no edits)

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
git show 4206203 --stat
git show 4206203 -- web/src/components/react/SearchOverlay.tsx
git show 4206203 -- web/src/components/astro/TopNav.astro

cd web
npx tsc --noEmit
npm test -- --run                            # vitest 34/34 expected
npm run build                                # 31 pages + Pagefind index
ls dist/pagefind/                            # 17 artifacts expected
cat dist/pagefind/pagefind-entry.json | head -30

# To exercise the e2e:
npm run preview &
sleep 3
npx playwright test tests/e2e/search.spec.ts
kill %1

# To inspect the dynamic-import path resolution:
grep -rn 'pagefind' dist/zh/guide/user-guide/index.html | head
```

You can also `curl -sI` the production CF Pages site (`https://sdtm-pedia.pages.dev/pagefind/pagefind.js`) to verify the dynamic import path will resolve in production AFTER the next push (Phase 8 close commit hasn't pushed yet; the reviewer SHOULD note that `/pagefind/pagefind.js` is presumed-to-exist post-push since CF Pages does serve `dist/` root, but confirm by checking `astro.config.mjs` `outDir` and CF Pages publish path if visible in repo).

## What to produce

Write the structured report to `.work/07_website/phase8/evidence/checkpoints/phase_8_reviewer_report.md`. Format per Phase 7 reviewer report (453 lines at `.work/07_website/phase7/evidence/checkpoints/phase_7_reviewer_report.md` for style reference):

```
# Phase 8 — End-of-Phase Reviewer Report

> **Reviewer**: `superpowers:silent-failure-hunter` ...
> **Date**: 2026-04-29
> **Scope**: Phase 8 = Pagefind search, 1 commit `4206203`
> **Mode**: read-only adversarial silent-failure-focused review
> **Branch**: `main`

## Verdict

PASS or CONDITIONAL_PASS or FAIL.

## What Phase 8 did well (acknowledge first)

[~5-8 bullets]

## Findings

### F-N [SEVERITY] Title
**Class**: ...
**File**: web/src/components/...:N-M
**Concrete evidence**: code excerpt or curl output or test trace
**Why it matters**: ...
**Fix**: ...

[Repeat per finding]

## Recommendations for Phase 8 → Phase 9 handoff
- C-P8-* carryover IDs proposed
```

Severity ladder:
- **HIGH** — production breakage, security, blocks release. Must fix in Phase 8.5 fix bundle (mirrors Phase 7.5 pattern) OR Phase 8 PASS-with-carryover impossible.
- **MEDIUM** — visible-but-niche, defer-acceptable with carryover ID
- **LOW** — polish, defer or ignore

## Pass criteria

- All Phase 8 commits diffed against PLAN.md exit criteria
- 0 HIGH unaddressed (CONDITIONAL_PASS if HIGH exists with clear fix path)
- M-level findings deferred OK (carryover IDs C-P8-*)

## Constraints

- **Read-only**. Do not edit source. Write only the report file at the path above.
- **Do not** push, do not commit, do not modify `.work/07_website/phase8/_progress.json` (the main session updates it post-review).
- **Do not** touch anything under `.work/06_deep_verification/`.
- Be concrete: file paths + line numbers + code excerpts. Vague findings are noise.
- Be honest about confidence: silent-failure findings often need "I'd test this in production to confirm" — state that explicitly rather than overstating.
- Use ~300-450 lines (Phase 7 reviewer was 453 — that's the upper end). Brevity is fine if findings are few; verbosity isn't a quality signal.

## What "done" looks like

- Report written at `.work/07_website/phase8/evidence/checkpoints/phase_8_reviewer_report.md`
- Verdict line in §Verdict
- Per-finding severity + file:line + concrete evidence
- Recommended C-P8-* carryover IDs at the end
- Brief summary back to the main session: verdict, count by severity, top 3 things to act on
