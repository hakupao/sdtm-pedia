import test from "node:test";
import assert from "node:assert/strict";
import { splitCitations } from "../js/citations.js";

test("默认剥除 bold 出处并收敛空白", () => {
  const { md, cites } = splitCitations("AETERM is the term. **[Source: domains/AE.md]** Next.");
  assert.equal(md, "AETERM is the term. Next.");
  assert.deepEqual(cites, [{ kind: "source", ref: "domains/AE.md", raw: "**[Source: domains/AE.md]**" }]);
});

test("非 bold 形式与多处出处", () => {
  const { md, cites } = splitCitations("A [Source: x.md] and B [Source: y.md].");
  assert.equal(md, "A and B.");
  assert.deepEqual(cites.map((c) => c.ref), ["x.md", "y.md"]);
});

test("Web 引用同样处理, kind=web", () => {
  const { md, cites } = splitCitations("Practice. **[Web: https://a.b/c (retrieved 2026-09-01)]**");
  assert.equal(md, "Practice.");
  assert.deepEqual(cites, [{ kind: "web", ref: "https://a.b/c (retrieved 2026-09-01)",
                             raw: "**[Web: https://a.b/c (retrieved 2026-09-01)]**" }]);
});

test("剥除后留下的空括号与标点前空格清理", () => {
  const { md } = splitCitations("Use AESEV (**[Source: a.md]**) here , ok.");
  assert.equal(md, "Use AESEV here, ok.");
});

test("show 模式渲染为 span, ref 做 HTML 转义", () => {
  const { md } = splitCitations("Term. [Source: a<b>.md]", { show: true });
  assert.equal(md, 'Term. <span class="cite cite-source">Source: a&lt;b&gt;.md</span>');
});

test("streaming 剥掉尾部半截, 非 streaming 不动", () => {
  assert.equal(splitCitations("Text **[Source: dom", { streaming: true }).md, "Text");
  assert.equal(splitCitations("Text [S", { streaming: true }).md, "Text");
  assert.equal(splitCitations("Text [", { streaming: true }).md, "Text");
  assert.equal(splitCitations("Text [Sx", { streaming: true }).md, "Text [Sx");
  assert.equal(splitCitations("Text **[Source: dom").md, "Text **[Source: dom");
});

test("无出处文本原样返回 (含代码块缩进)", () => {
  const src = "```py\n    x = 1\n```\n\nline  two";
  assert.equal(splitCitations(src).md, src.replace("line  two", "line two"));
  assert.equal(splitCitations("no cite").cites.length, 0);
  assert.equal(splitCitations(null).md, "");
});
