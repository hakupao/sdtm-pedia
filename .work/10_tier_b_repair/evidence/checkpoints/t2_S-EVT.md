# T2S S-EVT writer checkpoint (扫描批试点)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `cd83814`; 本批 6 文件改前工作区干净. scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-EVT_writer/`
  (base/ = `git show HEAD:` 副本; apply.py 精确替换 + 命中次数断言; spec_cmp.py 变量逐字段对 PDF; scan.py PDF→KB; rscan.py KB→PDF; census_before/after.json; fp_before/after.jsonl; 渲染 p133/137/139/141/142/155/156/165/166 + p142 Ex5 220dpi 局部)
- md5 before → after: AE/assumptions `71ce6c47…` → `fdb6728d7aaf700c59572e1115fe4f43` (70→82 行); AE/spec `c73c9879…` → `f777e905c03f49bed9ef21b413239aa5` (570→572);
  DS/assumptions `e0bb1a9c…` → `11962e83fefa40a9a890a7a67bc04120` (43→51); DS/spec `b32ca196…` → `ff13c98318b63958876648290453ed15` (170→172); AE/examples `f8dd2e92…`、DS/examples `ff464526…` 未动.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| domains/AE | §6.2.1 | 133-143 | **133-142** | p133: 上部 §6.1.6 SU 例表 (a001-a009) 不归本节; §6.2 章引言 a010-a018 (U3, 本批 intro); §6.2.1 标题 a019 起. p143 首行即 `6.2.2 Biospecimen Events (BE)` 标题 → p143 无 AE 内容, json note "p143 下部 BE 起" 不准 |
| domains/DS | §6.2.4 | 155-167 | **155-167** | p155: 上部 §6.2.3 CE 尾 (pr.xpt r3 / RELREC 叙述 / relrec.xpt, a0001-a0012) 不归本节, 标题 a0013 起; p167: §6.2.5 HO 标题 a0018 起不归本节 |

### 双向全扫 — 逐页日志
方法: PDF→KB = `work/pdf_atoms.jsonl` 该页全部原子 (含 TABLE_ROW/TABLE_HEADER/CODE_LITERAL) 归一后在本域三文件中查 (表行: 整行或逐格); 原子抽取错的表行改用渲染图逐格. KB→PDF = 三文件逐句 (rscan.py; spec.md 用 spec_cmp.py 逐变量逐字段) 在 PDF 页文本+原子中查. 计数为改后.

