# D6 + D5 (model_used 上闸 + 恢复容灾且诚实呈现) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 先给 SSE `done` 事件的 `model_used` 补上取值断言 (D6), 再恢复 Chat UI 主路径的
fallback 容灾 (D5), 并让「实际答题的是谁」在徽章、存档、⚑ 归档三处都说真话。

**Architecture:** `create_router` 从 `selectable_models` 派生 fallback 表 (不手写第二份清单);
`server/llm_config.py` 新增纯函数 `fell_back(s, group, reported)` 做三态判定 (`True`/`False`/`None`);
`done` 事件多发一个 `fell_back` 字段; `webchat/app.js` 的徽章/存档/⚑ 归因全部跟着这个字段走。

**Tech Stack:** Python 3.14 · FastAPI · litellm Router · pytest (`.venv/bin/python -m pytest`) ·
原生 JS (`webchat/`) · node `vm` 探针 (`scripts/tests/fixtures/*.mjs`)

**Spec:** `docs/superpowers/specs/2026-09-02-model-fallback-honesty-design.md`

## Global Constraints

- **基线**: `2bcd840` = **1956 passed, 1 skipped**。每个 task 报数字必须**实际重跑**, 不许套用记忆; 报数字必须附 commit 号。
- **顺序硬约束**: Task 1 (D6) 必须先于 Task 2/3 (D5) 合入 —— 先有闸再引入 fallback 行为。
- **Rule D (审阅隔离)**: 实现者与复审必须是不同 `subagent_type`, 不得同 context 自审。
- **变异验证**: 每条新闸都要**逐条隔离**变异 (一次只打一处), 且变异脚本**必须自证变异真的打上了** (改完 `grep` 回读或比 `sha256`)。
- **变异范围**: 一律跑**整个测试文件**, ⛔ 禁用 `-k` 过滤 (子串与函数命名的耦合是隐式的, 失配的表现就是"全绿")。
- **还原方式**: ⛔ **不许 `git checkout -- <file>`** —— 工作区有未提交修复时它撤销的是**一切**。一律用**字节回写** (变异前存原文, 变异后写回, 再比 sha256)。
- **红线**: ⛔ **绝不碰 `localhost:8000` 的 launchd 服务** (用户在用): 不重启、不 `kill`、不改 plist。需要跑服务时用备用端口一次性 stub。
- ⚠ **`webchat/` 是从工作树挂载的** (`StaticFiles`, 每请求现读) ⇒ 改 `app.js` **立刻**出现在用户正在跑的服务上, 而 Python 改动要重启才生效。⇒ spec §5 的 B1「新前端 + 老后端」不是假想, 是必然中间态, 闸 G10 必须绿。
- **不动的文件**: `server/grounding.py`、`eval/prod_wirein/check_code_grounding.py`、`scripts/tests/test_ask_stream.py`、`scripts/tests/test_ask_stream_web.py` (红线文件, 本轮零改动)。
- 提交信息用中文, 结尾按仓库约定加 `Co-Authored-By` 与 `Claude-Session` 两行。

---

### Task 1: D6 —— `model_used` 三向上闸 + 去掉写死的 `"default"`

**Files:**
- Modify: `sdtm-rag/server/router.py` (`ask_stream` 的 `done` 事件, `yield sse("done", {...})` 那一处)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py` (追加, 放在既有 `test_done_event_verified_is_null_for_default_group` 之后)

**Interfaces:**
- Consumes: 既有 `_stream_client()` / `_CapturingRouter` / `_done_event()` helper (同文件内)
- Produces: `_stream_client(router=None)` 签名 (Task 2/3 会复用); `_EchoModelRouter` 类 (Task 3 会复用)

- [ ] **Step 1: 写失败的测试**

在 `scripts/tests/test_model_switching.py` 里, 先把既有 helper 改成可注入 router
(原调用点 `_stream_client()` 不传参, 行为不变):

```python
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
```

再追加三条闸:

```python
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
```

- [ ] **Step 2: 跑测试确认它失败**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
```
Expected: 前两条 PASS (现有实现已经从 chunk 取值), **第三条 FAIL** —— 实际拿到 `"default"`。
⚠ 前两条一开始就绿是**预期**的 (它们补的是"零断言"这个洞, 不是修 bug); 它们的有效性由 Step 5 的变异证明, 不是由"红过"证明。

- [ ] **Step 3: 改实现**

`server/router.py`, `done` 事件那一行:

```python
            yield sse("done", {"model_used": model_used,
```

(删掉 ` or "default"`) 并在 `model_used = None` 的初始化处补一句注释:

```python
        model_used = None   # 流里一个 chunk 都没报模型时就一直是 None —— done 事件如实发 null,
                            # ⛔ 不许兜成 "default": 那是**编**一个模型名, 而这个值会进历史存档
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings   # 全绿
.venv/bin/python -m pytest scripts/tests/ -p no:warnings                          # 1959 passed, 1 skipped
```
⚠ 报告里必须写**实际跑出来的数字**, 不许照抄这里的 1959 —— 对不上就说明有别的东西动了, 那是信息不是噪音。

- [ ] **Step 5: 变异验证 (逐条隔离, 脚本自证变异打上了)**

三个变异各跑一次, 每次只打一处:

| # | 变异 | 期望 |
|---|---|---|
| M1 | `"model_used": model_used` → `"model_used": body.model` | G1 两条红 |
| M2 | `"model_used": model_used` → `"model_used": model_used or "default"` | G3 红 |
| M3 | `_EchoModelRouter` 的 `yield SimpleNamespace(model=reported, ...)` → `model="resolved-" + model` | G1 反向红 (证明该 fake 真的与组名解耦, 不是碰巧) |

变异脚本骨架 (放 scratchpad, 不进仓库):

