"""SSE 事件契约: 后端实际吐出的事件名与字段, 必须正是前端 dispatch 认得的那些。

这个闸防的是「两侧各自绿、拼起来不工作」—— Task 4 的测试只验后端发了什么,
Task 5 的验证只验渲染函数收到 dict 后怎么画, 中间的解析层没人管。
"""
import re
from pathlib import Path

from server.config import Settings
from scripts.tests.test_ask_stream_web import (
    _AlwaysToolRouter, _FakeSearcher, _ScriptedRouter, _ToolThenTextRouter,
    _client, _events, _of, _text_chunk, _tool_chunk,
)

_ROOT = Path(__file__).resolve().parents[2]
WEBCHAT = _ROOT / "webchat"
# 前端 2026-09-08 拆成 ES 模块, 这三样各自搬了家: SSE dispatch → js/stream.js,
# tool_result 文案表 → js/render.js, done 事件的字段读取还在 app.js。抽取形状一字未动。
STREAM_JS = WEBCHAT / "js" / "stream.js"
RENDER_JS = WEBCHAT / "js" / "render.js"
ROUTER_PY = _ROOT / "server" / "router.py"
WEB_SEARCH_PY = _ROOT / "server" / "web_search.py"


def _frontend_sources() -> str:
    """整个前端的源码 (入口 app.js + js/ 下全部模块) 拼成一份。

    扫**全部**模块而不是只挑 app.js, 理由是**抗重构**, 不是"把诱饵纳入视野": 下面那条闸钉的
    是"字段以 `.web_status` 这种带点形式被真的读到", 而读取点今天在 app.js 的 onDone 里 ——
    明天它被挪进 js/stream.js 或新拆出来的模块, 只扫 app.js 的版本会一路绿着退化成什么也没钉。
    (js/render.js 里那条解释字段取值域的注释是**裸词** `web_status`, 没有前导点, 带点的正则
    本来就匹配不到它 —— 扫不扫 render.js, 那个诱饵都不影响这条闸的判定, 别把理由记反了。)
    """
    files = [WEBCHAT / "app.js"] + sorted((WEBCHAT / "js").glob("*.js"))
    names = {f.name for f in files}
    # 尺寸下限 (同文件其余各闸的同款): 目录改名 / glob 失配会让列表塌成 1 份,
    # 下面的断言随之变成"只在 app.js 里找", 悄悄退回单文件时代。
    # 8 = app.js + js/ 下 7 个模块; 拆得更细只会变多, 变少一定是抽取坏了。
    assert len(files) >= 8, f"前端模块抽取失效, 只拿到 {len(files)} 份源码: {sorted(names)}"
    # 光看份数不够: 数目够了但恰好漏掉入口或 render.js, 断言照样会悄悄换掉被测对象。
    assert {"app.js", "render.js"} <= names, f"抽取结果缺入口或 render.js: {sorted(names)}"
    return "\n".join(f.read_text(encoding="utf-8") for f in files)


def _dispatched_events() -> set[str]:
    """从 js/stream.js 的 dispatch 里抠出前端认得的事件名。"""
    src = STREAM_JS.read_text(encoding="utf-8")
    return set(re.findall(r'ev\.event === "([a-z_]+)"', src))


def _frontend_status_table() -> set[str]:
    """前端 tool_result 的文案表 (js/render.js 的 onToolResultUI) 覆盖了哪些 status。"""
    src = RENDER_JS.read_text(encoding="utf-8")
    block = src.split("note.textContent = {", 1)[1].split("}[d.status]", 1)[0]
    return set(re.findall(r'^\s*([a-z_]+):', block, re.M))


