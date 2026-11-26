# T2S.S-SPEC2 Auditor (Rule A) — attempt 1

> agent: oh-my-claudecode:verifier (opus); 与 writer (executor) / reviewer (code-reviewer) 不同. 先独立判, 判完才读 writer/reviewer 报告.
> 口径: 主控派发覆盖 — P = 8 域 (CE HO MH DV DA DD IE BS) PDF spec 表全部变量行 (每变量 1 单元, 以 PDF 原页为准) + 各域 spec 表脚注; N = min(30, max(20, ceil(0.1×|P|))); seed 20261126; 1/3 取自 writer 改动 (CT `*` 20 + 脚注 8 = W 28). CT C-code 记法与 DOMAIN CT 不计 (U5/U6 → S-CT).

## 1. 计数闸 (PDF 变量数 = KB 变量数 + 顺序一致)
独立方法: `pdftotext -layout` 首列变量名 (去掉域代码单词行、p196 §6.3.5.1 通用表的 VISITNUM/VISIT/VISITDY、KB Cross References 小标题) vs KB `### VAR` 序列; KB `Order` 连续 1..n.

| 域 | PDF 页 | PDF 变量 | KB 变量 | 顺序一致 | KB Order 连续 |
|---|---|---|---|---|---|
| CE | 148-150 | 32 | 32 | 是 | 是 |
| HO | 167-169 | 28 | 28 | 是 | 是 |
| MH | 171-172 | 27 | 27 | 是 | 是 |
| DV | 178-179 | 16 | 16 | 是 | 是 |
| DA | 180-181 | 27 | 27 | 是 | 是 |
| DD | 183 | 12 | 12 | 是 | 是 |
| IE | 193 | 18 | 18 | 是 | 是 |
| BS | 196-198 | 35 | 35 | 是 | 是 |
| 合计 | | 195 | 195 | | |

## 2. 抽样 (可复跑)
```
# cd repo 根; python3 -I <下列脚本>
import json,math,random,re,subprocess
D=['CE','HO','MH','DV','DA','DD','IE','BS']; seed=20261126
P=[];W=[]
for d in D:
    f=f'knowledge_base/domains/{d}/spec.md'
    kb=re.findall(r'^### (\S+)',open(f).read(),re.M)
    kb=[v for v in kb if v not in ('Controlled','Related','General','Model')]
    P+= [f'{d}:{v}' for v in kb]; P.append(f'{d}:FOOTNOTE'); W.append(f'{d}:FOOTNOTE')
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
print(json.dumps({'seed':seed,'P':len(P),'W':len(W),'N':N,'k':k,'W_list':W,'sample':s1+s2},indent=0))
```
结果: |P| = 203 (195 变量 + 8 脚注), |W| = 28, N = 21, k = 7 (W 抽 7) + P−s1 抽 14.
样本: DV:DVSCAT, DV:DVDECOD, BS:FOOTNOTE, HO:HOSCAT, IE:IESCAT, CE:CEBODSYS, DA:DASCAT | DA:DATEST, IE:TAETORD, CE:CESTRTPT, IE:IETESTCD, IE:IETEST, DA:DAREASND, BS:BSTPTNUM, DD:FOOTNOTE, DA:STUDYID, CE:FOOTNOTE, HO:HOSEQ, BS:VISIT, HO:HOREASND, IE:VISITNUM

