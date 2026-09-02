"""多模型切换 (U1) 的闸。spec docs/superpowers/specs/2026-09-01-model-switching-design.md"""
import json
import re
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings, SelectableModel
from server.router import api_router


def test_selectable_models_defaults():
    """四个候选全部在, 且 id 唯一 —— id 是 Router 组名与前端提交值的共用键,
    重复会让 Router 后写覆盖先写而 UI 毫无察觉。"""
    s = Settings()
    ids = [m.id for m in s.selectable_models]
    assert ids == ["opus-5", "sonnet-5", "gpt-terra", "gpt-sol"]
    assert len(set(ids)) == len(ids)


def test_selectable_models_all_on_bedrock():
    """C3: GPT 与 Claude 不得走用户个人 API。"""
    s = Settings()
    for m in s.selectable_models:
        assert m.model.startswith("bedrock/"), f"{m.id} 不走 Bedrock: {m.model}"


def test_only_opus5_is_verified():
    """verified 语义 = 该模型跑过反捏造抽检并通过。目前只有 opus-5 验过 ——
    sonnet-5 是 Claude 不代表验过, 两个方向都钉住, 免得有人顺手全填 true。"""
    s = Settings()
    v = {m.id: m.verified for m in s.selectable_models}
    assert v["opus-5"] is True
    assert v["sonnet-5"] is False
    assert v["gpt-terra"] is False
    assert v["gpt-sol"] is False


def _group_names(router):
    """Router 已知的组名集合。model_list 是构造时传入的那份, 逐项取 model_name。"""
    return {m["model_name"] for m in router.model_list}


def test_router_derives_a_group_per_selectable_model():
    from server.llm_config import create_router
    s = Settings()
    names = _group_names(create_router(s))
    for m in s.selectable_models:
        assert m.id in names, f"Router 缺少组 {m.id}"


def test_router_keeps_internal_groups():
    """C1: 判库(light)/hard/default 是内部用途, 不受用户选择影响, 必须仍在。"""
    from server.llm_config import create_router
    names = _group_names(create_router(Settings()))
    assert {"default", "default-fallback", "hard", "light"} <= names


def test_known_groups_equals_what_router_actually_has():
    """裁定 F-1 的补偿闸: 给『校验端读 known_model_groups (意图)』与『Router 是事实』
    这层关系上闸, 二者必须逐项相等。不需要任何假 Router。

    这条**不防派生逻辑本身漂移**: 若 create_router 与 known_model_groups 两处同时
    手滑把 m.id 写成 m.label, 两边算出来的错法一致, 本测试照绿。真正锚定字面量、
    防住这种 co-drift 的是 test_router_derives_a_group_per_selectable_model 和
    test_router_group_maps_to_the_configured_model_string。"""
    from server.llm_config import create_router, known_model_groups
    s = Settings()
    assert known_model_groups(s) == {m["model_name"] for m in create_router(s).model_list}
    assert len(known_model_groups(s)) >= 8, "抽取端失效: 集合为空时上面的等式恒真"


def test_router_group_maps_to_the_configured_model_string():
    """方向钉: 组名对了但指向错模型, 上面两条照样绿。"""
    from server.llm_config import create_router
    s = Settings()
    by_name = {m["model_name"]: m["litellm_params"]["model"] for m in create_router(s).model_list}
    for m in s.selectable_models:
        assert by_name[m.id] == m.model


def test_create_router_succeeds_when_no_id_collision():
    """两个方向之一: 默认配置的 id 不撞内部组, 正常构造不该被误伤。"""
    from server.llm_config import create_router
    create_router(Settings())  # 不应抛


