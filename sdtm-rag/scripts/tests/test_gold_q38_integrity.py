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


def test_q38_gold_requires_all_three_sources_as_and():
    """三个源互补、不可互相替代 —— 必须全 AND, 不许有 OR 组。

    2026-08-07 (Step 6 独立判定) 补入 ch04 §4.1.6。曾短暂并成 OR 组, 同日经评审**撤回**,
    理由有二:

    1. **正文实测: 两节互补而非等价。** §4.2.2 含 "two-character"/"2-character" 与首位
       字符集规则; §4.1.6 **全文不含** "two-character", 讲的是数据集命名 + X/Y/Z 自定义域
       保留 + 第二位可为任意字母数字。判定文档 §4 建议列写"等价", 但同文档第 128 行写
       "互补而非重复" —— 文档自相矛盾, 以正文为准。
    2. **OR 组会抹掉挤占证据。** OR 组里未命中的成员**不进 miss 列**。而"§4.2.2 在生产口径下
       被同质簇挤出 top-15"是检索挤占那条线的头号证据; 一旦并成 OR, 评测账本里就再也看不到
       它 miss 过。**判别力优先于分数** —— 全 AND 下本题得 1/3, 低于 OR 的 1/2, 这是正确方向。

    本测试锁死"不许有 OR 组", 就是锁死上面第 2 条。
    """
    q = _q38()
    assert q.get("expected_sources_any") is None, (
        "q38 不得使用 OR 组 —— OR 组未命中的成员不进 miss 列, 会抹掉 §4.2.2 的挤占证据")
    assert q["expected_sources"] == [
        "chapters/ch02",
        "chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$",
        "chapters/ch04_general_assumptions.md#4.1.6 Additional Guidance on Dataset Naming$",
    ]


def test_q38_gold_ch04_section_needs_exact_section_match():
    """§4.2.2 用 `$` 精确匹配: 不带 $ 时 '4.2.2 Two-character Domain Identifier'
    是子串语义, 而 ch04 里不存在更长的兄弟 section —— 但标识符+子串是通用隐患,
    统一按精确写。这条测试锁住"召回了 4.2 或 4.2.3 不算命中"。"""
    q = _q38()
    gold = q["expected_sources"]
    ch04 = "knowledge_base/chapters/ch04_general_assumptions.md"
    ch02 = "knowledge_base/chapters/ch02_fundamentals.md"

    # 只召回邻节 -> 三项全 miss
    recall, _, _ = check_source_recall(
        [ch04], gold, retrieved_sections=["4.2.3 Use of \"Subject\" and USUBJID"])
    assert recall == 0.0, "邻节不得冒名命中"

    # 三槽全中才 1.0
    recall, hits, _ = check_source_recall(
        [ch04, ch04, ch02], gold,
        retrieved_sections=["4.2.2 Two-character Domain Identifier",
                            "4.1.6 Additional Guidance on Dataset Naming", "whole_file"],
    )
    assert recall == 1.0, hits

    # 关键: 少召回 §4.2.2 时它必须**出现在 miss 列**里 —— 这正是 OR 组会抹掉的那条挤占证据,
    # 也是本题坚持全 AND 的理由。断言 miss 内容而非只断言分数, 否则换成 OR 组这里照样绿。
    recall, _, misses = check_source_recall(
        [ch04, ch02], gold,
        retrieved_sections=["4.1.6 Additional Guidance on Dataset Naming", "whole_file"],
    )
    assert abs(recall - 2 / 3) < 1e-9, recall
    assert misses == [
        "chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$"
    ], f"§4.2.2 未命中时必须现身 miss 列, 实际 misses={misses}"
