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
