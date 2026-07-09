"""SP5 graph validator — cross-domain checks over meta.yaml (deterministic, no Neo4j)."""
from __future__ import annotations

import pandas as pd
import pytest

from server.config import settings
from server.graph_engine import GraphEngine
from server.graph_validator import check_completeness
from server.meta_store import MetaStore


@pytest.fixture(scope="module")
def engine():
    return GraphEngine(MetaStore(settings.meta_path))


def _df(domain: str) -> pd.DataFrame:
    return pd.DataFrame({"STUDYID": ["S1"], "DOMAIN": [domain], "USUBJID": ["S1-1"]})


def test_completeness_flags_missing_relrec_target(engine):
    # AE is curated-related to CM via mechanism RELREC (meta.yaml). Submit AE without CM.
    findings = check_completeness({"AE": _df("AE")}, engine)
    assert any(f.rule == "GXDOM" and "CM" in f.message for f in findings)
    assert all(f.severity == "WARN" for f in findings)


def test_completeness_silent_when_target_present(engine):
    findings = check_completeness({"AE": _df("AE"), "CM": _df("CM")}, engine)
    assert not any("CM" in f.message for f in findings)


def test_completeness_unknown_domain_no_crash(engine):
    assert check_completeness({"ZZ": _df("ZZ")}, engine) == []
