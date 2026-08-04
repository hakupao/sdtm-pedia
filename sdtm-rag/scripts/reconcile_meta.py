"""Independent-anchor reconciliation for data/meta/meta.yaml.

Does NOT reuse spec_loader / build_meta parsing — re-derives authoritative
totals from VARIABLE_INDEX.md / INDEX.md text plus a raw spec `- **Order:**`
grep, to break the tautology trap. The grep is a SECOND independent anchor for
the entry total: it cross-checks the VARIABLE_INDEX header count from a second
place (raw spec text vs the published header). Both are independent of the
generator, but they measure the SAME number (the per-domain entry total, 1917)
— it is not a distinct third quantity. Exit 1 on any mismatch.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from re import Match

import yaml


def _require(m: Match[str] | None, what: str, path: Path) -> Match[str]:
    """Make anchor-parse drift fail LOUD (named anchor + source file), so the
    gate's own parsing never dies with a bare NoneType AttributeError."""
    if m is None:
        raise ValueError(
            f"reconcile anchor parse failed: {what} not found in {path} (format drift?)"
        )
    return m


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
    vidx_path = kb_root / "VARIABLE_INDEX.md"
    index_path = kb_root / "INDEX.md"
    vidx = vidx_path.read_text(encoding="utf-8")
    index = index_path.read_text(encoding="utf-8")

    # VARIABLE_INDEX.md is English-only; the legacy CJK header is still accepted
    # so older copies of the file keep reconciling.
    hdr = _require(
        re.search(
            r"(?:Unique variables|唯一变量数):\s*(\d+)\s*\|\s*"
            r"(?:Total entries|条目总数):\s*(\d+)\s*\|\s*"
            r"(?:Domains covered|覆盖域):\s*(\d+)",
            vidx,
        ),
        "VARIABLE_INDEX header (Unique variables/Total entries/Domains covered)",
        vidx_path,
    )
    uniq, entries, _cov = (int(hdr.group(i)) for i in (1, 2, 3))

    def _domain_count(var: str) -> int:
        m = _require(
            re.search(rf"^\|\s*{re.escape(var)}\s*\|\s*(\d+)\s*\|", vidx, re.MULTILINE),
            f"VARIABLE_INDEX row for {var}",
            vidx_path,
        )
        return int(m.group(1))

    cl = _require(
        re.search(r"\(([\d,]+)\s*codelists,\s*([\d,]+)\s*terms\)", index),
        "INDEX codelists/terms aggregate",
        index_path,
    )
    codelists = int(cl.group(1).replace(",", ""))
    terms = int(cl.group(2).replace(",", ""))

    # Second independent anchor for the entry total: raw spec '- **Order:**'
    # grep cross-checks the VARIABLE_INDEX header count from a second place
    # (raw spec text vs published header). Same quantity (1917), not a third one.
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
        # terms_total is the WEAKEST of the 8 anchors: equality holds only if
        # INDEX's published term aggregate and meta's sum(term_count) both count
        # raw terms with no cross-codelist dedup. Both likely trace to the same
        # source xlsx, so this is a consistency check, not an independent one.
        "terms_total": terms,
        "TAETORD_domain_count": _domain_count("TAETORD"),
        "VISITDY_domain_count": _domain_count("VISITDY"),
        "raw_order_line_count": raw_order,
    }


def reconcile(meta_path: Path, kb_root: Path) -> list[dict]:
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    derived = _meta_derived(meta)
    anchors = _anchors(kb_root)
    # raw_order_line_count is a second independent anchor for the entry total:
    # it measures the SAME quantity as variable_entries_total (one - **Order:**
    # line per variable per domain), so meta's number is compared against it too.
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
    kb_root = here.parents[2] / "knowledge_base"
    meta_path = here.parents[1] / "data" / "meta" / "meta.yaml"
    report = reconcile(meta_path, kb_root)
    for c in report:
        flag = "OK " if c["ok"] else "FAIL"
        print(f"[{flag}] {c['check']}: expected={c['expected']} actual={c['actual']}")
    if any(not c["ok"] for c in report):
        sys.exit(1)


if __name__ == "__main__":
    main()
