# Website Build — Phase 6 → Phase 7 Handoff

> **Date**: 2026-04-28
> **Outgoing session**: Phase 6 (Multi-dim Comparison Page) — 4 commits on `main`
> **Incoming session**: Phase 7 (master plan §"Phase 7" — TBD per `docs/superpowers/plans/2026-04-27-sdtm-release-website.md`)
> **Branch**: `main`. HEAD = `0b0e822`. Not pushed.

## What's done — Phase 6

| Commit | Subject |
|---|---|
| `b25b834` | 07 Website Phase 6.0 — remark plugin for .md cross-refs + PLATFORM_COMPARISON slug rename + e2e link-resolution strict (C-P5-1 + C-P5-2 absorbed) |
| `c52b4a7` | 07 Website Phase 6.1 — CompareFilter React island + overwrite [lang]/compare.astro real page (path-based i18n per plan deviation) |
| `362b401` | 07 Website Phase 6.2 — expand compare-dimensions to 9 dims (preview shows first 4 via slice) |
| `0b0e822` | 07 Website Phase 6.4 — reviewer fix bundle (H1 + H2 + M3): catchall changelog skip + plugin widen drops directory refs + e2e strict over 8 routes + landing tbody count guard |

(Intervening `72ef5a9` was unrelated round-10/11 deep-verification cleanup, not part of Phase 6 scope.)

## End-of-Phase-6 review verdict

`oh-my-claudecode:critic` (Rule D cross-family — first-burn `oh-my-claudecode` family on website lane after `pr-review-toolkit` ×4 + `feature-dev` ×1): initial **CONDITIONAL_PASS H=2 M=5 L=4** (report in `.work/07_website/phase6/evidence/checkpoints/phase_6_reviewer_report.md`, 457 lines). Both HIGH findings (H1 dual-route changelog SEO dupe + H2 `./self_deploy/` dead link in 3-lang README) were exact "build-green-but-data-broken" pattern Phase 5 G-P5-2 lesson warned about — Phase 6 reproduced the lesson.

**Phase 6.4 fix bundle applied** (commit `0b0e822`, ~25 LOC across 4 files): H1 + H2a (plugin) + H2b (e2e) + M3 (defensive). Both HIGHs verified directly via dist HTML + sitemap diff + e2e 6/6 over expanded 8-route + landing tbody count assertion. Reviewer brief upgrade path satisfied → **effective PASS** for Phase 7 entry. M-level + L-level findings deferred per reviewer recommendation.

## Pre-flight decisions made at Phase 6 start (carryover from Phase 5 handoff)

1. **C-P5-1 + C-P5-2 absorbed into Task 6.0 entry** — markdown cross-link rewrite plugin (~30 dead `[X](FOO.md)` cross-refs) + PLATFORM_COMPARISON `slug: compare` → `slug: platform-comparison` rename. Both done in `b25b834`.
2. **Plan deviation**: `/[lang]/compare` (path-based i18n) instead of master plan §6.1 Step 3 root + `?lang=` query. 4 reasons in PLAN.md L12-21 (Phase 4 CTA + Phase 5 stub + project-wide `prefixDefaultLocale: true` + verbatim plan would break existing CTA). Done in `c52b4a7`.
3. **Reviewer slot**: `oh-my-claudecode:critic` (Opus, READ-ONLY, deep adversarial framing). Cross-family from `pr-review-toolkit` (×4) AND `feature-dev` (×1). Done in `0b0e822` post-6.3 dispatch.

## §1 Retrospective — what went well (Rule C R-P6-*)

