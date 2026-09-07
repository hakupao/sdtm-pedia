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


def test_blind_order_permutation_differs_across_tags():
    """Rule D 审阅 (2026-09-07) 实测: 固定 seed + `pick_sample` 恒定形状 (clean×5 + flagged×3)
    ⇒ 置换恒定 ⇒ 四份人判包报警项位次全是 (3,7,8), 一次位次泄漏对后续所有包永久有效。
    置换必须随 tag 派生; 抽样 seed (预登记锁死) 不受影响。

    分辨力: 若实现只用 seed 不用 tag, 四个 tag 的输出全同, 这条会红。
    """
    from eval.prod_wirein.run_class_assertion_scan import blind_order

    sample = ([{"id": f"clean{i}"} for i in range(5)]
              + [{"id": f"flag{i}"} for i in range(3)])
    orders = {tag: tuple(r["id"] for r in blind_order(sample, seed=0, tag=tag))
              for tag in ("opus-5", "sonnet-5", "gpt-terra", "gpt-sol")}

    assert len(set(orders.values())) > 1, f"四个 tag 同一置换 = 位次泄漏跨包有效: {orders}"
    # 同 tag 仍可复现
    assert blind_order(sample, seed=0, tag="opus-5") == blind_order(sample, seed=0, tag="opus-5")


def test_scan_json_sample_ids_are_stored_in_blind_order(tmp_path, monkeypatch):
    """`sample_ids` 曾按 clean 段 + flagged 段落盘 ⇒ 打印它 = 打印 verdict (2026-09-06 实际泄漏)。
    落盘顺序必须与人判包一致 (blind), 让"随手打印"不再泄漏。

    分辩力: 若仍按 pick_sample 原序落盘, 末三位恒为裁判 flagged 的, 这条会红。
    """
    import json
    import sys
    import eval.prod_wirein.run_class_assertion_scan as mod

    report = {"results": [{"id": f"q{i:02d}", "answer": f"Answer {i} about AE."} for i in range(12)]}
    rp = tmp_path / "run_fake.json"
    rp.write_text(json.dumps(report))
    # 桩裁判: 前 9 条 consistent, 后 3 条 inconsistent ⇒ 抽样 5+3, 末三位 verdict 全 flagged
    def fake_scan(entries, judge, authority_md):
        return [{"id": e["id"], "has_assertion": True,
                 "verdict": "inconsistent" if i >= 9 else "consistent",
                 "quote": "", "authority": "", "parse_error": False, "error": None}
                for i, e in enumerate(entries)]
    monkeypatch.setattr(mod, "scan_answers", fake_scan)
    monkeypatch.setattr(mod, "load_class_authority", lambda: {"AE": "Events"})
    monkeypatch.setattr(sys, "argv", ["x", str(rp), "--dry-run", "--out-dir", str(tmp_path)])
    assert mod.main() == 0

    scan = json.loads((tmp_path / "class_scan_fake.json").read_text())
    verdict = {r["id"]: r["verdict"] for r in scan["rows"]}
    tail = [verdict[i] for i in scan["sample_ids"][-3:]]
    assert tail != ["inconsistent"] * 3, "sample_ids 末三位仍全是 flagged = 顺序仍泄漏 verdict"
    # 与人判包条目顺序一致
    import re
    packet = (tmp_path / "human_packet_fake.md").read_text()
    packet_order = re.findall(r"^### \d+\. `([^`]+)`", packet, re.M)
    assert packet_order == scan["sample_ids"]
