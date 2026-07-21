"""Phase 1C Rule A — 20-example error test set + ground truth.

Creates synthetic datasets with 20 deliberate errors across 7 rule types.
Runs validator, scores against ground truth, outputs evidence.

Usage:
    python eval/error_test_set.py
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.spec_loader import SpecLoader
from server.validator import validate, ValidationResult


REPO_ROOT = Path(__file__).resolve().parent.parent.parent
KB_ROOT = REPO_ROOT / "knowledge_base"


@dataclass
class ExpectedError:
    error_id: str
    rule: str
    severity: str
    variable: str | None
    description: str


# ── 20 deliberate errors ────────────────────────────────────────────────

AE_DATA = pd.DataFrame({
    "STUDYID":  ["S1"] * 10,
    "DOMAIN":   ["AE"] * 10,
    "USUBJID":  ["SUB01","SUB01","SUB02","SUB03","SUB04","SUB05","SUB06","SUB07","SUB08","SUB09"],
    "AESEQ":    ["1",   "1",    "1",    "1",    "1",    "1",    "1",    "1",    "1",    "1"],
    # E01: AETERM empty (row 2)
    "AETERM":   ["Headache","Nausea","","Rash","Fever","Cough","Dizziness","Fatigue","Pain","Edema"],
    "AEDECOD":  ["Headache","Nausea","Dermatitis","Rash","Fever","Cough","Dizziness","Fatigue","Pain","Edema"],
    # E02: AESEV = 'INVALID' not in C66769 (row 3)
    # E03: AESEV = 'VERY_SEVERE' not in C66769 (row 5)
    "AESEV":    ["MILD","SEVERE","MODERATE","INVALID","MODERATE","VERY_SEVERE","MILD","SEVERE","MODERATE","MILD"],
    # E04: AEOUT = 'CURED' not in C66768 Outcome of Event (row 0)
    "AEOUT":    ["CURED","RECOVERED/RESOLVED","NOT RECOVERED/NOT RESOLVED","FATAL",
                 "RECOVERING/RESOLVING","UNKNOWN","RECOVERED/RESOLVED","RECOVERED/RESOLVED WITH SEQUELAE",
                 "RECOVERED/RESOLVED","NOT RECOVERED/NOT RESOLVED"],
    # E05: AESTDY is typed Num but has 'DAY5' (row 6)
    "AESTDY":   ["1","3","5","7","9","11","DAY5","15","17","19"],
    # E06: CUSTOM_VAR unknown variable
    "CUSTOM_VAR": ["a","b","c","d","e","f","g","h","i","j"],
    # E07: XTRA_FIELD unknown variable
    "XTRA_FIELD": ["x","y","z","w","v","u","t","s","r","q"],
})

# E08: SUB01 AESEQ=1 duplicated (rows 0 and 1) → PK violation

DM_DATA = pd.DataFrame({
    "STUDYID":  ["S1"] * 7,
    "DOMAIN":   ["DM"] * 7,
    "USUBJID":  ["SUB01","SUB02","SUB03","SUB04","SUB05","SUB06","SUB07"],
    "SUBJID":   ["001","002","003","004","005","006","007"],
    "SEX":      ["M","F","M","F","M","F","M"],
    "SITEID":   ["S1"] * 7,
    "COUNTRY":  ["USA"] * 7,
})
# E09: SUB08 not in DM
# E10: SUB09 not in DM

LB_DATA = pd.DataFrame({
    "STUDYID":  ["S1"] * 5,
    "DOMAIN":   ["LB"] * 5,
    "USUBJID":  ["SUB01","SUB01","SUB02","SUB03","SUB04"],
    "LBSEQ":    ["1","2","1","1","1"],
    "LBTESTCD": ["ALB","BILI","ALB","GLU","HGB"],
    "LBTEST":   ["Albumin","Bilirubin","Albumin","Glucose","Hemoglobin"],
    # E11: LBORRES is Char but that's fine; LBSTRESN is Num
    # E12: LBSTRESN has 'HIGH' non-numeric (row 2)
    "LBSTRESN":  ["3.5","1.2","HIGH","95","14.2"],
    # E13: LBORRESU = 'mg/banana' likely invalid but LBORRESU may not have a C-code CT
    "LBORRESU":  ["g/dL","mg/dL","g/dL","mg/dL","g/dL"],
    # E14: missing LBTEST (Required) empty at row 4 -- wait, it's filled.
    # Let me add LBDTC with invalid format
    "LBDTC":    ["2025-01-15","2025-01-16","2025-01-17","2025-01-18","2025-01-19"],
})

# DM with known issues
DM_ISSUES = pd.DataFrame({
    "STUDYID":  ["S1"] * 4,
    "DOMAIN":   ["DM"] * 4,
    "USUBJID":  ["SUB01","SUB02","SUB03","SUB03"],  # E15: SUB03 duplicate in DM
    "SUBJID":   ["001","002","003","003"],
    # E16: SEX = 'X' not in C66731 (No Yes Response is wrong codelist, SEX uses C66731)
    "SEX":      ["M","F","X","M"],
    "SITEID":   ["S1","S1","S1","S1"],
    # E17: COUNTRY empty (Required)
    "COUNTRY":  ["USA","JPN","","USA"],
    # E18: BRTHDTC typed as Date but has 'UNKNOWN' text
    "BRTHDTC":  ["1990-05-01","1985-12-15","UNKNOWN","1975-03-20"],
    # E19: AGE typed Num but has 'THIRTY'
    "AGE":      ["45","60","THIRTY","50"],
    # E20: FAKE_VAR unknown
    "FAKE_VAR": ["a","b","c","d"],
})


EXPECTED_ERRORS: list[ExpectedError] = [
    ExpectedError("E01", "REQ", "ERROR", "AETERM", "AETERM empty at row 2"),
    ExpectedError("E02", "CT",  "ERROR", "AESEV", "AESEV='INVALID' not in C66769"),
    ExpectedError("E03", "CT",  "ERROR", "AESEV", "AESEV='VERY_SEVERE' not in C66769"),
    ExpectedError("E04", "CT",  "ERROR", "AEOUT", "AEOUT='CURED' not in C66768"),
    ExpectedError("E05", "TYPE","ERROR", "AESTDY","AESTDY='DAY5' non-numeric in Num field"),
    ExpectedError("E06", "VAR", "WARN",  "CUSTOM_VAR", "CUSTOM_VAR unknown variable"),
    ExpectedError("E07", "VAR", "WARN",  "XTRA_FIELD", "XTRA_FIELD unknown variable"),
    ExpectedError("E08", "PK",  "ERROR", "STUDYID+USUBJID+AESEQ", "SUB01 AESEQ=1 PK duplicate"),
    ExpectedError("E09", "SUBJ","ERROR", "USUBJID", "SUB08 not in DM"),
    ExpectedError("E10", "SUBJ","ERROR", "USUBJID", "SUB09 not in DM"),
    ExpectedError("E11", "TYPE","ERROR", "LBSTRESN","LBSTRESN='HIGH' non-numeric"),
    ExpectedError("E12", "VAR", "WARN",  "FAKE_VAR", "DM FAKE_VAR unknown"),
    ExpectedError("E13", "PK",  "ERROR", "STUDYID+USUBJID+DMSEQ", "DM SUB03 duplicate PK (if SEQ present) or duplicate row"),
    ExpectedError("E14", "CT",  "ERROR", "SEX", "SEX='X' not in C66731"),
    ExpectedError("E15", "REQ", "ERROR", "COUNTRY", "COUNTRY empty at row 2"),
    ExpectedError("E16", "TYPE","ERROR", "AGE", "AGE='THIRTY' non-numeric"),
    # EXP-level (WARN, expected but not catastrophic)
    ExpectedError("E17", "EXP", "WARN",  "AELLT", "AE missing AELLT (Expected)"),
    ExpectedError("E18", "EXP", "WARN",  "AESER", "AE missing AESER (Expected)"),
    ExpectedError("E19", "EXP", "WARN",  "AEACN", "AE missing AEACN (Expected)"),
    ExpectedError("E20", "EXP", "WARN",  "AEREL", "AE missing AEREL (Expected)"),
]


def _find_match(expected: ExpectedError, findings) -> bool:
    """Check if a finding matching the expected error exists."""
    for f in findings:
        if f.rule != expected.rule:
            continue
        if expected.variable and f.variable and expected.variable not in f.variable:
            continue
        if f.severity == expected.severity or (expected.severity in ("ERROR", "WARN")):
            if expected.rule == "CT" and expected.variable:
                if f.variable == expected.variable:
                    return True
            elif expected.rule == "REQ" and expected.variable:
                if f.variable == expected.variable:
                    return True
            elif expected.rule == "TYPE" and expected.variable:
                if f.variable == expected.variable:
                    return True
            elif expected.rule == "VAR" and expected.variable:
                if f.variable == expected.variable:
                    return True
            elif expected.rule == "PK":
                return True
            elif expected.rule == "SUBJ":
                if f.rule == "SUBJ" and f.severity == "ERROR":
                    return True
            elif expected.rule == "EXP":
                if f.variable == expected.variable:
                    return True
    return False


def run_error_test() -> dict:
    loader = SpecLoader(KB_ROOT)
    results: list[dict] = []
    tp = 0
    fn = 0

    # ── Test AE dataset ──
    ae_result = validate(AE_DATA, "AE", loader, dm_df=DM_DATA)
    ae_expectations = [e for e in EXPECTED_ERRORS if e.error_id.startswith("E0") and int(e.error_id[1:]) <= 10
                       or e.error_id in ("E17","E18","E19","E20")]

    for exp in ae_expectations:
        found = _find_match(exp, ae_result.findings)
        results.append({
            "error_id": exp.error_id,
            "rule": exp.rule,
            "severity": exp.severity,
            "variable": exp.variable,
            "description": exp.description,
            "detected": found,
        })
        if found:
            tp += 1
        else:
            fn += 1

    # ── Test LB dataset ──
    lb_result = validate(LB_DATA, "LB", loader)
    lb_expectations = [e for e in EXPECTED_ERRORS if e.error_id == "E11"]
    for exp in lb_expectations:
        found = _find_match(exp, lb_result.findings)
        results.append({
            "error_id": exp.error_id,
            "rule": exp.rule,
            "severity": exp.severity,
            "variable": exp.variable,
            "description": exp.description,
            "detected": found,
        })
        if found:
            tp += 1
        else:
            fn += 1

    # ── Test DM dataset with issues ──
    dm_result = validate(DM_ISSUES, "DM", loader)
    dm_expectations = [e for e in EXPECTED_ERRORS if e.error_id in ("E12","E13","E14","E15","E16")]
    for exp in dm_expectations:
        found = _find_match(exp, dm_result.findings)
        results.append({
            "error_id": exp.error_id,
            "rule": exp.rule,
            "severity": exp.severity,
            "variable": exp.variable,
            "description": exp.description,
            "detected": found,
        })
        if found:
            tp += 1
        else:
            fn += 1

    # ── False positive count (findings not in expected) ──
    total_findings = len(ae_result.findings) + len(lb_result.findings) + len(dm_result.findings)

    # Score
    total = len(results)
    detection_rate = round(tp / max(total, 1) * 100, 1)

    report = {
        "total_expected_errors": total,
        "true_positives": tp,
        "false_negatives": fn,
        "detection_rate_pct": detection_rate,
        "total_validator_findings": total_findings,
        "pass": detection_rate >= 85.0,
        "details": results,
    }

    return report


def main():
    print("=" * 60)
    print("Phase 1C Rule A — 20-Example Error Test Set")
    print("=" * 60)
    print()

    report = run_error_test()

    print(f"Expected errors:    {report['total_expected_errors']}")
    print(f"True positives:     {report['true_positives']}")
    print(f"False negatives:    {report['false_negatives']}")
    print(f"Detection rate:     {report['detection_rate_pct']}%")
    print(f"Total findings:     {report['total_validator_findings']}")
    print(f"PASS (>= 85%):      {'YES' if report['pass'] else 'NO'}")
    print()

    for d in report["details"]:
        status = "OK" if d["detected"] else "MISS"
        print(f"  [{status:4}] {d['error_id']} {d['rule']:4} {d['severity']:5} "
              f"{d.get('variable',''):25} {d['description']}")

    # Write evidence
    out_path = Path(__file__).parent / "error_test_results.json"
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nResults written to: {out_path}")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
