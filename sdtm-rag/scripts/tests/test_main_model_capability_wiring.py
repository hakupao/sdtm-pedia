"""main.py 生产启动路径上的模型能力注册 / C3 告警接线锁 (终审 I-2)。

漏在这里的表现是完全静默的: 服务照常起, 答题照常出结果 —— 只是 GPT 系模型的
tool 能力从没注册 (spec §4.2 原话: 「一切正常, 直到有人开联网」), 而 C3 的
"钱走谁的账"告警永远报"全部合规"。

终审实测: 把 lifespan 里这两处接线整块换成空列表, **全量 1922 passed 无一变红**
⇒ spec §8 的闸 4、闸 6 与 §4.2 启动期自检, 三条全部只测了纯函数, 没测生产调用点。

故两个方向都锁, 且尽量锁**事实**而非"某函数被调用过":
- 注册: 用一个全仓库别处从未注册过的假 bedrock key 开机, 看 litellm 的世界变没变;
- C3 / 自检: 看 ready 日志真的带上了那两个字段, 且内容随配置变化。

写法与协作者 stub 沿用 test_main_signal_wiring.py (同一条 lifespan)。
"""
from __future__ import annotations

import asyncio
from types import SimpleNamespace

import litellm
import pytest
import structlog
from fastapi import FastAPI

from server import main as main_mod
from server.config import Settings, SelectableModel

# 全部走 bedrock/ 的一套内部组 —— 生产 .env 改写后的样子。不写成 Settings() 是因为
# config.py 顶层 load_dotenv() 会把本机 .env 灌进 os.environ, 那样测试结论会随机器变。
_ALL_BEDROCK = dict(
    default_model="bedrock/converse/global.anthropic.claude-opus-5",
    hard_model="bedrock/converse/global.anthropic.claude-opus-5",
    light_model="bedrock/converse/global.anthropic.claude-haiku-4-5",
)


def _settings(**kw) -> Settings:
    """联邦/S2 一律关掉 —— 本文件只关心 llm_router 那几行, 别把 study 那半条 lifespan
    也拖进来 (它有自己的三个接线锁)。"""
    return Settings(**{**_ALL_BEDROCK, "federation_enabled": False,
                       "study_lookup_enabled": False, "study_docs_enabled": False,
                       # 研读包也属 study 那半条 lifespan; 且本文件替换 selectable_models,
                       # 会触发 dossier_auto_attach_models 的未知 id 拒启动 (与本文件关注点无关).
                       "dossier_enabled": False, **kw})


def _probe_model(name: str) -> SelectableModel:
    """一个别处从未注册过的假 Bedrock 模型。key 唯一, 故"注册生效了没有"这件事
    不会被同进程里其它测试注册过的真模型污染。"""
    return SelectableModel(id=name, label=name,
                           model=f"bedrock/converse/global.openai.gpt-9.9-{name}",
                           verified=False)


def _probe_key(name: str) -> str:
    return f"converse/global.openai.gpt-9.9-{name}"


def _supported(name: str) -> bool:
    return litellm.supports_function_calling(model=_probe_key(name),
                                             custom_llm_provider="bedrock_converse")


@pytest.fixture
def boot(monkeypatch):
    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            self.collection = FakeCollection()

        def _vi_section_map(self):
            return {}

    monkeypatch.setattr(main_mod, "RAGEngine", FakeEngine)
    monkeypatch.setattr(main_mod, "create_router", lambda *a, **k: None)
    monkeypatch.setattr(main_mod, "maybe_build_answerer", lambda s: None)
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
        return SimpleNamespace(logs=logs, app=app)

    return _run


def _ready(logs) -> dict:
    return next(e for e in logs if e["event"] == "ready")


# ── 闸 4: 工具能力注册的调用点 ───────────────────────────────────────────

def test_lifespan_actually_registers_selectable_model_capabilities(boot):
    """事实层, 不是"函数被调用过": 开机前这个 key 在 litellm 眼里不支持 tools,
    开机后必须支持。删掉 lifespan 里那一行 ⇒ 世界没变 ⇒ 红。

    注册没上线的表现是静默的 —— bedrock allowlist 不认 openai.*, 拒收 tools,
    联网通道对 GPT 直接不可用, 而这在有人开联网之前一点症状都没有 (spec §4.2)。"""
    probe = _probe_model("wiring-register")
    assert not _supported("wiring-register"), "前提破了: 这个 key 已被别处注册过"
    boot(_settings(selectable_models=[probe]))
    assert _supported("wiring-register"), "lifespan 没有注册可选模型的工具能力"


# ── 闸 6 (C3): 非 Bedrock 告警的调用点 ──────────────────────────────────

def test_ready_log_reports_non_bedrock_models(boot):
    """闸 6 的产物是**每次启动的一条观测记录**, 不是一个纯函数的返回值。
    这里钉的就是那条记录: 配置里有非 Bedrock 的答题模型时, ready 日志必须点名它,
    且另发一条 warning。"""
    r = boot(_settings(light_model="anthropic/claude-haiku-4-5",
                       selectable_models=[
                           SelectableModel(id="x", label="X",
                                           model="anthropic/claude-opus-5", verified=False)]))
    assert _ready(r.logs)["non_bedrock_models"] == ["light", "x"]
    warn = next(e for e in r.logs if e["event"] == "models_not_on_bedrock")
    assert warn["log_level"] == "warning"
    assert warn["models"] == ["light", "x"]


def test_ready_log_is_quiet_when_every_model_is_on_bedrock(boot):
    """反方向: 只钉"会报"的话, 把这行写成恒返回一串组名也全绿, 而那是条恒响的
    假警报。生产 .env 下这个字段必须是空列表, 且不发 warning。"""
    r = boot(_settings(selectable_models=[_probe_model("wiring-quiet")]))
    assert _ready(r.logs)["non_bedrock_models"] == []
    assert not [e for e in r.logs if e["event"] == "models_not_on_bedrock"]


# ── spec §4.2: 启动期自检的调用点 ───────────────────────────────────────

def test_ready_log_reports_capability_registration_failure(boot, monkeypatch):
    """自检的调用点。把注册换成 no-op 模拟"注册静默无效"(实测里带 bedrock/ 前缀的
    key 注册就是这样), 自检必须在 ready 日志里点名没生效的模型并发 warning。

    ⚠ 注册被 no-op 掉是**故意**的: 自检的全部价值就在于"注册跑过 ≠ 生效",
    所以它必须能在注册什么都没做的时候仍然报出来。"""
    monkeypatch.setattr(main_mod, "register_selectable_model_capabilities", lambda s: None)
    r = boot(_settings(selectable_models=[_probe_model("wiring-verify")]))
    assert _ready(r.logs)["capability_registration_failed"] == ["wiring-verify"]
    warn = next(e for e in r.logs
                if e["event"] == "selectable_model_capability_registration_failed")
    assert warn["log_level"] == "warning"


def test_ready_log_capability_field_is_empty_on_a_healthy_boot(boot):
    """反方向: 注册正常时自检必须闭嘴 —— 否则它是条恒响的假警报, 与没有一样。"""
    r = boot(_settings(selectable_models=[_probe_model("wiring-healthy")]))
    assert _ready(r.logs)["capability_registration_failed"] == []
    assert not [e for e in r.logs
                if e["event"] == "selectable_model_capability_registration_failed"]
