# Task 6.3 (gate) — End-of-Phase-6 reviewer brief

> **Reviewer subagent**: `oh-my-claudecode:critic` (Opus, READ-ONLY)
> **Rule D isolation**: cross-family from `pr-review-toolkit` (×4 Phases 1-3.6+4) AND `feature-dev` (×1 Phase 5). 6.3 = first-burn `oh-my-claudecode` family on the website lane. Critic-class agent (deep adversarial analysis) chosen over `oh-my-claudecode:code-reviewer` because Phase 6 introduces *infrastructure* (remark plugin, React island, e2e strict) that historically surfaces issues phases later (per Phase 5 G-P5-2 lesson — "Phase 5.1 build green = false negative until 5.3 wired the catchall"). Adversarial framing wanted.
> **Branch**: `main`. Phase 6 commit range = `b25b834..362b401` (3 commits). Pre-Phase-6 baseline = `3fd5adb`.
> **Output verdict**: PASS / CONDITIONAL_PASS / FAIL with H/M/L finding count. CONDITIONAL_PASS or FAIL → main session applies HIGH+blocking fixes in a `Phase 6.4` follow-up commit before Phase 6 → 7 handoff.

## Phase 6 commit range

```
362b401 07 Website Phase 6.2 — expand compare-dimensions to 9 dims (preview shows first 4 via slice)
c52b4a7 07 Website Phase 6.1 — CompareFilter React island + overwrite [lang]/compare.astro real page (path-based i18n per plan deviation)
b25b834 07 Website Phase 6.0 — remark plugin for .md cross-refs + PLATFORM_COMPARISON slug rename + e2e link-resolution strict (C-P5-1 + C-P5-2 absorbed)
```

(`72ef5a9` between 6.0 and 6.1 is unrelated round-10/11 deep-verification kickoff cleanup — NOT part of Phase 6 review scope.)

## Required reading (in this order, then dive into commits)

1. `.work/meta/website_phase5_to_phase6_handoff_2026-04-28.md` — Phase 5 retro + carryover rationale.
2. `.work/07_website/phase6/PLAN.md` — Phase 6 task breakdown + plan deviation flag (`/[lang]/compare` not `compare?lang=`).
3. `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` lines 2313-2480 — master plan §6.
4. `.work/07_website/phase6/evidence/checkpoints/task_6_0_report.md` (190 lines)
5. `.work/07_website/phase6/evidence/checkpoints/task_6_1_report.md`
6. `.work/07_website/phase6/evidence/checkpoints/task_6_2_report.md`
7. `.work/07_website/phase6/subagent_prompts/task_6_0_prompt.md`, `task_6_1_prompt.md` (reviewer can compare brief vs delivered to spot scope creep / scope cuts)

## NEW dimensions introduced in Phase 6 (focus areas — explicit per Phase 5 G-P5-4 lesson)

The Phase 5 reviewer brief was generic and the cross-family reviewer caught 3 HIGH issues anyway. To force focused stress on the actual new surface, here are the 7 dimensions Phase 6 introduces — interrogate each:

### D1 — Remark plugin AST surgery (`web/remark-md-link-rewrite.mjs`)

The plugin visits mdast `link` nodes during content-collection load and either rewrites `node.url` (in-collection) or splices the node out preserving children (out-of-collection). Stress-test:

