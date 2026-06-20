# scripts/tests/test_graph_answer.py
from server.graph_answer import detect_graph_intents


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
    assert "aggregate" in detect_graph_intents("how many domains are in the Events class?")


def test_must_not_fire_sp2_and_plain():
    # SP2 territory (counting/dist) -> NO graph intent (disjoint by design)
    assert detect_graph_intents("how many domains include TAETORD?") == set()
    assert detect_graph_intents("which domains use the VISITNUM variable?") == set()
    # plain concept / how-to -> nothing
    assert detect_graph_intents("how should missing values be represented?") == set()
    assert detect_graph_intents("what is the structure of the DM domain?") == set()