def test_create_router_raises_on_internal_group_collision():
    """另一个方向: selectable id 撞上 INTERNAL_GROUPS (如 "light") 时必须 fail-loud。

    litellm Router 允许同一 model_name 出现两次并当同一组的多个 deployment 做
    load-balance —— 撞名会让判库(light)悄悄混进用户选的答题模型, 静默打破 C1,
    且没有任何既有测试会变红。selectable_models 还能被 SDTM_RAG_SELECTABLE_MODELS
    在运行时注入, 只挡默认配置不够, 必须在构造时就拒绝。"""
    from server.llm_config import create_router
    s = Settings(selectable_models=[
        SelectableModel(id="light", label="撞名", model="bedrock/x", verified=False),
    ])
    with pytest.raises(ValueError, match="light"):
        create_router(s)


def test_known_model_groups_raises_on_internal_group_collision():
    """同一防线在 known_model_groups 这条路径上也要生效 —— Task 5 的白名单校验
    走的正是这个函数, 不经过 create_router。"""
    from server.llm_config import known_model_groups
    s = Settings(selectable_models=[
        SelectableModel(id="hard", label="撞名", model="bedrock/x", verified=False),
    ])
    with pytest.raises(ValueError, match="hard"):
        known_model_groups(s)


def test_registration_makes_tools_supported_for_gpt():
    """LiteLLM 1.88.1 的 bedrock allowlist 不认 openai.*, 不注册就拒收 tools ——
    联网通道对 GPT 直接不可用。裸 boto3 已实测工具调用本身通 ⇒ 这是客户端元数据缺口。
    ⚠ 注册 key 必须**去掉 bedrock/ 前缀**, 用错前缀是静默无效 (spec §4.2)。"""
    import litellm
    from server.llm_config import register_selectable_model_capabilities
    register_selectable_model_capabilities(Settings())
    for mid in ["converse/global.openai.gpt-5.6-terra", "converse/global.openai.gpt-5.6-sol"]:
        assert litellm.supports_function_calling(model=mid, custom_llm_provider="bedrock_converse")


def _class_default(field: str) -> str:
    """字段的**类默认值** —— 即 config.py 里写死的那个串。

    ⚠ 不能用 `Settings().<field>`: config.py 顶层 `load_dotenv()` 把本机 .env 灌进了
    os.environ, 所以 `Settings()` 拿到的是**这台机器**的 .env 值 (实测本机是 bedrock/)。
    闸 6 要防的恰恰是 ".env 缺失/被覆盖" 那个世界, 而那个世界里生效的正是类默认值。
    读默认值让本组测试与本机 .env 解耦 —— 否则换台机器测试结论就变。
    """
    return Settings.model_fields[field].default


_ALL_BEDROCK = dict(
    default_model="bedrock/converse/global.anthropic.claude-opus-5",
    hard_model="bedrock/converse/global.anthropic.claude-opus-5",
    light_model="bedrock/converse/global.anthropic.claude-haiku-4-5",
)
_ENV_LESS = {f: _class_default(f) for f in ("default_model", "hard_model", "light_model")}


def test_c3_gate_covers_the_three_hardcoded_claude_models():
    """闸 6 (C3) 的**主要**目标就是 config.py 里 default/hard/light 那三个硬编码默认值
    (`anthropic/` 直连, 只靠 .env 改写且无任何启动期校验) —— spec §8 闸 6 的脚注点名的
    正是它们。终审 I-1: 老实现只扫 selectable_models, 而那四条硬编码全是 `bedrock/`,
    于是默认配置下返回值恒为 [], 结构上不可能报警。

    场景 = ".env 缺失/后段被删/两段顺序一换" ⇒ 三个内部组回落到类默认值。"""
    from server.llm_config import non_bedrock_model_groups
    # 前提自证: 这三个类默认值今天确实是 anthropic/ 直连。前提一变本组测试就该重写,
    # 而不是安静地测一个已经不存在的风险。
    assert all(v.startswith("anthropic/") for v in _ENV_LESS.values()), _ENV_LESS
    assert non_bedrock_model_groups(Settings(**_ENV_LESS)) == ["default", "hard", "light"]


