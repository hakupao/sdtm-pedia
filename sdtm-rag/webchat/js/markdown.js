// Markdown 渲染管线。marked / DOMPurify / hljs 是 vendor 脚本挂在 window 上的全局,
// 这里只在函数体内引用 —— 让 prepareStreaming 能在 node 里单测。
import { splitCitations } from "./citations.js";

const RE_FENCE = /^ {0,3}(`{3,}|~{3,})/gm;

// 流中未闭合的代码围栏会把后文全吞进 <pre>, 一帧一帧看就是"整段正文变成代码"。
// 奇数个围栏 ⇒ 补一个与最后一个开栏同记号的闭合 (``` 关不掉 ~~~)。
export function prepareStreaming(md) {
  const text = md || "";
  const fences = text.match(RE_FENCE) || [];
  if (fences.length % 2 === 0) return text;
  const last = fences[fences.length - 1].trim();
  return text + "\n" + last;
}

export function mdToSafeHTML(md) {
  return DOMPurify.sanitize(marked.parse(md || ""));
}

// 统一入口: 出处处理 → (流中) 围栏补全 → 解析 → 净化。
export function renderMarkdown(md, { streaming = false, showCitations = false } = {}) {
  const { md: body } = splitCitations(md, { show: showCitations, streaming });
  return mdToSafeHTML(streaming ? prepareStreaming(body) : body);
}

export function highlightIn(el) {
  el.querySelectorAll("pre code").forEach((b) => hljs.highlightElement(b));
}
