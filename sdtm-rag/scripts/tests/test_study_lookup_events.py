"""事件通道: OID 与名称双向命中. 零真名: 全部伪值."""
from server.study_lookup import StudyLookup

CAT = {
    "study": "st01",
    "items": [{"form_oid": "偽F", "item_oid": "偽IT_A", "label": "偽ラベル甲",
               "raw": {}}],
    "events": [{"oid": "偽EV1", "name": "偽イベント名甲", "event_type": "偽型",
                "description": "", "visibility_condition": "",
                "sched_reference": "", "sched_minus_days": "", "sched_plus_days": ""}],
    "activities": [{"oid": "偽AC1", "event_oid": "偽EV1", "name": "偽活動名乙",
                    "event_name": "偽イベント名甲", "description": "",
                    "visibility_condition": ""}],
    "assignments": [{"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F",
                     "event_name": "偽イベント名甲", "activity_name": "偽活動名乙",
                     "repeating": "0", "item_visibility": "", "hidden_items": ""}],
}


def test_resolve_events_by_oid():
    lk = StudyLookup(CAT)
    assert "event:偽EV1" in lk.resolve_events("偽EV1 について教えて")


def test_resolve_events_by_name():
    lk = StudyLookup(CAT)
    assert "event:偽EV1" in lk.resolve_events("偽イベント名甲 はいつ実施しますか")


def test_resolve_activity_by_name():
    lk = StudyLookup(CAT)
    assert "activity:偽EV1/偽AC1" in lk.resolve_events("偽活動名乙 のタイミングは")


def test_resolve_events_empty_on_no_hit():
    lk = StudyLookup(CAT)
    assert lk.resolve_events("まったく無関係な質問") == []


def test_resolve_events_missing_pools_degrades_quietly():
    """老 catalog (无三池) 不许炸 —— 三池是新增, 旧数据要能跑."""
    lk = StudyLookup({"study": "st01", "items": CAT["items"]})
    assert lk.resolve_events("偽EV1") == []


# ── item 采集范围 (类型6/item_collection_scope): collect_scope() 减法接线 ──────
# spec §2.3 的推导 (Task 4 `collect_scope`) 经 resolve_events 接通查询, 而不是只
# 停留在渲染器里 (Task 4 review M4/M5)。索引对象是 item_oid (子串命中, 与事件/
# 活动索引同精神), 命中后现算 collect_scope 减法, 换算成 assignment 目标。

def test_resolve_events_item_scope_via_collect_scope():
    """item_oid 命中 -> collect_scope 减法 -> 只有未被隐藏的 assignment 目标入选."""
    cat = {
        "study": "st01",
        "items": [{"form_oid": "偽F", "item_oid": "偽IT_X", "label": "偽ラベル乙",
                   "raw": {"Visibility::Hidden in activity": "偽AC2"}}],
        "events": [{"oid": "偽EV1", "name": "偽イベント名甲"},
                   {"oid": "偽EV2", "name": "偽イベント名乙"}],
        "activities": [],
        "assignments": [
            {"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F"},
            {"event_oid": "偽EV2", "activity_oid": "偽AC2", "form_oid": "偽F"},
        ],
    }
    lk = StudyLookup(cat)
    got = lk.resolve_events("偽IT_X はどこで採取されますか")
    assert "assignment:偽EV1/偽AC1/偽F" in got
    assert "assignment:偽EV2/偽AC2/偽F" not in got   # 隐藏于 偽AC2, 减法排除


def test_resolve_events_item_scope_empty_when_form_has_no_assignments():
    """M4 (task-4-review.md): form 在 assignments 池里零分配時, 不臆造任何目标
    —— 静默空集, 与"没查到"外部不可区分是已知限制 (见 checkpoint), 但不得报错
    或返回假目标。"""
    cat = {
        "study": "st01",
        "items": [{"form_oid": "偽孤立F", "item_oid": "偽IT_Y", "label": "偽ラベル丙",
                   "raw": {}}],
        "events": [], "activities": [],
        "assignments": [{"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F"}],
    }
    lk = StudyLookup(cat)
    assert lk.resolve_events("偽IT_Y") == []
