"""DM1 T5: study 侧引擎在域码扩写 OFF/ON 下到底检索到什么 —— 可复跑的尺子。

为什么单独有这个脚本: T5 报告对"扩写在 study 侧起没起作用"下过结论, 而那个结论最初来自
一次一次性的肉眼观察 (没有命令、没有产物)。按本仓纪律, 「实测」必须附可复跑命令 —— 假实测
比缺陷更害人, 它让下一个人跳过复验。

量的是**联邦里那台 study cards 引擎单独的检索**, 不是联邦合并后的结果 (合并后 CDISC 的 15
席吃满, study 侧出不出现看的是席位分配, 那是另一个问题)。

判据是**从 gold 推出来的**, 不是手挑的: 每题 gold 卡片的表单集合 = 该题的"目标表单", 然后数
top-N 里有几条落在目标表单内。手挑一个表单名去数会变成对着答案调参 (而且换一题就失效)。

⚠ 本文件不写任何 study OID / 表单名 / 日文标签 —— 问句与 gold 全部从 gitignored 的题集读,
产物写到同样 gitignored 的 runs/ 下。

跑 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/repro_t5_study_expand.py \
    > data/study/st01/eval/runs/dm1_t5_study_expand_repro.txt 2>&1
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import yaml  # noqa: E402

from server.config import settings  # noqa: E402
from server.domain_expand import build_expander  # noqa: E402
from server.rag import RAGEngine  # noqa: E402
from server.study_lookup import StudyLookup  # noqa: E402

TEST_SET = Path("data/study/st01/eval/test_set_domain_mapping_v1.yml")
TOP_N = 5          # 与报告里那句话同口径
DEEP_N = 15        # 引擎的 top_k: gold 到底进没进席


def form_of(source: str) -> str | None:
    """study 卡片文件名的表单段。形如 <study>__<FORM>__<ITEM>.md; 非此形状返回 None
    (CDISC 侧的 source 是路径, 不该被当成表单)。"""
    parts = Path(source).stem.split("__")
    return parts[1] if len(parts) >= 3 else None


def build(expander) -> RAGEngine:
    """联邦里那台 study cards 引擎的同构型复制 (S1 恒关, S2 开, hybrid 随 settings)。"""
    return RAGEngine(
        chroma_dir=settings.chroma_dir,
        kb_root=settings.study_kb_root,
        collection_name=settings.study_collection_name,
        embedding_model=settings.embedding_model,
        top_k=DEEP_N,
        structured_lookup_enabled=False,
        study_lookup=StudyLookup.from_paths(
            settings.study_catalog_path, settings.study_aliases_path),
        hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion,
        hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
        domain_expander=expander,
    )


def main() -> int:
    rows = yaml.safe_load(TEST_SET.read_text(encoding="utf-8"))
    engines = {"OFF": build(None), "ON": build(build_expander(settings))}

    totals = {arm: {"in_form": 0, "gold": 0} for arm in engines}
    print(f"test_set={TEST_SET}  top_n={TOP_N}  deep_n={DEEP_N}")
    print("in_form = top5 里落在该题 gold 表单集合内的条数; gold = top15 里命中的 gold 卡数\n")
    for row in rows:
        qid, question = row["id"], row["question"]
        gold = [g for g in row.get("expected_sources", []) if form_of(g)]
        gold_forms = {form_of(g) for g in gold}
        print(f"{qid}: gold_cards={len(gold)} gold_forms={len(gold_forms)}")
        for arm, eng in engines.items():
            srcs = [c.source for c in eng.retrieve(question)]
            in_form = sum(1 for s in srcs[:TOP_N] if form_of(s) in gold_forms)
            hit = sum(1 for s in srcs[:DEEP_N] if s in set(gold))
            totals[arm]["in_form"] += in_form
            totals[arm]["gold"] += hit
            print(f"   {arm:3} in_form={in_form}/{TOP_N}  gold={hit}/{len(gold)}")
        print()

    print("=== 合计 (8 题) ===")
    for arm, t in totals.items():
        print(f"{arm:3} in_form={t['in_form']}  gold_hit={t['gold']}")
    d = totals["ON"]["in_form"] - totals["OFF"]["in_form"]
    print(f"\nin_form 差 (ON - OFF) = {d:+d}")
    print(f"gold_hit 差 (ON - OFF) = {totals['ON']['gold'] - totals['OFF']['gold']:+d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
