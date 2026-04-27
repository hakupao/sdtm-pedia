# SDTM Release Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the public-facing SDTM Knowledge website per `docs/superpowers/specs/2026-04-27-sdtm-release-website-design.md`, ship to Cloudflare Pages, with per-platform zip downloads on GitHub Releases.

**Architecture:** Astro static site with Tailwind v4 CSS variables for theming, content collections pulling trilingual `.md` from `ai_platforms/release/v1.0/`, React islands only for interactive bits (theme toggle, language switcher, count-up, comparison filter, search overlay), Pagefind for static full-text search, GitHub Releases for zip hosting.

**Tech Stack:** Astro 5.x, Tailwind CSS v4, React 18 (islands), TypeScript, Pagefind, Vitest + @testing-library/react, Playwright (e2e), self-hosted fonts via `@fontsource/*`, Cloudflare Pages.

---

## Pre-flight Notes

- **Working directory:** `/Users/bojiangzhang/MyProject/SDTM-compare`
- **GitHub repo:** `hakupao/sdtm-pedia` (public)
- **Spec to read first:** `docs/superpowers/specs/2026-04-27-sdtm-release-website-design.md` — this plan executes that spec, do not deviate without flagging.
- **Existing content (do not touch):** `ai_platforms/release/v1.0/*.md`, `ai_platforms/release/v1.0/self_deploy/**` — these are sources of truth, the website reads from them.
- **Out of scope for this plan:** anything in `.work/`, `source/`, other `ai_platforms/<platform>/` subdirs.

### Testing strategy (pragmatic TDD)

For an Astro static site, strict TDD applies cleanly to **data utilities, interactive islands, and end-to-end smoke flows**. It does NOT cleanly apply to pure-visual `.astro` components. The plan reflects this:

- **TDD applies (write test first):** i18n helpers, download URL builder, theme persistence, lang switcher path replacement, count-up math, comparison filter logic.
- **Component tests (Vitest + RTL):** Theme toggle, Lang switcher, Count-up, Search overlay, Compare filter — all React islands.
- **E2E smoke (Playwright):** lang switching, theme toggle, search opens + finds known string, all 4 download links resolve, mobile drawer toggles.
- **No tests:** purely visual `.astro` components — covered by E2E smoke.

### Conventions

- All website code in `web/`. The existing project's other dirs are not modified except via the documented content-collection glob.
- Commit early, commit often. Each task ends in a commit. Tests-first within tasks where TDD applies.
- Branch: work directly on `main` since this is a fresh feature in a personal repo (no PR review gate). Switch to feature branch if user requests.

---

## File Structure (planned)

### Pre-existing (read-only for this plan)

```
ai_platforms/release/v1.0/
├── README.{zh,en,ja}.md
├── USER_GUIDE.{zh,en,ja}.md
├── GLOSSARY.{zh,en,ja}.md
├── DEMO_QUESTIONS.md
├── KNOWN_LIMITATIONS.en.md
├── CHANGELOG.md
└── self_deploy/{claude,chatgpt,gemini,notebooklm}/...
```

### Created by this plan

```
ai_platforms/release/v1.0/
└── PLATFORM_COMPARISON.{zh,en,ja}.md       # Phase 0 content (NEW)

web/                                          # Astro project root (NEW)
├── astro.config.mjs
├── tailwind.config.mjs
├── postcss.config.mjs
├── tsconfig.json
├── package.json
├── playwright.config.ts
├── vitest.config.ts
├── README.md
├── RELEASE.md
├── .cloudflare-pages.md
├── public/
│   ├── favicon.svg
│   ├── og-default.png
│   └── robots.txt
├── scripts/
│   ├── build-bundles.sh
│   └── add-frontmatter.mjs
├── tests/e2e/
│   ├── smoke.spec.ts
│   ├── lang.spec.ts
│   ├── theme.spec.ts
│   └── search.spec.ts
└── src/
    ├── content/
    │   └── config.ts
    ├── data/
    │   ├── platforms.json
    │   ├── demos.json
    │   ├── downloads.json
    │   └── compare-dimensions.json
    ├── i18n/
    │   ├── ui.zh.json
    │   ├── ui.en.json
    │   ├── ui.ja.json
    │   ├── helpers.ts
    │   └── helpers.test.ts
    ├── styles/
    │   ├── global.css
    │   └── prose.css
    ├── components/
    │   ├── astro/
    │   │   ├── TopNav.astro
    │   │   ├── Footer.astro
    │   │   ├── SectionLabel.astro
    │   │   ├── HeroSection.astro
    │   │   ├── PlatformsSection.astro
    │   │   ├── ComparePreviewSection.astro
    │   │   ├── DemoSection.astro
    │   │   ├── DownloadsSection.astro
    │   │   ├── DocsSidebar.astro
    │   │   ├── DocsTOC.astro
    │   │   ├── PrevNextNav.astro
    │   │   └── EnterFadeScript.astro
    │   └── react/
    │       ├── ThemeToggle.tsx
    │       ├── ThemeToggle.test.tsx
    │       ├── LangSwitcher.tsx
    │       ├── LangSwitcher.test.tsx
    │       ├── CountUp.tsx
    │       ├── CountUp.test.tsx
    │       ├── SearchOverlay.tsx
    │       ├── SearchOverlay.test.tsx
    │       ├── CompareFilter.tsx
    │       └── CompareFilter.test.tsx
    ├── lib/
    │   ├── downloads.ts
    │   ├── downloads.test.ts
    │   ├── theme.ts
    │   ├── theme.test.ts
    │   ├── countup.ts
    │   └── countup.test.ts
    ├── layouts/
    │   ├── BaseLayout.astro
    │   ├── LandingLayout.astro
    │   └── DocsLayout.astro
    ├── pages/
    │   ├── index.astro
    │   ├── compare.astro
    │   └── [lang]/
    │       ├── index.astro
    │       ├── changelog.astro
    │       └── guide/
    │           ├── index.astro
    │           └── [...slug].astro
    └── test-setup.ts
```

---

## Phase 0 — Content & Asset Prep

### Task 0.1: Author `PLATFORM_COMPARISON.zh.md`

**Files:**
- Create: `ai_platforms/release/v1.0/PLATFORM_COMPARISON.zh.md`

- [ ] **Step 1: Confirm dimensions with user before writing**

Memo from brainstorm: §03 expands to multi-dim comparison. Confirm exact dimensions before authoring (proposed: 17题得分 / 容量上限 / 团队共享方式 / 套餐要求 / 联网能力 / 反虚构倾向 / 文件数限制 / 最强场景 / 最弱场景). If user has not confirmed, pause and ask: "Confirming PLATFORM_COMPARISON dimensions: [list] — keep all, drop any, add others?"

- [ ] **Step 2: Write the file**

Author with frontmatter and content. Pull facts from existing `USER_GUIDE.zh.md` and `KNOWN_LIMITATIONS.en.md`. Structure:

```markdown
---
lang: zh
slug: compare
order: 20
title: 4 平台多维对比
---

# 4 平台多维对比

> 横向对比 4 平台 9 个维度. 数据快照: 2026-04-27 v1.0.

## 评测得分 (smoke v4 / 17 题)

| 平台 | 得分 | 主要失分点 |
|---|---|---|
| Claude Projects | 17/17 | — |
| ChatGPT GPTs | 16.5/17 | Q4 long-tail chunk |
| Gemini Gems | 16/17 | Q1 GFGENE 个例 |
| NotebookLM | 15/17 | Q11/Q12 PUNT |

## 容量与文件限制

(...one section per dimension; for each section, table of 4 platforms × the cell content for that dimension. Example body for "容量与文件限制":)

| 平台 | 容量上限 | 当前用量 |
|---|---|---|
| Claude Projects | 1.29M tokens | 77% |
| ChatGPT GPTs | 20 文件硬限 | 9 文件 |
| Gemini Gems | 1M token 窗口 | 4 文件 |
| NotebookLM | 50 source per notebook | 42/50 |

## 团队共享方式

(table)

## 套餐要求

(table)

## 联网能力

(table)

## 反虚构倾向

(table)

## 最强场景

(table)

## 最弱场景

(table)
```

- [ ] **Step 3: Completeness checklist**

Verify every section has all 4 platforms covered. If any cell is N/A, write "不适用" not blank.

- [ ] **Step 4: Commit**

```bash
git add ai_platforms/release/v1.0/PLATFORM_COMPARISON.zh.md
git commit -m "07 Release v1.0 PLATFORM_COMPARISON.zh.md (multi-dim 平台对比 zh)"
```

### Task 0.2: Translate `PLATFORM_COMPARISON.zh.md` → `.en.md`

**Files:**
- Create: `ai_platforms/release/v1.0/PLATFORM_COMPARISON.en.md`

- [ ] **Step 1: Translate**

Mirror structure of `.zh.md` exactly. SDTM-specific terms (Domain / Variable / Core / CT C-code / SUPPQUAL) stay English. Soft tone matches existing `README.en.md`.

- [ ] **Step 2: Verify table cells parity**

Run: `wc -l ai_platforms/release/v1.0/PLATFORM_COMPARISON.{zh,en}.md` — line counts within ±5% of each other.

- [ ] **Step 3: Commit**

```bash
git add ai_platforms/release/v1.0/PLATFORM_COMPARISON.en.md
git commit -m "07 Release v1.0 PLATFORM_COMPARISON.en.md (multi-dim 平台对比 en)"
```

### Task 0.3: Translate `PLATFORM_COMPARISON.zh.md` → `.ja.md`

**Files:**
- Create: `ai_platforms/release/v1.0/PLATFORM_COMPARISON.ja.md`

- [ ] **Step 1: Translate** — mirror `.zh.md`, SDTM terms English, 敬体 (です/ます) consistent with `README.ja.md`.

- [ ] **Step 2: Verify parity** (same as 0.2 step 2)

- [ ] **Step 3: Commit**

```bash
git add ai_platforms/release/v1.0/PLATFORM_COMPARISON.ja.md
git commit -m "07 Release v1.0 PLATFORM_COMPARISON.ja.md (multi-dim 平台对比 ja)"
```

### Task 0.4: Favicon SVG

**Files:**
- Create: `assets/favicon.svg` (move to `web/public/` in Task 1.5)

- [ ] **Step 1: Hand-author SVG**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" fill="#1e40af"/>
  <text x="50%" y="50%" dominant-baseline="central" text-anchor="middle"
        font-family="Playfair Display, Georgia, serif" font-style="italic"
        font-weight="700" font-size="22" fill="#f8f5ef">S</text>
</svg>
```

Save to `assets/favicon.svg`. `mkdir -p assets` first.

- [ ] **Step 2: No commit yet** — defer with Task 1.5.

### Task 0.5: OG image (1200×630)

**Files:**
- Create: `assets/og-default.png`

- [ ] **Step 1: Generate via sharp**

```bash
npm install --save-dev sharp
node -e "
const sharp = require('sharp');
const svg = \`
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 630'>
  <rect width='1200' height='630' fill='#f8f5ef'/>
  <rect x='80' y='80' width='1040' height='4' fill='#0a0a0a'/>
  <text x='80' y='180' font-family='JetBrains Mono, monospace' font-size='20' font-weight='700' fill='#1e40af' letter-spacing='4'>SDTM/KB · VOL.01 · 2026</text>
  <text x='80' y='320' font-family='Playfair Display, Georgia, serif' font-size='80' font-weight='700' fill='#0a0a0a'>SDTM Knowledge,</text>
  <text x='80' y='420' font-family='Playfair Display, Georgia, serif' font-size='80' font-style='italic' font-weight='500' fill='#0a0a0a'>across four AI platforms.</text>
  <rect x='80' y='546' width='1040' height='4' fill='#0a0a0a'/>
  <text x='80' y='590' font-family='JetBrains Mono, monospace' font-size='16' fill='#555' letter-spacing='2'>CLAUDE 17/17 · GPT 16.5 · GEMINI 16 · NBLM 15</text>
</svg>
\`;
sharp(Buffer.from(svg)).png().toFile('assets/og-default.png');
"
```

- [ ] **Step 2: Visually verify**

Open `assets/og-default.png`. Should be 1200×630, off-white bg, two big serif lines, top + bottom rules, mono small text.

- [ ] **Step 3: No commit yet** — defer with Task 1.5.

---

## Phase 1 — Astro Scaffolding

### Task 1.1: Initialize Astro project in `web/`

**Files:**
- Create: `web/` directory tree (via `npm create astro`)

