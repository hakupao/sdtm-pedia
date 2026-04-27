# SDTM Release Website — Design Spec

> **Status**: Draft v1.0
> **Date**: 2026-04-27
> **Author**: Daisy (with brainstorming via Claude Code superpowers)
> **Scope**: Public-facing website for `ai_platforms/release/v1.0/` content, deployed on Cloudflare Pages from public GitHub repo (`hakupao/sdtm-pedia`), with downloads served via GitHub Releases.

---

## 1. Goals

Convert the v1.0 internal release (12 top-level docs in zh/en/ja + self-deploy bundle materials, currently at `ai_platforms/release/v1.0/`) into a public-facing website that:

1. Lets colleagues without markdown readers consume the content comfortably in a browser.
2. Provides per-platform `.zip` downloads of the deploy bundles.
3. Looks distinctly designed (not a generic doc-site template) while keeping the sober, clinical tone appropriate to SDTM context.
4. Supports trilingual switching (zh / en / ja).
5. Supports light / dark theming.
6. Auto-deploys via GitHub push → Cloudflare Pages, with single source of truth in the existing `SDTM-compare` repo.

## 2. Non-goals (v1.0)

- Browser-language auto-detection (deferred to v2).
- User accounts, login, or any per-user state.
- Server-side rendering, databases, or APIs (fully static).
- Heavy cinematic animation (Apple WWDC tier).
- Comment threads or in-page feedback forms (existing email-Daisy channel suffices).
- Analytics / tracking (internal release, not needed).
- Search rankings / SEO optimization (internal-leaning audience, organic discovery is not a goal).
- Markdown editing in-browser.

## 3. Architecture

### 3.1 Stack

| Layer | Choice | Rationale |
|---|---|---|
| Framework | **Astro** | MD-first, content collections for trilingual routing, zero default JS, islands for interactive bits, static output |
| Styling | **Tailwind CSS v4 + CSS variables** | Tailwind for utility velocity; CSS variables drive theme switching (light/dark) |
| Interactive bits | **React islands** | Theme toggle, language switcher, multi-dim comparison filter, count-up numbers |
| Search | **Pagefind** | Build-time indexed full-text search, static, supports CJK |
| Markdown | **rehype + remark** plugins | Code highlight, tables, footnotes, anchor IDs |
| Hosting | **Cloudflare Pages** | Free tier, zero-config GitHub deploy, global CDN, build path filtering |
| Downloads | **GitHub Releases** | Zero file hosting on CF; permanent versioned URLs; release-tag = canonical bundle set |
| Repo | Existing public `hakupao/sdtm-pedia` (local checkout dir: `SDTM-compare/`) | Single source of truth — content `.md` and site source live together |

### 3.2 Repo layout

```
SDTM-compare/
├── ai_platforms/release/v1.0/   ← existing content (untouched, source of truth)
│   ├── *.md (13 docs × 3 langs)
│   ├── PLATFORM_COMPARISON.md   ← NEW (per §6 implementation note)
│   └── self_deploy/             ← bundle source for zip packaging
├── web/                         ← NEW Astro project root
│   ├── astro.config.mjs
│   ├── src/
│   │   ├── content/             ← Astro content collections, pulls from ../ai_platforms/release/v1.0
│   │   ├── pages/[lang]/...     ← localized routes
│   │   ├── components/          ← Hero, PlatformCards, DemoCarousel, DownloadGrid, etc.
│   │   ├── layouts/             ← LandingLayout, DocsLayout
│   │   └── styles/              ← global.css with theme variables
│   ├── public/                  ← static assets (favicon, og image)
│   └── package.json
└── (rest of project)
```

CF Pages build root = `web/`, build command = `npm run build`, output = `web/dist/`.

### 3.3 Build path filtering

Cloudflare Pages build trigger configured to only re-build when changes occur in:
- `ai_platforms/release/v1.0/**`
- `web/**`

Edits to `.work/`, `source/`, etc. do not waste build minutes.

## 4. Information Architecture

### 4.1 URL structure

```
/                         → 302 redirect → /zh/
/zh/                      → Chinese landing (default)
/en/                      → English landing
/ja/                      → Japanese landing
/{lang}/guide/            → docs reader entry, redirects to /guide/user-guide
/{lang}/guide/user-guide  → USER_GUIDE
/{lang}/guide/demo        → DEMO_QUESTIONS
/{lang}/guide/glossary    → GLOSSARY
/{lang}/guide/limitations → KNOWN_LIMITATIONS (en-only originally; zh/ja stub-redirect to en for v1)
/{lang}/guide/deploy      → self_deploy/README + per-platform tutorials
/{lang}/changelog         → CHANGELOG (single page; en-only originally; zh/ja stub-redirect)
/compare                  → multi-dim platform comparison page (lang-agnostic table, labels per active lang)
```

