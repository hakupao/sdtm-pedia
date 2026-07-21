"""SP5 study-level report aggregation."""
from __future__ import annotations

from server.report import FullReport, generate_study_json
from server.validator import Finding, ValidationResult


def _full(domain: str, findings: list[Finding]) -> FullReport:
    vr = ValidationResult(domain=domain, row_count=1, col_count=3, findings=findings)
    return FullReport(domain=domain, file_path=f"{domain}.csv", row_count=1, col_count=3,
                      completeness_pct=100.0, validation=vr, review=None)


def test_study_verdict_warns_on_graph_findings():
    ds = [_full("AE", []), _full("MH", [])]
    graph = [Finding("WARN", "GXDOM", None, "AE RELREC-linked to CM, absent")]
    out = generate_study_json(ds, graph)
    assert out["study_verdict"] == "PASS_WITH_WARNINGS"
    assert out["n_datasets"] == 2
    assert sorted(out["domains"]) == ["AE", "MH"]
    assert out["total_warnings"] == 1
    assert out["graph_findings"][0]["rule"] == "GXDOM"
    assert len(out["datasets"]) == 2


def test_study_verdict_fail_on_dataset_error():
    ds = [_full("AE", [Finding("ERROR", "REQ", "USUBJID", "missing")])]
    out = generate_study_json(ds, [])
    assert out["study_verdict"] == "FAIL"
    assert out["total_errors"] == 1


def test_study_verdict_pass_clean():
    out = generate_study_json([_full("AE", [])], [])
    assert out["study_verdict"] == "PASS"
