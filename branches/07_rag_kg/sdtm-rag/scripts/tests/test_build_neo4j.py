"""SP4 build_neo4j extract layer — anchors pinned to reconcile-verified meta.yaml.

Pure-function tests only: NO live Neo4j needed (Gate 3 requires the whole pytest
suite to pass with Neo4j stopped)."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.build_neo4j import extract_graph, load_meta

META_PATH = Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml"


@pytest.fixture(scope="module")
def graph():
    return extract_graph(load_meta(META_PATH))


# ── 节点分类计数 (spec §3 + plan 偏差 D3/D4) ──────────────────────────────

def test_node_counts(graph):
    n = graph["nodes"]
    assert len(n["Domain"]) == 63          # DI 桩 counts_toward_63=false 不导
    assert len(n["Variable"]) == 1541      # 1523 IG + 18 model-only (偏差 D4)
    assert len(n["Codelist"]) == 1005
    assert len(n["Class"]) == 8
    assert len(n["ModelChapter"]) == 4     # 偏差 D3

def test_variable_model_only_split(graph):
    flags = [v["model_only"] for v in graph["nodes"]["Variable"]]
    assert flags.count(False) == 1523 and flags.count(True) == 18
    by_name = {v["name"]: v for v in graph["nodes"]["Variable"]}
    assert by_name["APID"]["model_only"] is True      # 模型级变量, 不在任何 IG 域
    assert "role" not in by_name["APID"]              # model-only 节点只有 name+model_only
    assert by_name["DTHFL"]["model_only"] is False

def test_di_stub_excluded(graph):
    assert "DI" not in {d["code"] for d in graph["nodes"]["Domain"]}

# ── 边分类计数 ────────────────────────────────────────────────────────────

def test_edge_counts(graph):
    e = graph["edges"]
    assert len(e["HAS_VARIABLE"]) == 1917
    assert len(e["USES_CT"]) == 542        # 唯一 (var, ct) 对, 跨域 union
    assert len(e["IN_CLASS"]) == 63
    assert len(e["DEFHOME"]) == 59         # 偏差 D4: 全量 59, 不静默丢 18
    assert len(e["RELATED_TO"]) == 52

# ── 语义抽点 (跨域分歧 / 逐域权威值 / advisory 保真) ──────────────────────

def test_has_variable_carries_per_domain_attrs(graph):
    rows = {(r["domain"], r["var"]): r for r in graph["edges"]["HAS_VARIABLE"]}
    dm_dthfl = rows[("DM", "DTHFL")]
    assert (dm_dthfl["role"], dm_dthfl["type"], dm_dthfl["core"]) == ("Record Qualifier", "Char", "Exp")
    visit_roles = {r["role"] for r in graph["edges"]["HAS_VARIABLE"] if r["var"] == "VISIT"}
    assert {"Synonym Qualifier", "Timing"} <= visit_roles   # 跨域 role 分歧存在于边上

def test_uses_ct_domains_property(graph):
    rows = {(r["var"], r["code"]): r["domains"] for r in graph["edges"]["USES_CT"]}
    assert rows[("FOCID", "C119013")] == ["OE"]   # 偏差 D2 的动机: 逐域精确
    assert "DM" in rows[("DTHFL", "C66742")]

def test_related_to_advisory_fidelity(graph):
    ae_fa = [r for r in graph["edges"]["RELATED_TO"] if r["src"] == "AE" and r["dst"] == "FA"]
    assert len(ae_fa) == 1
    r = ae_fa[0]
    assert r["advisory"] is True and r["fidelity"] == "curated_prose"
    assert r["category"] == "Findings About" and r["mechanism"] is None

def test_class_and_chapter_nodes(graph):
    sizes = {c["name"]: c["n_domains"] for c in graph["nodes"]["Class"]}
    assert sizes["Findings"] == 30 and sizes["Study Reference"] == 1
    assert {m["path"] for m in graph["nodes"]["ModelChapter"]} == {
        "model/02_observation_classes.md", "model/03_special_purpose_domains.md",
        "model/05_study_level_data.md", "model/06_relationship_datasets.md",
    }

def test_defhome_edge_shape(graph):
    rows = {r["var"]: r["chapter"] for r in graph["edges"]["DEFHOME"]}
    assert rows["APID"] == "model/06_relationship_datasets.md"
    assert len(rows) == 59

def test_load_meta_missing_key_fails_loud(tmp_path):
    bad = tmp_path / "meta.yaml"
    bad.write_text("meta_version: 1\ndomains: []\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing top-level key"):
        load_meta(bad)


def _minimal_domain(**overrides):
    """Smallest counts_toward_63 domain that reaches extract_graph's loud-fail
    checks — one real domain, one variable, no relations by default."""
    domain = {
        "domain": "DM",
        "label": "Demographics",
        "class": "Special Purpose",
        "structure": "One record per subject",
        "counts_toward_63": True,
        "same_class": [],
        "variables": [
            {
                "name": "STUDYID",
                "label": "Study Identifier",
                "role": "Identifier",
                "type": "Char",
                "core": "Req",
                "ct_codes": [],
                "ct_dict": {},
            }
        ],
        "relations_curated": [],
    }
    domain.update(overrides)
    return domain


def test_extract_graph_bad_relation_target_fails_loud():
    domain = _minimal_domain(relations_curated=[
        {"target": "ZZ", "mechanism": "manual", "note": "n/a",
         "category": "Other", "fidelity": "low"},
    ])
    bad_meta = {"meta_version": 1, "domains": [domain], "codelists": [], "model_defhome": {}}
    with pytest.raises(ValueError, match="relations_curated targets not in real domains"):
        extract_graph(bad_meta)


def test_extract_graph_dangling_ct_code_fails_loud():
    domain = _minimal_domain()
    domain["variables"][0]["ct_codes"] = ["C99999"]
    bad_meta = {"meta_version": 1, "domains": [domain], "codelists": [], "model_defhome": {}}
    with pytest.raises(ValueError, match="ct_codes not in codelists section"):
        extract_graph(bad_meta)
