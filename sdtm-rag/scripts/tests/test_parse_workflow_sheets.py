"""Study workflow-{Events,Activities,Forms} 三表解析. 零真名: 断言只用计数与形态.

`len(x) == N` / `x[i].attr == N` 若直接写进 assert, 失败时 pytest assertion rewriting
会把 x (真实 EventDef/ActivityDef/FormAssignment 列表, 含真实 oid/label) 整个打进
stdout —— 与 test_catalog_workflow_pools.py 的 I1/O1 同一类泄漏面, 已实测复现并按同法
修 (计数/属性值先落局部变量再断言标量). `all(genexpr)`/`sum(genexpr)` 已单独实测确认
安全 (pytest 只显示 generator object 的内存地址 repr, 不展开内容), 不需要改。

`cfg_path` fixture 另需 repr 层防护: 它是磁盘上真实 ConfigReport 的 Path, str/repr 里
带真实研究目录名 (如 study 代号) —— pytest 失败 traceback 默认会把它当函数实参打出来,
与 test_catalog_workflow_pools.py 的 `cat` fixture 是同一条独立泄漏面 (与断言改写无关,
任何一条断言红了都会触发), 已实测复现并用 `_RedactedPath.__repr__` 挡住 (只挡 repr,
不改 str/__fspath__, openpyxl 仍能正常打开文件)。"""
from pathlib import Path

import pytest

from scripts.study.parse_config_report import (
    parse_activities,
    parse_events,
    parse_form_assignments,
)
from scripts.study.paths import resolve_study


class _RedactedPath(Path):
    """Path 子类, 只改 __repr__: 路径本身 (str/__fspath__) 逐字不变, 只是 pytest 失败
    traceback 默认打印的函数实参 repr 不再吐出真实文件路径 (含真实研究代号)。"""

    def __repr__(self):
        return "<config_report_new path: redacted (real study path)>"


@pytest.fixture(scope="module")
def cfg_path():
    return _RedactedPath(resolve_study("st01").config_report_new)


def test_parse_events_counts(cfg_path):
    evs = parse_events(cfg_path)
    n_evs = len(evs)
    assert n_evs == 17                                      # 含脚注
    real = [e for e in evs if not e.is_trailer]
    n_real = len(real)
    assert n_real == 14
    assert all(e.oid and " " not in e.oid for e in real)


def test_parse_events_type_distribution(cfg_path):
    real = [e for e in parse_events(cfg_path) if not e.is_trailer]
    kinds = {}
    for e in real:
        kinds[e.event_type] = kinds.get(e.event_type, 0) + 1
    assert sorted(kinds.values()) == [1, 13]                # 13 + 1, 不写死日文取值


def test_parse_activities_counts(cfg_path):
    acs = parse_activities(cfg_path)
    n_acs = len(acs)
    assert n_acs == 80
    real = [a for a in acs if not a.is_trailer]
    n_real = len(real)
    assert n_real == 77
    assert all(a.oid and a.event_oid for a in real)


def test_parse_form_assignments_counts(cfg_path):
    fms = parse_form_assignments(cfg_path)
    n_fms = len(fms)
    assert n_fms == 112
    real = [f for f in fms if not f.is_trailer]
    n_real = len(real)
    assert n_real == 110
    n_form_oids = len({f.form_oid for f in real})
    assert n_form_oids == 21


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
    """row 必须是可溯源物理行号 (Events 数据自第 4 行起).

    `evs[0].row` 若直接写进 assert, 失败时 pytest 会把 evs[0] 整个 EventDef (真实
    oid/name/event_type) 打出来 (已实测复现, 与 len() 同一类问题) —— 属性值先落局部
    变量再断言标量.
    """
    evs = parse_events(cfg_path)
    row_first = evs[0].row
    row_last = evs[-1].row
    assert row_first == 4
    assert row_last == 22
