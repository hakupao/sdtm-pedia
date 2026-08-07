"""q38 gold 完整性: 题干两问需要两个不可互相替代的源。

背景: 原 gold 只有 chapters/ch02, 而字面回答"two-character 规则"的是 ch04 §4.2.2。

**下面这条是口径依赖的, 引用时必须带口径** (混口径正是本项目上一轮栽过的形态):
- dense-only 口径: §4.2.2 是检索 #1, 旧 gold 把这次正确召回判成 0.0 (假失分) ——
  这是补 gold 的理由。
- 生产口径 (hybrid + structured_lookup): §4.2.2 被挤出 top-15, 故 q38 改前改后
  同为 0.0。**本次改动不改变生产分数**, 它买到的是判别力 (能区分"召回了 §4.2.2"
  和"只召回了 ch04 的别的节"), 不是涨分。

两组实测数字见
.superpowers/sdd/2026-08-07-retrieval-crowding-and-gold-integrity/task-1-report.md
"""
import yaml

from eval.run_eval import check_source_recall

TEST_SET = "eval/test_set_v3.yml"


def _q38():
    # encoding 显式给死: 该题集含中文注释, 非 UTF-8 locale 下不指定会炸。
    with open(TEST_SET, encoding="utf-8") as f:
        test_set = yaml.safe_load(f)
    for q in test_set:
        if q["id"] == "q38":
            return q
    raise AssertionError("q38 not found in " + TEST_SET)


def test_q38_gold_keeps_ch02_as_a_separate_required_slot():
    """两问两槽: ch02 与 ch04 不可互相替代, ch02 必须留在 AND 里。

    2026-08-07 更新 (Step 6 独立判定): ch04 §4.1.6 也逐字回答"两字符域码的规则"
    (标准码取自 CT codelist C66734; X/Y/Z 保留给自定义域, 第二位可为任意字母或数字),
    与 §4.2.2 **在这一槽内互为等价源**, 故两者并成 OR 组。

    本测试的原意 (ch02 与 ch04 是两个不可互换的槽) **未变**: OR 组只发生在 ch04 槽内部,
    ch02 仍是独立的 AND 项。锁死这一点 —— 若哪天有人把 ch02 也并进 OR 组, 该题就退化成
    "召回任意一个就满分", 那正是 OR 组使用纪律禁止的放宽。
    """
    q = _q38()
    assert q["expected_sources"] == ["chapters/ch02"], "ch02 必须独立成 AND 槽"
    assert q["expected_sources_any"] == [
        "chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$",
        "chapters/ch04_general_assumptions.md#4.1.6 Additional Guidance on Dataset Naming$",
    ]
    assert "chapters/ch02" not in q["expected_sources_any"], "ch02 不得并入 OR 组"


def test_q38_gold_ch04_section_needs_exact_section_match():
    """§4.2.2 用 `$` 精确匹配: 不带 $ 时 '4.2.2 Two-character Domain Identifier'
    是子串语义, 而 ch04 里不存在更长的兄弟 section —— 但标识符+子串是通用隐患,
    统一按精确写。这条测试锁住"召回了 4.2 或 4.2.3 不算命中"。"""
    q = _q38()
    # ch04 的两节现在住在 OR 组里 —— 必须把 any_of 一起传, 否则本测试会变成空转:
    # 只用 expected_sources (= ["chapters/ch02"]) 根本碰不到 section 匹配逻辑, 断言照样
    # 全绿而 `$` 是否生效无人知道。
    gold = q["expected_sources"]
    any_of = q["expected_sources_any"]
    srcs = ["knowledge_base/chapters/ch04_general_assumptions.md"]

    recall, _, _ = check_source_recall(
        srcs, gold, any_of=any_of,
        retrieved_sections=["4.2.3 Use of \"Subject\" and USUBJID"],
    )
    assert recall == 0.0, "邻节不得冒名命中"

    # 命中 §4.2.2 -> OR 组满足; 再加 ch02 -> 两槽全中
    recall, hits, _ = check_source_recall(
        srcs + ["knowledge_base/chapters/ch02_fundamentals.md"],
        gold, any_of=any_of,
        retrieved_sections=["4.2.2 Two-character Domain Identifier", "whole_file"],
    )
    assert recall == 1.0, hits

    # 命中 §4.1.6 (OR 组另一成员) 同样满足该槽 —— 锁住"两节互为等价源"这件事本身
    recall, hits, _ = check_source_recall(
        srcs + ["knowledge_base/chapters/ch02_fundamentals.md"],
        gold, any_of=any_of,
        retrieved_sections=["4.1.6 Additional Guidance on Dataset Naming", "whole_file"],
    )
    assert recall == 1.0, hits
