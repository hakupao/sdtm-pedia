# T2S S-INT writer checkpoint (扫描批: AG / PR / EX / EC)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `056d8cc`; 本批 12 文件改前与 HEAD 一致 (cmp). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-INT_writer/`
  (base/ = `git show HEAD:` 副本; kbbase/ = git archive HEAD; apply.py 精确替换+命中断言; scan.py PDF→KB; rscan.py KB→PDF; spec_bbox.py = **bbox 词框按表头 x 分列**逐变量逐字段比对 (新, 不依赖原子; p125 原子是编造的); census_before/after.json; fp_before/after.jsonl; 渲染 p92, p111-p120 (100dpi), p118 两半 200dpi, Ex6 CRF p115/p116 220dpi, spec CT 列裁图 p93/94/104/105/107/108/109/125/126)
- md5 before → after (行数):
  AG/assumptions `92e729e0…` → `79fd2b04af3b0c670d29e2f654b0196f` (25→39); AG/examples `3e2e7634…` → `3657c0bb712a2ce9b4ec6f583ce895e1` (72); AG/spec `14aeb160…` → `2f2417bc974c817bc6d72d79d661d5be` (395→397);
  PR/assumptions `a938a2a8…` → `056d7e16a580e376ab714cc676254a7f` (16→26); PR/spec `a845d1de…` → `a7db4300b66f8ddbe526b0290b7fc686` (436→438);
  EX/assumptions `24f4b66d…` → `5fb2093e458d8ef612dd78cfb3ceb82e` (33→47); EX/examples `33e7ebcb…` → `f208c590475774eb219eaa01b43557e8` (461); EX/spec `f39d62b1…` → `06a74b34e7783b399624b14c3c883eec` (362→364);
  EC/spec `039d9ddd…` → `e922ad3c5b254089492559cdb76e93fe` (436→438). 未动: PR/examples, EC/assumptions, EC/examples.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| domains/AG | §6.1.1 | 92-98 | **92-97** | p92 顶部 §6 章标题 a001 + §6.1 引言 a002/a003 (U3 intro 归 AG), §6.1.1 标题 a004 起; p98 首行即 `6.1.2 Concomitant/Prior Medications (CM)` (a001) → 无 AG 内容 |
| domains/EX | §6.1.3.1 | 104-107 | **104-107** | p104 首行 §6.1.3.1 标题; p107 上部 assumptions 4b-6d 属 EX, 下部 a008 起 §6.1.3.2 EC |
| domains/EC | §6.1.3.2 | 107-111 | **107-110** | p107 a008 起; p111 首行即 `6.1.3.3 …Examples` 标题 → 归共用节 |
| domains/EX+EC | §6.1.3 (+§6.1.3.3) | 103-121 | **103-120** | p103 上部 CM Ex4/Ex5 (a001-a019) 属 §6.1.2 别节, a020 起 §6.1.3; §6.1.3.3 例 p111-120; p121 首行 `6.1.4 Meal Data (ML)` → 无本节内容 |
| domains/PR | §6.1.5 | 125-129 | **125-128** | p125 首行 §6.1.5; p129 首行 `6.1.6 Substance Use (SU)` → 无 PR 内容 |

### 双向全扫 — 逐页日志
方法: PDF→KB = `pdf_atoms.jsonl` 该页全部原子 (含 TABLE_ROW/TABLE_HEADER/CODE_LITERAL) 归一后在本域三文件查 (scan.py); spec 表一律以 spec_bbox.py (bbox 词框分列, 逐变量 Label/Type/CT/Role/Notes/Core + Order) 为准, 不采信原子; 例子表以 table_census.py + 渲染为准. KB→PDF = rscan.py 逐句 (assumptions/examples) + spec_bbox 反向 (kb-only 变量 = 0). 计数为改后.

