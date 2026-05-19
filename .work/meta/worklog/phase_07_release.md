# Phase 07 Release Worklog

> 入口: 跨 v1.0 + v1.1 (公司发布版) 工作日志.
> v1.0 历史细节在 `.work/07_release/{PLAN,RETROSPECTIVE}.md` (主体在那).
> v1.1 入口在 `.work/07_release_v1_1/PLAN.md`.
> Chain B: 本文件 → 各平台 `_progress.json` → `docs/PROGRESS.md`.

## 2026-04-27 — Release v1.0 (公司发布版) sign-off

详见 `.work/07_release/RETROSPECTIVE.md`. 24 文件三语 release 包, tag `v1.0-company-release`.

## 2026-05-15 — Release v1.1 cut (06 deep verification 修复回灌)

**触发**: 06 P7 COMPLETE 2026-05-12, 工程全部收官. knowledge_base/ 43 文件 +1,405 / -234 行净更新 (DI 新加, PC §6.3.5.9 RELREC 等) 未回灌到 ai_platforms 部署包和 release 自部署包.

**决策**: 走 v1.1 路线 (用户 ack 2026-05-15) — cut 新 tag, 而非 in-place 更新 v1.0 (tag 不可变).

**4 平台 rebuild**:
- chatgpt: merge_for_chatgpt.py --stage all, 9 文件 (4 changed: 02/03/05/06)
- gemini: merge_for_gemini.py --stage c_refactor, 3 KB 派生文件全 rebuild (01/02/03; 04 writer-authored 不动)
- notebooklm: merge_sources.py, 42 buckets (11 changed + bucket 25 加 DI)
- claude_projects: v1 + v2 双 builder 系统, executor subagent 后台跑 (路径 stale 需修复)

**Build 脚本改动**:
- chatgpt merge_for_chatgpt.py: 05 expected_segments 63→64 + token_cap 69K→85K (DI 加入)
- notebooklm bucket_config.json: bucket 25 (td_meta_ti_ts_oi) 加 domains/DI/assumptions.md

**Rule D 独立 reviewer**: TBD (pending claude rebuild 完成后统一 review)

**收尾**:
- evidence: `.work/07_release_v1_1/evidence/{diff_summary.md, rule_d_review.md, *_rebuild.log}`
- release 包: `release/v1.1/{CHANGELOG.{en,zh,ja}.md, BUILD_MANIFEST.json, self_deploy/{4 平台}/}`
- retrospective: `.work/07_release_v1_1/RETROSPECTIVE.md` (三段: 保留/缺口/决策)
- tag: `v1.1-company-release` 推送后

### 2026-05-15 PM — v1.1 cut COMPLETE (sign-off pending commit)

**Executor outcome** (sonnet, ~6.3 分钟, 51 tool uses):
- 7 文件 rebuilt (`02_chapters.md` +12.5KB, `03_model.md` +1.5KB, `06_assumptions.md` +24.2KB 含 DI, `07_examples_catalog.md` -4B, `09_examples_data_high.md` -15KB pre-existing cap, `10_examples_data_others.md` +202B)
- 1 文件 idempotent (`05_mega_spec.md` 0 byte; DI 无 spec.md, 63 域不变)
- 12 文件 unchanged (terminology + routing + index)
- Failures F1-F4 archived to `failures/claude_rebuild_failures.md` (Rule B 合规: stale REPO_ROOT path bug 工作绕过)

**Rule D verifier** (oh-my-claudecode:verifier opus, ~4.5 分钟, 46 tool uses): **ALL_PASS**
- Evidence 完整性 PASS
- Rule A 5/5 抽检 (PC §6.3.5.9 RELREC, DI assumption, TA assumption, ch02, ch08) × 4 平台 = 20 grep hits zero miss
- Build script 改动正确性 PASS (chatgpt 05 + notebooklm bucket 25, 最小必要)
- Release v1.1 包结构 PASS (4 平台 + 元文档 byte-identical 继承 v1.0 + 三语 CHANGELOG 一致 + BUILD_MANIFEST 完整)
- 红线 PASS (KB 0 反向污染 + baseline 25MB 完整 + failures Rule B 合规)
- 跨平台 delta oracle 自洽: chatgpt 05 ≡ gemini 02 = +74,178 bytes
- 5 项 LOW/MEDIUM 改善观察 (O1-O5) 已在 RETROSPECTIVE §二 主动记录

**Release artifact**: `release/v1.1/{CHANGELOG.{en,zh,ja}.md, BUILD_MANIFEST.json, self_deploy/{chatgpt(9.3M),claude(4.6M),gemini(2.2M),notebooklm(9.5M)}/}` = 26MB.

