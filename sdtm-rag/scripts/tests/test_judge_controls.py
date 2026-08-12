"""U2: 阳性/阴性对照 harness (spec §5.3)。

U1 Task 9 是一次性跑的; 这里变成可复跑脚本 —— 没有对照, 双臂数字不可解读。
抽样规则先写死, 事后不许换 (与分数无关是它唯一的价值)。
"""
import json

import pytest
import yaml

from eval import judge_controls as jc
from eval.judge_controls import sample_ids, positive_answer


def test_sample_ids_is_deterministic_and_spread():
    ids = [f"q{i:02d}" for i in range(30)]
    got = sample_ids(ids, 6)
    assert got == sample_ids(ids, 6)                    # 确定性
    assert len(got) == len(set(got)) == 6
    assert got[0] != ids[0]                             # 不取首题 (仿 U1)
    assert got == [ids[i] for i in (4, 8, 12, 17, 21, 25)]


def test_sample_ids_sorts_before_indexing():
    """入参顺序不该影响抽样 —— 否则"抽样规则"会随文件里的题序漂移。"""
    ids = [f"q{i:02d}" for i in range(30)]
    assert sample_ids(list(reversed(ids)), 6) == sample_ids(ids, 6)


def test_sample_ids_rejects_impossible_n():
    import pytest
    with pytest.raises(ValueError):
        sample_ids(["a", "b"], 6)


def test_positive_answer_is_the_gold_facts_joined():
    q = {"expected_facts": ["fact one", "fact two"]}
    a = positive_answer(q)
    assert "fact one" in a and "fact two" in a


# ------------------------------------------------------------------ 判别力补强 ↓
#
# 上面四条是 plan 逐字给的。按 Global Constraint 12 做方向②(「这行改坏了谁会红」)与
# 方向③(「断言的逻辑形状有什么盲区」)变异时实测: **16 条变异有 11 条存活**, 其中 9 条是
# 真缺口 —— `main()` 整个函数在四条断言下是零覆盖 (逐条见 evidence/step_u2_mutation_task7.md)。
# 最危险的两条都是**对调型**, 全绿存活:
#   C1 阳性/阴性两臂互换 —— 产出答案的集合一字不变, 只有配对方向翻转;
#   C2 judge 的 question/answer 两个位置参数互换 —— 同为 str, 不抛 TypeError。
# 两条都会让自毁条款 4 (阳性≥0.80 / 阴性≤0.20) 读出完全相反的结论, 而尺子本身没坏。
# 下面每条都钉**方向**而不只是"两者不同"。judge 全 stub, 零 LLM。

_FACTS = {
    "q01": ["FACT-alpha-01", "FACT-beta-01"],
    "q02": ["FACT-alpha-02", "FACT-beta-02"],
    "q03": ["FACT-alpha-03"],
    "q04": ["FACT-alpha-04", "FACT-beta-04"],
    "q05": ["FACT-alpha-05"],
    "q06": ["FACT-alpha-06", "FACT-beta-06"],
    "q07": ["FACT-alpha-07"],
}
# 文件里的题序**故意不是** id 升序 —— sample_ids 必须先排序再取位, 绕过它就会露馅。
_FILE_ORDER = ["q07", "q01", "q05", "q03", "q02", "q06", "q04"]


@pytest.fixture
def harness(tmp_path, monkeypatch):
    """写一份小题集 + 把 judge 换成记账 stub。返回 (run, calls)。"""
    path = tmp_path / "set.yml"
    path.write_text(
        yaml.safe_dump([{"id": i, "question": f"QUESTION-TEXT-{i}",
                         "expected_facts": _FACTS[i]} for i in _FILE_ORDER]),
        encoding="utf-8",
    )
    calls: list[dict] = []
    verdicts: dict[str, object] = {}

    def fake_judge(question, answer, expected_facts, judge_model, temperature=0.0):
        calls.append({"question": question, "answer": answer, "facts": expected_facts,
                      "judge_model": judge_model, "temperature": temperature})
        return verdicts.get(question, (1.0, list(expected_facts), []))

    monkeypatch.setattr(jc, "check_fact_recall_judge", fake_judge)

    def run(*argv):
        calls.clear()
        assert jc.main([str(path), *argv]) == 0
        return calls

    return run, calls, verdicts, tmp_path


