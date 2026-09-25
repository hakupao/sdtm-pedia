"""DM2 T5: 接线守两方向 (与 test_pdf_context_wiring 同构):
  ① app.state.dossier is None (总闸 OFF) → messages / sources / done 与引入前逐字节同, dossier 字段 null
  ② 挂上时: study chunks 从 sources 消失, routed=both, context 含包头, system 多且只多一条规则句,
     done/sources/AskResponse 的 dossier.attached=True; auto 未命中时 attached=False 带 reason

Fix round 1 追加的 4 条不变量 (每条都是"改坏了测试才会红"的形状, 不是复述实现):
  I1 补取 CDISC 侧炸了 → 502 (不是 500)
  I2 画面 PDF 通道看**过滤前**的 chunks —— 两条通道并存, 互不知情 (spec §5)
  I3 研读包把 routed 抬成 both 之后, 确定性事实通道 (answerer) 必须仍然跑
  I4 补取那次检索原样透传 domain / file_type / top_k, 席位口径与 federation 的 both 同式
"""
from __future__ import annotations

import json
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.router import _DOSSIER_RULES, api_router
from server.study_dossier import StudyDossier
from server.dossier_trigger import ANSWER_LANGUAGE_LINE

Q_MAP = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"
Q_CDISC = "DS 域有哪些变量？"
# 画面 PDF 通道の R1 を発火させる問い (test_pdf_context_wiring と同型)。
Q_PDF = "この項目はどの visit で表示されますか"

# 偽の field card (実データ由来の OID / label は 1 つも無い)。非表示アクティビティ 2 件で
# R1 のカード側条件を満たす。
CARD = """---
study: st99
version: VNEW
doc_type: field_card
form_oid: FA
field_oid: WX
---

# [偽フォーム FA] WX
- 表示条件: 常時表示
- 非表示アクティビティ: A_ONE, A_TWO
"""


def _chunk(i, corpus, ft="assumptions", text="t"):
    return SimpleNamespace(chunk_id=f"{corpus}{i}", source=f"{corpus}/{i}.md", domain="DS",
                           file_type=ft, section=None, similarity=0.5, text=text, corpus=corpus)


class _Cdisc:
    system_prompt = "SYS"

    def __init__(self):
        self._structured_lookup = SimpleNamespace(
            _query_domains=lambda q: ["DS"] if "ds" in q.lower() else [])
        self.calls = []   # I4: 補取が受け取った検索パラメータ

    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        self.calls.append({"domain": domain, "file_type": file_type, "top_k": top_k})
        return [_chunk(i, "cdisc") for i in range(2)]

    def format_context(self, chunks):
        return "CD:" + ",".join(c.chunk_id for c in chunks)

    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": "SYS"}, *(history or []),
                {"role": "user", "content": f"CTX={ctx}\nQ={q}"}]


class _Fed:
    top_k = 4

    def __init__(self, cdisc):
        self.cdisc = cdisc

    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        return [_chunk(0, "cdisc"), _chunk(1, "cdisc"),
                _chunk(0, "study", "field_card"), _chunk(1, "study", "field_card")], "both"

    def format_context(self, chunks):
        return "FED:" + ",".join(c.chunk_id for c in chunks)

    def build_messages(self, q, ctx, history=None, *, corpus):
        return [{"role": "system", "content": f"SYS[{corpus}]"}, *(history or []),
                {"role": "user", "content": f"CTX={ctx}\nQ={q}"}]


class _Router:
    def __init__(self):
        self.messages = None

    def completion(self, model, messages, **kw):
        self.messages = messages
        return SimpleNamespace(
            model="m",
            choices=[SimpleNamespace(message=SimpleNamespace(content="ans"),
                                     finish_reason="stop")],
            usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1, total_tokens=2))

    async def acompletion(self, model, messages, stream=False, **kw):
        self.messages = messages

        async def agen():
            yield SimpleNamespace(
                model="m", usage=None,
                choices=[SimpleNamespace(delta=SimpleNamespace(content="ans"),
                                         finish_reason="stop")])
        return agen()


class _PdfBuilder:
    """I2: PdfContextBuilder の外形だけ。何枚のカードを見せられたかだけ記録する。

    頁は 1 枚も返さない ⇒ `messages` には触らない (記録以外の副作用が無い)。
    """

    def __init__(self):
        self.cards_seen = None
        self.index = SimpleNamespace(form_named_in=lambda q: None)

    def select_pages(self, cards, question="", max_pages=None):
        self.cards_seen = len(cards)
        return SimpleNamespace(pages=(), omitted=(), truncated=False, max_pages=6)

    def render(self, selection):
        return []

    def to_message_parts(self, selection, images=None):
        return []


