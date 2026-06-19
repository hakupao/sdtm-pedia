# scripts/tests/test_meta_store.py
from pathlib import Path

import pytest

from server.meta_store import MetaStore


@pytest.fixture(scope="module")
def store() -> MetaStore:
    return MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml")


def test_loads_and_counts(store: MetaStore):
    # counts_toward_63 domains == 63 (DI stub excluded); 1523 unique vars / 1917 entries
    assert store.n_domains == 63
    assert store.n_unique_variables == 1523
    assert store.n_variable_entries == 1917


def test_domains_for_variable_counts(store: MetaStore):
    # SP1 reconcile-verified anchors; these ARE the q103/q104 targets
    assert len(store.domains_for_variable("TAETORD")) == 43
    assert len(store.domains_for_variable("VISITDY")) == 36
    # case-insensitive entry point
    assert len(store.domains_for_variable("taetord")) == 43
    # unknown variable -> empty, never raises
    assert store.domains_for_variable("NOTAVAR") == []


def test_variable_attributes(store: MetaStore):
    attr = store.variable_attributes("TAETORD")
    assert attr["label"] == "Planned Order of Element within Arm"
    assert attr["role"] == "Timing"
    assert attr["type"] == "Num"
    assert attr["core"] in {"Req", "Exp", "Perm"}
    assert store.variable_attributes("NOTAVAR") is None


def test_variables_in_domain(store: MetaStore):
    ae_vars = store.variables_in_domain("AE")
    assert "AETERM" in ae_vars
    assert store.variables_in_domain("ZZ") == []


def test_codelist_lookup(store: MetaStore):
    cl = store.codelist("C66742")
    assert cl["name"] == "No Yes Response"
    assert cl["extensible"] is False
    assert isinstance(cl["term_count"], int)
    assert store.codelist("C0000000") is None


def test_ctcode_locations_and_known_vocab(store: MetaStore):
    locs = store.locations_for_codelist("C66742")  # [(domain, var), ...]
    assert any(var == "AEPRESP" and dom == "AE" for dom, var in locs)
    assert "AETERM" in store.known_variables
    assert "AE" in store.known_domains
