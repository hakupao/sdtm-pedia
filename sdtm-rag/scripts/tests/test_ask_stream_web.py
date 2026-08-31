"""联网通道的 SSE 事件流与循环上限 (spec §7 §9.2)。

红线: 只用公开 CDISC 内容做假数据; 不打真实网络 (WebSearcher 一律替身)。
"""
import json
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.router import api_router


class _FakeRAG:
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return [SimpleNamespace(chunk_id="c1", source="domains/AE/spec.md", domain="AE",
                                file_type="spec", section="§1", similarity=0.9,
                                text="AETERM is the reported term.")]
    def format_context(self, chunks):
        return "CTX"
    def build_messages(self, q, ctx, history=None):
        return [{"role": "user", "content": q}]


def _tool_chunk(idx, call_id, name, args):
    """一个 tool_calls 增量分片。call_id / name / args 传 None 表示该片不带这个字段。"""
    return SimpleNamespace(model="opus-5", usage=None, choices=[SimpleNamespace(
        finish_reason=None,
        delta=SimpleNamespace(content=None, tool_calls=[SimpleNamespace(
            index=idx, id=call_id,
            function=SimpleNamespace(name=name, arguments=args))]))])


def _text_chunk(text, finish=None):
    return SimpleNamespace(model="opus-5", usage=None, choices=[SimpleNamespace(
        finish_reason=finish, delta=SimpleNamespace(content=text, tool_calls=None))])


def _usage_chunk(p, c, t):
    return SimpleNamespace(model="opus-5", choices=[], usage=SimpleNamespace(
        prompt_tokens=p, completion_tokens=c, total_tokens=t))


class _ScriptedRouter:
    """按脚本一轮吐一批 chunk; 顺便留存每轮收到的 messages 以便断言回灌内容。"""

    def __init__(self, rounds):
        self.rounds = rounds          # list[list[chunk]]
        self.calls = 0
        self.seen: list[list[dict]] = []
        self.seen_kwargs: list[dict] = []

    async def acompletion(self, model, messages, stream=False, **kw):
        self.calls += 1
        self.seen.append([dict(m) for m in messages])
        self.seen_kwargs.append(kw)
        batch = self.rounds[min(self.calls - 1, len(self.rounds) - 1)]
        async def agen():
            for ch in batch:
                yield ch
        return agen()


class _ToolThenTextRouter:
    """第 1 轮要搜索, 第 2 轮出文本 —— 最小的工具循环。"""
    def __init__(self):
        self.calls = 0

    async def acompletion(self, model, messages, stream=False, **kw):
        self.calls += 1
        first = self.calls == 1
        async def agen():
            if first:
                yield _tool_chunk(0, "tooluse_a", "web_search", '{"query": "SDTM custom domain"}')
                yield _text_chunk(None, finish="tool_calls")
            else:
                yield _text_chunk("Practice says X [Web: https://e.com/1 (retrieved 2026-08-31)]",
                                  finish="stop")
        return agen()


class _AlwaysToolRouter:
    """永远要搜索 —— 用来验轮数上限兜得住。"""
    def __init__(self):
        self.calls = 0

    async def acompletion(self, model, messages, stream=False, **kw):
        self.calls += 1
        async def agen():
            yield _tool_chunk(0, f"tooluse_{self.calls}", "web_search", '{"query": "q"}')
            yield _text_chunk(None, finish="tool_calls")
        return agen()


class _FakeSearcher:
    """替身: 不打网络。类级 made 记录所有实例, 供测试检查真实搜索次数。"""

    made: list = []

    def __init__(self, *a, **k):
        self.searches_used = 0
        self.queries: list[str] = []
        type(self).made.append(self)

    def search(self, query):
        from server.web_search import WebRef
        self.searches_used += 1
        self.queries.append(query)
        return [WebRef(url="https://e.com/1", title="T", content="C",
                       retrieved_at="2026-08-31")], "ok"


def _client(router, monkeypatch=None, searcher_cls=_FakeSearcher, settings=None):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router
    app.state.settings = settings or Settings()
    if monkeypatch:
        searcher_cls.made = []          # 每个测试独立计数
        monkeypatch.setattr("server.router.WebSearcher", searcher_cls)
    return TestClient(app)


def _events(body: str):
    out = []
    for block in body.split("\n\n"):
        if not block.strip():
            continue
        ev = dict(line.split(": ", 1) for line in block.splitlines() if ": " in line)
        if "event" in ev:
            out.append((ev["event"], json.loads(ev.get("data", "{}"))))
    return out


