# Chat UI 重构收口 — 模块化 + 流式 Markdown + 出处隐藏 (2026-09-08)

> 分支 `feat/chat-ui-redesign` (base `ab24bad`, HEAD `9b05c98`) · 16 commit
> spec `docs/superpowers/specs/2026-09-08-chat-ui-redesign-design.md` · plan `docs/superpowers/plans/2026-09-08-chat-ui-redesign.md`
> 台账 (逐条裁定 / 延后项 / 审阅结论) `.superpowers/sdd/2026-09-08-chat-ui-redesign/progress.md`

## 1. 目标与范围

用户点名两个体验缺陷: ① 流式输出期间只 `textContent` 追加, 屏上是裸 Markdown 语法, `done` 后才整体渲染; ② 正文里随处可见 `**[Source: path]**`, 与正文混排干扰阅读。

范围只有前端 `sdtm-rag/webchat/`: 654 行单体 `app.js` 拆成入口 + 7 个模块, `index.html` 43→76 行、`style.css` 67→154 行重写 (design tokens), 加 4 个 `node --test` 单测文件。**后端 SSE 契约、prompt、localStorage 存档格式一律不动**; 唯一的 `server/` 改动是限流豁免 (见 §7 裁定 8), 它是本次拆模块**引入的生产 blocker** 的修复, 不是功能改动。

## 2. 改动清单 (commit → 文件)

| commit | 文件 | 内容 |
|---|---|---|
| `c0be8fa` | `js/citations.js` + 测试 | 出处抽取/剥除纯函数 |
| `5c32fdb` | `js/markdown.js` + 测试 | 流式围栏补全 + `renderMarkdown` 管线 (出处→围栏→marked→DOMPurify) |
| `037c674` | `js/store.js` + 测试 | 会话存储搬家 + `renameConversation` + prefs (`sdtm_ui_prefs`) |
| `6877bab` | `js/stream.js` + 测试 | SSE 客户端搬家, payload 由调用方构造 (逻辑零改动) |
| `23b146c` | `js/citations.js` + 测试 | 逐行跳过围栏 + 局部空白整理 + `RE_FULL` 拆 bold/裸形 (审阅 I1/I2) |
| `6bec8b6` | `js/citations.js` + 测试 | 闭合围栏须同字符且不短于开启 (CommonMark) + 哨兵改 PUA |
| `be121d4` | `js/ui.js` | 复制/两步删除/行内重命名/滚动跟随/设置弹层/侧栏折叠 原语 |
| `cb5eac4` | `js/render.js` + `js/flag.js` | 消息渲染层重做 (turn/chips/tools/空状态), 护栏函数逐字搬家 |
| `b99815d` | `index.html` + `style.css` | design tokens / 设置弹层 / 空状态 / 工具条 |
| `dbf26be` | `js/render.js` `js/ui.js` `style.css` | 双击重命名不与单击切换竞争 + 三条廉价 Minor (审阅) |
| `4d23fa8` | `app.js` | 重写: 模块化入口 + rAF 节流流式渲染 + 出处开关 + 弹层接线 |
| `f64ba41` | `server/auth.py` + 新测试 | 限流豁免 `/static/` 前缀与 `/` (生产 429 blocker) |
| `f396eef` | `scripts/tests/{test_sse_contract,test_model_switching}.py` + 探针 | 护栏测试从 `app.js` 改读 `js/*.js` |
| `ac388d6` | `scripts/tests/test_webchat_stream_render.py` | playwright 闸 (流中 md / 出处开关 / 老存档) |
| `a2996a2` | plan 文档 | `node --test` 命令改 glob 形式 |
| `9b05c98` | `app.js` `style.css` `js/citations.js` + 4 测试文件 | 终审修复波 7 项 |

`webchat/vendor/` 三个库零改动 (`git log ab24bad..HEAD -- sdtm-rag/webchat/vendor` 为空)。

## 3. 不变量核对表 (spec §1 逐条)

行号取自 HEAD `9b05c98`, 由本文作者当场 grep 核对。

