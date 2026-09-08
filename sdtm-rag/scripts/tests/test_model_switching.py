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
from server.llm_config import fell_back
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


def test_verified_flags_match_spotcheck_record():
    """verified 语义 = 该模型跑过反捏造抽检并通过。值钉在 2026-09 兑现抽检的结果表
    (evidence/checkpoints/verified_spotcheck_2026-09.md): opus-5 / gpt-terra / gpt-sol 过,
    sonnet-5 (a) 层 1 条 ungrounded ⇒ false。两个方向都钉住 —— sonnet-5 是 Claude 不代表
    验过, 免得有人顺手全填 true; 改任一值须先有新一轮抽检记录。"""
    s = Settings()
    v = {m.id: m.verified for m in s.selectable_models}
    assert v["opus-5"] is True
    assert v["sonnet-5"] is False
    assert v["gpt-terra"] is True
    assert v["gpt-sol"] is True


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


_FALLBACK_GROUP = "default-fallback"


def _fallbacks(router) -> dict:
    """`Router.fallbacks` 是 list[dict], 摊平成 {组名: [兜底组]}。

    ⚠ 先断尺寸下限: 表塌成空的时候, 下面所有"某组**不在**表里"的断言都会变成
    永真式 (retrospective 规则 6 成因 A)。

    ⚠ 下限**从 Settings 算**, 不写死数字 (终审 Minor 3): 硬编码的 `>= 5` 在加第 5 个
    可选模型时要手改, 而"忘了手改"的表现是下限变松 —— 又是一条悄悄放宽的判定式。
    """
    expected = 1 + len(Settings().selectable_models)      # default + 每个可选模型
    flat = {k: v for entry in router.fallbacks for k, v in entry.items()}
    assert len(flat) >= expected, \
        f"fallback 表塌了 (期望至少 {expected} 条), 下面的断言会变永真: {router.fallbacks}"
    return flat


def test_every_selectable_group_falls_back_to_the_default_fallback_group():
    """闸 G4 (spec §9 D5): U1 那轮 UI 从"永发 default 组"改成"永发显式 id",
    而四个新派生组没有 fallback 条目 ⇒ **主模型没变, 容灾网没了**。
    DEPLOY_PLAN.md 记着实测「Anthropic credits 耗尽 → DeepSeek 自动回退」真的生效过。
    """
    from server.llm_config import create_router
    s = Settings()
    flat = _fallbacks(create_router(s))
    for m in s.selectable_models:
        assert flat.get(m.id) == [_FALLBACK_GROUP], f"{m.id} 没有容灾: {flat.get(m.id)}"
    assert flat["default"] == [_FALLBACK_GROUP], "既有 default 组的容灾不许丢"
    # 钉"**恰好**是这些", 不只是"这些都在" (复审 U11 实测: 往表里多塞一条不存在的组,
    # 44 条全绿)。左边是 Router 的事实、右边是 Settings 的意图, 两次独立计算 ——
    # 不是规则 6 成因 B2 那种"两边一起漂"的形状。
    assert set(flat) == {"default"} | {m.id for m in s.selectable_models}, \
        f"容灾表多/少了组: {sorted(flat)}"


def test_internal_worker_groups_have_no_fallback():
    """闸 G5 反方向 (C1)。"一律给所有组加 fallback" 的偷懒实现会让这条红:

    - `light` 是判库、`hard` 是检索改写 —— C1 明确要求它们**不受用户选择影响**,
      能悄悄换模型就等于破了 C1 (判库换了模型, 检索结果跟着变, 对比时分不清
      是模型差异还是检索差异);
    - `default-fallback` 给自己配 fallback 是个环。
    """
    from server.llm_config import create_router
    flat = _fallbacks(create_router(Settings()))
    for g in ("hard", "light", _FALLBACK_GROUP):
        assert g not in flat, f"{g} 不该有 fallback 条目: {flat}"


_OPUS5 = "bedrock/converse/global.anthropic.claude-opus-5"   # config.py 里 opus-5 的配置串
# ⚠ 这是一个**构造**的短形, 不是实测串。本轮实测 (真 create_router + litellm mock_response)
# bedrock 侧 chunk 报的是 `converse/global.anthropic.claude-opus-5` 与
# `bedrock/converse/...` 两种拼法 —— `converse/` **保留**。真实串见
# test_litellm_really_reports_two_spellings_for_one_model。这里留着它是因为它测的是
# `_same_model` 在"更短的合法后缀"上也成立, 那个性质本身要钉。
_OPUS5_REPORTED = "global.anthropic.claude-opus-5"


def test_fell_back_is_false_when_every_reported_model_is_the_configured_one():
    """闸 G7 (a): 配置串与 chunk 报的串**拼法不一定逐字相同**, 都必须认作"同一个模型"。

    ⚠ 措辞在终审修正过: 初稿写的是"实测 chunk 报的是**去掉 provider 前缀**的串" ——
    那是把 deepseek 那次非流式实测 (`deepseek/deepseek-v4-pro` → `deepseek-v4-pro`)
    **外推**到了 bedrock 串。本轮实测 bedrock 侧 `converse/` 是**保留**的
    (见 test_litellm_really_reports_two_spellings_for_one_model)。
    """
    s = Settings()
    assert fell_back(s, "opus-5", [_OPUS5_REPORTED]) is False
    assert fell_back(s, "opus-5", [_OPUS5]) is False
    assert fell_back(s, "opus-5", [_OPUS5_REPORTED, _OPUS5]) is False


def test_fell_back_is_true_when_another_model_answered():
    """闸 G7 (b): 容灾真的触发时的样子 —— 用户选 gpt-sol, DeepSeek 答的。"""
    assert fell_back(Settings(), "gpt-sol", ["deepseek-v4-pro"]) is True


def test_fell_back_is_true_when_any_single_chunk_came_from_another_model():
    """闸 **G7b** —— 本 task 的中心断言 (用户裁定 R6)。

    ⚠ 这条钉的正是 Task 1 复审抓到的 I-2: 联网多轮时每一轮是**独立**的 `acompletion`,
    各自可能回退 (`web_search_enabled` 默认 True, `web_max_rounds = 5`)。第 1 轮回退、
    第 2 轮落回主模型时, 按"最后一个"判会报 `False` —— **回退了却不说**, 正是本轮要
    修的那件事本身。把实现写成 `fell_back(..., reported_models[-1])` 会让这条红。

    流中途回退 (spec §3 P6, litellm `MidStreamFallbackError`) 是同一个形状的第二条路径。
    """
    s = Settings()
    assert fell_back(s, "opus-5", ["deepseek-v4-pro", _OPUS5_REPORTED]) is True   # 先回退后落回
    assert fell_back(s, "opus-5", [_OPUS5_REPORTED, "deepseek-v4-pro"]) is True   # 先正常后回退
    # 反方向: 全都是配置串就必须是 False, 否则"一律 True"也能让上面两条绿
    assert fell_back(s, "opus-5", [_OPUS5_REPORTED, _OPUS5_REPORTED]) is False


def test_fell_back_is_none_for_internal_groups_and_empty_reports():
    """闸 G7 (c): ⛔ 不知道就发 `None`, **不得发 `False`**。

    `False` 的语义是"确证没回退"; 内部组 (default/hard/light/default-fallback) 压根
    不在 `selectable_models` 里, **没有"用户选的模型串"这个概念** —— 发 False 就是
    把"没这个概念"报成了一个确证结论。与同一个 done 事件里 `verified` 的三态同一条原则。
    """
    s = Settings()
    for g in ("default", "hard", "light", "default-fallback"):
        assert fell_back(s, g, ["deepseek-v4-pro"]) is None, g
    assert fell_back(s, "opus-5", []) is None
    assert fell_back(s, "opus-5", None) is None


