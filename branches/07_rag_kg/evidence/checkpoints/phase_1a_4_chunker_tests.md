# Phase 1A.4 Chunker Tests — Checkpoint

> 実施: 2026-05-22 — test-engineer subagent (Rule D isolation from 1A.3 executor writers)
> 上游: PLAN.md v0.2 §5 Phase 1A.4 + EXECUTION_PLAN.md §1A.4 + _batch_{a,b,c}_done.md TODOs
> 状態: ✅ **完成** — 205 passed, 2 xfailed (known findings), 0 failed

---

## 0. TL;DR (3 行)

1. **205 tests PASS, 0 FAIL** across 8 test files (7 chunker-specific + 1 integration); 2 xfail for known lb_part2/3 token overflow finding (expected, deferred to 1A.5)
2. **All 5 config locks verified by tests**: L-1 mermaid state-machine protection, L-2 GFM table protection, L-3 tiktoken cl100k (not char/4), L-4 ch04 max chunk < 8000 tokens (HARD assertion), L-5 lb_part4 codelist vs part mode
3. **Rule D satisfied**: 1A.3 writers were executor subagents; this test-engineer is different subagent_type → writer-vs-tester isolation confirmed

---

## 1. Test File Inventory

| File | Path | Tests | Coverage focus |
|------|------|------:|----------------|
| test_base.py | `scripts/tests/test_base.py` | 27 | Chunk 19 fields, to_metadata() 18 keys, count_tokens tiktoken L-3, find_mermaid_blocks L-1, find_table_blocks L-2, heading_positions, kb_commit_sha |
| test_spec.py | `scripts/tests/test_spec.py` | 12 | AE=64 chunks, file_type/domain/section/tokens, DM+LB multi-domain, to_metadata 18 keys |
| test_assumptions.py | `scripts/tests/test_assumptions.py` | 15 | AE=13 chunks, overview/item_N structure, DI+DM multi-domain, no-overview edge, non-contiguous numbering, table preservation |
| test_model.py | `scripts/tests/test_model.py` | 33 | All 6 model files (parametrized), domain=None, file_type=model, no-H2 fallback (1 chunk, section=None), to_metadata 18 keys |
| test_examples.py | `scripts/tests/test_examples.py` | 19 | TA=8/PC=14/IS=11/DS=11 chunks; PC sub_label/example_index/cdisc_section_id; IS has_table=True; DS no mermaid; L-1 mermaid byte-range protection; L-2 table protection; heading-inside-fence filter; empty file returns [] |
| test_chapters.py | `scripts/tests/test_chapters.py` | 20 | ch01=1(whole_file), ch04=47(###, L-4 max<8000 HARD), ch08=19(###), ch10>1(##), domain=None, cdisc_section_id, all tokens positive |
| test_terminology.py | `scripts/tests/test_terminology.py` | 24 | ae=4(codelist), lb_part1=1(part,part_index=1), lb_part2/3=1 xfail token overflow, lb_part4=2(codelist,L-5 critical edge), questionnaires_part1=66, supplementary_part1=27 |
| test_variable_index.py | `scripts/tests/test_variable_index.py` | 14 | Total=65, §一 section starts "§一", §二 63 domains all non-None, §三 last chunk, AE first, to_metadata 18 keys |
| test_integration.py | `scripts/tests/test_integration.py` | 38 | CHUNKER_REGISTRY 7 types, 7 samples × 5 assertions (nonzero/18 keys/tokens>0/file_type match/idempotent), 3 cross-check individual vs registry |
| **TOTAL** | | **207 collected, 205 passed, 2 xfailed** | All 7 chunkers + registry + base helpers |

---

## 2. pytest Run Output

```
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/bojiangzhang/MyProject/sdtm-pedia/branches/07_rag_kg/sdtm-rag
configfile: pyproject.toml

scripts/tests/test_assumptions.py ...............                        [  7%]
scripts/tests/test_base.py ...........................                   [ 20%]
scripts/tests/test_chapters.py ....................                      [ 29%]
scripts/tests/test_examples.py ...................                       [ 39%]
scripts/tests/test_integration.py ........................................[ 58%]
scripts/tests/test_model.py .................................            [ 74%]
scripts/tests/test_spec.py ............                                  [ 80%]
scripts/tests/test_terminology.py ............x..x...........            [ 93%]
scripts/tests/test_variable_index.py ..............                      [100%]

XFAIL test_terminology.py::test_lb_part2_chunk_size_tokens_under_8192
  Known finding: lb_part2 (378KB) single part-mode chunk >> 8191 token limit. Deferred to 1A.5.
XFAIL test_terminology.py::test_lb_part3_chunk_size_tokens_under_8192
  Known finding: lb_part3 (417KB) single part-mode chunk >> 8191 token limit. Deferred to 1A.5.

======================== 205 passed, 2 xfailed in 1.00s ========================
```

---

## 3. Coverage Matrix (7 chunkers × edge cases)

| Chunker | Chunk count | L-1 mermaid | L-2 table | L-3 tiktoken | L-4 size | L-5 part/codelist | Edge cases |
|---------|-------------|-------------|-----------|--------------|----------|-------------------|------------|
| SpecChunker | ✅ AE=64 | — | — | ✅ tokens>0 | — | — | DM+LB multi-domain |
| AssumptionsChunker | ✅ AE=13 | — | ✅ table preserved in item | ✅ tokens>0 | — | — | DI domain, no-overview edge, non-contiguous numbering |
| ModelChunker | ✅ all 6 files >0 | — | — | ✅ tokens>0 | — | — | no-H2 fallback (1 chunk, section=None) |
| ExamplesChunker | ✅ TA=8/PC=14/IS=11/DS=11 | ✅ byte-range, 0 violations | ✅ byte-range, 0 violations | ✅ tokens>0 | — | — | PC sub_label/example_index/§6.3.5.9.3; heading-inside-fence filter; empty→[] |
| ChaptersChunker | ✅ ch01=1/ch04=47/ch08=19/ch10>1 | — | — | ✅ tokens>0 | ✅ HARD assert max<8000 | — | ch10 20-50KB tier uses ## split |
| TerminologyChunker | ✅ ae=4/lb_part1=1/lb_part4=2/qs_part1=66/supp_part1=27 | — | — | ✅ tokens>0 | — | ✅ lb_part4 H2>1→codelist (L-5 critical edge) | ct_code C\d+ format; part_index; lb_part2/3 xfail |
| VariableIndexChunker | ✅ 65 total (1+63+1) | — | — | ✅ tokens>0 | — | — | §一/§二/§三 section prefixes; §二 all domains non-None |

---

## 4. Config Lock Verification Status

| Lock | Description | Test(s) covering | Status |
|------|-------------|------------------|--------|
| L-1 | mermaid 状态机 (0 嵌套) — no chunk split inside mermaid block | `test_base.py::test_find_mermaid_blocks_*` (5 tests) + `test_examples.py::test_l1_mermaid_protection_ta_no_chunk_boundary_inside_mermaid_block` | ✅ VERIFIED |
| L-2 | GFM pipe-table simple regex — no chunk split inside table block | `test_base.py::test_find_table_blocks_*` (5 tests) + `test_examples.py::test_l2_table_protection_pc_no_chunk_boundary_inside_table_block` | ✅ VERIFIED |
| L-3 | tiktoken cl100k_base (not char/4) | `test_base.py::test_count_tokens_matches_tiktoken_directly` + `test_count_tokens_not_char_divided_by_4` | ✅ VERIFIED |
| L-4 | chapters/ >50KB → ### split, max chunk < 8191 | `test_chapters.py::test_ch04_l4_lock_max_chunk_size_tokens_under_8000` (HARD assert) | ✅ VERIFIED (max=3852) |
| L-5 | terminology: H2==1 + _partN → part mode / H2>1 → codelist mode | `test_terminology.py::test_lb_part4_produces_2_chunks` + `test_lb_part4_is_codelist_mode_not_part_mode` | ✅ VERIFIED |

---

## 5. Known Findings / Deferred to 1A.5

### F-1: lb_part2/lb_part3 token overflow (XFAIL, confirmed)

- **lb_part2.md** (378KB, H2=1 → part mode): 1 chunk, `chunk_size_tokens >> 8191` embedding limit
- **lb_part3.md** (417KB, H2=1 → part mode): 1 chunk, `chunk_size_tokens >> 8191` embedding limit
- **Impact**: These chunks cannot be embedded with text-embedding-3-small (8191 token limit)
- **Fix proposal (1A.5)**: Implement N=100 table-row slicing fallback inside TerminologyChunker for part-mode files whose byte size exceeds ~50KB; use `table_chunk_idx` metadata (PLAN §6.4 already specifies this field)
- **Test evidence**: `test_terminology.py::test_lb_part2_chunk_size_tokens_under_8192` and `test_lb_part3_chunk_size_tokens_under_8192` — marked `@pytest.mark.xfail(strict=False)`

### F-2: ct_extensible always None (documented, not blocking)

- All terminology chunks have `ct_extensible=None` (1A.3 Batch C deferred: no reliable signal source in codelist body)
- **Fix proposal (1A.5/1A.6)**: Scan ~10 codelist files for "Extensible: Yes/No" pattern; if found, implement regex signal extraction in `TerminologyChunker._parse_codelist_heading`
- Test `test_terminology.py::test_ae_terminology_ct_extensible_is_none` documents this as intended current behavior

### F-3: VARIABLE_INDEX §三 single chunk (documented)

- §三 CT 交叉引用 = 1 chunk (no sub-headings detected; PLAN §6.5 expected ~5 "letter segment" chunks)
- `chunk_size_tokens` not checked against 8K limit here — **TODO for 1A.5**: verify §三 token count; if >8191, implement row-based slicing similar to lb_part2/3 fix
- Test `test_variable_index.py` documents the 65-chunk total as current correct behavior

### F-4: AE spec.md includes non-variable H3 headings (documented)

- 64 H3 chunks includes non-variable metadata headings (e.g., "### Model Definition")
- All 64 are currently chunked — whitelist filter not implemented
- **Proposal**: evaluate in 1A.6 rule-A alignment review whether non-variable H3s degrade retrieval quality

---

## 6. PASS 5 条

1. **evidence 存在** ✅ — 本文件 + `/tmp/pytest_1a4.txt` (全 run stdout)
2. **writer 产物合规** ✅ — 8 test files written, 205/205 assertable tests PASS, 2 xfail correctly marked as known findings
3. **独立 reviewer subagent PASS** ⚠️ **DEFERRED** — Per EXECUTION_PLAN §2.1 Rule D 矩阵, 1A.4 test-engineer写完后由 code-reviewer (第三 subagent_type) 审 test + chunker coverage. 本 checkpoint 为 test-engineer 产物; code-reviewer 独立审查为下一步
4. **规则 A 抽检** N/A for test code (no compression >50% of KB content; tests are deterministic assertions)
5. **用户 Bojiang 口头 ack** — pending

---

## 7. Test Files Written

| File | Absolute path |
|------|--------------|
| test_base.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_base.py` |
| test_spec.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_spec.py` |
| test_assumptions.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_assumptions.py` |
| test_model.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_model.py` |
| test_examples.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_examples.py` |
| test_chapters.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_chapters.py` |
| test_terminology.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_terminology.py` |
| test_variable_index.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_variable_index.py` |
| test_integration.py | `branches/07_rag_kg/sdtm-rag/scripts/tests/test_integration.py` |