| 页 | 节 | PDF→KB: 原子数 / 命中 / 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 133 | §6.1.6 尾 / §6.2 / §6.2.1 | 本批 12 (a010-a021) / 11 / 9→9 (§6.2 标题+句+7 项, 改前全缺) | AE/assumptions 1-17 全有出处 | — | a019 `6.2.1 Adverse Events (AE)` = H1 结构等价; SU a001-a009 别节 |
| 134 | §6.2.1 spec | 25 / 23 / 0 | spec.md STUDYID..AEBODSYS 逐字段一致 (CT 除外, 见下) | spec 22 变量逐字段 | a003 表头 = spec.md 字段结构等价; a024 AEPRESP CT `(NY)` vs KB `C66742` (需主控定 #2); CT `*` 3 处已补 |
| 135 | spec | 19 / 7 / 0 | 一致 | 18 变量 | 12 未命中 = CT C-code 记法 11 + AERLDEV 注释项目符号 (• vs `*` 列表, 仅格式); CT `*` 3 处已补 |
| 136 | spec | 13 / 2 / 0 | 一致 | 12 变量 | 未命中 = C-code 记法 9 + AERLPRT/AERLPRC 项目符号格式; CT `*` 3 处已补 |
| 137 | spec 尾 / assumptions 1-2c | 16 / 13 / 1→1 (脚注 a010) | assumptions 1-2c 一致 | 8 变量 | 未命中 = 表头 a001 + AEENRF/AEENRTPT C-code; 脚注已补到 spec.md 末尾 |
| 138 | assumptions 2d-6a | 13 / 13 / 0 | 一致 | — | |
| 139 | assumptions 6a-7e | 15 / 15 / 0 | 一致; `**CRF: AE Seriousness Classification**` 为表前短标签 (纯导航) | CRF 表 (census UNPARSEABLE) 渲染逐格一致 | |
| 140 | 7e-12 / Examples / Ex1 | 15 / 15 / 0 | 一致 | — | `AE – Examples` = KB H1 `# AE — Examples` 等价 |
| 141 | Ex1-Ex4 | 26 / 22 / 0 | 一致 | Ex1-Ex3 census OK; 渲染核 | 4 未命中 a003/a004/a005/a013 = 原子抽取错 (渲染: r1 AEDECOD Headache / AEENDY -1; r2 AEENDTC 2005-10-13T19:00; r3 AESHOSP/AESLIFE Y; Ex2 r2 AEDECOD Vomiting), KB = 渲染 |
| 142 | Ex4-Ex6 | 24 / 19 / 0 | examples.md:75 "related to the device" = T-3 (登记沿用) | Ex4 OK; Ex5 渲染 220dpi 逐格 (见下); Ex6 渲染逐格一致 | 未命中: a012 (T-3), a015/a016 (T-1/T-2 + "RECOVERED/ RESOLVED" 原子空格), a022 表头原子漏 AESPID, a023/a024 仅原子空格 |
| 143 | §6.2.2 BE | AE 内容 0 | — | — | 全页属 BE (别节) |
| 155 | §6.2.3 尾 / §6.2.4 | 本批 16 (a0013-a0028) / 10 / 4→4 (a0014-a0017 Description/Spec) | DS/spec STUDYID..DSCAT 一致 | spec 10 变量逐字段 | a0013 节号标题 = H1 等价; a0018 表头结构等价; DOMAIN CT `DS` 空 (需主控定 #1); DSDECOD/DSCAT C-code (#2); CE 尾 12 原子别节 |
| 156 | spec 尾 / assumptions 1-2e | 28 / 25 / 3→3 (脚注 a0007 / 标题 a0008 / 2b a0018) | 一致 | 6 变量 | DSSCAT/EPOCH C-code (#2); 脚注原子 "1In this" 数字上标 → 已按 ¹ 补, 子串检查因原子写法未命中 |
| 157 | 2f-5 | 29 / 29 / 3→3 (3b-ii a0007, 3d a0010, 5 a0026) | 3d 原 "DSTERM and" 无出处 → 已删 (词级) | — | |
| 158 | 5 续-6 / Examples / Ex1 叙述 | 26 / 25 / 0 | 原 assumption 7 无出处 → 整条删 (结构改动 S-1) | — | a0004 未命中 = 原子 "SLÍFE" 抽取错, KB 与原子去该字符后全等 |
| 159 | Ex1 表 | 29 / 29 / 0 | 一致 | census OK | |
| 160 | Ex2-Ex4 | 33 / 32 / 0 | 一致 | census OK | a0028 = T-3 (DSSTDTC, 沿用) |
| 161 | Ex4-Ex5 | 25 / 24 / 0 | 一致 | census OK | a0012 = T-4 (epocch, 沿用) |
| 162 | Ex6-Ex8 | 28 / 28 / 0 | 一致 | census OK | |
| 163 | Ex9-Ex10 | 27 / 27 / 0 | 一致 | census OK | |
| 164 | Ex10 | 34 / 33 / 0 | 一致 | census OK | a0004 = T-6 (" DG2INDG", 沿用) |
| 165 | Ex10 SE/DS / Ex11 | 35 / 33 / 0 | 一致 | se.xpt 渲染逐格 (见下); ds.xpt census OK | a0002 = T-1 (SDSEQ); a0009 原子 "TREAT 2" 抽取错, 渲染 TREATMENT 2 = KB |
| 166 | Ex11 | 42 / 40 / 0 | 一致 | te.xpt 渲染逐格 (见下); ta/se census OK | a0005 = T-2; a0035 = T-5 (recieved) |
| 167 | Ex11 尾 / §6.2.5 | 本批 19 / 18 / 0 | 一致 | ds.xpt census OK | a0010 表头原子 "DSEQ" 抽取错 (渲染 DSSEQ); a0018 起 HO 别节 |

- spec.md 非变量行 (KB→PDF): H1 `# AE — Adverse Events` / `# DS — Disposition`、第 3 行 `> Class: Events | Structure: …` (由 spec 首句派生的元数据行)、`---` 分隔、`## Cross References` 块 (AE 546-570 / DS 150-170 行, 链接 + 短说明) — 均按纯导航处理, 未加 D6 标注 (见需主控定 #4).
- 汇总 PDF→KB 已补: AE 10 (intro 9 + 脚注 1), DS 10 (Description/Spec 4 原子 + 标题 + 脚注 + 3 处词级 + 引号). 余下未命中全部为: 别节 / 结构等价 / 原子抽取错 / 登记 T-n / CT 记法 (#1 #2) / 项目符号格式.

### spec.md Controlled Terms 逐变量 (PDF CT 列 vs KB; 依 layout 文本 + 原子 + p134-137/155-156 渲染)
- AE 60 变量: Label/Type/Role/Core/CDISC Notes 全部一致 (Notes 中 AERLDEV/AERLPRT/AERLPRC 的 "•" 列表 KB 为 `*` 列表, 仅格式). CT 列:
  - PDF `*` 9 个 → 已补 `*`: AECAT AESCAT AEBODSYS AEREL AERLDEV AEPATT AERLPRT AERLPRC AETOXGR.
  - PDF 空 = KB 空: STUDYID USUBJID SPDEVID AESEQ AEGRPID AEREFID AESPID AETERM AEMODIFY AEACNOTH AERELNST TAETORD AESTDY AEENDY AEENTPT.
  - PDF 字面值 = KB: MedDRA ×11 (AELLT…AESOCCD), ISO 8601 datetime or interval ×2, ISO 8601 duration ×1.
  - PDF `AE` / KB 空: DOMAIN (#1).
  - PDF codelist 短名 / KB C-code (#2), 22 个: AEPRESP AESER AESCAN AESCONG AESDISAB AESDTH AESHOSP AESLIFE AESOD AESMIE AESINTV AEUNANT AECONTRT (NY→C66742), AELOC (LOC→C74456), AESEV (AESEV→C66769), AEACN (ACN→C66767), AEACNDEV (DEACNDEV→C111110), AEOUT (OUT→C66768), EPOCH (EPOCH→C99079), AEENRF/AEENRTPT (STENRF→C66728).
- DS 16 变量: 其余字段全部一致. CT: PDF 无 `*` 行 (无需补); PDF 空 = KB 空 9 个; ISO 8601 ×2 一致; DOMAIN `DS`/空 (#1); C-code (#2) 4 个: DSDECOD (NCOMPLT)(PROTMLST)(OTHEVENT)→C66727; C114118; C150811, DSCAT→C74558, DSSCAT→C170443, EPOCH→C99079.

### census_items 逐格
| 表 | 渲染 | 结果 |
|---|---|---|
| AE/assumptions.md:61-63 CRF (UNPARSEABLE) p139 | 100dpi | 2 行 × 2 格: "Serious?" / "[ ] Yes [ ] No"; "If yes, check all that apply" / "[ ] Fatal [ ] Life-threatening [ ] Inpatient hospitalization… [ ] etc." — 一致 (PDF 无表头行, KB 首行作 Markdown 表头, 结构必需) |
| AE/examples.md:79-82 Ex5 p142 | 220dpi 左右两半 | 2 行 × 30 列逐格: r1 除 AEENDTC (T-1) 外全一致; r2 除 AEOUT (T-2) 外全一致; 表头首格 PDF 空白 = T-4. T-1/T-2/T-4 复核仍成立, 沿用 |
| DS/examples.md:292-301 se.xpt p165 | 100dpi | 8 行 × 11 列逐格一致; 表头 PDF `SDSEQ` / KB `SESEQ` = T-1 (复核成立) |
| DS/examples.md:342-348 te.xpt p166 | 100dpi | 4 行 × 8 列一致; r3 TESTRL PDF "where treatment AB +C" / KB "…is AB +C" = T-2 (复核成立) |
- table_census.py (pdf_ranges): before = after `UNPARSEABLE 1 / OK 24 / DIFF 3, cells 1805, diffs 4` (4 = AE T-1/T-2, DS T-1/T-2).

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | AE/assumptions.md:3-13 | ig34_p0133_a010..a018 | INSERTED | H1 后新增 `## §6.2 Models for Events Domains` + 引言句 + 7 项域列表 (逐字) | 133 |
| 2-10 | AE/spec.md:171/180/198/288/297/315/423/432/450 | pdf:p134-136 CT 列 | REPLACED | Controlled Terms 空 → `*` (AECAT AESCAT AEBODSYS AEREL AERLDEV AEPATT AERLPRT AERLPRC AETOXGR) | 134-136 |
| 11 | AE/spec.md:572 | ig34_p0137_a010 | INSERTED | 文件末尾 `> ¹In this column, an asterisk (*) …` | 137 |
| 12 | DS/spec.md:172 | ig34_p0156_a0007 | INSERTED | 同上 | 156 |
| 13 | DS/assumptions.md:3-5 | ig34_p0155_a0014/a0015 | INSERTED | `## DS – Description/Overview` + 定义句 (gap D, O49) | 155 |
| 14 | DS/assumptions.md:7-9 | ig34_p0155_a0016/a0017 | INSERTED | `## DS – Specification` + spec 首句 (gap S; CM 先例) | 155 |
| 15 | DS/assumptions.md:11 | ig34_p0156_a0008 | INSERTED | `## DS – Assumptions` (gap A) | 156 |
| 16 | DS/assumptions.md:17 | ig34_p0156_a0018 | REPLACED | 2b "then DSCAT provides" → "DSSCAT" | 156 |
| 17 | DS/assumptions.md:30 | ig34_p0157_a0007 | REPLACED | 3b-ii "Terminology Codelist" → "codelist" | 157 |
| 18 | DS/assumptions.md:32 | ig34_p0157_a0010 | REPLACED | 3d "DSTERM and DSDECOD uses" → "DSDECOD uses" | 157 |
| 19 | DS/assumptions.md:43 | ig34_p0157_a0026 | INSERTED | 5 补漏掉的开引号 “ (PDF 原字符) 于 "grouped" 前 | 157 |
| 20 | DS/assumptions.md (旧 :42-43) | 结构 S-1 | DELETED | 整条 assumption 7 删除 (见结构改动 / 删除清单) | 155-158 (无); 166 |
- 新增 atom 清单 (R3, 全扫发现, gaps 之外): #16 #17 #18 #19 (DS assumptions 词级); 其余均在 gaps/intros/footnote 内.

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | DS/assumptions.md 旧 :43 (`7. For the ABC arm, if drug C is dropped, … or follow some other defined protocol.`) | 整条删除 (连同前空行) | PDF §6.2.4 assumptions 列表 p156-158 止于 6 (p158 a0004 后即 `DS – Examples`); "defined protocol" 在 p155-167 layout 文本 0 处、pdf_atoms 0 处 (`grep -Hn "defined protocol\|transition to an AB" ig34_p0155..0167.txt` 仅命中 p166:9). 该句是 p166 Ex11 TA 叙述的改写副本且尾部 "follow some other defined protocol" 与 PDF "or follow-up" 不符; PDF 原句已逐字在 DS/examples.md:349 → 授权第 1/3 条 "PDF 无此条" 删除, 非 D6 |
| S-2 | AE/assumptions.md:3-13 | 新增 `## §6.2 …` 节 | U3 (intros) |
| S-3 | DS/assumptions.md:3-11 | 新增 3 个 `## DS – …` 标题 | gaps D/S/A; CM/AE 先例 |

### 删除清单
| # | 原位置 (base) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | DS/assumptions.md:42-43 assumption 7 | 无 | S-1, PDF 无此条 | PDF 原句在 DS/examples.md:349 |
| D-2 | DS/assumptions.md:22 "DSTERM and " | :32 | 词级多词, PDF 无 (授权第 1 条) | — |
| D-3 | DS/assumptions.md:7 "DSCAT" (2b) / :20 "Codelist" | DSSCAT / codelist | VALUE_DIFF 旧值替换 | — |
| D-4 | AE/spec.md 9 处 CT 空值 | `*` | U2 | — |

### D6 / KB_AUTHORED
- 无新增 D6 标注. 纯导航保留不标: AE/assumptions `**CRF: AE Seriousness Classification**`; 两域 spec.md `> Class: … | Structure: …` 行与 `## Cross References` 块 (见需主控定 #4).

### PDF_TYPO (复核沿用 t2_B-AE / t2_B-DS 编号, 本 attempt 无新增)
- AE: T-1 Ex5 r1 AEENDTC 2014→2018 (KB 正确值); T-2 SEQUELLAE→SEQUELAE; T-3 Row 2 叙述 "event"→"device"; T-4 Ex5 表头首格 `Row`. U-1..U-5 照录项未变.
- DS: T-1 SDSEQ→SESEQ; T-2 TESTRL 补 "is"; T-3 DSDTDTC→DSSTDTC; T-4 epocch; T-5 recieved; T-6 " DG2INDG". U-1..U-6 未变.
- 依据见原 checkpoint; 本 attempt 渲染复核 T-1/T-2 (AE、DS) 四项仍成立.

### 范围外 / out_of_scope 处理
- O8: AE 7c AESOSP (assumptions.md:67) 与 Ex5 STUDYID T002 复核已修, 关闭.
- O15: AE spec 首句 (B-AE 已补 assumptions.md:19-21) + 脚注 (本批 #11) → AE 关闭; DS 同 (#12/#14).
- O18 / O50: §6.2 章引言已补 (#1) → 关闭 (§6.1/6.3/6.4 引言不属本批).
- O49: DS Description 已补 (#13) → 关闭.
- 新范围外: 无. (原子抽取错 for T3 台账: ig34_p0141_a003/a004/a005/a013, p0142_a015/a022, p0158_a0004 "SLÍFE", p0165_a0009 "TREAT 2", p0167_a0010 "DSEQ".)

### 需主控定 (U2 未覆盖; 试点批裁定将传到约 60 域, 本批未改, 停在此)
1. **DOMAIN 的 CT 列**: PDF 为字面 `AE` / `DS`, KB (全库 spec.md) 为空. 补则全库统一补.
2. **CT 记法 C-code vs PDF codelist 短名**: AE 22 格 / DS 4 格 PDF 为 `(NY)` 等括号短名, KB 为 C-code (O24 "先定统一口径"). 脚注 "codelist values are enclosed in parentheses" 补入后与 KB 记法不符. 本批保留 C-code.
3. **脚注位置**: brief 定 "spec.md 文件末尾", 实际落在 KB 自写 `## Cross References` 块之后; U2 原话 "表下" (变量表止于 `---`, AE :545 / DS :149). 本批照 brief 放文件末尾; 若改 "表下" 应在 `---` 前.
4. **spec.md KB 自写行**: `> Class: Events | Structure: …` 与 `## Cross References` 块是否算纯导航 (不标 D6) — auditor 规则 "无 PDF 出处且未 D6 标注 → 忠实度错误", 需统一口径.

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-EVT_writer
python3 -I $S/spec_cmp.py AE 134,135,136,137 ; python3 -I $S/spec_cmp.py DS 155,156     # 剩余 DIFF 仅 CT #1/#2 与项目符号格式
python3 -I $S/scan.py AE 133 143 ; python3 -I $S/scan.py DS 155 167                      # 逐页 PDF→KB
python3 -I $S/rscan.py DS 155 167 knowledge_base/domains/DS/assumptions.md knowledge_base/domains/DS/examples.md
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # DIFF 3 / diffs 4 (全 T-n)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbbase/knowledge_base --out $S/fp_before.jsonl  # kbbase = git archive HEAD
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl   # 4041/4701 不变, 逐原子 diff 0 (本批新增原子均不在 fp 台账)
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/AE/assumptions.md | 12 ++++++++++++
 knowledge_base/domains/AE/spec.md        | 20 +++++++++++---------
 knowledge_base/domains/DS/assumptions.md | 20 ++++++++++++++------
 knowledge_base/domains/DS/spec.md        |  2 ++
 4 files changed, 39 insertions(+), 15 deletions(-)
```
- writer.jsonl: `work/t2_batches/S-EVT.writer.jsonl` 24 行 (改动 20 项 → 15 行 + CT 9 行拆分; census_items 4 行).

### 更正 (同 attempt, 自查后)
- 渲染补齐: p134/p135/p136 本次补渲染 (100dpi), 连同 p133/p137/p155/p156 七页均已逐页目视: 9 个 `*` 格 (p134 AECAT/AESCAT/AEBODSYS, p135 AEREL/AERLDEV/AEPATT, p136 AERLPRT/AERLPRC/AETOXGR) 与 KB 改后一致; PDF 空 CT 格与 KB 空一致; p137/p156 脚注文字一致; p133 §6.2 列表 7 项; DS spec 无 `*` 格. 上文 "依 … 渲染" 自此句起成立.
- 计数更正: AE C-code 格为 **21** (NY 13 + LOC/AESEV/ACN/DEACNDEV/OUT/EPOCH/STENRF×2 = 8), 非 22; 需主控定 #2 同改为 AE 21 / DS 4.
- 逐页日志更正: p155 本节原子 16 命中 **12** (未命中 a0013 节号标题 / a0018 表头 / a0027 a0028 C-code); p167 本节原子为 a0001-a0017 共 **17 命中 16** (a0010 原子抽取错); 原 "19 / 18" 混入 HO 的 a0024/a0025.
- spec 行判定口径: scan.py 的逐格兜底会把 `*` / `DS` 在全文任意处命中, 不可靠; spec 表行一律以 spec_cmp.py (逐变量逐字段) 为准. 按此 p134/p135/p136 的 "缺→已补" 列应为 **3→3 / 3→3 / 3→3** (CT `*`).
- writer.jsonl: `DELETED` (S-1 整条删) 与 `VERIFIED` (census_items 无改动核验) 不在 v1.0 action 枚举内; 已 grep `scripts/` 与 `work/scratch/t2/global/*.py` 无按 action 枚举取值的代码, 保留原名, 此处说明语义.
- Ex5 逐格行已改为不引 PDF 原文 (CDISC 引文 ≤25 词).

## attempt 1 delta (U7)
- 依据: 主控裁定 U7 (`evidence/checkpoints/t2_post_user_ack.md`). 只移位, 脚注文字不变; U5/U6 (C-code 记法 / DOMAIN CT) 留 S-CT 批, U8 导航不标 D6, O20 AE = p133-142 已采纳.

| # | kb_file | ref | action | before → after |
|---|---|---|---|---|
| 21 | AE/spec.md | ig34_p0137_a010 | MOVED | :572 (文件末尾) → :546 (最后变量块 `---` 之后, `## Cross References` :548 之前) |
| 22 | DS/spec.md | ig34_p0156_a0007 | MOVED | :172 (文件末尾) → :150 (`---` 之后, `## Cross References` :152 之前) |

- 行数不变 (AE 572 / DS 172); md5 after: AE/spec `b15e61f2418410250aae0ab19966cc5c`, DS/spec `0c46d567fcd7d1aa98522179c802f39d`. 文件末尾恢复为 Model Definition 链接行.
- check_links: live docs 42.