DOSSIER = StudyDossier(text="# 【本研究 研読パッケージ】 X", sha="abc", chars=17,
                       sections=("4.1",), n_items=1, study="st99", version="V")


def _client(dossier, enabled=None, auto_attach=True):
    app = FastAPI()
    app.include_router(api_router)
    cd = _Cdisc()
    app.state.rag = cd
    app.state.federation = _Fed(cd)
    app.state.llm_router = _Router()
    app.state.settings = Settings(
        dossier_enabled=(dossier is not None) if enabled is None else enabled,
        dossier_auto_attach=auto_attach)
    app.state.dossier = dossier
    app.state.pdf_context = None
    app.state.study_lookup = None
    app.state.answerer = None
    return TestClient(app), app


def _done(text):
    return json.loads(text.split("event: done\ndata: ")[1].split("\n\n")[0])


def _sources(text):
    return json.loads(text.split("event: sources\ndata: ")[1].split("\n\n")[0])


def _route_study(app, text="t"):
    """federation を study 単庫路由に差し替える (補取経路を通す)。"""
    app.state.federation.retrieve = lambda q, **kw: (
        [_chunk(0, "study", "field_card", text)], "study")


def test_off_is_byte_identical_and_reports_null():
    c, app = _client(None)
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.json()["dossier"] is None
    assert app.state.llm_router.messages == [
        {"role": "system", "content": "SYS[both]"},
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
    assert msgs[-1]["content"] == f"CTX=FED:cdisc0,cdisc1\n\n{DOSSIER.text}\nQ={Q_MAP}\n\n" + ANSWER_LANGUAGE_LINE["zh"]


def test_auto_paused_leaves_messages_alone_but_on_still_attaches():
    c, app = _client(DOSSIER, auto_attach=False)
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.json()["dossier"] == {"attached": False, "reason": "auto:paused", "domains": ["DS"],
                                   "sha": "abc", "sections": ["4.1"], "chars": 17}
    assert app.state.llm_router.messages[0]["content"] == "SYS[both]"
    assert len(r.json()["sources"]) == 4
    on = c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "on"})
    assert on.json()["dossier"]["attached"] is True


def test_default_settings_pause_auto_attach():
    # 2026-09-25 用户裁定: 默认暂停 (DM2 attempt 3 Claude 未达标); 恢复 = 改 config 这一行.
    assert Settings().dossier_auto_attach is False


def test_auto_no_match_reports_reason_and_leaves_messages_alone():
    c, app = _client(DOSSIER)
    r = c.post("/api/ask", json={"question": Q_CDISC, "history": []})
    assert r.json()["dossier"] == {"attached": False, "reason": "auto:no_match", "domains": ["DS"],
                                   "sha": "abc", "sections": ["4.1"], "chars": 17}
    assert app.state.llm_router.messages[0]["content"] == "SYS[both]"
    assert len(r.json()["sources"]) == 4


def test_forced_on_and_off():
    c, _ = _client(DOSSIER)
    on = c.post("/api/ask", json={"question": Q_CDISC, "history": [], "dossier": "on"})
    assert on.json()["dossier"]["reason"] == "forced_on"
    off = c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "off"})
    assert off.json()["dossier"]["reason"] == "forced_off"


def test_bad_mode_is_422():
    c, _ = _client(DOSSIER)
    r = c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "yes"})
    assert r.status_code == 422


def test_study_routed_gets_cdisc_side_refetched():
    c, app = _client(DOSSIER)
    _route_study(app)
    t = c.post("/api/ask_stream", json={"question": Q_MAP, "history": []}).text
    src = _sources(t)
    assert src["routed_corpus"] == "both"
    assert [s["chunk_id"] for s in src["sources"]] == ["cdisc0", "cdisc1"]


# ── Fix round 1 ──────────────────────────────────────────────────────────


def test_refetch_failure_is_502_not_500():
    """I1: 補取も検索 —— 落ちたら 502 (調用側が再試行できる), 500 ではない。"""
    c, app = _client(DOSSIER)
    _route_study(app)

    def _boom(q, **kw):
        raise RuntimeError("chroma down")

    app.state.rag.retrieve = _boom
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.status_code == 502
    assert r.json()["detail"] == "Retrieval service temporarily unavailable."


