"""Phase 0: check_source_recall 的 file#section 粒度判据 (spec §2 Phase 0).

动机: CDISC 侧存在 222-chunk 单文件, 纯路径子串判别力≈0 (study_golden_v1.md 血的教训:
"文件含答案"≠"被召回的 chunk 含答案")。
"""
import pytest

from eval.run_eval import check_source_recall

SOURCES = ["chapters/ch04.md", "chapters/ch04.md", "domains/AE/spec.md"]
SECTIONS = ["4.1 Timing", "4.2 Duration", None]


def test_plain_path_behavior_unchanged():
    recall, hits, misses = check_source_recall(SOURCES, ["domains/AE/spec.md"])
    assert recall == 1.0 and hits == ["domains/AE/spec.md"] and misses == []


def test_section_gold_hit_requires_same_entry():
    # 路径命中但 section 在另一条目上 → 不算命中
    recall, _, misses = check_source_recall(
        SOURCES, ["chapters/ch04.md#4.9"], retrieved_sections=SECTIONS)
    assert recall == 0.0 and misses == ["chapters/ch04.md#4.9"]


def test_section_gold_hit():
    recall, hits, _ = check_source_recall(
        SOURCES, ["chapters/ch04.md#4.2"], retrieved_sections=SECTIONS)
    assert recall == 1.0 and hits == ["chapters/ch04.md#4.2"]


def test_section_gold_none_section_never_matches():
    recall, _, _ = check_source_recall(
        SOURCES, ["domains/AE/spec.md#1"], retrieved_sections=SECTIONS)
    assert recall == 0.0


def test_section_gold_without_sections_fails_loud():
    # 判据要求 section 但调用方没给 → fail loud, 不静默降级为路径匹配
    with pytest.raises(ValueError, match="retrieved_sections"):
        check_source_recall(SOURCES, ["chapters/ch04.md#4.1"])


def test_any_of_group_supports_section_syntax():
    recall, hits, _ = check_source_recall(
        SOURCES, [], any_of=["nope.md", "chapters/ch04.md#4.1"],
        retrieved_sections=SECTIONS)
    assert recall == 1.0 and "chapters/ch04.md#4.1" in hits


def test_length_mismatch_fails_loud():
    with pytest.raises(ValueError):
        check_source_recall(SOURCES, ["chapters/ch04.md#4.1"],
                            retrieved_sections=["only-one"])
