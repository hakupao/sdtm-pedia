# 多模型切换 (U1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 用户在 Chat UI 每次提问时自选答题模型 (四选一), 全部走公司 Bedrock。

**Architecture:** `settings.selectable_models` 作**唯一事实源**, LiteLLM Router 的模型组与 `/api/info` 吐给前端的下拉列表**都从它派生** —— 「UI 提供了 Router 没有的模型」在结构上不可能发生。只换答题环节; 判库/检索改写等辅助环节继续用固定模型。

**Tech Stack:** Python 3.14 / FastAPI / pydantic-settings / LiteLLM Router 1.88.1 / AWS Bedrock (bearer token) / 原生 JS 前端 (webchat)

**Spec:** `docs/superpowers/specs/2026-09-01-model-switching-design.md`

## Global Constraints

- 测试命令一律: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/ -p no:warnings -o addopts="-ra"`。基线 **1899 passed**, 每个 task 结束必须报数字。
- **不得修改**: `server/grounding.py`、`eval/prod_wirein/check_code_grounding.py`。`scripts/tests/test_ask_stream.py` 与 `test_ask_stream_web.py` 是既有红线闸 —— **只允许新增测试文件, 不得改这两个文件的现有断言**; 若你的改动迫使它们变红, 那是信号: 换改法或停下来报告。
- 每个 task 的新闸必须**两个方向都钉**。只钉一个方向时, 把值写死成常量也能绿。
- ⚠ **变异验证一律跑整个 `test_model_switching.py`, 不许用 `-k <子串>` 过滤** —— Task 1 实测: `-k selectable` 会把 `test_only_opus5_is_verified` deselect 掉 (`2 passed, 1 deselected`), 照字面跑那条变异命令**捕获不到篡改**, 是假阴性。「看起来在验证、实际没验」同款。
- 每个 task 收尾做**变异验证**: 把本 task 的实现回滚掉, 确认新闸变红, 给命令与真实输出。**变异脚本必须自证变异真的打上了** (改完 grep 回读或比 sha256) —— 拿未变异的代码跑出的"全绿"是**假确认不是报错**。
- 长效文档/注释里**不得引行号**, 引函数名或常量名。
- 不 commit 到 main; 分支 `feat/model-switching` 已建。
- 四个模型串 (逐字, 勿改):
  - `bedrock/converse/global.anthropic.claude-opus-5`
  - `bedrock/converse/global.anthropic.claude-sonnet-5`
  - `bedrock/converse/global.openai.gpt-5.6-terra`
  - `bedrock/converse/global.openai.gpt-5.6-sol`

---

## File Structure

| 文件 | 责任 | 动作 |
|---|---|---|
| `sdtm-rag/server/config.py` | `SelectableModel` 类型 + `selectable_models` 设置 | 修改 |
| `sdtm-rag/server/llm_config.py` | Router 从 `selectable_models` 派生模型组 + 工具能力注册 | 修改 |
| `sdtm-rag/server/router.py` | `InfoResponse` 加模型表; `AskStreamRequest.model` + 校验; `done` 事件加 `model_id`/`verified` | 修改 |
| `sdtm-rag/server/main.py` | ready 日志加 Bedrock 告警 | 修改 |
| `sdtm-rag/webchat/index.html` | 下拉控件 + 未验证提示条 | 修改 |
| `sdtm-rag/webchat/app.js` | 渲染下拉、提交 model、localStorage、显示 verified | 修改 |
| `sdtm-rag/scripts/tests/test_model_switching.py` | 本单元全部新闸 | **新建** |

---

### Task 1: 配置 — `selectable_models` 单一事实源

**Files:**
- Modify: `sdtm-rag/server/config.py` (`Settings` 类, LLM models 段)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py` (新建)

**Interfaces:**
- Produces: `server.config.SelectableModel` (pydantic `BaseModel`, 字段 `id: str`, `label: str`, `model: str`, `verified: bool`); `Settings.selectable_models: list[SelectableModel]`

- [ ] **Step 1: 写失败测试**

新建 `sdtm-rag/scripts/tests/test_model_switching.py`:

