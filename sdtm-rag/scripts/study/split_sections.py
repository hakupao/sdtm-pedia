"""页文本 → 章节树。纯逻辑, 无 IO —— 故可用合成文本完整测试。

**锚点为什么只认二层及更深** (实测依据, 那份 113 页文档):
  二层 `n.m` 104 条, 序列干净单调 (2.1…2.7 | 3.1…3.10 | 4.1 4.2 | 5.1…);
  顶层 `^\\d+\\s` 50 条里混入正文数字 (实测出现 608), 非递减比例仅 38/49。
  ⇒ 顶层不可靠, 不作切分点。顶层归属由二层编号的父号推出, 不另外识别。

**本模块提供两把闸, 参照物都在生成器之外**:
  1. check_numbering  —— 参照物是文档自身的编号序列;
  2. assert_partition_complete —— 参照物是原始页文本。
"""
from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass

# 标题行: 行首最多 8 空格 + `n.m`(可更深) + 可选点 + 空白 + 非空白; 整行短。
_ANCHOR = re.compile(r"^[ \t]{0,8}(\d+(?:\.\d+){1,3})\.?[ \t]+(\S.*)$")
_MAX_HEADING_LEN = 60
# 标题不是句子 ⇒ 不含句末句点。正文里「6.4 項に…する。」这类以节号开头的引用句
# 会满足上面的正则, 实测在那份 113 页文档里制造了 2 个假锚点 (p66/p67, 落在第 8
# 章正文区里冒出 6.4, 顺带触发编号闸 3 条违规)。判别器用「含 。」而**不用长度**:
# 实测真标题最长 53 字符, 比那两条假锚点 (45/40) 还长, 长度阈值必然误伤真标题;
# 而「含 。」在 113 个锚点上命中 2 条、正好是那 2 条、零误伤。
_SENTENCE_END = "。"

# 目录页形态判据 —— **必须形态判定, 不许硬编码页号**: 页号写死后换一份 PDF 就会
# 静默排除掉真实正文, 而闸照样绿。两条判据取合取:
#   ① 编号行 >= _TOC_MIN_NUMBERED   ② 点线行 >= _TOC_MIN_DOT_LEADER
# 实测那份 113 页文档: 全文**只有 p11-16 这 6 页**满足 ①(正文页最多 2 条编号行),
# 且这 6 页各有 25-46 条点线行, 而 107 个正文页点线行**恒为 0** —— 两条各自都已能
# 分开, 合取是为了让"某页恰好排版成多列数字表"也不会被误判成目录。
_TOC_MIN_NUMBERED = 8
_TOC_MIN_DOT_LEADER = 3
_DOT_LEADER = re.compile(r"\.{10,}|・{10,}|…{3,}")


def _is_heading(line: str) -> bool:
    """锚点判定的单一入口 —— find_anchors 与 split_sections 必须用同一套口径,
    否则两者会在真实文档上给出不同的节数 (而两把闸都不查这种不一致)。"""
    stripped = line.strip()
    if _ANCHOR.match(line) is None:
        return False
    return len(stripped) <= _MAX_HEADING_LEN and _SENTENCE_END not in stripped


@dataclass(frozen=True)
class Section:
    number: str
    level: int
    heading_line: str
    body: str
    page_start: int
    page_end: int
    # 二次切分 (subdivide_oversized) 的产物编号; 未切分的节恒为 1/1。
    part: int = 1
    parts_total: int = 1


def find_anchors(pages: list[str]) -> list[tuple[int, int, str, str]]:
    """返回 (页码 1-based, 该页内行号 0-based, 编号, 整行原文)。"""
    out: list[tuple[int, int, str, str]] = []
    for pi, text in enumerate(pages, start=1):
        for li, line in enumerate(text.splitlines()):
            if _is_heading(line):
                m = _ANCHOR.match(line)
                assert m is not None  # _is_heading 已保证匹配
                out.append((pi, li, m.group(1), line))
    return out


def _flat(pages: list[str]) -> tuple[list[str], list[int]]:
    """展平成全局行列表, 并给出每行所属页码。切分在展平后的行序上做,
    这样跨页的一节能自然合并, 而页码范围仍可回算。"""
    lines: list[str] = []
    owner: list[int] = []
    for pi, text in enumerate(pages, start=1):
        for line in text.splitlines(keepends=True):
            lines.append(line)
            owner.append(pi)
    return lines, owner


def split_sections(pages: list[str]) -> list[Section]:
    lines, owner = _flat(pages)
    idx: list[tuple[int, str, str]] = []          # (全局行号, 编号, 整行)
    for gi, line in enumerate(lines):
        bare = line.rstrip("\n")
        if _is_heading(bare):
            m = _ANCHOR.match(bare)
            assert m is not None
            idx.append((gi, m.group(1), bare))
    sections: list[Section] = []
    for k, (gi, number, heading) in enumerate(idx):
        end = idx[k + 1][0] if k + 1 < len(idx) else len(lines)
        body = "".join(lines[gi:end])
        sections.append(Section(
            number=number,
            level=number.count(".") + 1,
            heading_line=heading,
            body=body,
            page_start=owner[gi],
            page_end=owner[end - 1] if end > gi else owner[gi],
        ))
    return sections


