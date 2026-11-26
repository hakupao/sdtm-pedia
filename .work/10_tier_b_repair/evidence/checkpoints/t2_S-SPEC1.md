# T2S S-SPEC1 — writer attempt 1 (spec-only: CO DM SM SV CM ML SU BE)

> 状态: writer 完成 (2026-11-26), 待 reviewer. 不 commit.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC1_writer/`
> 工具: `speccmp2.py` (由 `work/scratch/t2s_tools/speccmp.py` 派生: 表头行须含 Controlled+CDISC+Core; 表头词按词表剔除 (原版把首行 STUDYID 吞掉、无表头续页误认 body 里的 "Variable"); 表体止于 `In this column` 脚注 / `XX – Assumptions` / ©; **跨页续行并入上页末变量** (原版丢续行, 曾使 DM ARMCD / SU SUENRTPT 假阳); 另核 KB Order = 1..n). bbox = `pdftotext -bbox -f N -l N`; 渲染 100dpi: p60 62 63 64 84 86 87 98 99 100 121 122 129 130 131 143 144 全部目视.

## 完整节页范围 (O20 复核; spec-only 批只扫 spec 表所在页)
| 域 | 节 | 批 json lo-hi | spec 表实际页 | 复核依据 |
|---|---|---|---|---|
| CO | §5.1 | 60-62 | **p60** (表头→CODY + 脚注均在 p60) | 渲染 p60; p61 起为 CO – Assumptions/Examples |
| DM | §5.2 | 62-79 | **p62-64** (p62 STUDYID-SUBJID; p63 RFSTDTC-ARMCD; p64 ARMCD 续行-DMDY + 脚注¹²) | 渲染 p62-64; p65 起 DM – Assumptions |
| SM | §5.4 | 84-86 | **p84** (表 + 脚注, 其后 SM – Assumptions 同页) | 渲染 p84 |
| SV | §5.5 | 86-92 | **p86-87** (p86 STUDYID-SVREASOC; p87 SVCNTMOD-SVUPDES + 脚注) | 渲染 p86-87 |
| CM | §6.1.2 | 98-103 | **p98-100** (p100 CMSTRTPT-CMENTPT + 脚注) | 渲染 p98-100 |
| ML | §6.1.4 | 121-125 | **p121-122** | 渲染 p121-122 |
| SU | §6.1.6 | 129-133 | **p129-131** (p131 顶 = SUENRTPT Notes 续行, SUENTPT + 脚注) | 渲染 p129-131 |
| BE | §6.2.2 | 143-148 | **p143-144** (p144 BEDUR 后直接 BE – Assumptions, **PDF 无脚注文字**, 表头仍有 Format¹) | 渲染 p143-144; `grep "In this column" ig34_p014[2-9].txt` 空 |

## 双向全扫 (spec 表逐变量)
PDF→KB = speccmp2 bbox 逐变量 Label/Type/CT/Role/Core/CDISC Notes 比对 + 渲染目视; KB→PDF = 每个变量块只允许 `### VAR` + 7 个字段行 (awk 扫描: 块数 = PDF 变量数, 字段数 = 7×块数, 块内其它行 0 (BE 新增 D6 1 行除外)), `---` 之后仅脚注 + Cross References 导航 (U8). 改后数字:
| 域 | PDF 变量 | KB 变量 | 顺序/Order 1..n | 改后逐字段一致 | 改前差异 → 处理 | 剩余差异 (均非本批) |
|---|---|---|---|---|---|---|
| CO | 13 | 13 | 一致 / 是 | 9 | IDVAR CT 空→`*`; 脚注从 assumptions 迁入 | DOMAIN CT (U6); RDOMAIN/COEVAL/COEVALID C-code (U5) |
| DM | 32 | 32 | 一致 / 是 | 25 | RFSTDTC/RFENDTC Type DateTime→Char; `*`×5 (SITEID ARMCD ARM ACTARMCD ACTARM); RACE/ETHNIC guidance 上标 (T-1); 脚注¹² 补 | DOMAIN (U6); DTHFL AGEU SEX RACE ETHNIC ARMNRS C-code (U5); ETHNIC Notes "guidance¹" = T-1 |
| SM | 10 | 10 | 一致 / 是 | 9 | `*`×2 (MIDS MIDSTYPE); 脚注补 | DOMAIN (U6) |
| SV | 16 | 16 | 一致 / 是 | 9 | SVSTDTC/SVENDTC "IS0"→"ISO" (T-2); 脚注补; PDF 无 `*` (渲染核) | DOMAIN (U6); SVPRESP SVOCCUR SVCNTMOD SVEPCHGI C-code (U5); IS0 = T-2 |
| CM | 41 | 41 | 一致 / 是 | 28 | 脚注补; PDF 无 `*` (渲染 p98-100 核) | DOMAIN (U6); 12 处 C-code (U5) |
| ML | 37 | 37 | 一致 / 是 | 29 | `*`×3 (MLTRT MLCAT MLSCAT); 脚注补 | DOMAIN (U6); 6 处 C-code (U5); MLSTDTC CT = bbox 读序假阳 (layout p122:3-4 与渲染 = "ISO 8601 datetime or interval" = KB) |
| SU | 37 | 37 | 一致 / 是 | 24 | `*`×5 (SUDECOD SUCAT SUSCAT SUCLAS SUCLASCD); 脚注补; SUENRTPT Notes 末句在 p131 顶续行 = KB (VERIFIED, 未改) | DOMAIN (U6); 12 处 C-code (U5) |
| BE | 25 | 25 | 一致 / 是 | 22 | `*`×1 (BEPARTY); BECAT Notes 扩写 → 恢复 PDF 原文, 扩写部分 D6 (见下); 无脚注可补 | DOMAIN (U6); BEDECOD BELOC C-code (U5) |
- 长 Notes 逐字: speccmp2 两种比法 (去全部空白 / 仅折叠空白) 均跑, 后者另揭出 DM RACE/ETHNIC 上标与 SU "4.4.7 ," (PDF 原样 = KB). 跨页续行 2 处 (DM ARMCD p63→64, SU SUENRTPT p130→131) 已并入比对, KB 一致.
- 改后 speccmp2 输出: scratch `cmp2_after_<D>.txt`; 改前 `cmp2_before_<D>.txt`.

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | CO/spec.md:54 | pdf:p60:IDVAR CT | REPLACED | 空 → `*` | 60 |
| 2 | CO/spec.md:123 | pdf:p60:脚注¹ | MOVED | 自 CO/assumptions.md:17 迁入 (先插后删), `---` 后 Cross References 前 | 60 |
| 3 | DM/spec.md:44 / :53 | pdf:p63:RFSTDTC/RFENDTC Type | REPLACED | DateTime → Char | 63 |
| 4 | DM/spec.md:135 :216 :225 :234 :243 | pdf:p63-64 CT 列 | REPLACED | 空 → `*` ×5 (SITEID ARMCD ARM ACTARMCD ACTARM) | 63-64 |
| 5 | DM/spec.md:201 | pdf:p63:RACE Notes | REPLACED | "guidance2" → "guidance²" (上标, 绑定脚注²) | 63 |
| 6 | DM/spec.md:210 | pdf:p63:ETHNIC Notes | REPLACED | "guidance1" → "guidance²" (T-1) | 63 |
| 7 | DM/spec.md:294 / :296 | ig34_p0064_a011 / a012 | INSERTED | 脚注¹ + 脚注² (FDA guidance 引文, URL 纯文本) | 64 |
| 8 | SM/spec.md:45 :54 | pdf:p84 CT 列 | REPLACED | 空 → `*` ×2 | 84 |
| 9 | SM/spec.md:96 | ig34_p0084_a018 | INSERTED | 脚注¹ | 84 |
| 10 | SV/spec.md:111 :120 | pdf:p87:SVSTDTC/SVENDTC Notes | REPLACED | "IS0 8601" → "ISO 8601" (T-2) | 87 |
| 11 | SV/spec.md:150 | ig34_p0087_a009 | INSERTED | 脚注¹ | 87 |
| 12 | CM/spec.md:375 | ig34_p0100_a005 | INSERTED | 脚注¹ | 100 |
| 13 | ML/spec.md:63 :72 :81 | pdf:p121 CT 列 | REPLACED | 空 → `*` ×3 | 121 |
| 14 | ML/spec.md:339 | ig34_p0122_a015 | INSERTED | 脚注¹ | 122 |
| 15 | SU/spec.md:81 :90 :99 :144 :153 | pdf:p129 CT 列 | REPLACED | 空 → `*` ×5 | 129 |
| 16 | SU/spec.md:339 | ig34_p0131_a003 | INSERTED | 脚注¹ | 131 |
| 17 | BE/spec.md:111 | pdf:p143:BECAT Notes | REPLACED | KB 扩写尾 → PDF 原文 "…COLLECTION, PREPARATION, TRANSPORT." | 143 |
| 18 | BE/spec.md:113 | KB_AUTHORED | INSERTED (D6) | BECAT 扩写句移入 `> KB note (not in SDTMIG):` 行 (块内, CDISC Notes 下) | 143 |
| 19 | BE/spec.md:137 | pdf:p143:BEPARTY CT | REPLACED | 空 → `*` | 143 |
| 20 | SU/spec.md (SUENRTPT Notes) | pdf:p130-131 | VERIFIED | 末句 "Not all values … 4.4.7 , …" 在 p131 顶续行, KB = PDF, 不改 | 130-131 |
合计: 改动 19 处 (CT `*` 17 格计入 #1/4/8/13/15/19), VERIFIED 1. 插入文字全部取自 layout 文本 + 渲染.

## 结构改动清单
- 无整条/整块增删挪位. 仅: CO 脚注段在文件间 MOVED (#2); BE BECAT 块内新增 1 行 D6 (#18).

## 删除清单
| # | 位置 | 删除内容 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | CO/assumptions.md:17 (+前置空行) | spec 表脚注¹ 段 | footnote_moves (U2/U7, narrow 授权) | CO/spec.md:123 |
| D-2 | BE/spec.md:111 | BECAT Notes 内 "(CDISC canonical examples per SDTMIG v3.4)" 括注 | KB 自写括注, 冗余 (PDF 原文已含三例); 其余扩写句保留为 D6 | — |

## D6 标注清单
| # | 位置 | 内容 | 判断 |
|---|---|---|---|
| D6-1 | BE/spec.md:113 | BECAT sponsor-extensible / EXTRACTION 等 (KB 原文逐字) | EXTRACTION 为 PDF p146 BE Ex 实际 BECAT 值 (不矛盾); 但 "controlled-vocabulary convention" 无 PDF 依据 (BECAT CT 格 PDF 为空) → **需主控定** (保留 D6 还是 D2 删); 也是首个 spec.md 块内 D6 |

## PDF_TYPO 清单
| T | 位置 | PDF | KB 处理 | 依据 |
|---|---|---|---|---|
| T-1 | DM ETHNIC Notes (p63) | "FDA guidance¹" | 写 "guidance²" | PDF 自身: 脚注¹ = CT 星号说明, 脚注² = FDA Race and Ethnicity guidance; RACE 同句用 ² |
| T-2 | SV SVSTDTC/SVENDTC Notes (p87) | "IS0 8601" (数字 0) | 写 "ISO 8601" | 同表其它 ISO 8601 及 CT 列 "ISO 8601 datetime or interval" |
| T-3 | DM 脚注² 末尾 (p64) | URL 后孤立 ")" 、"Services;2016" 无空格 | **照录** | 无法由 PDF 自身确定原意 (可能引文格式残留), 报 T4 用户裁定 |

## 范围外发现
- O15/O21/O24/O26 (本批部分): 本批 8 域 spec 脚注 / `*` 已补 (BE 无 PDF 脚注); C-code 记法与 DOMAIN CT 留 S-CT (U5/U6). O21 (FA/spec) 不在本批.
- 工具: 原 `t2s_tools/speccmp.py` 有 3 处缺陷 (首变量 STUDYID 被表头窗口吞、续页 body 里 "Variable" 误当表头致崩溃、跨页续行丢失) — 后续 spec 批建议用 scratch `speccmp2.py` 或同等修正.
- 新范围外 KB 错: 无.

## 需主控定
1. D6-1 (BE BECAT 扩写): 保留为块内 D6, 还是因 "controlled-vocabulary" 与 PDF CT 空格冲突按 D2 整句删除.
2. T-3 DM 脚注² 照录 PDF 孤立 ")" 是否保留.

## 自查
- 只改: 8 个 spec.md + CO/assumptions.md (仅删脚注段). `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42.
- 复跑: `pdftotext -bbox -f N -l N "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/bb_N.html` (N = 60 62 63 64 84 86 87 98 99 100 121 122 129 130 131 143 144); `python3 -I $S/speccmp2.py $S <D> <pages>`.

## git diff --stat
```
 knowledge_base/domains/BE/spec.md        |  6 ++++--
 knowledge_base/domains/CM/spec.md        |  2 ++
 knowledge_base/domains/CO/assumptions.md |  2 --
 knowledge_base/domains/CO/spec.md        |  4 +++-
 knowledge_base/domains/DM/spec.md        | 22 +++++++++++++---------
 knowledge_base/domains/ML/spec.md        |  8 +++++---
 knowledge_base/domains/SM/spec.md        |  6 ++++--
 knowledge_base/domains/SU/spec.md        | 12 +++++++-----
 knowledge_base/domains/SV/spec.md        |  6 ++++--
 9 files changed, 42 insertions(+), 26 deletions(-)
```

## 双向全扫 — 逐变量结果表 (由 scratch `cmp2_after_<D>.txt` 机械生成, 未手填)
分类: OK = Label/Type/CT/Role/Core/CDISC Notes 六字段与 PDF bbox 一致 (Order 1..n 另核); U5 = CT C-code vs PDF 括号短名 (S-CT); U6 = DOMAIN CT (S-CT); T-n = PDF_TYPO; RO = bbox 读序假阳 (layout/渲染 = KB).

| 域 | 页 | 变量 | 结果 |
|---|---|---|---|
| CO | 60 | STUDYID | OK |
| CO | 60 | DOMAIN | U6 (DOMAIN CT) |
| CO | 60 | RDOMAIN | U5 (C-code) |
| CO | 60 | USUBJID | OK |
| CO | 60 | COSEQ | OK |
| CO | 60 | IDVAR | OK |
| CO | 60 | IDVARVAL | OK |
| CO | 60 | COREF | OK |
| CO | 60 | COVAL | OK |
| CO | 60 | COEVAL | U5 (C-code) |
| CO | 60 | COEVALID | U5 (C-code) |
| CO | 60 | CODTC | OK |
| CO | 60 | CODY | OK |
| DM | 62 | STUDYID | OK |
| DM | 62 | DOMAIN | U6 (DOMAIN CT) |
| DM | 62 | USUBJID | OK |
| DM | 62 | SUBJID | OK |
| DM | 63 | RFSTDTC | OK |
| DM | 63 | RFENDTC | OK |
| DM | 63 | RFXSTDTC | OK |
| DM | 63 | RFXENDTC | OK |
| DM | 63 | RFCSTDTC | OK |
| DM | 63 | RFCENDTC | OK |
| DM | 63 | RFICDTC | OK |
| DM | 63 | RFPENDTC | OK |
| DM | 63 | DTHDTC | OK |
| DM | 63 | DTHFL | U5 (C-code) |
| DM | 63 | SITEID | OK |
| DM | 63 | INVID | OK |
| DM | 63 | INVNAM | OK |
| DM | 63 | BRTHDTC | OK |
| DM | 63 | AGE | OK |
| DM | 63 | AGEU | U5 (C-code) |
| DM | 63 | SEX | U5 (C-code) |
| DM | 63 | RACE | U5 (C-code) |
| DM | 63 | ETHNIC | U5 (C-code); T-1 (guidance¹→²) |
| DM | 63 | ARMCD | OK |
| DM | 64 | ARM | OK |
| DM | 64 | ACTARMCD | OK |
| DM | 64 | ACTARM | OK |
| DM | 64 | ARMNRS | U5 (C-code) |
| DM | 64 | ACTARMUD | OK |
| DM | 64 | COUNTRY | OK |
| DM | 64 | DMDTC | OK |
| DM | 64 | DMDY | OK |
| SM | 84 | STUDYID | OK |
| SM | 84 | DOMAIN | U6 (DOMAIN CT) |
| SM | 84 | USUBJID | OK |
| SM | 84 | SMSEQ | OK |
| SM | 84 | MIDS | OK |
| SM | 84 | MIDSTYPE | OK |
| SM | 84 | SMSTDTC | OK |
| SM | 84 | SMENDTC | OK |
| SM | 84 | SMSTDY | OK |
| SM | 84 | SMENDY | OK |
| SV | 86 | STUDYID | OK |
| SV | 86 | DOMAIN | U6 (DOMAIN CT) |
| SV | 86 | USUBJID | OK |
| SV | 86 | VISITNUM | OK |
| SV | 86 | VISIT | OK |
| SV | 86 | SVPRESP | U5 (C-code) |
| SV | 86 | SVOCCUR | U5 (C-code) |
| SV | 86 | SVREASOC | OK |
| SV | 87 | SVCNTMOD | U5 (C-code) |
| SV | 87 | SVEPCHGI | U5 (C-code) |
| SV | 87 | VISITDY | OK |
| SV | 87 | SVSTDTC | T-2 (IS0→ISO) |
| SV | 87 | SVENDTC | T-2 (IS0→ISO) |
| SV | 87 | SVSTDY | OK |
| SV | 87 | SVENDY | OK |
| SV | 87 | SVUPDES | OK |
| CM | 98 | STUDYID | OK |
| CM | 98 | DOMAIN | U6 (DOMAIN CT) |
| CM | 98 | USUBJID | OK |
| CM | 98 | CMSEQ | OK |
| CM | 98 | CMGRPID | OK |
| CM | 98 | CMSPID | OK |
| CM | 98 | CMTRT | OK |
| CM | 98 | CMMODIFY | OK |
| CM | 98 | CMDECOD | OK |
| CM | 98 | CMCAT | OK |
| CM | 98 | CMSCAT | OK |
| CM | 98 | CMPRESP | U5 (C-code) |
| CM | 98 | CMOCCUR | U5 (C-code) |
| CM | 98 | CMSTAT | U5 (C-code) |
| CM | 98 | CMREASND | OK |
| CM | 98 | CMINDC | OK |
| CM | 98 | CMCLAS | OK |
| CM | 99 | CMCLASCD | OK |
| CM | 99 | CMDOSE | OK |
| CM | 99 | CMDOSTXT | OK |
| CM | 99 | CMDOSU | U5 (C-code) |
| CM | 99 | CMDOSFRM | U5 (C-code) |
| CM | 99 | CMDOSFRQ | U5 (C-code) |
| CM | 99 | CMDOSTOT | OK |
| CM | 99 | CMDOSRGM | OK |
| CM | 99 | CMROUTE | U5 (C-code) |
| CM | 99 | CMADJ | OK |
| CM | 99 | CMRSDISC | OK |
| CM | 99 | TAETORD | OK |
| CM | 99 | EPOCH | U5 (C-code) |
| CM | 99 | CMSTDTC | OK |
| CM | 99 | CMENDTC | OK |
| CM | 99 | CMSTDY | OK |
| CM | 99 | CMENDY | OK |
| CM | 99 | CMDUR | OK |
| CM | 99 | CMSTRF | U5 (C-code) |
| CM | 99 | CMENRF | U5 (C-code) |
| CM | 100 | CMSTRTPT | U5 (C-code) |
| CM | 100 | CMSTTPT | OK |
| CM | 100 | CMENRTPT | U5 (C-code) |
| CM | 100 | CMENTPT | OK |
| ML | 121 | STUDYID | OK |
| ML | 121 | DOMAIN | U6 (DOMAIN CT) |
| ML | 121 | USUBJID | OK |
| ML | 121 | MLSEQ | OK |
| ML | 121 | MLGRPID | OK |
| ML | 121 | MLSPID | OK |
| ML | 121 | MLTRT | OK |
| ML | 121 | MLCAT | OK |
| ML | 121 | MLSCAT | OK |
| ML | 121 | MLPRESP | U5 (C-code) |
| ML | 121 | MLOCCUR | U5 (C-code) |
| ML | 121 | MLSTAT | U5 (C-code) |
| ML | 121 | MLREASND | OK |
| ML | 121 | MLDOSE | OK |
| ML | 121 | MLDOSTXT | OK |
| ML | 121 | MLDOSU | U5 (C-code) |
| ML | 121 | MLDOSFRM | U5 (C-code) |
| ML | 121 | VISITNUM | OK |
| ML | 121 | VISIT | OK |
| ML | 121 | VISITDY | OK |
| ML | 121 | TAETORD | OK |
| ML | 121 | EPOCH | U5 (C-code) |
| ML | 121 | MLDTC | OK |
| ML | 122 | MLSTDTC | RO (CT 换行读序; layout p122:3-4 = KB) |
| ML | 122 | MLENDTC | OK |
| ML | 122 | MLDY | OK |
| ML | 122 | MLSTDY | OK |
| ML | 122 | MLENDY | OK |
| ML | 122 | MLDUR | OK |
| ML | 122 | MLTPT | OK |
| ML | 122 | MLTPTNUM | OK |
| ML | 122 | MLELTM | OK |
| ML | 122 | MLTPTREF | OK |
| ML | 122 | MLRFTDTC | OK |
| ML | 122 | MIDS | OK |
| ML | 122 | RELMIDS | OK |
| ML | 122 | MIDSDTC | OK |
| SU | 129 | STUDYID | OK |
| SU | 129 | DOMAIN | U6 (DOMAIN CT) |
| SU | 129 | USUBJID | OK |
| SU | 129 | SUSEQ | OK |
| SU | 129 | SUGRPID | OK |
| SU | 129 | SUSPID | OK |
| SU | 129 | SUTRT | OK |
| SU | 129 | SUMODIFY | OK |
| SU | 129 | SUDECOD | OK |
| SU | 129 | SUCAT | OK |
| SU | 129 | SUSCAT | OK |
| SU | 129 | SUPRESP | U5 (C-code) |
| SU | 129 | SUOCCUR | U5 (C-code) |
| SU | 129 | SUSTAT | U5 (C-code) |
| SU | 129 | SUREASND | OK |
| SU | 129 | SUCLAS | OK |
| SU | 129 | SUCLASCD | OK |
| SU | 129 | SUDOSE | OK |
| SU | 130 | SUDOSTXT | OK |
| SU | 130 | SUDOSU | U5 (C-code) |
| SU | 130 | SUDOSFRM | U5 (C-code) |
| SU | 130 | SUDOSFRQ | U5 (C-code) |
| SU | 130 | SUDOSTOT | OK |
| SU | 130 | SUROUTE | U5 (C-code) |
| SU | 130 | TAETORD | OK |
| SU | 130 | EPOCH | U5 (C-code) |
| SU | 130 | SUSTDTC | OK |
| SU | 130 | SUENDTC | OK |
| SU | 130 | SUSTDY | OK |
| SU | 130 | SUENDY | OK |
| SU | 130 | SUDUR | OK |
| SU | 130 | SUSTRF | U5 (C-code) |
| SU | 130 | SUENRF | U5 (C-code) |
| SU | 130 | SUSTRTPT | U5 (C-code) |
| SU | 130 | SUSTTPT | OK |
| SU | 130 | SUENRTPT | U5 (C-code) |
| SU | 131 | SUENTPT | OK |
| BE | 143 | STUDYID | OK |
| BE | 143 | DOMAIN | U6 (DOMAIN CT) |
| BE | 143 | USUBJID | OK |
| BE | 143 | SPDEVID | OK |
| BE | 143 | BESEQ | OK |
| BE | 143 | BEGRPID | OK |
| BE | 143 | BEREFID | OK |
| BE | 143 | BESPID | OK |
| BE | 143 | BETERM | OK |
| BE | 143 | BEMODIFY | OK |
| BE | 143 | BEDECOD | U5 (C-code) |
| BE | 143 | BECAT | OK |
| BE | 143 | BESCAT | OK |
| BE | 143 | BELOC | U5 (C-code) |
| BE | 143 | BEPARTY | OK |
| BE | 143 | BEPRTYID | OK |
| BE | 144 | VISITNUM | OK |
| BE | 144 | VISIT | OK |
| BE | 144 | VISITDY | OK |
| BE | 144 | BEDTC | OK |
| BE | 144 | BESTDTC | OK |
| BE | 144 | BEENDTC | OK |
| BE | 144 | BESTDY | OK |
| BE | 144 | BEENDY | OK |
| BE | 144 | BEDUR | OK |

变量行合计: CO 13, DM 32, SM 10, SV 16, CM 41, ML 37, SU 37, BE 25 = 211

### 逐页 (spec 表页)
| 页 | 域 | 变量数 (bbox) | 一致 | 非本批残留 | 已修 |
|---|---|---|---|---|---|
| 60 | CO | 13 | 9 | 4 | 2 |
| 62 | DM | 4 | 3 | 1 | 0 |
| 63 | DM | 20 | 15 | 5 | 6 |
| 64 | DM | 8 | 7 | 1 | 5 |
| 84 | SM | 10 | 9 | 1 | 3 |
| 86 | SV | 8 | 5 | 3 | 0 |
| 87 | SV | 8 | 4 | 4 | 3 |
| 98 | CM | 17 | 13 | 4 | 0 |
| 99 | CM | 20 | 13 | 7 | 0 |
| 100 | CM | 4 | 2 | 2 | 1 |
| 121 | ML | 23 | 16 | 7 | 3 |
| 122 | ML | 14 | 13 | 1 | 1 |
| 129 | SU | 18 | 14 | 4 | 5 |
| 130 | SU | 18 | 9 | 9 | 0 |
| 131 | SU | 1 | 1 | 0 | 1 |
| 143 | BE | 16 | 13 | 3 | 3 |
| 144 | BE | 9 | 9 | 0 | 0 |

- "已修" = writer.jsonl 中该页 spec.md 行级改动数 (含脚注插入). jsonl 共 35 行 = spec.md 33 行级改动 + CO/assumptions 1 删除 (MOVED 源) + 1 VERIFIED; 上文变更清单 19 行为分组行 (CT `*` 17 格分 6 行). `*` 写法与 AG/spec.md 先例同 (`- **Controlled Terms:** *`).

## 主控提醒后复跑 (`work/scratch/t2s_tools/sc2.py` + `sc2w.py`, 改后 KB)
上文逐变量/逐页表用的是 writer 自修版 `speccmp2.py` (scratch); 按主控要求以修正版 sc2 (去空白比) / sc2w (仅折叠空白比) 复跑全部 8 域, 输出 scratch `sc2_after_<D>.txt` / `sc2w_after_<D>.txt`. 命令: `python3 -I work/scratch/t2s_tools/sc2.py $S <D> <pages>` (pages 同上, 均取默认表头; CM p99/p100 无表头沿用前页列 x).

**计数闸 (PDF 变量数 = KB 变量数 + 顺序一致, KB Order 不符 0)**: CO 13=13 ✓ / DM 32=32 ✓ / SM 10=10 ✓ / SV 16=16 ✓ / CM 41=41 ✓ / ML 37=37 ✓ / SU 37=37 ✓ / BE 25=25 ✓. FOOT 识别: CO p60 / DM p64 / SM p84 / SV p87 / CM p100 / ML p122 / SU p131 均有脚注¹ (KB 已补); BE 无 (= PDF). (sc2 FOOT 只抓 ¹, DM 脚注² p64 已渲染核.)

sc2/sc2w 残留 (U5 C-code / U6 DOMAIN 之外) 逐条归类, 无新 KB 差异:
| 域 | 变量 | 脚本 | 归类 |
|---|---|---|---|
| DM | ARMCD Notes | sc2, sc2w | sc2 丢跨页续行 (p64 顶 "ARMCD values would be 20…Trial Arms dataset."); speccmp2 并续行后一致, 渲染 p64 核 = KB |
| SU | SUENRTPT Notes | sc2, sc2w | 同上, p131 顶续行 "Not all values … 4.4.7 , …"; 渲染 p131 = KB (VERIFIED) |
| DM | ETHNIC Notes | sc2, sc2w | T-1 |
| DM | RACE Notes | sc2w | 上标 ² 被 bbox 读成 " 2" (空白差), KB "guidance²" = 渲染 p63 |
| SV | SVSTDTC / SVENDTC Notes | sc2, sc2w | T-2 |
| CO | COREF / COVAL Notes | sc2w | 行尾连字符折行 ("650-␣VITALS", "COVAL1-␣COVALn"), 渲染 p60 为折行, KB 连写正确 |
| CM | CMCAT Notes | sc2w | 同上 ("ANTI-␣CANCER", 渲染 p98 折行) |
- speccmp2 曾报的 ML MLSTDTC CT 读序假阳在 sc2 下消失 (一致). 结论不变, KB 无需追加改动.

## attempt 1 delta (主控裁定 2026-11-26)
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| Δ1 | BE/spec.md:111-112 | kb_authored:BE:BECAT | DELETED (D2) | 删块内 D6 行 (BECAT sponsor-extensible / EXTRACTION / "controlled-vocabulary convention") 及其前空行; BECAT Notes = PDF 原文 | 143 |
| Δ2 | DM/spec.md:296 | ig34_p0064_a012 | REPLACED (T-3) | 脚注² 末尾孤立 ")" 删除 | 64 |
- 删除清单追加 D-3: BE/spec.md 原 :113 D6 行 (主控裁定: 与 PDF BECAT CT 空格矛盾 → D2); 上文 D6-1 作废, 本批 D6 = 0.
- PDF_TYPO T-3 改判: PDF 脚注² URL 后 ")" 无对应开括号, 正确值由 PDF 自身确定 → KB 写正确值 (去 ")"); "Services;2016" 无空格保留照录 (不在裁定内, 不动).
- 脚本: 主比对 = writer 自修版 scratch `speccmp2.py`; 复核 = 主控修正版 `work/scratch/t2s_tools/sc2.py` + `sc2w.py` (见上段). 计数闸 (PDF 变量数 = KB 变量数, 顺序一致, Order 1..n) 8 域全过: CO 13 / DM 32 / SM 10 / SV 16 / CM 41 / ML 37 / SU 37 / BE 25. delta 后 BE BECAT 与 DM 脚注已复核 (BE 块内非字段行 0).
- 合计 (终): spec.md 行级改动 33 (BE BECAT 由 "改+D6" 变为 "改") + CO/assumptions 删 1; 删除清单 3 条 (D-1 D-2 D-3); D6 0; PDF_TYPO T-1 T-2 T-3 均 KB 写正确值.
