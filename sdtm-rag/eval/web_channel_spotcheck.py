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

CODE_RE = re.compile(r"\bC\d{4,6}\b")
WEB_CITE_RE = re.compile(r"\[Web:\s*(https?://[^\s\]]+)")
KB_CITE_RE = re.compile(r"\[Source:\s*([^\]]+)\]")


def _iter_sse_frames(text: str):
    """按空行切分 SSE 帧, 逐帧解析 `event:` / `data:` 两行 —— 与 server/router.py
    的 `sse()` 输出格式 (`event: {e}\\ndata: {json}\\n\\n`) 一一对应。"""
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


def ask(base: str, q: str, timeout: float) -> dict:
    """打 /api/ask_stream (联网工具循环只在这条路径实现), 拼出完整答案 + 联网元信息。"""
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
    for event, data in _iter_sse_frames(r.text):
        if event == "token":
            answer_parts.append(data.get("text", ""))
        elif event == "tool_call":
            tool_calls.append(data.get("query", ""))
        elif event == "tool_result":
            tool_result_statuses.append(data.get("status", ""))
        elif event == "done":
            done = data
        elif event == "error":
            raise RuntimeError(f"SSE error event: {data.get('message')}")
    return {
        "answer": "".join(answer_parts),
        "tool_calls": tool_calls,
        "tool_result_statuses": tool_result_statuses,
        "web_status": done.get("web_status"),
        "web_searches_ok": done.get("web_searches_ok"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=len(QUESTIONS))
    ap.add_argument("--base", default="http://localhost:8000")
    # 读超时: requests 的 timeout 是每次 read 的超时, 不是总时长 —— 流式响应下,
    # 只要还在陆续收到字节就不会因总时长触发, 但单次卡住 (如联网调用挂起) 仍要有兜底。
    ap.add_argument("--timeout", type=float, default=300.0)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()

    rows = []
    for q in QUESTIONS[:a.n]:
        try:
            r = ask(a.base, q, a.timeout)
        except Exception as exc:  # noqa: BLE001
            rows.append({
                "q": q, "answer": "", "codes": ["调用失败: " + type(exc).__name__],
                "webs": [], "kbs": [], "web_status": None,
                "web_searches_ok": None, "n_calls": 0, "contexts": [],
            })
            continue
        ans = r["answer"]
        rows.append({
            "q": q,
            "answer": ans,
            "codes": CODE_RE.findall(ans),
            "webs": WEB_CITE_RE.findall(ans),
            "kbs": KB_CITE_RE.findall(ans),
            "web_status": r["web_status"],
            "web_searches_ok": r["web_searches_ok"],
            "n_calls": len(r["tool_calls"]),
            "contexts": _code_contexts(ans),
        })

    lines = ["# 联网通道语义抽检 (规则 A)", "",
             "> 联网答案不可复算, **不进 gold set** —— 本表是它唯一的质量证据。",
             "> ⚠ 机检只能查形状; **人判两列必须人眼逐条判**, 不得由脚本判 PASS。", "",
             "| # | 问题 | 机检: CT 码 | web_status | web_searches_ok | 搜索次数 | "
             "机检: [Web:] 数 | 机检: [Source:] 数 | 人判: 标注是否规矩 | "
             "人判: 借鉴是否标推测 |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for i, row in enumerate(rows, 1):
        flag = "⛔ " + ",".join(row["codes"]) if row["codes"] else "✅ 无"
        lines.append(
            f"| {i} | {row['q'][:60]} | {flag} | {row['web_status']} | "
            f"{row['web_searches_ok']} | {row['n_calls']} | {len(row['webs'])} | "
            f"{len(row['kbs'])} | ⬜ 待判 | ⬜ 待判 |"
        )
    lines += ["", "## 判读规则", "",
              "- **CT 码列出现任何码 = 立即查**: Rule 9(b) 禁止从网页产出 `Cxxxxx`。",
              "  码若能在 `knowledge_base/` 找到且答案标的是 `[Source:]`, 属正常 (KB 来源);",
              "  标 `[Web:]` 却带码 = **红线破**。",
              "- **`web_status`/`web_searches_ok` 直接给出联网是否真的发生** —— 比"
              "『`[Web:]` 数为 0 ⇒ 可能没真联网』这种间接推断可靠: "
              "`web_searches_ok` > 0 才是真的搜到了结果; `web_status` 应为 `ok`,"
              " 非 `ok` (如 `disabled`/`quota_exceeded`/`failed`/`off`) 说明联网本身有问题。",
              "- 人判两列必须逐条看答案原文, 不看就填 = 抽检失效 (规则 A 的意义就在这)。"]

    any_codes = any(row["contexts"] for row in rows)
    lines += ["", "## 附录: CT 码标注上下文 (机器只定位, 不判读)", "",
               "> ⚠ **\"最近引用标记\"是启发式定位, 不是来源判定。** 绝对字符距离只能告诉你"
               "\"这个码附近最近的标记是什么\", **推不出**\"这个码来自那个来源\" —— 同一段落"
               "可能引了多个来源, 物理最近的标记未必是这个码的事实依据所在。红线判定必须**读"
               "原文片段**确认该码的事实依据来自哪一边, 不能只看这一列的标签。", ""]
    if not any_codes:
        lines.append("(本轮没有命中任何 `Cxxxxx`。)")
    for i, row in enumerate(rows, 1):
        if not row["contexts"]:
            continue
        lines.append(f"### 第 {i} 题: {row['q']}")
        lines.append("")
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

    print(f"抽检表已写入 {a.out} ({len(rows)} 题)")
    print(f"答案原文已写入 {answers_path}")
    print("⚠ 机检只查形状/定位; 人判两列 + 标注上下文判读必须人眼完成后才算抽检done。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
