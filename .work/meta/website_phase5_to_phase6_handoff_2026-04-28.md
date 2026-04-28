# Website Build — Phase 5 → Phase 6 Handoff

> **Date**: 2026-04-28
> **Outgoing session**: Phase 5 (Docs Reader) — 4 commits on `main`
> **Incoming session**: Phase 6 — Multi-dim Comparison Page (plan §"Phase 6", lines 2313+)

## What's done — Phase 5

| Commit | Subject |
|---|---|
| `496ae6f` | 07 Website Phase 5.1 — DocsLayout 3-col + Sidebar (mobile drawer) + TOC scroll-spy + PrevNext |
| `43d7445` | 07 Website Phase 5.2 — prose.css for markdown body |
| `56a18f7` | 07 Website Phase 5.3 — docs catchall + lang fallback + /changelog + /compare stub + link-resolution e2e (decisions 2+3) |
| `ae05afd` | 07 Website Phase 5.4 — reviewer-fix bundle (H1 PrevNext lang-neutral filter + H2 changelog fallback banner + H3 schema slug required + M1 e2e en/ja routes) |

## End-of-Phase-5 review verdict

`feature-dev:code-reviewer` (Rule D cross-family from `pr-review-toolkit`): initial CONDITIONAL_PASS H=3 M=3 L=2, **PASS post-remediation in 5.4**. All 3 HIGH + M1 fixed; M2/M3/L1/L2 deferred to Phase 6 carryover with rationale. Detail in `.work/07_website/phase5/evidence/checkpoints/phase_5_reviewer_report.md`.

## Pre-flight decisions made in Phase 5 (carryover from Phase 4 handoff)

1. **H2 download zips** — already resolved by Phase 8.1-8.3 + flag default published before Phase 5 began. Did not block.
2. **DEMO_QUESTIONS lang attribution (Option B)** — `lang:` removed from frontmatter; treat as language-neutral. Sidebar filters include lang-undefined; catchall `getStaticPaths` emits zh+en+ja paths with `fallback: false` (no banner) for lang-neutral entries.
3. **Link-resolution e2e** — added; walks `<a>` in `main`/`article` of `/zh/`, `/en/`, `/ja/`, `/zh/guide/user-guide`, `/zh/changelog`. Skips `*.md` source-file cross-refs (deferred to Phase 6 remark plugin).

## §1 Retrospective — what went well (Rule C)

- **R-P5-1** Plan code skeletons in §5.1/5.3 were 95% correct against existing patterns. Subagent verbatim-copy contract held for the layout/components task. Saved review cycles.
- **R-P5-2** Pre-flight pattern probe (Lang type, BaseLayout/TopNav prop shapes, content collection schema) before dispatch eliminated the most common subagent failure mode (guessing imports). Subagent reported "nothing diverged from main session's confirmed patterns."
- **R-P5-3** Tier 3 plan trace (`PLAN.md` + `_progress.json` + checkpoint reports + subagent prompts) caught a retroactive issue: Phase 5.1 build was technically green but content collection was silently de-duping per-lang variants. Visible only because Phase 5.3 wired the catchall and surfaced it. Without the trace, this would have been an undebuggable regression weeks later.
- **R-P5-4** Rule D cross-family reviewer (`feature-dev:code-reviewer` after 4 `pr-review-toolkit` slots) found 3 HIGH integration risks per-task reviews + structural-PASS build all missed. Cross-family family-pool lesson confirmed: same family burns out faster than people think.
- **R-P5-5** Decisions 2 + 3 made BEFORE dispatch (DEMO_QUESTIONS lang-neutral + link-resolution e2e) drove fix shape. Phase 4's H2/M1 carryover was directly addressed in 5.3 because the call was made up-front, not as a follow-up.

## §2 Gaps (Rule C)

- **G-P5-1** Astro 6 API change (`entry.render()` → `import { render } from 'astro:content'`) was not in the plan. Subagent had to discover and fix mid-execution. **Fix for Phase 6**: when next touching content-collection code, do an Astro version sanity check against installed `web/package.json` first; update plan code skeletons if API changed.
- **G-P5-2** Phase 5.1 commit landed against a silently broken collection (`generateId` slug-collision overwriting per-lang variants). Build green was a false negative — the catchall hadn't been wired so the bug couldn't surface. **Lesson**: when a phase introduces *infrastructure* (like the layout components) that depends on data the next phase will exercise, defer the "build green = PASS" verdict until the consuming feature lands. Tag 5.1 as "PASS pending 5.3 verification" not "PASS".
- **G-P5-3** Markdown body `*.md` cross-refs (`[Glossary](GLOSSARY.zh.md)`) are dead links. ~30 instances. Skipped in e2e via regex. Phase 6 must add a remark plugin to rewrite them. (C-P5-1 carryover.)
- **G-P5-4** Rule D reviewer slot pre-allocation was correct (cross-family) but the brief did not explicitly tell reviewer to stress-test the lang-neutral path. Reviewer found H1+H2 anyway because the brief listed integration cross-cuts. Future reviewer briefs should explicitly enumerate the new dimensions introduced (lang-neutral here) so they get focused attention.

## §3 Decisions (Rule C)

