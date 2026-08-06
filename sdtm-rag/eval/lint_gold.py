"""gold 唯一性 lint — 把"期望来源必须唯一定位"变成可执行闸。

动机 (2026-08-06 勘察): v1.1 的 42 条 gold 里 9 条是多卡匹配。`check_source_recall`
是**子串**匹配, 所以 gold 写成家族前缀 (`..__FAM_`) 或写成兄弟卡的子串
(`ITEM_R` ⊂ `XITEM_R`) 时, 召回**任意**一张匹配卡都判满分 —— 答错也得分。
最极端的一例是一条 gold 匹配 17 张卡, 该题判别力≈0。

本工具不改 `check_source_recall` 的语义 (改了历史 run 就不可复算), 而是在出题侧
把这类 gold 拦下来。0 匹配同样报 —— 打错的 gold 恒 miss, 比多匹配更隐蔽。
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
    study = catalog["study"]
    return [f"{study}__{it['form_oid']}__{it['item_oid']}" for it in catalog["items"]]


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
            key = gold[:-3] if gold.endswith(".md") else gold
            hits = [n for n in names if key in n]
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