- [ ] **Step 1: Run scaffold**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
npm create astro@latest web -- --template minimal --no-install --no-git --typescript strict
```

Confirm `web/package.json` exists.

- [ ] **Step 2: Verify cleanliness**

```bash
ls web/
# expected: package.json, src/, public/, astro.config.mjs, tsconfig.json
```

- [ ] **Step 3: Commit**

```bash
git add web/
git commit -m "07 Website Phase 1.1 — Astro minimal scaffold (web/)"
```

### Task 1.2: Install dependencies

> **Astro v6 + Tailwind v4 integration note (2026-04-27 erratum).** The legacy `@astrojs/tailwind` integration only declares peer-dep support for Astro 3/4/5 and refuses to install against Astro 6. The supported 2026 path is the framework-agnostic `@tailwindcss/vite` plugin, registered via Astro's `vite.plugins` config. PostCSS-side deps (`@tailwindcss/postcss`, `postcss`, `autoprefixer`) are also dropped — `@tailwindcss/vite` compiles Tailwind directly through Vite/Lightning CSS.

**Files:**
- Modify: `web/package.json`

- [ ] **Step 1: Add deps**

```bash
cd web
npm install astro @astrojs/react @astrojs/sitemap react react-dom
npm install -D @types/react @types/react-dom typescript tailwindcss@next @tailwindcss/vite
npm install @fontsource/playfair-display @fontsource/source-serif-pro @fontsource/jetbrains-mono
npm install -D vitest @vitest/ui @testing-library/react @testing-library/jest-dom jsdom @playwright/test @vitejs/plugin-react
npm install -D pagefind
```

- [ ] **Step 2: Verify install**

`cd web && npm ls --depth 0` — all listed packages present.

- [ ] **Step 3: Commit**

```bash
git add web/package.json web/package-lock.json
git commit -m "07 Website Phase 1.2 — install Astro + React + Tailwind v4 + Pagefind + test deps"
```

### Task 1.3: Configure `astro.config.mjs`

**Files:**
- Modify: `web/astro.config.mjs`

- [ ] **Step 1: Replace contents**

```javascript
// web/astro.config.mjs
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://sdtm-pedia.pages.dev',  // replace with custom domain when set
  integrations: [
    react(),
    sitemap(),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en', 'ja'],
    routing: { prefixDefaultLocale: true },
  },
  build: {
    format: 'directory',
  },
});
```

- [ ] **Step 2: Smoke-test**

```bash
cd web && npm run dev
```

Should start on `http://localhost:4321` without errors (404 on `/` is expected — no pages yet). Kill with `Ctrl+C`.

- [ ] **Step 3: Commit**

```bash
git add web/astro.config.mjs
git commit -m "07 Website Phase 1.3 — astro.config: react + tailwind + sitemap + i18n (zh default, prefixDefaultLocale)"
```

### Task 1.4: Tailwind v4 CSS-first entry stub

> **Tailwind v4 is CSS-first.** No JS `tailwind.config.mjs` is needed — theme tokens, font families, and dark-mode selector are declared inside CSS via `@theme {…}` and `@custom-variant`. No `postcss.config.mjs` either, since `@tailwindcss/vite` (registered in Task 1.3) compiles Tailwind through Vite directly. Phase 2 §2.1 will fill in the full token set inside the same `global.css`. This task only creates the minimal entry so Tailwind utilities resolve in any Phase 1 smoke test.

**Files:**
- Create: `web/src/styles/global.css`

- [ ] **Step 1: Stub global.css**

```bash
cd web
mkdir -p src/styles
```

`web/src/styles/global.css`:
```css
/* Tailwind v4 entry. Phase 2 §2.1 expands this with @theme tokens, fonts, and dark-mode rules. */
@import "tailwindcss";
```

- [ ] **Step 2: Commit**

```bash
git add web/src/styles/global.css
git commit -m "07 Website Phase 1.4 — Tailwind v4 CSS entry stub (@import tailwindcss; full theme deferred to §2.1)"
```

### Task 1.5: Set up directory structure + assets

**Files:**
- Create: `web/src/{components,layouts,lib,i18n,data,styles,content}/...`
- Move: `assets/favicon.svg` → `web/public/favicon.svg`
- Move: `assets/og-default.png` → `web/public/og-default.png`

- [ ] **Step 1: Create empty dirs with `.gitkeep`**

```bash
cd web/src
mkdir -p components/astro components/react layouts lib i18n data styles content
touch components/astro/.gitkeep components/react/.gitkeep layouts/.gitkeep lib/.gitkeep i18n/.gitkeep data/.gitkeep styles/.gitkeep content/.gitkeep
```

- [ ] **Step 2: Move stashed assets**

```bash
mv ../../assets/favicon.svg public/favicon.svg
mv ../../assets/og-default.png public/og-default.png
rmdir ../../assets
```

- [ ] **Step 3: Add robots.txt**

`web/public/robots.txt`:
```
User-agent: *
Allow: /
Sitemap: https://sdtm-pedia.pages.dev/sitemap-index.xml
```

- [ ] **Step 4: Commit**

```bash
git add web/src web/public
git commit -m "07 Website Phase 1.5 — dir scaffold + favicon + og-default + robots"
```

### Task 1.6: Configure Vitest

**Files:**
- Create: `web/vitest.config.ts`
- Create: `web/src/test-setup.ts`

- [ ] **Step 1: Write config**

```typescript
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./src/test-setup.ts'],
  },
});
```

- [ ] **Step 2: Create setup file**

`web/src/test-setup.ts`:
```typescript
import '@testing-library/jest-dom/vitest';
```

- [ ] **Step 3: Add npm scripts**

Edit `web/package.json` `"scripts"`:
```json
{
  "scripts": {
    "dev": "astro dev",
    "build": "astro build && pagefind --site dist",
    "preview": "astro preview",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:e2e": "playwright test"
  }
}
```

- [ ] **Step 4: Smoke-test**

`cd web && npm test` — should run, find 0 tests, exit 0.

- [ ] **Step 5: Commit**

```bash
git add web/vitest.config.ts web/src/test-setup.ts web/package.json
git commit -m "07 Website Phase 1.6 — Vitest config + npm scripts (dev/build/test/test:e2e)"
```

### Task 1.7: Configure Playwright

**Files:**
- Create: `web/playwright.config.ts`
- Create: `web/tests/e2e/.gitkeep`

- [ ] **Step 1: Init Playwright browsers**

`cd web && npx playwright install --with-deps chromium`

- [ ] **Step 2: Write config**

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  use: {
    baseURL: 'http://localhost:4321',
    trace: 'on-first-retry',
  },
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:4321',
    reuseExistingServer: true,
    stdout: 'ignore',
    stderr: 'pipe',
  },
});
```

- [ ] **Step 3: Smoke**

`cd web && npx playwright test --list` — should print "Total: 0 tests" without error.

- [ ] **Step 4: Commit**

```bash
git add web/playwright.config.ts web/tests
git commit -m "07 Website Phase 1.7 — Playwright config (chromium, reuse dev server)"
```

---

## Phase 2 — Design System

### Task 2.1: CSS tokens (light/dark)

**Files:**
- Create: `web/src/styles/global.css`

- [ ] **Step 1: Write global.css**

```css
@import "@fontsource/playfair-display/400.css";
@import "@fontsource/playfair-display/700.css";
@import "@fontsource/playfair-display/700-italic.css";
@import "@fontsource/source-serif-pro/400.css";
@import "@fontsource/source-serif-pro/500.css";
@import "@fontsource/source-serif-pro/400-italic.css";
@import "@fontsource/jetbrains-mono/500.css";
@import "@fontsource/jetbrains-mono/700.css";

@import "tailwindcss";

:root, [data-theme="light"] {
  --bg:        #f8f5ef;
  --bg-alt:    #ffffff;
  --ink:       #0a0a0a;
  --ink-mute:  #555555;
  --ink-faint: rgba(10, 10, 10, 0.4);
  --accent:    #1e40af;
  --rule:      #1a1a1a;
}

[data-theme="dark"] {
  --bg:        #0d0c0a;
  --bg-alt:    #1a1815;
  --ink:       #f5f1ea;
  --ink-mute:  #b8b3a8;
  --ink-faint: rgba(245, 241, 234, 0.4);
  --accent:    #60a5fa;
  --rule:      #f5f1ea;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
    --bg:        #0d0c0a;
    --bg-alt:    #1a1815;
    --ink:       #f5f1ea;
    --ink-mute:  #b8b3a8;
    --ink-faint: rgba(245, 241, 234, 0.4);
    --accent:    #60a5fa;
    --rule:      #f5f1ea;
  }
}

html, body {
  background: var(--bg);
  color: var(--ink);
  font-family: 'Source Serif Pro', Georgia, serif;
  transition: background 250ms ease-in-out, color 250ms ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add web/src/styles/global.css
git commit -m "07 Website Phase 2.1 — global.css: tokens light+dark, font imports, reduced-motion guard"
```

### Task 2.2: Theme persistence library + tests

**Files:**
- Create: `web/src/lib/theme.ts`
- Create: `web/src/lib/theme.test.ts`

- [ ] **Step 1: Write the failing tests**

```typescript
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { getStoredTheme, setStoredTheme, applyTheme, resolveEffectiveTheme } from './theme';

describe('theme', () => {
  beforeEach(() => {
    localStorage.clear();
    document.documentElement.removeAttribute('data-theme');
  });

  it('getStoredTheme returns "system" by default', () => {
    expect(getStoredTheme()).toBe('system');
  });

  it('setStoredTheme persists choice to localStorage', () => {
    setStoredTheme('dark');
    expect(localStorage.getItem('theme')).toBe('dark');
    expect(getStoredTheme()).toBe('dark');
  });

  it('applyTheme sets data-theme attribute on root', () => {
    applyTheme('light');
    expect(document.documentElement.dataset.theme).toBe('light');
  });

  it('applyTheme with "system" removes the attribute', () => {
    document.documentElement.dataset.theme = 'dark';
    applyTheme('system');
    expect(document.documentElement.hasAttribute('data-theme')).toBe(false);
  });

  it('resolveEffectiveTheme returns "dark" when stored=system + media query dark', () => {
    setStoredTheme('system');
    vi.spyOn(window, 'matchMedia').mockReturnValue({ matches: true } as MediaQueryList);
    expect(resolveEffectiveTheme()).toBe('dark');
  });
});
```

- [ ] **Step 2: Verify tests fail**

`cd web && npm test theme` — expect 5 failures (module not found).

- [ ] **Step 3: Implement**

```typescript
// web/src/lib/theme.ts
export type ThemeChoice = 'light' | 'dark' | 'system';
export type EffectiveTheme = 'light' | 'dark';

const KEY = 'theme';

export function getStoredTheme(): ThemeChoice {
  if (typeof localStorage === 'undefined') return 'system';
  const v = localStorage.getItem(KEY);
  return v === 'light' || v === 'dark' || v === 'system' ? v : 'system';
}

export function setStoredTheme(t: ThemeChoice): void {
  localStorage.setItem(KEY, t);
}

export function applyTheme(t: ThemeChoice): void {
  if (t === 'system') {
    document.documentElement.removeAttribute('data-theme');
  } else {
    document.documentElement.dataset.theme = t;
  }
}

export function resolveEffectiveTheme(): EffectiveTheme {
  const stored = getStoredTheme();
  if (stored === 'light' || stored === 'dark') return stored;
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}
```

- [ ] **Step 4: Verify tests pass**

`cd web && npm test theme` — all 5 pass.

- [ ] **Step 5: Commit**

```bash
git add web/src/lib/theme.ts web/src/lib/theme.test.ts
git commit -m "07 Website Phase 2.2 — theme.ts: localStorage + system + applyTheme (5 tests)"
```

### Task 2.3: Theme toggle React island

**Files:**
- Create: `web/src/components/react/ThemeToggle.tsx`
- Create: `web/src/components/react/ThemeToggle.test.tsx`

- [ ] **Step 1: Write failing test**

```tsx
import { describe, it, expect, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ThemeToggle } from './ThemeToggle';

describe('<ThemeToggle>', () => {
  beforeEach(() => {
    localStorage.clear();
    document.documentElement.removeAttribute('data-theme');
  });

  it('renders an accessible button', () => {
    render(<ThemeToggle />);
    expect(screen.getByRole('button', { name: /theme/i })).toBeInTheDocument();
  });

  it('cycles system → dark → system on click', () => {
    render(<ThemeToggle />);
    const btn = screen.getByRole('button');
    fireEvent.click(btn);
    expect(localStorage.getItem('theme')).toBe('dark');
    fireEvent.click(btn);
    expect(localStorage.getItem('theme')).toBe('system');
    fireEvent.click(btn);
    expect(localStorage.getItem('theme')).toBe('light');
  });
});
```

- [ ] **Step 2: Verify fail**

- [ ] **Step 3: Implement**

```tsx
// web/src/components/react/ThemeToggle.tsx
import { useEffect, useState } from 'react';
import { getStoredTheme, setStoredTheme, applyTheme, type ThemeChoice } from '../../lib/theme';

const NEXT: Record<ThemeChoice, ThemeChoice> = { light: 'dark', dark: 'system', system: 'light' };
const LABEL: Record<ThemeChoice, string> = { light: '☀', dark: '☾', system: '◐' };

export function ThemeToggle() {
  const [theme, setTheme] = useState<ThemeChoice>('system');

  useEffect(() => {
    const t = getStoredTheme();
    setTheme(t);
    applyTheme(t);
  }, []);

  const handleClick = () => {
    const next = NEXT[theme];
    setStoredTheme(next);
    applyTheme(next);
    setTheme(next);
  };

  return (
    <button
      onClick={handleClick}
      aria-label={`Theme: ${theme}, click to switch`}
      className="font-mono text-sm px-2 py-1 hover:text-accent transition-colors"
    >
      {LABEL[theme]}
    </button>
  );
}
```

- [ ] **Step 4: Verify pass**

- [ ] **Step 5: Commit**

```bash
git add web/src/components/react/ThemeToggle.tsx web/src/components/react/ThemeToggle.test.tsx
git commit -m "07 Website Phase 2.3 — ThemeToggle island (cycle, 2 tests)"
```

### Task 2.4: SectionLabel ritual component

**Files:**
- Create: `web/src/components/astro/SectionLabel.astro`

- [ ] **Step 1: Write component**

```astro
---
interface Props {
  number: string;  // e.g., "01"
  label: string;   // e.g., "HERO"
}
const { number, label } = Astro.props;
---
<div class="flex items-baseline gap-3 mb-6">
  <div class="font-mono text-[9px] uppercase tracking-[0.2em] text-accent font-bold">
    § {number} / {label}
  </div>
  <div class="h-px bg-accent flex-1 opacity-30"></div>
</div>
```

- [ ] **Step 2: Commit**

```bash
git add web/src/components/astro/SectionLabel.astro
git commit -m "07 Website Phase 2.4 — SectionLabel.astro (§NN / LABEL ritual)"
```

### Task 2.5: BaseLayout

**Files:**
- Create: `web/src/layouts/BaseLayout.astro`

- [ ] **Step 1: Write layout**

```astro
---
import '../styles/global.css';
interface Props {
  title: string;
  description?: string;
  lang?: string;
}
const { title, description = 'SDTM Knowledge — across four AI platforms.', lang = 'zh' } = Astro.props;
---
<!DOCTYPE html>
<html lang={lang}>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta property="og:image" content="/og-default.png" />
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta name="description" content={description} />
    <title>{title}</title>
    <script is:inline>
      // Avoid theme flash: read localStorage before paint
      (function () {
        var t = localStorage.getItem('theme');
        if (t === 'light' || t === 'dark') {
          document.documentElement.dataset.theme = t;
        }
      })();
    </script>
  </head>
  <body>
    <slot />
  </body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add web/src/layouts/BaseLayout.astro
git commit -m "07 Website Phase 2.5 — BaseLayout.astro (theme flash guard, og meta, lang attr)"
```

---

## Phase 3 — Content Collections + i18n

### Task 3.1: Add frontmatter to release docs + content collection schema

**Files:**
- Create: `web/src/content/config.ts`
- Create: `web/scripts/add-frontmatter.mjs`
- Modify: `ai_platforms/release/v1.0/*.md` (frontmatter prepended where missing)

- [ ] **Step 1: Write add-frontmatter.mjs**

```javascript
// web/scripts/add-frontmatter.mjs
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const __dirname = path.dirname(url.fileURLToPath(import.meta.url));
const DIR = path.resolve(__dirname, '../../ai_platforms/release/v1.0');
const ORDER = { 'README': 0, 'USER_GUIDE': 10, 'PLATFORM_COMPARISON': 20, 'DEMO_QUESTIONS': 30, 'GLOSSARY': 40, 'KNOWN_LIMITATIONS': 50, 'CHANGELOG': 60 };
const TITLES = {
  'user-guide':         { zh: '用户手册',       en: 'User Guide',           ja: 'ユーザーガイド' },
  'demo-questions':     { zh: '演示题',         en: 'Demo Questions',       ja: 'デモクエスチョン' },
  'glossary':           { zh: '术语表',         en: 'Glossary',             ja: '用語集' },
  'known-limitations':  { zh: '已知限制',       en: 'Known Limitations',    ja: '既知の制限' },
  'changelog':          { zh: '变更日志',       en: 'Changelog',            ja: '変更履歴' },
  'readme':             { zh: 'README',         en: 'README',               ja: 'README' },
  'compare':            { zh: '4 平台对比',     en: 'Platform Comparison',  ja: 'プラットフォーム比較' },
};

for (const file of fs.readdirSync(DIR)) {
  if (!file.endsWith('.md')) continue;
  const m = file.match(/^([A-Z_]+)(?:\.(zh|en|ja))?\.md$/);
  if (!m) continue;
  const slug = m[1].toLowerCase().replace(/_/g, '-');
  const lang = m[2] || 'en';
  const order = ORDER[m[1]] ?? 99;
  const title = TITLES[slug]?.[lang] ?? m[1];
  const fp = path.join(DIR, file);
  const body = fs.readFileSync(fp, 'utf8');
  if (body.startsWith('---')) continue;  // already has frontmatter
  const fm = `---\nlang: ${lang}\nslug: ${slug}\norder: ${order}\ntitle: "${title}"\n---\n\n`;
  fs.writeFileSync(fp, fm + body);
  console.log(`+ ${file} (lang=${lang}, slug=${slug}, order=${order}, title="${title}")`);
}
```

Run: `cd web && node scripts/add-frontmatter.mjs`. Verify with `head -8 ../ai_platforms/release/v1.0/USER_GUIDE.zh.md`.

- [ ] **Step 2: Write content/config.ts**

```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import path from 'node:path';

const RELEASE_DIR = path.resolve('../ai_platforms/release/v1.0');

const guide = defineCollection({
  loader: glob({ pattern: '**/*.md', base: RELEASE_DIR }),
  schema: z.object({
    lang: z.enum(['zh', 'en', 'ja']).optional(),
    slug: z.string().optional(),
    order: z.number().optional(),
    title: z.string().optional(),
  }),
});

