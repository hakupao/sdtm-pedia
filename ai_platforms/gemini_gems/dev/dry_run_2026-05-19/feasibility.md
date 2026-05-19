# Gemini Gem — Dry-run 可行性 (2026-05-19)

> 通过 chrome-devtools-mcp 接管已有 Chrome (端口 9222, profile=ChromeDev) 检视 Gem 页面
> URL: `https://gemini.google.com/u/1/gem/3b572e310813`
> Gem 名: **SDTM Knowledge Base**
> 模式: dry-run, 仅 a11y snapshot + screenshot, 未键入未点击

## 接管结论: ✅ **可行**

页面元素 a11y 完整, 输入 / 提交 / 新开 / 搜索四种操作都能可靠定位。

## 关键 selector (按 a11y label 找, uid 每次 snapshot 重生成不固定)

| 用途 | role + accessible name | 备注 |
|---|---|---|
| **对话输入框** | `textbox "Enter a prompt for Gemini"` (multiline, focused) | 安全填写 |
| **提交按钮** | `button "Send message"` | **常驻**, 不像 ChatGPT/Claude 动态出现 |
| **新开 chat (留在当前 Gem)** | toolbar 上 `button "New chat"` 或 sidebar 上 `link "New chat"` (URL=`https://gemini.google.com/app`) | ⚠ sidebar 那个 link href 是 `/app` (Gemini 主页), 实测上 Gemini 会保持在当前 Gem 上下文 — 第一次正式跑前先验证一下 |
| **搜索 chat (与对话框分开)** | `button "Search" description="Search chats (⇧⌘K)"` | 跟输入框完全不同位置, 不会混淆 |
| 消息容器祖先 | `heading "Conversation with Gemini" level=1` | 用来锚定"新回答"在 DOM 哪一段 |

## 已知风险

1. **Grammarly 监听输入框** — `button "Rewrite with Grammarly"` 出现在输入框旁边。Grammarly 会在键入后自动 suggest rewrite, 可能改写 prompt 文本。
   - 缓解: 正式 SMOKE 跑前在 `chrome://extensions/` 暂停 Grammarly, 或者 fill 后 evaluate_script 校验 `textbox.value === expected`, 不匹配则重填。
2. **Sidebar 暴露 39 个历史 chat** — 隐私不大问题 (都是用户自己的 chat), 但截图 / evidence 可能含敏感标题, 后续 evidence 注意脱敏 (这次 dry-run 截图未脱敏)。
3. **"New chat" sidebar link 是 `/app` 而非 Gem URL** — 需要正式跑前验证: 点了之后是仍在 Gem (上下文保持) 还是跳到 default Gemini (上下文丢)? 截图看 toolbar 也有 New chat button, 优先用 toolbar 那个。

## 正式跑 SMOKE 前的前置动作 checklist

- [ ] 禁用 Grammarly (或加 fill 后校验)
- [ ] 验证 "New chat" 哪个入口能保持在 Gem 上下文 (toolbar button vs sidebar link)
- [ ] 确认 done 信号: Send button 发完后是否变 disabled / 变 stop icon? 还是只能轮询最后一条 message 文本稳定 N 秒? (需手工触发一次答题观察)
- [ ] 响应抽取 selector: 最后一条 model message 的 a11y 节点该怎么定位 (snapshot 一次实际答完的状态来固定)

## 截图

- `./01_gemini.png` — Gem landing page, 输入框空, 没有 conversation

## 校准结果 (2026-05-19 dry-run, 题 "什么是 SDTM?", 4 平台并行触发)

> 仅记录 selector / 信号 / 时序 metadata, **回答正文未保存** (按用户边界)。

### ✅ Pro mode 切换通过
- mode picker 实测 a11y label: `button "Open mode picker"`
- Pro 选项 实测完整 label: **`Pro  Advanced math and code with 3.1 Pro`** (注意 "Pro" 后有双空格)
- 推荐脚本判定: `[role="menuitem"]` 中 text 满足 `^Pro\b` 且不含 `Upgrade`

### Done 信号 (锁死)
- 生成中: `button[aria-label="Send message"]` **完全从 DOM 消失** (不是 disabled, 是被移除) — 与 ChatGPT/Claude 的"按钮变 Stop"行为不同
- **完成判定**: `button[aria-label="Send message"]` 重新出现且 `!disabled`
- 推荐 SMOKE 轮询: 每秒查 `document.querySelector('button[aria-label="Send message"]:not([disabled])')`, 非 null = done

### 时序
| 节点 | 耗时 (s) |
|---|---|
| 派发 → Pro 切换完成 | 2.0 |
| Pro 切完 → 输入完成 | 0.5 |
| 输入 → send click | <0.1 |
| send → 生成完成 | **~41** |
| **总单题墙钟** | **~44** |
| 响应字数 (元数据, 内容未存) | 1187 chars |

### 响应抽取 selector ✅
- `model-response` (custom element) 能命中, `querySelectorAll('model-response').length` 在生成开始后从 0→1
- assistant 文本: 取最后一个 `model-response` 的 `textContent`

### 风险更新
- ✅ Grammarly 干扰排除 (上一阶段已验证)
- ✅ Pro mode 切换可自动化
- ⚠ Gemini 生成中"按钮消失"的行为, 写 SMOKE 调度脚本时不能用"send 按钮变 Stop"假设
