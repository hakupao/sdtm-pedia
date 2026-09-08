"""LiteLLM Router configuration (PLAN §4.2, R-8).

Model groups:
- "default": Sonnet primary -> DeepSeek non-thinking fallback
- "hard": Opus (complex semantic review / dataset validation)
- "light": Haiku (intent classification / routing)
"""
from __future__ import annotations

import litellm
from litellm import Router

from server.config import Settings, SelectableModel


INTERNAL_GROUPS = ("default", "default-fallback", "hard", "light")

# 内部组名 → Settings 上存它模型串的字段名。写成显式表而不是 f"{group}_model" 拼字符串:
# 拼名字在字段改名时不会报错, 只会静默少检一个模型 —— 正是闸 6 已经栽过一次的形状
# (它只扫 selectable_models, 而那四条硬编码全是 bedrock/, 于是默认配置下结构上不可能报警)。
# 表里缺项则 KeyError 当场炸在启动路径上, 比静默漏检好。
# 与 INTERNAL_GROUPS 的一一对应由 test_model_switching 钉住, 新增内部组必须同步这里。
_INTERNAL_GROUP_MODEL_FIELDS = {
    "default": "default_model",
    "default-fallback": "fallback_model",
    "hard": "hard_model",
    "light": "light_model",
}

# C3 检查豁免: fallback 默认就是 DeepSeek 个人流量, 用户已明确裁定接受 (spec §9 D4)。
# 把它纳入会产生恒定假阳性, 而一条长期喊狼来了的告警等于没有告警。
_C3_EXEMPT_GROUPS = ("default-fallback",)


def _validated_selectable_models(s: Settings) -> list[SelectableModel]:
    """`s.selectable_models`, 但先 fail-loud 挡住与 INTERNAL_GROUPS 撞名的 id。

    撞名不是假设性风险: litellm `Router` 允许同一 `model_name` 出现多次并把它们
    当同一组的多个 deployment 做 load-balance (实测 `get_model_ids("hard")` 会
    返回两个)。一旦撞名, 判库(light)/检索改写(hard/default) 就会被用户选的答题
    模型悄悄混进去, 且不会有任何测试变红 —— 静默打破 spec C1。selectable_models
    还能被 `SDTM_RAG_SELECTABLE_MODELS` 在运行时用 JSON 覆盖, 所以只在测试里挡
    默认配置不够, 必须在这个两处 (`create_router` / `known_model_groups`) 共用
    的读取点上就地拒绝。
    """
    collisions = {m.id for m in s.selectable_models} & set(INTERNAL_GROUPS)
    if collisions:
        raise ValueError(
            f"selectable_models 里的 id {sorted(collisions)} 与内部组 "
            f"{INTERNAL_GROUPS} 撞名 —— 会被 litellm Router 当同一组的额外 "
            "deployment 合并 load-balance, 静默打破 C1 (判库/检索改写不受用户 "
            "选择影响)。请换一个不冲突的 id。"
        )
    return s.selectable_models


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


