"""DM2 T5: 接线守两方向 (与 test_pdf_context_wiring 同构):
  ① app.state.dossier is None (总闸 OFF) → messages / sources / done 与引入前逐字节同, dossier 字段 null
  ② 挂上时: study chunks 从 sources 消失, routed=both, context 含包头, system 多且只多一条规则句,
     done/sources/AskResponse 的 dossier.attached=True; auto 未命中时 attached=False 带 reason
"""
from __future__ import annotations
import json
from types import SimpleNamespace
from fastapi import FastAPI
from fastapi.testclient import TestClient
from server.config import Settings
from server.router import _DOSSIER_RULES, api_router
from server.study_dossier import StudyDossier

Q_MAP = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"
Q_CDISC = "DS 域有哪些变量？"


def _chunk(i, corpus, ft="assumptions"):
    return SimpleNamespace(chunk_id=f"{corpus}{i}", source=f"{corpus}/{i}.md", domain="DS",
                           file_type=ft, section=None, similarity=0.5, text="t", corpus=corpus)


class _Cdisc:
    system_prompt = "SYS"
    def __init__(self): self._structured_lookup = SimpleNamespace(_query_domains=lambda q: ["DS"] if "ds" in q.lower() else [])
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None): return [_chunk(i, "cdisc") for i in range(2)]
    def format_context(self, chunks): return "CD:" + ",".join(c.chunk_id for c in chunks)
    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": "SYS"}, {"role": "user", "content": f"CTX={ctx}\nQ={q}"}]


class _Fed:
    top_k = 4
    def __init__(self, cdisc): self.cdisc = cdisc
    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        return [_chunk(0, "cdisc"), _chunk(1, "cdisc"), _chunk(0, "study", "field_card"), _chunk(1, "study", "field_card")], "both"
    def format_context(self, chunks):
        return "FED:" + ",".join(c.chunk_id for c in chunks)
    def build_messages(self, q, ctx, history=None, *, corpus):
        return [{"role": "system", "content": f"SYS[{corpus}]"}, {"role": "user", "content": f"CTX={ctx}\nQ={q}"}]


class _Router:
    def __init__(self): self.messages = None
    def completion(self, model, messages, **kw):
        self.messages = messages
        return SimpleNamespace(model="m", choices=[SimpleNamespace(message=SimpleNamespace(content="ans"), finish_reason="stop")],
                               usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1, total_tokens=2))
    async def acompletion(self, model, messages, stream=False, **kw):
        self.messages = messages
        async def agen():
            yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(delta=SimpleNamespace(content="ans"), finish_reason="stop")])
        return agen()


DOSSIER = StudyDossier(text="# 【本研究 研読パッケージ】 X", sha="abc", chars=17, sections=("4.1",), n_items=1, study="st99", version="V")


def _client(dossier):
    app = FastAPI(); app.include_router(api_router)
    cd = _Cdisc()
    app.state.rag = cd; app.state.federation = _Fed(cd); app.state.llm_router = _Router()
    app.state.settings = Settings(dossier_enabled=dossier is not None)
    app.state.dossier = dossier; app.state.pdf_context = None; app.state.study_lookup = None
    app.state.answerer = None
    return TestClient(app), app


def _done(text):
    return json.loads(text.split("event: done\ndata: ")[1].split("\n\n")[0])

def _sources(text):
    return json.loads(text.split("event: sources\ndata: ")[1].split("\n\n")[0])


def test_off_is_byte_identical_and_reports_null():
    c, app = _client(None)
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.json()["dossier"] is None
    assert app.state.llm_router.messages == [{"role": "system", "content": "SYS[both]"},
                                              {"role": "user", "content": f"CTX=FED:cdisc0,cdisc1,study0,study1\nQ={Q_MAP}"}]
    t = c.post("/api/ask_stream", json={"question": Q_MAP, "history": []}).text
    assert _done(t)["dossier"] is None and _sources(t)["dossier"] is None
    assert len(_sources(t)["sources"]) == 4


def test_auto_attach_drops_study_chunks_and_adds_rule_once():
    c, app = _client(DOSSIER)
    t = c.post("/api/ask_stream", json={"question": Q_MAP, "history": []}).text
    src = _sources(t)
    assert [s["chunk_id"] for s in src["sources"]] == ["cdisc0", "cdisc1"]
    assert src["routed_corpus"] == "both"
    assert src["dossier"] == {"attached": True, "reason": "auto:domain+scope", "domains": ["DS"],
                              "sha": "abc", "sections": ["4.1"], "chars": 17}
    assert _done(t)["dossier"]["attached"] is True
    msgs = app.state.llm_router.messages
    assert msgs[0]["content"] == "SYS[both]" + _DOSSIER_RULES
    assert msgs[0]["content"].count(_DOSSIER_RULES) == 1
    assert msgs[-1]["content"] == f"CTX=FED:cdisc0,cdisc1\n\n{DOSSIER.text}\nQ={Q_MAP}"


def test_auto_no_match_reports_reason_and_leaves_messages_alone():
    c, app = _client(DOSSIER)
    r = c.post("/api/ask", json={"question": Q_CDISC, "history": []})
    assert r.json()["dossier"] == {"attached": False, "reason": "auto:no_match", "domains": ["DS"],
                                   "sha": "abc", "sections": ["4.1"], "chars": 17}
    assert app.state.llm_router.messages[0]["content"] == "SYS[both]"
    assert len(r.json()["sources"]) == 4


def test_forced_on_and_off():
    c, _ = _client(DOSSIER)
    assert c.post("/api/ask", json={"question": Q_CDISC, "history": [], "dossier": "on"}).json()["dossier"]["reason"] == "forced_on"
    assert c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "off"}).json()["dossier"]["reason"] == "forced_off"


def test_bad_mode_is_422():
    c, _ = _client(DOSSIER)
    assert c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "yes"}).status_code == 422


def test_study_routed_gets_cdisc_side_refetched():
    c, app = _client(DOSSIER)
    app.state.federation.retrieve = lambda q, **kw: ([_chunk(0, "study", "field_card")], "study")
    t = c.post("/api/ask_stream", json={"question": Q_MAP, "history": []}).text
    src = _sources(t)
    assert src["routed_corpus"] == "both"
    assert [s["chunk_id"] for s in src["sources"]] == ["cdisc0", "cdisc1"]
