# Phase 6 — End-of-Phase Reviewer Report (gate, Task 6.3)

> **Reviewer**: `oh-my-claudecode:critic` (Opus, READ-ONLY)
> **Rule D isolation**: cross-family from `pr-review-toolkit` (×4 Phases 1-3.6+4) AND `feature-dev` (×1 Phase 5). 6.3 = first-burn `oh-my-claudecode` family on the website lane (critic-class, deep adversarial framing).
> **Branch / commit range**: `main` `b25b834..362b401` (3 commits in scope; intervening `72ef5a9` deep-verification cleanup excluded).
> **Date**: 2026-04-28
> **Mode escalation**: started THOROUGH; escalated to ADVERSARIAL after 3 confirmed CRITICAL/HIGH findings + a systemic dual-route SEO pattern.

---

## Verdict

**CONDITIONAL_PASS** — H=2 / M=5 / L=4. Two HIGH findings (H1 dual-route SEO duplicate content; H2 raw `./self_deploy/` dead links rendered on `<lang>/guide/readme` for all 3 langs) reach end-users / search engines, but neither blocks Phase 7 starting (data layer infrastructure is sound; remark plugin behaves correctly per its written contract). Both should be remediated in a Phase 6.4 follow-up commit before the public release lifecycle that the website serves enters wider distribution.

**Rationale (one line)**: Infrastructure (remark plugin, React island, slug rename, e2e strict) is well-engineered and the test suite is meaningful, but Phase 6 left two scope-edge "build-green-but-data-broken" leaks (H1 + H2) plus the same hardcoded-English chrome on `/compare` that Phase 5 G-P5-2 lesson would have caught had its successor been written.

---

## Pre-commitment Predictions vs. Actuals

