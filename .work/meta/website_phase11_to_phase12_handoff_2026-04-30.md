# Website Build — Phase 11 → Phase 12 Handoff

> **Date**: 2026-04-30 PM
> **Outgoing session**: Phase 11 (v1.2 UX Polish + Font-Size 4-Tier Adjuster)
> **Incoming session**: Phase 12 (TBD — Daisy decides post-handoff scope; v1.2.x or v1.3 polish bundle)
> **Branch**: `main`. HEAD = (post 11.7 close commit, pending). Prior: `0549317` (11.5-fix).

## What's done — Phase 11

| Commit | Subject |
|---|---|
| `e36354c` | 07 Website Phase 11.1 — TopNav + Footer max-w-screen-xl content wrap (chrome aligns with landing+docs) |
| `43c0b84` | 07 Website Phase 11.2 — ⌘K hint → "搜索/Search/検索" (Option A) |
| `41c54da` | 07 Website Phase 11.3 — TopNav utilities visual divider |
| `d01aa0a` | 07 Website Phase 11.4 — DocsLayout add Footer mount |
| `6c92b05` | 07 Website Phase 11.5 — v1.2 font-size 4-tier adjuster (FontSizeToggle + html data-fontsize CSS) |
| `0549317` | 07 Website Phase 11.5-fix — html font-size cascade → body zoom (caught by Daisy visual smoke before push) |
| (pending) | 07 Website Phase 11 close — handoff + master plan annotation + index sync |

## End-of-Phase-11 state

**Reviewer verdict** (`oh-my-claudecode:code-reviewer`, 3rd-burn omc-family NEW agent vs Phase 6 critic + Phase 10 verifier; cross-family Rule D 5-phase rotation sustained): **PASS H=0 M=0 L=2** (report at `.work/07_website/phase11/evidence/checkpoints/phase_11_reviewer_report.md`). The 2 LOW are process notes (BaseLayout flash-prevention valid-set duplication mirroring theme pattern + FontSizeToggle.tsx nav className minor cosmetic divergence from ThemeToggle mirror).

**Daisy visual smoke** (NEW workflow rule codified mid-phase 2026-04-30 PM): screenshots taken via chrome-devtools MCP at /zh/ default-md + xl-zoom + sm-zoom + /zh/guide/user-guide/ Footer + TopNav close-up. **Caught fontsize bug NOT visible to code-reviewer**: original 11.5 used `html { font-size: var(--fs-base) }` rem-cascade strategy that didn't reach `text-[Npx]` arbitrary classes (which the site uses heavily for editorial typography). Fix in same phase via 11.5-fix commit: switched to `body { zoom: var(--fs-zoom) }` — scales entire visual tree regardless of unit.

Daisy ack post-fix: "可以推送吧" → push approved.

Test status post Phase 11 close: tsc 0 / **vitest 57/57** (+6 vs Phase 10 baseline 51/51) / e2e 7/7 (search.spec.ts selector updated to locale-scoped getByLabel) / build 31 pages / Pagefind 27 indexed / 6457 words.

## Pre-flight decisions made at Phase 11 start (Daisy ack 2026-04-30 PM)

1. **Scope = 5 user-driven items + v1.2 font-size adjuster all in one phase** — Y. Daisy: "把这次就当作 1.2, 1.1 可以结束了". Initial proposal had Phase 11 = chrome polish + Phase 12 = v1.2 implementation; Daisy chose merge.
2. **D-P11-1 ⌘K hint Option A (完全替换)** — Y. ⌘K hint deleted entirely; replaced with explicit "搜索/Search/検索" text via new `search.label` i18n key.
3. **Reviewer slot = `oh-my-claudecode:code-reviewer`** — Y, 3rd-burn omc NEW agent.
4. **Per-task commit cadence over bundle** — Y, sustained R-P10-2 (5 commits + 1 mid-flight fix).
5. **Mid-phase: visual-smoke-before-push workflow** — codified by Daisy 2026-04-30 PM ("调整结束后, 本地运行一下, 给我看一下效果, 你再 review, 然后再 commit push"). Saved to `~/.claude/projects/.../memory/feedback_preview_before_push.md`. Applied retroactively to Phase 11 — caught 11.5 bug before push.

