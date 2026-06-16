from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

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
