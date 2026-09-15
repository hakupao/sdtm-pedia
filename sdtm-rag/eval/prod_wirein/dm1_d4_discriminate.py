"""DM1 D4 区分实验: study 侧 gold 候选卡 0/32 到底是「问句→卡片语义鸿沟」还是「席位/切分问题」。

判据 (跑前登记, 见 evidence/checkpoints/dm1_d4_discrimination.md §0):
  臂 A body   : 卡片正文 (去 frontmatter) 当 query, 卡片自身进 top-8?  —— 索引/席位/切分是否健康
  臂 B title  : 卡片 `# [...]` 标题行当 query                          —— 只凭 表单名+项目名+OID 能否召回
  臂 C label  : 仅日文 表单 label + 项目 label (无任何 OID)             —— 用户自然说法能否召回
  臂 D defn   : 该域 assumptions.md item_1 定义段原文当 query            —— 管线现有原料 (定义→卡片) 有没有桥
    A ≥ 90% 且 C ≥ 50% 且 D ≈ 0  → 语义鸿沟 (SDTM 概念 ↔ EDC 日文 label 无桥), 走人手表/别名
    A < 90%                       → 席位/切分/索引问题, 先修检索层, 人手表不是对症药

引擎 = repro_t5_study_expand.build 同构 (联邦里那台 study cards 引擎, 扩写按 settings 实收)。
⚠ 本文件不写 study OID / 表单名 / 日文标签; 全部从 gitignored 题集与卡片读, 产物写 gitignored runs/.

跑 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/dm1_d4_discriminate.py \
    > data/study/st01/eval/runs/dm1_d4_discriminate.txt 2>&1
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import yaml  # noqa: E402

from eval.prod_wirein.repro_t5_study_expand import build, form_of  # noqa: E402
from server.config import settings  # noqa: E402
from server.domain_expand import build_expander  # noqa: E402

TEST_SET = Path("data/study/st01/eval/test_set_domain_mapping_v1.yml")
CARDS = Path("data/study/st01/cards")
KB = Path(settings.kb_root)
JUDGE_N = 8
_TITLE_RE = re.compile(r"^# \[(?P<form_label>.+?) (?P<form>[A-Z0-9_]+)\] (?P<item_label>.+?) \((?P<item>[A-Z0-9_]+)\)\s*$")


def card_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    return parts[2].strip() if len(parts) == 3 else text.strip()


def card_title(body: str) -> str:
    return next(l for l in body.splitlines() if l.startswith("# "))


def card_label_only(title: str) -> str:
    m = _TITLE_RE.match(title)
    if not m:
        return title
    return f"{m['form_label']} {m['item_label']}"


def domain_definition(domain: str) -> str:
    text = (KB / "domains" / domain / "assumptions.md").read_text(encoding="utf-8")
    # 取正文第一段落 (item_1 对应的首条假设), 与 rag._definition_chunk 口径一致: 首条
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith("#")]
    return paras[0] if paras else text[:600]


def main() -> int:
    rows = yaml.safe_load(TEST_SET.read_text(encoding="utf-8"))
    eng = build(build_expander(settings))
    print(f"test_set={TEST_SET}  judge_n={JUDGE_N}  engine=study cards (T5 同构, expander ON)")

    arms = ("A_body", "B_title", "C_label")
    hit = Counter()
    total = 0
    rank_sum = Counter()
    per_q_defn = {}
    seen_cards: set[str] = set()
    for row in rows:
        qid, domain = row["id"], row["domain"]
        gold = [g for g in row["expected_sources"] if form_of(g)]
        # 臂 D: 定义段 → 该题 gold 卡 (按题, 不按卡)
        defn_srcs = [c.source for c in eng.retrieve(domain_definition(domain))][:JUDGE_N]
        d_hit = sum(1 for s in defn_srcs if s in set(gold))
        d_forms = Counter(form_of(s) or "cdisc" for s in defn_srcs)
        per_q_defn[qid] = (d_hit, len(gold), dict(d_forms))
        print(f"\n{qid} [{domain}] D_defn: gold_hit={d_hit}/{len(gold)} top{JUDGE_N} forms={dict(d_forms)}")
        for g in gold:
            if g in seen_cards:      # dm01-03 同 gold, 只算一次
                continue
            seen_cards.add(g)
            total += 1
            body = card_body(CARDS / g)
            title = card_title(body)
            queries = {"A_body": body, "B_title": title, "C_label": card_label_only(title)}
            line = f"  {g:40s}"
            for arm in arms:
                srcs = [c.source for c in eng.retrieve(queries[arm])]
                rank = next((i + 1 for i, s in enumerate(srcs) if s == g), None)
                ok = rank is not None and rank <= JUDGE_N
                hit[arm] += ok
                rank_sum[arm] += rank if rank else 99
                line += f" {arm}={'HIT' if ok else 'miss'}@{rank or '-'}"
            print(line)

    print(f"\n=== 合计 ({total} 张 gold 卡, 去重) ===")
    for arm in arms:
        print(f"{arm}: {hit[arm]}/{total} = {hit[arm]/total:.0%}  (mean rank, miss=99: {rank_sum[arm]/total:.1f})")
    d_total = sum(v[0] for v in per_q_defn.values())
    d_gold = sum(v[1] for v in per_q_defn.values())
    print(f"D_defn (定义段→gold 卡, 按题): {d_total}/{d_gold} = {d_total/d_gold:.0%}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
