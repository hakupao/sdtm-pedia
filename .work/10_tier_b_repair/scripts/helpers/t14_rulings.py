"""T1.4 apply: build work/t1_rulings.json (overlay of user rulings R1/R2/R4 on triage_merged.json; lane files untouched).
Input = t1_merge.py --no-rulings output (regenerated into gitignored work/scratch/t14_apply/).
Each overlay entry: from (expected class before), to, ie_cat (IE only), rule, target (KB fix location, optional), note.
Run from repo root: python3 -I .work/10_tier_b_repair/scripts/helpers/t14_rulings.py
**冻结**: 它按行号读现 KB (R1 表行断言 / R4 逐字检查). T2 一旦开始改 KB 就不要再跑; work/t1_rulings.json 是冻结产物."""
import json, re, sys
sys.path.insert(0, "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/scripts")
from fp_match import norm
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
import subprocess
PRE = f"{TB}/work/scratch/t14_apply/triage_merged.pre_rulings.json"   # gitignored; regenerated each run
subprocess.run([sys.executable, "-I", f"{TB}/scripts/t1_merge.py", "--no-rulings", "--out", PRE], check=True, stdout=subprocess.DEVNULL)
M = {r["atom_id"]: r for r in json.load(open(PRE))}
A = {json.loads(l)["atom_id"]: json.loads(l) for l in open(f"{TB}/work/pdf_atoms.jsonl")}
X = {json.loads(l)["atom_id"]: json.loads(l) for l in open(f"{TB}/work/triage/review_extra.jsonl")}
O = {}

def put(aid, to, rule, ie_cat=None, target=None, note=None, recheck=False, frm=None):
    assert aid in M, aid
    assert aid not in O, ("dup", aid)
    e = {"from": frm or M[aid]["final_class"], "to": to, "rule": rule}
    if ie_cat: e["ie_cat"] = ie_cat
    if target: e["target"] = target
    if note: e["note"] = note
    if recheck: e["t2_recheck"] = True
    O[aid] = e

K = "knowledge_base/"
# ── R1: 70 VERSION_MISMATCH IE_CAND ─────────────────────────────────────────────────────────────────
vm = [a for a, r in M.items() if r["final_class"] == "IE_CAND" and r["ie_cat"] == "VERSION_MISMATCH"]
assert len(vm) == 70
for a in vm:
    at = A[a]
    if at["atom_type"] == "TABLE_ROW":
        # verified: KB row at kb_loc has #/name/label/type/role equal to the PDF row (role may carry "(qualifies)")
        f, ln = M[a]["kb_loc"].split(":")
        k = [x.strip() for x in open(f"{ROOT}/{f}").read().split("\n")[int(ln) - 1].strip().strip("|").split("|")]
        p = [x.strip() for x in at["verbatim"].split("|")]
        assert k[:4] == p[:4] and k[4].startswith(p[5]), a
        put(a, "IE", "R1-row", ie_cat="VERSION_MISMATCH", note="sv20 变量表行; model/ 5 列精简版 #/name/label/type/role 与 PDF 一致; 缺列不补")
    elif at["parent_section"].startswith("§1 [INTRODUCTION]"):
        put(a, "REAL_GAP", "R1-intro", target=K + "model/01_concepts_and_terms.md",
            note="sv20 §1 Introduction; model/01 从 §2 起 → 在 §2 前新增 §1 节 (PDF 原标题), 逐字补")
    elif at["parent_section"].startswith("§5.1.4.2"):
        put(a, "REAL_GAP", "R1-TD", target=K + "model/05_study_level_data.md",
            note="sv20 §5.1.4.2 TD 句; 归属 model/05 '### Trial Disease Assessments (TD)' 节; TD/assumptions.md:3 是 IG 层近义改写, 不改")
    else:
        raise SystemExit(f"R1 unclassified {a}")
# R1 siblings: every non-IE sv20 atom in the fix/present classes is prose -> keeps its class (no flips; listed in t1_r1_resolution)
for a, r in M.items():
    if a.startswith("sv20") and r["final_class"] != "IE_CAND":
        assert A[a]["atom_type"] not in ("TABLE_ROW", "TABLE_HEADER"), a

