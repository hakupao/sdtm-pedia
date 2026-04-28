# Phase 10 — UX Polish Bundle (v1.1)

> **Tier**: 2 (5-15 steps, ~half-day)
> **Status**: PLAN ack'd 2026-04-30 (Daisy decision: "ok 落实 plan.md 然后不开干, 等 17 点 usage 恢复了再开干")
> **Branch**: `main`. HEAD = `0b39fc1` (Phase 9 close).
> **Reviewer slot**: `oh-my-claudecode:verifier` (per Phase 9→10 handoff §4 recommendation; 2nd-burn omc family — Phase 6 used `critic`, this uses `verifier`; cross-family vs Phase 8 pr / Phase 7 superpowers / Phase 9 feature-dev; evidence-based "is the polish actually polished" lens fit for live-prod verification)
> **Plan deviation flag**: NONE — master plan §"Phase 10 — QA + Polish" already done in Phase 9-of-execution. This is post-release **v1.1 user-feedback polish**, driven by direct Daisy feedback 2026-04-30 (5 items raised, 4 in-scope; #5 font size adjuster deferred to v1.2 per Daisy ack)
> **Scope discipline**: Only the 4 user-driven UX items below. C-P9-1..16 from Phase 9→10 handoff carryover NOT absorbed (Daisy: "这一轮只改这些, 其他问题慢慢来"). Reviewer freebies if any are co-located may be picked up at fix-bundle time.

## §0 Pre-flight state (2026-04-30 PM)

| Field | Value |
|---|---|
| Branch | `main` |
| HEAD | `0b39fc1` (Phase 9 close — handoff + master plan annotation + index sync) |
| `origin/main` | same |
| Test baseline | tsc 0 / vitest 47/47 in 11 files / e2e 7/7 against `npm run preview` lane / build 31 HTML pages green / Pagefind 17 artifacts in dist/pagefind/ |
| Production | `https://sdtm-pedia.pages.dev/` LIVE (CF Pages auto-deploy from main push) |
| GH Release | `v1.0` LIVE since 2026-04-28T00:42:36Z (4 assets) |
| Lighthouse | a11y 91 / Best Practices 73 / SEO 100 (Daisy ack baseline) |

## §1 User-driven scope (Daisy 2026-04-30)

5 raw items raised verbatim:

1. White-screen + "Redirecting from / to /zh/" small-text flash on page transitions — **体感很不好**
2. Landing page has no left/right padding vs docs — **不好看**, want consistent width
3. Theme toggle (cycle button) is unclear vs language switcher — want **same explicit pattern** as LangSwitcher
4. "Daisy" 在公开页面让人困惑 — replace with real name **Bojiang Zhang**
5. Font size too small in landing + non-md UI — wants **4-tier size adjuster** (small/medium/large/x-large)

**Resolution**:
- 1, 2, 3, 4 → in-scope for v1.1 (this PLAN)
- 5 → deferred to v1.2 (Daisy ack: "方案 A" — independent feature work with proper layout adaptation + QA)

## §2 Tasks

### Task 10.1 — Server-side 301 redirects (CF `_redirects`)

**Why**: User reports white-screen flash on `/` → `/zh/` and `/{lang}/guide/` → `/{lang}/guide/user-guide/`. Root cause: meta-refresh client-side redirect renders HTML body containing visible `<a>Redirecting from <code>/</code> to <code>/zh/</code></a>` text before bouncing. CF Pages `_redirects` file does server-side 301 — no HTML rendered, no flash, also better SEO.

**Decision (Daisy ack 2026-04-30)**: Option a+c — both root + secondary redirects converted.

**Files**:
- Create: `web/public/_redirects` (NEW)
- Edit: `web/src/pages/index.astro` — add HTML comment header noting CF `_redirects` supersedes in production; this HTML is local-dev fallback only
- Edit: `web/src/pages/[lang]/guide/index.astro` — same comment header (3 redirect HTMLs: zh/en/ja guide indexes, all share same pattern)

**`_redirects` content** (4 rules, both with and without trailing slash for safety):

```
# Server-side 301 redirects (CF Pages). Supersedes meta-refresh HTML
# in web/src/pages/{index,[lang]/guide/index}.astro for production.
# Local astro dev/preview falls back to the meta-refresh HTML.

/                /zh/                       301
/zh/guide        /zh/guide/user-guide/      301
/zh/guide/       /zh/guide/user-guide/      301
/en/guide        /en/guide/user-guide/      301
/en/guide/       /en/guide/user-guide/      301
/ja/guide        /ja/guide/user-guide/      301
/ja/guide/       /ja/guide/user-guide/      301
```

**Steps**:
1. Create `web/public/_redirects` with above content.
2. Add comment header to 4 redirect `.astro` files: `<!-- CF _redirects (web/public/_redirects) handles this in production with HTTP 301; this meta-refresh HTML is the local astro dev/preview fallback. -->`
3. Run vitest + e2e + build locally; expect 47/47 + 7/7 + 31 pages (no count change — redirect HTMLs preserved).
4. Defer post-deploy verify to §3 final step (after push).

**Verify locally**:
- `cd web && npm run build` → 31 HTML pages
- `npm run test` → 47/47
- `npm run test:e2e` → 7/7 (lang.spec.ts asserts final URL `/zh/`, not meta refresh — should pass)

**Verify post-push (production)**:
- `curl -sI https://sdtm-pedia.pages.dev/` → first line `HTTP/2 301` (was `HTTP/2 200`)
- `curl -sI https://sdtm-pedia.pages.dev/zh/guide` → `HTTP/2 301` to `/zh/guide/user-guide/`
- Browser open `/` → instant jump to `/zh/`, no white-screen flash visible

**Risk + rollback**:
- CF `_redirects` syntax mismatch → fallback to existing meta refresh HTML still serves; revert by deleting `web/public/_redirects`.
- Trailing-slash variants might over-match (e.g. `/en/` matching wrong). Both `/lang/guide` and `/lang/guide/` written explicitly; root `/` only matches `/` exactly per CF spec.

---

### Task 10.2 — Landing content container (max-w-screen-xl)

**Why**: User reports landing has no left/right padding, looks unprofessional. Docs uses `max-w-screen-xl` (1280px) total width with sidebar + content + TOC inside. Make landing content match docs width.

**Decision (Daisy ack 2026-04-30)**: Backgrounds preserved full-width (hero visual weight kept); content within ALL 5 sections constrained to `max-w-screen-xl mx-auto`.

**Files**:
- Edit: `web/src/components/astro/HeroSection.astro`
- Edit: `web/src/components/astro/PlatformsSection.astro`
- Edit: `web/src/components/astro/ComparePreviewSection.astro`
- Edit: `web/src/components/astro/DemoSection.astro`
- Edit: `web/src/components/astro/DownloadsSection.astro`

**Pattern** (each section):

```astro
<!-- BEFORE -->
<section class="bg-X py-Y">
  <h2>...</h2>
  <div>...content...</div>
</section>

<!-- AFTER -->
<section class="bg-X py-Y">
  <div class="max-w-screen-xl mx-auto px-6">
    <h2>...</h2>
    <div>...content...</div>
  </div>
</section>
```

**Steps**:
1. Read current structure of each of the 5 section files (parallel reads).
2. For each: wrap top-level content in `<div class="max-w-screen-xl mx-auto px-6">` (skip if already present).
3. Local visual smoke at `localhost:4321/zh/` — check all 5 sections + scroll + mobile viewport (Chrome devtools responsive mode).
4. Run vitest (no DOM-structure assumptions in unit tests — should pass) + e2e smoke.spec.ts.

**Risk**:
- ComparePreviewSection contains a 4-row × 4-col table (landing slice of compare-dimensions). At 1280px it should fit; at narrower viewport there's already overflow handling (verify).
- HeroSection might already have inner container — check before adding duplicate.

**Verify**:
- Visual check both light + dark theme
- Mobile breakpoint (375px): content still readable, no horizontal scroll
- e2e 7/7

---

### Task 10.3 — ThemeToggle 平铺 3 按钮 (LangSwitcher 模式)

**Why**: User feedback "深浅主题的切换 不如 旁边语言切换方式来的清晰具体". Current `ThemeToggle.tsx` is a single cycle button (`☀` / `☾` / `◐`) — current state and next-click-effect both ambiguous from icon. LangSwitcher is 3 inline links with current highlighted via `aria-current` + bold styling. User decision (Daisy ack 2026-04-30): mirror LangSwitcher pattern exactly — 3 inline buttons, current highlighted, 1-click to switch.

**Decision (Daisy ack 2026-04-30, clarified)**: Tile 3 buttons (NOT dropdown). Match LangSwitcher visual + interaction pattern.

**Files**:
- Edit: `web/src/components/react/ThemeToggle.tsx` (rewrite)
- Edit: `web/src/components/react/ThemeToggle.test.tsx` (rewrite for 3-button assertions)
- Edit: `web/src/i18n/ui.zh.json` (+3 keys: `theme.light` / `theme.dark` / `theme.system`)
- Edit: `web/src/i18n/ui.en.json` (+3 keys, English)
- Edit: `web/src/i18n/ui.ja.json` (+3 keys, Japanese)

**i18n keys** (for `aria-label` + `title` tooltips; UI shows icons only):

```json
// zh
"theme.light":  "浅色",
"theme.dark":   "深色",
"theme.system": "跟随系统"

// en
"theme.light":  "Light",
"theme.dark":   "Dark",
"theme.system": "System"

// ja
"theme.light":  "ライト",
"theme.dark":   "ダーク",
"theme.system": "システム"
```

**Component pattern** (mirrors `LangSwitcher.tsx` 3-link nav):

```tsx
import { useEffect, useState } from 'react';
import { getStoredTheme, setStoredTheme, applyTheme, type ThemeChoice } from '../../lib/theme';

const ICON: Record<ThemeChoice, string> = { light: '☀', dark: '☾', system: '◐' };

interface Props {
  labels: Record<ThemeChoice, string>;  // i18n strings passed from Astro caller
}

export function ThemeToggle({ labels }: Props) {
  const [theme, setTheme] = useState<ThemeChoice>('system');

  useEffect(() => {
    const t = getStoredTheme();
    setTheme(t);
    applyTheme(t);
  }, []);

  const choices: ThemeChoice[] = ['light', 'dark', 'system'];
  const switchTo = (t: ThemeChoice) => {
    setStoredTheme(t);
    applyTheme(t);
    setTheme(t);
  };

  return (
    <nav aria-label="Theme" className="flex gap-2 font-mono text-[10px] tracking-wider">
      {choices.map((t) => (
        <button
          key={t}
          onClick={() => switchTo(t)}
          aria-pressed={t === theme}
          aria-label={labels[t]}
          title={labels[t]}
          className={t === theme ? 'text-ink font-bold' : 'text-ink-mute hover:text-accent'}
        >
          {ICON[t]}
        </button>
      ))}
    </nav>
  );
}
```

**Astro caller change** (e.g. `TopNav.astro` where `<ThemeToggle client:load />` is mounted): pass `labels={{light: t('theme.light'), dark: t('theme.dark'), system: t('theme.system')}}`.

**Steps**:
1. Add 9 i18n keys (3 × 3 langs).
2. Rewrite `ThemeToggle.tsx` per pattern above.
3. Rewrite `ThemeToggle.test.tsx`:
   - Renders 3 buttons with correct aria-labels
   - Each click sets correct localStorage + applies theme
   - `aria-pressed=true` on current theme button
4. Find caller (`TopNav.astro` or similar) and update mount with `labels` prop.
5. Run vitest (expect 47/47 → likely 47/47 unchanged or +1 if extra test added) + tsc + build.
6. Visual smoke at localhost: 3 buttons render in TopNav, current highlighted, clicks work, hover tooltips show i18n labels.

**Risk**:
- Nav width: 3 inline buttons take more horizontal space than 1 cycle button. TopNav layout might need tweak. Visual check during step 6.
- `aria-pressed` vs `aria-current` semantics: LangSwitcher uses `aria-current="page"` because they're page links; ThemeToggle uses `aria-pressed` because they're state toggles. Both correct per WAI-ARIA.

**Verify**:
- vitest 3-button + click behaviors
- localhost visual: 3 buttons + click switches theme + applied immediately + persists via localStorage reload

---

### Task 10.4 — "Daisy" → "Bojiang Zhang" (web + release, 34 occurrences)

**Why**: User feedback — public-facing materials reference "Daisy" (internal codename) which confuses readers. Replace with real name in user-facing surfaces.

**Decision (Daisy ack 2026-04-30)**: Replace in `web/` (5 occurrences) + `ai_platforms/release/v1.0/` (29 occurrences) = 34 total. Internal `.work/` (137 occurrences) **retained** as historical trace.

**Files** (verified by pre-flight grep 2026-04-30):

| Path | Count |
|---|---|
| `web/.cloudflare-pages.md` | 1 |
| `web/qa/cross-browser-2026-04-30.md` | 4 |
| `web/src/i18n/ui.en.json` (`footer.maintainer`) | 1 |
| `web/src/i18n/ui.ja.json` (`footer.maintainer`) | 1 |
| `web/src/i18n/ui.zh.json` (`footer.maintainer`) | 1 |
| `ai_platforms/release/v1.0/README.zh.md` | 1 |
| `ai_platforms/release/v1.0/README.en.md` | 1 |
| `ai_platforms/release/v1.0/README.ja.md` | 1 |
| `ai_platforms/release/v1.0/GLOSSARY.en.md` | 2 |
| `ai_platforms/release/v1.0/GLOSSARY.zh.md` | 2 |
| `ai_platforms/release/v1.0/PLATFORM_COMPARISON.zh.md` | 2 |
| `ai_platforms/release/v1.0/PLATFORM_COMPARISON.en.md` | 2 |
| `ai_platforms/release/v1.0/PLATFORM_COMPARISON.ja.md` | 2 |
| `ai_platforms/release/v1.0/USER_GUIDE.zh.md` | 6 |
| `ai_platforms/release/v1.0/USER_GUIDE.en.md` | 6 |
| `ai_platforms/release/v1.0/USER_GUIDE.ja.md` | 6 |
| `ai_platforms/release/v1.0/CHANGELOG.md` | 1 |
| `ai_platforms/release/v1.0/DEMO_QUESTIONS.md` | 2 |
| `ai_platforms/release/v1.0/self_deploy/README.zh.md` | 2 |
| `ai_platforms/release/v1.0/self_deploy/README.en.md` | 2 |
| `ai_platforms/release/v1.0/self_deploy/README.ja.md` | 2 |
| **Total** | **47 / 53 (re-verify pre-execute)** |

(Total mismatch with the 34 announced earlier — pre-flight grep counted line-occurrences, some lines have 2 "Daisy" strings. Re-verify counts at execute time with `grep -c` per file.)

**Steps**:
1. Pre-execute re-verify with `grep -rc "Daisy" web/ ai_platforms/release/v1.0/` to lock baseline count.
2. Run sed batch:
   ```bash
   find web/ ai_platforms/release/v1.0/ -type f \( -name "*.md" -o -name "*.json" \) \
     -exec sed -i '' 's/Daisy/Bojiang Zhang/g' {} \;
   ```
3. Manual diff review for all changed files (`git diff` before staging) — check:
   - "@Daisy" → "@Bojiang Zhang" reads OK in chat-mention context
   - "Maintained by Daisy" / "维护者: Daisy" / "メンテナー: Daisy" reads OK
   - No accidental match in code/data context (shouldn't be any per pre-flight)
4. Post-replace verify: `grep -r "Daisy" web/ ai_platforms/release/v1.0/` returns 0 lines.
5. Run vitest + tsc + build (i18n JSON parse must still succeed; build must produce 31 pages).

**Risk**:
- JSON files (`ui.{en,zh,ja}.json`) — sed replacement could break syntax if "Daisy" appears in a key name (it doesn't — only in `footer.maintainer` value).
- Footer copy may need length tweak: "Maintained by Daisy. Internal release." → "Maintained by Bojiang Zhang. Internal release." (11 chars longer in EN; check footer wrapping at narrow viewports).

**Verify**:
- `grep -rc "Daisy" web/ ai_platforms/release/v1.0/` returns 0 across all files
- `grep -rc "Daisy" .work/` unchanged (still 137 — preserved)
- vitest + tsc + build green
- Visual check footer at `/zh/`, `/en/`, `/ja/` — text wraps OK

**Caveat**:
- GH Release v1.0 already shipped with old "Daisy" content. Asset re-upload would invalidate the v1.0 immutable tag. The "Bojiang Zhang" change ships immediately on next push (LIVE website + repo) but the **GH Release v1.0 asset bundle** stays as-is. Next minor release pack (v1.1 or v1.2) will include updated `release/v1.0/` (or `release/v1.1/`) content.

## §3 Test + verify protocol

After each task (per-task commit):
- `cd web && npm run build` → must produce 31 HTML pages
- `npm run test` → vitest expectation tracker:
  - Baseline: 47/47
  - After 10.3: likely 47/47 (test rewrite preserves count) or 47/47 + N (TBD during execution; record actual)
- `npm run test:e2e` → 7/7 against preview lane
- `tsc --noEmit` (or `npm run typecheck`) → 0 errors

After all tasks (final pre-push):
- All above green
- Visual smoke localhost:4321 — landing + docs + compare + theme toggle + lang switcher all functional in zh/en/ja + light/dark theme

After push (CF Pages auto-deploy ~3-5 min):
- `curl -sI https://sdtm-pedia.pages.dev/` → `HTTP/2 301`
- `curl -sI https://sdtm-pedia.pages.dev/zh/guide` → `HTTP/2 301`
- `curl -s https://sdtm-pedia.pages.dev/zh/ | grep -oE "Bojiang Zhang|Daisy"` → only "Bojiang Zhang"
- Browser smoke: `/` jumps clean (no flash) + ThemeToggle 3 buttons visible + theme switch works
- Pagefind index re-built: `curl -s https://sdtm-pedia.pages.dev/pagefind/pagefind-entry.json` still reports 27 pages

## §4 Reviewer brief — `oh-my-claudecode:verifier`

**Brief stress dimensions D1-D7** (sustained from Phase 7/8/9 pattern):

- **D1** `_redirects` syntax + production curl verification (HTTP 301 not 200; `Location` header correct; trailing-slash variants both work)
- **D2** i18n parity: 9 new theme keys × 3 langs all present, no missing key warnings, footer.maintainer string updated 3/3 langs
- **D3** ThemeToggle keyboard a11y: tab to first button, arrow/space/enter activates, focus ring visible (focus-visible CSS from Phase 9 covers it)
- **D4** Landing container responsive: mobile (375px) / tablet (768px) / desktop (1280px) all readable; no horizontal scroll; ComparePreview table doesn't overflow
- **D5** "Daisy" sweep completeness: `grep -rc "Daisy" web/ ai_platforms/release/v1.0/` = 0; `.work/` preserved
- **D6** No regressions: vitest 47+/47+ / e2e 7/7 / build 31 pages / Pagefind 27 indexed
- **D7** Production live verification (post-push): 301 status + footer "Bojiang Zhang" rendered + theme buttons clickable + no console errors

**Rule A spot-check**: 9 new i18n strings (theme.light/dark/system × 3 langs) verified semantically — zh "浅色"/"深色"/"跟随系统" reads natural; en "Light"/"Dark"/"System" standard; ja "ライト"/"ダーク"/"システム" カタカナ standard. Reviewer should confirm.

**Subagent prompt file**: `.work/07_website/phase10/subagent_prompts/task_10_5_reviewer_prompt.md` (to be written at reviewer-dispatch time, ~Step 5).

## §5 Commit + push cadence

**Per-task commits** (4 tasks → 4 commits, Phase 6/7 pattern for revertability):

1. `07 Website Phase 10.1 — CF _redirects 301 (kill meta-refresh white-screen)`
2. `07 Website Phase 10.2 — Landing content container (max-w-screen-xl, bg full-width preserved)`
3. `07 Website Phase 10.3 — ThemeToggle 平铺 3 按钮 (mirror LangSwitcher pattern)`
4. `07 Website Phase 10.4 — Daisy → Bojiang Zhang (web 5 + release 29)`

Then:
5. `07 Website Phase 10.5 — reviewer fix bundle (if any)`
6. `07 Website Phase 10 close — handoff + master plan annotation + index sync`

Push timing: after step 6 close, single `git push origin main`. CF Pages auto-rebuilds.

## §6 Carryover deferred to Phase 11

- **Font size adjuster (4-tier)** — Daisy explicit decision: v1.2 independent feature; needs UI control + localStorage + CSS variables + 4-tier × 7-flow layout QA
- All **C-P9-1..16** from Phase 9→10 handoff (cheap fixes + LOW carryover):
  - C-P9-1 Safari/Firefox manual sweep
  - C-P9-2 Lighthouse 95/95/95 remediation (optional)
  - C-P9-3..9 axe / Lighthouse Performance / color-contrast / etc.
  - C-P9-10 SearchOverlay Escape stale closure (F-2)
  - C-P9-12..15 cheap LOW fixes (F-6/F-7/F-8/F-9)
  - C-P9-16 process improvement (canonical-derivation grep)
- All **C-P5-M2 / C-P6-5 / C-P7-7 / C-P7-8 / C-P8-6** pre-existing carryover

## §7 Risks + rollback summary

| Task | Risk | Rollback |
|---|---|---|
| 10.1 | CF `_redirects` syntax mismatch (no 301, fallback to meta refresh) | `rm web/public/_redirects` + `git revert <commit>` |
| 10.2 | Container too narrow on mobile (already-narrow content cut off) | `git revert <commit>` (per-section diff small) |
| 10.3 | TopNav layout breaks (3 inline buttons too wide) | `git revert <commit>` ThemeToggle.tsx; old cycle button restored |
| 10.4 | sed false positive (Daisy in unexpected context) | `git revert <commit>`; pre-flight grep confirmed 0 such cases |

All 4 tasks are independently revertable.

## §8 Estimated time

| Phase | Time |
|---|---|
| 10.1 `_redirects` | 30 min (write file + 4 file comments + local test) |
| 10.2 5 sections × container | 1 hour (5 reads + 5 edits + visual check) |
| 10.3 ThemeToggle rewrite + i18n + tests | 1 hour (component + 9 i18n keys + test rewrite + visual) |
| 10.4 Daisy sed + diff review | 30 min (sed + manual review + verify) |
| Reviewer dispatch + verify + fix bundle | 1 hour |
| Close handoff + master plan annotation + index sync | 30 min |
| **Total** | **~4-5 hours (half-day)** |

## §9 Resume protocol

Daisy hard-stop 2026-04-30 PM: "落实 plan.md 然后不开干, 等 17 点 usage 恢复了再开干".

When resuming (post-17:00 cutoff or next session):
1. Read this PLAN.md
2. Read `_progress.json` for last-completed step
3. Continue from next step in §2 task list
4. No re-planning needed unless Daisy raises new scope

## §10 Self-review notes (filled at write time, 2026-04-30)

- **Tier check**: 4 tasks + reviewer + close = ~6 steps; well within Tier 2 5-15 step bracket.
- **Rule A applied**: Daisy → Bojiang Zhang sweep is mass replacement (rule A semantic spot-check warranted post-replace) but no compression/rewrite — straight name swap. Spot-check at reviewer step on i18n footer.maintainer + USER_GUIDE access instructions (3 langs × ~3 representative occurrences = 9 samples).
- **Rule B (failures preserved)**: any failed attempt during 10.1-10.4 → archive to `evidence/failures/` per Tier 2 template.
- **Rule C (retro mandatory)**: RETROSPECTIVE.md to be written at close — three sections + Rule A/B/C/D/E compliance + carryover IDs C-P10-* for Phase 11.
- **Rule D (reviewer isolation)**: Reviewer = `oh-my-claudecode:verifier` (different agent from any executor; cross-family from Phase 9 feature-dev:code-architect; sustained Rule D chain extension).