def test_pdf_channel_sees_prefilter_chunks():
    """I2: 研読包が study chunk を落としても、画面 PDF 通道はそれを見られる。

    過濾後を渡すと cards=0 ⇒ should_attach_pdf の第 1 条で不発 ⇒ select_pages が
    そもそも呼ばれない (cards_seen is None) —— 2 通道の静かな互斥。
    """
    c, app = _client(DOSSIER)
    builder = _PdfBuilder()
    app.state.pdf_context = builder
    app.state.federation.retrieve = lambda q, **kw: (
        [_chunk(0, "cdisc"), _chunk(0, "study", "field_card", CARD),
         _chunk(1, "study", "field_card", CARD)], "both")
    r = c.post("/api/ask", json={"question": Q_PDF, "history": [], "dossier": "on"})
    assert r.json()["dossier"]["attached"] is True
    # context からは study が消えている (研読包側の効果は保たれる)
    assert [s["chunk_id"] for s in r.json()["sources"]] == ["cdisc0"]
    # が、PDF 通道は 2 枚のカードを受け取っている
    assert builder.cards_seen == 2


def test_answerer_runs_on_the_dossier_path():
    """I3: routed が study→both に上がった後の値で answerer の要否を判断する。

    _DOSSIER_RULES 第 ① 歩は「標準から記録類別を列挙」—— その決定的事実通道を、
    もう成立していない「study 単庫」判定で黙らせてはいけない。
    """
    c, app = _client(DOSSIER)
    _route_study(app)
    seen = []
    app.state.answerer = SimpleNamespace(resolve=lambda q: seen.append(q))
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.json()["routed_corpus"] == "both"
    assert seen == [Q_MAP]


def test_refetch_passes_through_domain_file_type_and_top_k():
    """I4: 補取は federation の both と同じ席位式 (ceil(k/2)) と同じ絞り込みで走る。"""
    c, app = _client(DOSSIER)
    _route_study(app)
    c.post("/api/ask", json={"question": Q_MAP, "history": [],
                             "domain": "DS", "file_type": "assumptions"})
    assert app.state.rag.calls == [{"domain": "DS", "file_type": "assumptions", "top_k": 2}]

    c2, app2 = _client(DOSSIER)
    _route_study(app2)
    c2.post("/api/ask", json={"question": Q_MAP, "history": [], "top_k": 6})
    assert app2.state.rag.calls == [{"domain": None, "file_type": None, "top_k": 3}]


def test_master_switch_off_reports_disabled_and_leaves_messages_alone():
    """M4a: 包は組み上がっているが総闸 OFF。「跑了但没挂」を reason で言う。"""
    c, app = _client(DOSSIER, enabled=False)
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.json()["dossier"]["reason"] == "disabled"
    assert r.json()["dossier"]["attached"] is False
    assert app.state.llm_router.messages[0]["content"] == "SYS[both]"
    assert len(r.json()["sources"]) == 4


def test_attaches_on_the_single_corpus_path_too():
    """M4b: federation OFF —— routed は None のまま, それでも研読包は context に入る。"""
    c, app = _client(DOSSIER)
    app.state.federation = None
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.json()["routed_corpus"] is None
    assert r.json()["dossier"]["attached"] is True
    msgs = app.state.llm_router.messages
    assert msgs[0]["content"] == "SYS" + _DOSSIER_RULES
    assert msgs[-1]["content"] == f"CTX=CD:cdisc0,cdisc1\n\n{DOSSIER.text}\nQ={Q_MAP}\n\n" + ANSWER_LANGUAGE_LINE["zh"]


# ── T9 attempt 2: 规则句的内容不变量 ─────────────────────────────────────


def test_rule_pins_category_axis_and_no_candidate_wording():
    """T9 attempt 1 (4/6) 的失败是类别轴混淆: 模型拿 `--SCAT` / 阶段轴顶替类别轴,
    漏掉的那个类别既没列举也没申报无候选 (evidence/failures/dm2_task9_attempt_1.md)。

    修法落在规则层的两处措辞 —— 沿 `--CAT` 轴逐类穷举 + 每类要么给候选要么明写"无候选"。
    措辞不是结构, 下次重写规则句时最容易被顺手抹掉而没人发现, 所以钉在**实际拼进 system
    的那段文本**上 (不只钉常量): 掉了就红。
    """
    c, app = _client(DOSSIER)
    c.post("/api/ask", json={"question": Q_MAP, "history": []})
    appended = app.state.llm_router.messages[0]["content"]
    assert appended.endswith(_DOSSIER_RULES)
    assert "--CAT" in appended
    assert "no candidate" in appended


