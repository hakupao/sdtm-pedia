"""doc 侧题集的入池闸 —— 全部确定性, 零 LLM。

存在的理由: doc chunk 接线前必须先有尺子, 而"尺子本身是否有判别力"必须也是可执行的,
不能靠出题人自述。四道闸对应 spec §4:

  A gold_unique    gold 在 114 个 chunk 名里唯一定位 (委托 eval.lint_gold, 唯一实现)
  B anchor_unique  答案锚串**落在该题每个 gold chunk 里, 且不溢出到任何非 gold chunk**
  C fact_length    每条 expected_facts 够长 (1-2 词碎片会让 fact-recall 顶格失明)
  D card_unanswerable  没有任何一张 field card 同时含全部 card_probe_terms

**闸 B 的口径边界 (硬规矩 19, 引用绿灯时必须同时写)**: 锚串落位正确 != 语义唯一。
别的 chunk 可能换措辞表达同一事实, 本闸看不见。它只挡字面。
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from eval.lint_gold import doc_chunk_names, lint_gold, match_names

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


def gate_gold_unique(test_set_path: Path | str, docs_dir: Path | str) -> list[GateFinding]:
    return [
        GateFinding("gold_unique", f.qid,
                    f"[{f.side}] {f.gold!r} 匹配 {f.n_matches} 个 chunk — 期望唯一定位")
        for f in lint_gold(str(test_set_path), docs_dir=docs_dir)
    ]


def gate_anchor_unique(questions: list[dict], bodies: dict[str, str]) -> list[GateFinding]:
    """锚串必须落在该题**每个** gold chunk 里, 且**不溢出**到任何非 gold chunk。

    口径是 membership, 不是数量。初版比的是"含锚串的 chunk 数 == len(expected_sources)",
    复审复现了它的四条 fail-open (全部恒绿):

      ① OR-only 题 + 捏造锚串     n_gold==0, hits==0 → 0==0 判绿
      ② 完全无 gold 的题 + 捏造   同上; 而闸 A 对没有 gold 键的题零迭代也不报,
                                  两闸叠加 ⇒ 一道完全没有尺子的坏题四闸全绿入池
      ③ gold=[a] 但锚串只在 b     1==1 判绿, 指向完全错位 (最致命)
      ④ gold=[a,c] 锚串在 a,b     2==2 判绿, 半数错位

    ①②的病根是同一个: `n_gold == 0` 时 `0 == 0` 恒成立, 而"锚串根本不在语料里"
    正是这道闸存在的**唯一理由** —— 旧口径恰好在这一格失明。故无 gold 直接报。

    gold 两侧 (`expected_sources` / `expected_sources_any`) 都收: 闸 A 经 lint_gold
    是两侧都查的, 闸 B 只看 AND 侧就会与闸 A 口径不一致 (即①)。

    `targets` 必须走 `match_names` 而不是拿 gold 直接当 `bodies` 的键:
    闸 A 允许"子串唯一定位"的 gold (如写 `s22_1__part01` 不带 `.md`), 精确取键会对
    这类合法 gold 误报 missing。同一个函数 ⇒ 闸 A 与闸 B 对"哪些 chunk 算这题的 gold"
    永远给同一个答案。
    """
    findings: list[GateFinding] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        anchor = q.get("anchor")
        gold = list(q.get("expected_sources") or []) + list(q.get("expected_sources_any") or [])
        if not gold:
            findings.append(GateFinding("anchor_unique", qid, "无 gold — 锚串无从校验"))
            continue
        if not anchor:
            findings.append(GateFinding("anchor_unique", qid, "缺 anchor 字段"))
            continue
        if len(anchor) < ANCHOR_MIN_LEN:
            findings.append(GateFinding(
                "anchor_unique", qid,
                f"anchor 过短 {len(anchor)} < {ANCHOR_MIN_LEN} — 短串会碰巧命中"))
            continue
        targets = {n for g in gold for n in match_names(g, qid, list(bodies))}
        missing = sorted(n for n in targets if anchor not in bodies[n])
        extra = sorted(n for n, body in bodies.items() if anchor in body and n not in targets)
        if not targets:
            findings.append(GateFinding(
                "anchor_unique", qid, f"gold {gold} 未解析到任何 chunk — 锚串无从校验"))
        elif missing or extra:
            findings.append(GateFinding(
                "anchor_unique", qid,
                f"锚串不在 gold chunk {missing} / 溢出到非 gold chunk {extra[:3]}"))
    return findings


FACT_MIN_LEN = 12
# OID / codelist ID / 项目コード 形态: 全大写+数字+下划线, 长度 >= 3。
# 它们天生短但不是碎片 —— check_fact_recall 对它们有判别力 (v2 已验证)。
_ID_SHAPED = re.compile(r"^[A-Z][A-Z0-9_]{2,}$")


def card_texts(cards_dir: Path | str) -> dict[str, str]:
    """field card 全文语料。

    用卡片全文而不是 catalog 派生串: audit_v2 记过一次口径事故 —— 出题人用 catalog
    近似语料、审题人用卡片全文, 数字差几个百分点。以卡片全文为准。
    """
    return {p.name: p.read_text(encoding="utf-8")
            for p in sorted(Path(cards_dir).glob("*.md"))}


def gate_fact_length(questions: list[dict]) -> list[GateFinding]:
    findings: list[GateFinding] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        facts = q.get("expected_facts") or []
        if not facts:
            findings.append(GateFinding("fact_length", qid, "缺 expected_facts"))
            continue
        for fact in facts:
            if len(fact) >= FACT_MIN_LEN or _ID_SHAPED.match(fact):
                continue
            findings.append(GateFinding(
                "fact_length", qid,
                f"fact {fact!r} 长 {len(fact)} < {FACT_MIN_LEN} 且非 ID 形态 — "
                "1-2 词碎片会让 fact-recall 顶格失明"))
    return findings


def gate_card_unanswerable(questions: list[dict], cards: dict[str, str]) -> list[GateFinding]:
    """闸 D: 没有任何一张 field card 同时含全部 probe 词。

    口径边界 (硬规矩 19): 这是**字面**筛。语义等价的卡片本闸看不见, 故 spec §4 要求
    另抽 N=6 分层样本走实测复核。单词数 < 2 直接报 —— 一个词太容易不撞卡, 闸会白送。
    """
    findings: list[GateFinding] = []
    lowered = {name: text.lower() for name, text in cards.items()}
    for q in questions:
        qid = q.get("id", "<no id>")
        terms = q.get("card_probe_terms") or []
        if len(terms) < 2:
            findings.append(GateFinding(
                "card_unanswerable", qid,
                f"card_probe_terms 只有 {len(terms)} 个, 需 >= 2 — 单词筛会白送"))
            continue
        low = [t.lower() for t in terms]
        hit = [name for name, text in lowered.items() if all(t in text for t in low)]
        if hit:
            findings.append(GateFinding(
                "card_unanswerable", qid,
                f"卡片 {sorted(hit)[:3]} 同时含全部 probe 词 — 该题卡片可能答得出"))
    return findings