**Build script 改动** (Chain B 同步):
- `ai_platforms/chatgpt_gpt/dev/scripts/merge_for_chatgpt.py` — 05 entry expected_segments 63→64 + token_cap 69_000→85_000
- `ai_platforms/notebooklm/dev/scripts/bucket_config.json` — bucket 25 加 `domains/DI/assumptions.md` + description 加 DI 注

**Tag 候选**: `v1.1-company-release` (待用户 ack push 后创建).

### 2026-05-19 — Chrome MCP dry-run + R3 SMOKE_V4 并行执行 scaffold

**触发**: 用户接管 Chrome (`--remote-debugging-port=9222` + 旁路 `~/ChromeDev` profile, 因 Chrome 136+ 静默忽略默认 profile 的 debug 端口) 探"Chrome MCP 全自动并行 4 平台 R3 retest" 可行性. 与 `.work/07_release_v1_1/r3/r3_kickoff.md` (4 月预设的串行 cowork) 互补, 不替换.

**Dry-run (无 AI 答题, 仅 a11y snapshot + screenshot + selector probe)**:
- 4 平台接管 OK (chrome-devtools-mcp 自动挂 9222, 无需配 `--browser-url`)
- 关键发现:
  - NotebookLM `textarea[aria-label="Query box"]` 与顶部 notebook 标题改名框完全可区分 (a11y 严格匹配 — 用户预先警告的"搜索框"陷阱避开)
  - Grammarly 扩展可见按钮 disable 后 DOM 残留 `grammarly-desktop-integration` 是空壳 (bbox 0×0, 不监听输入框)
- Evidence 4 份 + 4 screenshot: `ai_platforms/{platform}/dev/dry_run_2026-05-19/{feasibility.md, NN_<platform>.png}`

**Round 1 校准 (4 平台并行触发 "什么是 SDTM?", 验 done 信号 + 时序)**:
- 4 平台 fire-and-forget script 同时跑, 总墙钟 ~107s (派 12s + 等 90s + 收 5s)
- Done 信号锁定:
  - Gemini: send 按钮**消失** during gen → 重新出现 + `!disabled` 即 done (~41s, 含 Pro mode 切换)
  - ChatGPT: `[data-testid="stop-button"]` 消失 (~21s, 最快)
  - NotebookLM: `button[aria-label="Submit"]` 重出现 + `disabled=true` (~41s, 含 ~30s RAG 检索)
  - Claude: `Send message` 按钮重出现 (stop-response 消失) (~48s, 最慢)
- Pro mode 实测 label: `"Pro Advanced math and code with 3.1 Pro"` (3.1 Pro 模型)

**Round 2 校准 (响应抽取 selector 细化 + NotebookLM 删 chat history 路径)**:
- NotebookLM 响应: `mat-card-content.message-content .message-text-content` (Angular Material), 简化 `.message-text-content`
- Claude 响应: `div.standard-markdown` (Claude markdown 渲染专用 class)
- NotebookLM "Chat options" menu 实测含 menuitem `"Delete chat history Chat history is private to you."` ✓ (confirm dialog 结构待 R3 第 1 题校准)

**R3 scaffold 落档** (`.work/07_release_v1_1/r3/`):
- `r3_orchestration_parallel.md` — Phase A-D 流程 + selector 引用表 + Rule D reviewer 规则 + Rule B failure 归档
- `scripts/{gemini,chatgpt,notebooklm,claude}_runner.js` — fire-and-forget runner, `__QUESTION_PLACEHOLDER__` 待 sed 替换
- `scripts/reset_{gemini,notebooklm}.js` — await-able 重置 (Gemini 新 chat + Pro mode; NotebookLM 删 chat history + confirm dialog 兜底)
- `scripts/reviewer_prompt_template.md` — Rule D 隔离 reviewer subagent prompt (推荐 `oh-my-claudecode:scientist`)
- 原 `r3_kickoff.md` 串行流程加 4 行注脚指向并行方法 (保留作 fallback)

**预估**: R3 实跑 17 题总墙钟 ~20 min (vs 串行 ~50 min, 2.5× 提速)

**遗留 (R3 实跑第 1 题校准)**:
1. NotebookLM "Delete chat history" confirm dialog 结构 (`reset_notebooklm.js` best-effort 兜底, 不命中则主 session 介入)
2. Claude multi-segment `.standard-markdown` (简单题单段; SMOKE_V4 含 mapping 表 / artifact 题需扩到外层包裹容器)
3. 4 平台 dry-run 测试 conversation 留有 1 道 "什么是 SDTM?" Q&A (Gemini/ChatGPT/Claude 新 chat / NotebookLM 共用 chat), R3 跑前 reset 流程自动清
