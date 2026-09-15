"""DM2 T8: 三个题集各有多少题会被 auto 触发 —— 140q 必须 0 (纯 CDISC 题不该整本喂).

跑 (从 sdtm-rag/):  .venv/bin/python eval/prod_wirein/dm2_trigger_sweep.py
"""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import yaml  # noqa: E402
from server.config import settings  # noqa: E402
from server.dossier_trigger import decide_dossier  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402
from server.structured_lookup import StructuredLookup  # noqa: E402

SETS = {
    "cdisc140": "eval/test_set_v3.yml",
    "study48": "data/study/st01/eval/test_set_study_v2.yml",
    "mapping8": "data/study/st01/eval/test_set_domain_mapping_v1.yml",
}

def main() -> int:
    # ⚠ StructuredLookup.from_kb(...) 不存在; 照 server/rag.py:198 的写法构造
    lookup = StructuredLookup(settings.kb_root, MetaStore(settings.meta_path))
    for name, path in SETS.items():
        rows = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        fired = [r["id"] for r in rows if decide_dossier(r["question"], "auto", True, lookup._query_domains).attach]
        print(f"{name}: {len(fired)}/{len(rows)} fired  {fired if len(fired) <= 12 else fired[:12] + ['…']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
