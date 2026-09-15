# DM1 — Domain-Level Mapping Retrieval Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Questions of the form "which of THIS study's data belong in SDTM domain X" get a context that contains the domain's definition chunk plus candidate cards from more than one form, for any domain and any phrasing (Chinese / Japanese / English, upper or lower case code).

**Architecture:** Four deterministic retrieval-layer changes inside the existing S1 structured-lookup + hybrid pipeline (case/anchor-aware domain detection; one reserved seat for the domain's `assumptions.md` first item; meta.yaml-driven query expansion applied to dense+BM25 only; query-side BM25 stopwords), one prompt bullet, one structured log line, and a new cross-domain federated gold set used as the gate. No KB content change, no re-ingest, no LLM in the new code paths.

**Tech Stack:** Python 3.14, FastAPI, chromadb, bm25s, structlog, pytest (`scripts/tests/`). Repo root for all paths below: `/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag`. KB: `/Users/bojiangzhang/MyProject/sdtm-pedia/knowledge_base`.

**Spec:** `sdtm-rag/PLAN_domain_mapping.md` (Tier 2 plan, decisions D1–D6) and root-cause evidence `sdtm-rag/evidence/checkpoints/dogfood_ds_domain_2026-09-15.md`.

## Global Constraints

- Zero regression on `eval/test_set_v3.yml` (140 q, baseline 99.17% source recall, run `eval/runs/dm1_cdisc_before.json`) and `data/study/st01/eval/test_set_study_v2.yml` (48 q, baseline 87.5%, run `data/study/st01/eval/runs/dm1_study_before.json`). "Zero regression" = per-question recall IDENTICAL or better; any question that drops → the task is archived under `evidence/failures/dm1_task<N>_attempt_<X>.md` and redone.
- Never touch `knowledge_base/`, never re-ingest chroma, never change `data/study/st01/docs` seat rules.
- Every new behaviour has a kill switch in `server/config.py` (`SDTM_RAG_` env prefix) defaulting to on.
- The user-visible question sent to the LLM is never rewritten; expansion text is used for retrieval only.
- Logs must not contain frame locals (`exc_info=True` near the question is forbidden, see `server/federation.py:142-149`).
- Tests live in `scripts/tests/`; run with `.venv/bin/python -m pytest scripts/tests/<file> -q`. No shared fixtures; embedding-free `RAGEngine` is built with `RAGEngine.__new__` + hand-set attributes (pattern: `scripts/tests/test_rag_variable_index_sections.py:37-42`).
- Commit after each task (one commit per task, message prefix `feat(rag): DM1 T<N>`), no push until the unit closes.
- Writer and reviewer are different agents (Rule D). The gold set (Task 2) is authored by an agent that has not read `server/`.

---

### Task 1: Structured log line for `/api/ask_stream` (D6)

**Files:**
- Modify: `server/router.py:554` (insert after the `sources = [...]` list, before `def sse`)
- Test: `scripts/tests/test_ask_stream_log.py` (new)

**Interfaces:**
- Produces: one structlog event `ask_stream` with keys `question` (≤100 chars), `corpus` (`routed`, may be `None`), `n_chunks` (int), `chunk_ids` (list[str]).

- [ ] **Step 1: Write the failing test**

Look at `scripts/tests/test_ask_stream.py:1-60` for how the app + fake `rag`/`federation` are assembled (bare FastAPI + `app.state.*` fakes, no lifespan). Reuse that assembly verbatim in the new file, then:

```python
# scripts/tests/test_ask_stream_log.py
import structlog
from structlog.testing import capture_logs

# copy the app/client fixture construction from test_ask_stream.py here
# (fake federation whose retrieve() returns (chunks, "both"))

def test_ask_stream_logs_question_corpus_and_chunk_ids(client):
    with capture_logs() as logs:
        r = client.post("/api/ask_stream", json={"question": "本研究中，哪些数据适合进入 sdtm 的 ds domain？"})
        assert r.status_code == 200
        list(r.iter_lines())  # drain the SSE stream
    ev = [e for e in logs if e["event"] == "ask_stream"]
    assert len(ev) == 1
    assert ev[0]["question"].startswith("本研究中")
    assert len(ev[0]["question"]) <= 100
    assert ev[0]["corpus"] == "both"
    assert ev[0]["n_chunks"] == len(ev[0]["chunk_ids"]) > 0
    assert "answer" not in ev[0]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest scripts/tests/test_ask_stream_log.py -q`
Expected: FAIL, `assert len(ev) == 1` with `ev == []`.

- [ ] **Step 3: Implement**

In `server/router.py`, directly after the `sources = [...]` block (ends line 554):

```python
    # DM1 D6: 问句落盘 (前 100 字 + 判库 + chunk id), 不记答案. 没有这一行, dogfood ⚑ 的
    # 第一轮原句就永久丢失, 只能用重构句复现 (evidence/checkpoints/dogfood_ds_domain_2026-09-15.md).
    log.info(
        "ask_stream", question=body.question[:100], corpus=routed,
        n_chunks=len(chunks), chunk_ids=[c.chunk_id for c in chunks],
    )
```

- [ ] **Step 4: Run tests**

Run: `.venv/bin/python -m pytest scripts/tests/test_ask_stream_log.py scripts/tests/test_ask_stream.py -q`
Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add server/router.py scripts/tests/test_ask_stream_log.py
git commit -m "feat(rag): DM1 T1 ask_stream 落盘问句/判库/chunk id (D6)"
```

---

### Task 2: Cross-domain mapping gold set and its "before" numbers

**Files:**
- Create (by the blind writer agent, already dispatched): `data/study/st01/eval/test_set_domain_mapping_v1.yml`, `data/study/st01/eval/test_set_domain_mapping_v1_NOTES.md`
- Create: `data/study/st01/eval/runs/dm1_mapping_before.json`

**Interfaces:**
- Consumes: `eval/run_eval.py --federated --corpus both` (existing), `eval/lint_gold.py` (existing; study-card golds only).
- Produces: the gate file used by Tasks 3–6 and 8.

- [ ] **Step 1: Validate the YAML loads and the golds exist**

```bash
.venv/bin/python - <<'EOF'
import yaml, pathlib
qs = yaml.safe_load(open("data/study/st01/eval/test_set_domain_mapping_v1.yml"))
assert len(qs) == 8, len(qs)
kb = pathlib.Path("../knowledge_base"); cards = pathlib.Path("data/study/st01/cards")
for q in qs:
    assert q["category"] == "domain_mapping" and q["domain"], q["id"]
    srcs = q["expected_sources"]
    assert any(s.startswith("domains/") and s.endswith("/assumptions.md") for s in srcs), q["id"]
    for s in srcs:
        p = (kb / s) if s.startswith("domains/") else (cards / s)
        assert p.exists(), (q["id"], s)
    if q["domain"] == "DS":
        forms = {s.split("__")[1] for s in srcs if s.startswith("st01__")}
        assert len(forms) >= 3, (q["id"], forms)
print("ok", [q["id"] for q in qs])
EOF
```
Expected: `ok [...]` with 8 ids. Also run `.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_domain_mapping_v1.yml --help >/dev/null` is not needed; `load_test_set` raises on unknown `expected*` keys, so the run in Step 2 doubles as schema validation. Note `domain` is a doc-only field for the parser (it only rejects unknown keys starting with `expected`).

- [ ] **Step 2: Run the "before" gate**

```bash
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_domain_mapping_v1.yml \
  --retrieval-only --hybrid --structured-lookup --study-lookup \
  --federated --corpus both --output data/study/st01/eval/runs/dm1_mapping_before.json \
  > data/study/st01/eval/runs/dm1_mapping_before.log 2>&1; grep -E "Source recall|src=" data/study/st01/eval/runs/dm1_mapping_before.log
```
Expected: a low number (the DS questions should miss `domains/DS/assumptions.md` and the RCT/F_REG/OC cards). Record `source_recall_avg` into `_progress_domain_mapping.json` → `gates.mapping_v1_before`. If `--study-lookup` errors under `--federated`, drop the flag (help text at `eval/run_eval.py:801-803` says it is accepted with `--federated`).

- [ ] **Step 3: Commit the gold set**

```bash
git add data/study/st01/eval/test_set_domain_mapping_v1.yml data/study/st01/eval/test_set_domain_mapping_v1_NOTES.md data/study/st01/eval/runs/dm1_mapping_before.json _progress_domain_mapping.json
git commit -m "feat(rag): DM1 T2 域级映射 gold v1 (8q, 5 域, 盲出题) + before 基线"
```

---

### Task 3: Case- and anchor-aware domain code detection (D1)

**Files:**
- Modify: `server/structured_lookup.py:58` (constants area) and `:370-382` (`_query_domains`)
- Test: `scripts/tests/test_structured_lookup.py` (append a class)

**Interfaces:**
- Produces: `StructuredLookup._query_domains(query) -> list[str]` now also returns codes written in lower/mixed case **when anchored** by a domain word (`域`, `ドメイン`, `データセット`, `domain(s)`, `dataset(s)`) or prefixed by `sdtm`/`cdisc`. Uppercase behaviour unchanged.

- [ ] **Step 1: Write the failing tests**

Append to `scripts/tests/test_structured_lookup.py`:

```python
class TestAnchoredLowercaseCodes:
    """DM1 D1: 2-8 letter codes in any case count as domain references when a
    domain word follows them or sdtm/cdisc precedes them. Unanchored lowercase
    never matches (English words like 'is'/'or' collide with real codes IS/OR)."""

    @pytest.mark.parametrize("q,code", [
        ("本研究中，哪些数据适合进入 sdtm 的 ds domain？", "DS"),
        ("DS域にはどんなデータが入りますか", "DS"),
        ("aeドメインに入る項目は？", "AE"),
        ("what goes into the dm dataset for our study", "DM"),
        ("SDTM的lb域应该包含本研究哪些数据", "LB"),
    ])
    def test_anchored_code_resolves(self, lookup, q, code):
        assert code in lookup._query_domains(q)
        assert f"domains/{code}/spec.md" in lookup.resolve(q)

    @pytest.mark.parametrize("q", [
        "is the dataset required?",          # 'is' collides with IS
        "or the domain must be listed",      # 'or' collides with OR
        "ds without any anchor word",
    ])
    def test_unanchored_or_stopword_code_does_not_resolve(self, lookup, q):
        assert not any(c in ("IS", "OR", "DS") for c in lookup._query_domains(q))

    def test_uppercase_behaviour_unchanged(self, lookup):
        assert lookup._query_domains("What are the required variables in the DM domain?") == ["DM"]
```

- [ ] **Step 2: Run to verify failure**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py -q -k Anchored`
Expected: the `test_anchored_code_resolves` cases FAIL (lowercase not detected; `DS域` fails because `\b` does not separate `S` from `域`).

- [ ] **Step 3: Implement**

Near line 58 of `server/structured_lookup.py` add:

```python
# DM1 D1 — domain code written in any case, but ONLY with a domain anchor.
# `\b` is useless before CJK (`DS域`: S and 域 are both \w), hence the lookarounds.
_DOMAIN_WORD = r"(?:域|ドメイン|データセット|domains?|datasets?)"
_ANCHORED_CODE_RE = re.compile(
    rf"(?<![A-Za-z0-9])([A-Za-z]{{2,8}})(?![A-Za-z0-9])\s*{_DOMAIN_WORD}",
    re.IGNORECASE,
)
_PREFIXED_CODE_RE = re.compile(
    r"(?:sdtm|cdisc)\s*(?:的|の|'s)?\s*(?<![A-Za-z0-9])([A-Za-z]{2,8})(?![A-Za-z0-9])",
    re.IGNORECASE,
)
# lowercase candidates that are ordinary English words; a real code spelled in
# lowercase and colliding with these (IS, OR, DO, ...) must be written uppercase.
_LOWER_CODE_BLOCKLIST = frozenset({
    "is", "or", "do", "to", "in", "on", "at", "be", "by", "as", "an", "if", "it",
    "no", "of", "so", "us", "we", "my", "me", "up", "the", "and", "for", "our",
})
```

Replace `_query_domains` (`:370-382`) with:

```python
    def _query_domains(self, query: str) -> list[str]:
        """Known SDTM domain codes referenced by the query, de-duped. Order:
        uppercase code tokens, then anchored/prefixed codes in any case (DM1 D1),
        then long names. All meta-derived, no hardcoded names."""
        out: list[str] = []
        for tok in _QUERY_VAR_TOKEN_RE.findall(query):
            if tok in self.domain_to_spec and tok not in out:
                out.append(tok)
        for rx in (_ANCHORED_CODE_RE, _PREFIXED_CODE_RE):
            for raw in rx.findall(query):
                if raw.lower() in _LOWER_CODE_BLOCKLIST and not raw.isupper():
                    continue
                code = raw.upper()
                if code in self.domain_to_spec and code not in out:
                    out.append(code)
        for code in self._query_longname_domains(query):
            if code not in out:
                out.append(code)
        return out
```

- [ ] **Step 4: Run the whole lookup test file**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py -q`
Expected: all PASS.

- [ ] **Step 5: Regression gate (CDISC 140 + mapping 8)**

```bash
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup \
  --output eval/runs/dm1_cdisc_t3.json > eval/runs/dm1_cdisc_t3.log 2>&1
.venv/bin/python eval/compare_runs.py eval/runs/dm1_cdisc_before.json eval/runs/dm1_cdisc_t3.json
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_domain_mapping_v1.yml --retrieval-only --hybrid \
  --structured-lookup --study-lookup --federated --corpus both --output data/study/st01/eval/runs/dm1_mapping_t3.json \
  > data/study/st01/eval/runs/dm1_mapping_t3.log 2>&1; grep "Source recall" data/study/st01/eval/runs/dm1_mapping_t3.log
```
Expected: compare_runs shows 0 questions regressed (check `eval/compare_runs.py --help` for its exact output; if it lacks a per-question diff, use the inline script in Task 8 Step 1). Mapping recall ≥ before.

- [ ] **Step 6: Commit**

```bash
git add server/structured_lookup.py scripts/tests/test_structured_lookup.py eval/runs/dm1_cdisc_t3.json data/study/st01/eval/runs/dm1_mapping_t3.json
git commit -m "feat(rag): DM1 T3 域码任意大小写+锚定识别 (D1); 140q 零回归"
```

---

### Task 4: Reserved seat for the domain definition chunk (D2)

**Files:**
- Modify: `server/structured_lookup.py` (add `domain_definition_targets`), `server/rag.py:434-480` (`_apply_structured_lookup`), `server/rag.py:82` (constants), `server/config.py` (kill switch)
- Test: `scripts/tests/test_rag_domain_definition_seat.py` (new), `scripts/tests/test_structured_lookup.py` (append)

**Interfaces:**
- Produces: `StructuredLookup.domain_definition_targets(query) -> list[str]` returning `domains/<X>/assumptions.md` for each named domain (≤ `_MAX_DOMAIN_SPECS`) when the query names no known variable (domain-level ask); `[]` otherwise.
- Produces: `RAGEngine._definition_chunk(rel_path) -> RetrievedChunk | None` — the chunk of that file whose `section == "item_1"`, else `"overview"`, else `None`.
- Setting: `domain_definition_seat_enabled: bool = True` in `Settings`; `RAGEngine.__init__` param `domain_definition_seat: bool = True`, wired in `server/main.py` (cdisc engine only; study engine has no structured lookup) and `eval/run_eval.py` cdisc engine construction (default from settings).

- [ ] **Step 1: Failing test for the lookup side**

Append to `scripts/tests/test_structured_lookup.py`:

```python
class TestDomainDefinitionTargets:
    def test_domain_level_ask_returns_assumptions(self, lookup):
        q = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"
        assert lookup.domain_definition_targets(q) == ["domains/DS/assumptions.md"]

    def test_variable_level_ask_returns_nothing(self, lookup):
        q = "What is AETERM and what are its variable attributes in the AE domain?"
        assert lookup.domain_definition_targets(q) == []

    def test_capped_at_max_domain_specs(self, lookup):
        q = "compare the AE, CM, EX and LB domains for our study"
        assert len(lookup.domain_definition_targets(q)) == lookup._MAX_DOMAIN_SPECS
```

- [ ] **Step 2: Failing test for the engine side (embedding-free)**

```python
# scripts/tests/test_rag_domain_definition_seat.py
from pathlib import Path
import server.rag as rag_mod
from server.rag import RetrievedChunk

KB = Path("/kb")
ABS = str((KB / "domains/DS/assumptions.md").resolve())

class _FakeCollection:
    def __init__(self, rows):
        self.rows = rows  # list of (id, doc, meta)
    def get(self, where=None, include=None, **_):
        def ok(meta):
            conds = where.get("$and", [where]) if where else []
            return all(meta.get(k) == v for c in conds for k, v in c.items())
        sel = [r for r in self.rows if ok(r[2])]
        return {"ids": [r[0] for r in sel], "documents": [r[1] for r in sel],
                "metadatas": [r[2] for r in sel]}

def _engine(rows):
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng.kb_root = KB
    eng.collection = _FakeCollection(rows)
    eng.domain_definition_seat = True
    return eng

def _chunk(cid, text="x", **meta):
    return RetrievedChunk(chunk_id=cid, source=meta.get("source", "s"), domain=meta.get("domain"),
                          file_type=meta.get("file_type"), section=meta.get("section"),
                          similarity=0.5, text=text)

ROWS = [
    ("domains/DS/assumptions.md#0", "DS — Assumptions", {"source": ABS, "domain": "DS", "file_type": "assumptions", "section": "overview"}),
    ("domains/DS/assumptions.md#1", "The Disposition (DS) dataset provides an accounting ...", {"source": ABS, "domain": "DS", "file_type": "assumptions", "section": "item_1"}),
]

def test_definition_chunk_prefers_item_1():
    ch = _engine(ROWS)._definition_chunk("domains/DS/assumptions.md")
    assert ch.chunk_id == "domains/DS/assumptions.md#1" and ch.via_lookup and ch.section == "item_1"

def test_definition_chunk_falls_back_to_overview():
    ch = _engine(ROWS[:1])._definition_chunk("domains/DS/assumptions.md")
    assert ch.chunk_id == "domains/DS/assumptions.md#0"

def test_definition_chunk_none_when_file_has_no_chunks():
    assert _engine([])._definition_chunk("domains/DS/assumptions.md") is None

def test_single_spec_seat_count_is_unchanged(monkeypatch):
    """1 definition + (N-1) spec rows == N seats: the seat comes out of S1's own quota."""
    eng = _engine(ROWS)
    class _SL:
        _MAX_DOMAIN_SPECS = 3
        def resolve(self, q): return ["domains/DS/spec.md"]
        def domain_definition_targets(self, q): return ["domains/DS/assumptions.md"]
    eng._structured_lookup = _SL()
    seen = {}
    def fake_file_lookup(query, rel_path, n, query_embedding=None):
        seen["n"] = n
        return [_chunk(f"{rel_path}#{i}", source=rel_path) for i in range(n)]
    eng._lookup_chunks_for_file = fake_file_lookup
    eng._lookup_chunks_for_variable_index = lambda *a, **k: []
    cosine = [_chunk(f"c{i}") for i in range(20)]
    out = eng._apply_structured_lookup("哪些数据进 DS domain", cosine, None, 15)
    assert seen["n"] == rag_mod.RAGEngine._SINGLE_DOMAIN_SPEC_CHUNKS - 1
    assert out[0].chunk_id == "domains/DS/assumptions.md#1"
    assert sum(c.via_lookup for c in out) == rag_mod.RAGEngine._SINGLE_DOMAIN_SPEC_CHUNKS
    assert len(out) == 15

def test_file_type_filter_other_than_assumptions_skips_seat():
    eng = _engine(ROWS)
    class _SL:
        _MAX_DOMAIN_SPECS = 3
        def resolve(self, q): return ["domains/DS/spec.md"]
        def domain_definition_targets(self, q): return ["domains/DS/assumptions.md"]
    eng._structured_lookup = _SL()
    eng._lookup_chunks_for_file = lambda query, rel_path, n, query_embedding=None: [_chunk(f"{rel_path}#{i}") for i in range(n)]
    eng._lookup_chunks_for_variable_index = lambda *a, **k: []
    out = eng._apply_structured_lookup("q DS domain", [_chunk("c")], {"file_type": "spec"}, 15)
    assert all("assumptions" not in c.chunk_id for c in out)
```

Run: `.venv/bin/python -m pytest scripts/tests/test_rag_domain_definition_seat.py scripts/tests/test_structured_lookup.py -q -k "Definition or definition"`
Expected: FAIL with AttributeError (`domain_definition_targets` / `_definition_chunk` missing).

- [ ] **Step 3: Implement the lookup side**

In `server/structured_lookup.py`, inside `class StructuredLookup` next to `resolve`:

```python
    def domain_definition_targets(self, query: str) -> list[str]:
        """DM1 D2: `domains/<X>/assumptions.md` for each domain the query names,
        only when the ask is domain-level (no known variable token in the query —
        "what goes into DS" yes, "what is DSDECOD" no). Capped like the spec channel."""
        if self._query_variables(query):
            return []
        return [f"domains/{d}/assumptions.md"
                for d in self._query_domains(query)[: self._MAX_DOMAIN_SPECS]]
```

Check `_query_variables` (used at `structured_lookup.py:353`) returns only *known* variables (meta-derived). If it returns raw uppercase tokens, filter with the same known-variable set that `variable_index_anchors` uses.

- [ ] **Step 4: Implement the engine side**

`server/config.py`: add next to `structured_lookup_enabled` (line ~167):
```python
    domain_definition_seat_enabled: bool = True  # DM1 D2: S1 命中域时保底带 assumptions 首条
```
`server/rag.py`: add `domain_definition_seat: bool = True` to `RAGEngine.__init__` and store `self.domain_definition_seat = domain_definition_seat`. Wire `domain_definition_seat=s.domain_definition_seat_enabled` in `server/main.py` cdisc engine (`main.py:124-140`) and in `eval/run_eval.py` cdisc engine construction (follow how `structured_lookup_enabled` is passed there).

Add to `RAGEngine`:

```python
    def _definition_chunk(self, rel_path: str) -> RetrievedChunk | None:
        """The domain-definition chunk of `rel_path` (section item_1, else overview).
        Literal section pin, no similarity search: the definition is always the first
        item and a cosine pick inside assumptions.md tends to land on examples."""
        abs_source = str((self.kb_root / rel_path).resolve())
        for section in ("item_1", "overview"):
            res = self.collection.get(
                where={"$and": [{"source": abs_source}, {"section": section}]},
                include=["documents", "metadatas"],
            )
            if res["ids"]:
                meta = res["metadatas"][0]
                return RetrievedChunk(
                    chunk_id=res["ids"][0], source=meta.get("source", abs_source),
                    domain=meta.get("domain"), file_type=meta.get("file_type"),
                    section=meta.get("section"), similarity=1.0,
                    text=res["documents"][0], via_lookup=True,
                )
        return None
```

Modify `_apply_structured_lookup` (`rag.py:434-480`): after `single_spec = ...` insert

```python
        # DM1 D2: domain-level ask → the domain's definition chunk takes the FIRST
        # seat. In the single-spec case it comes out of S1's own N seats (N-1 spec
        # rows), so total lookup seats do not grow; multi-domain asks add one seat
        # per domain (≤ _MAX_DOMAIN_SPECS).
        def_chunks: list[RetrievedChunk] = []
        ft = (where or {}).get("file_type")
        if getattr(self, "domain_definition_seat", True) and ft in (None, "assumptions"):
            for rel in self._structured_lookup.domain_definition_targets(query):
                ch = self._definition_chunk(rel)
                if ch is not None:
                    def_chunks.append(ch)
        spec_n = self._SINGLE_DOMAIN_SPEC_CHUNKS - (1 if (single_spec and def_chunks) else 0)
```
and change `n = self._SINGLE_DOMAIN_SPEC_CHUNKS if single_spec else 1` to `n = spec_n if single_spec else 1`, and build `lookup_chunks` starting from `def_chunks` (`lookup_chunks: list[RetrievedChunk] = list(def_chunks)`). Keep the `if not lookup_chunks: return cosine[:k]` guard.

- [ ] **Step 5: Run tests**

Run: `.venv/bin/python -m pytest scripts/tests/test_rag_domain_definition_seat.py scripts/tests/test_structured_lookup.py scripts/tests/test_rag_variable_index_sections.py -q`
Expected: all PASS.

- [ ] **Step 6: Regression gate**

Same three commands as Task 3 Step 5 with suffix `_t4`. Expected: 140q zero regression; mapping gold: every DS question now hits `domains/DS/assumptions.md`; `single_domain` category in v3 must stay 100%.

- [ ] **Step 7: Commit**

```bash
git add server/structured_lookup.py server/rag.py server/config.py server/main.py eval/run_eval.py scripts/tests/test_rag_domain_definition_seat.py scripts/tests/test_structured_lookup.py eval/runs/dm1_cdisc_t4.json data/study/st01/eval/runs/dm1_mapping_t4.json
git commit -m "feat(rag): DM1 T4 域级定义保底席 (D2): S1 命中域且域级问法时 assumptions item_1 占首席; 140q 零回归"
```

---

### Task 5: Deterministic domain query expansion for dense + BM25 (D3)

**Files:**
- Create: `server/domain_expand.py`
- Modify: `server/rag.py:362-432` (`retrieve`), `RAGEngine.__init__`; `server/main.py` (both engines); `eval/run_eval.py` (both engine constructions); `server/config.py`
- Test: `scripts/tests/test_domain_expand.py` (new)

**Interfaces:**
- Produces: `server/domain_expand.py::DomainExpander(store: MetaStore, lookup: StructuredLookup)` with `expand(query: str) -> str` returning `""` or `"<query> <Label> (<structure>)…"` for ≤3 named domains. Detection reuses `lookup._query_domains` so Task 3's anchors apply.
- `RAGEngine.__init__(..., domain_expander=None)`; inside `retrieve`, `q_ret = self._domain_expander.expand(query) if self._domain_expander else query`; `q_ret` feeds `_embed_query`, `_search`, `_bm25_search`; the original `query` still feeds `_apply_structured_lookup` and `_apply_study_lookup` (their resolve logic is token-based and must not see the appended English).
- Setting: `domain_expand_enabled: bool = True`.

- [ ] **Step 1: Failing tests**

```python
# scripts/tests/test_domain_expand.py
from pathlib import Path
import pytest
from server.config import settings
from server.meta_store import MetaStore
from server.structured_lookup import StructuredLookup
from server.domain_expand import DomainExpander

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"

@pytest.fixture(scope="module")
def expander():
    store = MetaStore(settings.meta_path)
    return DomainExpander(store, StructuredLookup(KB_ROOT, store))

def test_ds_lowercase_expands_with_label_and_structure(expander):
    q = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"
    out = expander.expand(q)
    assert out.startswith(q)
    assert "Disposition" in out
    assert "protocol milestone" in out  # from meta.yaml structure field

def test_no_domain_returns_query_unchanged(expander):
    q = "What does AETERM contain?"
    assert expander.expand(q) == q

def test_expansion_is_capped_and_deterministic(expander):
    q = "compare AE, CM, EX, LB and VS for our study"
    a, b = expander.expand(q), expander.expand(q)
    assert a == b
    assert a.count("(") <= 3

def test_expansion_never_adds_uppercase_variable_tokens(expander):
    """The appended text must not create new S1 variable hits if someone feeds it
    back into resolve(): labels/structures are prose, but guard the invariant."""
    import re
    q = "what belongs in the DS domain"
    extra = expander.expand(q)[len(q):]
    assert not re.search(r"\b[A-Z][A-Z0-9]{2,}\b", extra)
```

Run: `.venv/bin/python -m pytest scripts/tests/test_domain_expand.py -q` → FAIL (module missing).

- [ ] **Step 2: Implement the expander**

```python
# server/domain_expand.py
"""DM1 D3 — deterministic domain-code query expansion (retrieval side only).

A question like「sdtm 的 ds domain」carries one informative token, a 2-letter
code that is nearly invisible to both the embedding and BM25. Appending the
domain's official label and record structure from meta.yaml gives dense and
lexical search real words to match ("Disposition", "protocol milestone") without
an LLM and without rewriting what the user asked. The expanded text is used for
retrieval only; the LLM still sees the original question.
"""
from __future__ import annotations

from server.meta_store import MetaStore
from server.structured_lookup import StructuredLookup

_MAX_DOMAINS = 3


class DomainExpander:
    def __init__(self, store: MetaStore, lookup: StructuredLookup):
        self._store = store
        self._lookup = lookup

    def expand(self, query: str) -> str:
        parts: list[str] = []
        for code in self._lookup._query_domains(query)[:_MAX_DOMAINS]:
            info = self._store.domain_info(code)
            label = (info.get("label") or "").strip()
            structure = (info.get("structure") or "").strip()
            if not label:
                continue
            parts.append(f"{label} ({structure})" if structure else label)
        return f"{query} {' '.join(parts)}" if parts else query
```

- [ ] **Step 3: Wire into `RAGEngine.retrieve`**

In `server/rag.py`:
- `__init__`: add param `domain_expander=None`, store as `self._domain_expander`.
- At the top of `retrieve` (after `where = ...`): `q_ret = self._domain_expander.expand(query) if self._domain_expander else query`.
- Replace `query` with `q_ret` in: `self._embed_query(query)`, every `self._search(q, ...)` / `self._search(query, ...)` call in the `none`/hybrid branches, and `self._bm25_search(query, ...)`. Leave `_apply_structured_lookup(query, ...)`, `_apply_study_lookup(query, ...)` and the multiquery/hyde branches (production off) on the original `query`; those branches already pass `query_embedding=(q_emb if q == query ...)` — keep the comparison against `query` so the reused embedding still matches only the unexpanded original (or switch both to `q_ret` consistently; do not mix).

`server/config.py`: `domain_expand_enabled: bool = True`.

`server/main.py`: after the cdisc engine is built and `StructuredLookup` exists (see how `structured_lookup_enabled` constructs it inside `RAGEngine.__init__`; if the lookup object is only reachable as `app.state.rag._structured_lookup`, build the expander as `DomainExpander(MetaStore(s.meta_path), app.state.rag._structured_lookup)` and assign `app.state.rag._domain_expander = expander`), and pass the **same** expander object to the study engine (`rag_study._domain_expander = expander`) and to the docs engine created by `make_docs_engine` if it constructs its own `RAGEngine` (check `server/study_corpus.py`; the docs engine shares `study_levers`, so add `domain_expander` to that dict if `RAGEngine` accepts it, otherwise set the attribute after construction). Gate all of this on `s.domain_expand_enabled`.

`eval/run_eval.py`: mirror the same wiring for the cdisc engine and, under `--federated`, the study and docs engines. Add `--no-domain-expand` (store_true) that forces it off for A/B; default follows `settings.domain_expand_enabled`.

- [ ] **Step 4: Tests**

Run: `.venv/bin/python -m pytest scripts/tests/test_domain_expand.py scripts/tests/test_main_study_lookup_wiring.py scripts/tests/test_main_study_docs_wiring.py scripts/tests/test_docs_engine_parity.py scripts/tests/test_run_eval_federated.py -q`
Expected: PASS. If `test_docs_engine_parity.py` pins byte-identity between study and docs engines, the expander must be attached to both (same object) — that is the intended state.

- [ ] **Step 5: Regression gates (all three sets)**

```bash
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup \
  --output eval/runs/dm1_cdisc_t5.json > eval/runs/dm1_cdisc_t5.log 2>&1
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid \
  --study-lookup --collection study_st01 --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/dm1_study_t5.json > data/study/st01/eval/runs/dm1_study_t5.log 2>&1
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_domain_mapping_v1.yml --retrieval-only --hybrid \
  --structured-lookup --study-lookup --federated --corpus both --output data/study/st01/eval/runs/dm1_mapping_t5.json \
  > data/study/st01/eval/runs/dm1_mapping_t5.log 2>&1
grep "Source recall" eval/runs/dm1_cdisc_t5.log data/study/st01/eval/runs/dm1_study_t5.log data/study/st01/eval/runs/dm1_mapping_t5.log
```
Expected: 140q and 48q zero regression per question; mapping: study-side candidate cards (RCT/F_REG/OC for DS) begin to appear. If either baseline regresses, archive under `evidence/failures/dm1_task5_attempt_1.md` with the per-question diff and try the narrower variant "label only, no structure" before anything else.

- [ ] **Step 6: Commit**

```bash
git add server/domain_expand.py server/rag.py server/config.py server/main.py eval/run_eval.py scripts/tests/test_domain_expand.py eval/runs/dm1_*_t5.json data/study/st01/eval/runs/dm1_study_t5.json
git commit -m "feat(rag): DM1 T5 域码确定性扩写 (D3): meta.yaml label+structure 仅喂 dense/BM25; 140q+48q 零回归"
```

---

### Task 6: Query-side BM25 stopwords for corpus-generic words (D5)

**Files:**
- Modify: `server/rag.py:733-760` (`_bm25_search`), `server/config.py`
- Test: `scripts/tests/test_bm25_query_stopwords.py` (new)

**Interfaces:**
- Produces: module constant `_BM25_QUERY_STOPWORDS: tuple[str, ...]` = bm25s English defaults + `("sdtm", "sdtmig", "cdisc", "domain", "domains", "dataset", "datasets")`; applied to the **query** tokenization only. Empty token set after stopword removal → `_bm25_search` returns `[]` (dense-only for that query).
- Setting: `bm25_query_stopwords_enabled: bool = True`.

- [ ] **Step 1: Failing test**

```python
# scripts/tests/test_bm25_query_stopwords.py
import server.rag as rag_mod

def test_stopword_list_contains_generic_corpus_words():
    sw = set(rag_mod._BM25_QUERY_STOPWORDS)
    assert {"sdtm", "cdisc", "domain", "dataset", "the"} <= sw
    assert "disposition" not in sw

def test_all_stopword_query_yields_no_bm25_hits():
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng._bm25_chunk_ids = ["a"]
    eng._bm25_chunk_meta = {"a": {"meta": {}, "text": "x"}}
    eng.bm25_query_stopwords = True
    class _Idx:
        def retrieve(self, *a, **k):
            raise AssertionError("must not be called for an empty query")
    eng._bm25 = _Idx()
    assert eng._bm25_search("the sdtm domain dataset", 5, None) == []
```

Run → FAIL (`_BM25_QUERY_STOPWORDS` missing).

- [ ] **Step 2: Implement**

In `server/rag.py` near the other class-level constants:

```python
# DM1 D5 — words that appear in almost every CDISC chunk carry no lexical signal
# but out-rank the one informative token in short questions ("sdtm 的 ds domain"
# pulled IG overview chapters ahead of anything DS-specific). Query side only:
# the index is untouched, so this is a pure re-weighting of what the user typed.
def _bm25_query_stopwords() -> tuple[str, ...]:
    import bm25s  # lazy, same as the search path
    return tuple(bm25s.stopwords.STOPWORDS_EN) + (
        "sdtm", "sdtmig", "cdisc", "domain", "domains", "dataset", "datasets",
    )
_BM25_QUERY_STOPWORDS = _bm25_query_stopwords()
```
(If importing bm25s at module import time is unacceptable for the test suite's speed, keep the tuple literal: copy the 33 English words from `bm25s.stopwords.STOPWORDS_EN` verbatim and add a test asserting equality with the library list.)

In `_bm25_search`:
```python
        sw = _BM25_QUERY_STOPWORDS if getattr(self, "bm25_query_stopwords", True) else "english"
        query_tokens = bm25s.tokenize(cjk_bigrams(query_text), stopwords=sw, show_progress=False)
        if not query_tokens.vocab or not any(len(ids) for ids in query_tokens.ids):
            return []
```
Verify the `Tokenized` attribute names against the installed bm25s version (`.venv/bin/python -c "import bm25s,inspect;print(inspect.signature(bm25s.tokenize))"`; also check whether `bm25s.tokenize` with `return_ids=True` default returns `Tokenized(ids, vocab)`). Add `bm25_query_stopwords: bool = True` to `RAGEngine.__init__` and `Settings.bm25_query_stopwords_enabled`, wired in `main.py` (both engines via `study_levers`) and `run_eval.py`.

- [ ] **Step 3: Tests**

Run: `.venv/bin/python -m pytest scripts/tests/test_bm25_query_stopwords.py scripts/tests/test_ja_tokenize.py -q` → PASS.

- [ ] **Step 4: Regression gates** — same three commands as Task 5 Step 5 with suffix `_t6`. Expected: zero regression; on the mapping set the lowercase DS question's CDISC seats should no longer be IG overview chapters.

- [ ] **Step 5: Commit**

```bash
git add server/rag.py server/config.py server/main.py eval/run_eval.py scripts/tests/test_bm25_query_stopwords.py eval/runs/dm1_*_t6.json data/study/st01/eval/runs/dm1_study_t6.json
git commit -m "feat(rag): DM1 T6 BM25 查询侧泛词停用 (D5): sdtm/cdisc/domain/dataset; 140q+48q 零回归"
```

---

### Task 7: Federation rule for domain-level mapping questions

**Files:**
- Modify: `server/federation.py:77-85` (`_FEDERATION_RULES`)
- Test: `scripts/tests/test_federation.py` (append)

- [ ] **Step 1: Failing test**

```python
def test_federation_rules_cover_domain_level_mapping():
    from server.federation import _FEDERATION_RULES
    assert "Domain-level mapping" in _FEDERATION_RULES
    assert "not only the form whose name resembles" in _FEDERATION_RULES
```

- [ ] **Step 2: Implement** — append a third bullet inside `_FEDERATION_RULES`:

```python
    "- Domain-level mapping questions (\"which of this study's data belong in domain X\"): "
    "first enumerate the record categories the standard defines for X (e.g. DS: protocol "
    "milestones, disposition of study participation, disposition of each study treatment), "
    "then look for candidate fields — status, date, reason — across ALL forms in the context, "
    "not only the form whose name resembles the domain code. A similarly named form is one "
    "candidate source, never the only one. Say explicitly which categories have no candidate "
    "field in the retrieved context.\n"
```

- [ ] **Step 3: Run** `.venv/bin/python -m pytest scripts/tests/test_federation.py -q` → PASS.

- [ ] **Step 4: Commit**
```bash
git add server/federation.py scripts/tests/test_federation.py
git commit -m "feat(rag): DM1 T7 联邦规则句: 域级映射先按定义枚举类别再跨表单找候选"
```

---

### Task 8: Final gates and per-question diff report

**Files:**
- Create: `evidence/checkpoints/dm1_gates.md`
- Modify: `_progress_domain_mapping.json`

- [ ] **Step 1: Run the three final sets and diff per question**

```bash
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup --output eval/runs/dm1_cdisc_after.json > eval/runs/dm1_cdisc_after.log 2>&1
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup --collection study_st01 --kb-root data/study/st01/cards --output data/study/st01/eval/runs/dm1_study_after.json > data/study/st01/eval/runs/dm1_study_after.log 2>&1
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_domain_mapping_v1.yml --retrieval-only --hybrid --structured-lookup --study-lookup --federated --corpus both --output data/study/st01/eval/runs/dm1_mapping_after.json > data/study/st01/eval/runs/dm1_mapping_after.log 2>&1
.venv/bin/python - <<'EOF'
import json
def load(p): return {r["id"]: r for r in json.load(open(p))["results"]}
for name, b, a in [("cdisc140","eval/runs/dm1_cdisc_before.json","eval/runs/dm1_cdisc_after.json"),
                   ("study48","data/study/st01/eval/runs/dm1_study_before.json","data/study/st01/eval/runs/dm1_study_after.json"),
                   ("mapping8","data/study/st01/eval/runs/dm1_mapping_before.json","data/study/st01/eval/runs/dm1_mapping_after.json")]:
    B, A = load(b), load(a); key = "source_recall"
    worse = [q for q in B if A[q][key] < B[q][key]]; better = [q for q in B if A[q][key] > B[q][key]]
    print(name, "worse:", worse, "better:", better)
EOF
.venv/bin/python -m pytest -q
```
(Confirm the per-result recall key name by `python -c "import json;print(json.load(open('eval/runs/dm1_cdisc_before.json'))['results'][0].keys())"` and adjust `key`.)

- [ ] **Step 2: Write `evidence/checkpoints/dm1_gates.md`** with: the three commands, before/after `source_recall_avg` per set, the `worse`/`better` lists, per-question table for the mapping set (which golds hit: definition chunk yes/no, candidate cards hit per form), and the per-task run files. State the D4 trigger: for the DS questions, fraction of milestone cards (RCT/F_REG/OC) recalled; if < 50%, D4 goes to the user.

- [ ] **Step 3: Update `_progress_domain_mapping.json`** gates and step statuses; commit:
```bash
git add evidence/checkpoints/dm1_gates.md _progress_domain_mapping.json eval/runs/dm1_*_after.json data/study/st01/eval/runs/dm1_study_after.json
git commit -m "feat(rag): DM1 T8 闸: 140q/48q 零回归 + 映射 gold before→after"
```

---

### Task 9: End-to-end check on the production service (hard checkpoint, needs the user)

Not automatable from this plan: the launchd service reads the worktree but must be restarted by the user (`launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api`). After restart, run the user's original sentence and the two reconstructed sentences through `/api/ask_stream` on two selectable models, save the answers to `evidence/checkpoints/dm1_e2e_answers/`, and have a **different** subagent judge three pre-registered criteria written in `evidence/checkpoints/dm1_e2e.md` §0 before any answer is read: (1) the answer lists the domain's standard categories, (2) candidate fields come from ≥3 forms, (3) every EDC→SDTM link is labelled 推測/inference.

### Task 10/11: D4 ruling and wrap-up

Per `PLAN_domain_mapping.md` §4 rows 10–11: `RETROSPECTIVE_domain_mapping.md` (kept / must-add / decision review), `_progress` closed, one Key Path line in `CLAUDE.md`, and the dogfood entry gets a trailing line "→ DM1 修后复跑: see dm1_gates.md".
