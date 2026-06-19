# scripts/tests/test_meta_store.py
import tempfile
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
    # Exact value verified from meta.yaml first-occurrence (not guessed)
    assert attr["core"] == "Perm"
    assert store.variable_attributes("NOTAVAR") is None


def test_variable_attributes_mutation_safety(store: MetaStore):
    # Mutating the returned ct_codes list must NOT corrupt the internal index.
    # AEPRESP has ct_codes=['C66742'] in meta.yaml (first occurrence in AE domain).
    attr1 = store.variable_attributes("AEPRESP")
    assert attr1 is not None
    original_codes = list(attr1["ct_codes"])  # snapshot before mutation

    attr1["ct_codes"].append("POISON")  # mutate the returned copy

    attr2 = store.variable_attributes("AEPRESP")
    assert attr2 is not None
    assert attr2["ct_codes"] == original_codes, (
        "Mutating the returned ct_codes leaked into the internal index"
    )


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


def test_domains_for_codelist(store: MetaStore):
    domains = store.domains_for_codelist("C66742")
    assert isinstance(domains, list)
    assert "AE" in domains
    # result is sorted and deduplicated
    assert domains == sorted(set(domains))
    # unknown codelist -> empty list
    assert store.domains_for_codelist("C0000000") == []


def test_variables_for_codelist(store: MetaStore):
    variables = store.variables_for_codelist("C66742")
    assert isinstance(variables, list)
    assert "AEPRESP" in variables
    # result is sorted and deduplicated
    assert variables == sorted(set(variables))
    # unknown codelist -> empty list
    assert store.variables_for_codelist("C0000000") == []


def test_model_defhome(store: MetaStore):
    # ACTARM is a known model_defhome key (verified from meta.yaml)
    result = store.model_defhome("ACTARM")
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0
    # unknown variable -> None
    assert store.model_defhome("NOTAVAR") is None


def test_known_ctcodes_membership(store: MetaStore):
    assert "C66742" in store.known_ctcodes
    assert "C0000000" not in store.known_ctcodes
    assert isinstance(store.known_ctcodes, frozenset)


def test_loud_fail_missing_keys():
    # A meta.yaml missing required top-level keys must raise ValueError, not KeyError.
    minimal_yaml = "meta_version: 1\ndomains: []\n"  # missing codelists + model_defhome
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False, encoding="utf-8"
    ) as f:
        f.write(minimal_yaml)
        tmp_path = Path(f.name)
    try:
        with pytest.raises(ValueError, match="missing required top-level keys"):
            MetaStore(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)


def test_domain_info(store: MetaStore):
    info = store.domain_info("AE")
    assert info["class"] == "Events"
    assert info["label"] == "Adverse Events"
    assert info["n_variables"] == len(store.variables_in_domain("AE"))
    assert store.domain_info("ZZ") is None


def test_loud_fail_not_a_mapping():
    # A meta.yaml that is a list (not a dict) must raise ValueError.
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False, encoding="utf-8"
    ) as f:
        f.write("- item1\n- item2\n")
        tmp_path = Path(f.name)
    try:
        with pytest.raises(ValueError, match="must be a YAML mapping"):
            MetaStore(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)
