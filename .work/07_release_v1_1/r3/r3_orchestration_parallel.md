# SMOKE_V4 R3 — 并行方法论 (Chrome MCP 全自动 4 平台同步)

> 与 `r3_kickoff.md` (串行 per-platform, fallback) 并存. 本文档描述基于 dry-run (2026-05-19) 验证的**并行 per-question** 方法。
> **触发**: 用户 ack "R3 并行" + Chrome 已开 4 标签 + ChromeDev profile 通 9222 CDP
> **dry-run 校准证据**: `ai_platforms/{platform}/dev/dry_run_2026-05-19/feasibility.md` (4 份)

## 1. 方法对比

| | 串行 (r3_kickoff §每题 cowork 流程) | 并行 (本文档) |
|---|---|---|
| 流程 | 每题 4 平台串行: 切 P1→跑→收 → 切 P2→跑→收 → ... | 每题派发 4 平台 → 并行等 → 4 平台同时收 |
| 单题墙钟 | ~3 min (4 × ~45s) | **~70s** (12s 派 + 50s 等 + 5s 收) |
| 17 题总墙钟 | ~50 min | **~20 min** (~2.5× 提速) |
| MCP 串行点 | 64 次 select + 64 次 click + 64 snapshot | 17 × 8 = 136 次 select (派+收), 0 click 0 snapshot |
| 故障半径 | 任一题任一平台 fail → 阻塞下题 | 4 平台独立 fire-and-forget, 1 平台 fail 不影响其他 3 |
| 实测验证 | R1+R2 已用 (4 月 cowork paste) | dry-run 2026-05-19 通 (4 平台 "什么是 SDTM?" 一次过) |

## 2. 前置条件 (Phase A 之前必核)

- [ ] Chrome 9222 CDP 端口通: `curl -s localhost:9222/json/version` 返回 200
- [ ] 4 标签已开 + 已登录:
  - Gemini Gem: `gemini.google.com/u/1/gem/3b572e310813`
  - ChatGPT GPT: `chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc`
  - NotebookLM: `notebooklm.google.com/notebook/<id>`
  - Claude Project: `claude.ai/project/<id>`
- [ ] Grammarly disabled / removed (4 平台输入框 mutation 风险, dry-run 已验证清除生效)
- [ ] chrome-devtools-mcp 已挂 9222 (无需配 `--browser-url`, 自动检测)
- [ ] dry-run evidence 4 份在位 (作 selector / done-signal 权威参考)
- [ ] 题库 `ai_platforms/SMOKE_V4.md §2` 17 题 ready
- [ ] R3 结果目录初始化: `.work/07_release_v1_1/r3/{evidence,failures}/` (各平台子目录建好)

## 3. Phase 流程

### Phase A — 前置 sanity (~3 min, 主 session 串行)

1. `curl localhost:9222/json` 列 page, 确认 4 标签 page id (映射 1=Gemini, 3=ChatGPT, 4=NotebookLM, 5=Claude — 实际 page id 可能漂, 用 URL 匹配)
2. select_page 各 + take_snapshot 各 1 次, 确认:
   - 输入框 a11y label 与 dry-run 一致
   - 4 个 conversation 状态干净 (无 in-flight stream)
3. 写入 `r3/evidence/_preflight.md`

### Phase B — 17 题主循环 (~20 min)

题 N (1 ≤ N ≤ 17), 顺序按 SMOKE_V4 §2 (Q1-Q14 + AHP1-3):

1. **取题文** from `SMOKE_V4.md §2 Q<N>` (Read tool 抽段 + 主 session 整理出纯 prompt 文本)
2. **Reset 4 平台 conversation** (混合 MCP + JS, 顺序无关, 可串行):
   - **Gemini**: select_page → evaluate_script(`scripts/reset_gemini.js`) — 内部点 toolbar "New chat" + 切 Pro mode
   - **ChatGPT**: select_page → `mcp__chrome-devtools__navigate_page` 到 GPT URL (`chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc`)
   - **NotebookLM**: select_page → evaluate_script(`scripts/reset_notebooklm.js`) — 点 Chat options → "Delete chat history" → 处理 confirm dialog
   - **Claude**: select_page → `navigate_page` 到 project URL (`claude.ai/project/<id>`)
3. **派发 4 runner 脚本** (sequential through MCP, ~12s):
   - 每个 runner 文件用 `Read` 拿到内容, **替换 `__QUESTION_PLACEHOLDER__` 为题 N 文本** (Bash sed 或主 session 直接字符串拼接), 然后 evaluate_script 注入
   - 注入后立即返回 (fire-and-forget), 接下一平台
4. **等待**:
   - 简单方案: 主 session foreground `sleep 90`
   - 进阶方案: 每 30s 探一次 4 平台 `window.__SMOKE_<P>_RESULT.status`, 全 `complete` 提前结束 (max 150s timeout)
5. **收集 4 平台 result** (sequential, ~5s):
   - 切 P_i + evaluate_script `() => window.__SMOKE_<P>_RESULT`
   - 抓 4 个 result object
6. **写 4 份 evidence**:
   - `r3/evidence/<platform>/q<NN>.md`
   - 内容: 题文 + 平台 + 时序 + done signal trace + 原始 AI 回答 + inline self-score (PASS/PARTIAL/FAIL + 判据 mapping 引 SMOKE_V4 §2 Q<N> 判据段)
7. **更新 matrix**:
   - `r3/r3_matrix.md` 该 cell 填 verdict
8. **若任一平台 abort/error**:
   - 写 `r3/failures/q<NN>_<platform>_attempt_<X>.md` (Rule B), 含输入题文 + window state full dump + 推测原因 + 下次 attempt 修复点
   - **不阻塞**: 题 N+1 继续, 失败题 R3 末尾统一重试