def test_c3_gate_is_quiet_when_everything_is_on_bedrock():
    """反方向: 只测"会报"的话, 把函数写成恒返回三个组名也全绿。生产 .env 把这三个
    改写成 bedrock/ 之后, 闸必须闭嘴 —— 否则就是一条长期喊狼来了的告警。"""
    from server.llm_config import non_bedrock_model_groups
    assert non_bedrock_model_groups(Settings(**_ALL_BEDROCK)) == []


def test_c3_gate_reports_a_single_drifted_model():
    """逐个方向: 三个里只坏一个时必须精确报出是哪一个 —— 报全部或报空都会让运维
    看着日志找不到该改哪一行。"""
    from server.llm_config import non_bedrock_model_groups
    s = Settings(**{**_ALL_BEDROCK, "light_model": "anthropic/claude-haiku-4-5"})
    assert non_bedrock_model_groups(s) == ["light"]


def test_c3_gate_excludes_the_fallback_model():
    """spec §9 D4: fallback 走 DeepSeek 个人流量是用户明确裁定接受的。fallback_model 的
    类默认值就是 deepseek/, 若把它纳入检查, 这条告警在任何配置下都恒响 = 等于没有告警。"""
    from server.llm_config import non_bedrock_model_groups
    assert _class_default("fallback_model").startswith("deepseek/"), "前提变了, 本测试要重写"
    s = Settings(**_ALL_BEDROCK, fallback_model=_class_default("fallback_model"))
    assert non_bedrock_model_groups(s) == []


def test_c3_gate_still_covers_selectable_models():
    """selectable 那半边不能因为补了内部三组就丢: 两类模型走同一条 C3 约束。"""
    from server.llm_config import non_bedrock_model_groups
    bad = Settings(**_ALL_BEDROCK, selectable_models=[
        {"id": "x", "label": "X", "model": "anthropic/claude-opus-5", "verified": False}])
    assert non_bedrock_model_groups(bad) == ["x"]


def test_every_internal_group_has_a_c3_field_mapping():
    """新增内部组却忘了往 _INTERNAL_GROUP_MODEL_FIELDS 加一行, 表现是 KeyError 当场炸在
    启动路径上 (刻意的, 好过静默漏检)。这条测试把它提前到 CI —— 别让人在生产启动时才知道。"""
    from server.llm_config import INTERNAL_GROUPS, _INTERNAL_GROUP_MODEL_FIELDS
    assert set(_INTERNAL_GROUP_MODEL_FIELDS) == set(INTERNAL_GROUPS)
    s = Settings()
    for field in _INTERNAL_GROUP_MODEL_FIELDS.values():
        assert isinstance(getattr(s, field), str), f"{field} 不是模型串字段"


def test_verify_reports_empty_after_successful_registration():
    """spec §4.2 启动期自检: register 之后回查, 正常路径必须为空 —— 既包括注册后
    变 True 的 GPT 系, 也包括在 litellm bedrock allowlist 里原生就是 True 的 Claude
    系 (不注册也通过 allowlist)。两类模型都不该被自检误报。"""
    from server.llm_config import (
        register_selectable_model_capabilities,
        verify_selectable_model_capabilities,
    )
    s = Settings()
    register_selectable_model_capabilities(s)
    assert verify_selectable_model_capabilities(s) == []


def test_verify_flags_a_model_whose_registration_never_happened():
    """自检真的会抓: 用一个专造的、别处从未注册过的 bedrock key (不依赖源码变异,
    也不依赖测试执行顺序) 验证 supports_function_calling 仍为 False 时会被 flag。
    这是"注册未生效"在自检里的直接复现 —— 与控制器实测的『去掉 removeprefix 导致
    静默无效』是同一条检测路径, 只是不需要真的改坏源码就能钉住。"""
    from server.llm_config import verify_selectable_model_capabilities
    s = Settings(selectable_models=[
        SelectableModel(id="never-registered", label="从未注册",
                         model="bedrock/converse/global.openai.gpt-9.9-never-registered",
                         verified=False),
    ])
    assert verify_selectable_model_capabilities(s) == ["never-registered"]


