"""catalog 组装 + 覆盖台账 (孤儿=0 强制) + 新旧版 diff. 零 LLM."""
from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict
from pathlib import Path

from scripts.study.parse_config_report import (
    ItemRow, parse_codelists, parse_forms, parse_items,
)
from scripts.study.paths import StudyPaths, resolve_study

_DIFF_FIELDS = ("data_type", "required", "label", "choices", "data_checks",
                "system_checks", "min_length", "max_length", "control_type")


def _diff_items(new: dict[str, ItemRow], old: dict[str, ItemRow]):
    diffs: dict[str, list[str]] = {}
    for oid in new.keys() & old.keys():
        changes = [
            f"{f}: {getattr(old[oid], f)} → {getattr(new[oid], f)}"
            for f in _DIFF_FIELDS if getattr(old[oid], f) != getattr(new[oid], f)
        ]
        if changes:
            diffs[oid] = changes
    return (diffs, sorted(new.keys() - old.keys()), sorted(old.keys() - new.keys()))


def build_catalog(sp: StudyPaths) -> dict:
    all_forms = parse_forms(sp.config_report_new)
    forms = [f for f in all_forms if not f.is_trailer]   # 表尾脚注行不进 catalog, 但进台账
    rows = parse_items(sp.config_report_new)
    codelists = parse_codelists(sp.config_report_new)
    items = [r for r in rows if r.row_type == "Item"]
    groups = {(r.form_oid, r.group_oid): r for r in rows if r.row_type == "Item group"}

    old_index: dict[str, ItemRow] = {}
    if sp.config_report_old is not None:
        old_index = {r.item_oid: r
                     for r in parse_items(sp.config_report_old) if r.row_type == "Item"}
    diffs, new_items, removed = _diff_items({r.item_oid: r for r in items}, old_index) \
        if old_index else ({}, [], [])

    referenced = {r.choices for r in items if r.choices}
    ledger: list[dict] = []
    for f in all_forms:
        target = "trailer:footnote" if f.is_trailer else f"form:{f.oid}"
        ledger.append({"sheet": "Forms", "row": f.row, "status": "mapped",
                       "target": target})
    for r in rows:
        if r.row_type == "Item":
            target = f"card:{sp.study_id}__{r.form_oid}__{r.item_oid}"
        elif r.row_type == "Item group":
            target = f"group:{r.form_oid}/{r.group_oid}"
        elif r.row_type == "Trailer":
            target = "trailer:footnote"
        else:
            raise ValueError(f"orphan row {r.row} in Items and Groups: "
                             f"unknown Field type {r.row_type!r}")
        ledger.append({"sheet": "Items and Groups", "row": r.row,
                       "status": "mapped", "target": target})
    for oid, cl in codelists.items():
        status = "mapped" if oid in referenced else "unreferenced"
        for i, _ in enumerate(cl.entries):
            ledger.append({"sheet": "Code lists", "row": -1 if i else 0,
                           "status": status, "target": f"codelist:{oid}"})

    item_dicts = []
    for r in items:
        d = asdict(r)
        if not r.group_name:  # group 名折进 item (group 行携带)
            g = groups.get((r.form_oid, r.group_oid))
            d["group_name"] = g.group_name if g else ""
        item_dicts.append(d)

    return {
        "study": sp.study_id,
        "version_new": sp.version_label_new,
        "version_old": sp.version_label_old,
        "forms": [asdict(f) for f in forms],
        "items": item_dicts,
        "codelists": {oid: {"data_type": c.data_type, "entries": c.entries}
                      for oid, c in codelists.items()},
        "diffs": diffs, "new_items": new_items, "removed_items": removed,
        "ledger": ledger,
    }


def write_catalog(catalog: dict, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=1), encoding="utf-8")
    with (out_dir / "coverage_ledger.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["sheet", "row", "status", "target"])
        w.writeheader()
        w.writerows(catalog["ledger"])


def main(argv=None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True)
    args = ap.parse_args(argv)
    sp = resolve_study(args.study)
    cat = build_catalog(sp)
    write_catalog(cat, sp.out_dir)
    n_status: dict[str, int] = {}
    for r in cat["ledger"]:
        n_status[r["status"]] = n_status.get(r["status"], 0) + 1
    trailers = [r for r in cat["ledger"] if r["target"] == "trailer:footnote"]
    print(f"forms={len(cat['forms'])} items={len(cat['items'])} "
          f"codelists={len(cat['codelists'])} diffs={len(cat['diffs'])} "
          f"new={len(cat['new_items'])} removed={len(cat['removed_items'])} "
          f"ledger={n_status}")
    # 停用 form 被误判为 trailer 的观测哨: 版本间数字跳变即为信号
    print(f"trailer form_rows={sum(1 for r in trailers if r['sheet'] == 'Forms')} "
          f"item_rows={sum(1 for r in trailers if r['sheet'] == 'Items and Groups')}")


if __name__ == "__main__":
    main()
