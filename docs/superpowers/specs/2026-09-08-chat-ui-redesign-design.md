# Chat UI 重构设计 (视觉/UX + 流式 Markdown + 出处折叠)

> 状态: **已批准** (2026-09-08 brainstorming 通过)
> 范围: `sdtm-rag/webchat/` 前端; 后端 SSE 契约、prompt、localStorage 存档格式**不动**。

## 0. 背景与目标

现状 `webchat/` (index.html 43 行 / style.css 67 行 / app.js 654 行, 原生 JS 无构建) 是功能堆砌, 视觉粗糙。用户点名的两个体验缺陷:

1. 流式输出期间只 `textContent` 追加, 用户看到裸 Markdown 语法, `done` 后才整体渲染。
2. 正文里随处可见 `**[Source: path]**`, 与正文混排干扰阅读; 对使用者无意义, 仅调试需要。

目标: 克制专业型的新视觉 + 流式实时 Markdown + 出处默认隐藏 (调试开关可恢复) + 四项小 UX。**所有既有功能与护栏原样保留**。

## 1. 不变量 (硬约束)

- SSE 事件契约 (`sources/token/tool_call/tool_result/done/error`) 与 `POST /api/ask_stream` payload 字段不变。
- localStorage `sdtm_chat_v1` / `sdtm_model` 的结构与语义不变; 老存档必须能原样读出并渲染。
- 存档内容存**原始 md** (含 `[Source: ...]`), 剥除只发生在渲染层; `POST /api/flag` 上报的 answer 也是原文。
- 以下经 Rule D 审阅过的护栏逐字保留其语义 (可搬家不可改意):
  - `modelBadgeText` 三态 + `fellBack === true` 全等 + `Array.isArray(modelsUsed)` 容器级校验, ⛔ 不加 `filter(Boolean)`。
  - `refreshModelBadgeLabels` 原地补字, 不整体重建 `#messages` (在途气泡不在 `c.messages` 里)。
  - `flagModelName` 回退归因逻辑。
  - `streamAsk` 的 terminal / onClose / onAbort 三路处理; `save()` 的 QuotaExceeded 逐出。
  - IME `isComposing || keyCode===229` 回车保护。
  - `renderWebStatus` 六态文案; `onToolResultUI` 六态文案。
  - `selectedCorpus()` 四值映射; 联邦关时 scope 控件隐藏; 下拉为空时 payload 省略 `model`。
- 无外网依赖: 字体只用系统栈 (`"Source Serif 4"` 若本机有则用, 否则 Georgia); 不新增 vendored 库。
- 缓存策略测试 `scripts/tests/test_webchat_cache_*.py` 必须继续通过。

## 2. 文件结构

```
webchat/
  index.html            骨架 (重写)
  style.css             design tokens + 全部样式 (重写)
  app.js                入口: 事件绑定 + 启动 (type=module)
  js/store.js           load/save/current/newConversation/delete/rename + prefs
  js/citations.js       [Source:]/[Web:] 抽取与剥除 (纯函数, 可单测)
  js/markdown.js        mdToSafeHTML + 流中未闭合围栏补全 + highlightIn
  js/render.js          sidebar / messages / meta chips / sources / web-panel / empty state
  js/stream.js          parseSSE + streamAsk (搬家, 不改逻辑)
  js/flag.js            ⚑ attachFlag/openFlag/flagModelName/postFlag (搬家)
  js/ui.js              设置弹层 / 滚动跟随 / 复制 / 删除两步确认 / 重命名
  tests/citations.test.mjs   node --test
  vendor/               不动
```

`index.html` 用 `<script type="module" src="/static/app.js">`; 模块间相对 import。StaticFiles 已托管整个 `webchat/`, 无需后端改动。

## 3. 视觉系统

Design tokens (CSS 变量, `:root`):