export const collections = { guide };
```

- [ ] **Step 3: Verify Astro can read**

`cd web && npm run dev`. Open `http://localhost:4321` (will 404, that's fine). Astro should NOT throw collection errors in dev console.

- [ ] **Step 4: Commit (separately)**

```bash
git add ai_platforms/release/v1.0/*.md
git commit -m "07 Release v1.0 frontmatter — lang+slug+order+title added to top-level docs (web 集成准备)"
git add web/src/content/config.ts web/scripts/add-frontmatter.mjs
git commit -m "07 Website Phase 3.1 — content collection schema + add-frontmatter.mjs one-shot"
```

### Task 3.2: i18n UI strings

**Files:**
- Create: `web/src/i18n/ui.zh.json`, `web/src/i18n/ui.en.json`, `web/src/i18n/ui.ja.json`

- [ ] **Step 1: Author 3 dictionaries**

`web/src/i18n/ui.zh.json`:
```json
{
  "nav.guide": "文档",
  "nav.platforms": "4 平台",
  "nav.demo": "演示",
  "nav.download": "下载",
  "hero.cta.read": "查看文档 →",
  "hero.cta.download": "下载 .ZIP",
  "hero.cta.github": "→ GITHUB",
  "section.platforms.subhead": "四种部署, 各有性格.",
  "section.compare.subhead": "按你想做的事来挑.",
  "section.compare.cta": "→ 完整对比",
  "section.demo.subhead": "试试这三道. 完整十题在文档里.",
  "section.demo.cta": "→ 完整 10 题",
  "section.downloads.subhead": "自部署你自己的.",
  "section.downloads.cta": "→ 全部 release 资产",
  "footer.maintainer": "维护: Daisy. 内部发布版.",
  "search.placeholder": "搜索文档...",
  "search.shortcut": "Cmd K"
}
```

`ui.en.json`:
```json
{
  "nav.guide": "Guide",
  "nav.platforms": "Platforms",
  "nav.demo": "Demo",
  "nav.download": "Download",
  "hero.cta.read": "READ THE GUIDE →",
  "hero.cta.download": "DOWNLOAD .ZIP",
  "hero.cta.github": "→ GITHUB",
  "section.platforms.subhead": "Four deployments, each with a temperament.",
  "section.compare.subhead": "Pick by what you're about to do.",
  "section.compare.cta": "→ FULL COMPARISON",
  "section.demo.subhead": "Try these three. The full ten are in the guide.",
  "section.demo.cta": "→ ALL TEN QUESTIONS",
  "section.downloads.subhead": "Self-deploy your own.",
  "section.downloads.cta": "→ ALL RELEASES",
  "footer.maintainer": "Maintained by Daisy. Internal release.",
  "search.placeholder": "Search docs...",
  "search.shortcut": "Cmd K"
}
```

`ui.ja.json` (敬体):
```json
{
  "nav.guide": "ドキュメント",
  "nav.platforms": "4 プラットフォーム",
  "nav.demo": "デモ",
  "nav.download": "ダウンロード",
  "hero.cta.read": "ガイドを読む →",
  "hero.cta.download": ".ZIP をダウンロード",
  "hero.cta.github": "→ GITHUB",
  "section.platforms.subhead": "4 つのデプロイ、それぞれの性格。",
  "section.compare.subhead": "やりたいことで選ぶ。",
  "section.compare.cta": "→ 完全比較",
  "section.demo.subhead": "この 3 問をお試しください。10 問全てはガイドに。",
  "section.demo.cta": "→ 全 10 問",
  "section.downloads.subhead": "セルフデプロイしましょう。",
  "section.downloads.cta": "→ 全リリース",
  "footer.maintainer": "メンテナー: Daisy. 社内公開版。",
  "search.placeholder": "ドキュメント検索...",
  "search.shortcut": "Cmd K"
}
```

- [ ] **Step 2: Commit**

```bash
git add web/src/i18n/ui.zh.json web/src/i18n/ui.en.json web/src/i18n/ui.ja.json
git commit -m "07 Website Phase 3.2 — i18n UI strings (zh/en/ja, 17 keys)"
```

### Task 3.3: i18n helpers + tests

**Files:**
- Create: `web/src/i18n/helpers.ts`
- Create: `web/src/i18n/helpers.test.ts`

- [ ] **Step 1: Write tests**

```typescript
// web/src/i18n/helpers.test.ts
import { describe, it, expect } from 'vitest';
import { getUIStrings, replaceLangInPath, supportedLangs, type Lang } from './helpers';

describe('i18n.getUIStrings', () => {
  it('returns zh dictionary', () => {
    expect(getUIStrings('zh')['nav.guide']).toBe('文档');
  });
  it('returns en dictionary', () => {
    expect(getUIStrings('en')['nav.guide']).toBeTruthy();
  });
  it('throws on invalid lang', () => {
    expect(() => getUIStrings('fr' as Lang)).toThrow();
  });
});

describe('i18n.replaceLangInPath', () => {
  it('swaps zh→en at prefix', () => {
    expect(replaceLangInPath('/zh/guide/demo', 'en')).toBe('/en/guide/demo');
  });
  it('inserts lang prefix on root', () => {
    expect(replaceLangInPath('/', 'ja')).toBe('/ja/');
  });
  it('preserves trailing slash and query', () => {
    expect(replaceLangInPath('/zh/changelog?v=1', 'en')).toBe('/en/changelog?v=1');
  });
});

describe('supportedLangs', () => {
  it('lists exactly zh/en/ja', () => {
    expect(supportedLangs).toEqual(['zh', 'en', 'ja']);
  });
});
```

- [ ] **Step 2: Verify fail**

`cd web && npm test helpers` — 7 fail (module not found).

- [ ] **Step 3: Implement**

```typescript
// web/src/i18n/helpers.ts
import zh from './ui.zh.json';
import en from './ui.en.json';
import ja from './ui.ja.json';

export type Lang = 'zh' | 'en' | 'ja';
export const supportedLangs: Lang[] = ['zh', 'en', 'ja'];

const DICTS: Record<Lang, Record<string, string>> = { zh, en, ja };

export function getUIStrings(lang: Lang): Record<string, string> {
  if (!supportedLangs.includes(lang)) throw new Error(`Unsupported lang: ${lang}`);
  return DICTS[lang];
}

export function replaceLangInPath(pathname: string, target: Lang): string {
  const m = pathname.match(/^\/(zh|en|ja)(\/|$)(.*)$/);
  if (m) {
    const rest = m[2] + m[3];
    return `/${target}${rest}`;
  }
  return `/${target}${pathname.endsWith('/') ? '' : '/'}${pathname.slice(1)}`;
}
```

- [ ] **Step 4: Verify pass**

- [ ] **Step 5: Commit**

```bash
git add web/src/i18n/helpers.ts web/src/i18n/helpers.test.ts
git commit -m "07 Website Phase 3.3 — i18n helpers (getUIStrings + replaceLangInPath, 7 tests)"
```

### Task 3.4: LangSwitcher React island

**Files:**
- Create: `web/src/components/react/LangSwitcher.tsx`
- Create: `web/src/components/react/LangSwitcher.test.tsx`

- [ ] **Step 1: Write tests**

```tsx
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { LangSwitcher } from './LangSwitcher';

describe('<LangSwitcher>', () => {
  it('renders 3 lang links', () => {
    render(<LangSwitcher currentLang="zh" pathname="/zh/guide" />);
    expect(screen.getAllByRole('link')).toHaveLength(3);
  });
  it('marks current lang as aria-current', () => {
    render(<LangSwitcher currentLang="en" pathname="/en/" />);
    const current = screen.getByText('EN');
    expect(current).toHaveAttribute('aria-current', 'page');
  });
  it('builds correct hrefs', () => {
    render(<LangSwitcher currentLang="zh" pathname="/zh/guide/demo" />);
    expect(screen.getByText('EN').closest('a')).toHaveAttribute('href', '/en/guide/demo');
    expect(screen.getByText('日').closest('a')).toHaveAttribute('href', '/ja/guide/demo');
  });
});
```

- [ ] **Step 2: Verify fail**

- [ ] **Step 3: Implement**

```tsx
// web/src/components/react/LangSwitcher.tsx
import { replaceLangInPath, type Lang } from '../../i18n/helpers';

const LABELS: Record<Lang, string> = { zh: '中', en: 'EN', ja: '日' };

interface Props {
  currentLang: Lang;
  pathname: string;
}

export function LangSwitcher({ currentLang, pathname }: Props) {
  const langs: Lang[] = ['en', 'zh', 'ja'];
  return (
    <nav className="flex gap-2 font-mono text-[10px] tracking-wider">
      {langs.map((l) => (
        <a
          key={l}
          href={replaceLangInPath(pathname, l)}
          aria-current={l === currentLang ? 'page' : undefined}
          className={l === currentLang ? 'text-ink font-bold' : 'text-ink-mute hover:text-accent'}
        >
          {LABELS[l]}
        </a>
      ))}
    </nav>
  );
}
```

