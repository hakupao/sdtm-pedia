"""DM2 研读包 prompt cache (spec docs/superpowers/specs/2026-09-25-dossier-prompt-cache-design.md).

布局: 研读包挂上时 system = 原 system + 规则 + "\\n\\n" + 研读包全文, 末尾一个 ephemeral 断点;
user 消息不再含研读包。kill switch `dossier_prompt_cache=False` = 逐字节回到旧布局
(fixtures/dossier_attached_legacy_messages_golden.json 是改动前用同一套 fake 录下的)。
断点只对解析后是 Anthropic 的模型下; 其余模型同布局但 system 为字符串。
⛔ 只用虚构 OID。
"""
from __future__ import annotations

import json
from pathlib import Path

from scripts.tests.test_router_dossier_gate import BAD, GOOD, _gated_client, _stream
from scripts.tests.test_router_dossier_wiring import DOSSIER, OPUS, Q_CDISC, Q_MAP, _client
from server.config import Settings
from server.dossier_trigger import ANSWER_LANGUAGE_LINE
from server.router import _DOSSIER_RULES, _PDF_SOURCE_RULE

LEGACY = Path(__file__).parent / "fixtures" / "dossier_attached_legacy_messages_golden.json"
EPHEMERAL = {"type": "ephemeral"}
GPT = next(m.model for m in Settings().selectable_models if m.id == "gpt-terra")


def _post(c, ep, **kw):
    body = {"question": Q_MAP, "history": [], "dossier": "on", **kw}
    return c.post(ep, json=body)


def _cached_system(sys_text):
    return [{"type": "text", "text": sys_text + _DOSSIER_RULES + "\n\n" + DOSSIER.text,
             "cache_control": EPHEMERAL}]


def test_attached_moves_dossier_into_system_with_breakpoint():
    for ep in ("/api/ask", "/api/ask_stream"):
        for fed, sys_text, ctx in ((True, "SYS[both]", "FED:cdisc0,cdisc1"),
                                   (False, "SYS", "CD:cdisc0,cdisc1")):
            c, app = _client(DOSSIER)
            if not fed:
                app.state.federation = None
            _post(c, ep)
            msgs = app.state.llm_router.messages
            assert msgs[0] == {"role": "system", "content": _cached_system(sys_text)}, (ep, fed)
            assert msgs[-1]["content"] == (f"CTX={ctx}\nQ={Q_MAP}\n\n"
                                           + ANSWER_LANGUAGE_LINE["zh"]), (ep, fed)
            assert all(DOSSIER.text not in json.dumps(m, ensure_ascii=False)
                       for m in msgs[1:]), (ep, fed)


def test_dossier_body_is_byte_identical_at_the_tail_of_system():
    c, app = _client(DOSSIER)
    _post(c, "/api/ask")
    block = app.state.llm_router.messages[0]["content"][-1]
    assert block["text"].endswith(_DOSSIER_RULES + "\n\n" + DOSSIER.text)


def test_rule_reference_points_at_system_not_context():
    assert "The system prompt ends with 【本研究 研読パッケージ】: this study's protocol" in _DOSSIER_RULES
    assert "The context ends with" not in _DOSSIER_RULES


def test_kill_switch_restores_legacy_layout_byte_for_byte():
    golden = json.loads(LEGACY.read_text(encoding="utf-8"))
    for key, want in golden["messages"].items():
        ep, mode = key.split("|")
        c, app = _client(DOSSIER)
        app.state.settings = app.state.settings.model_copy(update={"dossier_prompt_cache": False})
        if mode == "single":
            app.state.federation = None
        _post(c, ep)
        assert app.state.llm_router.messages == want, key


def test_default_is_on_and_info_exposes_it():
    from scripts.tests.test_model_switching import _info_client
    assert Settings().dossier_prompt_cache is True
    assert _info_client().get("/api/info").json()["dossier_prompt_cache"] is True
    assert _info_client(dossier_prompt_cache=False).get(
        "/api/info").json()["dossier_prompt_cache"] is False


def test_unattached_leaves_system_a_plain_string():
    c, app = _client(DOSSIER)
    c.post("/api/ask", json={"question": Q_CDISC, "history": []})
    assert app.state.llm_router.messages[0] == {"role": "system", "content": "SYS[both]"}


