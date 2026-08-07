"""source_matches 是 check_source_recall 与扫描工具的唯一匹配实现。

硬规矩 1: 判据检查工具与判据必须逐字同语义。上一轮靠"照着再写一遍"来保证,
制造了 8 条假阳性。这里把同语义变成结构保证, 并用测试锁住"两者调用同一个函数"。
"""
import inspect

import pytest

from eval.run_eval import check_source_recall, source_matches


def test_path_only_gold_is_substring_match():
    assert source_matches("chapters/ch02", ["kb/chapters/ch02_fundamentals.md"])
    assert not source_matches("chapters/ch09", ["kb/chapters/ch02_fundamentals.md"])


def test_section_gold_requires_same_entry():
    srcs = ["kb/chapters/ch04.md", "kb/chapters/ch02.md"]
    secs = ["4.1 Other", "4.2.2 Two-character Domain Identifier"]
    # 路径命中的是 #0, 但 section 命中的是 #1 -> 不同条目, 不算命中
    assert not source_matches("chapters/ch04.md#4.2.2", srcs, secs)
    assert source_matches("chapters/ch02.md#4.2.2", srcs, secs)


def test_exact_section_marker():
    srcs = ["kb/VARIABLE_INDEX.md"]
    assert source_matches("VARIABLE_INDEX.md#§一 通用变量: ARM", srcs, ["§一 通用变量: ARMCD"])
    assert not source_matches("VARIABLE_INDEX.md#§一 通用变量: ARM$", srcs, ["§一 通用变量: ARMCD"])


def test_empty_section_raises():
    with pytest.raises(ValueError, match="empty section"):
        source_matches("chapters/ch04.md#", ["kb/chapters/ch04.md"], ["4.1"])


def test_section_gold_without_sections_raises():
    with pytest.raises(ValueError, match="retrieved_sections"):
        source_matches("chapters/ch04.md#4.2.2", ["kb/chapters/ch04.md"])


def test_none_section_never_matches_section_gold():
    assert not source_matches("chapters/ch04.md#4.2.2", ["kb/chapters/ch04.md"], [None])


def test_check_source_recall_delegates_to_source_matches():
    """结构锁: check_source_recall 不得自带第二份匹配实现。"""
    src = inspect.getsource(check_source_recall)
    assert "source_matches(" in src, "check_source_recall 必须调用 source_matches"
    assert "def _matches" not in src, "不得保留内部匹配闭包 (会与共享实现漂移)"
