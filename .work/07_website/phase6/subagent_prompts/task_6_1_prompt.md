# Task 6.1 — CompareFilter island + overwrite [lang]/compare.astro real page

> **Subagent**: `oh-my-claudecode:executor` (opus)
> **Branch**: `main` (HEAD = `b25b834` post 6.0). Commit at end with the HEREDOC message in §Commit.
> **Scope**: Create the React `CompareFilter` island + 2 vitest, OVERWRITE the Phase 5 `[lang]/compare.astro` placeholder with the real page. Path-based i18n per **plan deviation** (PLAN.md §"⚠️ Plan deviation flag"). DO NOT touch `compare-dimensions.json` (Task 6.2 owns it) — work against the existing 4-dim version.
> **Pre-work assumed in main session and NOT to re-research**: Astro 6.1.9 + React 19.2.5 + vitest 4.1.5 + @testing-library/react 16.3.2 + @testing-library/jest-dom auto-wired via `web/src/test-setup.ts` (`import '@testing-library/jest-dom/vitest'`).

## Working directory

`/Users/bojiangzhang/MyProject/SDTM-compare/`

## Pre-flight context (verified, do NOT redo)

- **`web/src/data/platforms.json`** has 4 entries: `{ key: 'claude'|'chatgpt'|'gemini'|'notebooklm', name: <UPPERCASE>, score, scoreText, strength: { zh, en, ja } }`. Names are `CLAUDE`, `CHATGPT`, `GEMINI`, `NOTEBOOKLM`.
- **`web/src/data/compare-dimensions.json`** currently has 4 dims: `best-at`, `capacity`, `sharing`, `anti-halluc`. Each entry shape: `{ key, label: { zh, en, ja }, values: { claude, chatgpt, gemini, notebooklm }, winners: string[] }`. Task 6.2 expands to 9 dims; 6.1 must work with whatever is there at build time.
- **Existing React test pattern** (e.g. `web/src/components/react/LangSwitcher.test.tsx`) uses explicit imports `import { describe, it, expect } from 'vitest'; import { render, screen } from '@testing-library/react';` — plan template does the same; DO NOT switch to globals.
- **Existing Astro page pattern** for `[lang]/*.astro`: see `web/src/pages/[lang]/changelog.astro` and `web/src/pages/[lang]/compare.astro` (Phase 5 stub). Both: `getStaticPaths()` returns 3 lang params, `Astro.params.lang as Lang`, mount `<TopNav lang={lang} pathname={pathname} />` inside `<BaseLayout title=... lang={lang}>`.
- **`BaseLayout`** does NOT inject TopNav; pages mount it themselves. Pattern: layout wraps html/head/body + theme flash script; page provides nav + main.
- **Lang type** lives in `web/src/i18n/helpers.ts` and is `'zh'|'en'|'ja'`.

## Files to create / overwrite (exhaustive — no others)

### 1. CREATE `web/src/components/react/CompareFilter.tsx`