## §1 Retrospective — what went well (Rule C R-P11-*)

See `.work/07_website/phase11/RETROSPECTIVE.md` §1 R-P11-1..7 for full detail.

Highlights:
- **R-P11-1** Per-task commit cadence sustained 5 phases (Phase 6/7/8/10/11 = per-task; Phase 9 = bundle exception)
- **R-P11-2** Visual smoke before commit/push for UX phases — codified mid-phase, caught fontsize bug on first iteration
- **R-P11-4** Component pattern reuse over invention (FontSizeToggle = ThemeToggle near-perfect mirror)
- **R-P11-5** Reviewer pass + Daisy visual catch are complementary — both required for UX phases (Rule D writer/reviewer code-isolation alone insufficient)
- **R-P11-6** CSS architecture fix: 1-file `body { zoom }` over multi-file `text-[Npx]→rem` refactor (minimal blast radius)
- **R-P11-7** Sustained Rule D 5-phase rotation at omc family extension (3 different omc agents)

## §2 Gaps (Rule C G-P11-*)

See `.work/07_website/phase11/RETROSPECTIVE.md` §2 G-P11-1..5 for full detail.

Highlights:
- **G-P11-1** 11.5 shipped with documented-but-unverified-against-real-content risk note. CSS architecture decision needed cascade-coverage grep before commit, not post-commit review. Filed as C-P11-1 process improvement.
- **G-P11-2** Reviewer brief missed cascade-coverage check for CSS architecture phase. Sister to G-P11-1; same C-P11-1 carryover.
- **G-P11-3** Phase 11 PLAN.md §2 listed visual smoke as deferred-post-deploy, not before-commit. Daisy mid-phase rule retrofitted. Filed as C-P11-2 template addition.
- **G-P11-4** Fix-as-new-commit pattern (not amend) chosen for 11.5-fix; full bug+fix narrative preserved.
- **G-P11-5** i18n re-keying (search.shortcut → search.label) broke e2e selector; caught + fixed same commit.

## §3 Decisions (Rule C D-P11-*)

See `.work/07_website/phase11/RETROSPECTIVE.md` §3 D-P11-1..8 for full detail.

Highlights:
- **D-P11-1** All 5 items + v1.2 in one phase (Daisy ack)
- **D-P11-2** ⌘K Option A (完全替换)
- **D-P11-3** Existing border-l divider design token reused
- **D-P11-5** font-size CSS: rem-cascade → body zoom mid-flight fix
- **D-P11-6** Reviewer = omc:code-reviewer 3rd-burn
- **D-P11-7** Visual-smoke-before-push workflow codified

## Carryover for Phase 12 (consolidated, IDs C-P11-*)

### Phase 11.5-fix already RESOLVED (no carryover)
- C-P11-(11.5 px-cascade bug) — fixed in 11.5-fix via body zoom

### Phase 12 carryover (numbered)
- **C-P11-1** [Process improvement] CSS architecture decisions MUST verify cascade coverage via grep before commit (not via post-commit review). Extend Rule A coverage to "any architectural CSS strategy decision MUST verify scope coverage via grep before commit". G-P11-1+G-P11-2 sister. Candidate for `~/.claude/CLAUDE.md` `personal_operating_principles` extension.
- **C-P11-2** [Template addition] Tier 2/3 PLAN templates should include explicit "N.M visual smoke" task BEFORE reviewer dispatch for UX-touching phases. G-P11-3 sister. Candidate for `~/.claude/templates/workflow-tier2.md` and `workflow-tier3.md` template update.
- **C-P11-3** [LOW review finding F-1] BaseLayout.astro:34-37 flash-prevention inline script duplicates the valid-set check that fontSize.ts already encodes as VALID[]. Bounded duplication mirrors theme pattern; if a 5th tier is ever added, audit the inline script.
- **C-P11-4** [LOW review finding F-2] FontSizeToggle.tsx:28 nav className drops `text-[10px] tracking-wider` vs ThemeToggle's mirror. Functionally fine (per-button style fontSize overrides anyway) but cosmetically diverges from established mirror pattern.
- **C-P11-5** [Visual QA Daisy manual] 4-tier × 7-flow font-size matrix manual smoke (per Phase 10 entry feedback "方案 A: 独立 feature 配 layout QA"). Some tiers verified via screenshots already (md/xl/sm); full 7-flow matrix at production deferred to Daisy manual.

