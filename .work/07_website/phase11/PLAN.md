# Phase 11 — v1.2 UX Polish + Font-Size 4-Tier Adjuster

> **Tier**: 2 (mid-large; 5 implementation tasks + reviewer + close, ~half-day)
> **Status**: PLAN ack'd inline 2026-04-30 (Daisy: "把这次就当作1.2，1.1可以结束了" + D-P11-1=A + D-P11-2=全实施)
> **Branch**: `main`. HEAD = `cdd8f8e` (Phase 10 close).
> **Reviewer slot**: `oh-my-claudecode:code-reviewer` (3rd-burn omc-family NEW agent vs Phase 6 critic + Phase 10 verifier; cross-family vs Phase 9 feature-dev / Phase 8 pr / Phase 7 superpowers — sustained Rule D 6-phase rotation chain at omc family extension)
> **Plan deviation flag**: NONE — post-master-plan v1.2 release scoped from Daisy 2026-04-30 user feedback (5 items raised, all in scope, ⌘K hint Option A "完全替换" + font-size adjuster from C-P10-3 deferred).

## §0 Pre-flight state (2026-04-30 PM, post Phase 10 push)

| Field | Value |
|---|---|
| Branch | `main` |
| HEAD | `cdd8f8e` (Phase 10 close) |
| `origin/main` | same |
| Production | `https://sdtm-pedia.pages.dev/` LIVE post Phase 10 (HTTP/2 301 + footer "Bojiang Zhang" + ThemeToggle 3-button verified 2026-04-30) |
| Test baseline | tsc 0 / vitest 51/51 / e2e 7/7 / build 31 pages / Pagefind 27 / 6457 words |

## §1 User-driven scope (Daisy 2026-04-30 PM)

5 items raised verbatim post Phase 10 verification:

1. **页眉 (TopNav) 页脚 (Footer) 宽度** 也要和中间 (landing content) 一致, 不要分散两边
2. **⌘K 不要这个快捷键的显示方式**, 要写明白搜索的中日英文表达 ("搜索"/"Search"/"検索")
3. **右上角挤一起没分割**, 要区分开 (无论用什么方式)
4. **开始字号 4 阶的计划** (从 Phase 10 deferred C-P10-3, "方案 A 独立 feature 配 layout QA")
5. **现在文档界面没有页脚显示**, 帮我加上

**Resolution** (Daisy ack 2026-04-30):
- **D-P11-1** (item 2): Option A — ⌘K hint 完全删除, 替换成 "搜索" 明文
- **D-P11-2** (item 4 scope): "把这次就当作 1.2" — 全实施 (PLAN + 实施同 phase, 不再分 Phase 12)

## §2 Tasks

### Task 11.1 — TopNav `<header>` + Footer `<footer>` max-w-screen-xl 内层 wrap

**Why**: After Phase 10.2 landing 5 sections constrained to max-w-screen-xl, TopNav + Footer remain full-width — 视觉上分散两边, 跟 landing+docs content 主体宽度不一致. Daisy: "希望页眉页脚的宽度也和中间保持一致, 而不是分散两边".

**Files**: `web/src/components/astro/TopNav.astro`, `web/src/components/astro/Footer.astro`

**Pattern** (mirroring Phase 10.2):
```astro
<!-- BEFORE -->
<header class="flex justify-between items-center px-7 py-4 border-b border-rule">
  ...children...
</header>

<!-- AFTER -->
<header class="border-b border-rule">
  <div class="max-w-screen-xl mx-auto px-7 py-4 flex justify-between items-center">
    ...children...
  </div>
</header>
```

Outer `<header>`/`<footer>`: bg + border全宽 preserved. Inner `<div>`: content constrained to max-w-screen-xl matching docs+landing.

### Task 11.2 — ⌘K hint button text → "搜索/Search/検索" (Option A)

**Why**: Daisy "Cmd K 不要这个快捷键的显示方式, 要写明白: 搜索的中日英文表达". Option A = 完全替换, 不保留 `<kbd>⌘K</kbd>` 辅助.

**Files**:
- `web/src/i18n/ui.{zh,en,ja}.json` (+1 key each: `search.label`)
- `web/src/components/astro/TopNav.astro` (button text `{t['search.shortcut']}` → `{t['search.label']}`)

**i18n keys**:
- zh: `"search.label": "搜索"`
- en: `"search.label": "Search"`
- ja: `"search.label": "検索"`

`search.shortcut` ("Cmd K") key retained for SearchOverlay internal use (placeholder hint inside the overlay if any) — only the TopNav button **text** changes. Cmd+K trigger still works (keyboard listener unchanged).

### Task 11.3 — TopNav utilities visual divider

**Why**: Post Phase 10.3 (ThemeToggle 3 buttons, was 1), right-side utilities = 1 search button + 3 LangSwitcher links + 3 ThemeToggle buttons = 7 inline items in `gap-3` `<span>`. Visually挤在一起, no separation between [search]/[lang]/[theme] groups. Daisy: "区分开, 无论用什么方式".

