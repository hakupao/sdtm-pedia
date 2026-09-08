# Vendored frontend libs (无外网 CDN, 运行时本地 serve)

- marked@12.0.2 — markdown 渲染
- dompurify@3.1.6 — 净化 LLM 输出 (XSS 防护)
- highlight.js@11.9.0 (cdn-assets) + github 主题 — 代码高亮

下载源 jsDelivr (**仅下载时**联网; 运行时全部由 FastAPI `/static` 本地 serve, 不依赖外网)。版本固定。

升级: 重下对应版本并复测。下载 URL (注意 highlight.js 的 npm 包名是 `@highlightjs/cdn-assets`, **无点**):

```bash
curl -fsSL https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js -o marked.min.js
curl -fsSL https://cdn.jsdelivr.net/npm/dompurify@3.1.6/dist/purify.min.js -o purify.min.js
curl -fsSL https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11.9.0/highlight.min.js -o highlight.min.js
curl -fsSL https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11.9.0/styles/github.min.css -o highlight.github.min.css
```

---

## 模块结构 (2026-09 重构)

`../app.js` (入口, `type=module`) → `../js/{store,citations,markdown,render,stream,flag,ui}.js`; `index.html` + `style.css` 同期重写 (design tokens)。本目录的三个 vendored 库**零改动**。

- 单测: `node --test 'webchat/tests/*.test.mjs'` (27 条; ⚠ 目录形式在 node 26 会失败, 必须用 glob)。
- e2e: `scripts/tests/test_webchat_stream_render.py` (playwright, 未装则可见地 skip)。
- 护栏测试: `scripts/tests/test_sse_contract.py` / `test_model_switching.py` (+ `fixtures/flag_attribution_probe.mjs`) 已从 `app.js` 改读 `js/*.js` —— 再拆模块时**这三处的锚点要一起改**, 否则闸会一路绿着退化成什么也没钉。
- 正文 `[Source: path]` 由 `citations.js` 在**渲染层**剥除 (设置 → 显示行内出处 可开); 存档与 ⚑ 上报存原文。

收口证据: `sdtm-rag/evidence/checkpoints/chat_ui_redesign_2026-09.md`。
