"""真浏览器端到端闸: 改了 webchat 文件、不强刷, 也能拿到新版。

为什么非要真浏览器: 这条缺陷的形状是"服务器是对的、客户端拿的不是"。服务端断言看不见它,
httpx / TestClient 也顶不了 —— 它们**没有 HTTP 缓存实现**, 每次都真发请求, 修前修后都拿到
新文件, 永远绿。只有带磁盘缓存的真浏览器能复现同一失败形状。响应头那一层由
test_webchat_cache_headers.py 钉。

装法 (dev-only 可选; 没装则本文件整体 skip, skip 是可见的, 不是静默跳过):
    uv pip install playwright        # 或 uv sync --extra browser
    .venv/bin/playwright install chromium   # 可跳过: 会回退到本机已装的 Google Chrome (见 _launch)
"""
from __future__ import annotations

import os
import socket
import threading
import time
import urllib.request
from types import SimpleNamespace

import pytest
import uvicorn

from server import main as main_mod
from server.config import Settings

pw_api = pytest.importorskip(
    "playwright.sync_api",
    reason="真浏览器端到端闸需要 playwright (dev-only 可选): uv sync --extra browser",
)

# 浏览器给一条没有 Cache-Control 的响应编造的新鲜期, 惯例是 (now - Last-Modified) 的 10%。
# 刚写出来的文件新鲜期约等于 0, 浏览器本来就会回源 —— 那样连未修的服务器都显得健康, 这条闸
# 会永远绿。回拨 30 天买到约 3 天新鲜期, 才是真实部署资产的样子。
# ⚠ 不要把回拨改成固定时间戳: 两次写入的 mtime 一样, ETag (starlette 取自 mtime+size) 就会
#   碰撞, 修好的服务器也会回 304 + 旧内容, 同样是一条永远绿的假闸。
_BACKDATE_S = 30 * 24 * 3600

_INDEX = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8" /><title>webchat cache e2e</title></head>
<body>
  <h1 id="doc-version">{version}</h1>
  <script src="/static/marker.js"></script>
</body>
</html>
"""

_MARKER = 'window.__MARKER = "{version}";\n'


def _write_version(directory, version: str) -> None:
    """两个独立标记: #doc-version 来自 index.html (走 `GET /` 的 FileResponse),
    window.__MARKER 来自 /static/marker.js (走 StaticFiles mount) —— 修复的两半各有证人。"""
    directory.mkdir(parents=True, exist_ok=True)
    backdated = time.time() - _BACKDATE_S
    for name, text in (("index.html", _INDEX.format(version=version)),
                       ("marker.js", _MARKER.format(version=version))):
        path = directory / name
        path.write_text(text, encoding="utf-8")
        os.utime(path, (backdated, backdated))


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _etag(url: str) -> str:
    with urllib.request.urlopen(url, timeout=5) as resp:  # noqa: S310 — 固定 127.0.0.1
        return resp.headers["ETag"]


@pytest.fixture
def live_webchat(tmp_path, monkeypatch):
    """真 uvicorn + 真 create_app(), 只是把 _WEBCHAT_DIR 指到临时目录 —— 测的是生产接线,
    不是一个长得像的 stub。端口取空闲口, 绝不碰生产的 8000。lifespan 关掉: 静态文件用不着
    RAG 引擎。"""
    monkeypatch.setattr(main_mod, "_WEBCHAT_DIR", tmp_path)
    _write_version(tmp_path, "V1")
    settings = Settings(federation_enabled=False, study_lookup_enabled=False,
                        study_docs_enabled=False)
    port = _free_port()
    server = uvicorn.Server(uvicorn.Config(
        main_mod.create_app(settings), host="127.0.0.1", port=port,
        lifespan="off", log_level="warning",
    ))
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    deadline = time.monotonic() + 15
    while not server.started:
        if time.monotonic() > deadline or not thread.is_alive():
            server.should_exit = True
            raise RuntimeError("uvicorn 没起来")
        time.sleep(0.05)
    try:
        yield SimpleNamespace(url=f"http://127.0.0.1:{port}/", dir=tmp_path)
    finally:
        server.should_exit = True
        thread.join(timeout=15)


def _launch(pw):
    """优先用 playwright 自带的 chromium; 没下载过就退回本机已装的 Google Chrome, 免得为一条
    测试拖 150 MB 浏览器。两条都不通才 skip —— 装了 wheel 却没浏览器不该报成失败。"""
    try:
        return pw.chromium.launch()
    except Exception:
        try:
            return pw.chromium.launch(channel="chrome")
        except Exception as exc:
            pytest.skip(f"没有可用的 chromium/chrome: {exc}")


def _markers(page) -> tuple:
    return tuple(page.evaluate(
        "() => [document.getElementById('doc-version').textContent, window.__MARKER]"))


def _marker_transfer_size(page) -> int:
    return page.evaluate(
        "() => performance.getEntriesByType('resource')"
        ".filter(e => e.name.endsWith('/static/marker.js')).map(e => e.transferSize)[0] ?? -1")


@pytest.mark.parametrize("revisit", ["fresh_navigation", "soft_reload"])
def test_edited_files_reach_the_browser_without_a_hard_reload(live_webchat, revisit):
    """用户看得到的两条回访路径都得拿到新版。

    修前实测两条都红, 且红法不同 —— soft_reload 只强制校验主文档, 子资源照吃缓存, 于是
    拿到**新 HTML + 旧 JS**, 元素在、功能不在, 正是"新功能没上线"的假象。"""
    with pw_api.sync_playwright() as pw:
        browser = _launch(pw)
        try:
            page = browser.new_page()
            page.goto(live_webchat.url)
            assert _markers(page) == ("V1", "V1")
            first_transfer = _marker_transfer_size(page)
            assert first_transfer > 0, "首次加载就没走网络, 环境不对"

            marker_url = live_webchat.url + "static/marker.js"
            before = _etag(marker_url)
            _write_version(live_webchat.dir, "V2")
            # 非空性前提: 两版的 ETag 必须真的不同, 否则"拿到旧版"可能只是 ETag 撞车导致的
            # 304, 而不是浏览器压根没问 —— 那样这条闸测的就不是这个缺陷了。
            assert _etag(marker_url) != before

            if revisit == "fresh_navigation":
                page.goto("about:blank")
                page.goto(live_webchat.url)
            else:
                page.reload()  # 普通刷新, 不是 Cmd+Shift+R
            assert _markers(page) == ("V2", "V2")

            # 反向非空性: 文件没变时必须只回 304 (传输量掉下来), 而不是整份重下。若浏览器
            # 的缓存被整个关掉, 上面那条断言无论修没修都会绿 —— 这一条把那种情况钉出来。
            page.goto("about:blank")
            page.goto(live_webchat.url)
            assert _markers(page) == ("V2", "V2")
            assert 0 < _marker_transfer_size(page) < first_transfer
        finally:
            browser.close()
