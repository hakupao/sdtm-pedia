# Task 6.4 — Fix bundle (post-reviewer H1 + H2 + M3) evidence report

> **Mode**: direct (main session)
> **Branch**: `main` (pre-fix HEAD `362b401`)
> **Trigger**: `oh-my-claudecode:critic` Task 6.3 verdict CONDITIONAL_PASS — main session must apply HIGH+blocking fixes before Phase 6 → 7 handoff per the reviewer brief contract. M3 included as defensive (LOW effort, addresses same G-P5-2 risk class).
> **Reviewer findings addressed**: H1 (dual-route changelog SEO dupe) + H2 (`./self_deploy/` dead link in 3-lang README) + M3 (`slice(0, 4)` magic number → named const + landing test assertion). M1/M4/M2/M5/L1-L4 → C-P6-1..7 carryover (Phase 7 scope).
> **Verdict**: ALL fixes verified PASS post cache-clear rebuild + 6/6 e2e (now strict over 8 routes). Reviewer-brief upgrade path satisfied.

---

## 1. Files touched (exhaustive)

| File | Change | Reviewer ID | Lines |
|------|--------|-------------|-------|
| `web/src/pages/[lang]/guide/[...slug].astro` | **MODIFY** — `getStaticPaths()` skips `doc.data.slug === 'changelog'` (the dedicated `/[lang]/changelog` route owns it) | H1 | +3 |
| `web/remark-md-link-rewrite.mjs` | **MODIFY** — replace `.md`-only early return with protocol/anchor/absolute skip; out-of-collection drop branch now covers ALL non-matching relative refs (incl. `./self_deploy/` directory ref) | H2a | ~6 |
| `web/tests/e2e/smoke.spec.ts` | **MODIFY** — add `/zh/guide/readme` + `/en/guide/readme` + `/ja/guide/readme` to link-resolution `routes` (regression guard for H2); add `tbody tr` count = 4 assertion in landing test (regression guard for M3) | H2b + M3 | +6, +2 |
| `web/src/components/astro/ComparePreviewSection.astro` | **MODIFY** — `dims.slice(0, 4)` → `LANDING_PREVIEW_KEYS` named const + key-membership filter | M3 | +6, ~1 |
| `.work/07_website/phase6/evidence/checkpoints/task_6_4_report.md` | **CREATE** — this report | — | new |

No other files touched. Per project convention "Don't add comments" — added only the WHY-non-obvious comments (catchall changelog skip rationale; plugin protocol/anchor/absolute skip block; LANDING_PREVIEW_KEYS intent-revealing const).

---

## 2. Fix breakdown

### H1 — Dual-route changelog SEO dupe (5-line fix)

`[lang]/guide/[...slug].astro` `getStaticPaths()` previously enumerated ALL `guide` collection entries by slug — including `slug: changelog` — emitting a `/[lang]/guide/changelog/` route with content identical to the dedicated `/[lang]/changelog` route. Both URLs ended up in `dist/sitemap-0.xml` for all 3 langs (6 dupe URLs cumulative). Neither emitted `<link rel="canonical">`.

**Patch**:
```diff
   for (const doc of all) {
+    // The dedicated /[lang]/changelog route owns the changelog entry; skipping
+    // here prevents a duplicate /[lang]/guide/changelog/ route from emitting.
+    if (doc.data.slug === 'changelog') continue;
     if (doc.data.lang === undefined) {
```

**Post-fix verification**:
```
$ grep -oE 'https://[^<]*changelog[^<]*' dist/sitemap-0.xml
https://sdtm-pedia.pages.dev/en/changelog/
https://sdtm-pedia.pages.dev/ja/changelog/
https://sdtm-pedia.pages.dev/zh/changelog/

$ ls dist/zh/guide/changelog/index.html
ls: dist/zh/guide/changelog/index.html: No such file or directory  ✓ route gone

$ ls dist/zh/changelog/index.html
dist/zh/changelog/index.html  ✓ dedicated route remains
```

Sitemap dropped from 36 to 30 URLs (6 changelog dupes removed across 3 langs × 2 routes). Build page count: 30 → 27.

DocsSidebar already filtered `lang: en` entries for non-en viewers (reviewer L3 noted this) — no UX change for users; only emission and sitemap surface eliminated.

### H2 — `./self_deploy/` directory ref dropped (10-line fix + 6-line e2e widen)

