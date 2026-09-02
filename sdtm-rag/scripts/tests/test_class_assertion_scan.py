"""(b) 层裁判扫描器。⚠ 本文件**零真实 LLM 调用** —— judge 是注入的可调用对象。
真实调用只发生在 Task 6, 且要先经用户同意。"""
import json

import pytest

from eval.prod_wirein.class_assertion_scan import (
    build_judge_prompt, parse_judge_verdict, scan_answers,
)

_AUTH_MD = "| Dataset | Class |\n|---|---|\n| AE | Events |\n| SUPP-- | Relationship |"


def test_prompt_carries_the_whole_authority_table():
    """裁判必须**看着表**判, 不是凭记忆。表没进提示词 = 它在猜。"""
    p = build_judge_prompt("AE is an Events domain.", _AUTH_MD)
    assert "| AE | Events |" in p
    assert "| SUPP-- | Relationship |" in p


def test_prompt_tells_the_judge_about_the_supp_naming_variant():
    """⚠ 实测坑 (Task 2): 表键是 `SUPP--`, 而 "SUPPQUAL" 在 ch03 出现 0 次。
    不告诉裁判这个变体, 它会把「SUPPQUAL 是 special-purpose」当成"查不到 ⇒ 没断言"放过。
    本测试守的判据: **M4 (删掉整段 Naming note) 必须让它红。**

    ⚠⚠ 修复轮 1 (原版本经 M4 实测证伪, 见 task-3-report.md 「修复轮 1」段): 原来的
    answer 文本是 `"SUPPQUAL is a special-purpose dataset."`, 它本身就含字面
    "SUPPQUAL", 经 `{answer}` 占位符原样进了 prompt —— 于是 `"SUPPQUAL" in p` 不管
    Naming note 在不在都为真, 这条闸形同虚设。

    ⇒ 改法两处:
    1. answer **刻意换成不含字面 "SUPPQUAL" 的句子** (`SUPPAE`)。这样 prompt 里
       "SUPPQUAL" 就**只可能来自 Naming note** (Naming note 是措辞里唯一列出这个
       具体例子的地方) —— `assert "SUPPQUAL" in p` 才真的钉住 Naming note。
       ⛔ 谁把 answer 换回含字面 "SUPPQUAL" 的句子, 这条闸就会重新失效, 而且不会
       报错 (只会悄悄变回恒真) —— 改 answer 前务必重跑 M4。
    2. 删掉了原来的 `assert "SUPP--" in p`: 它的真值来自 `_AUTH_MD` 本身, 跟
       Naming note 无关, 对本测试零分辨力; "权威表整段进了 prompt" 这件事已经由
       `test_prompt_carries_the_whole_authority_table` 单独钉住, 留在这里只会让
       读者误以为这条闸比实际更强。"""
    p = build_judge_prompt("SUPPAE is a special-purpose dataset.", _AUTH_MD)
    assert "SUPPQUAL" in p


def test_parse_accepts_a_clean_verdict():
    raw = json.dumps({"has_assertion": True, "verdict": "inconsistent",
                      "quote": "SUPPQUAL is a special-purpose dataset",
                      "authority": "SUPP-- | Relationship"})
    v = parse_judge_verdict(raw)
    assert v["has_assertion"] is True
    assert v["verdict"] == "inconsistent"
    assert v["quote"].startswith("SUPPQUAL")


def test_parse_tolerates_a_fenced_verdict():
    """裁判常把 JSON 包在 ```json 里 —— 解析不了就等于整条扫描白跑。"""
    v = parse_judge_verdict('```json\n{"has_assertion": false, "verdict": "consistent",\n'
                            ' "quote": "", "authority": ""}\n```')
    assert v["has_assertion"] is False


def test_parse_marks_unparseable_as_unsure_not_consistent():
    """⛔ 解析失败**不得**落成 `consistent` —— 那会把「裁判没说清」读成「干净」,
    而对抗抽样正是从 consistent 里抽。落 `unsure` 才会被抽进人判。"""
    v = parse_judge_verdict("I think it's fine, honestly.")
    assert v["verdict"] == "unsure"
    assert v["parse_error"] is True


def test_scan_returns_one_row_per_answer_and_keeps_ids():
    calls = []

    def fake_judge(prompt: str) -> str:
        calls.append(prompt)
        return json.dumps({"has_assertion": False, "verdict": "consistent",
                           "quote": "", "authority": ""})

    entries = [{"id": "q01", "answer": "A"}, {"id": "q02", "answer": "B"}]
    rows = scan_answers(entries, fake_judge, _AUTH_MD)
    assert [r["id"] for r in rows] == ["q01", "q02"]
    assert len(calls) == 2, "每个答案必须各调一次裁判"
    assert all(r["verdict"] == "consistent" for r in rows)


def test_scan_isolates_a_judge_failure():
    """一个答案judge 挂掉不得让整批白跑 —— 记成 unsure + error, 继续扫。
    ⛔ 不得记成 consistent (同上: 会躲开对抗抽样)。"""
    def flaky_judge(prompt: str) -> str:
        if "BOOM" in prompt:
            raise RuntimeError("judge exploded")
        return json.dumps({"has_assertion": False, "verdict": "consistent",
                           "quote": "", "authority": ""})

    rows = scan_answers([{"id": "q01", "answer": "BOOM"}, {"id": "q02", "answer": "ok"}],
                        flaky_judge, _AUTH_MD)
    assert rows[0]["verdict"] == "unsure" and rows[0]["error"]
    assert rows[1]["verdict"] == "consistent" and not rows[1].get("error")
