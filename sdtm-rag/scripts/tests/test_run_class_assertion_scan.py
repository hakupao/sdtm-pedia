"""(b) 层驱动的取数闸。⚠ 本文件零真实 LLM 调用。

守一个静默降级: run 报告里 `answer` 是完整答案, `answer_preview` 只有 **600 字符**。
opus-5 那轮答案中位数 3187 字符、最长 8754 —— 拿 preview 去问裁判, 大部分归属断言
根本不在截断范围内, 裁判会大面积判"无断言 ⇒ consistent", 而**这种失败看起来和
全部通过一模一样** (retrospective 规则 6 成因 A)。

`check_code_grounding.py` 有 `r.get("answer", r.get("answer_preview"))` 这个回退,
(b) 层**绝不能照抄** —— 那里回退只影响找码, 这里回退会让整层判定失效。
"""
from __future__ import annotations

import pytest

from eval.prod_wirein.run_class_assertion_scan import entries_from_report


def test_entries_use_the_full_answer():
    report = {"results": [{"id": "q01", "answer": "A" * 5000,
                           "answer_preview": "A" * 600}]}

    entries = entries_from_report(report)

    assert entries == [{"id": "q01", "answer": "A" * 5000}]


def test_missing_full_answer_is_fatal_not_silently_downgraded_to_preview():
    """⛔ 分辨力: 若实现写成 `r.get("answer", r.get("answer_preview"))`, 这条会红。"""
    report = {"results": [{"id": "q01", "answer_preview": "A" * 600}]}

    with pytest.raises(ValueError) as exc:
        entries_from_report(report)

    assert "q01" in str(exc.value)
    assert "--full-answers" in str(exc.value)


def test_empty_answer_is_also_fatal():
    """空字符串是"生成失败"的形状, 不是"没有归属断言" —— 混为一谈会把失败记成 PASS。"""
    report = {"results": [{"id": "q01", "answer": ""}]}

    with pytest.raises(ValueError):
        entries_from_report(report)


def test_blind_order_hides_which_items_the_judge_flagged():
    """⛔ `pick_sample` 返回的是 `clean 段 + flagged 段` ⇒ **后 3 条恒是裁判报警的**。
    顺序本身就是 verdict, 而预登记写死"人判 ⛔ 不看裁判的 verdict"。

    既有的 `test_packet_shows_answer_and_quote_but_not_the_verdict` 只查了字面词,
    查不到这条泄漏通道 —— 那条闸把自己的能力说大了。

    分辨力: 若实现直接 `return sample` 不打乱, 这条会红。
    """
    from eval.prod_wirein.run_class_assertion_scan import blind_order

    sample = ([{"id": f"clean{i}"} for i in range(5)]
              + [{"id": f"flag{i}"} for i in range(3)])

    out = blind_order(sample, seed=0)
    tail = {r["id"] for r in out[-3:]}

    assert tail != {"flag0", "flag1", "flag2"}, "报警项仍全在末三位 = 顺序仍泄漏 verdict"


def test_blind_order_loses_nothing():
    from eval.prod_wirein.run_class_assertion_scan import blind_order

    sample = [{"id": f"q{i}"} for i in range(8)]

    out = blind_order(sample, seed=0)

    assert sorted(r["id"] for r in out) == sorted(r["id"] for r in sample)


def test_blind_order_is_deterministic_for_a_given_seed():
    """人判包要可复现 —— 同 seed 重跑必须给同一份包。"""
    from eval.prod_wirein.run_class_assertion_scan import blind_order

    sample = [{"id": f"q{i}"} for i in range(8)]

    assert blind_order(sample, seed=0) == blind_order(sample, seed=0)
