# scripts/tests/test_graph_engine.py
from pathlib import Path

import pytest

from server.config import settings
from server.meta_store import MetaStore
from server.graph_engine import DictBackend


@pytest.fixture(scope="module")
def store() -> MetaStore:
    return MetaStore(settings.meta_path)


@pytest.fixture(scope="module")
def backend(store) -> DictBackend:
    return DictBackend(store)


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