- [ ] **Step 4: Verify pass**

- [ ] **Step 5: Commit**

```bash
git add web/src/components/react/LangSwitcher.tsx web/src/components/react/LangSwitcher.test.tsx
git commit -m "07 Website Phase 3.4 — LangSwitcher island (3 tests)"
```

### Task 3.5: Root redirect `/` → `/zh/`

**Files:**
- Create: `web/src/pages/index.astro`
- Create: `web/tests/e2e/lang.spec.ts`

- [ ] **Step 1: Write redirect**

```astro
---
return Astro.redirect('/zh/');
---
```

- [ ] **Step 2: E2E smoke**

```typescript
import { test, expect } from '@playwright/test';

test('root redirects to /zh/', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveURL(/\/zh\//);
});
```

- [ ] **Step 3: Verify**

`cd web && npx playwright test lang.spec.ts` — passes after `/zh/` exists; will fail with 404 here. That's OK — Phase 4 makes it pass. Document this.

- [ ] **Step 4: Commit**

```bash
git add web/src/pages/index.astro web/tests/e2e/lang.spec.ts
git commit -m "07 Website Phase 3.5 — / → /zh/ redirect + e2e smoke (passes after Phase 4 lands)"
```

---

## Phase 4 — Landing Page

### Task 4.1: Landing layout + TopNav + Footer

**Files:**
- Create: `web/src/layouts/LandingLayout.astro`
- Create: `web/src/components/astro/TopNav.astro`
- Create: `web/src/components/astro/Footer.astro`

- [ ] **Step 1: TopNav.astro**

```astro
---
import { ThemeToggle } from '../react/ThemeToggle';
import { LangSwitcher } from '../react/LangSwitcher';
import { getUIStrings, type Lang } from '../../i18n/helpers';
interface Props { lang: Lang; pathname: string; }
const { lang, pathname } = Astro.props;
const t = getUIStrings(lang);
---
<header class="flex justify-between items-center px-7 py-4 border-b border-rule">
  <div class="font-mono text-[10px] tracking-[0.18em] text-ink font-bold">
    SDTM/KB · VOL.01 · 2026
  </div>
  <button id="mobile-nav-toggle" class="md:hidden font-mono text-base px-2" aria-label="Open menu">☰</button>
  <nav id="mobile-nav-content" class="hidden md:flex items-center gap-4 font-mono text-[10px] tracking-wider text-ink-mute">
    <a href={`/${lang}/guide/`} class="hover:text-accent">{t['nav.guide']}</a>
    <a href={`/${lang}/#platforms`} class="hover:text-accent">{t['nav.platforms']}</a>
    <a href={`/${lang}/guide/demo-questions`} class="hover:text-accent">{t['nav.demo']}</a>
    <a href={`/${lang}/#downloads`} class="hover:text-accent">{t['nav.download']}</a>
    <span class="border-l border-rule pl-4 ml-2 flex items-center gap-3">
      <LangSwitcher client:load currentLang={lang} pathname={pathname} />
      <ThemeToggle client:load />
    </span>
  </nav>
</header>
<script>
  const btn = document.getElementById('mobile-nav-toggle');
  const nav = document.getElementById('mobile-nav-content');
  btn?.addEventListener('click', () => {
    nav?.classList.toggle('hidden');
  });
</script>
```

- [ ] **Step 2: Footer.astro**

```astro
---
import { getUIStrings, type Lang } from '../../i18n/helpers';
interface Props { lang: Lang; }
const { lang } = Astro.props;
const t = getUIStrings(lang);
---
<footer class="bg-ink text-bg px-7 py-6 flex justify-between items-center">
  <div>
    <div class="font-mono text-[10px] tracking-[0.18em] font-bold">SDTM/KB · v1.0 · 2026</div>
    <div class="font-serif text-[11px] italic mt-1" style="color: rgba(245, 241, 234, 0.6);">{t['footer.maintainer']}</div>
  </div>
  <div class="flex gap-3 font-mono text-[10px] tracking-wider">
    <a href={`/${lang}/changelog`}>CHANGELOG</a>
    <a href={`/${lang}/guide/`}>GUIDE</a>
    <a href="https://github.com/hakupao/sdtm-pedia">GITHUB</a>
  </div>
</footer>
```

- [ ] **Step 3: LandingLayout.astro**

```astro
---
import BaseLayout from './BaseLayout.astro';
import TopNav from '../components/astro/TopNav.astro';
import Footer from '../components/astro/Footer.astro';
import type { Lang } from '../i18n/helpers';
interface Props { title: string; lang: Lang; }
const { title, lang } = Astro.props;
const pathname = Astro.url.pathname;
---
<BaseLayout title={title} lang={lang}>
  <TopNav lang={lang} pathname={pathname} />
  <main>
    <slot />
  </main>
  <Footer lang={lang} />
</BaseLayout>
```

- [ ] **Step 4: Commit**

```bash
git add web/src/components/astro/TopNav.astro web/src/components/astro/Footer.astro web/src/layouts/LandingLayout.astro
git commit -m "07 Website Phase 4.1 — LandingLayout + TopNav (mobile drawer) + Footer"
```

### Task 4.2: §01 Hero section

**Files:**
- Create: `web/src/components/astro/HeroSection.astro`

- [ ] **Step 1: Write component**

```astro
---
import { getUIStrings, type Lang } from '../../i18n/helpers';
interface Props { lang: Lang; }
const { lang } = Astro.props;
const t = getUIStrings(lang);
const headline = {
  zh: { main: 'SDTM 知识库,', em: '横跨四个', tail: 'AI 平台.' },
  en: { main: 'SDTM Knowledge,', em: 'across four', tail: 'AI platforms.' },
  ja: { main: 'SDTM ナレッジ、', em: '4 つの', tail: 'AI プラットフォームへ。' },
}[lang];
const subdeck = {
  zh: '一份精心整理的 CDISC SDTMIG v3.4 参考 — 已映射, 已部署, 已评测. 一道问题, 一分钟, 一个带引用的答案.',
  en: 'A curated reference of CDISC SDTMIG v3.4 — mapped, deployed, evaluated. One question, one minute, one cited answer.',
  ja: 'CDISC SDTMIG v3.4 のキュレーテッドリファレンス — マッピング・デプロイ・評価済み。1 つの問い、1 分、1 つの引用付き回答。',
}[lang];
---
<section class="enter-fade px-7 pt-14 pb-8 border-b border-rule">
  <div class="font-mono text-[10px] tracking-[0.2em] text-accent font-bold mb-6">
    — 04 INTERNAL RELEASE
  </div>
  <h1 class="font-display text-4xl md:text-6xl font-bold leading-[1.05] tracking-[-0.025em] mb-4">
    {headline.main}<br />
    <em class="font-medium italic">{headline.em}</em> {headline.tail}
  </h1>
  <p class="font-serif text-[15px] leading-[1.55] text-ink-mute max-w-[480px] mt-5">{subdeck}</p>
  <div class="flex gap-2 mt-8 items-center flex-wrap">
    <a href={`/${lang}/guide/`} class="bg-ink text-bg px-4 py-2 font-mono text-[11px] tracking-wider font-bold hover:bg-accent transition-colors">
      {t['hero.cta.read']}
    </a>
    <a href="#downloads" class="border border-ink px-4 py-2 font-mono text-[11px] tracking-wider font-bold hover:border-accent hover:text-accent transition-colors">
      {t['hero.cta.download']}
    </a>
    <a href="https://github.com/hakupao/sdtm-pedia" class="px-3 py-2 font-mono text-[11px] tracking-wider text-ink-mute hover:text-accent transition-colors">
      {t['hero.cta.github']}
    </a>
  </div>
  <div class="mt-4 font-mono text-[9px] tracking-wider text-ink-mute">
    <span class="text-accent">●</span>  LIVE · CLAUDE 17/17 · GPT 16.5 · GEMINI 16 · NBLM 15
  </div>
</section>
```

- [ ] **Step 2: Commit**

```bash
git add web/src/components/astro/HeroSection.astro
git commit -m "07 Website Phase 4.2 — HeroSection.astro"
```

### Task 4.3: §02 Four Platforms with count-up island

**Files:**
- Create: `web/src/data/platforms.json`
- Create: `web/src/lib/countup.ts`
- Create: `web/src/lib/countup.test.ts`
- Create: `web/src/components/react/CountUp.tsx`
- Create: `web/src/components/react/CountUp.test.tsx`
- Create: `web/src/components/astro/PlatformsSection.astro`

- [ ] **Step 1: Data**

`web/src/data/platforms.json`:
```json
[
  { "key": "claude",     "name": "CLAUDE",     "score": 17,   "scoreText": "17",   "strength": { "zh": "精确变量 + 多步推理", "en": "Precise vars + multi-step", "ja": "精確変数 + 多段推論" } },
  { "key": "chatgpt",    "name": "CHATGPT",    "score": 16.5, "scoreText": "16.5", "strength": { "zh": "团队共享 / Store",    "en": "Team / Store sharing",  "ja": "チーム共有 / Store" } },
  { "key": "gemini",     "name": "GEMINI",     "score": 16,   "scoreText": "16",   "strength": { "zh": "长上下文 / 跨域",     "en": "Long context / cross-domain", "ja": "長文脈 / クロスドメイン" } },
  { "key": "notebooklm", "name": "NOTEBOOKLM", "score": 15,   "scoreText": "15",   "strength": { "zh": "100% 反虚构",         "en": "100% anti-hallucination",     "ja": "100% アンチハルシネーション" } }
]
```

- [ ] **Step 2: Count-up math + tests**

```typescript
// web/src/lib/countup.ts
export function easeOutQuad(t: number): number { return t * (2 - t); }

export function frameValue(start: number, end: number, elapsed: number, duration: number): number {
  if (elapsed >= duration) return end;
  const t = elapsed / duration;
  return start + (end - start) * easeOutQuad(t);
}
```

```typescript
// web/src/lib/countup.test.ts
import { describe, it, expect } from 'vitest';
import { easeOutQuad, frameValue } from './countup';

describe('easeOutQuad', () => {
  it('0 → 0', () => expect(easeOutQuad(0)).toBe(0));
  it('1 → 1', () => expect(easeOutQuad(1)).toBe(1));
  it('0.5 → 0.75', () => expect(easeOutQuad(0.5)).toBe(0.75));
});

describe('frameValue', () => {
  it('elapsed >= duration returns end', () => {
    expect(frameValue(0, 17, 1000, 600)).toBe(17);
  });
  it('elapsed 0 returns start', () => {
    expect(frameValue(0, 17, 0, 600)).toBe(0);
  });
  it('mid duration eases', () => {
    expect(frameValue(0, 17, 300, 600)).toBeCloseTo(12.75, 2);
  });
});
```

`cd web && npm test countup` — 6 pass.

- [ ] **Step 3: CountUp React + tests**

```tsx
// web/src/components/react/CountUp.tsx
import { useEffect, useRef, useState } from 'react';
import { frameValue } from '../../lib/countup';

interface Props { end: number; duration?: number; decimals?: number; }

export function CountUp({ end, duration = 600, decimals = 0 }: Props) {
  const [value, setValue] = useState(0);
  const ref = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    if (typeof window === 'undefined') return;
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) {
      setValue(end);
      return;
    }
    const node = ref.current;
    if (!node) return;
    const observer = new IntersectionObserver((entries) => {
      if (!entries[0].isIntersecting) return;
      observer.disconnect();
      const startTime = performance.now();
      let raf = 0;
      const tick = (t: number) => {
        const elapsed = t - startTime;
        setValue(frameValue(0, end, elapsed, duration));
        if (elapsed < duration) raf = requestAnimationFrame(tick);
      };
      raf = requestAnimationFrame(tick);
      return () => cancelAnimationFrame(raf);
    });
    observer.observe(node);
    return () => observer.disconnect();
  }, [end, duration]);

  return <span ref={ref}>{value.toFixed(decimals)}</span>;
}
```

```tsx
// web/src/components/react/CountUp.test.tsx
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import { CountUp } from './CountUp';

describe('<CountUp>', () => {
  it('renders 0 initially', () => {
    render(<CountUp end={17} />);
    expect(screen.getByText('0')).toBeInTheDocument();
  });
  it('renders end value when reduced motion preferred', () => {
    vi.spyOn(window, 'matchMedia').mockReturnValue({
      matches: true, addEventListener: vi.fn(), removeEventListener: vi.fn(),
    } as unknown as MediaQueryList);
    render(<CountUp end={16.5} decimals={1} />);
    expect(screen.getByText('16.5')).toBeInTheDocument();
  });
});
```

`npm test CountUp` — 2 pass.

- [ ] **Step 4: PlatformsSection.astro**

```astro
---
import SectionLabel from './SectionLabel.astro';
import { CountUp } from '../react/CountUp';
import platforms from '../../data/platforms.json';
import { type Lang } from '../../i18n/helpers';
interface Props { lang: Lang; }
const { lang } = Astro.props;
const subhead = {
  zh: '四种部署, 各有性格.',
  en: 'Four deployments, each with a temperament.',
  ja: '4 つのデプロイメント、それぞれの性格。',
}[lang];
---
<section id="platforms" class="enter-fade px-7 py-8 bg-bg-alt border-b border-rule">
  <SectionLabel number="02" label="FOUR PLATFORMS" />
  <h2 class="font-display text-2xl mb-5 leading-tight">{subhead}</h2>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-2">
    {platforms.map((p) => (
      <div class="bg-bg p-4 border border-rule">
        <div class="font-mono text-[8px] tracking-[0.15em] text-ink-mute">{p.name}</div>
        <div class="font-display text-3xl font-bold my-1">
          <CountUp client:visible end={p.score} decimals={p.score % 1 === 0 ? 0 : 1} />
          <span class="text-sm text-ink-faint">/17</span>
        </div>
        <div class="font-serif text-[11px] text-ink-mute leading-snug">{p.strength[lang]}</div>
      </div>
    ))}
  </div>
