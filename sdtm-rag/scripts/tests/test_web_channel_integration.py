"""联网通道的红线断言 (spec §9 测试 4)。

不打真实网络: 用受控的假搜索结果**故意投毒**一个 CT 码, 断言它**原样存活**到
回灌给模型的 tool result 里 —— 红线不是"数据层把码洗掉", 而是 Rule 9(b) 在
prompt 层挡"模型看见码也不许拿它当事实依据"。数据层如果偷偷做了内容过滤,
会让人误以为安全边界在那里, 从而放松 prompt 层约束——而模型仍能从网页的
自然语言描述里拿到同一个事实。
"""
import re

from server.web_search import WebRef, render_tool_result


def test_render_tool_result_marks_web_provenance():
    """回灌给模型的每条结果都必须自带 url 与抓取日期 —— 标注不能靠模型记忆。
    正文也必须原样透传 (不能连标注对但内容被动过手脚)。"""
    import json
    refs = [WebRef(url="https://blog.example.com/x", title="T",
                   content="Use C12345 for this codelist.", retrieved_at="2026-08-31")]
    payload = json.loads(render_tool_result(refs, "ok"))
    r = payload["results"][0]
    assert r["url"] and r["retrieved_at"] == "2026-08-31"
    assert "C12345" in r["content"]


def test_poisoned_web_content_is_not_silently_filtered():
    """投毒内容 (含 CT 码) 必须原样进 tool result —— 这不是漏洞, 是设计: 红线
    由 Rule 9(b) 在 prompt 层挡 (见 test_rule9b_text_forbids_web_derived_codes),
    数据层不做内容审查。本测试钉住的是"没有偷偷加数据层过滤来假装安全"——
    如果这条测试变红, 说明有人在 render_tool_result 或它上游悄悄洗掉了码,
    那正是该被发现的回归, 不要把断言方向改成"码被过滤掉了"。"""
    import json
    refs = [WebRef(url="https://blog.example.com/x", title="T",
                   content="C99999 is the code.", retrieved_at="2026-08-31")]
    payload = json.loads(render_tool_result(refs, "ok"))
    assert "C99999" in payload["results"][0]["content"]


def test_search_result_content_is_not_filtered_for_ct_codes(monkeypatch):
    """真正容易被"好心添加"内容过滤的地方不是 render_tool_result (一个五行
    json.dumps, 没有藏东西的缝), 而是 WebSearcher.search() 里已经存在的内容
    变换槽位 (正文截断 `content=(it.get("content") or "")[:max_chars]`) ——
    加过滤不需要新开地方, 在截断旁边补一句 re.sub 读起来就像日常清洗。
    test_web_search.py 里唯一看那个槽位的 test_search_truncates_content 喂的是
    `"x" * 5000` (输入里没有任何码), 结构上不可能发现码被洗掉, 所以这里单独
    钉一条: 真实网页结果里的 Cxxxxx 经过 search() 后必须原样存活。"""
    from scripts.tests.test_web_search import _FakeResp, _payload, _searcher
    sr = _searcher(monkeypatch, lambda *a, **k: _FakeResp(_payload([
        {"url": "https://blog.example.com/x", "title": "T", "content": "C99999 is the code."},
    ])))
    refs, status = sr.search("q")
    assert status == "ok"
    assert "C99999" in refs[0].content


def test_rule9b_text_forbids_web_derived_codes():
    """Rule 9(b) 必须真的写着禁止从 web 产出码 —— 措辞被改掉时本测试要响。"""
    from server.rag import RAGEngine
    rules = RAGEngine._WEB_RULES
    assert "Cxxxxx" in rules
    assert "class" in rules.lower()
    assert re.search(r"do not|never", rules, re.I)