def test_main_positive_arm_feeds_gold_and_negative_arm_feeds_the_empty_sentinel(harness):
    """杀 C1 (对调型) 与 B1。

    只断言"两臂不同"是不够的 —— 两臂互换后它们**照样不同**。必须钉方向: 阳性那臂
    逐字等于 gold 拼接, 阴性那臂一个 gold fact 都不含且是个常量句。
    """
    run, _, _, _ = harness
    pos = {c["question"]: c["answer"] for c in run("--mode", "positive", "--n", "3")}
    neg = {c["question"]: c["answer"] for c in run("--mode", "negative", "--n", "3")}

    assert set(pos) == set(neg) and len(pos) == 3
    for qtext, ans in pos.items():
        qid = qtext.rsplit("-", 1)[1]
        assert ans == positive_answer({"expected_facts": _FACTS[qid]})
    all_facts = [f for fs in _FACTS.values() for f in fs]
    for ans in neg.values():
        assert not any(f in ans for f in all_facts)
    assert len(set(neg.values())) == 1          # 阴性臂是同一个常量句, 与题目无关


def test_main_puts_question_and_answer_in_their_own_slots(harness):
    """杀 C2 (对调型): judge 的前两个位置参数互换后同样不报错, 尺子却整个失效。

    阳性模式下若两者互换, judge 被问的是"题干是否覆盖了 gold", 阳性对照会假性崩到 ~0
    并触发自毁条款 4 —— 表现为"judge 坏了", 实际是 harness 传参反了。
    """
    run, _, _, _ = harness
    for c in run("--mode", "positive", "--n", "3"):
        assert c["question"].startswith("QUESTION-TEXT-")
        assert not c["answer"].startswith("QUESTION-TEXT-")
        assert all(f in c["answer"] for f in c["facts"])


def test_main_selects_exactly_the_written_down_sample_ids_in_order(harness):
    """杀 B6: 抽样规则被绕过 (改取文件前 n 题) 时必须红。

    题集的文件序是 q07,q01,q05,… 而抽样规则要求 id 升序后取位 ⇒ 两者产出不同的三题。
    用列表相等而非集合相等, 顺序一并钉住。
    """
    run, _, _, _ = harness
    got = [c["question"].rsplit("-", 1)[1] for c in run("--mode", "positive", "--n", "3")]
    assert got == sample_ids(list(_FACTS), 3) == ["q02", "q04", "q06"]


def test_main_honours_judge_model_and_pins_temperature_to_zero(harness):
    """杀 B2/B3: --judge-model 被静默忽略, 或温度不是 0 (对照不再可复跑)。"""
    run, _, _, _ = harness
    calls = run("--mode", "positive", "--n", "3", "--judge-model", "vendor/model-under-test")
    assert {c["judge_model"] for c in calls} == {"vendor/model-under-test"}
    assert {c["temperature"] for c in calls} == {0.0}


def test_main_requires_an_explicit_mode(capsys):
    """杀 B4: --mode 不再必填时会静默走阴性臂, 把阳性对照悄悄跑成阴性。

    仿 Task 3 的教训: 只断 SystemExit 分不出"闸拒绝"与"flag 压根不存在", 故同判 stderr。
    """
    with pytest.raises(SystemExit):
        jc.main(["x.yml"])
    err = capsys.readouterr().err
    assert "unrecognized" not in err
    assert "--mode" in err


def test_main_keeps_unparseable_verdicts_out_of_the_average(harness):
    """杀 B5: judge 回复不可解析的题必须落 parse_ok=False 且**不进均值** (spec §5.3)。

    把它当 0.0 混进均值, 会让一次 judge 解析故障看起来像一次真实的低分。
    """
    run, _, verdicts, tmp_path = harness
    verdicts["QUESTION-TEXT-q04"] = None          # 抽中的三题之一解析失败
    out = tmp_path / "ctrl.json"
    run("--mode", "positive", "--n", "3", "--output", str(out))

    got = json.loads(out.read_text(encoding="utf-8"))
    assert got["mode"] == "positive"
    assert [r["parse_ok"] for r in got["rows"]] == [True, False, True]
    assert [r["recall"] for r in got["rows"]] == [1.0, None, 1.0]
    assert got["avg"] == 1.0                      # 2/2, 不是 2/3


def test_positive_answer_preserves_gold_fact_order_and_line_separation():
    """杀 C4 (对调型): 上面那条阳性断言是**成员形状** (`in`), 对顺序倒置结构上不可见。

    judge 被要求"逐 gold fact 按序输出一个布尔", 阳性对照的答案顺序与 gold 顺序一致
    是这条对照最干净的形态; 顺序漂移会让 judge 的对齐负担凭空变大。
    """
    q = {"expected_facts": ["fact one", "fact two", "fact three"]}
    assert positive_answer(q).splitlines() == q["expected_facts"]
