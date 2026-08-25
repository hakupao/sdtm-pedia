"""Study workflow-{Events,Activities,Forms} 三表解析. 零真名: 断言只用计数与形态."""
import pytest

from scripts.study.parse_config_report import (
    parse_activities,
    parse_events,
    parse_form_assignments,
)
from scripts.study.paths import resolve_study


@pytest.fixture(scope="module")
def cfg_path():
    return resolve_study("st01").config_report_new


def test_parse_events_counts(cfg_path):
    evs = parse_events(cfg_path)
    assert len(evs) == 17                                   # 含脚注
    real = [e for e in evs if not e.is_trailer]
    assert len(real) == 14
    assert all(e.oid and " " not in e.oid for e in real)


def test_parse_events_type_distribution(cfg_path):
    real = [e for e in parse_events(cfg_path) if not e.is_trailer]
    kinds = {}
    for e in real:
        kinds[e.event_type] = kinds.get(e.event_type, 0) + 1
    assert sorted(kinds.values()) == [1, 13]                # 13 + 1, 不写死日文取值


def test_parse_activities_counts(cfg_path):
    acs = parse_activities(cfg_path)
    assert len(acs) == 80
    real = [a for a in acs if not a.is_trailer]
    assert len(real) == 77
    assert all(a.oid and a.event_oid for a in real)


def test_parse_form_assignments_counts(cfg_path):
    fms = parse_form_assignments(cfg_path)
    assert len(fms) == 112
    real = [f for f in fms if not f.is_trailer]
    assert len(real) == 110
    assert len({f.form_oid for f in real}) == 21


def test_repeating_values(cfg_path):
    real = [f for f in parse_form_assignments(cfg_path) if not f.is_trailer]
    counts = {}
    for f in real:
        counts[f.repeating] = counts.get(f.repeating, 0) + 1
    assert counts == {"0": 106, "Unlimited": 4}


def test_scheduling_columns_are_sparse_by_design(cfg_path):
    """本研究 Scheduling 只有 Reference/±days 各 2 条非空 — 钉死, 防未来静默变化."""
    real = [e for e in parse_events(cfg_path) if not e.is_trailer]
    assert sum(1 for e in real if e.sched_reference) == 2
    assert sum(1 for e in real if e.sched_minus_days) == 2
    assert sum(1 for e in real if e.sched_plus_days) == 2


def test_row_numbers_are_physical(cfg_path):
    """row 必须是可溯源物理行号 (Events 数据自第 4 行起)."""
    evs = parse_events(cfg_path)
    assert evs[0].row == 4
    assert evs[-1].row == 22