def test_verify_does_not_let_a_natively_true_model_mask_a_broken_one():
    """Claude 天然 True; 若 verify 是"存在一个 True 即通过", 混一个天然 True 的
    Claude 与一个从未注册的假 bedrock 模型会让后者被掩盖。同一个 Settings 里
    混装两者, 专门钉这条(与两条现有新测试互补, 它们都没测到这个组合)。"""
    from server.llm_config import verify_selectable_model_capabilities
    s = Settings(selectable_models=[
        SelectableModel(id="opus-5", label="Claude Opus 5",
                         model="bedrock/converse/global.anthropic.claude-opus-5",
                         verified=True),
        SelectableModel(id="never-registered", label="从未注册",
                         model="bedrock/converse/global.openai.gpt-9.9-never-registered",
                         verified=False),
    ])
    assert verify_selectable_model_capabilities(s) == ["never-registered"]


def _info_client(**kw):
    """/api/info 只读 rag/settings 上的几个属性, 最小 stub 即可 (照
    test_web_search_config.py 的既有写法), 不碰 chroma/embedding。"""
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = SimpleNamespace(
        collection=SimpleNamespace(count=lambda: 1),
        structured_lookup_enabled=True, hybrid_enabled=True, hybrid_fusion="rrf",
        prompt_guardrail_enabled=True, web_search_enabled=True,
    )
    app.state.settings = Settings(**kw)
    return TestClient(app)


def test_info_exposes_selectable_models_with_verified():
    got = _info_client().get("/api/info").json()["selectable_models"]
    assert [m["id"] for m in got] == ["opus-5", "sonnet-5", "gpt-terra", "gpt-sol"]
    by_id = {m["id"]: m for m in got}
    assert by_id["opus-5"]["verified"] is True
    assert by_id["gpt-sol"]["verified"] is False
    assert by_id["opus-5"]["label"] == "Claude Opus 5"


def test_info_model_table_is_subset_of_router_groups():
    """闸 3: 结构上杜绝「UI 提供了 Router 没有的模型」。这条是本设计选方案 C 的理由,
    必须有闸兜住 —— 派生逻辑将来被改坏时它要响。"""
    from server.llm_config import create_router
    s = Settings()
    exposed = {m["id"] for m in _info_client().get("/api/info").json()["selectable_models"]}
    assert exposed <= {m["model_name"] for m in create_router(s).model_list}
    assert len(exposed) >= 4, "抽取端失效: 暴露的模型表为空时上面的子集断言恒真"


class _FakeRAG:
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return [SimpleNamespace(chunk_id="c1", source="domains/AE/spec.md", domain="AE",
                                file_type="spec", section="§1", similarity=0.9,
                                text="AETERM is the reported term." * 5)]
    def format_context(self, chunks):
        return "CTX"
    def build_messages(self, q, ctx, history=None):
        return [{"role": "user", "content": q}]


class _CapturingRouter:
    """记下**实际**传给 acompletion 的组名与**整份** kwargs。

    校验通过 ≠ 真的用了那个模型 —— 少了这一层, 把 kw 里的组名写死成 "default"
    也能让"接受每个模型"的测试全绿 (记事实不记意图)。

    `calls` 存整份调用实参 (含 model/messages/stream 三个具名形参): 闸 2 写的是
    "请求体逐位相同", 只记组名的话往 kw 里无条件插一个 temperature 全量都不会红
    (终审 M-2 实测), 闸名就说大了。
    """

    def __init__(self):
        self.last_model = None
        self.calls: list[dict] = []

    async def acompletion(self, model, messages, stream=False, **kw):
        self.last_model = model
        self.calls.append({"model": model, "messages": messages, "stream": stream, **kw})

        async def agen():
            yield SimpleNamespace(model=f"resolved-{model}", usage=None,
                                  choices=[SimpleNamespace(delta=SimpleNamespace(content="ok"))])
            yield SimpleNamespace(model=f"resolved-{model}", choices=[],
                                  usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1,
                                                        total_tokens=2))
        return agen()