def test_fell_back_match_requires_a_path_boundary():
    """闸 G8: 匹配必须带 `/` 边界, ⛔ 不许裸子串。

    `claude-opus-5` 是配置串的真子串, 但它**不是**一个完整的模型标识 ——
    把实现写成 `reported in configured` 会让这条红。裸子串正是 retrospective
    规则 6 成因 A 的形状 (判定式被悄悄放宽成近乎恒真)。
    """
    s = Settings()
    assert fell_back(s, "opus-5", ["claude-opus-5"]) is True
    assert fell_back(s, "opus-5", ["anthropic.claude-opus-5"]) is True


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
    assert by_id["sonnet-5"]["verified"] is False  # 2026-09 抽检唯一 false 的, 保住一真一假
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


class _ChunkScriptRouter:
    """逐 chunk 控制"这一片报不报模型 / 带不带 choices" —— 用来钉**累积端**。

    `chunks` 每项是 `(reported, has_choices)`:
    `reported=None` 造"这一片的 .model 是 None" (provider 只在首片报模型是常态);
    `has_choices=False` 造 usage chunk —— 它的 `choices` 是**空列表**, 而有 provider
    只在这一片上报模型。

    ⚠ 不改 `_EchoModelRouter` 来做这件事: 它"整条流只有一片、固定回一个串"的语义被
    既有三条发射端闸依赖, 动它等于同时动那三条闸的被测面。
    """

    def __init__(self, chunks: list[tuple[str | None, bool]]):
        self.chunks = chunks
        self.last_model = None
        # 实际发出去的 chunk。⚠ 没有它的话, 下面 usage-only 闸的全部分辨力压在
        # `choices=(... if has_choices else [])` 这一个三元式上: 把它改成恒非空,
        # 被测的"空 choices"场景就悄悄不存在了, 而闸照绿 (复审实测: 40 passed)。
        # 这是 retrospective 规则 6 成因 A —— 抽取端变形 ⇒ 判定式恒真。
        self.emitted: list = []

    async def acompletion(self, model, messages, stream=False, **kw):
        self.last_model = model
        script = self.chunks
        emitted = self.emitted

        async def agen():
            for reported, has_choices in script:
                chunk = SimpleNamespace(
                    model=reported,
                    usage=None if has_choices else SimpleNamespace(
                        prompt_tokens=1, completion_tokens=1, total_tokens=2),
                    choices=([SimpleNamespace(delta=SimpleNamespace(content="ok"))]
                             if has_choices else []))
                emitted.append(chunk)
                yield chunk
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
    ev = _done_event(_stream_client(), model="sonnet-5")  # 2026-09 抽检唯一 false 的
    assert ev["model_id"] == "sonnet-5"
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

    ⛔ **不许把这条单独留下、删掉兄弟测试**
    (`…follows_the_router_not_the_request`)。复审实测: 把实现伪装成
    `"resolved-" + body.model` (纯回显意图) 时**这条照绿** —— `_CapturingRouter` 回的
    `resolved-{组名}` 与它逐字相同, 连那句"两字段不相等"的诱饵也拦不住。分辨力全在
    兄弟那条 (`_EchoModelRouter` 把事实与意图解耦) 上。
    本仓库既有判例: 把一道闸的能力说大, 后来人会据此删掉真正在保护的那条。
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


def test_done_event_model_used_survives_later_chunks_that_report_nothing():
    """闸: **累积端**保值 —— 报模型的往往只有首片, 后续片的 `.model` 是 None。

    上面三条闸全在**发射端** (done 事件那一行), 累积端零断言: 复审实测把
    `model_used = getattr(chunk, "model", None) or model_used` 的 ` or model_used`
    删掉 ⇒ 本文件 38 条全绿。裸赋值会让最后一片把已拿到的模型串抹成 None。

    丢成 None 不是"少个字段"这么轻: D5 落地后 `fell_back` 只能据它返 `None`,
    于是一次**真实的回退**在用户界面上静默降级成"验证状态未知" ——
    "回退了却不说出来"正是本轮要修的那件事本身。
    """
    c = _stream_client(_ChunkScriptRouter([("deepseek-v4-pro", True), (None, True)]))
    ev = _done_event(c, model="opus-5")
    assert ev["model_used"] == "deepseek-v4-pro", ev


def test_done_event_model_used_reads_a_model_reported_only_on_the_usage_chunk():
    """闸: 累积端**位置** —— usage chunk 的 `choices` 是空列表。

    累积行原先写在 `if choices:` **里面**, 所以只在 usage 那一片上报模型的 provider
    会让整条流的 `model_used` 是 None。把它挪回 `if` 里面 ⇒ 这条红。

    ⚠ 与上一条是同一个洞的两半, 分开钉: 只有"保值"那条时, 把累积行搁回 `if` 里
    照样全绿; 只有本条时, 删掉 ` or model_used` 照样全绿。
    """
    r = _ChunkScriptRouter([(None, True), ("deepseek-v4-pro", False)])
    ev = _done_event(_stream_client(r), model="opus-5")
    # 形状闸: 被测场景真的发生过 —— 第二片的 choices 确实是空的。缺这句时, 把
    # fixture 的三元式改成恒非空 ⇒ "只在 usage 片报模型"这个场景压根没被造出来,
    # 而断言照绿 (成因 A)。
    assert [bool(getattr(c, "choices", None)) for c in r.emitted] == [True, False], r.emitted
    assert ev["model_used"] == "deepseek-v4-pro", ev
    # 同一件事在**兄弟字段**上也要钉 (复审 M-8): 累积块被拆成 model_used / models_used 两半后,
    # 只把 append 那半限回"有 choices 才收"⇒ 54 条全绿 (V9 实测)。Task 1 的 M-1 在
    # models_used 上原样重演了一次 —— 一类缺陷极少只出现一处。
    assert ev["models_used"] == ["deepseek-v4-pro"], ev


def _real_router_stream(monkeypatch, *, model, fallbacks=None) -> SimpleNamespace:
    """用**真 litellm Router** 跑一次 `/api/ask_stream`, 返回整段 SSE 文本**与实际派单序列**。

    ⚠ patch 的是 `litellm.acompletion` —— Router 每个 deployment 最终调的那个函数
    (实测: `Router.acompletion` 无论 stream 与否都走 `async_function_with_fallbacks`,
    再落到它)。⛔ 不能用仓库里的假 Router 测这条: 假 Router 根本没有 fallback 逻辑,
    拿它测容灾等于测了个寂寞 —— 这正是"闸看起来在测、其实没测"的形状。

    `fallbacks=None` 用 `create_router` 派生的真实配置; 传别的值可以模拟"没有容灾"。

    返回 `SimpleNamespace(text=<整段 SSE>, calls=[实际派到的 deployment 模型串, ...])`。
    ⚠ `calls` 不是装饰: 只断 SSE 文本的话, "主模型压根没失败、直接答对了"与"失败后由
    fallback 答对了"**长得一模一样** (复审 U13 实测: 把主模型改成不失败, 正向那条照绿)。
    """
    import litellm
    from server.llm_config import create_router

    calls: list[str] = []

    async def fake_acompletion(**kw):
        calls.append(str(kw.get("model")))
        if "anthropic" in str(kw.get("model")):
            raise Exception("primary deployment boom")     # 模拟 credits 耗尽/认证失败

        async def agen():
            yield SimpleNamespace(model="deepseek-v4-pro", usage=None,
                                  choices=[SimpleNamespace(delta=SimpleNamespace(content="ok"))])
        return agen()

    monkeypatch.setattr(litellm, "acompletion", fake_acompletion)
    s = Settings()
    router = create_router(s)
    router.num_retries = 0        # 重试只会让这条测试变慢, 与被测的容灾无关
    if fallbacks is not None:
        router.fallbacks = fallbacks
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router
    app.state.settings = s
    text = TestClient(app).post("/api/ask_stream",
                                json={"question": "AETERM?", "model": model}).text
    return SimpleNamespace(text=text, calls=calls)