### 4.2 Language switching

- Default: zh.
- Top-right of every page: `EN / 中 / 日` switcher; clicking replaces `lang` URL segment, preserves rest of path.
- For pages without an exact translation (e.g., `KNOWN_LIMITATIONS.en.md` has no `.zh.md`), render the English source with a small banner "Available in English only".
- localStorage remembers user's last-chosen lang; if stored lang ≠ URL lang on next visit, show a soft hint banner offering to switch (do not auto-redirect).

### 4.3 Theme switching

- Default: respect `prefers-color-scheme`.
- Top-right toggle (sun/moon icon) overrides; choice stored in localStorage `theme=light|dark|system`.
- Theme switch transitions all colors via 250ms CSS-variable interpolation (no abrupt flash).

## 5. Visual System

### 5.1 Direction

**B+C fusion**: editorial-serif spine (Playfair / Source Serif headlines, generous whitespace, italic emphasis) + engineering-mono details (JetBrains Mono labels, section numbers, metadata, button text). Heavy black borders / rules retained as the structural rhythm of the system (line treatment **option A**, locked after considering hairline / no-rule alternatives).

### 5.2 Tokens

```css
/* Light */
--bg:           #f8f5ef;   /* warm off-white */
--bg-alt:       #ffffff;   /* card surface */
--ink:          #0a0a0a;   /* near-black text */
--ink-mute:     #555555;
--ink-faint:    rgba(10, 10, 10, 0.4);
--accent:       #1e40af;   /* cobalt blue */
--rule:         #1a1a1a;   /* heavy rule */

/* Dark */
--bg:           #0d0c0a;   /* warm near-black */
--bg-alt:       #1a1815;
--ink:          #f5f1ea;   /* warm off-white */
--ink-mute:     #b8b3a8;
--ink-faint:    rgba(245, 241, 234, 0.4);
--accent:       #60a5fa;   /* brighter cobalt */
--rule:         #f5f1ea;   /* inverted */
```

### 5.3 Typography

| Role | Font | Notes |
|---|---|---|
| Display headline | **Playfair Display** (700, italic for emphasis) | 36-64px, letter-spacing -0.025em, line-height 1.05 |
| Body serif | **Source Serif Pro** (400/500) | 14-16px body, 1.55 line-height |
| Mono labels / code / metadata | **JetBrains Mono** (500/600/700) | 9-12px, letter-spacing 0.08-0.2em, often UPPERCASE |
| UI sans (fallback) | system `-apple-system, Inter, sans-serif` | rare — most UI uses serif or mono |

Self-host via `@fontsource/*` packages (no Google Fonts CDN, GDPR-friendly + faster).

### 5.4 Motion

**Principle**: 克制, serves SDTM's clinical seriousness. No spring bounce, no playful overshoot, no exuberant easing.

| Trigger | Effect | Duration | Easing |
|---|---|---|---|
| Section enter viewport | opacity 0→1 + translate-y 6px→0 | 400ms | ease-out |
| Number reveal (§02 scores) | count-up 0 → target | 600ms | ease-out |
| Theme toggle | CSS variable interp | 250ms | ease-in-out |
| Lang toggle | text cross-fade | 200ms | ease-in-out |
| Link hover | underline expand left→right | 200ms | ease-out |
| Button hover | bg color shift | 150ms | ease-out |

All animations gated on `@media (prefers-reduced-motion: no-preference)`. With reduced motion preferred, transitions become instant.

### 5.5 Line treatment

- Heavy 1px rules (`--rule`) between landing sections.
- Heavy 1px borders on all platform / download cards.
- Section labels: mono `§ NN / NAME` prefix in `--accent`, followed by 1px rule extending right.
- Footer: full-width black band (`--ink` background, `--bg` text).

## 6. Landing Page Components

Six sections, in order:

### §01 — Hero
- Top nav: brand mark `SDTM/KB · VOL.01 · 2026` (mono) | nav links `GUIDE PLATFORMS DEMO DOWNLOAD` | language switcher | theme toggle.
- Section label: `— 04 INTERNAL RELEASE` (mono, accent).
- Headline (Playfair, 48-64px): "SDTM Knowledge, *across four* AI platforms." (italic on "across four").
- Sub-deck (Source Serif, 14-16px, max-width 480px): "A curated reference of CDISC SDTMIG v3.4 — mapped, deployed, evaluated. One question, one minute, one cited answer."
- CTA row: primary `READ THE GUIDE →` (filled `--ink` button) | secondary `DOWNLOAD .ZIP` (outline) | tertiary `→ GITHUB` (text-only).
- Status strip (mono, bottom): `● LIVE · CLAUDE 17/17 · GPT 16.5 · GEMINI 16 · NBLM 15`.

