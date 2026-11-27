#!/usr/bin/env python3
"""Classify the 60 HEAD regressions (R1-R4) from manual review; re-assert evidence (norm direct check vs KB and PDF);
write work/t2_fp_expected_regressions.jsonl and print md table rows."""
import sys, json, os
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
sys.path.insert(0, f"{TB}/scripts")
from fp_match import norm, norm_pdf, lj
ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
G = f"{TB}/work/scratch/t3"
reg = [r["atom_id"] for r in lj(f"{G}/regress_head.jsonl")]
# S3 (scope=all, baseline = KB at 302ec4c): fp_match --scope all regressions outside the §5.0 section scope
if os.path.exists(f"{G}/regress_all.jsonl"):
    reg = sorted(set(reg) | {r["atom_id"] for r in lj(f"{G}/regress_all.jsonl")})
atoms = {a["atom_id"]: a for a in lj(f"{TB}/work/pdf_atoms.jsonl")}
base = {r["atom_id"]: r for r in lj(f"{TB}/work/fp_baseline.jsonl")}
err = json.load(open(f"{TB}/work/t1_errata.json"))
def K(f): return norm(open(f"{ROOT}/knowledge_base/{f}", encoding="utf-8").read())
def P(p): return norm_pdf("\n".join(open(f"{TB}/work/pdf_pages/ig34_p{q:04d}.txt", encoding="utf-8").read()
                                    for q in (p, p + 1) if os.path.exists(f"{TB}/work/pdf_pages/ig34_p{q:04d}.txt")))
# (atom_set, class, basis, errata_key, kb_file, kb_token, pdf_token) ; tokens: KB must contain kb_token, PDF page must contain pdf_token
FA = [f"ig34_p0363_a0{n}" for n in (11, 12, 13, 15, 16, 17, 18, 19)] + \
     [f"ig34_p0364_a00{n}" for n in range(1, 10)] + [f"ig34_p0364_a0{n}" for n in (11, 12, 13, 17, 18, 19)]
CE = ["ig34_p0153_a0034", "ig34_p0154_a0002", "ig34_p0154_a0013", "ig34_p0154_a0014", "ig34_p0154_a0015",
      "ig34_p0154_a0029", "ig34_p0154_a0030", "ig34_p0155_a0002"]
MBV = [f"ig34_p0258_a0{n}" for n in range(19, 25)]
R = []
def add(ids, cls, basis, key, f, kt, pt):
    for i in ids: R.append(dict(atom_id=i, cls=cls, basis=basis, key=key, f=f, kt=kt, pt=pt))
