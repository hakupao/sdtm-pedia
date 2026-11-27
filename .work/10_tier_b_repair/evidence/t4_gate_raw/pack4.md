<!-- 原样誊录: feature-dev:code-reviewer (opus) 对 `work/t4/gate_pack_4.md` 的回复, 2026-11-27. 主控未改动内容 (仅把绝对路径缩成仓库相对路径). -->

# T4.1 总闸独立审：gate_pack_4（样本 64-84，共 21 条）

全部 21 条终态都成立，HOLDS 21 / NOT_HOLD 0 / UNVERIFIABLE 0。只有 #84 是按定义解释判的，KB 标题比 PDF 多了一个 `(TE)`，下面单独说明。

审查方式：样本包只当线索，KB 现文我用 Grep / Read 在 live 文件里重新定位过。PDF 侧每条都用 Grep 查过 `pdf_pages/` 文本层。表格、字形和笔误类加看了渲染页：p152、p224、p240、p257、p258、p267、p373、p378。p79 和 p371 没看渲染页，#73、#71 只以文本层为据。3 条长行（CP:245、FA asm:37、ch08:187）读了整行，与 PDF 对应段落逐字比过。全程只读，没有改任何文件。

## 1. 判定表

路径说明：`pdf_pages/` 指 `.work/10_tier_b_repair/work/pdf_pages/`，KB 路径相对 `knowledge_base/`，typo 登记文件为 `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl`。

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF 文件:行 / 渲染页; KB 文件:行) | NOT_HOLD / UNVERIFIABLE 原因 |
|---|---|---|---|---|---|---|
| 64 | ig34_p0148_a001 | CONTROL | EXACT | HOLDS | ig34_p0148.txt:1-2；domains/BE/examples.md:145 逐字一致 | - |
| 65 | ig34_p0152_a0003 | CONTROL | EXACT | HOLDS | ig34_p0152.txt:5 + 渲染页 p152：表头 "Event" 横跨两列，Yes/No 列没有独立列名；domains/CE/examples.md:41 `\| Event \| \| Date Started \| Date Ended \| Severity \|` 是合并格的合理表达 | - |
| 66 | ig34_p0217_a014 | CONTROL | EQUIVALENT | HOLDS | ig34_p0217.txt:43-46；domains/CP/examples.md:245 读整行，逐字一致（实际可以算 EXACT） | - |
| 67 | ig34_p0235_a012 | CONTROL | EQUIVALENT | HOLDS | ig34_p0235.txt:18；domains/IS/examples.md:79，只多了粗体标签 | - |
| 68 | ig34_p0240_a003 | CONTROL | EQUIVALENT | HOLDS | ig34_p0240.txt:3-4 + 渲染页 p240；domains/IS/examples.md:213 逐字一致 | - |
| 69 | ig34_p0257_a011 | CONTROL | EQUIVALENT | HOLDS | ig34_p0257.txt:18-19 + 渲染页 p257 Row 4：MSCONC/MSCONCU、MSORRESU、MSSTRESN/U 为空，MSORRES/MSSTRESC=RESISTANT；domains/MS/examples.md:26 与表头 :21 列位全对 | - |
| 70 | ig34_p0267_a011 | CONTROL | EXACT | HOLDS | ig34_p0267.txt:17-18 + 渲染页 p267 Row 5：MIORRES/MIORRESU/MISTRESU 为空，MISTRESC/MISTRESN=110，DRVFL=Y；domains/MI/examples.md:56 一致 | - |
| 71 | ig34_p0371_a010 | CONTROL | EQUIVALENT | HOLDS | ig34_p0371.txt:11（只看了文本层，没看渲染页）；domains/FA/examples.md:142，○ 字形与值一致 | - |
| 72 | ig34_p0431_a027 | CONTROL | EXACT | HOLDS | ig34_p0431.txt:41-49；chapters/ch08_relationships.md:187 读整行，整段逐字一致 | - |
| 73 | ig34_p0079_a009 | SUPP_ATOM_ERR | ATOM_ERR | HOLDS | ig34_p0079.txt:21-22 文本层是 `--DTC`，原子是 `– DTC`，原子确实抄错；domains/SE/assumptions.md:17 写 `--DTC`，与 PDF 一致（没看渲染页） | - |
| 74 | ig34_p0240_a011 | SUPP_ATOM_ERR | ATOM_ERR | HOLDS | 渲染页 p240 Row 4：ISTSTDTL 空、ISTSTOPO=QUANTIFY、ISORRES=1:170、ISORRESU 空、ISSTRESC=170、ISSTRESN=170、titer。原子在 AUTOANTIGENS 后多一个空格，又少一个 170，列错位；domains/IS/examples.md:225 对照表头 :220 列位全对 | - |
| 75 | ig34_p0258_a021 | SUPP_ATOM_ERR | ATOM_ERR | HOLDS | 渲染页 p258 Row 3：VISIT="VISIT 1"（折行）。原子写 "VISIT"，抄错；domains/MB/examples.md:78 写 "VISIT 1"，其余格一致 | - |
| 76 | ig34_p0373_a021 | SUPP_ATOM_ERR | ATOM_ERR | HOLDS | ig34_p0373.txt:27 + 渲染页 p373：表头末列是 FAEVLINT。原子写 FAEVINTX，抄错；domains/FA/examples.md:239 写 FAEVLINT，一致 | - |
| 77 | ig34_p0085_a019 | SUPP_PDF_TYPO | PDF_TYPO | HOLDS | ig34_p0085.txt:28 确为 "hyypoglycemic"；登记 B-SM T-3 处理方式 = KB 写正确值；domains/SM/examples.md:22 写 "hypoglycemic"，与登记一致 | - |
| 78 | ig34_p0215_a018 | SUPP_PDF_TYPO | PDF_TYPO | HOLDS | ig34_p0215.txt:42 写 "CPCSMRKR"，全部 pdf_pages 里只出现这一次，其余 40 处都是 CPCSMRKS；登记 B-CP T-2 = KB 写正确值；domains/CP/examples.md:202 写 CPCSMRKS，一致 | - |
| 79 | ig34_p0224_a010 | SUPP_PDF_TYPO | PDF_TYPO | HOLDS | ig34_p0224.txt:18 + 渲染页 p224 确为 "--ORNRLO, ORNRHI,--STNRLO"；登记 B-GF T-6 = KB 写正确值；domains/GF/assumptions.md:39 写 "--ORNRLO, --ORNRHI, --STNRLO"，一致 | - |
| 80 | ig34_p0378_a017 | SUPP_PDF_TYPO | PDF_TYPO | HOLDS | ig34_p0378.txt:32 + 渲染页 p378 Row 7 确为 "0.15 BAU mL"，同表 r5/6/8 都是 BAU/mL；登记 id 实为 `B-SR T-1 (examples)`（样本包写的是 "B-SR T-1"），处理方式 = KB 写正确值；domains/SR/examples.md:22 写 "0.15 BAU/mL"，一致 | - |
| 81 | ig34_p0094_a008 | SUPP_EXACT | EXACT | HOLDS | ig34_p0094.txt:30 "AG – Assumptions"；domains/AG/assumptions.md:15 "## AG – Assumptions"，en dash 一致 | - |
| 82 | ig34_p0350_a008 | SUPP_EXACT | EXACT | HOLDS | ig34_p0350.txt:10；domains/TR/assumptions.md:10，位于该文件 "## TR – Description/Overview" 节下（:3），位置正确 | - |
| 83 | ig34_p0362_a009 | SUPP_EXACT | EXACT | HOLDS | ig34_p0362.txt:36-46；domains/FA/assumptions.md:37 读整行，与 PDF 整段逐字比对无差异 | - |
| 84 | sv20_p0051_a016 | SUPP_EXACT | EXACT | HOLDS（定义解释判定） | PDF 标题在 sv20_p0051.txt:25 "5.1.1.1 Trial Elements"；样本包自动定位到的 :12 是正文列表项，定位错了。KB model/05_study_level_data.md:29 是 `### 5.1.1.1 Trial Elements (TE)`，PDF 字串完整、连续地出现在 KB 里，但 KB 多了后缀 "(TE)"。brief 的 EXACT 容差没有列"追加后缀"，禁止项（换词、漏词、改值）也没有列，所以按"逐字承载"判成立，差异记在这里 | - |