**Decision**: Add `border-l border-rule pl-3 ml-1` to LangSwitcher container + ThemeToggle container (or wrap each in flex span with divider). Match the existing `border-l border-rule pl-4 ml-2` separator already between nav-links and utilities — sustained design token.

**Files**: `web/src/components/astro/TopNav.astro` (single edit; LangSwitcher.tsx + ThemeToggle.tsx already accept className but cleanest is wrapping in TopNav).

### Task 11.4 — DocsLayout add Footer mount

**Why**: Daisy: "现在文档界面没有页脚显示, 帮我加上". DocsLayout.astro currently has no Footer — only LandingLayout does. Inconsistent UX between landing and docs reader. Quick fix: import Footer + mount before `</BaseLayout>`.

**Files**: `web/src/layouts/DocsLayout.astro`

**Pattern**: After `</div>` flex container (DocsSidebar+article+DocsTOC):
```astro
<Footer lang={lang} />
```

### Task 11.5 — v1.2 font-size 4-tier adjuster (Daisy "方案 A 独立 feature + layout QA")

**Why**: Daisy 2026-04-30 (Phase 10 entry): "字号太小 想要 4 阶 size adjuster small/medium/large/x-large". Deferred to v1.2 as C-P10-3; now implementing this round per "把这次就当作 1.2".

**Design**:
- 4 tiers: `sm` / `md` (default) / `lg` / `xl`
- CSS strategy: `html` element gets `data-fontsize="sm|md|lg|xl"` attribute mapped to `--fs-base` CSS variable in `global.css`:
  - `sm`: `14px` (87.5%)
  - `md`: `16px` (100% default)
  - `lg`: `18px` (112.5%)
  - `xl`: `20px` (125%)
- `html { font-size: var(--fs-base); }` — Tailwind rem-relative tokens (`text-base`, `text-lg`, `prose`, sidebar, TOC) scale automatically. Chrome `text-[Npx]` arbitrary classes stay fixed by design (preserves data-density typography intent — TopNav `text-[10px]`, SectionLabel etc).
- localStorage key `'fontsize'` → 4 valid values (default `'md'`)
- Flash-prevention inline script in `BaseLayout.astro` (mirrors theme flash prevention) reads `localStorage.getItem('fontsize')` before paint
- UI: `<FontSizeToggle>` 4-button React island mirroring `<ThemeToggle>` pattern (aria-pressed for current tier; A⁻/A/A⁺/A⁺⁺ icons or "A" with size scaling visual)
- Mount in TopNav alongside ThemeToggle (after the ThemeToggle node, before `</nav>`)

**Files**:
- NEW `web/src/lib/fontSize.ts` (mirrors theme.ts: `getStoredFontSize/setStoredFontSize/applyFontSize/type FontSize`)
- NEW `web/src/components/react/FontSizeToggle.tsx` (mirrors ThemeToggle.tsx pattern)
- NEW `web/src/components/react/FontSizeToggle.test.tsx` (vitest, mirrors ThemeToggle.test.tsx)
- EDIT `web/src/i18n/ui.{zh,en,ja}.json` (+5 keys each: `fontsize.label`, `fontsize.sm`, `fontsize.md`, `fontsize.lg`, `fontsize.xl`)
- EDIT `web/src/styles/global.css` (add `--fs-base` defaults + 4 `[data-fontsize="sm|md|lg|xl"]` overrides + `html { font-size: var(--fs-base); }`)
- EDIT `web/src/layouts/BaseLayout.astro` (add inline flash-prevention script for fontsize, alongside existing theme one)
- EDIT `web/src/components/astro/TopNav.astro` (mount `<FontSizeToggle client:load navLabel + labels />` after ThemeToggle)

**i18n keys**:
- zh: `"fontsize.label": "字号"`, `"fontsize.sm": "小"`, `"fontsize.md": "中"`, `"fontsize.lg": "大"`, `"fontsize.xl": "特大"`
- en: `"fontsize.label": "Font size"`, `"fontsize.sm": "Small"`, `"fontsize.md": "Medium"`, `"fontsize.lg": "Large"`, `"fontsize.xl": "X-Large"`
- ja: `"fontsize.label": "文字サイズ"`, `"fontsize.sm": "小"`, `"fontsize.md": "中"`, `"fontsize.lg": "大"`, `"fontsize.xl": "特大"`

**Tests** (vitest, ~6 tests):
- Renders 4 inline buttons with i18n aria-labels
- Marks "md" as pressed by default (no stored choice)
- Each click persists + applies `data-fontsize` + flips aria-pressed
- nav with passed aria-label

**QA matrix** (Daisy ack 2026-04-30 phase 10 entry: "方案 A 独立 feature 配 layout QA"):
- 4 tiers × 7 flows = 28 manual smoke checkpoints (deferred to Daisy manual post-push):
  - Flows: landing zh / landing en / landing ja / docs reader user-guide / compare table / search overlay / changelog
  - Tiers: sm 14px / md 16px / lg 18px / xl 20px
