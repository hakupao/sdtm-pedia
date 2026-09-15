"""DM2 T8: 三个题集各有多少题会被 auto 触发 —— 140q 必须 0 (纯 CDISC 题不该整本喂).
DM2 终审 I2: 再核 gold 卡是否都在研读包 part B 里 (spec §7「part B 穷尽」断言的实测闸).

跑 (从 sdtm-rag/):  .venv/bin/python eval/prod_wirein/dm2_trigger_sweep.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import yaml  # noqa: E402
from server.config import settings  # noqa: E402
from server.dossier_trigger import decide_dossier  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402
from server.structured_lookup import StructuredLookup  # noqa: E402
from server.study_dossier import build_dossier  # noqa: E402

SETS = {
    "cdisc140": "eval/test_set_v3.yml",
    "study48": "data/study/st01/eval/test_set_study_v2.yml",
    "mapping8": "data/study/st01/eval/test_set_domain_mapping_v1.yml",
}
MAPPING_SET = SETS["mapping8"]
# gold 卡 basename 形状: st01__<FORM>__<ITEM>.md (非此形状的 expected_sources = CDISC chunk 路径)
_CARD_RE = re.compile(r"^st01__(?P<form>.+?)__(?P<item>.+)\.md$")


def gold_cards_in_part_b() -> None:
    """研读包 part B 是否逐条含 mapping 集的 gold 卡. part B 行形如
    `[<フォーム名> <FORM>] <項目名> (<ITEM>) | 型 ...` → 同一行同时含 ` <FORM>] ` 与 ` (<ITEM>) `.
    ⚠ 只打印计数与 id, 不打印 FORM/ITEM 本身 (红线: 不落 OID / 表单名)."""
    d = build_dossier(settings.dossier_docs_dir, settings.dossier_cards_dir,
                      sections=settings.dossier_prt_sections,
                      max_chars=settings.dossier_max_chars)
    part_b = d.text[d.text.index("## B."):]
    lines = part_b.splitlines()
    rows = yaml.safe_load(Path(MAPPING_SET).read_text(encoding="utf-8"))
    total = hit = 0
    uniq: dict[tuple[str, str], bool] = {}
    misses: list[str] = []
    for r in rows:
        for src in r.get("expected_sources", []):
            m = _CARD_RE.match(Path(src).name)
            if not m:
                continue
            key = (m["form"], m["item"])
            found = any(f" {key[0]}] " in ln and f" ({key[1]}) " in ln for ln in lines)
            total += 1
            hit += found
            uniq[key] = uniq.get(key, False) or found
            if not found:
                misses.append(r["id"])
    print(f"gold_cards_in_partB: {hit}/{total}")
    print(f"unique: {sum(uniq.values())}/{len(uniq)}")
    if misses:
        print(f"  MISS in: {sorted(set(misses))}")


def main() -> int:
    # ⚠ StructuredLookup.from_kb(...) 不存在; 照 server/rag.py:198 的写法构造
    lookup = StructuredLookup(settings.kb_root, MetaStore(settings.meta_path))
    for name, path in SETS.items():
        rows = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        fired = [r["id"] for r in rows if decide_dossier(r["question"], "auto", True, lookup._query_domains).attach]
        print(f"{name}: {len(fired)}/{len(rows)} fired  {fired if len(fired) <= 12 else fired[:12] + ['…']}")
    gold_cards_in_part_b()
    return 0

if __name__ == "__main__":
    sys.exit(main())