# ── targets for fix atoms whose kb_loc is null / ledger target wrong (lane notes; T1.3 verified) ──────────
for a in ("sv20_p0068_a012", "sv20_p0068_a019", "sv20_p0068_a020"):
    put(a, "REAL_GAP", "TARGET", target=K + "model/06_relationship_datasets.md:129", note="§6.6 APRELSUB; ledger 目标 model/04 错 (lane B)")
for a in ("sv20_p0008_a007", "sv20_p0008_a009"):
    put(a, "REAL_GAP", "TARGET", target=K + "model/01_concepts_and_terms.md", note="sv20 §2; 归属 model/01 (lane D, C10)")
for a in ("ig34_p0285_a009", "ig34_p0285_a010"):
    put(a, "REAL_GAP", "TARGET", target=K + "domains/NV/assumptions.md:5", note="§6.3.7 概述宿主 NV/assumptions.md (lane D/C)")
loc = [a for a, r in M.items() if r["final_class"] == "LOCATE"]
assert len(loc) == 28
for a in loc:
    put(a, "REAL_GAP", "LOCATE-LB", target=K + "domains/LB/assumptions.md:1",
        note="§6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补")
for a, src, tgt in (("ig34_p0363_a014", "chapters/ch02_fundamentals.md:219", "domains/FA/assumptions.md:62"),
                    ("ig34_p0364_a003", "chapters/ch02_fundamentals.md:227", "domains/FA/assumptions.md:62"),
                    ("ig34_p0364_a011", "model/02_observation_classes.md:188-190", "domains/FA/assumptions.md:64")):
    put(a, "RELOCATE", "TARGET", target=K + tgt, note=f"source {K}{src} (仅这些行允许删除)")

# ── R2: dropped phrase present elsewhere = REAL_GAP (scan of all 97 final REWRITE_OK, see t1_r2_scan.md) ────
R2_FLIP = {
    "ig34_p0009_a026": "丢 'as noted in the table note' (指向表注的交叉引用)",
    "ig34_p0011_a014": "数字 5 由行数隐含, 原文计数短语丢",
    "ig34_p0011_a022": "'study day of the start' 由引语隐含; 与 a020 同口径 (a020 用户裁 REAL_GAP)",
    "ig34_p0013_a018": "Define-XML 管理无数据 一句被移到同节 :102, 原位缺",
    "sv20_p0008_a004": "丢 '(see Concept Map, below)' 交叉引用",
}
R2_RECHECK = {
    "ig34_p0010_a009": "'Format' 小标题丢 (仅标签)",
    "ig34_p0011_a017": "'equivalent terms' 改写为 'for'",
    "sv20_p0009_a016": "括号内概念示例被具体变量例替换",
    "sv20_p0009_a019": "'described in Section 2.2' 交叉引用因所在即 2.2 而略",
    "ig34_p0043_a012": "C02 型: 'observation' 由 :894 覆盖 (多行映射, R2 下待定)",
    "ig34_p0043_a013": "C02 型: 参考期由 :894 覆盖",
    "ig34_p0044_a003": "两种情形被压成一条限制说明",
    "ig34_p0044_a004": "C02 型: 排除 AFTER 在 :916 另行",
    "ig34_p0044_a008": "C02 型: AFTER 有效条件在 :916 另行",
    "ig34_p0367_a013": "4 行合并为 1 行, 症状-选项对应靠顺序",
    "ig34_p0367_a016": "4 行合并为 1 行, 症状-选项对应靠顺序",
    "ig34_p0367_a019": "4 行合并为 1 行, 症状-选项对应靠顺序",
    "ig34_p0374_a011": "KB 表头 6 列 / 数据行 9 列, 表格不齐",
    "ig34_p0139_a010": "KB 把 '…/etc.' 扩写成 6 项 (O11, 超出 PDF)",
    "ig34_p0121_a005": "数据集标题行 'ml.xpt … Tabulation' 由文件约定隐含 (同 R4 受阻 5 条标题行, 待用户)",
}
for a, n in R2_FLIP.items():
    assert M[a]["final_class"] == "REWRITE_OK", a
    put(a, "REAL_GAP", "R2-flip", note=n)