add(["ig34_p0118_a017"], "R2", "B-EX T-6 PDF_TYPO mg/mL→mg/kg", "t3_atom_err", "domains/EX/examples.md", "scheduled dose is represented in mg/kg.", "represented in mg/ml.")
add(CE, "R1", "原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定)", "t3_atom_err", "domains/CE/examples.md", "abc -us-701-002", "abc -us-701-002")
add(["ig34_p0174_a0012"], "R2", "B-MH T-1 PDF_TYPO 第二处 MHENDTYP→MHEVDTYP (原子=PDF)", "t3_atom_err", "domains/MH/assumptions.md", "date of diagnosis and mhevdtyp = \"diagnosis\"", "mhendtyp = \"diagnosis\"")
add(["ig34_p0179_a0018"], "R1", "原子丢 DVTERM 句点; PDF p179 为 `PERFORMED.`, KB 同 (B-DV E-1)", "t3_atom_err", "domains/DV/examples.md", "no dose call performed. treatment deviation", "no dose call performed. treatment deviation")
add(["ig34_p0215_a018"], "R2", "B-CP T-2 PDF_TYPO CPCSMRKR→CPCSMRKS", "t3_atom_err", "domains/CP/examples.md", "cpcelsta, cpcsmrks and cpsptstd", "cpcelsta, cpcsmrkr and cpsptstd")
add(["ig34_p0218_a014"], "R2", "B-CP T-15 PDF_TYPO CPGATEDEF→CPGATDEF; 另 B-CP D-19 删 assumptions 附录副本, 现在 CP/examples.md:267", "t3_atom_err (次: t3_target_remap→CP/examples.md)", "domains/CP/examples.md", "cpgate, and cpgatdef are used to identify the cell population on which the binding of interest was measured.", "cpgate, and cpgatedef are used")
add(["ig34_p0254_a040", "ig34_p0254_a042"], "R3", "B-MS 迁移: 原子命中于 MS/spec.md (已在 t3_target_remap)", "t3_target_remap (已有)", "domains/MS/spec.md", None, None)
add(["ig34_p0257_a010"], "R1", "原子抄自旧 KB 错值 (MSORRES/MSSTRESC 空; PDF r3 = 1/1); 另 B-MS D-5 去 MB 副本, 现在 MS/examples.md:25", "t3_atom_err (已有; 次: remap→MS/examples.md)", "domains/MS/examples.md", "amoxicillin 1 ug/dl 1 1 ug/dl central lab abc epsilometer", None)
add(["ig34_p0257_a016"], "R2", "B-MS T-1 r9 MSSTRESC PDF 空, KB 保留 25 (原子=PDF); 另 D-5 去 MB 副本, 现在 MS/examples.md:31", "t3_atom_err (已有; 次: remap→MS/examples.md)", "domains/MS/examples.md", "amoxicillin 25 mm 25 25 mm local lab xyz", None)
add(MBV, "R1", "原子抄自旧 KB 错值: VISIT 缺 `1` (PDF p258 VISIT 列换行为 `VISIT 1`) (B-MB)", "t3_atom_err (已有)", "domains/MB/examples.md", "gram stain 1 visit 1 2005-06-19t08:00", None)
add(["ig34_p0260_a009"], "R1", "原子 BEREFID `100`; PDF p260 r4 = `100.3` (B-MB)", "t3_atom_err (已有)", "domains/MB/examples.md", "abc be abc-01-101 4 100.3 aliquoting", "abc-01-101 4 100.3 aliquoting")
add(["ig34_p0260_a015"], "R1", "原子 BELNKID `3`; PDF p260 r10 BELNKID 空 (B-MB)", "t3_atom_err (已有)", "domains/MB/examples.md", "abc be abc-01-101 10 100.1 concentrating", "abc-01-101 10 100.1 concentrating")
add(["ig34_p0262_a029", "ig34_p0262_a030"], "R2", "B-MS T-3 PDF_TYPO IDVAR MBREFID→MSREFID", "t3_atom_err (已有)", "domains/MS/examples.md", "abc-01-101 msrefid", "abc-01-101 mbrefid")
add(["ig34_p0263_a020"], "R2", "B-MB T-3 PDF_TYPO 表头 MBTRESN→MBSTRESN; 另 PDF 印刷 MBGPRID, 原子与 KB 均为 MBGRPID (B-MB T-2)", "t3_atom_err (已有)", "domains/MB/examples.md", "mbstresc mbstresn mbstresu", "mbstresc mbtresn mbstresu")
add(["ig34_p0263_a021", "ig34_p0263_a022"], "R1", "原子 VISIT `WEEK 1`; PDF p263 VISIT 列换行为 `WEEK 5` (B-MB)", "t3_atom_err (已有)", "domains/MB/examples.md", "5 week 5 2011-03-01t22:00", None)
add(["ig34_p0289_a024", "ig34_p0289_a025"], "R1", "原子漏 `Cross-sec.` 句点; PDF p289 文本层 rows 7-8 为 `Cross-sec.` (ig34_p0289.txt:48,52), KB 同 (B-CV #5/#6)", "t3_atom_err (已有)", "domains/CV/examples.md", "axis cross-sec. diameter, mvs", None)
add(["ig34_p0311_a035"], "R2", "B-RE T-1 PDF_TYPO IREEA2→IRREA2", "t3_atom_err (已有)", "domains/RE/examples.md", "qnam=\"irrea1\" and \"irrea2\".", "qnam=\"irrea1\" and \"ireea2\".")
add(FA, "R3", "B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条)", "t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键)", "domains/FA/assumptions.md", "", None)
add(["ig34_p0370_a021"], "R2", "B-FA T-7 PDF_TYPO parent CE→AE", "t3_atom_err (已有)", "domains/FA/examples.md", "linked to the parent ae record via the ae reference number", "linked to the parent ce record")
add(["ig34_p0373_a013"], "R2", "B-FA T-9 PDF_TYPO FAEVINTX→FAEVLINT", "t3_atom_err (已有)", "domains/FA/examples.md", "faevlint indicates that assessments were for the previous 24 hours.", "faevintx indicates")
add(["ig34_p0374_a011"], "R1", "原子把 AE ID 行与合并格说明抽成同一行, 与渲染不符; KB :263 为 4 空格 + 说明合并格, :265 为 AE ID…Visit 6 (按渲染分两行, 9 列)", "t3_atom_err (已有)", "domains/FA/examples.md", "at each visit, record the maximum severity of the adverse event since the last visit.", None)
add(["ig34_p0396_a009"], "R1", "原子 `represents`; PDF p396 为 `represented this rule`, KB 同 (B-TA #31)", "t3_atom_err", "domains/TA/examples.md", "skip forward\" arrow represented this rule in the diagrams).", "skip forward\" arrow represented this rule")