def create_router(s: Settings) -> Router:
    """⚠ `max_tokens` 挂在**每个 deployment 的 `litellm_params`** 上, ⛔ 不是 per-call kwarg。

    两条理由, 第二条是决定性的:

    1. **回退目标要带自己的天花板**。答题组回退到 `default-fallback` (DeepSeek) 时,
       per-call 的 `max_tokens` 会被原样带过去 —— 于是 DeepSeek 被扣上一个按 Claude
       量的数。deployment 级则各组各自带各自的值, 回退后自动换成 DeepSeek 那个。
       (`_fallback_map` 那条"兜底落在个人流量"的代价已经够明了, 不该再叠一个隐性错配。)
    2. **不写 = 静默截断**。`bedrock/converse/...` 路径下 litellm 只在"开了 thinking 又
       没给 max_tokens"那一支才补 `maxTokens`; 其余情况该字段整个缺席, Bedrock 落到一个
       远低于模型上限的服务端默认值。2026-09-08 一条 ~3.5k 汉字的答案在 ≈4k output token
       处半句话被切断, 界面上没有任何提示 —— 那次截断本身就是证据。

    值的出处与"哪些是未经一手文档确认的"写在 `server/config.py` 的字段注释里, 不在这里
    抄第二份 (两份数字会各自漂移)。

    ⚠ 上面那条 ⛔ 说的是 **`server/` 里的请求路径**, 不是"全仓库禁止 per-call max_tokens"。
    已知的**有意例外**: `eval/run_eval.py` 显式传 `max_tokens=8192` (`MAX_TOKENS`,
    run_eval.py:45-50) —— V-2 要求跨模型比较必须同一个上限, 各 provider 的隐式默认值不同
    会让截断率不同, 进而让话痨模型在 (a) 层显得更干净。⛔ 别照着这段注释去"修" eval:
    把它改成吃 deployment 天花板会砸掉历史 run 的可比性。
    """
    model_list = [
        {
            "model_name": "default",
            "litellm_params": {"model": s.default_model,
                               "max_tokens": s.default_max_output_tokens},
        },
        {
            "model_name": "default-fallback",
            "litellm_params": {"model": s.fallback_model,
                               "max_tokens": s.fallback_max_output_tokens},
        },
        {
            "model_name": "hard",
            "litellm_params": {"model": s.hard_model,
                               "max_tokens": s.hard_max_output_tokens},
        },
        {
            "model_name": "light",
            "litellm_params": {"model": s.light_model,
                               "max_tokens": s.light_max_output_tokens},
        },
    ]
    # 用户可选模型: 每个 SelectableModel 派生一个同名组 (spec §3.3)。与上面四个内部组
    # 并存 —— default/hard/light 是内部用途 (判库/改写), 不受用户选择影响 (C1)。
    model_list += [
        {"model_name": m.id,
         "litellm_params": {"model": m.model, "max_tokens": m.max_output_tokens}}
        for m in _validated_selectable_models(s)
    ]
    return Router(
        model_list=model_list,
        fallbacks=_fallback_map(s),
        num_retries=1,
        timeout=120,
    )


def known_model_groups(s: Settings) -> set[str]:
    """Router 会有的全部组名 —— Task 5 白名单校验读的"意图"侧。

    `create_router` 与 `/api/ask_stream` 的白名单校验**共用**本函数, 故"能选的"与
    "能调的"不存在两份定义。校验端不读 `llm_router.model_list` 是有意的: 仓库里 4 个
    测试文件约 15 处假 Router 都没有该属性, 而用 getattr 兜底会造出"没有 model_list
    就不校验"的静默旁路。

    注意本函数的边界: 它不防"派生逻辑本身漂移"(例如 `create_router` 和这里同时手滑
    把 `m.id` 写成 `m.label`) —— 那种漂移会让"意图"与"事实"错得一致, 靠等式闸测不
    出来, 真正防住它的是直接锚定字面量的
    `test_router_derives_a_group_per_selectable_model` /
    `test_router_group_maps_to_the_configured_model_string`。本函数只保证"校验端
    读到的意图"与"Router 实际构造出的事实"这两份独立计算不会各走各的, 那条等式由
    `test_known_groups_equals_what_router_actually_has` 钉住。
    """
    return set(INTERNAL_GROUPS) | {m.id for m in _validated_selectable_models(s)}