def subdivide_oversized(
    pages: list[str],
    sections: list[Section],
    max_tokens: int,
    count_tokens: Callable[[str], int],
) -> list[Section]:
    """把超过 max_tokens 的节按行切成多份, 正文逐字保留, 页码逐份重算。

    **为什么必须有这一层**: embedding 模型 (text-embedding-3-small) 硬上限 8191
    token, `scripts.ingest.embed_texts` 对超限文本的处理是**截断后继续** ——
    文本整篇入库但向量只覆盖前 8191 token, 超出部分检索不到。那是静默降级
    (Global Constraint 6 禁止), 且看不出来: 入库计数、完备性闸、编号闸全绿。
    实测那份文档有 2 节超限 (16173 / 9738 token)。

    切点选择是确定性的: 贪心累积行, 需要切时优先回退到本份内**最后一个空行**
    (段落边界), 没有空行才在当前行前硬切。单行本身超限时不再细切 (保正文完整),
    这种份会被 ingest 侧截断 —— 属已知限制, 实测未发生。
    """
    lines, owner = _flat(pages)
    joined = "".join(lines)
    out: list[Section] = []
    for sec in sections:
        if count_tokens(sec.body) <= max_tokens:
            out.append(sec)
            continue
        start = joined.find(sec.body)
        if start < 0:  # 不该发生: body 必来自 joined
            raise AssertionError(f"节 {sec.number} 的正文不在原文里, 切分器状态不一致")
        # 该节覆盖的全局行区间
        offsets: list[int] = []
        acc = 0
        for ln in lines:
            offsets.append(acc)
            acc += len(ln)
        gi = offsets.index(start)
        n_lines = 0
        consumed = 0
        while consumed < len(sec.body):
            consumed += len(lines[gi + n_lines])
            n_lines += 1
        span = list(range(gi, gi + n_lines))

        parts: list[list[int]] = []
        cur: list[int] = []
        for g in span:
            cand = cur + [g]
            if cur and count_tokens("".join(lines[i] for i in cand)) > max_tokens:
                blanks = [k for k, i in enumerate(cur) if not lines[i].strip()]
                if blanks and blanks[-1] > 0:          # 回退到段落边界
                    cut = blanks[-1] + 1
                    parts.append(cur[:cut])
                    cur = cur[cut:] + [g]
                else:
                    parts.append(cur)
                    cur = [g]
            else:
                cur = cand
        if cur:
            parts.append(cur)

        total = len(parts)
        for k, idxs in enumerate(parts, start=1):
            body = "".join(lines[i] for i in idxs)
            out.append(Section(
                number=sec.number,
                level=sec.level,
                heading_line=sec.heading_line,
                body=body,
                page_start=owner[idxs[0]],
                page_end=owner[idxs[-1]],
                part=k,
                parts_total=total,
            ))
    return out


def check_numbering(sections: list[Section]) -> list[str]:
    """编号连续性闸。返回违规描述列表 (空 = 通过)。

    只查两条可机器判定的性质, 不猜语义:
      - 章号 (第一段) 非递减;
      - **同一父前缀**内, 末段严格递增。父前缀 = 去掉末段的全部前缀,
        故 `6.2.3.1` 的父是 `6.2.3` 而不是 `6` —— 按 `6` 比会把文档里
        9 个四层标题 (6.2.3.1 / 8.2.19.1 …) 全误报成「子号未递增」。
    违规不代表切分一定错 (源文档可能真的乱编号), 但**必须被人看到**,
    不许静默通过 —— 这是有损轨唯一的自动预警。
    """
    problems: list[str] = []
    last_chapter: int | None = None
    last_child: dict[str, int] = {}
    for s in sections:
        if s.part > 1:
            continue  # 二次切分的续份复用同一编号, 不是新节, 不参与序列判定
        parts = s.number.split(".")
        chapter = int(parts[0])
        if last_chapter is not None and chapter < last_chapter:
            problems.append(f"章号回退: {s.number} (前一个章号 {last_chapter}) p.{s.page_start}")
        last_chapter = chapter if last_chapter is None else max(chapter, last_chapter)
        if len(parts) > 1:
            prefix, child = ".".join(parts[:-1]), int(parts[-1])
            prev = last_child.get(prefix)
            if prev is not None and child <= prev:
                problems.append(
                    f"子号未递增: {s.number} (同父上一个 {prefix}.{prev}) p.{s.page_start}")
            last_child[prefix] = child
    return problems


