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
    assert any(f.rule == "GXDOM" and f.severity == "WARN" and "CM" in f.message for f in findings)
    assert all(f.severity in ("WARN", "INFO") for f in findings)  # advisory only, never ERROR


def test_completeness_silent_when_relrec_target_present(engine):
    # Submitting AE and CM -> CM is never named as an absent partner ("...to CM..."),
    # though CM may appear as the *source* of its own hints (e.g. "Domain CM related to EC").
    findings = check_completeness({"AE": _df("AE"), "CM": _df("CM")}, engine)
    assert not any("to CM" in f.message for f in findings)


def test_completeness_symmetric_relrec(engine):
    # RELREC is bidirectional: submitting CM without AE also warns (AE is CM's RELREC
    # partner, from the AE->CM edge), not just AE-without-CM.
    findings = check_completeness({"CM": _df("CM")}, engine)
    assert any(f.rule == "GXDOM" and f.severity == "WARN" and "AE" in f.message for f in findings)


def test_completeness_curated_relation_is_info(engine):
    # AE is curated-related to FA (Findings About, non-RELREC) — a softer INFO hint, not
    # a WARN, when FA is absent.
    findings = check_completeness({"AE": _df("AE")}, engine)
    assert any(f.rule == "GXDOM" and f.severity == "INFO" and "FA" in f.message for f in findings)


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


def test_ct_cascade_silent_when_subset_coverage(engine):
    # AE uses {Y}, MH uses {Y,N,U} for shared C66742 — a legitimate coverage subset
    # (nested), NOT an inconsistency. Only non-nested divergence should WARN.
    ae = pd.DataFrame({"DOMAIN": ["AE"], "AESER": ["Y"]})
    mh = pd.DataFrame({"DOMAIN": ["MH", "MH", "MH"], "MHPRESP": ["Y", "N", "U"]})
    assert check_ct_cascade({"AE": ae, "MH": mh}, engine) == []


# ── Task 3: check_impact + run_graph_checks ───────────────────────────────


def test_impact_flags_high_impact_nonidentifier(engine):
    # EPOCH appears in 44 domains (>= threshold 10) and is role=Timing (not an
    # Identifier) — a genuinely informative high-impact variable.
    df = pd.DataFrame({"DOMAIN": ["AE"], "EPOCH": ["TREATMENT"]})
    findings = check_impact({"AE": df}, engine)
    assert any(f.rule == "GIMPACT" and f.variable == "EPOCH" for f in findings)
    assert all(f.severity == "INFO" for f in findings)


def test_impact_skips_identifier_variables(engine):
    # USUBJID (55 domains) / DOMAIN / STUDYID are role=Identifier — their wide spread is
    # trivially known, so flagging them is pure noise. Skip them.
    df = pd.DataFrame({"STUDYID": ["S1"], "DOMAIN": ["AE"], "USUBJID": ["S1-1"]})
    findings = check_impact({"AE": df}, engine)
    assert not any(f.variable in {"USUBJID", "DOMAIN", "STUDYID"} for f in findings)


def test_impact_flags_high_impact_codelist(engine):
    # AESER binds C66742 (used by 41 domains) — codelist-level high impact still flagged.
    df = pd.DataFrame({"DOMAIN": ["AE"], "AESER": ["Y"]})
    findings = check_impact({"AE": df}, engine)
    assert any(f.rule == "GIMPACT" and "C66742" in f.message for f in findings)


def test_impact_silent_low_impact_variable(engine):
    # AETERM is AE-specific (1 domain) — below threshold, no impact finding for it.
    df = pd.DataFrame({"DOMAIN": ["AE"], "AETERM": ["headache"]})
    findings = check_impact({"AE": df}, engine)
    assert not any(f.variable == "AETERM" for f in findings)


def test_run_graph_checks_merges_all_three(engine):
    # EPOCH (non-Identifier, 44 domains) -> GIMPACT; MHPRESP binds C66742 (see sp5_attempt_1.md).
    ae = pd.DataFrame({"DOMAIN": ["AE", "AE"], "EPOCH": ["T", "T"], "AESER": ["Y", "N"]})
    mh = pd.DataFrame({"DOMAIN": ["MH"], "MHPRESP": ["U"]})
    findings = run_graph_checks({"AE": ae, "MH": mh}, engine)
    rules = {f.rule for f in findings}
    assert {"GIMPACT", "GXDOM", "GCASCADE"} <= rules
    assert not any(f.severity == "ERROR" for f in findings)  # advisory only
