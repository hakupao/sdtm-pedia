"""I2-3: 接線 (`/api/ask` + `/api/ask_stream` + 起動時装配)。

守るのは 2 方向:
  ① 開関 OFF (既定) では `messages` が本機能導入前と**逐位同一**である
  ② 開関 ON で発火したときだけ、user メッセージが content parts になり、
     system prompt に出典分離の 1 文が付き、done 事件が何頁付けたかを言う
"""
from __future__ import annotations

import asyncio
import json
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from server import main as main_mod
from server.config import Settings
from server.pdf_context import ImagePart, PageRef, PageSelection
from server.router import api_router

CARD = """---
study: st99
version: VNEW
doc_type: field_card
form_oid: FA
field_oid: {item}
---

# [偽フォーム FA] {item}
- 表示条件: 常時表示
- 非表示アクティビティ: A_ONE, A_TWO
"""
Q_FIRES = "この項目はどの visit で表示されますか"
Q_QUIET = "この項目の型は何ですか"


class _FakeRAG:
    def __init__(self, texts):
        self.texts = texts
        self.via_lookup = False   # S2 直查で union-add されたか (R3 のフロアが見る)

    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return [SimpleNamespace(chunk_id=f"c{i}", source=f"st99__FA__I{i}.md", domain="FA",
                                file_type="field_card", section="FA", similarity=0.9, text=t,
                                via_lookup=self.via_lookup)
                for i, t in enumerate(self.texts)]

    def format_context(self, chunks):
        return "CTX"

    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": "SYS"}, {"role": "user", "content": f"U:{q}"}]


class _FakeBuilder:
    """本物の PdfContextBuilder の外形だけ (描画は I2-2 側でテスト済み)。

    `n_rendered` で「選んだけれど描画できなかった」を作れる —— 報告すべきは選んだ頁では
    なく**付いた頁** (M3)。
    """

    def __init__(self, n_rendered: int | None = None, form_named: str | None = None):
        self.calls = []
        self.n_rendered = n_rendered
        # r3b: 接線は builder の索引に「問いがフォームを名指ししたか」を訊く
        self.index = SimpleNamespace(form_named_in=lambda q: form_named)

    def select_pages(self, cards, question="", max_pages=None):
        self.calls.append((len(cards), question))
        return PageSelection(
            pages=(PageRef("annotated", 174, "【画面 annotated p.174】", "item"),
                   PageRef("workflow", 315, "【画面 workflow p.315】", "shows")),
            omitted=(), truncated=False, max_pages=6)

    def render(self, selection):
        n = len(selection.pages) if self.n_rendered is None else self.n_rendered
        return [ImagePart(p.pdf, p.page, p.label, "AAA") for p in selection.pages[:n]]

    def to_message_parts(self, selection, images=None):
        imgs = self.render(selection) if images is None else images
        parts = []
        for i in imgs:
            parts.append({"type": "text", "text": i.label})
            parts.append({"type": "image_url",
                          "image_url": {"url": f"data:image/png;base64,{i.b64}"}})
        return parts


class _CaptureRouter:
    def __init__(self):
        self.messages = None

    def completion(self, model, messages, **kw):
        self.messages = messages
        return SimpleNamespace(
            model="m", choices=[SimpleNamespace(
                message=SimpleNamespace(content="ans"), finish_reason="stop")],
            usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1, total_tokens=2))

    async def acompletion(self, model, messages, stream=False, **kw):
        self.messages = messages

        async def agen():
            yield SimpleNamespace(model="m", usage=None,
                                  choices=[SimpleNamespace(
                                      delta=SimpleNamespace(content="ans"), finish_reason="stop")])
        return agen()


_DEFAULT_TEXTS = (CARD.format(item="WX"), CARD.format(item="KX"))


def _client(pdf_context=None, texts=_DEFAULT_TEXTS, study_lookup=None):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG(list(texts))
    app.state.llm_router = _CaptureRouter()
    app.state.settings = Settings()
    app.state.pdf_context = pdf_context
    app.state.study_lookup = study_lookup
    return TestClient(app), app


# ── ① OFF ──────────────────────────────────────────────────────────────
def test_messages_are_untouched_when_the_channel_is_off():
    c, app = _client(pdf_context=None)
    r = c.post("/api/ask", json={"question": Q_FIRES, "history": []})
    assert r.status_code == 200
    assert app.state.llm_router.messages == [
        {"role": "system", "content": "SYS"}, {"role": "user", "content": f"U:{Q_FIRES}"}]
    assert r.json()["pdf_pages"] is None and r.json()["pdf_trigger"] is None