```python
import hashlib, pathlib, subprocess, sys
p = pathlib.Path("server/router.py")
orig = p.read_bytes()
before = hashlib.sha256(orig).hexdigest()
new = orig.replace(b'"model_used": model_used,', b'"model_used": body.model,')
assert new != orig, "锚点没命中 —— 变异根本没打上, 下面跑出来的绿是假的"
p.write_bytes(new)
assert hashlib.sha256(p.read_bytes()).hexdigest() != before, "回读自证失败"
r = subprocess.run([".venv/bin/python", "-m", "pytest",
                    "scripts/tests/test_model_switching.py", "-p", "no:warnings"],
                   capture_output=True, text=True)
p.write_bytes(orig)                                  # 字节回写, ⛔ 不用 git checkout
assert hashlib.sha256(p.read_bytes()).hexdigest() == before, "还原失败"
print(r.stdout[-1500:])
```

⚠ **自问一遍**: 如果我的变异根本没打上, 这次运行的输出会跟现在有什么不同? 答不出来就还没验证。

- [ ] **Step 6: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
git add sdtm-rag/server/router.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "fix(models): D6 — done 事件 model_used 三向上闸 + 去掉写死的 default"
```

---

### Task 2: D5.1 —— fallback 表从 `selectable_models` 派生

**Files:**
- Modify: `sdtm-rag/server/llm_config.py` (`create_router`)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py`

**Interfaces:**
- Consumes: `_validated_selectable_models(s)` (同文件既有的 fail-loud 撞名闸)
- Produces: `_fallback_map(s) -> list[dict[str, list[str]]]`; 测试 helper `_fallbacks(router) -> dict`; 测试 helper `_real_router_stream(monkeypatch, *, model, fallbacks=None) -> str` (Task 3 复用)

- [ ] **Step 1: 写失败的测试**

```python
_FALLBACK_GROUP = "default-fallback"


def _fallbacks(router) -> dict:
    """`Router.fallbacks` 是 list[dict], 摊平成 {组名: [兜底组]}。

    ⚠ 先断尺寸下限: 表塌成空的时候, 下面所有"某组**不在**表里"的断言都会变成
    永真式 (retrospective 规则 6 成因 A)。
    """
    flat = {k: v for entry in router.fallbacks for k, v in entry.items()}
    assert len(flat) >= 5, f"fallback 表塌了, 下面的断言会变永真: {router.fallbacks}"
    return flat


def test_every_selectable_group_falls_back_to_the_default_fallback_group():
    """闸 G4 (spec §9 D5): U1 那轮 UI 从"永发 default 组"改成"永发显式 id",
    而四个新派生组没有 fallback 条目 ⇒ **主模型没变, 容灾网没了**。
    DEPLOY_PLAN.md 记着实测「Anthropic credits 耗尽 → DeepSeek 自动回退」真的生效过。
    """
    s = Settings()
    flat = _fallbacks(create_router(s))
    for m in s.selectable_models:
        assert flat.get(m.id) == [_FALLBACK_GROUP], f"{m.id} 没有容灾: {flat.get(m.id)}"
    assert flat["default"] == [_FALLBACK_GROUP], "既有 default 组的容灾不许丢"


def test_internal_worker_groups_have_no_fallback():
    """闸 G5 反方向 (C1)。"一律给所有组加 fallback" 的偷懒实现会让这条红:

    - `light` 是判库、`hard` 是检索改写 —— C1 明确要求它们**不受用户选择影响**,
      能悄悄换模型就等于破了 C1 (判库换了模型, 检索结果跟着变, 对比时分不清
      是模型差异还是检索差异);
    - `default-fallback` 给自己配 fallback 是个环。
    """
    flat = _fallbacks(create_router(Settings()))
    for g in ("hard", "light", _FALLBACK_GROUP):
        assert g not in flat, f"{g} 不该有 fallback 条目: {flat}"


def _real_router_stream(monkeypatch, *, model, fallbacks=None) -> str:
    """用**真 litellm Router** 跑一次 `/api/ask_stream`, 返回整段 SSE 文本。

    ⚠ patch 的是 `litellm.acompletion` —— Router 每个 deployment 最终调的那个函数
    (实测: `Router.acompletion` 无论 stream 与否都走 `async_function_with_fallbacks`,
    再落到它)。⛔ 不能用仓库里的假 Router 测这条: 假 Router 根本没有 fallback 逻辑,
    拿它测容灾等于测了个寂寞 —— 这正是"闸看起来在测、其实没测"的形状。

    `fallbacks=None` 用 `create_router` 派生的真实配置; 传别的值可以模拟"没有容灾"。
    """
    import litellm

    async def fake_acompletion(**kw):
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
    return TestClient(app).post("/api/ask_stream",
                                json={"question": "AETERM?", "model": "opus-5"}).text


def test_stream_survives_a_dead_primary_deployment(monkeypatch):
    """闸 G6 正向, **端到端**: 主模型开流抛错 ⇒ 流不该死, 由 default-fallback 接管,
    且 `done.model_used` 报的是**实际**答题的那个。

    ⚠ `Settings()` 的类默认值里 opus-5 走 `bedrock/converse/global.anthropic.*`,
    所以 fake 里那句 `"anthropic" in model` 打的就是它。
    """
    text = _real_router_stream(monkeypatch, model="opus-5")
    assert "event: error" not in text, text[:400]
    blocks = [b for b in text.split("\n\n") if b.startswith("event: done")]
    assert len(blocks) == 1, f"没解析到唯一的 done 事件: {text[:400]!r}"
    ev = json.loads(next(l for l in blocks[0].splitlines() if l.startswith("data: "))[6:])
    assert ev["model_used"] == "deepseek-v4-pro", ev
    assert ev["model_id"] == "opus-5", ev


def test_stream_dies_without_the_fallback_entry(monkeypatch):
    """闸 G6 反向: 把 fallback 表退回**分支前的样子** (只有 default 组一条) ⇒
    同样的失败变成 `event: error`。

    这条同时是 D5 那个回归的**复现**: 它红了才说明上一条不是靠别的什么东西绿的。
    """
    text = _real_router_stream(monkeypatch, model="opus-5",
                               fallbacks=[{"default": ["default-fallback"]}])
    assert "event: error" in text, text[:400]
```

