"""U2: 生产 lifespan 上的 doc 通道接线锁 (spec §4.5)。

接线漏在这里是完全静默的 —— 服务照常起, study 侧只是回到纯卡片。所以三个方向都要锁:
开着一定包成 StudyCorpusEngine / 关着一定不包 / 开着但联邦关着要留声。
仿 test_main_study_lookup_wiring.py 的 stub 编制, 不碰 chroma。
"""
from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest
import structlog
from fastapi import FastAPI

from server import main as main_mod
from server.config import Settings
from server.study_corpus import StudyCorpusEngine


@pytest.fixture
def boot(monkeypatch):
    engines: list[dict] = []

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            engines.append(kwargs)
            self.collection = FakeCollection()
            self.system_prompt = "SYS"

        def _vi_section_map(self):
            return {}

    monkeypatch.setattr(main_mod, "RAGEngine", FakeEngine)
    monkeypatch.setattr(main_mod, "create_router", lambda s: SimpleNamespace(model_list=[]))
    monkeypatch.setattr(main_mod, "SpecLoader",
                        lambda root: SimpleNamespace(domains=[], codelists=[]))

    def _run(**overrides):
        s = Settings(**overrides)
        app = FastAPI()
        app.state.settings = s
        events: list[tuple] = []
        # ⚠ 计划原文写的是 `lambda _l, m, ed: events.append((m, ed))`, 但 structlog 的
        # processor 签名是 (logger, method_name, event_dict) —— `m` 绑的是 "info"/"warning"
        # 这个**方法名**, 事件名在 `ed["event"]` 里 (实测: log.warning("study_docs_ignored")
        # → ("warning", {"event": "study_docs_ignored", ...}))。照原文抄则下面两条日志断言
        # 在任何实现下都不可能通过。这里只把元组首位换成真正的事件名, 四条断言一字不动。
        # 用 capture_logs 而非裸 configure: 后者会把处理器永久留在全局配置里泄漏给后续测试。
        async def go():
            async with main_mod.lifespan(app):
                pass
        with structlog.testing.capture_logs() as logs:
            asyncio.run(go())
        events.extend((e["event"], e) for e in logs)
        return app, engines, events

    return _run


def test_docs_engine_is_built_and_wrapped_when_enabled(boot):
    app, engines, _ = boot(federation_enabled=True, study_docs_enabled=True, study_docs_seats=5)
    built = [e["collection_name"] for e in engines]
    assert "study_st01_docs" in built
    assert isinstance(app.state.federation.study, StudyCorpusEngine)
    assert app.state.federation.study.doc_seats == 5


def test_docs_engine_absent_when_disabled(boot):
    app, engines, _ = boot(federation_enabled=True, study_docs_enabled=False)
    assert "study_st01_docs" not in [e["collection_name"] for e in engines]
    assert not isinstance(app.state.federation.study, StudyCorpusEngine)


def test_docs_enabled_without_federation_logs_ignored(boot):
    _, engines, events = boot(federation_enabled=False, study_docs_enabled=True)
    assert "study_st01_docs" not in [e["collection_name"] for e in engines]
    assert any(m == "study_docs_ignored" for m, _ in events)


def test_seats_and_collection_are_reported_in_the_ready_log(boot):
    """条数/库名进日志: 席位写死成常量或库名指错时, 唯一的现场线索就是这一行。"""
    app, _, events = boot(federation_enabled=True, study_docs_enabled=True, study_docs_seats=7)
    hit = [ed for m, ed in events if m == "study_docs"]
    assert hit and hit[0]["seats"] == 7 and hit[0]["collection"] == "study_st01_docs"
    # ↓ 补做的断言 (实现方自查, 计划没有)。计划的三条变异里 `doc_seats=s.study_docs_seats`
    # 改成常量 `5` 实测**全绿 1131 passed** —— 因为上面唯一检查引擎席位的那条测试恰好也用
    # seats=5, 而这条只看日志。日志报 7 而引擎实际只拿 5 席正是"日志在撒谎"的那类故障,
    # 用非默认值把两者钉成同源。
    assert app.state.federation.study.doc_seats == 7