def test_stream_survives_a_dead_primary_deployment(monkeypatch):
    """闸 G6 正向, **端到端**: 主模型开流抛错 ⇒ 流不该死, 由 default-fallback 接管,
    且 `done.model_used` 报的是**实际**答题的那个。

    ⚠ `Settings()` 的类默认值里 opus-5 走 `bedrock/converse/global.anthropic.*`,
    所以 fake 里那句 `"anthropic" in model` 打的就是它。

    ⛔ **兄弟闸 `test_stream_dies_without_the_fallback_entry` 承重, 不许单删本条留它、
    也不许单删它留本条。** 复审 U13 实测: 只断 SSE 文本时, 把主模型改成**不失败**,
    本条照绿 —— "没回退也能答对"与"回退后答对"在 SSE 层长得一模一样。故这里补
    `calls` 的**绝对**断言 (真的先派了主模型、失败后真的派了 fallback), 分辨力才在本条自己身上。
    """
    r = _real_router_stream(monkeypatch, model="opus-5")
    assert "event: error" not in r.text, r.text[:400]
    blocks = [b for b in r.text.split("\n\n") if b.startswith("event: done")]
    assert len(blocks) == 1, f"没解析到唯一的 done 事件: {r.text[:400]!r}"
    ev = json.loads(next(l for l in blocks[0].splitlines() if l.startswith("data: "))[6:])
    assert ev["model_used"] == "deepseek-v4-pro", ev
    assert ev["model_id"] == "opus-5", ev
    # 派单序列钉到绝对值: 主模型先被派过(且它就是失败的那个), 最后落到 fallback 部署。
    s = Settings()
    assert r.calls == [_OPUS5, s.fallback_model], f"派单序列不对: {r.calls}"


def test_stream_dies_without_the_fallback_entry(monkeypatch):
    """闸 G6 反向: 把 fallback 表退回**分支前的样子** (只有 default 组一条) ⇒
    同样的失败变成 `event: error`。

    这条同时是 D5 那个回归的**复现**: 它红了才说明上一条不是靠别的什么东西绿的。
    """
    r = _real_router_stream(monkeypatch, model="opus-5",
                            fallbacks=[{"default": ["default-fallback"]}])
    assert "event: error" in r.text, r.text[:400]


def test_done_event_models_used_is_ordered_and_deduped():
    """闸 **G7c**: `models_used` 是**有序去重**。

    去重坏掉 ⇒ 长度断言红 (真实流里同一个模型会在几十上百片上重复报);
    顺序坏掉 (例如用 set) ⇒ 顺序断言红。两个方向各自有断言, 不靠一条兼职。

    ⚠ **测试数据必须让插入序 ≠ 字典序**, 否则"顺序"那半是空断言: plan 原本给的
    `["m-a", "m-b"]` 恰好已是字典序, `sorted(set(...))` 的变异**一条都打不红**
    (本轮实测, 且 G7b 端到端那组 `["deepseek-v4-pro", "global.anthropic..."]` 同病)。
    故这里用 m-b 先出现 —— 期望 `["m-b", "m-a"]`, 排序实现会得到 `["m-a", "m-b"]`。
    """
    c = _stream_client(_ChunkScriptRouter([("m-b", True), ("m-b", True), ("m-a", True),
                                           ("m-b", True), (None, False)]))
    ev = _done_event(c, model="opus-5")
    assert ev["models_used"] == ["m-b", "m-a"], ev
    assert ev["model_used"] == "m-b", "单值字段仍是**最后一个**报出的, 语义不变"


def test_done_event_carries_fell_back_three_ways():
    """闸 G7 端到端 (SSE 层): 纯函数对不代表接线对。"""
    ev = _done_event(_stream_client(_EchoModelRouter(_OPUS5_REPORTED)), model="opus-5")
    assert ev["fell_back"] is False, ev
    ev = _done_event(_stream_client(_EchoModelRouter("deepseek-v4-pro")), model="opus-5")
    assert ev["fell_back"] is True, ev
    ev = _done_event(_stream_client(_EchoModelRouter("deepseek-v4-pro")))   # 不传 model
    assert ev["fell_back"] is None, ev


def test_done_event_fell_back_sees_every_chunk_not_just_the_last():
    """闸 G7b 端到端: 纯函数按列表判是一回事, **接线时真的把整份列表喂进去**是另一回事。

    ⚠ 这条与上面那条纯函数版**不可互相替代**: 把接线写成
    `fell_back(s, body.model, [model_used])` (只喂最后一个) 会让纯函数那条照绿。
    """
    c = _stream_client(_ChunkScriptRouter([("deepseek-v4-pro", True), (_OPUS5_REPORTED, True)]))
    ev = _done_event(c, model="opus-5")
    assert ev["models_used"] == ["deepseek-v4-pro", _OPUS5_REPORTED], ev
    assert ev["model_used"] == _OPUS5_REPORTED, "最后一个是主模型 —— 诱饵摆上了"
    assert ev["fell_back"] is True, "有一段是 DeepSeek 答的, 就必须说"


def test_real_fallback_path_reports_fell_back(monkeypatch):
    """闸 G6 + G7 合流: 真 Router 真触发容灾时, 事件必须自己说出这件事。

    这条是本轮的**中心断言** —— 用户原话: 不做的话"用户选 Sol、DeepSeek 答题、
    徽章却说 Sol", 就是刚修掉的 C-1 (⚑ 归错模型) 同族缺陷换了个位置。

    ⚠ **`calls` 断言不可省** (复审 M-9): 只断事件字段的话, 把主模型改成**根本不失败**
    (于是压根没有回退) 这条**照绿** —— fake 无论派到哪个 deployment 都回
    `model="deepseek-v4-pro"`, 事件字段一模一样。中心断言必须自己钉住"回退真的发生了",
    不能靠兄弟闸。
    """
    r = _real_router_stream(monkeypatch, model="opus-5")
    blocks = [b for b in r.text.split("\n\n") if b.startswith("event: done")]
    assert len(blocks) == 1, r.text[:400]
    ev = json.loads(next(l for l in blocks[0].splitlines() if l.startswith("data: "))[6:])
    assert r.calls == [_OPUS5, Settings().fallback_model], f"派单序列不对: {r.calls}"
    assert ev["fell_back"] is True, ev
    assert ev["models_used"] == ["deepseek-v4-pro"], ev
    assert ev["model_used"] == "deepseek-v4-pro", ev
    assert ev["model_id"] == "opus-5", ev
    assert ev["verified"] is True, "verified 记的是**用户选的**模型验没验过, 这个事实不变"


