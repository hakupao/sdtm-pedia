# T2S.S-SPC1 Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-SPC1.md` / `t2_S-SPC1_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC1_auditor/` (sample.py / locate.py / reverse.py / fuzzy.py, 均 repo 根执行 `python3 -I`)

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (N=30).

## 抽样 (可复跑; repo 根 `python3 -I $S/sample.py`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW},
    且 (parent_section 前缀, 页范围) ∈ {§6.3.5.3 CP 199-220, §6.3.5.4 GF 220-228, §6.3.5.5 IS 228-241, §6.3.5.6 LB 241-248,
    §6.3.5 194-196, §6.3.5.1 194-196 (LB 通用, 主控指定)}; 边界页别节原子 (BS/MB/§6.3.5.7) 排除;
    减 ledger INTENTIONAL_EXCLUDE (本范围命中 247). intros 为空.
writer 页 = S-SPC1.writer.jsonl pdf_page 集合 (24 页: 195,199-201,204-206,212,216,219,220,222,223,227,229,231-233,236,241,242,244,245,247); C = P 中落在 writer 页的原子.
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 638, |C| = 240, N = 30 (writer 页 10 + 其余 20), seed = 20261126.

## 样本判定 (pdf_atoms 本段抽取错多, 终判以 `pdftotext -layout` + 110dpi 渲染为准; TABLE_ROW 渲染逐格: p195/201/203/211/213/226/228/229/239)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0223_a015 | 223: GF asm 2 non-host organisms 引句 | GF/assumptions.md:19 | 否 | 是 | 是 | 逐字 |
| 2 | ig34_p0220_a002 | 220: CP Ex8 Row 1 续 (penultimate gate, CPBDAGNT/CPTSTPNL) | CP/examples.md:303 | 否 | 是 | 是 | 原子作 "identified in", layout 为 "identified using" = KB |
| 3 | ig34_p0195_a011 | 195: 通用表 USUBJID 行 | LB/assumptions.md:24 | 否 | 是 | 是 | 渲染逐格 |
| 4 | ig34_p0232_a003 | 232: IS asm 5 Ag/Ab 组合例外 | IS/assumptions.md:21 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0233_a003 | 233: IS Ex1 引句 tiered ADA | IS/examples.md:5 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0195_a023 | 195: 通用表 --STRESN 行 | LB/assumptions.md:36 | 否 | 是 | 是 | 渲染逐格 |
| 7 | ig34_p0241_a019 | 241: IS Ex11 区域过敏原 SUPPIS 句 | IS/examples.md:269 | 否 | 是 | 是 | 逐字 (边界页属 §6.3.5.5) |
| 8 | ig34_p0205_a009 | 205: CP asm 6a-i | CP/assumptions.md:64 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0206_a001 | 206: CP asm 6c 续 (CPBNDAGT) | CP/assumptions.md:72 | 否 | 是 | 是 | CPBDAGNT = T-21 改正 (spec 变量名 p201) |
| 10 | ig34_p0232_a007 | 232: IS asm 7b mixed antigens panel | IS/assumptions.md:27 | 否 | 是 | 是 | 本批 "mixed antigens" 照 PDF; 弯/直引号 = S-TYPO |
| 11 | ig34_p0212_a010 | 212: CP Ex3 "Sub" 后缀说明 | CP/examples.md:105 | 否 | 是 | 是 | 逐字 |
| 12 | ig34_p0218_a015 | 218: CP Ex7 CPSPTSTD/CPTSTPNL 句 | CP/examples.md:267 | 否 | 是 | 是 | 同段 CPGATEDEF→CPGATDEF 为 B-CP 既有登记 |
| 13 | ig34_p0203_a016 | 203: spec CPNAM 行 | CP/spec.md (### CPNAM) | 否 | 是 | 是 | 渲染逐格 |
| 14 | ig34_p0229_a010 | 229: spec ISREFID 行 | IS/spec.md:66 | 否 | 是 | 是 | 渲染逐格 |
| 15 | ig34_p0226_a002 | 226: GF Ex2 Rows 2-4, 8-10 | GF/examples.md:74 | 否 | 是 | 是 | 逐字 |
| 16 | ig34_p0213_a021 | 213: CP Ex4 引句 CCR5 | CP/examples.md:144 | 否 | 是 | 是 | 逐字 |
| 17 | ig34_p0239_a014 | 239: IS Ex9 r1 SAU1230 | IS/examples.md:205 | 否 | 是 | 是 | 渲染逐格; PDF "AUREUS–EPITOPE" en dash = S-TYPO |
| 18 | ig34_p0205_a011 | 205: CP asm 6b-iii | CP/assumptions.md:66 | 否 | 是 | 是 | 逐字 |
| 19 | ig34_p0239_a003 | 239: IS Ex8 r1 RSV1230 | IS/examples.md:185 | 否 | 是 | 是 | 渲染逐格 |
| 20 | ig34_p0245_a012 | 245: LB asm 4 (Section 4.4.8) | LB/assumptions.md:70 | 否 | 是 | 是 | 交叉引用在 |
| 21 | ig34_p0229_a008 | 229: spec ISSEQ 行 | IS/spec.md (### ISSEQ) | 否 | 是 | 是 | 渲染逐格 |
| 22 | ig34_p0228_a014 | 228: GF Ex5 ms.xpt r1 | GF/examples.md:179 | 否 | 是 | 是 | 渲染逐格 |
| 23 | ig34_p0226_a030 | 226: GF Ex2 di.xpt r2 MANUF | GF/examples.md:114 | 否 | 是 | 是 | 渲染逐格 |
| 24 | ig34_p0227_a004 | 227: GF Ex4 Rows 2-6 | GF/examples.md:122 | 否 | 是 | 是 | 逐字 |
| 25 | ig34_p0211_a001 | 211: CP Ex1 r4 (跨页续行) LYMLE | CP/examples.md:65 | 否 | 是 | 是 | 渲染逐格 |
| 26 | ig34_p0235_a028 | 235: IS Ex5 RSV 疫苗叙述首句 | IS/examples.md:101 | 否 | 是 | 是 | 逐字 (KB 合段, S-FND 口径不计) |
| 27 | ig34_p0201_a007 | 201: spec CPTSTCND 行 | CP/spec.md:138 | 否 | 是 | 是 | 渲染; CT C181175 = U5 归 S-CT |
| 28 | ig34_p0246_a001 | 246: LB asm 7 续 (Define.xml, new-term) | LB/assumptions.md:76 | 否 | 是 | 是 | 逐字 |
| 29 | ig34_p0213_a010 | 213: CP Ex3 r3 Mono Sub NON-PROLIFERATING | CP/examples.md:131 | 否 | 是 | 是 | 原子列错位; 渲染逐格 = KB (CPSBMRKS 空, CPGATDEF FSC+SSC+\|CD14+) |
| 30 | ig34_p0203_a018 | 203: spec CPSPEC 行 | CP/spec.md (### CPSPEC) | 否 | 是 | 是 | 渲染; CT C-code = U5 |

独有丢失 0 / 30; 忠实度错误 0 / 30; 位置错误 0.

## 另查
- **gaps**: CP S (`## CP – Specification` + cp.xpt 句, CP/assumptions.md:46-48, Description 之后 Assumptions 之前, 对 p200 逐字) + F (CP/spec.md:564); IS F (IS/spec.md:492) + 补 `## IS – Specification` 标题 (p229 原有); LB D (:54-56) + S (:58-60) 对 p241/242 逐字, 位于通用 §6.3.5.1 表/脚注之后、LB Assumptions 之前. 各 spec 脚注均在最后变量块之后、`## Cross References` 之前 (U7), 逐字对 p204/223/231/245.
- **footnote_moves**: GF/assumptions.md 脚注删除 → GF/spec.md:519 落地. ✔
- **CT `*`** (layout p200-205/221-223/229-232/242-245 CT 列): CP 0, GF GFSYM, IS ISCAT/ISSCAT, LB LBCAT/LBSCAT/LBTOX/LBTOXGR = KB `Controlled Terms:** *` 恰此 7 项. ✔
- **本批词级改动** 逐条对 layout: CP asm 6 "structure of CPTEST depends" (p205)、8a `"|"` (p206)、IS asm 2 "allergy trials" / 7b "mixed antigens panel" (p232) 均 = PDF; T-17..T-21 (sting / CSMRKS / CPSMRKS / --BNDAGT / --GATEDEF / CPBNDAGT / spec CPCELSTA CPSMRKS) 正确值均可由 PDF 自身 spec 变量名定 → 改正合规.
- **IS "Examples Notes" 附录删除 (D2)**: 12 行叙述在 IS/examples.md 逐条命中 (Ex1 Row1-3, Ex8-9 引句, Ex10 引言+Rows 1-5/6-11, Ex11 Row1/2-3/4-5/6-7/8-9); 唯一差 "nucleoar" (PDF p240) vs examples.md "nucleolar" = B-IS T-4 既有登记. 留 1 行交叉引用 = D2 口径.
- **反向 KB→PDF 全文件扫** (12 文件, `python3 -I $S/reverse.py $S` 129 条未命中 → `fuzzy.py` + layout 逐条定性): 全部归为 (a) 导航 (Cross References / `> Class|Structure` / 交叉引用指针行, U8); (b) 已登记 PDF_TYPO: CP T-8b/T-9/GATEDEF 系 (B-CP)、T-16b CPSCMRKS、T-17..T-21; GF inheritabilty/respresented (B-GF); IS T-4 nucleoar、T-5 "participating in" (B-IS); (c) pdftotext 跨页/跨列交错伪阴性 (LBCOLSRT/LBSTRESC/LBSTRESN/ISDRVFL/ISELTM/ISTPTREF/CPGATE 等, layout 逐字一致). 无 PDF 出处且未 D6 的行 = 0.
- **授权范围**: `git diff HEAD --stat` 本批仅 CP/GF/IS/LB 的 assumptions.md + spec.md 8 文件 (∈ kb_files); narrow_files 空. 工作树 MB/MS/PC/PP 改动属 S-SPC2, 未计.
- **G-TB8**: trace 有 writer (executor) 07:05:02Z、reviewer (code-reviewer, PASS) 07:16:58Z; 8 文件 mtime 06:57:02Z (15:57:02 JST) < reviewer 完成, 无 reviewer 后改动; 无 agent main 写 KB. ✔
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).

## 对照 writer / reviewer (判完后读)
与 reviewer PASS 一致 (CT `*` 7/7 且 CP 0、T-16..T-21 依据、IS D2 12 行副本全在、脚注位置). writer 方法注记 "pdf_atoms 本批页至少 12 处抽取错" 与本审 #2/#29 观察一致. 无分歧.
