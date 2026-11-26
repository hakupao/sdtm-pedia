# T2S S-HOST writer checkpoint (扫描批: TI 宿主 §7.3/§7.4/§7.5 引言核 + NV narrow §6.3.6 MO 框)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `8426871`; 本批 2 文件改前对 HEAD 干净 (`git status --short knowledge_base/domains/{TI,NV}` 空). 工作区其余改动 (FA/SR/TA/TD/TM/TR) 属并行批, 未触碰.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-HOST_writer/` (scan.py 双向句级扫描; 渲染 p285/p407/p415/p425/p426 110dpi)
- md5: NV/assumptions `21f2e97e` → `85a25375` (48 → 58 行, 10+/0-); TI/assumptions `cf4905bc` (= B-TI attempt 2 终版, **未改**).

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| TI (宿主核) | §7.3 引言 | 407-407 | **p407 中部** (标题 a010 起, 至 `7.3.1 Trial Visits (TV)` 前) | p407 上部为 §7.2 TA Ex special.xpt + 注释段 (别节); 下部 §7.3.1 TV 起 |
| TI | §7.4 引言 | 415 | **p415 末** (a025 标题 – a029) | p415 上部 §7.3.3 TM (别节); p416 首行 `7.4.1` |
| TI | §7.5 | 425-427 | **p425 下部 (a026) – p426 末** | p425 上部为 §7.4.2 TS NullFlavor 表/层级说明 (别节); **p427 首行即 `8 Representing Relationships and Data`** → p427 无 §7.5 内容, json 止页多 1 页 |
| NV (narrow) | §6.3.6 | 285 | **p285 上部** (a001-a005, 红框) | 框下 `6.3.7 Morphology/Physiology Domains` 起别节 (NV 已承载) |

### 双向全扫 — 逐页日志
方法: PDF→KB = `work/pdf_atoms.jsonl` 该节原子 (含 NOTE/LIST_ITEM) 归一 (空白/弯引号) 后在宿主文件查; 另 scan.py 以 layout 文本句级切分双向扫 (TI 全文件 vs p415-417+p425-426; KB→PDF 无出处 0). 渲染图核版面/框边界.

| 页 | 节 | PDF→KB: 原子 / 命中 / 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 285 | §6.3.6 MO 框 (narrow) | 5 / 0→5 / 5→5 (a001 标题, a002 框标题, a003-a005 三段) | NV/asm:3-13 新增, 与 PDF 框文字归一后全等 (脚本 `pb==ks` True) | — | §6.3.7/§6.3.7.1 (a006-a017) 属 NV 既有, 未动 |
| 407 | §7.3 引言 (宿主核) | 5 / 5 (a011 → TI:5 与 TV:5 共享句; a012-a015 仅 TV:7-11) | TI 无 §7.3 专属内容 | — | **覆盖矩阵 TI 归属为假阳**: a011 "This section contains the Trial Design (TD) datasets that describe:" 与 §7.4 引言 (p415 a026) 同句; §7.3 引言正身在 TV/assumptions.md:3-11 (O47 结论成立). TI 不改 |
| 415 | §7.4 引言 | 5 / 4 / 0 | TI/asm:3-10, 无出处 0 | — | 未命中 a025 = 节标题, KB `## §7.4 … (TI, TS) — Introduction` (PDF "(TI and TS)", O48 已登记, 规则 6 不改) |
| 425 | §7.5 引言 + step 1-3 前半 | 7 / 7 / 0 | TI/asm:38-44, 无出处 0 | — | 引言已于 B-TI a2 合 1 段 |
| 426 | §7.5 step 3 后半 – 12 | 9 / 9 / 0 | TI/asm:44-53, 无出处 0 | — | step 6 “split”/“lump” 直引号 = 排版字符, 归 S-TYPO 不计 |

- TI/assumptions.md 其余段 (:12-36, §7.4.1 p416-417) 属 B-TI 终版; 本批反向扫描一并覆盖, KB→PDF 无出处 0, 未改.
- 章标题不落地: 无 (本批节均有正文).

### 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | NV/assumptions.md:3 | pdf:p285:ig34_p0285_a001 | INSERTED | 新增 `## §6.3.6 Morphology (MO)` (U3/O31, §6.3.7 标题前) | 285 |
| 2 | NV/assumptions.md:5 | pdf:p285:ig34_p0285_a002 | INSERTED | 框标题 `**Domain Decommissioning Update**` (粗体, 不新建锚点) | 285 |
| 3 | NV/assumptions.md:7 | pdf:p285:ig34_p0285_a003 | INSERTED | "The MO domain has been decommissioned as of SDTMIG v3.4." | 285 |
| 4 | NV/assumptions.md:9 | pdf:p285:ig34_p0285_a004 | INSERTED | 段 1 "When the Morphology domain was introduced in SDTMIG v3.2, …" 逐字 (5 句) | 285 |
| 5 | NV/assumptions.md:11 | pdf:p285:ig34_p0285_a005 | INSERTED | 段 2 "For data prepared using a version of the SDTMIG …" 逐字 (2 句) | 285 |
| 6 | TI/assumptions.md | pdf:p407:ig34_p0407_a011 | VERIFIED | §7.3 归属假阳, 不改 | 407 |
| 7 | TI/assumptions.md:3-10, 38-53 | pdf:p415/p425/p426 | VERIFIED | §7.4 引言 + §7.5 复扫 0 缺 | 415-426 |

- 结构改动清单: 无 (narrow 插入一节, 无列表整条增删/挪位).
- 删除清单: 无.
- D6 标注清单: 无 (TI/NV 本批范围内无 KB 自写解释).
- PDF_TYPO: 无新增; B-TI T-1 (p417 "a trial that with") 在 TI/examples.md, 非本批文件, 沿用不动.

### 范围外发现
- F-1: `chapters/ch10_appendices.md:216-224` 也承载 MO 退役框文字, 且 :222 写 "deprecate MO in SDTMIG v3.4", p285 为 "deprecate MO in a future version of the SDTMIG". 若 ch10 该段是从 §6.3.6 搬运 → 与 PDF 矛盾; 若是 PDF §10 自身内容需对其原页. 归 S-CH 批 (json notes 已指明), 本批未碰.
- F-2: O48 (TI §7.4 标题 "(TI, TS)" vs PDF "(TI and TS)") 仍在, 规则 6 不改.

### 需主控定
- 无 (F-1 交 S-CH).

### 验证
- `python3 -I <scratch>/scan.py knowledge_base/domains/TI/assumptions.md 415,416,417,425,426` → KB→PDF kbonly 0; PDF→KB 未命中全部为节外 (TM / TI spec 表 / TS / NullFlavor) 或标题粘连.
- p285 框: 归一后 PDF 框文字 == KB 新节文字 (True).
- `git diff --stat -- knowledge_base/domains/NV knowledge_base/domains/TI` → NV/assumptions.md | 10 ++++++++++ (1 file, 10+); TI 无改动.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42