def test_models_used_spans_every_web_round(monkeypatch):
    """闸 I-4: `models_used` 必须**跨轮**累积 —— 这是裁定 R6 的**第一条动机**。

    联网时每一轮是一次**独立**的 `acompletion` (`web_max_rounds = 5`), 各自可能回退。
    第 1 轮回退到 DeepSeek、第 2 轮落回主模型时, 只看最后一个会报"没回退" —— 那正是
    I-2 那个静默谎言。

    ⚠ **这条闸存在的直接理由**: 在轮循环里加一行 `models_used.clear()` (它旁边的
    `acc` / `round_parts` / `cu_round` **三个都真的是每轮重置**, 所以这是这段代码里最
    自然的一个误读, 不是刻意破坏) ⇒ 全套件 1975 条**零红** (复审实测, 本人复跑确认)。
    在此之前 R6 的第一条动机是靠"models_used 在 gen() 作用域里跨轮天然累积"这个**结构
    事实**成立的, 没有任何闸真的跑过两轮。

    ⛔ 不改红线文件 `test_ask_stream_web.py` —— 这里用本地假搜索器 + 本地两轮 fake router,
    monkeypatch `server.router.WebSearcher` (本文件既有先例:
    `test_request_body_gate_actually_sees_an_added_kwarg`)。

    ⚠ **本闸在顺序上的分辨力边界** (成因 D 自查, 实测得出, 别把它记宽也别记窄):
    对**反序**型有分辨力 (`append` → `insert(0, …)` ⇒ 本闸红), 但对**排序归一化**型
    (`sorted` / `sorted(set)`) **没有** —— 期望值 `["deepseek-v4-pro", "global.…"]`
    恰好已是字典序, 排序实现输出与它逐字相同。排序归一化那一支由
    `test_done_event_models_used_is_ordered_and_deduped` 负责 (它的数据是 `["m-b","m-a"]`)。
    ⛔ 别为了补这一支把这里的模型串换成 m-a/m-b: 它俩有语义 (回退串 / 主模型串),
    换掉就不再像它要测的那个真实场景了。
    """
    from server.web_search import WebRef

    class _FakeSearcher:
        def __init__(self, s):
            self.searches_used = 0

        def search(self, query):
            self.searches_used += 1
            return ([WebRef(url="https://example.org/x", title="T", content="C",
                            retrieved_at="2026-09-02")], "ok")

    monkeypatch.setattr("server.router.WebSearcher", _FakeSearcher)

    class _TwoRoundRouter:
        """第 1 轮工具调用 + 报**回退**串; 第 2 轮纯文本 + 报**主模型**串。"""

        def __init__(self):
            self.rounds = 0

        async def acompletion(self, model, messages, stream=False, **kw):
            self.rounds += 1
            first = self.rounds == 1

            async def agen():
                if first:
                    yield SimpleNamespace(model="deepseek-v4-pro", usage=None, choices=[
                        SimpleNamespace(delta=SimpleNamespace(content=None, tool_calls=[
                            SimpleNamespace(index=0, id="call-1",
                                            function=SimpleNamespace(
                                                name="web_search",
                                                arguments='{"query": "AETERM"}'))]))])
                else:
                    yield SimpleNamespace(model=_OPUS5_REPORTED, usage=None, choices=[
                        SimpleNamespace(delta=SimpleNamespace(
                            content="Per [Web: https://example.org/x (retrieved 2026-09-02)] ok.",
                            tool_calls=None))])
            return agen()

    r = _TwoRoundRouter()
    ev = _done_event(_stream_client(r), model="opus-5", web=True)
    assert r.rounds == 2, f"没真的跑两轮, 这条闸就没测到跨轮: {r.rounds}"
    assert ev["models_used"] == ["deepseek-v4-pro", _OPUS5_REPORTED], ev
    assert ev["model_used"] == _OPUS5_REPORTED, "最后一轮是主模型 —— 诱饵摆上了"
    assert ev["fell_back"] is True, "第 1 轮是 DeepSeek 答的, 就必须说"


def test_ask_now_falls_back_instead_of_502(monkeypatch):
    """闸 I-3: 钉住 Task 2 **静默扩大**的 `/api/ask` 行为面。

    分支前 `/api/ask model=opus-5` 在主模型 deployment 抛错时是 **502**
    (`opus-5` 组没有 fallback 条目); Task 2 把容灾表从 `selectable_models` 派生之后,
    同一个失败变成 **200 + 由 default-fallback 作答**。这是**期望**的 (裁定 R2 的
    全部意义就在这), 但它属于 `/api/ask` —— 而本轮 spec §1 的非目标里写着"不动
    `/api/ask` 的 model_used"。⇒ 行为面确实变了, 必须**被测试记住, 而不是只被文档记住**:
    文档没有执行力, 下一个人重构 `_fallback_map` 时不会读 spec §1, 但会看见这条红。

    ⚠ **残留 (spec §7 L5, 本轮不修)**: `/api/ask` 里那句
    `model_used = getattr(response, "model", None) or body.model` 的回显分支还在 ——
    provider 不报 `.model` 的回退会把 DeepSeek 的答案标成 `opus-5` (终审 C-1 同族)。
    它今天无调用方 (streamlit 只读自己那次请求的返回), 且改 `AskResponse` 契约属
    上一轮的 D11, 不在本轮单内。这条闸**不**断言 `model_used` 的取值, 免得把"今天碰巧
    是对的"钉成"契约保证"。
    """
    import litellm
    from server.llm_config import create_router

    calls: list[str] = []

    def fake_completion(**kw):
        calls.append(str(kw.get("model")))
        if "anthropic" in str(kw.get("model")):
            raise Exception("primary deployment boom")
        return SimpleNamespace(model="deepseek-v4-pro", usage=None,
                               choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))])

    monkeypatch.setattr(litellm, "completion", fake_completion)
    s = Settings()
    router = create_router(s)
    router.num_retries = 0
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router
    app.state.settings = s
    resp = TestClient(app).post("/api/ask", json={"question": "AETERM?", "model": "opus-5"})
    assert resp.status_code == 200, f"分支前是 502, Task 2 之后应回退作答: {resp.text[:300]}"
    assert calls == [_OPUS5, s.fallback_model], f"派单序列不对: {calls}"


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

# 前端 2026-09-08 拆成 ES 模块 (app.js 只剩入口): 归因逻辑 flagModelName 搬进 js/flag.js,
# 徽章文案 modelBadgeText 搬进 js/render.js。下面三条静态闸只换了读哪个文件, 切片锚点
# ("function flagModelName" / "function modelBadgeText" 前面多了个 export, 子串照样命中)
# 与断言形状一字未动。
_WEBCHAT = Path(__file__).resolve().parents[2] / "webchat"
FLAG_JS = _WEBCHAT / "js" / "flag.js"
RENDER_JS = _WEBCHAT / "js" / "render.js"
_FLAG_PROBE = Path(__file__).resolve().parent / "fixtures" / "flag_attribution_probe.mjs"


