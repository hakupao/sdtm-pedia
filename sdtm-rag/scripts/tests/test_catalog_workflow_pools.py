"""catalog 三池 + spec §5.A/B/C 三闸. 零真名: 只断言计数/差集长度等标量,不直接比较
原始集合/列表/字典 —— 后者失败时会被 pytest assertion rewriting 把真实内容打进 stdout
(控制方 I1, 已实测复现; §5.C 转置结构与 §5.A event_type 分布同类风险一并排查修正).

`cat` fixture 另需要 repr 层防护 (与断言改写是两条独立机制): pytest 默认 (--tb=long)
的失败 traceback 会在每个失败用例最上方打印 "cat = <fixture repr>" —— 这与具体哪条
assert 无关, 任何一条断言红了都会触发, 已实测复现 (整个真实 catalog dict, 含真实
form OID / 真实日文 label 逐字打出). 断言层的改写只挡住了"比较双方"这一处, repr 层
的默认参数打印是另一处独立泄漏面, 必须靠 `_RedactedCatalog.__repr__` 挡, 单靠标量化
断言挡不住。"""
import collections

import pytest

from scripts.study.build_catalog import build_catalog
from scripts.study.paths import resolve_study


class _RedactedCatalog(dict):
    """dict 包一层, 只改 __repr__/__str__: 内容 (含真实 OID/label) 逐字不变, 只是
    pytest 失败 traceback 默认打印的函数实参 repr 不再吐出整个 catalog。

    生效范围 (已实测钉死, 控制方 O3):
    - 只对 `--tb=long` / `--tb=auto`(pytest 默认, 本仓未显式设置 `--tb`)生效;
      `--tb=short` 根本不打印函数实参这一行, 不需要这层防护(但断言本身仍要标量化,
      两者是独立机制)。
    - `-q`(本仓 `addopts = "-ra -q"` 就是这个)**不会**抑制这层防护要挡的那一行 ——
      已实测复现: `-q` 下失败详情段仍会打印 `cat = <fixture repr>`。
    - `--junitxml` 落盘的是同一份 longrepr 字符串, 所以这层防护对终端输出和 junit
      文件同时生效, 不需要分别处理。

    **不要做的事** (下一个人若碰这几条会绕过防护, 而且不会意识到):
    1. 不要把 `cat` 整体拿去和字面量 dict 比较(如 `assert cat == {...}`) —— dict 相等
       比较走 pytest 的 `assertrepr_compare` 结构化 diff, **绕开 `__repr__`**, 会把双方
       内容原样展开(已用哨兵字符串实测复现: "Differing items" / "Full diff" 段直接打出
       真实值, 与 `__repr__` 无关)。当前文件没有这种写法, 但这是最容易踩的坑。
    2. 不要把 `cat[...]` 的子对象(`cat["events"]` 等, 都是裸 list/dict, 没有包这层)
       当函数实参传给别的测试函数或 helper —— 包装只在 `cat` 这一层, 子对象逐一取出
       后就是原始真实数据, 传给任何会被 traceback 打印实参的函数都会泄漏。
    3. `--showlocals` / `-l` 下本防护**完全失效**, 且不是本防护范围能解决的: 本文件里
       `ev_ids`/`ac_ids`/`form_ids`/`fwd`/`bwd`/`mismatched`/`used` 等局部变量本身就是
       真实 OID 的裸 set/dict, `-l` 会把这些原样打出来(已实测复现)。本仓当前不跑
       `-l`, 但这是显式的已知限制, 不是"以为挡住了其实没挡住"。"""

    def __repr__(self):
        return f"<catalog: {len(self)} top-level keys, content redacted (real st01 data)>"

    __str__ = __repr__


@pytest.fixture(scope="module")
def cat():
    return _RedactedCatalog(build_catalog(resolve_study("st01")))


