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

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from eval.lint_gold import doc_chunk_names, lint_gold, load_questions, match_names

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

    ## 多 gold 题走 `anchors` (逐 gold 锚串), 2026-08-12 实测逼出

    单条锚串要求它**逐字出现在每个 gold chunk 里**。实测 114 个 chunk 的 20 字 shingle:

        20 字 shingle 总数                104,553
        恰好只出现在 2 个 chunk 的         2,715
        存在这种串的 chunk 对              90 / 6,441  = **1.4%**
        s22_1__part01 + part02 (切点两侧)  **0 条**

    即 **98.6% 的 chunk 对之间不存在可用作双 gold 锚串的 20 字串**, 而这不是缺陷:
    两个**互补**的节本来就不共享逐字长串; 共享长串的恰是重复节与父子节。
    ⇒ 单条共享锚串证明的是"有句话同时出现在两块" —— 那是**重复的证据**,
    而跨节聚合题要的是**互补**。**方向是反的, 旧口径不是严一点, 是量错了东西。**

    故多 gold 时改判: `anchors[i]` 必须落在 `expected_sources[i]` 解析出的**每个**
    chunk 里, 且**任何一条 anchor 都不得落到 gold 集合之外**。这直接表达
    "这半在这块、那半在那块" —— 表格被切点劈开 (L6 探针) 本来就该这么表达。

    单 gold 路径**行为不变** (`test_single_gold_path_unchanged_by_anchors_feature` 钉住)。
    """
    findings: list[GateFinding] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        and_gold = list(q.get("expected_sources") or [])
        or_gold = list(q.get("expected_sources_any") or [])
        gold = and_gold + or_gold
        anchor, anchors = q.get("anchor"), q.get("anchors")

        if not gold:
            findings.append(GateFinding("anchor_unique", qid, "无 gold — 锚串无从校验"))
            continue
        if anchor is not None and anchors is not None:
            findings.append(GateFinding(
                "anchor_unique", qid,
                "anchor 与 anchors 同时给出 — 两键互斥, 否则判的是哪条无从确定"))
            continue

        if anchors is not None:
            if not isinstance(anchors, list):
                findings.append(GateFinding(
                    "anchor_unique", qid,
                    f"anchors 不是列表 (拿到 {type(anchors).__name__}) — 标量会被逐字符当锚串"))
                continue
            if or_gold:
                findings.append(GateFinding(
                    "anchor_unique", qid,
                    "anchors 只与 expected_sources 一一对应, 不支持 OR 组"))
                continue
            if len(anchors) != len(and_gold):
                findings.append(GateFinding(
                    "anchor_unique", qid,
                    f"anchors 长 {len(anchors)} != expected_sources 长 {len(and_gold)} "
                    "— 必须一一对应, 否则错位对齐会静默判绿"))
                continue
            pairs = list(zip(and_gold, anchors, strict=True))
        else:
            if len(and_gold) > 1:
                findings.append(GateFinding(
                    "anchor_unique", qid,
                    f"多 gold ({len(and_gold)} 个) 必须用 anchors 逐 gold 给锚串 — "
                    "单条锚串要求两节共享逐字长串, 实测 98.6% 的 chunk 对不存在这种串"))
                continue
            if not anchor:
                findings.append(GateFinding("anchor_unique", qid, "缺 anchor 字段"))
                continue
            pairs = [(g, anchor) for g in gold]

        short = [a for _, a in pairs if not a or len(a) < ANCHOR_MIN_LEN]
        if short:
            findings.append(GateFinding(
                "anchor_unique", qid,
                f"anchor 过短/缺失 (最短 {min(len(a) if a else 0 for a in short)} "
                f"< {ANCHOR_MIN_LEN}) — 短串会碰巧命中"))
            continue

        targets: set[str] = set()
        missing: list[str] = []
        for g, a in pairs:
            names = match_names(g, qid, list(bodies))
            targets |= set(names)
            missing += [n for n in names if a not in bodies[n]]
        if not targets:
            findings.append(GateFinding(
                "anchor_unique", qid, f"gold {gold} 未解析到任何 chunk — 锚串无从校验"))
            continue
        extra = sorted({n for _, a in pairs
                        for n, body in bodies.items() if a in body and n not in targets})
        if missing or extra:
            findings.append(GateFinding(
                "anchor_unique", qid,
                f"锚串不在 gold chunk {sorted(missing)} / 溢出到非 gold chunk {extra[:3]}"))
    return findings


FACT_MIN_LEN = 12
# OID / codelist ID / 项目コード 形态: 全大写+数字+下划线, 长度 >= 3。
# 它们天生短但不是碎片 —— check_fact_recall 对它们有判别力 (v2 已验证)。
_ID_SHAPED = re.compile(r"^[A-Z][A-Z0-9_]{2,}$")


def card_texts(cards_dir: Path | str) -> dict[str, str]:
    """field card 全文语料 —— **只收 field card, 不收 kb 导航文件**。

    用卡片全文而不是 catalog 派生串: audit_v2 记过一次口径事故 —— 出题人用 catalog
    近似语料、审题人用卡片全文, 数字差几个百分点。以卡片全文为准。

    **为什么必须滤掉不含 `__` 的文件** (2026-08-11 实测逼出): `cards_dir` 是
    `RAGEngine` 的 kb_root, 它**硬要求**该目录下存在 `ROUTING.md` + `INDEX.md`
    两个导航文件。这两个文件**不在检索语料里** —— 实测:

        cards/*.md            = 961      含 `__` (即 `<study>__<form>__<item>.md`) = 959
        不含 `__` 的           = INDEX.md + ROUTING.md 两个
        chroma `study_st01`   = 959      ⇒ 与含 `__` 的数量逐一相等

    而 spec §4 闸 2 的口径是「没有任何一张 **field card** 同时含全部 probe 词」。
    把导航文件算进来量的就不是那件事: `INDEX.md` 是一张**列全部 form 名的表**,
    任意两个 form 级词都会在它里面双双命中, 于是闸 D 对着一段**不可检索**的内容判红。

    方向上"过严"不等于安全: 闸 D 的筛掉率直接喂给 spec §7 那条 **>50% 停止条款**,
    而该条款的作用是**否掉 C1 的整个价值假设**。用虚高的分子触发它, 会得出
    "文档与卡片高度重叠、C1 没价值"的**错误结论**, 真相却只是我们扫了一张导航表。
    这不是保守, 是量错了东西。

    判据用命名形态而不是硬编码两个文件名: field card 恒为 `<study>__<form>__<item>.md`,
    导航文件恒无 `__`。将来 kb_root 下再多一个导航文件也自动被排除。

    空语料必须响亮失败 (与 `lint_gold.doc_chunk_names` 逐字同一处理): 静默返回 `{}`
    会让闸 D **整闸白送** —— 没有卡片可撞, `hit` 恒空, 每题判绿。而 `Path.glob` 对
    **不存在**的目录也不报错、只给空迭代, 所以打错一个 `--cards-dir` 就够了:
    闸 D 变 no-op 且以退出码 0 全绿收工。同一系列里两个语料装载器对空目录给相反处理
    是最坏形态, 故这里照抄先写那个的选择 —— 宁可现在炸。
    **守卫必须在过滤之后**: 一个只有导航文件、没有 field card 的目录同样是空语料。
    """
    out = {p.name: p.read_text(encoding="utf-8")
           for p in sorted(Path(cards_dir).glob("*.md"))
           if "__" in p.name}
    if not out:
        raise ValueError(
            f"cards_dir 无 field card (形如 `<study>__<form>__<item>.md`), "
            f"空语料会让闸 D 每题判绿: {cards_dir}")
    return out


def gate_fact_length(questions: list[dict]) -> list[GateFinding]:
    findings: list[GateFinding] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        facts = q.get("expected_facts") or []
        if not facts:
            findings.append(GateFinding("fact_length", qid, "缺 expected_facts"))
            continue
        for fact in facts:
            if len(fact) >= FACT_MIN_LEN or _ID_SHAPED.fullmatch(fact):
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
        if not isinstance(terms, list):
            # YAML 标量 (`card_probe_terms: TERM_A`) 长度 >= 2 会滑过下面的守卫, 然后
            # **逐字符**当 probe 词 —— 单字符几乎撞不上"全部命中", 于是静默判绿。
            findings.append(GateFinding(
                "card_unanswerable", qid,
                f"card_probe_terms 不是列表 (拿到 {type(terms).__name__}) — "
                "YAML 标量会被逐字符当 probe 词, 静默判绿"))
            continue
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


def probe_binding(questions: list[dict],
                  cards: dict[str, str]) -> list[tuple[str, list[int], bool]]:
    """每题各 probe 词**单独**命中的卡数, 以及闸 D 对该题**是否可能变红**。

    ## 存在的理由 (2026-08-11 实测逼出, 批 1 的 12 题里 11 题踩中)

    闸 D 判的是 `all(t in card_text for t in terms)`。只要**任一** probe 词单独命中
    **0 张卡**, 该合取对每张卡恒 False ⇒ **闸 D 结构上不可能变红**。实测批 1:

        q01[0,0] q02[0,0] q03[1,0] q04[0,0] q05[0,3] q08[0,0]
        q09[8,0] q11[1,0] q12[10,2]✓ q14[0,0] q15[0,0] q16[186,0]
        ⇒ 12 题里闸 D 真正施加了约束的只有 1 题

    那 11 题的绿灯**不可证伪** —— 它不是"卡片答不出"的独立检验, 只是"我挑的词不在
    任何卡里"的复述。**而不可证伪的绿灯, 和通过了的检验, 长得一模一样。**

    ## 为什么只打印、不设阈值、不设闸、不改退出码

    照抄本仓 `lint_gold.or_groups` 的选择 (它只打印 OR 组成员数而不设成员数阈值,
    docstring 已论证过"拍脑袋的常数会把排序搞反")。这里是同一情形: 我们无法为
    "probe 词该命中几张卡"定一个有原则的阈值 ——

    - 0 命中**不等于**坏题: 词在 959 张卡里一次都不出现, 本身就是"EDC 里没有这个概念"
      的真实证据 (如临床假设类词汇, EDC 本就不会有)。
    - 但 0 命中**也可能**是"卡片用另一套措辞写同一概念"。**本函数分不开这两种** ——
      分开它们需要语义判断, 那是 spec §4 要求另抽 N=6 走实测复核的活。

    设成闸就会把上面第一种情形误杀, 并逼出"为了让闸变难而改 probe 词"——
    那与"红了改词"是同一种病、反方向。故: **只保证后人看得见这道闸对该题有没有
    约束力, 判断留给人。**

    ## 为什么只回计数、不回 probe 词本身

    probe 词是研究文档的日文词汇。本函数的输出会被贴进 `evidence/checkpoints/`,
    而那个目录**进 git**、红线是"零正文零真名"。回计数 (位置对应 `card_probe_terms`
    的顺序) 就够定位, 且贴进证据不泄漏原文。

    Returns: `[(qid, [各 probe 词的命中卡数], 闸 D 是否可触发), ...]`
    """
    low = [t.lower() for t in cards.values()]
    out: list[tuple[str, list[int], bool]] = []
    for q in questions:
        terms = q.get("card_probe_terms") or []
        if not isinstance(terms, list):
            # 标量 probe 词已由闸 D 自己报 finding; 这里只保证不炸且判为不可触发。
            out.append((q.get("id", "<no id>"), [], False))
            continue
        counts = [sum(1 for text in low if str(t).lower() in text) for t in terms]
        binding = len(terms) >= 2 and all(c > 0 for c in counts)
        out.append((q.get("id", "<no id>"), counts, binding))
    return out


def run_all_gates(test_set_path: Path | str, docs_dir: Path | str,
                  cards_dir: Path | str) -> list[GateFinding]:
    """四道闸的唯一汇总点 —— Task 5-7 的每道新题都靠它决定能否入池。

    `questions` 只加载一次并喂给闸 B/C/D, 闸 A 收路径 (内部经 `lint_gold._load` 加载),
    但两条路径都落到 `lint_gold.load_questions` 这一份实现上, 所以四道闸判的是同一批题。
    `test_all_gates_see_the_same_question_set` 钉住这件事。
    """
    questions = load_questions(test_set_path)
    bodies = chunk_bodies(docs_dir)
    cards = card_texts(cards_dir)
    return (gate_gold_unique(test_set_path, docs_dir)
            + gate_anchor_unique(questions, bodies)
            + gate_fact_length(questions)
            + gate_card_unanswerable(questions, cards))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="doc 侧题集四道入池闸 (确定性, 零 LLM)")
    ap.add_argument("test_set")
    ap.add_argument("--docs-dir", required=True)
    ap.add_argument("--cards-dir", required=True)
    ap.add_argument("--json", help="把 findings 另存为 JSON (收口证据用)")
    args = ap.parse_args(argv)

    findings = run_all_gates(args.test_set, args.docs_dir, args.cards_dir)
    questions = load_questions(args.test_set)
    n_q = len(questions)
    for f in findings:
        print(f"[{f.gate}] {f.qid}: {f.detail}")
    if args.json:
        Path(args.json).write_text(
            json.dumps([f.__dict__ for f in findings], ensure_ascii=False, indent=2),
            encoding="utf-8")

    # 闸 D 可触发性 —— **无阈值可见性, 不设闸、不改退出码** (见 probe_binding docstring)。
    binding = probe_binding(questions, card_texts(args.cards_dir))
    for qid, counts, ok in binding:
        verdict = "可触发" if ok else "**不可触发** (任一词 0 命中 ⇒ 合取恒空, 绿灯不可证伪)"
        print(f"[probe] {qid}: 各 probe 词单独命中卡数 {counts} — 闸 D {verdict}")
    n_bind = sum(1 for _, _, ok in binding if ok)

    print(f"\n计分题 {n_q} 道 · {len(findings)} 条 finding "
          f"(闸 B 只挡字面, 语义等价看不见 — 引用绿灯时必须同时写这句)")
    print(f"闸 D 对 {n_bind}/{n_q} 题有约束力 "
          f"— 其余题的绿灯不可证伪, 只说明所选 probe 词不在任何卡里, "
          f"**不构成**「卡片答不出」的独立检验")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
