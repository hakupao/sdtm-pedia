"""真浏览器闸: 流式期间 Markdown 已渲染 + 正文出处默认隐藏、开关后以 .cite 显示。

为什么真浏览器: 这两条都是"某一帧 DOM 长什么样"的断言, 只有浏览器能回答。
SSE 用 page.route 在浏览器侧 stub, 不需要 RAG 引擎 (lifespan 关掉)。
装法见 test_webchat_cache_browser.py docstring; 未装 playwright 则本文件可见地 skip。
"""
from __future__ import annotations

import json
import socket
import threading
import time
from pathlib import Path
from types import SimpleNamespace

import pytest
import uvicorn

from server import main as main_mod
from server.config import Settings

pw_api = pytest.importorskip(
    "playwright.sync_api",
    reason="真浏览器闸需要 playwright (dev-only 可选; 装法见 test_webchat_cache_browser.py)",
)

_WEBCHAT = Path(__file__).resolve().parents[2] / "webchat"

# 只放前端真读的字段 + SelectableModel 的 `model` (保持与 /api/info 真实形状同构):
# app.js loadModelName 读 default_model / federation / selectable_models[].{id,label,verified}。
_INFO = {
    "default_model": "bedrock/converse/global.anthropic.claude-opus-5",
    "federation": False,
    "selectable_models": [
        {"id": "opus-5", "label": "Claude Opus 5",
         "model": "bedrock/converse/global.anthropic.claude-opus-5", "verified": True},
    ],
}

# 四帧: sources → 两帧 token → done。出处夹在正文中间, 且**跨帧**分行, 逼出前端每帧全量重解析。
_FRAMES = [
    ('sources', '{"sources":[{"chunk_id":"c1","source":"domains/AE.md","domain":"AE","file_type":"spec",'
                '"section":"§1","similarity":0.9,"text_preview":"AETERM"}],"routed_corpus":null}'),
    ('token', '{"text":"## AE 域\\n\\n- AETERM 是报告术语 **[Source: domains/AE.md]**\\n"}'),
    ('token', '{"text":"- AEDECOD 是编码术语"}'),
    ('done', '{"model_id":"opus-5","verified":true,"web_status":"off","web_searches_ok":0,'
             '"models_used":["opus-5"],"fell_back":false}'),
]


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest.fixture
def live(monkeypatch):
    """真 uvicorn + 真 create_app(), _WEBCHAT_DIR 指向**真实** webchat/ —— 测的是生产前端,
    不是一个长得像的 stub。端口取空闲口, 绝不碰生产的 8000。lifespan 关掉: 页面与静态资源
    用不着 RAG 引擎, 而 /api/* 全部被 page.route 在浏览器侧截走, 到不了服务端。

    rate_limit_enabled=False 是**必需**的, 不是洁癖: .env 里 SDTM_RAG_RATE_LIMIT_ENABLED=true,
    Settings 会读进来。首屏一次要下 index.html + style.css + 3 个 vendor + app.js + 7 个
    js 模块, 远超 BURST=10。/static/ 与 / 现在有豁免 (f64ba41), 但这条闸不该把自己的绿
    押在另一处豁免名单上 —— 那份名单改了, 失败会以"页面加载不全"的形状出现在这里。
    """
    monkeypatch.setattr(main_mod, "_WEBCHAT_DIR", _WEBCHAT)
    settings = Settings(federation_enabled=False, study_lookup_enabled=False,
                        study_docs_enabled=False, rate_limit_enabled=False)
    port = _free_port()
    server = uvicorn.Server(uvicorn.Config(main_mod.create_app(settings), host="127.0.0.1", port=port,
                                           lifespan="off", log_level="warning"))
    t = threading.Thread(target=server.run, daemon=True)
    t.start()
    deadline = time.monotonic() + 15
    while not server.started:
        if time.monotonic() > deadline or not t.is_alive():
            server.should_exit = True
            raise RuntimeError("uvicorn 没起来")
        time.sleep(0.05)
    try:
        yield SimpleNamespace(url=f"http://127.0.0.1:{port}/")
    finally:
        server.should_exit = True
        t.join(timeout=15)