def test_rule_pins_attempt4_patterns():
    """T9 attempt 3 (evidence/failures/dm2_task9_attempt_3.md) 的四个失败模式各对应一处措辞:
    无 CT / 无 --CAT 的形态声明、CT 原文大写串、OID 全文作用域、答题语言。钉在实际拼进 system
    的文本上 (同上一条的理由); 另钉规则里不得出现具体 CT 取值 —— 那是题面级修法的信号。"""
    c, app = _client(DOSSIER)
    c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "on"})
    appended = app.state.llm_router.messages[0]["content"]
    assert appended.endswith(_DOSSIER_RULES)
    for phrase in ("without controlled terminology", "has no `--CAT` variable",
                   "exact uppercase CT string", "anywhere in the answer",
                   "language of the question", "SUPPQUAL QNAM proposal",
                   # attempt 6 (evidence/failures/dm2_task9_attempt_5.md): 示例值 / 保留语气候选 / 缺席≠不存在
                   "examples and illustrations", "however hedged", "do not claim the standard lacks it"):
        assert phrase in appended, phrase
    for leak in ("DISPOSITION EVENT", "PROTOCOL MILESTONE", "OTHER EVENT", "OTHEVENT"):
        assert leak not in _DOSSIER_RULES, leak
    # 模式级防泄漏: 规则里不得出现双字母域码 (CT 是缩写, 不是域) 或 DS 专属的事件措辞.
    import re
    assert set(re.findall(r"\b[A-Z]{2}\b", _DOSSIER_RULES)) <= {"CT"}
    for leak in ("完了の定義", "中止規準", "status / date / reason"):
        assert leak not in _DOSSIER_RULES, leak


def test_dossier_appends_answer_language_line_to_last_user_message():
    """attempt 4 (evidence/failures/dm2_task9_attempt_4.md): sonnet 两轮 en 问 → ja 答, 规则句措辞压不住
    ⇒ 挂研读包时在**最后一条 user 消息末尾**追加确定的语言指令 (离生成最近, 不在 13 万字日文之前)。
    不挂时 user 消息不得多出任何东西。"""
    from server.dossier_trigger import ANSWER_LANGUAGE_LINE
    c, app = _client(DOSSIER)
    c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "on"})
    last = app.state.llm_router.messages[-1]["content"]
    assert last.endswith(ANSWER_LANGUAGE_LINE["zh"])
    t = c.post("/api/ask_stream", json={"question": Q_MAP, "history": [], "dossier": "on"}).text
    assert app.state.llm_router.messages[-1]["content"].endswith(ANSWER_LANGUAGE_LINE["zh"])
    c2, app2 = _client(DOSSIER)
    c2.post("/api/ask", json={"question": Q_CDISC, "history": []})
    assert not any(v in app2.state.llm_router.messages[-1]["content"]
                   for v in ANSWER_LANGUAGE_LINE.values())


def test_language_line_goes_to_current_question_not_history():
    """审查意见: fake 忽略 history 时 `messages[-1]`→`messages[1]` 的变异测不出来。"""
    c, app = _client(DOSSIER)
    hist = [{"role": "user", "content": "earlier"}, {"role": "assistant", "content": "prev"}]
    c.post("/api/ask", json={"question": Q_MAP, "history": hist, "dossier": "on"})
    msgs = app.state.llm_router.messages
    assert msgs[1] == {"role": "user", "content": "earlier"}
    assert msgs[2] == {"role": "assistant", "content": "prev"}
    assert msgs[-1]["content"].endswith(ANSWER_LANGUAGE_LINE["zh"])


def test_attach_rules_handles_multimodal_last_message():
    """PDF 通道会把 content 变成 parts 列表; 顺序若被对调, `list += str` 会静默逐字符 extend。"""
    from server.router import _attach_dossier_rules
    msgs = [{"role": "system", "content": "S"},
            {"role": "user", "content": [{"type": "text", "text": "Q"}, {"type": "image_url"}]}]
    _attach_dossier_rules(msgs, "In our study, which items go to AE?")
    parts = msgs[-1]["content"]
    assert len(parts) == 2 and parts[0]["text"].endswith(ANSWER_LANGUAGE_LINE["en"])
