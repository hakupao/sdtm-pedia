# NotebookLM — Dry-run 可行性 (2026-05-19)

> 通过 chrome-devtools-mcp 接管已有 Chrome (端口 9222, profile=ChromeDev) 检视 notebook 页面
> URL: `https://notebooklm.google.com/notebook/453999fc-2927-414a-9e43-3d15dd0a97ca?authuser=1`
> Notebook 名: **SDTM Knowledge Base** (42 sources, May 19 2026)
> 模式: dry-run, 仅 a11y snapshot + screenshot, 未键入未点击

## 接管结论: ✅ **可行, 一个明确陷阱已锁定 (顶部 notebook 标题框)**

## 关键 selector

| 用途 | role + accessible name | 备注 |
|---|---|---|
| ✅ **对话输入框 (唯一正确)** | `textbox "Query box"` (multiline) | **就是这个**, label 自带 "Query box" 标识 |
| ✅ **提交按钮** | `button "Submit"` (disableable) | 常驻, 输入空时 disabled, 有内容自动 enable — 比 ChatGPT 的"动态出现"更稳 |
| ⚠ **陷阱: notebook 标题输入框** | `textbox value="SDTM Knowledge Base"` (在顶部 toolbar 里, 跟 logo 同行) | **不是对话框, 也不是搜索框, 是 notebook 改名字的 input**! 点它会进入 rename 模式。**绝对不能 fill 进这里** |
| 搜索 source / 搜索笔记本 | 当前 notebook detail 页**没有显示** search 框 (顶部只有 notebook title) | 用户提到的"搜索框"实际就是 ↑ 顶部 title input, 物理上是同一个元素 |
| ❌ **新开 conversation** | **不存在** — `button "Chat options"` 的 description 自带 "Chat history is now saved across sessions, delete it here" | 用户的策略 (一直用同一 chat) 是 NotebookLM 唯一选项, 不需要也无法 New chat |
| 已有内容 | chat 区显示的是 notebook auto summary (about "试验设计 / 实验室检查 / 变量合规性审计"), 还没开始问答 | 干净状态, 可以直接发第一条问题 |
| Studio 区 (副产物) | `Audio Overview` / `Slide Deck` / `Mind Map` / `Quiz` 等 button | SMOKE 不需要, 忽略 |
| 42 个 source 全列出 | 每个 `button "View source button"` description = 文件名 | 跟项目 `_progress.json` 中 42 source 一致, ✅ |

## 已知风险

1. **顶部 notebook title 输入框 (`textbox value="SDTM Knowledge Base"`) 跟对话框长得像** — 这是用户提醒过的"搜索框"陷阱。
   - 缓解: 写死流程"找 a11y label 严格匹配 **'Query box'** 的 textbox", 不依赖 viewport 位置。
2. **没有"新开 chat"机制** — chat 历史持久保存。
   - 影响: SMOKE 跑多题时, 同一 conversation 内累积上下文, 后续题会被前题污染 (Gemini/ChatGPT/Claude 可以每题开新 chat 隔离, NotebookLM 不行)。
   - 缓解: 接受这个限制, 或者每题之后用 `button "Chat options"` 菜单清除 chat history (需要再 snapshot 验证 menu item)。
3. **NotebookLM 答题速度较慢** — 引用 42 个 source 做 RAG, response time 通常比 chat-only 平台长 (经验值 15-40s)。
   - 影响 done 检测策略: 比其他平台需要更长 timeout。
4. ✅ **无 Grammarly 干扰** — NotebookLM 输入框上没有 Grammarly hook (Google 自家产品对扩展加白名单管得严), 比 Gemini/ChatGPT/Claude 都干净。

## 正式跑 SMOKE 前的前置动作 checklist

- [ ] **死锁 selector**: a11y label === `"Query box"` 才允许 fill, 任何其他 textbox 一律 reject
- [ ] 决定多题策略: 接受 conversation 累积污染, 还是每题后清除 chat history?
- [ ] 实测一次答题, 固定:
  - done 信号 (Submit button 变 disabled 后再变 enabled? 还是 message 区出现新 model 回答 + N 秒不变?)
  - 响应抽取 (NotebookLM 的回答带 citation `[1] [2]` 标记, evidence 是只抽纯文本还是连 citation?)
