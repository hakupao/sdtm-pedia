# ChatGPT GPT — Dry-run 可行性 (2026-05-19)

> 通过 chrome-devtools-mcp 接管已有 Chrome (端口 9222, profile=ChromeDev) 检视 GPT 页面
> URL: `https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc`
> GPT 名: **SDTM Knowledge Base** (by bojiangz.com)
> 模式: dry-run, 仅 a11y snapshot + screenshot, 未键入未点击

## 接管结论: ✅ **可行, 但有 2 个明显坑要绕**

## 关键 selector

| 用途 | role + accessible name | 备注 |
|---|---|---|
| **对话输入框** | `textbox "Chat with ChatGPT"` (multiline, focused) | 安全填写 |
| **提交按钮** | ⚠ **动态生成** — 输入框为空时**没有** send 按钮, 只有 `button "Start dictation"` + `button "Start Voice"`; **fill 进文字后 send 按钮才出现** | 必须 fill 后重新 snapshot 找新按钮 uid |
| **新开 chat (回到当前 GPT)** | ⚠ **不要点 sidebar `link "New chat"` (href=`https://chatgpt.com/`) — 它会跳到 ChatGPT default 主页, 离开当前 GPT!** 正确做法: 点 `link "SDTM Knowledge Base"` (sidebar GPTs 区), 或 `navigate_page` 到 GPT URL `https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc` | **关键陷阱**, 跟 Gemini 行为不一致 |
| **搜索 chat** | `button "Search chats"` | 跟输入框分开 |
| 4 个建议 prompt | 4 个 button, e.g. "1. AE 域的 AESER 变量定义是什么?" | landing page 才有, 进 conversation 后消失 |
| 消息容器 | 当前页面 `main` 下方, 由于 conversation 未开始, 此次无消息 dom 可参考 | 第一次正式答题后再固定 |

## 已知风险

1. **Send 按钮动态出现** — 这是 OpenAI UI 的特点, 输入空时 send button 不挂载。
   - 缓解流程: `fill` 输入 → 再 `take_snapshot` → 找新出现的 `button "Send"` (或 ARIA 名 "Send prompt") → click。
2. **"New chat" 会跳出 GPT** — sidebar 里 `link "New chat"` href 是 `chatgpt.com` 根 URL, 不带 GPT slug, 一点就回到普通 ChatGPT。
   - 缓解: 每次新开 conversation 用 `navigate_page` 直接打 GPT URL, 或者点 sidebar 里的 GPT 名字 `link "SDTM Knowledge Base"`。
3. **Grammarly 监听输入框** (同 Gemini) — `button "Rewrite with Grammarly"` 在场, 可能改写 prompt。
   - 缓解: 同 Gemini, 禁用扩展或 fill 后校验。
4. **侧边栏暴露大量历史 chat** (Personal/工作隐私) — 截图脱敏问题, 同 Gemini 情况。

## 正式跑 SMOKE 前的前置动作 checklist

- [ ] 禁用 Grammarly (或加 fill 后校验)
- [ ] 固化"新开 conversation"的入口选 `navigate_page` 还是 `click GPT-name link` (推荐 navigate, 更稳定)
- [ ] 实测一次答题, 固定:
  - send 按钮 fill 后的 a11y label (大概率是 `button "Send prompt"` 或 `button "Send"`)
  - done 信号 (ChatGPT 答题中 send 按钮会变成 `button "Stop generating"`, 答完恢复为 send)
  - 响应抽取的 message bubble selector (一般是 `[data-message-author-role="assistant"]`, 但要确认 a11y label)

## 截图

- `./02_chatgpt.png` — GPT landing page, 输入框空, 显示 4 个建议 prompt

## 校准结果 (2026-05-19 dry-run, 题 "什么是 SDTM?", 4 平台并行触发)

> 仅记录 selector / 信号 / 时序 metadata, **回答正文未保存** (按用户边界)。

### ✅ 输入框 selector 修正
- **`#prompt-textarea`** 直接命中 (id 选择器最稳, 比 a11y label 更可靠)
- 实测 tagName=DIV (contenteditable 不是 textarea)
- 推荐 SMOKE 用: `document.querySelector('#prompt-textarea')`

### ✅ Send 按钮 selector 实测
- **`[data-testid="send-button"]`** 直接命中 (推荐用 data-testid, 比 aria-label 更稳)
- aria-label 实测: `"Send prompt"` (之前 evidence 猜测的, 现在确认)
- **fill 后立即出现** (没有明显延迟, 不必 wait_for)

### Done 信号 (锁死)
- 生成中: 按钮替换为 **`[data-testid="stop-button"]`** + `aria-label="Stop answering"`
- **完成判定**: `[data-testid="stop-button"]` 从 DOM 消失 (即 `document.querySelector('[data-testid="stop-button"]') === null`)
- 推荐 SMOKE 轮询: 每秒查 stop-button, 非 null = 生成中; null = 完成

### 时序
| 节点 | 耗时 (s) |
|---|---|
| 派发 → 输入完成 | 0.5 |
| 输入 → send click | <0.1 |
| send → 生成完成 | **~21** (4 平台最快) |
| **总单题墙钟** | **~22** |
| 响应字数 (元数据, 内容未存) | 577 chars |

### 响应抽取 selector ✅
- **`[data-message-author-role="assistant"]`** 能命中, length 0→1 后稳定
- assistant 文本: 取最后一个该选择器节点的 `textContent`

### 风险更新
- ✅ Grammarly 排除
- ✅ Send 按钮"动态生成"假设证实, 但 fill 后立刻出现 — 用 wF (waitFor) 即可
- ⚠ "New chat 跳出 GPT" 风险仍然存在 — 这次因为 GPT URL 是初始状态没触发; SMOKE 多题时仍需走 `navigate_page` 回 GPT URL