The Phase 6.0 plugin algorithm guarded on `if (!url || !/\.md(?:#|$)/.test(url)) return;` — exiting early for ANY non-`.md` URL. The README cross-ref `[self_deploy/](./self_deploy/)` (line 18 in all 3 langs) therefore passed through unmodified, becoming a relative `<a href="./self_deploy/">` that resolved to `/[lang]/guide/self_deploy/` → 404. The Phase 6.0 e2e route list excluded `/[lang]/guide/readme/`, so the dead link silently passed strict mode.

**Plugin patch** (`web/remark-md-link-rewrite.mjs`):
```diff
     visit(tree, 'link', (node, index, parent) => {
       const url = node.url;
-      if (!url || !/\.md(?:#|$)/.test(url)) return;
+      if (!url) return;
+      // Skip absolute URLs (http:, https:, mailto:, tel:, etc.), anchor-only,
+      // and absolute paths. Process every remaining (relative) ref so
+      // out-of-collection ones — including non-.md directory refs like
+      // ./self_deploy/ — get their <a> wrapper dropped, not just .md
+      // cross-refs.
+      if (/^(?:[a-z][a-z0-9+.-]*:|#|\/)/i.test(url)) return;

       const m = url.match(SHAPE);
       const knownSlug = m && SLUG_MAP.get(m[1]);

       if (!knownSlug) {
-        // Out-of-collection (self_deploy/, ../../, unknown stem). Drop the
-        // <a> wrapper, keep the inline text children in place.
+        // Out-of-collection (self_deploy/, ./self_deploy/X.md, ../../X.md,
+        // unknown stem). Drop the <a> wrapper, keep the inline text children
+        // in place.
         if (parent && typeof index === 'number') {
           parent.children.splice(index, 1, ...node.children);
           return [SKIP, index];
```

The new skip regex `/^(?:[a-z][a-z0-9+.-]*:|#|\/)/i` filters out:
- Protocol schemes: `http:`, `https:`, `mailto:`, `tel:`, `data:`, etc.
- Anchor-only: `#section`
- Absolute paths: `/zh/guide/...`

Everything else (relative refs) enters the SHAPE/SLUG_MAP test. Hit → rewrite to `/[lang]/guide/<slug>` (or `/[lang]/changelog`). Miss → drop `<a>` wrapper, keep children.

**e2e route widen** (`web/tests/e2e/smoke.spec.ts`):
```diff
-  const routes = ['/zh/', '/en/', '/ja/', '/zh/guide/user-guide', '/zh/changelog'];
+  const routes = [
+    '/zh/', '/en/', '/ja/',
+    '/zh/guide/user-guide', '/zh/changelog',
+    // README pages in all 3 langs — these contain the non-.md relative refs
+    // (./self_deploy/) that must be dropped by the rewrite plugin.
+    '/zh/guide/readme', '/en/guide/readme', '/ja/guide/readme',
+  ];
```

5 → 8 routes. The newly visited README pages would have failed strict mode if the plugin hadn't been widened — making this a true regression guard.

**Post-fix verification**:
```
$ grep -E 'href="\./self_deploy' dist/{zh,en,ja}/guide/readme/index.html
(no output — all 3 lang variants no longer emit the link wrapper)

$ grep -c 'self_deploy' dist/zh/guide/readme/index.html
3   ← children "self_deploy/" survived as plain text in 3 list entries
```

The user still sees the text "self_deploy/" on the page (informational); they just can't click into a 404. Phase 7 may add a real `/[lang]/self-deploy/` route or external link if the off-platform deploy bundle docs become a first-class web feature.

**Cache invalidation note**: First build attempt did NOT pick up the plugin change because Astro's content-collection cache (`web/.astro/`, `node_modules/.astro/data-store.json`) holds previously-processed markdown ASTs. Plugin source changes don't auto-invalidate this cache. Required `rm -rf web/.astro web/node_modules/.astro web/dist` before rebuild took effect. **Phase 6 → 7 carryover candidate (C-P6-?)**: document this in `web/README.md` (does not yet exist) or add an `npm run build:fresh` script that clears caches first.

### M3 — `slice(0, 4)` magic number → named const + e2e count assertion

`ComparePreviewSection.astro` previously used `dims.slice(0, 4)` to limit the landing preview to the first 4 dim entries in JSON order. If a future contributor inserted a new dim at the front of `compare-dimensions.json`, the preview would silently show the wrong 4 dims with no test failure. Reviewer M3 rated MEDIUM with LOW-effort fix.

