"""切分逻辑全部用合成文本 —— 不碰真实 PDF, 不引入真名 (Global Constraint 8)。"""
import pytest

from scripts.study.split_sections import (
    assert_partition_complete,
    check_numbering,
    find_anchors,
    split_sections,
    subdivide_oversized,
)

# 合成 token 计数器: 1 字符 = 1 token, 让阈值在测试里可控且与真实分词器无关
def _chars(text: str) -> int:
    return len(text)

# 合成两页日文文档: 二层编号连续, 夹带一个会诱骗顶层匹配的正文数字
PAGES = [
    "治験実施計画書\n\n"
    "2.1 目的\n"
    "本試験の目的は安全性の評価である。\n"
    "対象は 608 例とする。\n"
    "2.2 対象\n"
    "選択基準を以下に示す。\n",
    "2.3 方法\n"
    "投与方法について記す。\n"
    "3.1 評価項目\n"
    "主要評価項目は奏効率とする。\n",
]


def test_anchors_only_pick_second_level_and_deeper():
    """顶层裸数字不作为锚点 —— 实测源文档里它会把正文数字 (608) 当成标题。"""
    nums = [a[2] for a in find_anchors(PAGES)]
    assert nums == ["2.1", "2.2", "2.3", "3.1"]
    assert "608" not in nums


def test_sections_carry_page_range():
    secs = split_sections(PAGES)
    assert [s.number for s in secs] == ["2.1", "2.2", "2.3", "3.1"]
    assert (secs[0].page_start, secs[0].page_end) == (1, 1)
    assert (secs[2].page_start, secs[2].page_end) == (2, 2)


def test_body_is_preserved_verbatim():
    """本轨唯一允许的有损是切分位置; 正文一个字都不许改 (Global Constraint 3)。"""
    body = split_sections(PAGES)[0].body
    assert "本試験の目的は安全性の評価である。" in body
    assert "対象は 608 例とする。" in body


def test_check_numbering_accepts_monotonic_sequence():
    assert check_numbering(split_sections(PAGES)) == []


def test_check_numbering_flags_backwards_child():
    bad = ["2.1 甲\n本文\n2.3 乙\n本文\n2.2 丙\n本文\n"]
    problems = check_numbering(split_sections(bad))
    assert problems and "2.2" in problems[0]


def test_check_numbering_flags_backwards_parent():
    bad = ["3.1 甲\n本文\n2.1 乙\n本文\n"]
    problems = check_numbering(split_sections(bad))
    assert problems and "2.1" in problems[0]


def test_partition_is_complete_and_non_overlapping():
    """把所有 section 拼回去必须逐字等于「首锚点及其之后」的全文。

    参照物是**原始页文本**, 不是切分器自己声称的任何数字 —— 护栏不许自洽
    (硬规矩 6)。切丢一段、切重一段、顺手 strip 掉一个空行, 这条都会红。
    """
    assert_partition_complete(PAGES, split_sections(PAGES))


def test_partition_assertion_actually_fires_when_a_section_is_dropped():
    """变异自检: 一道不会红的闸就是装饰 (硬规矩 18)。"""
    secs = split_sections(PAGES)
    with pytest.raises(AssertionError):
        assert_partition_complete(PAGES, secs[:-1])


def test_partition_assertion_fires_when_body_is_trimmed():
    secs = split_sections(PAGES)
    mutated = [secs[0].__class__(**{**secs[0].__dict__, "body": secs[0].body.strip()})] + secs[1:]
    with pytest.raises(AssertionError):
        assert_partition_complete(PAGES, mutated)


def test_no_anchors_yields_empty_and_does_not_crash():
    assert split_sections(["ただの本文。番号なし。\n"]) == []


def test_long_heading_line_is_not_an_anchor():
    """标题行短; 一行很长的正文即使以 n.m 开头也不是标题。"""
    long_line = "2.1 " + "あ" * 80
    assert find_anchors([long_line + "\n"]) == []


# ---- 回源裁定后新增的两条口径 (实测依据见 split_sections 模块 docstring 与
#      evidence/checkpoints/study_c1_doc_sections.md) ----

