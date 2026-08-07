"""section 级 gold 必须在索引里真实存在 —— 否则静默恒 miss。

用 `路径#节` / `路径#节$` 精确匹配后, gold 与 chunker 的 section 命名**强耦合**。重灌索引
若改了命名 (加前缀 / 重编号 / 去引号), gold 会无声失效: 题目一直低分, 而看不出是判据坏了
还是检索坏了 —— 正是 `check_source_recall` docstring 里那句"打错的 gold 恒 miss, 比多匹配
更隐蔽"。**Task 8 要重灌索引, 故本闸必须先于它就位。**

`test_terminology_usage_line.py` 里已有同形态的 `unresolved` 检查, 但它只覆盖指向
`terminology/core` 的那些 gold; 本闸是**全题集**版本 (实测 2026-08-07: 49 条 / 37 题)。

**匹配用 `eval.run_eval.source_matches`, 不在这里重写** (run_eval 硬规矩 1): 判据检查工具
与判据必须逐字同语义。闸若有第二份匹配实现, 它自己就会漂移 —— 上一轮 lint 剥 `.md` 后匹配
制造 8 条假阳性, 并连锁导致出题人删掉合法 gold, 就是这么来的。
"""
from __future__ import annotations

import pytest

from eval.run_eval import load_test_set, source_matches

TEST_SET = "eval/test_set_v3.yml"


def _section_golds() -> list[tuple[str, str]]:
    """题集里所有 section 级 gold, 返回 [(qid, gold)]。

    走 `load_test_set` 而非裸 `yaml.safe_load`: 它顺带拦"gold 键拼错"(拼错的键被静默忽略,
    该题白得满分)。本闸只读 gold, 但没有理由绕过既有校验。
    """
    out = []
    for q in load_test_set(TEST_SET):
        golds = (q.get("expected_sources") or []) + (q.get("expected_sources_any") or [])
        for g in golds:
            if "#" in str(g):
                out.append((q["id"], g))
    return out


def _indexed_pairs() -> tuple[list[str], list[str | None]]:
    """索引里全部 (source, section), 去重后拆成 source_matches 要的两条等长列表。"""
    from server.config import settings
    from server.rag import RAGEngine

    try:
        rag = RAGEngine(
            chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
            collection_name=settings.collection_name,
            embedding_model=settings.embedding_model, top_k=1,
        )
        got = rag.collection.get(include=["metadatas"])
    except Exception as exc:  # 无索引的环境跳过, 与既有集成测试同策
        pytest.skip(f"needs live index: {exc}")

    pairs = sorted(
        {((m.get("source") or ""), m.get("section")) for m in got["metadatas"]},
        key=lambda p: (p[0], p[1] or ""),
    )
    return [src for src, _ in pairs], [sec for _, sec in pairs]


def test_there_are_section_golds_to_check():
    """护栏的护栏: 若这里变成 0, 上面的解析八成坏了, 而下面的测试会空转通过。

    下限 40 对实测 49 条 (2026-08-07, Task 3 补 gold 之后) 留了退役余量; 解析坏掉时
    返回的是 0 或个位数, 与"少了几条 gold"分得开。
    """
    golds = _section_golds()
    assert len(golds) >= 40, (
        f"只解析到 {len(golds)} 条 section 级 gold, 期望 >=40 (实测 49) —— "
        "解析逻辑或题集结构可能变了"
    )


def test_every_section_gold_exists_in_index():
    """每条 section 级 gold 都要在索引里找得到对应 chunk。

    判定与真实判据同一函数: 把**整个索引**当作"被召回的 chunk"喂给 `source_matches` ——
    连全库都匹配不上的 gold, 在任何一次评测里都不可能命中。
    """
    sources, sections = _indexed_pairs()
    assert sources, "索引里一个 chunk 都没有 —— 先重建索引再跑本闸"

    missing = [f"{qid}: {gold}" for qid, gold in _section_golds()
               if not source_matches(gold, sources, sections)]

    assert not missing, (
        "以下 section 级 gold 在索引里不存在 —— 它们会静默恒 miss:\n  "
        + "\n  ".join(missing)
    )