- [ ] **Step 2: 跑测试确认它失败**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
```
Expected: `test_every_selectable_group_falls_back...` FAIL (`flat.get("opus-5")` 是 `None`);
`_fallbacks` 的尺寸下限也会先炸 (今天只有 1 条) —— 两种红都算预期。
`test_stream_survives_a_dead_primary_deployment` FAIL (`event: error`)。
`test_internal_worker_groups_have_no_fallback` 因尺寸下限 FAIL。
⚠ 若某条**没红**, 停下来查原因再往下走。

- [ ] **Step 3: 改实现**

`server/llm_config.py`:

```python
def _fallback_map(s: Settings) -> list[dict[str, list[str]]]:
    """答题组 → `default-fallback` 的容灾表, 从 `selectable_models` **派生**。

    ⛔ 不手写第二份清单 —— 与 `known_model_groups` 同一条理由 (spec 2026-09-01 §3.1):
    两份真相会各自漂移, 而"UI 有某个组、容灾表没有"这种漏正好是无声的。

    表里**只有**答题组: `default` (既有调用方 / `/api/ask` / eval 脚本) 与四个可选模型。
    ⛔ `hard` / `light` 不进表 —— 它们是检索改写与判库, C1 要求不受用户选择影响,
    能悄悄换模型就破了 C1。`default-fallback` 也不进表 (给自己配 fallback 是个环)。

    ⚠ 代价是**明的**: 兜底落在 `default-fallback` = DeepSeek **个人流量** (spec §9 D4),
    即答题有可能不走公司 Bedrock。用户 2026-09-02 裁定接受, 条件是**必须让用户看得见** ——
    `done` 事件的 `fell_back` 字段与前端徽章就是那个条件的兑现, 不许只补这半边。
    """
    return [{g: ["default-fallback"]}
            for g in ("default", *(m.id for m in _validated_selectable_models(s)))]
```

`create_router` 的 `Router(...)` 调用改一行:

```python
        fallbacks=_fallback_map(s),
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -p no:warnings
```
⚠ 端到端那两条若单条超过 ~10 秒, 记下实际耗时并在报告里说明 (litellm 的冷却/退避)。

- [ ] **Step 5: 变异验证 (逐条隔离)**

| # | 变异 | 期望 |
|---|---|---|
| M1 | `_fallback_map` 的 `("default", *(...))` → `("default",)` | G4 + G6 正向红 |
| M2 | `_fallback_map` 改成给 `known_model_groups(s)` 里**所有**组加 fallback | G5 红 (C1 方向) |
| M3 | `_fallbacks()` helper 里的尺寸下限 `>= 5` 删掉, 同时把 `_fallback_map` 返回 `[]` | 证明尺寸下限确实是那条防永真的锚 (删掉后 G5 变绿 = 假阴性) |

M3 是**对闸本身**的变异 —— 规则 6 成因 A 那一族。做完必须两处都还原。

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/server/llm_config.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "fix(models): D5.1 — 四个可选模型组补 fallback, 表从 selectable_models 派生"
```

---

### Task 3: D5.2 —— `fell_back` 三态判定 + `done` 事件接线

**Files:**
- Modify: `sdtm-rag/server/llm_config.py` (新增 `fell_back`)
- Modify: `sdtm-rag/server/router.py` (`done` 事件 + import + 一条 warning 日志)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py`

**Interfaces:**
- Consumes: Task 2 的 `_real_router_stream` helper; Task 1 的 `_EchoModelRouter`
- Produces: `fell_back(s: Settings, model_group: str, reported_model: str | None) -> bool | None`;
  `done` 事件新字段 `fell_back` (Task 4/5 的前端读它)

- [ ] **Step 1: 写失败的测试**

```python
_OPUS5 = "bedrock/converse/global.anthropic.claude-opus-5"   # config.py 里 opus-5 的配置串


def test_fell_back_is_false_when_the_reported_model_is_the_configured_one():
    """闸 G7 (a): 实测 chunk 报的是**去掉 provider 前缀**的串
    (`bedrock/converse/global.anthropic.claude-opus-5` → `global.anthropic.claude-opus-5`),
    两种形式都必须认作"同一个模型"。"""
    s = Settings()
    assert fell_back(s, "opus-5", "global.anthropic.claude-opus-5") is False
    assert fell_back(s, "opus-5", _OPUS5) is False


def test_fell_back_is_true_when_another_model_answered():
    """闸 G7 (b): 这就是容灾真的触发时的样子 —— 用户选 gpt-sol, DeepSeek 答的。"""
    assert fell_back(Settings(), "gpt-sol", "deepseek-v4-pro") is True


def test_fell_back_is_none_for_internal_groups_and_missing_reports():
    """闸 G7 (c): ⛔ 不知道就发 `None`, **不得发 `False`**。

    `False` 的语义是"确证没回退"; 内部组 (default/hard/light/default-fallback) 压根
    不在 `selectable_models` 里, **没有"用户选的模型串"这个概念** —— 发 False 就是
    把"没这个概念"报成了一个确证结论。与同一个 done 事件里 `verified` 的三态同一条原则。
    """
    s = Settings()
    for g in ("default", "hard", "light", "default-fallback"):
        assert fell_back(s, g, "deepseek-v4-pro") is None, g
    assert fell_back(s, "opus-5", None) is None
    assert fell_back(s, "opus-5", "") is None


