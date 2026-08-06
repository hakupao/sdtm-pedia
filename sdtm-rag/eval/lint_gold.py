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


def _load(test_set_path, catalog_path) -> tuple[list[dict], list[str]]:
    catalog = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
    data = yaml.safe_load(Path(test_set_path).read_text(encoding="utf-8"))
    qs = data["questions"] if isinstance(data, dict) else data
    return [q for q in qs if not q.get("out_of_scope")], _card_names(catalog)


def _count(gold: str, qid: str, names: list[str]) -> list[str]:
    if "#" in gold:
        # `路径#节` 在 check_source_recall 下是双条件匹配, 需要 retrieved_sections;
        # catalog 里没有 section 信息, 本工具建模不了。宁可报错也不静默按字面数 ——
        # 那正是本文件要消灭的"工具与判据不同语义"。
        raise ValueError(
            f"{qid}: section 级 gold {gold!r} 无法由 catalog 建模 "
            "(study 卡无 section)。card 级 gold 请写完整卡名。"
        )
    return [n for n in names if gold in n]


def lint_gold(test_set_path, catalog_path, max_matches: int = 1) -> list[Finding]:
    """返回所有"匹配卡数 != 期望"的 gold, AND 侧与 OR 侧同查。

    max_matches=1 要求唯一定位; 家族题可显式放宽 (与出题人声明的家族规模一致)。
    **放宽只作用于 AND 侧**: OR 组本身已是"任一成员命中即得分"的放宽, 再叠加家族
    放宽等于两层稀释相乘, 而 OR 正是最容易制造虚高的地方。
    """
    qs, names = _load(test_set_path, catalog_path)
    findings: list[Finding] = []
    for q in qs:
        for side, key, allowed in (
            ("AND", "expected_sources", q.get("gold_max_matches", max_matches)),
            ("OR", "expected_sources_any", 1),
        ):
            for gold in (q.get(key) or []):
                hits = _count(gold, q["id"], names)
                if len(hits) != allowed:
                    findings.append(Finding(q["id"], gold, len(hits), sorted(hits)[:3], side))
    return findings


def or_groups(test_set_path, catalog_path) -> list[tuple[str, list[int]]]:
    """每个 OR 组的成员匹配数, 用于**无条件**打印可见性行。

    为什么只打印不设成员数阈值 (2026-08-06 实测, n=21 题 / 105 召回槽位):
    多加一个成员白买的命中率取决于该成员与检索结果的相关性, 不是成员数 ——
    同 form 兄弟卡 6.0%, 全库随机卡 0.52%, 差 12 倍。计数阈值会把"3 个跨 form
    成员"判得比"2 个同 form 成员"更危险, 排序是反的。且逐成员唯一定位闸通过后,
    组的总覆盖卡数恒等于成员数, 确定性信息已被榨干 —— 再加阈值只能是拍脑袋的常数。
    故此处只保证审题人每次都看见 OR 组, 语义上"每个成员能否独立回答该题"由人判。
    """
    qs, names = _load(test_set_path, catalog_path)
    return [(q["id"], [len(_count(g, q["id"], names)) for g in q["expected_sources_any"]])
            for q in qs if q.get("expected_sources_any")]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="lint study golden gold 唯一性")
    ap.add_argument("test_set")
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--max-matches", type=int, default=1)
    args = ap.parse_args(argv)
    findings = lint_gold(args.test_set, args.catalog, args.max_matches)
    for f in findings:
        verdict = "匹配 0 卡 (gold 打错?)" if f.n_matches == 0 else f"匹配 {f.n_matches} 卡"
        print(f"{f.qid}: [{f.side}] {verdict} — 期望唯一定位")
    for qid, counts in or_groups(args.test_set, args.catalog):
        print(f"[OR] {qid}: {len(counts)} 成员 (各匹配 {'/'.join(map(str, counts))} 卡) "
              "— OR 不增分母, 成员越多越易命中; 请人工确认每个成员都能独立回答该题")
    print(f"\n{len(findings)} 条 gold 未唯一定位")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