def test_frontend_knows_every_event_the_backend_emits():
    # 后端 sse() 的调用点 = 实际会吐出的事件名
    router = ROUTER_PY.read_text(encoding="utf-8")
    emitted = set(re.findall(r'sse\("([a-z_]+)"', router))
    known = _dispatched_events()
    # 尺寸下限 (兄弟断言 `len(backend) >= 6` 的同款): `sse(` 一旦改名, `emitted` 变空集,
    # `set() <= known` 恒真 —— 正是这条闸本该防的那类失效。
    assert len(emitted) >= 6, f"事件名抽取失效, 只拿到 {emitted}"
    assert emitted <= known, f"后端会发但前端不认识的事件: {emitted - known}"


def test_frontend_reads_web_fields_from_done():
    """断言的是**读取形状** (`.web_status` / `.web_searches_ok` 属性访问), 不是
    字符串在全文出现过——`webchat/js/render.js` 里 renderWebStatus 上方解释这两个字段
    取值域的**注释**里也裸写着 "web_status" / "web_searches_ok" 这两个词 (没有前导 `.`),
    删掉 `webchat/app.js` onDone 里唯一的真实读取点
    (`gotWebStatus = (data || {}).web_status` 那两行) 之后, 老断言 (`"web_status" in src`)
    照样能在注释里找到匹配, 变成纸老虎。
    要求前导 `.` 就把注释行 (裸词, 无 `.`) 排除在外, 只认真实属性访问。
    扫的是**整个前端**而非单个文件, 是为了读取点搬家时这条闸不失效 (见 `_frontend_sources`)。"""
    src = _frontend_sources()
    assert re.search(r"\.web_status\b", src), "前端没有以 .web_status 形式读取该字段"
    assert re.search(r"\.web_searches_ok\b", src), "前端没有以 .web_searches_ok 形式读取该字段"


def _backend_tool_result_statuses() -> set[str]:
    """tool_result.status 的真实取值域 (静态字面量扫描, 见 test_frontend_covers_
    every_tool_result_status 的 docstring 说明这道闸的定位与局限)。

    router.py 里赋值写的是 `refs, st = [], "value"` 这类元组解包, 不是裸的
    `st = "value"`。早期用 `st = \\[\\], "..."` 做字面匹配, 但那个形状太窄:
    reviewer 实测把某处改成 `refs, st = refs2, "rate_limited"` (同样是元组解包,
    只是右边不是空列表 `[]`) 时, 老正则完全抠不到这个新状态值, `backend` 集合
    里根本不会出现 "rate_limited", 测试照样绿——契约漏洞被这条"闸"放过了。
    这里换成更宽的 `st\\s*=\\s*[^=\\n]*?"..."`, 只要求"`st` 被赋值为某个含双引号
    字符串的表达式", 不再挑剔右边的具体形状。

    `\\b` 前缀不能省: 不加的话会误抓 `test = "hello"` / `last = "world"` /
    `manifest = "boom"` 这类变量名恰好以 "st" 结尾的赋值 (reviewer 实测证实)。
    `\\b` 要求"st"前是词边界, 而这些变量名里"st"前一个字符 (e/a) 都是词字符,
    没有边界, 天然被排除。
    """
    router = ROUTER_PY.read_text(encoding="utf-8")
    from_router = set(re.findall(r'\bst\s*=\s*[^=\n]*?"([a-z_]+)"', router))

    web_search = WEB_SEARCH_PY.read_text(encoding="utf-8")
    from_search = set(re.findall(r'return\s+[^\n]*"([a-z_]+)"', web_search))

    return from_router | from_search | {"ok"}


