# Website Phase 9 — Pre-Public-Release Polish + QA Bundle

> **Date opened**: 2026-04-30
> **Tier**: 3 (multi-step, release-grade, ack'd Option D)
> **Branch**: `main`. HEAD = `0e682a7`. (`M CLAUDE.md` + 4 untracked `?? batch_47..49 / reconciler_round12 kickoff.md` are 06 Deep Verification round-12 prep — DO NOT touch.)

## §0 — Archeology finding (re-scoping)

The Phase 8→9 handoff (`.work/meta/website_phase8_to_phase9_handoff_2026-04-29.md`) recommended Phase 9 = master plan §"Phase 8 — Downloads Pipeline". **That premise is wrong**: Pre-flight `git log --oneline web/scripts/build-bundles.sh web/RELEASE.md` + `gh release view v1.0` + `git ls-remote --tags origin` revealed Tasks 8.1+8.2+8.3 already shipped on `main` four commits below the Phase 5/6/7/8 (Search) chain:

| Commit (UTC) | What | State |
|---|---|---|
| `2de87c4` 2026-04-28 09:37 | Phase 8.1+8.2 — `web/scripts/build-bundles.sh` + `web/RELEASE.md` + corrected `web/src/data/downloads.json` | merged on `main` |
| `8e7bd83` 2026-04-28 09:44 | Phase 8.3 — **GH Release `v1.0` cut LIVE** (4 zip assets) + DownloadsSection feature flag inverted to default-published | merged on `main`, tag `v1.0` pushed `origin` |

Verified: `gh release view v1.0` → 4 assets / published `2026-04-28T00:42:36Z` / title "v1.0 — Company Release (Internal)". Master plan §"Phase 9 — CF Pages Deploy" is similarly already done — `web/.cloudflare-pages.md` (5351 bytes) shipped as part of Phase 9.2 spec, production `https://sdtm-pedia.pages.dev/` is live. Master plan §"Phase 10.4 README" was done in Phase 7.3 (`web/README.md`).

**Real Phase 9 scope (Daisy ack'd Option D 2026-04-30)**: combine remaining master plan §"Phase 10 — QA + Polish" tasks **plus** Phase 8 carryover `C-P8-1..6` **plus** selected Phase 6/7 deferred carryover. Ship a single pre-public-release polish-and-QA bundle.

## §1 — Scope (Option D: B + C combined)

| Bundle | Source | Contents |
|---|---|---|
| **A** Phase 8 carryover (C-P8-1..6) | `.work/meta/website_phase8_to_phase9_handoff_2026-04-29.md` §"Phase 9 carryover" | C-P8-1 playwright preview lane / C-P8-2 real keypress promotion / C-P8-3 focus return / C-P8-4 aria live / C-P8-5 retry backoff (assess) / C-P8-6 mobile UX (defer) |
| **B** Phase 6/7 deferred polish (selective) | Phase 8 close handoff §"Pre-existing Phase 6/7 carryover" | C-P5-L2 empty TOC guard / C-P6-6 plugin throw fixture test / C-P6-7 zod schema for `downloads.json` + `compare-dimensions.json` / C-P7-6 4 redirect HTML warnings |
| **C** Master plan §"Phase 10" QA | `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` lines 2864+ | 10.1 Lighthouse on prod URL / 10.2 axe + focus-visible CSS / 10.3 cross-browser smoke / 10.5 final 8-item verify checklist |

**Out of scope** (deferred to v1.1 polish OR explicit user direction): C-P8-6 mobile UX (no UX direction yet) / C-P6-5 `/guide/platform-comparison` vs `/compare` redundancy (design decision) / C-P5-M2 ViewTransitions / C-P7-7 Rule A rubric expansion (process docs) / C-P7-8 README "auto-deploys from main" verify (manual CF dashboard check) / C-P7-1 Astro i18n soft-404 (accepted).

## §2 — Tasks (sequence)

| Task | What | Files | Verification | Mode |
|---|---|---|---|---|
| **9.1** | C-P8-1 playwright `npm run dev` → `npm run build && npm run preview` lane | `web/playwright.config.ts` | `npm run test:e2e` 7/7 pass against built dist | direct main session (~5 LOC config edit) |
| **9.2** | C-P8-2 promote `search.spec.ts` synthetic keydown → real `page.keyboard.press('Control+k')` | `web/tests/e2e/search.spec.ts` | e2e 7/7 incl real keypress green | direct (~10 LOC test edit) |
| **9.3** | C-P8-3 focus-return + C-P8-4 aria live region in SearchOverlay | `web/src/components/react/SearchOverlay.tsx` + `.test.tsx` | vitest 36/36 (+2 focus + live region tests) / e2e still 7/7 | direct (~15 LOC) |
| **9.4** | C-P8-5 1-retry backoff on Pagefind init failure | `SearchOverlay.tsx` | vitest +1 retry test (or merge with 9.3) | direct (~8 LOC) — assess if cheap |
| **9.5** | 10.2 focus-visible CSS for keyboard a11y | `web/src/styles/global.css` | dist HTML grep `*:focus-visible` selector emitted via Tailwind class OR raw CSS class — visual smoke via dev server | direct (~6 LOC CSS) |
| **9.6** | C-P5-L2 empty TOC `<aside>` guard | `web/src/components/astro/DocsLayout.astro` (or wherever TOC renders) | vitest spec covers empty heading list path | direct (~3 LOC) |
| **9.7** | C-P6-6 vitest fixture for plugin lang-neutral throw | `web/remark-md-link-rewrite.test.mjs` (NEW) | vitest +1 = 37/37 | direct (~25 LOC test) |
| **9.8** | C-P6-7 zod schema for `downloads.json` + `compare-dimensions.json` | `web/src/data/schemas.ts` (NEW) + import in consumers | tsc validates at build, +runtime parse smoke | direct (~30 LOC) |
| **9.9** | C-P7-6 4 redirect pages `<html lang>` (suppress Pagefind warnings) | `web/src/pages/[lang]/guide/index.astro` (and 3 sibling redirects if any) | `npm run build` Pagefind output 0 redirect warnings | direct (~3 LOC × N redirects) |
| **9.10** | 10.1 Lighthouse audit on production URL | `web/qa/lighthouse-zh-landing-2026-04-30.{html,json}` (NEW) | Performance / Accessibility / Best Practices ≥ 95 (target per spec §9; if any < 95, identify + remediation TBD) | chrome-devtools MCP `lighthouse_audit` |
| **9.11** | 10.3 cross-browser smoke (Chrome automated; Safari/Firefox checklist for Daisy manual) | `web/qa/cross-browser-2026-04-30.md` (NEW) | Chrome auto green; Safari/Firefox documented as manual-checklist for Daisy | chrome-devtools MCP + manual handoff |
| **9.12** | 10.5 final 8-item verify checklist | `.work/07_website/phase9/evidence/checkpoints/final_verify_checklist.md` (NEW) | 8 items checked: CF green / `https://sdtm-pedia.pages.dev/zh/` renders / 4 download links 302 / `/compare` filter / Cmd+K search / theme toggle / lang switcher / Lighthouse ≥ 95 | direct + curl + e2e |
| **9.13** | Reviewer dispatch | `.work/07_website/phase9/subagent_prompts/task_9_13_reviewer_prompt.md` (NEW) | `feature-dev:code-architect` (2nd-burn feature-dev family, NEW agent within family — code-architect vs Phase 5 code-reviewer); cross-family from Phase 8 pr-family + Phase 7 superpowers + Phase 6 omc-critic | adversarial review with explicit D1-D7 stress dims |
| **9.14** | Reviewer fix bundle (if CONDITIONAL_PASS) | TBD per findings | reviewer effective PASS | direct main session |
| **9.15** | Master plan annotation re: 4-28 archeology + Phase 9 close handoff + RETROSPECTIVE.md + index sync | `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` + `.work/meta/website_phase9_to_phase10_handoff_2026-04-30.md` (NEW) + `.work/07_website/phase9/RETROSPECTIVE.md` (NEW) + CLAUDE.md Key Paths + MANIFEST + PROGRESS + worklog | git status clean | direct |

## §3 — Reviewer slot pre-allocation

**Slot**: `feature-dev:code-architect` (Daisy ack 2026-04-30 entry decision b).
- **Family rotation**: feature-dev family 2nd burn (Phase 5 = `feature-dev:code-reviewer`); NEW agent within family.
- **Cross-family vs Phase 8**: Phase 8 = `pr-review-toolkit:silent-failure-hunter`; ✓
- **Lens fit**: architect lens for "is the design fit for purpose?" — Phase 9 spans cross-cutting concerns (e2e infrastructure, schema design, a11y CSS, QA evidence chain, archeology). code-architect's "comprehensive implementation blueprint" perspective suits release-grade pre-public-release polish.
- **Verified registered**: ✓ (per C-P8-8 lesson — agent definition includes `feature-dev:code-architect` in this environment's roster).
- **Backup**: `oh-my-claudecode:verifier` (evidence-based verification of GH Release URL resolution + final 8-item checklist).

## §4 — Plan deviation flag

**NONE** — Phase 9's actual scope matches master plan §"Phase 10 — QA + Polish" + carryover absorption queues. Two non-deviation observations:

1. **Renumbering archeology**: master plan §"Phase 8 Downloads" + §"Phase 9 CF Deploy" + §"Phase 10.4 README" already done (4-28 / 4-28 / Phase 7.3); Phase 9 of THIS execution covers what master plan called §"Phase 10 — QA + Polish" + Phase 8 close carryover. Annotation in 9.15.
2. **10.1 Lighthouse target ≥ 95** is master plan target; if any category < 95 in 9.10, document remediation as 9.10b sub-task or carryover C-P9-* (don't block Phase 9 close on a 94 if remediation cost > marginal value).

## §5 — Carryover absorption matrix

| Carryover ID | Source phase | Disposition |
|---|---|---|
| C-P8-1 playwright preview lane | Phase 8 close | ABSORB Task 9.1 |
| C-P8-2 real keypress promotion | Phase 8 close | ABSORB Task 9.2 |
| C-P8-3 focus return | Phase 8 close | ABSORB Task 9.3 |
| C-P8-4 aria live region | Phase 8 close | ABSORB Task 9.3 |
| C-P8-5 retry backoff | Phase 8 close | ASSESS Task 9.4 (cheap → absorb; complex → defer to v1.1) |
| C-P8-6 mobile UX | Phase 8 close | DEFER (no UX direction) |
| C-P8-7 pre-PLAN infrastructure grep | Phase 8 process improvement | RESOLVED via §0 archeology pre-flight (this PLAN demonstrates it) |
| C-P8-8 reviewer agent registration verify | Phase 8 process improvement | RESOLVED via §3 verified-registered annotation (this PLAN demonstrates it) |
| C-P5-L2 empty TOC guard | Phase 5 close | ABSORB Task 9.6 |
| C-P6-4 playwright reuseExistingServer | Phase 6 close | RESOLVED transitively via Task 9.1 (preview lane behavior re-evaluated) |
| C-P6-5 compare route redundancy | Phase 6 close | DEFER (design decision out of scope) |
| C-P6-6 plugin throw fixture | Phase 6 close | ABSORB Task 9.7 |
| C-P6-7 schema validation | Phase 6 close | ABSORB Task 9.8 |
| C-P7-1 Astro i18n soft-404 | Phase 7 close | ACCEPTED indefinitely (documented `web/README.md`) |
| C-P7-6 redirect HTML warnings | Phase 7 close | ABSORB Task 9.9 |
| C-P7-7 Rule A rubric expansion | Phase 7 close | DEFER (process improvement, no urgent action) |
| C-P7-8 README CF auto-deploy verify | Phase 7 close | DEFER (Daisy manual verify in CF dashboard) |
| C-P7-10 CF preview probe checklist | Phase 7 close | RESOLVED transitively via `web/.cloudflare-pages.md` §"First-deploy walkthrough" + §"Troubleshooting" |

## §6 — Exit criteria

1. ✅ All §2 tasks 9.1-9.12 verified GREEN (vitest 37+/37+, e2e 7+/7+, tsc 0, build 31+ pages, Lighthouse ≥ 95 OR documented exception)
2. ✅ Reviewer (Task 9.13) verdict effective-PASS post any 9.14 fix bundle
3. ✅ Master plan annotated (4-28 archeology + Phase 9-of-execution = master plan §"Phase 10")
4. ✅ Phase 9 close handoff written (Rule C retro: R-P9-* / G-P9-* / D-P9-* / C-P9-* namespace)
5. ✅ Index sync: CLAUDE.md Key Paths / MANIFEST / PROGRESS / worklog
6. ✅ Tier 3 trace preserved: PLAN.md + `_progress.json` + `evidence/checkpoints/` + `evidence/failures/` + `subagent_prompts/` + RETROSPECTIVE.md + audit_matrix.md

## §7 — References

- Master plan: `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` §"Phase 8 — Downloads Pipeline" (already done 4-28) + §"Phase 9 — CF Pages Deploy" (already done) + §"Phase 10 — QA + Polish" (this Phase 9 covers)
- Phase 8 close handoff: `.work/meta/website_phase8_to_phase9_handoff_2026-04-29.md`
- Phase 8 reviewer report: `.work/07_website/phase8/evidence/checkpoints/phase_8_reviewer_report.md`
- Phase 7 close handoff: `.work/meta/website_phase7_to_phase8_handoff_2026-04-29.md`
- CF Pages settings: `web/.cloudflare-pages.md`
- Release runbook: `web/RELEASE.md`
- GH Release: `https://github.com/hakupao/sdtm-pedia/releases/tag/v1.0` (LIVE)
- Production: `https://sdtm-pedia.pages.dev/`
