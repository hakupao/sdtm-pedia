# scripts/tests/test_graph_answer.py
import pytest

from server.config import settings
from server.graph_answer import GraphAnswerer, detect_graph_intents
from server.graph_engine import GraphEngine
from server.meta_store import MetaStore
from server.structured_answer import CheckableCount


def test_impact_intent():
    assert "impact" in detect_graph_intents("what is affected if C66742 changes?")
    assert "impact" in detect_graph_intents("which domains are impacted by changing VSORRESU?")
    assert "impact" in detect_graph_intents("what downstream variables depend on EPOCH?")


def test_relationship_intent():
    assert "relationship" in detect_graph_intents("how is AE related to other domains?")
    assert "relationship" in detect_graph_intents("what domains are linked to DM?")


def test_aggregate_intent():
    assert "aggregate" in detect_graph_intents("which variables appear in more than 30 domains?")
    assert "aggregate" in detect_graph_intents("what is the most shared codelist?")
    # class-roster removed from NL surface — must NOT produce aggregate intent
    assert "aggregate" not in detect_graph_intents("how many domains are in the Events class?")


def test_must_not_fire_sp2_and_plain():
    # SP2 territory (counting/dist) -> NO graph intent (disjoint by design)
    assert detect_graph_intents("how many domains include TAETORD?") == set()
    assert detect_graph_intents("which domains use the VISITNUM variable?") == set()
    # plain concept / how-to -> nothing
    assert detect_graph_intents("how should missing values be represented?") == set()
    assert detect_graph_intents("what is the structure of the DM domain?") == set()


# ── Task 9: GraphAnswerer.resolve() battery ───────────────────────────────────


@pytest.fixture(scope="module")
def ga() -> GraphAnswerer:
    return GraphAnswerer(GraphEngine(MetaStore(settings.meta_path)))


def test_impact_codelist_fires_with_cardinality(ga):
    facts = ga.resolve("What is affected if codelist C66742 changes?")
    assert facts is not None
    n = len(ga.engine.impact_of_codelist("C66742")["domains"])
    assert str(n) in facts.text_block
    assert CheckableCount("C66742", "impacted_domains", n) in facts.checkable_counts


def test_impact_variable_fires(ga):
    facts = ga.resolve("Which domains are impacted by changing TAETORD?")
    assert facts is not None
    assert CheckableCount("TAETORD", "impacted_domains", 43) in facts.checkable_counts


def test_relationship_fires_advisory_only(ga):
    facts = ga.resolve("How is AE related to other domains?")
    assert facts is not None
    # curated relations go to advisory_block, NOT the authoritative text_block / counts
    assert facts.advisory_block
    assert "same class" in facts.text_block.lower() or facts.text_block == ""
    assert all("RELATED" not in c.kind for c in facts.checkable_counts)


def test_aggregate_min_domains_fires(ga):
    # "more than 40" is strict (>40): TAETORD=43 qualifies, a var with exactly 40 does not
    facts = ga.resolve("Which variables appear in more than 40 domains?")
    assert facts is not None
    assert "TAETORD" in facts.text_block or "VISITDY" in facts.text_block
    # strict "more than 40" → threshold 41; a variable with exactly 40 domains must NOT appear
    vars_exact_40 = [v for v, c in ga.engine.variables_in_min_domains(40)
                     if c == 40]
    for v in vars_exact_40:
        assert v not in facts.text_block, f"{v} (exactly 40 domains) should be excluded by 'more than 40'"


def test_aggregate_at_least_includes_exact(ga):
    # "at least 40" is inclusive (>=40): a variable with exactly 40 domains IS included
    facts = ga.resolve("Which variables appear in at least 40 domains?")
    assert facts is not None
    vars_exact_40 = [v for v, c in ga.engine.variables_in_min_domains(40) if c == 40]
    if vars_exact_40:
        assert any(v in facts.text_block for v in vars_exact_40), (
            f"at-least-40 should include vars with exactly 40 domains: {vars_exact_40[:3]}"
        )


def test_impact_degenerate_codelist_skipped(ga):
    # C100134 has 0 impacted domains/variables — must not inject "affects 0" line
    facts = ga.resolve("What is affected if codelist C100134 changes?")
    assert facts is None or "C100134" not in facts.text_block
    if facts is not None:
        assert not any(cc.subject == "C100134" for cc in facts.checkable_counts)


def test_must_not_fire_no_anchor(ga):
    # impact cue but no anchored entity -> None
    assert ga.resolve("what is affected by a protocol amendment?") is None


def test_must_not_fire_sp2_query(ga):
    # SP2 territory, no graph intent -> None (no double injection)
    assert ga.resolve("How many domains include TAETORD?") is None
    assert ga.resolve("Which domains use VISITNUM?") is None


def test_must_not_fire_min_domains_without_domain_context(ga):
    # "more than" + "variable" + number but NO "domain" → no min-domains injection
    assert ga.resolve("How many variables are in more than 5 records?") is None


def test_must_not_fire_class_roster(ga):
    # class-roster questions removed from NL surface (class names = common words, fragile)
    assert ga.resolve("how many domains are in the Events class?") is None
    assert ga.resolve("What are the Special-Purpose datasets in SDTM and which domains fall into this category?") is None