def assert_partition_complete(pages: list[str], sections: list[Section]) -> None:
    """把所有 section 的 body 顺序拼接, 必须逐字等于「首锚点行起」的全文。

    参照物是**原始页文本**而非切分器自报的任何计数 —— 生成物的校验参照物
    必须来自生成器之外 (硬规矩 6)。丢一节 / 重一节 / 顺手 strip 一个空行, 全会红。
    """
    if not sections:
        return
    lines, _ = _flat(pages)
    joined = "".join(s.body for s in sections)
    first = "".join(lines).find(sections[0].heading_line)
    tail = "".join(lines)[first:]
    assert joined == tail, (
        f"分割不完备: 拼回 {len(joined)} 字符 vs 原文尾段 {len(tail)} 字符 "
        f"(差 {len(tail) - len(joined)})"
    )


def detect_toc_pages(pages: list[str]) -> list[int]:
    """目录页 (1-based) —— 靠版面形态识别, 判据与阈值见 `_TOC_MIN_*` 处的实测依据。

    目录是导航不是内容: 它的每一条都是某个真实章节标题的**重复**, 而那些标题本身
    已经在编号 chunk 里; 把目录也入库, 命中它只会返回一块「只有点线和页码」的东西,
    还要跟正文抢检索名额。故本函数的产物是**排除清单**, 不是待切分清单。
    """
    out: list[int] = []
    for pi, text in enumerate(pages, start=1):
        lines = [ln for ln in text.splitlines() if ln.strip()]
        numbered = sum(1 for ln in lines if _ANCHOR.match(ln))
        leaders = sum(1 for ln in lines if _DOT_LEADER.search(ln))
        if numbered >= _TOC_MIN_NUMBERED and leaders >= _TOC_MIN_DOT_LEADER:
            out.append(pi)
    return out


def split_front_matter(pages: list[str], excluded_pages: list[int]) -> list[Section]:
    """首锚点之前、且不在 `excluded_pages` 里的内容 → **每页一个** Section。

    为什么按页而不按锚点: 真实文档的卷首 (p1-10) 实测 **编号行 0 条、可识别标题
    0 条** —— 锚点切分器在这里无处下手。页是抽取器本来的单位 (`pdftotext -f N -l N`
    逐页), 且实测单页 169-1,907 token, 远低于 8,191 上限 (整块则是 10,034, 超限)。

    编号用 `front{页号:02d}`: 页号即出处, 且与编号节的命名空间不相交, 不会污染
    `check_numbering` 的编号序列。首锚点所在页只取锚点行**之前**的部分 (真实文档
    这半页是 578 字符), 否则那段会继续漏掉。
    """
    anchors = find_anchors(pages)
    if not anchors:
        return []          # 无锚点时不猜; build_docs 已对"切出 0 节"fail-closed
    first_page, first_line, _, _ = anchors[0]
    excluded = set(excluded_pages)
    out: list[Section] = []
    for pi, text in enumerate(pages, start=1):
        if pi > first_page or pi in excluded:
            continue
        if pi == first_page:
            body = "".join(text.splitlines(keepends=True)[:first_line])
        else:
            body = text
        if not body:
            continue
        if not body.strip():
            raise AssertionError(
                f"卷首第 {pi} 页只有空白 —— 拒绝写出空 chunk (会被 embed 成噪声向量)。"
                f"若该页确实无内容, 把它显式加进排除清单, 别让它静默变成空块。")
        out.append(Section(number=f"front{pi:02d}", level=0, heading_line="",
                           body=body, page_start=pi, page_end=pi))
    return out


def assert_full_coverage(pages: list[str], sections: list[Section],
                         excluded_pages: list[int]) -> None:
    """**全文**每个字符必须落在某个 section 里, 或落在显式声明的排除页里。

    与 `assert_partition_complete` 的区别就是这条闸存在的理由: 那把闸的口径是
    「逐字等于**首锚点行起**的全文」, 对首锚点**之前**的区域**天然免疫** ——
    真实文档 66,200 字符 (全文 27.42%) 就是这么漏掉的, 而那把闸全程绿灯
    (见 study_c1_doc_sections.md 已知限制 L1: "不得把闸绿读成内容都能检索到")。

    排除页必须由调用方**显式传入**并有形态依据 (见 `detect_toc_pages`), 不接受
    "反正没覆盖到就算排除"这种事后追认 —— 那等于把闸的口径交给缺陷自己定义。
    """
    excluded = set(excluded_pages)
    expected = "".join(t for i, t in enumerate(pages, start=1) if i not in excluded)
    joined = "".join(s.body for s in sections)
    if joined == expected:
        return
    n = min(len(joined), len(expected))
    at = next((i for i in range(n) if joined[i] != expected[i]), n)
    raise AssertionError(
        f"未覆盖: 拼回 {len(joined)} 字符 vs 应覆盖 {len(expected)} 字符 "
        f"(差 {len(expected) - len(joined)}), 首个不一致在偏移 {at}; "
        f"排除页 {sorted(excluded) or '无'}")