- [ ] 验证 "Chat options" 菜单里到底有没有 "Delete chat history" 项

## 截图

- `./03_notebooklm.png` — notebook detail page, 显示 42 sources + auto summary, 对话框空

## 校准结果 (2026-05-19 dry-run, 题 "什么是 SDTM?", 4 平台并行触发)

> 仅记录 selector / 信号 / 时序 metadata, **回答正文未保存** (按用户边界)。

### ✅ 输入框 selector 锁定 — 用户提醒的陷阱避开了
- **`textarea[aria-label="Query box"]`** 命中 (tagName=TEXTAREA, 不是 contenteditable; 与其他 3 平台不同)
- 顶部 `textbox value="SDTM Knowledge Base"` (notebook 标题改名框) **未被错触** ✅
- 推荐 SMOKE 用: `document.querySelector('textarea[aria-label="Query box"]')`

### ✅ Submit 按钮 selector
- **`button[aria-label="Submit"]`** 命中
- 生成中 from DOM 消失 (或被替换), 完成后重新出现且 **`disabled=true`** (因为 input box 已清空)

### Done 信号 (锁死)
- **完成判定**: `button[aria-label="Submit"]` 重新出现, 且 `.disabled === true`
- 推荐 SMOKE 轮询: 每秒查 submit btn, 存在且 disabled = done

### 时序 ⚠ 最特殊
| 节点 | 耗时 (s) |
|---|---|
| 派发 → 输入完成 | 0.5 |
| 输入 → submit click | <0.1 |
| submit → **首字出现** | **~34** ← RAG 检索阶段 (42 个 source) |
| 首字 → 全文完成 | **~5** ← 实际流式很快 |
| send → 生成完成 (总) | **~40** |
| **总单题墙钟** | **~41** |
| 响应字数 (元数据, 内容未存) | 1425 chars (4 平台中**最长**) |

### ⚠ NotebookLM 比其他 3 平台多 ~30s "RAG 检索" 时间
- 前 34s 看似无反应, 实际在检索 42 个 source — **SMOKE timeout 必须 ≥ 90s 单题**, 不能用 30s 短超时判 fail
- 这是预期行为, 不是 bug

### 响应抽取 selector ✅ (二轮校准锁定)
- **每条消息卡片**: `mat-card-content.message-content` (Angular Material, NotebookLM Angular SPA)
- **纯文本子节点**: `div.message-text-content` (推荐用这个抽响应文本)
- 简化 selector: `.message-text-content` 全局唯一够用
- ⚠ 这个 selector 同时匹配用户消息和 AI 消息; 区分方法: AI 响应外层 `mat-card` 的 class 通常含 "from-model" 或类似 (需正式 SMOKE 跑时再细化), 或简单按"count 增长 + textLen > N"启发判定
- 已实测当前 conversation: 1 条 AI 响应 textContent = 1368 chars (与轮 1 的 1425 略差, gAL 兜底匹配多算了 citation 区域)

### 删 chat history 路径 ✅ (二轮 probe 确认)
- 入口: `button[aria-label="Chat options"]` → 弹出菜单
- 菜单项 (实测两项):
  1. `button[role="menuitem"]` text="Customize notebook"
  2. **`button[role="menuitem"]` text="Delete chat history Chat history is private to you."** ⭐
- SMOKE 多题流程: 每题答完 → 点 Chat options → 点 "Delete chat history" → **可能弹 confirm dialog** (本轮没实测点击避免误删数据, 下次必要时再 probe 确认 dialog 结构)
- 推荐脚本判定: menuitem text 以 `"Delete chat history"` 开头

### 风险更新
- ✅ 用户最担心的"搜索框 vs 对话框"陷阱通过 — `aria-label="Query box"` 严格匹配, 不可能选错
- ✅ Submit disabled 状态作 done 信号, 比其他平台 button 切换更可靠
- ❌ 不支持新开 chat — 这次答完后, conversation 中已留下"什么是 SDTM?" + 回答; 下次 SMOKE 题会跟这条上下文同 chat
- ⚠ 建议正式 SMOKE 前实测一次"删 chat history" 路径 (`button "Chat options"` → menu item)