- **Lang inference**: pulled from `file.data.astro.frontmatter.lang`. What happens if a future entry sets `lang: 'fr'`? Schema enforces enum so this fails earlier — but does the plugin's throw message help debug? Re-confirm.
- **Lang-neutral throw guard**: triggers on `!lang` + `.md` cross-ref. DEMO_QUESTIONS is lang-neutral — does it have ANY `.md` URLs that the SHAPE regex would match? (Pre-flight inventory said 0; verify by `grep -E '\]\([^)]*\.md' ai_platforms/release/v1.0/DEMO_QUESTIONS.md`.)
- **`./self_deploy/` directory ref NOT dropped** (Task 6.0 judgment call #2): the algorithm guard `if (!url || !/\.md(?:#|$)/.test(url)) return;` skips the URL because it has no `.md`. README.zh/en/ja line 18 has `[self_deploy/](./self_deploy/)` which becomes a relative link `./self_deploy/` from `/zh/guide/readme` rendering at `/zh/guide/self_deploy/` → 404 on click. Current e2e DOES NOT visit `/zh/guide/readme` (only `/zh/guide/user-guide`), so the link-resolution test silently passes. **Two questions**: (a) should the plugin be widened to also drop directory-only relative refs, OR (b) should e2e route list include `/zh/guide/readme` to surface the issue? Recommend a fix path.
- **CHANGELOG dual-route** (Task 6.0 judgment call #4): plugin always rewrites `CHANGELOG.md` → `/<lang>/changelog` (dedicated route per D-P5-1), but `dist/<lang>/guide/changelog/index.html` ALSO emits because the catchall `[...slug].astro` renders the `slug: changelog` collection entry. Two routes for the same content — is this a problem? Sitemap dupes? SEO canonicalization gap? Or design-intentional?
- **Hash preservation** (`#section`): SHAPE regex captures `#hash` group; rewrite preserves it. Does any cross-ref in the corpus actually use a hash? (`grep -E '\.md#' ai_platforms/release/v1.0/*.md`.) If so, do the rewritten anchors land at sections that exist in the rendered HTML, given that Astro adds id slugs differently than the source `# Heading`?
- **Backtick text preservation** (`[\`./FOO.md\`](./FOO.md)`): Task 6.0 report shows the inline `<code>` is preserved — this is correct mdast behavior (children survive when only `node.url` mutates). Re-confirm by inspecting actual built HTML for `<a href="/zh/guide/glossary"><code>` shape.
- **Race conditions / build determinism**: does the plugin produce identical output across re-runs? (Plugin is pure function of mdast + frontmatter.lang; should be deterministic.)

### D2 — Slug rename atomicity (PLATFORM_COMPARISON `compare` → `platform-comparison`)

- Verify NO stale references survive: `git grep -wF compare ai_platforms/release/v1.0/PLATFORM_COMPARISON.{zh,en,ja}.md` should hit only inside body prose, NOT in `slug:` frontmatter.
- Verify the catchall `[lang]/guide/[...slug].astro` consumes the new slug correctly: `dist/{zh,en,ja}/guide/platform-comparison/index.html` exists; `dist/{zh,en,ja}/guide/compare/` does NOT.
- Verify naming-collision avoidance: `/[lang]/compare` (page route, Phase 6.1) and `/[lang]/guide/platform-comparison` (doc route) coexist without route-precedence conflict.
- Side-channel checks: any other file (e.g. release/v1.0/README.*) reference the old `compare` slug? (Should be 0 — README cross-refs were always to filename `PLATFORM_COMPARISON.zh.md`, never to slug.)
- Sitemap.xml: does `dist/sitemap-0.xml` (or whatever Astro emits) include the renamed `/guide/platform-comparison/` and exclude old `/guide/compare/`?

### D3 — `[lang]/compare.astro` plan deviation (path-based i18n)

The master plan explicitly says `web/src/pages/compare.astro` (root) + `?lang=` query. PLAN.md REJECTED this and used `[lang]/compare.astro` + `Astro.params.lang`. Reasons documented in PLAN.md L12-21. Reviewer:

- Confirm the deviation is the right call by checking: (a) `astro.config.mjs` has `prefixDefaultLocale: true`, (b) Phase 4 `ComparePreviewSection` CTA is `/${lang}/compare`, (c) Phase 5 stub was at `[lang]/compare.astro`, (d) verbatim plan would have produced a redirect-or-dead-link.
- Inspect the actual deployed shape: `dist/{zh,en,ja}/compare/index.html` exists; no `dist/compare/index.html` at root; `?lang=` query handling absent (no `Astro.url.searchParams.get('lang')` in the file).
- Cross-check that the plan-deviation rationale was recorded in commit message (it was — verify wording is sufficient for archeology).

### D4 — CompareFilter React island a11y / i18n / behavior

- **a11y**: input has `aria-label="Filter dimensions"`. Sufficient? Should `<table>` have `<caption>`? `winners` styling (`text-accent font-bold`) — convey "winner" status to screen readers? Currently relies on color + bold only — WCAG SC 1.4.1 (Use of Color) potential gap.
- **i18n**: `placeholder="Filter dimensions..."` and `aria-label="Filter dimensions"` are hardcoded English. Page heading "Multi-dimensional Comparison" + subhead "Side-by-side across 4 platforms. Filter by dimension keyword." also hardcoded English. zh/ja viewers see English chrome around translated dim labels. Carryover candidate (parallel to C-P5-L1 fallback-banner-i18n)?
- **Filter logic**: case-insensitive + lowercase + substring match on `label[lang]`. What about CJK input methods (Pinyin → 中文 latency)? `useState` + controlled input handles IME composition states correctly? The 2 vitest don't cover CJK input — risk is theoretical.
- **Empty state**: `dims.filter(...)` returning [] renders `<tbody></tbody>` (no rows, no "No matches" message). Acceptable UX or v1.1 polish?
- **client:load directive**: forces immediate hydration. Justification documented in 6.1 brief (lazier strategies cause input flash). Reviewer: any reason to revisit?
- **dims prop drift**: `dims` JSON imported in `[lang]/compare.astro` and passed to React. Static at build time. If `compare-dimensions.json` is edited post-build, does dev server hot-reload pick it up? Not blocking; build-time binding is acceptable.

### D5 — e2e link-resolution strict mode

- The `.md` skip block (Phase 5 carryover) was deleted in 6.0. Reviewer: are there OTHER hand-rolled skips in `smoke.spec.ts` that should also reconsider given the plugin? (e.g. `if (href.startsWith('#') || ...)`. ) These are correct skips (anchors / external) but worth confirming none silently mask a regression.
- The e2e route list `['/zh/', '/en/', '/ja/', '/zh/guide/user-guide', '/zh/changelog']` covers landing × 3 + 1 guide + 1 changelog. **Coverage gap**: does NOT visit `/zh/guide/readme` (where the unhandled `./self_deploy/` directory ref lives — see D1 finding). Recommend adding `/zh/guide/readme` to the route list.
- After 6.2, does `/zh/compare` need an e2e? Currently link-resolution doesn't visit it; landing visits a 4-row preview, not the full table. Phase 6.4 candidate or v1.1 OK?
- `reuseExistingServer: true` in playwright.config burned 6.0's first attempt with a stale dev. Both 6.0 and 6.2 fixed via `lsof -ti:4321 | xargs -r kill` pre-run. Reviewer: should playwright config flip to `reuseExistingServer: false` (slower but safer) OR add a pretest hook that kills :4321? Or document in README/CONTRIBUTING?

### D6 — Data layer (compare-dimensions.json 4→9 dims)

- Inspect new 5 dims for: (a) all `key` strings unique against existing 4 + each other, (b) `label` has all 3 langs (zh/en/ja) populated, (c) `values` covers all 4 platform keys, (d) `winners` array contains only valid platform keys (no typos), (e) `winners` may be `[]` for non-superlative dims (acceptable).
- Mixed-language `values` (e.g. `internet.chatgpt: "默认开"` vs `score.chatgpt: "16.5/17"`): consistent with existing 4 dims OR introducing new inconsistency? (Existing 4 also mixed — pattern, not regression.)
- Are any of the new 5 facts STALE relative to the source `PLATFORM_COMPARISON.*.md`? E.g. `subscription.claude: "Pro/Team/Ent"` — does the .md actually still claim this? Spot-check 2-3 to verify data accuracy isn't drifting from source.

### D7 — slice(0, 4) preview cut

- Hardcoded `4` index. If 6.2 had appended new dims at the FRONT of the array instead of the end, the preview would have shown wrong dims. Brittle? Should be a named const `LANDING_PREVIEW_COUNT = 4`?
- Does the slice cut match the plan template's "user-relevant" 4-dim selection? Plan §6.2 Step 2 says "best-at / capacity / sharing / anti-halluc". Verify these are the first 4 in the JSON file.
- Landing test currently asserts section presence (`'WHICH ONE?'` heading), NOT row count. Is there a missing test that the preview shows exactly 4 rows? (Risk: if slice index is changed accidentally, test wouldn't catch. Phase 6.4 candidate or v1.1 OK?)

## Phase 5 lessons applied — verify carryover (do NOT reintroduce)

- **R-P5-1**: subagent verbatim-copy contract — Phase 6 used it for 6.0 + 6.1 (full file bodies in briefs). Confirm by diffing brief code blocks vs committed code.
- **R-P5-2**: pre-flight pattern probe — main session's pre-flight pre-6.0 dispatch read content.config.ts + cross-ref inventory before brief. Confirm subagent reports show "no divergence from main session's confirmed patterns".
- **R-P5-3**: Tier 3 plan trace — `_progress.json` + per-task evidence reports + subagent prompts all preserved. Verify by `ls .work/07_website/phase6/{evidence/checkpoints,subagent_prompts}/`.
- **R-P5-4**: cross-family reviewer — 6.3 = `oh-my-claudecode:critic`, cross-family from previous 5 reviewers. Confirm.
- **R-P5-5**: decisions made BEFORE dispatch — 3 entry decisions ack'd at session start (absorb C-P5-1+2, plan deviation, reviewer slot). Confirm trace.
- **G-P5-1**: Astro 6 API check — was `import { render } from 'astro:content'` still in use? Phase 6 didn't touch content collection rendering, but reviewer should confirm no regression.
- **G-P5-2**: defer "build green = PASS" until consuming feature lands — Phase 6.0 commit had no consuming feature; e2e strict mode IS the consumer (it would fail loudly if rewrites were broken). 6.2 dim expansion has 2 consumers (landing preview + compare page) and both verified manually. OK.
- **G-P5-3**: `.md` cross-refs dead links — RESOLVED in 6.0.
- **G-P5-4**: reviewer brief explicit new-dimension enumeration — THIS document does it (D1-D7 above).

## Carryover bookkeeping (verify status mapping per PLAN.md table)

| ID | PLAN.md status | Phase 6 actual |
|---|---|---|
| C-P5-1 .md cross-refs | "absorbed into Task 6.0" | Verify resolved by inspecting commit `b25b834` |
| C-P5-2 PLATFORM_COMPARISON slug | "absorbed into Task 6.0" | Verify resolved |
| C-P5-M2 DocsSidebar drawer VT | "DEFER no VT enabled" | Confirm no VT introduced in Phase 6 (none expected) |
| C-P5-M3 trailing-slash hosting | "VERIFY during Phase 6 CF preview deploy" | NOT done in Phase 6 — flag if reviewer thinks it should be in scope |
| C-P5-L1 fallback banner i18n | "DEFER next i18n touch" | Phase 6.1 added MORE hardcoded English (compare page chrome). Worth widening C-P5-L1 scope? |
| C-P5-L2 empty TOC aside guard | "DEFER cosmetic" | Confirm not regressed |

## Output format

Write reviewer report to `.work/07_website/phase6/evidence/checkpoints/phase_6_reviewer_report.md` with:

1. **Verdict**: PASS / CONDITIONAL_PASS / FAIL (one of three) + 1-line rationale.
2. **Findings**: H/M/L counts + per-finding entries with: severity / dimension (D1-D7) / description / suggested fix / blocking-or-defer status.
3. **Phase 5 lessons re-validation**: each R-P5-* / G-P5-* with PASS or DRIFT.
4. **Carryover bookkeeping**: status check for each C-P5-* per the table above.
5. **Recommendations for Phase 6 → Phase 7 handoff**: what new carryover does Phase 6 generate?
6. **Adversarial probe summary**: top 3 things you tried to break and what happened.

## Conduct rules

- READ-ONLY: do NOT edit any source files. Suggested fixes go in the report only; main session applies them in 6.4 if blocking.
- Independence: do NOT consult or mirror the main session's analysis. Form independent verdicts. If you find issues that 6.0/6.1/6.2 evidence reports flagged for you (the 4-5 judgment calls listed across the reports), confirm or rebut them — don't just rubber-stamp.
- Adversarial framing: assume infrastructure introduced in Phase 6 will be exercised in Phase 7+. Hunt for "build-green-but-data-broken" silent-pass scenarios per G-P5-2.
- Time budget: opus + thorough, no upper limit; thoroughness matters more than speed for a Phase-gate review.
- No git commands, no shell mutations, no `npm run dev` / `npm run build` (read `dist/` if needed — it was rebuilt during 6.2 verify and is current).
- Working directory: `/Users/bojiangzhang/MyProject/SDTM-compare/`

Report back with: (a) verdict line, (b) total H/M/L counts, (c) absolute path to your report file, (d) top 3 highest-severity findings in 1 line each.
