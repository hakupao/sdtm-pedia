"""SP5 end-to-end golden: run_graph_checks over a synthetic study fixture.

Pass study = {AE, CM, PR}: RELREC-closed (AE -> CM, PR both present) with the shared
codelist C66742 (AESER/CMPRESP/PRPRESP) consistent (all Y) -> no GXDOM, no GCASCADE.
Fail study = {AE, MH}: CM absent (AE RELREC target) -> GXDOM; AESER {Y,N} vs MHPRESP {U}
-> GCASCADE. (Plan's {AE,CM,MH} pass set was not RELREC-closed; see sp5_attempt_1.md.)
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from server.config import settings
from server.graph_engine import GraphEngine
from server.graph_validator import run_graph_checks
from server.meta_store import MetaStore

FIX = Path(__file__).resolve().parent / "fixtures" / "sp5_study"


@pytest.fixture(scope="module")
def engine():
    return GraphEngine(MetaStore(settings.meta_path))


def _load(name: str) -> pd.DataFrame:
    df = pd.read_csv(FIX / name, dtype=str, keep_default_na=False)
    df.columns = [c.upper() for c in df.columns]
    return df


def test_pass_study_no_completeness_or_cascade_warns(engine):
    study = {"AE": _load("ae_pass.csv"), "CM": _load("cm_pass.csv"), "PR": _load("pr_pass.csv")}
    findings = run_graph_checks(study, engine)
    # RELREC-closed -> no GXDOM WARN (soft non-RELREC INFO hints e.g. AE->FA are allowed).
    assert not any(f.rule == "GXDOM" and f.severity == "WARN" for f in findings)
    assert not any(f.rule == "GCASCADE" for f in findings)  # AESER/CMPRESP/PRPRESP all Y
    assert all(f.severity in ("INFO", "WARN") for f in findings)


def test_fail_study_hits_completeness_and_cascade(engine):
    study = {"AE": _load("ae_fail.csv"), "MH": _load("mh_fail.csv")}  # no CM; AESER {Y,N} vs MHPRESP {U}
    findings = run_graph_checks(study, engine)
    assert any(f.rule == "GXDOM" and "CM" in f.message for f in findings)
    assert any(f.rule == "GCASCADE" and "C66742" in f.message for f in findings)
    assert not any(f.severity == "ERROR" for f in findings)
