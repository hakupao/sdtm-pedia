"""(b) 层: 逐答案问裁判「这条答案有没有做 class/Core/Role/Type 归属断言, 与权威表一致吗」。

⚠ **为什么是逐答案扫而不是并排比**: (b) 层要判的是"这条答案本身对不对", 不是"谁更好"。
逐答案扫顺带**结构性地满足匿名** —— 裁判从头到尾不知道答案出自哪个模型, 不需要
`compare.py :: run_judge` 那套 A/B/C 映射 (那是给排名用的)。

⚠ **解析失败一律落 `unsure`, ⛔ 绝不落 `consistent`**: 对抗抽样是从 `consistent` 里抽的,
把"裁判没说清"读成"干净"会让它躲开人判 —— 而人判正是用来兜裁判漏网的。
"""
from __future__ import annotations

import json
import re

_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.S)
_BARE_RE = re.compile(r"(\{.*\})", re.S)

_PROMPT = """You are auditing ONE answer produced by a SDTM knowledge-base assistant.

AUTHORITATIVE dataset→class table (the ONLY source of truth for class membership):

{authority}

Naming note: the table keys the supplemental-qualifier datasets as `SUPP--`.
Answers may instead write `SUPPQUAL`, `SUPPAE`, `SUPPDM`, etc. Treat all of those as `SUPP--`.

Task: decide whether the answer below makes any assertion about a dataset's
class / Core / Role / Type membership, and whether that assertion agrees with the table.

Reply with ONLY a JSON object, no prose:
{{"has_assertion": <true|false>,
  "verdict": "consistent" | "inconsistent" | "unsure",
  "quote": "<the exact sentence from the answer that carries the assertion, or empty>",
  "authority": "<the table row you compared against, or empty>"}}

If the answer makes no class/Core/Role/Type assertion at all, use
has_assertion=false and verdict="consistent".

ANSWER:
{answer}
"""


def build_judge_prompt(answer: str, authority_md: str) -> str:
    return _PROMPT.format(authority=authority_md, answer=answer)


def parse_judge_verdict(raw: str) -> dict:
    """把裁判的回复解析成结构化判定。解析不了 ⇒ `unsure` + `parse_error`。"""
    blob = None
    m = _FENCE_RE.search(raw) or _BARE_RE.search(raw)
    if m:
        try:
            blob = json.loads(m.group(1))
        except json.JSONDecodeError:
            blob = None
    if not isinstance(blob, dict):
        return {"has_assertion": None, "verdict": "unsure", "quote": "",
                "authority": "", "parse_error": True, "raw": raw[:400]}
    verdict = blob.get("verdict")
    if verdict not in ("consistent", "inconsistent", "unsure"):
        verdict = "unsure"
    return {"has_assertion": blob.get("has_assertion"),
            "verdict": verdict,
            "quote": blob.get("quote") or "",
            "authority": blob.get("authority") or "",
            "parse_error": False}


def scan_answers(entries, judge, authority_md: str) -> list[dict]:
    """`entries` = [{"id", "answer"}]; `judge` = (prompt) -> raw text。

    单条失败**隔离**: 记成 `unsure` + `error` 继续扫, 不让一个答案毁掉整批
    (照 `compare.py :: _one_completion` 的失败隔离先例)。
    """
    rows = []
    for e in entries:
        prompt = build_judge_prompt(e["answer"], authority_md)
        try:
            v = parse_judge_verdict(judge(prompt))
            v["error"] = None
        except Exception as exc:  # noqa: BLE001 — 逐条隔离
            v = {"has_assertion": None, "verdict": "unsure", "quote": "",
                 "authority": "", "parse_error": False, "error": str(exc)[:200]}
        v["id"] = e["id"]
        rows.append(v)
    return rows