def test_three_pools_exist_with_expected_sizes(cat):
    # len() 的结果先落局部变量再断言标量: `assert len(cat["events"]) == 14` 若失败,
    # pytest assertion rewriting 会在 "+ where" 里把 cat["events"] 整个 list[dict]
    # (含真实 label/description) 打出来 —— 已实测复现 (控制方 I1 同类问题, 扩大排查发现).
    n_events = len(cat["events"])
    n_activities = len(cat["activities"])
    n_assignments = len(cat["assignments"])
    assert n_events == 14
    assert n_activities == 77
    assert n_assignments == 110


def test_gate_a_cross_check_against_design_summary(cat):
    """spec §5.A: 四条数字必须与 ConfigReport 设计摘要吻合 (已由 PDF 封面独立确认)."""
    asg = cat["assignments"]
    n_assignments = len(asg)
    n_form_oids = len({a["form_oid"] for a in asg})
    assert n_assignments == 110
    assert n_form_oids == 21
    by_type = {e["oid"]: e["event_type"] for e in cat["events"]}
    # .get() 而非 [] 索引: 引用不到时不抛 KeyError('真名')。但这有副作用 (控制方 N1
    # 实测复现): 若 events 池丢的恰好是分布 [1, 109] 里那个"独占型" (只挂 1 条
    # assignment) event, .get() 返回 None, counts 变成 {109型: 109, None: 1},
    # sorted(values) 仍是 [1, 109] —— 下面的分布判据**挡不住**这种破坏, 必须单独
    # 断言"引用得到"这件事本身 (n_unresolved, 只是个数, 不含真实 event_oid)。
    n_unresolved = sum(1 for a in asg if a["event_oid"] not in by_type)
    assert n_unresolved == 0
    counts = collections.Counter(by_type.get(a["event_oid"]) for a in asg)
    event_type_counts = sorted(counts.values())   # 值是计数 (int), 不含真实 event_type 字符串
    assert event_type_counts == [1, 109]


def test_gate_b_referential_integrity(cat):
    """spec §5.B: 四条引用完整性.

    差集先落局部变量, 断言只比较标量长度 —— 直接 `assert set_a <= set_b` 在失败时会被
    pytest assertion rewriting 把两个集合的真实内容 (真实 OID) 打进 stdout/报告
    (控制方 I1, 已实测复现), 而失败输出是最容易被复制粘贴带出红线的地方.
    """
    ev_ids = {e["oid"] for e in cat["events"]}
    ac_ids = {a["oid"] for a in cat["activities"]}
    form_ids = {f["oid"] for f in cat["forms"]}
    n_bad_activity_event = len({a["event_oid"] for a in cat["activities"]} - ev_ids)
    n_bad_assignment_event = len({a["event_oid"] for a in cat["assignments"]} - ev_ids)
    n_bad_assignment_activity = len({a["activity_oid"] for a in cat["assignments"]} - ac_ids)
    n_bad_assignment_form = len({a["form_oid"] for a in cat["assignments"]} - form_ids)
    assert n_bad_activity_event == 0
    assert n_bad_assignment_event == 0
    assert n_bad_assignment_activity == 0
    assert n_bad_assignment_form == 0


def test_activity_oid_globally_unique(cat):
    """spec §5.B 第 3 条的隐含前提: activity OID 全局唯一。

    gate B 的三条差集判据 (上面) 全部成立**不需要**这条前提也能通过——它们只检查
    "被引用的 OID 是否都在 activities 池里", 不检查 activities 池自身有没有重复键。
    Task 6 的 `resolve_events` 直接把 activity OID 当字典键用 (item/事件/活动索引都
    是 dict[oid -> targets]), 若真实数据里有重复 activity OID, 后一条会静默覆盖前一
    条, 不会报错——2026-08-26 复审指出这条前提此前无测试看守, 复算成立 (77/77 互异),
    但"成立"是当前数据的事实, 不是被测试钉死的契约, 换一版 ConfigReport 有重复时
    这里会先红, 而不是让 resolve_events 静默丢数据。"""
    ac_ids = [a["oid"] for a in cat["activities"]]
    n_total = len(ac_ids)
    n_unique = len(set(ac_ids))
    assert n_total == n_unique == 77


