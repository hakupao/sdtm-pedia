#!/usr/bin/env python3
"""One-off fixation (T4 问题 C 改台账 R4L, 规格 subagent_prompts/t4/t4_round4_ledger_spec_v1.0.md §1) -> work/t4_r4l_relabel.json.
relabel: the NOT_HOLD atoms of the add-on check (work/t4/atomerr/verdicts.json; asserted: exactly 1) — the ATOM_ERR
  (S1-R1) label came only from a t1_errata t3_atom_err note; the two independent reviewers found atom = PDF and KB = PDF.
  t3_errata_build.py revokes that errata entry; t3_writeback.py decides the atom by the existing live-hit path (asserted).
registry_ptr: 4 ATOM_ERR atoms whose row lacks the registry id the reviewers named (t4_atomerr_fullcheck.md §5b);
  pointer only — t3_writeback.py appends the id to evidence.registry, label / rule / batch unchanged.
Asserts: raw file:line exist; registry ids exist, are 'KB 写正确值' and sit within ±1 page of the atom (p337_a003 sits
on p336); the reviewer note names the same registry id. Idempotent. Run once; afterwards the JSON is the source.
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_r4l_build.py
"""
import json, os
TB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = f"{TB}/work"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
REG = {r["id"]: r for r in lj(f"{W}/t2_pdf_typo_registry.jsonl")}
A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
V = json.load(open(f"{W}/t4/atomerr/verdicts.json", encoding="utf-8"))
DEC = "owner 2026-11-27 问题 C = C1 (evidence/checkpoints/t4_owner_confirmation.md 消息 5)"
SPEC = "subagent_prompts/t4/t4_round4_ledger_spec_v1.0.md §1"
SECOND = "evidence/t4_atomerr_raw/second_look.md"
# §5b of evidence/checkpoints/t4_atomerr_fullcheck.md (spec §1 last item); the p339 row's registry id carries its copy suffix
PTR = {"ig34_p0161_a0012": "B-DS T-4", "ig34_p0337_a003": "B-RS T-3", "ig34_p0339_a001": "B-RS T-6 (RS 副本)",
       "ig34_p0361_a016": "B-FA T-2"}


def raw_ok(p):
    f, n = p.rsplit(":", 1)
    return os.path.exists(f"{TB}/{f}") and int(n) <= len(open(f"{TB}/{f}", encoding="utf-8").read().splitlines())


def line_of(f, needle):
    return next((f"{f}:{n}" for n, l in enumerate(open(f"{TB}/{f}", encoding="utf-8"), 1) if l.startswith("|") and needle in l), None)


nh = sorted(i for i, v in V.items() if v["verdict"] == "NOT_HOLD")
assert nh == ["ig34_p0124_a001"], nh
rel = {}
for i in nh:
    v = V[i]
    raw = [f"{v['file']}:{v['line']}", line_of(SECOND, i)]
    assert all(raw) and all(raw_ok(p) for p in raw), raw
    assert "NOT_HOLD" in open(f"{TB}/{SECOND}", encoding="utf-8").read().splitlines()[int(raw[1].rsplit(':', 1)[1]) - 1], raw
    rel[i] = dict(group="atomerr-not-hold", now="ATOM_ERR", to="EXACT", raw=raw, decision=DEC,
                  why="两位互不知情的独立审查者 (tracer / general-purpose) 都判 NOT_HOLD: 原子与 PDF 逐格一致 (没抽错), "
                      "KB 与 PDF 逐字一致; ATOM_ERR 只出自 t1_errata t3_atom_err 的一句 B-ML review 顺带话",
                  revoke="t1_errata.t3_atom_err", spec=SPEC)
ptr = {}
for i, rid in PTR.items():
    v, r = V[i], REG[rid]
    raw = f"{v['file']}:{v['line']}"
    assert raw_ok(raw) and v["verdict"] == "HOLDS" and v["registry_note"], (i, v["verdict"])
    assert rid.split(" (")[0] in v["note"] and r["handling"].startswith("KB 写正确值"), (i, rid)
    assert abs(r["pdf_page"] - A[i]["page"]) <= 1, (i, rid, r["pdf_page"], A[i]["page"])
    ptr[i] = dict(add=[rid], raw=raw, decision="t4_atomerr_fullcheck.md §5b (只补登记指针; 规格 §1 末项)", spec=SPEC)
out = dict(_note="T4 问题 C 改台账 R4L (主人 2026-11-27 直接回答 C1; evidence/checkpoints/t4_owner_confirmation.md 消息 5). "
                 "relabel: 1 条 ATOM_ERR → EXACT; t3_errata_build.py 撤销它的 t1 errata 条目 (断言: 只因这条 errata 才是 ATOM_ERR), "
                 "t3_writeback.py 让它进允许集并由现有 live-hit 路径判定 (断言 rule = live-hit, 终态 = to). "
                 "registry_ptr: 4 条 ATOM_ERR 只补 evidence.registry (断言标签 / 规则不变). 生成: scripts/t4/t4_r4l_build.py (一次性).",
           relabel=dict(sorted(rel.items())), registry_ptr=dict(sorted(ptr.items())))
json.dump(out, open(f"{W}/t4_r4l_relabel.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("r4l relabel", sorted(rel), "| registry_ptr", {i: p["add"] for i, p in ptr.items()})