```python
"""多模型切换 (U1) 的闸。spec docs/superpowers/specs/2026-09-01-model-switching-design.md"""
from server.config import Settings


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
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q`
Expected: FAIL — `AttributeError` / `ImportError`, `Settings` 没有 `selectable_models`

- [ ] **Step 3: 实现**

在 `sdtm-rag/server/config.py` 的 `Settings` 类**之前**加类型, 在 LLM models 段**之后**加字段:

```python
class SelectableModel(BaseModel):
    """用户可在 Chat UI 选择的答题模型。

    这是 Router 模型组与前端下拉的**唯一事实源** —— 两者都从这张表派生, 故
    「UI 提供了 Router 没有的模型」在结构上不可能发生 (spec §3.1)。
    """

    id: str          # Router 组名 = 前端提交值
    label: str       # 下拉显示文字
    model: str       # litellm 模型串
    verified: bool   # ⟺ 该模型跑过反捏造抽检 (Rule 9 + 答题侧 guardrail) 并通过
```

```python
    # 用户可选答题模型 (spec §3.2)。只作用于**答题**; 判库(light)/检索改写不受影响 (C1)。
    # verified 的语义写死: 跑过反捏造抽检并通过。目前只有 opus-5 —— 联网通道那轮抽检
    # 就在它上面做的; sonnet-5 是 Claude 不代表验过。
    selectable_models: list[SelectableModel] = [
        SelectableModel(id="opus-5", label="Claude Opus 5",
                        model="bedrock/converse/global.anthropic.claude-opus-5",
                        verified=True),
        SelectableModel(id="sonnet-5", label="Claude Sonnet 5",
                        model="bedrock/converse/global.anthropic.claude-sonnet-5",
                        verified=False),
        SelectableModel(id="gpt-terra", label="GPT-5.6 Terra",
                        model="bedrock/converse/global.openai.gpt-5.6-terra",
                        verified=False),
        SelectableModel(id="gpt-sol", label="GPT-5.6 Sol",
                        model="bedrock/converse/global.openai.gpt-5.6-sol",
                        verified=False),
    ]
```

`BaseModel` 若尚未导入, 在文件顶部 `from pydantic import BaseModel`。

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q`
Expected: 3 passed

- [ ] **Step 5: 全量 + 变异验证**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/ -p no:warnings -o addopts="-ra"`
Expected: 1902 passed (1899 + 3)

变异: 把 `sonnet-5` 的 `verified` 改成 `True`, 跑 `-k selectable` → 必须变红。改回, grep 回读确认已还原。

- [ ] **Step 6: Commit**

```bash
git add sdtm-rag/server/config.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "feat(models): selectable_models 单一事实源 + verified 语义"
```

---

### Task 2: Router 从 `selectable_models` 派生模型组

**Files:**
- Modify: `sdtm-rag/server/llm_config.py` (`create_router`)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py` (追加)

**Interfaces:**
- Consumes: `Settings.selectable_models` (Task 1)
- Produces: `create_router(s)` 返回的 Router 除 `default`/`default-fallback`/`hard`/`light` 外, 另含每个 `SelectableModel.id` 同名组

- [ ] **Step 1: 写失败测试**

追加到 `test_model_switching.py`:

```python
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
    """裁定 F-1 的补偿闸: 校验端读 known_model_groups (意图), Router 是事实 ——
    二者必须逐项相等, 派生一旦坏掉这条就响。不需要任何假 Router。"""
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
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q -k router`
Expected: FAIL — `AssertionError: Router 缺少组 opus-5`

- [ ] **Step 3: 实现**

`sdtm-rag/server/llm_config.py` 的 `create_router` 里, 在 `model_list` 字面量之后追加:

```python
    # 用户可选模型: 每个 SelectableModel 派生一个同名组 (spec §3.3)。与上面四个内部组
    # 并存 —— default/hard/light 是内部用途 (判库/改写), 不受用户选择影响 (C1)。
    model_list += [
        {"model_name": m.id, "litellm_params": {"model": m.model}}
        for m in s.selectable_models
    ]
