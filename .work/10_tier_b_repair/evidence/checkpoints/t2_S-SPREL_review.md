# T2S S-SPREL reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 5 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/{SE,RELREC,RELSUB,RELSPEC,OI,DI}`. scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPREL_reviewer/`
  脚本: `bscan.py` / `speccmp.py` (S-EVT reviewer 自写, 非 writer 脚本) + 本批新写 `frag.py` + `bnorm.py` (PDF 侧在表/Row 标签/节号处切开再逐句查, 消除粘连伪差). 渲染 100dpi: p79/80/82/83/84/429/430/438/439/440/441 (另渲染 p427/431/437/442/443 备查).
- 授权范围: `git diff HEAD --stat` 本批 9 文件 = SE/{assumptions,examples,spec}, RELREC/spec, RELSUB/spec, RELSPEC/spec, OI/{assumptions,spec} (∈ kb_files) + DI/assumptions (narrow). 工作树中 FA/SR/TA/TD/TM/TR 改动属 S-TDM / S-TUFA, 不计. 其余 6 个 kb_files 零 diff.
- DI narrow: diff 仅 +7 行 (文件顶部 `## §9 Study References` + 段 + 2 bullet), 无删除; 逐字比较 (下方命令) = `True`. narrow (b) 不适用 (主控已裁定; p441 渲染确认 §9.1 无 spec 表, 页内唯一脚注在 OI 表下).

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPREL_reviewer; K=knowledge_base/domains
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; KB 表 12: OK 10 / DIFF 2; cells 588; diffs 2 (= SE T-1 表头 ×2)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1 RED; 71 regress, 对 t2_fp_expected_regressions.jsonl 差集 = 0; 本批页回归 = p0079_a004/a006/a009/a010 (均已在 expected)
for d in SE:79,80 RELREC:429 RELSUB:438 RELSPEC:439 OI:441; do python3 -I $S/speccmp.py $S ${d%%:*} ${d#*:}; done   # bb_<p>.html = pdftotext -bbox; 非 OK 仅 U5/U6
bash -c 'for u in "RELREC 427 431" "RELSUB 437 439" "RELSPEC 439 440" "OI 441 443"; do set -- $u; python3 -I '$S'/bscan.py k2p $2 $3 knowledge_base/domains/$1/assumptions.md knowledge_base/domains/$1/examples.md; done'
python3 -I $S/bscan.py k2p 79 84 $K/SE/assumptions.md $K/SE/examples.md ; python3 -I $S/bscan.py k2p 441 441 $K/DI/assumptions.md
bash -c 'for u in "RELREC 427 431" "RELSUB 437 439" "RELSPEC 439 440" "OI 441 443" "SE 79 84"; do set -- $u; python3 -I '$S'/frag.py '$S' $2 $3 knowledge_base/domains/$1/assumptions.md knowledge_base/domains/$1/examples.md knowledge_base/domains/$1/spec.md; done'
python3 -I -c "import re;t=open('.work/10_tier_b_repair/work/pdf_pages/ig34_p0441.txt').read();p=re.sub(r'\s+',' ',t[t.index('There are occasions'):t.index('9.1 Device')].replace('•','')).strip();k=open('knowledge_base/domains/DI/assumptions.md').read();k=re.sub(r'\s+',' ',k[k.index('There are occasions'):k.index('## DI –')].replace('\n- ',' ')).strip();print(p==k)"   # True
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
- census PDF_ONLY 落在本批页的 2 张: p79 suppdm.xpt (§5.2 DM Ex7) / p428 cm.xpt (§8.1, ch08) — 均别节, 不计. pdf_unparsed 无本批页.
- gap 原子直查目标文件 (`fp_match.norm`): ig34_p0080_a010 (去掉抽取错的前导 `*`) → SE/spec ✔; p0429_a030 → RELREC/spec ✔; p0438_a011 (去掉 `1 `) → RELSUB/spec ✔; p0439_a039 → RELSPEC/spec ✔; p0443_a001 → OI/spec ✔; p0441_a002..a005 → DI/assumptions ✔.

### 页范围复核 (同意 writer O20 更正)
- SE §5.3 = p79 中部 – p84 上部 (p79 上部 suppdm 属 §5.2; p84 dm Ex2 r2 后即 §5.4 SM). RELREC = p427 下部 (§8 引言 IDVAR 段, D7/B-REL) + p429-431 (§8.4 标题前止). RELSUB §8.7 = p437 下部 – p439 中部. RELSPEC §8.8 = p439 中部 – p440 (p441 首行即 §9). OI §9.2 = p441 下半 – p443. DI = p441 上部 §9 引言.

### 双向全扫 — 逐页 (reviewer 自己的计数)
| 页 | PDF→KB | KB→PDF | 表 | 结论 |
|---|---|---|---|---|
| 79 | §5.3 标题 / Description 7 句 + 3 bullet / Spec 标题 + xpt 句 全命中 (frag 未命中仅别节 suppdm Row1/2/Note + spec 表行粘连) | SE/asm :1-23 全有出处 (改 4 处与渲染一致) | spec 4 变量: USUBJID/SESEQ speccmp OK; STUDYID 渲染核 (bbox 漏读) 一致; DOMAIN = U6 | 一致 |
| 80 | spec 9 变量 + 脚注 + Assumptions 标题/2 段/1-3 全命中 | SE/asm :25-35 全有出处 | ETCD 渲染核 (bbox 漏读; Label/Type/`*`/Topic/Req/Notes 1-2 一致); ELEMENT…SEUPDES speccmp OK; EPOCH = U5 | 一致 |
| 81 | asm 4-11 + SE – Examples 引言全命中 | SE/asm :37-54、SE/ex :1-3 全有出处 | — | 一致 |
| 82 | Ex1 叙述 Row 1-4 / Rows 5-8 / 9-10 / dm Row 1-3 叙述全命中 | SE/ex :5-41 全有出处 | se.xpt census OK 10×9; dm r1-2 渲染逐格 (下) | 一致 |
| 83 | Ex2 叙述 4 段 + Rows 1-2/3-6 + Row 1/2 全命中 (含新补句) | SE/ex :48-75 全有出处 | se.xpt census OK 6×9; dm r3 / Ex2 r1 渲染逐格 | 一致 |
| 84 | dm Ex2 r2 (其余 = §5.4 SM 别节) | SE/ex :79-82 | 渲染逐格 | 一致 |
| 427 | §8 IDVAR 段 + 3 bullet 命中; 章标题/首段/8 bullet 未在 RELREC (主控定留 ch08) | RELREC/asm :3-10 (Source text 行 / D6 note = 导航+既有 D6) | — | 一致 |
| 428 | 全页 §8.1 别节 | — | cm.xpt 别节 | — |
| 429 | §8.2 4 段 + "either:" 列表 (KB :20-22 拆行, 逐字) / §8.2.1 Description / Spec 句 全命中 | RELREC/asm :12-30 全有出处 | 7 变量: 5 OK + RDOMAIN/RELTYPE = U5; IDVAR `*` 渲染一致 | 一致 |
| 430 | §8.2.2 Ex1-3 叙述 + "Additional examples…" + §8.3 2 段全命中 (渲染核) | RELREC/ex :5-53、asm :32-36 全有出处 | relrec ×3 census OK; Ex3 "COMBO 1" 弯引号 (PDF) vs KB 直引号 = 排版 | 一致 |
| 431 | §8.3.1 叙述全命中; `‑‑LNKID` U+2011 归一化后命中 | RELREC/ex :55-68 全有出处 | relrec census OK | 一致 |
| 437 | §8.7 标题 + RELSUB Description 命中 (其余 §8.6 别节) | RELSUB/asm :5-9 | — | 一致 |
| 438 | RELSUB Spec / 5 变量 / 脚注 / asm 1-8 全命中 (asm 7 句末 PDF 无句号 = T-9) | RELSUB/asm :11-31 全有出处 | 5 变量: 4 OK + SREL = U5; 无 `*` (渲染) | 一致 |
| 439 | RELSUB Ex1 叙述 + §8.8 框注 + RELSPEC Description / Spec / 6 变量 / 脚注 全命中 | RELSUB/ex、RELSPEC/asm :5-13 全有出处 | dm / relsub census OK; RELSPEC 5 OK + STUDYID 渲染核一致 + SPEC = U5; 无 `*` | 一致 |
| 440 | RELSPEC asm 1-3 + Examples + 图后 3 句全命中 | RELSPEC/asm :15-21、ex 全文; Mermaid = 既有 D6 | relspec census OK; 图 (渲染) L1 SPC-001(Tissue)/SPC-003(Brain), L2 -001-A/-001-B(Tissue)/-003-A(RNA), L3 -001-B-1(DNA), 4 边 = Mermaid 一致 | 一致 |
| 441 | §9 引言 (→DI) / §9.1 (DI 既有) / §9.2 OI Description 2 段 / Spec 句 / 7 变量 / 脚注 全命中 | DI/asm 全文, OI/asm :1-11 全有出处 | 7 变量: 4 OK + DOMAIN U6 + OIPARMCD/OIPARM U5; OIVAL `*` 渲染一致 | 一致 |
| 442 | OI – Assumptions 1-5 + Examples 叙述全命中 | OI/asm :13-30、OI/ex :1-23 | oi.xpt census OK (跨 p442-443) | 一致 |
| 443 | oi r6-14 | OI/ex :24-32 | census OK | 一致 |
- k2p (KB→PDF) 总计: SE 141 单元 miss 7 (全为 dm 表头/行 = PDF 单元格折行, census+渲染已核); RELREC 108 miss 9 / RELSUB 64 miss 5 / RELSPEC 61 miss 30 / OI 56 miss 0 / DI 11 miss 3 — 全部为 H1/H2 导航、`> Source text:` (D7)、既有 D6 note + Mermaid 代码、T-9 句号、U+2011 排版. 无无出处正文.

### spec.md Controlled Terms 逐变量 (bbox + 渲染)
- **SE 13**: `*` 2 = ETCD ELEMENT (p80 渲染 ✔); 空 7 = STUDYID USUBJID SESEQ TAETORD SESTDY SEENDY SEUPDES; ISO 8601 datetime or interval 2 = SESTDTC SEENDTC; U5 1 = EPOCH; U6 1 = DOMAIN. 合计 2+7+2+1+1 = 13.
- **RELREC 7**: `*` 1 = IDVAR (p429 ✔); 空 4 = STUDYID USUBJID IDVARVAL RELID; U5 2 = RDOMAIN (DOMAIN) / RELTYPE.
- **RELSUB 5**: 无 `*` (p438 ✔); 空 4 = STUDYID USUBJID POOLID RSUBJID; U5 1 = SREL (RELSUB).
- **RELSPEC 6**: 无 `*` (p439 ✔); 空 5 = STUDYID USUBJID REFID PARENT LEVEL; U5 1 = SPEC (SPECTYPE)(GENSMP).
- **OI 7**: `*` 1 = OIVAL (p441 ✔); 空 3 = STUDYID NHOID OISEQ; U6 1 = DOMAIN; U5 2 = OIPARMCD (OIPRMCD) / OIPARM (OIPRM).
- 非 CT 字段 (Label/Type/Role/Core/Notes): 全 38 变量一致 (speccmp + 渲染补 3 个 bbox 漏读变量).

### census_items 人工逐格 (渲染, 不采信 writer)
| 表 | 渲染 | 结果 |
|---|---|---|
| SE/examples.md:44 Ex1 dm.xpt (p82 r1-2, p83 r3) | 100dpi | 3 行 × 20 列逐格一致 (r1 789/001/2006-06-03/2006-06-17/01/SMITH, J/1948-12-13/57/YEARS/M/WHITE/HISPANIC OR LATINO/IO/IV-ORAL/IO/IV-ORAL/空/空/USA; r2 OI/ORAL-IV/IO/IV-ORAL; r3 791/003/…/2006-06-07/1956-07-17/49). 表头 col 8 PDF BIRTHDTC / KB BRTHDTC = **SE T-1** |
| SE/examples.md:79 Ex2 dm.xpt (p83 r1, p84 r2) | 100dpi | 2 行 × 20 列逐格一致 (r1 123/012/…/JONES, D/1943-12-08/62/M/ASIAN/HISPANIC OR LATINO/A/A/A/A; r2 456/103/2006-05-03/2006-07-30/1950-05-15/55/F/WHITE/NOT HISPANIC OR LATINO/AR/A-Rescue/空/空/UNPLANNED TREATMENT/Drug B dispensed for part of Drug A element/USA). 表头 = SE T-1 |
- SE T-1 依据核: `grep -l BIRTHDTC pdf_pages/ig34_p*.txt` 全书仅 p82/83/84; DM spec/例 BRTHDTC p63(2)/65/66/68 → 正确值由 PDF 自身确定, KB 保留 BRTHDTC ✔.

### gaps / intros / footnote 逐项
| 项 | 位置 | 逐字 / 字符 | 签字 |
|---|---|---|---|
| intro §9 (a001-a005) | DI/assumptions.md:3-8, H1 后、`## DI – Description/Overview (§9.1)` 前 (U3 host 顶部) | 逐字 True | ✔ |
| SE S | SE/asm :21-23 Description 与 Assumptions 之间 | `SE – Specification` en dash、`se.xpt, Subject Elements — Special Purpose.` em dash = PDF U+2013/U+2014 | ✔ |
| SE F | SE/spec :123, SEUPDES `---` 后、`## Cross References` 前 (U7) | 逐字 (PDF p80 上标 1 → ¹) | ✔ |
| RELREC F / RELSUB F / RELSPEC F | spec :71 / :53 / :62, 末变量 `---` 后、Cross References 前 | 逐字 (p429/438/439) | ✔ |
| OI D/S/A | OI/asm :3 / :9-11 / :13 | 标题 en dash、oi.xpt 句 em dash = PDF; D 两段原有文字未动 | ✔ |
| OI F | OI/spec :69, OIVAL `---` 后、Cross References 前 | 逐字 (p441 OI 表下) | ✔ |

### 词级改动 / 新增句 逐条签字
| # | 改动 | PDF 依据 (p79/p83 渲染 + layout) | 签字 |
|---|---|---|---|
| W-1 | "study elements" → "epochs and elements" | p79 "…progress through the epochs and elements of the trial." | ✔ |
| W-2 | "definitions of ELEMENT values in" → "definitions (TESTRL values) in" | p79 "according to the definitions (TESTRL values) in the Trial Elements (TE) dataset" | ✔ |
| W-3 | `– DTC` → `--DTC` | p79 layout "Comparison of the --DTC of a finding" (两个 U+002D) | ✔ (CODE_LITERAL) |
| W-4 | "can relate" → "relate"; `(–DY)` → `(--DY)` | p79 "Such variables relate an observation…study day (--DY) variables" | ✔ |
| W-5 | SE/ex:75 补 "The subject's assignment to Rescue treatment for the open treatment epoch proceeded as planned." | p83 Row 2 第 3 句, 位置在 "…deviated from plan." 与 "The sponsor decided…" 之间; PDF 为直撇号 ' (layout 无 >0x7F 字符) = KB | ✔ |
| CT | `*` ×4 (ETCD/ELEMENT/IDVAR/OIVAL) | 见上 | ✔ |
- fp 预期回归 p0079_a004/a006/a009/a010: 原子 verbatim = 旧 KB 文本 ("study elements" / "of ELEMENT values" / "– DTC" / "can relate…(–DY)"), 与 p79 渲染不符 → 原子抽取错, 回归合理 ✔.

### 结构改动 / 删除 / D6 签字
- S-1 SE `## SE – Specification` (p79) ✔; S-2 OI 三标题 (p441/p442) ✔; S-3 DI `## §9 Study References` (p441 标题, § 前缀同 NV/FT/AE 先例) ✔.
- 删除: 仅 W-1..W-4 旧词与 4 格 CT 空值, 无整句/整条删除 ✔.
- D6: 本批无新增. 既有 RELREC/asm:5 note、RELSPEC/ex:11 Mermaid note — 复核不矛盾 (Mermaid 与 p440 图逐节点/边一致) ✔.
- PDF_TYPO: SE T-1 (KB 改正值, PDF 自身可定) ✔; SE T-2 SESEQ 缺 "with" (p79 渲染 "to be consistent chronological order") 照录 ✔; OI T-1 "to given" / T-2 "OIVAL ." (p441 渲染) 照录 ✔.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 | 原子台账 | ig34_p0443_a001 页号标 p443, 内容实为 p441 OI 表脚注; ig34_p0080_a010 上标 1 抽成 `*` (O58) | p441 / p80 渲染 |
| L-2 | 排版 (S-TYPO) | RELREC/ex Ex3 "COMBO 1" PDF 弯引号 KB 直引号; RELREC/asm:24 `RELREC – Description/Overview` en dash vs PDF p429 `RELREC - Description` 连字符 (既有, 非本批改) | p429/p430 |
| L-3 | 导航 (既有) | RELREC/ex `## Peer Record Examples` / `## Dataset Relationship Example` 为 KB 自拟, PDF 为 "8.2.2 RELREC Dataset Examples" / "8.3.1 RELREC Dataset Relationship Example"; 纯导航 (U8 口径), B-REL 既有, 不阻断 | p430/p431 |
| L-4 | 既有标题 | SE/OI/RELSUB/RELSPEC examples.md 无 `XX – Examples` H2 (H1 承担), 本批 gaps 未列 E, 规则 6 不改 | p81/p439/p440/p442 |
| L-5 | writer 报告 | 逐页日志 "未命中" 列为改前数, 已由报告末 "更正" 段修正; 本审计数为改后独立数 | — |

### 结论
PASS. 授权范围内; 双向全扫无缺口、无无出处正文; CT `*` 4/4 与渲染一致, 其余 CT 差异仅 U5/U6 (归 S-CT); 脚注 5 处位置 U7、逐字; DI narrow 仅 §9 引言逐字; census 12 表 OK 10 / DIFF 2 = SE T-1; fp 回归差集 0; live docs 42.
