"""DM1 T1 (D6): /api/ask_stream must log question/corpus/chunk_ids, never the answer.

没有这一行, dogfood ⚑ 的第一轮原句就永久丢失, 只能用重构句复现
(evidence/checkpoints/dogfood_ds_dscont_2026-09-15.md)。
"""
from types import SimpleNamespace

import pytest
import structlog
from structlog.testing import capture_logs
from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.router import api_router


class _FakeFed:
    """联邦引擎 fake: retrieve() 返回 (chunks, routed) — 与 test_federation_api.py 同型。"""

    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        return [SimpleNamespace(chunk_id="c1", source="domains/DS/spec.md", domain="DS",
                                file_type="spec", section="§1", similarity=0.9,
                                text="DSTERM." * 5, corpus="cdisc")], "both"

    def format_context(self, chunks):
        return "CTX"

    def build_messages(self, q, ctx, history=None, *, corpus):
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


@pytest.fixture
def client():
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = None  # federation 路径不得触碰单库引擎
    app.state.federation = _FakeFed()
    app.state.llm_router = _FakeRouter()
    app.state.settings = Settings()
    return TestClient(app)


def test_ask_stream_logs_question_corpus_and_chunk_ids(client):
    with capture_logs() as logs:
        r = client.post("/api/ask_stream", json={"question": "本研究中，哪些数据适合进入 sdtm 的 ds domain？"})
        assert r.status_code == 200
        list(r.iter_lines())  # drain the SSE stream
    ev = [e for e in logs if e["event"] == "ask_stream"]
    assert len(ev) == 1
    assert ev[0]["question"].startswith("本研究中")
    assert len(ev[0]["question"]) <= 100
    assert ev[0]["corpus"] == "both"
    assert ev[0]["n_chunks"] == len(ev[0]["chunk_ids"]) > 0
    assert "answer" not in ev[0]