```

并在同文件加一个**共用**函数 (Task 5 的校验也读它, 见控制器裁定 F-1):

```python
INTERNAL_GROUPS = ("default", "default-fallback", "hard", "light")


def known_model_groups(s: Settings) -> set[str]:
    """Router 会有的全部组名。

    `create_router` 与 `/api/ask_stream` 的白名单校验**共用**本函数, 故"能选的"与
    "能调的"不存在两份定义。校验端不读 `llm_router.model_list` 是有意的: 仓库里 4 个
    测试文件约 15 处假 Router 都没有该属性, 而用 getattr 兜底会造出"没有 model_list
    就不校验"的静默旁路。等式由下面的闸钉住。
    """
    return set(INTERNAL_GROUPS) | {m.id for m in s.selectable_models}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q`
Expected: 7 passed

- [ ] **Step 5: 全量 + 变异验证**

Expected: 1906 passed

变异: 把派生那段的 `m.id` 改成 `m.label` → `test_router_derives_a_group_per_selectable_model` 必须变红。还原并 grep 回读。

- [ ] **Step 6: Commit**

```bash
git add sdtm-rag/server/llm_config.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "feat(models): Router 模型组从 selectable_models 派生"
```

---

### Task 3: 启动期 — 工具能力注册 + Bedrock 告警

**Files:**
- Modify: `sdtm-rag/server/llm_config.py` (新函数 `register_selectable_model_capabilities`)
- Modify: `sdtm-rag/server/main.py` (lifespan 调用 + ready 日志字段)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py` (追加)

**Interfaces:**
- Consumes: `Settings.selectable_models`
- Produces: `server.llm_config.register_selectable_model_capabilities(s) -> list[str]` — 返回**未走 Bedrock** 的模型 id 列表 (供 ready 日志告警; 空列表 = 全部合规)

- [ ] **Step 1: 写失败测试**

```python
def test_registration_makes_tools_supported_for_gpt():
    """LiteLLM 1.88.1 的 bedrock allowlist 不认 openai.*, 不注册就拒收 tools ——
    联网通道对 GPT 直接不可用。裸 boto3 已实测工具调用本身通 ⇒ 这是客户端元数据缺口。
    ⚠ 注册 key 必须**去掉 bedrock/ 前缀**, 用错前缀是静默无效 (spec §4.2)。"""
    import litellm
    from server.llm_config import register_selectable_model_capabilities
    register_selectable_model_capabilities(Settings())
    for mid in ["converse/global.openai.gpt-5.6-terra", "converse/global.openai.gpt-5.6-sol"]:
        assert litellm.supports_function_calling(model=mid, custom_llm_provider="bedrock_converse")


def test_registration_reports_non_bedrock_models():
    """闸 6 (C3): config.py 里三个 Claude 的硬编码默认值是 anthropic/ 直连, 只靠 .env
    改写且无任何校验 ⇒ .env 一缺就静默走直连。两个方向都钉。"""
    from server.llm_config import register_selectable_model_capabilities
    assert register_selectable_model_capabilities(Settings()) == []
    bad = Settings(selectable_models=[
        {"id": "x", "label": "X", "model": "anthropic/claude-opus-5", "verified": False}])
    assert register_selectable_model_capabilities(bad) == ["x"]
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q -k registration`
Expected: FAIL — `ImportError: cannot import name 'register_selectable_model_capabilities'`

- [ ] **Step 3: 实现**

`sdtm-rag/server/llm_config.py` 加:

```python
import litellm


def register_selectable_model_capabilities(s: Settings) -> list[str]:
    """给可选模型补 LiteLLM 能力元数据, 并报出未走 Bedrock 的那些。

    为什么需要: LiteLLM 的 bedrock provider allowlist 只认
    anthropic|mistral|cohere|meta.llama3-*|amazon.nova, 其余走 supports_function_calling()
    兜底, 而 registry 里没有 openai.gpt-5.6-* ⇒ 拒收 tools, 联网通道对 GPT 不可用。
    裸 boto3 Converse 已实测工具调用本身是通的 ⇒ 客户端元数据缺口, 非服务端限制。

    ⚠ 注册 key 必须是**去掉 bedrock/ 前缀**的形式 (litellm 内部就用这个查表)。
    用带前缀的 key 注册会**静默无效** —— 不报错, 直到有人开联网才炸。

    返回未走 Bedrock 的模型 id (C3 告警用); 空列表 = 全部合规。
    """
    info = {"litellm_provider": "bedrock_converse", "mode": "chat",
            "supports_function_calling": True}
    non_bedrock: list[str] = []
    for m in s.selectable_models:
        if not m.model.startswith("bedrock/"):
            non_bedrock.append(m.id)
            continue
        litellm.register_model({m.model.removeprefix("bedrock/"): dict(info)})
    return non_bedrock
```

`sdtm-rag/server/main.py` 的 lifespan 里, 紧跟 `app.state.llm_router = create_router(s)` 之后:

```python
    non_bedrock_models = register_selectable_model_capabilities(s)
    if non_bedrock_models:
        log.warning("selectable_models_not_on_bedrock", models=non_bedrock_models)
```

并把 `non_bedrock_models=non_bedrock_models` 加进 `ready` 日志的字段。
`from server.llm_config import create_router` 改为一并导入新函数。

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q`
Expected: 9 passed

- [ ] **Step 5: 全量 + 变异验证**

Expected: 1908 passed

变异两条, 各自还原并 grep 回读:
1. 把 `removeprefix("bedrock/")` 去掉 (即用带前缀的 key 注册) → `test_registration_makes_tools_supported_for_gpt` 必须变红。**这条正是控制器实测时踩过的静默失败。**
2. 把 `non_bedrock.append(m.id)` 那行删掉 → `test_registration_reports_non_bedrock_models` 必须变红。

- [ ] **Step 6: Commit**

```bash
git add sdtm-rag/server/llm_config.py sdtm-rag/server/main.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "feat(models): 启动期注册工具能力 + 非 Bedrock 告警"
```

---

### Task 4: `/api/info` 暴露模型表

**Files:**
- Modify: `sdtm-rag/server/router.py` (`InfoResponse` + `/api/info` 处理函数)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py` (追加)

**Interfaces:**
- Consumes: `Settings.selectable_models`, `create_router`
- Produces: `InfoResponse.selectable_models: list[SelectableModel]`

- [ ] **Step 1: 写失败测试**

```python
def _info_client(**kw):
    """/api/info 只读 rag/settings 上的几个属性, 最小 stub 即可 (照
    test_web_search_config.py 的既有写法), 不碰 chroma/embedding。"""
    from types import SimpleNamespace

    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from server.router import api_router

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
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q -k info`
Expected: FAIL — `KeyError: 'selectable_models'`

- [ ] **Step 3: 实现**

`sdtm-rag/server/router.py` 的 `InfoResponse` 加字段 (放在 `compare_models` 旁):

```python
    # 用户可选答题模型 (spec §7)。前端下拉直接渲染这张表 —— 与 Router 组同源, 见 §3.1。
    selectable_models: list[SelectableModel] = Field(default_factory=list)
```

`/api/info` 处理函数的 `InfoResponse(...)` 调用里加 `selectable_models=s.selectable_models,`。
顶部导入 `SelectableModel`。

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q`
Expected: 11 passed

- [ ] **Step 5: 全量 + 变异验证**

Expected: 1910 passed

变异: 让 `/api/info` 吐一个 Router 里没有的模型 (临时在传给 `InfoResponse` 的列表里塞一项
`{"id": "ghost", ...}`) → `test_info_model_table_is_subset_of_router_groups` 必须变红。还原并 grep 回读。

- [ ] **Step 6: Commit**

```bash
git add sdtm-rag/server/router.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "feat(models): /api/info 暴露模型表 (含 verified)"
```

---

### Task 5: `AskStreamRequest.model` + 白名单校验

**Files:**
- Modify: `sdtm-rag/server/router.py` (`AskStreamRequest`, `ask_stream` 的 `kw` 构造)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py` (追加)

