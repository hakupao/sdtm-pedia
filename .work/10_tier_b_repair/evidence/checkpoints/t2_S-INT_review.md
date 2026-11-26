# T2S S-INT reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 3 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/{AG,PR,EX,EC}` (含 attempt 1 delta #21). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-INT_reviewer/`
  自写脚本 (不复用 writer 的): `bscan.py` (k2p: KB 逐行分句/表行逐格查 PDF 页段; p2k: PDF 页逐句查 KB, 连字符折行容错), `ctcol.py` + `ctcmp.py` (pdftotext -bbox 按表头 Type/Role x 取 CT 列, 逐变量对 spec.md), `speccmp.py` (bbox 按 6 列表头分列, 逐变量 Label/Type/Role/Notes/Core 对 spec.md); 渲染 p92/103/104/105/107/108/111/112/114/115/116/118/119/125.
- 授权范围: `git diff HEAD --stat -- knowledge_base/` 中本批改动 9 文件 (AG asm/ex/spec, PR asm/spec, EX asm/ex/spec, EC spec), 全部 ∈ kb_files; narrow_files 空; PR/examples、EC/assumptions、EC/examples 未动. 其余 diff 文件 (CP/DA/EG/GF/IS/LB/MB/MS/OE/PC/PE/PP/SS/UR) 属并行批, 不计.
- md5 与 writer 报告逐一相符 (9 文件, 含 EX/examples `2fd243a8…` delta 后).

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-INT_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; OK 30 / UNPARSEABLE 11 / DIFF 1; cells 2390; diffs 3 (= EX T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1 RED; 67 regress, 60 已登记预期; 余 7 在 p199/200/206/240/255 (他批), 本批页 0
for D in AG:92,93,94 PR:125,126 EX:104,105 EC:107,108,109; do python3 -I $S/ctcmp.py ${D%%:*} ${D#*:} $S; python3 -I $S/speccmp.py ${D%%:*} ${D#*:}; done   # 变量数/顺序 AG 41 PR 45 EX 37 EC 45 一致; 非 CT 字段 DIFF 仅末变量吸入表下脚注/正文 (bbox 截止误差)
python3 -I $S/bscan.py k2p 92 97 knowledge_base/domains/AG/{assumptions,examples}.md   # (及 PR 125 128 / EX 103 120 / EC 103 120)
python3 -I $S/bscan.py p2k 92 97 knowledge_base/domains/AG/{assumptions,examples,spec}.md   # (及 PR / EX+EC)
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
- census PDF_ONLY 落在本批页的 2 张 (p102-103 cm.xpt Ex4 / p103 cm.xpt Ex5) 属 §6.1.2 CM, 不计. pdf_unparsed (p274/p342) 非本批页.

### 页范围复核 (O20)
- 同意 writer 更正: AG p92-97 (p92 顶 §6 章标题 + §6.1 引言, p98 首行 §6.1.2); EX p104-107 上部; EC p107 下部-p110; §6.1.3 父节 p103 下部 (上部 CM Ex4/Ex5 别节) 至 p120 (p121 首行 §6.1.4 ML); PR p125-128 (p129 首行 §6.1.6 SU).

### 双向全扫 — 逐页 (reviewer 自己的计数)
| 页 | PDF→KB (p2k) | KB→PDF (k2p) | 表 | 结论 |
|---|---|---|---|---|
| 92 | 27 句段, miss 9 = §6/§6.1/§6.1.1 标题与正文拼段 2 + spec 表拼段 7; §6.1 引言句、Description、spec 首句逐字核 (layout) 命中 | AG/asm 45 单元 miss 1 = `## §6.1 …` 的 § (结构, AE §6.2 先例) | spec 14 变量 (bbox) | 一致; §6 章标题不落地 (主控裁定) |
| 93 | 43 / 14 = 全部 spec 表拼段 | spec 逐字段 | 22 变量 | 一致 |
| 94 | 35 / 12 = spec 拼段 + "AG – Assumptions 1." 拼段 | 脚注逐字 | 5 变量 + 脚注 | 一致 |
| 95 | 32 / 0 | AG/asm 2b-5b, examples 叙述 | — | 一致 |
| 96 | 14 / 3 = 表拼段 (首句 CMSPID/AGSPID 定点核命中); "SDTMIG-MD" PDF p96:153 | AG/ex 54 单元 miss 0 | ag/cm/ag census OK | 一致 |
| 97 | 1 / 1 = re/relrec 表拼段 | 同 | census OK | 一致 |
| 103 | 15 / 12 = CM Ex4/Ex5 别节 11 + 表 1; §6.1.3 引言 2 句逐字命中 | EX/asm:3 `## §6.1.3 …` 结构 | — | 一致 |
| 104 | 43 / 12 = 标题拼段 1 + spec 拼段 11 | spec | 27 变量 | 一致 |
| 105 | 34 / 12 = spec 拼段 | 脚注逐字; asm 1a-1b | 10 变量 + 脚注 | 一致 |
| 106 | 31 / 0 | EX/asm k2p miss 2 (:25 :38) = pdftotext 去连字符假阳 (layout 核 "protocol-specified" / "constant-dosing" 命中) | — | 一致 |
| 107 | 31 / 4 = T-7 句、§6.1.3.2 标题拼段、spec 拼段 | EX/asm:47 miss = T-8 | EC 11 变量 | 一致 (T-7/T-8 渲染确认) |
| 108 | 45 / 15 = spec 拼段 | spec | 25 变量 | 一致 |
| 109 | 32 / 9 = spec 拼段 + 脚注拼段 + "EC – Assumptions 1." | EC/asm 50 单元 miss 0 | 9 变量 + 脚注 | 一致 |
| 110 | 27 / 0 | 同 | — | 一致 |
| 111 | 15 / 5 = §6.1.3.3 标题拼段 + CRF/表拼段 (首句定点核命中) | EX/ex:3 新标题 = PDF p111 原标题 | Ex1 CRF ×2 渲染逐格 (下) | 一致 |
| 112 | 6 / 3 = CRF/表拼段 | 同 | Ex2 CRF 渲染逐格 | 一致 |
| 113 | 5 / 2 = bullet 拼段 | EX/ex:115-118 bullet (• vs -), :118 = T-3 | census OK | 一致 |
| 114 | 9 / 2 = CRF 拼段 | 同 | Ex5 CRF ×3 渲染逐格 | 一致 |
| 115 | 13 / 3 = 表拼段 + T-4 句 | EX/ex:207 = T-4 | Ex6 CRF 56789001 渲染逐格 | 一致 |
| 116 | 1 / 1 = CRF 拼段 | 同 | Ex6 CRF 56789003 渲染逐格 | 一致 |
| 117 | 9 / 4 = 表 + bullet 拼段 ("The CRF shows that:" 定点命中) | EX/ex:333-335 bullet | census OK | 一致 |
| 118 | 15 / 4 = CRF 拼段 + T-6 | EX/ex:362 = T-6 | Ex7 CRF 渲染逐格 | 一致 |
| 119 | 11 / 4 = T-2 + CRF/表拼段 | EX/ex:403 = T-2 | relrec T-1; Ex8 CRF ×2 渲染逐格 | 一致 |
| 120 | 5 / 2 = 表拼段 ("Shows the remaining administrations…" 命中) | EX/ex 339 单元 miss 18 全部归入上列 (H1/§ 标题/KB note/bullet/T-n) | census OK | 一致 |
| 125 | 33 / 13 = 标题拼段 + spec 拼段 | PR/asm 32 单元 miss 0 | 22 变量 (bbox 全字段 = KB; 不依赖原子) | 一致 |
| 126 | 39 / 14 = spec 拼段 | 脚注逐字 | 23 变量 + 脚注 | 一致 |
| 127 | 28 / 0 (PR T-1 句以去空格容错命中) | 同 | — | 一致 |
| 128 | 5 / 3 = 表拼段 (首句定点核命中) | PR/ex 40 单元 miss 0 | census OK | 一致 |

### intros / gaps / footnote 逐项
| 项 | 位置 | 逐字 | 结论 |
|---|---|---|---|
| §6.1 引言 (AG/asm:3-5) | H1 后、AG Description 前 | **p92 渲染确认 PDF 以 "the Interventions class include:" 结束, 其后直接 §6.1.1, 无域列表**; KB 逐字一致 | ✓ |
| §6.1.3 引言 (EX/asm:3-5) | H1 后、EX Description 前 | p103 一段 2 句逐字一致 | ✓ |
| AG D/S/A | asm:7-15 | 定义句、spec 首句 (— em dash) 逐字; 标题 en dash 照 PDF | ✓ |
| PR D/S/A | asm:3-11 | 逐字 | ✓ |
| EX D/S/A | asm:7-15 | 逐字 (2 句 Description) | ✓ |
| 脚注 ×4 (AG:375 PR:411 EX:339 EC:411) | 末变量块 `---` 后、`## Cross References` 前 (U7) | `¹In this column, …enclosed in parentheses.` 与 p94/p126/p105/p109 逐字 | ✓ |
| EC D/S | 既有 (B-EC) | p107 逐字 | ✓ |

### spec.md Controlled Terms 逐变量 (bbox CT 列 + 渲染 p92/93/105/108)
- PDF `*` 14 = KB `*` 14: AG AGDECOD AGCAT AGSCAT (p92) AGCLAS AGCLASCD (p93); PR PRCAT PRSCAT (p125); EX EXTRT EXCAT EXSCAT (p104) EXADJ (p105); EC ECTRT (p107) ECCAT ECSCAT (p108). 渲染确认 ECADJ PDF 空、EXADJ `*`.
- ISO 8601 格: AG 3 / PR 5 / EX 5 / EC 5 全一致.
- 其余 CT 差异全部为 C-code vs PDF 括号短名 (AG 14, PR 15, EX 11, EC 17) 与 DOMAIN 空 (4) → U5/U6 归 S-CT, 本批不改 ✓.
- 非 CT 字段 (Label/Type/Role/Notes/Core) 四域全一致 (p125 原子编造, 以 bbox 为准: PRGRPID/PRLNKID/PRINDC/PRDECOD = KB).

### census_items 人工逐格 (渲染, 不采信 writer)
| KB 表 (改后行号) | 渲染 | 结果 |
|---|---|---|
| EX/ex:15 Ex1 CRF ABC1001 | p111 100dpi | 表头 5 + 1 行 × 5 格一致 |
| :21 Ex1 CRF ABC2001 | p111 | 3 行 × 5 格一致 (含 0 / Patient mistake / 2011-01-24) |
| :67 Ex2 Exposure CRF | p112 100dpi | 14 行 × 2 格一致; PDF 无表头 (Markdown 空表头 = 结构); "Injection 1/2/3" PDF 常规字重 → 去粗体正确 |
| :175/:182/:189 Ex5 CRF ×3 | p114 | 各 2 行 × 5 格一致 (2012-01/02/03-01 → -08) |
| :245 Ex6 CRF 56789001 | p115 100dpi | 2 级表头 + 3 行 × 10 格一致 (07:30/07:30/07:32; 07:30/07:30/07:34) |
| :254 Ex6 CRF 56789003 | p116 100dpi | 3 行 × 10 格一致 (07:30/07:24/07:24; 07:30/07:43/07:38) |
| :341 Ex7 CRF | p118 100dpi | 15 行 × 4 列一致; 粗体 = PDF 粗体 (V1 10 mg/kg, Yes; V2 7.5 mg/kg, Dose-limiting toxicity, Yes, Injection site reaction; V3 7.5 mg/kg, No, "Other, specify:" + 常规 Personal reason); • 与下划线未录 (格式) |
| :409 Ex7 relrec | p119 | 6 行 × 8 列; Row PDF 1,2,6,3,4,6 vs KB 1-6 = T-1 (同表连续编号 + "Rows 1-3/4-6" 叙述自证), 余一致 |
| :424 / :428 Ex8 CRF ×2 | p119 | 1 行 × 2 / 2 行 × 2 一致 |

### PDF_TYPO 依据核
| T | 核 | 结论 |
|---|---|---|
| EX T-7 (p107 item 5 尾 "…document.Additional interventions qualifiers") | p107 渲染可见重复, 下一行即 "6. Additional interventions qualifiers" | 成立, PDF 自身可定, KB 正确值 ✓ |
| EX T-8 (p107 6d "–PRESP") | 渲染可见 en dash; 同句 --OCCUR/--STAT/--REASND | 成立 ✓ |
| PR T-1 (p127 "collected.Measurements") | pdftotext p127:30 缺空格 | 成立 ✓ |
| EX T-1..T-6 沿用 | T-1 (p119 渲染)、T-2 (p119 "--LNKID, .")、T-3 (layout "ottles")、T-4 (p115 "protocol specified")、T-6 (p118 渲染 "mg/mL") 复核成立; T-5 仍 T4 | ✓ |

### 结构改动 / 删除 / D6 签字
- S-1 AG/asm `## §6.1 Models for Interventions Domains` — PDF p92 标题 ✓ (U3; AE §6.2 先例)
- S-2 EX/asm `## §6.1.3 Exposure Domains` — PDF p103 ✓ (U3/O45)
- S-3 AG/PR/EX 各 `## XX – Description/Overview|Specification|Assumptions` — PDF p92/94, p125/127, p104/105 ✓ (DS/EC 先例)
- #21 EX/ex:3 `## §6.1.3.3 Exposure/Exposure as Collected Examples` — PDF p111 原标题 ✓ (主控裁定; `grep -rn "EX/examples.md#"` 无入链)
- §6 章标题 p92 不落地 — 主控裁定 (dispatch notes T2S 末条) ✓
- D-1 "SDTM-MD"→"SDTMIG-MD" (p96:153 原文; 全 PDF 无 "SDTM-MD") ✓; D-2 14 处 CT 空→`*` ✓; D-3 Ex2 CRF 粗体去除 ✓. 无内容整条删除.
- D6: 无新增; EX/ex:5 既有 KB note 与 PDF 不矛盾 ✓. G-TB6 新增/改动行 (diff `+` 非空行) 共 42 条 (标题 11、引言/定义/spec 首句 8、脚注 4、CT `*` 14、SDTMIG-MD 1、去粗体 3、§6.1.3.3 标题 1), 无出处 0.

### LOW 观察 (不阻断)
| ref | 问题 | 建议 |
|---|---|---|
| L-1 EX/ex:171 :241 :337 :422 `**CRF:**`, :339 `**Subject ABC123-0201**` | PDF 无此标签 (p114/115/118/119 表前直接是 Subject 标签或表); 既有 (非本批改动) | 按 U8/dispatch "表前短标签" 属导航, 保留; 记录供 S-TYPO/T3 参考 |
| L-2 EX/ex:5 KB note | 新 §6.1.3.3 标题后该 note 部分冗余 | 不矛盾, 保留 |
| L-3 AG/asm:5 §6.1 引言以 ":" 结尾无列表 | PDF 原样 (与 §6.2 有列表不同) | 照录正确; 可在 T3/T4 汇总提示为 PDF 自身遗漏 (非 KB 缺陷) |

### fp_match 回归
- 67 regress − 60 已登记预期 = 7, 页码 p199/200/206/240/255 (并行批), 本批页 (92-97/103-120/125-128) 新增 RED 0.
