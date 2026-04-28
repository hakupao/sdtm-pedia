# Phase 7 — End-of-Phase Reviewer Report

> **Reviewer**: `superpowers:code-reviewer` (3rd-family inaugural on website lane after `pr-review-toolkit` ×4 + `feature-dev` ×1 + `oh-my-claudecode` ×1)
> **Date**: 2026-04-29
> **Scope**: Phase 7 = pre-public-release bundle, 3 commits `e1737f1..a1ad23e`
> **Mode**: read-only adversarial review (per brief D-P6-4 + R-P6-5 lesson; release-readiness = pseudo-infrastructure phase)
> **Branch**: `main`

---

## Verdict

**CONDITIONAL_PASS** → upgrades to **PASS** if F-1 + F-2 are addressed in a small Phase 7.5 fix bundle (~20 LOC across 2 files, both fixes mechanical).

If Daisy elects to defer F-1 + F-2 to Phase 8, **PASS-with-carryover** is acceptable — neither finding is launch-blocking, both are visible-but-niche SEO/i18n polish. The recommendation below leans toward "fix in 7.5" because both are ~5 minute edits and one (F-2 Japanese punctuation) WILL bite a JP-native reader on first viewing.

| Severity | Count | Items |
|---|---|---|
| **HIGH** | 1 | F-1 redirect-page canonical → 308-target URL (canonical→redirect chain) |
| **MEDIUM** | 4 | F-2 ja punctuation drift; F-3 ja placeholder convention drift; F-4 ja aria-label verb-form; F-5 deferred WCAG color-only winner cells (C-P6-2 pre-public release) |
| **LOW** | 5 | F-6 redirect template build noise unsuppressed; F-7 README "auto-deploys from main" unverified; F-8 build:fresh script subtly diverges from PLAN spec; F-9 plan deviation reason #4 hand-wavey; F-10 Rule A N=3 sample for translation might be too low |

---

## What Phase 7 did well (acknowledge first)

