# scripts/tests/test_structured_answer.py
from server.structured_answer import detect_intents


def test_count_intent():
    assert "count" in detect_intents("how many domains include taetord?")
    assert "count" in detect_intents("what is the number of domains carrying visitdy")


def test_enumerate_intent():
    assert "enumerate" in detect_intents("which domains carry visitdy?")
    assert "enumerate" in detect_intents("list all domains that include taetord")


def test_attribute_intent():
    assert "attribute" in detect_intents("what is the label of aeterm?")
    assert "attribute" in detect_intents("what role and core is aeser")


def test_codelist_intent():
    assert "codelist" in detect_intents("what codelist does aesev use?")
    assert "codelist" in detect_intents("which controlled terminology applies to route")


def test_usage_question_has_no_capability_intent():
    # must-not-fire seed: a usage/how-to question names entities but no capability cue
    assert detect_intents("how is visitdy used in practice?") == set()
    assert detect_intents("explain the purpose of the ae domain") == set()


# ── Task 4: StructuredAnswerer must-fire / must-not-fire battery ──────────────
from pathlib import Path

import pytest

from server.meta_store import MetaStore
from server.structured_answer import StructuredAnswerer, CheckableCount


@pytest.fixture(scope="module")
def answerer() -> StructuredAnswerer:
    store = MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml")
    return StructuredAnswerer(store)


def test_must_fire_count(answerer: StructuredAnswerer):
    facts = answerer.resolve("How many domains include TAETORD, and what is its label?")
    assert facts is not None
    assert "43" in facts.text_block
    assert "Planned Order of Element within Arm" in facts.text_block
    assert CheckableCount("TAETORD", "domains", 43) in facts.checkable_counts


def test_must_fire_enumerate_visitdy(answerer: StructuredAnswerer):
    facts = answerer.resolve("Which domains carry VISITDY?")
    assert facts is not None
    assert "36" in facts.text_block
    assert CheckableCount("VISITDY", "domains", 36) in facts.checkable_counts


def test_must_not_fire_unknown_entity(answerer: StructuredAnswerer):
    # count intent but no anchored SDTM entity and no corpus-total phrasing -> None
    assert answerer.resolve("How many patients are usually enrolled in a phase 3 study?") is None


def test_must_not_fire_usage_question(answerer: StructuredAnswerer):
    # names a known variable but no capability intent -> None (relevance guard)
    assert answerer.resolve("How is VISITDY used in a typical submission?") is None


def test_must_not_fire_bare_mention(answerer: StructuredAnswerer):
    # bare mention, no capability cue
    assert answerer.resolve("Tell me about the AE domain.") is None
