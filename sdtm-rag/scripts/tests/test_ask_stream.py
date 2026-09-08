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


# ── 空轮: 一个可见字都没吐就触顶 (2026-09-08 探针实测) ────────────────────
#
# 实测 (.superpowers/probe_e2e_continue.py, 真 Bedrock + opus-5, 天花板压到 200/1200):
# 某一轮的预算可能被模型的内部思考吃光, 于是 delta.content 一个字都没有却报 length。
# 此时按"回灌 assistant(本轮原文)"照做, 回灌的就是 `assistant: ""` ——
#   · litellm 当场警告 "Potential consecutive user/tool blocks. Trying to merge.",
#     把这条空消息丢掉并把相邻的两条 user 合并;
#   · 模型于是收到一句"从断处接着写", 却**没有任何可接的东西**, 只能凭空编一个续写点。
#     实测产物就是从一个中段小标题 ("### Timing variables and the temporal anchoring
#     of measurements") 开始写 —— 一篇没有开头的文章。
# 正确做法: 没吐字就**不加锚**, 用同样的 msgs 再开一轮 (预算刷新)。

class _EmptyThenTextRouter:
    """第 1 轮只有 finish_reason=length、没有任何 content; 第 2 轮正常出文本。"""

    def __init__(self):
        self.calls = 0
        self.seen: list[list[dict]] = []

    async def acompletion(self, model, messages, stream=False, **kw):
        self.calls += 1
        self.seen.append([dict(m) for m in messages])
        first = self.calls == 1

        async def agen():
            if first:
                yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(
                    finish_reason="length",
                    delta=SimpleNamespace(content=None, tool_calls=None))])
            else:
                yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(
                    finish_reason="stop",
                    delta=SimpleNamespace(content="真正的开头", tool_calls=None))])
        return agen()


def test_empty_round_retries_without_an_empty_anchor():
    router = _EmptyThenTextRouter()
    evs = _events(_client_for(router).post(
        "/api/ask_stream", json={"question": "q"}).text)

    assert router.calls == 2
    # ⛔ 第 2 轮的 messages 必须与第 1 轮**逐字相同**: 既没有 `assistant: ""`,
    # 也没有失去落点的 CONTINUE_PROMPT。
    assert router.seen[1] == router.seen[0], router.seen[1]
    assert all(m.get("content") != "" for m in router.seen[1])
    assert CONTINUE_PROMPT not in json.dumps(router.seen[1], ensure_ascii=False)
    # 仍然算一轮续写 (它确实多花了一次调用), 用户看到的正文是完整的开头
    assert [d for e, d in evs if e == "continue"] == [{"round": 1}]
    assert _tokens(evs) == "真正的开头"
    done = [d for e, d in evs if e == "done"][0]
    assert done["continue_rounds"] == 1 and done["truncated"] is False


def test_ask_non_stream_empty_round_retries_without_an_empty_anchor():
    """/api/ask 同一件事 (两份实现, 两边都要挡)。"""
    router = _SyncContinueRouter([("", "length"), ("真正的开头", "stop")])
    j = _ask_json(router)
    assert router.calls == 2
    assert router.seen[1] == router.seen[0], router.seen[1]
    assert j["answer"] == "真正的开头"
    assert j["continue_rounds"] == 1 and j["truncated"] is False


# ── 复审第 1 轮修正 (2026-09-08) ──────────────────────────────────────────

def test_finish_reason_survives_a_trailing_choices_chunk():
    """m1: `finish_reason` 取**最后一个非 None**, 裸赋值会被收尾片之后的尾片抹回 None。

    ⚠ 初版注释把危险说成"usage 片的 finish_reason 缺失会抹回 None" —— 那个理由**不成立**:
    读取点在 `if choices:` 里面, 而 usage 片的 choices 是空列表, 根本进不来。守卫本身是对的,
    防的是**带 choices 的尾片**: 有 provider 在收尾片之后还会再发一两片 (空 content、
    finish_reason=None)。这条测试用的正是那个形状 —— 独立复审实测裸赋值时 39 条全绿,
    即这道守卫此前零覆盖。
    """
    class _TrailingChunkRouter:
        def __init__(self):
            self.calls = 0

        async def acompletion(self, model, messages, stream=False, **kw):
            self.calls += 1
            first = self.calls == 1

            async def agen():
                yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(
                    finish_reason=None,
                    delta=SimpleNamespace(content="前半", tool_calls=None))])
                yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(
                    finish_reason="length" if first else "stop",
                    delta=SimpleNamespace(content=None, tool_calls=None))])
                # 收尾片**之后**还有一片带 choices 的尾片 —— 裸赋值会在这里把理由抹成 None
                yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(
                    finish_reason=None,
                    delta=SimpleNamespace(content=None, tool_calls=None))])
            return agen()

    router = _TrailingChunkRouter()
    evs = _events(_client_for(router).post("/api/ask_stream", json={"question": "q"}).text)
    assert router.calls == 2, "尾片把触顶理由抹掉了 ⇒ 截断重新变回静默"
    assert [d for e, d in evs if e == "continue"] == [{"round": 1}]


class _SlowSyncRouter:
    """每次调用真睡一小会儿, 用来验非流式的**总**时长预算 (不是每次调用的预算)。"""

    def __init__(self, sleep_s: float = 0.05):
        self.sleep_s = sleep_s
        self.calls = 0

    def completion(self, model, messages, **kw):
        import time as _t
        self.calls += 1
        _t.sleep(self.sleep_s)
        return SimpleNamespace(
            model="stub",
            choices=[SimpleNamespace(finish_reason="length",
                                     message=SimpleNamespace(content=f"片{self.calls}"))],
            usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1, total_tokens=2))


