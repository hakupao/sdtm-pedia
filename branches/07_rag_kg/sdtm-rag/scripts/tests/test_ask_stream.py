from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.router import api_router


class _FakeRAG:
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return [SimpleNamespace(chunk_id="c1", source="domains/AE/spec.md", domain="AE",
                                file_type="spec", section="§1", similarity=0.9,
                                text="AETERM is the reported term." * 5)]
    def format_context(self, chunks):
        return "CTX"
    def build_messages(self, q, ctx, history=None):
        return [{"role": "user", "content": q}]


class _FakeRouter:
    async def acompletion(self, model, messages, stream=False, **kw):
        async def agen():
            for t in ["Hello", " world"]:
                yield SimpleNamespace(model="deepseek-v4-pro",
                                      choices=[SimpleNamespace(delta=SimpleNamespace(content=t))],
                                      usage=None)
            yield SimpleNamespace(model="deepseek-v4-pro", choices=[],
                                  usage=SimpleNamespace(prompt_tokens=10, completion_tokens=2, total_tokens=12))
        return agen()


def _client():
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = _FakeRouter()
    app.state.settings = Settings()
    return TestClient(app)


def test_ask_stream_event_sequence():
    r = _client().post("/api/ask_stream", json={"question": "what is AETERM?", "history": []})
    assert r.status_code == 200
    body = r.text
    assert "event: sources" in body
    assert "event: token" in body
    assert '"text": "Hello"' in body
    assert "event: done" in body
    assert '"total_tokens": 12' in body
    # sources event precedes first token
    assert body.index("event: sources") < body.index("event: token")


def test_ask_stream_empty_question_422():
    r = _client().post("/api/ask_stream", json={"question": "   ", "history": []})
    assert r.status_code == 422


class _NoStreamOptsRouter:
    """Provider that rejects the stream_options kwarg (simulates a non-DeepSeek swap)."""

    def __init__(self):
        self.calls = []

    async def acompletion(self, model, messages, stream=False, **kw):
        self.calls.append(kw)
        if "stream_options" in kw:
            raise TypeError("stream_options not supported by this provider")

        async def agen():
            for t in ["Hi", "!"]:
                yield SimpleNamespace(model="m", usage=None,
                                      choices=[SimpleNamespace(delta=SimpleNamespace(content=t))])
        return agen()


def test_ask_stream_falls_back_without_stream_options():
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.settings = Settings()
    router = _NoStreamOptsRouter()
    app.state.llm_router = router
    r = TestClient(app).post("/api/ask_stream", json={"question": "hi", "history": []})
    assert r.status_code == 200
    body = r.text
    assert "event: token" in body and '"text": "Hi"' in body
    assert "event: done" in body
    assert '"usage": null' in body  # usage unavailable on the fallback path -> null, not fabricated
    # First attempt carried stream_options (rejected); retry dropped it.
    assert any("stream_options" in c for c in router.calls)
    assert any("stream_options" not in c for c in router.calls)


# ── Task 10: ask_stream structured-answer injection + gate ────────────────

def test_stream_injects_facts_and_appends_correction():
    from pathlib import Path
    from types import SimpleNamespace

    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from server.config import Settings
    from server.meta_store import MetaStore
    from server.router import api_router
    from server.structured_answer import StructuredAnswerer

    class _CtxRAG:
        def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
            return [SimpleNamespace(chunk_id="c1", source="s", domain="AE", file_type="spec",
                                    section="§1", similarity=0.9, text="ctx")]
        def format_context(self, chunks):
            return "RETRIEVED_CTX"
        def build_messages(self, q, ctx, history=None):
            # Propagate ctx so the test can assert the facts block reached the LLM
            return [{"role": "system", "content": "sys"}, {"role": "user", "content": ctx}]

    class _StreamRouter:
        async def acompletion(self, model, messages, stream=False, **kw):
            saw = "Structured Facts (authoritative" in messages[-1]["content"]
            async def agen():
                yield SimpleNamespace(model="stub", usage=None,
                    choices=[SimpleNamespace(delta=SimpleNamespace(
                        content=f"[saw={saw}] TAETORD appears in 41 domains."))])
            return agen()

    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _CtxRAG()
    app.state.llm_router = _StreamRouter()
    app.state.settings = Settings()
    app.state.answerer = StructuredAnswerer(
        MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml"))

    body = TestClient(app).post(
        "/api/ask_stream", json={"question": "How many domains include TAETORD?", "history": []}
    ).text
    assert "[saw=True]" in body
    assert "Authoritative correction" in body  # correction emitted as token(s) before done
    assert "43" in body
