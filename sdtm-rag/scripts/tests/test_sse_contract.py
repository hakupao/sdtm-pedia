"""SSE 事件契约: 后端实际吐出的事件名与字段, 必须正是前端 dispatch 认得的那些。

这个闸防的是「两侧各自绿、拼起来不工作」—— Task 4 的测试只验后端发了什么,
Task 5 的验证只验渲染函数收到 dict 后怎么画, 中间的解析层没人管。
"""
import re
from pathlib import Path

APP_JS = Path(__file__).resolve().parents[2] / "webchat" / "app.js"
ROUTER_PY = Path(__file__).resolve().parents[2] / "server" / "router.py"
WEB_SEARCH_PY = Path(__file__).resolve().parents[2] / "server" / "web_search.py"


def _dispatched_events() -> set[str]:
    """从 app.js 的 dispatch 里抠出前端认得的事件名。"""
    src = APP_JS.read_text(encoding="utf-8")
    return set(re.findall(r'ev\.event === "([a-z_]+)"', src))


def test_frontend_knows_every_event_the_backend_emits():
    # 后端 sse() 的调用点 = 实际会吐出的事件名
    router = ROUTER_PY.read_text(encoding="utf-8")
    emitted = set(re.findall(r'sse\("([a-z_]+)"', router))
    known = _dispatched_events()
    assert emitted <= known, f"后端会发但前端不认识的事件: {emitted - known}"


def test_frontend_reads_web_fields_from_done():
    src = APP_JS.read_text(encoding="utf-8")
    # done 的两个新字段必须真的被读取, 不能只在后端存在
    assert "web_status" in src, "前端没有读 done.web_status"
    assert "web_searches_ok" in src, "前端没有读 done.web_searches_ok"


def _backend_tool_result_statuses() -> set[str]:
    """tool_result.status 的真实取值域。

    router.py 里赋值写的是 `refs, st = [], "value"` (元组解包), 不是裸的
    `st = "value"` —— 用后一种形式抠字符串的话在这份代码里一个都抠不到,
    会让本测试的 backend 集合基本是空集, `backend <= frontend` 变成永远
    为真的伪命题, 起不到契约闸的作用。所以这里按两处真实来源分别抠:
      - router.py 里 `st = [...], "value"` 形式的字面量 (unknown_tool / bad_query / quota_exceeded)
      - web_search.py 的 WebSearcher.search() 各 return 语句 (disabled / quota_exceeded / failed / ok)
    """
    router = ROUTER_PY.read_text(encoding="utf-8")
    from_router = set(re.findall(r'st = \[\], "([a-z_]+)"', router))

    web_search = WEB_SEARCH_PY.read_text(encoding="utf-8")
    from_search = set(re.findall(r'return\s+[^\n]*"([a-z_]+)"', web_search))

    return from_router | from_search | {"ok"}


def test_frontend_covers_every_tool_result_status():
    """后端 tool_result.status 的取值域必须被前端文案表全覆盖 —— 少一个就会显示裸状态码。"""
    backend = _backend_tool_result_statuses()
    src = APP_JS.read_text(encoding="utf-8")
    block = src.split("note.textContent = {", 1)[1].split("}[d.status]", 1)[0]
    frontend = set(re.findall(r'^\s*([a-z_]+):', block, re.M))
    assert backend <= frontend, f"后端会发但前端文案表没有的 status: {backend - frontend}"
