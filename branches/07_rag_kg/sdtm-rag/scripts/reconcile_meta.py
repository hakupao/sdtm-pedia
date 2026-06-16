"""Independent-anchor reconciliation for data/meta/meta.yaml.

Does NOT reuse spec_loader / build_meta parsing — re-derives authoritative
totals from VARIABLE_INDEX.md / INDEX.md text + a third raw Order-line count,
to break the tautology trap. Exit 1 on any mismatch.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


def _meta_derived(meta: dict) -> dict:
    domains = meta["domains"]
    all_var_names: list[str] = []
    taetord = visitdy = 0
    for d in domains:
        names = [v["name"] for v in d["variables"]]
        all_var_names.extend(names)
        if "TAETORD" in names:
            taetord += 1
        if "VISITDY" in names:
            visitdy += 1
    return {
        "domains_counts_toward_63": sum(1 for d in domains if d["counts_toward_63"]),
        "variable_entries_total": len(all_var_names),
        "unique_variable_names": len(set(all_var_names)),
        "codelists_total": len(meta["codelists"]),
        "terms_total": sum(c["term_count"] for c in meta["codelists"]),
        "TAETORD_domain_count": taetord,
        "VISITDY_domain_count": visitdy,
    }


def _anchors(kb_root: Path) -> dict:
    vidx = (kb_root / "VARIABLE_INDEX.md").read_text(encoding="utf-8")
    index = (kb_root / "INDEX.md").read_text(encoding="utf-8")

    hdr = re.search(
        r"唯一变量数:\s*(\d+)\s*\|\s*条目总数:\s*(\d+)\s*\|\s*覆盖域:\s*(\d+)", vidx
    )
    uniq, entries, _cov = (int(hdr.group(i)) for i in (1, 2, 3))

    def _domain_count(var: str) -> int:
        m = re.search(rf"^\|\s*{var}\s*\|\s*(\d+)\s*\|", vidx, re.MULTILINE)
        return int(m.group(1))

    cl = re.search(r"\(([\d,]+)\s*codelists,\s*([\d,]+)\s*terms\)", index)
    codelists = int(cl.group(1).replace(",", ""))
    terms = int(cl.group(2).replace(",", ""))

    # 第三独立源：裸数 spec.md 的 '- **Order:**' 行
    order_re = re.compile(r"^- \*\*Order:\*\*", re.MULTILINE)
    raw_order = sum(
        len(order_re.findall(p.read_text(encoding="utf-8")))
        for p in sorted((kb_root / "domains").glob("*/spec.md"))
    )
    return {
        "domains_counts_toward_63": 63,
        "variable_entries_total": entries,
        "unique_variable_names": uniq,
        "codelists_total": codelists,
        "terms_total": terms,
        "TAETORD_domain_count": _domain_count("TAETORD"),
        "VISITDY_domain_count": _domain_count("VISITDY"),
        "raw_order_line_count": raw_order,
    }


def reconcile(meta_path: Path, kb_root: Path) -> list[dict]:
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    derived = _meta_derived(meta)
    anchors = _anchors(kb_root)
    # raw_order is the third independent source; it counts the same quantity as
    # variable_entries_total (one - **Order:** line per variable per domain).
    derived["raw_order_line_count"] = derived["variable_entries_total"]
    report: list[dict] = []
    for check, expected in anchors.items():
        actual = derived.get(check)
        report.append(
            {
                "check": check,
                "expected": expected,
                "actual": actual,
                "ok": actual == expected,
            }
        )
    return report


def main() -> None:
    here = Path(__file__).resolve()
    # scripts -> sdtm-rag -> 07_rag_kg -> branches -> sdtm-pedia
    kb_root = here.parents[4] / "knowledge_base"
    meta_path = here.parents[1] / "data" / "meta" / "meta.yaml"
    report = reconcile(meta_path, kb_root)
    for c in report:
        flag = "OK " if c["ok"] else "FAIL"
        print(f"[{flag}] {c['check']}: expected={c['expected']} actual={c['actual']}")
    if any(not c["ok"] for c in report):
        sys.exit(1)


if __name__ == "__main__":
    main()
