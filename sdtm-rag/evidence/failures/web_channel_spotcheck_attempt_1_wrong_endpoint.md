> ⚠ **失败归档 (规则 B) — 本表无效, 不代表联网通道的质量, 仅留痕不删。**
>
> **输入**: `eval/web_channel_spotcheck.py` (v1) 调 `POST /api/ask`, `json={"question": q, "corpus": "cdisc", "web": True}`。
>
> **技术判定**: `server/router.py::AskRequest` (非流式端点的请求模型) **没有 `web` 字段**,
> pydantic 静默丢弃多传的 `"web": True`; `ask()` 端点本体也从未把 `WEB_TOOL_SPEC` /
> `WebSearcher` 接进 `llm_router.completion(...)` 调用 (对照下面 `/api/ask_stream` 才有
> `tools = [WEB_TOOL_SPEC] if use_web else None`)。也就是说这三题**根本没联网**, 走的是
> 纯 KB 问答, 三行的 `[Web:] 数 = 0` 反映的是这个事实, 不是"联网了但没引用"。
>
> **业务判定**: 第 3 题 `⛔ C101832,C101833` **不是红线破**。`ask()` 端点在这条调用链上
> 从未把 `web_search` 工具传给模型 (见上), 模型结构上不可能调用它、也不可能有真实网页
> 内容进入 `messages`——Rule 9(b) 约束的"网页结果存在时不得凭它产码"这一条件从未触发。
> 那两个码只能来自 `context`(KB 检索结果), 与联网通道无关, 无需人工看原文复核。
>
> **下一 attempt 输入**: 改打 `/api/ask_stream` (SSE), 按 `event:`/`data:` 帧解析
> `token`/`tool_call`/`tool_result`/`done`, 见 `eval/web_channel_spotcheck.py` (v2) 与
> `evidence/checkpoints/web_channel_spotcheck.md`。

---

# 联网通道语义抽检 (规则 A) — v1 (无效, 端点打错)

> 联网答案不可复算, **不进 gold set** —— 本表是它唯一的质量证据。
> ⚠ 机检只能查形状; **第 3、4 列必须人眼逐条判**, 不得由脚本判 PASS。

| # | 问题 | 机检: CT 码 | 机检: [Web:] 数 | 机检: [Source:] 数 | 人判: 标注是否规矩 | 人判: 借鉴是否标推测 |
|---|---|---|---|---|---|---|
| 1 | How do other teams handle EDC fields that don't map to any s | ✅ 无 | 0 | 11 | ⬜ 待判 | ⬜ 待判 |
| 2 | What do practitioners say about overusing SUPPQUAL versus cr | ✅ 无 | 0 | 23 | ⬜ 待判 | ⬜ 待判 |
| 3 | How is Findings About (FA) used in practice versus a custom  | ⛔ C101832,C101833 | 0 | 26 | ⬜ 待判 | ⬜ 待判 |

## 判读规则

- **CT 码列出现任何码 = 立即查**: Rule 9(b) 禁止从网页产出 `Cxxxxx`。
  码若能在 `knowledge_base/` 找到且答案标的是 `[Source:]`, 属正常 (KB 来源);
  标 `[Web:]` 却带码 = **红线破**。
- `[Web:]` 数为 0 而问题明显需要业界实践 ⇒ 可能没真联网, 查 `web_status`。
- 人判两列必须逐条看答案原文, 不看就填 = 抽检失效 (规则 A 的意义就在这)。
