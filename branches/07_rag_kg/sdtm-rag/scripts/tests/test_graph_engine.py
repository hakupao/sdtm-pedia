# scripts/tests/test_graph_engine.py
from collections import defaultdict

import pytest
import yaml as _yaml

from server.config import settings
from server.graph_engine import DictBackend, GraphEngine
from server.meta_store import MetaStore


@pytest.fixture(scope="module")
def store() -> MetaStore:
    return MetaStore(settings.meta_path)


@pytest.fixture(scope="module")
def backend(store) -> DictBackend:
    return DictBackend(store)


@pytest.fixture(scope="module")
def engine(store) -> GraphEngine:
    return GraphEngine(store)


# ── Task 2: DictBackend primitives ───────────────────────────────────────────
def test_nodes_of_type(backend, store):
    assert len(backend.nodes_of_type("Domain")) == 63
    assert len(backend.nodes_of_type("Variable")) == 1523
    assert len(backend.nodes_of_type("Codelist")) == 1005
    assert set(backend.nodes_of_type("Class")) == {
        d_class for d_class in (store.domain_info(d)["class"] for d in store.known_domains)
    }
    assert backend.nodes_of_type("Bogus") == []


def test_out_neighbors_edges(backend, store):
    # HAS_VARIABLE / IN_DOMAIN are inverse
    assert "AETERM" in backend.out_neighbors("AE", "HAS_VARIABLE")
    assert "AE" in backend.out_neighbors("AETERM", "IN_DOMAIN")
    # USES_CT / CT_USED_BY
    assert "C66742" in backend.out_neighbors("AESER", "USES_CT")
    assert "AESER" in backend.out_neighbors("C66742", "CT_USED_BY")
    # CT_IN_DOMAIN matches MetaStore.domains_for_codelist exactly
    assert sorted(backend.out_neighbors("C66742", "CT_IN_DOMAIN")) == store.domains_for_codelist("C66742")
    # SAME_CLASS / class membership
    assert backend.out_neighbors("AE", "SAME_CLASS") == store.same_class("AE")
    assert "AE" in backend.out_neighbors(store.domain_info("AE")["class"], "CLASS_HAS")
    assert backend.out_neighbors("AE", "BELONGS_TO") == [store.domain_info("AE")["class"]]
    # RELATED_TO targets + edge_data
    tgts = backend.out_neighbors("AE", "RELATED_TO")
    assert tgts and all(isinstance(t, str) for t in tgts)
    ed = backend.edge_data("AE", tgts[0], "RELATED_TO")
    assert ed is not None and "mechanism" in ed
    # unknown node/edge -> [] / None, never raise
    assert backend.out_neighbors("ZZ", "HAS_VARIABLE") == []
    assert backend.edge_data("AE", "ZZ", "RELATED_TO") is None


# ── Task 3: GraphEngine high-level queries ────────────────────────────────────
def test_impact_of_codelist(engine, store):
    imp = engine.impact_of_codelist("C66742")
    assert imp["name"] == store.codelist("C66742")["name"]
    assert imp["domains"] == store.domains_for_codelist("C66742")
    assert imp["variables"] == store.variables_for_codelist("C66742")
    assert imp["n_domains"] == len(imp["domains"])
    assert imp["n_variables"] == len(imp["variables"])
    assert engine.impact_of_codelist("C0000000") is None


def test_impact_of_variable(engine, store):
    imp = engine.impact_of_variable("TAETORD")
    assert imp["domains"] == store.domains_for_variable("TAETORD")
    assert imp["n_domains"] == 43
    assert engine.impact_of_variable("NOTAVAR") is None


def test_variables_in_min_domains(engine, store):
    res = dict(engine.variables_in_min_domains(40))
    # cross-checked against MetaStore directly
    truth = {v: len(store.domains_for_variable(v)) for v in store.known_variables}
    truth = {v: c for v, c in truth.items() if c >= 40}
    assert res == truth
    # sorted descending by count
    counts = [c for _v, c in engine.variables_in_min_domains(40)]
    assert counts == sorted(counts, reverse=True)


def test_domains_in_class_and_sizes(engine, store):
    events = engine.domains_in_class("Events")
    assert "AE" in events
    assert all(store.domain_info(d)["class"] == "Events" for d in events)
    sizes = engine.class_sizes()
    assert sum(sizes.values()) == 63
    assert sizes["Events"] == len(events)


def test_most_shared_codelists(engine, store):
    top = engine.most_shared_codelists(5)
    assert len(top) == 5
    nvs = [t["n_variables"] for t in top]
    assert nvs == sorted(nvs, reverse=True)
    assert top[0]["n_variables"] == max(
        len(store.variables_for_codelist(c)) for c in store.known_ctcodes
    )


def test_same_class_and_co_users(engine, store):
    assert engine.same_class_domains("AE") == store.same_class("AE")
    co = engine.codelist_co_users("AESER")
    for code, info in co.items():
        assert "AESER" not in info["others"]
        assert set(info["others"]) == set(store.variables_for_codelist(code)) - {"AESER"}


# ── Task 4: domain_relations (structural HIGH + curated advisory) ─────────────
def test_domain_relations(engine, store):
    rel = engine.domain_relations("AE")
    assert rel["structural"]["same_class"] == store.same_class("AE")
    curated = rel["curated"]
    assert curated == store.relations_curated("AE")  # advisory edges passed through verbatim
    # every curated edge is tagged LOW-fidelity for the answerer to mark advisory
    assert all(c.get("fidelity") for c in curated) or all("mechanism" in c for c in curated)
    assert engine.domain_relations("ZZ") is None


# ── Task 5: exhaustive engine vs raw meta.yaml reconciliation (anti-tautology) ─
def _raw_meta():
    return _yaml.safe_load(settings.meta_path.read_text(encoding="utf-8"))


def test_exhaustive_impact_of_variable_vs_raw(engine):
    raw = _raw_meta()
    truth: dict[str, set[str]] = defaultdict(set)
    for d in raw["domains"]:
        if not d["counts_toward_63"]:
            continue
        for v in d["variables"]:
            truth[v["name"]].add(d["domain"])
    for var, doms in truth.items():
        imp = engine.impact_of_variable(var)
        assert imp is not None and imp["n_domains"] == len(doms), var
        assert set(imp["domains"]) == doms, var


def test_exhaustive_impact_of_codelist_vs_raw(engine):
    raw = _raw_meta()
    dom_truth: dict[str, set[str]] = defaultdict(set)
    var_truth: dict[str, set[str]] = defaultdict(set)
    for d in raw["domains"]:
        if not d["counts_toward_63"]:
            continue
        for v in d["variables"]:
            for code in v["ct_codes"]:
                dom_truth[code].add(d["domain"])
                var_truth[code].add(v["name"])
    for code in {c["ct_code"] for c in raw["codelists"]}:
        imp = engine.impact_of_codelist(code)
        assert imp is not None, code
        assert set(imp["domains"]) == dom_truth.get(code, set()), code
        assert set(imp["variables"]) == var_truth.get(code, set()), code


def test_exhaustive_class_sizes_vs_raw(engine):
    raw = _raw_meta()
    truth: dict[str, int] = defaultdict(int)
    for d in raw["domains"]:
        if d["counts_toward_63"]:
            truth[d["class"]] += 1
    assert engine.class_sizes() == dict(truth)
