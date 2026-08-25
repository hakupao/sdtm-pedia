"""gold 唯一性 lint — 把"期望来源必须唯一定位"变成可执行闸。

动机: gold 写成家族前缀 (`..__FAM_`) 时, 子串匹配下召回**任意**一张同族卡都判满分,
答错也得分。v1.1 有一条这样的 gold 匹配 17 张卡, 该题判别力≈0。

**本工具必须与 `check_source_recall` 逐字同语义** (这是本文件唯一的正确性要求):
判据末行是 `any(exp in src for src in retrieved_sources)` —— gold **原样**去匹配
retrieval 返回的**完整 source 串**, 不做任何规范化。study 侧的 source 实测是裸文件名
`<study>__<form>__<item>.md` (无目录前缀), 所以 `.md` **参与匹配且有判别力**:
`…__ITEM_R.md` 不是 `…__ITEM_RX.md` 的子串 (R 后面是 `.` 不是 `X`)。

初版曾先剥掉 `.md` 再匹配无后缀卡名, 比真实判据**严**, 于是把 12 条带 `.md` 的合法 gold
中的 8 条报成多匹配。连锁后果: 出题人为迁就假阳性删过合法 gold。教训是判据检查工具
一旦与被检查的判据不同语义, 就会制造连锁误判 —— 故 `test_lint_semantics_match_check_source_recall`
直接钉住两者等价, 改任一侧都会红。

不改 `check_source_recall` 本身 (改了历史 run 就不可复算), 只在出题侧设闸。
0 匹配同样报 —— 打错的 gold 恒 miss, 比多匹配更隐蔽。

**两个 gold 键都查** (`_GOLD_KEYS`): `expected_sources` (AND) 与 `expected_sources_any`
(OR)。OR 组不增加分母却多一次命中机会, `check_source_recall` 的 docstring 记过一次
实际翻车 —— 正是最该查的地方, 而初版只查 AND 侧, 只写 OR 的题 (v2 q20 形态) 整题零覆盖。
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class Finding:
    qid: str
    gold: str
    n_matches: int
    matched_sample: list[str]
    side: str = "AND"          # gold 来自 expected_sources / expected_sources_any


def _card_names(catalog: dict) -> list[str]:
    """卡名带 `.md`, 与 retrieval 返回的 source 串逐字一致。"""
    study = catalog["study"]
    return [f"{study}__{it['form_oid']}__{it['item_oid']}.md" for it in catalog["items"]]


def doc_chunk_names(docs_dir: Path | str) -> list[str]:
    """doc 侧 gold 全集 = docs/ 下的文件名 (带 `.md`)。

    与 retrieval 返回的 `source` 元数据逐字一致 (ingest_study 写的就是 `p.name`),
    所以这里和 catalog 侧一样, `.md` 参与匹配且有判别力。

    空目录必须响亮失败: 名字全集为空时"匹配数 != 1"对每条 gold 恒成立, 闸会
    全红看似严格; 但若将来有人把 0 匹配当成"跳过", 就变成恒绿。宁可现在炸。
    """
    names = sorted(p.name for p in Path(docs_dir).glob("*.md"))
    if not names:
        raise ValueError(f"docs_dir 无 md 文件, 空全集不可用作 gold 全集: {docs_dir}")
    return names


def event_target_names(catalog_path: Path | str) -> list[str]:
    """event 侧 gold 的全集: 三池各自的目标名 (与 catalog ledger 的 target 同构).

    命名与 build_catalog 的 ledger target 保持一致, 让 gold 可直接对照台账溯源。
    """
    cat = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
    names: list[str] = []
    for e in cat.get("events", []):
        names.append(f"event:{e['oid']}")
    for a in cat.get("activities", []):
        names.append(f"activity:{a['event_oid']}/{a['oid']}")
    for s in cat.get("assignments", []):
        names.append(f"assignment:{s['event_oid']}/{s['activity_oid']}/{s['form_oid']}")
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        raise ValueError(f"duplicate event target names: {sorted(dupes)[:5]}")
    # 空全集必须响亮失败 (同 doc_chunk_names 的纪律): 三池全空时"匹配数 != 1"对每条
    # gold 恒成立, 闸会全红看似严格; 但若把 0 匹配的空全集当成合法返回值, 将来某次
    # catalog 路径拼错/三池字段名改了, 闸会悄悄退化成"每条 gold 都不唯一定位"这种
    # 噪音, 而不是在此处直接报错指出"根本没读到数据"。
    if not names:
        raise ValueError(
            f"catalog 三池 (events/activities/assignments) 全为空, "
            f"空全集不可用作 gold 全集: {catalog_path}"
        )
    return names


def load_questions(test_set_path: Path | str) -> list[dict]:
    """题集读取的**唯一实现** —— 所有闸必须判同一批题。

    此前 `docs_gold_gates` 有一份逐字相同的副本: 闸 A 走这里, 闸 B/C/D 走那里。
    将来任一侧加个跳过标志 (如 `draft: true`), 两道闸就会**判不同的题集且不报错** ——
    与本文件 `_load` 那句"两个 gold 全集不可混用"同一类失败, 只是从"全集"挪到了"题集"。
    """
    data = yaml.safe_load(Path(test_set_path).read_text(encoding="utf-8"))
    qs = data["questions"] if isinstance(data, dict) else data
    return [q for q in qs if not q.get("out_of_scope")]


def _load(test_set_path, catalog_path=None, docs_dir=None,
          events_catalog=None) -> tuple[list[dict], list[str]]:
    given = sum(x is not None for x in (catalog_path, docs_dir, events_catalog))
    if given != 1:
        raise ValueError(
            "catalog 与 docs-dir 与 events-catalog 必须且只能给一个 —— 三个 gold 全集不可混用"
        )
    if catalog_path is not None:
        names = _card_names(json.loads(Path(catalog_path).read_text(encoding="utf-8")))
    elif docs_dir is not None:
        names = doc_chunk_names(docs_dir)
    else:
        names = event_target_names(events_catalog)
    return load_questions(test_set_path), names


def match_names(gold: str, qid: str, names: list[str]) -> list[str]:
    """gold → 它匹配到的名字列表。**"哪些 chunk 算这题的 gold" 的唯一实现。**

    公开 (原 `_count`) 是因为闸 B 也要问这个问题。若闸 B 自己写一个 `g in n` 推导式,
    就是第二份匹配语义 —— 本文件开头记的那场翻车 (工具与判据不同语义, 真实题集上
    8 条假阳性) 会在闸 A / 闸 B 之间重演: 两道闸对同一条 gold 给出不同的 chunk 集合。
    """
    if "#" in gold:
        # `路径#节` 在 check_source_recall 下是双条件匹配, 需要 retrieved_sections;
        # catalog 里没有 section 信息, 本工具建模不了。宁可报错也不静默按字面数 ——
        # 那正是本文件要消灭的"工具与判据不同语义"。
        raise ValueError(
            f"{qid}: section 级 gold {gold!r} 无法由 catalog 建模 "
            "(study 卡无 section)。card 级 gold 请写完整卡名。"
        )
    return [n for n in names if gold in n]


def lint_gold(test_set_path, catalog_path=None, max_matches: int = 1, *,
              docs_dir=None, events_catalog=None) -> list[Finding]:
    """返回所有"匹配卡数 != 期望"的 gold, AND 侧与 OR 侧同查。

    max_matches=1 要求唯一定位; 家族题可显式放宽 (与出题人声明的家族规模一致)。
    **放宽只作用于 AND 侧**: OR 组本身已是"任一成员命中即得分"的放宽, 再叠加家族
    放宽等于两层稀释相乘, 而 OR 正是最容易制造虚高的地方。
    """
    qs, names = _load(test_set_path, catalog_path, docs_dir, events_catalog)
    findings: list[Finding] = []
    for q in qs:
        for side, key, allowed in (
            ("AND", "expected_sources", q.get("gold_max_matches", max_matches)),
            ("OR", "expected_sources_any", 1),
        ):
            for gold in (q.get(key) or []):
                hits = match_names(gold, q["id"], names)
                if len(hits) != allowed:
                    findings.append(Finding(q["id"], gold, len(hits), sorted(hits)[:3], side))
    return findings


def or_groups(test_set_path, catalog_path=None, *, docs_dir=None,
              events_catalog=None) -> list[tuple[str, list[int]]]:
    """每个 OR 组的成员匹配数, 用于**无条件**打印可见性行。

    为什么只打印不设成员数阈值 (2026-08-06 实测, n=21 题 / 105 召回槽位):
    多加一个成员白买的命中率取决于该成员与检索结果的相关性, 不是成员数 ——
    同 form 兄弟卡 6.0%, 全库随机卡 0.52%, 差 12 倍。计数阈值会把"3 个跨 form
    成员"判得比"2 个同 form 成员"更危险, 排序是反的。且逐成员唯一定位闸通过后,
    组的总覆盖卡数恒等于成员数, 确定性信息已被榨干 —— 再加阈值只能是拍脑袋的常数。
    故此处只保证审题人每次都看见 OR 组, 语义上"每个成员能否独立回答该题"由人判。
    """
    qs, names = _load(test_set_path, catalog_path, docs_dir, events_catalog)
    return [(q["id"], [len(match_names(g, q["id"], names)) for g in q["expected_sources_any"]])
            for q in qs if q.get("expected_sources_any")]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="lint study golden gold 唯一性")
    ap.add_argument("test_set")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--catalog", help="card 侧 gold 全集来源")
    src.add_argument("--docs-dir", help="doc 侧 gold 全集来源 (章节 chunk 目录)")
    src.add_argument("--events-catalog", help="event 侧 gold 全集来源 (catalog.json 三池)")
    ap.add_argument("--max-matches", type=int, default=1)
    args = ap.parse_args(argv)
    findings = lint_gold(args.test_set, args.catalog, args.max_matches,
                          docs_dir=args.docs_dir, events_catalog=args.events_catalog)
    for f in findings:
        verdict = "匹配 0 卡 (gold 打错?)" if f.n_matches == 0 else f"匹配 {f.n_matches} 卡"
        print(f"{f.qid}: [{f.side}] {verdict} — 期望唯一定位")
    for qid, counts in or_groups(args.test_set, args.catalog, docs_dir=args.docs_dir,
                                  events_catalog=args.events_catalog):
        print(f"[OR] {qid}: {len(counts)} 成员 (各匹配 {'/'.join(map(str, counts))} 卡) "
              "— OR 不增分母, 成员越多越易命中; 请人工确认每个成员都能独立回答该题")
    print(f"\n{len(findings)} 条 gold 未唯一定位")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
