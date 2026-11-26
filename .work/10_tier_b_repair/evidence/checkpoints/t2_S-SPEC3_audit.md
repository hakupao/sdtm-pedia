# T2S.S-SPEC3 Auditor (Rule A) — attempt 1

> agent: oh-my-claudecode:verifier (opus); 与 writer (executor) / reviewer (code-reviewer) 不同. 先独立判, 判完才读 writer/reviewer 报告.
> 口径: 主控派发覆盖 — P = 8 域 (CV MI MK NV RE RP QS FT) PDF spec 表全部变量行 (每变量 1 单元, 以 PDF 原页为准) + 各域 spec 表脚注; N = min(30, max(20, ceil(0.1×|P|))); seed 20261126; 1/3 取自 writer 改动 (CT `*` 13 + 脚注 8 = W 21). CT C-code 记法与 DOMAIN CT 不计 (U5/U6 → S-CT).
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC3_auditor/`

## 1. 计数闸 (PDF 变量数 = KB 变量数 + 顺序一致)
方法: `pdftotext -bbox` 20 页 + 共享工具 `work/scratch/t2s_tools/speccmp2.py` (p286 先裁掉 y<483 的 §6.3.7.1 `--.xpt` 通用表, 规避 "一页两表头" 盲区), 再以渲染图核顺序位 (Order) 作独立复核.

| 域 | spec 页 | PDF 变量 | KB 变量 | 顺序一致 | KB Order 1..n |
|---|---|---|---|---|---|
| MI | 264-265 | 37 | 37 | 是 | 是 |
| CV | 286-288 | 42 | 42 | 是 | 是 |
| MK | 290-291 | 42 | 42 | 是 | 是 |
| NV | 294-296 | 42 | 42 | 是 | 是 |
| RP | 305-306 | 36 | 36 | 是 | 是 |
| RE | 308-310 | 47 | 47 | 是 | 是 |
| FT | 319-320 | 38 | 38 | 是 | 是 |
| QS | 324-326 | 35 | 35 | 是 | 是 |
| 计 | | 319 | 319 | | |

全字段比对差异: 仅 U5 (C-code vs 括号短名) / U6 (DOMAIN 空) + 2 处工具伪差 (NVTEST p295 / RPSTRESC p306 页顶首行的 "Name"/"or" 被当表头词剔除; `pdftotext -layout` 与渲染图均显示 PDF 含该词, KB 正确).

## 2. 抽样 (可复跑)
```
# cd repo 根; python3 -I <下列脚本>
import json,math,random,re,subprocess
D=['CV','MI','MK','NV','RE','RP','QS','FT']; seed=20261126
P=[];W=[]
for d in D:
    f=f'knowledge_base/domains/{d}/spec.md'
    t=open(f).read().split('\n## Cross References')[0]
    kb=re.findall(r'^### (\S+)',t,re.M)
    P+=[f'{d}:{v}' for v in kb]; P.append(f'{d}:FOOTNOTE'); W.append(f'{d}:FOOTNOTE')
    diff=subprocess.run(['git','diff','-U30','HEAD','--',f],capture_output=True,text=True).stdout
    cur=None
    for L in diff.splitlines():
        m=re.match(r'^[ +-]### (\S+)',L)
        if m: cur=m.group(1)
        if L.startswith('+- **Controlled Terms:** *'): W.append(f'{d}:{cur}')