| spec §1 不变量 | 现在在哪 | 验证证据 |
|---|---|---|
| SSE 事件契约 + `/api/ask_stream` payload 字段不变 | `js/stream.js:13`(handlers) / `:42-43`(done·error) | 重定向后的 `test_sse_contract.py::test_frontend_knows_every_event_the_backend_emits` 改扫 `js/stream.js`, 正则与 `>= 6` 下限一字未动 (task-8b-report §1) |
| localStorage `sdtm_chat_v1` / `sdtm_model` 结构语义不变; 老存档可读可渲染 | `js/store.js:2` / `app.js:191,199` | playwright `test_webchat_stream_render.py` 第 2 条真跑老存档; Task 8 冒烟第 7 项刷新真实存档 (`07_history_reload.png`) |
| 存档存原始 md (含 `[Source:`), 剥除只在渲染层; ⚑ 上报也是原文 | 剥除在 `js/citations.js`, 落盘在 `js/store.js` | Task 8 冒烟实测: 关掉开关后正文 21 条 `Source:` 归 0, 而 localStorage `content` 仍含 `[Source:` (task-8-report §4 额外覆盖) |
| `modelBadgeText` 三态 + `fellBack === true` 全等 + `Array.isArray`, ⛔ 不加 `filter(Boolean)` | `js/render.js:161,171,175` | Task 6 的 `GUARDS-IDENTICAL` diff 闸 (`diff <(app.js 老函数体) <(render.js 新函数体 去 export)` 三条同时为空, task-5-7-report §Task 6); 另有 `test_model_switching.py::test_badge_text_reads_the_fell_back_field` 改读 `RENDER_JS` 同一切片锚点 |
| `refreshModelBadgeLabels` 原地补字, 不重建 `#messages` | `js/render.js:211` (调用点 `app.js:203`) | 同一条 `GUARDS-IDENTICAL` diff 闸; 终审 rev-final 另行追踪了 app.js 全部 9 处 `renderMessages`/`paintAll` 调用点, 结论见 final-review.md §Strengths 第 2 条 |
| `flagModelName` 回退归因逻辑 | `js/flag.js:50-67` | 单独 diff, **差异只有 brief 明写的那一处** (topbar 回退改读 `#topbar-model.dataset.defaultModel`), 14 行注释块逐字一致 (task-5-7-report §Task 6 尾部 diff 输出) |
| `streamAsk` terminal / onClose / onAbort 三路 | `js/stream.js:28,35,58,62,66` | `refactor(webchat)` commit `6877bab` 自述逻辑零改动; final-review.md §Strengths 第 1 条逐条点名核实 |
| `save()` QuotaExceeded 逐出 | `js/store.js:26` | 修复波新增 `store.test.mjs` 逐出测试, 并做变异验证: 拆掉逐出循环后该条转红 (`actual: 3 expected: 2`, fixwave-report §变异证据 item 5) |
| IME `isComposing \|\| keyCode===229` | `app.js:219-220` (composer) + `js/ui.js:56` (行内重命名) | final-review.md §Strengths 第 1 条点名两处均在 |
| `renderWebStatus` 六态 / `onToolResultUI` 六态文案 | `js/render.js:319` / `:294` | `renderWebStatus` 进 `GUARDS-IDENTICAL` 闸 (对 `holder`→`turn` 改名做等价替换后比对); `onToolResultUI` 文案表由 `test_sse_contract.py::test_frontend_covers_every_tool_result_status` 从 `render.js` 抽取比对, 后端矩阵侧一行未改 |
| `selectedCorpus` 四值映射; 联邦关时 scope 隐藏; 下拉为空时省略 `model` | `js/ui.js:109` / `app.js:178` / `js/stream.js:22` | `js/stream.js:16-22` 保留了原裁定注释;「省略 vs 显式传 default」的理由逐字搬家 |
| 无外网依赖: 系统字体栈, 不新增 vendored 库 | `style.css:7-9` | `--font-serif/sans/mono` 全系统栈; vendor 目录零 commit (见 §2 末) |
| `test_webchat_cache_*.py` 必须继续通过 | — | 全量回归里 `test_webchat_cache_headers.py` 17 条 + `test_webchat_cache_browser.py` 真浏览器条目全绿 (§4) |

## 4. 测试与命令

全部命令工作目录 `sdtm-rag/`, 跑在 HEAD `9b05c98`。

```bash
node --test 'webchat/tests/*.test.mjs'
#  ℹ tests 27  ℹ pass 27  ℹ fail 0  ℹ skipped 0
```

27 = citations 15 + store 6 + markdown 5 + stream 1 (逐文件单跑核过)。⚠ 目录形式 `node --test webchat/tests/` 在 node 26 会失败, 见裁定 2。

```bash
.venv/bin/python -m pytest scripts/tests/ -q -x --ignore=scripts/tests/test_build_neo4j.py 2>&1 | tail -3
```

本仓 `pyproject.toml` 的 `addopts = "-ra -q"` 叠加命令行 `-q` 会吞掉计数行, 上面这条的 tail 只剩第三方 DeprecationWarning。加 `-o addopts=""` 后计数可见:

```
2051 passed in 49.54s        # exit 0, 零 F / 零 E
```

修复波报告里那条 webchat 相关子集 (`test_sse_contract` + `test_model_switching` + `test_webchat_stream_render` + `test_webchat_cache_headers` + `test_rate_limit_static_exempt`) 单跑是 **109 passed** (fixwave-report §验证)。

**playwright 是真跑的, 不是 skip**: `test_webchat_stream_render.py` 2 条与 `test_webchat_cache_browser.py` 一并计入上面的 2051。装法 (Task 9 实测, `uv.lock`/`pyproject.toml` md5 装前装后相同):

```bash
uv pip install --python .venv/bin/python playwright
.venv/bin/playwright install chromium
```

未装 playwright 时 `pytest.importorskip` 让整个文件**可见地 skip** (显示 `s`), 装了 wheel 却没浏览器则在 `_launch` 里 skip。⚠ 因此 CI / 新克隆默认拿不到这条闸的保护 (延后项, §8)。

## 5. 浏览器实测

截图在 `.superpowers/sdd/2026-09-08-chat-ui-redesign/screens/`。冒烟跑在**同一份工作树、同一份 server 代码**另起的 `:8100` 实例上 (`SDTM_RAG_RATE_LIMIT_ENABLED=false`), 因为当时生产 `:8000` 被 429 挡着打不开; 冒烟结束该实例已 `pkill`。

| 文件 | 一句话 |
|---|---|
| `00_BLOCKER_prod_429.png` | 生产 `:8000` 只渲染外壳 — 2-3 个 `/static/js/*.js` 吃 429 |
| `01_empty.png` | 空状态: 衬线标题 + 4 张示例卡 (联邦开 ⇒ 含 ST01 那张) |
| `02_streaming.png` | 流中已是渲染后的表格/标题/列表 + 红色「停止」— 用户缺陷 ① 的正面证据 |
| `03_done.png` | 完成态 meta chips (判定库 + 模型) + 「来源 (15)」折叠 |
| `04_settings_citations_on.png` | 设置弹层 + 行内出处开启后 21 个 `.cite.cite-source` 独行淡灰等宽 |
| `05_sidebar_rename_delete.png` | 双击重命名结果 + ✕ 两步确认的 armed 态 (3.3 s 后实测自动复原) |
| `06_to_bottom.png` | 上滚 2765 px 后「↓ 回到底部」出现, 点击回底且跟随恢复 |
| `07_history_reload.png` | 刷新后老存档: 4 表格 / 9 标题 / 15 来源 / 代码块复制 / 回退琥珀徽章 / 联网警告条 |
| `08_prod_after_reload.png` | 用户 `launchctl kickstart` 重载生产后, `:8000` 的空状态 |
| `console.txt` | 两个 origin 的完整 console: `:8100` **零应用报错**, 只有既存 favicon 404 与合成存档触发的 hljs `sas` WARN |

⚠ `08_prod_after_reload.png` 与 `01_empty.png` **字节完全相同** (md5 `e8e3bf06b9f63c2c9d650db34bfdbfe1`) —— 空状态在两个 origin 上像素一致, 所以这张图本身不能证明它拍自 `:8000`。「生产重载后恢复」的独立证据是台账记的 health 200 + **42/42 static 请求 200 (3 轮冷加载), 429 消失**。

冒烟共 8 项全 PASS, 逐项证据见 `task-8-report.md` §4; 额外覆盖了 abort / retry / 存档保真 / Esc 关弹层 / 跨会话切换。付费提问全程只发 2 次; ⚑ 只打开后取消, 未写 `dogfood_failures.md`。

## 6. Rule D 审阅链

实现与审阅全程分 agent、分 session (规则 D)。

| 单元 | 实现 | 审阅 | 结论 | 修复轮 |
|---|---|---|---|---|
| Task 1-4 (citations/markdown/store/stream) | impl-t1-4 (opus) | rev-t1-4 (opus) | PASS-WITH-FIXES, Important×2 (tidy 全文改写破坏代码块; `RE_FULL` 吞配对 `**` 与链接) | 2 轮 (r1 opus 复审又抓出围栏长度; r2 sonnet 复审干净) |
| Task 5-7 (ui/render/flag/html/css) | impl-t5-7 (opus) | rev-t5-7 (opus) | PASS-WITH-FIXES, Important×2 (双击与单击竞争; 空状态读 `#scope` 早于 `/api/info`) | 1 轮 (第 2 条按裁定由 Task 8 覆盖) |
| Task 8 (app.js 重写 + 冒烟) | impl-t8 (opus) | rev-t8 (opus) | **Approved, 0 C / 0 I** | — |
| 限流豁免 | impl-ratelimit | rev-ratelimit | **Approved** | — |
| Task 8b (护栏测试重定向) | impl-t8b (opus) | rev-t8b (opus) | **Approved** | — |
| Task 9 (playwright 闸) | impl-t9 | rev-t9 (sonnet) | **Approved, 0 C / 0 I** | — |
| 全分支终审 `ab24bad..ac388d6` | — | rev-final (**fable**) | **Ready to merge with fixes** — 0 Critical / 0 Important / **16 Minor**, 无裁定被推翻 | — |
| 终审修复波 7 项 | impl-fixwave | rerev-final (opus) | **7/7 ADDRESSED, 无新破坏** | — |

