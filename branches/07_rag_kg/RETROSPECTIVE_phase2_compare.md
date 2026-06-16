# RETROSPECTIVE — 阶段 2 多模型对比 + 裁判 + 四方 eval (2026-06-16)

> DEPLOY_PLAN §3 阶段 2 (★核心) · Tier 2 · 规则 C 三段复盘
> 产物: `server/compare.py` `server/cost.py` + `router.py`/`config.py`/`ui` 改动; 证据 `evidence/checkpoints/phase2_{compare_judge,model_comparison}.md`; eval `eval/cmp_{deepseek,sonnet,gpt4o,gpt54mini}_v3.json`

## 1. 保留下来的做法 (有效, 下次继续)

- **设计稿先落地到真实代码再动手**: 开工前精读 `rag.py`/`router.py`/`run_eval.py`, 把 DEPLOY_PLAN 里的函数名核到实际签名 (retrieve/format_context/build_messages), 发现"compare 应绕过命名 Router 直接 acompletion(任意串)"才满足 FR7 — 避免照设计稿盲写。
- **验证抓真 bug, 不只结构检查 (规则 A)**: 临时实例真端到端调 `/api/ask_compare` 抓到 ① `cost.py` 用错 litellm API (`completion_cost` 不收 token kwargs → gpt-4o 静默 None) → 改 `cost_per_token`; ② 裁判偶发 None 定位到 provider 空返回 (非 bug) → 加 `judge_skipped` 观测日志。结构 py_compile 全过也挡不住这俩。
- **审阅隔离 (规则 D)**: 两个不同 subagent_type (code-reviewer 并发/正确性 + security-reviewer 匿名/注入) 独立 context 审, 均 SHIP; 8 项加固 (去重/注入加固/best 索引/cost 锚定/host 收环回/_get_info 不缓存失败/观测日志) 当场落。
- **模型决策必须有 eval 数据 + 语义抽检**: 140 题全量配对 (同 top_k/temp=0/检索杠杆全 ON/同判官), 不只看 overall 数字 — 抽检 q02 发现 DeepSeek/mini "枚举弱"是真实能力差非判官噪声。
- **长任务用文件落地信号守望**: nohup detached 进程不被 harness 跟踪 → 轮询 `--output` JSON 是否落地当完成信号, 比盯进程稳。

## 2. 必须补上的缺口 (本期欠的 / 下次别再犯)

- **守望循环上限设太短两次**: 60 min 上限在被速率限制的 Sonnet/gpt-4o 跑超时, 守望先退导致多查几轮。教训: 守望上限要按"最慢 provider × 限速 backoff"留余量 (rate-limited 模型可慢 5-8x)。
- **eval 默认与生产不一致是隐坑**: `run_eval` 的 `--structured-lookup/--hybrid/--guardrail` 默认 OFF, 若不显式带上就是在退化检索上比模型 — 差点跑出无效对比。下次跑生产对标 eval 先核对默认值。
- **延后项要显式记成 gate, 不能默默跳过**: 错误串透传 UI sanitize (SEC MED) / 限流 / asyncio 外层超时上限 / pip-audit — 均 localhost 单用户可接受, 已写进 DEPLOY_PLAN §3 阶段 3 gate + 证据 §4, 阶段 3 共享前必做。
- **Compare 多轮追问未做**: 用户本地试时提出"想边追问边对比", 当期决定暂用 Single 追问 (Single 已多轮)。Compare 改对话式 (每栏独立线程, 后端 history 字段已预留) 是明确的下一候选。

## 3. 关键决策复盘

- **D1 主力模型维持 DeepSeek-v4-pro** (用户定): 四方质量 Sonnet 96.0 > DeepSeek 93.6 > GPT-4o 90.4 ≈ GPT-5.4-mini 90.2; DeepSeek **比两个 OpenAI 都准且最便宜** ($0.0075/题)。Sonnet +2.4pt 但 9.6x 成本。决定不切, Sonnet 留 hard 档/Compare 手动。规则 A 满足 (140q×4 eval + 抽检)。
- **D2 裁判默认 deepseek-chat 而非 §2.6 的 Opus**: 起草时 Anthropic credits 耗尽, Opus 裁判会每次失败 → 默认改可跑的 deepseek-chat, 注释保留"credits 回血后切 Opse"。一个能跑的默认 > 一个理论最优但报错的默认。
- **D3 compare 绕过命名 Router 直接 acompletion(任意串)**: 满足 FR7 每槽任意模型; Router 只认 default/hard/light 不够用。
- **D4 GPT-5.4-mini 经 /models 查实再跑**: 用户报"5.4 mini"我知识截止 (2026-01) 不认识 → 查 OpenAI /models 确认 `gpt-5.4-mini` (2026-03 发布) 真实存在 + 冒烟确认接受 temp=0, 才跑 — 不盲猜模型串浪费长任务。结论: mini 完胜 gpt-4o (同质量/1-3 成本/7x 速度), 但都不及 DeepSeek。
- **D5 错误串透传 UI 有意保留到阶段 3**: SEC 审标 MED, 但 localhost 单用户下上游错误文本 ("credit too low") 对操作者有用 (实测靠它诊断 Anthropic), 操作者即查看者非泄漏。阶段 3 绑 0.0.0.0 共享时再 sanitize。
