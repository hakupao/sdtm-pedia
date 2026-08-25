"""collect_scope() 单测 — 移出 build_field_cards.py 后独立成模块 (Task 6, M5).

原住 test_build_field_cards.py; 挪到这里与 collect_scope.py 同名对应。零真名。
"""
from scripts.study.collect_scope import collect_scope


def test_collect_scope_subtracts_hidden():
    """采集范围 = form 被分配到的 activity - 该 item 被隐藏的 activity."""
    assignments = [
        {"form_oid": "偽F", "activity_oid": "偽A1"},
        {"form_oid": "偽F", "activity_oid": "偽A2"},
        {"form_oid": "偽F", "activity_oid": "偽A3"},
        {"form_oid": "偽G", "activity_oid": "偽A9"},   # 别的 form, 不算
    ]
    item = {"form_oid": "偽F",
            "raw": {"Visibility::Hidden in activity": "偽A2"}}
    assert collect_scope(item, assignments) == ["偽A1", "偽A3"]


def test_collect_scope_empty_hidden_keeps_all():
    assignments = [{"form_oid": "偽F", "activity_oid": "偽A1"},
                   {"form_oid": "偽F", "activity_oid": "偽A1"}]   # 重复 → 去重
    item = {"form_oid": "偽F", "raw": {}}
    assert collect_scope(item, assignments) == ["偽A1"]


def test_collect_scope_empty_when_form_has_no_assignments():
    """M4 (task-4-review.md): 该 item 所属 form 在 assignments 池里零分配時返回 [].

    真实数据 0 例 (231/231 有隐藏清单的 item 所属 form 均有至少一条分配), 故用合成
    fixture 补上这条此前"从未被执行过一次"的分支 —— assignments 里压根没有
    form_oid == 该 item 所属 form 的任何行 (不是"该 form 的分配全被隐藏", 是"该 form
    在 assignments 池里不存在", 与 test_collect_scope_empty_hidden_keeps_all 测的是
    不同诱因, 见 collect_scope docstring 的两种诱因说明)。
    """
    assignments = [{"form_oid": "偽別F", "activity_oid": "偽A9"}]   # 与 item 的 form 不同
    item = {"form_oid": "偽孤立F", "raw": {}}
    assert collect_scope(item, assignments) == []


def test_collect_scope_missing_raw_key_treated_as_no_hidden():
    """2026-08-26 复审 (规则 D 审查方 Minor-1): item 缺 raw 键时不许 KeyError, 视同无
    隐藏清单——生产 catalog 恒有 raw (asdict() 输出), 但 resolve_events 接线后本函数
    首次会被"任意手搭 fixture"调用到 (测试文件里已有不带 raw 的手搭 item), 审查方实测
    复现过 KeyError, 已修复 (`item.get("raw") or {}`)。"""
    assignments = [{"form_oid": "偽F", "activity_oid": "偽A1"}]
    item = {"form_oid": "偽F"}   # 无 raw 键
    assert collect_scope(item, assignments) == ["偽A1"]
