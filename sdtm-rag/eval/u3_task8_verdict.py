"""U3 Task 8 Step 3: 六条条款逐条判定 (plan Task 8 Step 3 原脚本 + spec §7.1 处置 #2 多数类基线并排).

复跑: ./.venv/bin/python eval/u3_task8_verdict.py
"""
import collections
import json

after = [json.load(open(f'data/study/st01/eval/runs/u3_after_run_{i}.json')) for i in (1, 2, 3)]
base = [json.load(open(f'data/study/st01/eval/runs/u3_baseline_run_{i}.json')) for i in (1, 2, 3)]


def g(run, name, key='exact'):
    return run['summary']['by_group'][name][key]


print('=== 条款 1: 三遍每一遍 fatal_excl_final==0 且 legacy_exact>=178 ===')
c1 = all(r['summary']['fatal_excl_final'] == 0 and r['summary']['legacy_exact'] >= 178
         for r in after)
for i, r in enumerate(after, 1):
    print(f'  r{i}: fatal={r["summary"]["fatal_excl_final"]} '
          f'legacy={r["summary"]["legacy_exact"]}/181 '
          f'fatal_ids={r["summary"]["fatal_ids_excl_final"]}')
print('  条款 1:', '未触发 (PASS)' if c1 else '⛔ 触发')

print('=== 条款 2: heldout% >= dev% - 25.0pt (三遍均值) ===')
dev = sum(g(r, 'dev') for r in after) / 3 / 12 * 100
hold = sum(g(r, 'heldout') for r in after) / 3 / 12 * 100
print(f'  dev={dev:.2f}%  heldout={hold:.2f}%  gap={dev-hold:.2f}pt')
print('  条款 2:', '未触发 (PASS)' if hold >= dev - 25.0 else '⛔ 触发')

print('=== 条款 3: dev exact >= 10/12 (三遍均值) ===')
print(f'  dev 均值 = {sum(g(r,"dev") for r in after)/3:.2f}/12')
print('  条款 3:', '未触发 (PASS)' if sum(g(r, 'dev') for r in after) / 3 >= 10 else '⛔ 触发')

print('=== 条款 4: distractor_cdisc 较基线下降 <= 1 题 ===')
b = sum(g(r, 'distractor_cdisc') for r in base) / 3
a = sum(g(r, 'distractor_cdisc') for r in after) / 3
print(f'  基线 {b:.2f}/12 → 改动后 {a:.2f}/12  drop={b-a:.2f}')
print('  条款 4:', '未触发 (PASS)' if b - a <= 1 else '⛔ 触发')

print('=== 条款 5: final 三题只报告, 不作判据 ===')
for i, r in enumerate(after, 1):
    fin = {d['id']: d['pred'] for d in r['detail'] if d['group'] == 'final'}
    print(f'  r{i}: {fin}')
print('  ⚠ 看到这三题结果后不许回头改 prompt (spec §7 条款 5)')

print('=== 条款 6: 三遍稳定性 ===')
preds = [{d['id']: d['pred'] for d in r['detail']} for r in after]
uns = {k: [p[k] for p in preds] for k in preds[0] if len({p[k] for p in preds}) > 1}
print(f'  unstable = {len(uns)}')
for k, v in uns.items():
    print('   ', k, v)

# spec §7.1 处置 #2: 多数类基线并排打出, 让读者一眼看到余量 (只加信息, 不动阈值)
print('=== 多数类基线并排 (spec §7.1 处置 #2) ===')
detail = after[0]['detail']
gold_all = collections.Counter(d['gold'] for d in detail)
maj_all, n_maj = gold_all.most_common(1)[0]
new42 = [d for d in detail if d['group'] in ('dev', 'heldout', 'distractor_cdisc', 'ambiguous_both')]
gold_42 = collections.Counter(d['gold'] for d in new42)
maj_42, n_maj42 = gold_42.most_common(1)[0]
print(f'  dev: 12 题全 gold=study → 「一律答 study」得 12/12 = 100% (条款 3 单独看零判别力)')
print(f'  heldout: 12 题全 gold=study → 同上 100% (条款 2 单独看零判别力)')
print(f'  新写 42 题: gold={dict(gold_42)} → 多数类 {maj_42} = {n_maj42}/42 = {n_maj42/42*100:.1f}%')
print(f'  全 253 题: gold={dict(gold_all)} → 多数类 {maj_all} = {n_maj}/253 = {n_maj/253*100:.1f}%')
print(f'  ⚠ 条款 2/3 的数字不得单独引用, 必须与条款 1/4 结果同时给出 (spec §7.1 处置 #1)')