@pytest.fixture(scope="module")
def flag_probe():
    """在 node 里真的跑一遍 webchat 的那套 ES 模块 (app.js 入口 + js/*.js), 驱动
    renderMessages → attachTools → flagButton → openFlag → postFlag, 返回各场景实际发给
    /api/flag 的请求体 (加载方式与场景说明见同名 .mjs 的头注释)。"""
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
    src = FLAG_JS.read_text(encoding="utf-8")
    body = src.split("function flagModelName", 1)
    assert len(body) == 2, "flagModelName 没了 —— 归因逻辑被搬走或删掉了"
    body = body[1].split("\n}", 1)[0]
    assert re.search(r"\.modelId\b", body), "归因没有读 msgObj.modelId"


def test_badge_says_which_model_actually_answered_when_it_fell_back(flag_probe):
    """闸 G9 正向 (用户裁定 R4): 回退时徽章必须写出**实际**答题的模型。

    不做的话: 用户选 Sol、DeepSeek 答题、徽章却说 Sol —— 与终审 C-1 (⚑ 归错模型)
    同族, 只是位置从归档换到了徽章。
    `verified` 按未知处理: 它描述的是用户**选的**那个模型验没验过, 拿它给一条
    **别人答的**消息背书就是撒谎。
    """
    badge = flag_probe["fellBack"]["badgeText"]
    assert badge == "模型: GPT-5.6 Sol → 实际 deepseek-v4-pro（已回退）· 验证状态未知", badge
    assert "⚠未验证" not in badge, f"verified 那一支必须被盖掉: {badge}"


def test_badge_lists_every_model_that_answered(flag_probe):
    """闸 **G9b** (用户裁定 R6): 一次回答里有两个模型各答了一段时, **两个都要出现**。

    只显示最后一个 / 只显示第一个都会让这条红。单模型场景 (上一条) 的文案则必须
    与 R4 原样一字不差 —— 不许因为改成列表就冒出个悬空的顿号。
    """
    badge = flag_probe["fellBackMulti"]["badgeText"]
    assert "deepseek-v4-pro" in badge, badge
    assert "global.openai.gpt-5.6-sol" in badge, badge
    assert "已回退" in badge and "验证状态未知" in badge, badge


def test_badge_is_byte_identical_when_it_did_not_fall_back(flag_probe):
    """闸 G9 反向: 没回退时徽章与今天**逐字相同**。

    ⚠ 这条不是形式主义: 把回退分支写成"只要有 modelsUsed 就显示箭头"的实现会让它红,
    而那种实现会给**每一条**正常回答都挂上"已回退", 三天之内没人再看这个徽章。
    """
    assert flag_probe["notFellBack"]["badgeText"] == "模型: GPT-5.6 Sol ⚠未验证"


def test_badge_ignores_records_that_predate_the_field(flag_probe):
    """闸 G10 (spec §5 B1/B2): 老后端不发这两个字段、老存档里没有这两个键时,
    徽章必须与今天逐字相同。

    ⚠ B1 不是假想: `webchat/` 是从工作树挂载的 (`StaticFiles` 每请求现读), 这个前端
    一保存就出现在用户正在跑的服务上, 而 Python 改动要重启才生效 ——
    "新前端 + 老后端"是**必然发生的中间态**, 且是用户真的会看到的那一刻。

    `withModelId` 场景的历史记录里 `modelsUsed` / `fellBack` **两个键都不存在**
    (探针的 `scenario()` 对显式 undefined 整个键都不设), 正是那个形状。
    """
    assert flag_probe["withModelId"]["badgeText"] == "模型: GPT-5.6 Sol ⚠未验证"


def test_badge_text_reads_the_fell_back_field():
    """闸 G13 静态第二重 (照 `test_flag_payload_reads_the_message_model_id` 双闸写法):
    node 缺席时行为闸会 skip, 这条不会。断的是**属性/形参读取形状**, 不是"源码里出现过这个词"。

    ⚠ **只断 `\\bfellBack\\b` / `\\bmodelsUsed\\b` 是不够的** (本轮实测): 那两个词出现在
    **函数签名**里, 所以把整个回退分支删光 (变异 M2) 这条**照绿** —— 而 M2 正是 node 缺席时
    最需要它拦住的那种改动。故这里再钉两样**只存在于分支体内**的东西:
    - `fellBack === true` 的**全等**判据: 它就是 spec §5 B1 的降级保证 (老后端/老存档
      发 undefined 时必须落回原文案)。写成 `fellBack !== false` 之类会让这条红。
    - `已回退` 这个用户可见串: 分支存在与否的锚。

    成因 D 自查 —— **哪种错误实现在这组输入上会产出相同输出?** 答: 保留这两样却把列表
    接错 (例如只显示 `modelsUsed[0]`)。那一支**不归本闸**, 由行为闸
    `test_badge_lists_every_model_that_answered` 负责 (变异 M4 实测只打红它)。
    ⛔ 别为此在这里加 `modelsUsed\\.join` 之类的字面断言: 那会把一种写法钉死成契约,
    而它保证的事已经有行为闸在管。
    """
    src = RENDER_JS.read_text(encoding="utf-8")
    body = src.split("function modelBadgeText", 1)
    assert len(body) == 2, "modelBadgeText 没了 —— 徽章文案逻辑被搬走或删掉了"
    body = body[1].split("\n}", 1)[0]
    assert re.search(r"\bfellBack\b", body), "徽章文案没读 fellBack"
    assert re.search(r"\bmodelsUsed\b", body), "徽章文案没读 modelsUsed"
    assert re.search(r"fellBack\s*===\s*true", body), \
        "回退判据不是全等 —— 老后端发 undefined 时会落错分支 (spec §5 B1)"
    assert "已回退" in body, "回退分支没了 —— 徽章不会再说出实际答题的模型"


def test_archive_records_the_models_that_actually_answered(flag_probe):
    """闸 G11 正向 (用户裁定 R5): `modelsUsed` / `fellBack` 必须落进历史存档,
    刷新之后徽章仍然诚实。

    只做 UI 标注的话, 对话存下来之后这条信息就没了 —— 读的人得靠记得自己当时选了什么。
    与 2026-09-01 清掉的 B6 同形: **产物必须能自证**。
    """
    got = flag_probe["streamFellBack"]
    assert got["stored"]["modelsUsed"] == ["deepseek-v4-pro"], got["stored"]
    assert got["stored"]["fellBack"] is True, got["stored"]
    assert "已回退" in got["badgeAfterReload"], got["badgeAfterReload"]
    assert "deepseek-v4-pro" in got["badgeAfterReload"], got["badgeAfterReload"]


def test_archive_records_a_clean_run_as_not_fallen_back(flag_probe):
    """闸 G11 反向: 没回退的那条存的是 `False`, 不是缺字段也不是 `True`。
    把 persist 写成"一律存 true/一律不存"都会让这一对里的某条红。"""
    got = flag_probe["streamNoFallback"]
    assert got["stored"]["fellBack"] is False, got["stored"]
    assert got["badgeAfterReload"] == "模型: GPT-5.6 Sol ⚠未验证", got["badgeAfterReload"]


def test_flag_is_attributed_to_the_fallback_model_that_actually_answered(flag_probe):
    """闸 G12 (⚑ 归因): 回退时 `dogfood_failures.md` 记的必须是**实际**答题的模型。

    ⚠ 诱饵: 这条消息的 `msgObj.modelId` 是 `gpt-sol` —— 只读 modelId 的实现
    (也就是终审 C-1 的修法) 在这里会把 DeepSeek 的捏造记到 GPT-5.6 Sol 头上。
    backlog 是 append-only 的 (用户全局规则 B), 错误写入即永久且无从回溯,
    读的人还可能据此把一轮反捏造工作投到错误的模型上。
    """
    body = flag_probe["streamFellBack"]["flagBody"]
    assert "deepseek-v4-pro" in body["model"], body
    assert "GPT-5.6 Sol" in body["model"], "当时选的是谁也要留着, 否则复盘断线"


