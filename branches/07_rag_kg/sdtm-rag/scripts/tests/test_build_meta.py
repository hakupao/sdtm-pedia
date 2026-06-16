from __future__ import annotations
from pathlib import Path
import pytest
from scripts.build_meta import (
    build_meta, _split_ct, _parse_label, _same_class_map,
    _relations_curated, _model_defhome, _codelists,
)

KB_ROOT = Path(__file__).resolve().parents[5] / "knowledge_base"

@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT

@pytest.fixture(scope="module")
def meta(kb_root):
    return build_meta(kb_root)


# ── Task 1: domain scalars + SUPPQUAL flag ────────────────────────────────

def test_domain_count_and_special_flag(meta):
    domains = {d["domain"]: d for d in meta["domains"]}
    # 64 个目录（含 SUPPQUAL），但只 63 个计入标准域
    assert len(domains) == 64
    assert sum(1 for d in meta["domains"] if d["counts_toward_63"]) == 63
    assert domains["SUPPQUAL"]["is_special"] is True
    assert domains["SUPPQUAL"]["counts_toward_63"] is False
    assert domains["AE"]["counts_toward_63"] is True

def test_domain_scalars(meta):
    ae = next(d for d in meta["domains"] if d["domain"] == "AE")
    assert ae["class"] == "Events"
    assert ae["label"] == "Adverse Events"
    assert ae["structure"] == "One record per adverse event per subject"

def test_parse_label_unit():
    assert _parse_label("# AE — Adverse Events") == "Adverse Events"
    assert _parse_label("# LB — Laboratory Test Results") == "Laboratory Test Results"
    assert _parse_label("no title here") == ""


# ── Task 2: variables + ct_codes/ct_dict split ────────────────────────────

def test_split_ct_unit():
    assert _split_ct("C66742") == (["C66742"], [])
    assert _split_ct("C85494; C128684; C128683") == (["C85494", "C128684", "C128683"], [])
    assert _split_ct("MedDRA") == ([], ["MedDRA"])
    assert _split_ct("ISO 8601 datetime or interval") == ([], ["ISO 8601 datetime or interval"])
    assert _split_ct("") == ([], [])

def test_variables_present_and_ct(meta):
    ae = next(d for d in meta["domains"] if d["domain"] == "AE")
    by_name = {v["name"]: v for v in ae["variables"]}
    aeser = by_name["AESER"]
    assert aeser["role"] == "Record Qualifier"
    assert aeser["type"] == "Char"
    assert aeser["core"] == "Exp"
    assert aeser["label"] == "Serious Event"
    assert aeser["ct_codes"] == ["C66742"]
    assert aeser["ct_dict"] == []
    # STUDYID has no controlled terms
    assert by_name["STUDYID"]["ct_codes"] == []
