# SDTM Pedia — website

Static documentation site for the SDTM Pedia knowledge base, deployed to
Cloudflare Pages at `https://sdtm-pedia.pages.dev/`. Serves the multi-platform
release bundle (Claude / ChatGPT / Gemini / NotebookLM) plus user guide,
glossary, multi-dimensional comparison, and changelog across `zh / en / ja`.

## Stack

- [Astro 6](https://astro.build/) — static-site generator with i18n routing
- [React 19](https://react.dev/) — interactive islands (`CompareFilter`)
- [Tailwind 4](https://tailwindcss.com/) — design tokens via Vite plugin
- [Vitest 4](https://vitest.dev/) + [Testing Library](https://testing-library.com/) — unit tests
- [Playwright](https://playwright.dev/) — e2e smoke tests
- [Pagefind](https://pagefind.app/) — static search index built post-build

## Scripts

```bash
cd web
npm install            # one-time
npm run dev            # local dev at http://localhost:4321
npm run build          # incremental build → dist/ (uses Astro content cache)
npm run build:fresh    # clear .astro caches first, then build (use after editing remark plugins or markdown processors)
npm run preview        # serve dist/ locally
npm test               # vitest (unit)
npm run test:e2e       # playwright (e2e; runs against dev server)
```

## Architecture

- **Routes**: path-based i18n (`prefixDefaultLocale: true`). Every page lives at `/[lang]/...` (no root-level `?lang=` query). Three langs: `zh` (default) / `en` / `ja`.
- **Content collection**: markdown sources in `../ai_platforms/release/v1.0/*.md` (with optional `.{lang}.md` suffix), picked up by `web/src/content.config.ts`. Catchall route `[lang]/guide/[...slug]/` emits one HTML per `slug:` frontmatter. Slug `changelog` is excluded from the catchall (owned by dedicated `[lang]/changelog.astro`).
- **Markdown cross-link rewrite**: `remark-md-link-rewrite.mjs` transforms `[X](FOO.zh.md)` → `/zh/guide/foo` for top-level guide-collection refs. Out-of-collection relative paths drop the `<a>` wrapper. Lang-neutral entries with `.md` cross-refs throw at build time (intentional fail-loud).
- **i18n keys**: single source of truth at `src/i18n/ui.zh.json`; `en` + `ja` mirrors enforced by `helpers.test.ts` key-parity tests.
- **Layouts**: `BaseLayout.astro` (head + canonical + theme-flash guard) → `LandingLayout.astro` / `DocsLayout.astro`.

## Tribal knowledge

A few pieces of project-specific lore that have bitten before. Read once before contributing.

### Astro content cache after editing markdown processors

When you edit `remark-md-link-rewrite.mjs` (or anything in the markdown processing pipeline), the Astro content cache (`.astro/`, `node_modules/.astro/data-store.json`) holds parsed AST from the previous run. A plain `npm run build` may silently produce unchanged output despite the new plugin code being correct.

Use `npm run build:fresh` (clears `.astro/`, `node_modules/.astro/`, `dist/` first). This was the root cause of a wasted debugging cycle in Phase 6.4. Documented as Phase 6 D-P6-7 / C-P6-8.

### Playwright dev-server reuse foot-gun

`playwright.config.ts` has `reuseExistingServer: true`, which speeds up local iteration but means a stale `astro dev` from a previous session can serve outdated bundles to e2e. Symptom: e2e fails with assertions matching pre-edit code.

Fix: `lsof -ti:4321 | xargs -r kill` before `npm run test:e2e`. Logged as C-P6-4 (deferred).

### Lang-neutral entries

Most release docs are `*.{zh,en,ja}.md` (one variant per lang). A few (e.g. `DEMO_QUESTIONS.md`) are lang-neutral — they share content across all 3 langs. For those:

- Frontmatter must NOT set `lang:`
- They must NOT contain `[X](FOO.md)` cross-refs (the remark plugin throws — by design, since the rewrite has no `currentLang` to target)

If you need a lang-neutral page to link out, use absolute URLs (`https://...`) or drop the link.

### Adding a new doc

1. Drop `MY_DOC.{zh,en,ja}.md` into `ai_platforms/release/v1.0/` (or `MY_DOC.md` for lang-neutral)
2. Set `slug: my-doc` in frontmatter (lowercase, hyphenated)
3. Build — `[lang]/guide/my-doc/` is emitted automatically by the catchall route
4. Cross-link from other docs as `[X](MY_DOC.zh.md)` / `[X](MY_DOC.md)` — the remark plugin rewrites to `/[lang]/guide/my-doc`

### Soft-404 on unmatched `/[lang]/*` paths

Astro 6 + `prefixDefaultLocale: true` returns **200 + `<meta http-equiv="refresh">`** for any `/[lang]/<unknown>/` path (rather than a hard 404). Mitigated by `<meta name="robots" content="noindex">` so search engines don't index. Logged as C-P7-1; accepted as Astro design intent.

## Hosting

Cloudflare Pages auto-deploys from `main`. Build command: `npm run build` (CF Pages picks up `web/` as project root). No `_redirects` / `_routes.json` overrides — CF Pages serves `dist/` directly + auto-308 redirects no-trailing-slash to with-trailing-slash to match Astro's `build.format: 'directory'`.

For local CF preview (rare; usually unnecessary): `wrangler pages dev dist`.

## Cutting a release bundle

See `RELEASE.md` (in this directory) — covers `scripts/build-bundles.sh`, GH release tagging, and the `PUBLIC_RELEASE_PUBLISHED` feature flag.

## Phase trace

Tier 3 plan-trace artifacts for each phase live at `../.work/07_website/phase{N}/` with `PLAN.md` + `_progress.json` + per-task evidence + reviewer reports. Read these for context on past architectural decisions (e.g. Phase 6 D-P6-* decisions for the comparison page, Phase 7 D-P7-* decisions for release-readiness chrome).
