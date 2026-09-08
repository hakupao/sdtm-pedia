// 正文出处 `**[Source: path]**` / `[Web: url]` 的抽取与剥除。
// prompt (server/rag.py) 强制模型写这些标记, 是反捏造设计的一部分, 前端**不改 prompt**,
// 只在渲染层处理; 存档与 ⚑ 上报永远是原文 (spec §1)。
const RE_FULL = /\*{0,2}\[(Source|Web):\s*([^\]]*)\]\*{0,2}/g;
// 流中尾部半截: `[`, `[S`, `**[Sour`, `[Source: dom` ... 都先藏起来, 下一帧闭合后走 RE_FULL。
// `[Sx` 这类不是出处前缀的不动 —— 前缀枚举比宽松匹配多几个字符, 但不会误吞正文里的 `[`。
const RE_TAIL = /\*{0,2}\[(?:S|So|Sou|Sour|Sourc|Source|W|We|Web)?(?::[^\]]*)?$/;

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

// 剥除后的空白整理。只碰"非空白字符之间"的多余空格, 行首缩进 (代码块) 不动。
function tidy(text) {
  return text
    .replace(/\(\s*\)/g, "")
    .replace(/(\S) {2,}(?=\S)/g, "$1 ")
    .replace(/ +([.,;:!?])/g, "$1")
    .replace(/[ \t]+$/gm, "");
}

export function splitCitations(md, { show = false, streaming = false } = {}) {
  let text = md || "";
  if (streaming) text = text.replace(RE_TAIL, "");
  const cites = [];
  text = text.replace(RE_FULL, (raw, kind, ref) => {
    const k = kind.toLowerCase();
    const r = ref.trim();
    cites.push({ kind: k, ref: r, raw });
    if (!show) return "";
    return `<span class="cite cite-${k}">${kind}: ${escapeHtml(r)}</span>`;
  });
  text = tidy(text);
  return { md: text, cites };
}