def non_bedrock_model_groups(s: Settings) -> list[str]:
    """C3 闸 (spec §8 闸 6): 报出模型串**不走公司 Bedrock** 的全部 Router 组名。

    检查集合 = 内部组 (default/hard/light, 经 `_INTERNAL_GROUP_MODEL_FIELDS` 取字段)
    ∪ selectable_models, **不含** default-fallback (见 `_C3_EXEMPT_GROUPS`)。

    ⚠ 内部三组是这条闸的**主要**目标, 不是附带: spec §8 闸 6 的脚注点名的正是
    「`server/config.py` 里三个 Claude 模型的硬编码默认值是 `anthropic/` 直连,
    只有 `.env` 把它们改写成 Bedrock, 且无任何启动期校验」。selectable_models 那
    四条硬编码本来就全是 `bedrock/`, 只扫它们的话默认配置下返回值恒为 `[]` ——
    结构上不可能报警, 而闸要防的失败 (.env 缺一段、或两段并列时顺序一换) 全在
    内部三组上。`default` 组还是 `/api/ask`、eval 脚本、以及 Chat UI 在 /api/info
    加载失败时的降级落点。

    C3 与 C1 正交, 纳入 light/hard **不**触碰 C1: 本函数只读模型串判前缀、结果进
    ready 日志, 不往 model_list 加组、不进 known_model_groups、不进 /api/info、
    不碰答题请求的 `kw["model"]`。C1 管"谁能被用户切", C3 管"钱走谁的账"。

    返回组名列表; 空列表 = 全部合规。告警不阻止启动 (spec §8 闸 6)。
    """
    off = [
        g for g in INTERNAL_GROUPS
        if g not in _C3_EXEMPT_GROUPS
        and not getattr(s, _INTERNAL_GROUP_MODEL_FIELDS[g]).startswith("bedrock/")
    ]
    off += [m.id for m in _validated_selectable_models(s)
            if not m.model.startswith("bedrock/")]
    return off


def register_selectable_model_capabilities(s: Settings) -> None:
    """给可选模型补 LiteLLM 能力元数据。

    为什么需要: LiteLLM 的 bedrock provider allowlist 只认
    anthropic|mistral|cohere|meta.llama3-*|amazon.nova, 其余走 supports_function_calling()
    兜底, 而 registry 里没有 openai.gpt-5.6-* ⇒ 拒收 tools, 联网通道对 GPT 不可用。
    裸 boto3 Converse 已实测工具调用本身是通的 ⇒ 客户端元数据缺口, 非服务端限制。

    ⚠ 注册 key 必须是**去掉 bedrock/ 前缀**的形式 (litellm 内部就用这个查表)。
    用带前缀的 key 注册会**静默无效** —— 不报错, 直到有人开联网才炸。

    经 `_validated_selectable_models` 读取 (与 `create_router` / `known_model_groups`
    同一道 fail-loud 撞名闸), 不直接读 `s.selectable_models`。

    非 Bedrock 的模型跳过注册 (这里的元数据写死 `bedrock_converse` provider, 套到别的
    provider 上是错的)。它们的合规问题由 `non_bedrock_model_groups` 管 —— C3 告警是
    一个函数一个口径, 不在这里分一半出去。
    """
    info = {"litellm_provider": "bedrock_converse", "mode": "chat",
            "supports_function_calling": True}
    for m in _validated_selectable_models(s):
        if not m.model.startswith("bedrock/"):
            continue
        litellm.register_model({m.model.removeprefix("bedrock/"): dict(info)})


def verify_selectable_model_capabilities(s: Settings) -> list[str]:
    """spec §4.2 启动期自检: `register_model()` 跑过不等于生效 (实测带前缀的 key
    注册就是这样静默无效的) ——理由原文: 「注册失败的表现是『一切正常, 直到有人开
    联网』」。这里回查 litellm 是否真的认了每个 Bedrock 模型的 tool-calling 能力,
    而不是假定调用 `register_model()` 没抛异常就算数。

    逐模型独立回查 (而非"任意一个通过就算过"): Claude 系在 litellm bedrock
    allowlist 里原生认 `anthropic` 前缀, 不注册也是 True —— 若把检查做成"存在
    一个 True 即通过", 只要 Claude 天然为真, GPT 系注册悄悄失效也测不出来, 自
    检就形同虚设。故每个模型各自核对自己的 `supports_function_calling`, Claude
    天然为 True 不会被误报, 也不会因为它天然为真就让 GPT 那份检查跟着恒真。

    非 Bedrock 的模型不在本自检范围内 —— 那是 C3 (`register_selectable_model_
    capabilities` 的返回值) 管的另一个问题, 两者语义不混。

    返回注册后仍未生效 (`supports_function_calling` 为 False) 的模型 id;
    空列表 = 全部生效。
    """
    failed: list[str] = []
    for m in _validated_selectable_models(s):
        if not m.model.startswith("bedrock/"):
            continue
        key = m.model.removeprefix("bedrock/")
        if not litellm.supports_function_calling(model=key, custom_llm_provider="bedrock_converse"):
            failed.append(m.id)
    return failed