**Interfaces:**
- Consumes: Router 组名集合 (Task 2)
- Produces: `AskStreamRequest.model: str = "default"`; 未知值 → HTTP 422

- [ ] **Step 1: 写失败测试**

```python
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


def test_ask_stream_default_is_unchanged():
    """零影响硬要求: 不传 model 时走 default 组, 与本功能引入前逐位相同。"""
    c = _stream_client()
    assert c.post("/api/ask_stream", json={"question": "AETERM?"}).status_code == 200
    assert c.app.state.llm_router.last_model == "default"
```

本 task 需要的两个 helper (加在 `test_model_switching.py` 里; **不得改** `test_ask_stream.py`,
下面的 `_FakeRAG` 是照它的形状**另写一份**):

```python
import json
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.router import api_router


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
    """记下**实际**传给 acompletion 的组名。

    校验通过 ≠ 真的用了那个模型 —— 少了这一层, 把 kw 里的组名写死成 "default"
    也能让"接受每个模型"的测试全绿 (记事实不记意图)。
    """

    def __init__(self):
        self.last_model = None

    async def acompletion(self, model, messages, stream=False, **kw):
        self.last_model = model

        async def agen():
            yield SimpleNamespace(model=f"resolved-{model}", usage=None,
                                  choices=[SimpleNamespace(delta=SimpleNamespace(content="ok"))])
            yield SimpleNamespace(model=f"resolved-{model}", choices=[],
                                  usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1,
                                                        total_tokens=2))
        return agen()


def _stream_client():
    s = Settings()
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = _CapturingRouter()
    app.state.settings = s
    return TestClient(app)
```

第三条测试的最后一行相应写成 `assert c.app.state.llm_router.last_model == "default"`。

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q -k ask_stream`
Expected: FAIL — 未知模型返回 200 而非 422 (字段被 pydantic 忽略或未校验)

- [ ] **Step 3: 实现**

`AskStreamRequest` 加字段 (与 `AskRequest` 同名同默认值, 两端点口径一致):

```python
    # 答题模型组名。与 AskRequest.model 同名同默认值。校验在 ask_stream 里做 ——
    # 合法值集合来自 Router (与 /api/info 同源), pydantic 层拿不到它。
    model: str = "default"
```

`ask_stream` 函数体内, 在空问题校验之后加:

⚠ **控制器裁定 F-1**: 校验读 `known_model_groups(s)`, **不读** `llm_router.model_list` ——
仓库里 4 个测试文件约 15 处假 Router 都没有该属性 (含两个红线文件), 读它会让它们全部 500。
等式由 Task 2 的 `test_known_groups_equals_what_router_actually_has` 钉住。

```python
    known = known_model_groups(s)
    if body.model not in known:
        # ⛔ 不静默退回 default: 静默退回会让"选了模型 X 却拿到 Y 的答案"完全不可见。
        raise HTTPException(status_code=422,
                            detail=f"unknown model {body.model!r}; known: {sorted(known)}")
```

并把开流处 `kw = {"model": "default", ...}` 改为 `kw = {"model": body.model, ...}`。

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q`
Expected: 14 passed

- [ ] **Step 5: 全量 + 变异验证**

Expected: 1913 passed。**`test_ask_stream.py` / `test_ask_stream_web.py` 必须一字未改且全绿** —— 单独跑一遍并贴输出。

变异两条, 各自还原并 grep 回读:
1. 把 422 改成静默退回 `body.model = "default"` → `test_ask_stream_rejects_unknown_model` 必须变红。
2. 把 `kw` 里的 `body.model` 改回写死 `"default"` → `test_ask_stream_accepts_every_selectable_model` 仍绿 (它只看状态码), 但 Task 6 的闸会抓 —— **在 Task 6 收尾时复跑这条变异确认**。

- [ ] **Step 6: Commit**

```bash
git add sdtm-rag/server/router.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "feat(models): ask_stream 收 model 参数 + 白名单校验 (未知 422)"
```

---

### Task 6: `done` 事件带 `model_id` + `verified` (产物自证)

