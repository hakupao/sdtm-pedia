"""Plan B Phase 1: API 层联邦接线. Fake FederatedEngine, 不碰 chroma/LLM.

关键边界: federation 关闭 (app.state.federation=None) 时行为与现状逐字节一致;
routed=study 时跳过 CDISC 专用 structured answerer。
"""
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.router import api_router

# ── Settings 默认值: study KB 根必须是 RAGEngine 能直接吃的那一层 ──────────
# 修复轮 1: 默认曾指 data/study/st01, 但 ROUTING.md/INDEX.md 在其 cards/ 子目录,
# 开着 federation 启动即 FileNotFoundError (Task 4 冒烟发现)。

def test_study_kb_root_default_points_at_cards_dir():
    root = Settings().study_kb_root
    assert root.parts[-3:] == ("study", "st01", "cards")


def test_study_kb_root_default_holds_ragengine_required_files():
    root = Settings().study_kb_root
    if not root.is_dir():  # data/study 是本地数据, 不入库
        pytest.skip(f"study data not present: {root}")
    # RAGEngine.__init__ 硬要求这两个文件就在 kb_root 下 (server/rag.py)
    assert (root / "ROUTING.md").is_file()
    assert (root / "INDEX.md").is_file()


def _chunk(corpus):
    return SimpleNamespace(chunk_id=f"{corpus}-1", source=f"{corpus}/f.md", domain=None,
                           file_type=None, section=None, similarity=0.9,
                           text="x" * 400, corpus=corpus)


class _FakeFed:
    def __init__(self, routed="study", context="FED-CTX"):
        self.routed = routed
        self.context = context
        self.calls = []
        self.messages_ctx = None

    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        self.calls.append(corpus)
        return [_chunk("study"), _chunk("cdisc")], self.routed

    def format_context(self, chunks):
        return self.context

    def build_messages(self, q, ctx, history=None, *, corpus):
        self.messages_ctx = ctx
        return [{"role": "system", "content": f"S-{corpus}"},
                {"role": "user", "content": q}]


class _FakeLLM:
    def completion(self, model, messages, **kw):
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="ANS"))],
            model="m", usage=None)


class _Answerer:
    def __init__(self):
        self.called = False

    def resolve(self, q):
        self.called = True  # 返回 None = 无结构化事实, 不改写 context


def _client(fed=None, answerer=None):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = None  # federation 路径不得触碰单库引擎
    app.state.llm_router = _FakeLLM()
    app.state.settings = Settings()
    app.state.federation = fed
    if answerer is not None:
        app.state.answerer = answerer
    return TestClient(app)


def test_ask_federated_returns_corpus_and_routed():
    r = _client(fed=_FakeFed(routed="study")).post(
        "/api/ask", json={"question": "画面の項目は?", "corpus": "auto"})
    assert r.status_code == 200
    body = r.json()
    assert body["routed_corpus"] == "study"
    assert {s["corpus"] for s in body["sources"]} == {"study", "cdisc"}


def test_ask_corpus_passthrough():
    fed = _FakeFed()
    _client(fed=fed).post("/api/ask", json={"question": "q", "corpus": "both"})
    assert fed.calls == ["both"]


def test_ask_invalid_corpus_422():
    r = _client(fed=_FakeFed()).post("/api/ask", json={"question": "q", "corpus": "all"})
    assert r.status_code == 422


def test_ask_routed_study_skips_cdisc_answerer():
    ans = _Answerer()
    _client(fed=_FakeFed(routed="study"), answerer=ans).post(
        "/api/ask", json={"question": "q"})
    assert ans.called is False


def test_ask_routed_cdisc_keeps_answerer():
    ans = _Answerer()
    _client(fed=_FakeFed(routed="cdisc"), answerer=ans).post(
        "/api/ask", json={"question": "q"})
    assert ans.called is True


def test_ask_stream_sources_event_carries_routed_corpus():
    # ask_stream 用 async llm; 复用 test_ask_stream.py 的 _FakeRouter 形态
    from scripts.tests.test_ask_stream import _FakeRouter
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = None
    app.state.llm_router = _FakeRouter()
    app.state.settings = Settings()
    app.state.federation = _FakeFed(routed="both")
    r = TestClient(app).post("/api/ask_stream", json={"question": "q", "corpus": "auto"})
    assert r.status_code == 200
    assert '"routed_corpus": "both"' in r.text
    assert '"corpus": "study"' in r.text


# ── Task 2 复审转结论 1: 空联邦 context 必须退回单库哨兵串 ──────────────────
# FederatedEngine.format_context 在两组都空时返回 ""; 空串喂给 LLM 会让模型
# 以为"上下文段落缺失"而自由发挥, 单库路径在同一情形下给的是显式哨兵句。

def test_empty_federation_context_falls_back_to_sentinel():
    from server.rag import RAGEngine
    from server.router import _NO_CONTEXT

    # 哨兵串必须与单库 RAGEngine 逐字节一致 (format_context 空列表分支不碰 self)
    assert RAGEngine.format_context(None, []) == _NO_CONTEXT

    fed = _FakeFed(routed="both", context="")
    r = _client(fed=fed).post("/api/ask", json={"question": "q"})
    assert r.status_code == 200
    assert fed.messages_ctx == _NO_CONTEXT


def test_ask_stream_empty_federation_context_falls_back_to_sentinel():
    from scripts.tests.test_ask_stream import _FakeRouter
    from server.router import _NO_CONTEXT

    fed = _FakeFed(routed="both", context="")
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = None
    app.state.llm_router = _FakeRouter()
    app.state.settings = Settings()
    app.state.federation = fed
    assert TestClient(app).post(
        "/api/ask_stream", json={"question": "q"}).status_code == 200
    assert fed.messages_ctx == _NO_CONTEXT


# ── Task 2 复审转结论 2: build_messages 不得吞掉 history ────────────────────

def test_build_messages_keeps_system_first_and_preserves_history():
    from server.federation import FederatedEngine

    class _Stub:
        system_prompt = "SYS"

        def build_messages(self, q, ctx, history=None):
            msgs = [{"role": "system", "content": self.system_prompt}]
            if history:
                msgs.extend(history)
            msgs.append({"role": "user", "content": ctx})
            return msgs

    fed = FederatedEngine(_Stub(), _Stub(), None)
    history = [{"role": "user", "content": "H1"}, {"role": "assistant", "content": "H2"}]
    msgs = fed.build_messages("q", "CTX", history, corpus="both")
    assert msgs[0]["role"] == "system"
    assert "SYS" in msgs[0]["content"]
    assert msgs[1:3] == history
    assert msgs[-1]["content"] == "CTX"
