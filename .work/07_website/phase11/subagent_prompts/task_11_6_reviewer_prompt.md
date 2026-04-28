# Phase 11 Reviewer Brief — `oh-my-claudecode:code-reviewer`

> **Date**: 2026-04-30
> **Reviewer slot**: `oh-my-claudecode:code-reviewer` (per PLAN §1 + handoff §"How the Phase 11 session should start" recommendation)
> **Family pool extension**: 3rd-burn omc-family NEW agent within family. omc family lineage on website lane: Phase 6 `critic` (1st) → Phase 10 `verifier` (2nd, NEW) → Phase 11 `code-reviewer` (3rd, NEW). Cross-family vs Phase 9 feature-dev / Phase 8 pr / Phase 7 superpowers — sustained Rule D 6-phase rotation chain at omc family extension.
> **Stress dimensions D1-D7** (sustained from Phase 7/8/9/10 reviewer brief pattern, adapted to Phase 11 surface — chrome layout + new feature + i18n + a11y).

## Scope of review

Phase 11 = 5 implementation commits on `main` (HEAD = `6c92b05`):

- **`e36354c`** — 11.1 TopNav + Footer max-w-screen-xl content wrap
- **`43c0b84`** — 11.2 ⌘K hint → "搜索/Search/検索" Option A (search.shortcut key removed; new search.label key)
- **`41c54da`** — 11.3 TopNav utilities visual divider (border-l between [search]/[lang]/[theme] groups)
- **`d01aa0a`** — 11.4 DocsLayout add Footer mount (Footer was missing on docs reader)
- **`6c92b05`** — 11.5 v1.2 font-size 4-tier adjuster (FontSizeToggle component + lib + CSS + 15 i18n keys + 6 tests + caller mount + flash prevention)

Branch: `main`. Pre-Phase-11 baseline: HEAD was `cdd8f8e` (Phase 10 close). Phase 11 commits unpushed at review time.

Scope discipline: only the 5 user-driven UX items above. C-P9-1..16 + C-P10-1..5 carryover NOT in scope (Daisy 2026-04-30 PM ack: implement v1.2 polish, not the older carryover bundle).

## What you must do (D1-D7 + Rule A)

### D1 — TopNav + Footer max-w-screen-xl chrome wrap (11.1)

Read `web/src/components/astro/TopNav.astro` + `Footer.astro`:
- Outer `<header>`/`<footer>` keeps `bg + border` full-width strip
- Inner `<div class="max-w-screen-xl mx-auto px-7 py-N">` constrains content
- Mobile px-7 28px parity preserved with landing (Phase 10.2)

Verify: visually consistent width with landing on desktop ≥1280px. Check that the wrap doesn't break TopNav's `flex justify-between items-center` layout — the `<div>` wrapper now holds those classes.

### D2 — ⌘K hint Option A (11.2) + Rule A semantic spot-check on new keys

Read `web/src/i18n/ui.{zh,en,ja}.json`:
- `search.shortcut` key removed from all 3 langs
- `search.label` key added: zh "搜索" / en "Search" / ja "検索"
- 5 new fontsize keys × 3 langs = 15 strings (added in 11.5)

Read `web/src/components/astro/TopNav.astro`:
- Search button text + aria-label both reference `t['search.label']`
- Cmd+K trigger `onclick` keyboard event still wired (only visible hint deleted)

**Rule A semantic spot-check** (mass-replacement context — 18 total new i18n strings = 1 search.label × 3 + 5 fontsize × 3 = 18):
- zh "搜索" / "字号" / "小/中/大/特大" — natural? canonical UI terminology?
- en "Search" / "Font size" / "Small/Medium/Large/X-Large" — standard?
- ja "検索" / "文字サイズ" / "小/中/大/特大" — natural Japanese? Should "特大" use カタカナ "Xラージ" instead? Consider zh-as-template ja convention.

Flag any awkward fragments as F-* finding. Verify helpers.test.ts parity test still passes (vitest 57/57 implies key count parity confirmed).

### D3 — TopNav utilities visual divider (11.3) + dividers consistency

Read `web/src/components/astro/TopNav.astro` post 11.3:
- 4 vertical dividers via `border-l border-rule pl-4 [pr-4]` pattern: nav-utilities | [search] | [lang] | [theme] | [fontsize]
- Note Phase 11.5 added 5th utility group (fontsize) AFTER 11.3 was committed — verify the divider pattern was sustained correctly when fontsize was added

Verify: visually each group reads as distinct unit; spacing consistent across 4 group boundaries; no border-l collision with text.

### D4 — DocsLayout Footer mount (11.4) + parity with LandingLayout

Read `web/src/layouts/{Landing,Docs}Layout.astro`:
- Both layouts now mount `<Footer lang={lang} />` before `</BaseLayout>`
- Footer is full-width strip (Phase 11.1) with internal max-w-screen-xl content
- DocsLayout flex container (DocsSidebar+article+DocsTOC) closes before Footer — verify document flow

