// 正文出处 `**[Source: path]**` / `[Web: url]` 的抽取与剥除。
// prompt (server/rag.py) 强制模型写这些标记, 是反捏造设计的一部分, 前端**不改 prompt**,
// 只在渲染层处理; 存档与 ⚑ 上报永远是原文 (spec §1)。
//
// 两条硬约束 (Rule D 审阅 I1/I2), 改这个文件前先读:
// 1. 没剥掉任何标记的行**逐字节原样返回**。空白整理只在真删了东西的行上跑, 而且只碰删除点
//    周围, 全文级重写一律不做 —— 否则代码块里的 `read_xpt()` 会被吃成 `read_xpt`, 对齐的
//    空格会塌, 行尾两空格的 markdown 硬换行会消失。
// 2. 围栏代码块内的行完全不碰 —— 里面的 `[Source: ...]` 是代码, 不是出处。
const RE_FENCE_LINE = /^ {0,3}(`{3,}|~{3,})/;
// 两种形态分开写, 绝不用 `\*{0,2}`: 那会把成对 bold 的后半截单边吃掉
// (`**Severity [Source: a.md]** rest` → `**Severity rest`, 星号失衡)。
// 裸形末尾的 `(?!\()` 用来放过普通链接 `[Source: guide](http://x/y)`。
const RE_FULL = /\*\*\[(Source|Web):\s*([^\]\n]*)\]\*\*|\[(Source|Web):\s*([^\]\n]*)\](?!\()/g;
// 流中尾部半截: `[`, `[S`, `**[Sour`, `[Source: dom` ... 都先藏起来, 下一帧闭合后走 RE_FULL。
// `[Sx` 这类不是出处前缀的不动 —— 前缀枚举比宽松匹配多几个字符, 但不会误吞正文里的 `[`。
const RE_TAIL = /\*{0,2}\[(?:S|So|Sou|Sour|Sourc|Source|W|We|Web)?(?::[^\]]*)?$/;

// 删除点占位符 (下面注释里记作 ␀), 只在一行的处理过程中存活, 返回前一定被清干净。
// 用私用区 (PUA) 码位而不是 NUL: NUL 在正文里虽然罕见但是合法字符, 拿它当哨兵会把作者原有的
// NUL 连同左边的空格一起吃掉; PUA 码位不会出现在真实 markdown 里。
const SENT = "\uE000";
const RE_EMPTY_PARENS = /\(\s*\uE000(?:\s*\uE000)*\s*\)/g; // `(␀)`: 括号本身也是残渣
// 连排出处之间的分隔符也是残渣: `见 ␀、␀。` 里的 `、` 是用来连接两条出处的, 两条都删了以后
// 它就成了孤儿顿号。收成一个哨兵 (吃掉前一个 + 分隔符, 留后一个), 三条以上靠 /g 逐对收干净。
const RE_JOIN_SEP = /\uE000[ \t]*[、,][ \t]*(?=\uE000)/g;
// `Text ␀.` → `Text.`; 中文正文里句读是全角的, 只列 ASCII 那半边等于对中文答案不设防
// (`见 ␀。` 会留下 `见 。`)。收尾类的右半闭合符 (`）」』`) 同理。
const RE_GLUE_PUNCT = /[ \t]*\uE000[ \t]*(?=[.,;:!?。，、；：！？）」』])/g;
const RE_EOL = /[ \t]*\uE000[ \t]*$/g;                     // 行尾: 连空格一起去
const RE_MID = /(^|[ \t])\uE000[ \t]+/g;                   // 词 ␀ 词: 留一个空格
const RE_LEFT = /[ \t]*\uE000/g;                           // 右侧无空白的残留: 左空格一并去,
                                                           // 让 `**` 这类闭合记号贴回词尾

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

// 只在删除点周围收口, 顺序固定: 连排分隔 → 空括号 → 粘标点 → 行尾 → 行中 → 残留。
// 连排分隔必须排在空括号前面: `(␀、␀)` 先收成 `(␀)`, 空括号那条才认得出来。
function tidyLocal(line) {
  return line
    .replace(RE_JOIN_SEP, "")
    .replace(RE_EMPTY_PARENS, SENT)
    .replace(RE_GLUE_PUNCT, "")
    .replace(RE_EOL, "")
    .replace(RE_MID, "$1")
    .replace(RE_LEFT, "");
}

// 半截标记连同它前面的空格一起藏起来 —— 那段空白属于被删内容, 下一帧会随标记一起回来。
function stripTail(line) {
  const m = line.match(RE_TAIL);
  if (!m) return line;
  return line.slice(0, m.index).replace(/[ \t]+$/, "");
}

function replaceCites(line, cites, show) {
  let stripped = false;
  const text = line.replace(RE_FULL, (raw, boldKind, boldRef, bareKind, bareRef) => {
    const kind = boldKind || bareKind;
    const k = kind.toLowerCase();
    const r = (boldRef !== undefined ? boldRef : bareRef).trim();
    cites.push({ kind: k, ref: r, raw });
    if (show) return `<span class="cite cite-${k}">${kind}: ${escapeHtml(r)}</span>`;
    stripped = true;
    return SENT;
  });
  return stripped ? tidyLocal(text) : text; // 没删东西 ⇒ 原样, 一个字节都不动
}

export function splitCitations(md, { show = false, streaming = false } = {}) {
  const cites = [];
  const lines = (md || "").split("\n");
  let fence = null; // 开启中的围栏 {char, len}; null = 不在围栏里
  const out = lines.map((line, i) => {
    const f = line.match(RE_FENCE_LINE);
    if (f) {
      const run = f[1];
      // CommonMark: 闭合围栏必须是同一个字符, 且不短于开启围栏。只比字符不比长度的话,
      // ````markdown 里嵌的 ```py 会把外层关掉, 嵌套代码块的后半截就被当成正文剥了出处。
      // 关不掉的围栏行 (异族记号 / 更短) 只是内容, 原样返回。
      if (fence === null) fence = { char: run[0], len: run.length };
      else if (run[0] === fence.char && run.length >= fence.len) fence = null;
      return line;
    }
    if (fence !== null) return line;
    const text = streaming && i === lines.length - 1 ? stripTail(line) : line;
    return replaceCites(text, cites, show);
  });
  return { md: out.join("\n"), cites };
}
