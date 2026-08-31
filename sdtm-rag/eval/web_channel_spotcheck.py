"""联网通道语义抽检 (规则 A; spec §8)。

联网答案不可复算, 不进 gold set ⇒ 质量只能靠人工抽检。本脚本跑 N 个真实问答,
把**需要人眼判断的四件事**列成表, 结果留 evidence/。

v2 (2026-08-31): 联网工具循环只在 `POST /api/ask_stream` (SSE) 里实现 ——
`AskRequest`(`/api/ask` 用的非流式请求模型) 没有 `web` 字段, `ask()` 端点也从未把
`web_search` 工具接进 LLM 调用。v1 打的是 `/api/ask`, 三题全部零联网, 已作废归档
到 `evidence/failures/web_channel_spotcheck_attempt_1_wrong_endpoint.md`。v2 改打
`/api/ask_stream`, 按 `event:`/`data:` 帧解析 `token`/`tool_call`/`tool_result`/`done`,
顺带覆盖了「真实 SSE 字节流 → 解析」这一层 (静态正则契约闸 test_sse_contract.py
够不到的部分)。

v3 (2026-08-31): v2 测出了真联网 (`web_status=ok`), 但主表命中的 CT 码判不了
红线 —— 判读规则要看"码标的是 `[Source:]` 还是 `[Web:]`", 而主表只有计数, 答案
原文没有落盘。本版加两样东西, **只做定位, 不替人下结论**:
  (a) 每题完整答案原文另存一个 `_answers.md` 文件;
  (b) 主表后加一个"CT 码标注上下文"附录, 对每个命中的 `Cxxxxx` 抠出前后文 + 离它
      最近的引用标记, 供人一眼判读; 人判两列依旧留 `⬜ 待判`, 机器不判 PASS。

v4 (2026-08-31, 代码审查后修复): 审查发现同一类失败模式反复出现三次——「解析
失败时的表现和成功时长得一样」(v1 打错端点、SSE 帧解析器潜在的 CRLF 问题、
答案为空但表照样显示"干净"), 所以这版补的都是**让失败可见**:
  (a) `ask()` 现在跟踪是否真的收到 `done` 事件; `main()` 对"答案为空"或"没收到
      done"的行标记 `⛔ 解析失败`, 不再让解析失败悄悄显示成 `✅ 无`;
  (b) `搜索次数==0` 的行在附录里直接标"已结构性排除", 不再只靠"最近引用"这条
      弱启发式 (弱启发式仍保留给`搜索次数>0`时用);
  (c) 新增一列机检: `[Web:]` 引用所在句子里有没有 Core/Role/Class/Type 这类
      "硬事实"关键词——Rule 9(b) 禁的是三样 (CT 码 / class / Core-Role-Type),
      之前只查了 CT 码那一样;
  (d) `main()` 在任何一行失败 (调用异常 / 解析失败) 时返回非零, 不再恒 0。

跑法:
  cd sdtm-rag && .venv/bin/python eval/web_channel_spotcheck.py --n 5 \
      --out evidence/checkpoints/web_channel_spotcheck.md
  # 同时写出 evidence/checkpoints/web_channel_spotcheck_answers.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import requests

QUESTIONS = [
    "How do other teams handle EDC fields that don't map to any standard SDTM domain?",
    "What do practitioners say about overusing SUPPQUAL versus creating a custom domain?",
    "How is Findings About (FA) used in practice versus a custom findings domain?",
    "What does FDA's Study Data Technical Conformance Guide say about custom domains?",
    "How do sponsors document non-standard variables in define.xml in practice?",
]

# C\d{4,6} 会漏掉 7 位及以上的 CDISC 码; 上限去掉后误报只会落在"更愿意去查一下"
# 这一侧, 比漏检安全。
CODE_RE = re.compile(r"\bC\d{4,}\b")
WEB_CITE_RE = re.compile(r"\[Web:\s*(https?://[^\s\]]+)")
KB_CITE_RE = re.compile(r"\[Source:\s*([^\]]+)\]")

# Rule 9(b) 禁的是三样硬事实: CT 码 (CODE_RE 管这个) / class 或 category 归属 /
# Core-Role-Type。后两样目前没有专门的机检, 这组关键词只是在"含 [Web: 引用的
# 句子"里做形状扫描, 供人判读时优先看——不是判定, 见 I-6 相关注释。
_HARD_FACT_KEYWORDS = re.compile(
    r"\b(Req|Perm|Exp|Core|Role|Qualifier|Class|Identifier|Topic|Grouping|Timing)\b")


def _iter_sse_frames(text: str):
    """按空行切分 SSE 帧, 逐帧解析 `event:` / `data:` 两行。

    ⚠ 这不是通用 SSE 解析器, 是与 `server/router.py::sse()` 的输出格式绑定的:
    - 该函数固定产出 `event: {e}\\ndata: {json}\\n\\n` (单个 event 行 + 单个
      data 行), 所以这里每帧只取**最后一个** `data:` 行 (循环里直接覆盖赋值)——
      通用 SSE 允许一帧里出现多个 `data:` 行并用换行拼接, 这里没有实现那种拼接,
      因为本项目的 `sse()` 从不这样发。
    - 假设换行符是纯 `\\n`; 若反代/中间层把行尾改写成 `\\r\\n` (SSE 规范允许),
      `text.split("\\n\\n")` 会切错帧数, 解析结果会残缺但**不会抛异常**——这正是
      为什么 `ask()`/`main()` 要单独检查"有没有收到 done 事件"、"答案是否为空"
      (v4 新增), 不能假设"解析不报错 = 解析对了"。
    """
    for frame in text.split("\n\n"):
        frame = frame.strip("\n")
        if not frame:
            continue
        event = None
        data_line = None
        for line in frame.split("\n"):
            if line.startswith("event:"):
                event = line[len("event:"):].strip()
            elif line.startswith("data:"):
                data_line = line[len("data:"):].strip()
        if event is None or data_line is None:
            continue
        try:
            data = json.loads(data_line)
        except json.JSONDecodeError:
            continue
        yield event, data


_CONTEXT_WINDOW = 150  # 每侧字符数, 够看清一句话但不至于整段搬进来


def _code_contexts(answer: str) -> list[dict]:
    """给每个命中的 `Cxxxxx` 抠出前后文, 并标出离它最近的引用标记 —— Rule 9(b)
    判读的唯一依据是"这个码标的是 [Source:] 还是 [Web:]", 不是"码存不存在"。

    ⚠ 这里只做**定位**(找最近的引用标记 + 给出原文片段), 不做判读: 距离最近不等于
    "属于"那条引用 (同一段落可能引了多个来源), 真正的归属仍要人读 snippet 判断。
    这是**启发式弱路径**——`搜索次数==0` 的行有更硬的结构性排除, 见
    `main()` 里对应的判读规则与附录标注, 优先级更高。

    ⚠ 距离度量本身不对称 (向后从码首算, 向前从引用标记**尾**算, 偏向前置引用约
    7 个字符): 这是已知的非承重实现细节, 有意不改——这个数字已经声明"不构成
    来源判定", 而已提交证据里记录的具体距离值 (来自一次花过钱、不会重跑的运行)
    若因为改度量方式而变化, 会让脚本产出的数字和已提交证据对不上, 后人 diff 到
    会误以为数据被动过。详见 `task-6-report.md` 里对这条 Minor 的说明。
    """
    cites: list[tuple[int, int, str, str]] = []  # (start, end, kind, raw)
    for m in WEB_CITE_RE.finditer(answer):
        cites.append((m.start(), m.end(), "Web", m.group(0)))
    for m in KB_CITE_RE.finditer(answer):
        cites.append((m.start(), m.end(), "Source", m.group(0)))

    out = []
    for m in CODE_RE.finditer(answer):
        pos, code = m.start(), m.group(0)
        nearest_kind = nearest_raw = None
        nearest_dist = None
        for cs, ce, kind, raw in cites:
            dist = (cs - pos) if cs >= pos else (pos - ce)
            dist = max(dist, 0)
            if nearest_dist is None or dist < nearest_dist:
                nearest_dist, nearest_kind, nearest_raw = dist, kind, raw
        lo = max(0, pos - _CONTEXT_WINDOW)
        hi = min(len(answer), m.end() + _CONTEXT_WINDOW)
        snippet = answer[lo:hi].replace("\n", " ")
        out.append({
            "code": code, "pos": pos,
            "nearest_kind": nearest_kind, "nearest_raw": nearest_raw,
            "nearest_dist": nearest_dist, "snippet": snippet,
        })
    return out


def _web_sentences(answer: str) -> list[str]:
    """粗切句子 (按 `. `/`! `/`? `/换行), 只留含 `[Web:` 引用的那些——给 I-6 的
    关键词机检定位扫描范围, 不是严谨的分句器。"""
    sentences = re.split(r"(?<=[.!?])\s+|\n+", answer)
    return [s for s in sentences if "[Web:" in s]


def _hard_fact_keyword_hits(answer: str) -> list[tuple[str, str]]:
    """Rule 9(b) 禁的另外两样 (class/category 归属, Core-Role-Type) 目前没有像
    CT 码那样的专门机检——这里只做最粗的形状扫描: `[Web:` 引用句里出现的
    Core/Role/Class/Type 一类关键词, 返回 (关键词, 命中句子) 列表供人核对。
    命中不等于红线破 (这些词在 KB 来源的句子里也会正常出现), 只是提示"这句话
    里混着硬事实词汇, 且旁边有 web 引用, 值得多看一眼"。"""
    hits = []
    for s in _web_sentences(answer):
        for kw in _HARD_FACT_KEYWORDS.findall(s):
            hits.append((kw, s.strip()))
    return hits