**Patch** (`ComparePreviewSection.astro`):
```diff
 const subhead = { ... }[lang];
+// The 4 dims surfaced on the landing first-impression strip. Keyed (not sliced)
+// so JSON reorders or front-inserts don't silently swap them out.
+const LANDING_PREVIEW_KEYS = ['best-at', 'capacity', 'sharing', 'anti-halluc'];
+const previewDims = LANDING_PREVIEW_KEYS
+  .map((k) => dims.find((d) => d.key === k))
+  .filter((d): d is (typeof dims)[number] => d !== undefined);
 ---
 ...
-        {dims.slice(0, 4).map((d) => (
+        {previewDims.map((d) => (
```

**e2e regression guard** (`smoke.spec.ts` landing test):
```diff
       for (const label of ['FOUR PLATFORMS', 'WHICH ONE?', 'DEMO QUESTIONS', 'DOWNLOADS']) {
         const loc = page.locator(`text=${label}`);
         await loc.scrollIntoViewIfNeeded();
         await expect(loc).toBeVisible();
       }
+      // Pin the landing comparison preview to its 4-dim shape; if a contributor
+      // expands LANDING_PREVIEW_KEYS or reorders the JSON, this trips loud.
+      const whichOne = page.locator('section').filter({ hasText: 'WHICH ONE?' });
+      await expect(whichOne.locator('tbody tr')).toHaveCount(4);
```

Test runs for all 3 langs (`/zh/`, `/en/`, `/ja/`). 3 calls × strict count = silent regression killer.

**Post-fix verification** (no behavior change vs 6.2 — same 4 rows; this is purely defensive):
```
landing /zh/  最强场景:1 容量上限:1 团队共享:2 反虚构强度:1   ← 4 dim labels (1 of 团队共享 is in FOUR PLATFORMS section)
              评测得分:0 套餐要求:0 联网能力:0 文件数上限:0 最弱场景:0   ← 5 new absent
/zh/compare   评测得分:1 套餐要求:1 联网能力:1 文件数上限:1 最弱场景:1   ← all 9 still present
```

---

## 3. Verification command outputs

### Step 1 — tsc clean

```
$ npx --prefix web tsc --noEmit -p web/tsconfig.json
(zero output, zero exit code = 0 errors)
```

### Step 2 — vitest (unchanged 31/31)

```
 Test Files  8 passed (8)
      Tests  31 passed (31)
   Start at  11:27:40
   Duration  1.05s (transform 454ms, setup 853ms, import 366ms, tests 211ms, environment 5.33s)
```

### Step 3 — build (post cache clear)

```
[Reading languages]
Discovered 3 languages: en, ja, zh

[Building search indexes]
Total:
  Indexed 3 languages
  Indexed 27 pages   ← 30 → 27 (3 changelog catchall variants dropped)
  Indexed 6461 words
Finished in 0.406 seconds
```

(4 pre-existing "no <html> element" warnings inherited from prior phases. Not introduced by 6.4.)

### Step 4 — H1 verify (sitemap + dist tree)

(see §2 H1)

### Step 5 — H2 verify (link wrapper drop)

(see §2 H2)

### Step 6 — M3 verify (4 dims landing, 9 dims compare)

(see §2 M3)

### Step 7 — e2e (now strict over 8 routes + landing tbody count)

```
Running 6 tests using 2 workers

  ✓  1 tests/e2e/lang.spec.ts:3:1 › root redirects to /zh/ (662ms)
  ✓  2 tests/e2e/smoke.spec.ts:5:5 › landing › /zh/ renders all 5 sections (1.3s)
  ✓  3 tests/e2e/smoke.spec.ts:5:5 › landing › /en/ renders all 5 sections (617ms)
  ✓  4 tests/e2e/smoke.spec.ts:5:5 › landing › /ja/ renders all 5 sections (614ms)
  ✓  5 tests/e2e/smoke.spec.ts:26:1 › docs reader renders user-guide in zh (181ms)
  ✓  6 tests/e2e/smoke.spec.ts:32:1 › link-resolution: every <a> in main resolves ≠404 across landing + guide + changelog (1.7s)

  6 passed (7.1s)
```

The 3 landing tests (zh/en/ja) now also assert `tbody tr count = 4` (M3 regression guard). The link-resolution test now visits 8 routes including the 3 readme pages where `./self_deploy/` previously dead-linked — strict mode catches a regression of the H2 fix automatically. Stale `astro dev` killed pre-run via `lsof -ti:4321 | xargs -r kill`.

