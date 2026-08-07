"""码表 gold 依赖的 `Used by variable(s):` 抬头必须真实存在 —— 它是切块时注入的。

**为什么需要这道闸 (硬规矩: 护栏不能自洽)**

Step 6 独立判定把 14 条 gold 补进了 `terminology/core/*.md` 的码表小节, 判定依据是这些
chunk 抬头的 `Used by variable(s): DM.SEX.` 这类交叉引用行 —— 它逐字回答了"变量 V 用哪个
码表 / 码表 C 覆盖哪些变量"。

但**那一行不在 `knowledge_base/` 正文里**: 它由 `scripts/chunkers/terminology.py` 在切块时
拼进 chunk 文本 (`chunk_text = f"Used by variable(s): {used_by}.\\n\\n" + chunk_text`)。
判据依赖生成器注入的内容, 就必须有独立的闸锁住那个注入 —— 否则日后改了 chunker 或关掉注入,
这 14 条 gold 会**静默失效变成永久假阴性**: 题目一直低分, 而看不出是判据坏了还是检索坏了。

**闸为什么是 gold 驱动而不是"所有码表 chunk 都必须有"**: 注入是有条件的 (仅当该码表的
CT code 出现在 §三 使用映射里)。实测 258 个 terminology chunk 只有 134 个 (51%) 带这行,
写成全量断言会当场误报。故这里只锁"**被 gold 依赖的那些**", 并随 gold 变化自动扩张。
"""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from server.config import settings

TEST_SET = "eval/test_set_v3.yml"
USAGE_PREFIX = "Used by variable(s):"
KB_ROOT = Path(settings.kb_root)


def _terminology_section_golds() -> list[tuple[str, str]]:
    """题集里所有指向 terminology/core 的 section 级 gold, 返回 [(qid, gold)]。"""
    with open(TEST_SET, encoding="utf-8") as f:
        qs = yaml.safe_load(f)
    out = []
    for q in qs:
        golds = (q.get("expected_sources") or []) + (q.get("expected_sources_any") or [])
        for g in golds:
            if "#" in str(g) and "terminology/core" in str(g):
                out.append((q["id"], g))
    return out


def _chunks():
    from server.rag import RAGEngine

    try:
        rag = RAGEngine(
            chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
            collection_name=settings.collection_name,
            embedding_model=settings.embedding_model, top_k=1,
        )
        got = rag.collection.get(include=["documents", "metadatas"])
    except Exception as exc:  # 无索引的环境跳过, 与既有集成测试同策
        pytest.skip(f"needs live index: {exc}")
    return got


def test_there_are_terminology_section_golds_to_check():
    """护栏的护栏: 若这里变成 0, 上面的解析八成坏了, 而下面的断言会空转通过。"""
    golds = _terminology_section_golds()
    assert len(golds) >= 10, (
        f"只解析到 {len(golds)} 条 terminology section 级 gold, 期望 >=10 —— "
        "解析逻辑或题集结构可能变了"
    )


def test_usage_line_is_injected_not_authored():
    """这行必须**不在** KB 正文里 —— 那正是它脆弱、需要本闸的原因。

    若哪天它真的被写进了 KB 正文, 本测试会红: 那是好消息 (依赖不再脆弱), 但届时应当
    重新评估本闸是否还需要, 而不是直接删掉断言。
    """
    hits = [p.relative_to(KB_ROOT).as_posix()
            for p in sorted((KB_ROOT / "terminology" / "core").glob("*.md"))
            if USAGE_PREFIX in p.read_text(encoding="utf-8")]
    assert not hits, (
        f"{USAGE_PREFIX!r} 现在出现在 KB 正文里了 ({hits[:3]}) —— "
        "它原本是 chunker 注入的; 依赖关系变了, 请重新评估本闸"
    )


def test_every_terminology_gold_chunk_carries_the_usage_line():
    """每条 terminology section 级 gold 指向的 chunk 必须带注入的抬头。

    这是那 14 条 gold 成立的**唯一**前提: 判定方判的是 chunk 正文, 而正文里能把码表连到
    题干变量的就只有这一行。抬头没了, gold 还在 —— 那就是恒 miss 的假阴性。
    """
    got = _chunks()
    by_key: dict[tuple[str, str | None], str] = {}
    for doc, meta in zip(got["documents"], got["metadatas"]):
        by_key[((meta.get("source") or ""), meta.get("section"))] = doc

    unresolved, no_line = [], []
    for qid, gold in _terminology_section_golds():
        path, sec = gold.split("#", 1)
        if sec.endswith("$"):
            sec = sec[:-1]
        docs = [d for (src, s), d in by_key.items() if path in src and s == sec]
        if not docs:
            unresolved.append(f"{qid}: {gold}")
        elif not docs[0].startswith(USAGE_PREFIX):
            no_line.append(f"{qid}: {gold} -> chunk 开头是 {docs[0][:40]!r}")

    assert not unresolved, (
        "以下 gold 在索引里找不到对应 chunk (会静默恒 miss):\n  " + "\n  ".join(unresolved))
    assert not no_line, (
        f"以下 gold 依赖的 chunk 已不带 {USAGE_PREFIX!r} 抬头 —— 判据将变成永久假阴性:\n  "
        + "\n  ".join(no_line))


def test_injection_still_alive_at_scale():
    """整体注入机制没被关掉 (防"逐条都还在, 但机制已废"的假绿)。

    实测 2026-08-07: 258 个 terminology chunk 中 134 个带该抬头 (51%)。注入是有条件的
    (仅当码表 CT code 在 §三 使用映射里), 故这里用下限而非全量相等。
    """
    got = _chunks()
    term = [d for d, m in zip(got["documents"], got["metadatas"])
            if "terminology/core" in (m.get("source") or "")]
    assert term, "索引里没有 terminology/core chunk"
    with_line = [d for d in term if d.startswith(USAGE_PREFIX)]
    assert len(with_line) >= 100, (
        f"带 {USAGE_PREFIX!r} 抬头的 terminology chunk 只剩 {len(with_line)}/{len(term)}, "
        "低于下限 100 —— 注入机制可能被关掉或大面积失效"
    )