- **Correct plan deviation justification**: master-plan §"Phase 7" Pagefind deferred for release-readiness bundle is defensible (release surface > additional UX); 4 reasons in PLAN.md L12-21 are concrete (carryovers framed "before public release", visible canonical/i18n gaps on already-shipped pages, cheap CF preview verify) and not hand-wavey (with one minor exception — F-9). Phase 6 D-P6-1 deviation precedent supports this pattern.
- **Tier 3 trace artifacts complete**: `PLAN.md` 242 lines + `_progress.json` 118 lines + 4 task evidence reports + this report — full archeology preserved.
- **Mechanical work done cleanly**: 7.1/7.2/7.3 all stay within their diff scope (15 files, 792 line additions, no scope creep).
- **+1 vitest test for new keys** (CompareFilter localizes filter input placeholder + aria-label per lang) — locks the 4 new keys against future regression.
- **Canonical coverage 31/31 dist HTML pages** — true 100% coverage including the 4 redirect pages (a strict reading of "site-wide canonical" was achieved, including via Astro's built-in redirect template).
- **Trailing-slash format check passed** — `Astro.url.pathname` returns `/zh/compare/` (with slash) on the 27 content pages, matching `build.format: 'directory'` consistently.
- **README is genuinely useful** — 5 tribal-knowledge sections each verified accurate against current code (build:fresh cache trap / playwright reuseExistingServer / lang-neutral throw / catchall recipe / soft-404), not aspirational/rotted-on-day-one content.
- **Rule A spot-check disclosed transparently** — Task 7.1 report cites the optional polish on `compare.filter.label.ja` rather than glossing over it.

---

## Plan deviation re-litigation (D5)

**Verdict on the deviation itself**: justified. Pagefind is additive UX; canonical/i18n parity/CF preview are distribution gates. Phase 6 reviewer raised 8 carryovers framed "before public release" — Phase 7 absorbing 3 of those (C-P6-1 i18n, C-P6-3 canonical, C-P6-8 build:fresh+README) before adding a search index is sequencing-correct.

**Counter-argument considered**: "Pagefind enables search, which enables product discoverability, which is also a distribution gate." Rejected on the merits — Pagefind without canonical means search-engine signals fragment across non-canonical URLs (the `/zh/guide/` redirect-target inconsistency below would be much worse if search results pointed at canonical-less pages). Canonical-first ordering is correct.

**Reason audit** (4 reasons in PLAN.md):
- Reason #1 (8 carryovers framed as before-release): **strong** ✓
- Reason #2 (canonical missing + compare i18n hardcoded): **strong** ✓ (verified visible in dist HTML grep pre-Phase-7)
- Reason #3 (CF preview verify cheap, risk grows): **strong** ✓ (Task 7.0 ran 27 probes, came back clean — exactly the cheap check that gets skipped)
- Reason #4 (master-plan §7 renumbers to §8, downstream phases shift): **F-9 hand-wavey** — see Findings.

---

## Findings

### F-1 [HIGH] Redirect-page canonical points to a URL that itself 308-redirects

**Class**: SEO correctness regression (visible to crawlers, latent to dev mode)
**File**: Affects `dist/index.html`, `dist/zh/guide/index.html`, `dist/en/guide/index.html`, `dist/ja/guide/index.html` (4 routes total)
**Source**: Astro's built-in i18n redirect template (NOT BaseLayout) — `astro.config.mjs` `i18n.routing.prefixDefaultLocale: true` + the implicit `/[lang]/guide/` → `/[lang]/guide/user-guide` redirect.
**Phase 7 attribution**: Pre-existing (Phase 5/6 era). NOT introduced by Phase 7. **However**: the brief explicitly asked D2 question "should redirect canonical point to the page where the redirect target lives?" — and Task 7.2 evidence answered "search engines consolidate signals on the destination" without inspecting the destination URL format. The destination URL format is the bug.

**Concrete evidence**:
```
$ grep -h 'rel="canonical"' dist/zh/guide/index.html
<!doctype html><title>Redirecting to: /zh/guide/user-guide</title>
<meta http-equiv="refresh" content="2;url=/zh/guide/user-guide">
<meta name="robots" content="noindex">
<link rel="canonical" href="https://sdtm-pedia.pages.dev/zh/guide/user-guide">
                                                              ^^^^^^^^^^^^^ no trailing slash
```

```
$ curl -sI https://sdtm-pedia.pages.dev/zh/guide/user-guide
HTTP/2 308
location: /zh/guide/user-guide/
```

```
$ grep -h 'rel="canonical"' dist/zh/guide/user-guide/index.html
<link rel="canonical" href="https://sdtm-pedia.pages.dev/zh/guide/user-guide/">
                                                                          ^ trailing slash
```

**Why it's HIGH not LOW**: The redirect-page canonical and the actual content-page canonical disagree on trailing-slash format. To a search engine following canonical signals:
1. `/zh/guide/` says canonical = `/zh/guide/user-guide` (no slash)
2. `/zh/guide/user-guide` 308-redirects to `/zh/guide/user-guide/` (with slash)
3. `/zh/guide/user-guide/` says canonical = `/zh/guide/user-guide/` (with slash)

This is a **canonical-points-at-redirect** chain, which Google explicitly documents as confusing for consolidation. The `<meta name="robots" content="noindex">` on the redirect page mitigates indexing, but does NOT mitigate canonical consolidation.

**Risk amplification**: Task 7.0 evidence found that ALL unmatched `/[lang]/*` paths return the same soft-404 redirect template. This means the same canonical-chain pattern applies to:
- The 4 known redirect routes (above)
- ANY future `/[lang]/<typo>/` URL (which inherits the same template)
- C-P7-1's "accept indefinitely" recommendation amplifies this finding because soft-404s ARE indexable canonical-pointers, just not direct-indexable

**Fix** (mechanical, ~3 LOC):
Either (A) add trailing slash to the redirect target so canonical matches build.format:'directory' convention, OR (B) use Astro's redirect-with-template-override to emit a real `<html>` redirect with a corrected canonical, OR (C) rely on `_routes.json` / CF Pages `_redirects` to do a real 301 (not meta-refresh).

Simplest = (A): change the redirect target from `/zh/guide/user-guide` to `/zh/guide/user-guide/`. Locate where the redirect is emitted (likely `src/pages/[lang]/guide/index.astro` or similar i18n redirect config) and add the trailing slash. One-line fix per route.

**Why fixable in Phase 7.5 instead of carrying to Phase 8**: 4 routes × 1 LOC = ~4 LOC. Search-engine indexing cycle of public release matters; getting canonical right at v1.0 launch costs effectively zero, whereas un-fixing canonical signals a few weeks post-launch costs reputation in dead-link checkers.

---

### F-2 [MEDIUM] Japanese subhead uses ASCII period, not idiomatic 「。」 — punctuation drift

**Class**: i18n quality / typographic correctness, JP-native-reader-jarring
**File**: `web/src/i18n/ui.ja.json` line 21
**Phase 7 attribution**: Introduced in 7.1 commit `3c151de`.

**Concrete evidence**:
```json
"compare.subhead": "4 プラットフォーム横並び. 次元キーワードで絞り込み.",
                                       ^                   ^
                                       ASCII .             ASCII .
```

vs every other ja string in the same file:
```json
"section.platforms.subhead": "4 つのデプロイ、それぞれの性格。",     // ←「。」
"section.compare.subhead": "やりたいことで選ぶ。",                  // ←「。」
"section.demo.subhead": "この 3 問をお試しください。10 問全てはガイドに。",  // ←「。」
"section.downloads.subhead": "セルフデプロイしましょう。",          // ←「。」
"footer.maintainer": "メンテナー: Daisy. 社内公開版。",            // ← mixed (already a smell, but `Daisy.` is a name with English-style period)
```

**Why MEDIUM not LOW**: A first-impression-Japanese reader on `/ja/compare` will read this as machine-translated. The rest of the JP UI uses 「。」 consistently (12 of 13 sentence-terminating positions). One file line that breaks convention reads as an oversight.

The Rule A spot-check in 7.1 report sampled `compare.subhead.ja` and ruled "PASS — 横並び idiomatic + プラットフォーム loanword consistent". The spot-check focused on lexical accuracy and missed the punctuation. This is a Rule A coverage gap, not a Rule A failure — see F-10.

**Fix** (mechanical, 2 char swap):
```diff
- "compare.subhead": "4 プラットフォーム横並び. 次元キーワードで絞り込み.",
+ "compare.subhead": "4 プラットフォーム横並び。次元キーワードで絞り込み。",
```

(The Japanese full-width period 「。」 also doubles as a sentence-break-no-space convention, removing the awkward space-after-period that ASCII style introduces.)

Also worth checking: `compare.subhead.zh` uses ASCII `.` too: `"四平台横向对比. 按维度关键字过滤."`. Chinese tolerates ASCII period more than JP does, but the rest of `ui.zh.json` uses `,` and `.` reasonably. Not a finding, but flag for stylistic review.

---

### F-3 [MEDIUM] Japanese placeholder convention drift — verb-stem instead of noun-form

**Class**: i18n consistency / convention drift
**File**: `web/src/i18n/ui.ja.json` line 22

**Concrete evidence**:
```json
"search.placeholder": "ドキュメント検索...",        // noun-form (検索 = search [noun])
"compare.filter.placeholder": "次元を絞り込み...",  // verb-stem (絞り込み = filter-stem)
                                  ^^^^^^^^^^^
```

Two placeholders in the same file, two different grammatical forms.

**Adversarial reading**: native-JP reader sees `次元を絞り込み...` as truncated mid-sentence ("filter dimensions [continued]..."). The `...` reads as "continued action expected", which is exactly what a placeholder should NOT do — it's a static label not a progress indicator. The `search.placeholder` form `ドキュメント検索...` reads cleanly as "search docs" + ellipsis = "type to search".

**Idiomatic fix**:
```diff
- "compare.filter.placeholder": "次元を絞り込み...",
+ "compare.filter.placeholder": "次元の絞り込み...",
```

(Noun-form 絞り込み, attached to 次元 with の. Reads as "dimension filter..." matching the search.placeholder pattern.)

OR, an alternative idiomatic form that keeps the imperative-ish flavor:
```diff
- "compare.filter.placeholder": "次元を絞り込み...",
+ "compare.filter.placeholder": "次元で絞り込む...",
```

Either fix removes the convention drift.

---

### F-4 [MEDIUM] Japanese aria-label uses finite verb instead of label-noun

**Class**: a11y / screen-reader correctness
**File**: `web/src/i18n/ui.ja.json` line 23

**Concrete evidence**:
```json
"compare.filter.label": "次元を絞り込む",
```

The 7.1 report disclosed this as "PASS with minor polish suggestion — not blocking". **Adversarial position**: aria-label is read aloud verbatim by VoiceOver / NVDA. A finite verb (`絞り込む` = "filter [conjugated, finite]") read as a label sounds like an action statement, not a control description. JP screen-reader convention for input-control labels is noun-form (`絞り込み` or `フィルター`).

**Why MEDIUM not LOW**: a11y impacts a real user class (JP-native users with screen readers). The rest of the project uses aria-labels with noun-form (`Open menu`, `Theme: system, click to switch`, `Language`). The form-drift here will be audible to a JP screen-reader user.

**Fix**:
```diff
- "compare.filter.label": "次元を絞り込む",
+ "compare.filter.label": "次元の絞り込み",
```

Or `次元フィルター` if Daisy prefers a katakana loanword for technical-term clarity.

---

### F-5 [MEDIUM] Pre-public-release WCAG 1.4.1 violation deferred (C-P6-2 carryover)

**Class**: a11y / pre-release blocker reading
**Source**: Phase 6 reviewer carryover, Phase 7 PLAN.md says "DEFER — split into Phase 8 carryover or polish (not blocking release)"

**Adversarial reading**: WCAG 1.4.1 says info conveyed by color must also be conveyed by another visual cue. The compare table's winner highlighting uses `text-accent font-bold` (color + weight). Bold-weight CAN qualify as a non-color cue per some WCAG interpretations, but only if the weight contrast is strong enough (typically requires a non-default font-weight delta). Looking at `CompareFilter.tsx`:

```tsx
className={`py-2 px-2 ${d.winners.includes(p.key) ? 'text-accent font-bold' : ''}`}
```

`font-bold` (700) vs the default `font-serif` weight (varies; Source Serif Pro probably 400). Bold-vs-regular CAN satisfy a non-color cue if the weight gap is perceptible at the rendered size. At `text-sm` (14px), 700-vs-400 IS perceptible.

**However**: text-accent is a CSS variable. If a custom theme or color-blind user override removes the accent color, the only remaining cue is `font-bold` — which is fine in that scenario. If a user keeps default theme but is red-blind / red-green color-blind, they see weight-only — still a valid signal.

**Verdict**: WCAG 1.4.1 is **probably NOT violated** at strict reading because `font-bold` IS a non-color cue. Phase 6 reviewer's classification of this as M-class (not H-class) was correct. PLAN.md's "DEFER" is **defensible** but the rationale should be stated more precisely — see C-P7-2 below. Flagged as MEDIUM here only because the PLAN.md justification is thin ("DEFER — split into Phase 8 carryover or polish"), not because the underlying issue is HIGH-class.

**Recommendation**: rewrite the PLAN.md / handoff carryover to record the WCAG analysis explicitly. Either keep the deferral with the "font-bold is a sufficient non-color cue" justification documented, OR add a `★` / `▶` glyph marker (non-color visual) to be conservative. Either is fine; the current "DEFER" without documented analysis leaves a soft spot in the audit trail.

---

### F-6 [LOW] Inherited build noise (4 redirect "no `<html>` element" warnings) unsuppressed

**Class**: build hygiene / pre-existing
**Source**: Phase 6 handoff §"Inherited build noise" — known, already deferred.
**Phase 7 attribution**: Phase 7 surfaced this in F-1 above (the redirect-page canonicals); the underlying `Astro.redirect()` template still emits warnings.

**Adversarial reading**: every CI build will continue to emit 4 noise warnings forever. Build noise has signal-to-noise cost: when REAL warnings appear (e.g. content-collection schema breakage), they get lost in the noise.

**Fix options** (from Phase 6 handoff §"Inherited build noise"):
- (a) Replace `Astro.redirect()` with explicit `*.astro` files that DO have full `<html>` (5-10 LOC × 4 files)
- (b) Configure Astro / sitemap-integration to exclude redirect routes from the warning emitter
- (c) Accept noise

PLAN.md doesn't address this. Defer-as-is is reasonable, but add to Phase 8 carryover so it doesn't drop off the radar.

---

### F-7 [LOW] README claims "Cloudflare Pages auto-deploys from `main`" — unverifiable in review

**Class**: documentation accuracy
**File**: `web/README.md` line 76
**Phase 7 attribution**: Introduced in 7.3 commit `a1ad23e`.

**Adversarial reading**: claim is plausible (CF Pages git integration is the default). But this review has no access to the CF dashboard or the deploy log. If CF Pages is actually configured with manual deploy or a different branch, the README rots on day one.

**Verification gap**: the brief specifically called this out — "(You can't verify without CF dashboard access, but flag if unverifiable.)" Flagging.

**Recommendation**: at the next CF Pages dashboard touch, confirm `main` branch + auto-deploy configured. If yes, document branch + last successful deploy timestamp in the README to make the claim falsifiable. If no, fix the README. Low ROI to fix in 7.5; medium ROI to verify before Daisy's first external announcement of the site.

---

### F-8 [LOW] `npm run build:fresh` script subtly diverges from PLAN spec

**Class**: spec-vs-implementation drift (does NOT cause regressions, just docs/audit drift)
**File**: `web/package.json` line 11

**Concrete evidence**:
- PLAN.md L132 spec: `"build:fresh": "rm -rf .astro node_modules/.astro dist && npm run build"`
- Actual: `"build:fresh": "rm -rf .astro node_modules/.astro dist && astro build && pagefind --site dist"`

These ARE equivalent IF AND ONLY IF `npm run build` = `astro build && pagefind --site dist`. Verified `package.json`:
```json
"build": "astro build && pagefind --site dist",
```

✓ Equivalent today. Risk: future edit to `build` script (e.g. add `&& cp robots.txt dist/`) would NOT propagate to `build:fresh`. The two scripts will silently diverge.

**Fix** (cleaner, ~5 char swap):
```diff
- "build:fresh": "rm -rf .astro node_modules/.astro dist && astro build && pagefind --site dist",
+ "build:fresh": "rm -rf .astro node_modules/.astro dist && npm run build",
```

Composable form. Always tracks `build` script. Trivial fix; would prevent the silent-divergence risk class.

The 7.3 evidence report didn't flag this. Worth a tiny correction in 7.5.

---

### F-9 [LOW] PLAN.md plan-deviation reason #4 hand-wavey

**Class**: plan-trace audit quality
**File**: `.work/07_website/phase7/PLAN.md` lines 19-20

**Quote**:
> 4. Master-plan §"Phase 7" is renumbered to **Phase 8 (deferred)** under this deviation. Pagefind moves down one slot; current Phase 8 (Downloads Pipeline) and Phase 9 (Deploy) shift to Phase 9/10. Updates to master plan deferred to Phase 7 close.

**Adversarial reading**: this isn't a *justification* for the deviation, it's an *administrative consequence* of the deviation. Reasons #1-#3 are real reasons (carryover prioritization + visible bug + cheap-now-expensive-later). Reason #4 is "things will renumber" — but Phase 7 close doesn't appear to have a "master plan annotated with Phase-7-renumbered" deliverable in `_progress.json`. Exit criterion #8 in PLAN.md says "Master plan annotated with Phase-7-renumbered-Pagefind-to-Phase-8 deviation note (deferred to Phase 7 close)" — at review-time, has this been done?

**Verification**: searched git status / git log for master-plan edits in Phase 7 commits. None found. The `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` is presumably untouched.

**Risk**: future Phase 8 session reads master plan §"Phase 7" Pagefind, doesn't read the website-lane handoff, gets confused about what Phase 8 should do.

**Fix at Phase 7 close** (mechanical, 1 file edit): add a 1-line annotation to master plan §"Phase 7" pointing to the Phase 7 PLAN.md deviation note. E.g. `> ⚠️ Renumbered to Phase 8 — see .work/07_website/phase7/PLAN.md §"Plan deviation flag" (2026-04-29).`

---

### F-10 [LOW] Rule A N=3 of 12 strings (25%) might be too low for translation work

**Class**: process / sample-size adequacy
**File**: `.work/07_website/phase7/PLAN.md` §"Rule A semantic spot-check"

**Adversarial reading**: F-2 (ja punctuation drift) was NOT caught by the Rule A spot-check despite the spot-check sampling `compare.subhead.ja` (the exact string with the bug). The spot-check ruled "PASS — 横並び idiomatic + プラットフォーム loanword consistent". It evaluated lexical correctness, not punctuation/typography.

This is not a Rule A failure but a **Rule A coverage gap**: the rubric for "PASS" should include typography/punctuation conformance to the surrounding dictionary's convention, not just lexical accuracy.

**Recommendation for future i18n phases**:
1. Increase N to ~50% for translation work (i18n is uniquely high-rewrite, low-volume, so per-string review is cheap)
2. Add to Rule A rubric: "punctuation matches surrounding dict convention"
3. Add to Rule A rubric: "grammatical form (noun/verb/adjective) matches the role (label/placeholder/sentence)"

Phase 7 specific: would have caught F-2 + F-3 + F-4 if rubric had been broader.

---

## D4: CF preview verification (Task 7.0) — adversarial pass

**Brief asked**: 27 probes is enough? Class missed?

**Adversarial probe-class audit**:
- ✓ Probed: trailing-slash redirect for `/[lang]/*` (with and without slash) — **27 probes**
- ✓ Probed: cross-lang redirect anomaly (none observed)
- ✓ Probed: H1 fix (changelog dual-route) — surfaced C-P7-1 incidentally
- ✓ Probed: 3 nonsense paths
- ✗ NOT probed: query strings (e.g. `/zh/?lang=en`) — re-ran live: returns 200 OK (CF preserves query through whatever Astro emits). NOT a bug, just untested.
- ✗ NOT probed: HEAD vs GET differences — `curl -sI` uses HEAD; some routes might 404 on HEAD but 200 on GET (typical CF Pages: HEAD = same as GET sans body, low risk)
- ✗ NOT probed: lang-neutral resources (`/sitemap-0.xml` `/sitemap-index.xml` `/robots.txt`) — re-ran live: all 200 + correct content-type ✓ (but worth recording in evidence for reproducibility)
- ✗ NOT probed: encoded characters / Unicode in URL paths
- ✗ NOT probed: `/[lang]/compare?dim=capacity` — does the CompareFilter island read query strings? (Quick code check: it doesn't — uses local React state. So query strings on /compare are no-ops, but worth a one-line note in C-P7-1 docs.)

**Verdict on Task 7.0**: probes are **sufficient for the C-P5-M3 trailing-slash hosting question**. C-P7-1's discovery (Astro soft-404 200) is a useful incidental, framed correctly as drift-not-regression.

The probe gaps above are LOW-severity per-class — probably not worth re-running for Phase 7. Worth folding into a "CF preview probe checklist" for future infrastructure phases.

---

## D1 (i18n key parity + correctness) — adversarial pass

**Confirmed**:
- ✓ 4 new keys in all 3 langs (`ui.zh.json`, `ui.en.json`, `ui.ja.json`)
- ✓ Key parity test in `helpers.test.ts` line 21-25 covers via `Object.keys().sort()` equality — **automatic regression test** for any future key drift
- ✓ Vitest 32/32 passing (verified independently — `bgp94id5z` background run exit 0)
- ✓ TSC 0 errors (verified independently — exit 0)
- ✓ Dist HTML grep confirms zh/en/ja strings emit on respective lang variants

**Issues found**:
- F-2 / F-3 / F-4 (ja convention drift, see above)
- ✓ NO English chrome leaks into zh/ja — confirmed via dist grep `grep -c "Filter dimensions" dist/{zh,ja}/compare/index.html` → both 0
- ✓ `<title>` matches lang-key — confirmed via grep `<title>多次元プラットフォーム比較</title>` on `dist/ja/compare/index.html`

---

## D2 (canonical URL correctness) — adversarial pass

**Confirmed**:
- ✓ 31/31 dist HTML pages have canonical
- ✓ 27 content pages: self-referential canonical with trailing-slash matching `build.format: 'directory'`
- ✓ `og:url` matches canonical (intentional per spec; same href both elements; no divergence case in this app — see commentary below)
- ✓ `Astro.site` is set in `astro.config.mjs` — fallback path-only branch in `BaseLayout` is unreachable in production (defensive only)

**Issue**: F-1 (HIGH) — see above. The 4 redirect pages canonical href has trailing-slash mismatch.

**Brief asked: is `Astro.site` fallback misleading?**
- Quick analysis: `Astro.site` is set, fallback is unreachable. If a future dev removes `site:` from config (low-likelihood, but possible during a domain rename), the canonical would render as `<link rel="canonical" href="/zh/compare/">` (relative, no protocol). Search engines treat relative canonical as relative-to-current-URL → effectively self-referential, not actively misleading.
- ✓ Defensive fallback is fine. Not a finding.

**Brief asked: og:url and canonical always same — is divergence ever needed?**
- For static documentation site: no, they should always match. Divergence cases (e.g. social-card-targeted alt URL) don't apply here.
- ✓ Same-href is the right design for this app. Not a finding.

---

## D3 (README content vs tribal-knowledge accuracy) — adversarial pass

**Verified each tribal-knowledge claim against current source**:
- ✓ "Cache invalidation requires `build:fresh`" — Phase 6.4 evidence confirms (cache-stale incident reproduced and resolved by `rm -rf .astro`)
- ✓ "Playwright `reuseExistingServer: true`" — verified `web/playwright.config.ts` line 12
- ✓ "Lang-neutral entries throw on `.md` cross-refs" — verified `web/remark-md-link-rewrite.mjs` lines 49-55 (exact throw with helpful message)
- ✓ "Adding a new doc — 4-step recipe" — verified `web/src/pages/[lang]/guide/[...slug].astro` exists; confirmed `slug:` is required in `web/src/content.config.ts` (would need to read content.config.ts for full verification, but the recipe is consistent with how Phase 6 added README/USER_GUIDE/etc.)
- ✓ "Soft-404 200 + meta-refresh" — Task 7.0 F-7.0-2 evidence confirms across 3 nonsense URLs
- ✓ External links (Astro / React / Tailwind / Vitest / Testing Library / Playwright / Pagefind) — extracted via grep, all standard project URLs (https://astro.build/, etc.) — not deep-checked but well-known
- ✓ `RELEASE.md` referenced exists at `/Users/bojiangzhang/MyProject/SDTM-compare/web/RELEASE.md` ✓
- ✓ DEMO_QUESTIONS.md path referenced exists at `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/release/v1.0/DEMO_QUESTIONS.md` ✓
- ⚠ "Cloudflare Pages auto-deploys from `main`" — F-7 unverifiable in review

**Verdict**: README is genuinely accurate at write-time. Minor F-8 (build:fresh script divergence) is the only spec-vs-impl drift. Excellent quality — the 5 tribal sections are precisely the kind of content that's normally tribal AND has rotted by month 2; verifying each one tells me they're correct NOW. Survival depends on future contributors NOT silently changing the patterns the README describes.

---

## Recommendations for Phase 7 → Phase 8 handoff

### Recommended 7.5 fix bundle (5 minutes total)

1. **F-1 fix** (or accept as deferred): adjust the 4 redirect-route canonical hrefs to match trailing-slash format. Likely 1-line edit in the redirect source file (need to grep `Astro.redirect` callsite).
2. **F-2 fix**: `ui.ja.json` line 21 — replace 2 ASCII periods with 「。」.
3. **F-3 fix**: `ui.ja.json` line 22 — `次元を絞り込み...` → `次元の絞り込み...` (or `次元で絞り込む...`).
4. **F-4 fix**: `ui.ja.json` line 23 — `次元を絞り込む` → `次元の絞り込み` (or `次元フィルター`).
5. **F-8 fix**: `package.json` line 11 — `astro build && pagefind --site dist` → `npm run build` (composable form).

If 7.5 is not run, all 4 land as Phase 8 carryover.

### Carryover IDs for Phase 8 (continuing C-P7-* namespace, C-P7-1 already exists from Task 7.0)

- **C-P7-2 [HIGH if F-1 deferred / N/A if 7.5 fixes]** — Redirect-page canonical href trailing-slash mismatch (4 routes). Pre-existing, surfaced in Phase 7 review. Fix when convenient; should be fixed before public release for SEO consolidation correctness.
- **C-P7-3 [MEDIUM if F-2/F-3/F-4 deferred]** — JP i18n convention drift on compare page chrome (3 strings × `ui.ja.json`). Punctuation, placeholder noun-form, aria-label noun-form. Polish; trivial 5-line fix.
- **C-P7-4 [MEDIUM]** — C-P6-2 WCAG 1.4.1 carryover needs documented analysis. Either explicitly justify "font-bold = sufficient non-color cue" in handoff OR add visual marker glyph. Not actually a violation per analysis but the audit trail is thin.
- **C-P7-5 [LOW]** — Master plan §"Phase 7" not yet annotated for Pagefind renumber. Phase 7 close exit criterion #8 unmet at review-time. 1-line annotation needed.
- **C-P7-6 [LOW]** — Build noise (4 redirect "no `<html>` element" warnings) — Phase 6 carryover unaddressed in Phase 7. Add to Phase 8 backlog or accept indefinitely with rationale.
- **C-P7-7 [LOW]** — Rule A rubric expansion: include punctuation/grammatical-form conformance, not just lexical accuracy. Phase 8+ i18n work should adopt expanded rubric. Increase N% for translation work.
- **C-P7-8 [LOW]** — README claim "Cloudflare Pages auto-deploys from `main`" verification with CF dashboard. Verify-or-amend before first external announcement.
- **C-P7-9 [LOW]** — `build:fresh` script composability — depend on `npm run build` rather than copying. (Subsumed by F-8 fix if 7.5 is run.)
- **C-P7-10 [LOW]** — CF preview probe checklist for future infrastructure phases (query strings / HEAD-vs-GET / encoded URLs / lang-neutral resources). Saves ~5 minutes of probe-class re-derivation in Phase 9 deploy.
- **C-P7-1** — (existing) Astro i18n soft-404 LOW — accept-as-is recommended. Documented in README (verified). No further action.

### Phase 8 entry recommendations

When Phase 8 (Pagefind, per master plan §"Phase 7" pre-renumber) starts:

1. **First action**: read `.work/07_website/phase7/_progress.json` carryover_new_phase_7 list + this report's C-P7-* carryover.
2. **Pre-flight**: confirm whether 7.5 fix bundle was run. If yes, drop C-P7-2 + C-P7-3. If no, decide whether to absorb into Phase 8.
3. **Reviewer slot for Phase 8**: 4th-family inaugural candidate. Phase 7 used `superpowers:code-reviewer`; available cross-family options for Phase 8: `superpowers:silent-failure-hunter` (deeper bug-hunt mode if Pagefind hits indexing-edge cases), `oh-my-claudecode:code-reviewer` (omc family extension), `pr-review-toolkit:silent-failure-hunter` (pr family extension), `feature-dev:silent-failure-hunter` (feature-dev family extension), or a fresh family entirely.
4. **Master plan annotation** still pending (C-P7-5). Cheapest to bundle into Phase 7 close commit.

---

## Process notes (Rule D + Rule A audit trail)

- **Rule D (writer-reviewer isolation)**: writer = main session (direct mode for 7.0-7.3 mechanical work); reviewer = `superpowers:code-reviewer` (this report) — different family from writer's tooling AND different family from prior 6 reviewers (pr ×4, feature ×1, omc ×1). Cross-family isolation maintained ✓.
- **Rule A (semantic spot-check)**: PLAN.md says N=3 of 12 strings. Sample executed in 7.1 evidence. F-10 above flags rubric coverage gap (lexical-only) that missed F-2/F-3/F-4. Not a Rule A failure (the rule was followed); it's a rule-rubric improvement opportunity.
- **Rule B (failures archive)**: PLAN.md says "none expected"; none archived; no obvious failures hidden ✓.
- **Rule C (retro)**: Phase 7 close handoff doc pending per PLAN.md exit criterion #7. This report feeds in.

---

## Pass-criteria check

- ✗ "0 HIGH findings UNLESS the finding is fixable in a small post-review patch and you'd recommend doing so before declaring Phase 7 done" — F-1 IS HIGH, IS fixable in a small patch, IS recommended.

→ **CONDITIONAL_PASS** (upgrades to PASS when F-1 + F-2 fixed in 7.5 fix bundle, OR Daisy elects PASS-with-carryover and absorbs them into Phase 8).

If Daisy prefers ship-now-fix-later: PASS-with-carryover is acceptable. The F-1 SEO chain affects 4 URLs, none of which are core-content pages; the public release reach Risk × Severity is low-to-moderate. Daisy's call.

---

## Summary

Phase 7 delivers what it promised: 4 carryover absorptions (C-P5-M3, C-P6-1, C-P6-3, C-P6-8) + a fact-correction (web/README.md exists with placeholder, not missing) + an incidental discovery (C-P7-1 Astro soft-404). All exit criteria 1-6 met; criterion 7 (handoff doc) and 8 (master plan annotation) pending at review-time.

The work is mechanically clean. The findings cluster around **typography/i18n polish on the compare page chrome** (F-2/F-3/F-4) and **a pre-existing canonical-redirect chain that Phase 7's new canonical infrastructure illuminated** (F-1). Both clusters are 5-minute fixes if you fix them in 7.5; both are tolerable-as-carryover if you'd rather sequence them into Phase 8.

The team should be proud of (a) the README — it's the genuinely-correct kind of tribal-knowledge doc that's hard to write — and (b) the disclosed-not-glossed Rule A polish item on `compare.filter.label.ja`, which adversarial review converted into 3 related findings (F-2/F-3/F-4) by widening the lens. That kind of "we noticed but didn't fix" disclosure is exactly the discipline that survives Phase 8+ scaling.

Phase 7 is fundamentally PASS-class. The 5 LOW findings are real-but-low-stakes; the 4 MEDIUM findings are quality polish; the 1 HIGH is a pre-existing bug newly visible. Recommendation: 5-minute 7.5 fix bundle, then ship.