def _stream_client(router=None):
    s = Settings()
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router if router is not None else _CapturingRouter()
    app.state.settings = s
    return TestClient(app)


class _EchoModelRouter:
    """回一个**固定**的模型串, 与请求的组名无关 —— 模拟 "Router 换了别的 deployment"。

    为什么不能只用 `_CapturingRouter`: 它回的是 `resolved-{组名}`, **跟着组名走**。
    只有它的话, 把 `model_used` 实现成 `body.model` 的某种变形也可能蒙混过关。
    这个类把"事实"与"意图"彻底解耦: 请求 gpt-sol、回 deepseek-v4-pro。

    `reported=None` 用来造"chunk 压根没报模型"那一档 (getattr 取到 None)。
    """

    def __init__(self, reported: str | None = "deepseek-v4-pro"):
        self.reported = reported
        self.last_model = None

    async def acompletion(self, model, messages, stream=False, **kw):
        self.last_model = model
        reported = self.reported

        async def agen():
            yield SimpleNamespace(model=reported, usage=None,
                                  choices=[SimpleNamespace(delta=SimpleNamespace(content="ok"))])
        return agen()


def test_ask_stream_rejects_unknown_model():
    """白名单外 → 422。⛔ 不得静默退回 default —— 静默退回正是本仓库反复栽的形状
    (参见 AskRequest 的 extra=forbid 注释所记的抽检事故)。"""
    c = _stream_client()
    r = c.post("/api/ask_stream", json={"question": "AETERM?", "model": "gpt-9000"})
    assert r.status_code == 422, r.text
    assert "gpt-9000" in r.text or "model" in r.text


def test_ask_stream_accepts_every_selectable_model():
    """反方向: 只测拒绝的话, 把校验写成"一律 422"也能绿。"""
    c = _stream_client()
    for m in Settings().selectable_models:
        r = c.post("/api/ask_stream", json={"question": "AETERM?", "model": m.id})
        assert r.status_code == 200, f"{m.id}: {r.text}"


_BASE_CALL_KEYS = {"model", "messages", "stream", "stream_options"}


def test_ask_stream_default_is_unchanged():
    """闸 2 (spec §5「不传 model 时请求体与今日**逐位相同**」)。

    ⚠ 只断组名不算数: 终审 M-2 在 `_open_stream` 的 kw 构造后无条件插了一行
    `kw["temperature"] = 0.7`, 全量 1922 无一变红 —— 闸名写的是"逐位相同", 实际只
    钉了一个字段。这里钉**整份** kwargs: 键集合恰好这四个 (多一个少一个都红), 值也
    逐个对上。"""
    c = _stream_client()
    assert c.post("/api/ask_stream", json={"question": "AETERM?"}).status_code == 200
    calls = c.app.state.llm_router.calls
    assert len(calls) == 1, f"开流次数不对: {len(calls)}"
    call = calls[0]
    assert set(call) == _BASE_CALL_KEYS, f"请求体多/少了字段: {sorted(set(call))}"
    assert call["model"] == "default"
    assert call["stream"] is True
    assert call["stream_options"] == {"include_usage": True}
    assert call["messages"] == [{"role": "user", "content": "AETERM?"}]


def test_request_body_gate_actually_sees_an_added_kwarg(monkeypatch):
    """上面那条只有在"捕获端真看得见多出来的 kwarg"时才有意义 —— 否则它是个纸老虎:
    捕获端漏记时键集合恒等于期望集合, 断言恒真。

    这里用生产里唯一会往 kw 加字段的路径 (联网通道加 `tools`) 做活体对照:
    键集合确实增大且**恰好**多 `tools` 一项。⇒ 任何别的新增字段同样会被上面那条抓到。"""
    monkeypatch.setattr("server.router.WebSearcher",
                        lambda s: SimpleNamespace(searches_used=0))
    c = _stream_client()
    assert c.post("/api/ask_stream",
                  json={"question": "AETERM?", "web": True}).status_code == 200
    call = c.app.state.llm_router.calls[0]
    assert set(call) == _BASE_CALL_KEYS | {"tools"}, f"实际键: {sorted(set(call))}"


