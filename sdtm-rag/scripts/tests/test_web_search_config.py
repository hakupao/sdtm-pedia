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
