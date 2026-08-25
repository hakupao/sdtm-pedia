"""catalog 组装 + 覆盖台账 (孤儿=0 强制) + 新旧版 diff. 零 LLM."""
from __future__ import annotations

import argparse
import csv
import html
import json
import unicodedata
from dataclasses import asdict
from pathlib import Path

from scripts.study.parse_config_report import (
    ItemRow, parse_activities, parse_codelists, parse_events,
    parse_form_assignments, parse_forms, parse_items,
)
from scripts.study.paths import StudyPaths, resolve_study

_DIFF_FIELDS = ("data_type", "required", "label", "choices", "data_checks",
                "system_checks", "min_length", "max_length", "control_type")


def _norm(v):
    """比较用归一化: HTML 实体解码 (迭代到不动点, 解双重转义) → NFKC → 空白折叠.

    只用于比较判定与 diff 文案; catalog 存的是原值. 非 str (如 required: bool) 原样返回.
    """
    if not isinstance(v, str):
        return v
    prev, cur = None, v
    while cur != prev:
        prev, cur = cur, html.unescape(cur)
    return " ".join(unicodedata.normalize("NFKC", cur).split())


def _same(a, b) -> bool:
    """表記ゆれ判定: 导出设置差异 (NBSP 插入/顶替空格, HTML 实体) 不算变更.

    NBSP 既可能插在字符之间 (删掉才等价), 也可能顶替原有空格 (折叠成空格才等价),
    单条规则覆盖不全, 故两种归一化取或. 普通空格增删仅在改变 token 结构时报出;
    纯空白数量差异与首尾空白差异被抑制 (不做全空白无关比较).
    """
    if _norm(a) == _norm(b):
        return True
    if not isinstance(a, str) or not isinstance(b, str):
        return False
    return _norm(a.replace("\u00a0", "")) == _norm(b.replace("\u00a0", ""))


def _diff_items(new: dict[str, ItemRow], old: dict[str, ItemRow]):
    diffs: dict[str, list[str]] = {}
    for oid in new.keys() & old.keys():
        # 判定用归一化, 文案打原值: NFKC 会改写丸数字/全角括号等有语义的字符,
        # 卡片必须逐字可溯源到导出报告 (换行由 Task 7 渲染层 _flat 清洗)
        changes = [
            f"{f}: {getattr(old[oid], f)} → {getattr(new[oid], f)}"
            for f in _DIFF_FIELDS
            if not _same(getattr(old[oid], f), getattr(new[oid], f))
        ]
        if changes:
            diffs[oid] = changes
    return (diffs, sorted(new.keys() - old.keys()), sorted(old.keys() - new.keys()))


