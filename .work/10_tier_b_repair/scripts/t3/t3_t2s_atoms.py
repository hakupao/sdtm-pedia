#!/usr/bin/env python3
"""T3 S2 input: explicit T2S atom list -> work/t3_t2s_atoms.jsonl.
Only S-* writer rows whose ref names atom ids AND whose action is a fix (INSERTED/REPLACED/TABLE_REBUILT/MOVED...)
are taken; VERIFIED / SKIPPED_* / DELETED / D6 rows and atom ids merely mentioned in checkpoints are NOT.
Each row: atom_id, batch, action, kb_file, writer ptr (file:line), checkpoint ptr (file:line|None), review/audit ptr, commit.
Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_t2s_atoms.py
"""
import collections, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t3_common import ROOT, CK, ck_lines, W, FIX_ACTIONS, atom_order, expand_ref, writer_rows, ck_line_of, ck_find, verdict_ptr, batch_commits

order, idx = atom_order()
triage = {t["atom_id"] for t in json.load(open(f"{W}/triage_merged.json"))}
commits = batch_commits()
out, unparsed, skipped = [], [], collections.Counter()
for b, wf, n, r in writer_rows():
    if not b.startswith("S-"):
        continue
    ids, bad = expand_ref(str(r["ref"]), idx, order)
    if bad:
        unparsed.append((b, f"{wf}:{n}", r["ref"], bad))
    if not ids:
        continue
    if r["action"] not in FIX_ACTIONS:
        skipped[r["action"]] += len(ids)
        continue
    for i in ids:
        ck = ck_line_of(b, i) or ck_line_of(b, ids[0])  # range members fall back to the range head's line
        if not ck:  # raw ref text, then '<file>:<kb_line_after>' as the checkpoint change table writes it
            stem = "/".join(r["kb_file"].split("/")[-2:])
            ck = ck_find(b, [str(r["ref"]), f"{stem}:{r['kb_line_after']}", f"{os.path.basename(r['kb_file'])}:{r['kb_line_after']}"])
        if not ck:  # page-row tables in scan checkpoints: '| 92 | … a002 a003 …'
            pg, an = re.match(r"\w+_p(\d{4})_(a\d+)", i).groups()
            p = f"{CK}/t2_{b}.md"
            num = int(an[1:])
            def names(l):  # 'a011' as a token, or inside an 'a010-a013' range on the line
                return re.search(rf"(?<![\w]){an}(?![\w])", l) or any(int(x) <= num <= int(y) for x, y in re.findall(r"\ba(\d+)-a(\d+)\b", l))
            ck = next((f"{os.path.relpath(p, ROOT)}:{n}" for n, l in enumerate(ck_lines(p), 1)
                       if names(l) and (f"| {int(pg)} |" in l or f"p{int(pg)}" in l)), None)
        out.append(dict(atom_id=i, batch=b, action=r["action"], kb_file=r["kb_file"], writer=f"{wf}:{n}",
                        checkpoint=ck, review=verdict_ptr(b, "review"), audit=verdict_ptr(b, "audit"),
                        commit=commits.get(b), in_triage=i in triage))
with open(f"{W}/t3_t2s_atoms.jsonl", "w", encoding="utf-8") as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
u = {r["atom_id"] for r in out}
print(f"rows={len(out)} unique_atoms={len(u)} in_triage={len(u & triage)} not_in_triage={len(u - triage)}")
print("by batch:", dict(collections.Counter(r["batch"] for r in out)))
print("by action:", dict(collections.Counter(r["action"] for r in out)))
print("atom refs with non-fix action (not taken):", dict(skipped))
nock = [r for r in out if r["checkpoint"] is None]
print("no checkpoint line:", len(nock), sorted({(r["batch"], r["writer"]) for r in nock})[:20])
print("  (writer row pointer is present for every row)", " no review/audit ptr:",
      sum(not (r["review"] and r["audit"]) for r in out), " no commit:", sum(r["commit"] is None for r in out))
print("unparsed ref parts:", len(unparsed))
for x in unparsed:
    print("  UNPARSED", *x)