def test_body_sentence_starting_with_section_number_is_not_an_anchor():
    """正文里「6.4 項に…する。」这类以节号开头的引用句不是标题。

    实测: 那份 113 页文档第 8 章正文区里有 2 行这样的句子, 旧口径把它们当成
    标题 ⇒ 凭空冒出两个 6.4 节并触发编号闸 3 条违规。判别器是「含句末句点」,
    **不是长度** —— 实测真标题最长 53 字符, 比这两行 (45/40) 还长。
    """
    body = ["6.4 項に規定する手順に従う。\n"]
    assert find_anchors(body) == []
    assert split_sections(body) == []


def test_short_real_heading_without_period_still_anchors():
    """反向钉一次: 判别器只挡句子, 不挡真标题 (真标题不带 。)。"""
    assert [a[2] for a in find_anchors(["6.4 偽見出し甲\n"])] == ["6.4"]


def test_anchor_rule_is_shared_by_find_anchors_and_split_sections():
    """两个入口必须同口径 —— 若哪天只改一处, 真实文档上节数会与锚点数不等,
    而两把闸都查不出这种不一致 (完备性闸只看相邻锚点之间)。"""
    mixed = ["2.1 目的\n本文。\n6.4 項に定める。\n2.2 対象\n本文\n"]
    assert [a[2] for a in find_anchors(mixed)] == [s.number for s in split_sections(mixed)]


def test_check_numbering_accepts_deep_numbering_under_same_prefix():
    """四层编号: 6.2.3.1 的父是 6.2.3, 不是 6 —— 按 6 比会把 9 个真标题误报。"""
    pages = ["6.2 甲\n本文\n6.2.3.1 乙\n本文\n6.2.3.2 丙\n本文\n6.3 丁\n本文\n"]
    assert check_numbering(split_sections(pages)) == []


def test_subdivide_leaves_small_sections_untouched():
    secs = split_sections(PAGES)
    assert subdivide_oversized(PAGES, secs, 10_000, _chars) == secs
    assert all(s.part == 1 and s.parts_total == 1 for s in secs)


def test_subdivide_splits_oversized_section_verbatim_and_completely():
    """超限节切成多份后: 逐字拼回原节正文, 且完备性闸对整份列表仍成立。

    这一层挡的是**静默降级**: embedding 上限 8191 token, ingest 侧对超限文本
    截断后继续 —— 文本入库但向量只覆盖前半截, 而入库计数与两把闸全绿看不出来。
    """
    pages = ["2.1 目的\n" + "".join(f"行{i}あいうえお\n" for i in range(40))]
    secs = split_sections(pages)
    parts = subdivide_oversized(pages, secs, 120, _chars)
    assert len(parts) > 1
    assert "".join(p.body for p in parts) == secs[0].body          # 逐字
    assert all(_chars(p.body) <= 120 for p in parts)               # 真的没超限
    assert [p.part for p in parts] == list(range(1, len(parts) + 1))
    assert {p.parts_total for p in parts} == {len(parts)}
    assert_partition_complete(pages, parts)                        # 闸仍成立


def test_subdivide_prefers_blank_line_cut_points():
    """切点优先落在段落边界 (空行之后), 而不是句子中间。"""
    pages = ["2.1 目的\n" + "あ" * 50 + "\n\n" + "い" * 50 + "\n"]
    parts = subdivide_oversized(pages, split_sections(pages), 70, _chars)
    assert len(parts) == 2
    assert parts[0].body.endswith("\n\n")      # 在空行后切开
    assert parts[1].body.startswith("い")


def test_subdivide_recomputes_page_range_per_part():
    pages = ["2.1 目的\n" + "あ" * 40 + "\n", "い" * 40 + "\n", "う" * 40 + "\n"]
    parts = subdivide_oversized(pages, split_sections(pages), 60, _chars)
    assert (parts[0].page_start, parts[0].page_end) == (1, 1)
    assert (parts[-1].page_start, parts[-1].page_end) == (3, 3)
    assert all(p.page_start <= p.page_end for p in parts)


def test_subdivide_keeps_single_oversized_line_whole():
    """单行本身超限时不再细切 —— 保正文完整优先, 该情形记入已知限制。"""
    pages = ["2.1 目的\n" + "あ" * 300 + "\n"]
    parts = subdivide_oversized(pages, split_sections(pages), 100, _chars)
    assert "".join(p.body for p in parts) == split_sections(pages)[0].body
    assert any(_chars(p.body) > 100 for p in parts)


def test_check_numbering_ignores_continuation_parts():
    """续份复用同一编号 —— 若参与序列判定会被误报成「子号未递增」。"""
    pages = ["2.1 目的\n" + "".join(f"行{i}あいうえお\n" for i in range(40))]
    parts = subdivide_oversized(pages, split_sections(pages), 120, _chars)
    assert len(parts) > 1 and check_numbering(parts) == []


