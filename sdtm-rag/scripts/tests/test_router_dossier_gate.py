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
