"""联网通道的红线断言 (spec §9 测试 4)。

不打真实网络: 用受控的假搜索结果**故意投毒**一个 CT 码, 断言它不出现在答案里
—— 这才是 Rule 9(b) 的闸, 而不是「跑一次没看见码」。
"""
import re

from server.web_search import WebRef, render_tool_result


def test_render_tool_result_marks_web_provenance():
    """回灌给模型的每条结果都必须自带 url 与抓取日期 —— 标注不能靠模型记忆。"""
    import json
    refs = [WebRef(url="https://blog.example.com/x", title="T",
                   content="Use C12345 for this codelist.", retrieved_at="2026-08-31")]
    payload = json.loads(render_tool_result(refs, "ok"))
    r = payload["results"][0]
    assert r["url"] and r["retrieved_at"] == "2026-08-31"


def test_poisoned_web_content_still_carries_no_authority():
    """投毒内容原样进 tool result 是对的 (不做内容审查), 红线由 Rule 9(b) 在 prompt 层挡。
    本测试钉住: 我们没有偷偷做内容过滤来假装安全。"""
    import json
    refs = [WebRef(url="https://blog.example.com/x", title="T",
                   content="C99999 is the code.", retrieved_at="2026-08-31")]
    payload = json.loads(render_tool_result(refs, "ok"))
    assert "C99999" in payload["results"][0]["content"]


def test_rule9b_text_forbids_web_derived_codes():
    """Rule 9(b) 必须真的写着禁止从 web 产出码 —— 措辞被改掉时本测试要响。"""
    from server.rag import RAGEngine
    rules = RAGEngine._WEB_RULES
    assert "Cxxxxx" in rules
    assert "class" in rules.lower()
    assert re.search(r"do not|never", rules, re.I)