def test_frontend_covers_every_tool_result_status():
    """后端 tool_result.status 的取值域必须被前端文案表全覆盖 —— 少一个就会显示裸状态码。

    这道闸是**静态**的 (抠源码字面量), 优点是能看到"源码里出现过哪些取值"这个
    信息本身、不依赖能不能真的构造出触发它的场景; 缺点是抠取形状可能跟不上写法
    变化 (见 `_backend_tool_result_statuses` docstring)。所以配了
    `test_tool_result_status_matrix_matches_frontend_table` 做**行为**层的第二重——
    那道闸从真实吐出的 SSE 事件收集 status, 抠取形状对不对无所谓, 局限反过来:
    只覆盖"有测试场景触发"的分支, 新增一个没场景覆盖的状态它不会报警。两者互补,
    缺一都会漏掉一类回归。
    """
    backend = _backend_tool_result_statuses()
    # 尺寸下限: brief 原版的字面匹配正则在这份代码上会把 backend 抠成几乎空集
    # (`{"ok"}` 兜底值以外一个都抠不到), `backend <= frontend` 对任何前端文案表
    # 都成立, 变成永真式——这条断言本该防的正是"契约闸失效却仍然全绿", 结果自己
    # 先失效了, 而且是手动 grep 才发现的。加这条下限, 一旦抠取逻辑又被写法变化
    # 绕过导致集合缩水, 测试直接报错, 不需要再靠人工複查才发现。
    assert len(backend) >= 6, f"status 抽取失效, 只拿到 {backend}"
    frontend = _frontend_status_table()
    assert backend <= frontend, f"后端会发但前端文案表没有的 status: {backend - frontend}"


def _observed_tool_result_statuses(monkeypatch) -> set[str]:
    """跑一个小矩阵, 触发 6 种 tool_result.status 里的每一种, 从真实吐出的 SSE
    事件收集 —— 比静态抠源码更硬: 断的是"这个分支真的会被触发且正确上报",
    不是"源码里字面出现过这个词"。

    ⚠ 局限 (与静态闸互补, 不能互相替代): 只覆盖这里写了场景的分支。新增一个
    没有对应测试场景的状态分支, 这个矩阵不会报警——它只是漏测那个值, 不会主动
    发现"少测了一种"; 静态闸至少能看到源码字面出现过哪些取值, 兜住这个盲区。
    """
    observed: set[str] = set()

    class _FailSearcher(_FakeSearcher):
        def search(self, query):
            self.searches_used += 1
            self.queries.append(query)
            return [], "failed"

    class _DisabledSearcher(_FakeSearcher):
        def search(self, query):
            self.searches_used += 1
            self.queries.append(query)
            return [], "disabled"

    scenarios = [
        # ok
        (_ToolThenTextRouter(), _FakeSearcher, None),
        # failed: searcher 自己报失败 (与"server 端整体未启用"的 disabled 不同)
        (_ToolThenTextRouter(), _FailSearcher, None),
        # disabled: searcher 报没有 API key (工具仍被提供给模型, 只是搜索本身报废)
        (_ToolThenTextRouter(), _DisabledSearcher, None),
        # quota_exceeded (+顺带再出一次 ok): 配额=1, 模型永远要搜, 第 2 轮起超额
        (_AlwaysToolRouter(), _FakeSearcher, Settings(web_max_searches=1)),
        # unknown_tool: 模型点名了一个不存在的工具
        (_ScriptedRouter([[_tool_chunk(0, "t", "run_shell", '{"query": "x"}'),
                           _text_chunk(None, finish="tool_calls")]]),
         _FakeSearcher, None),
        # bad_query: 模型给出截断的畸形 JSON 参数, 解不出 query
        (_ScriptedRouter([[_tool_chunk(0, "t", "web_search", '{"query": '),
                           _text_chunk(None, finish="tool_calls")]]),
         _FakeSearcher, None),
    ]
    for router, searcher_cls, settings in scenarios:
        client = _client(router, monkeypatch, searcher_cls, settings)
        r = client.post("/api/ask_stream", json={"question": "q", "web": True})
        for d in _of(_events(r.text), "tool_result"):
            observed.add(d["status"])
    return observed


def test_tool_result_status_matrix_matches_frontend_table(monkeypatch):
    observed = _observed_tool_result_statuses(monkeypatch)
    assert len(observed) >= 6, f"场景矩阵没能触发全部 6 种 status, 只观测到 {observed}"
    frontend = _frontend_status_table()
    assert observed <= frontend, (
        f"运行时真实吐出但前端文案表没有的 status: {observed - frontend}")
