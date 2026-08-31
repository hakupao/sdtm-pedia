"""Web 搜索通道的配置旋钮 (spec §6 组件表 / §7 上限)。"""
from server.config import Settings


def test_web_search_defaults():
    s = Settings()
    # 默认开 (Rule 9 进 prompt), 但请求级 web 默认 off —— 两件事互不影响
    assert s.web_search_enabled is True
    assert s.web_max_rounds == 5
    assert s.web_max_searches == 15
    assert s.web_results_per_search == 3
    assert s.web_result_max_chars == 1200
    assert s.web_daily_quota == 200
    assert s.web_timeout_s == 30.0


def test_web_search_env_override(monkeypatch):
    """逐字节回滚路径: 关掉即回到引入前 (对齐 prompt_guardrail_enabled 先例)。"""
    monkeypatch.setenv("SDTM_RAG_WEB_SEARCH_ENABLED", "false")
    monkeypatch.setenv("SDTM_RAG_WEB_MAX_ROUNDS", "2")
    s = Settings()
    assert s.web_search_enabled is False
    assert s.web_max_rounds == 2


def _info_client(*, web_search_enabled: bool):
    """/api/info 只读 rag/settings 上的几个属性, 用最小 stub 起一个 app 即可 —— 不碰
    chroma/embedding。"""
    from types import SimpleNamespace

    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from server.router import api_router

    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = SimpleNamespace(
        collection=SimpleNamespace(count=lambda: 1),
        structured_lookup_enabled=True, hybrid_enabled=True, hybrid_fusion="rrf",
        prompt_guardrail_enabled=True, web_search_enabled=web_search_enabled,
    )
    app.state.settings = Settings(web_search_enabled=web_search_enabled)
    return TestClient(app)


def test_info_reports_web_search_lever():
    """I-B: `web_search_enabled` 的存在理由是"瞬时回滚 + A/B", 但翻了 env 之后必须
    能确认进程真吃到了。/api/info 是运维唯一的在线出口 (兄弟 lever prompt_guardrail
    早已在这里), 两个方向都要跟着开关走 —— 只测 True 的话, 把这个字段写死成常量也能绿。"""
    assert _info_client(web_search_enabled=True).get("/api/info").json()["web_search"] is True
    assert _info_client(web_search_enabled=False).get("/api/info").json()["web_search"] is False


def test_ask_rejects_unknown_fields():
    """Minor 1: `AskRequest` 若不 forbid extra, `/api/ask` 收到 `web: true` 会**静默
    丢弃**并照常返回 200 —— 抽检脚本 v1 就是这样产出了一整张"全 ✅ 却什么都没测到"的表
    (evidence/failures/web_channel_spotcheck_attempt_1_wrong_endpoint.md)。"""
    c = _info_client(web_search_enabled=True)
    r = c.post("/api/ask", json={"question": "AETERM?", "web": True})
    assert r.status_code == 422, r.text
    assert "web" in r.text
