"""DM2 研读包答案闸的接线 (spec 2026-09-25-dossier-output-gate-design.md §3).

两个方向:
  ① 研读包没挂 (总闸 OFF / auto 未命中 / auto 暂停) → 两端点输出与引入前**逐字节**相同 (golden 是
     本功能写之前用同一套 fake 录下的, scripts/tests/fixtures/dossier_gate_unattached_golden.json);
  ② 挂上时: 首轮 → 闸 → grounding 事件; 不过 → regenerate 事件 → 第二轮 (反馈 = 运行时数据) → 闸;
     done / AskResponse 带 grounding; 上限 1 次; 闸看续写拼好的整轮; usage 两轮累计;
     /api/ask 只返回最终轮; index 缺失 → 闸不跑、grounding=None、不 500.
⛔ 只用虚构 OID。
"""
from __future__ import annotations

import inspect
import json
from pathlib import Path
from types import SimpleNamespace

from scripts.tests.test_router_dossier_wiring import DOSSIER, Q_MAP, _client
from server import router as router_mod
from server.dossier_gate import OidIndex

GOLDEN = Path(__file__).parent / "fixtures" / "dossier_gate_unattached_golden.json"
IDX = OidIndex(forms=frozenset({"FORM_X"}), items=frozenset({"ITEM_Y1"}))
GOOD = "候选项目：[表单 FORM_X] 登记日 (ITEM_Y1) (推測)"
BAD = "候选项目：[表单 FORM_X] 登记日 (ITEM_Z9) (推測)"


def _usage():
    return SimpleNamespace(prompt_tokens=10, completion_tokens=5, total_tokens=15)


class _ScriptRouter:
    """每次调用按脚本吐一轮 (text, finish_reason); 记下每次收到的 messages。
    脚本元素是异常实例时, 那次调用抛它。"""

    def __init__(self, script):
        self.script = list(script)
        self.calls: list[list[dict]] = []

    def _next(self, messages):
        self.calls.append([dict(m) for m in messages])
        step = self.script.pop(0)
        if isinstance(step, Exception):
            raise step
        return step

    def completion(self, model, messages, **kw):
        text, fr = self._next(messages)
        return SimpleNamespace(
            model="m", usage=_usage(),
            choices=[SimpleNamespace(message=SimpleNamespace(content=text), finish_reason=fr)])

    async def acompletion(self, model, messages, stream=False, **kw):
        text, fr = self._next(messages)

        async def agen():
            yield SimpleNamespace(model="m", usage=None, choices=[
                SimpleNamespace(delta=SimpleNamespace(content=text), finish_reason=fr)])
            yield SimpleNamespace(model="m", usage=_usage(), choices=[])
        return agen()


def _gated_client(script, index=IDX):
    c, app = _client(DOSSIER)
    app.state.llm_router = _ScriptRouter(script)
    if index is not None:
        app.state.dossier_gate_index = index
    return c, app


def _events(text):
    out = []
    for frame in text.split("\n\n"):
        if frame.startswith("event: "):
            head, data = frame.split("\ndata: ", 1)
            out.append((head[len("event: "):], json.loads(data)))
    return out


def _stream(c):
    return _events(c.post("/api/ask_stream", json={"question": Q_MAP, "history": []}).text)


def _ask(c):
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.status_code == 200, r.text
    return r.json()


# ── ① 没挂: 逐字节 ───────────────────────────────────────────────────

def test_unattached_is_byte_identical_to_pre_gate_golden():
    golden = json.loads(GOLDEN.read_text(encoding="utf-8"))
    cases = {"off": dict(dossier=None), "auto_no_match": dict(dossier=DOSSIER),
             "auto_paused": dict(dossier=DOSSIER, auto_attach=False)}
    assert set(cases) == set(golden)
    for name, kw in cases.items():
        c, app = _client(kw.pop("dossier"), **kw)
        app.state.dossier_gate_index = IDX   # index 在也不许动没挂的题
        q = golden[name]["question"]
        assert c.post("/api/ask", json={"question": q, "history": []}).text == golden[name]["ask"], name
        assert (c.post("/api/ask_stream", json={"question": q, "history": []}).text
                == golden[name]["ask_stream"]), name


# ── ② 挂上 ──────────────────────────────────────────────────────────

def test_clean_first_answer_one_call_and_grounding_reported():
    c, app = _gated_client([(GOOD, "stop")])
    ev = _stream(c)
    assert [e for e, _ in ev] == ["sources", "token", "grounding", "done"]
    assert ev[2][1]["ok"] is True
    g = ev[-1][1]["grounding"]
    assert g["regenerated"] is False and g["first"] is None and g["final"]["ok"] is True
    assert len(app.state.llm_router.calls) == 1

    c, app = _gated_client([(GOOD, "stop")])
    body = _ask(c)
    assert body["answer"] == GOOD and body["grounding"]["final"]["ok"] is True
    assert body["grounding"]["regenerated"] is False


