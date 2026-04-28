# Task 6.2 — Evidence Report (main session direct execution)

> **Task**: Expand `compare-dimensions.json` 4 → 9 dims + landing `slice(0, 4)`
> **Mode**: direct (trivial; main session per PLAN.md task table)
> **Branch**: `main` (pre-edit HEAD `c52b4a7`)
> **Verdict**: ALL verification steps PASS — ready for commit.

---

## 1. Files touched (exhaustive)

| File | Change | Lines |
|------|--------|-------|
| `web/src/data/compare-dimensions.json` | **MODIFY** — append 5 dims after existing 4 (score, subscription, internet, file-limit, worst-at) per master plan §6.2 lines 2452-2461 verbatim | +5 entries (10 → 11 lines incl wrapping `[]`) |
| `web/src/components/astro/ComparePreviewSection.astro` | **MODIFY** — `{dims.map((d) => (` → `{dims.slice(0, 4).map((d) => (` (line 29) | 1-line change |
| `.work/07_website/phase6/evidence/checkpoints/task_6_2_report.md` | **CREATE** — this report | new |

No other files touched. The 4 dim-keys preserved order (`best-at`, `capacity`, `sharing`, `anti-halluc`) so `slice(0, 4)` continues to surface the user-relevant preview set per master plan §6.2 Step 2 commentary.

---

## 2. Master plan §6.2 verbatim adherence

5 new dim entries match plan template lines 2452-2461 character-for-character (including `winners: []` for non-superlative dims like `subscription`/`worst-at`, and the mixed-language values like `chatgpt: "默认开"` for the `internet` dim — the existing 4 dims also use mixed zh/en values so this is consistent).

The plan template intentionally keeps `values` as language-agnostic short descriptors (some Chinese, some English). Reviewer 6.3 may flag this as a v1.1 i18n polish opportunity (key gap parallel to Phase 5 C-P5-L1 fallback-banner-i18n). Out-of-scope for 6.2 per the verbatim contract.

---

## 3. Verification command outputs

### Step 1 — tsc clean

```
$ npx --prefix web tsc --noEmit -p web/tsconfig.json
(zero output, zero exit code = 0 errors)
```

### Step 2 — vitest (no regression, no new tests)

```
 Test Files  8 passed (8)
      Tests  31 passed (31)
   Start at  11:12:51
   Duration  1.04s (transform 455ms, setup 950ms, import 374ms, tests 220ms, environment 5.10s)
```

Landing smoke + ComparePreviewSection-related tests still pass with the 4-row sliced preview.

### Step 3 — build green

```
[Reading languages]
Discovered 3 languages: ja, zh, en

[Building search indexes]
Total:
  Indexed 3 languages
  Indexed 30 pages
  Indexed 6461 words
  Indexed 0 filters
  Indexed 0 sorts

Finished in 0.411 seconds
```

30 pages indexed. Page count unchanged from 6.0 baseline (no new routes; only data + 1 component edit).

(4 pre-existing "no <html> element" warnings on `/`, `/zh/guide/`, `/en/guide/`, `/ja/guide/` inherited from pre-Phase-6 state — unrelated, not blocking. Flag for 6.3 as inherited issue.)

### Step 4 — Landing `/zh/` ComparePreviewSection (must show ONLY 4 dims)

```
$ for label in '最强场景' '容量上限' '团队共享' '反虚构强度' '评测得分' '套餐要求' '联网能力' '文件数上限' '最弱场景'; do
    grep -c "$label" web/dist/zh/index.html
  done
最强场景: 1
容量上限: 1
团队共享: 2   ← 1 dim row + 1 section subhead "团队共享" — expected
反虚构强度: 1
评测得分: 0   ← all 5 new dims absent on landing (slice working)
套餐要求: 0
联网能力: 0
文件数上限: 0
最弱场景: 0
```

✓ `slice(0, 4)` correctly limits the landing preview to the existing 4-dim set. The new 5 dims do NOT leak into the landing.

### Step 5 — `/zh/compare` full table (must show ALL 9 dims)

```
$ for label in '最强场景' '容量上限' '团队共享' '反虚构强度' '评测得分' '套餐要求' '联网能力' '文件数上限' '最弱场景'; do
    grep -c "$label" web/dist/zh/compare/index.html
  done
最强场景: 1
容量上限: 1
团队共享: 1
反虚构强度: 1
评测得分: 1   ← all 5 new dims present on /compare (full table)
套餐要求: 1
联网能力: 1
文件数上限: 1
最弱场景: 1
```

✓ React `CompareFilter` island (server-rendered initial state) emits all 9 rows. Client-side filter will operate on the full 9.

### Step 6 — e2e (must stay 6/6 strict)

```
Running 6 tests using 2 workers

  ✓  1 tests/e2e/lang.spec.ts:3:1 › root redirects to /zh/ (684ms)
  ✓  2 tests/e2e/smoke.spec.ts:5:5 › landing › /zh/ renders all 5 sections (1.2s)
  ✓  3 tests/e2e/smoke.spec.ts:5:5 › landing › /en/ renders all 5 sections (1.1s)
  ✓  4 tests/e2e/smoke.spec.ts:5:5 › landing › /ja/ renders all 5 sections (1.1s)
  ✓  5 tests/e2e/smoke.spec.ts:22:1 › docs reader renders user-guide in zh (175ms)
  ✓  6 tests/e2e/smoke.spec.ts:28:1 › link-resolution: every <a> in main resolves ≠404 across landing + guide + changelog (1.6s)

  6 passed (7.8s)
```

Stale `astro dev` on :4321 was killed pre-run (`lsof -ti:4321 | xargs -r kill`) per 6.0 lesson; first attempt clean, no retry needed. The link-resolution strict mode (no `.md` skip) continues to pass after JSON expansion since the 5 new dims add no new external hrefs.

---

## 4. Open questions / observations

1. **Mixed-language `values` in dim entries** — both the original 4 and the new 5 dims contain a mix of Chinese (e.g. `internet` `chatgpt: "默认开"`) and English (e.g. `score` `claude: "17/17"`) value strings. The CompareFilter renders these as-is regardless of viewing lang. v1.1 polish candidate: dim values become per-lang triples like `label`. Out-of-scope per plan; flag for 6.3.
2. **`team-sharing` dim has 2 occurrences in `/zh/` but 1 in `/zh/compare`** — the extra hit is the section subhead phrase `团队共享` matching as substring in the section title or nearby copy. Not a duplicate row. Verified by `DIMENSION` header count = 1 (only 1 preview table).
3. **Pre-existing build warnings inherited** — 4 "no <html> element" warnings (`/`, `/zh/guide/`, `/en/guide/`, `/ja/guide/`) are Phase-5-or-earlier carryover. Not introduced by 6.2; flag for 6.3 reviewer to decide whether to fix in Phase 6 fix bundle or defer.
4. **No new tests written** — plan §6.2 doesn't require any (data-only edit + 1-line slice). The existing `<CompareFilter>` test suite uses an inline 2-dim fixture and is independent of the JSON file content, so no test rewrite needed.

---

## 5. Commit (next step)

```
git add web/src/data/compare-dimensions.json \
        web/src/components/astro/ComparePreviewSection.astro \
        .work/07_website/phase6/evidence/checkpoints/task_6_2_report.md

git -c commit.gpgsign=false commit -m "07 Website Phase 6.2 — expand compare-dimensions to 9 dims (preview shows first 4 via slice)"
```