def _same_model(a: str, b: str) -> bool:
    """两个模型串指的是不是**同一个模型**。

    ⚠ 这是本仓库对"同一个模型"的**唯一**定义 —— `fell_back` 的比对与 `merge_reported_model`
    的去重都走它。⛔ 不许在收集端另写一套判据: 两份真相会各自漂移, 而"去重认为相同、
    回退判定认为不同"这种漏正好是无声的 (与 `known_model_groups` 同一条理由)。

    判据是"一方是另一方带 `/` 边界的后缀"。⛔ **必须带 `/`**: 裸子串会让 `claude-opus-5`
    这类**不完整**标识也算命中 (retrospective 规则 6 成因 A) —— 它是配置串的真子串,
    但不是一个完整的模型标识。
    ⛔ **不许用"取最后一段"** (`rsplit("/")[-1]`): 那会把 `openai/gpt-4` 与 `azure/gpt-4`
    这种**跨 provider 同名**静默合并成一个, 于是真回退被判成没回退。

    ⚠ **本关系不满足传递性**: `openai/gpt-4` ≡ `gpt-4` ≡ `azure/gpt-4`, 但
    `openai/gpt-4` ≢ `azure/gpt-4`。⇒ 任何"沿着已存条目往下缩"的合并策略都会经由中间的
    裸形把两个 provider 串起来。`merge_reported_model` 因此**只往更长(更限定)的方向**
    更新已存条目 —— 见那里的证明。
    """
    return a == b or a.endswith("/" + b) or b.endswith("/" + a)


def merge_reported_model(models_used: list[str], reported: str) -> None:
    """把一个 chunk 报出的模型串并进有序列表 —— 同一模型只留一项, 已存条目**只朝更限定
    (更长) 的方向增长**, ⛔ 绝不缩短。

    ⚠ 为什么需要这个 (2026-09-02 终审 I-2, 本轮实测): litellm 对**同一次**回答会报出
    **两种拼法** —— 内容 chunk 是 `converse/global.anthropic.claude-opus-5`, 收尾/usage
    chunk 是 `bedrock/converse/global.anthropic.claude-opus-5` (源码: `chunk_creator` 用
    `model_response.model = self.model`, 而"用 chunk 自带 model 覆盖"那支只对 Azure 生效)。
    不合并的话, 徽章会把 2 个模型写成 4 个串、上百字符, 而且"实际答题的是谁"这一栏里还混着
    **用户自己选的那个** —— 直接把 R4 想要的"一眼看出实际是谁答的"给毁了。

    留**最长(最限定)形**, 位置不动 (列表顺序 = **首次出现**顺序, 它表达的是"谁先答的")。

    ⚠ **为什么必须是"最长"而不是"最短"或"首见"** (2026-09-02 终审第 2 轮 N-2, 三策略实测):
    `_same_model` **不传递** (`openai/gpt-4` ≡ `gpt-4` ≡ `azure/gpt-4`, 但两端 ≢)。
    已存条目一旦被**缩短**, 它就成了通往别的 provider 的跳板:

    | 策略 | `openai/gpt-4, gpt-4, azure/gpt-4` | `gpt-4, openai/gpt-4, azure/gpt-4` | `gpt-4, azure/gpt-4, openai/gpt-4` |
    |---|---|---|---|
    | 最短形 | `['gpt-4']` ❌ | `['gpt-4']` ❌ | `['gpt-4']` ❌ |
    | 首见形 | 2 项 ✅ | `['gpt-4']` ❌ | `['gpt-4']` ❌ |
    | **最长形** | 2 项 ✅ | 2 项 ✅ | 2 项 ✅ |

    **最长形是无条件安全的**, 证明: 已存条目只会朝"更限定"增长, 即新值 `A'` 必有
    `A' = 前缀 + "/" + A`。若 `A'` 与另一已存条目 `B` 等价, 则 `B` 必是 `A'` 的 `/` 后缀
    或反之; 而 `B` 若以 `A` 结尾则 `A` 是 `B` 的 `/` 后缀 ⇒ `A ≡ B`, 与"`A`、`B` 是两个
    不同条目"矛盾。⇒ **增长永远不会把原本互不等价的两项并到一起。**

    代价: 展示的是较长那个形 (`bedrock/converse/…` 而非 `converse/…`, 多 7 个字符),
    换来的是**与到达顺序无关的确定性输出** + 上面那条 ⛔ 承诺真的无条件成立。
    """
    for i, seen in enumerate(models_used):
        if _same_model(seen, reported):
            if len(reported) > len(seen):
                models_used[i] = reported     # 只朝"更限定"增长, ⛔ 绝不缩短
            return
    models_used.append(reported)