def _launch(pw):
    """优先用 playwright 自带的 chromium; 没下载过就退回本机已装的 Google Chrome。两条都不通
    才 skip —— 装了 wheel 却没浏览器不该报成失败 (同 test_webchat_cache_browser.py)。"""
    try:
        return pw.chromium.launch()
    except Exception:
        try:
            return pw.chromium.launch(channel="chrome")
        except Exception as exc:
            pytest.skip(f"没有可用的 chromium/chrome: {exc}")


def _stub_routes(page, frames=None):
    """/api/info 固定; /api/ask_stream 一次性吐完给定的帧 (默认上面那四帧)。

    ⚠ route.fulfill 是**一次性**给 body 的, 卡不住流 —— 所以这里不假装能卡。前端按 `\\n\\n`
    切帧 (stream.js 的 while 循环), 一次性 body 照样正确分出 4 帧, done 之后的 DOM 断言不受
    影响; 而"流**进行中**那一帧长什么样"由 test 里的 page.evaluate 直接调
    renderMarkdown(streaming=True) 来钉 —— 同一份模块代码, 不是另写一个近似物。
    """
    page.route("**/api/info", lambda r: r.fulfill(
        status=200, content_type="application/json", body=json.dumps(_INFO)))

    def sse(route):
        body = b"".join(f"event: {ev}\ndata: {data}\n\n".encode()
                        for ev, data in (frames or _FRAMES))
        route.fulfill(status=200, content_type="text/event-stream", body=body)

    page.route("**/api/ask_stream", sse)


def _ask(page, text: str):
    page.fill("#input", text)
    page.press("#input", "Enter")


def test_markdown_renders_before_done_and_citation_hidden(live):
    """两段验证:
    (a) 全量帧完成后 DOM 是渲染后的 md 且无 [Source; (b) 用 page.evaluate 直接调
    renderMarkdown(streaming=True) 断言流中半截围栏/半截出处的行为 (同一份模块代码)。"""
    with pw_api.sync_playwright() as pw:
        browser = _launch(pw)
        try:
            page = browser.new_page()
            _stub_routes(page)
            page.goto(live.url)
            page.wait_for_selector(".empty h1")
            # /api/info 落地后再问 —— 否则模型下拉是空的, 走的是"info 没加载出来"那条降级路径,
            # 与用户真实看到的不是同一条。native select 的 option 本身不渲染, 故等 attached 而非 visible。
            page.wait_for_selector("#model-select option", state="attached")
            # 高频控件在输入框工具行, 不在齿轮弹层里 (2026-09-08 方案 A)
            assert page.locator("#composer #model-select").is_visible()
            assert page.locator("#settings-panel #model-select").count() == 0
            # scope 在 federation=false 时是 hidden 的, 所以只断言"在 composer 里", 不断言可见
            assert page.locator("#composer #scope-web").count() == 1
            _ask(page, "AE 域问题")
            page.wait_for_selector(".turn.assistant .chip.model-meta")
            html = page.inner_html(".turn.assistant .bubble")
            assert "<h2" in html and "<li" in html
            assert "[Source" not in html and "Source:" not in html
            assert page.inner_text(".turn.assistant .bubble").strip().endswith("AEDECOD 是编码术语")
            # 来源折叠区仍在, 与正文出处无关
            assert page.inner_text(".sources summary") == "来源 (1)"

            # (b) 流中行为: 同一模块, streaming=True
            mid = page.evaluate(r"""async () => {
                const m = await import('/static/js/markdown.js');
                return [m.renderMarkdown('## T\n\n- a **[Source: x', {streaming:true}),
                        m.renderMarkdown('```py\nx=1', {streaming:true})];
            }""")
            assert "<h2" in mid[0] and "<li" in mid[0] and "Source" not in mid[0]
            assert "<pre" in mid[1] and "x=1" in mid[1]

            # 开关打开 → 出处以 .cite 显示; 存档原文不变 (复制按钮拿到的还是原文)
            page.click("#settings-btn")
            page.check("#show-citations")
            page.wait_for_selector(".turn.assistant .bubble .cite")
            assert page.inner_text(".turn.assistant .bubble .cite") == "Source: domains/AE.md"
            stored = page.evaluate("() => JSON.parse(localStorage.getItem('sdtm_chat_v1')).conversations[0].messages[1].content")
            assert "**[Source: domains/AE.md]**" in stored
        finally:
            browser.close()


