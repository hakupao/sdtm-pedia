"""联网通道的 SSE 事件流与循环上限 (spec §7 §9.2)。

红线: 只用公开 CDISC 内容做假数据。
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
    return SimpleNamespace(model="opus-5", usage=None, choices=[SimpleNamespace(
        finish_reason=None,
        delta=SimpleNamespace(content=None, tool_calls=[SimpleNamespace(
            index=idx, id=call_id,
            function=SimpleNamespace(name=name, arguments=args))]))])


def _text_chunk(text, finish=None):
    return SimpleNamespace(model="opus-5", usage=None, choices=[SimpleNamespace(
        finish_reason=finish, delta=SimpleNamespace(content=text, tool_calls=None))])


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
    def __init__(self, *a, **k):
        self.searches_used = 0

    def search(self, query):
        from server.web_search import WebRef
        self.searches_used += 1
        return [WebRef(url="https://e.com/1", title="T", content="C",
                       retrieved_at="2026-08-31")], "ok"


def _client(router, monkeypatch=None, searcher_cls=_FakeSearcher):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router
    app.state.settings = Settings()
    if monkeypatch:
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
    assert router.calls <= s.web_max_rounds + 1   # +1 = 触顶后不带工具的收尾轮
    evs = _events(r.text)
    # 触顶也必须正常收尾: done 事件在, 不是把连接晾着
    assert [e for e, _ in evs].count("done") == 1
    # 搜索次数不得越过 15 次上限
    assert len([e for e, _ in evs if e == "tool_result"]) <= s.web_max_searches


def test_search_failure_surfaces_status(monkeypatch):
    class _FailSearcher(_FakeSearcher):
        def search(self, query):
            return [], "failed"
    r = _client(_ToolThenTextRouter(), monkeypatch, _FailSearcher).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert [d for e, d in evs if e == "tool_result"][0]["status"] == "failed"
    assert [d for e, d in evs if e == "done"][0]["web_status"] == "failed"