Verify: docs reader pages now have footer; check that Footer's `bg-ink text-bg` strip doesn't overlap with DocsTOC's potentially-sticky positioning.

### D5 — v1.2 font-size 4-tier adjuster (11.5) — biggest verification target

Read in order:
- `web/src/lib/fontSize.ts` — 22 LOC (FontSize type + 3 functions)
- `web/src/components/react/FontSizeToggle.tsx` — 45 LOC (mirrors ThemeToggle.tsx)
- `web/src/components/react/FontSizeToggle.test.tsx` — 6 tests
- `web/src/styles/global.css` — `:root --fs-base: 100%` + 3 data-fontsize overrides + `html { font-size: var(--fs-base) }`
- `web/src/layouts/BaseLayout.astro` — flash-prevention inline script extended to read 'fontsize' alongside 'theme'
- `web/src/components/astro/TopNav.astro` — FontSizeToggle mounted in own `border-l` divider span after ThemeToggle

Stress points:
- **a11y**: 4 buttons inside `<nav aria-label>`, aria-pressed boolean toggle (correct WAI-ARIA for state, NOT aria-current). Each button has aria-label + title from i18n labels prop. Tab focus → arrow/space/enter activation works (focus-visible CSS from Phase 9 covers this).
- **localStorage**: key 'fontsize' → 4 valid values, default 'md' (which clears the data attribute, no CSS specificity drift).
- **Flash prevention**: BaseLayout inline script reads BOTH 'theme' and 'fontsize' before paint. Verify try/catch wraps both.
- **CSS strategy**: percentage-based (87.5% / 100% / 112.5% / 125%) respects browser-level zoom defaults (a11y win) over absolute px override. Tailwind rem-relative scales; chrome text-[Npx] arbitrary stays fixed by design.
- **Default behavior**: 'md' tier removes attribute (line 16 of fontSize.ts) — verify CSS handles absent attribute as default 100%.
- **Caller wiring**: TopNav passes `navLabel + labels` props; FontSizeToggle uses both correctly.
- **Tests**: 6 vitest tests cover render-4-buttons / Medium-pressed-default / Small-click-persists+applies+flips / X-Large-click-persists+applies / Medium-after-Large-removes-attribute / nav-aria-label-from-prop.

### D6 — No regressions (test re-run)

Run locally:
```bash
cd web && npx tsc --noEmit                       # 0 errors expected
cd web && npm run test                            # 57/57 expected (+6 from FontSizeToggle vs Phase 10's 51/51)
cd web && npm run test:e2e                        # 7/7 expected
cd web && npm run build                           # 31 HTML pages expected
```

Pagefind index should still report 27 indexed pages (Phase 11 changes affect chrome + new feature, not docs body content).

### D7 — Plan deviation flag

Verify `git diff cdd8f8e..6c92b05 --name-only` shows zero files outside:
- `web/src/components/{astro,react}/`
- `web/src/i18n/`
- `web/src/layouts/`
- `web/src/lib/`
- `web/src/styles/`
- `web/tests/e2e/`
- `.work/07_website/phase11/`

No C-P9-1..16 or C-P10-1..5 carryover silently absorbed.

## Output format

Standard severity-rated checkpoint report at:
`.work/07_website/phase11/evidence/checkpoints/phase_11_reviewer_report.md`

Findings: F-1, F-2, ... HIGH / MEDIUM / LOW. Verdict: PASS / CONDITIONAL_PASS / FAIL.

If CONDITIONAL_PASS:
- Recommend fix-bundle scope (HIGH always, MEDIUM if mechanical/co-located, LOW carryover to Phase 12)
- Pattern: same as Phase 7.5 / Phase 8.5 / Phase 9.14 / Phase 10.5 fix bundles

## Reviewer constraints

- READ-ONLY recommended; do not modify source files (code-reviewer role separation)
- Run shell commands: `grep`, `cd web && npm run {build,test,test:e2e}`, `npx tsc --noEmit`, `git show`, `git diff`
- Do NOT push to origin; do NOT amend commits
- Trace artifacts written by reviewer go under `.work/07_website/phase11/evidence/checkpoints/`

## References

- PLAN: `.work/07_website/phase11/PLAN.md`
- Progress: `.work/07_website/phase11/_progress.json`
- Phase 10 → 11 handoff: `.work/meta/website_phase10_to_phase11_handoff_2026-04-30.md`
- Reviewer pattern lineage: Phase 7 → Phase 8 → Phase 9 → Phase 10 → THIS

## Output to caller (under 400 words)

1. Verdict (one word)
2. Findings count by severity (H=N M=N L=N)
3. Top-3 findings (one line each)
4. Whether you recommend a fix-bundle commit before phase close, with scope
5. Path to your full report file