# ---- T3 S0 additions: 13 entries appended to t2 list after 50c3958 (S-SPC1/S-SPC2/S-SPREL/S-SPEC1), re-evidenced at HEAD
add(["ig34_p0255_a021"], "R3", "S-SPC2 MOVED: MS spec 脚注由 MS/assumptions.md 迁到 MS/spec.md (U2/U7)", "t3_target_remap→domains/MS/spec.md", "domains/MS/spec.md", None, None)
add(["ig34_p0060_a024"], "R3", "S-SPEC1 MOVED: CO spec 脚注由 CO/assumptions.md 迁到 CO/spec.md (U2/U7)", "t3_target_remap→domains/CO/spec.md", "domains/CO/spec.md", None, None)
add(["ig34_p0278_a051"], "R1", "S-SPC2 #15: 原子抄自旧错 KB (多 and \"10\" through \"12\"/individual); KB PC/examples.md:146 = p278 渲染 (非 fp 机制回归: baseline 即未命中)", "t3_atom_err", "domains/PC/examples.md", 'pcseq values "1" through "12" and pp records with ppseq values "1" through "7".', None)
add(["ig34_p0199_a020"], "R2", "S-SPC1 CP T-21 PDF_TYPO --BNDAGT/--GATEDEF→--BDAGNT/--GATDEF (spec 变量名)", "t3_atom_err", "domains/CP/assumptions.md", "--bdagnt (binding agent)", "--bndagt (binding agent)")
add(["ig34_p0200_a007"], "R2", "S-SPC1 CP T-21 PDF_TYPO --GATEDEF→--GATDEF", "t3_atom_err", "domains/CP/assumptions.md", "--gate and --gatdef variables", "--gate and --gatedef variables")
add(["ig34_p0206_a001"], "R2", "S-SPC1 CP T-21 PDF_TYPO CPBNDAGT→CPBDAGNT", "t3_atom_err", "domains/CP/assumptions.md", "cpbdagnt and/or cptstpnl", "cpbndagt and/or cptstpnl")
add(["ig34_p0200_a006"], "R2", "S-SPC1 CP T-17 PDF_TYPO sting→string", "t3_atom_err", "domains/CP/assumptions.md", "complete marker string information", "complete marker sting information")
add(["ig34_p0206_a003"], "R2", "S-SPC1 CP T-18 PDF_TYPO CSMRKS→CPCSMRKS", "t3_atom_err", "domains/CP/assumptions.md", "cpcelsta and cpcsmrks with viability", "cpcelsta and csmrks with viability")
add(["ig34_p0240_a004"], "R2", "B-IS T-4 PDF_TYPO nucleoar→nucleolar; S-SPC1 D2 删 IS/assumptions 附录副本, 现在 IS/examples.md:215", "t3_atom_err (次: t3_target_remap→IS/examples.md)", "domains/IS/examples.md", "(i.e., nucleolar)", "(i.e., nucleoar)")
add(["ig34_p0079_a004"], "R1", "S-SPREL SE asm 按 p79 渲染改词 (epochs and elements); 原子抄自旧错 KB", "t3_atom_err", "domains/SE/assumptions.md", "progress through the epochs and elements of the trial.", "progress through the epochs and elements of the trial.")
add(["ig34_p0079_a006"], "R1", "S-SPREL SE asm 按 p79 渲染改词 (definitions (TESTRL values)); 原子抄自旧错 KB", "t3_atom_err", "domains/SE/assumptions.md", "according to the definitions (testrl values) in the trial elements", "according to the definitions (testrl values) in the trial elements")
add(["ig34_p0079_a009"], "R1", "S-SPREL SE asm 按 p79 渲染 (--DTC); 原子抄自旧错 KB", "t3_atom_err", "domains/SE/assumptions.md", "comparison of the --dtc of a finding observation", "comparison of the --dtc of a finding observation")
add(["ig34_p0079_a010"], "R1", "S-SPREL SE asm 按 p79 渲染 (Such variables relate / --DY); 原子抄自旧错 KB", "t3_atom_err", "domains/SE/assumptions.md", "study day (--dy) variables relate it", "study day (--dy) variables relate it")