def build_catalog(sp: StudyPaths) -> dict:
    all_forms = parse_forms(sp.config_report_new)
    # 语义钉死: is_trailer 判据是 "oid 含空格 或 In use 空" 的并集; form 形态 Id (无空格)
    # 却 In use 空 = 疑似停用 form, 静默按脚注吞会让整个 form 无声消失 — 必须响亮失败,
    # 由人裁决 (真脚注行 Id 恒为含空格句子, 真实 21 form 的 In use 均非空)
    for f in all_forms:
        if f.is_trailer and f.oid and " " not in f.oid:
            raise ValueError(
                f"Forms row {f.row}: form-shaped Id {f.oid!r} with empty 'In use' — "
                f"疑似停用 form, 不能静默归为脚注")
        if f.is_trailer and not f.oid and (f.name or f.description):
            # 与 Items 二次闸对称: Id 空但带载荷的行不是已知脚注形态
            raise ValueError(
                f"Forms row {f.row}: blank Id with payload "
                f"(name={f.name!r}) — 未知行形态, 不能静默归为脚注")
    forms = [f for f in all_forms if not f.is_trailer]   # 表尾脚注行不进 catalog, 但进台账
    rows = parse_items(sp.config_report_new)
    codelists = parse_codelists(sp.config_report_new)
    items = [r for r in rows if r.row_type == "Item"]
    groups = {(r.form_oid, r.group_oid): r for r in rows if r.row_type == "Item group"}

    if sp.config_report_old is not None:
        old_index = {r.item_oid: r
                     for r in parse_items(sp.config_report_old) if r.row_type == "Item"}
        diffs, new_items, removed = _diff_items({r.item_oid: r for r in items}, old_index)
    else:   # 无旧版才降级; 旧版存在但 0 item 时 new_items = 全部 (不静默吞)
        diffs, new_items, removed = {}, [], []

    all_events = parse_events(sp.config_report_new)
    all_activities = parse_activities(sp.config_report_new)
    all_assignments = parse_form_assignments(sp.config_report_new)
    # 与 Forms 二次闸同构: OID 形态却缺关键载荷 = 未知行形态, 不能静默归为脚注
    for e in all_events:
        if e.is_trailer and e.oid and " " not in e.oid:
            raise ValueError(f"workflow Events row {e.row}: event-shaped Id {e.oid!r} "
                             f"判为脚注 — 未知行形态")
    for a in all_activities:
        if a.is_trailer and a.oid and " " not in a.oid:
            raise ValueError(f"workflow Activities row {a.row}: activity-shaped Id {a.oid!r} "
                             f"判为脚注 — 未知行形态")
    for f in all_assignments:
        if f.is_trailer and (f.activity_oid and " " not in f.activity_oid):
            raise ValueError(f"workflow Forms row {f.row}: 空 Form ID 但 Activity ID "
                             f"{f.activity_oid!r} 是 OID 形态 — 未知行形态, 不能静默归为脚注")
    events = [e for e in all_events if not e.is_trailer]
    activities = [a for a in all_activities if not a.is_trailer]
    assignments = [f for f in all_assignments if not f.is_trailer]

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
            # 二次闸: 归一化把一切未知都标成 Trailer, 这里区分真脚注与未知结构值
            # 词形启发 (单词形态如 "Section") + 语义不变量 (真脚注 item_oid 恒空;
            # 959 条真实 Item 行 item_oid 100% 非空) — 带 item 载荷的未知类型必须响亮失败
            ft = r.raw.get("Type and container::Field type", "")
            if (ft and " " not in ft) or r.item_oid:
                raise ValueError(f"orphan row {r.row} in Items and Groups: "
                                 f"unknown Field type {ft!r} (非脚注形态/含 item 载荷)")
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
    for e in all_events:
        ledger.append({"sheet": "Study workflow-Events", "row": e.row, "status": "mapped",
                       "target": "trailer:footnote" if e.is_trailer else f"event:{e.oid}"})
    for a in all_activities:
        ledger.append({"sheet": "Study workflow-Activities", "row": a.row, "status": "mapped",
                       "target": "trailer:footnote" if a.is_trailer
                                 else f"activity:{a.event_oid}/{a.oid}"})
    for f in all_assignments:
        ledger.append({"sheet": "Study workflow-Forms", "row": f.row, "status": "mapped",
                       "target": "trailer:footnote" if f.is_trailer
                                 else f"assignment:{f.event_oid}/{f.activity_oid}/{f.form_oid}"})

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
        "events": [asdict(e) for e in events],
        "activities": [asdict(a) for a in activities],
        "assignments": [asdict(f) for f in assignments],
        "diffs": diffs, "new_items": new_items, "removed_items": removed,
        # diffs=={} 双义消解: True=对比过且零变更, False=无旧版未对比 (Plan B 输入)
        "diff_available": sp.config_report_old is not None,
        "ledger": ledger,
    }


def write_catalog(catalog: dict, out_dir: Path) -> None:
    """写 catalog.json + coverage_ledger.csv.

    注意: coverage_ledger.csv 里 Code lists 行的 row 是占位符 (首 entry 0, 后续 -1),
    不是物理行号 — Code lists 逐 entry 记账, entry 无独立行号语义. Forms /
    Items and Groups 两个 sheet 的 row 才是可溯源的物理行号.
    """
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
          f"codelists={len(cat['codelists'])} events={len(cat['events'])} "
          f"activities={len(cat['activities'])} assignments={len(cat['assignments'])} "
          f"diffs={len(cat['diffs'])} "
          f"new={len(cat['new_items'])} removed={len(cat['removed_items'])} "
          f"ledger={n_status}")
    # 停用 form 被误判为 trailer 的观测哨: 版本间数字跳变即为信号
    print(f"trailer form_rows={sum(1 for r in trailers if r['sheet'] == 'Forms')} "
          f"item_rows={sum(1 for r in trailers if r['sheet'] == 'Items and Groups')}")


if __name__ == "__main__":
    main()
