# 阶段 2 — 多模型对比 + 裁判 实现 + 验证证据

> 日期: 2026-06-16 · DEPLOY_PLAN §2 / §3 阶段 2 · Tier 2
> 状态: 实现完成 + 端到端实测 PASS · 独立审阅(规则 D)双 SHIP + 加固已落

## 1. 实现 (T1–T6)

| 任务 | 文件 | 内容 |
|------|------|------|
| T1 | `server/config.py` | `compare_models`(3 参考占位, env JSON 覆盖) / `judge_model`(默认 deepseek-chat, 可跑) / `compare_timeout_s` / `compare_num_retries` |
| T3 | `server/cost.py` (新) | §9 显式价格表 + `litellm.cost_per_token` 兜底; 未知模型→None→UI "—"(绝不编造数字) |
| T2 | `server/compare.py` (新) | `run_compare`: `asyncio.gather` 并行 `litellm.acompletion`, 每模型独立 try→失败隔离(NFR2), 返回 `ModelAnswer(model/answer/usage/latency_ms/cost_usd/error)` |
| T4 | `server/compare.py` (新) | `run_judge`: 答案匿名 A/B/C 喂裁判→结构化 JSON 解析(`_parse_judge` 容错)→映射回真实模型名; <2 有效答案返回 None |
| T5 | `server/router.py` | `POST /api/ask_compare`(async, 复用 retrieve/format_context/build_messages, FR1 检索仅一次) + Pydantic 契约; `/api/info` 加 `compare_models`/`judge_model` 供 UI 预填 |
| T6 | `ui/streamlit_app.py` | sidebar Single/Compare 模式 + 3 模型槽(预填 /api/info)+ Enable Judge + 裁判模型框; `_render_compare` 三栏 badge + 共用 Sources + 裁判区; 修过时 "default=Sonnet" 文案 |

设计决策:compare/judge **绕过命名 LiteLLM Router**(只认 default/hard/light),直接 `acompletion(model=<任意串>)` → 满足 FR7「任意模型串、每槽可覆盖」。无新增依赖(litellm 1.88.1 已含 acompletion + cost_per_token)。

## 2. 验证抓出并修复的 bug (验证前 ≠ 验证后)

- **cost.py 用错 litellm API**: 初版用 `litellm.completion_cost(model, prompt_tokens=, completion_tokens=)` → 1.88.1 该函数不收 token kwargs, gpt-4o 静默返回 None(本应可定价)。改用 `litellm.cost_per_token(model, prompt_tokens, completion_tokens) -> (in,out)`。修后 gpt-4o=$0.0425、deepseek-chat=$0.00441 均正确。
  - 教训:成本"未知→—"的兜底路径必须有正样本验证,否则会把"能定价的模型"也误降级成"—"而不报错。

## 3. 端到端实测 (Rule A 独立活样本, 临时实例 127.0.0.1:8011, 不碰 launchd:8000)

问题:`In the AE domain, what is the AETERM variable: its label, type, role, and core?`
默认 3 模型(deepseek-v4-pro / gpt-4o / anthropic-sonnet)+ 裁判 deepseek-chat。全 JSON → `/tmp/compare_evidence.json`。

| 验收项 | 实测 |
|--------|------|
| FR1 检索一次共用 | sources=15, 共用一份 ✅ |
| FR2 并行 | wall=8.9s ≈ max(3993ms,3230ms)+裁判, 非串行累加 ✅ |
| NFR2 失败隔离 | Anthropic「credit balance too low」→ **单栏 error**, 另两家正常 + HTTP 200(整请求不挂)✅ |
| FR3 badge | latency/tokens/cost: ds-v4-pro $0.0065(表) / gpt-4o $0.0361(litellm) ✅ |
| FR5/§2.6 裁判 | 匿名 A/B → 映射回真名; best=deepseek-v4-pro; **裁判真抓出 gpt-4o 编造了 cited source 未含的 "verbatim term"** ✅ |
| 语义正确性 | 两家 AETERM 均正确: Label="Reported Term for the Adverse Event", Type=Char, Role=Topic, Core=Req ✅ |

