# Subagent prompt — Phase 5 Task 5.1 (DocsLayout + 3 components)

**Subagent**: `oh-my-claudecode:executor` (opus)
**Dispatched**: 2026-04-28 (Phase 5 entry)
**Plan reference**: `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` §"Phase 5 → Task 5.1" lines 2012-2155
**Existing patterns probed by main session**:
- `web/src/layouts/BaseLayout.astro` — wraps `<html>/<head>/<body><slot/></body>`, props `{title, description?, lang?}`
- `web/src/layouts/LandingLayout.astro` — pattern: BaseLayout + TopNav + main + Footer + EnterFadeScript
- `web/src/components/astro/TopNav.astro` — props `{lang: Lang, pathname: string}`, uses `getUIStrings`
- `web/src/i18n/helpers.ts` — exports `Lang = 'zh'|'en'|'ja'`, `UIKey`, `getUIStrings`
- Content collection `guide` defined in `web/src/content.config.ts`, glob loads from `../ai_platforms/release/v1.0/**/*.md`, schema: `{lang?, slug?, order?, title?}`
- Tailwind classes used in repo: `border-rule`, `text-ink`, `text-ink-mute`, `text-accent`, `bg-bg-alt`, `font-mono`, `font-serif`

**Files to create** (all exact path):
1. `web/src/components/astro/DocsSidebar.astro` (per plan lines 2022-2055)
2. `web/src/components/astro/DocsTOC.astro` (per plan lines 2059-2093)
3. `web/src/components/astro/PrevNextNav.astro` (per plan lines 2097-2121)
4. `web/src/layouts/DocsLayout.astro` (per plan lines 2125-2148)

**Implementation rule**: copy the plan code verbatim. The plan author wrote against exact patterns above. Do NOT improvise different class names, prop shapes, or import paths.

**Verification before reporting done** (Rule D + project memory `feedback_verification_pass_criteria` — never PASS without evidence):
1. `cd /Users/bojiangzhang/MyProject/SDTM-compare/web && npx tsc --noEmit` → 0 errors
2. `cd /Users/bojiangzhang/MyProject/SDTM-compare/web && npm test -- --run 2>&1 | tail -10` → existing 29/29 still green (4 components added but no new test files yet — that's fine, layout components covered by e2e in Task 5.3)
3. `cd /Users/bojiangzhang/MyProject/SDTM-compare/web && npm run build 2>&1 | tail -10` → build green. Note: build may complain that `DocsLayout` is unused (no page consumes it yet until Task 5.3). That's expected — Astro tree-shakes unused layouts; verify build still emits all 3 lang landing pages.

**Commit when verified**:
```bash
git add web/src/layouts/DocsLayout.astro web/src/components/astro/DocsSidebar.astro web/src/components/astro/DocsTOC.astro web/src/components/astro/PrevNextNav.astro
git -c commit.gpgsign=false commit -m "07 Website Phase 5.1 — DocsLayout 3-col + Sidebar (mobile drawer) + TOC scroll-spy + PrevNext"
```

**Report back format** (concise):
- Files created (paths + line counts)
- tsc result
- vitest result
- build result
- commit SHA
- Anything you noticed that diverged from the plan or surprised you

**Do NOT**:
- Run `npm run test:e2e` (e2e setup not in scope of 5.1; covered in 5.3)
- Edit any other file outside the 4 listed paths
- Push to remote (main session handles push at Phase 5 close)
- Create test files for these components (covered by e2e in 5.3)