### §02 — Four Platforms
- Section label `§ 02 / FOUR PLATFORMS`.
- Subhead (Playfair italic): "Four deployments, *each with* a temperament."
- 4-column card grid. Each card: mono platform name (CLAUDE / CHATGPT / GEMINI / NOTEBOOKLM), Playfair giant score (17 / 16.5 / 16 / 15) with `/17` muted, Source Serif one-liner strength.
- Score numbers count-up on enter viewport.

### §03 — Multi-dimensional Comparison Preview
- Section label `§ 03 / WHICH ONE?`.
- Subhead (Playfair italic): "Pick by what you're *about to do*."
- Preview table: 3-4 rows × 4 platforms (e.g., Best at / Sharing / Capacity / Anti-hallucination), with cobalt highlight on best-fit cell per row.
- CTA: `→ FULL COMPARISON` link to `/compare` page (which renders all dimensions from `PLATFORM_COMPARISON.md`).
- The full `/compare` page: full table from `release/v1.0/PLATFORM_COMPARISON.md` content collection, sortable / filterable by dimension.

### §04 — Demo Questions
- Section label `§ 04 / DEMO QUESTIONS`.
- Subhead: "Try these *three*. The full ten are in the guide."
- 3 cards (D0 warmup / D1 new domain / D5 premise probe), each: mono code (D0/D1/D5) + Source Serif question + small italic muted hint where relevant.
- CTA: `→ ALL TEN QUESTIONS` link to `/{lang}/guide/demo`.

### §05 — Downloads
- Section label `§ 05 / DOWNLOADS`.
- Subhead: "Self-deploy *your own*."
- 2×2 grid (or 1×4 on mobile): one card per platform zip with mono filename + file count + size + cobalt `↓` icon. Click → direct GH Release asset URL.
- Sub-CTA: `→ ALL ASSETS ON GITHUB RELEASES`.

### §06 — Footer
- Full-width `--ink` background band.
- Left: `SDTM/KB · v1.0 · 2026` (mono) + `Maintained by Daisy. Internal release.` (Source Serif italic).
- Right: nav links `CHANGELOG GUIDE GITHUB` (mono, uppercase).

## 7. Docs Reader (`/{lang}/guide/...`)

### 7.1 Layout (desktop)