for a, n in R2_RECHECK.items():
    assert M[a]["final_class"] == "REWRITE_OK", a
    put(a, "REWRITE_OK", "R2-recheck", note=n, recheck=True)
for a in ("ig34_p0010_a023", "ig34_p0011_a020", "ig34_p0012_a005", "ig34_p0056_a006"):
    assert M[a]["src"] == "pending_user" and M[a]["final_class"] == "REAL_GAP"
    put(a, "REAL_GAP", "R2-ack", note="T1.4 争议 4 条, 用户维持 REAL_GAP")

# ── R4: IE ack; verbatim-in-KB → PRESENT (fp_match.norm, whole kb_loc file); label unification ───────────
def verbatim_in(a):
    f = M[a]["kb_loc"].split(":")[0] if M[a]["kb_loc"] else None
    return bool(f) and norm(A[a]["verbatim"]) in norm(open(f"{ROOT}/{f}").read())

r4 = [a for a, x in X.items() if M[a]["final_class"] == "IE_CAND" and "PRESENT 亦可" in x["reason"]]
assert len(r4) == 44, len(r4)
sib = [a for a, r in M.items() if r["final_class"] == "IE_CAND" and r["ie_cat"] == "CODE_LITERAL_IE" and a not in r4
       and (r["kb_loc"] or "").startswith(K + "chapters/ch03_submitting_data.md") and re.fullmatch(r"[a-z]{2}\.xpt", A[a]["verbatim"].strip())]
title_sib = [a for a, r in M.items() if r["final_class"] == "IE_CAND" and r["ie_cat"] == "REDUNDANT_WITH_SPEC" and a not in r4
             and re.match(r"[a-z]{2}\.xpt, ", A[a]["verbatim"])]
for a in r4 + sib:
    if verbatim_in(a):
        put(a, "PRESENT", "R4-present" if a in r4 else "R4-present-sibling", note=f"逐字在 {M[a]['kb_loc']}")
    else:
        put(a, "IE", "R4-blocked", ie_cat=M[a]["ie_cat"],
            note="用户裁 PRESENT, 但 fp_match.norm 全文件不命中 (KB '> Class: … | Structure: …' 缺 'xx.xpt,' 与 'Tabulation') → 暂留 IE, 待用户")
for a in title_sib:
    put(a, "IE", "R4-blocked", ie_cat=M[a]["ie_cat"], note="同 R4 标题行 (T1.3 已复核, 不在 44 内); 非逐字 → 暂留 IE, 待用户")

# label unification (whitelist precedent: asterisk footnote REDUNDANT_WITH_SPEC 13 vs EDITORIAL_META 5 → majority;
# sv20 TOC → VERSION_MISMATCH (sv20_p0002_a001/a004/a006/a010/a021); sv20 column header → VERSION_MISMATCH (13 + sdtm_v2_superseded 4))
for a, r in M.items():
    if r["final_class"] != "IE_CAND" or a in O:
        continue
    at, cat, new = A[a], r["ie_cat"], None
    if "asterisk (*)" in at["verbatim"]:
        new = "REDUNDANT_WITH_SPEC"
    elif a.startswith("sv20") and at["parent_section"].startswith("§0 [TOC]"):
        new = "VERSION_MISMATCH"
    elif a.startswith("sv20") and at["atom_type"] == "TABLE_HEADER":
        new = "VERSION_MISMATCH"
    elif cat is None:
        assert a == "ig34_p0195_a008"; new = "SPEC_TABLE_HEADER"
    if new and new != cat:
        put(a, "IE", "R4-relabel", ie_cat=new, note=f"{cat} → {new} (whitelist 先例)")

json.dump({"_note": "T1.4 user rulings overlay (t1_user_ack.md R1/R2/R4), applied by t1_merge.py after t1_errata.json. "
                    "Lane/review files are not edited. Unlisted IE_CAND → IE (R4 整体 ack) keeping ie_cat.",
           "built_by": "scripts/helpers/t14_rulings.py", "date": "2026-11-26", "atoms": O},
          open(f"{TB}/work/t1_rulings.json", "w"), ensure_ascii=False, indent=1)
import collections
print(len(O), collections.Counter(e["rule"] for e in O.values()))