</section>
```

- [ ] **Step 5: Commit**

```bash
git add web/src/data/platforms.json web/src/lib/countup.ts web/src/lib/countup.test.ts web/src/components/react/CountUp.tsx web/src/components/react/CountUp.test.tsx web/src/components/astro/PlatformsSection.astro
git commit -m "07 Website Phase 4.3 — §02 PlatformsSection (count-up island, 8 tests, JSON data)"
```

### Task 4.4: §03 Compare preview section

**Files:**
- Create: `web/src/data/compare-dimensions.json`
- Create: `web/src/components/astro/ComparePreviewSection.astro`

- [ ] **Step 1: Data (preview is 4 of 9 full dimensions)**

```json
[
  { "key": "best-at",     "label": { "zh": "最强场景",   "en": "Best at",      "ja": "最も得意" },     "values": { "claude": "精确变量+推理", "chatgpt": "团队共享", "gemini": "长上下文", "notebooklm": "反虚构" }, "winners": ["claude"] },
  { "key": "capacity",    "label": { "zh": "容量上限",   "en": "Capacity",     "ja": "容量上限" },     "values": { "claude": "1.29M tok", "chatgpt": "20 file 硬限", "gemini": "1M tok 窗口", "notebooklm": "50 source/notebook" }, "winners": ["claude", "gemini"] },
  { "key": "sharing",     "label": { "zh": "团队共享",   "en": "Sharing",      "ja": "チーム共有" },   "values": { "claude": "Org/Project", "chatgpt": "Org/Store", "gemini": "Workspace", "notebooklm": "Email 邀请" }, "winners": ["chatgpt"] },
  { "key": "anti-halluc", "label": { "zh": "反虚构强度", "en": "Anti-halluc.", "ja": "アンチハル強度" }, "values": { "claude": "强", "chatgpt": "中", "gemini": "中", "notebooklm": "极强 (in-KB-only)" }, "winners": ["notebooklm"] }
]
```

- [ ] **Step 2: ComparePreviewSection.astro**

```astro
---
import SectionLabel from './SectionLabel.astro';
import dims from '../../data/compare-dimensions.json';
import platforms from '../../data/platforms.json';
import { getUIStrings, type Lang } from '../../i18n/helpers';
interface Props { lang: Lang; }
const { lang } = Astro.props;
const t = getUIStrings(lang);
const subhead = {
  zh: '按你想做的事来挑.',
  en: "Pick by what you're about to do.",
  ja: 'やりたいことで選ぶ。',
}[lang];
---
<section class="enter-fade px-7 py-8 border-b border-rule">
  <SectionLabel number="03" label="WHICH ONE?" />
  <h2 class="font-display text-2xl mb-5 leading-tight">{subhead}</h2>
  <div class="overflow-x-auto">
    <table class="w-full font-serif text-[12px] border-collapse min-w-[600px]">
      <thead>
        <tr class="border-b border-rule">
          <th class="text-left py-2 px-2 font-mono text-[9px] tracking-wider text-ink-mute">DIMENSION</th>
          {platforms.map((p) => (
            <th class="text-left py-2 px-2 font-mono text-[9px] tracking-wider text-ink-mute">{p.name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {dims.map((d) => (
          <tr class="border-b border-rule">
            <td class="py-2 px-2 font-mono text-[10px] tracking-wider">{d.label[lang]}</td>
            {platforms.map((p) => (
              <td class={`py-2 px-2 ${d.winners.includes(p.key) ? 'text-accent font-bold' : ''}`}>
                {d.values[p.key as keyof typeof d.values]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  </div>
  <a href="/compare" class="inline-block mt-4 font-mono text-[10px] tracking-wider text-accent hover:underline">
    {t['section.compare.cta']}
  </a>
</section>
```

- [ ] **Step 3: Commit**

```bash
git add web/src/data/compare-dimensions.json web/src/components/astro/ComparePreviewSection.astro
git commit -m "07 Website Phase 4.4 — §03 ComparePreviewSection (4-dim preview, x-scroll wrapper, accent winners)"
```

### Task 4.5: §04 Demo section

**Files:**
- Create: `web/src/data/demos.json`
- Create: `web/src/components/astro/DemoSection.astro`

- [ ] **Step 1: Data**

```json
[
  {
    "code": "D0",
    "kind": "WARMUP",
    "question": {
      "zh": "AESER 是 SDTMIG v3.4 哪个域什么变量? Core? CT C-code?",
      "en": "Which SDTMIG v3.4 domain and variable is AESER? Core? CT C-code?",
      "ja": "AESER は SDTMIG v3.4 のどのドメイン・変数？Core？CT C-code？"
    }
  },
  {
    "code": "D1",
    "kind": "NEW DOMAIN",
    "question": {
      "zh": "EGFR / Exon 19 / dbSNP 怎么映射到 GF 域?",
      "en": "How do EGFR / Exon 19 / dbSNP map to the GF domain?",
      "ja": "EGFR / Exon 19 / dbSNP は GF ドメインにどうマッピングされる？"
    }
  },
  {
    "code": "D5",
    "kind": "PREMISE PROBE",
    "question": {
      "zh": "SUPPTS 是 SDTM 标准里什么? QORIG 必填吗?",
      "en": "What is SUPPTS in the SDTM standard? Is QORIG required?",
      "ja": "SUPPTS は SDTM 標準の何？QORIG は必須？"
    },
    "hint": { "zh": "(故意问错前提)", "en": "(deliberate false premise)", "ja": "(意図的な誤前提)" }
  }
]
```

- [ ] **Step 2: Component**

```astro
---
import SectionLabel from './SectionLabel.astro';
import demos from '../../data/demos.json';
import { getUIStrings, type Lang } from '../../i18n/helpers';
interface Props { lang: Lang; }
const { lang } = Astro.props;
const t = getUIStrings(lang);
---
<section class="enter-fade px-7 py-8 bg-bg-alt border-b border-rule">
  <SectionLabel number="04" label="DEMO QUESTIONS" />
  <h2 class="font-display text-2xl mb-5 leading-tight">{t['section.demo.subhead']}</h2>
  <div class="flex flex-col gap-2">
    {demos.map((d) => (
      <div class="bg-bg p-3 border-l-[3px] border-accent">
        <div class="font-mono text-[9px] tracking-wider text-accent mb-1">{d.code} · {d.kind}</div>
        <div class="font-serif text-[12px]">
          {d.question[lang]}
          {d.hint && <span class="text-ink-mute italic ml-1">{d.hint[lang]}</span>}
        </div>
      </div>
    ))}
  </div>
  <a href={`/${lang}/guide/demo-questions`} class="inline-block mt-4 font-mono text-[10px] tracking-wider text-accent hover:underline">
    {t['section.demo.cta']}
  </a>
</section>
```

- [ ] **Step 3: Commit**

```bash
git add web/src/data/demos.json web/src/components/astro/DemoSection.astro
git commit -m "07 Website Phase 4.5 — §04 DemoSection (3 demos D0/D1/D5 trilingual)"
```

### Task 4.6: §05 Downloads section + URL builder

**Files:**
- Create: `web/src/data/downloads.json`
- Create: `web/src/lib/downloads.ts`
- Create: `web/src/lib/downloads.test.ts`
- Create: `web/src/components/astro/DownloadsSection.astro`

- [ ] **Step 1: Test for downloads URL builder**

```typescript
// web/src/lib/downloads.test.ts
import { describe, it, expect } from 'vitest';
import { buildReleaseAssetURL, REPO } from './downloads';

describe('downloads', () => {
  it('REPO matches actual repo', () => {
    expect(REPO).toBe('hakupao/sdtm-pedia');
  });
  it('buildReleaseAssetURL builds canonical GH URL', () => {
    expect(buildReleaseAssetURL('v1.0', 'claude_bundle_v1.0.zip'))
      .toBe('https://github.com/hakupao/sdtm-pedia/releases/download/v1.0/claude_bundle_v1.0.zip');
  });
});
```

- [ ] **Step 2: Implement**

```typescript
// web/src/lib/downloads.ts
export const REPO = 'hakupao/sdtm-pedia';

export function buildReleaseAssetURL(tag: string, filename: string): string {
  return `https://github.com/${REPO}/releases/download/${tag}/${filename}`;
}
```

`npm test downloads` — 2 pass.

- [ ] **Step 3: Data**

```json
{
  "tag": "v1.0",
  "bundles": [
    { "platform": "claude",     "filename": "claude_bundle_v1.0.zip",     "files": 19, "sizeMB": 4.6 },
    { "platform": "chatgpt",    "filename": "chatgpt_bundle_v1.0.zip",    "files":  9, "sizeMB": 9.3 },
    { "platform": "gemini",     "filename": "gemini_bundle_v1.0.zip",     "files":  4, "sizeMB": 2.2 },
    { "platform": "notebooklm", "filename": "notebooklm_bundle_v1.0.zip", "files": 43, "sizeMB": 9.4 }
  ]
}
```

- [ ] **Step 4: Component**

```astro
---
import SectionLabel from './SectionLabel.astro';
import downloads from '../../data/downloads.json';
import { buildReleaseAssetURL, REPO } from '../../lib/downloads';
import { getUIStrings, type Lang } from '../../i18n/helpers';
interface Props { lang: Lang; }
const { lang } = Astro.props;
const t = getUIStrings(lang);
const subhead = { zh: '自部署你自己的.', en: 'Self-deploy your own.', ja: 'セルフデプロイしましょう。' }[lang];
---
<section id="downloads" class="enter-fade px-7 py-8 border-b border-rule">
  <SectionLabel number="05" label="DOWNLOADS" />
  <h2 class="font-display text-2xl mb-5 leading-tight">{subhead}</h2>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
    {downloads.bundles.map((b) => (
      <a href={buildReleaseAssetURL(downloads.tag, b.filename)}
         class="bg-bg-alt p-3 border border-rule flex justify-between items-center hover:border-accent transition-colors">
        <div>
          <div class="font-mono text-[11px] font-bold">{b.filename}</div>
          <div class="font-mono text-[9px] text-ink-mute">{b.files} files · {b.sizeMB} MB</div>
        </div>
        <span class="font-mono text-lg text-accent">↓</span>
      </a>
    ))}
  </div>
  <a href={`https://github.com/${REPO}/releases`} class="inline-block mt-3 font-mono text-[9px] tracking-wider text-ink-mute hover:text-accent">
    {t['section.downloads.cta']}
  </a>
</section>
```

- [ ] **Step 5: Commit**

```bash
git add web/src/data/downloads.json web/src/lib/downloads.ts web/src/lib/downloads.test.ts web/src/components/astro/DownloadsSection.astro
git commit -m "07 Website Phase 4.6 — §05 DownloadsSection (4-bundle grid, GH Release URL builder, 2 tests)"
```

### Task 4.7: Wire landing page

**Files:**
- Create: `web/src/pages/[lang]/index.astro`

- [ ] **Step 1: Page**

```astro
---
import LandingLayout from '../../layouts/LandingLayout.astro';
import HeroSection from '../../components/astro/HeroSection.astro';
import PlatformsSection from '../../components/astro/PlatformsSection.astro';
import ComparePreviewSection from '../../components/astro/ComparePreviewSection.astro';
import DemoSection from '../../components/astro/DemoSection.astro';
import DownloadsSection from '../../components/astro/DownloadsSection.astro';
import { supportedLangs, type Lang } from '../../i18n/helpers';

export function getStaticPaths() {
  return supportedLangs.map((lang) => ({ params: { lang } }));
}

const lang = Astro.params.lang as Lang;
const titles = { zh: 'SDTM 知识库', en: 'SDTM Knowledge', ja: 'SDTM ナレッジ' };
---
<LandingLayout title={titles[lang]} lang={lang}>
  <HeroSection lang={lang} />
  <PlatformsSection lang={lang} />
  <ComparePreviewSection lang={lang} />
  <DemoSection lang={lang} />
  <DownloadsSection lang={lang} />
</LandingLayout>
```

- [ ] **Step 2: Build smoke**

```bash
cd web && npm run build
```

Expected: build succeeds, `web/dist/zh/index.html`, `web/dist/en/index.html`, `web/dist/ja/index.html` exist.

- [ ] **Step 3: E2E smoke**

```typescript
// web/tests/e2e/smoke.spec.ts
import { test, expect } from '@playwright/test';

test.describe('landing', () => {
  for (const lang of ['zh', 'en', 'ja']) {
    test(`/${lang}/ renders all 5 sections`, async ({ page }) => {
      await page.goto(`/${lang}/`);
      await expect(page.locator('h1')).toBeVisible();
      await expect(page.locator('text=FOUR PLATFORMS')).toBeVisible();
      await expect(page.locator('text=WHICH ONE?')).toBeVisible();
      await expect(page.locator('text=DEMO QUESTIONS')).toBeVisible();
      await expect(page.locator('text=DOWNLOADS')).toBeVisible();
    });
  }
});
```

`cd web && npm run test:e2e` — 3 tests pass + redirect test.

- [ ] **Step 4: Commit**

```bash
git add web/src/pages/[lang]/index.astro web/tests/e2e/smoke.spec.ts
git commit -m "07 Website Phase 4.7 — landing page wired (3 langs × 5 sections, e2e smoke 4/4)"
```

### Task 4.8: Section enter-viewport fade animation

**Files:**
- Modify: `web/src/styles/global.css`
- Create: `web/src/components/astro/EnterFadeScript.astro`
- Modify: `web/src/layouts/LandingLayout.astro`

- [ ] **Step 1: Add CSS**

Append to `web/src/styles/global.css`:
```css
.enter-fade {
  opacity: 0;
  transform: translateY(6px);
  transition: opacity 400ms ease-out, transform 400ms ease-out;
}
.enter-fade.is-visible {
  opacity: 1;
  transform: translateY(0);
}
@media (prefers-reduced-motion: reduce) {
  .enter-fade { opacity: 1; transform: none; transition: none; }
}
```

- [ ] **Step 2: EnterFadeScript.astro**

```astro
<script>
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.15 });
    document.querySelectorAll('.enter-fade').forEach((el) => observer.observe(el));
  } else {
    document.querySelectorAll('.enter-fade').forEach((el) => el.classList.add('is-visible'));
  }
</script>
```

- [ ] **Step 3: Include in LandingLayout**

Edit `web/src/layouts/LandingLayout.astro`, add before closing `</BaseLayout>`:
```astro
import EnterFadeScript from '../components/astro/EnterFadeScript.astro';
...
<EnterFadeScript />
```

- [ ] **Step 4: Visual smoke**

`cd web && npm run dev`, open `/zh/`, scroll: each section fades up smoothly.

- [ ] **Step 5: Reduced motion smoke**

In Chrome DevTools → Rendering → "Emulate CSS media feature prefers-reduced-motion: reduce" → reload. Sections should be instantly visible.

- [ ] **Step 6: Commit**

```bash
git add web/src/styles/global.css web/src/components/astro/EnterFadeScript.astro web/src/layouts/LandingLayout.astro
git commit -m "07 Website Phase 4.8 — section enter-fade animation (IO + prefers-reduced-motion guard)"
```

---

## Phase 5 — Docs Reader

### Task 5.1: Docs sidebar + TOC + prev/next + layout

**Files:**
- Create: `web/src/components/astro/DocsSidebar.astro`
- Create: `web/src/components/astro/DocsTOC.astro`
- Create: `web/src/components/astro/PrevNextNav.astro`
- Create: `web/src/layouts/DocsLayout.astro`

- [ ] **Step 1: DocsSidebar.astro**

```astro
---
import { getCollection } from 'astro:content';
import type { Lang } from '../../i18n/helpers';
interface Props { lang: Lang; currentSlug: string; }
const { lang, currentSlug } = Astro.props;
const all = await getCollection('guide', (e) => e.data.lang === lang);
all.sort((a, b) => (a.data.order ?? 99) - (b.data.order ?? 99));
---
<button id="docs-sidebar-toggle" class="lg:hidden font-mono text-[10px] tracking-wider px-3 py-2 border border-rule mx-7 mt-4" aria-controls="docs-sidebar-content" aria-expanded="false">
  ☰ DOCS
</button>
<aside id="docs-sidebar-content" class="hidden lg:block w-full lg:w-60 border-b lg:border-b-0 lg:border-r border-rule p-5 shrink-0">
  <div class="font-mono text-[9px] tracking-wider text-ink-mute mb-3">DOCS / {lang.toUpperCase()}</div>
  <ul class="flex flex-col gap-1 font-serif text-[13px]">
    {all.map((doc) => (
      <li>
        <a href={`/${lang}/guide/${doc.data.slug}`}
           class={`block py-1 ${doc.data.slug === currentSlug ? 'text-accent font-bold' : 'hover:text-accent'}`}>
          {doc.data.title || doc.data.slug}
        </a>
      </li>
    ))}
  </ul>
</aside>
<script>
  const btn = document.getElementById('docs-sidebar-toggle');
  const drawer = document.getElementById('docs-sidebar-content');
  btn?.addEventListener('click', () => {
    const open = drawer?.classList.toggle('hidden');
    btn.setAttribute('aria-expanded', String(!open));
  });
</script>
```

- [ ] **Step 2: DocsTOC.astro**

```astro
---
interface Props { headings: { depth: number; slug: string; text: string }[]; }
const { headings } = Astro.props;
const filtered = headings.filter((h) => h.depth === 2 || h.depth === 3);
---
<aside class="w-56 p-5 hidden xl:block sticky top-0 self-start max-h-screen overflow-y-auto shrink-0">
  <div class="font-mono text-[9px] tracking-wider text-ink-mute mb-3">ON THIS PAGE</div>
  <ul class="flex flex-col gap-1 font-serif text-[12px]">
    {filtered.map((h) => (
      <li class={h.depth === 3 ? 'pl-3' : ''}>
        <a href={`#${h.slug}`} class="text-ink-mute hover:text-accent block py-0.5" data-toc-link={h.slug}>
          {h.text}
        </a>
      </li>
    ))}
  </ul>
</aside>
<script>
  const links = document.querySelectorAll('[data-toc-link]');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        const id = (e.target as HTMLElement).id;
        links.forEach((l) => {
          const match = l.getAttribute('data-toc-link') === id;
          l.classList.toggle('text-accent', match);
          l.classList.toggle('font-bold', match);
        });
      }
    });
  }, { rootMargin: '-30% 0px -60% 0px' });
  document.querySelectorAll('h2[id], h3[id]').forEach((h) => observer.observe(h));
</script>
```

- [ ] **Step 3: PrevNextNav.astro**

```astro
---
import { getCollection } from 'astro:content';
import type { Lang } from '../../i18n/helpers';
interface Props { lang: Lang; currentSlug: string; }
const { lang, currentSlug } = Astro.props;
const all = await getCollection('guide', (e) => e.data.lang === lang);
all.sort((a, b) => (a.data.order ?? 99) - (b.data.order ?? 99));
const idx = all.findIndex((d) => d.data.slug === currentSlug);
const prev = idx > 0 ? all[idx - 1] : null;
const next = idx < all.length - 1 ? all[idx + 1] : null;
---
<nav class="flex justify-between border-t border-rule pt-6 mt-10 font-mono text-[10px] tracking-wider">
  <div>
    {prev && (
      <a href={`/${lang}/guide/${prev.data.slug}`} class="hover:text-accent">← {prev.data.title || prev.data.slug}</a>
    )}
  </div>
  <div>
    {next && (
      <a href={`/${lang}/guide/${next.data.slug}`} class="hover:text-accent">{next.data.title || next.data.slug} →</a>
    )}
  </div>
</nav>
```

- [ ] **Step 4: DocsLayout.astro**

```astro
---
import BaseLayout from './BaseLayout.astro';
import TopNav from '../components/astro/TopNav.astro';
import DocsSidebar from '../components/astro/DocsSidebar.astro';
import DocsTOC from '../components/astro/DocsTOC.astro';
import PrevNextNav from '../components/astro/PrevNextNav.astro';
import type { Lang } from '../i18n/helpers';
interface Props { title: string; lang: Lang; slug: string; headings: { depth: number; slug: string; text: string }[]; }
const { title, lang, slug, headings } = Astro.props;
const pathname = Astro.url.pathname;
---
<BaseLayout title={title} lang={lang}>
  <TopNav lang={lang} pathname={pathname} />
  <div class="flex max-w-screen-xl mx-auto flex-col lg:flex-row">
    <DocsSidebar lang={lang} currentSlug={slug} />
    <article class="flex-1 px-6 py-10 max-w-[720px] prose-doc">
      <slot />
      <PrevNextNav lang={lang} currentSlug={slug} />
    </article>
    <DocsTOC headings={headings} />
  </div>
</BaseLayout>
```

- [ ] **Step 5: Commit**

```bash
git add web/src/layouts/DocsLayout.astro web/src/components/astro/DocsSidebar.astro web/src/components/astro/DocsTOC.astro web/src/components/astro/PrevNextNav.astro
git commit -m "07 Website Phase 5.1 — DocsLayout 3-col + Sidebar (mobile drawer) + TOC scroll-spy + PrevNext"
```

### Task 5.2: Markdown body styling

**Files:**
- Create: `web/src/styles/prose.css`
- Modify: `web/src/styles/global.css`

- [ ] **Step 1: Write prose.css**

```css
.prose-doc {
  font-family: 'Source Serif Pro', Georgia, serif;
  font-size: 16px;
  line-height: 1.7;
  color: var(--ink);
}
.prose-doc h1 { font-family: 'Playfair Display', serif; font-size: 36px; font-style: italic; font-weight: 700; margin-top: 0; margin-bottom: 24px; line-height: 1.1; }
.prose-doc h2 { font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 700; margin-top: 48px; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid var(--rule); }
.prose-doc h3 { font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; margin-top: 32px; margin-bottom: 12px; }
.prose-doc h4 { font-family: 'Playfair Display', serif; font-size: 18px; font-weight: 700; margin-top: 24px; margin-bottom: 8px; }
.prose-doc p { margin-bottom: 16px; }
.prose-doc a { color: var(--accent); text-decoration: underline; text-underline-offset: 3px; }
.prose-doc a:hover { text-decoration-thickness: 2px; }
.prose-doc code { font-family: 'JetBrains Mono', monospace; font-size: 13px; background: var(--bg-alt); padding: 1px 6px; }
.prose-doc pre { font-family: 'JetBrains Mono', monospace; font-size: 13px; background: var(--bg-alt); border: 1px solid var(--rule); padding: 16px; overflow-x: auto; margin: 16px 0; }
.prose-doc pre code { background: none; padding: 0; }
.prose-doc table { border-collapse: collapse; margin: 24px 0; width: 100%; font-size: 14px; }
.prose-doc table th { background: var(--ink); color: var(--bg); padding: 8px 12px; text-align: left; font-weight: 700; }
.prose-doc table td { padding: 8px 12px; border: 1px solid var(--rule); }
.prose-doc ul, .prose-doc ol { padding-left: 24px; margin-bottom: 16px; }
.prose-doc li { margin-bottom: 6px; }
.prose-doc blockquote { border-left: 3px solid var(--accent); padding-left: 16px; margin: 24px 0; color: var(--ink-mute); font-style: italic; }
.prose-doc hr { border: 0; border-top: 1px solid var(--rule); margin: 32px 0; }
.prose-doc em { font-style: italic; }
.prose-doc strong { font-weight: 700; }
```

- [ ] **Step 2: Import into global.css**

Append to `web/src/styles/global.css`:
```css
@import './prose.css';
```

- [ ] **Step 3: Commit**

```bash
git add web/src/styles/prose.css web/src/styles/global.css
git commit -m "07 Website Phase 5.2 — prose.css for markdown body"
```

### Task 5.3: Catchall docs page route + lang fallback

**Files:**
- Create: `web/src/pages/[lang]/guide/[...slug].astro`
- Create: `web/src/pages/[lang]/guide/index.astro`
- Create: `web/src/pages/[lang]/changelog.astro`

- [ ] **Step 1: guide/index.astro (redirect)**

```astro
---
const { lang } = Astro.params;
return Astro.redirect(`/${lang}/guide/user-guide`);
---
```

- [ ] **Step 2: [...slug].astro with lang fallback**

```astro
---
import { getCollection } from 'astro:content';
import DocsLayout from '../../../layouts/DocsLayout.astro';
import { type Lang } from '../../../i18n/helpers';

export async function getStaticPaths() {
  const all = await getCollection('guide');
  const paths: any[] = [];
  for (const doc of all) {
    const docLang = doc.data.lang || 'en';
    const slug = doc.data.slug;
    paths.push({ params: { lang: docLang, slug }, props: { entry: doc, fallback: false } });
    if (docLang === 'en') {
      for (const altLang of ['zh', 'ja']) {
        const localized = all.find((d) => d.data.slug === slug && d.data.lang === altLang);
        if (!localized) {
          paths.push({ params: { lang: altLang, slug }, props: { entry: doc, fallback: true } });
        }
      }
    }
  }
  return paths;
}

const { entry, fallback } = Astro.props;
const { Content, headings } = await entry.render();
const lang = Astro.params.lang as Lang;
const slug = entry.data.slug as string;
const title = entry.data.title || slug;
---
<DocsLayout title={title} lang={lang} slug={slug} headings={headings}>
  {fallback && (
    <div class="bg-bg-alt border border-rule p-3 mb-6 font-mono text-[10px] tracking-wider text-ink-mute">
      English source — translation pending
    </div>
  )}
  <Content />
</DocsLayout>
```

- [ ] **Step 3: changelog.astro**

```astro
---
import { getCollection } from 'astro:content';
import DocsLayout from '../../layouts/DocsLayout.astro';
import { type Lang } from '../../i18n/helpers';
const lang = Astro.params.lang as Lang;
const all = await getCollection('guide');
const entry = all.find((d) => d.data.slug === 'changelog');
if (!entry) throw new Error('CHANGELOG entry not found in collection');
const { Content, headings } = await entry.render();
---
<DocsLayout title="Changelog" lang={lang} slug="changelog" headings={headings}>
  <Content />
</DocsLayout>
```

- [ ] **Step 4: Build smoke**

`cd web && npm run build` — succeeds. Verify dirs:
```bash
ls web/dist/zh/guide/ web/dist/en/guide/ web/dist/ja/guide/
```

Each should have user-guide/, glossary/, demo-questions/, known-limitations/, etc.

- [ ] **Step 5: E2E smoke**

```typescript
// extend web/tests/e2e/smoke.spec.ts
test('docs reader renders user-guide in zh', async ({ page }) => {
  await page.goto('/zh/guide/user-guide');
  await expect(page.locator('article h1')).toBeVisible();
  await expect(page.locator('aside').first()).toBeVisible();
});
```

- [ ] **Step 6: Commit**

```bash
git add web/src/pages/[lang]/guide/index.astro web/src/pages/[lang]/guide/[...slug].astro web/src/pages/[lang]/changelog.astro web/tests/e2e/smoke.spec.ts
git commit -m "07 Website Phase 5.3 — docs catchall + lang fallback + /changelog (e2e)"
```

---

## Phase 6 — Multi-dim Comparison Page

### Task 6.1: Full /compare page with filter

**Files:**
- Create: `web/src/components/react/CompareFilter.tsx`
- Create: `web/src/components/react/CompareFilter.test.tsx`
- Create: `web/src/pages/compare.astro`

- [ ] **Step 1: Test for filter logic**

```tsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { CompareFilter } from './CompareFilter';

const dims = [
  { key: 'best-at',  label: { zh: '最强场景', en: 'Best at',    ja: '最も得意' }, values: { claude: 'A', chatgpt: 'B', gemini: 'C', notebooklm: 'D' }, winners: ['claude'] },
  { key: 'capacity', label: { zh: '容量上限', en: 'Capacity',   ja: '容量上限' }, values: { claude: '1.29M', chatgpt: '20', gemini: '1M', notebooklm: '50' }, winners: ['claude'] },
];

describe('<CompareFilter>', () => {
  it('renders all rows by default', () => {
    render(<CompareFilter dims={dims} lang="zh" />);
    expect(screen.getByText('最强场景')).toBeInTheDocument();
    expect(screen.getByText('容量上限')).toBeInTheDocument();
  });
  it('filters rows by search input', () => {
    render(<CompareFilter dims={dims} lang="zh" />);
    const input = screen.getByRole('searchbox');
    fireEvent.change(input, { target: { value: '容量' } });
    expect(screen.queryByText('最强场景')).not.toBeInTheDocument();
    expect(screen.getByText('容量上限')).toBeInTheDocument();
  });
});
```

- [ ] **Step 2: Implement**

```tsx
// web/src/components/react/CompareFilter.tsx
import { useState } from 'react';
import platforms from '../../data/platforms.json';
import type { Lang } from '../../i18n/helpers';

interface Dim {
  key: string;
  label: Record<Lang, string>;
  values: Record<string, string>;
  winners: string[];
}

interface Props { dims: Dim[]; lang: Lang; }

export function CompareFilter({ dims, lang }: Props) {
  const [q, setQ] = useState('');
  const lower = q.toLowerCase().trim();
  const filtered = lower ? dims.filter((d) => d.label[lang].toLowerCase().includes(lower)) : dims;

  return (
    <>
      <input
        type="search"
        value={q}
        onChange={(e) => setQ(e.target.value)}
        placeholder="Filter dimensions..."
        className="font-mono text-sm px-3 py-2 border border-rule bg-bg w-64 mb-6"
      />
      <div className="overflow-x-auto">
        <table className="w-full font-serif text-sm border-collapse min-w-[600px]">
          <thead>
            <tr className="border-b border-rule">
              <th className="text-left py-2 px-2 font-mono text-[9px] tracking-wider">DIMENSION</th>
              {platforms.map((p) => (
                <th key={p.key} className="text-left py-2 px-2 font-mono text-[9px] tracking-wider">{p.name}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {filtered.map((d) => (
              <tr key={d.key} className="border-b border-rule">
                <td className="py-2 px-2 font-mono text-[10px] tracking-wider">{d.label[lang]}</td>
                {platforms.map((p) => (
                  <td key={p.key} className={`py-2 px-2 ${d.winners.includes(p.key) ? 'text-accent font-bold' : ''}`}>
                    {d.values[p.key]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}
```

`npm test CompareFilter` — 2 pass.

- [ ] **Step 3: compare.astro**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import TopNav from '../components/astro/TopNav.astro';
import { CompareFilter } from '../components/react/CompareFilter';
import dims from '../data/compare-dimensions.json';
import { type Lang } from '../i18n/helpers';

const url = new URL(Astro.request.url);
const langParam = url.searchParams.get('lang');
const lang: Lang = langParam === 'en' || langParam === 'ja' ? langParam : 'zh';
---
<BaseLayout title="Platform Comparison" lang={lang}>
  <TopNav lang={lang} pathname={url.pathname} />
  <main class="px-7 py-8 max-w-screen-xl mx-auto">
    <h1 class="font-display text-4xl font-bold mb-2">Multi-dimensional Comparison</h1>
    <p class="font-serif text-ink-mute mb-8">Side-by-side across 4 platforms. Filter by dimension keyword.</p>
    <CompareFilter client:load dims={dims} lang={lang} />
  </main>
</BaseLayout>
```

- [ ] **Step 4: Commit**

```bash
git add web/src/pages/compare.astro web/src/components/react/CompareFilter.tsx web/src/components/react/CompareFilter.test.tsx
git commit -m "07 Website Phase 6.1 — /compare page + CompareFilter island (search, 2 tests)"
```

### Task 6.2: Expand compare-dimensions.json to full 9 dims

**Files:**
- Modify: `web/src/data/compare-dimensions.json`

- [ ] **Step 1: Add 5 more dimensions**

Append to existing 4 (best-at / capacity / sharing / anti-halluc) — add: subscription, internet, file-limit, worst-at, score. Source content from `PLATFORM_COMPARISON.zh.md` (Phase 0 output).

```json
[
  // ...existing 4 dimensions...
  { "key": "score",        "label": { "zh": "评测得分",   "en": "Score",        "ja": "評価スコア" },     "values": { "claude": "17/17", "chatgpt": "16.5/17", "gemini": "16/17", "notebooklm": "15/17" }, "winners": ["claude"] },
  { "key": "subscription", "label": { "zh": "套餐要求",   "en": "Subscription", "ja": "サブスク要件" },   "values": { "claude": "Pro/Team/Ent", "chatgpt": "Plus/Team/Ent", "gemini": "Advanced/Workspace", "notebooklm": "Pro/Workspace" }, "winners": [] },
  { "key": "internet",     "label": { "zh": "联网能力",   "en": "Internet",     "ja": "インターネット" }, "values": { "claude": "需手开", "chatgpt": "默认开", "gemini": "默认开", "notebooklm": "in-KB-only" }, "winners": ["chatgpt", "gemini"] },
  { "key": "file-limit",   "label": { "zh": "文件数上限", "en": "File limit",   "ja": "ファイル数上限" }, "values": { "claude": "无显式 (按 token)", "chatgpt": "20 file 硬限", "gemini": "无显式", "notebooklm": "50/notebook" }, "winners": ["claude", "gemini"] },
  { "key": "worst-at",     "label": { "zh": "最弱场景",   "en": "Worst at",     "ja": "最も苦手" },       "values": { "claude": "实时联网", "chatgpt": "长尾 chunk", "gemini": "团队共享(非Workspace)", "notebooklm": "in-KB 外问题" }, "winners": [] }
]
```

- [ ] **Step 2: Update preview to use 4 chosen highlight dims** (already 4 in `ComparePreviewSection.astro`, no code change needed — but verify the dims in preview are the most user-relevant: best-at / capacity / sharing / anti-halluc)

- [ ] **Step 3: Decide preview vs full presentation**

`ComparePreviewSection.astro` reads ALL dims from the JSON but landing should show only first 4. Modify the section's loop:
```astro
{dims.slice(0, 4).map((d) => ( ... ))}
```

`/compare` page passes ALL dims to the React filter. No change needed there.

- [ ] **Step 4: Commit**

```bash
git add web/src/data/compare-dimensions.json web/src/components/astro/ComparePreviewSection.astro
git commit -m "07 Website Phase 6.2 — expand compare-dimensions to 9 dims (preview shows first 4 via slice)"
```

---

## Phase 7 — Search (Pagefind)

### Task 7.1: Verify Pagefind builds with site

- [ ] **Step 1: Run build**

```bash
cd web && npm run build
ls dist/pagefind/
```

Expected: `pagefind.js`, `pagefind-ui.js`, `*.pf_index`, `*.pf_meta` exist. If not, troubleshoot — `pagefind --site dist` in build script (Task 1.6) should produce these.

- [ ] **Step 2: No commit unless config tweaks needed**

### Task 7.2: SearchOverlay React island

**Files:**
- Create: `web/src/components/react/SearchOverlay.tsx`
- Create: `web/src/components/react/SearchOverlay.test.tsx`

- [ ] **Step 1: Test (UI behavior; Pagefind itself needs built index)**

```tsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { SearchOverlay } from './SearchOverlay';

describe('<SearchOverlay>', () => {
  it('opens on Cmd+K', () => {
    render(<SearchOverlay />);
    expect(screen.queryByRole('searchbox')).not.toBeInTheDocument();
    fireEvent.keyDown(document, { key: 'k', metaKey: true });
    expect(screen.getByRole('searchbox')).toBeInTheDocument();
  });
  it('closes on Escape', () => {
    render(<SearchOverlay />);
    fireEvent.keyDown(document, { key: 'k', metaKey: true });
    fireEvent.keyDown(document, { key: 'Escape' });
    expect(screen.queryByRole('searchbox')).not.toBeInTheDocument();
  });
});
```

- [ ] **Step 2: Implement (no innerHTML — render plain text excerpt for safety)**

```tsx
// web/src/components/react/SearchOverlay.tsx
import { useEffect, useRef, useState } from 'react';

interface Result {
  url: string;
  meta?: { title?: string };
  excerpt?: string;
}

function stripHtml(html: string): string {
  return html.replace(/<[^>]*>/g, '');
}

export function SearchOverlay() {
  const [open, setOpen] = useState(false);
  const [results, setResults] = useState<Result[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);
  const pagefindRef = useRef<any>(null);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setOpen(true);
      }
      if (e.key === 'Escape') setOpen(false);
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, []);

  useEffect(() => {
    if (!open) return;
    inputRef.current?.focus();
    if (!pagefindRef.current && typeof window !== 'undefined') {
      // @ts-ignore — runtime import of static asset
      import(/* @vite-ignore */ '/pagefind/pagefind.js').then((m) => { pagefindRef.current = m; });
    }
  }, [open]);

  const onChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const q = e.target.value;
    if (!q || !pagefindRef.current) { setResults([]); return; }
    const { results: pageResults } = await pagefindRef.current.search(q);
    const data = await Promise.all(pageResults.slice(0, 10).map((r: any) => r.data()));
    setResults(data);
  };

  if (!open) return null;
  return (
    <div className="fixed inset-0 bg-black/60 z-50 flex items-start justify-center pt-32" onClick={() => setOpen(false)}>
      <div className="bg-bg border border-rule w-full max-w-xl mx-4" onClick={(e) => e.stopPropagation()}>
        <input
          ref={inputRef}
          type="search"
          role="searchbox"
          placeholder="Search docs..."
          onChange={onChange}
          className="w-full px-4 py-3 font-mono text-sm border-b border-rule bg-bg"
        />
        <ul className="max-h-96 overflow-y-auto">
          {results.map((r, i) => (
            <li key={i} className="border-b border-rule p-3">
              <a href={r.url} className="block hover:bg-bg-alt">
                <div className="font-mono text-[10px] tracking-wider text-accent">{r.meta?.title || r.url}</div>
                <div className="font-serif text-sm text-ink-mute mt-1">{r.excerpt ? stripHtml(r.excerpt) : ''}</div>
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
```

`npm test SearchOverlay` — 2 pass.

- [ ] **Step 3: Mount overlay + Cmd+K hint in TopNav**

Edit `TopNav.astro` to include `<SearchOverlay client:load />` (place anywhere, the overlay positions itself). Add a visible hint button:
```astro
<button class="font-mono text-[10px] text-ink-mute hover:text-accent" onclick="document.dispatchEvent(new KeyboardEvent('keydown', {key:'k', metaKey:true}))" aria-label="Open search">
  ⌘K
</button>
```

Place inside the nav `<span>` block, alongside ThemeToggle and LangSwitcher.

- [ ] **Step 4: E2E smoke**

```typescript
// web/tests/e2e/search.spec.ts
import { test, expect } from '@playwright/test';

test('search opens with Cmd+K and finds AESER', async ({ page }) => {
  // Note: requires `npm run build && npm run preview` not just dev (pagefind index built only on build)
  await page.goto('/zh/guide/user-guide');
  await page.keyboard.press('Meta+k');
  const input = page.getByRole('searchbox');
  await expect(input).toBeVisible();
  await input.fill('AESER');
  await expect(page.locator('text=AESER').first()).toBeVisible({ timeout: 5000 });
});
```

Run: `cd web && npm run build && npm run preview &` then `npx playwright test search.spec.ts`. After test, kill preview server.

- [ ] **Step 5: Commit**

```bash
git add web/src/components/react/SearchOverlay.tsx web/src/components/react/SearchOverlay.test.tsx web/src/components/astro/TopNav.astro web/tests/e2e/search.spec.ts
git commit -m "07 Website Phase 7.2 — SearchOverlay (Cmd+K, Pagefind dynamic import, plain-text excerpt, 2 tests + e2e)"
```

---

## Phase 8 — Downloads Pipeline

### Task 8.1: Bundle build script

**Files:**
- Create: `web/scripts/build-bundles.sh`

- [ ] **Step 1: Write script**

```bash
#!/usr/bin/env bash
# web/scripts/build-bundles.sh — produces 4 platform zip bundles in web/dist-bundles/
set -euo pipefail

VERSION="${1:-v1.0}"
SRC_ROOT="$(cd "$(dirname "$0")/../.." && pwd)/ai_platforms/release/v1.0/self_deploy"
OUT_DIR="$(cd "$(dirname "$0")/.." && pwd)/dist-bundles"

mkdir -p "$OUT_DIR"
rm -f "$OUT_DIR"/*.zip

for PLATFORM in claude chatgpt gemini notebooklm; do
  SRC="$SRC_ROOT/$PLATFORM"
  if [[ ! -d "$SRC" ]]; then
    echo "ERROR: $SRC not found" >&2
    exit 1
  fi
  OUT="$OUT_DIR/${PLATFORM}_bundle_${VERSION}.zip"
  ( cd "$SRC_ROOT" && zip -rq "$OUT" "$PLATFORM/" )
  echo "✓ $OUT  ($(du -h "$OUT" | cut -f1))"
done

echo ""
echo "Done. Upload to GH Release: gh release create $VERSION $OUT_DIR/*.zip"
```

- [ ] **Step 2: Make executable + test**

```bash
chmod +x web/scripts/build-bundles.sh
cd web && bash scripts/build-bundles.sh v1.0
ls -lh dist-bundles/
```

Expected: 4 zips, each a few MB.

- [ ] **Step 3: Add `dist-bundles/` to `.gitignore`**

Append to repo root `.gitignore`:
```
web/dist-bundles/
web/dist/
web/node_modules/
```

- [ ] **Step 4: Commit**

```bash
git add web/scripts/build-bundles.sh .gitignore
git commit -m "07 Website Phase 8.1 — build-bundles.sh produces 4 platform zips (versioned)"
```

### Task 8.2: GH Release how-to doc

**Files:**
- Create: `web/RELEASE.md`

- [ ] **Step 1: Write doc**

```markdown
# Cutting a release (v1.0+)

1. Build bundles:
   ```
   cd web && bash scripts/build-bundles.sh v1.0
   ```

2. Verify zips locally:
   ```
   ls -lh dist-bundles/
   unzip -l dist-bundles/claude_bundle_v1.0.zip | head
   ```

3. Tag + create GH Release:
   ```
   git tag v1.0
   git push origin v1.0
   gh release create v1.0 \
     --title "v1.0" \
     --notes-file ../ai_platforms/release/v1.0/CHANGELOG.md \
     dist-bundles/*.zip
   ```

4. Verify URLs resolve:
   ```
   curl -I https://github.com/hakupao/sdtm-pedia/releases/download/v1.0/claude_bundle_v1.0.zip
   ```
   Expected: `HTTP/2 302` redirect to S3 download.

5. Update site `web/src/data/downloads.json` if filename or version changes.

## Bumping version

For v1.1, edit `downloads.json` `tag: "v1.1"`, run `build-bundles.sh v1.1`, repeat.
```

- [ ] **Step 2: Commit**

```bash
git add web/RELEASE.md
git commit -m "07 Website Phase 8.2 — RELEASE.md: GH Release cut-a-release runbook"
```

### Task 8.3: Cut the actual v1.0 GH Release

- [ ] **Step 1: Build bundles**

```bash
cd web && bash scripts/build-bundles.sh v1.0
```

- [ ] **Step 2: Tag and release**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
git tag v1.0
git push origin v1.0
gh release create v1.0 \
  --title "v1.0" \
  --notes-file ai_platforms/release/v1.0/CHANGELOG.md \
  web/dist-bundles/*.zip
```

- [ ] **Step 3: Verify URLs**

```bash
for f in claude_bundle_v1.0.zip chatgpt_bundle_v1.0.zip gemini_bundle_v1.0.zip notebooklm_bundle_v1.0.zip; do
  curl -sI "https://github.com/hakupao/sdtm-pedia/releases/download/v1.0/$f" | head -1
done
```

Expected: each returns `HTTP/2 302`.

- [ ] **Step 4: No commit (release is a tag, not a commit)**

---

## Phase 9 — CF Pages Deploy

### Task 9.1: First push smoke

- [ ] **Step 1: Push current branch**

```bash
git push origin main
```

- [ ] **Step 2: Verify GitHub repo updated**

```bash
gh repo view hakupao/sdtm-pedia --web
```

### Task 9.2: Configure CF Pages project

**Files:**
- Create: `web/.cloudflare-pages.md` (config notes for Daisy)

- [ ] **Step 1: Manual CF Pages setup via dashboard**

In Cloudflare dashboard → Pages → Create project → Connect to Git → select `hakupao/sdtm-pedia`. Configure:
- Production branch: `main`
- Build command: `cd web && npm install && npm run build`
- Build output dir: `web/dist`
- Root directory: `/`
- Environment variables: `NODE_VERSION=20`

- [ ] **Step 2: Configure build watch paths**

In CF Pages project → Settings → Builds & deployments → Build watch paths:
- Include: `web/**`, `ai_platforms/release/v1.0/**`

(Excludes `.work/`, `source/`, etc.)

- [ ] **Step 3: Verify first build succeeds**

After CF Pages dashboard shows green check, visit assigned `*.pages.dev` URL. Confirm landing renders.

- [ ] **Step 4: Document**

`web/.cloudflare-pages.md`:
```markdown
# Cloudflare Pages settings (sdtm-pedia)

- Project: sdtm-pedia
- Production branch: main
- Build command: `cd web && npm install && npm run build`
- Output: `web/dist`
- Watch paths: `web/**`, `ai_platforms/release/v1.0/**`
- Node version: 20
- Custom domain: not configured (deferred to v1.1, out of scope for this plan)
```

- [ ] **Step 5: Commit doc**

```bash
git add web/.cloudflare-pages.md
git commit -m "07 Website Phase 9.2 — CF Pages settings doc (build cmd, watch paths, NODE_VERSION)"
```

---

## Phase 10 — QA + Polish

### Task 10.1: Lighthouse audit

- [ ] **Step 1: Run Lighthouse on production URL**

In Chrome DevTools → Lighthouse → Categories: Performance, Accessibility, Best Practices, SEO. Run on `*.pages.dev/zh/`.

Targets (per spec §9):
- Performance ≥ 95
- Accessibility ≥ 95
- Best Practices ≥ 95

If any < 95, identify top failing audit and fix. Common fixes: image dimensions, font preload, color contrast.

- [ ] **Step 2: Capture report**

Save report HTML to `web/qa/lighthouse-zh-landing-2026-04-27.html` (mkdir qa first).

- [ ] **Step 3: Commit if any code changes occurred**

### Task 10.2: Accessibility audit

- [ ] **Step 1: axe DevTools scan**

Install axe DevTools Chrome extension. Run on `/zh/`, `/zh/guide/user-guide`, `/compare`. Fix all "Critical" + "Serious" issues.

- [ ] **Step 2: Keyboard-only navigation**

Tab through landing: TopNav nav items → CTAs → Platform cards (if focusable) → footer. All focusable elements show focus ring.

Add focus-visible styling to `web/src/styles/global.css`:
```css
*:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
```

- [ ] **Step 3: Color contrast verify**

WebAIM contrast checker on:
- `#0a0a0a` on `#f8f5ef` (light body) — must pass AA (4.5:1)
- `#f5f1ea` on `#0d0c0a` (dark body)
- `#1e40af` on `#f8f5ef` (light accent on light bg)
- `#60a5fa` on `#0d0c0a` (dark accent)

If any fails AA, adjust. Most likely: `#1e40af` on `#f8f5ef` is fine (~10:1), `#60a5fa` on `#0d0c0a` is ~7:1 — both should pass.

- [ ] **Step 4: Commit**

```bash
git add web/src/styles/global.css
git commit -m "07 Website Phase 10.2 — a11y pass: focus-visible ring + axe Critical/Serious cleared"
```

### Task 10.3: Cross-browser smoke

- [ ] **Step 1: Test in Chrome, Safari, Firefox at /zh/**

For each browser at `*.pages.dev/zh/`:
- Theme toggle works (cycles 3 states)
- Lang switcher swaps URL + content
- Section animations play
- Downloads links resolve to GH Release
- Cmd+K opens search overlay

- [ ] **Step 2: Document issues found**

Add to `web/qa/cross-browser-2026-04-27.md`. If any fail, fix the smallest offending CSS/JS and re-test.

### Task 10.4: README + handoff

**Files:**
- Create: `web/README.md`

- [ ] **Step 1: Write README**

```markdown
# SDTM Knowledge Website

Public-facing site for `ai_platforms/release/v1.0/`. Deployed: https://sdtm-pedia.pages.dev (custom domain set in v1.1).

## Local dev

```
cd web
npm install
npm run dev
# open http://localhost:4321
```

## Build

```
npm run build
npm run preview
```

## Test

```
npm test           # vitest unit + component
npm run test:e2e   # playwright
```

## Cut a release

See `RELEASE.md`.

## Stack

- Astro 5 + Tailwind v4 + React islands
- Pagefind static search
- CF Pages hosting
- GH Releases for zip downloads

Spec: `../docs/superpowers/specs/2026-04-27-sdtm-release-website-design.md`
Plan: `../docs/superpowers/plans/2026-04-27-sdtm-release-website.md`
```

- [ ] **Step 2: Commit + push**

```bash
git add web/README.md
git commit -m "07 Website Phase 10.4 — web/README.md (dev + build + test + release pointers)"
git push origin main
```

### Task 10.5: Final wrap-up

- [ ] **Step 1: Update project root CLAUDE.md Key Paths**

Add row to root `CLAUDE.md` Key Paths table:
```markdown
| **Phase 7 Website (live)** | **`web/`** + Cloudflare Pages — 三语 landing + docs reader + /compare + GH Release 下载 (`hakupao/sdtm-pedia`) |
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "07 Website live — CLAUDE.md Key Paths 加 web/ + CF Pages 入口 + GH Release 下载"
git push origin main
```

- [ ] **Step 3: Final verify checklist**

Confirm all of these are green:
- [ ] CF Pages production build green
- [ ] `https://sdtm-pedia.pages.dev/zh/` renders
- [ ] All 4 download links resolve to GH Release (302 to S3)
- [ ] `/compare` filter works (type "容量" in zh, table shrinks)
- [ ] Cmd+K search opens + finds known string ("AESER")
- [ ] Theme toggle cycles + persists across reload
- [ ] Lang switcher swaps URL + content
- [ ] Lighthouse all categories ≥ 95
- [ ] axe Critical/Serious = 0

---

## Self-Review Notes (filled by author at write time)

- [x] **Spec coverage:** Walked through spec §1-12 — every section has at least one task. §3 Architecture → Phase 1 + 9. §4 IA → Phase 3 + 4 + 5. §5 Visual → Phase 2 + 4 + 5.2. §6 Landing → Phase 4. §7 Docs reader → Phase 5. §8 Content sources → Phase 0 + 3. §9 Performance → Phase 10.1. §10 Implementation notes → Phase 0 (PLATFORM_COMPARISON, OG, favicon) + Phase 8 (bundle script + GH Release).
- [x] **Placeholder scan:** No "TBD" / "TODO" / "<placeholder>" / "implement later" in any task body. All file paths absolute or repo-relative. All commands have expected output.
- [x] **Type consistency:** `ThemeChoice`, `Lang`, `EffectiveTheme`, `Result` (in SearchOverlay), `Dim` (in CompareFilter) used consistently across files where they appear. `REPO`, `buildReleaseAssetURL` exported from `lib/downloads.ts` and used in Tasks 4.6 + 5.x. `getUIStrings(lang)` signature matches across components.
- [x] **No dangling refs:** Every `import` in code samples points to a file that's created earlier in the plan or in the same task.
- [x] **TDD coverage:** 9 test files specified — theme.test.ts, countup.test.ts, downloads.test.ts, helpers.test.ts (i18n), ThemeToggle.test.tsx, LangSwitcher.test.tsx, CountUp.test.tsx, CompareFilter.test.tsx, SearchOverlay.test.tsx — covering every interactive island and pure-logic util.
- [x] **Reduced-motion guards:** Mentioned in Tasks 2.1 (global.css), 4.3 (CountUp), 4.8 (enter-fade).
- [x] **Lang fallback:** Task 5.3 handles en-only docs (KNOWN_LIMITATIONS, CHANGELOG) generating zh + ja routes from the en source with a banner.
- [x] **CF Pages build path filter:** Task 9.2 step 2 sets watch paths to avoid wasted builds on `.work/` edits.
- [x] **No XSS surface:** SearchOverlay uses `stripHtml()` on Pagefind excerpt and renders as text; no `dangerouslySetInnerHTML`.

---

*End of plan. Total: ~50 distinct tasks across 11 phases. Each phase produces a coherent, testable slice; phases can be executed in order without rework.*
