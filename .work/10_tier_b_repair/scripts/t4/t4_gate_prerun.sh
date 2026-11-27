#!/bin/bash
# Current outputs for a T4.1 gate reviewer that has no shell (feature-dev:code-reviewer): every command the gate asks for is
# run here on the current HEAD and logged verbatim. Read-only on knowledge_base/ (mutations run on scratch copies), on the
# working ledger and on every tracked file except the log itself.
# Usage (repo root): bash .work/10_tier_b_repair/scripts/t4/t4_gate_prerun.sh [LOG]   (default work/t4/gate_prerun.log)
set -u
R=/Volumes/DevSSD/Project/sdtm-pedia
T=.work/10_tier_b_repair
cd "$R" || exit 1
LOG=${1:-$T/work/t4/gate_prerun.log}
S=$T/work/scratch/t4/gate_prerun; mkdir -p "$S"
run() { echo; echo "\$ $*"; "$@" 2>&1; echo "[exit=$?]"; }
{
  echo "# gate pre-run $(date -u +%Y-%m-%dT%H:%M:%SZ)  HEAD $(git rev-parse --short HEAD)  KB tree $(git rev-parse HEAD:knowledge_base)"
  echo "# ledger md5 $(md5 -q $T/work/coverage_ledger.wc.jsonl)  registry rows $(wc -l < $T/work/t2_pdf_typo_registry.jsonl | tr -d ' ')"
  run git status --short
  run git status --short knowledge_base archive releases
  echo; echo "## G-TB7 links"
  echo '$ python3 tools/check_links.py 2>&1 | grep "live docs"'; python3 tools/check_links.py 2>&1 | grep "live docs"
  echo; echo "## G-TB1 / G-TB2 (section recompute -> scratch)"
  echo "\$ python3 -I $T/scripts/t3_recompute.py --out $S/sc.jsonl | grep TB:"; python3 -I $T/scripts/t3_recompute.py --out "$S/sc.jsonl" | grep "TB:"
  echo; echo "## G-TB3 coverage"
  run python3 -I $T/scripts/t4/t4_coverage_decomp.py
  echo; echo "## final verdict counts"
  python3 -I -c "
import json,collections
c=collections.Counter(json.loads(l)['verdict'] for l in open('$T/work/coverage_ledger.wc.jsonl') if l.strip()); print(dict(c), 'rows', sum(c.values()))"
  echo; echo "## direct-hit recheck (stock EXACT in scope + TB EXACT)"
  run python3 -I $T/scripts/t3/t3_direct_hit.py --out "$S/direct_hit.json"
  echo; echo "## G-TB4 full census on HEAD (-> scratch)"
  echo "\$ python3 -I $T/scripts/table_census.py --manifest $T/work/census_full_manifest.json --out $S/census_head.json | tail -2"
  python3 -I $T/scripts/table_census.py --manifest $T/work/census_full_manifest.json --out "$S/census_head.json" | tail -2
  echo; echo "## G-TB9 t3 mutation"
  echo "\$ bash $T/scripts/t3/t3_mutation.sh | grep -E 'RESULT|real KB md5|unchanged|^== '"; bash $T/scripts/t3/t3_mutation.sh 2>&1 | grep -E "RESULT|real KB md5|unchanged|^== "
  echo; echo "## G-TB9 t0 mutation on the current KB"
  echo "\$ bash $T/scripts/t4/t0_mutation_head.sh | sed -n '/^real KB md5 (after)/,\$p'"; bash $T/scripts/t4/t0_mutation_head.sh 2>&1 | sed -n '/^real KB md5 (after)/,$p'
  echo; echo "## G-TB6 reverse trace on the working tree (-> scratch)"
  echo "\$ python3 -I $T/scripts/t3/t3_reverse_trace.py --rev WORKTREE --out $S/reverse_trace.json | tail -25"
  python3 -I $T/scripts/t3/t3_reverse_trace.py --rev WORKTREE --out "$S/reverse_trace.json" 2>&1 | tail -25
  echo; echo "## R2L + R3L + R4L change set (pre-R2L backup vs working ledger; R3L alone = pre-R3L vs pre-R4L backup; R4L alone = pre-R4L backup vs working ledger) and overlap with every judged sample"
  run python3 -I $T/scripts/t4/t4_r2l_sample_overlap.py
  echo; echo "## ack list: PDF_TYPO / ATOM_ERR / FIG by decision source (regenerated to scratch, compared with the committed file)"
  echo "\$ grep -c '(未归因)' $T/evidence/checkpoints/t4_ack_lists.md"; grep -c '(未归因)' $T/evidence/checkpoints/t4_ack_lists.md
  echo "\$ sed -n '1,12p' $T/evidence/checkpoints/t4_ack_lists.md"; sed -n '1,12p' $T/evidence/checkpoints/t4_ack_lists.md
  echo; echo "## ATOM_ERR add-on check (S1-R1): parsed verdicts of the 83 atoms; per-atom verdict rows for every ATOM_ERR / PDF_TYPO; scenario numbers"
  echo "\$ python3 -I $T/scripts/t4/t4_atomerr_report.py | grep -v 'second-look pack'"; python3 -I $T/scripts/t4/t4_atomerr_report.py 2>&1 | grep -v 'second-look pack'
  run python3 -I $T/scripts/t4/t4_atomerr_coverage.py
  echo; echo "## sample files"
  run md5 -r $T/work/t4/gate_sample.jsonl $T/work/t4/human_sample.jsonl $T/work/t4/supp/supp_sample.jsonl $T/work/t4/q9/q9_sample.jsonl $T/work/t4/round2/round2_sample.jsonl $T/work/t4/round2/round2b_sample.jsonl $T/work/t4/round3/round3_sample.jsonl $T/work/t4/atomerr/atomerr_sample.jsonl $T/work/t4/atomerr/atomerr_population.json $T/work/t4/atomerr/verdicts.json
  echo; echo "## working-ledger backups / derived data md5"
  run md5 -r $T/work/coverage_ledger.wc.jsonl $T/work/coverage_ledger.wc.pre_r2l.jsonl $T/work/coverage_ledger.wc.pre_r3l.jsonl $T/work/coverage_ledger.wc.pre_r4l.jsonl $T/work/t2_pdf_typo_registry.jsonl $T/work/t4_r2l_relabel.json $T/work/t4_r3l_relabel.json $T/work/t4_r4l_relabel.json $T/work/t3_k3b_out_of_scope_keep.json $T/work/t3_errata.json $T/work/t3_rules.json $T/work/t3_writeback_decisions.json $T/work/t4/supp/scenarios.json $T/work/t4/supp/relabel_pending.json
  echo; echo "## after"
  echo "KB tree $(git rev-parse HEAD:knowledge_base); ledger md5 $(md5 -q $T/work/coverage_ledger.wc.jsonl)"
  run git status --short knowledge_base archive releases
} > "$LOG" 2>&1
echo "wrote $LOG"; tail -3 "$LOG"
