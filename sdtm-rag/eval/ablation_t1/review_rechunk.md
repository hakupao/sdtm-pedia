# Code Review: Re-chunking Fix (per-row §一/§三 splitting)

**Reviewer:** code-reviewer agent (Rule D — independent pass, not the authoring context)
**Date:** 2026-06-08
**Files reviewed:**
- `scripts/chunkers/variable_index.py`
- `scripts/chunkers/terminology.py`
- `scripts/tests/test_variable_index.py`
- `scripts/tests/test_terminology.py`

**Total issues:** 7 (0 CRITICAL · 1 HIGH · 3 MEDIUM · 3 LOW)

---

## Stage 1 — Spec Compliance

Design intent verified against implementation:

| Requirement | Implemented? |
|---|---|
| §一 → per-variable chunks (24) | YES — `_parse_gfm_data_rows` + loop in `variable_index.py:132-159` |
| §三 → per-CT-code chunks (135) | YES — same helper, loop at `variable_index.py:198-225` |
| §二 → unchanged (63 H3 domain chunks) | YES — H3 loop untouched `variable_index.py:162-192` |
| chunk_index sequential across all three sections | YES — single `chunk_idx` counter |
| Terminology codelist chunks enriched with "Used by variable(s): …" | YES — `terminology.py:249-253` |
| Enrichment derived generically from §三 map (not hardcoded) | YES — generic `_CT_CODE_RE` + dict lookup |
| Map cached (not rebuilt per-chunk) | YES — lazy `@property ct_usage_map` with `None` sentinel |
| Graceful fallback if VARIABLE_INDEX.md missing | YES — `return {}` at `terminology.py:135-136` |

Spec compliance: **PASS**.

---

## Stage 2 — Code Quality Issues

### Issues

---

**[HIGH] `terminology.py:140-158` — `_build_ct_usage_map` uses a single `seen_separator` flag across the entire file, not scoped to §三 only**

Confidence: HIGH

The function iterates every line of VARIABLE_INDEX.md. After the first GFM separator row (in §一), `seen_separator` becomes `True` permanently. Every data row from §一 onward — including all 1499 §二 domain variable rows — is then passed through the `_CT_CODE_RE` filter. The filter (`^C\d+$` on `cells[0]`) correctly rejects §一/§二 rows because their first column is a variable name (e.g. `STUDYID`, `AESEQ`). Verified against the actual file: zero §一/§二 first-column values match `C\d+`.

**However, this is a latent correctness assumption.** If VARIABLE_INDEX.md is ever regenerated with a schema change where a §二 variable name starts with `C` followed only by digits (unlikely but possible for numeric codes), or if a new section is added between §一 and §三, the function would silently populate the map with wrong data. The function is also slightly wasteful, parsing all 1800+ rows instead of only the ~140 §三 rows.

**Fix:** Scope the parse to §三 only, analogous to how `variable_index.py` slices `text[san_start:]`. After finding the `## 三、` heading, only iterate lines from that point forward:
```python
# Skip to §三 section first
san_marker = re.search(r'^## 三、', text, re.MULTILINE)
if not san_marker:
    return {}
text = text[san_marker.start():]
# then iterate
```

---

**[MEDIUM] `variable_index.py:198-225` — §三 `ct_code` metadata field is not validated; a malformed first-column cell would store a non-`C\d+` string in Chroma metadata**

Confidence: HIGH

In the §三 loop, `ct_code` is taken directly from `cells[0]` with only a `len(cells) < 3` guard. Unlike `terminology.py` which validates `_CT_CODE_RE.match(ct_code)` before storing, `variable_index.py` stores the raw cell value into the `ct_code` metadata field without validation. If VARIABLE_INDEX.md were regenerated with a header row that leaks through (e.g. if a second separator is absent), a non-CT-code string would end up in Chroma's `ct_code` field, potentially corrupting metadata-filtered queries.

In practice the current file has a clean §三 table, but the asymmetry with `terminology.py`'s validated path is a latent bug.

**Fix:** Add the same guard used in `terminology.py`:
```python
# variable_index.py, inside the §三 loop
from scripts.chunkers.terminology import _CT_CODE_RE  # or re-declare locally
if not re.match(r'^C\d+$', ct_code):
    continue  # skip malformed or header leak rows
```

---

**[MEDIUM] `terminology.py:253` — trailing space before `\n\n` in the enrichment prepend**

Confidence: HIGH

```python
chunk_text = f"Used by variable(s): {used_by}. \n\n" + chunk_text
```

The literal `". \n\n"` contains a trailing space between `.` and `\n`. This is cosmetically harmless for retrieval but violates clean text hygiene — some embedding tokenizers treat trailing whitespace specially and it produces an inconsistent text format compared to all other chunk types. It will also cause `text.startswith("Used by variable(s):")` checks (as used in `test_terminology.py:108`) to pass while `chunk_text.split('\n')[0]` would produce `"Used by variable(s): AE.AESEV. "` with a trailing space.

**Fix:** Remove the space: `f"Used by variable(s): {used_by}.\n\n"`.

