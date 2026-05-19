# SMOKE_V4 R3 — Phase A Preflight

> 执行: 2026-05-19 R3 并行 kickoff
> 模式: r3_orchestration_parallel.md (并行 per-question, dry-run 已验证 2026-05-19)

## 1. CDP / Chrome 版本

- Chrome: 148.0.7778.168
- CDP Protocol: 1.3
- WebSocket: `ws://localhost:9222/devtools/browser/bcc97b77-8bea-49d5-b6fe-556aa85e9a59`
- 状态: ✅ 通

## 2. 4 平台标签 + selector verification

| 平台 | pageId | URL | 输入框 | 输入框 aria | Send/Submit btn | 历史 msg | Reset 方式 |
|---|:-:|---|---|---|---|:-:|---|
| **Gemini Gem** | 1 | `gemini.google.com/u/1/gem/3b572e310813/3e670722f609be44` | DIV contenteditable | `Enter a prompt for Gemini` | `aria-label="Send message"` exists, enabled | 1 model-response (历史) | `scripts/reset_gemini.js` (内 click "New chat" + Pro mode) |
| **ChatGPT GPT** | 3 | `chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-.../c/6a0bcc2f-3cb8-...` | DIV `#prompt-textarea` | `Chat with ChatGPT` | `[data-testid="send-button"]` 隐藏 (input 空) / `[data-testid="stop-button"]` 不在 (无 in-flight) | 1 user + 1 assistant | `navigate_page` 到 `chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-knowledge-base` (回 landing, 起新 chat) |
| **NotebookLM** | 4 | `notebooklm.google.com/notebook/453999fc-2927-414a-9e43-3d15dd0a97ca?authuser=1` | TEXTAREA | `Query box` | `aria-label="Submit"` exists, disabled (input 空) | 2 messages (历史) | `scripts/reset_notebooklm.js` (内 click Chat options → "Delete chat history") |
| **Claude Project** | 5 | `claude.ai/chat/331be618-b312-4a68-9e2e-601284c15689` (内 project "SDTM Knowledge Base") | DIV contenteditable | `Write your prompt to Claude` | `aria-label="Send message"` exists, enabled / `aria-label="Stop response"` 不在 | 1 .standard-markdown | `navigate_page` 到 project URL `claude.ai/project/019da929-2822-77c9-af9a-febc22c83255` (回 landing, 起新 chat 内 project) |

**Project URL (Claude)** verified via sidebar a 元素: `https://claude.ai/project/019da929-2822-77c9-af9a-febc22c83255`

## 3. Sanity check 结果

✅ 4 平台输入框 selector 与 dry-run (2026-05-19) 完全一致, 无漂移
✅ 4 平台均无 in-flight stream (stop btn 不存在, generation 未在跑)
✅ 4 平台 URL 与 r3_orchestration_parallel.md §2 锁定一致

⚠️ 4 平台均有历史 conversation, 入 Phase B 每题前需先跑 reset:
- Gemini + NotebookLM: 跑 `reset_*.js`
- ChatGPT + Claude: `navigate_page` 到 landing URL

## 4. R3 evidence + scripts 目录

```
.work/07_release_v1_1/r3/
├── evidence/
│   ├── _preflight.md  ← 本文件
│   ├── chatgpt/       (空, Phase B 写入)
│   ├── claude/        (空)
│   ├── gemini/        (空)
│   └── notebooklm/    (空)
├── scripts/
│   ├── chatgpt_runner.js
│   ├── claude_runner.js
│   ├── gemini_runner.js
│   ├── notebooklm_runner.js
│   ├── reset_gemini.js
│   ├── reset_notebooklm.js
│   └── reviewer_prompt_template.md
├── r3_kickoff.md (串行 fallback)
├── r3_matrix.md (17 × 4 = 68 cells, 待填)
└── r3_orchestration_parallel.md (本次方法主线)
```

## 5. Phase A 结论

**全 PASS, 可进 Phase B**.

下一步等用户口头 ack (规则 D 第 4 条 PASS 四条), 然后:
- Phase B 17 题主循环 (取 Q1 题文 → reset 4 平台 → fire-and-forget → 等 ~70-90s → 收 4 个 result → 写 4 份 evidence + matrix cell)
- 题目优先级按 SMOKE_V4.md §2: Q1-Q14 + AHP1-3