def test_flag_model_field_fits_the_worst_case_attribution():
    """归因串变长了 (可能是"两个模型名 + 回退自 + label"), 而 `FlagRequest.model` 有
    `max_length` —— 超了后端会 422, 用户侧表现是 **⚑ 静默记录失败**。

    ⚠ 这条钉的是"最坏情况装得下", 用**真实配置串**算, 不是拍一个宽松的数字。
    """
    from server.router import FlagRequest
    s = Settings()
    worst = "、".join(m.model.split("/")[-1] for m in s.selectable_models)
    worst += f"（回退自 {max((m.label for m in s.selectable_models), key=len)}）"
    FlagRequest(question="q", answer="a", note="n", model=worst)   # 不抛 = 装得下


def test_flag_payload_reads_the_message_fell_back():
    """闸 G13 静态第二重: node 缺席时行为闸 skip, 这条不会。

    ⚠ 按 Task 4 那条教训自查: 搜的 token **不能**也出现在引入它的声明里 (签名/const/import),
    否则对"体内有没有用它"零分辨力。这里搜的是 `.fellBack` / `.modelsUsed` (**带前导点**的
    属性读取形状), 而 `flagModelName(msgObj)` 的签名里只有 `msgObj` —— 两个 token 都只可能
    来自函数体内的真实读取。
    """
    src = FLAG_JS.read_text(encoding="utf-8")
    body = src.split("function flagModelName", 1)[1].split("\n}", 1)[0]
    assert re.search(r"\.fellBack\b", body), "归因没有读 msgObj.fellBack"
    assert re.search(r"\.modelsUsed\b", body), "归因没有读 msgObj.modelsUsed"
    # ⚠ 与 `test_badge_text_reads_the_fell_back_field` **对称**的一条 (复审 M5):
    # 同一条三态规矩有两个消费者 (徽章 / ⚑ 归因), 徽章那处的全等判据有静态闸钉着,
    # 这里此前**零覆盖** —— 复审变异 V-M5 (改成 truthy) 是 69 passed 零红 (本人复跑确认)。
    # 钉的是**判据形状一致**, 不是 JS 真值语义: 后端 `fell_back()` 返 bool|None, 产不出
    # "truthy 但非 true"的值, 所以这里**不该**写成行为闸去钉一个后端产不出的输入。
    assert re.search(r"fellBack\s*===\s*true", body), \
        "回退判据不是全等 —— 与徽章那处的三态写法不一致 (spec §5 B1 同一条规矩)"


def test_badge_survives_a_models_used_that_is_not_a_list(flag_probe):
    """闸 **F-1**: `modelsUsed` 形状不对时, 徽章**落回老文案且不抛**, 且**整段历史渲染不中止**。

    ⚠ 死法与"一条徽章降级"完全不是一个量级: `.join is not a function` 抛在
    `renderMessages` 里 ⇒ **整段对话历史渲染不出来**。现有 try/catch 只包了 `JSON.parse`,
    没包 `.join`。

    今天不可达 (回退分支在生产上结构性够不到), **但接通它的正是本 commit** ——
    `onDone` 从这一版起把 `models_used` 原样喂进来, 且是 `?? null` 零形状校验。
    这是"今天不可达"与"下一个 commit 就可达"的交界, 拖一轮就变成活缺陷。

    判据用 `Array.isArray`: 只判 truthy + `.length` 挡不住字符串 ("abc".length 是 3),
    也挡不住 array-like 对象 —— 两者都会走到 `.join` 上。
    """
    for key in ("badShapeString", "badShapeObject"):
        got = flag_probe[key]
        assert got["renderError"] is None, f"{key}: 渲染抛了 —— {got['renderError']}"
        assert got["renderedCount"] == 2, f"{key}: 历史渲染中止了, 只画出 {got['renderedCount']} 条"
        assert got["badgeText"] == "模型: gpt-sol ⚠未验证", f"{key}: {got['badgeText']}"


def test_flagging_still_records_when_models_used_is_not_a_list(flag_probe):
    """闸 **I-5**: 同一个护栏加在了 `flagModelName`, 那一处也必须有闸。

    ⚠ 与徽章那处**不是同一个后果, 而且更重**: `flagModelName` 抛出的异常穿过 `postFlag`
    ⇒ **用户点了 ⚑, 结果什么都没记下**, 而 `dogfood_failures.md` 是 append-only 的优先级
    backlog (用户全局规则 B)。"归错模型"至少还留下一条错记录, 事后能翻出来纠正;
    这个是**连记录都没有**, 且用户以为记上了 —— 缺陷本身把发现缺陷的渠道给堵了。

    ⚠ 只钉徽章那处不够: 复审变异 V-F1b (**只**拿掉 `flagModelName` 的 `Array.isArray`)
    在本条存在之前是 **69 passed 零红** (本人复跑确认)。
    """
    for key in ("badShapeString", "badShapeObject"):
        got = flag_probe[key]
        assert got["flagError"] is None, f"{key}: ⚑ 抛了 —— {got['flagError']}"
        assert got["flagBody"] is not None, f"{key}: /api/flag 压根没被调用, 记录丢了"
        # 归因退回"用户选的那个" (label 表此时还没加载, 所以是原始 id) —— 形状不对时
        # 不知道实际是谁, 报选的那个是诚实的降级, 空着或崩掉都不是。
        assert got["flagBody"]["model"] == "gpt-sol", got["flagBody"]


def test_badge_at_first_paint_is_observed_not_only_after_the_label_table_loads(flag_probe):
    """闸 **F-2**: 初次渲染那一版也要被观测。

    此前全套闸只看 `/api/info` 之后 `refreshModelBadgeLabels()` 重写的文案, 于是:
    - 初次渲染那条路径 (`renderModelBadge` 直接调 `modelBadgeText`) 无人观测;
    - `fellBack === undefined` —— **spec §5 B1 字面的那个值** —— 在被观测路径里从不出现
      (刷新那版走的是 dataset 三路比较后的 `null`)。

    初次渲染时 label 表还没到, 所以是原始 id `gpt-sol` 而不是 `GPT-5.6 Sol` —— 这个差异
    本身就证明抓的确实是**另一个**时点。
    """
    # B1 形状 (两个键都不存在) ⇒ 与今天逐字相同, 只是 label 还没补上
    assert flag_probe["withModelId"]["badgeTextInitial"] == "模型: gpt-sol ⚠未验证", \
        flag_probe["withModelId"]["badgeTextInitial"]
    # 回退形状 ⇒ 首屏就该说实话, 不能等 /api/info 回来才说
    assert flag_probe["fellBack"]["badgeTextInitial"] == \
        "模型: gpt-sol → 实际 deepseek-v4-pro（已回退）· 验证状态未知", \
        flag_probe["fellBack"]["badgeTextInitial"]