---

**[MEDIUM] `variable_index.py:83-84` — class docstring still says "§一 (1) + §二 (63 by domain) + §三 (1)" after the re-chunking**

Confidence: HIGH

```python
class VariableIndexChunker(BaseChunker):
    """Chunk VARIABLE_INDEX.md into §一 (1) + §二 (63 by domain) + §三 (1)."""
```

The class docstring was not updated when the module docstring was updated. It still describes the old 1+63+1 = 65 chunk layout, which contradicts the actual 24+63+135 = 222 behavior documented in the module docstring and tests.

**Fix:** Update to:
```python
"""Chunk VARIABLE_INDEX.md into §一 (24 per-row) + §二 (63 by domain) + §三 (135 per-row)."""
```

---

**[LOW] `variable_index.py:84` / `terminology.py:113` — `_GFM_SEP_RE` is duplicated across both files**

Confidence: HIGH

Identical regex `r"^\|[\s\-:|]+\|?\s*$"` is defined in both `variable_index.py:40` and `terminology.py:37`. The companion helper `_parse_gfm_data_rows` (which uses this regex) exists only in `variable_index.py` and is re-implemented inline in `terminology.py:_build_ct_usage_map`. This is a DRY violation: if the separator pattern ever needs to change (e.g. to handle a new alignment variant), it must be updated in two places.

**Fix:** Move `_GFM_SEP_RE` and `_parse_gfm_data_rows` to `base.py` and import from there.

---

**[LOW] `test_variable_index.py:95-105` — `test_variable_index_section1_epoch_chunk_natural_language` asserts `"44" in text` as a proxy for domain count, but this is fragile**

Confidence: MEDIUM

The string `"44"` could appear in other fields of the rendered text (e.g. if a label or domain abbreviation contained `"44"`). The current EPOCH row renders as `"EPOCH (Epoch) — Timing variable, type Char, Core Perm*. Appears in 44 SDTM domains: ..."`, so the assertion holds now, but it is testing a string fragment rather than a semantic field.

**Fix (optional):** Assert `"Appears in 44 SDTM domains" in text` which is the exact rendered phrase and is unambiguous.

---

**[LOW] `test_terminology.py:98-110` — `test_ae_terminology_c66769_enriched_with_variable_usage` is the only enrichment test; no negative test for a CT code absent from the §三 map**

Confidence: MEDIUM

There is no test verifying that a codelist chunk whose CT code has no §三 entry (i.e. `ct_usage_map.get(ct_code)` returns `None`) is emitted unchanged — i.e. that the enrichment is correctly skipped rather than prepending `"Used by variable(s): None."`. The guard `if used_by:` at `terminology.py:251` handles this correctly, but it is untested.

**Fix (optional):** Add a test that picks a codelist file containing a CT code not in VARIABLE_INDEX.md §三 and asserts its chunk does NOT start with `"Used by variable(s):"`.

---

## Positive Observations

- chunk_index sequencing is correct: a single `chunk_idx` counter increments across §一 → §二 → §三 in document order, producing 0-based sequential indices with no gaps or collisions (`variable_index.py:97, 159, 192, 225`).
- §二 domain chunks are byte-identical to the pre-refactor code — the H3 loop was not touched and uses the same `heading_positions` + `_parse_domain_h3` path.
- The `ct_usage_map` lazy property pattern is correct: `None` sentinel distinguishes "not yet built" from `{}` ("built but empty"), so the cache works even when VARIABLE_INDEX.md is absent.
- `_GFM_SEP_RE` is well-designed: it correctly matches real separator rows (`|---------|`, `:--:` alignment) and correctly rejects em-dash data rows (`| — |`), as verified against the actual file.
- The `_parse_gfm_data_rows` helper handles both trailing and leading pipe presence robustly via the two `cells[0] == ""` / `cells[-1] == ""` checks.
- Test count assertions (222, 24, 63, 135) are exact, not just `>`, which will catch future regressions immediately.
- The `TerminologyChunker.__init__` override correctly calls `super().__init__(kb_root)`, preserving all `BaseChunker` state initialization.
- No hardcoded CT codes (C66742, C66769, EPOCH) appear in production code paths — all lookups are generic via the parsed map.

---

## Open Questions (low-confidence findings — surfaced, not blocking)

None.

---

## Verdict

**CONDITIONAL PASS**

Must-fix before merging:

1. **[HIGH] `terminology.py:140`** — Scope `_build_ct_usage_map` iteration to §三 only (currently safe but relies on an undocumented assumption about §一/§二 variable names not matching `C\d+`; a future schema change could silently corrupt the map).

Should-fix (low risk but clean code):

2. **[MEDIUM] `variable_index.py:~201`** — Add `C\d+` validation guard before storing `ct_code` in §三 chunks.
3. **[MEDIUM] `terminology.py:253`** — Remove trailing space in `". \n\n"` prepend string.
4. **[MEDIUM] `variable_index.py:84`** — Update class docstring to reflect 24+63+135 layout.