def test_ask_non_stream_stops_continuing_when_the_time_budget_runs_out():
    """I-1: `/api/ask` 的续写必须受**整次请求**的墙钟预算约束, 而不是只受轮数约束。

    ⚠ 病因: `Router(timeout=120)` 是**每次调用**的上限, 不是整次请求的。最坏 (1+8) 轮 ⇒
    单个 HTTP 请求可以占用十几分钟, 而唯一的真实客户端 `ui/streamlit_app.py` 只等 120 秒
    —— 用户拿到 ReadTimeout, 服务端**仍在为一条没人接的请求烧钱**。
    (流式那边没有这个问题: token 一直在流, 客户端不会判超时。)

    预算取 `request_timeout_s`; 剩余不足 `_CONTINUE_MIN_REMAINING_S` 就收尾并**如实**
    报 truncated —— 已经拿到的正文照常返回, 不丢。
    """
    from server.router import _CONTINUE_MIN_REMAINING_S

    router = _SlowSyncRouter()
    # 预算刚好比"续写所需的最小剩余"多一点点: 第 1 轮睡掉 0.05s 后剩余必然 < 门槛 ⇒ 收手
    s = Settings(request_timeout_s=_CONTINUE_MIN_REMAINING_S + 0.02, max_continue_rounds=8)
    j = _ask_json(router, s)
    assert router.calls == 1, f"预算已尽却还在续写: {router.calls} 次调用"
    assert j["truncated"] is True
    assert j["answer"] == "片1", "收手不等于丢内容 —— 已拿到的正文必须照常返回"


def test_ask_non_stream_keeps_continuing_while_the_budget_allows():
    """上一条的对照: 预算充足时轮数上限仍是唯一的收手理由 (否则那条闸恒真)。"""
    router = _SlowSyncRouter()
    j = _ask_json(router, Settings(request_timeout_s=180.0, max_continue_rounds=2))
    assert router.calls == 3
    assert j["continue_rounds"] == 2 and j["truncated"] is True


class _FailOnRoundRouter:
    """第 fail_on 次调用抛异常, 之前的调用正常返回被截断的文本。"""

    def __init__(self, fail_on: int):
        self.fail_on = fail_on
        self.calls = 0

    def completion(self, model, messages, **kw):
        self.calls += 1
        if self.calls == self.fail_on:
            raise RuntimeError("provider exploded")
        return SimpleNamespace(
            model="stub",
            choices=[SimpleNamespace(finish_reason="length",
                                     message=SimpleNamespace(content=f"片{self.calls}"))],
            usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1, total_tokens=2))


def _ask_raw(router, settings=None):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router
    app.state.settings = settings or Settings()
    return TestClient(app).post("/api/ask", json={"question": "q", "model": "default"})


def test_ask_non_stream_continuation_failure_keeps_what_was_written():
    """I-5: 续写轮抛异常 ⇒ 200 + 已拿到的正文 + truncated + continue_error, ⛔ 不是 502。

    这是一次**没被记录的行为变更**: 引入续写之前, 一次成功但被截断的调用返回 200 +
    半截答案; 引入之后, 第 1 轮成功、第 2 轮失败会变成 502 什么都没有 —— 「本来能拿到
    半篇」退化成「什么都拿不到」。
    """
    router = _FailOnRoundRouter(fail_on=2)
    r = _ask_raw(router)
    assert r.status_code == 200, f"续写失败不该吃掉第 1 轮的正文: {r.text[:200]}"
    j = r.json()
    assert j["answer"] == "片1"
    assert j["truncated"] is True
    assert j["continue_error"] == "RuntimeError"
    assert j["continue_rounds"] == 1


def test_ask_non_stream_first_round_failure_is_still_502():
    """对照: 第 1 轮就失败仍是 502 —— 没有任何内容时返 200 等于把失败伪装成空答案。"""
    r = _ask_raw(_FailOnRoundRouter(fail_on=1))
    assert r.status_code == 502


def test_ask_non_stream_usage_marks_partial_when_a_round_lacks_usage():
    """m2: 与流式同口径。少加一轮却呈现成一个看起来完整的总量, 就是**低报成本**。"""
    class _MixedUsageRouter:
        def __init__(self):
            self.calls = 0

        def completion(self, model, messages, **kw):
            self.calls += 1
            first = self.calls == 1
            return SimpleNamespace(
                model="stub",
                choices=[SimpleNamespace(finish_reason="length" if first else "stop",
                                         message=SimpleNamespace(content=f"片{self.calls}"))],
                usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1, total_tokens=2)
                if first else None)

    j = _ask_json(_MixedUsageRouter())
    assert j["usage"]["total_tokens"] == 2
    assert j["usage"]["partial"] is True


def test_streamlit_consumer_reads_the_truncation_fields():
    """I-3(c): `/api/ask` 的**唯一真实消费者**必须真的读 `truncated`。

    复审抓到的形状: 服务端老老实实报了 `truncated`, 而 `ui/streamlit_app.py` 只读
    `answer`/`sources`/`usage`/`model_used` ⇒ 在那条路上"截断依旧不可见", 正是本功能
    要消灭的失败模式。字段发了没人读 = 没做。

    断的是**带点的属性/键访问**形状 (`.get("truncated")`), 不是"这个词在文件里出现过"
    —— 注释里提一嘴不算兑现 (与 test_sse_contract 的 `.web_status` 同款理由)。
    """
    import re
    from pathlib import Path

    src = (Path(__file__).resolve().parents[2] / "ui" / "streamlit_app.py").read_text(
        encoding="utf-8")
    for field in ("truncated", "continue_rounds"):
        assert re.search(rf'\.get\(\s*["\']{field}["\']', src), \
            f"streamlit_app.py 没有以 .get({field!r}) 形式读取该字段"