def _done_event(client, **body):
    """POST 后解析出 done 事件的 JSON。

    ⚠ 先断言确实**只**拿到一个 done 事件再取字段 —— 抽取端失效 (0 个) 时,
    下面所有字段断言都会变成永真式 (retrospective 规则 6 成因 A)。
    """
    text = client.post("/api/ask_stream", json={"question": "AETERM?", **body}).text
    blocks = [b for b in text.split("\n\n") if b.startswith("event: done")]
    assert len(blocks) == 1, f"没解析到唯一的 done 事件: {text[:400]!r}"
    line = next(l for l in blocks[0].splitlines() if l.startswith("data: "))
    return json.loads(line[len("data: "):])


def test_done_event_carries_model_id_and_verified():
    """产物自证 (spec §6): 只做 UI 标注的话, 对话存下来之后这条信息就没了。
    与 2026-09-01 清掉的 B6 同形 —— 产物必须能自证。"""
    ev = _done_event(_stream_client(), model="gpt-sol")
    assert ev["model_id"] == "gpt-sol"
    assert ev["verified"] is False
    ev2 = _done_event(_stream_client(), model="opus-5")
    assert ev2["model_id"] == "opus-5"
    assert ev2["verified"] is True


def test_done_event_verified_is_null_for_default_group():
    """default 组不在 selectable_models 里, 没有 verified 这个概念。
    ⛔ 必须发 null(未知), 不得发 false —— 那会把"没这个概念"误报成"验过且不通过"。"""
    ev = _done_event(_stream_client())          # 不传 model
    assert ev["model_id"] == "default"
    assert ev["verified"] is None


def test_done_event_model_used_is_what_the_router_returned():
    """闸 G1 正向 (spec §6): `model_used` 记的是**事实** —— 实际答题的模型,
    与 `model_id` (意图, = body.model) 是两个东西。

    ⚠ 这个字段在 U1 那轮**整套件零断言** (spec §9 D6)。它今天低风险的唯一原因是
    四个新组还没有 fallback, 事实与意图在结构上不会分叉 —— Task 2 一补 fallback,
    分叉立刻成为活场景, 那时缺断言就从"欠账"变成"漏洞"。
    """
    ev = _done_event(_stream_client(), model="opus-5")
    assert ev["model_used"] == "resolved-opus-5", ev
    # 诱饵: 两个字段必须不相等, 否则这条测试对"回显 model_id"的实现无分辨力
    assert ev["model_used"] != ev["model_id"], ev


def test_done_event_model_used_follows_the_router_not_the_request():
    """闸 G1 反向: Router 交出别的模型时, `model_used` 必须跟着变。

    把实现写成 `"model_used": body.model` (回显意图) 会让这条红 —— 而那正是
    U2 容灾落地后最容易发生的静默错误: 用户选 gpt-sol、DeepSeek 答题、事件却说 gpt-sol。
    """
    c = _stream_client(_EchoModelRouter("deepseek-v4-pro"))
    ev = _done_event(c, model="gpt-sol")
    assert ev["model_used"] == "deepseek-v4-pro", ev
    assert ev["model_id"] == "gpt-sol", ev


def test_done_event_model_used_is_null_when_the_router_reports_nothing():
    """闸 G3: 一个 chunk 都没带 `.model` 时真相是"不知道" ——
    ⛔ 不得发写死的 `"default"`。

    与同一个事件里 `verified` 的裁定同一条原则 (2026-09-01 spec §6:
    「不得把'没这个概念'误报成一个具体值」)。Task 5 会把这个字段**存进
    append-only 的历史存档**, 一个编出来的 "default" 从此永久留档 ——
    正是用户全局规则 B 最贵的那类数据被污染。
    """
    c = _stream_client(_EchoModelRouter(None))
    ev = _done_event(c, model="opus-5")
    assert ev["model_used"] is None, ev