| Predicted | Actual |
|---|---|
| SHAPE regex too narrow (won't match absolute paths / lower-case stems) | NOT FOUND — every cross-ref in the inventory matches; lower-case stems would also be out-of-collection (correct drop) |
| `./self_deploy/` directory ref dead link surfaces in `dist/zh/guide/readme/` | **CONFIRMED — H2** ; rendered as `<a href="./self_deploy/">` on all 3 langs at `/<lang>/guide/readme/` line 25 |
| Hardcoded English chrome on `/compare` violates per-lang UX | **CONFIRMED — M2** for all 3 langs |
| New 5 dim values may drift from source PLATFORM_COMPARISON.md | NOT FOUND — spot-check 3 dims (subscription / internet / score) all match source values |
| `/changelog` AND `/guide/changelog` BOTH emit | **CONFIRMED — H1** ; both routes emit duplicate content + both appear in sitemap-0.xml + neither has `<link rel="canonical">` pointing to the other |

3/5 predictions hit. The two misses (regex / drift) are themselves signal that the author worked carefully on those dimensions.

---

## Findings

### H1 — Dual-route SEO duplicate content for changelog (D2 + D5)

**Severity**: HIGH (CRITICAL post-discovery; downgraded by Realist Check — see Verdict Justification)
**Confidence**: HIGH
**Dimension**: D2 (slug rename atomicity) + D2-adjacent (route emission rules)

The changelog entry has frontmatter `slug: changelog`. After the remark plugin in Phase 6.0:
- The dedicated route `/<lang>/changelog/` is emitted by `web/src/pages/[lang]/changelog.astro` (Phase 5 D-P5-1).
- The catchall route `/<lang>/guide/changelog/` is ALSO emitted by `web/src/pages/[lang]/guide/[...slug].astro` because the catchall's `getStaticPaths()` enumerates ALL `guide` collection entries by slug — and `slug: changelog` is in that collection.

**Evidence** (`web/dist/sitemap-0.xml`):
```
https://sdtm-pedia.pages.dev/zh/changelog/
https://sdtm-pedia.pages.dev/zh/guide/changelog/
https://sdtm-pedia.pages.dev/en/changelog/
https://sdtm-pedia.pages.dev/en/guide/changelog/
https://sdtm-pedia.pages.dev/ja/changelog/
https://sdtm-pedia.pages.dev/ja/guide/changelog/
```
Both URLs in the sitemap. `diff dist/zh/changelog/index.html dist/zh/guide/changelog/index.html` shows the body content (h1, paragraphs, table) is **identical**; only the LangSwitcher pathname (`/zh/changelog/` vs `/zh/guide/changelog/`) and the navigation context (TopNav vs DocsLayout) differ. Neither emits `<link rel="canonical">`.

The remark plugin always rewrites `[...](./CHANGELOG.md)` to `/<lang>/changelog` (the dedicated route per D-P5-1). Good — but:
- The DocsSidebar on `/<lang>/guide/changelog/` does NOT show changelog as the active item (the entry has `lang: 'en'` and DocsSidebar filters for matching-lang; the doc page is reachable but invisible in nav).
- Footer / TopNav links (the dedicated route) and the catchall enumeration (the doc route) disagree about which is canonical.
- For SEO this is exactly the duplicate-content pattern Google penalizes.

**Why this matters**: search engines see two URLs returning the same body and either consolidate (often picks the wrong one) or splits ranking signal between them. Internal link signal is split: `/zh/changelog` from TopNav + `/zh/guide/changelog` from CompareFilter-adjacent docs nav.

**Realist Check downgrade rationale**: not a CRITICAL because (a) site is internal-company-distribution today (CHANGELOG L25 in the project root says "公司发布版"), so SEO impact is low pre-public-release; (b) easily fixed by either excluding `slug:'changelog'` from the catchall `getStaticPaths()` or by adding `<link rel="canonical" href="/<lang>/changelog">` to the catchall-rendered version. **Mitigated by**: small audience, easy rollback, existing dedicated-route is the intended canonical.

**Suggested fix** (Phase 6.4 candidate, blocking before public release):
1. In `web/src/pages/[lang]/guide/[...slug].astro` `getStaticPaths()`, skip the entry when `doc.data.slug === 'changelog'`. The dedicated route owns it.
2. OR add `<link rel="canonical" href="/<lang>/changelog">` to the catchall-rendered changelog, but option 1 is cleaner (no dead `dist/<lang>/guide/changelog/` directory tree).
3. After fix, re-verify `dist/<lang>/guide/changelog/` does not exist and sitemap-0.xml no longer lists it.

---

### H2 — `./self_deploy/` directory link rendered as a relative dead link on `/<lang>/guide/readme` for all 3 langs (D1 + D5)

**Severity**: HIGH
**Confidence**: HIGH
**Dimension**: D1 (remark plugin scope) + D5 (e2e coverage)

Confirmed Task 6.0 evidence report's open question #2. The remark plugin algorithm guards on `if (!url || !/\.md(?:#|$)/.test(url)) return;` — so `[self_deploy/](./self_deploy/)` (line 25 of README.zh/en/ja.md) does NOT enter the rewrite logic and is rendered as a literal HTML anchor.

**Evidence** (`web/dist/zh/guide/readme/index.html` line 25):
```html
<li><a href="./self_deploy/">self_deploy/</a> — 4 平台独立部署教程</li>
```
Same line in `dist/en/guide/readme/index.html` and `dist/ja/guide/readme/index.html` (verified — see lang-specific text). When the user clicks this link from `/<lang>/guide/readme/`, the browser resolves it to `/<lang>/guide/self_deploy/` which **404s** (no such route is built; `self_deploy/` is excluded from the content collection per `web/src/content.config.ts` line 10-12).

The e2e link-resolution test does NOT visit `/<lang>/guide/readme/` (its `routes` array is `['/zh/', '/en/', '/ja/', '/zh/guide/user-guide', '/zh/changelog']`), so this dead link **silently passes** the strict e2e mode added in 6.0. This is the EXACT "build-green-but-data-broken" scenario Phase 5 G-P5-2 warned about.

**Adversarial probe** — I traced from a hypothetical visitor: open https://sdtm-pedia.pages.dev/zh/ → click 文档 → land on user-guide → use sidebar to navigate to README → click "self_deploy/" → 404. Three clicks from landing.

**Suggested fix** (Phase 6.4 candidate, blocking — both parts):
1. **Plugin widening** — extend `web/remark-md-link-rewrite.mjs` to ALSO drop link wrappers for relative refs that match `^(?:\.\/)?self_deploy\/` OR a stricter "any relative ref to a path NOT in SLUG_MAP". The Task 6.0 evidence report explicitly flags this as a 6.3 reviewer decision. Recommended: add a second SHAPE-like check that drops any relative ref starting with `./self_deploy/` (preserving children, like the existing drop branch).
2. **e2e widening** — add `/zh/guide/readme` to `web/tests/e2e/smoke.spec.ts` `routes` array (line 29). Once the plugin is widened, the test will be a regression guard. Tier 3 lesson: "if you fix it, test it; if you can't test it, fix it deeper".
3. Optionally also test `/en/guide/readme` and `/ja/guide/readme` to mirror the en+ja landing coverage from Phase 5 M1.

---

### M1 — Hardcoded English chrome on `/<lang>/compare` page for all 3 langs (D3 + D4)

**Severity**: MEDIUM
**Confidence**: HIGH
**Dimension**: D3 (compare page i18n shape) + D4 (CompareFilter island i18n)

The page heading + subhead + filter input chrome are hardcoded English in `web/src/pages/[lang]/compare.astro` lines 22-24 and `web/src/components/react/CompareFilter.tsx` lines 28-29:
- `"Multi-dimensional Comparison"` (h1)
- `"Side-by-side across 4 platforms. Filter by dimension keyword."` (subhead)
- `"Filter dimensions..."` (placeholder)
- `"Filter dimensions"` (aria-label)

**Evidence**:
```
$ grep -A1 'Multi-dimensional Comparison' web/dist/{zh,en,ja}/compare/index.html
zh: <h1>Multi-dimensional Comparison</h1>
en: <h1>Multi-dimensional Comparison</h1>
ja: <h1>Multi-dimensional Comparison</h1>
```
A Japanese-only viewer arriving at `/ja/compare` sees: a Japanese TopNav (ドキュメント / 4 プラットフォーム / デモ / ダウンロード), then English h1/subhead/input chrome, then Japanese dim labels (最も得意 / 容量上限 / チーム共有 / アンチハル強度 / 評価スコア / サブスク要件 / インターネット / ファイル数上限 / 最も苦手), then mixed Chinese/English values. The cognitive load of switching languages mid-page is real.

The plan template explicitly defers chrome i18n (per Task 6.1 prompt L97 "Hardcoded English `Filter dimensions...` placeholder is acceptable for 6.1 (matches plan); reviewer 6.3 may flag for v1.1 i18n polish — that is OK"). I am flagging it. The existing i18n infrastructure (`web/src/i18n/ui.{zh,en,ja}.json` with `section.compare.*` keys already used by `ComparePreviewSection.astro` line 43) is already the right pattern — adding `compare.title` / `compare.subhead` / `compare.filter.placeholder` / `compare.filter.label` keys is mechanical.

**Why this matters**: this is the C-P5-L1 fallback-banner-i18n carryover pattern in NEW form. Phase 6 didn't reduce the i18n debt; it grew it. C-P5-L1 should be widened to include `/<lang>/compare` chrome.

**Suggested fix** (v1.1 polish OR Phase 6.4 if doing the H1+H2 fix bundle anyway):
1. Add 4 keys to `ui.{zh,en,ja}.json`: `compare.title`, `compare.subhead`, `compare.filter.placeholder`, `compare.filter.label`.
2. In `[lang]/compare.astro`: import `getUIStrings`, render `t['compare.title']` etc.
3. In `CompareFilter.tsx`: change `Props` to accept `placeholder: string; ariaLabel: string`, pass them in from the `.astro` page.
4. Verify all 3 langs render the per-lang strings.

Note: this widens C-P5-L1 carryover scope from "fallback banner" to "all hardcoded English UI chrome" — explicit acknowledgment is Phase 7+ candidate.

---

### M2 — Catchall `/<lang>/guide/platform-comparison` exists in addition to `/<lang>/compare` page route (D2 + D7)

**Severity**: MEDIUM
**Confidence**: HIGH
**Dimension**: D2 (slug rename) + D7 (preview-vs-full split)

Post slug rename, BOTH of these exist:
- `dist/<lang>/guide/platform-comparison/index.html` — the source PLATFORM_COMPARISON.{lang}.md rendered as a docs page (DocsLayout, sidebar, prose, TOC)
- `dist/<lang>/compare/index.html` — the new Phase 6.1 React island filter table

These are two different views of overlapping data. The TopNav doesn't link to `/<lang>/compare/`; only the landing CTA (`ComparePreviewSection.astro` line 42) and direct URL navigation reach it. The DocsSidebar entry for `4 平台多维对比` (in zh) links to `/<lang>/guide/platform-comparison/` (the .md doc page).

**Evidence** (`web/dist/zh/guide/platform-comparison/index.html` line 16-17):
```
<li> <a href="/zh/guide/platform-comparison" class="block py-1 text-accent font-bold"> 4 平台多维对比 </a> </li>
```
Versus `ComparePreviewSection.astro` line 42:
```
<a href={`/${lang}/compare`} ...>{t['section.compare.cta']}</a>
```

The two routes are not redundant — `/compare` adds interactive filter while `/guide/platform-comparison` is the static doc — but the relationship is not signposted to the user. A user landing on `/guide/platform-comparison` from the sidebar has no link to `/compare` and vice versa. This isn't a regression (Phase 5 had the same shape with a stub `/compare`), but the rename + real page now make the redundancy concrete.

**Suggested fix** (v1.1 polish, NOT blocking):
1. Add a "Filter interactively →" link from `/guide/platform-comparison` to `/compare`.
2. Add a "See the full article →" link from `/compare` to `/guide/platform-comparison`.
3. OR consolidate: drop `/guide/platform-comparison` from the sidebar enumeration (still emit the route) and let `/compare` be the canonical; sidebar link "4 平台多维对比" points to `/compare`. Cleaner mental model.

---

### M3 — `slice(0, 4)` magic number in `ComparePreviewSection.astro` line 29 (D7)

**Severity**: MEDIUM
**Confidence**: HIGH
**Dimension**: D7 (slice cut brittleness)

Hardcoded `4`. If a future contributor inserts a new dim at the front of `compare-dimensions.json`, the landing preview silently shows the wrong dims. The current order (`best-at`, `capacity`, `sharing`, `anti-halluc`) was deliberate per master plan §6.2 Step 2 commentary, but no test enforces it.

**Evidence** (`web/src/components/astro/ComparePreviewSection.astro` line 29):
```
{dims.slice(0, 4).map((d) => (
```

**Why this matters**: silent UX regression class. Build-green-but-data-broken precisely because there's no test asserting "the landing preview shows exactly these 4 dims".

**Suggested fix** (LOW effort, Phase 6.4 if doing fix bundle):
1. Extract `const LANDING_PREVIEW_KEYS = ['best-at', 'capacity', 'sharing', 'anti-halluc'] as const;` (named, intent-revealing).
2. Filter by membership instead of slice: `dims.filter((d) => LANDING_PREVIEW_KEYS.includes(d.key as ...))`.
3. Add a vitest assertion in landing tests: "ComparePreviewSection renders rows for each LANDING_PREVIEW_KEY in order" (would have caught accidental reorder).
4. Document the rationale in a code comment ("user-relevant 4 dims for first-impression").

---

### M4 — `aria-label="Filter dimensions"` is hardcoded English even for zh/ja viewers (D4)

**Severity**: MEDIUM
**Confidence**: HIGH
**Dimension**: D4 (a11y)

Screen-reader users in zh/ja will hear "Filter dimensions" announced in English over the Japanese page chrome. This is also a WCAG SC 3.1.2 (Language of Parts) gap — the input has no `lang="en"` attribute to mark it as English content embedded in a `<html lang="ja">` document.

**Evidence**: `CompareFilter.tsx` line 29: `aria-label="Filter dimensions"`. Combined with M1 — fixing M1 fixes M4 transitively (per-lang aria-label). Calling it out separately because some teams might accept the visible chrome in English while still wanting the SR announcement to be per-lang.

**Suggested fix**: covered by M1 fix.

---

### M5 — `winners` color-only signaling fails WCAG SC 1.4.1 (D4)

**Severity**: MEDIUM
**Confidence**: MEDIUM
**Dimension**: D4 (a11y)

The "winner" column in the compare table is signaled ONLY by `text-accent font-bold`. Color-blind viewers + screen-reader users have no programmatic way to know which platform "wins" a dimension.

**Evidence** (`CompareFilter.tsx` line 53-55):
```
<td className={`py-2 px-2 ${d.winners.includes(p.key) ? 'text-accent font-bold' : ''}`}>
  {d.values[p.key]}
</td>
```

Bold + color-accent communicates winner status; no `aria-label`, no `<sup>★</sup>`, no text marker. Per WCAG 2.1 SC 1.4.1 (Use of Color), color must not be the only visual means of conveying information. The bold text helps for sighted users with color-blindness, but a screen reader will read "Pro/Team/Ent" identically whether it's a winner or not.

**Realist Check**: this is a comparison table with dim-by-dim winner annotation; the screen-reader user can still consume all the values. Mitigating factor: not a critical action element; informational only. Keeping at MEDIUM.

**Suggested fix** (v1.1 polish):
1. Append a hidden text marker for screen readers when winner: `{isWinner && <span className="sr-only">winner</span>}`.
2. OR use a visible marker like `★` prepended to winner cells.

---

### L1 — Empty filter result renders empty `<tbody></tbody>` (no "No matches" message) (D4)

**Severity**: LOW
**Confidence**: HIGH
**Dimension**: D4 (UX)

Type a string that matches no dim labels (e.g. `xyzzy`); the table goes empty with no feedback. Acceptable for a v1 inline filter; better UX is a "No matching dimensions for 'xyzzy'" row.

**Evidence**: `CompareFilter.tsx` line 45-58 — no empty-state branch.

**Suggested fix**: add `{filtered.length === 0 && (<tr><td colSpan={5} className="text-center py-4 text-ink-mute">No matching dimensions</td></tr>)}` (also a M4 carryover for i18n).

---

### L2 — `playwright.config.ts` `reuseExistingServer: true` burned 6.0's first attempt with stale dev (D5)

**Severity**: LOW
**Confidence**: HIGH
**Dimension**: D5 (e2e infra)

Phase 6.0 evidence report §6 "Open questions" #1 documents that a stale `astro dev` from 23:52 the prior day served pre-plugin HTML, and only `kill 92189 92320` unblocked the e2e. Phase 6.2 evidence confirms the workaround (`lsof -ti:4321 | xargs -r kill` pre-run). This is institutional knowledge that lives only in evidence reports.

**Evidence**: `web/playwright.config.ts` line 11 `reuseExistingServer: true`.

**Suggested fix** (LOW effort):
1. Either flip to `reuseExistingServer: !process.env.CI` (slow but safe locally; reuse in CI where the dev server is already cold-started).
2. OR add a `pretest:e2e` script that runs `lsof -ti:4321 | xargs -r kill || true` (POSIX-safe).
3. OR document in `web/README.md` (does not exist; create one).

---

### L3 — DocsSidebar does not enumerate `slug: changelog` entry (D2-adjacent)

**Severity**: LOW
**Confidence**: HIGH
**Dimension**: D2

The CHANGELOG entry has `lang: 'en'`. DocsSidebar enumerates `e.data.lang === lang || e.data.lang === undefined` (`web/src/components/astro/DocsSidebar.astro` line 6). For `lang === 'zh'` viewers, the `lang: 'en'` changelog entry is filtered OUT. So users on `/<zh>/guide/readme` see a sidebar with README / 用户手册 / 4 平台多维对比 / Demo Questions / 术语表 — NO changelog. Yet the dedicated route `/zh/changelog/` is accessible from TopNav, AND the catchall route `/zh/guide/changelog/` exists (per H1 finding) but is unreachable from the sidebar.

This compounds H1: not only is the duplicate route emitted, but the docs sidebar cannot navigate to it (so the dedicated route is the only sensible reach path), making the catchall version even more "dead but indexed".

**Evidence**: `dist/zh/guide/readme/index.html` (sidebar excerpt above) — only 5 entries listed, no changelog.

**Suggested fix**: same as H1 — drop the catchall `slug: 'changelog'` emission. After H1 fix, this becomes invisible.

---

### L4 — `'no <html> element'` build warnings on 4 redirect routes (carryover, observation only)

**Severity**: LOW
**Confidence**: HIGH
**Dimension**: build noise

Inherited from prior phases (Task 6.1 evidence report §4 + Task 6.2 evidence report §3.3). The 4 routes are:
- `/` (root → /zh/)
- `/zh/guide/` (→ /zh/guide/user-guide)
- `/en/guide/` (→ /en/guide/user-guide)
- `/ja/guide/` (→ /ja/guide/user-guide)

These are intentional `Astro.redirect()` pages without an `<html>` shell. The dist HTML is `<!doctype html><title>Redirecting to: X</title><meta http-equiv="refresh"...`. Astro logs a warning but the redirect works. Not introduced by Phase 6.

**Suggested fix**: ignore for Phase 6 (pre-existing). If desired, add a no-op `<html><body></body></html>` wrapper in the redirect pages. Phase 7+ cosmetic.

---

## What's Missing (gap analysis)

- **No e2e for `/<lang>/compare/`** — the new core page from Phase 6.1 is not visited by `link-resolution`. If a future change breaks the React island hydration or its server-rendered initial state, smoke would not catch it. Phase 6.4 candidate: add `/zh/compare` to e2e routes (already covered by H2 fix #2).
- **No row-count assertion on landing `<ComparePreviewSection>`** — covered by M3, but worth re-stating: "the landing shows exactly 4 dims" is not asserted; only "the WHICH ONE? section heading is visible". Slice index could break silently.
- **No vitest covering `lang-neutral` plugin throw guard** — the safeguard (`if (!lang) throw`) is dead code today (DEMO_QUESTIONS has 0 .md cross-refs). Adding a fixture-level vitest with a fake `frontmatter.lang === undefined` + a `.md` URL would lock the contract before a future contributor adds such a cross-ref.
- **No CJK input-method (IME) test for filter** — D4 brief flags this as "theoretical". I agree it's theoretical for v1 (`controlled <input>` + React 19 handle composition events well enough), but a single integration test (`fireEvent.compositionStart` / `fireEvent.compositionUpdate` / `fireEvent.compositionEnd`) would prove it.
- **No `<link rel="canonical">` ANYWHERE** — checked all 3 lang-variants of compare/, guide/changelog/, changelog/, guide/platform-comparison/. None emit canonical. Even without H1's specific dual-route concern, missing canonical is a generic SEO gap. Phase 7 candidate.
- **No `compare-dimensions.json` schema validation** — the JSON file is loose (TS-typed only at the consumer site). A future malformed entry (missing `winners` array, extra platform key, etc.) would cause runtime React errors at hydration. Phase 7 candidate: add zod schema.

---

## Ambiguity Risks

> Step 4 (PLAN.md plan-deviation §): `"Override: overwrite web/src/pages/[lang]/compare.astro (same path as the Phase 5 stub)"` → Interpretation A (followed): overwrite the file body in place. Interpretation B: keep Phase 5 stub backup somewhere. The chosen interpretation is correct per Phase 5 D-P5-3, but the PLAN.md L73 verification "OK: stub gone" is the only artifact confirming the overwrite — no `git mv` trace, no `failures/` archive of the stub. Risk if Phase 7 needed to restore the stub: 0 (git history has it). Acceptable.

> Task 6.0 spec line 60 `SHAPE = /^(?:\.\/)?([A-Z_]+)(?:\.(zh|en|ja))?\.md(#.*)?$/` → Interpretation A (followed): only `.md` URLs enter the rewrite logic, all others (incl. `./self_deploy/`) pass through unchanged. Interpretation B: drop ALL relative refs that don't resolve to a built route. The brief said "implement EXACTLY this algorithm" → A is correct per spec. But "EXACTLY this algorithm" + a documented gap = the Task 6.0 evidence report #2 raised this as a 6.3 reviewer judgment call — see H2.

---

## Multi-Perspective Notes

- **Executor / new-hire**: a developer adding a 10th dim to `compare-dimensions.json` would have a clean experience: TS types at the `.tsx` import site catch missing keys; vitest fixtures are independent of the file. Adding a new lang-variant cross-ref (e.g. `[Foo](FOO.fr.md)`) would silently drop (no SHAPE match) — should be caught at ingestion-time per content schema enum. ⚠️ But: a developer replacing README.zh.md's `self_deploy/` link with another non-`.md` directory ref would not realize it becomes a dead `<a>` until they check the rendered HTML. Same H2 trap.
- **Stakeholder**: the user-facing experience is good — TopNav works, sidebar works, compare table renders fast (server-rendered initial state + client-load island). BUT: a Japanese-only stakeholder hits English chrome on `/compare` — perception of "this is a half-translated product" is real even if all the data is there. Recommend M1 fix before public release.
- **Skeptic / adversarial**: I tried to break the plugin with: empty url (handled), url without `.md` (correctly skipped), url with `.md` mid-path like `foo.md/bar` (regex `\.md(?:#|$)/` correctly rejects), url `BAR.md` without `./` prefix (matches SHAPE — correct), URL `bar.md` lower-case (no SHAPE match → drop link wrapper, correct for out-of-collection). The plugin is robust to its declared input space. The H2 finding is a SCOPE problem, not an algorithm bug.

---

## Phase 5 lessons re-validation

| Lesson | Status | Notes |
|---|---|---|
| R-P5-1 verbatim-copy contract | PASS | Task 6.0 + 6.1 prompts contain full code skeletons; committed code matches |
| R-P5-2 pre-flight pattern probe | PASS | Task 6.0 prompt §"Pre-flight context" verified content.config.ts + cross-ref inventory before dispatch |
| R-P5-3 Tier 3 plan trace | PASS | `_progress.json` + 3 evidence reports + 3 subagent prompts all present in `.work/07_website/phase6/` |
| R-P5-4 cross-family reviewer | PASS | This report = `oh-my-claudecode:critic`, cross-family from `pr-review-toolkit` (×4) and `feature-dev` (×1) |
| R-P5-5 entry decisions before dispatch | PASS | 3 decisions ack'd at session start (PLAN.md §"Plan deviation flag" + reviewer slot pre-allocation) |
| G-P5-1 Astro 6 API check | PASS | Phase 6 didn't touch content rendering; `import { render } from 'astro:content'` still in use, `[...slug].astro` line 33 `await render(entry)` confirmed |
| G-P5-2 defer "build green = PASS" | DRIFT (HALF) | Phase 6.0's e2e strict mode IS the consumer for the plugin (good) BUT silently passed H2's `./self_deploy/` because the e2e route list doesn't include `/zh/guide/readme` (see H2). The lesson would say "expanding strict-mode requires expanding route coverage to the entries that contain the new edge cases" — that didn't happen. |
| G-P5-3 .md cross-refs dead links | RESOLVED | Phase 6.0 plugin handles all 30 `.md` cross-refs cleanly. Confirmed: 0 `.md` endings in any `dist/<lang>/guide/*/index.html` href. |
| G-P5-4 enumerate new dimensions | PASS | Brief D1-D7 enumeration was effective (this reviewer found 2 HIGHs and 5 MEDIUMs that the per-task evidence reports flagged as judgment calls or implicit; wouldn't have happened without the structured probe) |

---

## Carryover bookkeeping (per PLAN.md table)

| ID | PLAN.md status | Phase 6 actual | Reviewer verdict |
|---|---|---|---|
| C-P5-1 .md cross-refs | "absorbed into Task 6.0" | Plugin landed in `b25b834`; rewrites all 7 known stems correctly | RESOLVED for `.md`; **partially resolved** — directory refs (`./self_deploy/`) NOT covered by current shape (see H2) |
| C-P5-2 PLATFORM_COMPARISON slug | "absorbed into Task 6.0" | All 3 lang variants frontmatter `slug: platform-comparison`; `dist/<lang>/guide/platform-comparison/` exists; `dist/<lang>/guide/compare/` does NOT (verified) | RESOLVED |
| C-P5-M2 DocsSidebar drawer VT | "DEFER no VT enabled" | No VT introduced | UNCHANGED — defer correct |
| C-P5-M3 trailing-slash hosting | "VERIFY during Phase 6 CF preview deploy" | NOT done in Phase 6 | DRIFT — Phase 6 plan committed to verify but no evidence of CF Pages preview verification. The astro config `build.format: 'directory'` emits `/foo/` URLs; sidebar emits `/foo` (no slash) hrefs — relies on CF redirect. Phase 7 must verify before public-release distribution. |
| C-P5-L1 fallback banner i18n | "DEFER next i18n touch" | Phase 6.1 added MORE hardcoded English (compare page chrome) | **WIDEN scope** — see M1. New scope: "all hardcoded English UI chrome incl. fallback banner + compare page chrome + filter input chrome" |
| C-P5-L2 empty TOC aside guard | "DEFER cosmetic" | Not regressed (DocsTOC not touched in Phase 6) | UNCHANGED — defer correct |

---

## Recommendations for Phase 6 → Phase 7 handoff

**Phase 6.4 fix bundle (BLOCKING before Phase 7)**:
- H1 fix (drop changelog from catchall, OR add canonical) — 5-line change in `[...slug].astro`
- H2 fix (widen plugin to drop `./self_deploy/` link wrapper + add `/zh/guide/readme` to e2e routes) — ~10 lines plugin + 1 line spec
- M3 fix optional (named const + filter membership + landing test assertion) — defensive

**Phase 7 carryover (NEW)**:
- **C-P6-1** Hardcoded English UI chrome on `/compare` (M1 + M4) — widen C-P5-L1 scope to include compare page + filter input.
- **C-P6-2** Color-only winner signaling (M5) — accessibility fix.
- **C-P6-3** Missing `<link rel="canonical">` site-wide — adds defensive SEO baseline before public release.
- **C-P6-4** `playwright.config.ts reuseExistingServer: true` (L2) — pick one of three documented workarounds.
- **C-P6-5** Catchall `/<lang>/guide/platform-comparison` vs `/<lang>/compare` UX redundancy (M2) — design decision.
- **C-P6-6** No vitest for plugin lang-neutral throw guard — fixture test before a future cross-ref breaks build at runtime instead of at test-time.
- **C-P6-7** `compare-dimensions.json` no schema validation — zod or content-collection-style schema before runtime React explodes on malformed entry.

**Pre-existing carryover NOT touched in Phase 6**:
- C-P5-M2 (VT — defer correct), C-P5-M3 (CF trailing-slash — must verify Phase 7 before distribution), C-P5-L2 (empty TOC — defer correct).

---

## Adversarial probe summary (top 3 things I tried to break)

1. **Plugin SHAPE regex edge cases** — tried URLs with absolute paths, lower-case stems, mid-path `.md`, missing `./` prefix, hash without `.md` (e.g. `#foo`), double extensions (`foo.md.bak`). Plugin handled all cases per its declared contract — either rewrote correctly, dropped link wrapper for out-of-collection, or correctly skipped (passed through). No algorithm bug. **Result**: plugin is robust within its scope.

2. **Dual-route emission for collection entries with dedicated routes** — diff'd `dist/zh/changelog/index.html` vs `dist/zh/guide/changelog/index.html` body content; both identical; both in sitemap; neither has canonical. Confirmed H1. Then checked if `slug: platform-comparison` had the same dual-route problem (could a hypothetical `pages/[lang]/platform-comparison.astro` exist?). It does not — only the catchall route emits `/guide/platform-comparison/`. So dual-route is changelog-only today. **Result**: H1 confirmed; isolated to changelog by virtue of changelog being the only entry with a dedicated `[lang]/changelog.astro` page.

3. **e2e silent-pass scenarios** — manually traced from each route in the e2e list to all transitively-reachable `<a>` targets. The e2e visits 5 routes; `/zh/guide/readme` is not in the list; `dist/zh/guide/readme/` contains a `<a href="./self_deploy/">` that resolves to a 404 path; e2e silent-passes. Then checked en+ja: same dead link. Then checked /<lang>/guide/platform-comparison and /<lang>/guide/glossary for similar non-`.md` relative refs that the plugin doesn't touch — both clean. **Result**: H2 confirmed for README only; isolated to README in current corpus.

---

## Verdict Justification

**CONDITIONAL_PASS** because:
- Infrastructure quality is HIGH: remark plugin algorithm is precise to spec, React island is sane, slug rename is atomic, e2e strict mode is meaningful, vitest 31/31, build green, 9 dim values match source data with no drift.
- Plan deviation (path-based i18n) is well-justified, well-documented, and correctly executed.
- Phase 5 lessons R-P5-1 through R-P5-5 all PASS; G-P5-1 / G-P5-3 / G-P5-4 PASS; G-P5-2 partial DRIFT manifests as H2.
- BUT two HIGH findings (H1 + H2) reach end-users / search engines and are the exact "build-green-but-data-broken" pattern Phase 5 warned about.
- Both have low-effort fixes (~15 LOC total) and are testable post-fix.
- Mode escalation: started THOROUGH, escalated to ADVERSARIAL after confirming H1 + H2 + M1 + the systemic dual-route issue. Adversarial pass uncovered M2/M3/M4/M5 + L1-L4 that THOROUGH wouldn't have surfaced.
- Realist Check downgrades: H1 from CRITICAL→HIGH (mitigated by internal-company audience pre-public-release; easy rollback). H2 stays HIGH (real dead link, all 3 langs, public-facing once distribution widens). M1 stays MEDIUM (UX-but-not-blocking).

**To upgrade to PASS**: apply Phase 6.4 fix bundle (H1 + H2). M-level findings can defer to Phase 7 (with explicit carryover IDs above).

**To downgrade to FAIL**: only if main session declines to address H1/H2 before Phase 7, OR if CF Pages preview deploy (C-P5-M3) reveals trailing-slash regressions that block landing.

---

## Open Questions (unscored)

- Did the master plan §6 anticipate dual-route changelog emission? Plan §6.0 doesn't mention it; D-P5-1 in Phase 5 retro acknowledges the dedicated route trade-off but doesn't address the catchall side-effect. Possible documentation gap for Phase 6 plan author OR an oversight in catchall design.
- Should the e2e have a "visit every dist `index.html` for at least one lang" sweep (e.g., generate route list from `glob('dist/zh/**/index.html')`)? More expensive but catches the H2 class of issue automatically. Phase 7+ design question.
- Is `1.29M tok` (capacity dim, claude column) consistent with `tok` vs `tokens`? PLATFORM_COMPARISON.zh.md L25 says `1.29M tokens (Pro 软上限附近)`; compare-dimensions.json says `"1.29M tok"`. Truncation in dim values is an editorial choice, not a drift. Note for v1.1 polish: consider `tokens` for clarity at the cost of column width.
- Filter input `value=""` initial server-rendered state — when the React island hydrates client-side, does it preserve any state? Currently all server-rendered values match initial useState. If a user types and then refreshes, no state persists. Acceptable for filter v1 (no bookmarkable filter URLs). Phase 7+ candidate: add `?q=foo` URL sync if filter UX matters.
- Confidence on M5 is MEDIUM (not HIGH) because some teams interpret WCAG SC 1.4.1 as satisfied by bold typography alongside color (bold is a non-color visual cue). Stricter interpretations require text/symbol. I'd recommend the stricter interpretation for an official internal release; weaker is defensible.

---

## Appendix — Adversarial probe trace evidence

### A. Sitemap dual-route inventory

```
$ grep -E '(changelog|compare|platform-comparison)' web/dist/sitemap-0.xml
https://sdtm-pedia.pages.dev/en/changelog/
https://sdtm-pedia.pages.dev/en/compare/
https://sdtm-pedia.pages.dev/en/guide/changelog/
https://sdtm-pedia.pages.dev/en/guide/platform-comparison/
https://sdtm-pedia.pages.dev/ja/changelog/
https://sdtm-pedia.pages.dev/ja/compare/
https://sdtm-pedia.pages.dev/ja/guide/changelog/
https://sdtm-pedia.pages.dev/ja/guide/platform-comparison/
https://sdtm-pedia.pages.dev/zh/changelog/
https://sdtm-pedia.pages.dev/zh/compare/
https://sdtm-pedia.pages.dev/zh/guide/changelog/
https://sdtm-pedia.pages.dev/zh/guide/platform-comparison/
```
Dual-route changelog confirmed in all 3 langs. compare/ vs guide/platform-comparison/ are different pages (CompareFilter island vs static doc) — not dual-route in the same sense; M2 instead of H1.

### B. Self-deploy dead link in all 3 langs

```
$ grep -E 'href="\./self_deploy' web/dist/{zh,en,ja}/guide/readme/index.html
zh: <li><a href="./self_deploy/">self_deploy/</a> — 4 平台独立部署教程</li>
en: <li><a href="./self_deploy/">self_deploy/</a> — Independent deployment tutorials for all 4 platforms</li>
ja: <li><a href="./self_deploy/">self_deploy/</a> — 4 プラットフォーム個別デプロイチュートリアル</li>
```
All 3 langs of README, line 25 of dist HTML. Each resolves to `/<lang>/guide/self_deploy/` from the parent route — 404 (no such build target).

### C. Hardcoded English chrome on /compare

```
$ grep 'Multi-dimensional Comparison' web/dist/{zh,en,ja}/compare/index.html
zh: <h1 class="font-display text-4xl font-bold mb-2">Multi-dimensional Comparison</h1>
en: <h1 class="font-display text-4xl font-bold mb-2">Multi-dimensional Comparison</h1>
ja: <h1 class="font-display text-4xl font-bold mb-2">Multi-dimensional Comparison</h1>
```
Identical English h1 in all 3 lang variants.

### D. Spot-check dim values vs source

| Dim | JSON value | Source PLATFORM_COMPARISON.zh.md or CHANGELOG.md | Drift? |
|---|---|---|---|
| `score.claude` | `"17/17"` | CHANGELOG.md L23 `Claude Projects: 17/17 (100%)` | No |
| `subscription.notebooklm` | `"Pro/Workspace"` | PLATFORM_COMPARISON.zh.md L46 `NotebookLM: NotebookLM Pro / Google Workspace` | No |
| `internet.notebooklm` | `"in-KB-only"` | PLATFORM_COMPARISON.zh.md L55 `严格 in-KB-only` | No |
| `worst-at.claude` | `"实时联网"` | PLATFORM_COMPARISON.zh.md L88 `实时联网 (FDA / Pinnacle 21 需手动核 cdisc.org)` | No (truncated, faithful) |

No drift in 4-of-9 spot-checks across all dim families.

### E. Plugin algorithm pure-function check

`web/remark-md-link-rewrite.mjs` is a pure function of `tree` (mdast) + `file.data.astro.frontmatter.lang`. No I/O, no module-level mutable state, no `Date.now()` or random. Idempotent across re-runs of `npm run build`. ✓
