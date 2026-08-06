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


def _card_names(catalog: dict) -> list[str]:
    """卡名带 `.md`, 与 retrieval 返回的 source 串逐字一致。"""
    study = catalog["study"]
    return [f"{study}__{it['form_oid']}__{it['item_oid']}.md" for it in catalog["items"]]


def lint_gold(test_set_path, catalog_path, max_matches: int = 1) -> list[Finding]:
    """返回所有"匹配卡数 != 期望"的 gold。max_matches=1 要求唯一定位;
    家族题可显式放宽 (与出题人声明的家族规模一致)。"""
    catalog = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
    names = _card_names(catalog)
    data = yaml.safe_load(Path(test_set_path).read_text(encoding="utf-8"))
    qs = data["questions"] if isinstance(data, dict) else data

    findings: list[Finding] = []
    for q in qs:
        if q.get("out_of_scope"):
            continue
        allowed = q.get("gold_max_matches", max_matches)
        for gold in (q.get("expected_sources") or []):
            if "#" in gold:
                # `路径#节` 在 check_source_recall 下是双条件匹配, 需要 retrieved_sections;
                # catalog 里没有 section 信息, 本工具建模不了。宁可报错也不静默按字面数 ——
                # 那正是本文件要消灭的"工具与判据不同语义"。
                raise ValueError(
                    f"{q['id']}: section 级 gold {gold!r} 无法由 catalog 建模 "
                    "(study 卡无 section)。card 级 gold 请写完整卡名。"
                )
            hits = [n for n in names if gold in n]
            if len(hits) != allowed:
                findings.append(Finding(q["id"], gold, len(hits), sorted(hits)[:3]))
    return findings


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="lint study golden gold 唯一性")
    ap.add_argument("test_set")
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--max-matches", type=int, default=1)
    args = ap.parse_args(argv)
    findings = lint_gold(args.test_set, args.catalog, args.max_matches)
    for f in findings:
        verdict = "匹配 0 卡 (gold 打错?)" if f.n_matches == 0 else f"匹配 {f.n_matches} 卡"
        print(f"{f.qid}: {verdict} — 期望唯一定位")
    print(f"\n{len(findings)} 条 gold 未唯一定位")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