| 页 | 节 | PDF→KB: 原子 / 命中 / 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 92 | §6 / §6.1 / §6.1.1 | 25 / 22 / 6→6 (a002 a003 intro; a005-a007 a009 Description/Spec) | AG/spec STUDYID..AGPRESP 逐字段一致 | spec 14 变量 (bbox) | 未命中: a001 §6 章标题 (需主控定 #1), a004 节号标题 = KB H1 等价, a010 表头 = spec 字段结构等价; CT `*` 3→3 (AGDECOD AGCAT AGSCAT); AGPRESP C-code (U5, S-CT) |
| 93 | spec | 22 / 12 / 0 | 一致 | 22 变量 | 10 未命中 = CT C-code 记法 8 + `*` 2 (已补 AGCLAS AGCLASCD); 原子 a022 AGSTRF Notes 跨页截断 (p94 续), bbox 合并后一致 |
| 94 | spec 尾 / assumptions 1-2a | 15 / 11→12 / 1→1 (脚注 a007) | assumptions 1a-1d 一致 | 5 变量 | 脚注已补 spec.md:375 (原子写法 "1In" 数字, 子串检查不命中); AGENRTPT Notes 内重复句 = PDF 原样 (p94 layout), KB 照录; `## AG – Assumptions` a008 已补 |
| 95 | assumptions 2b-5b / Examples / Ex1 叙述 | 17 / 17 / 0 | 一致 | — | `AG – Examples` = H1 `# AG — Examples` 等价 |
| 96 | Ex1 表 / Ex2 | 17 / 16→17 / 1→1 | examples.md:40 "SDTM-MD" 无出处 → 改 "SDTMIG-MD" (a017) | ag/cm/ag census OK | |
| 97 | Ex2 | 15 / 15 / 0 | 一致 | re/di/relrec census OK | |
| 103 | §6.1.2 尾 / §6.1.3 | 本批 3 (a020-a022) / 1→3 / 2→2 | EX/assumptions:3-5 | — | a001-a019 CM 别节; a020 `6.1.3 Exposure Domains` → `## §6.1.3 Exposure Domains` (U3/O45) |
| 104 | §6.1.3.1 spec | 原子 + bbox 27 变量 | spec 一致 | 27 变量 (bbox) | 缺→已补: Description 2 句 (a003 a004) + Spec (a006) + 2 标题; CT `*` 3 (EXTRT EXCAT EXSCAT); a001 节号标题 H1 等价; a007 表头结构等价 |
| 105 | spec 尾 / assumptions 1a-1b | 10 变量 + 叙述 5 / 全命中 (脚注除外) / 2→2 (脚注 a016, 标题 a017) | 一致 | 10 变量 | CT `*` EXADJ 1→1; 脚注原子漏上标 "1" (渲染有 ¹) |
| 106 | 1c-4a | 16 / 16 / 0 | 一致 | — | |
| 107 | EX 4b-6d / §6.1.3.2 EC spec 首 | EX 7 / 5 / 0; EC 原子 + bbox | EX 一致; EC/assumptions:3-9 一致 | EC 11 变量 | EX 未命中 a002 a007 = PDF_TYPO T-7 / T-8 (KB 不改); EC Description/Spec 已在 (B-EC); CT `*` ECTRT 1→1; ECMOOD C-code (U5) |
| 108 | EC spec | 31 变量 | 一致 | 31 变量 | CT `*` ECCAT ECSCAT 2→2; 余 C-code |
| 109 | EC spec 尾 / EC assumptions 1-3a | 9 变量 + 叙述 10 / 全命中 (脚注除外) / 1→1 | 一致 | 9 变量 | ECENDTC CT bbox 读成 "datetime interval" = 换行词序 (渲染为 "ISO 8601 datetime or interval" = KB) |
| 110 | EC 3a-7b | 15 / 15 / 0 | 一致 | — | |
| 111 | §6.1.3.3 Ex1 | 29 / 28 / 0 | 一致 | Ex1 CRF ×2 (C3) 渲染逐格一致; ec/ex census OK | a001 `6.1.3.3 …Examples` 标题无 KB 对应 (需主控定 #2) |
| 112 | Ex1 relrec / Ex2 | 33 / 32 / 0 | 一致; Ex2 CRF "Injection 1/2/3" KB 粗体 → 去粗体 (见变更 #18) | Ex2 CRF (C3) 渲染逐格一致; ec/ex/relrec census OK | a009 原子 "[Field] \| [Value]" = 原子虚构表头 (PDF 无表头) |
| 113 | Ex2 relrec / Ex3 | 34 / 33 / 0 | 一致 | census OK | a011 = T-3 (ottles, 沿用) |
| 114 | Ex4 / Ex5 | 27 / 27 / 0 | 一致 | Ex5 CRF ×3 (C3) 渲染逐格一致; ex census OK | |
| 115 | Ex5 / Ex6 | 33 / 31 / 0 | 一致 | Ex6 CRF 56789001 (B) 220dpi 逐格一致; census OK | a009 = T-4 (沿用); a030 原子把两级表头拼成 "Period 1: Day" (抽取错) |
| 116 | Ex6 | 30 / 21 / 0 | 一致 | Ex6 CRF 56789003 (B) 220dpi 逐格一致; ec census OK | a009 表头原子 "ECPREP/ECDOSEU" 抽取错; a017-a028 原子编造 (B-EX 已注) |
| 117 | Ex6 / Ex7 | 12 / 10 / 0 | 一致 | ex census OK | a001 编造; a009 原子与 KB:331 逐字比对一致 (原子尾截断) |
| 118 | Ex7 | 31 / 29 / 0 | 一致 | Ex7 CRF (B) 200dpi 两半逐格一致 (粗体 = PDF 勾选, 含 V3 Other specify: Personal reason); ec census OK | a013 原子 "reason?" vs PDF "reason:" 抽取错; a017 = T-6 (layout p118:20 仍为 "mg/mL", 沿用) |
| 119 | Ex7 / Ex8 | 31 / 29 / 0 | 一致 | ex/vs census OK; relrec DIFF 3 = T-1; Ex8 CRF ×2 (C3) 渲染逐格一致 | a007 VS 表头原子 "VSTRESC" 抽取错 (渲染 VSSTRESC); a011 = T-2 |
| 120 | Ex8 | 9 / 8 / 0 | 一致 | ec/ex census OK | a003 原子 "FIRST DOSE INTERVAL" 抽取错 (layout = KB "FIRST TO LAST DOSE INTERVAL") |
| 125 | §6.1.5 spec | 原子不可用 + bbox 22 变量 | spec 一致 | 22 变量 (bbox) | **p125 原子编造** (PRGRID / PRLNKID Notes / PRINDC Notes / PRDECOD Notes 均与 layout+渲染不符, KB = PDF); 缺→已补: Description/Spec 2 句 + 2 标题; CT `*` PRCAT PRSCAT 2→2; PRDECOD (PROCEDUR) C-code (U5) |
| 126 | spec 尾 | 23 变量 + 脚注 | 一致 | 23 变量 | 脚注 a025 已补 spec.md:411 |
| 127 | PR assumptions / Examples / Ex1 叙述 | 24 / 24 / 1→1 (`## PR – Assumptions` a001) | 一致 | — | 1 段末 "collected.Measurements" PDF 缺空格 = T-1 (PR) |
| 128 | Ex1-Ex3 | 31 / 31 / 0 | 一致 | pr/eg/relrec/pr census OK | |

- spec.md 非变量行 (H1、`> Class: … | Structure: …`、`---`、`## Cross References` 块) 按 U8 为导航, 未标 D6.
- spec_bbox 改后: AG 41 / PR 45 / EX 37 / EC 45 变量, Order 全一致, kb-only 0; 剩余 DIFF 全部为 CT 列 C-code vs PDF 括号短名 (U5) 与 DOMAIN CT (U6), 归 S-CT; EC ECENDTC 1 处为 bbox 读序假阳 (渲染核).

### spec.md Controlled Terms `*` (U2; PDF `*` 全部依 bbox + CT 列渲染裁图核)
- AG 5: AGDECOD :99, AGCAT :108, AGSCAT :117 (p92), AGCLAS :162, AGCLASCD :171 (p93). p94 无 `*`.
- PR 2: PRCAT :99, PRSCAT :108 (p125). p126 无 `*`.
- EX 4: EXTRT :90, EXCAT :99, EXSCAT :108 (p104), EXADJ :225 (p105).
- EC 3: ECTRT :90 (p107), ECCAT :108, ECSCAT :117 (p108). ECADJ PDF 空 (p108), p109 无 `*`.

### census_items 逐格 (渲染)
| KB 表 (改后行号) | 页 / dpi | 结果 |
|---|---|---|
| EX/examples.md:13 Ex1 CRF ABC1001 | p111 100 | 1 行 × 5 格一致 (PDF 有表头行) |
| :19 Ex1 CRF ABC2001 | p111 100 | 3 行 × 5 格一致 |
| :65 Ex2 Exposure CRF | p112 100 | 14 行 × 2 格一致; PDF 无表头行, KB 首行 `\| \| \|` 为 Markdown 结构必需; "Injection 1/2/3" PDF 非粗体 → KB 去粗体 (#18) |
| :173 / :180 / :187 Ex5 CRF ×3 | p114 100 | 各 2 行 × 5 格一致 |
| :243 Ex6 CRF 56789001 | p115 220 | 2 级表头 (Period 1/2 跨 5 列) + 3 行 × 10 格一致 |
| :252 Ex6 CRF 56789003 | p116 220 | 同上, 3 行 × 10 格一致 (07:30/07:24/07:24; 07:30/07:43/07:38) |
| :339 Ex7 CRF | p118 200 (两半) | 15 行 × 4 列逐格一致; 粗体位置 = PDF 粗体 (V1 10 mg/kg, Yes; V2 7.5 mg/kg, Dose-limiting toxicity, Yes, Injection site reaction; V3 7.5 mg/kg, No, Other, specify:); PDF 项目符号 • 与填写下划线未录 (B-EX 已说明) |
| :407 Ex7 relrec | p119 100 | 6 行 × 8 列; Row 列 PDF 1,2,6,3,4,6 = T-1 (复核成立), 其余一致 |
| :422 / :426 Ex8 CRF ×2 | p119 100 | 1 行 × 2 / 2 行 × 2 一致 |
- table_census.py (manifest = 本批 12 文件 × 复核页范围): before = after `OK 30 / UNPARSEABLE 11 / DIFF 1, cells 2390, diffs 3` (3 = T-1); 本页段 PDF_ONLY 0.

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | AG/assumptions.md:3-5 | ig34_p0092_a002/a003 | INSERTED | `## §6.1 Models for Interventions Domains` + 引言句 (以 "include:" 结尾, PDF 无域列表) | 92 |
| 2 | AG/assumptions.md:7-9 | ig34_p0092_a005/a006 | INSERTED | `## AG – Description/Overview` + 定义句 (gap D) | 92 |
| 3 | AG/assumptions.md:11-13 | ig34_p0092_a007/a009 | INSERTED | `## AG – Specification` + spec 首句 (gap S) | 92 |
| 4 | AG/assumptions.md:15 | ig34_p0094_a008 | INSERTED | `## AG – Assumptions` (gap A) | 94 |
| 5 | AG/spec.md:99/108/117/162/171 | pdf:p92-93 CT 列 | REPLACED | CT 空 → `*` ×5 | 92-93 |
| 6 | AG/spec.md:375 | ig34_p0094_a007 | INSERTED | 脚注 `> ¹In this column…` (最后变量块 `---` 后, Cross References 前; gap F) | 94 |
| 7 | AG/examples.md:40 | ig34_p0096_a017 | REPLACED | "See the SDTM-MD" → "See the SDTMIG-MD" (新增 atom, 全扫发现) | 96 |
| 8 | PR/assumptions.md:3-5 | ig34_p0125_a002/a003 | INSERTED | `## PR – Description/Overview` + 定义句 | 125 |
| 9 | PR/assumptions.md:7-9 | ig34_p0125_a004/a005 | INSERTED | `## PR – Specification` + spec 首句 | 125 |
| 10 | PR/assumptions.md:11 | ig34_p0127_a001 | INSERTED | `## PR – Assumptions` | 127 |
| 11 | PR/spec.md:99/108 | pdf:p125 CT 列 | REPLACED | CT 空 → `*` ×2 | 125 |
| 12 | PR/spec.md:411 | ig34_p0126_a025 | INSERTED | 脚注 | 126 |
| 13 | EX/assumptions.md:3-5 | ig34_p0103_a020/a021/a022 | INSERTED | `## §6.1.3 Exposure Domains` + 引言 2 句 (U3/O45) | 103 |
| 14 | EX/assumptions.md:7-9 | ig34_p0104_a002/a003/a004 | INSERTED | `## EX – Description/Overview` + 2 句 | 104 |
| 15 | EX/assumptions.md:11-13 | ig34_p0104_a005/a006 | INSERTED | `## EX – Specification` + spec 首句 | 104 |
| 16 | EX/assumptions.md:15 | ig34_p0105_a017 | INSERTED | `## EX – Assumptions` | 105 |
| 17a | EX/spec.md:90/99/108/225 | pdf:p104-105 CT 列 | REPLACED | CT 空 → `*` ×4 (EXTRT EXCAT EXSCAT EXADJ) | 104-105 |
| 17b | EX/spec.md:339 | ig34_p0105_a016 | INSERTED | 脚注 | 105 |
| 18 | EX/examples.md:69/73/77 | census_item :65 (Ex2 CRF) | REPLACED | `**Injection N**` → `Injection N` ×3 (PDF 非粗体; 本文件粗体在 Ex7 CRF 表示 PDF 勾选, 保留会误导) | 112 |
| 19 | EC/spec.md:90/108/117 | pdf:p107-108 CT 列 | REPLACED | CT 空 → `*` ×3 (ECTRT ECCAT ECSCAT) | 107-108 |
| 20 | EC/spec.md:411 | ig34_p0109_a010 | INSERTED | 脚注 (gap F) | 109 |
- 插入文字全部取自 layout 文本 / 渲染 (未用原子 verbatim); 引号/破折号照 PDF 字符 (p92/p104 撇号 pdftotext 为直引号 ', 照录; spec 首句 em dash —; 标题 en dash –).
- 新增 atom 清单 (R3, gaps/intros/footnote 之外): #7 (ig34_p0096_a017), #18 (格式).

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | AG/assumptions.md:3-5 | 新增 `## §6.1 …` 节 (H1 之后、Description 之前) | U3 intros (§6.1 首域 = AG); 先例 NV §6.3.7 / AE §6.2 |
| S-2 | EX/assumptions.md:3-5 | 新增 `## §6.1.3 Exposure Domains` 节 | U3/O45 (§6.1.3 首域 = EX) |
| S-3 | AG/PR/EX assumptions.md | 各新增 `## XX – Description/Overview`、`## XX – Specification`、`## XX – Assumptions` 3 个标题 | gaps D/S/A; DS/EC/CM 先例; 既有 H1 与列表未动 |
- 无整条 assumption 增删/挪位.

### 删除清单
| # | 原位置 (base) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | AG/examples.md:40 "SDTM-MD" | "SDTMIG-MD" | VALUE_DIFF 旧值替换 | — |
| D-2 | 14 处 spec CT 空值 | `*` | U2 | — |
| D-3 | EX/examples.md:69/73/77 粗体标记 `**` | 去掉 | 格式, PDF 非粗体 (#18) | — |
- 无内容删除 (授权第 3 条 "PDF 无此条" 整条删除: 0).

### D6 / KB_AUTHORED
- 无新增 D6. 既有: EX/examples.md:3 `> KB note (not in SDTMIG):` (B-EX 已标). 纯导航保留不标: EX/examples 表前短标签 `**CRF:**` (:169 :239 :335 :420)、`**Subject ABC123-0201**` (:337); EC/examples.md:3 交叉引用 (D2, B-EC); 4 域 spec.md `> Class|Structure` 行 + Cross References (U8).

### PDF_TYPO (EX 沿用 t2_B-EX 编号并续编; AG/PR 新开)
| T | 位置 | PDF | KB 处理 | 依据 |
|---|---|---|---|---|
| EX T-1..T-6 | 见 t2_B-EX.md | — | 沿用 | 本 attempt 复核: T-1 (p119 渲染 Row 1,2,6,3,4,6)、T-2 (p119:15 "--LNKID, .")、T-3 (p113:13 "ottles")、T-4 (p115:10 "protocol specified")、T-6 (p118:20 "mg/mL") 仍成立; T-5 (Ex6 EXENDTC 空, p117 渲染) 仍为 T4 用户裁定项 |
| EX T-7 | EX/assumptions.md:41 (item 5, p107) | 句尾多出 "…Define-XML document.Additional interventions qualifiers" (下一条标题文字被并入) | KB 保留 "…Define-XML document." 不改 | PDF 自身: 紧接下一行即 "6. Additional interventions qualifiers" 标题, 属重复排版错 |
| EX T-8 | EX/assumptions.md:47 (6d, p107) | "–PRESP" (en dash) | KB 保留 "--PRESP" | 同句 --OCCUR/--STAT/--REASND 均为双连字符; SDTMIG 变量前缀记法 "--" |
| PR T-1 | PR/assumptions.md:20 (1 段末, p127) | "collected.Measurements" (缺空格) | KB 保留 "collected. Measurements" | 句界缺空格, 印刷错 |

### 范围外 / out_of_scope 处理
- O45 (§6.1.3 父节引言): 已补 (#13) → 关闭.
- O15/O16 (spec 首句/脚注/Description): AG PR EX 全补; EC 脚注补 (Description/Spec 已由 B-EC 补) → 4 域关闭.
- 新范围外: 无 KB 错误. 原子台账问题 (T3 用): p125 原子 a011-a021 等编造 (PRGRID 等); p105_a016 漏上标; p112_a009 虚构表头; p116_a009 / p119_a007 / p120_a003 / p118_a013 抽取错.

### 需主控定
1. **§6 章标题 "6 Domain Models Based on the General Observation Classes" (p92 a001)**: 全 KB 无对应 (不在 intros). 该章标题下无正文 (紧接 §6.1). 建议: 与其他章级标题 (§7/§8 等) 一并定口径; 若要收, 放 AG/assumptions.md §6.1 之前作 `## §6 …` 单行标题. 本批未加.
2. **"6.1.3.3 Exposure/Exposure as Collected Examples" 标题 (p111 a001)**: EX/examples.md 无该标题, 仅 :3 KB note 提到 §6.1.3.3 (B-EX 按规则 6 未加). 建议: 在 `# EX — Examples` 后、KB note 前加 `## §6.1.3.3 Exposure/Exposure as Collected Examples` (仿 intro 标题写法) 而 `## Example N` 层级不变; 或维持现状视作 H1 等价. 本批未改.

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-INT_writer
python3 -I $S/spec_bbox.py AG 92,93,94 ; python3 -I $S/spec_bbox.py PR 125,126 ; python3 -I $S/spec_bbox.py EX 104,105 ; python3 -I $S/spec_bbox.py EC 107,108,109   # 剩余 DIFF 仅 CT C-code/DOMAIN (U5/U6) + EC ECENDTC 读序假阳
python3 -I $S/scan.py AG 92 97 ; python3 -I $S/scan.py PR 125 128 ; python3 -I $S/scan.py EX 103 120 ; python3 -I $S/scan.py EC 107 110
python3 -I $S/rscan.py EX 103 120 knowledge_base/domains/EX/assumptions.md knowledge_base/domains/EX/examples.md   # 余: T-3/T-4/T-6/T-2/T-8, KB note, 短标签
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 30 / UNPARSEABLE 11 / DIFF 1, diffs 3 (T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbbase/knowledge_base --out $S/fp_before.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl   # 逐原子比对: p92-p128 翻转 0 (全部翻转来自并行批 UR/EG/SS)
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat (限本批文件)
```
 knowledge_base/domains/AG/assumptions.md | 14 ++++++++++++++
 knowledge_base/domains/AG/examples.md    |  2 +-
 knowledge_base/domains/AG/spec.md        | 12 +++++++-----
 knowledge_base/domains/EC/spec.md        |  8 +++++---
 knowledge_base/domains/EX/assumptions.md | 14 ++++++++++++++
 knowledge_base/domains/EX/examples.md    |  6 +++---
 knowledge_base/domains/EX/spec.md        | 10 ++++++----
 knowledge_base/domains/PR/assumptions.md | 10 ++++++++++
 knowledge_base/domains/PR/spec.md        |  6 ++++--
 9 files changed, 64 insertions(+), 18 deletions(-)
```

### 更正 (同 attempt, 自查后; 以下取代上文逐页日志的计数列)
- 上文 "双向全扫 — 逐页日志" 的 原子/命中 计数为手填, 多页与脚本输出不符 (p92/p93/p96/p108/p111/p113/p114/p116/p118/p120). 下表由 `scan_after_<D>.txt` 各页 stat 行机械求和生成 (全原子, 未按节过滤; scan 输出已完整读取, 无截断); spec 页另给 spec_bbox 变量数. 未命中原子逐个归类.

| 页 | scan 域 | 原子 / 命中 (改后) | 未命中原子 → 归类 | spec_bbox 变量 | 叙述句 lscan (layout 文本, 不依赖原子) 句 / 命中 |
|---|---|---|---|---|---|
| 92 | AG | 24 / 20 | a001 §6 章标题 (需主控定 #1); a004 节号标题 (H1 等价); a010 spec 表头 (结构等价); a024 AGPRESP C-code (U5) | 14 | 16 / 8 (未命中 = 标题+正文拼段 2、spec 表片段 6) |
| 93 | AG | 22 / 14 | a001 a002 a008 a009 a010 a011 a016 a022 = C-code (U5) | 22 | 20 / 5 (全为 spec 表片段) |
| 94 | AG | 15 / 11 | a002 a003 a005 C-code; a007 脚注 (原子 "1In" 数字上标, KB `¹In` 已补) | 5 | 33 / 24 (spec 片段) |
| 95 | AG | 17 / 17 | — | — | 31 / 30 (`AG – Examples` 标题拼段) |
| 96 | AG | 20 / 20 | — | — | 17 / 16 (表片段) |
| 97 | AG | 15 / 15 | — | — | 4 / 1 (表片段 + "di.xpt" 拼段) |
| 103 | EX | 22 / 4 | a001-a019 = §6.1.2 CM 别节 | — | 15 / 3 (12 = CM 别节) |
| 104 | EX | 29 / 18 | a001 节号标题 (H1 等价); a007 表头; a017 a020 a022-a026 a028 a029 = C-code | 27 | 18 / 6 (标题拼段 1 + spec 片段 11) |
| 105 | EX | 20 / 9 | a001-a003 a005-a007 a010 a011 a013-a015 = C-code (ISO 8601 行除外均已核) | 10 | 20 / 12 (spec 片段) |
| 106 | EX | 16 / 16 | — | — | 31 / 31 |
| 107 | EX | 25 / 13 (EX 部分 7 / 5) | EX: a002 = T-7, a007 = T-8; 其余 a008-a025 = EC 节 (见 EC 行) | — | EX 部分未命中 = T-7/T-8 |
| 107 | EC | 25 / 16 | a001-a007 = EX 节; a008 节号标题; a014 表头; a025 ECMOOD C-code | 11 | 19 / 7 (EX 节 8 + spec 片段 4) |
| 108 | EC | 25 / 12 | a003 a004 a008-a010 a013 a015-a019 a021 a024 = C-code | 25 | 22 / 5 (spec 片段) |
| 109 | EC | 20 / 19 | a010 脚注 (原子写法) | 9 | 26 / 21 (spec 片段) |
| 110 | EC | 15 / 15 | — | — | 27 / 27 |
| 111 | EX | 27 / 26 | a001 §6.1.3.3 标题 (需主控定 #2) | — | 20 / 11 (标题拼段 + CRF/表片段) |
| 112 | EX | 33 / 32 | a009 原子虚构表头 | — | 9 / 8 (CRF 表拼段) |
| 113 | EX | 31 / 30 | a011 = T-3 | — | 7 / 4 (列表/表拼段) |
| 114 | EX | 26 / 26 | — | — | 13 / 13 |
| 115 | EX | 33 / 31 | a009 = T-4; a030 原子拼表头 | — | 12 / 9 (T-4 + 拼段) |
| 116 | EX | 31 / 22 | a009 表头抽取错; a017 a018 a020 a022-a025 a028 原子编造 (B-EX 已注) | — | 2 / 1 (CRF 标题拼段) |
| 117 | EX | 12 / 10 | a001 编造; a009 原子 "5.5 mL/mL" ≠ layout p117:40 "5.5 mg/mL" = KB:331 (原子抽取错, 非截断; 更正上文) | — | 8 / 6 (bullet 列表拼段, 逐项已在 KB) |
| 118 | EX | 32 / 30 | a013 "reason?" 抽取错 (渲染 "reason:"); a017 = T-6 | — | 25 / 14 (CRF/表片段 10 + T-6) |
| 119 | EX | 31 / 29 | a007 表头 "VSTRESC" 抽取错; a011 = T-2 | — | 13 / 10 (T-2 + CRF 拼段 2) |
| 120 | EX | 15 / 14 | a003 抽取错 (layout = KB "FIRST TO LAST DOSE INTERVAL") | — | 5 / 5 |
| 125 | PR | 28 / 15 | a001 节号标题; a006 表头; a011-a013 a016 a021 原子编造 (bbox/渲染 = KB); a019 a020 a024-a026 a028 C-code | 22 | 13 / 3 (spec 片段) |
| 126 | PR | 25 / 17 | a001 表头; a002-a005 a010 a021 a023 C-code | 23 | 24 / 9 (spec 片段) |
| 127 | PR | 24 / 24 | — | — | 28 / 26 (PR T-1 + `PR – Examples` 拼段) |
| 128 | PR | 31 / 31 | — | — | 8 / 7 (relrec 拼段) |
- p108 spec 变量数为 **25** (上文误写 31); EC 合计 11+25+9 = 45 ✓. EX 27+10 = 37 ✓, AG 14+22+5 = 41 ✓, PR 22+23 = 45 ✓.
- lscan.py (scratch, 新): layout 文本去表格行后按句切分查 KB, 用于 p116-p118 等原子不可信页的叙述 PDF→KB; 其未命中全部归入: 标题与正文/表拼段、spec 表片段、别节、已登记 T-n. 叙述句缺失 0.
- Ex2 CRF 去粗体 (#18) 依据补强: p112 200dpi 裁图 (`crf112-112.png`) "Injection 1/2/3" 为常规字重.
- p120 已渲染但未目视; 其表以 census OK + layout 文本为准 (上文 "census OK" 不含目视).
- 复跑: `python3 -I $S/lscan.py EX 103 120` (及 AG 92 97 / PR 125 128 / EC 107 110).

## attempt 1 delta (主控裁定, 2026-11-26)
- 依据: 主控裁定 (t2_dispatch_notes.md 末条). 需主控定 #1: §6 章标题无正文, **章标题不落地** (KB 不补). #2: 加 §6.1.3.3 标题. O20 页范围更正由主控改 json.

| # | kb_file:line | ref | action | before → after |
|---|---|---|---|---|
| 21 | EX/examples.md:3 | ig34_p0111_a001 | INSERTED | H1 后、KB note 前新增 `## §6.1.3.3 Exposure/Exposure as Collected Examples` (PDF 原标题; ## 与同文件 `## Example N` 同级; 既有标题/锚点未动) |

- EX/examples.md md5 `f208c590…` → `2fd243a8fdd4f9941e57ba1325e3508a` (461→463 行); 本文件 :3 之后所有上文行号 +2.
- 入链: `grep -rn "EX/examples.md#" knowledge_base docs web/src` 0 处 → 无锚点受影响. check_links: live docs 42.
