"""SP4 reconcile — yaml-side derivation anchors (offline; live checks are the
script's own job, run as Gate 1, never inside pytest)."""

from __future__ import annotations

from pathlib import Path

from scripts.reconcile_neo4j import expected_from_yaml

META_PATH = Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml"


def test_expected_counts_match_golden_anchors():
    exp = expected_from_yaml(META_PATH)
    assert exp["node_counts"] == {"Domain": 63, "Variable": 1541, "Codelist": 1005,
                                  "Class": 8, "ModelChapter": 4}
    assert exp["edge_counts"] == {"HAS_VARIABLE": 1917, "USES_CT": 542, "IN_CLASS": 63,
                                  "DEFHOME": 59, "RELATED_TO": 52}

def test_expected_neighborhood_derivation():
    exp = expected_from_yaml(META_PATH)
    dm = exp["domain_nbhd"]("DM")
    assert dm["in_class"] == "Special-Purpose"
    assert ("DTHFL", "Record Qualifier", "Char", "Exp") in dm["has_variable"]
    v = exp["variable_nbhd"]("VISIT")
    assert len(v["domains"]) == 36

def test_independence_no_forbidden_imports():
    src = (Path(__file__).resolve().parents[1] / "reconcile_neo4j.py").read_text(encoding="utf-8")
    for banned in ("build_neo4j", "meta_store", "graph_engine", "MetaStore", "GraphEngine"):
        assert banned not in src, f"reconcile must not reference {banned} (independence rule)"
