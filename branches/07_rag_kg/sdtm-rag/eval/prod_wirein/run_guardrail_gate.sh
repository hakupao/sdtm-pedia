#!/bin/bash
# Paired guardrail gate: OFF vs ON (retrieval levers ON, DeepSeek temp=0, v2 102q) + forensic.
set -e
cd "$(dirname "$0")/../.."
PY=.venv/bin/python
echo "[$(date +%H:%M:%S)] START guardrail gate"
echo "[$(date +%H:%M:%S)] === ARM 1/3: guardrail OFF ==="
$PY eval/run_eval.py eval/test_set_v2.yml --structured-lookup --hybrid --temperature 0.0 \
    --tag g_off --output eval/prod_wirein/g_off_t0.json 2>&1 | tail -20
echo "[$(date +%H:%M:%S)] === ARM 2/3: guardrail ON ==="
$PY eval/run_eval.py eval/test_set_v2.yml --structured-lookup --hybrid --temperature 0.0 --guardrail \
    --tag g_on --output eval/prod_wirein/g_on_t0.json 2>&1 | tail -20
echo "[$(date +%H:%M:%S)] === ARM 3/3: forensic full answers (off vs on, 16q subset) ==="
$PY eval/prod_wirein/forensic_guardrail.py 2>&1 | tail -20
echo "[$(date +%H:%M:%S)] DONE guardrail gate"
