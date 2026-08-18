"""main.py 生产启动路径上的 U6 信号层接线锁 (Task 8)。

接线漏在这里的表现是完全静默的: 服务照常起, 判库照常出结果, 只是永远不拓宽 ——
即 Task 10 的全闸会量到"修法无效", 而真正的原因是修法根本没上线。故两个方向都要锁:
S2 在时必须挂上**同一份** StudyLookup, S2 不在时必须挂 None 且留声 (不得为了凑上
信号层而自己再读一遍 catalog —— 那会绕过 study_lookup_enabled 开关)。

写法与协作者 stub 沿用 test_main_study_lookup_wiring.py (同一条 lifespan)。
"""
from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest
import structlog
from fastapi import FastAPI

from server import federation as federation_mod
from server import main as main_mod
from server import study_lookup as study_lookup_mod
from server.config import Settings
from server.routing_signals import RoutingSignals


class _FakeLookup:
    def stats(self) -> str:
        return "7 items/0 aliases"


class _FakeFederated:
    """记录构造实参 —— signals 是不是真被传进来, 只有这里看得见。"""

    def __init__(self, cdisc, study, llm_router, top_k=15, signals=None):
        self.cdisc, self.study = cdisc, study
        self.llm_router, self.top_k, self.signals = llm_router, top_k, signals


@pytest.fixture
def boot(monkeypatch):
    engines: list[dict] = []
    feds: list[_FakeFederated] = []

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            engines.append(kwargs)
            self.collection = FakeCollection()

        def _vi_section_map(self):
            return {}

    def _fake_fed(*a, **k):
        fed = _FakeFederated(*a, **k)
        feds.append(fed)
        return fed

    monkeypatch.setattr(main_mod, "RAGEngine", FakeEngine)
    monkeypatch.setattr(main_mod, "create_router", lambda *a, **k: None)
    monkeypatch.setattr(main_mod, "maybe_build_answerer", lambda s: None)
    monkeypatch.setattr(federation_mod, "FederatedEngine", _fake_fed)
    monkeypatch.setattr(
        main_mod, "SpecLoader", lambda root: SimpleNamespace(domains=[], codelists=[])
    )
    monkeypatch.setattr("server.meta_store.MetaStore", lambda p: SimpleNamespace())
    monkeypatch.setattr(
        "server.graph_engine.GraphEngine",
        lambda store: SimpleNamespace(store=SimpleNamespace(n_domains=0)),
    )
    monkeypatch.setattr(
        "scripts.kb_freshness.check_freshness",
        lambda *a, **k: SimpleNamespace(fresh=True, reason=""),
    )

    def _run(app_settings: Settings):
        app = FastAPI()
        app.state.settings = app_settings

        async def _enter():
            async with main_mod.lifespan(app):
                pass

        with structlog.testing.capture_logs() as logs:
            asyncio.run(_enter())
        return SimpleNamespace(engines=engines, feds=feds, logs=logs, app=app)

    return _run


@pytest.fixture
def fake_lookup(monkeypatch):
    """`loads` 记的是**加载次数** —— 桩恒返回同一个对象, 光靠 `is` 判不出"读了两遍"。"""
    recorded: dict = {"loads": 0}
    lookup = _FakeLookup()

    def _fake(catalog_path, aliases_path):
        recorded["catalog"] = catalog_path
        recorded["loads"] += 1
        return lookup

    monkeypatch.setattr(study_lookup_mod.StudyLookup, "from_paths", staticmethod(_fake))
    return lookup, recorded


def test_signals_wired_onto_the_federated_engine(boot, fake_lookup):
    lookup, recorded = fake_lookup
    r = boot(Settings(study_lookup_enabled=True, study_docs_enabled=False))
    fed = r.feds[0]
    assert isinstance(fed.signals, RoutingSignals)
    # 同一实例, 不是"另建一份": 两份 S2 可以来自不同文件 (路径 override 只改一处时),
    # 而信号层用的那份从不出现在任何日志里 —— 不一致会静默到 Task 10 的数字上。
    assert fed.signals.study_lookup is lookup
    _, study = r.engines
    assert study["study_lookup"] is fed.signals.study_lookup
    # ↑ 那条 `is` 判不出"读了两遍" (桩恒返回同一对象, 真 from_paths 则会造出两份索引)。
    assert recorded["loads"] == 1, "信号层自己又加载了一份 S2 = 复用没接上"


def test_no_signals_and_a_warning_when_s2_is_off(boot, fake_lookup):
    """S2 关着 = 信号层的 study 半边没有数据源。此时挂空并留声, 但**绝不**自己去读
    catalog —— 那等于让信号层绕开 study_lookup_enabled 开关。"""
    _, recorded = fake_lookup
    r = boot(Settings(study_lookup_enabled=False, study_docs_enabled=False))
    assert r.feds[0].signals is None
    assert recorded["loads"] == 0, "开关关着却读了 catalog = 信号层绕过了开关"
    warn = next(e for e in r.logs if e["event"] == "signal_layer_off")
    assert warn["log_level"] == "warning"


def test_federation_log_reports_the_signal_layer(boot, fake_lookup):
    """判库为什么没拓宽, 第一现场是启动日志: 没有这行就分不清"没接线"与"没命中"。"""
    logs = boot(Settings(study_lookup_enabled=True)).logs
    assert next(e for e in logs if e["event"] == "federation")["signal_layer"] is True
