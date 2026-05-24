"""Phase 1D — 5 validation scenario tests.

Extends Phase 1C error_test_set.py with 5 higher-level scenarios:
  V1: Valid VS dataset → 0 ERROR findings
  V2: CM dataset with mixed REQ+CT+TYPE errors
  V3: EX dataset with PK violations
  V4: Cross-domain USUBJID mismatch (AE subjects missing from DM)
  V5: Single-row minimal dataset → graceful handling

Usage:
    .venv/bin/python eval/validation_scenarios.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.spec_loader import SpecLoader  # noqa: E402
from server.validator import validate  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
KB_ROOT = REPO_ROOT / "knowledge_base"


def v1_valid_vs() -> dict:
    """Valid VS dataset with correct values → expect 0 ERROR findings."""
    df = pd.DataFrame({
        "STUDYID": ["S1"] * 3,
        "DOMAIN": ["VS"] * 3,
        "USUBJID": ["SUB01", "SUB02", "SUB03"],
        "VSSEQ": ["1", "1", "1"],
        "VSTESTCD": ["SYSBP", "DIABP", "HR"],
        "VSTEST": ["Systolic Blood Pressure", "Diastolic Blood Pressure", "Heart Rate"],
        "VSORRES": ["120", "80", "72"],
        "VSORRESU": ["mmHg", "mmHg", "beats/min"],
        "VSDTC": ["2025-01-15", "2025-01-15", "2025-01-15"],
    })
    loader = SpecLoader(KB_ROOT)
    result = validate(df, "VS", loader)
    errors = [f for f in result.findings if f.severity == "ERROR"]
    return {
        "scenario": "V1",
        "description": "Valid VS dataset → expect 0 ERROR",
        "total_findings": len(result.findings),
        "error_count": len(errors),
        "pass": len(errors) == 0,
    }


def v2_cm_mixed_errors() -> dict:
    """CM dataset with REQ+CT+TYPE errors → expect at least 3 findings."""
    df = pd.DataFrame({
        "STUDYID": ["S1"] * 4,
        "DOMAIN": ["CM"] * 4,
        "USUBJID": ["SUB01", "SUB02", "SUB03", "SUB04"],
        "CMSEQ": ["1", "1", "1", "1"],
        "CMTRT": ["Aspirin", "", "Ibuprofen", "Metformin"],
        "CMSTDY": ["1", "DAY2", "5", "7"],
    })
    loader = SpecLoader(KB_ROOT)
    result = validate(df, "CM", loader)
    errors = [f for f in result.findings if f.severity == "ERROR"]
    has_req = any(f.rule == "REQ" for f in result.findings)
    has_type = any(f.rule == "TYPE" for f in result.findings)
    return {
        "scenario": "V2",
        "description": "CM dataset with REQ+TYPE errors",
        "total_findings": len(result.findings),
        "error_count": len(errors),
        "has_req_finding": has_req,
        "has_type_finding": has_type,
        "pass": has_req and has_type,
    }


def v3_ex_pk_violation() -> dict:
    """EX dataset with duplicate primary key → expect PK error."""
    df = pd.DataFrame({
        "STUDYID": ["S1"] * 4,
        "DOMAIN": ["EX"] * 4,
        "USUBJID": ["SUB01", "SUB01", "SUB02", "SUB02"],
        "EXSEQ": ["1", "1", "1", "2"],
        "EXTRT": ["DrugA", "DrugA", "DrugB", "DrugB"],
        "EXDOSE": ["100", "100", "200", "200"],
        "EXDOSU": ["mg", "mg", "mg", "mg"],
    })
    loader = SpecLoader(KB_ROOT)
    result = validate(df, "EX", loader)
    has_pk = any(f.rule == "PK" for f in result.findings)
    return {
        "scenario": "V3",
        "description": "EX dataset with PK duplicate (SUB01 EXSEQ=1)",
        "total_findings": len(result.findings),
        "has_pk_finding": has_pk,
        "pass": has_pk,
    }


def v4_cross_domain_subj() -> dict:
    """AE with subjects not in DM → expect SUBJ error."""
    dm = pd.DataFrame({
        "STUDYID": ["S1"] * 2,
        "DOMAIN": ["DM"] * 2,
        "USUBJID": ["SUB01", "SUB02"],
        "SUBJID": ["001", "002"],
        "SEX": ["M", "F"],
        "SITEID": ["S1", "S1"],
        "COUNTRY": ["USA", "USA"],
    })
    ae = pd.DataFrame({
        "STUDYID": ["S1"] * 3,
        "DOMAIN": ["AE"] * 3,
        "USUBJID": ["SUB01", "SUB03", "SUB04"],
        "AESEQ": ["1", "1", "1"],
        "AETERM": ["Headache", "Nausea", "Rash"],
        "AEDECOD": ["Headache", "Nausea", "Rash"],
    })
    loader = SpecLoader(KB_ROOT)
    result = validate(ae, "AE", loader, dm_df=dm)
    subj_findings = [f for f in result.findings if f.rule == "SUBJ"]
    missing_subs = set()
    for f in subj_findings:
        if f.value_sample:
            missing_subs.update(f.value_sample)
    return {
        "scenario": "V4",
        "description": "AE with subjects SUB03/SUB04 not in DM",
        "total_findings": len(result.findings),
        "subj_findings": len(subj_findings),
        "missing_subjects_detected": sorted(missing_subs),
        "pass": "SUB03" in missing_subs and "SUB04" in missing_subs,
    }


def v5_minimal_dataset() -> dict:
    """Single-row minimal AE dataset → graceful handling, no crash."""
    df = pd.DataFrame({
        "STUDYID": ["S1"],
        "DOMAIN": ["AE"],
        "USUBJID": ["SUB01"],
        "AESEQ": ["1"],
        "AETERM": ["Headache"],
        "AEDECOD": ["Headache"],
    })
    loader = SpecLoader(KB_ROOT)
    try:
        result = validate(df, "AE", loader)
        return {
            "scenario": "V5",
            "description": "Single-row minimal AE dataset → no crash",
            "total_findings": len(result.findings),
            "row_count": result.row_count,
            "pass": result.row_count == 1,
        }
    except Exception as e:
        return {
            "scenario": "V5",
            "description": "Single-row minimal AE dataset → no crash",
            "error": str(e),
            "pass": False,
        }


def main() -> int:
    print("=" * 60)
    print("Phase 1D — 5 Validation Scenarios")
    print("=" * 60)
    print()

    scenarios = [v1_valid_vs, v2_cm_mixed_errors, v3_ex_pk_violation,
                 v4_cross_domain_subj, v5_minimal_dataset]
    results = []
    all_pass = True

    for fn in scenarios:
        r = fn()
        results.append(r)
        status = "PASS" if r["pass"] else "FAIL"
        if not r["pass"]:
            all_pass = False
        print(f"  [{status}] {r['scenario']}: {r['description']}")
        for k, v in r.items():
            if k not in ("scenario", "description", "pass"):
                print(f"         {k}: {v}")
        print()

    print(f"Overall: {'ALL PASS' if all_pass else 'SOME FAIL'} ({sum(r['pass'] for r in results)}/5)")

    out_path = Path(__file__).parent / "validation_scenario_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Results written to: {out_path}")

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
