# Task 6.0 — remark plugin + PLATFORM_COMPARISON slug rename + e2e strict

> **Subagent**: `oh-my-claudecode:executor` (opus)
> **Carryover absorbed**: C-P5-1 (`.md` cross-ref rewrite) + C-P5-2 (PLATFORM_COMPARISON slug rename)
> **Phase 6 entry task** — clears tech debt before adding new compare surface (6.1).
> **Branch**: `main` (HEAD = `3d00a96`); commit at end with the message under §Commit.

## Working directory

`/Users/bojiangzhang/MyProject/SDTM-compare/`

The Astro app lives under `web/`. The release docs live under `ai_platforms/release/v1.0/`. The content collection loader (`web/src/content.config.ts`) globs only TOP-LEVEL `*.md` of `release/v1.0/`, NOT `self_deploy/**`.

## Pre-flight context (already verified by main session, do NOT re-research)

- **Astro version**: 6.1.9 (per `web/package.json`). React 19.2.5. Tailwind 4.0. Vite 7. Node ≥22.12.0.
- **Content collection schema** (`web/src/content.config.ts`): `slug: z.string()` is REQUIRED; `lang: z.enum(['zh','en','ja'])` is OPTIONAL. `generateId` returns `${lang}-${slug}` when langed, bare `${slug}` when lang-neutral.
- **Existing slugs** (post-rename targets):
  - `readme` (langed zh/en/ja)
  - `user-guide` (langed)
  - `glossary` (langed)
  - `platform-comparison` (langed) — **THIS IS THE RENAME** from current `compare`
  - `known-limitations` (en only — fallback handles zh/ja per `[...slug].astro`)
  - `demo-questions` (lang-neutral, no frontmatter `lang`)
  - `changelog` (langed `lang: en`, served via dedicated `[lang]/changelog.astro`)
- **Cross-ref inventory** (web-consumed top-level docs only):
  - ~24 `[X](./FOO.md)` shape across README/USER_GUIDE/GLOSSARY × 3 langs
  - ~6 `[X](./FOO.{zh,en,ja}.md)` shape
  - ~3 `[X](./self_deploy/README.{zh,en,ja}.md)` (out-of-collection, drop link)
  - 1 `[X](./self_deploy/)` directory ref (out-of-collection, drop link)
  - 0 cross-refs in DEMO_QUESTIONS.md (lang-neutral safety net)
  - 0 cross-refs to PLATFORM_COMPARISON anywhere (only the doc itself uses `slug: compare`)
- **Phase 5 e2e skip line** to remove: `web/tests/e2e/smoke.spec.ts:41` — the `if (/\.md(?:#|$)/.test(href)) continue;` guard plus its 3-line comment block above (lines 38-41).

## Files to create/modify (exhaustive — no others)

### 1. CREATE `web/remark-md-link-rewrite.mjs` (project root, sibling of astro.config.mjs)

Spec — implement EXACTLY this algorithm:

```js
// web/remark-md-link-rewrite.mjs
import { visit, SKIP } from 'unist-util-visit';

// Top-level guide-collection slugs (post 6.0 rename). Maps source filename
// stem (UPPER_SNAKE) → web slug (lowercase-hyphenated).
const SLUG_MAP = new Map([
  ['README', 'readme'],
  ['USER_GUIDE', 'user-guide'],
  ['GLOSSARY', 'glossary'],
  ['PLATFORM_COMPARISON', 'platform-comparison'],
  ['KNOWN_LIMITATIONS', 'known-limitations'],
  ['DEMO_QUESTIONS', 'demo-questions'],
  ['CHANGELOG', 'changelog'],
]);

// Strict shape: optional ./ prefix + UPPER_SNAKE name + optional .lang suffix
// + .md + optional #hash. Anything with a / inside the path component (e.g.
// self_deploy/X.md) or .. parent-crawl is out-of-collection.
const SHAPE = /^(?:\.\/)?([A-Z_]+)(?:\.(zh|en|ja))?\.md(#.*)?$/;

export default function remarkMdLinkRewrite() {
  return (tree, file) => {
    const lang = file?.data?.astro?.frontmatter?.lang;

    visit(tree, 'link', (node, index, parent) => {
      const url = node.url;
      if (!url || !/\.md(?:#|$)/.test(url)) return;

      const m = url.match(SHAPE);
      const knownSlug = m && SLUG_MAP.get(m[1]);

      if (!knownSlug) {
        // Out-of-collection (self_deploy/, ../../, unknown stem). Drop the
        // <a> wrapper, keep the inline text children in place.
        if (parent && typeof index === 'number') {
          parent.children.splice(index, 1, ...node.children);
          return [SKIP, index];
        }
        return;
      }

      if (!lang) {
        throw new Error(
          `remark-md-link-rewrite: entry without frontmatter.lang has .md cross-ref to ${url}. ` +
          `Lang-neutral entries cannot rewrite per-lang. Either add lang: to the entry frontmatter ` +
          `or remove the cross-ref.`
        );
      }

      const hash = m[3] || '';
      // CHANGELOG has a dedicated /[lang]/changelog route (D-P5-1); everything
      // else lives under /[lang]/guide/.
      node.url = knownSlug === 'changelog'
        ? `/${lang}/changelog${hash}`
        : `/${lang}/guide/${knownSlug}${hash}`;
    });
  };
}
```