def test_old_archive_still_renders(live):
    """老存档 (无 modelId / fellBack 字段) 刷新后照常渲染, 徽章不画 (modelId 缺失时什么都不画)。"""
    with pw_api.sync_playwright() as pw:
        browser = _launch(pw)
        try:
            page = browser.new_page()
            _stub_routes(page)
            page.goto(live.url)
            page.evaluate("""() => localStorage.setItem('sdtm_chat_v1', JSON.stringify({
                conversations:[{id:'o1',title:'旧',createdAt:1,messages:[
                  {role:'user',content:'q'},
                  {role:'assistant',content:'**A** [Source: a.md]',sources:[]}]}], currentId:'o1'}))""")
            page.reload()
            page.wait_for_selector(".turn.assistant .bubble strong")
            assert page.locator(".chip.model-meta").count() == 0
            assert "Source" not in page.inner_text(".turn.assistant .bubble")
            assert page.locator(".turn-tools .flag-btn").count() == 1
        finally:
            browser.close()


# ── 输出触顶自动续写: 前端呈现 (2026-09-08) ──────────────────────────────
#
# 后端把答案分成多次 API 调用续写完, 前端必须做到两件事: (1) 拼出来的正文是**连续**的,
# 中间那个 `continue` 事件不能把渲染打断也不能自己冒出可见文字; (2) "自动续写过 N 轮"
# 与"到了续写上限、可能还没写完"是两种不同的状态, 要分开说 —— 后者是**警告**。

def _continue_frames(truncated: bool, rounds: int = 1):
    return [
        ('sources', '{"sources":[],"routed_corpus":null}'),
        ('token', '{"text":"前半段"}'),
        ('continue', '{"round":1}'),
        ('token', '{"text":"后半段"}'),
        ('done', '{"model_id":"opus-5","verified":true,"web_status":"off","web_searches_ok":0,'
                 '"models_used":["opus-5"],"fell_back":false,'
                 f'"continue_rounds":{rounds},"truncated":{"true" if truncated else "false"}}}'),
    ]


def test_auto_continue_chip_and_truncation_warning(live):
    """两个变体跑在同一个浏览器里: 未触顶 → 只挂 chip; 触顶 → 挂 .turn-note.warn。

    正文断言放在两边都做: `continue` 事件若被 dispatch 当成未知事件吞掉是无害的, 但若
    被误当成 token 渲染, 用户会在答案中间看到一段 JSON —— 那正是这条闸要挡的形状。
    """
    with pw_api.sync_playwright() as pw:
        browser = _launch(pw)
        try:
            page = browser.new_page()
            _stub_routes(page, _continue_frames(truncated=False))
            page.goto(live.url)
            page.wait_for_selector("#model-select option", state="attached")
            _ask(page, "长问题")
            page.wait_for_selector(".turn.assistant .chip.model-meta")
            assert page.inner_text(".turn.assistant .bubble").strip() == "前半段后半段"
            assert page.inner_text(".turn.assistant .chip.continue") == "自动续写 ×1"
            assert page.locator(".turn.assistant .turn-note.warn").count() == 0

            # 触顶变体: 换一份帧, 开新会话重问
            page.unroute("**/api/ask_stream")
            _stub_routes(page, _continue_frames(truncated=True, rounds=8))
            page.click("#new-chat")
            _ask(page, "更长的问题")
            page.wait_for_selector(".turn.assistant .turn-note.warn")
            warn = page.inner_text(".turn.assistant .turn-note.warn")
            assert "8" in warn and "自动续写上限" in warn
            # 触顶时不再重复挂 chip —— 同一件事说两遍, 而警告已经含轮数
            assert page.locator(".turn.assistant .chip.continue").count() == 0

            # 刷新后两者都必须复原 —— 只在 onDone 里画的话, 存档里一条被截断的答案
            # 与一条完整答案长得一模一样 (与 webStatus / fellBack 同一条教训)。
            page.reload()
            page.wait_for_selector(".turn.assistant .turn-note.warn")
            assert "8" in page.inner_text(".turn.assistant .turn-note.warn")
        finally:
            browser.close()