def _of(evs, kind):
    return [d for e, d in evs if e == kind]


# ── 基础: 开关 / 事件顺序 / 上限 ──────────────────────────────────────────

def test_web_off_emits_no_tool_events_and_status_off(monkeypatch):
    r = _client(_ToolThenTextRouter(), monkeypatch).post(
        "/api/ask_stream", json={"question": "what is AETERM?", "web": False})
    assert r.status_code == 200
    evs = _events(r.text)
    assert not [e for e, _ in evs if e in ("tool_call", "tool_result")]
    done = [d for e, d in evs if e == "done"][0]
    assert done["web_status"] == "off"


def test_web_on_emits_tool_call_and_result(monkeypatch):
    r = _client(_ToolThenTextRouter(), monkeypatch).post(
        "/api/ask_stream", json={"question": "how do others map custom fields?", "web": True})
    evs = _events(r.text)
    kinds = [e for e, _ in evs]
    assert kinds.index("tool_call") < kinds.index("tool_result")
    tc = [d for e, d in evs if e == "tool_call"][0]
    assert tc["round"] == 1 and tc["id"] == "tooluse_a"
    tr = [d for e, d in evs if e == "tool_result"][0]
    assert tr["count"] == 1 and tr["status"] == "ok" and tr["urls"] == ["https://e.com/1"]
    assert "".join(d.get("text", "") for e, d in evs if e == "token").startswith("Practice says")
    assert [d for e, d in evs if e == "done"][0]["web_status"] == "ok"


def test_round_cap_stops_loop(monkeypatch):
    """§9.2: 第 6 轮必须停, 且不得无限循环。"""
    router = _AlwaysToolRouter()
    r = _client(router, monkeypatch).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    assert r.status_code == 200
    s = Settings()
    assert router.calls == s.web_max_rounds + 1   # +1 = 触顶后不带工具的收尾轮
    evs = _events(r.text)
    # 触顶也必须正常收尾: done 事件在, 不是把连接晾着
    assert [e for e, _ in evs].count("done") == 1
    # 收尾轮**不带工具**, 所以它吐的 tool_calls 不执行 —— 搜索恰好 web_max_rounds 次,
    # 不是 +1 次 (多出来那次纯属烧配额, 结果没人看)
    assert len(_of(evs, "tool_result")) == s.web_max_rounds
    assert sum(len(x.queries) for x in _FakeSearcher.made) == s.web_max_rounds


def test_final_round_carries_no_tools(monkeypatch):
    """触顶后的收尾轮请求体里不得有 tools —— 模型必须用手上的材料作答。"""
    tool_round = [_tool_chunk(0, "t", "web_search", '{"query": "q"}'),
                  _text_chunk(None, finish="tool_calls")]
    router = _ScriptedRouter([tool_round])          # 永远要搜索
    _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    s = Settings()
    assert router.calls == s.web_max_rounds + 1
    assert all("tools" in kw for kw in router.seen_kwargs[:s.web_max_rounds])
    assert "tools" not in router.seen_kwargs[-1]


def test_search_failure_surfaces_status(monkeypatch):
    class _FailSearcher(_FakeSearcher):
        def search(self, query):
            self.searches_used += 1
            self.queries.append(query)
            return [], "failed"
    r = _client(_ToolThenTextRouter(), monkeypatch, _FailSearcher).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert _of(evs, "tool_result")[0]["status"] == "failed"
    assert _of(evs, "done")[0]["web_status"] == "failed"


# ── F-11: 增量分片累积 (累积器存在的唯一理由) ────────────────────────────

def test_fragmented_arguments_are_reassembled(monkeypatch):
    """arguments 跨 3 片到达, id/name 只在首片。"""
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "web_search", '{"que'),
         _tool_chunk(0, None, None, 'ry": "SDTM AE '),
         _tool_chunk(0, None, None, 'domain"}'),
         _text_chunk(None, finish="tool_calls")],
        [_text_chunk("answer", finish="stop")],
    ])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert _of(evs, "tool_call")[0]["query"] == "SDTM AE domain"
    assert _of(evs, "tool_call")[0]["id"] == "tooluse_a"
    assert _FakeSearcher.made[0].queries == ["SDTM AE domain"]
    assert _of(evs, "tool_result")[0]["status"] == "ok"


