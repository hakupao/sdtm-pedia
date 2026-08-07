"""q38 gold 完整性: 题干两问需要两个不可互相替代的源。

背景: 原 gold 只有 chapters/ch02, 而字面回答"two-character 规则"的是
ch04 §4.2.2 (dense 检索 #1)。原判据把一次正确检索判成 0.0 (假失分)。
"""
import yaml

from eval.run_eval import check_source_recall

TEST_SET = "eval/test_set_v3.yml"


def _q38():
    for q in yaml.safe_load(open(TEST_SET)):
        if q["id"] == "q38":
            return q
    raise AssertionError("q38 not found in " + TEST_SET)


def test_q38_gold_requires_both_sources():
    q = _q38()
    assert q.get("expected_sources_any") is None, "两问都要, 必须 AND 而非 OR"
    assert q["expected_sources"] == [
        "chapters/ch02",
        "chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$",
    ]


def test_q38_gold_ch04_section_needs_exact_section_match():
    """§4.2.2 用 `$` 精确匹配: 不带 $ 时 '4.2.2 Two-character Domain Identifier'
    是子串语义, 而 ch04 里不存在更长的兄弟 section —— 但标识符+子串是通用隐患,
    统一按精确写。这条测试锁住"召回了 4.2 或 4.2.3 不算命中"。"""
    q = _q38()
    gold = q["expected_sources"]
    srcs = ["knowledge_base/chapters/ch04_general_assumptions.md"]

    recall, _, _ = check_source_recall(
        srcs, gold, retrieved_sections=["4.2.3 Use of \"Subject\" and USUBJID"]
    )
    assert recall == 0.0, "邻节不得冒名命中"

    recall, hits, _ = check_source_recall(
        srcs + ["knowledge_base/chapters/ch02_fundamentals.md"],
        gold,
        retrieved_sections=["4.2.2 Two-character Domain Identifier", "whole_file"],
    )
    assert recall == 1.0, hits
