"""V-1 闸: (a) 层码接地检查必须在**模型当时看见的那个上下文**上判。

⚠ 本文件零 chroma / 零 LLM 调用 —— 测的是纯函数。

事故 (evidence/checkpoints/verified_spotcheck_2026-09.md):
`check_code_grounding.py::prod_engine()` 写死 `structured_lookup_enabled=True,
hybrid_enabled=True`, 而 2026-09-02 那轮 opus-5 生成时两者都关。于是它重建出来的 top-15
不是模型看见的那个 —— 实测**102 题里 0 题还原得上** (同口径重建则 102/102)。
后果: 8 条 "ungrounded" 全是假阳性, (a) 层判了个假 FAIL。

两道防线, 缺一不可:
1. **口径取自报告** (`retrieval_levers`), 不再写死;
2. **保真断言**: 重建的 top5 必须等于报告里落盘的 `top5_sources`, 不等就 fail-loud
   **不出数**。第 2 条才是真闸 —— 第 1 条只要报告缺字段就退回猜, 而猜错必须炸,
   不能默默算出一个看着像模像样的数。
"""
from __future__ import annotations

import pytest

from eval.prod_wirein.check_code_grounding import (
    FAKE_CODE,
    DegenerateContextError,
    ReconstructionMismatchError,
    assert_context_not_degenerate,
    check_fidelity,
    engine_kwargs_from_levers,
    levers_from_report,
)


def test_levers_come_from_the_report_when_recorded():
    """报告记了什么就用什么 —— 这是 V-1 的直接修法。"""
    report = {"summary": {"retrieval_levers": {
        "top_k": 15, "structured_lookup": False, "hybrid": False,
        "rerank": False, "query_expansion": "none",
    }}, "results": []}

    assert levers_from_report(report)["hybrid"] is False
    assert levers_from_report(report)["structured_lookup"] is False


def test_levers_are_honoured_even_when_they_are_on():
    """分辨力: 若实现退化成"永远返回默认 (全 OFF)", 这条会红。"""
    report = {"summary": {"retrieval_levers": {
        "top_k": 30, "structured_lookup": True, "hybrid": True,
        "rerank": True, "query_expansion": "hyde",
    }}, "results": []}

    levers = levers_from_report(report)

    assert levers["hybrid"] is True
    assert levers["top_k"] == 30
    assert levers["query_expansion"] == "hyde"


def test_old_reports_without_levers_fall_back_to_run_eval_defaults():
    """2026-09-02 那轮的报告没有这个字段。退回 run_eval 的**默认实参**(全 OFF),
    ⛔ 而不是退回旧的写死值 (lookup/hybrid=ON) —— 那正是 V-1 的成因。

    猜错不要紧: `check_fidelity` 会当场炸。但猜的方向必须是 run_eval 的默认。
    """
    levers = levers_from_report({"summary": {"verdict": "PASS"}, "results": []})

    assert levers["structured_lookup"] is False
    assert levers["hybrid"] is False
    assert levers["rerank"] is False
    assert levers["query_expansion"] == "none"


def test_engine_kwargs_do_not_reintroduce_the_hardcoded_on():
    """把 lever 翻成 RAGEngine kwargs 时不能再私自打开任何一个。"""
    kwargs = engine_kwargs_from_levers({
        "top_k": 15, "structured_lookup": False, "hybrid": False,
        "rerank": False, "query_expansion": "none",
    })

    assert kwargs["structured_lookup_enabled"] is False
    assert kwargs["hybrid_enabled"] is False
    assert kwargs["rerank_enabled"] is False
    assert kwargs["query_expansion"] == "none"
    assert kwargs["top_k"] == 15


def test_fidelity_passes_when_rebuilt_top5_matches_the_recorded_one():
    check_fidelity("q01", ["a.md", "b.md"], ["a.md", "b.md"])  # 不抛即通过