## 3. 逐样本判 (渲染 `pdftoppm -r 120` 逐格核 Order(序位)/Label/Type/CT/Role/Core/CDISC Notes)
| # | 样本 | PDF 页 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | DV:DVSCAT (W) | p178 行10: Subcategory for Protocol Deviation / Char / * / Grouping Qualifier / Perm | DV/spec.md:86 | 否 | 是 | 是 | CT `*` 照录 |
| 2 | DV:DVDECOD (W) | p178 行8: Protocol Deviation Coded Term / * / Synonym Qualifier / Perm; Notes 4 个 Examples | DV/spec.md:68 | 否 | 是 | 是 | Notes 逐字 |
| 3 | BS:FOOTNOTE (W) | p198 表下 "¹In this column, an asterisk (*) indicates …" | BS/spec.md:321 | 否 | 是 | 是 | 末变量 BSRFTDTC 后、Cross References 前 (U7) |
| 4 | HO:HOSCAT (W) | p168: Subcategory for Healthcare Encounter / * / Grouping Qualifier / Perm; "A further categorization of HOCAT values." | HO/spec.md:95 | 否 | 是 | 是 | |
| 5 | IE:IESCAT (W) | p193: Inclusion/Exclusion Subcategory / * / Grouping Qualifier / Perm; Notes 含 PDF 原文 "or for to categorize … exceptions" | IE/spec.md:77 | 否 | 是 | 是 | PDF 自身语病照录 (非 KB 错) |
| 6 | CE:CEBODSYS (W) | p149: Body System or Organ Class / * / Record Qualifier / Perm; Notes 2 句 (MedDRA/SOC) | CE/spec.md:140 | 否 | 是 | 是 | |
| 7 | DA:DASCAT (W) | p180: Subcategory / * / Grouping Qualifier / Perm | DA/spec.md:113 | 否 | 是 | 是 | |
| 8 | DA:DATEST | p180: Name of Accountability Assessment / (DATEST) / Synonym Qualifier / Req; ≤40 字符 + Examples | DA/spec.md:95 | 否 | 是 | 是 | CT 为 C78731 = U5 记法, 不计 |
| 9 | IE:TAETORD | p193: Planned Order of Element within Arm / Num / Timing / Perm; "…in which the assessment was made." | IE/spec.md:131 | 否 | 是 | 是 | |
| 10 | CE:CESTRTPT | p149: Start Relative to Reference Time Point / (STENRF) / Timing / Perm; Notes + "Not all values … Section 4.4.7" | CE/spec.md:257 | 否 | 是 | 是 | CT C66728 = U5; 交叉引用保留 |
| 11 | IE:IETESTCD (W 外随机抽中, 属 W) | p193: Inclusion/Exclusion Criterion Short Name / * / Topic / Req; 8 字符/首字符/字符集 + Examples | IE/spec.md:50 | 否 | 是 | 是 | |
| 12 | IE:IETEST | p193: Inclusion/Exclusion Criterion / Synonym Qualifier / Req; ≤200 字符 | IE/spec.md:59 | 否 | 是 | 是 | |
| 13 | DA:DAREASND | p181: Reason Not Done / Record Qualifier / Perm; "…when value is "NOT DONE"." | DA/spec.md:176 | 否 | 是 | 是 | |
| 14 | BS:BSTPTNUM | p198: Planned Time Point Number / Num / Timing / Perm | BS/spec.md:284 | 否 | 是 | 是 | |
| 15 | DD:FOOTNOTE | p183 表下脚注 | DD/spec.md:114 | 否 | 是 | 是 | 末变量 DDDY 后 (U7) |
| 16 | DA:STUDYID | p180: Study Identifier / Identifier / Req; "…for a study within the submission." | DA/spec.md:5 | 否 | 是 | 是 | DA 独有 "within the submission" 已保留 |
| 17 | CE:FOOTNOTE | p150 表下脚注 | CE/spec.md:294 | 否 | 是 | 是 | 末变量 CEENTPT 后 (U7) |
| 18 | HO:HOSEQ | p168: Sequence Number / Num / Identifier / Req | HO/spec.md:32 | 否 | 是 | 是 | |
| 19 | BS:VISIT | p197: Visit Name / Char / Timing / Perm; "Protocol-defined description of clinical encounter." | BS/spec.md:239 | 否 | 是 | 是 | 非 p196 通用表的 VISIT (该行多一句), KB 取对表 |
| 20 | HO:HOREASND | p168: Reason Healthcare Encounter Not Done / Record Qualifier / Perm; 2 句 | HO/spec.md:131 | 否 | 是 | 是 | |
| 21 | IE:VISITNUM | p193: Visit Number / Num / Timing / Perm | IE/spec.md:104 | 否 | 是 | 是 | |

注: 样本 11 IETESTCD 属 W (随机段抽中), 故实际 W 样本 8/21 ≥ 1/3.
**独有丢失 0/21; 忠实度错 0; 位置错 0.**

## 4. 补充核查 (独立方法)
- **CT `*` 全总体 (195 变量)**: `pdftotext -bbox` 取 CT 列 x∈(150,350) 的 "*" 词, 按 y 映射到首列变量名, 对 KB `Controlled Terms: *`. CE 5 / HO 2 / MH 4 / DV 3 / DA 2 / DD 1 / IE 2 / BS 1 = 20, 逐变量全等. (BS 页 p196 顶部 5 个 "*" 属 §6.3.5.1 通用表 --STAT/--NAM/--SPEC/--METHOD/--LOBXFL, 渲染 p196 确认非 BS, 排除.)
- **gaps (8 脚注原子)**: 8 域 spec.md 各 1 段, 逐字 = PDF (p150/p169/p172/p179/p181/p183/p193/p198), 均位于最后变量块 `---` 之后、`## Cross References` 之前 (U7). 已落地 8/8.
- **反向 KB→PDF (8 文件全扫, Cross References 前)**: 除变量字段行/`###`/`---` 外仅 `# XX — Name` 标题、`> Class|Structure` 行 (U8 导航)、新增脚注行; Cross References 块为导航 (U8). 无 PDF 出处且未 D6 的解释性行 = 0.
- **范围外渲染顺带核 (非样本)**: IE:VISIT / DA:VISIT ("a clinical encounter") / DA:TAETORD (Section 7.2.1 xref) / CE:CESTTPT (--STRTPT) / CE:CEENRTPT / HO:HOSTTPT / DV:TAETORD / BS:BSREFID (Exp) / DD:DDDTC 与渲染一致.
- **diff 授权范围**: `git diff HEAD -- 8×spec.md` 仅 20 处 `Controlled Terms:` 空→`*` + 8 段脚注插入; 无其他改动. (工作树别批文件 model/03、model/04、CO 等不计.)
- live docs: `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).
- G-TB8: trace.jsonl L374 writer (`oh-my-claudecode:executor`) + L379 reviewer (`oh-my-claudecode:code-reviewer`, PASS) 的 subagent_done 存在; 无本批 `agent: main` 写 KB 记录.

## 5. 与 writer / reviewer 对照 (独立判后)
- writer: 28 改动 (CT * 20 + 脚注 8), 结构/删除/PDF_TYPO 0 — 与本审 diff 与 CT 全总体结果一致.
- reviewer PASS: 195/195 变量 + 顺序、CT * 20/20、脚注 8/8、U7 位置 — 与本审计数闸及补充核查一致. 无分歧.

## 结论
抽检 N=21 (seed 20261126): 独有丢失 0, 忠实度错 0, 位置错 0 → **PASS**.
