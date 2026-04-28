# Phase 11 retrospective — v1.2 UX Polish + Font-Size 4-Tier Adjuster

> **Closed**: 2026-04-30 PM
> **Tier**: 2 (mid-large; 5 implementation tasks + 1 mid-flight fix + reviewer + close)
> **Daisy ack**: scope 4 user-driven items + v1.2 font-size adjuster all in one phase ("把这次就当作 1.2"); D-P11-1 = Option A (⌘K hint deleted); 11.5 fix ack post visual smoke
> **Outcome**: PASS post 11.5-fix (reviewer code-reviewer 0H/0M/2L PASS BEFORE Daisy's visual-smoke catch; user-perceived bug caught + fixed via the new "preview-before-push" workflow Daisy codified mid-phase)

This is the Rule C-mandated retrospective. Three sections per `~/.claude/CLAUDE.md` Rule C.

---

## §1 保留下来的做法 (R-P11-*)

- **R-P11-1 Per-task commit cadence sustained 5 phases.** Phase 11 had 5 implementation tasks (11.1-11.5) + 1 mid-flight fix (11.5-fix) + 1 close = 7 commits. R-P10-2 pattern locked across Phase 6→7→8→10→11 (Phase 9 was the bundle exception for 12 small same-edit-family tasks). Pattern criterion still working: "per-task when independent + risk-isolated + ≥1 file or ≥20 LOC; bundle when many small same-edit-family tasks". Phase 11.5-fix as separate commit (vs amend) preserved git archeology of the bug + fix decision.

- **R-P11-2 Visual smoke before commit/push for UX phases — codified mid-phase.** Daisy 2026-04-30 PM established the workflow rule: "调整结束后, 本地运行一下, 给我看一下效果, 你再 review, 然后再 commit push". Saved to memory at `feedback_preview_before_push.md`. Caught the 11.5 fontsize bug ON THE FIRST screenshot review iteration — without this rule, the broken zoom-via-rem CSS would have shipped to production and Daisy would have discovered it post-deploy. **Pattern locked: any UX/typography/layout phase MUST go through preview + screenshots before commit/push, not just unit/e2e.** Filed in memory as Rule E candidate ready for absorption to global personal_operating_principles.

- **R-P11-3 Reviewer brief D-dimension structure carries forward 5 phases.** R-P7-1 → R-P8-1 → R-P9-3 → R-P10-3 → R-P11-3: structured `task_N_M_reviewer_prompt.md` with explicit D1-D7 stress dimensions. Phase 11 D2 explicitly asked Rule A spot-check on 18 new i18n strings (1 search.label × 3 + 5 fontsize × 3); reviewer hit it directly + extended to broader Rule A pass. Brief structure proves real work across 5 phases now.

- **R-P11-4 Component pattern reuse over invention.** FontSizeToggle.tsx is a near-perfect mirror of ThemeToggle.tsx (Phase 10.3) — same `<nav aria-label>` shell, same aria-pressed semantics, same useState+useEffect+localStorage handshake, same Active class delta. Verifier explicitly noted "FontSizeToggle = near-perfect ThemeToggle mirror, default-as-absent-attribute trick (avoids CSS-specificity drift), shared flash-prevention IIFE (one try/catch for both keys)". Pattern lesson sustained from Phase 10.3 R-P10-6: when adjacent component is the design reference, mirror exactly except for semantically-required deltas. Saved ~half the implementation time vs designing from scratch.

- **R-P11-5 Reviewer pass + Daisy visual catch are complementary, not redundant.** Code-reviewer (omc) ran AFTER all 5 commits + before push, found 0 HIGH/MEDIUM (PASS verdict). Daisy's visual smoke ran AFTER the reviewer + still caught the fontsize bug. Lesson: reviewer's lens (code structure / a11y / test coverage / i18n parity) and user's lens (perceived effect on real surfaces) are orthogonal — both required for UX phases. Phase 11 = first phase where both lanes ran in series and caught DIFFERENT classes of issues. **Rule D writer/reviewer isolation alone is not sufficient for UX phases; add user-visual-smoke as a third independent lane.**

- **R-P11-6 CSS strategy: prefer 1-file `zoom` over multi-file `text-[Npx]→rem` refactor.** When the original 11.5 CSS strategy didn't deliver, two options: (a) refactor 30+ files mechanically to convert `text-[Npx]` → `text-[N/16rem]` then re-test all visual surfaces; (b) 1-file CSS change to `body { zoom }` which scales the entire visual tree at once. Option b chosen — same visual outcome, fraction of the LOC change, no test re-run risk per file. Lesson: when fixing a CSS architecture decision, prefer the minimal-blast-radius mechanism even if non-standard (zoom is non-standard but evergreen-supported in 2024+). Document the trade-off explicitly.

- **R-P11-7 Persisted Rule D 5-phase rotation chain at omc family extension.** omc-family burns: Phase 6 critic (1st) → Phase 10 verifier (2nd, NEW) → Phase 11 code-reviewer (3rd, NEW). 3 different agents within omc family at increasing intra-family depth. Cross-family chain unbroken: pr ×5 / feature-dev ×2 / superpowers ×1 / omc ×3 = 4 active families on website lane post Phase 11 close.

---

## §2 必须补上的缺口 (G-P11-*)

- **G-P11-1 Phase 11.5 originally shipped a documented-but-unverified-against-real-content bug.** The 11.5 commit message §Risk explicitly noted "Chrome typography uses arbitrary text-[Npx] heavily ... Current scope = primary user benefit prose readability scaling without chrome regression risk". The risk note WAS accurate but underestimated how much LANDING (not just chrome) uses px-typed text — Hero subdeck, Platforms cards, Compare cells, Demo, Downloads — all px. **Pattern lesson: when a commit message says "Risk: X may not work for Y surface", actually GREP for Y surface size before committing, not just "document and ship".** A 30-second `grep -r "text-\[" web/src/components` before 11.5 ship would have shown >40 occurrences and triggered scope rethink. Filed as **C-P11-1** Rule E candidate process improvement: extend Rule A coverage to include "any architectural CSS strategy decision MUST verify scope coverage via grep before commit, not via post-commit review".

- **G-P11-2 Reviewer pass missed the px-vs-rem cascade gap.** Reviewer report PASS 0H/0M/2L confirmed CSS strategy was "well-designed" + "respects browser-level zoom defaults" + "rem cascades through Tailwind". Reviewer didn't grep for `text-[Npx]` to verify the cascade actually reaches 100% of surfaces. **Pattern lesson: reviewer briefs for CSS architecture changes should explicitly include "verify cascade coverage" check (grep for known-non-cascading patterns).** Sister to G-P11-1; both filed as same C-P11-1 carryover. Adding to brief template: a "cascade coverage" sub-step in D-dim for any phase that introduces a CSS-architecture-level change.

- **G-P11-3 Visual smoke was not in the original Phase 11 PLAN.md §2 — added mid-flight.** PLAN.md §2 task 11.5 listed manual smoke as "Daisy 4-tier × 7-flow QA matrix" deferred post-deploy, NOT before commit. Daisy's mid-phase rule "preview-before-push" effectively retrofitted the PLAN. **Pattern lesson: future phase PLANs that touch UX surfaces should include "visual smoke + screenshot evidence" as an explicit task BEFORE reviewer dispatch, not deferred to post-deploy.** Filed as **C-P11-2** template addition: add a §2 task "N.M visual smoke" with screenshot evidence step in `~/.claude/templates/workflow-tier2.md` and `workflow-tier3.md` for any UX-touching phase.

- **G-P11-4 Mid-phase user-feedback handling — fix-as-new-commit pattern (not amend).** When Daisy caught the 11.5 bug via visual review, the original 11.5 commit `6c92b05` was already in git locally (unpushed). Two options: (a) amend `6c92b05` (rewrites history, fewer commits but less archeology) vs (b) new commit `Phase 11.5-fix` (more commits but full bug+fix narrative preserved). Chose (b) per CLAUDE.md "Prefer to create a new commit rather than amending". **Pattern lesson: even for mid-phase pre-push bug fixes, prefer fix-as-new-commit when the bug + fix narrative is non-trivial. The git archeology value (future devs reading the bug+fix story) outweighs the cosmetic prefereence for a single commit.** Filed as informational pattern note (no carryover).

- **G-P11-5 Mass-replacement i18n re-keying (search.shortcut → search.label) modified e2e selectors.** 11.2 removed `search.shortcut` and added `search.label` — this changed the Open-search button's aria-label from `"Open search"` (English-hardcoded) to `t['search.label']` (locale-dependent). e2e search.spec.ts hydration probe was hardcoded to `getByLabel('Open search')` and broke. Detected during 11.2 verify, fixed in same commit via locale-scoped `getByLabel('搜索')`. **Pattern lesson: when an i18n key change affects an aria-label, grep for ALL e2e selectors using that aria-label AT EDIT TIME, not post-fail.** Filed as informational pattern (caught in same commit, no carryover).

---

## §3 关键决策复盘 (D-P11-*)

- **D-P11-1 Scope = 5 user-driven items + v1.2 font-size adjuster all in one phase.** Daisy 2026-04-30 PM ack "把这次就当作 1.2, 1.1 可以结束了". Initial proposal had partition (Phase 11 = items 1-3 polish + Phase 11 ends with v1.2 PLAN.md draft only; Phase 12 = v1.2 implementation). Daisy chose全实施. **Decision held**: Tier 2 mid-large fits in one session; per-task commits keep risk isolation. Avoided phase-fragmentation overhead.

- **D-P11-2 ⌘K hint Option A (完全替换为"搜索"明文, 不保留 kbd 辅助).** Daisy ack 2026-04-30 PM. Alternative was Option B: text + small `<kbd>⌘K</kbd>` next to it (GitHub-style "Search /"). Decision held: keyboard shortcut hint is opaque to non-power users; keyboard shortcut still WORKS via Cmd+K listener; only the visible hint deleted. Power users lose the visual shortcut hint as accepted trade-off.

- **D-P11-3 TopNav utilities visual divider via existing `border-l border-rule pl-N` design token.** Already established between nav-links and utilities since Phase 5 era. Extended same token between [search]/[lang]/[theme]/[fontsize] groups. **Decision held**: design token reuse over inventing new dividers (e.g. `divide-x`, gap-N spacing only, dropdown menu). 4× same border style across the row visually consistent.

- **D-P11-4 DocsLayout Footer mount = single-line addition (import + JSX line).** Footer.astro already accepts `lang` prop and renders i18n maintainer line + 3 nav links. Phase 5 (DocsLayout) shipped without it as oversight, never raised in any prior phase reviewer pass because reviewers focused on docs body content not layout shell. **Decision held**: mechanical fix, no design decision needed.

- **D-P11-5 v1.2 font-size CSS strategy: original `html { font-size: var(--fs-base) }` rem-cascade → fixed mid-flight to `body { zoom: var(--fs-zoom) }`.** Original strategy assumed Tailwind rem-cascade; failed because site uses `text-[Npx]` heavily for editorial typography. Mid-flight fix via Daisy visual review: switched to CSS zoom which scales entire visual tree (text + spacing + borders + icons) regardless of unit. **Decision held post-fix**: zoom is non-standard but Chrome/Safari historical + Firefox 126+ (2024) supported = acceptable for evergreen browsers. Refactoring all `text-[Npx]` → rem would touch 30+ files mechanically; zoom is 1-file 1-line change with same visual outcome.

- **D-P11-6 Reviewer = `oh-my-claudecode:code-reviewer`.** 3rd-burn omc-family NEW agent (Phase 6 critic / Phase 10 verifier / Phase 11 code-reviewer = 3 different omc agents at 3-burn intra-family depth). Cross-family vs Phase 9 feature-dev / Phase 8 pr / Phase 7 superpowers — sustained Rule D 5-phase rotation chain. Reviewer caught 0 HIGH/MEDIUM (PASS); the px-cascade bug was caught by Daisy's visual lens, not the code review lens. **Decision held**: Rule D writer/reviewer code-isolation is necessary but not sufficient for UX phases — visual smoke is the third independent lane.

- **D-P11-7 Workflow change: visual-smoke-before-push codified mid-phase.** Daisy explicit: "调整结束后, 本地运行一下, 给我看一下效果, 你再 review, 然后再 commit push". Saved to memory at `~/.claude/projects/.../memory/feedback_preview_before_push.md`. **Decision held**: applied retroactively to current Phase 11 (commits already in local git, took screenshots before push, caught fontsize bug, applied 11.5-fix, re-screenshot to verify, then ack'd by Daisy "可以推送吧"). Future UX phases will follow this workflow as standard.

- **D-P11-8 Subagent_prompts/ trace + reviewer report committed at Phase close** (D-P6-6 → D-P10-8 → D-P11-8). Sustained pattern across 6 phases.

---

## Rule A/B/C/D/E compliance

- **Rule A** semantic spot-check: 18 new i18n strings (1 search.label × 3 + 5 fontsize × 3 langs). Writer pass implicit (chosen via lang convention review pre-commit). Reviewer extended to N=18 explicit pass (all natural per zh/en/ja standards). ja "特大" kanji native-of-domain (size grades) vs theme.system "システム" katakana (loanword) — appropriate domain split, no flag. Compliant + EFFECTIVE.
- **Rule B** failures archive: 0 entries in `evidence/failures/`. The 11.5 broken-cascade bug WAS caught and fixed mid-phase, not after a full failure-archive event. Compliant.
- **Rule C** retrospective: this file. Three-section structure (R / G / D) per template. Compliant.
- **Rule D** writer/reviewer isolation: writer = main session opus 1M context (direct mode for all 5 tasks + 11.5-fix) + reviewer = `oh-my-claudecode:code-reviewer` (different agent within omc family vs Phase 6 critic / Phase 10 verifier; cross-family rotation 5-phase sustained). Compliant.
- **Rule E** cross-platform learning: 3 candidates filed for absorption to global rules:
  - **R-P11-2 / D-P11-7** (visual-smoke-before-push for UX phases) — strongest candidate, already saved to memory as feedback type, ready for global rule absorption
  - **C-P11-1** (CSS architecture decisions need cascade-coverage grep before commit) — process improvement candidate
  - **C-P11-2** (Tier 2/3 PLAN templates should include explicit "N.M visual smoke" task for UX phases) — template addition candidate

---

## Phase 11 close metrics

| Metric | Phase 10 baseline | Phase 11 close | Delta |
|---|---|---|---|
| tsc errors | 0 | 0 | — |
| vitest pass | 51/51 | **57/57** | +6 (FontSizeToggle 6 new) |
| vitest files | 11 | 12 | +1 |
| e2e pass | 7/7 | 7/7 | — (search.spec.ts selector updated to locale-scoped) |
| build pages | 31 | 31 | — |
| Pagefind pages | 27 | 27 | — |
| Pagefind words | 6457 | 6457 | — (no body content changes) |
| dist/pagefind artifacts | 17 | 17 | — |

| Commit | Subject | Files | LOC delta |
|---|---|---|---|
| `e36354c` | 11.1 TopNav + Footer max-w-screen-xl content wrap | 4 | +293 / -39 |
| `43c0b84` | 11.2 ⌘K hint → "搜索/Search/検索" Option A | 5 | +9 / -7 |
| `41c54da` | 11.3 TopNav utilities visual divider | 1 | +16 / -12 |
| `d01aa0a` | 11.4 DocsLayout add Footer mount | 1 | +2 / -0 |
| `6c92b05` | 11.5 v1.2 font-size 4-tier adjuster | 9 | +174 / -2 |
| `0549317` | 11.5-fix html font-size → body zoom | 1 | +13 / -10 |
| (pending) | 11.7 close + handoff + master plan + index sync | TBD | TBD |

Family pool state at Phase 11 close (sustained from Phase 10 + 1 new agent):
- pr-review-toolkit ×5 / feature-dev ×2 / **oh-my-claudecode ×3** (NEW agent code-reviewer in 3rd burn) / superpowers ×1 = 4 active families on website lane.

Ready for: Phase 12 (TBD scope — see Phase 11→12 handoff). C-P11-* carryover + sustained C-P9-1..16 + C-P10-1..5.