def test_fell_back_match_requires_a_path_boundary():
    """闸 G8: 匹配必须带 `/` 边界, ⛔ 不许裸子串。

    `claude-opus-5` 是配置串的真子串, 但它**不是**一个完整的模型标识 ——
    把实现写成 `reported in configured` 会让这条红。裸子串正是 retrospective
    规则 6 成因 A 的形状 (判定式被悄悄放宽成近乎恒真)。
    """
    assert fell_back(Settings(), "opus-5", "claude-opus-5") is True
    assert fell_back(Settings(), "opus-5", "anthropic.claude-opus-5") is True


def test_done_event_carries_fell_back_three_ways():
    """闸 G7 端到端 (SSE 层): 纯函数对不代表接线对。"""
    ev = _done_event(_stream_client(_EchoModelRouter("global.anthropic.claude-opus-5")),
                     model="opus-5")
    assert ev["fell_back"] is False, ev
    ev = _done_event(_stream_client(_EchoModelRouter("deepseek-v4-pro")), model="opus-5")
    assert ev["fell_back"] is True, ev
    ev = _done_event(_stream_client(_EchoModelRouter("deepseek-v4-pro")))   # 不传 model
    assert ev["fell_back"] is None, ev


def test_real_fallback_path_reports_fell_back(monkeypatch):
    """闸 G6 + G7 合流: 真 Router 真触发容灾时, 事件必须自己说出这件事。

    这条是本轮的**中心断言** —— 用户原话: 不做的话"用户选 Sol、DeepSeek 答题、
    徽章却说 Sol", 就是刚修掉的 C-1 (⚑ 归错模型) 同族缺陷换了个位置。
    """
    text = _real_router_stream(monkeypatch, model="opus-5")
    blocks = [b for b in text.split("\n\n") if b.startswith("event: done")]
    assert len(blocks) == 1, text[:400]
    ev = json.loads(next(l for l in blocks[0].splitlines() if l.startswith("data: "))[6:])
    assert ev["fell_back"] is True, ev
    assert ev["model_used"] == "deepseek-v4-pro", ev
    assert ev["model_id"] == "opus-5", ev
    assert ev["verified"] is True, "verified 记的是**用户选的**模型验没验过, 这个事实不变"
```

`fell_back` 需要 import: 在测试文件顶部既有的 `from server.llm_config import ...` 里加。

- [ ] **Step 2: 跑测试确认它失败**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
```
Expected: 全部新条目 FAIL/ERROR (`ImportError: cannot import name 'fell_back'`)。

- [ ] **Step 3: 改实现**

`server/llm_config.py` 追加:

```python
def fell_back(s: Settings, model_group: str, reported_model: str | None) -> bool | None:
    """答这道题的, 是不是用户选的那个模型? 不知道就返 `None` —— ⛔ 不返 `False`。

    `None` 与 `False` 语义不同, 混同即撒谎: `False` 是"确证没回退", `None` 是
    "这里没有可比对的东西"。内部组 (default/hard/light/default-fallback) 不在
    `selectable_models` 里, 没有"用户选的模型串"这个概念 ⇒ `None`。
    同一个 done 事件里 `verified` 的三态是同一条原则 (2026-09-01 spec §6)。

    `reported_model` 来自流式 chunk 的 `.model`, 实测是**去掉 provider 前缀**的串
    (`bedrock/converse/global.anthropic.claude-opus-5` → `global.anthropic.claude-opus-5`),
    故两种形式都认。⛔ 匹配必须带 `/` 边界: 裸子串会让 `claude-opus-5` 这类**不完整**
    标识也算命中 (retrospective 规则 6 成因 A)。

    ⚠ 已知限制 (spec §7 L1): "真实回退时 chunk 里到底写什么串"本轮没有真实调用的实测,
    唯一证据是 DEPLOY_PLAN.md 里 `/api/ask` 非流式那次。若真串与配置串对不上, 表现是
    **每条答案都误报"已回退"** —— 响的失败, 不是静默的, 上线第一条真实回答即可证伪。
    """
    if not reported_model:
        return None
    configured = next((m.model for m in _validated_selectable_models(s)
                       if m.id == model_group), None)
    if configured is None:
        return None
    return not (configured == reported_model
                or configured.endswith("/" + reported_model))
```

`server/router.py`: 在既有 `from server.llm_config import known_model_groups` 一行里补 `fell_back`
(若 import 形态不同, 照它的样子加), 然后把 `done` 事件那段改成:

```python
            fell = fell_back(s, body.model, model_used)
            if fell:
                # 让运维日志也留痕, 不只在用户屏幕上 —— 回退是"钱走了别的账"(C3/D4)
                # 与"答案来自未验证模型"两件事同时发生, 值得能被 grep 到。
                log.warning("model_fell_back", model_id=body.model, model_used=model_used)
            yield sse("done", {"model_used": model_used,
                               "model_id": body.model,
                               "verified": model_verified,
                               "fell_back": fell,
                               "usage": usage, "web_status": web_status,
                               "web_searches_ok": web_ok})
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -p no:warnings
```

- [ ] **Step 5: 变异验证 (逐条隔离)**

| # | 变异 | 期望 |
|---|---|---|
| M1 | `fell_back` 里 `return None` (内部组那支) → `return False` | G7 (c) 红 |
| M2 | 匹配式 → `return reported_model not in configured` (裸子串) | G8 红 |
| M3 | `"fell_back": fell` → `"fell_back": False` | G7 端到端 + G6/G7 合流红 |
| M4 | `configured.endswith("/" + reported_model)` → `configured.endswith(reported_model)` | G8 第二条 (`anthropic.claude-opus-5`) 红 |

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/server/llm_config.py sdtm-rag/server/router.py sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "fix(models): D5.2 — done 事件加 fell_back 三态 + 回退打 warning 日志"
```

---

### Task 4: D5.3 —— 前端徽章跟着回退变 (含 B1/B2 降级)

**Files:**
- Modify: `sdtm-rag/webchat/app.js` (`modelBadgeText` / `renderModelBadge` / `refreshModelBadgeLabels` / `messageEl` / `renderMessages`)
- Modify: `sdtm-rag/scripts/tests/fixtures/flag_attribution_probe.mjs` (`scenario()` 加参数 + `out` 加场景)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py`

