# T2S 扫描批 S-SPEC4 — auditor attempt 1 (Rule A 独立抽检)

> oh-my-claudecode:verifier (opus), 2026-11-26. Brief `subagent_prompts/t2s_scan_review_audit_v1.0.md` Auditor 段 + `t2_auditor_v1.0.md` + common brief + dispatch notes (T2S 段) + U1-U8. spec-only 口径 (主控派发覆盖 P 定义).
> 先独立判, 判完才读 `t2_S-SPEC4.md` / `t2_S-SPEC4_review.md`. 只读 KB; 无 stash/checkout/commit.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC4_auditor/` (bb_N.html bbox, rN-N.png 110dpi 渲染, cmp_XX.txt, sample.py/json)

## Verdict: **PASS** — 独有丢失 0 / 忠实度错误 0 (N=20)

## 总体与抽样
- P = 9 域 PDF spec 表全部变量行 (每变量 1 单元) + 各域 spec 脚注 1 单元 = 184 + 9 = **193**. 计数闸 (`speccmp2.py` 对 bbox, 9 域): PDF 变量数 = KB 变量数, 顺序一致, KB Order 1..n 连续: RS 46 / SC 24 / TU 31 / VS 38 / SUPPQUAL 10 / TE 7 / TI 8 / TS 11 / TV 9.
- spec 表页 (bbox 定位 + 渲染): RS 329-332, SC 340-341, TU 345-346, VS 358-360, SUPPQUAL 432, TE 403, TV 407-408, TI 416, TS 417-418.
- C (writer 改动单元) = `git diff HEAD` 中新增 `Controlled Terms: *` 的变量 17 + 脚注 9 = **26**.
- N = min(30, max(20, ceil(0.1×193))) = **20**; 从 C 抽 ceil(N/3)=7, 余 13 从 P−s1 随机 (含 TV:ARM 再落 C). seed **20261126**.
- 抽样命令 (repo 根; S=上述 scratch): `python3 -I $S/sample.py` — 脚本如下:
```
import re, math, random, json, subprocess
D = ["RS","SC","TU","VS","SUPPQUAL","TE","TI","TS","TV"]; seed = 20261126
P = []; C = set()
for d in D:
    f = f"knowledge_base/domains/{d}/spec.md"
    names = re.findall(r'^### (\S+)\n- \*\*Order:\*\*', open(f).read(), re.M)
    P += [f"{d}:{n}" for n in names]
    P.append(f"{d}:FOOTNOTE"); C.add(f"{d}:FOOTNOTE")
    diff = subprocess.run(["git","diff","-U12","HEAD","--",f], capture_output=True, text=True).stdout
    for blk in re.split(r'\n(?=[ +-]### )', diff):
        m = re.match(r'[ +-]### (\S+)', blk)
        if m and re.search(r'^\+- \*\*Controlled Terms:\*\* \*$', blk, re.M): C.add(f"{d}:{m[1]}")