def test_failed_first_answer_regenerates_once_with_runtime_feedback():
    c, app = _gated_client([(BAD, "stop"), (GOOD, "stop")])
    ev = _stream(c)
    assert [e for e, _ in ev] == ["sources", "token", "grounding", "regenerate", "token",
                                  "grounding", "done"]
    assert ev[2][1]["ok"] is False and ev[2][1]["unknown_oids"] == ["ITEM_Z9"]
    assert ev[3][1]["reasons"] and "ITEM_Z9" in ev[3][1]["reasons"][0]
    assert ev[4][1]["text"] == GOOD
    done = ev[-1][1]
    assert done["grounding"]["regenerated"] is True
    assert done["grounding"]["final"]["ok"] is True and done["grounding"]["first"]["ok"] is False
    assert done["usage"] == {"prompt_tokens": 20, "completion_tokens": 10, "total_tokens": 30}
    first, second = app.state.llm_router.calls
    assert second[:len(first)] == first
    assert second[len(first)] == {"role": "assistant", "content": BAD}
    assert second[-1]["role"] == "user" and "ITEM_Z9" in second[-1]["content"]
    assert len(second) == len(first) + 2


def test_ask_returns_only_final_round_and_sums_usage():
    c, app = _gated_client([(BAD, "stop"), (GOOD, "stop")])
    body = _ask(c)
    assert body["answer"] == GOOD
    assert body["usage"] == {"prompt_tokens": 20, "completion_tokens": 10, "total_tokens": 30}
    g = body["grounding"]
    assert g["regenerated"] is True and g["first"]["unknown_oids"] == ["ITEM_Z9"]
    assert g["final"]["ok"] is True
    assert app.state.llm_router.calls[1][-1]["role"] == "user"


def test_second_failure_is_reported_not_retried():
    c, app = _gated_client([(BAD, "stop"), (BAD, "stop")])
    done = _stream(c)[-1][1]
    assert done["grounding"]["final"]["ok"] is False and done["grounding"]["regenerated"] is True
    assert len(app.state.llm_router.calls) == 2

    c, app = _gated_client([(BAD, "stop"), (BAD, "stop")])
    assert _ask(c)["grounding"]["final"]["ok"] is False
    assert len(app.state.llm_router.calls) == 2


def test_gate_runs_on_the_continued_whole_answer_not_on_fragments():
    # 捏造 OID 跨续写接缝: 分片上跑闸看不见它
    head, tail = BAD.split("ITEM_Z9")
    script = [(head + "ITEM_", "length"), ("Z9" + tail, "stop"), (GOOD, "stop")]
    c, app = _gated_client(script)
    ev = _stream(c)
    names = [e for e, _ in ev]
    assert names.index("continue") < names.index("grounding") < names.index("regenerate")
    assert ev[names.index("grounding")][1]["unknown_oids"] == ["ITEM_Z9"]
    assert len(app.state.llm_router.calls) == 3

    c, app = _gated_client(list(script))
    body = _ask(c)
    assert body["answer"] == GOOD and body["grounding"]["first"]["unknown_oids"] == ["ITEM_Z9"]


def test_missing_index_skips_gate_without_500():
    c, app = _gated_client([(BAD, "stop")], index=None)
    ev = _stream(c)
    assert [e for e, _ in ev] == ["sources", "token", "done"]
    assert ev[-1][1]["grounding"] is None and ev[-1][1]["dossier"]["attached"] is True
    c, app = _gated_client([(BAD, "stop")], index=None)
    body = _ask(c)
    assert body["answer"] == BAD and body["grounding"] is None
    assert len(app.state.llm_router.calls) == 1


def test_ask_regeneration_call_failure_keeps_first_answer():
    c, app = _gated_client([(BAD, "stop"), RuntimeError("boom")])
    body = _ask(c)
    assert body["answer"] == BAD
    g = body["grounding"]
    assert g["regenerated"] is False and g["final"]["ok"] is False
    assert g["regenerate_error"] == "RuntimeError"


def test_both_endpoints_share_the_one_orchestrator():
    for fn in (router_mod.ask, router_mod.ask_stream):
        src = inspect.getsource(fn)
        assert "_dossier_gate_run(" in src and ".should_regenerate()" in src, fn.__name__


def test_stream_regeneration_open_failure_keeps_first_answer_and_done():
    # 首轮已流给用户; 重答开流就失败时不能以 error 收场 (那样首轮连 done/徽章/存档都丢)。
    # 两个异常: _open_stream 失败后会去掉 stream_options 再开一次。
    c, app = _gated_client([(BAD, "stop"), RuntimeError("boom"), RuntimeError("boom")])
    ev = _stream(c)
    assert [e for e, _ in ev] == ["sources", "token", "grounding", "regenerate", "done"]
    g = ev[-1][1]["grounding"]
    assert g["regenerate_error"] == "RuntimeError" and g["regenerated"] is False
    assert g["final"]["ok"] is False and g["first"] is None
    assert ev[-1][1]["usage"]["total_tokens"] == 15