Implement EXACTLY this (matches plan §6.1 Step 2 verbatim, with one addition: `aria-label` on the search input for a11y):

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
  const filtered = lower
    ? dims.filter((d) => d.label[lang].toLowerCase().includes(lower))
    : dims;

  return (
    <>
      <input
        type="search"
        value={q}
        onChange={(e) => setQ(e.target.value)}
        placeholder="Filter dimensions..."
        aria-label="Filter dimensions"
        className="font-mono text-sm px-3 py-2 border border-rule bg-bg w-64 mb-6"
      />
      <div className="overflow-x-auto">
        <table className="w-full font-serif text-sm border-collapse min-w-[600px]">
          <thead>
            <tr className="border-b border-rule">
              <th className="text-left py-2 px-2 font-mono text-[9px] tracking-wider">DIMENSION</th>
              {platforms.map((p) => (
                <th key={p.key} className="text-left py-2 px-2 font-mono text-[9px] tracking-wider">
                  {p.name}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {filtered.map((d) => (
              <tr key={d.key} className="border-b border-rule">
                <td className="py-2 px-2 font-mono text-[10px] tracking-wider">
                  {d.label[lang]}
                </td>
                {platforms.map((p) => (
                  <td
                    key={p.key}
                    className={`py-2 px-2 ${d.winners.includes(p.key) ? 'text-accent font-bold' : ''}`}
                  >
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

Notes:
- `aria-label="Filter dimensions"` is the ONLY addition over the master plan template — needed because the input has no visible `<label>` and the placeholder doesn't satisfy a11y. The `getByRole('searchbox')` test still works.
- Hardcoded English `"Filter dimensions..."` placeholder is acceptable for 6.1 (matches plan); reviewer 6.3 may flag for v1.1 i18n polish — that is OK, do not preemptively widen scope.

### 2. CREATE `web/src/components/react/CompareFilter.test.tsx`

Implement EXACTLY this (matches plan §6.1 Step 1 verbatim):

```tsx
// web/src/components/react/CompareFilter.test.tsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { CompareFilter } from './CompareFilter';

const dims = [
  {
    key: 'best-at',
    label: { zh: '最强场景', en: 'Best at', ja: '最も得意' },
    values: { claude: 'A', chatgpt: 'B', gemini: 'C', notebooklm: 'D' },
    winners: ['claude'],
  },
  {
    key: 'capacity',
    label: { zh: '容量上限', en: 'Capacity', ja: '容量上限' },
    values: { claude: '1.29M', chatgpt: '20', gemini: '1M', notebooklm: '50' },
    winners: ['claude'],
  },
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

### 3. OVERWRITE `web/src/pages/[lang]/compare.astro`

This file currently exists as the Phase 5 placeholder. **OVERWRITE its full contents** (do NOT create alongside, do NOT use a different filename, do NOT create `web/src/pages/compare.astro` at root — the master plan §6.1 Step 3 specifies root + `?lang=` but PLAN.md §"⚠️ Plan deviation flag" REJECTS this. Follow the plan deviation, not the master plan template).

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import TopNav from '../../components/astro/TopNav.astro';
import { CompareFilter } from '../../components/react/CompareFilter';
import dims from '../../data/compare-dimensions.json';
import { type Lang } from '../../i18n/helpers';

export function getStaticPaths() {
  return [
    { params: { lang: 'zh' } },
    { params: { lang: 'en' } },
    { params: { lang: 'ja' } },
  ];
}

const lang = Astro.params.lang as Lang;
const pathname = Astro.url.pathname;
---
<BaseLayout title="Platform Comparison" lang={lang}>
  <TopNav lang={lang} pathname={pathname} />
  <main class="px-7 py-8 max-w-screen-xl mx-auto">
    <h1 class="font-display text-4xl font-bold mb-2">Multi-dimensional Comparison</h1>
    <p class="font-serif text-ink-mute mb-8">
      Side-by-side across 4 platforms. Filter by dimension keyword.
    </p>
    <CompareFilter client:load dims={dims} lang={lang} />
  </main>
</BaseLayout>
```

Notes:
- Title and prose copy stay English for 6.1 (plan template). i18n of those strings is v1.1 polish — flagged in `<C-P5-L1>`-equivalent carryover. Do NOT add i18n to scope here.
- `client:load` directive is required because state hooks live in the React island; lazier strategies (`client:idle`, `client:visible`) would introduce a paint flash for the input.
- `dims` JSON import is statically bound at build time — Phase 6.2 expanding to 9 dims will be picked up automatically the next build.

## Files NOT to touch

- `web/src/data/compare-dimensions.json` — Task 6.2 owns expansion; do NOT touch.
- `web/src/components/astro/ComparePreviewSection.astro` — Task 6.2 adds `slice(0, 4)`; do NOT touch.
- `web/astro.config.mjs` — already configured in 6.0; do NOT touch.
- `web/src/pages/compare.astro` (root) — DO NOT create; the page lives under `[lang]/`.
- TopNav, LangSwitcher, ThemeToggle, BaseLayout — all reusable as-is.

## Verification (run all in order; ALL must be green before commit)

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/web

# 1. tsc clean (incl. CompareFilter type-check)
npx tsc --noEmit
# expect: 0 errors

# 2. unit + new tests
npm test -- --run
# expect: 31/31 (was 29 + 2 new in CompareFilter.test.tsx)

# 3. build green
npm run build 2>&1 | tail -20
# expect: 0 errors. Verify each lang variant of /compare/ exists:
ls dist/zh/compare/index.html dist/en/compare/index.html dist/ja/compare/index.html

# 4. confirm real page replaced stub
grep -l "PHASE 6 PENDING" dist/zh/compare/index.html && echo "FAIL: stub still present" || echo "OK: stub gone"
grep -c '<table' dist/zh/compare/index.html
# expect: ≥ 1 (the comparison table is server-rendered)
grep -c 'role="searchbox"' dist/zh/compare/index.html
# expect: ≥ 1 (input element with type=search has implicit searchbox role)

# 5. e2e still green (no smoke spec changes; should be 6/6)
npm run test:e2e
# expect: 6/6 PASS. If a stale astro dev process is still bound to :4321 from
# 6.0, kill it first: lsof -ti:4321 | xargs -r kill ; then re-run.
```

If any step fails, do NOT mask the failure (e.g. don't add ts-ignore, don't skip tests). Fix root cause.

## Rule B (failure archive)

If you abandon an attempt, write `.work/07_website/phase6/evidence/failures/task_6_1_attempt_<N>.md` with input/produit/judgment/next-attempt. Do NOT delete failed attempts.

## Evidence to write before committing

`.work/07_website/phase6/evidence/checkpoints/task_6_1_report.md` with sections:

1. **Files touched** (exhaustive table: filename / change-type / lines-delta).
2. **Plan-deviation confirmation** — quote the file body of the new `[lang]/compare.astro` showing `Astro.params.lang` (NOT `?lang=`) + `getStaticPaths()` returning 3 langs. This is the artifact for "plan deviation followed".
3. **vitest output** — verbatim tail showing 31/31 with 2 new `<CompareFilter>` tests.
4. **Build output** — confirm `dist/{zh,en,ja}/compare/index.html` exist.
5. **Stub-replacement check** — confirm "PHASE 6 PENDING" text is gone from new HTML; confirm `<table>` and `role="searchbox"` present.
6. **e2e** — verbatim 6/6 tail.
7. **Open questions / surprises** — anything beyond the brief that needed judgment.

## Commit

```bash
git -c commit.gpgsign=false commit -m "$(cat <<'EOF'
07 Website Phase 6.1 — CompareFilter React island + overwrite [lang]/compare.astro real page (path-based i18n per plan deviation)

- Add web/src/components/react/CompareFilter.tsx: client:load island, useState
  search filter over dims by label[lang]. Implements plan §6.1 Step 2 verbatim
  + a11y aria-label on the searchbox input.
- Add web/src/components/react/CompareFilter.test.tsx: 2 vitest covering
  default-render and lowercase-substring-filter, identical to plan §6.1 Step 1.
- Overwrite web/src/pages/[lang]/compare.astro (was Phase 5 stub): real page
  mounting BaseLayout + TopNav + CompareFilter island. Uses Astro.params.lang
  (NOT ?lang=) per PLAN.md deviation flag — plan §6.1 Step 3 root +
  searchParams was rejected because (1) Phase 4 ComparePreviewSection CTA
  links to /<lang>/compare, (2) Phase 5 stub already at [lang]/compare.astro,
  (3) project-wide path-based i18n (prefixDefaultLocale: true), (4) verbatim
  plan would have broken the existing CTA + forced a redirect or dead link.

Verification: tsc 0 / vitest 31/31 (29 + 2) / build 33+ pages / dist/{zh,en,ja}/compare/index.html
real page (no PHASE 6 PENDING marker, table + searchbox present) / e2e 6/6.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Stage with explicit paths only (do NOT use `-A` or `.`):

```bash
git add web/src/components/react/CompareFilter.tsx \
        web/src/components/react/CompareFilter.test.tsx \
        web/src/pages/[lang]/compare.astro \
        .work/07_website/phase6/evidence/checkpoints/task_6_1_report.md
```

The 5 pre-existing `.work/06_deep_verification/multi_session/batch_*_kickoff.md` deletions and any other unstaged files MUST NOT be staged.

After commit, run `git status` to confirm only the 5 deletions + 4 new round-11 untracked + `.work/07_website/phase6/subagent_prompts/` remain unstaged. Report back: (a) commit SHA, (b) one-line success/failure, (c) vitest count delta (was 29, now 31), (d) any judgment calls.