- **R-P6-1** Reviewer brief explicit new-dimension enumeration (D1-D7) FORCED focused stress per Phase 5 G-P5-4 lesson. Generic brief on Phase 5 still caught 3 HIGHs; structured D1-D7 brief on Phase 6 caught 2 HIGHs + 5 MEDIUMs + 4 LOWs incl. the dual-route SEO finding that no per-task evidence report had even hinted at. The structured brief is ~3× more findings per dollar.
- **R-P6-2** Pre-flight context in subagent prompts (Astro 6 version, content schema, cross-ref inventory, pattern probe) eliminated the most common subagent failure mode. Both 6.0 and 6.1 subagents reported "no divergence from main session's confirmed patterns" — saving ~1 review iteration each.
- **R-P6-3** Subagent verbatim-copy contract held perfectly for 6.0 + 6.1 (full file bodies in briefs). Diffing committed code vs brief code blocks shows pixel-identical algorithm + 1 surgical addition (`aria-label` on CompareFilter input — flagged as the ONE deviation, justified for a11y).
- **R-P6-4** Cache-clear-before-rebuild lesson surfaced organically (H2 first attempt didn't apply because Astro content-cache held stale AST). Caught at the 6.4 verify step before commit, fixed cleanly, documented as C-P6-8. The ~10 min spent diagnosing now saves N future plugin-edit-without-cache-clear silent regressions.
- **R-P6-5** Path-based i18n plan deviation was correct. PLAN.md flagged it explicitly with 4 reasons, brief reinforced it, subagent followed it. Zero "but the master plan says X" friction. Adversarial reviewer (D3) confirmed the deviation's necessity — would have produced redirect-or-dead-link otherwise.
- **R-P6-6** Tier 3 trace artifacts (PLAN.md, _progress.json, 4 evidence checkpoints, 3 subagent prompts, reviewer report) all preserved + committed in 6.4. Future archeology can reconstruct the full decision chain from `git log --follow .work/07_website/phase6/`.
- **R-P6-7** Realist Check downgrade (H1 dropped from CRITICAL → HIGH because internal-company audience pre-public-release) prevented the reviewer's verdict from over-blocking. The fix was still applied because cheap (~5 LOC), but the framing kept the team from treating a SEO dupe as a launch blocker.

## §2 Gaps (Rule C G-P6-*)

- **G-P6-1** Phase 6.0 evidence flagged `./self_deploy/` as a known gap "for 6.3 reviewer to decide" but the 6.0 commit landed anyway. The Phase 5 G-P5-2 lesson was: defer the "build green = PASS" verdict until the consuming feature lands. Phase 6's twist: defer "PASS" until the **expanded e2e route coverage** lands — the Phase 6.0 e2e strict mode was strict-but-narrow (5 routes); broadening route coverage to surface new failure modes is itself a Phase deliverable. **Lesson for Phase 7**: when a phase introduces strict checking infrastructure, the same phase should expand the cases under check, not defer to the next reviewer pass.
- **G-P6-2** Astro content-collection cache invalidation is not in any project doc. First 6.4 build silently produced unchanged output despite plugin source being correct. Required `rm -rf .astro node_modules/.astro dist`. Need to either add `npm run build:fresh` OR document the trap in `web/README.md` (does not exist; create one in Phase 7 alongside CONTRIBUTING.md). Tracked as C-P6-8.
- **G-P6-3** No `web/CONTRIBUTING.md` or `web/README.md`. Local-dev tribal knowledge (kill stale `astro dev` for e2e + cache-clear-before-plugin-rebuild + `prefixDefaultLocale: true` + lang-neutral entry handling) lives only in evidence reports. New contributor onboarding will be harder than necessary. Phase 7 candidate.
- **G-P6-4** Phase 6 grew the i18n debt instead of reducing it. CompareFilter island + compare.astro page chrome are hardcoded English. Reviewer M1 + M4 raised this; we deferred to Phase 7 C-P6-1. Pattern: when adding NEW user-facing surface, plan for 3 langs from day 1, even if the strings ship in English first (just thread the i18n mechanism through). Phase 7 lesson: budget i18n work on every new surface, not just at the "i18n polish" milestone.
- **G-P6-5** Reviewer adversarial mode found 4 things THOROUGH mode wouldn't have. The brief invited adversarial framing explicitly. **Pattern to keep**: always invite adversarial framing for end-of-phase reviewers when infrastructure (vs incremental UX) is being introduced. Defer adversarial framing only when the phase is purely additive UX (low risk).

## §3 Decisions (Rule C D-P6-*)

- **D-P6-1** **Plan deviation `[lang]/compare.astro` over root `compare.astro` + `?lang=`** — confirmed correct (D3 reviewer pass). Trade-off: master plan template has to be re-read with PLAN.md `Plan deviation flag` overlay. Marginal cost; keeps consistent path-based i18n architecture. Future plan deviations: PLAN.md is the right place for the override notice (not a separate file).
- **D-P6-2** **Catchall `[...slug].astro` skips `slug: 'changelog'`** — chose Option 1 from reviewer (skip emission) over Option 2 (`<link rel="canonical">` on the catchall variant). Cleaner: dist tree has no dead `/guide/changelog/` directory, sitemap drops 6 URLs naturally, no ongoing canonical-link maintenance. Trade-off: future need for `/guide/changelog/` in any context (e.g. SDK redirect) requires re-adding the entry. Acceptable.
- **D-P6-3** **Plugin widening: skip-protocol-anchor-absolute then drop-everything-else** over reviewer's Option 1a (narrow `^(?:\.\/)?self_deploy\/` carve-out). The wider design covers `./self_deploy/` PLUS `[X](./Y/)` PLUS `[X](../../Z.md)` PLUS any future relative-but-out-of-collection ref (e.g. someone adds `[X](docs-internal/foo.md)`). Future-proof. Risk: a legitimate relative ref to a non-collection path would silently lose its `<a>`. Mitigation: collection refs are `[X](./FOO.md)` shape (UPPER_SNAKE) and rewriting still works; everything else is editorial intent unclear → drop is the right default per "fail by removing surface, not by leaving dead surface" principle.
- **D-P6-4** **Reviewer = `oh-my-claudecode:critic` (Opus + adversarial)** — chose critic-class over `code-reviewer` because Phase 6 introduces *infrastructure* (plugin, island, e2e strict, slug rename) that historically surfaces issues phases later. The adversarial framing produced 5 findings that THOROUGH mode wouldn't have (per reviewer §"Verdict Justification"). **Pattern locked**: critic-class for infrastructure phases; code-reviewer for UX-only phases.
- **D-P6-5** **Phase 6.4 included defensive M3 fix** (LANDING_PREVIEW_KEYS + e2e tbody count) over deferring it to Phase 7. Cost: 8 LOC + 1 e2e assertion. Benefit: locks landing-preview shape against silent regression in the same risk class as G-P5-2 + H1 + H2. Including a defensive Medium fix in a HIGH-fix bundle is cheap when the testing infrastructure is already being touched.
- **D-P6-6** **Subagent_prompts/ trace dir committed in 6.4 (deferred from per-task commits)** — the Tier 3 plan-trace artifacts were created during 6.0/6.1/6.3 dispatch but each per-task commit only added the report file, not the prompt. Rolling them up at Phase 6 close is cleaner: one chronological commit shows "all subagent prompts archived as part of phase closeout" rather than fragmenting prompt commits across 4 commits with redundant evidence-vs-prompt updates. Accepted for Phase 7+: defer prompt-archive commits to phase close unless a per-task evidence report references the prompt directly.
- **D-P6-7** **Cache invalidation incident NOT a regression archive (Rule B `failures/`)** — debated whether to write `failures/task_6_4_attempt_1.md`. Decided no: the first attempt was technically a build-green/algorithm-correct case where the cache layer hid the change. It wasn't a "wrong approach abandoned"; it was a "correct fix not visible until cache clear". Documented as C-P6-8 carryover instead. Phase 7 may revisit Rule B threshold for "cache-stale" vs "approach-wrong" failure types.

## Carryover for Phase 7 (consolidated, IDs C-P6-*)

### From reviewer findings (M-level deferred, L-level deferred or transitively resolved)

- **C-P6-1** Hardcoded English UI chrome on `/[lang]/compare` (M1 + M4) — page h1, subhead, filter input placeholder, filter input aria-label all hardcoded English. Widens C-P5-L1 carryover scope from "fallback banner" to "all hardcoded English UI chrome incl. fallback banner + compare page chrome + filter input chrome". 4 keys to add: `compare.title`, `compare.subhead`, `compare.filter.placeholder`, `compare.filter.label`. Mechanical: existing `getUIStrings(lang)` infrastructure handles it.
- **C-P6-2** Color-only winner signaling on `/[lang]/compare` table (M5) — `text-accent font-bold` on winner cells fails WCAG SC 1.4.1 strict reading. Add `<span className="sr-only">winner</span>` (per-lang via M1 fix) or visible `★` marker. Touches `CompareFilter.tsx` only.
- **C-P6-3** Missing `<link rel="canonical">` site-wide — all routes lack canonical. Pre-public-release SEO baseline. Generic gap: emit `<link rel="canonical" href={Astro.url.pathname}>` (or normalized) in `BaseLayout.astro` so every page has it for free.
- **C-P6-4** `playwright.config.ts reuseExistingServer: true` (L2) — burned 6.0's first e2e attempt with stale dev. Three workarounds: (a) `reuseExistingServer: !process.env.CI`, (b) `pretest:e2e` script `lsof -ti:4321 | xargs -r kill || true`, (c) document in `web/README.md`. Pick one.
- **C-P6-5** `/[lang]/guide/platform-comparison` vs `/[lang]/compare` redundancy (M2) — two different views (static doc vs interactive filter) of overlapping data; no signposting between them. Three options: (a) cross-link "Filter interactively →" / "See the full article →", (b) drop `/guide/platform-comparison` from sidebar enumeration so `/compare` is canonical, (c) merge content.
- **C-P6-6** No vitest for plugin lang-neutral throw guard — safeguard is dead code today (DEMO_QUESTIONS has 0 `.md` cross-refs). Add fixture-level vitest with `frontmatter.lang === undefined` + `.md` URL → expect throw. Locks contract before a future contributor adds such a cross-ref and breaks build at runtime.
- **C-P6-7** No schema validation on `compare-dimensions.json` — TS-typed at consumer site only. A malformed entry (missing `winners` array, extra platform key, etc.) would crash React at hydration. Add zod schema or content-collection-style schema validation at JSON load.

### From 6.4 fix process (NEW)

- **C-P6-8** Astro content-cache invalidation — plugin source edits do NOT auto-invalidate `web/.astro/` + `node_modules/.astro/data-store.json`. After plugin (or any markdown processor) edit, run `rm -rf web/.astro web/node_modules/.astro web/dist && npm run build`. Phase 7: add `package.json` `"build:fresh"` script + document in `web/README.md` (creates G-P6-3 web/README too).

### Pre-existing carryover NOT touched in Phase 6

- **C-P5-M2** DocsSidebar drawer ViewTransitions — DEFER (no VT enabled).
- **C-P5-M3** TopNav trailing-slash hosting — Phase 6 plan committed to "VERIFY during Phase 6 CF preview deploy" but no evidence of CF preview verification in commit log. Phase 7 must verify before public-release distribution. The astro config `build.format: 'directory'` emits `/foo/` URLs; sidebar emits `/foo` (no slash) hrefs — relies on CF redirect. Manual verify on live `https://sdtm-pedia.pages.dev/` or a feature-branch preview.
- **C-P5-L2** Empty TOC `<aside>` guard — DEFER (cosmetic, xl-only).

### Inherited build noise

- 4 "no `<html>` element" warnings on `/`, `/zh/guide/`, `/en/guide/`, `/ja/guide/` redirect routes (L4) — pre-Phase-6, intentional `Astro.redirect()` pages. Cosmetic; suppress in Phase 7 or accept noise.

## Working state — Phase 6 close

- **Branch**: `main`. HEAD = `0b0e822`. Not pushed.
- **`web/` tree**:
  - `BaseLayout` + `LandingLayout` + `DocsLayout` all available for Phase 7 to consume.
  - `TopNav` + `Footer` + `EnterFadeScript` + `LangSwitcher` + `ThemeToggle` reusable.
  - `i18n/helpers.ts` `UIKey` type-safety + 3 ui.*.json key parity (vitest enforced).
  - Content collection `guide` schema strict on `slug:` (required); `lang:` optional. Add new docs at `ai_platforms/release/v1.0/*.md` with `slug:` to be picked up automatically. Catchall route `/[lang]/guide/[...slug]/` emits except for `slug: 'changelog'` (dedicated `/[lang]/changelog` route owns it).
  - Remark plugin `web/remark-md-link-rewrite.mjs` rewrites `[X](./<UPPER_SNAKE>[.lang].md(#hash)?)` → `/${entryLang}/guide/<lowercase-hyphenated>${hash}` for top-level guide-collection docs. Out-of-collection refs (relative paths not matching SHAPE) drop the `<a>` wrapper. Lang-neutral entry with `.md` cross-ref throws (fail-loud).
  - React island `CompareFilter` (`web/src/components/react/CompareFilter.tsx`) + dedicated landing route `/[lang]/compare/` with full 9-dim table + search filter. Landing `ComparePreviewSection` shows first 4 dims via `LANDING_PREVIEW_KEYS`.
  - 9-dim `compare-dimensions.json` (was 4 in Phase 5).
- **Test status**: tsc 0 errors / vitest 31/31 / e2e **6/6 strict over 8 routes** (was 5 routes Phase 5; +3 README/{zh,en,ja} routes in Phase 6.4) / build 27 pages green (was 30 in 6.2; -3 changelog catchall variants in 6.4 H1 fix) / pagefind 3 langs indexed.
- **Evidence preserved**: `.work/07_website/phase6/{PLAN.md, _progress.json, evidence/checkpoints/*, subagent_prompts/*}` — 4 task evidence reports + reviewer report + 3 subagent prompts + plan trace.

## How the Phase 7 session should start

1. Read this handoff first.
2. Read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` Phase 7 section (line search for `## Phase 7`). Skip Phases 0-6 (done).
3. Check Phase 6 reviewer report `.work/07_website/phase6/evidence/checkpoints/phase_6_reviewer_report.md` §"Recommendations for Phase 6 → Phase 7 handoff" for C-P6-1..8 and pre-existing C-P5-* status.
4. Decisions to make BEFORE Phase 7 entry tasks:
   a. Which C-P6-* to bundle as Phase 7 entry tasks vs defer further? Recommend: C-P6-1 (i18n chrome) + C-P6-3 (canonical site-wide) as entry tasks since both are mechanical and unblock confidence in public-release distribution. C-P6-8 (cache + README) as cheap onboarding deliverable.
   b. CF Pages preview deploy verification (C-P5-M3): do as Phase 7 first task or defer to release-prep? Recommend: do it first; cheap to spin up a feature-branch deploy and worth catching trailing-slash regressions before more pages land.
   c. Phase 7 reviewer slot pre-allocation. Cross-family options remaining post Phase 6: `superpowers:code-reviewer`, `pr-review-toolkit:silent-failure-hunter` (4th burn pr-family), `pr-review-toolkit:type-design-analyzer`, `oh-my-claudecode:code-reviewer` / `verifier`. Recommend: `superpowers:code-reviewer` (3rd family, no prior burn on website lane).
5. Same execution mode as Phases 1-6: subagent-driven dev for non-trivial tasks, direct-verify for trivial, end-of-phase reviewer (cross-family) before declaring done. Tier 3 trace mandatory: PLAN.md + _progress.json + per-task evidence reports + subagent prompts + reviewer report all preserved.

Family pool state at Phase 6 close: pr-review-toolkit ×4 (Phases 1, 2, 3.6, 4), feature-dev ×1 (Phase 5), oh-my-claudecode ×1 (Phase 6 critic). Phase 7 candidates: `superpowers:code-reviewer` (inaugural), `pr-review-toolkit:silent-failure-hunter` / `type-design-analyzer` (4th burn pr-family), `oh-my-claudecode:code-reviewer` / `verifier` / `critic` (2nd burn omc-family).