### Pre-existing Phase 6/7/8/9/10 carryover NOT touched in Phase 11 (Daisy explicit "把这次就当作 1.2")

All C-P9-1..16 carryover from Phase 9→10 handoff still pending:
- C-P9-1 Safari + Firefox cross-browser sweep (Daisy manual)
- C-P9-2 Lighthouse remediation 95/95/95
- C-P9-3 axe DevTools manual scan
- C-P9-4 Lighthouse Performance trace
- C-P9-5..9 a11y fail items (color-contrast / label-content-name-mismatch / target-size / errors-in-console / third-party-cookies)
- C-P9-10 SearchOverlay Escape stale closure
- C-P9-12..15 cheap LOW fixes
- C-P9-16 Process improvement: canonical-derivation grep

C-P10-1..5 carryover from Phase 10→11 handoff:
- C-P10-1 mass-replacement commit message methodology (occurrences-vs-lines)
- C-P10-2 _progress.json mid-phase EXECUTING state machine
- C-P10-3 v1.2 font-size 4-tier adjuster — RESOLVED in Phase 11 (no carryover)
- C-P10-4 v1.2 visual snapshot regression harness — partially materialized via R-P11-2 visual smoke workflow
- C-P10-5 v1.1+ release pack with Bojiang Zhang

Pre-Phase-9 carryover:
- C-P7-1 Astro i18n soft-404 200 — ACCEPTED indefinitely
- C-P7-7 Rule A rubric expansion for translation work — partially materialized R-P9-4 + R-P10-5 + R-P11-2
- C-P7-8 README "auto-deploys from main" verify
- C-P8-6 Mobile UX
- C-P6-5 /guide/platform-comparison vs /compare redundancy
- C-P5-M2 DocsSidebar drawer ViewTransitions

## Working state — Phase 11 close

