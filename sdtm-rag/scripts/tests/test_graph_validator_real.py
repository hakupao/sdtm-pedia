"""SP5 real-data integration: run the graph checks over a small sample extracted from
the public CDISC pilot study (CDISCPILOT01, phuse-org/phuse-scripts). Guards the
real-data-driven behavior — genuine SDTM column/value shapes, extensible-codelist skip,
and RELREC completeness — against regression. See evidence/checkpoints/sp5_real_data_validation.md.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from server.config import settings
from server.graph_engine import GraphEngine
from server.graph_validator import run_graph_checks
from server.meta_store import MetaStore

FIX = Path(__file__).resolve().parent / "fixtures" / "sp5_real_sample"


@pytest.fixture(scope="module")
def engine():
    return GraphEngine(MetaStore(settings.meta_path))


@pytest.fixture(scope="module")
def real_study():
    study = {}
    for fp in sorted(FIX.glob("*.csv")):
        df = pd.read_csv(fp, dtype=str, keep_default_na=False)
        df.columns = [c.upper() for c in df.columns]
        study[df["DOMAIN"].iloc[0].upper()] = df
    return study


def test_real_study_runs_advisory_only(engine, real_study):
    # Real SDTM shapes (AE/CM/EX/LB/DM) must run without crashing, advisory-only.
    findings = run_graph_checks(real_study, engine)
    assert findings  # produces some advisory findings
    assert all(f.severity in ("INFO", "WARN") for f in findings)


def test_real_study_extensible_unit_codelist_not_flagged(engine, real_study):
    # C71620 (Unit, extensible, 830 terms) is bound by CM/EX/LB with disjoint unit
    # vocabularies — must NOT produce a cascade WARN (the real-data false positive we fixed).
    findings = run_graph_checks(real_study, engine)
    assert not any(f.rule == "GCASCADE" and "C71620" in f.message for f in findings)


def test_real_study_relrec_completeness_fires_for_absent_partner(engine, real_study):
    # The sample has AE but not PR; AE is RELREC-linked to PR -> a legitimate WARN.
    findings = run_graph_checks(real_study, engine)
    assert any(f.rule == "GXDOM" and f.severity == "WARN" and "PR" in f.message for f in findings)
