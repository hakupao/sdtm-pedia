"""SP5 graph validator — cross-domain checks over meta.yaml (deterministic, no Neo4j)."""
from __future__ import annotations

import pandas as pd
import pytest

from server.config import settings
from server.graph_engine import GraphEngine
from server.graph_validator import (
    check_completeness,
    check_ct_cascade,
    check_impact,
    run_graph_checks,
)
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


# ── Task 2: check_ct_cascade ──────────────────────────────────────────────
# NOTE: plan used AESER/MHSER; MHSER binds no codelist (verified against meta.yaml),
# so the second-domain variable is MHPRESP, which binds C66742 like AESER.
# See evidence/failures/sp5_attempt_1.md.


def test_ct_cascade_flags_inconsistent_values(engine):
    # AESER + MHPRESP both bind codelist C66742 (No Yes Response). Different value sets.
    ae = pd.DataFrame({"DOMAIN": ["AE", "AE"], "AESER": ["Y", "N"]})
    mh = pd.DataFrame({"DOMAIN": ["MH"], "MHPRESP": ["U"]})
    findings = check_ct_cascade({"AE": ae, "MH": mh}, engine)
    assert any(f.rule == "GCASCADE" and "C66742" in f.message for f in findings)
    assert all(f.severity == "WARN" for f in findings)


def test_ct_cascade_silent_when_consistent(engine):
    ae = pd.DataFrame({"DOMAIN": ["AE"], "AESER": ["Y"]})
    mh = pd.DataFrame({"DOMAIN": ["MH"], "MHPRESP": ["Y"]})
    assert check_ct_cascade({"AE": ae, "MH": mh}, engine) == []


def test_ct_cascade_silent_single_domain(engine):
    ae = pd.DataFrame({"DOMAIN": ["AE", "AE"], "AESER": ["Y", "N"]})
    assert check_ct_cascade({"AE": ae}, engine) == []


# ── Task 3: check_impact + run_graph_checks ───────────────────────────────


def test_impact_flags_high_impact_variable(engine):
    # USUBJID appears in 55 domains (>= threshold 10) — high impact INFO.
    df = pd.DataFrame({"DOMAIN": ["AE"], "USUBJID": ["S1-1"], "AESER": ["Y"]})
    findings = check_impact({"AE": df}, engine)
    assert any(f.rule == "GIMPACT" and f.variable == "USUBJID" for f in findings)
    assert all(f.severity == "INFO" for f in findings)


def test_impact_silent_low_impact_variable(engine):
    # AETERM is AE-specific (1 domain) — below threshold, no impact finding for it.
    df = pd.DataFrame({"DOMAIN": ["AE"], "AETERM": ["headache"]})
    findings = check_impact({"AE": df}, engine)
    assert not any(f.variable == "AETERM" for f in findings)


def test_run_graph_checks_merges_all_three(engine):
    # MHPRESP (not MHSER) binds C66742; equal-length columns (see sp5_attempt_1.md).
    ae = pd.DataFrame({"DOMAIN": ["AE", "AE"], "USUBJID": ["S1-1", "S1-2"], "AESER": ["Y", "N"]})
    mh = pd.DataFrame({"DOMAIN": ["MH"], "MHPRESP": ["U"]})
    findings = run_graph_checks({"AE": ae, "MH": mh}, engine)
    rules = {f.rule for f in findings}
    assert {"GIMPACT", "GXDOM", "GCASCADE"} <= rules
    assert not any(f.severity == "ERROR" for f in findings)  # advisory only