终审是自己在 checkout 上复跑的 (24 node / 29+30 pytest), 另做了 24 种真实模型输出形状的 `splitCitations` 探针, 以及 19 KB 表格答案的 `marked.parse` 计时 (暖 1.4 ms / 冷 18 ms) —— 「不做增量 md diff」的 YAGNI 裁定由此得到实测支持。

## 7. 裁定清单

台账里全部 9 条 `Ruling:`, 逐条抄录。

| 裁定 | 理由 | 代价 |
|---|---|---|
| 用 feature branch 而非独立 worktree | launchd 生产服务 (localhost:8000) 从主工作树现读 `webchat/`, Task 8 浏览器冒烟必须在主工作树跑; 分支已满足"不在 main 上开工" | 若同时有别的 session 改主工作树会互相干扰 (本 session 独占) |
| 计划中所有 `node --test webchat/tests/` 改为 `node --test 'webchat/tests/*.test.mjs'` | 目录形式在 node 26 会把目录当模块加载而失败 | 无 (纯命令形式) |
| 各模块首行 `// webchat/js/x.js` 路径定位注释不写入文件 | 仓库无此惯例; Tasks 5-8 同样省略 | 无 |
| I1/I2 是真缺陷, **覆盖计划文本** — 逐行处理跳过围栏; 剥除用哨兵只做局部空白整理 (仅当确有 cite 被剥除); `RE_FULL` 拆成 bold 完整形 \| 裸形 (后不跟 `(`) | 计划的全局 tidy 会把代码块里的 `f()` 改成 `f`、吃掉硬换行 | `citations.js` 比计划复杂 ~20 行 |
| I1 修 `render.js` (`e.detail>1` 时不 onSelect); I2 不另修 | I2 已由 Task 8 计划代码覆盖 (`loadModelName` 末尾空会话重画 emptyState), Task 8 审阅时核 | 无 |
| 顺带修三条廉价 Minor: `armDelete` confirm 时 `clearTimeout`; `:has()` 拆独立规则; `renderModelBadge`/`setSources` 在无 `.turn-meta` 时 no-op | `:has()` 不拆则整条 hover 规则被不支持的浏览器丢弃; no-op 是恢复旧 role 守卫语义 | (未记) |
| `setSources` 的 `.sources-slot` 解引用**不加**守卫 | 调用点仅 assistant turn (`messageEl` 内 + `app.js` `onSources` 的 holder 是 assistant), 路径不可达, 与"不为不可达路径写防御"惯例一致 | 若未来有人对 user turn 调 `setSources` 会抛 (可见失败, 非静默) |
| **突破"不改 `server/`"约束** — `RateLimitMiddleware` 加 `exempt_prefixes=("/static/",)` 且 `"/"` 入 exempt | 限流保护的是 LLM/API, 静态壳子不该计数 (调 BURST 只是推迟); 附 TDD 测试; 生产服务重载需用户在终端执行 | 静态路径失去限流 (小文件、本地盘、无 LLM 成本) |
| 新增 Task 8b「护栏测试重定向到模块」 | 保留每条测试意图与判别力 (不削弱断言), 只改源文件定位/加载方式; `app.js` 已是 ESM, node 直跑的用例改为 import 模块 | 测试文件改动量中等; 若某测试的意图在模块化后不可达需逐条说明 |

## 8. 已知限制与延后项

**spec 偏离 (终审确认为有意, 记录在案)**
- spec §6 说侧栏折叠开关在设置面板, 实际做在**侧栏头部**; 终审判 Defer (brief 有意)。
- spec §3 说联网状态做成 meta chip, 实际留在 `web-panel` —— 被「`renderWebStatus` 逐字保留」这条护栏所迫。

