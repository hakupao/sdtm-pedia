"""catalog 三池 + spec §5.A/B/C 三闸. 零真名: 只断言计数/集合关系."""
import collections

import pytest

from scripts.study.build_catalog import build_catalog
from scripts.study.paths import resolve_study


@pytest.fixture(scope="module")
def cat():
    return build_catalog(resolve_study("st01"))


def test_three_pools_exist_with_expected_sizes(cat):
    assert len(cat["events"]) == 14
    assert len(cat["activities"]) == 77
    assert len(cat["assignments"]) == 110


def test_gate_a_cross_check_against_design_summary(cat):
    """spec §5.A: 四条数字必须与 ConfigReport 设计摘要吻合 (已由 PDF 封面独立确认)."""
    asg = cat["assignments"]
    assert len(asg) == 110
    assert len({a["form_oid"] for a in asg}) == 21
    by_type = {e["oid"]: e["event_type"] for e in cat["events"]}
    counts = collections.Counter(by_type[a["event_oid"]] for a in asg)
    assert sorted(counts.values()) == [1, 109]


def test_gate_b_referential_integrity(cat):
    """spec §5.B: 四条引用完整性."""
    ev_ids = {e["oid"] for e in cat["events"]}
    ac_ids = {a["oid"] for a in cat["activities"]}
    form_ids = {f["oid"] for f in cat["forms"]}
    assert {a["event_oid"] for a in cat["activities"]} <= ev_ids
    assert {a["event_oid"] for a in cat["assignments"]} <= ev_ids
    assert {a["activity_oid"] for a in cat["assignments"]} <= ac_ids
    assert {a["form_oid"] for a in cat["assignments"]} <= form_ids


def test_gate_c_transpose_consistency(cat):
    """spec §5.C: assignments.hidden_items 与 items 的 Hidden in activity 互为精确转置.

    这是解析正确性的**独立参照物** —— 两处表示由 Viedoc 分别导出, 一致即互证。
    不一致 ⇒ spec §6 S2 触发, 停。
    """
    fwd = collections.defaultdict(set)
    for a in cat["assignments"]:
        if not a["hidden_items"].strip():
            continue
        for x in a["hidden_items"].replace("\n", ",").split(","):
            if x.strip():
                fwd[a["activity_oid"]].add(x.strip())
    bwd = collections.defaultdict(set)
    for it in cat["items"]:
        raw = str(it["raw"].get("Visibility::Hidden in activity") or "")
        for x in raw.replace("\n", ",").split(","):
            if x.strip():
                bwd[x.strip()].add(it["item_oid"])
    assert set(fwd) == set(bwd), "两侧 activity 键集不同"
    assert len(fwd) == 61
    mismatched = [k for k in fwd if fwd[k] != bwd[k]]
    assert mismatched == [], f"{len(mismatched)} 个 activity 的 item 集合不一致"


def test_hidden_activities_subset_of_activities(cat):
    """items 引用的 activity 必须全部在 activities 池里 (否则采集范围推导会静默丢)."""
    ac_ids = {a["oid"] for a in cat["activities"]}
    used = set()
    for it in cat["items"]:
        raw = str(it["raw"].get("Visibility::Hidden in activity") or "")
        for x in raw.replace("\n", ",").split(","):
            if x.strip():
                used.add(x.strip())
    assert len(used) == 61
    assert used <= ac_ids


def test_ledger_covers_workflow_sheets(cat):
    sheets = collections.Counter(r["sheet"] for r in cat["ledger"])
    assert sheets["Study workflow-Events"] == 17
    assert sheets["Study workflow-Activities"] == 80
    assert sheets["Study workflow-Forms"] == 112


def test_no_consumed_column_is_silently_empty(cat):
    """键名守卫 (控制方 Ruling I-2, 源自 Task 2 审查 I-1)。

    三个 parse 函数只有 ID 列走 `_req()`; 其余字段用 `r.get(key, "")` —— 上游改列名时
    **不报错, 静默给 ""**, 而 Task 2 的测试仍全绿。本条钉死"每个被消费的必填字段至少有值",
    用 `> 0` 而非精确计数: 精确计数需要先看数据再定判据, 违反判据先于数据。
    注: `hidden_items` 这一最关键字段另有闸 C (转置 61/61) 兜底, 静默全空会让闸 C 先红。
    刻意不含 description / visibility_condition —— 它们**合法地**稀疏。
    """
    required = [
        ("events", ["oid", "name", "event_type"]),
        ("activities", ["oid", "event_oid", "name"]),
        ("assignments", ["event_oid", "activity_oid", "form_oid",
                         "repeating", "item_visibility", "hidden_items"]),
    ]
    for pool, fields in required:
        for f in fields:
            n = sum(1 for r in cat[pool] if str(r[f]).strip())
            assert n > 0, f"{pool}.{f} 全空 — 列名可能已改, .get() 静默返回 ''"