def test_parallel_tool_calls_are_kept_separate(monkeypatch):
    """两个并行调用的分片交错到达, 必须按 index 各归各位, 不能串味。"""
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "web_search", '{"que'),
         _tool_chunk(1, "tooluse_b", "web_search", '{"que'),
         _tool_chunk(0, None, None, 'ry": "AE"}'),
         _tool_chunk(1, None, None, 'ry": "CM"}'),
         _text_chunk(None, finish="tool_calls")],
        [_text_chunk("answer", finish="stop")],
    ])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    calls = _of(evs, "tool_call")
    assert [(c["id"], c["query"]) for c in calls] == [("tooluse_a", "AE"), ("tooluse_b", "CM")]
    assert _FakeSearcher.made[0].queries == ["AE", "CM"]
    # 回灌给模型的 assistant 消息里两个 tool_call 也必须是分开的两条
    assistant = [m for m in router.seen[1] if m["role"] == "assistant"][0]
    assert [t["function"]["arguments"] for t in assistant["tool_calls"]] == [
        '{"query": "AE"}', '{"query": "CM"}']


def test_repeated_name_fragments_are_not_concatenated(monkeypatch):
    """有 provider 每片都重发 name; 拼接会得到 'web_searchweb_search'。"""
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "web_search", '{"query": '),
         _tool_chunk(0, "tooluse_a", "web_search", '"AE"}'),
         _text_chunk(None, finish="tool_calls")],
        [_text_chunk("answer", finish="stop")],
    ])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert _of(evs, "tool_result")[0]["status"] == "ok"   # 名字拼坏了这里会是 unknown_tool
    assistant = [m for m in router.seen[1] if m["role"] == "assistant"][0]
    assert assistant["tool_calls"][0]["function"]["name"] == "web_search"
    tool_msg = [m for m in router.seen[1] if m["role"] == "tool"][0]
    assert tool_msg["name"] == "web_search"


def test_missing_index_and_id_attrs_do_not_kill_the_answer(monkeypatch):
    """缺 index/id 的 delta 不得让 AttributeError 穿透 —— 那会丢掉整个答案。"""
    bare = SimpleNamespace(function=SimpleNamespace(name="web_search",
                                                    arguments='{"query": "AE"}'))
    chunk = SimpleNamespace(model="opus-5", usage=None, choices=[SimpleNamespace(
        finish_reason=None, delta=SimpleNamespace(content=None, tool_calls=[bare]))])
    router = _ScriptedRouter([[chunk, _text_chunk(None, finish="tool_calls")],
                              [_text_chunk("answer", finish="stop")]])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert not _of(evs, "error")
    assert _of(evs, "tool_call")[0]["query"] == "AE"
    assert "".join(d.get("text", "") for e, d in evs if e == "token") == "answer"


# ── F-12: 配额耗尽 ───────────────────────────────────────────────────────

def test_quota_exhaustion_stops_real_searching(monkeypatch):
    """web_max_searches=2: 第 3 次起只发 quota_exceeded, 不再真搜。"""
    s = Settings(web_max_searches=2)
    router = _AlwaysToolRouter()
    r = _client(router, monkeypatch, settings=s).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    statuses = [d["status"] for d in _of(evs, "tool_result")]
    assert statuses == ["ok", "ok", "quota_exceeded", "quota_exceeded", "quota_exceeded"]
    # 真实搜索恰好 2 次 —— searches_used 是在 asyncio.to_thread 的工作线程里自增的,
    # 主协程 await 之后读到的必须是更新后的值, 否则这里会看到 5 次。
    assert sum(len(x.queries) for x in _FakeSearcher.made) == 2
    assert _of(evs, "done")[0]["web_status"] == "partial"   # 有成有败


# ── F-3: 调工具前说的话要回灌 ────────────────────────────────────────────

def test_assistant_text_before_tool_call_is_fed_back(monkeypatch):
    router = _ScriptedRouter([
        [_text_chunk("Let me look that up. "),
         _tool_chunk(0, "tooluse_a", "web_search", '{"query": "AE"}'),
         _text_chunk(None, finish="tool_calls")],
        [_text_chunk("Practice says X.", finish="stop")],
    ])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert "".join(d.get("text", "") for e, d in evs
                   if e == "token") == "Let me look that up. Practice says X."
    assistant = [m for m in router.seen[1] if m["role"] == "assistant"][0]
    assert assistant["content"] == "Let me look that up. "   # 不是 None


