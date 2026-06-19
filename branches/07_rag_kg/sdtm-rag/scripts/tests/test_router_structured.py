# scripts/tests/test_router_structured.py
# Mirrors conftest.py: bare FastAPI + manual app.state.* fakes (NO lifespan/create_app).
# _CtxRAG.build_messages propagates the (possibly augmented) context into messages so we
# can assert the facts block reached the LLM. The fake completion emits a WRONG count (41)
# to exercise the counting gate.
from pathlib import Path
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.meta_store import MetaStore
from server.router import api_router
from server.structured_answer import StructuredAnswerer

_META = Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml"


class _CtxRAG:
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return [SimpleNamespace(chunk_id="c1", source="domains/AE/spec.md", domain="AE",
                                file_type="spec", section="§1", similarity=0.9, text="ctx")]

    def format_context(self, chunks):
        return "RETRIEVED_CTX"

    def build_messages(self, q, ctx, history=None):
        # Propagate ctx into messages so the test can assert the facts block reached LLM
        return [{"role": "system", "content": "sys"}, {"role": "user", "content": ctx}]


class _SyncRouter:
    def completion(self, model, messages, **kw):
        ctx = messages[-1]["content"]
        saw = "Structured Facts (authoritative" in ctx
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(
                content=f"[saw_facts={saw}] TAETORD appears in 41 domains."))],
            usage=None, model="stub")


def _app():
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _CtxRAG()
    app.state.llm_router = _SyncRouter()
    app.state.settings = Settings()
    app.state.answerer = StructuredAnswerer(MetaStore(_META))
    return app


def test_ask_injects_facts_and_gate_corrects():
    r = TestClient(_app()).post(
        "/api/ask",
        json={"question": "How many domains include TAETORD?", "model": "default"},
    )
    assert r.status_code == 200, r.text
    ans = r.json()["answer"]
    assert "[saw_facts=True]" in ans          # facts block prepended to context
    assert "Authoritative correction" in ans  # gate caught the wrong 41 -> appends 43
    assert "43" in ans


def test_ask_passthrough_when_no_entity():
    r = TestClient(_app()).post(
        "/api/ask",
        json={"question": "Give an overview of clinical trials.", "model": "default"},
    )
    assert r.status_code == 200, r.text
    assert "[saw_facts=False]" in r.json()["answer"]  # resolve()->None, no injection
