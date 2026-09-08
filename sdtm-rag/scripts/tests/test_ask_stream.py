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


# ── 输出触顶自动续写 (2026-09-08) ─────────────────────────────────────────
#
# 背景 (真实事故): 一条 ~3.5k 汉字的答案在 ≈4k output token 处**半句话被切断**, 界面
# 上没有任何提示。根因是 `bedrock/converse/...` 这条路径下 litellm 不传 `maxTokens`,
# Bedrock 落到一个远低于模型上限的服务端默认值 (截断本身就是"那不是模型上限"的证据)。
# 两条修法必须同时存在: 显式 max_tokens (把天花板抬到模型真实上限) + 触顶自动续写
# (即便抬高后仍触顶, 也要接着写完, 而不是留半句话)。

from server.router import CONTINUE_PROMPT  # noqa: E402
from scripts.tests.test_ask_stream_web import _events  # noqa: E402


class _ContinueRouter:
    """按脚本逐次调用吐一批 chunk: (正文, finish_reason)。

    形状照抄真实流: 正文片的 finish_reason 是 None, 收尾片才带 finish_reason 且没有
    content, 最后一片是 choices 为空的 usage 片。留存每次调用收到的 messages, 以便断言
    续写轮**真的**回灌了上一轮原文 + CONTINUE_PROMPT (只断"调了两次"挡不住空回灌)。
    """

    def __init__(self, rounds):
        self.rounds = rounds          # list[tuple[str, str | None]]
        self.calls = 0
        self.seen: list[list[dict]] = []

    async def acompletion(self, model, messages, stream=False, **kw):
        self.calls += 1
        self.seen.append([dict(m) for m in messages])
        text, finish = self.rounds[min(self.calls - 1, len(self.rounds) - 1)]

        async def agen():
            yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(
                finish_reason=None,
                delta=SimpleNamespace(content=text, tool_calls=None))])
            yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(
                finish_reason=finish,
                delta=SimpleNamespace(content=None, tool_calls=None))])
            yield SimpleNamespace(model="m", choices=[], usage=SimpleNamespace(
                prompt_tokens=10, completion_tokens=5, total_tokens=15))
        return agen()


def _client_for(router, settings=None):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router
    app.state.settings = settings or Settings()
    return TestClient(app)


def _tokens(evs) -> str:
    return "".join(d.get("text", "") for e, d in evs if e == "token")


def test_length_truncation_auto_continues_and_concatenates():
    router = _ContinueRouter([("first half", "length"), (" second half", "stop")])
    evs = _events(_client_for(router).post(
        "/api/ask_stream", json={"question": "q"}).text)

    assert _tokens(evs) == "first half second half"
    assert router.calls == 2, "触顶后必须自动再开一轮"
    # 续写轮的 messages 尾部 = [assistant(上一轮原文), user(CONTINUE_PROMPT)]。
    # ⛔ 不能只断长度: 回灌成空串时"接着写"没有落点, 模型会从头再写一遍。
    tail = router.seen[1][-2:]
    assert tail[0] == {"role": "assistant", "content": "first half"}
    assert tail[1] == {"role": "user", "content": CONTINUE_PROMPT}
    assert [d for e, d in evs if e == "continue"] == [{"round": 1}]
    done = [d for e, d in evs if e == "done"][0]
    assert done["continue_rounds"] == 1
    assert done["truncated"] is False
    # 每一轮都是一次独立计费的调用 —— usage 必须把续写轮也算进去
    assert done["usage"]["total_tokens"] == 30
    assert done["usage"]["completion_tokens"] == 10


def test_anthropic_style_max_tokens_reason_also_continues():
    """Anthropic 原生报的是 `max_tokens`, OpenAI/litellm 报 `length` —— 两个都算触顶。
    只认 `length` 的话, 走原生 Anthropic 拼法的那条路上截断依旧是静默的。"""
    router = _ContinueRouter([("part1", "max_tokens"), ("part2", "stop")])
    evs = _events(_client_for(router).post(
        "/api/ask_stream", json={"question": "q"}).text)
    assert router.calls == 2
    assert _tokens(evs) == "part1part2"
    assert [d for e, d in evs if e == "done"][0]["continue_rounds"] == 1