def test_refresh_survives_a_corrupt_dataset(flag_probe):
    """闸 **F-3**: `refreshModelBadgeLabels` 里 `JSON.parse` 的 try/catch 在做事, 钉住它。

    契约是"坏数据不该让整条历史渲染崩掉" —— 抛出去的话 `forEach` 中断, 后面所有徽章
    都停在旧文案上, 而且异常会一路穿到 `loadModelName` 的调用点。
    """
    got = flag_probe["corruptDataset"]
    assert got["refreshError"] is None, f"try/catch 没兜住: {got['refreshError']}"
    # 坏数据 ⇒ 当"没有这个信息", 退回非回退文案 (label 表此时已加载)
    assert got["badgeText"] == "模型: GPT-5.6 Sol ⚠未验证", got["badgeText"]


def test_archive_says_unknown_not_false_when_the_backend_never_sent_the_field(flag_probe):
    """闸 **G11c** (spec §5 B1 在**存档层**): 老后端不发 `fell_back` / `models_used` 时,
    存档里必须是 `null`(不知道), ⛔ 不是 `false`(确证没回退)。

    ⚠ 这不是洁癖, 是本轮全部工作的那条原则本身: `false` 会让一条**可能回退过**的历史
    记录永久地自称"确证没回退"。存档是 append-only 的, 写错就是永久错。
    与同一事件里 `verified` 的三态、与 `fell_back(...)` 内部组返 `None` 同一条规矩。

    ⚠ 它同时是 `?? null` 那一处唯一有分辨力的输入 (本轮实测): 另两个 stream 场景都发
    显式值, `?? false` 与 `?? null` 在它们身上输出**逐字相同** —— 成因 D。
    """
    got = flag_probe["streamOldBackend"]
    assert got["stored"]["fellBack"] is None, got["stored"]
    assert got["stored"]["modelsUsed"] is None, got["stored"]
    assert got["badgeAfterReload"] == "模型: GPT-5.6 Sol ⚠未验证", got["badgeAfterReload"]


def test_flag_attribution_is_unchanged_when_the_backend_is_old(flag_probe):
    """闸 G10 在 **⚑ 归因层**的那一半 (spec §5 B1)。

    ⚠ 单独成条是有理由的 (复审 M-12): 这条断言原本挂在上面那个**名字只讲存档**的测试里,
    按名字精简时会被当成"重复的多余断言"顺手删掉, 而删掉即**无声重开** ⚑ 层的 B1 缺口。
    闸的名字就是它的说明书 —— 说明书没提到的东西, 下一个人不会知道要保护。
    """
    got = flag_probe["streamOldBackend"]
    assert got["flagBody"]["model"] == "GPT-5.6 Sol", got["flagBody"]


def _badge_classes(probe_entry) -> set:
    """徽章的 class 集合。⚠ 先断基础 class 在, 否则"没有 unverified"会变成永真式
    (抽取端塌成 None / 空串时下面的 `not in` 恒成立 —— 规则 6 成因 A)。"""
    cls = probe_entry["badgeClass"]
    assert cls, f"抽取端失效: badgeClass 是 {cls!r}, 下面的断言会变永真"
    parts = set(cls.split())
    assert "model-meta" in parts, f"抽取端失效: 拿到的不是徽章元素 {cls!r}"
    return parts


def test_badge_is_amber_when_it_fell_back(flag_probe):
    """闸 **I-1** (spec §6 G9 的"**且带 `.unverified`**"那半, 此前全套件零覆盖)。

    ⚠ 终审实测: 把回退分支的 `unverified: true` 改成 `false` ⇒ 71 条**全绿**;
    把 `classList.add("unverified")` 整行删光 ⇒ 也**全绿** (本人复跑确认)。
    失败场景是"文字对、但没颜色" —— 而四个可选模型里三个 `verified=false`, **琥珀是常态**,
    于是唯独"真出事"那条长得像正常消息, 正好反了。
    """
    assert "unverified" in _badge_classes(flag_probe["fellBack"]), \
        flag_probe["fellBack"]["badgeClass"]
    assert "unverified" in _badge_classes(flag_probe["fellBackMulti"]), \
        flag_probe["fellBackMulti"]["badgeClass"]


def test_badge_is_not_amber_for_a_verified_model_that_did_not_fall_back(flag_probe):
    """闸 I-1 反方向: 没有它的话"一律加 unverified"也能让上面那条绿, 而那样琥珀色就
    不再传递任何信息了。"""
    assert "unverified" not in _badge_classes(flag_probe["verifiedTrue"]), \
        flag_probe["verifiedTrue"]["badgeClass"]


def test_badge_is_amber_for_an_unverified_model(flag_probe):
    """闸 I-1 第三向 (既有欠账, 顺手补): `verified === false` 的琥珀色此前也从来没闸。
    它与回退那一支共用同一条 `if (unverified) classList.add(...)` 接线。"""
    assert "unverified" in _badge_classes(flag_probe["notFellBack"]), \
        flag_probe["notFellBack"]["badgeClass"]


def test_same_model_does_not_merge_across_providers():
    """闸 **I-2 反方向**: 归一化**不许做过头**。

    ⚠ 这条钉的正是 team-lead 点名禁掉的那种实现: `rsplit("/")[-1]` 取最后一段会把
    `openai/gpt-4` 与 `azure/gpt-4` 判成同一个模型 ⇒ 真回退被合并掉 ⇒ `fell_back`
    从 True 变 False, 正是本轮要防的那件事。
    """
    from server.llm_config import _same_model
    assert _same_model("openai/gpt-4", "azure/gpt-4") is False
    assert _same_model("bedrock/converse/x", "converse/x") is True      # 带 / 边界的后缀
    assert _same_model("converse/x", "bedrock/converse/x") is True      # 反方向也认
    assert _same_model("bedrock/converse/claude-opus-5", "claude-opus-5") is True
    # ⛔ 不完整标识不算命中 (`.` 不是 `/`)
    assert _same_model("bedrock/converse/global.anthropic.claude-opus-5",
                       "claude-opus-5") is False


def test_done_event_merges_two_spellings_of_one_model():
    """闸 **I-2 正向** (终审实测的那个真实形状): litellm 对**同一次**回答会报两种拼法,
    `models_used` 必须收成**一项**, 且是**最限定形** (合并只朝更长方向增长)。

    ⚠ **期望值在终审第 2 轮从"最短形"改成了"最长形"** —— 本分支唯一一次改既有闸的期望值,
    原因不是这条闸写错了, 而是**被测语义变了** (N-2): `_same_model` 不传递, 任何"缩短已存
    条目"的策略都会经由裸形把两个 provider 串起来, 故合并改为**只朝更限定方向增长**。
    改前钉的是"同一模型收成一项**且展示最短形**", 改后钉的是"同一模型收成一项**且展示
    最限定形**" —— "收成一项"这半**一字未动**, 变的只是展示选哪个形。

    成因 D 自查 —— 哪种错误实现在这组输入上会产出相同输出?
    答: "保留首次出现的那个"。它在**长形先到**那半与正确实现输出**逐字相同**
    (改期望值前, 是**短形先到**那半相同) ⇒ 两个到达顺序都必须跑, 只是有分辨力的那半换了边。
    """
    long_, short = "bedrock/converse/global.anthropic.claude-opus-5", \
                   "converse/global.anthropic.claude-opus-5"
    for first, second in ((long_, short), (short, long_)):
        c = _stream_client(_ChunkScriptRouter([(first, True), (second, True)]))
        ev = _done_event(c, model="opus-5")
        assert ev["models_used"] == [long_], f"{first} 先到: {ev['models_used']}"
        assert ev["fell_back"] is False, ev