def ask(base: str, q: str, timeout: float) -> dict:
    """打 /api/ask_stream (联网工具循环只在这条路径实现), 拼出完整答案 + 联网元信息。

    超时语义: requests 的 `timeout` 是每次底层 socket 读的超时, 不是整个请求的
    总时长——但下面用 `r.text` 一次性拿**完整**响应体, 不是边收边解析; 之所以
    这样也不会有跨读取边界的问题, 是因为 `.text` 内部本来就会把所有分片攒齐了
    才返回给我们, `_iter_sse_frames` 拿到手的已经是完整字符串, 不存在"一帧被
    截成两半"的风险。只要服务端还在陆续发送字节, 单次底层读取就不会超时;
    真正会触发这个超时的是"服务端完全停止发送任何字节" (比如联网调用整体挂起)。
    """
    r = requests.post(
        f"{base}/api/ask_stream",
        json={"question": q, "corpus": "cdisc", "web": True},
        timeout=timeout, stream=True,
    )
    r.raise_for_status()
    answer_parts: list[str] = []
    tool_calls: list[str] = []
    tool_result_statuses: list[str] = []
    done: dict = {}
    done_seen = False
    for event, data in _iter_sse_frames(r.text):
        if event == "token":
            answer_parts.append(data.get("text", ""))
        elif event == "tool_call":
            tool_calls.append(data.get("query", ""))
        elif event == "tool_result":
            tool_result_statuses.append(data.get("status", ""))
        elif event == "done":
            done = data
            done_seen = True
        elif event == "error":
            raise RuntimeError(f"SSE error event: {data.get('message')}")
    return {
        "answer": "".join(answer_parts),
        "tool_calls": tool_calls,
        "tool_result_statuses": tool_result_statuses,
        "web_status": done.get("web_status"),
        "web_searches_ok": done.get("web_searches_ok"),
        "done_seen": done_seen,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=len(QUESTIONS))
    ap.add_argument("--base", default="http://localhost:8000")
    ap.add_argument("--timeout", type=float, default=300.0)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()

    rows = []
    for q in QUESTIONS[:a.n]:
        try:
            r = ask(a.base, q, a.timeout)
        except Exception as exc:  # noqa: BLE001
            rows.append({
                "q": q, "answer": "", "failed": True,
                "codes": [f"解析失败: 调用异常 {type(exc).__name__}: {exc}"],
                "webs": [], "kbs": [], "web_status": None,
                "web_searches_ok": None, "n_calls": 0, "contexts": [], "hard_fact_hits": [],
            })
            continue

        ans = r["answer"]
        # v4/I-4: 答案为空或整轮没收到 done 事件, 说明 SSE 帧解析没有真的成功
        # (比如反代把换行改写成了 CRLF), 不能让这一行显示成"✅ 无"那种最干净的
        # 假象——之前这种情况会悄悄产出一行看起来完全正常的记录。
        if not ans or not r["done_seen"]:
            rows.append({
                "q": q, "answer": ans, "failed": True,
                "codes": [f"解析失败: answer_empty={not bool(ans)}, "
                          f"done_seen={r['done_seen']}"],
                "webs": [], "kbs": [],
                "web_status": r["web_status"], "web_searches_ok": r["web_searches_ok"],
                "n_calls": len(r["tool_calls"]), "contexts": [], "hard_fact_hits": [],
            })
            continue

        rows.append({
            "q": q,
            "answer": ans,
            "failed": False,
            "codes": CODE_RE.findall(ans),
            "webs": WEB_CITE_RE.findall(ans),
            "kbs": KB_CITE_RE.findall(ans),
            "web_status": r["web_status"],
            "web_searches_ok": r["web_searches_ok"],
            "n_calls": len(r["tool_calls"]),
            "contexts": _code_contexts(ans),
            "hard_fact_hits": _hard_fact_keyword_hits(ans),
        })

    lines = ["# 联网通道语义抽检 (规则 A)", "",
             "> 联网答案不可复算, **不进 gold set** —— 本表是它唯一的质量证据。",
             "> ⚠ 机检只能查形状; **人判两列必须人眼逐条判**, 不得由脚本判 PASS。",
             "> ⚠ 任何一行「零码」的观察都只是这次运行的证据, 不构成 Rule 9(b) 在统计"
             "意义上的有效性证明——样本量以本表实际行数为准, 不要脑补成「已充分验证」。",
             "",
             "| # | 问题 | 机检: CT 码 | web_status | web_searches_ok | 搜索次数 | "
             "机检: [Web:] 数 | 机检: [Source:] 数 | 机检: Web句含硬事实词 | "
             "人判: 标注是否规矩 | 人判: 借鉴是否标推测 |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, row in enumerate(rows, 1):
        flag = "⛔ " + ",".join(row["codes"]) if row["codes"] else "✅ 无"
        lines.append(
            f"| {i} | {row['q'][:60]} | {flag} | {row['web_status']} | "
            f"{row['web_searches_ok']} | {row['n_calls']} | {len(row['webs'])} | "
            f"{len(row['kbs'])} | {len(row['hard_fact_hits'])} | ⬜ 待判 | ⬜ 待判 |"
        )
    lines += ["", "## 判读规则", "",
              "- **CT 码列出现 `⛔ 解析失败`**: 不是码命中, 是脚本自己没拿到有效"
              "数据 (调用异常 / 答案为空 / 没收到 done 事件)——先查这一行的调用"
              "是否真的成功, 不要当成红线可疑处理; 也不要把这种行当「零码」计入"
              "正面证据。",
              "- **CT 码列出现真实码 = 立即查**: Rule 9(b) 禁止从网页产出 `Cxxxxx`、"
              "class/category 归属、Core/Role/Type。",
              "  码若能在 `knowledge_base/` 找到且答案标的是 `[Source:]`, 属正常 (KB 来源);",
              "  标 `[Web:]` 却带码 = **红线破**。",
              "- **`搜索次数` 列 = 0 时优先看它, 比「最近引用标记」这条弱启发式更硬**:"
              "该轮没有触发任何工具调用 ⇒ context 内不可能混入任何网页内容 ⇒ Rule 9(b)"
              "的触发条件从未成立——这一行任何 CT 码命中都只能来自 KB, 可直接判"
              "非红线破 (附录会对这类行标「已结构性排除」), 不需要再去核对最近引用标记。",
              "- **`web_status`/`web_searches_ok` 直接给出联网是否真的发生** —— 比"
              "『`[Web:]` 数为 0 ⇒ 可能没真联网』这种间接推断可靠: "
              "`web_searches_ok` > 0 才是真的搜到了结果; `web_status` 应为 `ok`,"
              " 非 `ok` (如 `partial`/`disabled`/`quota_exceeded`/`failed`/`off`)"
              " 说明联网本身有问题或不完整 (`partial` = 有成有败, 不是全灭)。",
              "- **`机检: Web句含硬事实词` 只是形状扫描, 不是判定**: 命中不等于红线破"
              "(这些词在 KB 来源句子里也会正常出现), 只是提示该句混着 Core/Role/Class"
              "一类硬事实词汇又带 [Web: 引用, 值得人多看一眼——具体命中在附录列出。",
              "- 人判两列必须逐条看答案原文, 不看就填 = 抽检失效 (规则 A 的意义就在这)。"]

    any_codes = any(row["contexts"] for row in rows)
    lines += ["", "## 附录: CT 码标注上下文 (机器只定位, 不判读)", "",
               "> ⚠ **「最近引用标记」是启发式定位, 不是来源判定。** 绝对字符距离只能告诉你"
               "「这个码附近最近的标记是什么」, **推不出**「这个码来自那个来源」 —— 同一段落"
               "可能引了多个来源, 物理最近的标记未必是这个码的事实依据所在。红线判定必须**读"
               "原文片段**确认该码的事实依据来自哪一边, 不能只看这一列的标签。"
               "`搜索次数==0` 的行不适用这条弱路径, 见下方逐条标注的「已结构性排除」。", ""]
    if not any_codes:
        lines.append("(本轮没有命中任何 `Cxxxxx`。)")
    for i, row in enumerate(rows, 1):
        if not row["contexts"]:
            continue
        lines.append(f"### 第 {i} 题: {row['q']}")
        lines.append("")
        if row["n_calls"] == 0:
            lines.append(
                "- **已结构性排除**: 本轮零工具调用 ⇒ context 内无任何网页内容 "
                "⇒ Rule 9(b) 适用前提未成立, 下面命中的码只可能来自 KB。"
                "(不依赖下面的「最近引用」这条启发式。)")
        for ctx in row["contexts"]:
            if ctx["nearest_kind"] is None:
                near = "附近 150 字符内没有任何 `[Source:]`/`[Web:]` 标记"
            else:
                near = (f"最近引用标记是 `[{ctx['nearest_kind']}:...]` "
                        f"(距 `{ctx['code']}` {ctx['nearest_dist']} 字符): "
                        f"`{ctx['nearest_raw'][:80]}`")
            lines.append(f"- **`{ctx['code']}`** @ char {ctx['pos']} — {near}")
            lines.append(f"  > …{ctx['snippet']}…")
        lines.append("")

    any_hits = any(row["hard_fact_hits"] for row in rows)
    lines += ["", "## 附录: [Web:] 句子里的 Core/Role/Class 等硬事实关键词 "
              "(机器只定位, 不判读)", ""]
    if not any_hits:
        lines.append("(本轮没有命中。)")
    for i, row in enumerate(rows, 1):
        if not row["hard_fact_hits"]:
            continue
        lines.append(f"### 第 {i} 题: {row['q']}")
        lines.append("")
        for kw, sentence in row["hard_fact_hits"]:
            lines.append(f"- 关键词 `{kw}`: …{sentence}…")
        lines.append("")

    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    answers_path = a.out.with_name(a.out.stem + "_answers" + a.out.suffix)
    ans_lines = ["# 联网通道语义抽检 — 答案原文 (人判材料; 不进 gold set)", ""]
    for i, row in enumerate(rows, 1):
        ans_lines += [f"## 第 {i} 题: {row['q']}", "",
                      f"- web_status={row['web_status']} "
                      f"web_searches_ok={row['web_searches_ok']} "
                      f"搜索次数={row['n_calls']}",
                      "", row["answer"] or "(无答案 / 调用失败)", ""]
    answers_path.write_text("\n".join(ans_lines) + "\n", encoding="utf-8")

    n_failed = sum(1 for row in rows if row["failed"])
    print(f"抽检表已写入 {a.out} ({len(rows)} 题, {n_failed} 题解析失败)")
    print(f"答案原文已写入 {answers_path}")
    print("⚠ 机检只查形状/定位; 人判两列 + 标注上下文判读必须人眼完成后才算抽检done。")
    return 1 if n_failed else 0


if __name__ == "__main__":
    sys.exit(main())
