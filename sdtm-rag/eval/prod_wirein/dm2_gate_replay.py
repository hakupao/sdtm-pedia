"""DM2 研读包答案闸 §4 离线回放 —— 零 LLM, 实跑前必过.

spec: docs/superpowers/specs/2026-09-25-dossier-output-gate-design.md §4.
读 gitignored runs/dm2_e2e_{claude,attempt4,attempt5,attempt6}/judge_pack.json 共 42 份已独立判分的
答案, 逐份跑 server.dossier_gate.check_answer, 与下面写死的预期 (以判分方逐 run 结论为真值) 比对.

跑 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/dm2_gate_replay.py

⚠ 只打印数量与 attempt/qid/model/语言, **不打印 OID 本身** (输出可能被贴进提交的证据文件).
  预期表同理只写数量, 不写 OID.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from server.config import settings  # noqa: E402
from server.dossier_gate import OidIndex, check_answer  # noqa: E402

# attempt 名 → runs/ 下目录名 (attempt 3 = Claude 两模型那一批, 目录沿用当时的名字).
ATTEMPT_DIRS = {"attempt3": "dm2_e2e_claude", "attempt4": "dm2_e2e_attempt4",
                "attempt5": "dm2_e2e_attempt5", "attempt6": "dm2_e2e_attempt6"}
N_EXPECTED = 42

# spec §4: 未列出的 run 一律预期 0 个未知 OID、观测语言 = 问句语言 (假阳性 = 0).
EXPECTED_UNKNOWN = {
    ("attempt3", "dm07", "opus-5"): 1,    # 1 个项目 OID
    ("attempt3", "dm07", "sonnet-5"): 3,  # 3 个表单 OID
    ("attempt5", "dm09", "opus-5"): 1,    # 1 个示例 OID
}
EXPECTED_LANG_DRIFT = {                   # (expected, observed)
    ("attempt3", "dm01", "opus-5"): ("zh", "ja"),
    ("attempt3", "dm05", "sonnet-5"): ("en", "ja"),
    ("attempt4", "dm05", "sonnet-5"): ("en", "ja"),
    ("attempt6", "dm10", "opus-5"): ("zh", "ja"),
}


def main() -> int:
    study_dir = Path(settings.study_kb_root).parent
    index = OidIndex.from_catalog(study_dir / "catalog.json", settings.kb_root)
    rows, fails = 0, 0
    for attempt, sub in ATTEMPT_DIRS.items():
        pack = json.loads((study_dir / "eval" / "runs" / sub / "judge_pack.json")
                          .read_text(encoding="utf-8"))
        for run in pack["runs"]:
            key = (attempt, run["qid"], run["model"])
            r = check_answer(run["answer"], run["question"], index)
            exp_n = EXPECTED_UNKNOWN.get(key, 0)
            exp_lang = EXPECTED_LANG_DRIFT.get(key)
            lang_ok = ((r.lang_expected, r.lang_observed) == exp_lang if exp_lang
                       else r.lang_observed == r.lang_expected)
            ok = len(r.unknown_oids) == exp_n and lang_ok
            rows += 1
            fails += not ok
            print(f"{'PASS' if ok else 'FAIL'}  {attempt} {run['qid']} {run['model']:9s} "
                  f"unknown_oids={len(r.unknown_oids)} (expect {exp_n})  "
                  f"lang={r.lang_expected}->{r.lang_observed}"
                  f" (expect {'->'.join(exp_lang) if exp_lang else 'match'})  gate_ok={r.ok}")
    if rows != N_EXPECTED:
        print(f"# FAIL: replayed {rows} runs, expected {N_EXPECTED}")
        return 1
    print(f"# replay: {rows - fails}/{rows} PASS" + ("" if not fails else f", {fails} FAIL"))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