def test_done_event_keeps_genuinely_different_models_apart():
    """闸 I-2 另一个反方向: 真的两个不同模型进来 ⇒ 列表**两项**, 且 `fell_back` 仍是 True。

    归一化做过头会把这两项合并 ⇒ `fell_back` 翻成 False ⇒ 一次**真回退**被说成没回退。
    """
    c = _stream_client(_ChunkScriptRouter(
        [("deepseek-v4-pro", True), ("converse/global.anthropic.claude-opus-5", True)]))
    ev = _done_event(c, model="opus-5")
    assert ev["models_used"] == ["deepseek-v4-pro",
                                 "converse/global.anthropic.claude-opus-5"], ev
    assert ev["fell_back"] is True, ev


def test_litellm_really_reports_two_spellings_for_one_model():
    """**现实锚**: 上面那条用的是我们自己的假 Router, 证的是"我们的合并逻辑"。
    这一条用**真 `create_router` + litellm 自带 `mock_response`** (零外部调用) 钉住
    "litellm 确实会报两种拼法" —— 它一旦变了, 这条会红, 而不是让合并逻辑悄悄变成一段无用代码。

    ⚠ **它证的是 litellm 的 mock 流的拼法逻辑, 不是真实 Bedrock 返回什么** (终审 N-3 /
    spec §7 L6b)。真实回退时 chunk 里到底写什么串仍未实测 (spec §7 L1) —— 别把这条闸
    读成"真实 provider 也这样"。

    源码佐证: `chunk_creator` 里 `model_response.model = self.model`, 而"用 chunk 自带
    model 覆盖"那支只对 Azure 生效。
    """
    import asyncio
    from server.llm_config import create_router, merge_reported_model

    async def collect():
        r = create_router(Settings())
        resp = await r.acompletion(model="opus-5", messages=[{"role": "user", "content": "hi"}],
                                   stream=True, mock_response="hello world",
                                   stream_options={"include_usage": True})
        return [getattr(ch, "model", None) async for ch in resp]

    raw = [m for m in asyncio.run(collect()) if m]
    assert len(raw) >= 2, f"抽取端失效, 下面的断言会变永真: {raw}"
    assert len(set(raw)) == 2, f"litellm 的拼法行为变了 (不再是两种): {sorted(set(raw))}"
    merged: list[str] = []
    for m in raw:
        merge_reported_model(merged, m)
    # 期望值随 N-2 一并从最短形改成最长(最限定)形 —— 见 merge_reported_model 的证明。
    assert merged == ["bedrock/converse/global.anthropic.claude-opus-5"], merged


def test_fell_back_warning_is_logged(capsys):
    """闸 (终审 Minor 4): 回退时那条运维日志此前零闸。

    它是回退在**用户屏幕之外**的唯一痕迹 —— 回退同时意味着"钱走了别的账"(C3/D4) 与
    "答案来自未验证模型", 值得能被 grep 到。删掉它不会有任何别的测试变红。
    """
    # ⚠ 用 capsys 不是 caplog: 本服务的 structlog 直接写 stdout, 不经 stdlib logging
    # 的 handler 链 —— caplog.text 恒为空, 那会让"没打日志"这一支变成永真式。
    ev = _done_event(_stream_client(_EchoModelRouter("deepseek-v4-pro")), model="opus-5")
    assert ev["fell_back"] is True, ev
    out = capsys.readouterr().out
    assert "model_fell_back" in out, \
        f"stdout 里没有 model_fell_back 这条日志; 末 500 字符: {out[-500:]!r}"
    assert "deepseek-v4-pro" in out, "日志里没写实际答题的模型, grep 出来也没用"
    # 反方向: 没回退时**不该**打这条 (否则日志里全是狼来了)
    _done_event(_stream_client(_EchoModelRouter(_OPUS5_REPORTED)), model="opus-5")
    assert "model_fell_back" not in capsys.readouterr().out


def test_badge_is_amber_when_a_verified_model_fell_back(flag_probe):
    """闸 **N-1**: 回退时的琥珀色判据必须是**常量 `true`**, 不能顺着 `verified` 走。

    ⚠ 终审复核变异 K05 存活 (79 全绿, 本人复跑确认): 把回退分支的 `unverified: true` 改成
    `unverified: verified === false`。此前**两个**回退场景的 `verified` 都是 `false`,
    与常量 `true` **逐字同输出** ⇒ 成因 D, 判据形状根本没被钉住。

    ⚠ 为什么这一格特别重要: `opus-5` 是四个可选模型里**唯一** `verified: true` 的, 又是
    下拉第一项 ⇒ **"用户停在 Opus 5 → Bedrock 挂 → DeepSeek 答"是最可能真实发生的那次回退**,
    而它的琥珀色恰好落在此前唯一没闸的那一格。

    成因 D 自查 —— 哪种错误实现在这组输入上会产出相同输出?
    答: `unverified: fellBack === true` (在这个分支里恒真) —— 但那与常量 `true` 在**本分支内
    语义等价**, 不是缺陷。真正要挡的"顺着 verified 走"已被这组输入分辨开。
    """
    got = flag_probe["fellBackVerified"]
    assert "unverified" in _badge_classes(got), got["badgeClass"]
    # 诱饵在场才算数: 这条消息的 verified 确实是 true (文案里没有 ⚠未验证)
    assert "⚠未验证" not in got["badgeText"], got["badgeText"]
    assert "已回退" in got["badgeText"], got["badgeText"]


def test_merge_never_collapses_two_providers_in_any_arrival_order():
    """闸 **N-2**: `_same_model` **不传递** —— `openai/gpt-4` ≡ `gpt-4` ≡ `azure/gpt-4`,
    但两端 ≢。任何"缩短已存条目"的合并策略都会经由中间那个裸形把两个 provider 串起来,
    于是**真回退被判成没回退** (`fell_back` 读的就是这份列表)。

    ⚠ 这条钉的是 `merge_reported_model` docstring 里那句**无条件** ⛔ 承诺真的无条件 ——
    本仓库既有判例: **假约束注释比过期注释更害人**。故这里跑**全部 6 种到达顺序**,
    而不是挑一个顺序验一下就算。

    实测三策略 (终审第 2 轮): 最短形 6/6 全错; 首见形只在"限定形先到"时对; 最长形 6/6 全对。
    """
    from itertools import permutations
    from server.llm_config import merge_reported_model
    for order in permutations(("openai/gpt-4", "gpt-4", "azure/gpt-4")):
        merged: list[str] = []
        for m in order:
            merge_reported_model(merged, m)
        assert len(merged) == 2, f"到达顺序 {order} 把两个 provider 并成了: {merged}"
        assert set(merged) == {"openai/gpt-4", "azure/gpt-4"}, f"{order} -> {merged}"


def test_merge_still_collapses_one_model_in_any_arrival_order():
    """闸 N-2 反方向: 别为了防合并把该合的也不合了 —— 同一模型的两种拼法, 无论谁先到,
    都必须收成**一项**, 且结果与到达顺序无关 (最长形的一个附带好处)。"""
    from server.llm_config import merge_reported_model
    long_, short = "bedrock/converse/global.anthropic.claude-opus-5", \
                   "converse/global.anthropic.claude-opus-5"
    for order in ((long_, short), (short, long_)):
        merged: list[str] = []
        for m in order:
            merge_reported_model(merged, m)
        assert merged == [long_], f"{order} -> {merged}"