# ── 审查修正: B1 重答轮任何失败都还原首轮 / N8 预算 / N9 续写计数 / N7 重答 prompt 形状 / B2 info ──

class _MidFailRouter(_ScriptRouter):
    """第 1 次调用吐 BAD; 之后的调用吐半截文本后在流中途 / 同步调用里抛。"""

    async def acompletion(self, model, messages, stream=False, **kw):
        n = len(self.calls)
        self.calls.append([dict(m) for m in messages])

        async def agen():
            if n == 0:
                yield SimpleNamespace(model="m", usage=None, choices=[
                    SimpleNamespace(delta=SimpleNamespace(content=BAD), finish_reason="stop")])
                yield SimpleNamespace(model="m", usage=_usage(), choices=[])
            else:
                yield SimpleNamespace(model="m", usage=None, choices=[
                    SimpleNamespace(delta=SimpleNamespace(content="半截"), finish_reason=None)])
                raise RuntimeError("mid-stream boom")
        return agen()


def test_stream_regeneration_mid_stream_failure_keeps_first_answer_and_done():
    c, app = _gated_client([])
    app.state.llm_router = _MidFailRouter([])
    ev = _stream(c)
    assert [e for e, _ in ev] == ["sources", "token", "grounding", "regenerate", "token", "done"]
    done = ev[-1][1]
    g = done["grounding"]
    assert g["regenerate_error"] == "RuntimeError" and g["regenerated"] is False
    assert g["final"]["unknown_oids"] == ["ITEM_Z9"]
    assert done["usage"]["total_tokens"] == 15 and done["model_used"] == "m"
    assert done["dossier"]["attached"] is True


def test_ask_regeneration_continuation_failure_restores_first_answer():
    head = GOOD[:5]
    c, app = _gated_client([(BAD, "stop"), (head, "length"), RuntimeError("boom")])
    body = _ask(c)
    assert body["answer"] == BAD and body["truncated"] is False and body["continue_error"] is None
    assert body["grounding"]["regenerate_error"] == "RuntimeError"
    assert body["usage"]["total_tokens"] == 30   # 两次成功调用都付过钱


def test_ask_skips_regeneration_when_wall_clock_budget_is_short():
    c, app = _gated_client([(BAD, "stop"), (GOOD, "stop")])
    app.state.settings.request_timeout_s = 1.0   # 剩余 < _CONTINUE_MIN_REMAINING_S
    body = _ask(c)
    assert body["answer"] == BAD and len(app.state.llm_router.calls) == 1
    assert body["grounding"]["regenerate_error"] == "budget"
    assert body["grounding"]["regenerated"] is False


def test_continue_rounds_describe_the_final_round():
    head, tail = BAD.split("ITEM_Z9")
    script = [(head + "ITEM_", "length"), ("Z9" + tail, "stop"), (GOOD, "stop")]
    c, app = _gated_client(list(script))
    assert _stream(c)[-1][1]["continue_rounds"] == 0
    c, app = _gated_client(list(script))
    assert _ask(c)["continue_rounds"] == 0


def test_regeneration_prompt_is_snapshot_plus_first_answer_plus_feedback():
    # MUT2: 首轮有续写 —— 重答 prompt 里不许混进 CONTINUE_PROMPT / 续写回灌
    head, tail = BAD.split("ITEM_Z9")
    script = [(head + "ITEM_", "length"), ("Z9" + tail, "stop"), (GOOD, "stop")]
    for call in (_stream, _ask):
        c, app = _gated_client(list(script))
        call(c)
        first, _, regen = app.state.llm_router.calls
        assert regen == [*first, {"role": "assistant", "content": BAD}, regen[-1]]
        assert regen[-1]["role"] == "user" and "ITEM_Z9" in regen[-1]["content"]
        assert all(router_mod.CONTINUE_PROMPT not in str(m["content"]) for m in regen)


class _ToolThenTextScript(_ScriptRouter):
    """首轮: 先要一次 web_search, 再吐 BAD; 重答: GOOD。"""

    async def acompletion(self, model, messages, stream=False, **kw):
        n = len(self.calls)
        self.calls.append([dict(m) for m in messages])

        async def agen():
            if n == 0:
                yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(
                    finish_reason="tool_calls", delta=SimpleNamespace(content=None, tool_calls=[
                        SimpleNamespace(index=0, id="t1", function=SimpleNamespace(
                            name="web_search", arguments='{"query": "q"}'))]))])
            else:
                text = BAD if n == 1 else GOOD
                yield SimpleNamespace(model="m", usage=None, choices=[
                    SimpleNamespace(delta=SimpleNamespace(content=text, tool_calls=None),
                                    finish_reason="stop")])
        return agen()


