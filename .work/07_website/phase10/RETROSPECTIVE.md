# Phase 10 retrospective — v1.1 User-Driven UX Polish

> **Closed**: 2026-04-30
> **Tier**: 2 (5-15 steps, ~half-day; PLAN ack'd "落实 plan.md 然后不开干, 等 17 点 usage 恢复了再开干")
> **Daisy ack**: 4-item scope locked 2026-04-30 (5 raised, #5 font-size adjuster deferred to v1.2 — "方案 A" independent feature)
> **Outcome**: CONDITIONAL_PASS (0 HIGH / 0 MEDIUM / 2 LOW) → effective PASS post 10.5 fix bundle

This is the Rule C-mandated retrospective. Three sections (保留下来的做法 / 必须补上的缺口 / 关键决策复盘) per `~/.claude/CLAUDE.md` Rule C.

---

## §1 保留下来的做法 (R-P10-*)

- **R-P10-1 User-driven scope locked at PLAN ack with explicit "v1.2-deferred" line.** Daisy raised 5 items 2026-04-30; 4 went into Phase 10 (v1.1 polish), 1 deferred to v1.2 (font-size 4-tier adjuster) with concrete reason ("方案 A: independent feature work with proper layout adaptation + QA"). Pattern: when a phase batches multiple user-feedback items, the PLAN.md should explicitly enumerate which items are scope and which are deferred (not just listed silently); Daisy ack on the partition is captured in PLAN §1. Saved Phase 10 from scope creep and gives Phase 11 a clear v1.2 entry.

- **R-P10-2 Per-task commit cadence for 4 independent tasks.** Phase 6 used 5 per-task commits, Phase 9 bundled 12 small tasks into 1 commit. Phase 10's 4 tasks were **independent + non-trivial each** (≥3 files / ≥20 LOC), so 4 separate commits + 1 fix-bundle + 1 close = revertable per task. ThemeToggle rewrite (10.3) had its own risk profile (component+test+i18n+caller wiring); separating it from Daisy-sweep (10.4) means a regression in either is a single `git revert <hash>` instead of a complex partial-revert. **Commit cadence rule confirmed**: per-task when tasks are independent + ≥1 risk-isolation boundary; bundle when tasks are small + same edit-family.

- **R-P10-3 Reviewer brief D-dimension structure carries forward across 4 phases.** R-P7-1 → R-P8-1 → R-P9-3 → R-P10-3: structured `task_N_M_reviewer_prompt.md` with explicit D1-D7 stress dimensions adapted to phase surface. Phase 10's D5 (Daisy sweep completeness) explicitly enumerated `grep -rc` checks; D2 explicitly asked for Rule A spot-check on 12 new i18n strings. Reviewer hit both directly. **Brief structure is doing real work, not ceremony — 4-phase pattern locked.**

- **R-P10-4 Pre-flight grep before sed batch.** PLAN §2 task 10.4 mandated pre-flight grep baseline (75 occurrences across 26 files in web+release; 192 occurrences in .work/), then sed batch, then post-replace verify (75 → 0 in scope, .work/ unchanged). Pattern: any mass replacement must establish a counted baseline + post-state verification, not just "looks right". Caught zero false positives because pre-flight enumerated all contexts and confirmed no code (.ts/.tsx/.astro/.js) contained "Daisy".

- **R-P10-5 Rule A spot-check N=12 → reviewer extension N=20+.** Writer (10.4 commit) documented N=12 spot-check (3 langs × 4 surfaces). Reviewer extended to N=20+ (8 additional samples from USER_GUIDE/PLATFORM_COMPARISON/GLOSSARY × 3 langs). Two independent passes catch different sample distributions. **Pattern: writer pass states N≥3 minimum; reviewer pass extends with N additional independent samples.** Materializes Rule A "writer says PASS + reviewer says PASS" as numerical-coverage rule, not just verbal.

- **R-P10-6 ThemeToggle 3-button mirroring LangSwitcher = pattern reuse over invention.** Daisy feedback was specifically "不如 旁边语言切换方式来的清晰具体" — pointed at LangSwitcher as the visual reference. The component rewrite is a textbook copy-pattern: same `<nav aria-label>` wrapper, same "current item highlighted" rule, same `flex gap-2 font-mono text-[10px] tracking-wider` styling. WAI-ARIA semantics swapped (aria-pressed for state toggle vs aria-current for nav link) — that's the only delta. **Lesson: when user references an adjacent component as the design reference, mirror its pattern exactly except for semantically-required deltas. Don't reinvent.**

- **R-P10-7 _progress.json updated alongside completed_steps + reviewer verdict at fix-bundle commit.** F-1 LOW (verifier finding) was that `_progress.json` still read PLAN_ACK state with empty `completed_steps`. Fix-bundle commit promoted it to REVIEWER_COMPLETE_PENDING_CLOSE with all 4 commits + LOC deltas + reviewer verdict block + post-close test baseline. **Pattern: phase progress JSON should be an executable state machine — `PLAN_ACK_AWAITING_EXECUTE_WINDOW` → `EXECUTING` → `REVIEWER_COMPLETE_PENDING_CLOSE` → `CLOSED`. Update at each transition, not just at close.** Future phases should set `EXECUTING` at first task start.

---

## §2 必须补上的缺口 (G-P10-*)

- **G-P10-1 `_progress.json` not promoted from PLAN_ACK state during execution.** Tasks 10.1-10.4 were completed and committed, but the JSON's `status` field stayed at `PLAN_ACK_AWAITING_EXECUTE_WINDOW` and `completed_steps` stayed empty until verifier flagged it. Pattern lesson: **mid-phase JSON updates after each task commit, not just at close.** Captured as R-P10-7 sister rule. Future phases should add a `_progress.json` update step to per-task verify protocol (alongside vitest/e2e/build).

- **G-P10-2 Commit message "75 occurrences" used `grep -roh | wc -l` semantics; reviewer used `grep -rc` (line count = 60).** Both correct numerically (75 occurrences exist on 60 lines because some lines have 2 "Daisy" strings — e.g. "@Daisy ... @Daisy" chat-mention dual mentions), but the commit message didn't specify the methodology. Captured as C-P10-1 process improvement: **mass-replacement commit messages should specify count methodology (occurrences vs lines vs files).** Sister to G-P10-1: documentation precision matters when reviewer cross-checks.

- **G-P10-3 No mid-phase visual smoke before reviewer dispatch.** PLAN §3 listed visual smoke localhost:4321 — landing + docs + compare + theme toggle + lang switcher all functional in zh/en/ja + light/dark theme. This was deferred to "after all tasks (final pre-push)" but verifier doesn't run a browser. Pattern lesson: **for UX-driven phases, the pre-reviewer visual smoke is a writer-side artifact (screenshot or "looks correct" affirmation) that should be captured in evidence/, not just verbal in PLAN §3.** Phase 11+ candidate: add a screenshot evidence step pre-reviewer. Risk: visual regression (e.g. ThemeToggle 3-button width breaking TopNav layout on narrow viewport) could slip through if reviewer doesn't run a browser.

- **G-P10-4 GH Release v1.0 zip assets shipped 4-28 with old "Daisy" content; immutable.** PLAN §2 task 10.4 documented this caveat ("asset re-upload would invalidate v1.0 immutable tag"). Decision was correct: don't re-cut v1.0 over a name swap. But it leaves a small inconsistency window — the LIVE website + repo + downloadable bundle disagree on the maintainer name until v1.1+ ships. Pattern lesson: **when an immutable artifact (GH Release tag, npm package version, container image digest) is part of the deliverable, scope changes that affect its content require explicit defer-or-recut decision documented in the PLAN, not just "we'll catch it next time".** Captured.

- **G-P10-5 No CSS regression harness — visual changes verified via test count + e2e structural assertions only.** Phase 10.2 (landing container) and 10.3 (ThemeToggle layout) are CSS-class changes that vitest + e2e + build cannot catch (e2e asserts text content, not pixel layout). The reviewer noted "ComparePreview table min-w-[600px] inside overflow-x-auto inside max-w-screen-xl — fits on desktop ≥1280px, mobile keeps horizontal scroll" as confirmed via reading the file, not via running a viewport-resize Playwright test. Pattern lesson: **for UX-class phases, visual regression coverage is a documented gap; mitigation is reviewer reading the markup + Daisy manual smoke at post-push verify.** Filed as candidate for v1.2+ tooling (Playwright visual snapshot or Chromatic-style harness if scope grows).

---

## §3 关键决策复盘 (D-P10-*)

- **D-P10-1 Scope = 4-of-5 user-feedback items, font-size deferred.** Daisy 2026-04-30 raised 5 items; #5 (4-tier font-size adjuster) deferred because it's independent feature work needing UI control + localStorage + CSS variables + 4-tier × 7-flow layout QA = ~half-day on its own. Combining all 5 would have doubled phase duration + risked layout regressions across docs + landing. **Decision held**: clean partition between "polish current chrome" (10.1-10.4) and "add new feature with QA scope" (v1.2). Daisy ack: "方案 A".

- **D-P10-2 CF `_redirects` server-side 301 over removing meta-refresh HTML entirely.** Option a+c (root + secondary both converted to 301). Alternative was deleting the meta-refresh `.astro` files entirely. Decision held: keep them as **local astro dev/preview fallback** (CF `_redirects` only honored in production). Comment headers in both files explain the dev-vs-prod split. Pattern: when a feature is environment-specific (CF Pages-only behavior), preserve the dev-time fallback so localhost development isn't broken.

- **D-P10-3 Backgrounds preserved full-width in landing container fix (10.2).** Two layout options were presented for landing max-w fix: (a) constrain entire `<section>` (kills full-width hero/strip backgrounds), (b) constrain inner content only (preserves backgrounds). Daisy ack: option b. Backgrounds are a deliberate visual weight; constraining them too would reduce the "magazine feel" of the landing. **Decision held**: section keeps `bg-X py-Y border-b`, inner div gets `max-w-screen-xl mx-auto px-7`. 5 sections all follow the same pattern.

- **D-P10-4 ThemeToggle = tile 3 buttons, NOT dropdown.** Daisy ack 2026-04-30 (clarified): tile mirroring LangSwitcher exactly — 3 inline buttons, current highlighted. Alternative was a dropdown (more compact, but obscures state until opened). Decision held: tile beats dropdown for 3-state toggles where (a) state visibility is a UX requirement, (b) the user just complained that the cycle button hid state. Dropdown has the same state-hiding problem; tile fixes both.

- **D-P10-5 Daisy sweep scope: web + release/v1.0/, NOT .work/.** Daisy ack 2026-04-30. Internal `.work/` directory has 192 "Daisy" occurrences as historical/process trace (reviewer reports, retros, PLAN docs, kickoffs). Replacing them would rewrite history and break archeology references. **Decision held**: public surfaces (web + release docs) get the real name; internal trace stays as-is. Pattern: distinguish "public-facing" from "process trace" when doing global text replacements.

- **D-P10-6 GH Release v1.0 zip NOT re-cut over name swap.** PLAN §2 task 10.4 caveat. Re-uploading assets would invalidate the v1.0 immutable tag. Cost: small inconsistency until v1.1+ release pack. Benefit: v1.0 stays immutable as advertised; users who downloaded 4-28 don't see asset hash changes. **Decision held**: defer to next release pack.

- **D-P10-7 Reviewer = `oh-my-claudecode:verifier`.** Daisy ack via PLAN reference (PLAN §4 + handoff §"How the Phase 10 session should start" recommendation). 2nd-burn omc-family but NEW agent within family (Phase 6 used `critic`). Cross-family vs Phase 7 superpowers / Phase 8 pr / Phase 9 feature-dev. Sustained Rule D writer/reviewer isolation chain. Verifier's evidence-based "is the polish actually polished" lens fit perfectly for this phase: 0 HIGH / 0 MEDIUM / 2 LOW with one of the LOWs (F-1) being a process-discipline catch (`_progress.json` housekeeping that wouldn't surface from a code-only review). **Decision held**: cross-family rotation working as designed; verifier lens is right for UX-polish phases.

- **D-P10-8 Subagent_prompts/ trace dir + reviewer report committed at Phase close** (D-P6-6 → D-P7-* → D-P8-* → D-P9-8 → D-P10-8). Cleaner chronological commit; reviewer prompt + report co-located. **Pattern locked across 5 phases.**

---

## Rule A/B/C/D/E compliance

- **Rule A** semantic spot-check: 12 new i18n strings (theme.label/light/dark/system × 3 langs) — writer N=12 + reviewer N=20+ (8 additional). All natural, 0 errors. **WARRANTED + EFFECTIVE** (mass-replacement context).
- **Rule B** failures archive: 0 entries in `evidence/failures/`. No halt states, no abandoned attempts. Compliant.
- **Rule C** retrospective: this file. Three-section structure (R / G / D) per template. Compliant.
- **Rule D** writer/reviewer isolation: writer = main session opus 1M context (direct mode for all 4 tasks + 5th fix bundle) + reviewer = `oh-my-claudecode:verifier` (different agent + different context + different lens; cross-family rotation sustained 5 phases). Compliant.
- **Rule E** cross-platform learning: not applicable (website-only scope). 0 candidates filed for global rules absorption this phase.

## Phase-spanning patterns (Rule E candidates from Phase 10)

- **R-P10-7 (`_progress.json` should be an executable state machine, not just opening + closing snapshots)**: candidate for `~/.claude/templates/workflow-tier2.md` template addition: add a "post-task" step in §3 protocol → "update `_progress.json` `status` field + append to `completed_steps`". G-P10-1 sister.

- **R-P10-4 (mass-replacement requires pre-flight counted baseline + post-state grep verify)**: candidate for `~/.claude/CLAUDE.md` `personal_operating_principles` rule addition: extend Rule A coverage to include "any sed/find-replace with N>5 occurrences gets pre-flight count + post-state verify; commit message documents methodology (occurrences-vs-lines)". G-P10-2 sister.

- **G-P10-3 (visual smoke is a documented evidence step for UX-class phases)**: candidate skill template addition for any phase that touches visible chrome (theme/i18n/layout/typography). Visual smoke evidence (screenshot via chrome-devtools MCP `take_screenshot` if available, else "verified at localhost:4321 — see commit message for surfaces tested").

These are CANDIDATES for Rule E absorption; final decision Daisy's at v1.1 retro / cross-platform retro.

---

## Phase 10 close metrics

| Metric | Phase 9 baseline | Phase 10 close | Delta |
|---|---|---|---|
| tsc errors | 0 | 0 | — |
| vitest pass | 47/47 | **51/51** | +4 (ThemeToggle 6 new − 2 old) |
| vitest files | 11 | 11 | — |
| e2e pass | 7/7 | 7/7 | — |
| e2e lane | `npm run preview` | `npm run preview` | — |
| build pages | 31 | 31 | — |
| Pagefind pages | 27 | 27 | — |
| Pagefind words | 6454 | **6457** | +3 (Bojiang Zhang name additions) |
| dist/pagefind artifacts | 17 | 17 | — |

| Commit | Subject | Files | LOC delta |
|---|---|---|---|
| `58173ba` | 10.1 CF _redirects 301 | 3 | +24 / -0 |
| `09e6424` | 10.2 Landing container | 5 | +113 / -103 |
| `41f2aee` | 10.3 ThemeToggle 3-button | 6 | +90 / -33 |
| `a718c95` | 10.4 Daisy → Bojiang Zhang | 26 | +60 / -60 |
| `39c7d68` | 10.5 reviewer fix bundle | 3 | +480 / -0 (mostly trace artifacts) |
| (pending) | 10.6 close + handoff + index sync | TBD | TBD |

Family pool state at Phase 10 close (sustained from Phase 9):
- pr-review-toolkit ×5 / feature-dev ×2 / **oh-my-claudecode ×2** (NEW agent verifier in 2nd burn) / superpowers ×1 = 4 active families on website lane.

Ready for: Phase 11 (TBD scope — see Phase 10→11 handoff).