# ---- T3 S3 additions: fp_match --scope all (baseline KB 302ec4c) regressions outside §5.0 scope (10)
add(["ig34_p0086_a011"], "R1", "B-SM audit: 原子 verbatim 错, 以渲染图为准 (SV Description); t1 t3_atom_err", "t3_atom_err", "domains/SV/assumptions.md", "the sv dataset provides reviewers with a summary of a subject's visits", "the sv dataset provides reviewers with a summary of a subject's visits")
add(["ig34_p0160_a0028"], "R2", "B-DS T-3 PDF_TYPO (DSDTDTC)→(DSSTDTC) (t2_B-DS.md:35)", "t3_atom_err", "domains/DS/examples.md", "participation ended. (dsstdtc).", "participation ended. (dsdtdtc).")
add(["ig34_p0274_a019"], "R1", "原子 row 7 多 `Collected`; PDF p274 文本层 :35 row 7 = SINGLE DOSE 无 Collected; KB PP/examples.md:74 = PDF", "t3_atom_err", "domains/PP/examples.md", "pkcond condition of pk analysis single dose", "pkcond condition of pk analysis single dose")
add(["ig34_p0334_a011"], "R2", "B-RS T-8 PDF_TYPO 'symptomatic determination'→'deterioration' (attempt 2 / 审计 K4-E4: 原子 = PDF, 原 R1 依据不成立)", "t3_atom_err", "domains/RS/examples.md", "symptomatic deterioration", "symptomatic determination")
add(["ig34_p0335_a015", "ig34_p0335_a016", "ig34_p0335_a017", "ig34_p0335_a018"], "R2", "B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP", "t3_atom_err", "domains/RS/examples.md", "rslnkgrp", "rsplnkgrp")
add(["ig34_p0340_a002"], "R3", "B-SC dedup: spec 首句迁到 SC/assumptions.md:9 (t2_B-SC_audit.md:16)", "t3_target_remap→domains/SC/assumptions.md", "domains/SC/assumptions.md", None, None)
add(["ig34_p0342_a004"], "R1", "原子表头 SCORESU; PDF p342 与 KB 均 SCORRESU", "t3_atom_err", "domains/SC/examples.md", "scorres scorresu scstresc", "scorres scorresu scstresc")