**Files:**
- Modify: `sdtm-rag/server/router.py` (`ask_stream` 的 `done` 事件)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py` (追加)

**Interfaces:**
- Consumes: `body.model`, `Settings.selectable_models`
- Produces: `done` 事件新增 `model_id: str`、`verified: bool | None`

- [ ] **Step 1: 写失败测试**

```python
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
```

本 task 需要的 helper (加在 `test_model_switching.py`)。`sse()` 的格式是
`event: <name>\ndata: <json>\n\n`:

```python
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
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q -k done_event`
Expected: FAIL — `KeyError: 'model_id'`

- [ ] **Step 3: 实现**

`ask_stream` 内, 在校验之后算一次 (供 `gen()` 闭包使用):

```python
    verified_by_id = {m.id: m.verified for m in s.selectable_models}
    # default/hard/light 不在表里 ⇒ None = "未知", 不是 False。发 False 会把"没这个概念"
    # 误报成"验过且不通过" (spec §6)。
    model_verified = verified_by_id.get(body.model)
```

`done` 事件改为:

```python
            yield sse("done", {"model_used": model_used or "default",
                               "model_id": body.model,
                               "verified": model_verified,
                               "usage": usage, "web_status": web_status,
                               "web_searches_ok": web_ok})
```

⚠ `model_used` 保持原样 —— 它装的是 provider 返回的**真实模型串** (`getattr(chunk, "model")`),
与 `model_id` (用户选的组名) 是两件事, 两个都要留: 前者是事实, 后者是选择, fallback 触发时二者会不同。

- [ ] **Step 3b: `reasoningContent` 显式决定丢弃 (spec §4.3)**

流式循环现在只读 `getattr(ch.delta, "content", ...)` 与 `getattr(ch.delta, "tool_calls", ...)`,
其余字段一律忽略 ⇒ Sol 的推理块**今天就是被丢的**。功能上正确 (模型内部思考不该进知识库答案),
但它现在是**构造上的偶然, 不是决定**。在那两行 `getattr` 之上加注释, 把它变成决定:

```python
                        # 只取 content / tool_calls, 其余 delta 字段有意丢弃 ——
                        # 含 GPT-5.6 Sol 的 reasoning_content (模型内部思考, 不该进
                        # 知识库答案, 更不该被当成引用来源)。spec §4.3。
                        # 实测边界: 流式下两个 GPT 均未发该增量, 只有非流式 boto3 调用
                        # 时 Sol 发了 reasoningContent 块 ⇒ 这是预防, 不是现实问题。
```

⚠ 本步**只加注释, 不改行为** —— 不要为它加闸 (没有可断言的行为变化), 也不要顺手去"支持"它。

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings -q`
Expected: 16 passed

- [ ] **Step 5: 全量 + 变异验证**

Expected: 1915 passed

变异三条, 各自还原并 grep 回读:
1. `verified_by_id.get(body.model)` 改成 `verified_by_id.get(body.model, False)` →
   `test_done_event_verified_is_null_for_default_group` 必须变红。
2. `"model_id": body.model` 改成写死 `"opus-5"` → 第一条测试必须变红。
3. **复跑 Task 5 遗留的那条**: `kw` 里的 `body.model` 改回写死 `"default"` → 确认现在有闸抓得到
   (若仍无人变红, 这是 finding, 报告并补闸)。

- [ ] **Step 6: Commit**

```bash
git add sdtm-rag/server/router.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "feat(models): done 事件带 model_id + verified (产物自证)"
```

---

### Task 7: Chat UI 下拉 + 未验证标注 + localStorage

**Files:**
- Modify: `sdtm-rag/webchat/index.html` (`#scope` fieldset 旁加控件)
- Modify: `sdtm-rag/webchat/app.js` (渲染下拉 / 提交 model / 持久化 / 显示 verified)
- Test: 浏览器手工验证 (本项目 webchat 无自动化前端测试; 照 I-E 先例用浏览器变异验证)

**Interfaces:**
- Consumes: `/api/info` 的 `selectable_models`; `done` 事件的 `model_id`/`verified`

- [ ] **Step 1: 加控件**

