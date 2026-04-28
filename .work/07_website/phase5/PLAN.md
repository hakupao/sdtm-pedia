# Website Phase 5 — Docs Reader (Tier 3 plan trace)

> **Date opened**: 2026-04-28
> **Master plan**: `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` §"Phase 5" lines 2010-2312
> **Handoff**: `.work/meta/website_phase4_to_phase5_handoff_2026-04-28.md`
> **Branch**: `main` (HEAD = `8e7bd83` post Phase 8.3 + H2 Step 3)

## Scope

Build the docs reader: 3-col layout (sidebar + article + on-page TOC) + markdown body styling + catchall `[lang]/guide/[...slug]` route + `/changelog` + lang-neutral handling for trilingual `DEMO_QUESTIONS.md`.

## Pre-flight decisions (handoff §"How the new session should start")

| # | Question | Decision | Rationale |
|---|---|---|---|
| 1 | H2 (zip files exist) | ✅ resolved pre-Phase-5 by Phase 8.1-8.3 + H2 Step 1 (`PUBLIC_RELEASE_PUBLISHED=true` default + GH release v1.0 live) | unblocks Phase 5 entry; no carryover work |
| 2 | DEMO_QUESTIONS lang attribution | **Option B**: drop `lang` from frontmatter (already optional in schema), treat as language-neutral; suppress "translation pending" banner when `entry.data.lang` undefined | DEMO is trilingual inline (题面三语), banner would mislead. CHANGELOG keeps `lang: en` (actually English) |
| 3 | Link-resolution e2e | **Add as 5.3 Step 5 increment**: walk every `<a href>` in `<main>` (or `article`), HEAD/GET, assert ≠404. Run for `/zh/`, `/zh/guide/user-guide`, `/zh/changelog` | the textbook structural-PASS-vs-semantic-PASS catch the Phase 4 reviewer flagged; cheap insurance |

## Task breakdown

| Task | Mode | Spec | Owner |
|---|---|---|---|
| 5.1 DocsLayout + Sidebar + TOC + PrevNextNav | subagent (executor opus) | plan §5.1 lines 2012-2155 | dispatched |
| 5.2 prose.css | direct (trivial) | plan §5.2 lines 2157-2205 | main session |
| 5.3 [...slug].astro + lang fallback + /changelog + link-resolution e2e | subagent (executor opus) | plan §5.3 lines 2207-2308 + decision 2 + decision 3 | dispatched |
| 5.4 (gate) end-of-Phase-5 reviewer | reviewer subagent | full Phase 5 commit range | feature-dev:code-reviewer |

## Reviewer slot pre-allocation (Rule D, project memory feedback_verification_pass_criteria + personal regulation D)

Phase 1-4 reviewer family hot list (must NOT collide):
- Phase 1 reviewer: `pr-review-toolkit:code-reviewer`
- Phase 2 reviewer: `pr-review-toolkit:code-reviewer`
- Phase 3.6 reviewer: `pr-review-toolkit:code-reviewer`
- Phase 4 reviewer: `pr-review-toolkit:code-reviewer`

**Phase 5 reviewer slot = `feature-dev:code-reviewer`** — cross-family from `pr-review-toolkit`, no in-session writer collision (writer = `executor` opus subagent, reviewer = different subagent_type + different family). Backup if dispatched: `oh-my-claudecode:code-reviewer`.

## Evidence layout

```
.work/07_website/phase5/
├── PLAN.md                                  ← this file
├── _progress.json                           ← step-by-step verdicts (writer + reviewer)
├── evidence/
│   ├── checkpoints/
│   │   ├── task_5_1_report.md               ← post-5.1 build/test verdict
│   │   ├── task_5_2_report.md
│   │   ├── task_5_3_report.md
│   │   └── phase_5_reviewer_report.md       ← end-of-Phase-5 reviewer verdict
│   └── failures/                            ← Rule B: failed attempts archived, never deleted
└── subagent_prompts/                        ← Rule C support: dispatched prompts archived for retro
```

## Carryover from Phase 4 still to handle inside Phase 5

- M1 — link-resolution e2e (handled in 5.3 Step 5 increment).
- M2 — TopNav drawer + ViewTransitions (NOT enabling VT in Phase 5; defer).
- M3 — `compare-dimensions.json` parity test (defer to Phase 6 when /compare lands).
- M4 — `<noscript>` no-JS unhide (defer to Phase 4.X polish bundle; not Phase 5 scope).
- Phase 3 H1 (`replaceLangInPath` regex query edge) — only surfaces if client-side mutates pathname; sidebar uses Astro path → not bitten.
- Phase 3 M3 (DEMO_QUESTIONS lang) — **resolved by decision 2 above**.

## Exit criteria

1. `cd web && npm test -- --run` green (29 → ≥31 vitest, +2 for new components if any add tests; main session won't add component-level tests for layout — covered by e2e).
2. `cd web && npm run build` green; `web/dist/{zh,en,ja}/guide/{user-guide,glossary,demo-questions,known-limitations,platform-comparison}/index.html` all present + `web/dist/{zh,en,ja}/changelog/index.html`.
3. `cd web && npm run test:e2e` green; new tests:
   - `docs reader renders user-guide in zh`
   - `link-resolution: every <a> in main resolves ≠404` (per decision 3)
4. `cd web && npx tsc --noEmit` clean.
5. Reviewer (`feature-dev:code-reviewer`) verdict ≥ CONDITIONAL_PASS with all HIGH fixed.
6. Phase 5 → Phase 6 handoff doc written at `.work/meta/website_phase5_to_phase6_handoff_2026-04-28.md`.

## Rule A semantic spot-check (per personal operating rule A)

Phase 5 doesn't compress/rewrite content (unlike release translation). Skip Rule A formal N-sample audit, BUT post-build manually verify:
- `/zh/guide/user-guide` page renders Chinese USER_GUIDE.zh.md content (not English fallback).
- `/zh/guide/demo-questions` page renders DEMO_QUESTIONS.md (lang-neutral, no banner).
- `/zh/guide/known-limitations` renders English KNOWN_LIMITATIONS.en.md WITH "translation pending" banner (decision 2 only suppresses banner when lang undefined; en→zh fallback should still show it).

## Rule B — failure archive

Any failed attempt → `evidence/failures/task_5_X_attempt_Y.md` with input/output/judgment/next-attempt-input. Never `rm`.

## Rule C — retrospective at Phase 5 close

`.work/meta/website_phase5_to_phase6_handoff_2026-04-28.md` to triple-section §1 retained, §2 gaps, §3 decisions; absorb into next phase plan.
