# regenerate v2 baselines + full census + per-unit reconcile (repo root)
T=.work/10_tier_b_repair
python3 -I $T/scripts/table_census.py --pages ig34:275-284 --kb knowledge_base/domains/PC/examples.md knowledge_base/domains/PP/examples.md knowledge_base/domains/PC/assumptions.md --out $T/work/census_BPCPP.v2.json | head -1
python3 -I $T/scripts/helpers/reconcile.py $T/work/census_BPCPP.json $T/work/census_BPCPP.v2.json | grep -v "lost=\[\] new=\[\]$"
python3 -I $T/scripts/table_census.py --pages ig34:248-264 --kb knowledge_base/domains/MB/assumptions.md knowledge_base/domains/MB/examples.md --out $T/work/census_mut_MB.v2.json | head -1
python3 -I $T/scripts/table_census.py --pages ig34:185-193 --kb knowledge_base/domains/EG/assumptions.md knowledge_base/domains/EG/examples.md --out $T/work/census_mut_EG.v2.json | head -1
for n in EG CP TR MB; do pg=$(python3 -I -c "import json;print(json.load(open('$T/work/census_t1/ig34_domains_$n.json'))['pages'])"); python3 -I $T/scripts/table_census.py --pages $pg --kb knowledge_base/domains/$n/assumptions.md knowledge_base/domains/$n/examples.md --out $T/work/scratch/census_fix/$n.v2.json >/dev/null; echo "-- $n"; python3 -I $T/scripts/helpers/reconcile.py $T/work/census_t1/ig34_domains_$n.json $T/work/scratch/census_fix/$n.v2.json | grep -v "lost=\[\] new=\[\]$"; done
python3 -I $T/scripts/table_census.py --manifest $T/work/census_full_manifest.json --out $T/work/census_full.json | head -1