Notes:
- The plugin lives at the project root (`web/remark-md-link-rewrite.mjs`), NOT under `web/src/lib/`, so it's clearly a build-time config artifact.
- Import as `unist-util-visit` — already a transitive dep of `@astrojs/markdown-remark` / `astro` (no `npm install` needed). If the build complains about a missing module, install it as a `web/` devDependency: `cd web && npm install --save-dev unist-util-visit`.
- Lang-neutral safeguard: throws (does NOT silently default to `en`). Fail-loud per project convention (Phase 5 D-P5-2 schema-required-slug parallel).

### 2. MODIFY `web/astro.config.mjs` — register the plugin

Add a `markdown.remarkPlugins` entry. The plugin import path is relative to the config file (`./remark-md-link-rewrite.mjs`).

```js
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import remarkMdLinkRewrite from './remark-md-link-rewrite.mjs';

export default defineConfig({
  site: 'https://sdtm-pedia.pages.dev',
  integrations: [react(), sitemap()],
  vite: { plugins: [tailwindcss()] },
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en', 'ja'],
    routing: { prefixDefaultLocale: true },
  },
  build: { format: 'directory' },
  markdown: {
    remarkPlugins: [remarkMdLinkRewrite],
  },
});
```

### 3. MODIFY 3 PLATFORM_COMPARISON frontmatter slugs (`compare` → `platform-comparison`)

Files (touch ONLY the `slug:` line in YAML frontmatter, leave body untouched):
- `ai_platforms/release/v1.0/PLATFORM_COMPARISON.zh.md` line 3: `slug: compare` → `slug: platform-comparison`
- `ai_platforms/release/v1.0/PLATFORM_COMPARISON.en.md` line 3: same
- `ai_platforms/release/v1.0/PLATFORM_COMPARISON.ja.md` line 3: same

### 4. MODIFY `web/tests/e2e/smoke.spec.ts` — remove `.md` skip (lines 38-41)

Delete this block (the comment + the `if`):

```ts
      // Skip raw .md links (markdown source cross-refs like [Glossary](GLOSSARY.zh.md));
      // these are render-pipeline artifacts, not navigation links. A remark plugin
      // to rewrite them to web routes is Phase 6+ scope.
      if (/\.md(?:#|$)/.test(href)) continue;
```

After removal the test enforces strict resolution of every internal href in `main`/`article` of `/zh/`, `/en/`, `/ja/`, `/zh/guide/user-guide`, `/zh/changelog`. This includes any rewritten `/zh/guide/glossary` etc. routes — the plugin output must produce 200s for all of them.

### 5. NO OTHER FILES — explicitly skip

