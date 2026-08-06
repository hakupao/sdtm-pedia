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


def test_empty_section_fails_loud():
    """`path#` (井号后为空) 必须响亮报错, 不许静默退化成路径匹配。

    根因: `sec = ""` 时 `"" in (s or "")` 恒 True, 该 gold 不但退化为路径匹配, 还绕过了
    "section 为 None 的条目永不命中 section 级 gold" 这条承诺 —— 比纯路径写法更松。
    改写 gold 时手滑打空一个 section, 会静默把该题退回无判别力口径, 且偏差单向朝上、
    任何闸都拦不住 (与 load_test_set 拦拼错 gold 键同一类防御)。
    """
    with pytest.raises(ValueError, match="empty section"):
        check_source_recall(SOURCES, ["chapters/ch04.md#"], retrieved_sections=SECTIONS)


def test_whitespace_only_section_fails_loud():
    with pytest.raises(ValueError, match="empty section"):
        check_source_recall(SOURCES, ["chapters/ch04.md#   "],
                            retrieved_sections=SECTIONS)


def test_empty_section_in_any_of_fails_loud():
    # OR 组同样过 _matches, 漏了这里等于留个后门
    with pytest.raises(ValueError, match="empty section"):
        check_source_recall(SOURCES, [], any_of=["chapters/ch04.md#"],
                            retrieved_sections=SECTIONS)


def test_empty_section_fails_loud_before_missing_sections_check():
    # 空 section 是 gold 写法错误, 与调用方给没给 retrieved_sections 无关 —— 两种畸形
    # 同时出现时也必须报空 section, 否则修完调用方才发现 gold 还是坏的
    with pytest.raises(ValueError, match="empty section"):
        check_source_recall(SOURCES, ["chapters/ch04.md#"])


def test_exact_section_marker_matches_only_whole_section():
    """`路径#节$` = 精确匹配整个 section, 不接受前缀。

    动机 (实测): section 判据是子串语义, 而 VARIABLE_INDEX 有 6 组 section 互为子串
    (`§一 通用变量: ARM` ⊂ `…ARMCD`, `…VISIT` ⊂ `…VISITNUM` 等)。q107 要 ARM 和 ARMCD
    两节但只召回了 ARMCD, 子串语义下 ARM 会被 ARMCD 的 chunk 冒名命中, 该题照样满分 ——
    正是 section 化要消灭的那种假命中。子串匹配对"标识符类 gold"是一类通用隐患, 但各库要各自
    验证: study 侧同形态的 gold 因带 `.md` 后缀实际有判别力, 照搬结论会误判。
    """
    sources = ["VARIABLE_INDEX.md", "VARIABLE_INDEX.md"]
    sections = ["§一 通用变量: ARMCD", "§一 通用变量: EPOCH"]

    # 子串语义: ARM 被 ARMCD 冒名命中 (旧行为, 保留给非碰撞场景)
    recall, _, _ = check_source_recall(
        sources, ["VARIABLE_INDEX.md#§一 通用变量: ARM"], retrieved_sections=sections)
    assert recall == 1.0

    # 精确语义: ARM 未被召回 -> miss
    recall, _, misses = check_source_recall(
        sources, ["VARIABLE_INDEX.md#§一 通用变量: ARM$"], retrieved_sections=sections)
    assert recall == 0.0 and misses == ["VARIABLE_INDEX.md#§一 通用变量: ARM$"]

    # 精确语义: ARMCD 确实被召回 -> hit
    recall, hits, _ = check_source_recall(
        sources, ["VARIABLE_INDEX.md#§一 通用变量: ARMCD$"], retrieved_sections=sections)
    assert recall == 1.0 and hits == ["VARIABLE_INDEX.md#§一 通用变量: ARMCD$"]


def test_exact_section_marker_never_matches_none_section():
    recall, _, _ = check_source_recall(
        SOURCES, ["domains/AE/spec.md#anything$"], retrieved_sections=SECTIONS)
    assert recall == 0.0


def test_exact_marker_with_empty_section_fails_loud():
    # `path#$` 是空 section 的另一种写法, 同样必须响亮报错
    with pytest.raises(ValueError, match="empty section"):
        check_source_recall(SOURCES, ["chapters/ch04.md#$"],
                            retrieved_sections=SECTIONS)


def test_any_of_group_supports_section_syntax():
    recall, hits, _ = check_source_recall(
        SOURCES, [], any_of=["nope.md", "chapters/ch04.md#4.1"],
        retrieved_sections=SECTIONS)
    assert recall == 1.0 and "chapters/ch04.md#4.1" in hits


def test_length_mismatch_fails_loud():
    with pytest.raises(ValueError):
        check_source_recall(SOURCES, ["chapters/ch04.md#4.1"],
                            retrieved_sections=["only-one"])