### Phase C — Reviewer subagent 审 (~5-10 min, 后台并行)

详见 §5 + `reviewer_prompt_template.md`. **可在 Phase B 跑题中后台并行启动** (题已答完 5+ 道时, 派 reviewer 看前面的, 流水线): 减总墙钟。

### Phase D — 汇总 + retro (~10 min)

1. 4 平台 summary score 算出, 填 `r3_matrix.md` 底部"汇总"表
2. 与 R1 baseline (kickoff §对比) delta 比较, 标 regression / improvement
3. 写 `r3/R3_RETROSPECTIVE.md` 三段式 (保留 / 缺口 / 决策) + 14-15th reviewer carry-over
4. 更新 `ai_platforms/SYNC_BOARD.md` 加 R3 row
5. 更新 `docs/PROGRESS.md` Phase 6.5 状态

## 4. Selector / Done-signal 引用 (dry-run 锁定, 2026-05-19)

| 平台 | 输入框 | Send 按钮 | Done 信号 | 响应抽取 |
|---|---|---|---|---|
| Gemini | `[contenteditable="true"][aria-label*="prompt for Gemini"]` | `button[aria-label="Send message"]` | `button[aria-label="Send message"]:not([disabled])` 重新出现 | 最后一个 `model-response` 的 `textContent` |
| ChatGPT | `#prompt-textarea` | `[data-testid="send-button"]` | `[data-testid="stop-button"]` 消失 | 最后一个 `[data-message-author-role="assistant"]` `textContent` |
| NotebookLM | `textarea[aria-label="Query box"]` | `button[aria-label="Submit"]` | `button[aria-label="Submit"]` 重新存在且 `disabled=true` | 最后一个 `.message-text-content` `textContent` |
| Claude | `[contenteditable="true"][aria-label*="prompt to Claude"]` | `button[aria-label="Send message"]` | `button[aria-label="Send message"]` 重新出现 (stop-response 变回 send) | 最后一个 `.standard-markdown` `textContent` |

**Grace period**: done signal 触发后再等 2s 让流式收尾稳定。NotebookLM 因 RAG 检索阶段长, max timeout 调到 180s, 其他 3 平台 120s。

## 5. Reviewer subagent 派发 (Phase C, Rule D 强制)

- **Writer (operator)** = 主 session (无 subagent_type)
- **Reviewer** 必走不同 subagent_type. 候选池 (R1-R2 已烧 14 个, R3 不强制不重 — Rule D 看每个 run 内不重, 跨 run 不禁):
  - 推荐 #15: `oh-my-claudecode:scientist` (数据分析 + 评分, 适合多题对照)
  - 备选 #16: `feature-dev:code-reviewer` (R2 13th 已烧过, 也行)
  - 严格 Rule D: 主 session ≠ reviewer subagent_type
- **派发模式** (两选一):
  - **A. 每题 1 reviewer call**: 17 个 reviewer subagents, 各看自己那题 4 平台答案. 总并行 17. 适合 deep dive per question.
  - **B. 每平台 1 reviewer call**: 4 个 reviewer subagents, 各看自己那平台 17 题. 适合 cross-question 平台一致性评估.
  - **推荐 A** (per question), 与 SMOKE_V4 §3 判据粒度一致
- **Reviewer 输入**: 题文 + SMOKE_V4 §2 该题判据段 + 4 平台 raw 答案 path + 评分 schema (PASS/PARTIAL/FAIL/PUNT)
- **Reviewer 输出**: `r3/evidence/_reviews/q<NN>_review.md`, 内含 4 平台 verdict + reasoning + 与主 session inline self-score 一致性 check
- **冲突处理**: reviewer vs main session 不一致 → 主 session 在 R3_RETROSPECTIVE 决策段写明谁取胜 + 原因

## 6. Failure 归档 (Rule B)

任一题任一平台 abort/error → `r3/failures/q<NN>_<platform>_attempt_<X>.md`:
- 题文 (输入)
- runner 注入的完整 script (再现性)
- `window.__SMOKE_<P>_RESULT` full dump (含 events / samples / abortReason)
- 技术判定 (selector failed / 网络中断 / done signal 永远不触发 / ...)
- 业务判定 (这题题文是否需要重写? 这平台是否需要预热?)
- 下一 attempt 输入 (题文 + 修复点)

**不 rm**. 失败数据是 R4 / 后续改进最贵的资料。

## 7. Retro (Rule C, R3 完成后必写)

`r3/R3_RETROSPECTIVE.md` 三段:
1. **保留下来的做法** — 并行方法是否真的 ROI > 串行? Done 信号是否在所有 17 题都稳? Reset 流程是否需调?
2. **必须补上的缺口** — 哪些题/平台需 R4 修?
3. **关键决策复盘** — 并行 vs 串行选哪个作主流?

## 8. 主 session 启动 checklist

收到用户 trigger "R3 并行开始" 后, 主 session:

1. Read `r3_orchestration_parallel.md` (本文件) 全文
2. Read `r3_kickoff.md` (定方向)
3. curl 9222 验 CDP
4. mcp `list_pages` 验 4 标签
5. 跑 Phase A preflight
6. **暂停, 报 preflight 结果给用户, 等 ack** 再进 Phase B
7. Phase B 17 题主循环 (Bash sleep + 异常归档)
8. Phase C reviewer subagent 派发
9. Phase D retro 写, 与用户确认后 commit

## 9. 与 r3_kickoff.md (串行 fallback) 的关系

并行失败 (e.g. 多平台 fire-and-forget 不可靠 / done 信号在长题失效 / Chrome tab 严重 throttle) 时, **退到 r3_kickoff §每题 cowork 流程** 串行跑。串行流程已 R1+R2 验证过, 保底可用。
