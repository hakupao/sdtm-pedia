"""DM1 final-review finding I3: 140q CDISC 集是否真的把 D1 (锚定小写域码正则)
的安全性过了一遍, 还是只是凑巧没碰到。

旧 = D1 之前的域识别 (大写 token pass `_QUERY_VAR_TOKEN_RE` 落在 domain_to_spec
里, 加长名 pass `_query_longname_domains`); 新 = `_query_domains` (含 D1 的
`_ANCHORED_CODE_RE`/`_PREFIXED_CODE_RE` 锚定小写/任意大小写域码识别)。

跑 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/dm1_d1_140q_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import yaml  # noqa: E402

from server.config import settings  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402
from server.structured_lookup import (  # noqa: E402
    _ANCHORED_CODE_RE,
    _PREFIXED_CODE_RE,
    _QUERY_VAR_TOKEN_RE,
    StructuredLookup,
)

TEST_SET = Path("eval/test_set_v3.yml")


def old_domains(lookup: StructuredLookup, query: str) -> list[str]:
    """域识别 pre-D1 口径: 大写 token pass + 长名 pass, 没有锚定小写/任意大小写正则。"""
    out: list[str] = []
    for tok in _QUERY_VAR_TOKEN_RE.findall(query):
        if tok in lookup.domain_to_spec and tok not in out:
            out.append(tok)
    for code in lookup._query_longname_domains(query):
        if code not in out:
            out.append(code)
    return out


def main() -> int:
    lookup = StructuredLookup(settings.kb_root, MetaStore(settings.meta_path))
    questions = [row["question"] for row in yaml.safe_load(TEST_SET.read_text(encoding="utf-8"))]

    regex_hits = 0
    diffs = []
    for q in questions:
        regex_hits += len(_ANCHORED_CODE_RE.findall(q)) + len(_PREFIXED_CODE_RE.findall(q))
        old, new = old_domains(lookup, q), lookup._query_domains(q)
        if old != new:
            diffs.append((q, old, new))

    print(f"{TEST_SET}: {len(questions)} questions")
    print(f"D1 正则 (_ANCHORED_CODE_RE + _PREFIXED_CODE_RE) 命中次数: {regex_hits}")
    print(f"旧/新域名识别不同的题数: {len(diffs)}")
    for q, old, new in diffs:
        print(f"  DIFF {q!r}: old={old} new={new}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
