"""main.py 生产启动路径上的 S2 (study_lookup) 接线锁 + 可见性锁 (Plan B Phase 2 Task 5)。

run_eval 的闸只管评测通道; 生产服务走的是 lifespan。接线漏在这里的表现是完全静默的
——服务照常起, study 侧只是回到纯 cosine。所以"开关开着确实注入 study 引擎"和"开关
关着一定不注入"两个方向都要锁, 日志能不能看出 S2 加载了什么也要锁。

lifespan 的重协作者 (RAGEngine/SpecLoader/GraphEngine/陈旧闸) 全部 stub, 不碰 chroma、
不读 knowledge_base、不发 embedding。
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


class _FakeLookup:
    """条数刻意用不寻常的值: 日志若把条数写死成常量, 断言立刻对不上。"""

    def __init__(self, n_items: int = 7, n_aliases: int = 0):
        self.n_items = n_items
        self.n_aliases = n_aliases

    def stats(self) -> str:
        return f"{self.n_items} items/{self.n_aliases} aliases"


@pytest.fixture
def boot(monkeypatch):
    """跑完整 lifespan (重协作者全 stub), 返回引擎构造实参与捕获到的日志事件。"""
    engines: list[dict] = []

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            engines.append(kwargs)
            self.collection = FakeCollection()
            self.vi_map_calls = 0

        def _vi_section_map(self):
            # lifespan 在 structured_lookup 开着时预热 S1 的 VI section 映射, 好让部署
            # 路径错配在启动期就炸 (而不是每个 CT 码问句 502)。stub 必须实现这个接口。
            self.vi_map_calls += 1
            return {"C99073": "§三 CT 交叉引用: C99073", "ARM": "§一 通用变量: ARM"}

    monkeypatch.setattr(main_mod, "RAGEngine", FakeEngine)
    monkeypatch.setattr(main_mod, "create_router", lambda *a, **k: None)
    monkeypatch.setattr(main_mod, "maybe_build_answerer", lambda s: None)
    monkeypatch.setattr(federation_mod, "FederatedEngine", lambda *a, **k: object())
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
        return SimpleNamespace(engines=engines, logs=logs, app=app)

    return _run


@pytest.fixture
def fake_lookup(monkeypatch):
    """StudyLookup.from_paths → 假货; recorded 为空即代表根本没被调用。"""
    recorded: dict = {}
    lookup = _FakeLookup()

    def _fake(catalog_path, aliases_path):
        recorded["catalog"] = catalog_path
        recorded["aliases"] = aliases_path
        return lookup

    monkeypatch.setattr(
        study_lookup_mod.StudyLookup, "from_paths", staticmethod(_fake)
    )
    return lookup, recorded


def _event(logs, name):
    return next(e for e in logs if e["event"] == name)


def test_enabled_injects_study_lookup_into_study_engine(boot, fake_lookup):
    lookup, recorded = fake_lookup
    # doc 通道显式关掉: 本条量的是 S2 挂在**哪台**引擎上, 二台引擎的世界最直白。
    # (U2 把 study_docs_enabled 默认翻成 True 后, 不关则多出第三台 docs 引擎。)
    s = Settings(study_lookup_enabled=True, study_docs_enabled=False)
    cdisc, study = boot(s).engines
    assert study["study_lookup"] is lookup
    # 路径必须来自 settings, 否则 SDTM_RAG_STUDY_CATALOG_PATH 覆盖形同虚设
    assert recorded["catalog"] == s.study_catalog_path
    assert recorded["aliases"] == s.study_aliases_path
    # S2 是 study 侧通道; 挂到 cdisc 引擎上会撞 RAGEngine 的 S1/S2 互斥闸
    assert cdisc.get("study_lookup") is None
    # ↓ 这行不是搭车断言, 重构 S2 时别删。S1 的 VI section 映射预热落地后, 丢掉这把锁
    # 的后果从"study 侧静默退化"升级成了"启动即崩" —— study collection 里 VI 行数为 0,
    # 真给 study 引擎开了 S1, 预热会 raise 而服务永远起不来。
    assert study["structured_lookup_enabled"] is False


def test_disabled_injects_nothing(boot, fake_lookup):
    _, recorded = fake_lookup
    cdisc, study = boot(
        Settings(study_lookup_enabled=False, study_docs_enabled=False)   # 同上, 二台引擎
    ).engines
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


# ---- 可见性 (fix round 1): 别名 0 条必须在日志里看得见 ----

def test_federation_log_reports_loaded_counts(boot, fake_lookup):
    """别名表缺失是静默降级 —— 条数是唯一能区分"加载成功"与"0 条空转"的现场线索."""
    logs = boot(Settings(study_lookup_enabled=True)).logs
    assert _event(logs, "federation")["study_lookup"] == "7 items/0 aliases"


def test_ready_log_reports_loaded_counts(boot, fake_lookup):
    logs = boot(Settings(study_lookup_enabled=True)).logs
    assert _event(logs, "ready")["study_lookup"] == "7 items/0 aliases"


def test_counts_come_from_the_lookup_object(boot, monkeypatch):
    """换一个规模, 日志数字必须跟着变 (不是写死的常量)."""
    monkeypatch.setattr(
        study_lookup_mod.StudyLookup, "from_paths",
        staticmethod(lambda c, a: _FakeLookup(n_items=41, n_aliases=5)),
    )
    logs = boot(Settings(study_lookup_enabled=True)).logs
    assert _event(logs, "ready")["study_lookup"] == "41 items/5 aliases"
    assert _event(logs, "federation")["study_lookup"] == "41 items/5 aliases"


def test_logs_report_off_when_disabled(boot):
    logs = boot(Settings(study_lookup_enabled=False)).logs
    assert _event(logs, "federation")["study_lookup"] == "OFF"
    assert _event(logs, "ready")["study_lookup"] is False


def test_federation_off_with_lookup_on_warns(boot, fake_lookup):
    """S2 只挂在联邦的 study 引擎上。关了联邦还开着 S2 = 静默空转, 必须留声。"""
    _, recorded = fake_lookup
    logs = boot(
        Settings(study_lookup_enabled=True, federation_enabled=False)
    ).logs
    warn = _event(logs, "study_lookup_ignored")
    assert warn["log_level"] == "warning"
    assert recorded == {}, "没有 study 引擎可挂时不该去读 catalog"


def test_federation_on_does_not_warn(boot, fake_lookup):
    logs = boot(Settings(study_lookup_enabled=True)).logs
    assert not [e for e in logs if e["event"] == "study_lookup_ignored"]


def test_federation_off_without_lookup_does_not_warn(boot):
    logs = boot(Settings(study_lookup_enabled=False, federation_enabled=False)).logs
    assert not [e for e in logs if e["event"] == "study_lookup_ignored"]


# ---- S1 VI section 映射的启动期预热 (审查 HIGH-1) -----------------------------


def test_startup_preheats_vi_section_map(boot, fake_lookup):
    """S1 开着时 lifespan 必须预热 VI section 映射。

    映射依赖 chroma 元数据里的 source 绝对路径与 kb_root 对得上。deploy.sh 把
    data/chroma 与 knowledge_base 一起拷到新目录时, chroma 里存的仍是构建树的路径 →
    映射为空。若留到请求期才炸, 每个 CT 码/分布类问句都 502 (v3 140 题里 71 题走这条
    路), 运维只看到"偶发 502"; 预热则让 launchd 启动即失败, 写进 api.launchd.log。
    删掉预热不会让任何功能测试变红 —— 所以这条锁必须存在。"""
    r = boot(Settings(structured_lookup_enabled=True))
    assert r.app.state.rag.vi_map_calls == 1
    assert _event(r.logs, "s1_vi_section_map")["entries"] == 2


def test_startup_skips_preheat_when_s1_off(boot, fake_lookup):
    # S1 关着时 VI 映射根本用不到, 预热它等于凭空引入一条启动期失败源
    r = boot(Settings(structured_lookup_enabled=False))
    assert r.app.state.rag.vi_map_calls == 0
    assert not [e for e in r.logs if e["event"] == "s1_vi_section_map"]