- Verify per flow: no horizontal scroll (mobile + desktop), no broken layout, prose readable, chrome text-[10px] stays unaffected (intentional)

### Task 11.6 — Reviewer dispatch `oh-my-claudecode:code-reviewer`

3rd-burn omc-family NEW agent (Phase 6 critic / Phase 10 verifier / Phase 11 code-reviewer = 3 different omc agents at 3-burn intra-family depth). Cross-family vs Phase 9 feature-dev / Phase 8 pr / Phase 7 superpowers. Sustained Rule D 6-phase rotation chain.

D1-D7 stress dimensions adapted to Phase 11 surface:
- D1 chrome layout (TopNav + Footer max-w + Footer mount on docs)
- D2 i18n parity (1 search.label + 5 fontsize.* × 3 langs = 18 new keys; Rule A spot-check)
- D3 a11y (FontSizeToggle keyboard + aria-pressed + nav label; chrome unchanged a11y)
- D4 fontsize CSS strategy (rem cascade + chrome text-[Npx] preserved + flash prevention)
- D5 no regressions (tsc/vitest/e2e/build/Pagefind unchanged baseline+adds)
- D6 plan deviation flag NONE (5 user-driven items only, no carryover absorbed)
- D7 production verify deferred post-push

### Task 11.7 — Phase 11 close + handoff + index sync + push

- RETROSPECTIVE.md (Rule C 三段 R-P11-* + G-P11-* + D-P11-*)
- Handoff `.work/meta/website_phase11_to_phase12_handoff_2026-04-30.md`
- Master plan annotation: §"Phase 10 — QA + Polish" extended with Phase 11-of-execution = post-master-plan v1.2 release
- Index sync: MANIFEST + worklog + PROGRESS (CLAUDE.md Key Paths still deferred if round-12 dirty state persists)
- Single push to origin/main

## §3 Test + verify protocol

After each task: `cd web && npm run build` (31 pages) + `npm run test` (vitest) + `npm run test:e2e` (7/7) + `npx tsc --noEmit` (0).

After all tasks (final pre-push):
- vitest 51 → ~57+ (FontSizeToggle tests +6)
- e2e still 7/7 (no DOM-structure asserts)
- build 31 pages
- Pagefind 27 indexed (footer mount on docs may add no new index since docs body is data-pagefind-body region — verify)
- localhost visual smoke 4-tier × 7-flow matrix (Daisy or manual)

After push: curl 301 + footer "Bojiang Zhang" + theme + new "搜索" text + browser fontsize 4 buttons + click switches root font-size.

## §4 Reviewer brief

Filed at `.work/07_website/phase11/subagent_prompts/task_11_6_reviewer_prompt.md` at dispatch time (Step 11.6).

## §5 Commit + push cadence

Per-task commits (R-P10-2 sustained — 5 implementation tasks, independent + risk-isolated):

1. `07 Website Phase 11.1 — TopNav + Footer max-w-screen-xl content wrap (chrome aligns with landing+docs)`
2. `07 Website Phase 11.2 — ⌘K hint → "搜索/Search/検索" (Option A: shortcut hint deleted, explicit text)`
3. `07 Website Phase 11.3 — TopNav utilities visual divider (separate [search]/[lang]/[theme] groups)`
4. `07 Website Phase 11.4 — DocsLayout add Footer mount (consistent footer across landing + docs)`
5. `07 Website Phase 11.5 — v1.2 font-size 4-tier adjuster (FontSizeToggle + html data-fontsize CSS)`

Then:
6. `07 Website Phase 11.6 — reviewer fix bundle (if any)` (skip if PASS clean)
7. `07 Website Phase 11 close — handoff + master plan annotation + index sync`

Push timing: after step 7. CF Pages auto-rebuilds.

## §6 Self-review notes (filled at write time, 2026-04-30)

- **Tier check**: 5 implementation tasks + reviewer + close = 7 steps; Tier 2 mid-large.
- **Rule A applied**: 18 new i18n strings (1 search.label + 5 fontsize.* × 3 langs). Spot-check N=18 (writer pass full coverage) + reviewer extension TBD.
- **Rule B (failures preserved)**: any failed attempt → archive `evidence/failures/` per Tier 2 template.
- **Rule C (retro mandatory)**: RETROSPECTIVE.md at close — 三段 + Rule A/B/C/D/E compliance.
- **Rule D (reviewer isolation)**: Reviewer = `oh-my-claudecode:code-reviewer` (NEW agent within omc family vs Phase 6 critic / Phase 10 verifier; cross-family rotation 6-phase sustained).

## §7 Carryover to Phase 12 (anticipated, IDs C-P11-*)

(Will fill at close based on reviewer findings + post-push verify.)

Pre-existing C-P9-1..16 + C-P10-1..5 + pre-existing C-P5-M2/C-P6-5/C-P7-1+7+8/C-P8-6 still pending.