| token | 值 | 用途 |
|---|---|---|
| `--bg` | `#faf9f6` | 页面底 |
| `--bg-side` | `#f2f0eb` | 侧栏 |
| `--bg-user` | `#eeece6` | 用户消息块 |
| `--ink` | `#1c1b19` | 正文 |
| `--ink-2` | `#5c5a55` | 次级文字 |
| `--ink-3` | `#9a978f` | 淡灰 (出处/时间) |
| `--line` | `#e4e1da` | 分隔线 |
| `--accent` | `#1f6f5f` | 发送键/选中/链接 |
| `--accent-soft` | `#e3efeb` | 选中底 |
| `--warn` | `#b45309` | 未验证/联网告警 (沿用) |
| `--danger` | `#b3261e` | 错误/删除确认 |
| `--font-serif` | `"Source Serif 4", "Songti SC", Georgia, serif` | 标题/空状态标题 |
| `--font-sans` | 系统栈 | 正文 |
| `--font-mono` | `ui-monospace, Menlo, monospace` | 代码/出处 |

布局:
- 侧栏 260px 固定, 可折叠 (按钮 + `localStorage` 记忆), 折叠后 0 宽仅留展开钮。
- 主区: 顶栏 (标题 + 当前模型名 + 设置齿轮) / 消息滚动区 / 底部 composer。
- 消息列 `max-width: 720px` 居中。用户消息: 右对齐浅色圆角块 (max 80%)。AI 回答: 无气泡, 左侧无头像, 直接排版, 段落 `line-height 1.7`。
- 每条 AI 回答底部一行 **meta chips** (12px, 圆角小标签): 模型徽章 (琥珀态沿用) / 判定库 / 联网状态; 再下方是「来源 (N)」折叠 + 悬停工具条。
- 联网搜索过程面板 (`web-panel`) 保留在回答上方, 改成浅底细左边条样式, 与 tokens 统一。

## 4. 流式 Markdown 渲染 (`markdown.js` + `render.js`)

- `onToken`: `acc += t`, 置 `dirty=true`; 一个 `requestAnimationFrame` 循环在 `dirty` 时执行 `bubble.innerHTML = mdToSafeHTML(prepareStreaming(acc))`, 每帧最多一次。
- `prepareStreaming(md)`: 统计 ``` 围栏数, 奇数则末尾补 "\n```"; 其他半截语法 (未闭合 `**`、表格半行) 交给 marked 自然容错, 不特判。
- 流中不跑 hljs; `done`/`error`/`abort`/`close` 四路仍走原 `renderFinal` (完整 parse + highlight)。
- 复杂度: 每帧全量 parse, 不做增量 diff。回答通常 < 10 KB, marked+DOMPurify 单次 < 2 ms。若实测超 16 ms 再考虑只重渲染最后一个 block (YAGNI, 不预做)。
- 自动滚动: 仅当 `followBottom === true` 时滚到底 (见 §6)。

## 5. 出处处理 (`citations.js`)

纯函数 `splitCitations(md, {show}) → {md, cites: [{kind:'source'|'web', ref, raw}]}`:

- 匹配模式 (全局): `\*\*\[Source:\s*([^\]]+)\]\*\*` 与 `\[Source:\s*([^\]]+)\]`; `\*\*\[Web:\s*([^\]]+)\]\*\*` 与 `\[Web:\s*([^\]]+)\]`。
- `show=false`: 剥除匹配段, 并收敛剥除后留下的多余空格 / 行尾空格 / 空的括号 `()`。
- `show=true`: 替换为 `<span class="cite cite-source">Source: path</span>` 前置换行 (独立一行淡灰 12px 等宽)。该 span 经 DOMPurify 保留 (class 在白名单)。
- 流中半截 (`[Source: dom` 未闭合, 位于文本末尾): 用 `\[(Source|Web):[^\]]*$` 暂时剥掉, 待下一帧闭合再正常处理。
- 底部「来源 (N)」折叠区继续用 SSE `sources` 事件的数据 (与正文引用无关), 样式重做。
- 开关: 设置弹层「显示行内出处 (调试)」→ `prefs.showCitations` (`localStorage: sdtm_ui_prefs`), 切换后对当前会话 `renderMessages()` 重渲染 (无在途生成时才允许切换, 否则禁用开关, 避免重建抹掉在途气泡)。

