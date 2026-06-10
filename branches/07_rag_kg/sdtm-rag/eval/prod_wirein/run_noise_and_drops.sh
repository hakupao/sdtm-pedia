#!/bin/bash
# (1) noise-floor: re-run OFF arm at temp=0 to measure DeepSeek non-determinism envelope.
# (2) drops forensic: full off/on text for the 10 paired-eval fact DROPS (judge needs it).
set -e
cd "$(dirname "$0")/../.."
PY=.venv/bin/python
echo "[$(date +%H:%M:%S)] START noise+drops"
echo "[$(date +%H:%M:%S)] === noise-floor: OFF re-run #2 ==="
$PY eval/run_eval.py eval/test_set_v2.yml --structured-lookup --hybrid --temperature 0.0 \
    --tag g_off2 --output eval/prod_wirein/g_off2_t0.json 2>&1 | tail -16
echo "[$(date +%H:%M:%S)] === drops forensic (10 drop questions) ==="
$PY eval/prod_wirein/forensic_guardrail.py forensic_drops.json \
    q02 q24 q06 q28 q35 q39 q17 q20 q67 q81 2>&1 | tail -14
echo "[$(date +%H:%M:%S)] DONE noise+drops"