class _SyncCapturingRouter:
    """/api/ask 走的是同步 `completion`, 与 ask_stream 的 `acompletion` 是两个方法。"""

    def __init__(self):
        self.last_model = None

    def completion(self, model, messages, **kw):
        self.last_model = model
        return SimpleNamespace(
            model=f"resolved-{model}", usage=None,
            choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))])


def _ask_client():
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = _SyncCapturingRouter()
    app.state.settings = Settings()
    return TestClient(app)


# 两端点白名单口径的取样点: 四个可选 id + 四个内部组 + 一个白名单外的名字。
_WHITELIST_PROBE = [m.id for m in Settings().selectable_models] + [
    "default", "default-fallback", "hard", "light", "gpt-9000"]


def _verdicts(client, path):
    return {name: client.post(path, json={"question": "AETERM?", "model": name}).status_code
            for name in _WHITELIST_PROBE}


def test_ask_and_ask_stream_agree_on_the_model_whitelist():
    """终审 I-3: 曾经 /api/ask 读一份写死的 {"default","hard","light"}, 而 ask_stream 读
    known_model_groups —— 同一个仓库两个端点对同一个模型名给出相反答案 (实测 opus-5
    在 /api/ask 是 422、在 /api/ask_stream 是 200), 且那份写死清单连 default-fallback
    都没有, 本身已与 Router 不同步。

    /api/info 现在**对外广播**四个 id, 客户端 (`ui/streamlit_app.py`、`viewer/app.js`、
    README 文档化的公开端点) 读了拿去打 /api/ask 就 422。故口径必须逐名一致。

    ⚠ 断的是"两端点判定相同"而不是"两边都 200": 白名单外的名字两边都必须 422,
    这条断言因此同时覆盖接受与拒绝两个方向。"""
    ask, stream = _verdicts(_ask_client(), "/api/ask"), _verdicts(_stream_client(), "/api/ask_stream")
    assert ask == stream, f"两端点口径分叉: {[k for k in ask if ask[k] != stream[k]]}"
    # 尺寸/内容下限: 若两边同时退化成"一律 422"或"一律 200", 上面的等式恒真。
    assert ask["gpt-9000"] == 422, ask
    assert {ask[m.id] for m in Settings().selectable_models} == {200}, ask


def test_ask_actually_dispatches_the_selected_model():
    """与 ask_stream 那条同源: 校验通过 ≠ 真的用了那个模型。"""
    for m in Settings().selectable_models:
        c = _ask_client()
        assert c.post("/api/ask", json={"question": "AETERM?", "model": m.id}).status_code == 200
        assert c.app.state.llm_router.last_model == m.id


def test_ask_rejection_message_lists_the_known_groups():
    """422 的正文要能自证白名单是哪份 —— 分叉时最先被人看到的就是这行。"""
    r = _ask_client().post("/api/ask", json={"question": "AETERM?", "model": "gpt-9000"})
    assert r.status_code == 422, r.text
    assert "gpt-9000" in r.text and "opus-5" in r.text, r.text


def test_ask_stream_actually_dispatches_the_selected_model():
    """闸 Task 5 遗留缺口: `done` 事件的 `model_id` 只是回显 `body.model` (意图),
    不是"Router 真的收到了这个模型" (事实)。若 `ask_stream` 内把传给 `acompletion`
    的 `kw["model"]` 写死回 "default", 上面两条 done 事件测试**测不到**——它们只
    看 `body.model` 有没有被原样塞回 JSON, 与实际派发无关。这里直接钉派发事实:
    `_CapturingRouter.last_model` 必须等于所选的组名, 不能是别的。"""
    for m in Settings().selectable_models:
        c = _stream_client()
        c.post("/api/ask_stream", json={"question": "AETERM?", "model": m.id})
        assert c.app.state.llm_router.last_model == m.id, (
            f"{m.id}: Router 实际收到的是 {c.app.state.llm_router.last_model!r}")


