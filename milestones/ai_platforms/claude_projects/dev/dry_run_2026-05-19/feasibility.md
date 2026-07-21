# Claude Project — Dry-run 可行性 (2026-05-19)

> 通过 chrome-devtools-mcp 接管已有 Chrome (端口 9222, profile=ChromeDev) 检视 project 页面
> URL: `https://claude.ai/project/019da929-2822-77c9-af9a-febc22c83255`
> Project 名: **SDTM Knowledge Base** (project capacity 77%, 15 source files)
> 模式: dry-run, 仅 a11y snapshot + screenshot, 未键入未点击

## 接管结论: ✅ **可行, 跟 ChatGPT 同套坑 (send 动态 + new chat 跳出)**

## 关键 selector

| 用途 | role + accessible name | 备注 |
|---|---|---|
| **对话输入框** | `textbox "Write your prompt to Claude"` (multiline, focused) | 安全填写 |
| **提交按钮** | ⚠ **动态生成** (同 ChatGPT) — 空时不存在, fill 后才出现, 需重新 snapshot 找 | 大概率名称 `button "Send Message"` 或类似 |
| **新开 chat (留在当前 Project)** | ⚠ **不要点 sidebar `link "New chat"` (href=`https://claude.ai/new`)** — 会跳出 project 上下文! 正确做法: **保持在 project URL** (`/project/<id>`) **+ 直接在 textbox 提交** — Claude 会自动把这条提交创建为 project 内的新 chat | **同 ChatGPT 行为** |
| **搜索** | `link "Search" ⌘K` | 分开 |
| 历史 project chats | `link "DSDECODE和TUSTDTC字段标准性 Last message 3 days ago"` 等 4 条 | project landing 页才显示 |
| Project Instructions | `button "Edit Instructions"` + 后面 StaticText 完整可读 | 内容是 "SDTM Expert — Project Instructions"完整 prompt (~ 6KB), 跟仓库 `release/v1.0/self_deploy/claude/` 教程一致 |
| Project Files | 15 个 `button "<file>.md, md, <N> lines"` | `00_routing.md` / `01_index.md` / `02_chapters.md` / ... / `13c_terminology_tail_supp.md` 全列出, ✅ |
| 模型选择器 | `button "Model: Opus 4.7 Adaptive"` | 当前是 Opus 4.7 |
| Memory | `heading "Memory" "Only you" "Project memory will show here after a few chats."` | 当前空 |

## 已知风险

1. **Send 按钮动态出现** (同 ChatGPT) — 输入空时无 send button。
   - 缓解: fill 后 re-snapshot, 找新出现的 send button uid。
2. **"New chat" sidebar link 跳出 project** (同 ChatGPT) — `link "New chat"` href=`/new`, 是普通 claude.ai 起一个 free-context chat, **不**带 project 上下文。
   - 缓解: 用 `navigate_page` 到 project URL (`https://claude.ai/project/<id>`), 在 landing 页直接发 prompt — Claude 会把这次提交自动创建为 project 内 chat。
3. **Grammarly 监听输入框** (同 Gemini/ChatGPT) — `button "Open Grammarly."` 在场。
   - 缓解: 禁用扩展或 fill 后校验。
4. **Project capacity 77%** — 不影响 dry-run, 但正式跑题时若 model 引用大量 source, response 慢。
5. **Sidebar 暴露大量 chat 历史** (Recents 30+) — 隐私问题同其他平台。

## 正式跑 SMOKE 前的前置动作 checklist

- [ ] 禁用 Grammarly (或加 fill 后校验)
- [ ] 固化"新开 conversation"流程: `navigate_page` → project URL → fill textbox → submit, 不点 New chat link
- [ ] 实测一次答题, 固定:
  - send 按钮 fill 后的实际 a11y label
  - done 信号 (Claude 答题中 send button 会变 `button "Stop"` 图标? 答完恢复? 还是要轮询 message 文本稳定?)
  - 响应抽取 (Claude 答题如果产出 artifact 怎么处理? SMOKE_V4 题目应该不会触发 artifact, 但需 evidence 中注明 "artifact 视为异常, 重跑")
- [ ] 确认是否要切到非 "Opus 4.7 Adaptive" 的固定模型 (Adaptive 会动态降级到 Haiku/Sonnet, 跨平台对照评测时 model 不固定会影响公平性)

## 截图

- `./04_claude.png` — project landing page, 显示 instructions + 4 个历史 chat + 15 files + 输入框空

## 校准结果 (2026-05-19 dry-run, 题 "什么是 SDTM?", 4 平台并行触发)

> 仅记录 selector / 信号 / 时序 metadata, **回答正文未保存** (按用户边界)。

### ✅ 输入框 selector
- **`[contenteditable="true"][aria-label*="prompt to Claude"]`** 命中 (实测 aria="Write your prompt to Claude")

### ✅ Send 按钮 — 修正之前的"动态出现"假设
- **fill 后立即可用** (没有明显延迟, 跟 ChatGPT 一样)
- 实测 aria-label: `"Send message"` (之前 evidence 假设"未知 label" 现在确认)
- 推荐 SMOKE 用: `Array.from(document.querySelectorAll('button')).find(b => b.getAttribute('aria-label') === 'Send message' && !b.disabled)`

### Done 信号 (锁死)
- 生成中: 按钮 aria-label 变为 **`"Stop response"`**
- **完成判定**: `button[aria-label="Send message"]` 重新出现
- 推荐 SMOKE 轮询: 每秒查 send btn, 看 aria-label 是 "Send message" 还是 "Stop response"

### 时序
| 节点 | 耗时 (s) |
|---|---|
| 派发 → 输入完成 | 0.5 |
| 输入 → send click | <0.1 |
| send → 生成完成 | **~47** (4 平台最慢) |
| **总单题墙钟** | **~48** |
| 响应字数 (元数据, 内容未存) | ~2070 chars |
| URL 转换 | 派发后 `/project/<id>` → `/chat/<chatid>` (Claude 自动把这次提交转为 project 内新 chat) |

### 响应抽取 selector ✅ (二轮校准锁定)
- **AI 响应容器**: **`div.standard-markdown`** (Claude 渲染 markdown 的专用 class, 不与用户消息撞)
- 完整 class list (供 fallback): `standard-markdown grid-cols-1 grid [&_>_*]:min-w-0 gap-3`
- 实测当前 conversation: 1 个 `.standard-markdown` 元素, textContent = 1694 chars (与轮 1 的 2070 略差, 之前 gAL 兜底多匹配了 sidebar)
- 推荐 SMOKE 用: `Array.from(document.querySelectorAll('.standard-markdown')).slice(-1)[0]?.textContent` 取最后一条
- ⚠ 一个 AI 回答可能产生**多个** `.standard-markdown` 元素 (artifact / code block 等会另起新 markdown 段), SMOKE 跑分前若题有 code 类型, 需进一步细化 "一条完整 AI turn" 的包裹容器 (推测在 `[class*="message-content"]` 这一层)

### 风险更新
- ✅ Grammarly 排除
- ✅ "New chat 跳出 project" 不需要点 New chat — 我的方法 "保持在 project URL + 直接 fill+submit" 工作: URL 自动从 `/project/<id>` 跳到 `/chat/<chatid>` (Claude 后台把这次对话挂到 project), 这是符合预期的
- ⚠ 响应 selector 还要细化 (上一项)
- ⚠ "Opus 4.7 Adaptive" 模型 — 这次没固定模型, 跨平台对照评测前要决定是否强制切到固定模型
