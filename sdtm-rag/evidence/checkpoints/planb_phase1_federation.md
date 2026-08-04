# Plan B Phase 0+1 — 双库联邦路由收口证据

> 状态: **DONE / 默认启用** (2026-08-04)。`SDTM_RAG_FEDERATION_ENABLED` 默认 `True`,
> 生产服务 `com.sdtmrag.api` 已带联邦重启并冒烟通过。
> 红线: 本文件**只含统计、题 id、结构描述** —— 无 study 题面、无 EDC 字段名/OID、无 form 标签。
> spec: `docs/superpowers/specs/2026-08-04-plan-b-federated-routing-design.md`
> plan: `docs/superpowers/plans/2026-08-04-plan-b-phase01-federated-core.md`

## 1. 范围

| 块 | 内容 | 落点 |
|---|---|---|
| Phase 0 | source 判据下沉到 section 粒度 | `eval/run_eval.py` `check_source_recall` |
| Phase 1 §1.1 | LLM 判库 + `FederatedEngine` 配额合并 | `server/federation.py` (新建) |
| Phase 1 §1.2 | API 接线: `corpus` 入参 + `routed_corpus` 出参 + study 引擎构建 | `server/router.py` / `server/main.py` |
| Phase 1 §1.3 | 前端: corpus 下拉 + 来源库徽章 + 判定行 | `webchat/{index.html,app.js,style.css}` |
| Phase 1 §1.4 | 路由准确率闸 (闸 1) | `eval/run_routing_eval.py` |
| Phase 1 §1.5 | `--federated` 全联邦检索评测通道 (闸 2/3) | `eval/run_eval.py` |
| rollout | 默认翻 True + 部署 + 本文件 | `server/config.py` |

**不在本 plan**: Phase 2 (study 结构化直查) / Phase 3 (eval chunk 粒度判据后续) /
Phase 4 (CDISC 变量索引挤占) —— 各自独立成 plan。

## 2. 三闸最终数字

### 闸 1 — 路由准确率 (三遍, `jp.anthropic.claude-haiku-4-5` @ temperature 0)

| 项 | 值 |
|---|---|
| gold | 181 题 (英文 cdisc 140 / 日文 cdisc 11 / 日文 both 5 / study 25) |
| run 1/2/3 exact | **178/181 = 98.3%** (三遍相同) |
| fatal (判错单库或缺失) | **0** (三遍) |
| fallback (降级双库) | **0** (543 次调用) |
| stability | **181/181 题三遍判定一致** |
| PASS 条件 | 每遍 exact ≥ 95% 且 fatal = 0 → 三遍全 PASS |

3 题非 exact 全部是安全侧 `both` (三遍相同): `q124` / `st_st01_v11_q17` / `st_st01_v11_q22`。
逐子集分布、历史轨迹、复跑方式见 `evidence/checkpoints/routing_gate.md`。

### 闸 2/3 — 检索无回归 (控制组 vs 联邦组配对, 全部 `--retrieval-only`)

| 组 | 题集 | lever | 控制组 | 联邦组 | Δ | 逐题 recall 差异 |
|---|---|---|---|---|---|---|
| CDISC-A | `eval/test_set_v3.yml` 140q | `--hybrid` | **81.07%** | **81.07%** | **0** | **0 题** |
| CDISC-B | 同上 | `--hybrid --structured-lookup` | **98.93%** | **98.93%** | **0** | **0 题** |
| study | golden v1.1 (25 计分 / 27 总) | `--hybrid` | **88.53%** | **88.53%** | **0** | **0 题** |

闸: CDISC ≥ 81.1% ✅ / study ≥ 88.5% ✅。**both 配额预案未触发** (无回归, 无需从
`ceil(k/2)` 提到 `k`; `test_federation.py` 未改)。

**基线记账口径 (易踩)**: **81.07% 对应 hybrid-only**, 98.93% 对应 hybrid + structured-lookup;
两者是同一题集的两套配置。引用 81.1% 时**必须同时写明 "hybrid-only"**。study 基线 88.53%。

