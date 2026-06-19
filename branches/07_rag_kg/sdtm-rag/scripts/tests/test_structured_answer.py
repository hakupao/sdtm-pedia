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
from server.structured_answer import StructuredAnswerer, CheckableCount, StructuredFacts, augment_context


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


# ── Task 4b: domain-entity + corpus-total + codelist->variables ───────────────

def test_domain_entity_variable_count(answerer: StructuredAnswerer):
    facts = answerer.resolve("How many variables does the AE domain contain?")
    assert facts is not None
    nv = len(answerer.store.variables_in_domain("AE"))
    assert CheckableCount("AE", "variables", nv) in facts.checkable_counts
    assert str(nv) in facts.text_block


def test_domain_enumerate_variables(answerer: StructuredAnswerer):
    facts = answerer.resolve("Which variables are in the DM domain?")
    assert facts is not None
    assert "USUBJID" in facts.text_block  # a known DM variable, enumerated


def test_total_domain_count(answerer: StructuredAnswerer):
    facts = answerer.resolve("How many domains are defined in SDTM in total?")
    assert facts is not None
    assert "63" in facts.text_block


def test_total_count_requires_corpus_phrase(answerer: StructuredAnswerer):
    # count intent + "domains" but no entity and no corpus phrase -> None (conservative)
    assert answerer.resolve("How many domains do you recommend for a small study?") is None


# ── Task 5: augment_context — authoritative-block prepend helper ──────────────

def test_augment_context_prepends_block():
    facts = StructuredFacts(text_block="- **X** — fact.", checkable_counts=[])
    out = augment_context(facts, "### [1] some_chunk\n\nbody")
    assert out.startswith("## Structured Facts (authoritative, exhaustive, from SDTM metadata)")
    assert "- **X** — fact." in out
    assert "### [1] some_chunk" in out  # original context preserved after the block


def test_augment_context_none_is_passthrough():
    assert augment_context(None, "ctx") == "ctx"


# ── Task 4b hardening: 2-letter domain code must-not-fire (no SDTM context) ──

def test_must_not_fire_pr_no_sdtm_context(answerer: StructuredAnswerer):
    # "PR" is a valid SDTM domain code, but this query has no "domain"/"sdtm" signal
    assert answerer.resolve("Could you do a PR review of this changeset?") is None


def test_must_not_fire_dm_message(answerer: StructuredAnswerer):
    # "DM" is a valid SDTM domain code, but this query is about messaging, not SDTM
    assert answerer.resolve("What does a DM message contain?") is None


# ── Task 8: maybe_build_answerer helper gated on structured_answer_enabled ────

def test_maybe_build_answerer_gated():
    from server.config import Settings
    from server.main import maybe_build_answerer
    assert maybe_build_answerer(Settings(structured_answer_enabled=False)) is None
    a = maybe_build_answerer(Settings(structured_answer_enabled=True))
    assert a is not None
    assert a.resolve("How many domains include TAETORD?") is not None


# ── SP2 Fix 1: codelist variable-count CheckableCount + text_block injection ──

def test_codelist_variable_count_in_checkable_counts(answerer: StructuredAnswerer):
    """resolve() for a codelist+count query must emit BOTH a domains count AND a
    codelist_variables count, and the text_block must state that variable count."""
    facts = answerer.resolve("How many variables use codelist C66742?")
    assert facts is not None, "resolve() must fire on a codelist+count query"

    expected_var_count = len(answerer.store.variables_for_codelist("C66742"))
    expected_dom_count = len(answerer.store.domains_for_codelist("C66742"))

    # Both CheckableCounts must be present
    assert CheckableCount("C66742", "domains", expected_dom_count) in facts.checkable_counts, (
        f"domains CheckableCount missing; counts={facts.checkable_counts}"
    )
    assert CheckableCount("C66742", "codelist_variables", expected_var_count) in facts.checkable_counts, (
        f"codelist_variables CheckableCount missing; counts={facts.checkable_counts}"
    )

    # text_block must state the variable count as a plain integer
    assert str(expected_var_count) in facts.text_block, (
        f"Variable count {expected_var_count} not found in text_block:\n{facts.text_block}"
    )
