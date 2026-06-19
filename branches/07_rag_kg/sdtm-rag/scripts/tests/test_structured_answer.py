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