def test_fidelity_raises_when_rebuilt_top5_differs():
    """这是 V-1 会当场炸的那一刻 —— 2026-09-02 那轮 102 题会全部落在这里。"""
    with pytest.raises(ReconstructionMismatchError) as exc:
        check_fidelity("q35", ["a.md", "b.md"], ["c.md", "d.md"])

    assert "q35" in str(exc.value)


def test_fidelity_is_order_sensitive():
    """检索顺序是上下文构成的一部分 (format_context 按序拼) ⇒ 同一集合不同顺序
    也是"没还原"。分辨力: 若实现拿 set 比较, 这条会红。"""
    with pytest.raises(ReconstructionMismatchError):
        check_fidelity("q01", ["a.md", "b.md"], ["b.md", "a.md"])


def test_degenerate_context_is_rejected():
    """⛔ 另一条假 PASS 通道: 若 `format_context` 有 bug 把整库拼进上下文,
    每个码都会"grounded" ⇒ 判据给出假 PASS。

    保真闸拦不住这个 —— 它比的是 `retrieve()` 的输出, 而这条 bug 在 format_context。
    所以另设否定控制: 一个 KB 里不存在的码, 绝不该出现在任何重建上下文里。
    """
    with pytest.raises(DegenerateContextError) as exc:
        assert_context_not_degenerate("q01", f"...blah {FAKE_CODE} blah...")

    assert "q01" in str(exc.value)


def test_normal_context_passes_the_degeneracy_control():
    assert_context_not_degenerate("q01", "AETERM is the topic variable. C66742 applies.")


def test_old_reports_without_the_seat_lever_rebuild_with_it_off():
    """T4 fix 1: 保底席是 T4 才有的通道, T4 之前的报告不可能记它。

    `RAGEngine` 的构造默认是 True, 所以只要不显式关掉, 按老报告重建出来的引擎会**多**
    一条注入通道 ⇒ top5 与落盘的对不上 ⇒ check_fidelity 把整批老档案判成重建失败。
    缺键 = 那轮没有这条通道 = OFF。
    """
    kwargs = engine_kwargs_from_levers({
        "top_k": 15, "structured_lookup": True, "hybrid": True,
        "rerank": False, "query_expansion": "none",
    })

    assert kwargs["domain_definition_seat"] is False


def test_recorded_seat_lever_is_honoured():
    """记了就照记的还原 —— 与其他 lever 同一约定。"""
    kwargs = engine_kwargs_from_levers({
        "top_k": 15, "structured_lookup": True, "hybrid": True,
        "rerank": False, "query_expansion": "none",
        "domain_definition_seat": True,
    })

    assert kwargs["domain_definition_seat"] is True


def test_old_reports_without_the_expand_lever_rebuild_with_it_off():
    """T5 同理: 域码扩写是 T5 才有的通道, T5 之前的报告不可能记它。

    `settings.domain_expand_enabled` 默认 True, 所以只要不显式关掉, 按老报告重建出来的
    引擎会去扩写问句 ⇒ 稠密/BM25 查的不是当时那段文本 ⇒ top5 对不上, 整批老档案被判成
    重建失败。缺键 = 那轮没有这条通道 = OFF。
    """
    kwargs = engine_kwargs_from_levers({
        "top_k": 15, "structured_lookup": True, "hybrid": True,
        "rerank": False, "query_expansion": "none",
    })

    assert kwargs["domain_expander"] is None


def test_recorded_expand_lever_rebuilds_the_expander():
    """记了就照记的还原 —— 与其他 lever 同一约定。lever 是 bool, 引擎收的是对象。"""
    kwargs = engine_kwargs_from_levers({
        "top_k": 15, "structured_lookup": True, "hybrid": True,
        "rerank": False, "query_expansion": "none",
        "domain_expand": True,
    })

    assert kwargs["domain_expander"] is not None
    assert hasattr(kwargs["domain_expander"], "expand")