P=sorted(set(P)); W=sorted(set(W))
N=min(30,max(20,math.ceil(0.1*len(P))))
rng=random.Random(seed); k=math.ceil(N/3)
s1=rng.sample(W,k); rest=sorted(set(P)-set(s1)); s2=rng.sample(rest,N-k)
print(json.dumps({'seed':seed,'P':len(P),'W':len(W),'N':N,'k':k,'W_list':W,'sample':s1+s2}))
```
结果: |P| = 327 (319 变量 + 8 脚注), |W| = 21, N = 30, k = 10 (W 抽 10) + P−s1 抽 20.

## 3. 逐样本判 (渲染 `pdftoppm -r 110` 逐格核 Order(序位)/Label/Type/CT/Role/Core/CDISC Notes)
| # | 样本 | PDF 页 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | QS:FOOTNOTE (W) | p326 表下 "¹In this column, an asterisk (*) indicates …" | QS/spec.md:321 | 否 | 是 | 是 | 末变量 QSEVINTX 后、Cross References 前 (U7) |
| 2 | NV:FOOTNOTE (W) | p296 NV 表下脚注 | NV/spec.md:384 | 否 | 是 | 是 | gaps 未列, writer 全扫补; 出处 p296 渲染确认 (非 §6.3.7.1 通用表那条) |
| 3 | CV:CVSCAT (W) | p287: Subcategory for Cardiovascular Test / Char / * / Grouping Qualifier / Perm | CV/spec.md:113 | 否 | 是 | 是 | Order 13 |
| 4 | CV:CVSTRESC (W) | p287: Character Result/Finding in Std Format / * / Result Qualifier / Exp; Notes 3 句含 NONE/NEG 例 | CV/spec.md:149 | 否 | 是 | 是 | Order 17 |
| 5 | MI:MIRESCAT (W) | p264: Result Category / * / Variable Qualifier / Perm; MALIGNANT/BENIGN | MI/spec.md:158 | 否 | 是 | 是 | Order 18 |
| 6 | MI:MISCAT (W) | p264: Subcategory for Microscopic Finding / * / Grouping Qualifier / Perm | MI/spec.md:104 | 否 | 是 | 是 | Order 12 |
| 7 | RP:FOOTNOTE (W) | p306 表下脚注 | RP/spec.md:330 | 否 | 是 | 是 | U7 |
| 8 | CV:FOOTNOTE (W) | p288 表下脚注 | CV/spec.md:384 | 否 | 是 | 是 | U7 |
| 9 | RE:FOOTNOTE (W) | p310 表下脚注 | RE/spec.md:429 | 否 | 是 | 是 | U7 |
| 10 | MK:MKCAT (W) | p290: Category for Musculoskeletal Test / * / Grouping Qualifier / Perm; Example SWOLLEN/TENDER JOINT ASSESSMENT | MK/spec.md:104 | 否 | 是 | 是 | Order 12 |
| 11 | MK:MKTPTREF | p291: Time Point Reference / Timing / Perm; MKELTM/MKTPTNUM/MKTPT + 2 例 | MK/spec.md:365 | 否 | 是 | 是 | Order 41 |
| 12 | FT:FTORRES | p319: Result or Finding in Original Units / Result Qualifier / Exp | FT/spec.md:113 | 否 | 是 | 是 | Order 13 |
| 13 | QS:QSEVLINT | p326: Evaluation Interval / ISO 8601 duration or interval / Timing / Perm; "-P2Y" 例 | QS/spec.md:302 | 否 | 是 | 是 | PDF "- P2Y" 为折行连字符, KB "-P2Y" 正确 |
| 14 | NV:NVORRES | p295: Result or Finding in Original Units / Exp; "Result of the procedure measurement or finding…" | NV/spec.md:131 | 否 | 是 | 是 | |
| 15 | MK:MKGRPID | p290: Group ID / Identifier / Perm; "Used to link together a block…" | MK/spec.md:41 | 否 | 是 | 是 | Order 5 |
| 16 | RE:VISIT | p309: Visit Name / Timing / Perm; "…of a clinical encounter. May be used in addition…" | RE/spec.md:329 | 否 | 是 | 是 | |
| 17 | FT:FTSTRESN | p319: Numeric Result/Finding in Standard Units / Num / Perm | FT/spec.md:140 | 否 | 是 | 是 | Order 16 |
| 18 | RE:SPDEVID | p308: Sponsor Device Identifier / Identifier / Perm | RE/spec.md:32 | 否 | 是 | 是 | Order 4 |
| 19 | RP:RPLNKGRP | p305: Link Group ID / Identifier / Perm; many-to-one | RP/spec.md:77 | 否 | 是 | 是 | Order 9 |
| 20 | QS:QSEVINTX | p326: Evaluation Interval Text / Timing / Perm; 4 例 | QS/spec.md:311 | 否 | 是 | 是 | Order 35 |
| 21 | QS:QSBLFL | p325: Baseline Flag / (NY) / Record Qualifier / Perm; ADaM 句 | QS/spec.md:176 | 否 | 是 | 是 | CT C66742 = U5, 不计; Order 20 |
| 22 | NV:NVTEST | p295: Name of Nervous System Test / (NVTEST) / Synonym Qualifier / Req; 40 字符 + 4 例 | NV/spec.md:104 | 否 | 是 | 是 | 工具伪差已由渲染排除; CT = U5 |
| 23 | NV:NVTPT | p295: Planned Time Point Name / Timing / Perm; "TIME OF LAST DOSE" + START/5 MIN POST | NV/spec.md:338 | 否 | 是 | 是 | Order 38 |
| 24 | MI:MISTRESN | p264: Numeric Result/Finding in Standard Units / Num / Perm | MI/spec.md:140 | 否 | 是 | 是 | Order 16 |
| 25 | RE:REORREF | p308: Reference Result in Original Units / Variable Qualifier / Perm; 2 句 | RE/spec.md:158 | 否 | 是 | 是 | Order 18 |
| 26 | CV:VISITDY | p288: Planned Study Day of Visit / Num / Timing / Perm; "…Should be an integer." | CV/spec.md:293 | 否 | 是 | 是 | Order 33 |
| 27 | RP:RPLOBXFL | p306: Last Observation Before Exposure Flag / (NY) / Record Qualifier / **Perm** | RP/spec.md:185 | 否 | 是 | 是 | RP 该行 Core=Perm (非 Exp), KB 一致; CT = U5; Order 21 |
| 28 | MK:MKDTC | p291: Date/Time of Collection / ISO 8601 datetime or interval / Timing / Exp | MK/spec.md:320 | 否 | 是 | 是 | Order 36 |
| 29 | FT:FTORRESU | p319: Original Units / (UNIT) / Variable Qualifier / Perm; "Unit for FTORRES." | FT/spec.md:122 | 否 | 是 | 是 | CT = U5; Order 14 |
| 30 | NV:NVRFTDTC | p296: Date/Time of Reference Time Point / ISO 8601 datetime or interval / Timing / Perm; "--TPTREF in ISO 8601 character format" | NV/spec.md:374 | 否 | 是 | 是 | PDF 原文即 "--TPTREF", KB 照录 |

W 样本 10/30 (= 1/3).
**独有丢失 0/30; 忠实度错 0; 位置错 0.**

## 4. 补充核查 (独立方法)
- **CT `*` 全总体 (319 变量)**: bbox 取全部 "*" 词, 按 y 映射同行首列变量名 → MI {MICAT, MISCAT, MIRESCAT} / CV {CVCAT, CVSCAT, CVSTRESC} / MK {MKCAT, MKSCAT} / FT {FTTESTCD, FTTEST} / QS {QSTESTCD, QSTEST, QSSCAT}; NV/RE/RP 0 = 13. KB `Controlled Terms: *` 集合逐变量全等. (p286 两个 "*" 属 §6.3.7.1 通用表 --TESTCD/--TEST, y<483, 排除.) NV/RP 渲染确认 NVCAT/NVSCAT/RPCAT/RPSCAT CT 列空.
- **脚注 8/8**: 8 域 spec.md 各 1 段, 逐字 = PDF (p265/p288/p291/p296/p306/p310/p320/p326 渲染), 均在最后变量块 `---` 之后、`## Cross References` 之前 (U7).
- **反向 KB→PDF (8 文件, Cross References 前全扫)**: 除 `###` / 7 字段行 / `---` 外仅 `# XX — Name` 标题、`> Class|Structure` 行 (U8 导航) 与新增脚注行. 无 PDF 出处且未 D6 的解释性行 = 0.
- **diff 授权范围**: `git diff HEAD -- 8×spec.md` = 13 处 `Controlled Terms:` 空→`*` + 8 段脚注 (+29/−13); 无其他改动. 工作树别批文件 (RS SC SUPPQUAL TE TI TS TU TV VS spec.md) 不计.
- **live docs**: `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).
- **G-TB8**: trace 中 `T2S.S-SPEC3` 有 executor (writer) 与 code-reviewer (PASS) 的 subagent_done; 本批无 `agent: main` 记录.

## 5. 对照 writer / reviewer 报告 (判完后读)
writer: 319/319, CT `*` 13, 脚注 8 (NV 为 gaps 外全扫新增), 结构/删除/D6/PDF_TYPO 均无; reviewer: 自写解析器 319/319 PASS. 与本审独立结论一致, 无分歧.

## Verdict: **PASS** (丢失 0 / 忠实 0 / 位置 0)
