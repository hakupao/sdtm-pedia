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


def test_resolve_events_does_not_match_on_event_or_activity_names():
    """事件/活动**名称**子串匹配 (旧 Tier 3) 已于 2026-08-26 整层移除。

    ⚠ **这是一次能力删除, 不是重构** —— 本测试原先是两条断言"名称能查到"的正面
    测试 (`test_resolve_events_by_name` / `test_resolve_activity_by_name`), 现在
    断言的是**反面**: 名称查不到了。

    判据 (证据 evidence/checkpoints/study_c3_precision_tradeoff.md §7): Tier 1b 收紧
    之后, 全通道剩余 23 条假阳性里 **19 条 (83%) 来自这一层**; 层内 tp 5 / fp 19。
    机制: 事件与活动的可读名是自然语言短语, 日文没有可用的词边界, 这层不做边界
    判定 —— 只要问题里出现该短语, 哪怕说的是别的意思也会被召回。
    移除后: 命中 20/33 → 15/33, precision **54.00% → 84.62%**, 返回 50 → 26。
    """
    lk = StudyLookup(CAT)
    assert lk.resolve_events("偽イベント名甲 はいつ実施しますか") == []
    assert lk.resolve_events("偽活動名乙 のタイミングは") == []


def test_resolve_events_empty_on_no_hit():
    lk = StudyLookup(CAT)
    assert lk.resolve_events("まったく無関係な質問") == []


def test_resolve_events_missing_pools_degrades_quietly():
    """老 catalog (无 events/activities/assignments 三池) 不许炸 —— 三池是新增, 旧数据
    要能跑。⚠ 本用例的 query 不含 CAT 里那个 item 的 OID, item 段整段不会被执行——只
    证明了事件/活动索引那一半会降级 (2026-08-26 复审 Minor-1 指出的范围澄清, 另见
    `test_resolve_events_item_scope_missing_raw_degrades_quietly` 补上 item 段那一半)。
    """
    lk = StudyLookup({"study": "st01", "items": CAT["items"]})
    assert lk.resolve_events("偽EV1") == []


def test_resolve_events_item_scope_missing_raw_degrades_quietly():
    """item 段那一半的降级验证 (Minor-1 的对称覆盖): item 缺 raw 键、query 确实命中该
    item OID 时, `collect_scope` (已修复用 `item.get("raw") or {}`) 视同无隐藏清单,
    不炸, 正常产出该 item 所属 form 的全部采集点。"""
    cat = {
        "study": "st01",
        "items": [{"form_oid": "偽F", "item_oid": "偽IT_Z", "label": "偽ラベル丁"}],  # 无 raw
        "events": [], "activities": [],
        "assignments": [{"event_oid": "偽EV9", "activity_oid": "偽AC9", "form_oid": "偽F"}],
    }
    lk = StudyLookup(cat)
    assert lk.resolve_events("偽IT_Z について") == ["assignment:偽EV9/偽AC9/偽F"]


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


# ── Ruling P2 (团队 lead 复审, 2026-08-26 修复轮1): form_oid -> 该 form 的全部
# assignment 原始清单 (未做 item 级减法)。修 event_form_assignment/repeating_rule
# 两类问法结构性 0 命中——这两类问法的 gold 是表单级事实, 题面常直接点名 form OID,
# 但旧实现只索引 event/activity OID, 对 form OID 视而不见。

def test_resolve_events_form_oid_lists_assignments_without_subtraction():
    """form OID 命中 -> 该 form 的 assignment 原始清单 (**不做 item 级减法**, 与 item
    采集范围索引是两个不同判据)。

    ⚠ **契约变更 (C3, 2026-08-26)**: 本测试原先用一个 2 条 assignment 的 form 断言
    "两条都在", 那条断言在 `_MAX_ASSIGNMENTS_PER_FORM = 1` 之后**不再成立** —— 清单
    超过上限的 form 现在整个不 fire (判据见常量处; 由
    `test_resolve_events_skips_form_whose_assignment_list_is_not_discriminative` 看守)。
    这里改用 1 条 assignment 的 form 演示同一个意图: 该 item 在这个活动里是**隐藏**的,
    Tier 2 会把它减掉, 而 Tier 1b 不减 —— 只要题面没点名 item OID, 原始清单照出。
    """
    cat = {
        "study": "st01",
        "items": [{"form_oid": "偽F", "item_oid": "偽IT_A", "label": "偽ラベル甲",
                   "raw": {"Visibility::Hidden in activity": "偽AC1"}}],
        "events": [], "activities": [],
        "assignments": [
            {"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F"},
        ],
    }
    lk = StudyLookup(cat)
    got = lk.resolve_events("偽Fフォームは繰り返し記録できますか")
    # 偽IT_A 在 偽AC1 里是隐藏的; 题面没点名它, 故 Tier 2 不 fire, Tier 1b 原样列出
    assert got == ["assignment:偽EV1/偽AC1/偽F"]


