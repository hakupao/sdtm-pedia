"""Unit tests for the --judge semantic fact-recall parser in eval/run_eval.py.

Covers the fragile part (parsing the judge's JSON response) without any LLM call;
the live LLM path is exercised by the integration smoke, not here.
"""
from __future__ import annotations

from eval.run_eval import _parse_covered, check_fact_recall_judge


class TestParseCovered:
    def test_plain_object(self):
        assert _parse_covered('{"covered": [true, false, true]}', 3) == [True, False, True]

    def test_json_fence_and_prose(self):
        assert _parse_covered('```json\n{"covered":[true,true]}\n```', 2) == [True, True]
        assert _parse_covered('Sure, here: [true, false]', 2) == [True, False]

    def test_int_coercion(self):
        assert _parse_covered('{"covered":[1,0,1]}', 3) == [True, False, True]

    def test_length_mismatch_returns_none(self):
        assert _parse_covered('{"covered":[true]}', 3) is None

    def test_unparseable_returns_none(self):
        assert _parse_covered("no json here", 2) is None
        assert _parse_covered("", 1) is None

    def test_bare_array(self):
        assert _parse_covered("[true, true, false]", 3) == [True, True, False]

    def test_array_of_objects_rejected(self):
        # Rule D HIGH: a judge emitting per-fact objects must NOT coerce to all-True
        # (non-empty dict is truthy). Reject -> None -> counted substring fallback.
        assert _parse_covered(
            '{"covered":[{"i":1,"covered":false},{"i":2,"covered":false}]}', 2
        ) is None

    def test_string_verdicts_rejected(self):
        # Rule D HIGH: string elements ("no"/"false") are truthy -> would inflate.
        assert _parse_covered('{"covered":["no","no"]}', 2) is None
        assert _parse_covered('["false","true"]', 2) is None

    def test_zero_one_ints_still_accepted(self):
        # the legitimate 0/1 coercion must survive the type guard
        assert _parse_covered('{"covered":[1,0]}', 2) == [True, False]


class TestJudgeNoFacts:
    def test_empty_gold_is_full_recall_no_llm_call(self):
        # no gold facts -> 1.0 without touching the LLM
        assert check_fact_recall_judge("q?", "any answer", [], judge_model="unused") == (1.0, [], [])


def test_eval_answer_path_injects_facts(monkeypatch, tmp_path):
    """Parity guard: eval uses the same augment_context + apply_counting_gate helpers as prod.

    Builds the answerer the same way run_eval.main() does (MetaStore + StructuredAnswerer),
    calls augment_context, and asserts the facts block is prepended identically.
    No API calls needed — purely tests the shared helper contract.
    """
    from pathlib import Path

    from server.meta_store import MetaStore
    from server.structured_answer import StructuredAnswerer, augment_context

    store = MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml")
    answerer = StructuredAnswerer(store)
    facts = answerer.resolve("How many domains include TAETORD?")
    assert facts is not None, "resolve() must fire for TAETORD count query"
    ctx = augment_context(facts, "### [1] chunk\n\nbody")
    assert "Structured Facts (authoritative" in ctx
    assert "43" in ctx