def test_stream_done_reports_nulls_when_the_channel_is_off():
    c, _ = _client(pdf_context=None)
    body = c.post("/api/ask_stream", json={"question": Q_FIRES, "history": []}).text
    done = json.loads(body.split("event: done\ndata: ")[1].split("\n\n")[0])
    assert done["pdf_trigger"] is None and done["pdf_pages"] is None


def test_state_attribute_absent_is_treated_as_off():
    """`app.state.pdf_context` を設定しない古い組み立て方 (テスト用アプリ等) でも
    落ちないこと —— getattr の既定値が効いているかを実際に確かめる。"""
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG([CARD.format(item="WX")])
    app.state.llm_router = _CaptureRouter()
    app.state.settings = Settings()
    r = TestClient(app).post("/api/ask", json={"question": Q_FIRES, "history": []})
    assert r.status_code == 200 and r.json()["pdf_pages"] is None


# ── ② ON ───────────────────────────────────────────────────────────────
def test_fired_request_turns_the_user_message_into_content_parts():
    b = _FakeBuilder()
    c, app = _client(pdf_context=b)
    r = c.post("/api/ask", json={"question": Q_FIRES, "history": []})
    msgs = app.state.llm_router.messages
    assert isinstance(msgs[-1]["content"], list)
    assert msgs[-1]["content"][0] == {"type": "text", "text": f"U:{Q_FIRES}"}
    assert any(p["type"] == "image_url" for p in msgs[-1]["content"])
    assert r.json()["pdf_pages"] == [{"pdf": "annotated", "page": 174},
                                     {"pdf": "workflow", "page": 315}]
    assert r.json()["pdf_trigger"] == "R1"


def test_fired_request_adds_exactly_one_source_separation_rule():
    b = _FakeBuilder()
    c, app = _client(pdf_context=b)
    c.post("/api/ask", json={"question": Q_FIRES, "history": []})
    sys_prompt = app.state.llm_router.messages[0]["content"]
    assert sys_prompt.startswith("SYS")
    assert sys_prompt.count("画面目視判読") == 1


def test_fired_request_limits_negative_claims_to_the_attached_pages():
    """N1: 添付頁は各ブロックの一部。label だけに書いても、「無い」と言い切る前に
    範囲を限定する義務は規則側に無いと効かない (V3 T3/T6 の同型 contradiction)。"""
    c, app = _client(pdf_context=_FakeBuilder())
    c.post("/api/ask", json={"question": Q_FIRES, "history": []})
    sys_prompt = app.state.llm_router.messages[0]["content"]
    assert "添付頁" in sys_prompt and "範囲では" in sys_prompt
    # 限定が掛かるのは画面由来の否定だけ。カード事実まで濁らせると、T1④/T5③ 型の
    # 「この活動では出ない」という**正解**が hedge に化ける。
    assert "に基づく否定は画面由来ではない" in sys_prompt
    assert sys_prompt.count("画面目視判読") == 1


def test_the_rule_says_index_metadata_is_not_something_read_off_the_image():
    """N3 (b): label の「頁索引メタ:」以降は索引が持っている事実であって、画像から
    読み取ったものではない。N2 起源の 3 件はこれを画像由来の出典で引用していた
    (底の事実は正しいのに、頁にはその注記が無い)。"""
    c, app = _client(pdf_context=_FakeBuilder())
    c.post("/api/ask", json={"question": Q_FIRES, "history": []})
    sys_prompt = app.state.llm_router.messages[0]["content"]
    assert "頁索引メタ" in sys_prompt and "『頁索引』" in sys_prompt
    # 枠 (パネル) の境界 = グループ境界、見出しの無い枠も 1 つと数える (N3 (a) の起源)
    assert "項目グループ順" in sys_prompt and "枠" in sys_prompt
    # 複審 MAJOR-1: 続き枠の見出しは前頁にしか無い。label が印を付けても、それが
    # 「本頁に見出しが無い」を意味することは規則側で言わないと伝わらない。
    assert "前頁からの続き" in sys_prompt and "本頁には見出しが描画されていない" in sys_prompt
    # 出典名は 1 つだけ。規則が増えるたびに出典名が増えると、モデルは画像を見ずに
    # 「それらしい出典名」を選べるようになる。
    assert sys_prompt.count("画面目視判読") == 1


def test_a_quiet_question_leaves_everything_alone_even_with_the_channel_on():
    """通道 ON でも、規則に当たらない問いでは 1 バイトも変わらない —— 反例集
    (P1 §2) が守っているのはこの性質。"""
    b = _FakeBuilder()
    c, app = _client(pdf_context=b)
    r = c.post("/api/ask", json={"question": Q_QUIET, "history": []})
    assert app.state.llm_router.messages[-1]["content"] == f"U:{Q_QUIET}"
    assert b.calls == [] and r.json()["pdf_trigger"] is None


