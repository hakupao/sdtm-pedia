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

// 空括号是剥除产生的残渣, 要清; 而 ` , ` 是作者原文里就有的空格, 局部整理不碰它
// (老版本用全局 `/ +([.,;:!?])/` 顺手改掉了 —— 那正是 I1 说的越界重写)。
test("剥除后留下的空括号清掉; 原文既有的标点前空格不动", () => {
  const { md } = splitCitations("Use AESEV (**[Source: a.md]**) here , ok.");
  assert.equal(md, "Use AESEV here , ok.");
});

test("紧跟标点的出处剥除后标点贴回前一个词", () => {
  assert.equal(splitCitations("Term [Source: a.md].").md, "Term.");
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

// I1: 没有出处可剥 ⇒ 一个字节都不许改。围栏里的 `read_xpt()` / 跨行括号 / 对齐空格,
// 以及正文行尾两空格的 markdown 硬换行, 全部原样。
test("无出处文本逐字节原样返回 (围栏 / 空括号 / 对齐空格 / 硬换行)", () => {
  const src = [
    "```py",
    "df = read_xpt()",
    "foo(",
    ")",
    "a    = 1",
    "bb   = 2",
    "```",
    "",
    "line one  ",
    "line two",
    "",
    "散文里的 empty () 和  双空格 也不动",
  ].join("\n");
  assert.equal(splitCitations(src).md, src);
  assert.equal(splitCitations("no cite").cites.length, 0);
  assert.equal(splitCitations(null).md, "");
});

// I1: 围栏内的 `[Source: ...]` 是代码, 不是出处 —— 不剥, 也不进 cites。
test("围栏代码块内的出处标记不剥除, 围栏外的照剥", () => {
  const src = '```\nprint("[Source: a.md]")\n```\n\n外面 [Source: b.md] 要剥。';
  const { md, cites } = splitCitations(src);
  assert.equal(md, '```\nprint("[Source: a.md]")\n```\n\n外面 要剥。');
  assert.deepEqual(cites.map((c) => c.ref), ["b.md"]);
});

// I2: `\*{0,2}` 会把成对 bold 的后半截单边吃掉, 剩下 `**Severity rest` 星号失衡。
test("成对 bold 里的出处: 只剥出处本身, 星号不失衡", () => {
  const { md, cites } = splitCitations("**Severity [Source: a.md]** rest");
  assert.equal(md, "**Severity** rest");
  assert.deepEqual(cites, [{ kind: "source", ref: "a.md", raw: "[Source: a.md]" }]);
});

// I2: 普通 markdown 链接的方括号部分长得像出处, 剥掉会留下孤儿 `(http://x/y)`。
test("普通 markdown 链接不当作出处", () => {
  const src = "see [Source: guide](http://x/y) here";
  const { md, cites } = splitCitations(src);
  assert.equal(md, src);
  assert.equal(cites.length, 0);
});

// 闭合围栏必须同字符且不短于开启围栏 (CommonMark)。只比字符不比长度的话, ```` 里嵌的 ```
// 会把外层关掉, 后半截代码就被当成正文, 里面的出处被剥、还进了 cites。
test("更短的同族围栏关不掉外层围栏, 嵌套代码块整体不动", () => {
  const src = "````markdown\n```py\nx = read_xpt()  [Source: a.md]\n```\n````";
  const { md, cites } = splitCitations(src);
  assert.equal(md, src);
  assert.equal(cites.length, 0);
});

// 哨兵用 PUA 码位而非 NUL: 正文里原有的 NUL 不该被顺手吃掉 (连同它左边的空格)。
test("正文里原有的 NUL 在被剥除的行上存活", () => {
  assert.equal(splitCitations("keep\u0000this [Source: a.md] tail").md, "keep\u0000this tail");
});

// 中文答案里句读是全角的: 老的粘合类只列了 ASCII `[.,;:!?]`, `见 [Source: a]。` 会剥成
// `见 。` (句号前多一个空格)。连排出处之间的顿号/逗号更糟 —— 两条都删完它就成了孤儿。
test("剥除后的全角标点贴回前一个词, 连排出处之间的分隔符一并收掉", () => {
  assert.equal(splitCitations("见 [Source: a]、[Source: b]。").md, "见。");
  assert.equal(splitCitations("见 [Source: a]。下一句").md, "见。下一句");
  assert.equal(splitCitations("A [Source: a], [Source: b].").md, "A.");
});

// 三条以上连排也要收干净 (RE_JOIN_SEP 靠 /g 逐对收), 且 cites 一条不少。
test("三条连排出处收成一处, cites 全数保留", () => {
  const { md, cites } = splitCitations("依据 [Source: a]、[Source: b]、[Source: c]；下一句");
  assert.equal(md, "依据；下一句");
  assert.deepEqual(cites.map((c) => c.ref), ["a", "b", "c"]);
});
