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
