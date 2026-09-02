"""对抗抽样: 8 条 = 5 条裁判判 consistent (漏网只可能在这里) + 3 条裁判报警。
⚠ 判据预登记里写死了「后者不足 3 条时缺额用前者补满 8 条」——
⛔ 不许因为报警的不够就少判几条。"""
from eval.prod_wirein.build_human_sample import pick_sample, render_human_packet


def _rows(n_consistent, n_flagged):
    rows = [{"id": f"c{i:02d}", "verdict": "consistent", "quote": "", "authority": ""}
            for i in range(n_consistent)]
    rows += [{"id": f"f{i:02d}", "verdict": "inconsistent", "quote": "q", "authority": "a"}
             for i in range(n_flagged)]
    return rows


def test_sample_is_five_consistent_plus_three_flagged():
    sample, comp = pick_sample(_rows(50, 10))
    assert len(sample) == 8
    assert comp == {"consistent": 5, "flagged": 3, "backfilled": 0}
    assert sum(1 for r in sample if r["verdict"] == "consistent") == 5


def test_shortfall_is_backfilled_to_eight_and_recorded():
    """报警只有 1 条时: 仍然 8 条, 缺的 2 条从 consistent 补, 且构成被记下来。"""
    sample, comp = pick_sample(_rows(50, 1))
    assert len(sample) == 8, "⛔ 不许少判"
    assert comp == {"consistent": 7, "flagged": 1, "backfilled": 2}


def test_sample_is_deterministic_for_a_given_seed():
    """同一 seed 必须给同一批 —— 否则人判结果绑不回那次抽样, 证据不可核。"""
    a, _ = pick_sample(_rows(50, 10), seed=7)
    b, _ = pick_sample(_rows(50, 10), seed=7)
    assert [r["id"] for r in a] == [r["id"] for r in b]


def test_different_seeds_give_different_samples():
    """反方向: seed 不生效的实现 (例如忽略 seed 直接取前 5 条) 会让这条红。"""
    a, _ = pick_sample(_rows(50, 10), seed=1)
    b, _ = pick_sample(_rows(50, 10), seed=2)
    assert [r["id"] for r in a] != [r["id"] for r in b]


def test_too_few_rows_fails_loud():
    """总共不足 8 条时 ⛔ 不许悄悄返回短样本 —— 那会让「8/8 PASS」变成「3/3 PASS」。"""
    import pytest
    with pytest.raises(ValueError, match="不足"):
        pick_sample(_rows(2, 1))


def test_packet_shows_answer_and_quote_but_not_the_verdict():
    """⚠ 人判看答案原文 + 权威表, ⛔ 不看裁判的 verdict (预登记判据原文)。
    包里出现 verdict 就等于把答案提前告诉判卷人。

    ⚠ brief 原文这条断言写的是 `"ANSWER-c00" in md`, 绑死了 `random.Random(0)` 在本机
    Python 版本下具体抽中哪几个 id —— 实测 seed=0 抽出的是 c24/c48/c26/c02/c16 (不含 c00),
    连 brief 自己给的参考实现都会在这条断言上 FAIL。改成遍历全部 8 条抽中样本, 逐条断言其
    答案原文都进了包 —— 这比"只查第一条"更强: 只查第一条对"渲染器只渲染第一条"这类真缺陷
    零分辨力 (见变异 M5)。"""
    sample, _ = pick_sample(_rows(50, 10))
    md = render_human_packet(sample, {r["id"]: f"ANSWER-{r['id']}" for r in sample},
                             "| Dataset | Class |\n|---|---|\n| AE | Events |")
    for r in sample:
        assert f"ANSWER-{r['id']}" in md, f"抽中的 {r['id']} 的答案原文没进包"
    assert "| AE | Events |" in md
    assert "consistent" not in md and "inconsistent" not in md