### 判库分布 (联邦组实测计数)

| run | routing Counter |
|---|---|
| CDISC-A 联邦 (140q) | `{'cdisc': 140}` |
| CDISC-B 联邦 (140q) | `{'cdisc': 140}` |
| study 联邦 (27q, 含 2 道 out_of_scope) | `{'study': 25, 'both': 2}` |

CDISC 侧 140/140 判 cdisc, 逐题 top5 与控制组完全一致 → 联邦包装对主库是恒等变换。
study 侧被判 both 的 2 题是全部 3 组中**仅有的 top5 集合变化**题, recall 仍 1.0。

## 3. 生产冒烟 (默认翻 True 后, 2026-08-04)

服务: launchd `com.sdtmrag.api` (repo 内 `.venv/bin/uvicorn`, `0.0.0.0:8000`, 无鉴权 = 决策 D2),
`launchctl kickstart -k` 重启, 启动日志零 error。

| 检查 | 结果 |
|---|---|
| 启动日志 | `federation study_collection=study_st01` → `ready` → `Application startup complete`, 无 traceback |
| `GET /api/info` | 200; `"federation": true`; `index_fresh: true` ("index is in sync with knowledge_base"); `chunk_count: 4303` |
| `POST /api/ask` 英文 CDISC 题 (`corpus:auto`) | 200; `routed_corpus: cdisc`; 15 sources **全 cdisc**; 真实答案 1785 字符 |
| `POST /api/ask` 日文 study 题 (`corpus:auto`, id `st01_v11_q01`) | 200; `routed_corpus: study`; 15 sources **全 study**; 日文答案; expected_facts 子串命中 **3/3** |
| 前端 ①下拉 | `#corpus` 可见, 选项 `自動 / 標準 (CDISC) / 本研究 / 両方`, **默认 `自動`** |
| 前端 ②study 题 (id `st01_v11_q05`, 自動) | 15 个 `corpus-badge study` = **本研究** |
| 前端 ③标准题 (自動) | 15 个 `corpus-badge` = **標準** |
| 前端 ④判定行 | study 题显示 `判定: 本研究`; 标准题显示 `判定: 標準` |
| 浏览器 console | 仅 1 条既存 `favicon.ico 404`, 无 JS 错误 |

答题模型实测为 `jp.anthropic.claude-sonnet-4-6` (Bedrock), 见 §4。

## 4. LLM 供给切换 — Anthropic 直连 → AWS Bedrock

Anthropic 直连额度耗尽 (credit balance too low), 这是切换的**直接原因**。改为经 `.env` 走
AWS Bedrock (`AWS_BEARER_TOKEN_BEDROCK` + region; boto3 装进 `.venv`):

| 槽位 | 模型 |
|---|---|
| light (含路由判库) | `bedrock/converse/jp.anthropic.claude-haiku-4-5` |
| default (答题) | `bedrock/converse/jp.anthropic.claude-sonnet-4-6` |
| hard | `bedrock/converse/jp.anthropic.claude-opus-4-7` |

`config.py` 的 `load_dotenv` 让服务与 CLI 同源读取, 无需分别配置。
**闸 1 对通道不敏感的证据**: 基线 prompt 在 Anthropic 直连与 Bedrock 上给出**完全相同**的
156/165 —— 但**换模型 (或换 haiku 版本) 必须重跑闸 1**, 见 `routing_gate.md` §4.4。

## 5. 决策记录 (本轮 review 期间确定, 无对应代码改动)

| # | 决策 |
|---|---|
| D2 (用户, 2026-08-04) | **局域网免密开放, study 库同样免密** —— 局域网视为受信内网。`server/auth.py` 代码保留, 供未来重新启用 |
| D-ask_compare | `/api/ask_compare` 联邦后**仍是 CDISC 单库**, 响应里无 corpus 信号 —— 已知限制, 不在本 plan 修 |
| D-corpus-ignored | federation 关闭时 `corpus` 入参被**静默忽略** (不报错) —— 刻意的前向兼容 |
| D-both-k+1 | `both` 模式对奇数 k 返回 **k+1** 条 (`ceil(k/2)` × 2, k=15 → 16) —— 设计如此, 单测钉住 |
| D-baseline | 基线记账: CDISC **81.07% (hybrid-only)** / 加 S1 **98.93%** / study **88.53%** |