## 2. 计数
- HOLDS：21
- NOT_HOLD：0
- UNVERIFIABLE：0

## 3. 样本外发现

**A. 新发现（不修，只记录）**
1. **sv20 Model 标题系统性地加了域代码后缀。** `knowledge_base/model/05_study_level_data.md:29` 是 `5.1.1.1 Trial Elements (TE)`，:45 是 `5.1.1.2 Trial Arms (TA)`。PDF `sv20_p0051.txt:25` 和 `sv20_p0052.txt:20` 都没有括号代码，KB 也没有加 "KB note" 标记。同文件其他 5.1.x 标题（例如 Trial Repro Stages、Trial Visits）很可能也是这样。这一条会影响 #84 这类 EXACT 标题原子该怎么判，请主控定一个口径：追加后缀算 EXACT 还是 EQUIVALENT。
2. **CE CRF 的勾选符字形与 PDF 不一致。** `knowledge_base/domains/CE/examples.md:43-46` 用 `( ) Yes  ( ) No` 和 `( ) Mild ...`，渲染页 p152 是 `○`。FA 的 CRF（`domains/FA/examples.md:140-144`）用的是 `○`，两处不统一。这属于已移交 T4 的 CRF ○□ 遗留问题，在这里作为具体实例报告。
3. **CE CRF 标题是 KB 自拟的。** `knowledge_base/domains/CE/examples.md:39` 写 "**CRF: CE Example 2 — Clinical Events with Severity**"，渲染页 p152 只有 "CRF"，KB 没有加 KB note 标记。
4. **样本包自动定位有误。** #84 的 PDF 行指针给的是 :12，实际标题在 :25。判定已经用正确行，只说明脚本定位有偏差。

**B. 顺带核过、已登记的 PDF 笔误（不是新发现，不用重提）**
- MS Ex1 r9 MSSTRESC：PDF 为空（渲染页 p257），KB 填 25，已登记为 B-MS T-1。
- MI Ex3 表头：PDF 写 `MIDRVL`（渲染页 p267），KB 写 MIDRVFL，已登记为 B-MI T-1。
- FA Ex5 叙述：PDF 写 "FAEVINTX indicates"（p373），KB :228 写 FAEVLINT，已登记为 B-FA T-9。

**C. 顺带看到、我没有查登记表的 PDF 拼写**
- p224 GF Example 1 叙述里有 "inheritabilty"（PDF 原文拼写，见渲染页 p224）。我没有核对它有没有登记、KB 现在怎么写，请主控按 B-GF 登记表自己确认。