**Interfaces:**
- Consumes: Task 3 产出的 `done.fell_back` / `done.model_used` 字段名
- Produces: 历史消息对象的两个新键 `modelUsed` / `fellBack` (Task 5 的 `persist` 要写它们); 探针 `out` 的新场景键

⚠ **本 task 一保存就会出现在用户正在跑的服务上** (`StaticFiles` 从工作树现读, Python 侧还没重启)。
所以 B1「新前端 + 老后端」这条降级必须在**同一个 commit 里就是绿的**, 不能留到 Task 5。

- [ ] **Step 1: 写失败的测试**

先扩探针 `scripts/tests/fixtures/flag_attribution_probe.mjs`:
把 `async function scenario({ modelId })` 改成

```javascript
async function scenario({ modelId, modelUsed, fellBack }) {
  ...
  if (modelId) { assistant.modelId = modelId; assistant.verified = false; }
  // 显式 undefined 时**整个键都不设** —— 那正是老历史存档的样子 (spec §5 B2)
  if (modelUsed !== undefined) assistant.modelUsed = modelUsed;
  if (fellBack !== undefined) assistant.fellBack = fellBack;
  ...
```

并在 `out` 里加两个场景 (⚠ 既有两条**一字不动**, 它们是 C-1 的既有闸):

```javascript
const out = {
  withModelId: await scenario({ modelId: "gpt-sol" }),
  legacyNoModelId: await scenario({ modelId: null }),
  fellBack: await scenario({ modelId: "gpt-sol", modelUsed: "deepseek-v4-pro", fellBack: true }),
  notFellBack: await scenario({ modelId: "gpt-sol", modelUsed: "global.openai.gpt-5.6-sol", fellBack: false }),
};
```

再在 `test_model_switching.py` 追加:

```python
def test_badge_says_which_model_actually_answered_when_it_fell_back(flag_probe):
    """闸 G9 正向 (用户裁定 R4): 回退时徽章必须写出**实际**答题的模型。

    不做的话: 用户选 Sol、DeepSeek 答题、徽章却说 Sol —— 与终审 C-1 (⚑ 归错模型)
    同族, 只是位置从归档换到了徽章。
    `verified` 按未知处理: 它描述的是用户**选的**那个模型验没验过, 拿它给一条
    **别人答的**消息背书就是撒谎。
    """
    badge = flag_probe["fellBack"]["badgeText"]
    assert "GPT-5.6 Sol" in badge, badge          # 选的是谁, 不能丢
    assert "deepseek-v4-pro" in badge, badge      # 实际是谁, 必须有
    assert "已回退" in badge, badge
    assert "验证状态未知" in badge, badge
    assert "⚠未验证" not in badge, f"verified 那一支必须被盖掉: {badge}"


def test_badge_is_byte_identical_when_it_did_not_fall_back(flag_probe):
    """闸 G9 反向: 没回退时徽章与今天**逐字相同**。

    ⚠ 这条不是形式主义: 把回退分支写成"只要有 modelUsed 就显示箭头"的实现会让它红,
    而那种实现会给**每一条**正常回答都挂上"已回退", 三天之内没人再看这个徽章。
    """
    assert flag_probe["notFellBack"]["badgeText"] == "模型: GPT-5.6 Sol ⚠未验证"


def test_badge_ignores_records_that_predate_the_field(flag_probe):
    """闸 G10 (spec §5 B1/B2): 老后端不发这两个字段、老存档里没有这两个键时,
    徽章必须与今天逐字相同。

    ⚠ B1 不是假想: `webchat/` 是从工作树挂载的, 这个前端一保存就上线, 而 Python
    改动要重启才生效 —— "新前端 + 老后端"是**必然发生的中间态**。
    """
    assert flag_probe["withModelId"]["badgeText"] == "模型: GPT-5.6 Sol ⚠未验证"


def test_badge_text_reads_the_fell_back_field():
    """闸 G13 静态第二重 (照 `test_flag_payload_reads_the_message_model_id` 双闸写法):
    node 缺席时行为闸会 skip, 这条不会。断的是**属性/形参读取形状**, 不是"源码里出现过这个词"。
    """
    src = APP_JS.read_text(encoding="utf-8")
    body = src.split("function modelBadgeText", 1)
    assert len(body) == 2, "modelBadgeText 没了 —— 徽章文案逻辑被搬走或删掉了"
    body = body[1].split("\n}", 1)[0]
    assert re.search(r"\bfellBack\b", body), "徽章文案没读 fellBack"
    assert re.search(r"\bmodelUsed\b", body), "徽章文案没读 modelUsed"
```