spec 决策表 D1-D7 (范围 / 安全边界 / 自动路由+前端覆盖 / 跨库 best-effort 不进验收 /
LLM 判库 / web search 透传 / study×搜索允许但警示) 见 spec 文档 §决策表, 本轮未改。

## 6. 已知限制

1. **闸 1 的 8 条限制整体引用** `evidence/checkpoints/routing_gate.md` §4 —— 其中最重的三条:
   调优集 == 闸集无 holdout; **反向盲区** (英文提问 study EDC 字段, 一题未覆盖);
   both 组与规则 3 线索词重合、无"含线索词但 gold≠both"的负例, 该方向不可证伪。
2. **`run_eval` 的联邦答题适配器把 `corpus` 硬写成 `"both"`** (`_FederatedAdapter.build_messages`),
   与生产的 `routed` 语义不同。**检索闸不受影响** (三闸全是 `--retrieval-only`), 但
   **做任何联邦答题 eval 之前必须先修这里** —— 否则答题侧 system prompt 与线上不一致。TODO。
3. **答题侧联邦路径无 eval 覆盖**: `format_context` / `build_messages` 只有单测 + 本文件 §3 的
   端到端冒烟, 没有成规模的联邦答题闸。
4. **跨库 (both) 回答质量不进验收** (spec D4, best-effort)。
5. **路由是系统里唯一的非确定性组件**; 其稳定性只由闸 1 的三遍一致性把守。
6. `_ROUTER_SYSTEM` prompt 是被闸 1 把守的资产: 改它必须重跑 `--runs 3` 三遍全 PASS。

## 7. commit 链与测试演进

`b08db80`(plan) → `HEAD`, 12 commits:

```
b08db80 docs(plan)      Plan B Phase 0+1 实施计划 (7 task, TDD + 三 eval 闸)
6f8e4a5 feat(eval)      source 判据下沉 section 粒度 (Phase 0)
d383452 feat(federation) LLM 判库 + FederatedEngine 配额合并
f8feb3a feat(api)       联邦路由接线 — corpus / routed_corpus / study 引擎 (默认关)
ef43301 feat(webchat)   corpus 下拉 + 来源库徽章 + 判定显示
404a624 fix(config)     study_kb_root 默认改指 st01/cards
ece3aa5 feat(eval)      路由三遍闸工具 (闸 1)
ce8ca77 fix(federation) 路由 prompt 迭代 — 163/165 三遍 PASS
e940f10 feat(eval)      --federated 通道; 闸 2/3 全 Δ0
eff32fd fix(federation) 补日语标准题堵语言盲区 — 174/176
9a70d44 feat(eval)      补 both 题 + 规则 3 让路 — 178/181
a144dc5 fix(eval)       审阅 fix round 1 — b03 措辞 + 两条不可证伪限制入档
+ 本 task: 默认翻 True + 本文件 + 收尾索引
```

测试数: **669 → 720** (+51, 0 failed / 0 skipped, junitxml 计数; 套件不打印 summary 行)。
默认翻 True 后全量重跑 **720 passed**, 无测试因默认值改变而需修改 (受影响的构造点此前
已显式传参隔离)。

## 8. 复跑 / 回滚

```bash
cd sdtm-rag
.venv/bin/python -m eval.run_routing_eval --runs 3          # 闸 1, 退出码 0 = 三遍全过
.venv/bin/python -m eval.run_eval --federated --hybrid ...  # 闸 2/3 联邦组
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api          # 重启服务
```

回滚到纯 CDISC 单库: 在 `.env` 设 `SDTM_RAG_FEDERATION_ENABLED=false` 并重启
(此时 `corpus` 入参被静默忽略, `routed_corpus` 恒为 `null`)。
