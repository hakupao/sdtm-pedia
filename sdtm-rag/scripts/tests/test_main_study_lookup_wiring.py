"""main.py 生产启动路径上的 S2 (study_lookup) 接线锁 (Plan B Phase 2 Task 5)。

run_eval 的闸只管评测通道; 生产服务走的是 lifespan。接线漏在这里的表现是完全静默的
——服务照常起, study 侧只是回到纯 cosine。所以"开关开着确实注入 study 引擎"和"开关
关着一定不注入"两个方向都要锁。

lifespan 在造完两台引擎后还要建 SpecLoader / GraphEngine / 陈旧闸 (都读真实数据),
与本测试无关, 故用 FederatedEngine 抛哨兵异常在两台引擎造好之后立即中断启动。
"""
from __future__ import annotations

import asyncio

import pytest
from fastapi import FastAPI

from server import federation as federation_mod
from server import main as main_mod
from server import study_lookup as study_lookup_mod
from server.config import Settings


class _StopBootError(Exception):
    """两台引擎已构造完毕 —— 后面的启动步骤与本测试无关, 到此为止。"""


@pytest.fixture
def boot(monkeypatch):
    """跑 lifespan 到联邦层为止; 返回按构造顺序排列的引擎 kwargs (cdisc, study)."""
    calls: list[dict] = []

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            calls.append(kwargs)
            self.collection = FakeCollection()

    def _stop(*a, **k):
        raise _StopBootError

    monkeypatch.setattr(main_mod, "RAGEngine", FakeEngine)
    monkeypatch.setattr(main_mod, "create_router", lambda *a, **k: None)
    monkeypatch.setattr(federation_mod, "FederatedEngine", _stop)

    def _run(app_settings: Settings) -> list[dict]:
        app = FastAPI()
        app.state.settings = app_settings

        async def _enter():
            async with main_mod.lifespan(app):
                pass

        with pytest.raises(_StopBootError):
            asyncio.run(_enter())
        assert len(calls) == 2, "federation 开着必须构造 cdisc + study 两台引擎"
        return calls

    return _run


@pytest.fixture
def fake_lookup(monkeypatch):
    """StudyLookup.from_paths → 哨兵; recorded 为空即代表根本没被调用。"""
    recorded: dict = {}
    sentinel = object()

    def _fake(catalog_path, aliases_path):
        recorded["catalog"] = catalog_path
        recorded["aliases"] = aliases_path
        return sentinel

    monkeypatch.setattr(
        study_lookup_mod.StudyLookup, "from_paths", staticmethod(_fake)
    )
    return sentinel, recorded


def test_enabled_injects_study_lookup_into_study_engine(boot, fake_lookup):
    sentinel, recorded = fake_lookup
    cdisc, study = boot(Settings(study_lookup_enabled=True))
    assert study["study_lookup"] is sentinel
    # 路径必须来自 settings, 否则 SDTM_RAG_STUDY_CATALOG_PATH 覆盖形同虚设
    s = Settings(study_lookup_enabled=True)
    assert recorded["catalog"] == s.study_catalog_path
    assert recorded["aliases"] == s.study_aliases_path
    # S2 是 study 侧通道; 挂到 cdisc 引擎上会撞 RAGEngine 的 S1/S2 互斥闸
    assert cdisc.get("study_lookup") is None
    assert study["structured_lookup_enabled"] is False


def test_disabled_injects_nothing(boot, fake_lookup):
    _, recorded = fake_lookup
    cdisc, study = boot(Settings(study_lookup_enabled=False))
    assert study.get("study_lookup") is None
    assert cdisc.get("study_lookup") is None
    assert recorded == {}, "开关关着却读了 catalog = 开关没接上"


def test_enabled_with_missing_catalog_fails_loud(boot, tmp_path):
    """开关开着但 catalog 不在 = 配置错误。静默退回 cosine 比启动失败更危险。"""
    s = Settings(
        study_lookup_enabled=True,
        study_catalog_path=tmp_path / "nope.json",
        study_aliases_path=tmp_path / "nope.yml",
    )
    with pytest.raises(FileNotFoundError):
        boot(s)