- [ ] **Step 2: 跑测试确认它失败**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
```
Expected: `..._when_it_fell_back` FAIL (徽章还是 `模型: GPT-5.6 Sol ⚠未验证`);
`..._reads_the_fell_back_field` FAIL。另两条 PASS (它们钉的是"不许变")。

- [ ] **Step 3: 改实现** (`webchat/app.js`)

```javascript
// verified 三态不可混同 (spec §6): true 正常; false 是拿到确证的"验过且不通过";
// null (default 组不在 selectable_models 里, 没有 verified 概念) 一律显"未知",
// 绝不能落进 false 那支 (会把"没这个概念"误报成"验过且不通过")。
//
// 回退 (fellBack === true, 2026-09-02 spec §4.4) 优先于以上三态: 答案是**另一个**模型
// 产的, 那么"用户选的那个验没验过"对这条消息不再成立 —— 拿 opus-5 的 verified: true
// 给一条 DeepSeek 答的消息背书, 就是终审 C-1 (⚑ 归错模型) 同族。琥珀色照挂: 回退是
// **已知的偏离**, 不是单纯的元数据缺失, 值得与"未验证模型"同级的视觉提示。
function modelBadgeText(modelId, verified, modelUsed, fellBack) {
  const label = modelLabelById[modelId] || modelId;
  if (fellBack === true && modelUsed) {
    return { text: `模型: ${label} → 实际 ${modelUsed}（已回退）· 验证状态未知`, unverified: true };
  }
  if (verified === true) return { text: `模型: ${label}`, unverified: false };
  if (verified === false) return { text: `模型: ${label} ⚠未验证`, unverified: true };
  return { text: `模型: ${label} · 验证状态未知`, unverified: false };
}
```

```javascript
function renderModelBadge(wrap, role, modelId, verified, modelUsed, fellBack) {
  if (role !== "assistant" || !modelId) return;
  const b = document.createElement("div");
  b.className = "msg-meta model-meta";
  // modelId/verified/modelUsed/fellBack 存进 dataset: /api/info 比首屏渲染慢一步是常态,
  // label 表填好后 refreshModelBadgeLabels() 要能原地补字, 不能靠重建 DOM 拿到这些值。
  b.dataset.modelId = modelId;
  b.dataset.verified = String(verified);      // "true" | "false" | "null"
  b.dataset.modelUsed = modelUsed == null ? "" : String(modelUsed);
  b.dataset.fellBack = String(fellBack);      // "true" | "false" | "null" | "undefined"(老存档)
  const { text, unverified } = modelBadgeText(modelId, verified, modelUsed, fellBack);
  b.textContent = text;
  if (unverified) b.classList.add("unverified");
  wrap.appendChild(b);
}
```

`refreshModelBadgeLabels` 的循环体:

```javascript
    const verified = b.dataset.verified === "true" ? true : b.dataset.verified === "false" ? false : null;
    // 显式三路比较, 不用 truthy —— dataset 里存的是字符串, "false" 是 truthy 的
    const fellBack = b.dataset.fellBack === "true" ? true : b.dataset.fellBack === "false" ? false : null;
    b.textContent = modelBadgeText(modelId, verified, b.dataset.modelUsed || null, fellBack).text;