# ---- T4 解冻 (主控决定 2026-11-27, evidence/checkpoints/t4_thaw_W3.md "attempt 1 续"): U-7 KB 写正确值 → 原子 = PDF 原错 (R2, 16);
#      A5-10 PP "RELREC Method Quick Reference" 换成交叉引用 → 原文只在 PC/examples.md (R3, 19)
U7 = "T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF"
add(["ig34_p0160_a0026"], "R2", f"{U7}: A3-2 B-DS U-4 删 in", "t3_atom_err", "domains/DS/examples.md", "between the ds record and the ae record was represented", "between the ds record and in the ae record")
add(["ig34_p0165_a0007"], "R2", f"{U7}: A1-9 B-DS U-1 se ETCD SCREEN→SCRN", "t3_atom_err", "domains/DS/examples.md", "xyz-767-002 1 scrn screen 2016-02-04", "screen screen 2016-02-04")
add(["ig34_p0419_a006"], "R2", f"{U7}: A2-5 B-TS T-3 DOSFREQ→DOSFRQ (+A2-4 B-TS T-2 Dose→DOSE)", "t3_atom_err", "domains/TS/assumptions.md", 'tsparmcd = "dose" and tsparmcd = "dosfrq"', 'tsparmcd = "dosfreq"')
add(["ig34_p0419_a011"], "R2", f"{U7}: A2-5 B-TS T-3 DOSFREQ→DOSFRQ", "t3_atom_err", "domains/TS/assumptions.md", "1 a dosfrq dosing frequency bid", "dosfreq dosing frequency bid")
add(["ig34_p0419_a013"], "R2", f"{U7}: A2-5 B-TS T-3 DOSFREQ→DOSFRQ", "t3_atom_err", "domains/TS/assumptions.md", "2 b dosfrq dosing frequency q24h", "dosfreq dosing frequency q24h")
add(["ig34_p0425_a024"], "R2", f"{U7}: A2-7 B-TS T-6 MAXAGE→AGEMAX", "t3_atom_err", "domains/TS/assumptions.md", "for the agemax case", "maxage case that provided")
add(["ig34_p0372_a013"], "R2", f"{U7}: A3-9 B-FA T-8 populated→populate", "t3_atom_err", "domains/FA/examples.md", "used to populate fadtc", "used to populated fadtc")
add(["ig34_p0298_a001"], "R2", f"{U7}: A3-15 B-NV N-2 删 the", "t3_atom_err", "domains/NV/examples.md", "nvgrpid links each", "nvgrpid links the")
add(["ig34_p0285_a015"], "R2", f"{U7}: A3-14 B-NV N-1 may included→include", "t3_atom_err", "domains/NV/assumptions.md", "may include additional", "may included additional")
add(["ig34_p0280_a036"], "R2", f"{U7}: A2-3 B-PCPP T-8b DYDRGX_HALF→DY1DRGX_HALF", "t3_atom_err", "domains/PC/examples.md", 'ppgrpid = "dy1drgx half", whereas', "dydrgx half")
add(["ig34_p0280_a039"], "R2", f"{U7}: A2-2 B-PCPP T-8 DYIDRGX_A→DY1DRGX_A", "t3_atom_err", "domains/PC/examples.md", 'all pp records with ppgrpid = "dy1drgx a"', "dyidrgx a")
add(["ig34_p0280_a040"], "R2", f"{U7}: A2-2 B-PCPP T-8 DYIDRGX_HALF→DY1DRGX_HALF", "t3_atom_err", "domains/PC/examples.md", 'all pp records with ppgrpid = "dy1drgx half"', "dyidrgx half")
add(["ig34_p0281_a002"], "R2", f"{U7}: A2-15 S-SPC2 N-1 PP→PC records with PCSEQ", "t3_atom_err", "domains/PC/examples.md", 'includes pc records with pcseq values "1" through "12"', "includes pp records with pcseq values")
add(["ig34_p0281_a003"], "R2", f"{U7}: A2-15 S-SPC2 N-1 PP→PC records with PCSEQ", "t3_atom_err", "domains/PC/examples.md", 'includes pc records with pcseq values "1" through "7"', "includes pp records with pcseq values")
add(["ig34_p0281_a031"], "R2", f"{U7}: A2-16 S-SPC2 N-2 PP/PGRPID→PC/PCGRPID", "t3_atom_err", "domains/PC/examples.md", 'all pc records with pcgrpid values "dy1 drgx a"', "all pp records with pgrpid values")
add(["ig34_p0281_a032"], "R2", f"{U7}: A2-16 S-SPC2 N-2 PP/PGRPID→PC/PCGRPID", "t3_atom_err", "domains/PC/examples.md", 'all pc records with pcgrpid value "dy1 drgx a"', "all pp records with pgrpid value")
# 另 3 条 U-7 原子 (已由 K3b 转 PDF_TYPO) 同为 fp 回归, 为使 NEW = 0 一并登记 (S1-R2 先于 K3b, 终态同为 PDF_TYPO)
add(["ig34_p0085_a010"], "R2", f"{U7}: A2-8 B-SM O32 SMDY→SMSTDY", "t3_atom_err", "domains/SM/examples.md", "smstdy is not populated", "smdy is not populated")
add(["ig34_p0190_a017"], "R2", f"{U7}: A3-5 B-EG T-3 investigation→investigator", "t3_atom_err", "domains/EG/examples.md", "principal investigator on three", "principal investigation on three")
add(["ig34_p0419_a017"], "R2", f"{U7}: A2-6 B-TS T-4 OUTMSPR→OUTMSPRI", "t3_atom_err", "domains/TS/assumptions.md", 'tsparm = "outmspri"', 'tsparm = "outmspr"')
add(["ig34_p0275_a019", "ig34_p0277_a020", "ig34_p0277_a023", "ig34_p0277_a024", "ig34_p0278_a002"] + [f"ig34_p0278_a0{n}" for n in range(33, 42)] +
    ["ig34_p0278_a054", "ig34_p0281_a034", "ig34_p0281_a049", "ig34_p0282_a035", "ig34_p0283_a012"], "R3",
    "T4 A5-10: PP RELREC Method Quick Reference 整节改为交叉引用, 原文在 PC/examples.md", "t3_target_remap→domains/PC/examples.md", "domains/PC/examples.md", None, None)