def fell_back(s: Settings, model_group: str, reported_models) -> bool | None:
    """答这道题的, 是不是**自始至终**都是用户选的那个模型? 不知道就返 `None` —— ⛔ 不返 `False`。

    `None` 与 `False` 语义不同, 混同即撒谎: `False` 是"确证没回退", `None` 是
    "这里没有可比对的东西"。内部组 (default/hard/light/default-fallback) 不在
    `selectable_models` 里, 没有"用户选的模型串"这个概念 ⇒ `None`。
    同一个 done 事件里 `verified` 的三态是同一条原则 (2026-09-01 spec §6)。

    **入参是列表**(本次问答逐 chunk 收到的、有序去重的模型串), 不是单值。
    ⚠ 为什么不能只看最后一个: 联网多轮 (`web_max_rounds = 5`) 里每一轮是独立的
    `acompletion`, 各自可能回退; 第 1 轮回退、末轮落回主模型时, 只看最后一个会报
    `False` —— **回退了却不说**。流中途回退 (litellm `MidStreamFallbackError`) 是
    同一形状的第二条路径。故判据是"**任一个**不符即 True", 不是"最后一个不符"。

    `reported_models` 的元素来自流式 chunk 的 `.model`, **拼法与配置串不一定逐字相同**,
    故比对走 `_same_model` (带 `/` 边界的后缀关系), 而不是 `==`。三个已知形态:

    - **bedrock 侧, 本轮实测** (真 `create_router` + litellm `mock_response`, 零外部调用):
      同一次回答里会出现**两种**拼法 —— `converse/global.anthropic.claude-opus-5` 与
      `bedrock/converse/global.anthropic.claude-opus-5`。`get_llm_provider` **保留** `converse/`,
      只剥掉最前面的 `bedrock/`。
    - **deepseek 侧, 实测但只有非流式那一次**: `DEPLOY_PLAN.md` 记的 `/api/ask` 回退到
      `deepseek/deepseek-v4-pro` 时 `response.model = deepseek-v4-pro` (provider 前缀被剥掉)。
    - ⚠ **真实 bedrock 回退时流式 chunk 里写什么, 仍未实测** (spec §7 L1)。上面第一条用的是
      litellm 的 mock 流, 证的是"litellm 的拼法逻辑", 不是"真实 provider 返回什么"。
      若真串与配置串对不上, 表现是**每条答案都误报"已回退"** —— 响的失败不是静默的,
      上线第一条真实回答即可证伪。

    ⚠ 上面这段是 2026-09-02 终审修正过的: 初稿把 deepseek 那次实测的"去掉 provider 前缀"
    **外推**到 bedrock 串并标成"实测", 而实测结果是 `converse/` 被保留。
    这正是 spec §3 P6 那条教训 (把自己实验的边界当成被测系统的边界) 在下一层重演。
    """
    if not reported_models:
        return None
    configured = next((m.model for m in _validated_selectable_models(s)
                       if m.id == model_group), None)
    if configured is None:
        return None
    return not all(_same_model(configured, r) for r in reported_models)