def test_resolve_events_form_raw_listing_yields_to_item_scope_same_form():
    """2026-08-26 复审后追加: 题面同时点名 form OID 与该 form 下某个具体 item OID
    时 (类型6常见形态), 该 form 的未减法原始清单要让位于 item 的减法结果——否则
    精确的减法答案会被同 form 的未减法条目稀释 (命中不丢, 但 precision 暴跌,
    实测复现见 checkpoint)。不相关的另一个 form 若同时被命中, 不受这条抑制影响。"""
    cat = {
        "study": "st01",
        "items": [{"form_oid": "偽F", "item_oid": "偽IT_X", "label": "偽ラベル乙",
                   "raw": {"Visibility::Hidden in activity": "偽AC2"}}],
        "events": [], "activities": [],
        "assignments": [
            {"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F"},
            {"event_oid": "偽EV2", "activity_oid": "偽AC2", "form_oid": "偽F"},
            {"event_oid": "偽EV3", "activity_oid": "偽AC3", "form_oid": "偽G"},
        ],
    }
    lk = StudyLookup(cat)
    got = lk.resolve_events("偽IT_X は偽Fフォームのどの活動で採取されますか")
    assert "assignment:偽EV1/偽AC1/偽F" in got     # Tier 2: item 減法保留的那条
    assert "assignment:偽EV2/偽AC2/偽F" not in got  # 偽F 的原始清单让位, 隐藏项不该露出


def test_bounded_contains_does_not_merge_across_whitespace():
    """有界匹配防被空格隔开的短 OID 与后随数字人为拼接误判边界 (2026-08-26 复审
    实测案例的最小复现): item OID 后紧跟空格加数字, 不该被误判为紧邻数字从而在
    _norm 去空白版本上产生假边界。"""
    cat = {
        "study": "st01",
        "items": [{"form_oid": "偽F", "item_oid": "偽XY", "label": "偽ラベル",
                   "raw": {}}],
        "events": [], "activities": [],
        "assignments": [{"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F"}],
    }
    lk = StudyLookup(cat)
    # "偽XY" 后面紧跟半角空格再接数字 "1" —— 保留空白版本里两侧都是非字母数字下划线
    # (空格 / 字符串起止), 边界应当成立, 命中正常触发。
    assert lk.resolve_events("偽XY 1回目の状況は") != []


def test_resolve_events_exact_oid_survives_when_a_later_tier_floods_the_cap():
    """精确命中 (Tier 1a) 必须留在结果里, 即便靠后的层单独就产出超过总 cap 的目标。

    ⚠ **本测试于 2026-08-26 换过洪水来源**: 原版
    (`..._not_squeezed_by_name_substring`) 用 61 个同名 event/activity 制造 Tier 3
    洪水, 而 Tier 3 已整层移除 —— 那个场景**再也构造不出来**, 原断言会恒真通过,
    即沦为装饰闸。现改用**能构造出来**的洪水源: 一个 item 的 `collect_scope` 覆盖
    60 个活动 → Tier 2 单层即产出 60 个目标, 远超 `_MAX_EVENTS_TOTAL`。

    这条守的是**拼接顺序**这个不变量 (Tier 1a 必须排在前面), 不是某一层的存在性;
    有人把 `out` 的拼接顺序改掉时它会红 (已变异实测)。
    """
    n = 60
    cat = {
        "study": "st01",
        "items": [{"form_oid": "偽F", "item_oid": "偽IT_A", "label": "偽ラベル甲",
                   "raw": {}}],
        "events": [{"oid": "偽EVX", "name": "偽イベントX"}],
        "activities": [{"oid": f"偽AC{i}", "event_oid": "偽EVX", "name": f"偽活動{i}"}
                       for i in range(n)],
        "assignments": [{"event_oid": "偽EVX", "activity_oid": f"偽AC{i}",
                         "form_oid": "偽F"} for i in range(n)],
    }
    lk = StudyLookup(cat)
    got = lk.resolve_events("偽EVX の 偽IT_A はどこで採取されますか")

    assert len(got) == 50                 # 总 cap 确实生效 (60 个 Tier 2 目标被截断)
    assert got[0] == "event:偽EVX"        # 精确命中排在最前, 没被后面的层冲掉


def test_resolve_events_skips_form_whose_assignment_list_is_not_discriminative():
    """Tier 1b 只在该 form 的 assignment 清单**足够短**时才 fire。

    判据来源 (C3 精度取舍单元, 2026-08-26 实测, 证据 evidence/checkpoints/study_c3_precision_tradeoff.md):
    Tier 1b 一层贡献 33 题里 220/259 条返回、214/231 条噪声, 层内 precision **2.7%**;
    噪声全部来自 4 个长清单 form (清单长度分布 {1:13, 2:3, 4:1, 14:1, 15:1, 18:1, 40:1})。
    收紧后 precision **10.81% → 54.00%**, 返回 259 → 50, 代价是 33 题里丢 1 题。

    与既有 `_MAX_CARDS_PER_MATCH` 同精神: **匹配集合太大 = 不具判别力, 整个跳过**。
    """
    cat = {
        "study": "st01",
        "items": [], "events": [], "activities": [],
        "assignments": [
            # 偽SHORT: 1 条 => 具判别力, 应 fire
            {"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽SHORT"},
            # 偽LONG: 2 条 (超过上限) => 不具判别力, 整个跳过
            {"event_oid": "偽EV2", "activity_oid": "偽AC2", "form_oid": "偽LONG"},
            {"event_oid": "偽EV3", "activity_oid": "偽AC3", "form_oid": "偽LONG"},
        ],
    }
    lk = StudyLookup(cat)

    assert lk.resolve_events("偽SHORT はどこに割り付けられていますか") == [
        "assignment:偽EV1/偽AC1/偽SHORT"
    ]
    assert lk.resolve_events("偽LONG はどこに割り付けられていますか") == []