def test_stream_done_reports_the_attached_pages():
    c, _ = _client(pdf_context=_FakeBuilder())
    body = c.post("/api/ask_stream", json={"question": Q_FIRES, "history": []}).text
    done = json.loads(body.split("event: done\ndata: ")[1].split("\n\n")[0])
    assert done["pdf_trigger"] == "R1"
    assert done["pdf_pages"][1] == {"pdf": "workflow", "page": 315}


def test_render_failure_degrades_to_no_attachment_not_a_500():
    """pdftoppm が消えた本番機でも答えは返る (画像が付かないだけ)。"""
    c, app = _client(pdf_context=_FakeBuilder(n_rendered=0))
    r = c.post("/api/ask", json={"question": Q_FIRES, "history": []})
    assert r.status_code == 200
    assert app.state.llm_router.messages[-1]["content"] == f"U:{Q_FIRES}"
    # M4: 発火はした。None にすると「規則に当たらなかった」と区別が付かず、
    # 「なぜ画面が付かないのか」を後から切り分けられない。
    assert r.json()["pdf_trigger"] == "R1" and r.json()["pdf_pages"] == []


def test_reported_pages_are_the_ones_actually_rendered():
    """M3: 選んだ頁ではなく付いた頁を報告する。答えの中の 画面目視判読 p.NN が
    どの頁から来たのかを、後から辿れる唯一の記録がこれ。"""
    c, _ = _client(pdf_context=_FakeBuilder(n_rendered=1))
    r = c.post("/api/ask", json={"question": Q_FIRES, "history": []})
    assert r.json()["pdf_pages"] == [{"pdf": "annotated", "page": 174}]


def test_cdisc_only_hits_never_fire(monkeypatch):
    """CDISC chunk には front matter が無い ⇒ カード 0 枚 ⇒ 不発火。単庫構成の
    /api/ask がこの通道に触れないことの担保。"""
    b = _FakeBuilder()
    c, app = _client(pdf_context=b, texts=("## AE ドメイン\nAETERM は…",))
    c.post("/api/ask", json={"question": Q_FIRES, "history": []})
    assert b.calls == [] and app.state.llm_router.messages[-1]["content"] == f"U:{Q_FIRES}"


# ── M10: R3 の関連性フロアは接線から供給される ─────────────────────────
Q_LAYOUT = "画面のレイアウトを教えて"


class _FakeLookup:
    def __init__(self, hit: bool, form_scopes=()):
        self.hit = hit
        self.form_scopes = list(form_scopes)
        self.asked = []
        self.resolved = []

    def strong_hit(self, q):
        self.asked.append(q)
        return self.hit

    def resolve(self, q):
        self.resolved.append(q)
        return SimpleNamespace(cards=[], form_scopes=list(self.form_scopes))


def test_r3_floor_uses_the_study_lookup_from_app_state():
    b = _FakeBuilder()
    c, app = _client(pdf_context=b, study_lookup=_FakeLookup(True))
    assert c.post("/api/ask", json={"question": Q_LAYOUT, "history": []}
                  ).json()["pdf_trigger"] == "R3"
    assert app.state.study_lookup.asked == [Q_LAYOUT]


def test_r3_does_not_fire_without_the_floor():
    """直查経由のカードも無く、問いも強通道に当たらない = corpus=both の配額で
    紛れ込んだだけのカード。語だけで画像を付けない。"""
    b = _FakeBuilder()
    c, _ = _client(pdf_context=b, study_lookup=_FakeLookup(False))
    r = c.post("/api/ask", json={"question": Q_LAYOUT, "history": []})
    assert r.json()["pdf_trigger"] is None and b.calls == []


def test_r3_floor_accepts_a_question_that_names_a_study_form():
    """予登記 r3 の (c)。T6 型 (純粋な画面レイアウト問い) は直查カードも強通道命中も
    無いので、これが唯一の通り道。"""
    b = _FakeBuilder()
    c, app = _client(pdf_context=b, study_lookup=_FakeLookup(False, form_scopes=["XFORM"]))
    assert c.post("/api/ask", json={"question": Q_LAYOUT, "history": []}
                  ).json()["pdf_trigger"] == "R3"
    assert app.state.study_lookup.resolved == [Q_LAYOUT]