def test_gate_c_transpose_consistency(cat):
    """spec §5.C: assignments.hidden_items 与 items 的 Hidden in activity 互为精确转置.

    这是解析正确性的**独立参照物** —— 两处表示由 Viedoc 分别导出, 一致即互证。
    不一致 ⇒ spec §6 S2 触发, 停。

    差集/不一致项先落局部变量再断言标量长度, 理由同 test_gate_b_referential_integrity
    的 docstring(控制方 I1)。
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
    n_key_mismatch = len(set(fwd) ^ set(bwd))
    assert n_key_mismatch == 0, "两侧 activity 键集不同"
    n_fwd_keys = len(fwd)   # fwd 是 defaultdict(set), len() 若直接写进 assert 会连值一起打出
    assert n_fwd_keys == 61
    mismatched = [k for k in fwd if fwd[k] != bwd[k]]
    n_mismatched = len(mismatched)
    assert n_mismatched == 0


def test_gate_c_transpose_consistency_form_aware(cat):
    """spec §5.C 转置一致性的加强版, 按 (activity_oid, form_oid) 二元键做转置,
    而不是只按 activity_oid (上面 `test_gate_c_transpose_consistency` 的口径)。

    2026-08-26 复审指出: 上面那条闸按纯 activity_oid 分组会把"同一个 activity
    被分配给多个不同 form"的情形合并成一个键, 掩盖掉 form 级错配的可能——若解析
    时把某 item 的隐藏清单错记到了同一 activity 下的**另一个** form, 纯 activity
    键的闸看不出来 (两个 form 的隐藏集合被合并进同一个 activity 键, 只要合并后的
    并集两侧还一致, 闸就还是绿的)。真实数据复算: 77 个 activity 里有 15 个被分配
    给了不止一个 form, 按 (activity, form) 二元键分组后从 61 键涨到 **82 键**,
    82/82 逐键相同——数据本身没有缺陷, 但升级前的闸看不出"没有 form 级错配"这件
    事, 只是恰好没错。约 5 行成本, 补上闸, 不改变判定结论(仍是"一致", PASS)。
    """
    fwd = collections.defaultdict(set)
    for a in cat["assignments"]:
        if not a["hidden_items"].strip():
            continue
        for x in a["hidden_items"].replace("\n", ",").split(","):
            if x.strip():
                fwd[(a["activity_oid"], a["form_oid"])].add(x.strip())
    bwd = collections.defaultdict(set)
    for it in cat["items"]:
        raw = str(it["raw"].get("Visibility::Hidden in activity") or "")
        for x in raw.replace("\n", ",").split(","):
            if x.strip():
                bwd[(x.strip(), it["form_oid"])].add(it["item_oid"])
    n_key_mismatch = len(set(fwd) ^ set(bwd))
    assert n_key_mismatch == 0, "两侧 (activity, form) 键集不同"
    n_fwd_keys = len(fwd)
    assert n_fwd_keys == 82
    mismatched = [k for k in fwd if fwd[k] != bwd[k]]
    n_mismatched = len(mismatched)
    assert n_mismatched == 0


def test_hidden_activities_subset_of_activities(cat):
    """items 引用的 activity 必须全部在 activities 池里 (否则采集范围推导会静默丢)."""
    ac_ids = {a["oid"] for a in cat["activities"]}
    used = set()
    for it in cat["items"]:
        raw = str(it["raw"].get("Visibility::Hidden in activity") or "")
        for x in raw.replace("\n", ",").split(","):
            if x.strip():
                used.add(x.strip())
    n_used = len(used)
    assert n_used == 61
    n_extra = len(used - ac_ids)
    assert n_extra == 0


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