## 6. 附加 UX (`ui.js`)

- **复制**: AI 回答悬停工具条 [复制 Markdown] [⚑ 标记]; 复制内容 = 存档原文 (含出处)。代码块右上角 [复制] 复制纯代码。`navigator.clipboard` 不可用 (LAN http) 时退回 `execCommand('copy')` 隐藏 textarea。
- **重命名**: 侧栏条目双击 → 行内 input, Enter/blur 提交, Esc 取消; 空则不改。
- **删除两步确认**: 点 ✕ → 按钮变「确认删除」(danger 色) 3 秒, 再点才删; 超时复原。
- **空状态**: 当前会话 0 条消息时显示: 衬线标题「SDTM 知识库助手」+ 一句说明 + 4 张示例问题卡 (点击即填入并发送)。示例:「AE 域中 AESER 与 AESEV 的区别?」「SUPPQUAL 什么情况下使用?」「--DTC 变量的 ISO 8601 部分日期怎么写?」「本研究 ST01 的 VS 域有哪些测试项?」(第 4 张仅联邦开启时显示)。
- **滚动跟随**: `#messages` scroll 监听, 距底 > 80px 置 `followBottom=false` 并显示「↓ 回到底部」浮钮; 点击或用户滚回底部恢复。发送新消息时强制恢复跟随。
- **设置弹层**: 齿轮按钮 → 弹出面板: 模型下拉 (+ 未验证提示) / 检索范围三勾选 / 显示行内出处开关 / 侧栏折叠。控件 id 保持 `model-select / scope-cdisc / scope-study / scope-web / model-warning / scope`, 使既有逻辑零改动。顶栏只显示标题 + 当前所选模型 label。

## 7. 错误 / 边界

- 流中 parse 抛错 (理论上 marked 不抛): try/catch 退回 `textContent`, 不中断流。
- 老存档缺字段: 渲染路径全部 `?? null`/可选链, 与现在一致。
- 剪贴板失败: 工具条按钮短暂显示「复制失败」。
- 重命名/删除在生成中: 允许 (不影响在途流, 因为在途气泡挂在 DOM 上、`c` 引用不变); 但**切换会话**在生成中沿用现状 (不阻止, 在途答案仍会 persist 到原会话)。

## 8. 测试

- `webchat/tests/citations.test.mjs` (`node --test`): 剥除 bold/非 bold 两种; Web 引用; 多处引用; show 模式输出 span; 半截尾部剥除; 无引用文本原样; 剥除后空括号清理。
- `webchat/tests/markdown.test.mjs`: `prepareStreaming` 奇数围栏补全 / 偶数不动。
- `scripts/tests/test_webchat_stream_render.py` (playwright, 未装则 skip, 复用 `test_webchat_cache_browser.py` 骨架): stub `/api/ask_stream` 慢速吐 `## 标题\n- 项` token, 断言流中 (done 前) bubble 含 `<h2>` 与 `<li>`; 断言 `[Source: x]` 默认不在正文 DOM 中, 打开开关后以 `.cite` 出现。
- 既有 `test_webchat_cache_headers.py` / `test_webchat_cache_browser.py` 回归。
- 人工: Chrome 实测截图 (空状态 / 流中 / 完成态 / 设置弹层 / 侧栏折叠), 交用户目视。
- Rule D: 实现与审阅分 agent; 审阅重点 = §1 不变量逐条核对。

## 9. 不做 (YAGNI)

- 深色主题; Preact 等框架; 增量 md diff; 上标角标引用; 会话搜索/导出; 修改后端或 prompt。