`index.html` 的 `#scope` fieldset 之后加:

```html
        <select id="model-select" title="答题模型"></select>
        <div id="model-warning" hidden>⚠ 该模型的反捏造边界未在其上验证</div>
```

- [ ] **Step 2: 渲染下拉 + 持久化**

`app.js` 读 `/api/info` 的那段 (现在只读 `default_model` 做 topbar 显示) 之后加:

```javascript
  // 下拉从 /api/info 的模型表渲染 —— 与 Router 组同源, 故不可能提供后端没有的模型。
  const sel = $("model-select");
  (info.selectable_models || []).forEach((m) => {
    const o = document.createElement("option");
    o.value = m.id;
    // 未验证的在文字上标出来: 用户选之前就该看见, 而不是选完才知道
    o.textContent = m.verified ? m.label : `${m.label} ⚠未验证`;
    o.dataset.verified = String(m.verified);
    sel.appendChild(o);
  });
  // 刷新保留 —— 终审 I-E (联网状态过不了刷新) 的同款, 不重犯
  const saved = localStorage.getItem("sdtm_model");
  if (saved && [...sel.options].some((o) => o.value === saved)) sel.value = saved;
  const syncWarning = () => {
    const o = sel.selectedOptions[0];
    $("model-warning").hidden = !o || o.dataset.verified === "true";
  };
  sel.addEventListener("change", () => {
    localStorage.setItem("sdtm_model", sel.value);
    syncWarning();
  });
  syncWarning();
```

- [ ] **Step 3: 提交 model**

在构造 `/api/ask_stream` 请求体处:

```javascript
  // spec §5 裁定: UI **永远发显式 id**, 绝不依赖默认值落到 default 组 ——
  // default 与 opus-5 今天都解析到 Opus 5, 但改 .env 的 default_model 会让二者静默分叉。
  // 下拉为空 (info 没加载出来) 时**整个字段省略**, 由服务端默认值接管, 而不是硬塞 "default"
  // ——「省略」与「显式传 default」在服务端是同一行为, 但省略不会在产物里留下一个
  // 用户根本没做过的选择。
  const chosen = $("model-select").value;
  if (chosen) payload.model = chosen;
```

- [ ] **Step 4: 浏览器验证 (四条, 逐条截图或贴 console 输出)**

1. 下拉出现四项, `Claude Sonnet 5 / GPT-5.6 Terra / GPT-5.6 Sol` 带 `⚠未验证`, `Claude Opus 5` 不带
2. 选未验证模型 → 提示条出现; 切回 Opus 5 → 消失
3. 选 `gpt-sol` → **刷新页面** → 仍是 `gpt-sol` 且提示条仍在 (I-E 同款验证)
4. 选 `gpt-terra` **并开启联网** 提一个问题 → 能正常出答案与 `[Web:]` 引用
   (这条同时验证 Task 3 的工具能力注册在真实链路上生效)

- [ ] **Step 5: 变异验证 (浏览器)**

把 Step 2 里 `o.textContent` 的三元改成恒 `m.label` → 刷新页面, 未验证模型的 `⚠未验证` 消失
⇒ 证明该标注确实由 `verified` 驱动而非写死。还原。

- [ ] **Step 6: 全量 + Commit**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/ -p no:warnings -o addopts="-ra"`
Expected: 1915 passed (前端改动不影响 Python 测试)

```bash
git add sdtm-rag/webchat/index.html sdtm-rag/webchat/app.js
git commit -m "feat(models): Chat UI 模型下拉 + 未验证标注 + 刷新保留"
```

---

## 收尾 (全部 task 完成后, 由控制器执行)

1. 独立复审 (Rule D: 与实现者不共享上下文), 重点核: 六条闸是否真有牙齿 (自己做变异)、
   `test_ask_stream*.py` 是否一字未改、Task 7 的浏览器验证是否真做了。
2. spec §9 欠账表按实际情况更新。
3. `.work/meta/worklog/phase_07_rag_kg.md` append; `docs/PROGRESS.md` 更新; `CLAUDE.md` Key Paths 加一行。