def test_r3_floor_accepts_a_form_named_in_the_question_via_the_page_index():
    """r3b: 別名表 (実データ 1 件) に頼らず、頁索引の名前表でフロアを通す経路。
    T6 型はここでしか通らない (直查カードも強通道命中も無い)。"""
    c, _ = _client(pdf_context=_FakeBuilder(form_named="XFORM"),
                   study_lookup=_FakeLookup(False))
    assert c.post("/api/ask", json={"question": Q_LAYOUT, "history": []}
                  ).json()["pdf_trigger"] == "R3"


def test_no_form_named_and_no_lookup_means_no_fire():
    c, _ = _client(pdf_context=_FakeBuilder(form_named=None), study_lookup=_FakeLookup(False))
    assert c.post("/api/ask", json={"question": Q_LAYOUT, "history": []}
                  ).json()["pdf_trigger"] is None


def test_a_broken_study_lookup_does_not_500_the_request():
    """フロアの供給元が壊れても答えは返る (R3 が発火しなくなるだけ)。"""
    class _Boom:
        def strong_hit(self, q):
            raise RuntimeError("boom")

        def resolve(self, q):
            raise RuntimeError("boom")
    c, _ = _client(pdf_context=_FakeBuilder(form_named=None), study_lookup=_Boom())
    r = c.post("/api/ask", json={"question": Q_LAYOUT, "history": []})
    assert r.status_code == 200 and r.json()["pdf_trigger"] is None


def test_cards_carry_their_lookup_provenance_into_the_trigger():
    """chunk の `via_lookup` が CardFacts まで届いていること —— 届かないと R3 は
    strong_hit だけが頼りになり、フロアの半分が死ぬ。"""
    b = _FakeBuilder()
    app_texts = (CARD.format(item="WX"),)
    c, app = _client(pdf_context=b, texts=app_texts, study_lookup=_FakeLookup(False))
    app.state.rag.via_lookup = True
    assert c.post("/api/ask", json={"question": Q_LAYOUT, "history": []}
                  ).json()["pdf_trigger"] == "R3"


# ── 起動時装配 ─────────────────────────────────────────────────────────
def test_builder_is_none_when_disabled():
    assert main_mod.maybe_build_pdf_context(Settings()) is None


def test_enabled_without_an_index_refuses_to_start(tmp_path):
    s = Settings(pdf_context_enabled=True,
                 pdf_page_index_path_override=str(tmp_path / "ghost.json"))
    with pytest.raises(RuntimeError, match="頁索引が無い"):
        main_mod.maybe_build_pdf_context(s)


def test_enabled_with_an_unusable_builder_refuses_to_start(tmp_path, monkeypatch):
    """索引は在るが pdftoppm が無い。黙って OFF に落ちると「開けたのに一枚も付かない」
    という完全に無症状の状態になる —— 起動で落とすのが唯一気付ける形。"""
    idx = tmp_path / "idx.json"
    idx.write_text(json.dumps({
        "meta": {"pdfs": {"workflow": {"sha256": "a" * 64}, "annotated": {"sha256": "b" * 64}}},
        "names": {}, "workflow": {"n_pages": 1, "blocks": []},
        "annotated": {"n_pages": 1, "blocks": [], "item_pages": {}}}), encoding="utf-8")
    (tmp_path / "w.pdf").write_bytes(b"%PDF")
    (tmp_path / "a.pdf").write_bytes(b"%PDF")
    monkeypatch.setattr("server.pdf_context.shutil.which", lambda _: None)
    s = Settings(pdf_context_enabled=True, pdf_page_index_path_override=str(idx),
                 pdf_workflow_path=str(tmp_path / "w.pdf"),
                 pdf_annotated_path=str(tmp_path / "a.pdf"))
    with pytest.raises(RuntimeError, match="pdftoppm"):
        main_mod.maybe_build_pdf_context(s)


def test_asyncio_is_untouched_by_this_module():
    """import 副作用の目印 (このファイルは asyncio を使わない)。"""
    assert asyncio.iscoroutinefunction(_CaptureRouter().acompletion)


def test_image_part_shape_is_the_probed_one():
    """S0-3 で 4 モデル全部が受け取れた並び。形を変えたらここが赤くなる。"""
    p = ImagePart("annotated", 174, "lbl", "AAA")
    assert (p.pdf, p.page, p.b64) == ("annotated", 174, "AAA")


def test_index_path_default_follows_the_configured_study(monkeypatch):
    """M7: 既定パスに st01 を焼き込むと、別 study に切り替えたとき索引だけ前の study の
    ものを読み続ける (キャッシュ先は study 連動なので、片方だけずれる)。"""
    assert Settings().pdf_page_index_path.parent.name == "st01"
    other = Settings(pdf_context_study_id="st02")
    assert other.pdf_page_index_path.parent.name == "st02"
    assert other.pdf_context_cache_dir.parent.name == "st02"
