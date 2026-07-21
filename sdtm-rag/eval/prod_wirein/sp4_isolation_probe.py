"""SP4 Gate 3 — production must be byte-identical with Neo4j stopped vs running.
Dumps the deterministic composite resolve() output for a fixed 12-query battery.
Run twice (Neo4j down / up), then `diff` the two dumps.
Run: .venv/bin/python eval/prod_wirein/sp4_isolation_probe.py /tmp/sp4_iso_<state>.json"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.config import settings          # noqa: E402
from server.main import maybe_build_answerer  # noqa: E402

BATTERY = [
    # SP2 结构化 (计数/穷举/属性/CT)
    "How many domains are in the SDTM IG?",
    "Which domains contain the variable TAETORD?",
    "What are the variables in the DM domain?",
    "Which codelist does DTHFL use?",
    "Is AESER required in AE?",
    # AGG 聚合
    "Which variables appear in at least 30 domains?",
    "What's the most reused controlled terminology?",
    # SP3 图 (impact / relationship)
    "What is affected if codelist C66742 changes?",
    "Which domains are impacted by changing EPOCH?",
    "How is AE related to other domains?",
    "Which domains belong to the same class as VS?",
    # 检索型 (通道应 silent — None 也是被钉住的输出)
    "What does the EX domain describe?",
]


def main() -> None:
    out = Path(sys.argv[1])
    answerer = maybe_build_answerer(settings)
    assert answerer is not None, "composite channels off — flags drifted?"
    dump = []
    for q in BATTERY:
        facts = answerer.resolve(q)
        dump.append({"query": q, "facts": None if facts is None else asdict(facts)})
    out.write_text(json.dumps(dump, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"wrote {out} ({sum(1 for d in dump if d['facts']) } fired / {len(dump)})")


if __name__ == "__main__":
    main()