def test_assistant_content_is_none_when_round_had_no_text(monkeypatch):
    """本轮一个字没说就回灌 None, 不是空串 —— 空串在部分 provider 上是非法的。"""
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "web_search", '{"query": "AE"}'),
         _text_chunk(None, finish="tool_calls")],
        [_text_chunk("answer", finish="stop")],
    ])
    _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    assistant = [m for m in router.seen[1] if m["role"] == "assistant"][0]
    assert assistant["content"] is None


# ── F-4: usage 跨轮累加 + partial 标记 ───────────────────────────────────

def test_usage_accumulates_across_rounds(monkeypatch):
    """每轮都是独立计费的调用, 只报最后一轮会系统性低报成本。"""
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "web_search", '{"query": "AE"}'),
         _text_chunk(None, finish="tool_calls"), _usage_chunk(1000, 50, 1050)],
        [_text_chunk("answer", finish="stop"), _usage_chunk(3000, 200, 3200)],
    ])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    usage = _of(_events(r.text), "done")[0]["usage"]
    assert usage == {"prompt_tokens": 4000, "completion_tokens": 250, "total_tokens": 4250}


def test_usage_marks_partial_when_a_round_reports_none(monkeypatch):
    """窄重试丢了 stream_options 的那一轮没有 usage —— 总量必须标明不完整。"""
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "web_search", '{"query": "AE"}'),
         _text_chunk(None, finish="tool_calls"), _usage_chunk(1000, 50, 1050)],
        [_text_chunk("answer", finish="stop")],            # 第 2 轮无 usage
    ])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    usage = _of(_events(r.text), "done")[0]["usage"]
    assert usage["total_tokens"] == 1050 and usage["partial"] is True


def test_usage_is_null_when_no_round_reported_any(monkeypatch):
    """一轮都没拿到就报 null, 不编造 0 —— 沿用本文件原有的 never-fabricated 原则。"""
    r = _client(_ToolThenTextRouter(), monkeypatch).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    assert _of(_events(r.text), "done")[0]["usage"] is None


# ── F-7 / F-8: 模型侧出错不算联网失败 ────────────────────────────────────

def test_unknown_tool_is_rejected_without_searching(monkeypatch):
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "run_shell", '{"query": "rm -rf /"}'),
         _text_chunk(None, finish="tool_calls")],
        [_text_chunk("answer", finish="stop")],
    ])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert _of(evs, "tool_result")[0]["status"] == "unknown_tool"
    assert _FakeSearcher.made[0].queries == []            # 一次都没搜, 没烧配额
    assert _of(evs, "done")[0]["web_status"] == "ok"      # 模型的错, 不是联网的错
    tool_msg = [m for m in router.seen[1] if m["role"] == "tool"][0]
    assert "run_shell" in tool_msg["content"] and "web_search" in tool_msg["content"]


def test_malformed_arguments_do_not_mark_web_failed(monkeypatch):
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "web_search", '{"query": '),   # 截断的 JSON
         _text_chunk(None, finish="tool_calls")],
        [_text_chunk("answer", finish="stop")],
    ])
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert _of(evs, "tool_result")[0]["status"] == "bad_query"
    assert _FakeSearcher.made[0].queries == []
    assert _of(evs, "done")[0]["web_status"] == "ok"


# ── F-9 / F-10: web_status 语义 ──────────────────────────────────────────

def test_server_side_disabled_reports_disabled_not_off(monkeypatch):
    """用户勾了联网、服务端关着 —— 报 off 会让界面一声不吭。"""
    r = _client(_ToolThenTextRouter(), monkeypatch,
                settings=Settings(web_search_enabled=False)).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert not _of(evs, "tool_call")                       # 没挂工具就不解释工具调用
    assert _of(evs, "done")[0]["web_status"] == "disabled"


def test_mixed_success_and_failure_reports_partial(monkeypatch):
    """第 1 次挂、后面成 —— 不能报 failed (答案里带着真实 [Web:] 引用, 提示会自相矛盾)。"""
    from server.web_search import WebRef

    class _FlakySearcher(_FakeSearcher):
        def search(self, query):
            self.searches_used += 1
            self.queries.append(query)
            if len(self.queries) == 1:
                return [], "failed"
            return [WebRef(url="https://e.com/2", title="T", content="C",
                           retrieved_at="2026-08-31")], "ok"
    r = _client(_AlwaysToolRouter(), monkeypatch, _FlakySearcher).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    statuses = [d["status"] for d in _of(evs, "tool_result")]
    assert statuses[0] == "failed" and statuses[1] == "ok"
    assert _of(evs, "done")[0]["web_status"] == "partial"


