"""doc 侧题集的入池闸 —— 全部确定性, 零 LLM。

存在的理由: doc chunk 接线前必须先有尺子, 而"尺子本身是否有判别力"必须也是可执行的,
不能靠出题人自述。四道闸对应 spec §4:

  A gold_unique    gold 在 114 个 chunk 名里唯一定位 (委托 eval.lint_gold, 唯一实现)
  B anchor_unique  答案锚串在全集出现次数 == gold 数
  C fact_length    每条 expected_facts 够长 (1-2 词碎片会让 fact-recall 顶格失明)
  D card_unanswerable  没有任何一张 field card 同时含全部 card_probe_terms

**闸 B 的口径边界 (硬规矩 19, 引用绿灯时必须同时写)**: 锚串唯一 != 语义唯一。
别的 chunk 可能换措辞表达同一事实, 本闸看不见。它只挡字面。
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from eval.lint_gold import doc_chunk_names, lint_gold

ANCHOR_MIN_LEN = 20
_FM_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


@dataclass(frozen=True)
class GateFinding:
    gate: str
    qid: str
    detail: str


def chunk_bodies(docs_dir: Path | str) -> dict[str, str]:
    """文件名 → 正文 (剥掉 frontmatter)。

    剥 frontmatter 而不是整文件扫: frontmatter 里只有编号/页码, 让它参与锚串计数
    只会制造与内容无关的假命中。用锚定正则一次性剥, 不用 `split('---')`
    —— C1 复核时正是那个写法多留了换行, 把 66,200 算成 66,086。
    """
    out: dict[str, str] = {}
    for name in doc_chunk_names(docs_dir):
        text = (Path(docs_dir) / name).read_text(encoding="utf-8")
        out[name] = _FM_RE.sub("", text, count=1)
    return out


def load_questions(test_set_path: Path | str) -> list[dict]:
    data = yaml.safe_load(Path(test_set_path).read_text(encoding="utf-8"))
    qs = data["questions"] if isinstance(data, dict) else data
    return [q for q in qs if not q.get("out_of_scope")]


def gate_gold_unique(test_set_path: Path | str, docs_dir: Path | str) -> list[GateFinding]:
    return [
        GateFinding("gold_unique", f.qid,
                    f"[{f.side}] {f.gold!r} 匹配 {f.n_matches} 个 chunk — 期望唯一定位")
        for f in lint_gold(str(test_set_path), docs_dir=docs_dir)
    ]


def gate_anchor_unique(questions: list[dict], bodies: dict[str, str]) -> list[GateFinding]:
    findings: list[GateFinding] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        anchor = q.get("anchor")
        n_gold = len(q.get("expected_sources") or [])
        if not anchor:
            findings.append(GateFinding("anchor_unique", qid, "缺 anchor 字段"))
            continue
        if len(anchor) < ANCHOR_MIN_LEN:
            findings.append(GateFinding(
                "anchor_unique", qid,
                f"anchor 过短 {len(anchor)} < {ANCHOR_MIN_LEN} — 短串会碰巧命中"))
            continue
        hits = sum(1 for body in bodies.values() if anchor in body)
        if hits != n_gold:
            findings.append(GateFinding(
                "anchor_unique", qid,
                f"anchor 在全集出现 {hits} 次, gold 数 {n_gold} — {hits} != {n_gold}"))
    return findings