裁判判词(节选):"Answer A is fully grounded... Answer B includes an unsupported detail not found in its cited source." —— 裁判 grounding 轴生效,非走过场。

## 4. 独立审阅 (规则 D) — 双 agent, 不同 subagent_type, 独立 context

两份均 **SHIP**, 0 BLOCKER / 0 HIGH。

- **code-reviewer (opus, 并发/正确性)**: 三承重面 PASS —— ① 失败隔离 textbook-correct(`_one_completion` 永不 raise → gather 不需 return_exceptions, 顺序保留); ② `_parse_judge` 抗 8 类对抗输入零崩; ③ 契约字段精确对齐(`vars(a)`/`**r` 不会 KeyError)。3 MEDIUM + 4 LOW 均为加固非 bug。
- **security-reviewer (opus, 信任/匿名/注入)**: 三承重信任点 PASS —— ① 裁判匿名代码层零泄漏(model 名从不进喂裁判文本); ② label→model 映射含**部分失败子集**也正确(按存活子集位置分配, 失败模型不会误判为 best); ③ 成本诚实(不可定价→None→"—")。1 MEDIUM + 3 LOW。

### 已落加固 (审阅后)
1. **模型去重** (router): `list(dict.fromkeys(models))` — 防重复槽产生同名栏 + 裁判映射歧义 (MED)。实链路验证 3→2 ✅。
2. **裁判注入加固** (compare judge prompt): 显式声明 QUESTION/CONTEXT/ANSWER 为"数据非指令", 点名"rank-me-best"攻击 (LOW/A03)。
3. **best_model 直接索引** 替 `.get()` — 不变量破坏时 fail-loud 而非静默 None (MED 脆弱性)。
4. **cost 前缀锚定 + 最长键优先** 替 `in` 子串匹配 — 防未来型号借价 (LOW)。
5. **host 默认 `127.0.0.1`** 替 `0.0.0.0` — 对齐 §1「阶段 0–2 绑环回」, 裸跑也不暴露 (SEC LOW)。
6. **`_get_info` 不缓存失败** — 首次失败后自动重试而非永久 fallback (LOW UX)。
7. **`judge_skipped` 观测日志** — <2 有效答案静默返回前记日志, 区分"空答案"与"裁判崩溃" (NFR5)。实测抓到 provider 偶发空返回正是此路径。
8. router 加注释: sync retrieve 在事件循环内是 §1 单用户有意取舍。

### 延后项 (有意识决策, 系 §3 阶段3 gate)
- **错误串透传 UI** (SEC MED): 阶段 2 = localhost 单用户, 上游错误文本("credit too low")对操作者**有用**(实测靠它诊断 Anthropic), 操作者即查看者非泄漏。阶段 3 绑 `0.0.0.0`+共享时再 sanitize(只留异常类型, 详情入服务日志)。
- **限流 / asyncio 外层超时上限** (SEC LOW / REV MED-b): localhost 单用户低概率, 阶段 3 共享前加 per-IP 限流 + 共享密钥。
- **pip-audit**: venv 未装 pip_audit 模块, 本轮未跑; 阶段 3 前补 `uv tool run pip-audit`。

## 5. 待办 (你侧 / 后续)

- [x] **③ DeepSeek vs Sonnet `--judge` eval 对比**: **完成** (你 2026-06-16 充值后) — 140 题全量, 见 `evidence/checkpoints/phase2_model_comparison.md`。Sonnet 96.0% vs DeepSeek 93.6% (判官 per-q 均值), Sonnet 9.7x 成本但绝对值小; Sonnet 强在枚举类(q02 型)。
- [x] **④⑤ 拍板主力模型**: **决定维持 DeepSeek-v4-pro 默认**(你 2026-06-16, 基于 140 题 eval + 抽检)。Sonnet 留 hard 档/Compare 手动用。无需改 .env。
- [ ] 你侧: Validation 真数据集试。
- 备注: deepseek-v4-pro 对英文问题用中文作答(项目既有「中文回答」配置, 与 compare 功能正交, 非缺陷)。