def test_check_numbering_still_flags_backwards_deep_child():
    """变异自检: 修口径不等于放宽 —— 同一父前缀下末段回退仍要红。"""
    pages = ["6.2.3.2 甲\n本文\n6.2.3.1 乙\n本文\n"]
    problems = check_numbering(split_sections(pages))
    assert problems and "6.2.3.1" in problems[0]


# ---- 全文覆盖闸 (L1 修复): 首锚点之前的区域必须被看见 ----

# 合成: 卷首 2 页 (无编号行) + 目录 1 页 (编号行 + 点线长行) + 正文 1 页
FRONT = "治験実施計画書\n実施医療機関一覧\n"
FRONT2 = "略語一覧\nAE 有害事象\n"
TOC = "".join(f"{i}.{j} 章題{'.' * 60} {i*10+j}\n"
              for i in range(2, 6) for j in range(1, 5))
BODY = "2.1 目的\n本試験の目的。\n"
FULL_PAGES = [FRONT, FRONT2, TOC, BODY]


def test_detect_toc_pages_by_shape_not_by_hardcoded_page_number():
    """目录页靠**形态**识别 (大量编号行 + 点线长行), 不靠硬编码页号 ——
    页号硬编码换一份 PDF 就会静默排除掉真实正文。"""
    from scripts.study.split_sections import detect_toc_pages

    assert detect_toc_pages(FULL_PAGES) == [3]          # 只有目录那页
    assert detect_toc_pages([FRONT, FRONT2, BODY]) == []  # 没有目录就不该乱排除


def test_full_coverage_gate_catches_content_before_first_anchor():
    """L1 的根因: `assert_partition_complete` 的口径是「首锚点行起」, 对首锚点
    **之前**的区域天然免疫 —— 那 66,200 字符 (全文 27.42%) 就是这么漏掉且闸全绿的。

    本闸改口径为「全文减去显式声明的排除区」, 故只切编号节时必须**红**。
    """
    from scripts.study.split_sections import assert_full_coverage

    sections = split_sections(FULL_PAGES)
    assert_partition_complete(FULL_PAGES, sections)      # 旧闸: 依然绿 (这正是问题)
    with pytest.raises(AssertionError, match="未覆盖"):
        assert_full_coverage(FULL_PAGES, sections, excluded_pages=[3])


def test_full_coverage_gate_passes_when_front_matter_is_covered():
    from scripts.study.split_sections import assert_full_coverage, split_front_matter

    sections = split_front_matter(FULL_PAGES, excluded_pages=[3]) + split_sections(FULL_PAGES)
    assert_full_coverage(FULL_PAGES, sections, excluded_pages=[3])


def test_split_front_matter_is_one_chunk_per_page_and_verbatim():
    """卷首没有编号行也没有可识别标题 (真实文档 p1-10 实测: 编号行 0 / 标题行 0),
    锚点切分器无处下手 ⇒ 按**页**切 (页本来就是抽取单位)。正文逐字。"""
    from scripts.study.split_sections import split_front_matter

    front = split_front_matter(FULL_PAGES, excluded_pages=[3])

    # 编号按**页号**编码 (front{页:02d}), 不是顺序号 —— 页号即出处, 换文档也自解释
    assert [s.number for s in front] == ["front01", "front02"]
    assert [s.body for s in front] == [FRONT, FRONT2]          # 逐字, 不 strip
    assert [(s.page_start, s.page_end) for s in front] == [(1, 1), (2, 2)]
    # 第 3 页是目录 (排除), 第 4 页整页都在首锚点之后 ⇒ 都不该出现在卷首里


def test_split_front_matter_covers_partial_page_before_the_anchor():
    """真实文档里首锚点落在 p17 页中 (该页前 578 字符属卷首侧, 其余属首节) ——
    卷首必须能切出**半页**, 否则那 578 字符会继续漏掉。"""
    from scripts.study.split_sections import split_front_matter

    pages = [FRONT, "前書き\n2.1 目的\n本文。\n"]
    front = split_front_matter(pages, excluded_pages=[])

    assert [s.number for s in front] == ["front01", "front02"]
    assert front[1].body == "前書き\n"                          # 只到锚点行为止
    assert front[1].page_start == 2 and front[1].page_end == 2