C = sorted(C); N = min(30, max(20, math.ceil(0.1*len(P))))
rng = random.Random(seed); s1 = rng.sample(C, math.ceil(N/3)); rest = sorted(set(P)-set(s1))
print(json.dumps({"seed":seed,"P":len(P),"C":len(C),"N":N,"C_list":C,"sample":s1+rng.sample(rest, N-len(s1))}, indent=0))
```
- 结果: P=193, C=26, N=20; sample = TS:TSVAL, TS:FOOTNOTE, SC:FOOTNOTE, TV:ARMCD, VS:FOOTNOTE, SC:SCCAT, TE:FOOTNOTE (C 7) + TE:ETCD, VS:VSGRPID, SC:SCSPID, VS:VSDY, VS:VSDTC, SUPPQUAL:QNAM, RS:RSRFTDTC, TS:TSVALNF, TI:DOMAIN, SC:SCTESTCD, TV:ARM, RS:RSSTRESN, TU:VISITDY.

## 逐样本 (渲染图逐字段: Order/Label/Type/CT/Role/Core/CDISC Notes; CT C-code 记法与 DOMAIN CT 不计 U5/U6)
| # | 单元 | PDF 页 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | TS:TSVAL | p417 末行; Char, CT `*`, Result Qualifier, Exp; Notes "Value of TSPARM … See Assumption 8." | TS/spec.md:59 | 无 | 是 | 是 | Order 7; CT `*` 本批补, 与渲染一致 |
| 2 | TS:FOOTNOTE | p418 表下上标1 "In this column, an asterisk (*) indicates … enclosed in parentheses." | TS/spec.md:105 | 无 | 是 | 是 | 逐字; 末变量 TSVCDVER 块后、CR(107) 前 (U7) |
| 3 | SC:FOOTNOTE | p341 表下脚注 | SC/spec.md:222 | 无 | 是 | 是 | 逐字; SCDY 块后, CR 224 前 |
| 4 | TV:ARMCD | p408 首行; Planned Arm Code, Char, `*`, Record Qualifier, Exp; Notes 两条编号 (20 字符…/null) | TV/spec.md:50 | 无 | 是 | 是 | 单元格内编号列表 KB 写成同行 "1. … 2. …", 文字逐字 |
| 5 | VS:FOOTNOTE | p360 表下脚注 | VS/spec.md:348 | 无 | 是 | 是 | 逐字; VSRFTDTC 块后, CR 350 前 |
| 6 | SC:SCCAT | p340; Category for Subject Characteristic, Char, `*`, Grouping Qualifier, Perm | SC/spec.md:77 | 无 | 是 | 是 | Order 9; `*` 本批补 |
| 7 | TE:FOOTNOTE | p403 表下脚注 | TE/spec.md:69 | 无 | 是 | 是 | 逐字; TEDUR 块后, CR 71 前 |
| 8 | TE:ETCD | p403; Element Code, Char, `*`, Topic, Req; Notes "ETCD (the companion to ELEMENT) is limited to 8 characters…" | TE/spec.md:23 | 无 | 是 | 是 | Order 3; `*` (C 集合, 随机段抽中) |
| 9 | VS:VSGRPID | p358; Group ID, Char, 空, Identifier, Perm | VS/spec.md:41 | 无 | 是 | 是 | Order 5 |
| 10 | SC:SCSPID | p340; Sponsor-Defined Identifier, Char, 空, Identifier, Perm; Notes "…preprinted on the CRF…" | SC/spec.md:50 | 无 | 是 | 是 | Order 6 |
| 11 | VS:VSDY | p359; Study Day of Vital Signs, Num, 空, Timing, Perm | VS/spec.md:293 | 无 | 是 | 是 | Order 33 |
| 12 | VS:VSDTC | p359; Date/Time of Measurements, Char, ISO 8601 datetime or interval, Timing, Exp | VS/spec.md:284 | 无 | 是 | 是 | Order 32 |
| 13 | SUPPQUAL:QNAM | p432; Qualifier Variable Name, Char, `*`, Topic, Req; Notes "short name of the qualifier variable … 8 characters … operational dataset." | SUPPQUAL/spec.md:52 | 无 | 是 | 是 | Order 6; `*` 本批补 |
| 14 | RS:RSRFTDTC | p331; Date/Time of Reference Time Point, Char, ISO 8601 datetime or interval, Timing, Perm | RS/spec.md:356 | 无 | 是 | 是 | Order 40 |
| 15 | TS:TSVALNF | p418; Parameter Value Null Flavor, Char, ISO 21090 NullFlavor, Result Qualifier, Perm | TS/spec.md:68 | 无 | 是 | 是 | Order 8 |
| 16 | TI:DOMAIN | p416; Domain Abbreviation, Char, CT `TI`, Identifier, Req | TI/spec.md:14 | 无 | 是 | 是 | KB CT 空 = U6 (归 S-CT, 不计) |
| 17 | SC:SCTESTCD | p340; Subject Characteristic Short Name, Char, (SCTESTCD), Topic, Req; Notes "…Examples: "MARISTAT", "NATORIG"." | SC/spec.md:59 | 无 | 是 | 是 | KB CT `C74559` = U5 记法 (不计) |
| 18 | TV:ARM | p408; Description of Planned Arm, Char, `*`, Synonym Qualifier, Perm; Notes 两条编号 | TV/spec.md:59 | 无 | 是 | 是 | `*` 本批补 |
| 19 | RS:RSSTRESN | p330; Numeric Result/Finding in Standard Units, Num, 空, Result Qualifier, Perm; Notes "…from --STRESC. --STRESN … may be a score." | RS/spec.md:149 | 无 | 是 | 是 | PDF "-- STRESC" 为折行 |
| 20 | TU:VISITDY | p346; Planned Study Day of Visit, Num, 空, Timing, Perm; Notes "…Should be an integer." | TU/spec.md:239 | 无 | 是 | 是 | Order 27 |
- **独有丢失 0 / 忠实度错误 0 / 位置错误 0.**

## 另查
- 全总体机检 (`speccmp2.py`, 9 域 184 变量): Label/Type/Role/Core/Notes 非 U5/U6 残差 3 条 (RSEVAL "Role"、RSENRTPT "or"、VSSCAT "or") 均为该脚本表头同形词过滤假阳性: p359 渲染含 "measurement or examination", p331 渲染含 "Role of the person", `pdftotext -layout -f 332` 含 "before or after" — KB 与 PDF 一致. PDF `*` 的变量 KB 全为 `*` (无 `PDF[*] KB[空]` 残差).
- gaps 9 项 (各域 spec 脚注): 9/9 落地, 逐字, U7 位置 (末变量块 `---` 后、`## Cross References` 前). intros 空.
- 无出处行扫描 (9 文件, 变量块字段/标题/`---`/空行以外): 仅 H1、`> Class|Structure` (U8)、SUPPQUAL `> Source text …` (来源指针, 既有)、脚注、Cross References 块 (U8) → 无出处未标注行 0.
- 授权范围: 本批 9 文件 diff 仅 CT `*` 17 处 + 脚注 9 处 (35+/17−), 无其他改动.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).
- G-TB8: trace 有 `T2S.S-SPEC4` writer (`oh-my-claudecode:executor`, 08:49:08Z) 与 reviewer (`oh-my-claudecode:code-reviewer`, PASS, 08:54:01Z) 的 subagent_done; 无 main 写 KB 记录.
- 与 writer/reviewer 报告对照 (判完后): 计数 184/184、CT `*` 17、脚注 9、U5 56 / U6 8 与本审一致; writer 对 speccmp2 三条假阳性的定性与本审相同. 无分歧.