- **Branch**: `main`. HEAD = (post 11.7 close commit, pending). Prior chain: `cdd8f8e` (Phase 10 close) → `e36354c` (11.1) → `43c0b84` (11.2) → `41c54da` (11.3) → `d01aa0a` (11.4) → `6c92b05` (11.5) → `0549317` (11.5-fix) → close (pending).
- **Test status**: tsc 0 errors / vitest **57/57** in 12 files (+6 vs Phase 10) / e2e **7/7** strict against `npm run preview` lane / build **31** HTML pages green / Pagefind 27 indexed pages / 6457 words / dist/pagefind/ 17 artifacts unchanged.
- **Production**: `https://sdtm-pedia.pages.dev/` LIVE post Phase 10. Phase 11 push will trigger CF auto-deploy ~3-5 min.
- **Lighthouse baseline**: a11y 91 / Best Practices 73 / SEO 100 (carryover from Phase 9; Phase 11 didn't touch).
- **Evidence preserved**:
  - `.work/07_website/phase11/PLAN.md` ~250 lines
  - `.work/07_website/phase11/_progress.json` — final CLOSED state
  - `.work/07_website/phase11/evidence/checkpoints/phase_11_reviewer_report.md` — code-reviewer pass report
  - `.work/07_website/phase11/evidence/screenshots/{02..10}_*.png` — 8 visual smoke screenshots (md/xl/sm tiers + docs Footer + TopNav close-up)
  - `.work/07_website/phase11/subagent_prompts/task_11_6_reviewer_prompt.md`
  - `.work/07_website/phase11/RETROSPECTIVE.md` — Rule C 三段

## How the Phase 12 session should start

1. **Read this handoff first.** Run `git log --follow web/` archeology pass per R-P9-1 lesson if scope names a specific surface.
2. **Apply preview-before-push workflow** (R-P11-2 codified rule, memory `feedback_preview_before_push.md`) — for any UX-touching phase: build → preview → screenshots via chrome-devtools MCP → user review → THEN commit + push.
3. **Decide Phase 12 scope**:
   - **A**: v1.2.x polish bundle absorbing C-P11-1..5 (CSS-cascade-grep process improvement + Tier 2 template addition + 2 LOW review findings + visual QA matrix completion)
   - **B**: C-P9-* carryover bundle (Lighthouse 95/95/95 + Safari/Firefox + cheap LOW fixes — half-day cleanup; PRIMARY recommendation if no new user feedback raised)
   - **C**: New user-feedback items (if Daisy raises any)
   - **D**: Daisy public-release announcement (out of code scope)
   - **E**: Migration/upgrade work (Astro 7 watch, etc.)
   - **F**: STOP — declare v1.2 complete, archive `web/` lane until next iteration
4. **Read** `.work/07_website/phase11/RETROSPECTIVE.md` for full §1 R-P11-1..7 / §2 G-P11-1..5 / §3 D-P11-1..8 + Rule A/B/C/D/E compliance.
5. **Reviewer slot for Phase 12** (if A/B/C): cross-family options remaining:
   - `pr-review-toolkit:type-design-analyzer` / `pr-test-analyzer` (6th-burn pr-family, NEW agent — strong choice if v1.2.x has type/test changes)
   - `superpowers:requesting-code-review` (2nd-burn superpowers, NEW agent)
   - `feature-dev:code-reviewer` (3rd-burn feature-dev, returning agent)
   - `oh-my-claudecode:debugger` or `tracer` (4th-burn omc-family NEW agent — strong if Phase 12 has any debugging spillover from C-P11-1 cascade-coverage work)
   Recommend: `pr-review-toolkit:type-design-analyzer` for v1.2.x polish OR `oh-my-claudecode:debugger` for cascade-coverage process improvement work.

Family pool state at Phase 11 close: `pr-review-toolkit` ×5 / `feature-dev` ×2 / `oh-my-claudecode` ×3 (NEW agent code-reviewer in 3rd burn) / `superpowers` ×1 = 4 active families on website lane.

## Push state at Phase 11 close

`origin/main` = `cdd8f8e` at session start. Phase 11 commits (`e36354c` 11.1 + `43c0b84` 11.2 + `41c54da` 11.3 + `d01aa0a` 11.4 + `6c92b05` 11.5 + `0549317` 11.5-fix + this handoff's index-sync commit pending) all unpushed at handoff write time.

After push, CF Pages will auto-rebuild ~3-5 min, picking up:
- 11.1 chrome max-w-screen-xl on TopNav + Footer
- 11.2 ⌘K → "搜索"/"Search"/"検索" explicit text
- 11.3 TopNav utilities 4-group vertical divider
- 11.4 DocsLayout Footer mount
- 11.5+11.5-fix v1.2 font-size 4-tier adjuster via `body { zoom }`

Verify CF re-deploy ~5 minutes post-push (Daisy will run via browser):
- TopNav `<header>` content visually constrained to ~1280px on desktop ≥1280px viewport (was edge-to-edge)
- Footer `<footer>` same constraint
- ⌘K hint button shows "搜索" on /zh/, "Search" on /en/, "検索" on /ja/
- TopNav right-side has 4 vertical dividers between groups
- Docs reader `/zh/guide/user-guide/` shows Footer at scroll bottom
- New "A A A A" 4-button FontSizeToggle in TopNav after ThemeToggle
- Click any non-md FontSizeToggle button: ENTIRE page scales (text + containers + chrome) — including arbitrary px-typed editorial typography

If any post-push verify fails, file as Phase 11 fast-follow fix; otherwise Phase 11 is officially CLOSED.