- DO NOT touch `web/src/pages/[lang]/guide/[...slug].astro` (it consumes whatever slug the collection emits; post-rename `compare` → `platform-comparison` is automatic).
- DO NOT touch `web/src/components/astro/ComparePreviewSection.astro` (that's a Phase 6.1/6.2 file; its CTA `/${lang}/compare` is the page route, not the doc route).
- DO NOT touch `web/src/pages/[lang]/compare.astro` (Phase 5 stub; Phase 6.1 overwrites it).
- DO NOT add the plugin to a `vite.plugins` slot (it's a Markdown remark plugin, only goes in `markdown.remarkPlugins`).

## Verification (must run, in order, all green before reporting back)

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/web

# 1. tsc clean
npx tsc --noEmit
# expect: 0 errors

# 2. unit tests still pass
npm test -- --run
# expect: 29/29 (no new test in 6.0)

# 3. build green
npm run build 2>&1 | tail -20
# expect: 0 errors, dist/zh/guide/platform-comparison/index.html exists,
# dist/zh/guide/glossary/index.html exists, etc. NO dist/zh/guide/compare/
# (renamed away).

# 4. spot-check rewritten HTML — README.zh.md links should be /zh/guide/X form
grep -oE 'href="[^"]*"' dist/zh/guide/readme/index.html | grep -E '/(guide|changelog)/' | sort -u
# expect lines like:
#   href="/zh/guide/user-guide"
#   href="/zh/guide/demo-questions"
#   href="/zh/guide/known-limitations"
#   href="/zh/changelog"
# and ZERO .md endings in any href.

# 5. confirm slug rename emitted under new route
ls dist/zh/guide/platform-comparison/index.html dist/en/guide/platform-comparison/index.html dist/ja/guide/platform-comparison/index.html
# expect all three exist
test ! -d dist/zh/guide/compare && echo "OK: /guide/compare/ NOT emitted (renamed away)"

# 6. e2e strict (now without .md skip)
npm run test:e2e
# expect: 6/6 pass. If a /zh/guide/<slug> 404s, the plugin missed a case
# OR a non-rewritable cross-ref leaked through — investigate; do NOT
# re-add the .md skip to mask the failure.
```

If verification step 6 fails because some link still resolves to a `.md` URL or 404s, the plugin has a gap. Add a console.warn temporarily, rebuild, find the offending source, fix the plugin (do NOT mask via skip).

## Rule B (failure archive)

If you have to abandon an attempt, write a brief failure note to `.work/07_website/phase6/evidence/failures/task_6_0_attempt_<N>.md` with: input/produit/judgment/next-attempt. Do NOT delete failed attempts.

## Evidence to write before completing

Write the report `.work/07_website/phase6/evidence/checkpoints/task_6_0_report.md` with these sections:

1. **Files touched** (exhaustive list with brief diff summary)
2. **Plugin algorithm trace** — for 5 representative cross-refs, show the source href → rewritten href, plus 2 "drop link wrapper" cases. e.g.:
   ```
   README.zh.md L14 [USER_GUIDE.zh.md](./USER_GUIDE.zh.md) → href="/zh/guide/user-guide"
   README.zh.md L17 [CHANGELOG.md](./CHANGELOG.md)         → href="/zh/changelog"
   GLOSSARY.zh.md L68 [`./KNOWN_LIMITATIONS.en.md`](./KNOWN_LIMITATIONS.en.md) → href="/zh/guide/known-limitations"
   USER_GUIDE.zh.md L27 [`../../SMOKE_V4.md`](../../SMOKE_V4.md) → DROPPED (link wrapper removed, text "../../SMOKE_V4.md" preserved)
   README.zh.md L33 [self_deploy/README.zh.md](./self_deploy/README.zh.md) → DROPPED
   ```
3. **Slug rename verification** — confirm `dist/{zh,en,ja}/guide/platform-comparison/index.html` exists and `dist/{zh,en,ja}/guide/compare/` does NOT.
4. **Verification command outputs** — verbatim tail of each of the 6 verify steps above.
5. **e2e link-resolution count** — how many unique URLs the now-strict link test resolved (was N, now N+M after stripping `.md` skip).
6. **Open questions / surprises** — anything that needed a judgment call beyond this brief.

## Commit

```bash
git -c commit.gpgsign=false commit -m "$(cat <<'EOF'
07 Website Phase 6.0 — remark plugin for .md cross-refs + PLATFORM_COMPARISON slug rename + e2e link-resolution strict (C-P5-1 + C-P5-2 absorbed)

- Add web/remark-md-link-rewrite.mjs: visits mdast 'link' nodes, rewrites
  ./FOO[.lang].md(#hash)? → /<entryLang>/guide/<kebab-slug><hash> for top-level
  guide-collection docs. CHANGELOG routes to /<lang>/changelog (D-P5-1
  dedicated route). Out-of-collection refs (self_deploy/, ../../) drop the
  <a> wrapper but keep inline text. Lang-neutral entry with .md cross-ref
  throws (fail-loud parallel to Phase 5 D-P5-2 schema-required-slug).
- Register in web/astro.config.mjs markdown.remarkPlugins.
- Rename PLATFORM_COMPARISON.{zh,en,ja}.md frontmatter slug compare → platform-comparison
  (C-P5-2; clears naming collision with /[lang]/compare page route landing
  in 6.1). Emits /<lang>/guide/platform-comparison/index.html.
- Drop .md skip in web/tests/e2e/smoke.spec.ts link-resolution test (was
  Phase 5 carryover comment lines 38-41); the test now strictly resolves
  all internal hrefs across landing + guide + changelog routes.

Verification: tsc 0 / vitest 29/29 / build green / e2e 6/6 strict / spot-check
rewritten HTML shows /zh/guide/{user-guide,glossary,demo-questions,known-limitations}
and /zh/changelog with zero .md endings.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

After commit, run `git status` to confirm clean tree, then report back.