# ── C-1: ⚑ 失败归档必须归到**这条答案实际用的模型** ──────────────────────────

APP_JS = Path(__file__).resolve().parents[2] / "webchat" / "app.js"
_FLAG_PROBE = Path(__file__).resolve().parent / "fixtures" / "flag_attribution_probe.mjs"


@pytest.fixture(scope="module")
def flag_probe():
    """在 node 里真的跑一遍 app.js, 驱动 renderMessages → attachFlag → openFlag →
    postFlag, 返回两个场景实际发给 /api/flag 的请求体 (探针见同名 .mjs 的头注释)。"""
    if shutil.which("node") is None:  # pragma: no cover - 环境缺 node 时的降级
        pytest.skip("node 不在 PATH; 静态闸 test_flag_payload_reads_the_message_model_id 仍在跑")
    r = subprocess.run(["node", str(_FLAG_PROBE)], capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, f"探针跑挂了:\n{r.stderr[-2000:]}"
    return json.loads(r.stdout)


def test_flag_is_attributed_to_the_model_that_actually_answered(flag_probe):
    """终审 C-1: postFlag 曾从 topbar 文本切模型名, 而那是 /api/info 的 default_model,
    与答题模型无关。分支前"唯一答题模型就是 default 组"这个不变量成立, 所以拿它凑合
    是对的; spec §5 裁定"UI 永远发显式 id"之后它被打破, 而 postFlag 没跟着改。

    后果不是信息缺失而是**信息错误**: 用 Sol 提问 → 答案捏造 → 点 ⚑, backlog 把 Sol
    的捏造记到 Opus 5 头上。dogfood_failures.md 是 append-only 的优先级 backlog
    (用户全局规则 B: 失败数据绝不删), 错误写入即永久且无从回溯 —— 读的人无从察觉,
    还可能据此把一轮反捏造工作投到错误的模型上。

    ⚠ 诱饵断言不能省: topbar 此刻确实写着另一个模型名, 若它与答案模型碰巧一样,
    这条测试就什么都没测到。"""
    got = flag_probe["withModelId"]
    assert "claude-opus-5" in got["topbarText"], f"诱饵没摆上, 本测试无效: {got['topbarText']}"
    assert got["flagBody"]["model"] == "GPT-5.6 Sol", got["flagBody"]
    # 徽章与归档必须指同一个模型 —— C2 的安全论证靠的就是这条标注链完整
    # (选项文字 → 常驻提示条 → 答案徽章 → 持久失败记录)。
    assert got["flagBody"]["model"] in got["badgeText"], (got["flagBody"], got["badgeText"])


def test_flag_falls_back_to_the_topbar_for_legacy_records(flag_probe):
    """反方向: 下拉上线前存的历史记录没有 modelId, 那些答案确实产自 default 组,
    退回 topbar 文本是对的。把 model 一律置空/写死会让这条红 —— 不许为了修上一条
    就把旧记录的归因整个丢掉。"""
    got = flag_probe["legacyNoModelId"]
    assert got["badgeText"] is None, "旧记录不该有模型徽章, 场景造错了"
    assert got["flagBody"]["model"] == "global.anthropic.claude-opus-5", got["flagBody"]


def test_flag_payload_reads_the_message_model_id():
    """静态第二重 (与上面的行为闸互补, 照 test_sse_contract.py 的双闸写法):
    node 缺席时行为闸会 skip, 这条不会。断的是**属性读取形状** `.modelId`,
    不是"源码里出现过这个词" —— 注释里的裸词没有前导点, 不会误判为真实读取。"""
    src = APP_JS.read_text(encoding="utf-8")
    body = src.split("function flagModelName", 1)
    assert len(body) == 2, "flagModelName 没了 —— 归因逻辑被搬走或删掉了"
    body = body[1].split("\n}", 1)[0]
    assert re.search(r"\.modelId\b", body), "归因没有读 msgObj.modelId"