**功能/交互 (未修)**
- `renderMessages` 的 `onRetry` 是死接口 ⇒ 重渲染会丢重试按钮 (与 main 同, parity)。
- `busy` 置位在 `try` 外 (parity)。
- 删在途会话已在修复波补 `stop()`, 但用的是 `store.currentId` 代理「在途会话」: 用户中途切走再删原会话则不 stop (rerev-final 记, parity 级)。
- 流中 rAF 路径只有**间接覆盖**: `route.fulfill` 一次性交付 body, 卡不住流; 流中行为由 `page.evaluate` 直调模块证明。要真堵这一格需要一个会在帧间 `await asyncio.sleep` 的真 SSE 测试端点。
- `prepareStreaming` 漏检列表内缩进围栏 / `~~~` / 4 反引号 (mid-stream 视觉, marked 在容器末尾会自行闭合)。
- 出处剥除的残留形状: `a ((cite))` → `a ()`; `*[cite]*` → `**`; 4 空格缩进代码块里的 `[Source:` 仍被剥; `**[Source: a] Severity**` 首部剥除后左侧 flanking 失效; `RE_FULL` 大小写敏感 (prompt 强制大写, 小写形态被放过 = 更安全的失败方向)。剥除同样会作用于代码块**外**任何字面 `[Source:` 字样, 极罕见。

**工程 / 安全 / 可访问性**
- `auth.py` `_is_exempt` 是裸 `startswith`: `/static/../api/x` 名义上豁免, 但 Starlette 路由到 `/static` 挂载后被 `StaticFiles` 规范化 404 挡住, 浏览器也会先规范化 ⇒ 无实际绕过。可选硬化 = 先拒含 `/../` 的路径。
- **`/static/tests/*.mjs` 经 StaticFiles 可取** (无机密, 但是 dev 文件) —— ⚠ **阶段 3 内网 go-live 前必须从静态挂载里排除**。
- `playwright` 只进了 `.venv/`, 没进 `pyproject.toml` dev 组 ⇒ CI / 新克隆默认 skip 这两个文件。
- a11y: 设置弹层无 `role="dialog"` / 焦点管理; `#messages` 无 `aria-live`。
- CSS off-token 颜色 (`.corpus-badge` / `.md pre` / `.web-panel` 边框 / `.chip.unverified` 边框); `.chip.model-meta` 无专属样式; `#to-bottom` 在输入框顶到 200px 时与 composer 重叠。
- `store.test.mjs` 顺序依赖 (同文件串行执行, 当前安全); `streamAsk` 三路终止无直接 node 单测 (逐字搬家 + 探针间接覆盖)。
- 探针 `flag_attribution_probe.mjs` 跨场景 `Object.assign(globalThis, g)` 不回收 (tmp 清理已在修复波进 `finally`)。
- 既存无关问题: `index.html` 无 `<link rel="icon">` ⇒ favicon 404; 打包的 highlight.js 无 SAS 语法 ⇒ ```sas 围栏降级为不高亮 (仍渲染、仍有复制钮)。

**已在修复波关闭的 7 项** (不再是延后项): 折叠侧栏出 tab 序 · 删末会话补 `newConversation` · 删在途会话先 `stop()` · 出处剥除 CJK 标点粘合 · `save()` 逐出测试 · `_frontend_sources` 下限 6→8 + docstring 理由改正 · 探针 tmp 进 `finally`。

## 9. 复跑指引

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# 单测 (27)
node --test 'webchat/tests/*.test.mjs'

# 全量回归 (2051 passed; 去掉 -o 那段则计数行会被 addopts 吞掉)
.venv/bin/python -m pytest scripts/tests/ -q -x \
  --ignore=scripts/tests/test_build_neo4j.py -o addopts="" -p no:warnings

# 只跑 webchat 相关子集 (109)
.venv/bin/python -m pytest scripts/tests/test_sse_contract.py \
  scripts/tests/test_model_switching.py scripts/tests/test_webchat_stream_render.py \
  scripts/tests/test_webchat_cache_headers.py scripts/tests/test_rate_limit_static_exempt.py -q

# 护栏逐字闸 (Task 6 的 GUARDS-IDENTICAL, 拿 base 的 app.js 当参照物)
git show ab24bad:sdtm-rag/webchat/app.js > /tmp/app_base.js
diff <(sed -n '/^function modelBadgeText/,/^}/p' /tmp/app_base.js) \
     <(sed -n '/^export function modelBadgeText/,/^}/p' webchat/js/render.js | sed 's/^export //') \
  && echo GUARDS-IDENTICAL

# 生产 (launchd, localhost:8000): 改完 webchat/ 后 StaticFiles 从工作树现读, 无需重启;
# 改 server/ 或 config 才需要 launchctl kickstart -k (用户在终端执行)
```