def test_non_anthropic_model_gets_same_layout_as_plain_string():
    """gpt-* 走 bedrock converse: litellm 会把 cache_control 转成 cachePoint, 模型不支持就 400。
    ⇒ 断点只对 Anthropic 下; 其余同布局 (研读包仍在 system 末尾) 但 system 是字符串。"""
    for model, cached in (("opus-5", True), ("default", True), ("gpt-terra", False),
                          ("gpt-sol", False), ("default-fallback", False)):
        c, app = _client(DOSSIER)
        _post(c, "/api/ask", model=model)
        sys_content = app.state.llm_router.messages[0]["content"]
        if cached:
            assert sys_content == _cached_system("SYS[both]"), model
        else:
            assert sys_content == "SYS[both]" + _DOSSIER_RULES + "\n\n" + DOSSIER.text, model


def test_prompt_cache_capable_resolves_like_router_groups():
    from server.router import _prompt_cache_capable
    s = Settings(default_model=OPUS)
    assert _prompt_cache_capable(s, "opus-5") and _prompt_cache_capable(s, "sonnet-5")
    assert _prompt_cache_capable(s, "default") and _prompt_cache_capable(s, "hard")
    assert not _prompt_cache_capable(s, "gpt-terra")
    assert not _prompt_cache_capable(s, "default-fallback")      # deepseek
    assert not _prompt_cache_capable(s, "nope")
    assert not _prompt_cache_capable(Settings(default_model=GPT), "default")


def test_deepseek_transform_flattens_list_system_and_drops_cache_control():
    """回退路径 (Anthropic 主模型 → default-fallback=deepseek) 由 litellm 自己降级:
    DeepSeekChatConfig._transform_messages 把 content list 拼成字符串。钉住 litellm 这一行为,
    升级 litellm 若改了它这里先红 (真探针结果见 commit message)。"""
    from litellm.llms.deepseek.chat.transformation import DeepSeekChatConfig
    sys_list = [{"type": "text", "text": "SYS-RULES\n\nDOSSIER", "cache_control": EPHEMERAL}]
    req = DeepSeekChatConfig().transform_request(
        model="deepseek-v4-pro",
        messages=[{"role": "system", "content": sys_list}, {"role": "user", "content": "q"}],
        optional_params={}, litellm_params={}, headers={})
    assert req["messages"][0]["content"] == "SYS-RULES\n\nDOSSIER"
    assert "cache_control" not in json.dumps(req)


def test_pdf_rule_appends_a_second_block_after_the_breakpoint(monkeypatch):
    """PDF 通道在研读包之后改 system: list 上 `+=` str 会逐字符 extend。另起一块且不带断点,
    缓存前缀 (第一块) 在附不附画面之间保持同一。"""
    from types import SimpleNamespace
    from server.router import maybe_attach_pdf_pages
    monkeypatch.setattr("server.pdf_trigger.should_attach_pdf",
                        lambda *a, **k: SimpleNamespace(fire=True, rule="R1", reason="t"))
    builder = SimpleNamespace(
        index=SimpleNamespace(form_named_in=lambda q: "F"),
        select_pages=lambda cards, q: SimpleNamespace(pages=(1,), folded=(), truncated=False),
        render=lambda sel: [SimpleNamespace(pdf="x.pdf", page=1)],
        to_message_parts=lambda sel, images: [{"type": "image_url", "image_url": {"url": "d"}}])
    req = SimpleNamespace(app=SimpleNamespace(state=SimpleNamespace(
        pdf_context=builder, study_lookup=None)))
    msgs = [{"role": "system", "content": _cached_system("SYS")},
            {"role": "user", "content": "Q"}]
    maybe_attach_pdf_pages(req, "q", [], msgs)
    assert msgs[0]["content"] == [*_cached_system("SYS"), {"type": "text", "text": _PDF_SOURCE_RULE}]
    plain = [{"role": "system", "content": "SYS"}, {"role": "user", "content": "Q"}]
    maybe_attach_pdf_pages(req, "q", [], plain)
    assert plain[0]["content"] == "SYS" + _PDF_SOURCE_RULE        # 字符串 system 照旧


# ── 闸重答: 第二轮沿用同一 system (前缀一致 ⇒ 必然命中) ──────────────────

def test_regenerate_round_reuses_the_same_system_block():
    for ep in ("stream", "ask"):
        c, app = _gated_client([(BAD, "stop"), (GOOD, "stop")])
        if ep == "stream":
            _stream(c)
        else:
            c.post("/api/ask", json={"question": Q_MAP, "history": []})
        first, second = app.state.llm_router.calls
        assert first[0] == second[0] == {"role": "system", "content": _cached_system("SYS[both]")}