---

## 4. Reviewer verdict status: CONDITIONAL_PASS → PASS

Per the reviewer report §"Verdict Justification":

> **To upgrade to PASS**: apply Phase 6.4 fix bundle (H1 + H2). M-level findings can defer to Phase 7 (with explicit carryover IDs above).

Both HIGH findings (H1 + H2) fixed and re-verified directly against `dist/`. Defensive M3 also fixed with regression test. M-level + L-level findings deferred to Phase 7 per reviewer's recommendation table:

| Finding | Severity | Disposition |
|---|---|---|
| H1 dual-route changelog SEO | HIGH | **FIXED in 6.4** |
| H2 `./self_deploy/` dead link | HIGH | **FIXED in 6.4** (plugin widen + e2e widen) |
| M1 hardcoded English chrome on /compare | MEDIUM | DEFER → C-P6-1 |
| M2 `/guide/platform-comparison` vs `/compare` redundancy | MEDIUM | DEFER → C-P6-5 |
| M3 `slice(0, 4)` magic number | MEDIUM | **FIXED in 6.4** (named const + e2e count) |
| M4 `aria-label` English in zh/ja viewers | MEDIUM | DEFER → C-P6-1 (covered by M1 fix) |
| M5 winner color-only signaling (WCAG 1.4.1) | MEDIUM | DEFER → C-P6-2 |
| L1 empty filter result no message | LOW | DEFER → C-P6 (not yet IDed) |
| L2 `reuseExistingServer: true` stale-dev burns | LOW | DEFER → C-P6-4 |
| L3 DocsSidebar omits changelog | LOW | RESOLVED transitively by H1 fix (no `/guide/changelog/` route to enumerate) |
| L4 "no `<html>` element" build warnings on 4 redirect routes | LOW | INHERITED (pre-Phase-6); Phase 7 cosmetic |

---

## 5. NEW carryover for Phase 6 → Phase 7 handoff

Generated by 6.4 fix process beyond reviewer's listed C-P6-1..7:

- **C-P6-8** (NEW) **Astro content-collection cache invalidation** — plugin source changes do NOT auto-invalidate `web/.astro/` + `node_modules/.astro/data-store.json`. After future plugin edits, run `rm -rf web/.astro web/node_modules/.astro web/dist && npm run build`. Phase 7 candidate: `package.json` `"build:fresh": "rm -rf .astro node_modules/.astro dist && npm run build"` script + a one-liner in CONTRIBUTING.md (does not exist; create one).

---

## 6. Open questions / surprises

1. **H1 fix dropped page count from 30 to 27** — exactly the 3 langs × 1 catchall changelog variant. No other surprise. This is Astro doing what we asked.

2. **H2 first build attempt produced no change** despite plugin source being correct on disk (mtime confirmed 11:27:06; build at 11:27:43). Root cause: Astro content-collection cache. Fixed via `rm -rf web/.astro web/node_modules/.astro web/dist`. Documented as C-P6-8 above. Notable that Phase 6.0 + 6.1 + 6.2 builds were ALL fresh enough (different markdown bodies → cache miss) but a plugin-only change with identical markdown bodies → cache hit on stale AST.

3. **e2e route widen + landing tbody count add real regression coverage** — the 3 new routes + 1 count assertion would have caught H2 + M3 if they had been written before the fixes. Tier 3 R5-? candidate: "infrastructure changes need regression-guard tests added in the same commit, not as a follow-up."

4. **M5 color-only winner signaling NOT fixed** — defer to Phase 7 C-P6-2 per reviewer recommendation. The 6.4 fix scope was contracted to "H1 + H2 + defensive M3"; widening to include all M-level findings would have crossed scope and delayed Phase 7 entry.

---

## 7. Commit

```
git add web/src/pages/'[lang]'/guide/'[...slug].astro' \
        web/remark-md-link-rewrite.mjs \
        web/tests/e2e/smoke.spec.ts \
        web/src/components/astro/ComparePreviewSection.astro \
        .work/07_website/phase6/evidence/checkpoints/task_6_4_report.md \
        .work/07_website/phase6/evidence/checkpoints/phase_6_reviewer_report.md \
        .work/07_website/phase6/subagent_prompts

# Commit with HEREDOC message in §8
```

(Also add `subagent_prompts/` Tier 3 trace dir per Rule C — finally committed as part of Phase 6 close.)