def test_all_failed_reports_the_most_severe_status(monkeypatch):
    """一次没成: 报最严重的那个 (disabled > quota_exceeded > failed), 不是最后一个。"""
    class _DegradingSearcher(_FakeSearcher):
        def search(self, query):
            self.searches_used += 1
            self.queries.append(query)
            return [], ("disabled" if len(self.queries) == 1 else "failed")
    r = _client(_AlwaysToolRouter(), monkeypatch, _DegradingSearcher).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert [d["status"] for d in _of(evs, "tool_result")][:2] == ["disabled", "failed"]
    assert _of(evs, "done")[0]["web_status"] == "disabled"   # 最后一个是 failed


# ── F-1: 同步搜索不得占死 event loop ─────────────────────────────────────

def test_search_runs_off_the_event_loop_thread(monkeypatch):
    """searcher.search 是同步 requests.post (单次最长 web_timeout_s, 单请求可 15 次)。
    直接 await 会冻结整个 uvicorn event loop —— 所有并发 SSE 流和健康检查一起挂。
    判据: search 体内取不到"正在运行的 event loop" == 它跑在工作线程上。"""
    import asyncio as _aio

    probe = {}

    class _ThreadProbeSearcher(_FakeSearcher):
        def search(self, query):
            try:
                _aio.get_running_loop()
                probe["on_loop_thread"] = True
            except RuntimeError:
                probe["on_loop_thread"] = False
            return super().search(query)

    r = _client(_ToolThenTextRouter(), monkeypatch, _ThreadProbeSearcher).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    assert _of(_events(r.text), "tool_result")[0]["status"] == "ok"
    assert probe["on_loop_thread"] is False


# ── done.web_searches_ok: 让"开了联网但一次没搜成"变得可观测 ──────────────

def test_web_searches_ok_counts_only_successful_searches(monkeypatch):
    r = _client(_ToolThenTextRouter(), monkeypatch).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    assert _of(_events(r.text), "done")[0]["web_searches_ok"] == 1


def test_web_off_reports_zero_successful_searches(monkeypatch):
    r = _client(_ToolThenTextRouter(), monkeypatch).post(
        "/api/ask_stream", json={"question": "q", "web": False})
    assert _of(_events(r.text), "done")[0]["web_searches_ok"] == 0


def test_model_burning_rounds_on_bogus_tools_is_visible(monkeypatch):
    """盲区: 模型净点名不存在的工具耗光 5 轮, web_status 仍是 ok (确实一次网都没打)。
    单看 web_status 用户无从判断; web_searches_ok == 0 把它变成可观测的。"""
    router = _ScriptedRouter([
        [_tool_chunk(0, "tooluse_a", "run_shell", '{"query": "x"}'),
         _text_chunk(None, finish="tool_calls")],
    ])                                        # _ScriptedRouter 会重复最后一批
    r = _client(router, monkeypatch).post("/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    s = Settings()
    assert router.calls == s.web_max_rounds + 1
    assert [d["status"] for d in _of(evs, "tool_result")] == ["unknown_tool"] * s.web_max_rounds
    assert _FakeSearcher.made[0].queries == []          # 一次网都没打
    done = _of(evs, "done")[0]
    assert done["web_status"] == "ok" and done["web_searches_ok"] == 0


def test_quota_run_reports_only_the_successful_searches(monkeypatch):
    """配额耗尽那几次不算成功。"""
    r = _client(_AlwaysToolRouter(), monkeypatch, settings=Settings(web_max_searches=2)).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    done = _of(_events(r.text), "done")[0]
    assert done["web_status"] == "partial" and done["web_searches_ok"] == 2


def test_all_failed_reports_zero_successful_searches(monkeypatch):
    class _FailSearcher(_FakeSearcher):
        def search(self, query):
            self.searches_used += 1
            self.queries.append(query)
            return [], "failed"
    r = _client(_AlwaysToolRouter(), monkeypatch, _FailSearcher).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    done = _of(_events(r.text), "done")[0]
    assert done["web_status"] == "failed" and done["web_searches_ok"] == 0