def test_continue_rounds_capped_and_reported_as_truncated():
    """永远触顶的模型不能让服务无限续写。到顶就收尾, 并且**如实说**答案可能不完整。"""
    router = _ContinueRouter([("more", "length")])
    evs = _events(_client_for(router, Settings(max_continue_rounds=2)).post(
        "/api/ask_stream", json={"question": "q"}).text)
    assert router.calls == 3          # 首轮 + 2 次续写
    assert [d["round"] for e, d in evs if e == "continue"] == [1, 2]
    done = [d for e, d in evs if e == "done"][0]
    assert done["continue_rounds"] == 2
    assert done["truncated"] is True


def test_normal_stop_does_not_continue():
    """回归: 正常收尾一轮就够, 不发 continue 事件, done 里两个新字段取"没发生"的值。"""
    router = _ContinueRouter([("all done", "stop")])
    evs = _events(_client_for(router).post(
        "/api/ask_stream", json={"question": "q"}).text)
    assert router.calls == 1
    assert not [e for e, _ in evs if e == "continue"]
    done = [d for e, d in evs if e == "done"][0]
    assert done["continue_rounds"] == 0
    assert done["truncated"] is False


# ── 非流式 /api/ask 的同一件事 ────────────────────────────────────────────
#
# 放在本文件是因为它与上面几条共用同一套语义与同一对常量; /api/ask 与 /api/ask_stream
# 是**两份**实现 (同步 completion vs 异步 acompletion, 不共用辅助函数), 所以两边都要有闸
# —— 只测流式的话, eval 脚本 (全走 /api/ask) 会继续静默拿到被截断的答案。

class _SyncContinueRouter:
    def __init__(self, rounds):
        self.rounds = rounds          # list[tuple[str, str | None]]
        self.calls = 0
        self.seen: list[list[dict]] = []

    def completion(self, model, messages, **kw):
        self.calls += 1
        self.seen.append([dict(m) for m in messages])
        text, finish = self.rounds[min(self.calls - 1, len(self.rounds) - 1)]
        return SimpleNamespace(
            model="stub",
            choices=[SimpleNamespace(finish_reason=finish,
                                     message=SimpleNamespace(content=text))],
            usage=SimpleNamespace(prompt_tokens=7, completion_tokens=3, total_tokens=10))


def _ask_json(router, settings=None):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router
    app.state.settings = settings or Settings()
    r = TestClient(app).post("/api/ask", json={"question": "q", "model": "default"})
    assert r.status_code == 200, r.text
    return r.json()


def test_ask_non_stream_auto_continues_on_length():
    router = _SyncContinueRouter([("前半", "length"), ("后半", "stop")])
    j = _ask_json(router)
    assert router.calls == 2
    assert j["answer"] == "前半后半"
    assert j["continue_rounds"] == 1
    assert j["truncated"] is False
    assert j["usage"]["total_tokens"] == 20      # 两轮都计费, 不能只报最后一轮
    tail = router.seen[1][-2:]
    assert tail[0] == {"role": "assistant", "content": "前半"}
    assert tail[1] == {"role": "user", "content": CONTINUE_PROMPT}


def test_ask_non_stream_reports_truncated_at_the_cap():
    router = _SyncContinueRouter([("还没写完", "length")])
    j = _ask_json(router, Settings(max_continue_rounds=1))
    assert router.calls == 2
    assert j["continue_rounds"] == 1
    assert j["truncated"] is True


def test_ask_non_stream_normal_stop_is_one_call():
    """回归: 正常收尾照旧一次调用, 两个新字段取"没发生"的值。"""
    router = _SyncContinueRouter([("完整答案", "stop")])
    j = _ask_json(router)
    assert router.calls == 1
    assert j["answer"] == "完整答案"
    assert j["continue_rounds"] == 0 and j["truncated"] is False