def test_regeneration_prompt_carries_no_tool_rounds(monkeypatch):
    from scripts.tests.test_ask_stream_web import _FakeSearcher
    monkeypatch.setattr("server.router.WebSearcher", _FakeSearcher)
    c, app = _gated_client([])
    app.state.llm_router = _ToolThenTextScript([])
    app.state.settings.web_search_enabled = True
    ev = _events(c.post("/api/ask_stream",
                        json={"question": Q_MAP, "history": [], "web": True}).text)
    assert "regenerate" in [e for e, _ in ev]
    first, _, regen = app.state.llm_router.calls[:3]
    assert regen[:len(first)] == first and len(regen) == len(first) + 2
    assert all(m["role"] != "tool" and "tool_calls" not in m for m in regen)


def test_info_reports_whether_the_gate_is_available():
    from scripts.tests.test_model_switching import _info_client
    c = _info_client()
    assert c.get("/api/info").json()["dossier_gate"] is False
    c.app.state.dossier_gate_index = IDX
    assert c.get("/api/info").json()["dossier_gate"] is True


# ── 复审第二轮: 还原首轮时 model/usage/计数闸修正都要对 ──

class _ModelMidFail(_MidFailRouter):
    """首轮由 m1 答; 重答由 m2 开始吐字后中途炸。"""

    async def acompletion(self, model, messages, stream=False, **kw):
        n = len(self.calls)
        self.calls.append([dict(m) for m in messages])

        async def agen():
            if n == 0:
                yield SimpleNamespace(model="m1", usage=None, choices=[
                    SimpleNamespace(delta=SimpleNamespace(content=BAD), finish_reason="stop")])
                yield SimpleNamespace(model="m1", usage=_usage(), choices=[])
            else:
                yield SimpleNamespace(model="m2", usage=None, choices=[
                    SimpleNamespace(delta=SimpleNamespace(content="半截"), finish_reason=None)])
                raise RuntimeError("mid-stream boom")
        return agen()


def test_stream_regen_failure_restores_models_and_marks_usage_partial():
    c, app = _gated_client([])
    app.state.llm_router = _ModelMidFail([])
    done = _stream(c)[-1][1]
    assert done["model_used"] == "m1" and done["models_used"] == ["m1"]
    assert done["usage"]["partial"] is True and done["usage"]["total_tokens"] == 15


def _with_counting_gate(monkeypatch, app):
    """确定性计数闸打桩: 任何答案都补一段修正。"""
    import server.grounding as gr
    import server.structured_answer as sa
    app.state.answerer = SimpleNamespace(resolve=lambda q: object())
    monkeypatch.setattr(sa, "augment_context", lambda facts, ctx: ctx)
    monkeypatch.setattr(gr, "apply_counting_gate",
                        lambda ans, facts: (ans + "〔计数修正〕", [{"v": 1}]))


def test_stream_regen_failure_carries_counting_correction_in_done(monkeypatch):
    c, app = _gated_client([])
    app.state.llm_router = _MidFailRouter([])
    _with_counting_gate(monkeypatch, app)
    done = _stream(c)[-1][1]
    assert done["grounding"]["regenerate_error"] == "RuntimeError"
    assert done["counting_correction"] == "〔计数修正〕"


def test_stream_counting_correction_not_in_done_without_regen_failure(monkeypatch):
    c, app = _gated_client([(BAD, "stop"), (GOOD, "stop")])
    _with_counting_gate(monkeypatch, app)
    assert "counting_correction" not in _stream(c)[-1][1]


def test_ask_regen_failure_keeps_counting_correction(monkeypatch):
    c, app = _gated_client([(BAD, "stop"), RuntimeError("boom")])
    _with_counting_gate(monkeypatch, app)
    assert _ask(c)["answer"] == BAD + "〔计数修正〕"


def test_grounding_payload_keys_match_the_frontend_shape_constant():
    """前端在中断时自己合成 grounding (js/grounding.js interruptedGrounding); 形状必须与后端
    GateRun.payload() 同步 —— 两边各写一份键名, 这条把它们钉在一起。"""
    import re as _re

    from server.dossier_gate import GateRun
    js = (Path(__file__).resolve().parents[2] / "webchat" / "js" / "grounding.js").read_text(
        encoding="utf-8")
    keys = set(_re.findall(r'"(\w+)"', js.split("GROUNDING_KEYS = [", 1)[1].split("]", 1)[0]))
    g = GateRun(IDX, Q_MAP)
    g.observe(BAD)
    g.regeneration_failed("interrupted")
    assert keys == set(g.payload())