- **D-P5-1** Keep dedicated `/${lang}/changelog` route (not delegate to catchall). Footer links there; URL is shorter than `/${lang}/guide/changelog`. Trade: changelog.astro carries duplicate fallback logic. Marginal cost; clean URL wins.
- **D-P5-2** Schema made `slug: z.string()` required. Hard contract for all release v1.0 top-level docs. If a future doc author forgets `slug:`, build fails fast with schema error — fail-loud > silent broken collection.
- **D-P5-3** Phase 6 stub `/${lang}/compare/` ships in 5.3 as a placeholder. Phase 6 will overwrite. This was a scope expansion (originally not in plan §5.3) but justified: kept link-resolution e2e clean instead of adding a "skip /compare" rule the next reviewer would have to relearn.
- **D-P5-4** Rule D reviewer = `feature-dev:code-reviewer` (chosen over `oh-my-claudecode:code-reviewer` etc.) — cross-family vs `pr-review-toolkit` AND adjacent-domain (feature-dev knows Astro/React patterns). Outcome justified the pick.

## Carryover for Phase 6 (consolidated)

### HIGH-priority carryover

- **C-P5-1** Markdown cross-link rewrite — add remark plugin to rewrite `[X](FOO.zh.md)` → `/${currentLang}/guide/foo` (lowercase, drop lang+suffix). ~30 dead links across README/USER_GUIDE/GLOSSARY in 3 langs. Once added, REMOVE the `.md` skip in `smoke.spec.ts` link-resolution test so it starts enforcing internal markdown integrity.

### MEDIUM-priority carryover

- **C-P5-M2** `DocsSidebar` mobile drawer JS uses top-level `getElementById`. New M2-pattern instance (matches TopNav-M2 carryover). Fix when Phase 5+ enables `<ViewTransitions />` — wrap drawer init in `astro:page-load` listener or add `transition:persist`. Same diff for TopNav-M2.
- **C-P5-M3** `TopNav` link `/${lang}/guide/` trailing-slash behavior is hosting-config dependent. Verify on Cloudflare Pages deploy smoke (Phase 9). Pre-Phase-9 mitigation: link to `/${lang}/guide/user-guide` directly (skip the index.astro redirect hop).

### LOW-priority carryover

- **C-P5-L1** Fallback banner copy ("English source — translation pending") is hard-coded English in `[...slug].astro` and `changelog.astro`. Add `'fallback.banner'` key to `i18n/ui.{zh,en,ja}.json` when next touching translations.
- **C-P5-L2** `DocsTOC.astro` renders empty `<aside>` for docs with no h2/h3. Add `{filtered.length > 0 && ...}` guard. Cosmetic, xl-only.

### Cosmetic / observation

- **C-P5-2** `PLATFORM_COMPARISON.{zh,en,ja}.md` frontmatter `slug: compare` collides naming-wise (not path-wise) with the Phase 6 `/${lang}/compare/` page route. Different paths so no functional issue. Phase 6 may want to rename the doc slug to `platform-comparison` for clarity. Cosmetic.

## How the Phase 6 session should start

Read this handoff first, then read `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` Phase 6 section (lines 2313+, scope = `/compare` page with filter). Skip Phases 0-5 (done).

Decisions to make BEFORE Phase 6 Task 6.1:

1. **Remark plugin for `.md` cross-refs** (C-P5-1) — add as Phase 6 entry task or defer? Recommend: entry task. Cheap, unblocks future reviewer tests.
2. **PLATFORM_COMPARISON slug rename** (C-P5-2) — keep `slug: compare` or rename to `platform-comparison`? Recommend rename for clarity once `/compare` (Phase 6 page route) exists alongside `/guide/compare/` (PLATFORM_COMPARISON guide route).
3. **Compare stub overwrite** — Phase 5.3 created `web/src/pages/[lang]/compare.astro` as a "PHASE 6 PENDING" placeholder. Phase 6 Task 6.1 will overwrite it. Confirm overwrite (not new file alongside).

## Working state — Phase 5 close

- **Branch**: `main`. HEAD = `ae05afd`. Not pushed.
- **`web/` tree**:
  - `BaseLayout` + `LandingLayout` + `DocsLayout` all available for Phase 6 to consume.
  - `TopNav` + `Footer` + `EnterFadeScript` reusable.
  - `i18n/helpers.ts` `UIKey` type-safety + 3 ui.*.json key parity (vitest enforced).
  - Content collection `guide` schema is now strict on `slug:` (required); `lang:` optional. Add new docs at `ai_platforms/release/v1.0/*.md` with `slug:` to be picked up automatically.
- **Test status**: tsc 0 errors / vitest 29/29 / e2e **6/6** / build 34 pages green / pagefind 3 langs indexed.

Same execution mode as Phases 1-5: subagent-driven dev for non-trivial tasks, direct-verify for trivial, end-of-phase Rule D reviewer (cross-family from `pr-review-toolkit` + `feature-dev`) before declaring done. Family pool state at Phase 5 close: pr-review-toolkit ×4, feature-dev ×1. Phase 6 reviewer candidates: `oh-my-claudecode:code-reviewer`, `oh-my-claudecode:critic`, `oh-my-claudecode:verifier`.