```
┌─────────────────────────────────────────────────────────────┐
│ Top nav (breadcrumbs · lang switcher · theme toggle)        │
├──────────────┬──────────────────────────────┬───────────────┤
│              │                              │               │
│  Sidebar     │  Content (Source Serif)      │  TOC (right)  │
│  (doc list)  │  Markdown body               │  H2 + H3      │
│              │                              │               │
├──────────────┴──────────────────────────────┴───────────────┤
│ Prev / Next nav (within same lang)                          │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Sidebar

Document index for current lang, current doc highlighted, expanded sections show H2 anchors. Width 240px desktop / collapses to top drawer on mobile.

### 7.3 Content area

- Max width 720px (reading-optimized).
- Body in Source Serif Pro, 16px, line-height 1.7.
- H1-H4 in Playfair (with H1 italic / H2-H4 standard), heavy black underline rule under H2.
- Code blocks: monospace, `--bg-alt` surface, 1px black border.
- Tables: borders all sides + headers `--ink` background.
- Inline `code`: mono, light `--bg-alt` background, 0 border.
- Anchor links auto-generated for H2/H3.

### 7.4 TOC (right column)

Sticky scroll-spy; current visible section highlighted with cobalt vertical bar. Hidden on mobile/tablet.

### 7.5 Prev / Next

Footer of each doc shows previous and next document in the canonical order (USER_GUIDE → DEMO → GLOSSARY → LIMITATIONS → DEPLOY → CHANGELOG). Adjacent only within same lang.

### 7.6 Search

Pagefind: build-time indexer crawls all rendered HTML, generates static index at `web/dist/pagefind/`. Frontend opens `Cmd+K` overlay; results show doc title + matched snippet + lang badge. Index built per-lang (queries scoped to current lang by default, with toggle to search all langs).

## 8. Content Sources & Data Flow

### 8.1 Sources of truth

| Content | Lives in | Used by |
|---|---|---|
| Landing copy (Hero / labels / CTAs) | `web/src/content/landing/{lang}.md` | Landing pages |
| Platform metadata (scores, strengths, capacity) | `web/src/data/platforms.json` | §02, §03, /compare |
| `PLATFORM_COMPARISON.md` | `ai_platforms/release/v1.0/PLATFORM_COMPARISON.{lang}.md` (NEW, build-time created) | §03 preview, /compare full |
| Demo questions metadata | `web/src/data/demos.json` | §04, /guide/demo |
| Downloads metadata (filename, size, count, GH URL) | `web/src/data/downloads.json` | §05 |
| User guide / Glossary / Limitations / Deploy / Changelog | `ai_platforms/release/v1.0/*.md` | docs reader |

### 8.2 Astro content collections

`web/src/content/config.ts` registers a `guide` collection pointing at `../../ai_platforms/release/v1.0/` glob. Frontmatter convention: `lang: zh|en|ja`, `slug: user-guide|demo|...`, `order: N`.

### 8.3 Build flow

1. Developer commits `.md` change in `ai_platforms/release/v1.0/`.
2. CF Pages build trigger fires (path filter matches).
3. `npm install` (cached).
4. `astro build`:
   - Reads content collection from `release/v1.0/`.
   - Renders pages per lang per slug.
   - Pagefind post-build indexes the `dist/` HTML.
5. CF Pages serves `web/dist/` globally.

### 8.4 Downloads pipeline

- Local script `web/scripts/build-bundles.sh` produces 4 zips from `ai_platforms/release/v1.0/self_deploy/{platform}/`, named `{platform}_bundle_v{version}.zip`.
- On release: `gh release create v1.0 --title "v1.0" --notes-file CHANGELOG.md *.zip`.
- `web/src/data/downloads.json` references `https://github.com/hakupao/sdtm-pedia/releases/download/v1.0/{filename}` for each zip.
- Zips are NOT committed to repo; they live only on GH Release.

## 9. Performance Budget

| Metric | Target | Why |
|---|---|---|
| Lighthouse Performance | ≥ 95 | Static site, no excuse |
| First Contentful Paint | < 1.0s on 4G | Static + CDN-edge |
| Total JS shipped (landing) | < 30kb gzipped | Astro islands keep this small |
| Total JS shipped (docs reader) | < 80kb gzipped | + Pagefind |
| Image weight (per page) | < 100kb | Hero is type-driven, no large imagery |
| Web fonts | self-hosted, 4 weights × 3 families = 12 files, subset to Latin + Common-CJK | Avoid Google Fonts FOIT |

## 10. Implementation Notes (for planning stage)

These are explicit content/asset items the implementation plan must address:

1. **Create `release/v1.0/PLATFORM_COMPARISON.md` (zh/en/ja)** — multi-dimensional comparison table content. Dimensions to confirm during planning: 17-question score / capacity ceiling / sharing model / subscription tier required / internet capability / anti-hallucination posture / file count limit / best-at / worst-at scenario.
2. **OG image / favicon** — design or commission a single sigil that works at 16×16 favicon and 1200×630 og:image. Editorial mark in B+C style (Playfair monogram on cobalt or off-white).
3. **Self-host fonts** — install `@fontsource/playfair-display`, `@fontsource/source-serif-pro`, `@fontsource/jetbrains-mono`; subset to needed weights only.
4. **Bundle build script** — `web/scripts/build-bundles.sh` zips `release/v1.0/self_deploy/{claude,chatgpt,gemini,notebooklm}/` into 4 versioned `.zip`s.
5. **GH Release workflow** — document the `gh release create` invocation; consider GitHub Action that auto-creates release + uploads zips on tag push (post-v1.0 polish).

## 11. Open Questions (defer to v1.1)

- Browser-language auto-detection: track usage data first, decide whether worth adding.
- Versioning strategy for older releases (e.g., v0.9 archive viewer): can be a `/v/<version>` namespace later.
- RSS / sitemap: trivial to add but not in v1.0 scope.
- Analytics: if added later, Plausible (privacy-friendly) preferred over GA.

## 12. Decision Log

Brainstorming convergence (2026-04-27):

| # | Decision | Rationale |
|---|---|---|
| 1 | Astro over Next.js | Static content + light interactivity, smaller JS, native i18n via content collections |
| 2 | Single repo (SDTM-compare) over separate site repo | Avoids content drift; CF supports private repos for build (n/a since this is public) |
| 3 | GitHub Releases over R2/CF Pages for zip hosting | Versioned semantics, zero ops, free, ~5MB×4 well under any limit |
| 4 | Landing + Docs Reader (option B) over single-page (A) or flat sub-pages (C) | Two spaces, two purposes — landing for "酷", docs for readability |
| 5 | Visual mood = B+C fusion over A (dark glass) or D (soft pastel) | A and D read AI-generic; B+C is editorial-with-engineering, designer-recognizable |
| 6 | Heavy borders (line treatment A) over hairline (B), color-block (C), big-numeral ritual (D) | User direct preference after seeing alternatives |
| 7 | Cobalt accent `#1e40af` over crimson / orange / no-accent | Crimson reads "error" in clinical context; cobalt = trust + clinical |
| 8 | Motion = Moderate but 克制 | Serves SDTM's medical seriousness; no bounce |
| 9 | zh default lang | Internal company use, primary audience is Chinese-speaking |
| 10 | 6 landing sections in fixed order | Density matched to attention curve: hook → proof → decision → demo → action → footer |

---

*End of design spec. Next stage: writing-plans skill produces an implementation plan from this document.*
