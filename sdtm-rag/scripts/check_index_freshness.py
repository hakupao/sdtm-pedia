"""部署前置检查: 向量库是否还对得上 knowledge_base/ (陈旧则非零退出).

用法 (deploy.sh / 手动):
    .venv/bin/python -m scripts.check_index_freshness

陈旧时退出码 1 —— 接进 deploy 流程即可阻断"改了 KB 却忘了重灌"这类静默漂移。
背景与判定口径见 `scripts/kb_freshness.py` 的模块 docstring。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from scripts.kb_freshness import check_freshness

_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_KB = _ROOT.parent / "knowledge_base"
_DEFAULT_STAMP = _ROOT / "data" / "chroma" / "ingested_at_commit.txt"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kb-root", default=str(_DEFAULT_KB))
    ap.add_argument("--stamp", default=str(_DEFAULT_STAMP))
    args = ap.parse_args(argv)

    res = check_freshness(Path(args.stamp), Path(args.kb_root))
    if res.fresh:
        print(f"[index] OK — in sync with knowledge_base ({res.current[:12]}…)")
        return 0
    print(f"[index] STALE — {res.reason}")
    print("[index] fix: .venv/bin/python -m scripts.ingest   # 然后重启服务")
    return 1


if __name__ == "__main__":
    sys.exit(main())