```

`messageEl` 签名与 `renderModelBadge` 调用:

```javascript
function messageEl(role, content, sources, routedCorpus, webStatus, webSearchesOk, modelId, verified,
                   modelUsed, fellBack) {
  ...
  renderModelBadge(wrap, role, modelId, verified, modelUsed, fellBack);
```

`renderMessages` 的调用:

```javascript
    const el = messageEl(m.role, m.content, m.sources, m.routedCorpus, m.webStatus, m.webSearchesOk,
                          m.modelId, m.verified, m.modelUsed, m.fellBack);
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -p no:warnings
```

- [ ] **Step 5: 变异验证 (逐条隔离)**

⚠ **JS 不热重载** —— 变异 `app.js` 必须**先改文件再跑 node 探针**。上一轮踩过: 先加载页面
后改文件, 已运行的闭包用的还是改之前编译进内存的代码, "变异没生效"与"修复正确"表现一模一样。
本探针每次从磁盘重读 (`readFileSync`), 只要顺序是"改文件 → 跑 pytest"就没这个坑。

| # | 变异 | 期望 |
|---|---|---|
| M1 | 回退分支的 `fellBack === true` → `modelUsed` (只要有就显示箭头) | G9 反向红 (`notFellBack` 场景挂上"已回退") |
| M2 | 回退分支整段删掉 | G9 正向 + G13 红 |
| M3 | 回退分支文案里去掉 `· 验证状态未知` | G9 正向红 |
| M4 | `b.dataset.fellBack = String(fellBack)` → 不写这一项 | 若无红, 说明 `refreshModelBadgeLabels` 那条路径没被任何闸覆盖 —— **如实报告为欠账**, 不许悄悄放过 |

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/webchat/app.js sdtm-rag/scripts/tests/fixtures/flag_attribution_probe.mjs sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "fix(webchat): D5.3 — 回退时徽章写出实际答题模型, verified 按未知处理"
```

---

### Task 5: D5.4 —— 存档诚实 + ⚑ 归因跟着回退走

**Files:**
- Modify: `sdtm-rag/webchat/app.js` (`runGeneration` 的 `onDone`/`persist`, `flagModelName`)
- Modify: `sdtm-rag/scripts/tests/fixtures/flag_attribution_probe.mjs` (加"跑完整条流"的场景)
- Test: `sdtm-rag/scripts/tests/test_model_switching.py`

**Interfaces:**
- Consumes: Task 4 的 `messageEl(..., modelUsed, fellBack)` 签名与历史键名
- Produces: 无下游 task

- [ ] **Step 1: 写失败的测试**

探针加一个**真的走一遍 SSE** 的场景 (前面的场景都是预置历史, 测不到 `persist`):

```javascript
// 走完整条 send() → streamAsk() → onDone() → persist() 链, 然后从 localStorage 重建 DOM。
// 为什么必须这么测: 前面的场景都是**预置**历史再渲染, `persist` 有没有把新字段存下来
// 它们一个都看不见 —— 而"存档不诚实"正是本轮 R5 要防的事。
async function streamScenario(doneData) {
  const flagBodies = [];
  const sandbox = makeSandbox(flagBodies);
  const frames =
    `event: sources\ndata: {"sources":[],"routed_corpus":null}\n\n` +
    `event: token\ndata: {"text":"ok"}\n\n` +
    `event: done\ndata: ${JSON.stringify(doneData)}\n\n`;
  const baseFetch = sandbox.fetch;
  sandbox.fetch = async (url, opts) => {
    if (String(url).includes("/api/ask_stream")) {
      const bytes = new TextEncoder().encode(frames);
      let sent = false;
      return { ok: true, body: { getReader: () => ({
        read: async () => (sent ? { done: true } : ((sent = true), { value: bytes, done: false })),
      }) } };
    }
    return baseFetch(url, opts);
  };
  const ctx = createContext(sandbox);
  runInContext(readFileSync(APP_JS, "utf8"), ctx, { filename: APP_JS });
  await flush(); await flush();
  sandbox.__byId.get("model-select").value = "gpt-sol";
  await sandbox.send("AETERM?");

  const stored = JSON.parse(sandbox.localStorage.getItem("sdtm_chat_v1"));
  const last = stored.conversations[0].messages.at(-1);
  sandbox.renderMessages();                       // 模拟刷新: 只从存档重建
  const messages = sandbox.__byId.get("messages");
  const btn = findByClass(messages, "flag-btn");
  btn.onclick();
  const box = findByClass(messages, "flag-box");
  box.children.find((c) => c.tagName === "textarea").value = "答案是捏造的";
  await findByClass(box.parentNode, "flag-send").onclick();

  return {
    stored: last,
    badgeAfterReload: (findByClass(messages, "model-meta") || { textContent: null }).textContent,
    flagBody: flagBodies[0],
  };
}
```

`out` 加两条:

```javascript
  streamFellBack: await streamScenario({ model_id: "gpt-sol", verified: false,
                                         model_used: "deepseek-v4-pro", fell_back: true,
                                         web_status: "off", web_searches_ok: 0 }),
  streamNoFallback: await streamScenario({ model_id: "gpt-sol", verified: false,
                                           model_used: "global.openai.gpt-5.6-sol", fell_back: false,
                                           web_status: "off", web_searches_ok: 0 }),
```

⚠ `TextEncoder` 要加进 sandbox 的全局表 (与 `TextDecoder` 并列)。
⚠ `renderMessages` 是 `app.js` 顶层的**函数声明**, 在 vm context 里可以从 sandbox 上拿到;
`send` 同理 (都是 `function`/`async function` 声明, 不是 `const`)。若拿不到, 就用
`runInContext("renderMessages()", ctx)` 驱动, **不要**去改 app.js 的声明形态。

测试:

```python
def test_archive_records_the_model_that_actually_answered(flag_probe):
    """闸 G11 正向 (用户裁定 R5): `modelUsed` / `fellBack` 必须落进历史存档,
    刷新之后徽章仍然诚实。

    只做 UI 标注的话, 对话存下来之后这条信息就没了 —— 读的人得靠记得自己当时选了什么。
    与 2026-09-01 清掉的 B6 同形: **产物必须能自证**。
    """
    got = flag_probe["streamFellBack"]
    assert got["stored"]["modelUsed"] == "deepseek-v4-pro", got["stored"]
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


def test_flag_payload_reads_the_message_fell_back():
    """闸 G13 静态第二重: node 缺席时行为闸 skip, 这条不会。"""
    src = APP_JS.read_text(encoding="utf-8")
    body = src.split("function flagModelName", 1)[1].split("\n}", 1)[0]
    assert re.search(r"\.fellBack\b", body), "归因没有读 msgObj.fellBack"
    assert re.search(r"\.modelUsed\b", body), "归因没有读 msgObj.modelUsed"
```

- [ ] **Step 2: 跑测试确认它失败**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
```
Expected: 四条新的全 FAIL。⚠ 既有 `test_flag_is_attributed_to_the_model_that_actually_answered`
与 `test_flag_falls_back_to_the_topbar_for_legacy_records` **必须仍绿** —— 它们红了说明探针被改坏了。

- [ ] **Step 3: 改实现** (`webchat/app.js`)

`runGeneration` 里 (与 `gotModelId` / `gotVerified` 并列):

```javascript
  let gotModelUsed = null;
  let gotFellBack = null;
```

`persist`:

```javascript
    savedMsg = { role: "assistant", content, sources: gotSources || [], routedCorpus: gotRouted,
                 webStatus: gotWebStatus, webSearchesOk: gotWebSearchesOk,
                 modelId: gotModelId, verified: gotVerified,
                 // 产物自证 (spec §6 / 2026-09-02 R5): 回退这件事必须活过刷新, 否则
                 // 存档里一条 DeepSeek 答的消息与 Opus 5 答的长得一模一样。
                 modelUsed: gotModelUsed, fellBack: gotFellBack };
```

`onDone`:

```javascript
        gotModelId = (data || {}).model_id ?? null;
        gotVerified = (data || {}).verified ?? null;
        // ?? 而非 || : fell_back 的 false 是**确证没回退**, 不能被当成缺失塌成 null
        gotModelUsed = (data || {}).model_used ?? null;
        gotFellBack = (data || {}).fell_back ?? null;
        renderWebStatus(holder, gotWebStatus, gotWebSearchesOk);
        renderModelBadge(holder, "assistant", gotModelId, gotVerified, gotModelUsed, gotFellBack);
```

`flagModelName`:

```javascript
function flagModelName(msgObj) {
  const id = msgObj && msgObj.modelId;
  // 回退过 ⇒ 答案是 modelUsed 产的, **不是**用户选的那个。把 DeepSeek 的捏造记到
  // GPT-5.6 Sol 头上, 与终审 C-1 是同一个缺陷换了触发路径 (那次是切 topbar 文本,
  // 这次是读了 modelId 但答案不是它产的)。两个都写进去: backlog 的读者既要知道
  // 谁捏造的, 也要知道当时选的是谁 —— 否则"为什么会用到这个模型"这条线索断了。
  if (msgObj && msgObj.fellBack === true && msgObj.modelUsed) {
    return `${msgObj.modelUsed}（回退自 ${id ? (modelLabelById[id] || id) : "未知"}）`;
  }
  if (id) return modelLabelById[id] || id;   // 表没加载好就发原始 id, 归因照样正确
  return ($("topbar-title").textContent.split("·").pop() || "").trim() || null;
}
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -p no:warnings
```

- [ ] **Step 5: 变异验证 (逐条隔离)**

| # | 变异 | 期望 |
|---|---|---|
| M1 | `persist` 里去掉 `modelUsed` / `fellBack` 两项 | G11 两条红 |
| M2 | `gotFellBack = (data \|\| {}).fell_back ?? null` → `?? false` | G11 正向红 (被塌成 false) |
| M3 | `flagModelName` 的回退分支删掉 | G12 + G13 红 |
| M4 | `flagModelName` 回退分支的 `msgObj.fellBack === true` → `msgObj.fellBack` (truthy) | 应**不红** —— 如实报告"这条分支的三态语义没有专属闸", 记为 minor 欠账; ⛔ 不许为了让它红而临时加一条没意义的测试 |

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/webchat/app.js sdtm-rag/scripts/tests/fixtures/flag_attribution_probe.mjs sdtm-rag/scripts/tests/test_model_switching.py
git commit -m "fix(webchat): D5.4 — modelUsed/fellBack 进存档, ⚑ 归因跟着实际答题模型"
```

---

### Task 6: 收尾 —— 文档、欠账账目、retrospective

**Files:**
- Modify: `docs/superpowers/specs/2026-09-01-model-switching-design.md` (§9 D5 / D6 标记已还)
- Modify: `.work/meta/worklog/phase_07_rag_kg.md` (append 本轮 entry)
- Modify: `docs/PROGRESS.md` (状态总览)
- Modify: `CLAUDE.md` Key Paths (一行, ≤ 80 字符)
- Create: `.superpowers/sdd/2026-09-02-model-fallback-honesty/RETROSPECTIVE.md` (规则 C)

**Interfaces:**
- Consumes: Task 1-5 的实际 commit 号与实际测试数字
- Produces: 无

- [ ] **Step 1: 前一轮 spec 的欠账表改账**

`docs/superpowers/specs/2026-09-01-model-switching-design.md` §9 表里, D5 与 D6 两行的
「用户裁定」列改写为 **已还** + 指向本轮 spec 与 commit; ⛔ 不许删行 —— 欠账表是账本,
删掉就看不出它曾经欠过、以及欠了多久。同时把 D5 那行末尾那句
「⛔ **在 U2 落地前, `opus-5` 失败时前端直接收到 `event: error`, 不再自动回退。**」
改成指向本轮的实际行为 (回退到 `default-fallback` 并在徽章/存档/⚑ 标注)。

- [ ] **Step 2: 按 CLAUDE.md "Session Wrap-up" checklist 更新三套索引**

- `.work/meta/worklog/phase_07_rag_kg.md`: append `## 2026-09-02 D6+D5 还债` 条目,
  写实际数字与 commit 号 (本项目硬规矩: **报告任何测量数字必须带 commit 号**)
- `docs/PROGRESS.md`: 更新 Phase 7 一行状态
- `CLAUDE.md` Key Paths: 加一行指向本轮 spec, ≤ 80 字符; 顺手扫一遍有没有过期的 round/version 状态该剪

- [ ] **Step 3: 写 RETROSPECTIVE.md (规则 C, 三段起)**

至少三段: 保留下来的做法 / 必须补上的缺口 / 关键决策复盘。
必须点名回答的两个问题:
1. 本轮有没有出现"闸看起来在测、其实没测"的新形状? 有就写进 `.work/meta/retrospective.md` 规则 5/6 的表。
2. spec §7 的 L1 (真实回退时 chunk 里写什么串, 本轮无实测) 打算怎么收 —— 谁在什么时候能证伪。

- [ ] **Step 4: 提交**

```bash
git add -A
git commit -m "docs(models): D6+D5 收尾 — 欠账改账 + worklog + PROGRESS + retrospective"
```

---

## Self-Review

**1. Spec coverage**

| spec 条目 | 落在哪 |
|---|---|
| R1 (D6 先) | Task 1 在 Task 2/3 之前, Global Constraints 里写成硬约束 |
| R2 (四组加 fallback) | Task 2 |
| R3 (`fell_back` 判定, 内部组 null) | Task 3 |
| R4 (徽章跟着变, verified 按未知) | Task 4 |
| R5 (存档诚实) | Task 5 |
| §4.1 (`or "default"` 改 null) | Task 1 Step 3 |
| §4.4 ⚑ 归因 | Task 5 |
| §5 B1/B2 降级 | Task 4 闸 G10 |
| §6 G1-G13 | G1-G3→T1, G4-G6→T2, G6-G8→T3, G9/G10/G13→T4, G11-G13→T5 |
| §7 L1-L4 | Task 6 Step 3 第 2 问 (L1 的收法); L2/L3/L4 已写在 spec, 不需要代码 |
| §8 收尾文档 | Task 6 |

**2. Placeholder scan**: 无 TBD / "类似 Task N" / "写测试覆盖以上"。每个代码步骤都给了可粘贴的代码。

**3. Type consistency**: `fell_back(s, model_group, reported_model) -> bool | None` 在 Task 3 定义,
Task 3 的 `router.py` 与测试用同一签名; 前端字段名 `fell_back`(线上) / `fellBack`(JS) 在
Task 3/4/5 一致; `modelUsed` / `model_used` 同理; `_stream_client(router=None)` 在 Task 1 定义,
Task 3 复用; `_real_router_stream` 在 Task 2 定义, Task 3 复用。