ids = [r["atom_id"] for r in R]
# 83 = T3 attempt 4 list; + 19 (T4 U-7 R2: 主控定 16 + 已由 K3b 触及的 3) + 19 (T4 A5-10 R3) = 121 (主控决定 2026-11-27, t4_thaw_W3.md "attempt 1 续")
assert len(set(ids)) == len(ids) == 121, len(ids)
missing = set(reg) - set(ids)          # current regressions not explained by the list = NEW regressions
print("current regress:", len(reg), " not in t3 list (NEW):", sorted(missing), " list entries not regressing now:", sorted(set(ids) - set(reg)))
bad = []
for r in R:
    a = atoms[r["atom_id"]]; v = norm(a["verbatim"]); kb = K(r["f"]); pdf = P(a["page"])
    r["in_errata_atom_err"] = r["atom_id"] in err["t3_atom_err"]
    r["in_errata_remap"] = r["atom_id"] in err["t3_target_remap"]
    r["verbatim_in_new_target"] = v in kb
    r["kb_token_ok"] = (r["kt"] in kb) if r["kt"] else None
    r["pdf_token_ok"] = (r["pt"] in pdf) if r["pt"] else None
    r["atom_in_pdf_page"] = v in pdf
    if r["cls"] == "R3" and not r["verbatim_in_new_target"]: bad.append(r["atom_id"])
    if r["cls"] != "R3" and r["verbatim_in_new_target"]: bad.append(r["atom_id"] + ":unexpected-hit")
    if r["kb_token_ok"] is False or r["pdf_token_ok"] is False: bad.append(r["atom_id"])
print("BAD", bad)
from collections import Counter
print(Counter(r["cls"] for r in R), "R4 =", sum(r["cls"] == "R4" for r in R))
with open(f"{TB}/work/t3_fp_expected_regressions.jsonl", "w", encoding="utf-8") as f:
    for r in sorted(R, key=lambda x: x["atom_id"]):
        ev = f"v∈KB={r['verbatim_in_new_target']}; kbTok={r['kb_token_ok']}; pdfTok={r['pdf_token_ok']}; atom∈PDF={r['atom_in_pdf_page']}"
        note = f"{r['basis']} | errata: {r['key']} | new_target: {r['f']} | {ev}"
        f.write(json.dumps({"atom_id": r["atom_id"], "class": r["cls"], "note": note}, ensure_ascii=False) + "\n")
sys.exit(1 if (bad or missing) else 0)
