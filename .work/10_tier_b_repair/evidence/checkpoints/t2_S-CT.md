# T2S 脚本批 S-CT — writer attempt 2 (写入; U5/U6 + KB note + SR T-5)

> 2026-11-26, oh-my-claudecode:executor (opus), 角色 writer. 批次 `work/t2_batches/S-CT.json`; 主控裁定 (a)-(d) 见下. dry-run (attempt 1) 报告 = `evidence/checkpoints/t2_S-CT_dryrun.md`, 逐变量源 = `work/t2_batches/S-CT.dryrun.jsonl`.
> 未 stash/checkout/reset/commit; 基线 = `git show HEAD:knowledge_base/domains/<D>/spec.md` (改前 `git diff --quiet -- knowledge_base` 为 clean). xlsx / PDF 文本未入库.
> 脚本 (提交): `scripts/t2s/ct_extract.py` (提取+分类, attempt 1) · `scripts/t2s/ct_apply.py` (变换) · `scripts/t2s/ct_assert.py` (断言闸). writer 日志 `work/t2_batches/S-CT.writer.jsonl` (689 行).
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CT_writer/` (kbA/ = 测试副本, 与仓库改后 `diff -r` 无输出; mut.log = 变异测试原始输出).

## 主控裁定 (attempt 2 授权)
- (a) U6 闸 = 59/59 (RELREC/RELSPEC/RELSUB/SUPPQUAL 无 DOMAIN 变量).
- (b) KB note 只加在含 C-code 的 59 个 spec.md (SM/TD/TE/TV 不加); 措辞 `> KB note (not in SDTMIG): C-codes after the parenthesised codelist names are NCI codelist codes added by this KB (CDISC CT).`; 位置 = 脚注之后、`## Cross References` 之前 (BE 无脚注 → `---` 之后).
- (c) SR SRDY "sponsor- defined" → "sponsor-defined", 登记 **SR T-5** (见下), 本批唯一非 CT 行改动 (断言白名单).
- (d) 多 codelist 格 `(A) Cx; (B) Cy`, 不登记.

## 完整节页范围 (每域 spec 表页; json = `.work/02_indexing/page_index.json`)
| 域 | 节 (json) | json spec | **spec 表页 (实测)** | PDF/KB 变量 | 顺序 | KB Order 1..n | 解析备注 |
|---|---|---|---|---|---|---|---|
| AE | 133-142 | 134-137 | **134-137** | 60/60 | 一致 | 是 | — |
| AG | 92-97 | 92-94 | **92-94** | 41/41 | 一致 | 是 | p94 CONT -> AGSTRF (续行并入) |
| BE | 143-148 | 143-144 | **143-144** | 25/25 | 一致 | 是 | — |
| BS | 196-199 | 196-198 | **196-198** | 35/35 | 一致 | 是 | — |
| CE | 148-155 | 148-150 | **148-150** | 32/32 | 一致 | 是 | — |
| CM | 98-103 | 98-100 | **98-100** | 41/41 | 一致 | 是 | p99 no header (reuse x); p100 no header (reuse x) |
| CO | 60-62 | 60 | **60** | 13/13 | 一致 | 是 | — |
| CP | 199-220 | 200-204 | **200-204** | 62/62 | 一致 | 是 | p202 CONT -> CPGATE (续行并入) |
| CV | 286-289 | 286-288 | **286-288** | 42/42 | 一致 | 是 | — |
| DA | 180-182 | 180-181 | **180-181** | 27/27 | 一致 | 是 | — |
| DD | 183-185 | 183 | **183** | 12/12 | 一致 | 是 | — |
| DM | 62-78 | 62-64 | **62-64** | 32/32 | 一致 | 是 | p63 superscript-size words dropped: 2 1; p64 CONT -> ARMCD (续行并入) |
| DS | 155-167 | 155-156 | **155-156** | 16/16 | 一致 | 是 | p156 no header (reuse x) |
| DV | 178-179 | 178-179 | **178-179** | 16/16 | 一致 | 是 | p179 no header (reuse x) |
| EC | 107-110 | 107-109 | **107-109** | 45/45 | 一致 | 是 | — |
| EG | 185-192 | 185-188 | **185-188** | 44/44 | 一致 | 是 | — |
| EX | 104-107 | 104-105 | **104-105** | 37/37 | 一致 | 是 | — |
| FA | 364-375 | 365-366 | **365-366** | 30/30 | 一致 | 是 | — |
| FT | 319-324 | 319-320 | **319-320** | 38/38 | 一致 | 是 | — |
| GF | 220-228 | 221-223 | **221-223** | 57/57 | 一致 | 是 | — |
| HO | 167-171 | 167-169 | **167-169** | 28/28 | 一致 | 是 | — |
| IE | 193-194 | 193 | **193** | 18/18 | 一致 | 是 | — |
| IS | 228-241 | 229-231 | **229-231** | 54/54 | 一致 | 是 | p231 CONT -> ISDRVFL (续行并入) |
| LB | 241-248 | 242-245 | **242-245** | 62/62 | 一致 | 是 | p243 CONT -> LBCOLSRT (续行并入) |
| MB | 248-252 | 249-251 | **249-251** | 47/47 | 一致 | 是 | — |
| MH | 171-178 | 171-172 | **171-172** | 27/27 | 一致 | 是 | — |
| MI | 263-267 | 264-265 | **264-265** | 37/37 | 一致 | 是 | — |
| MK | 290-294 | 290-291 | **290-291** | 42/42 | 一致 | 是 | — |
| ML | 121-124 | 121-122 | **121-122** | 37/37 | 一致 | 是 | — |
| MS | 252-256 | 252-255 | **252-255** | 61/61 | 一致 | 是 | — |
| NV | 294-298 | 294-296 | **294-296** | 42/42 | 一致 | 是 | — |
| OE | 298-305 | 299-301 | **299-301** | 52/52 | 一致 | 是 | — |
| OI | 441-443 | 441 | **441** | 7/7 | 一致 | 是 | — |
| PC | 267-283 | 267-269 | **267-269** | 41/41 | 一致 | 是 | — |
| PE | 315-318 | 316-317 | **316-317** | 30/30 | 一致 | 是 | — |
| PP | 271-283 | 271-272 | **271-272** | 26/26 | 一致 | 是 | — |
| PR | 125-128 | 125-126 | **125-126** | 45/45 | 一致 | 是 | — |
| QS | 324-329 | 324-326 | **324-326** | 35/35 | 一致 | 是 | — |
| RE | 308-312 | 308-310 | **308-310** | 47/47 | 一致 | 是 | — |
| RELREC | 428-430 | 428 | **429** (≠json) | 7/7 | 一致 | 是 | — |
| RELSPEC | 438-440 | 438 | **439** (≠json) | 6/6 | 一致 | 是 | — |
| RELSUB | 437-438 | 437 | **438** (≠json) | 5/5 | 一致 | 是 | — |
| RP | 305-307 | 305-306 | **305-306** | 36/36 | 一致 | 是 | — |
| RS | 329-339 | 329-332 | **329-332** | 46/46 | 一致 | 是 | p330 CONT -> RSTESTCD (续行并入) |
| SC | 339-342 | 340-341 | **340-341** | 24/24 | 一致 | 是 | — |
| SE | 79-83 | 79-80 | **79-80** | 13/13 | 一致 | 是 | — |
| SM | 84-86 | 84 | **84** | 10/10 | 一致 | 是 | — |
| SR | 375-381 | 376-377 | **376-377** | 39/39 | 一致 | 是 | — |
| SS | 342-343 | 342-343 | **342-343** | 22/22 | 一致 | 是 | — |
| SU | 129-132 | 129-131 | **129-131** | 37/37 | 一致 | 是 | p131 CONT -> SUENRTPT (续行并入) |
| SUPPQUAL | 430-432 | 431 | **432** (≠json) | 10/10 | 一致 | 是 | — |
| SV | 86-91 | 86-87 | **86-87** | 16/16 | 一致 | 是 | — |
| TA | 385-404 | 385-386 | **384-385** (≠json) | 10/10 | 一致 | 是 | p385 CONT -> ARMCD (续行并入) |
| TD | 412-416 | 412-413 | **410-411** (≠json) | 9/9 | 一致 | 是 | p411 no header (reuse x) |
| TE | 404-409 | 405 | **403** (≠json) | 7/7 | 一致 | 是 | — |
| TI | 418-419 | 418 | **416** (≠json) | 8/8 | 一致 | 是 | — |
| TM | 417-417 | 417 | **415** (≠json) | 5/5 | 一致 | 是 | — |
| TR | 350-353 | 350-352 | **350-352** | 32/32 | 一致 | 是 | — |
| TS | 419-425 | 419-420 | **417-418** (≠json) | 11/11 | 一致 | 是 | — |
| TU | 344-349 | 345-346 | **345-346** | 31/31 | 一致 | 是 | — |
| TV | 409-412 | 409-410 | **407-408** (≠json) | 9/9 | 一致 | 是 | — |
| UR | 312-315 | 312-314 | **312-314** | 43/43 | 一致 | 是 | — |
| VS | 358-361 | 358-360 | **358-360** | 38/38 | 一致 | 是 | — |
- 计数闸: **63/63 域 PDF 变量数 = KB 变量数, 顺序一致, KB Order 1..n 连续**; 合计 1917 变量 (= SDTMIG_v3.4.xlsx Variables 1917 行). KB 1917 个变量块均为 7 字段 (Order/Label/Type/Controlled Terms/Role/Core/CDISC Notes).
- page_index.json 的 spec 页对 RELREC/RELSPEC/RELSUB/SUPPQUAL/TA/TD/TE/TI/TM/TS/TV 偏 1-2 页 (json 标 "E" 估计值), 上表 "实测" 列为准.

## 双向全扫 (本批口径 = 63 个 spec.md 的 Controlled Terms 列 + B 部分 30 域全字段; 明细见 dry-run 报告)
- PDF→KB: 63/63 域 1917/1917 变量命中, 顺序一致, Order 1..n 连续; 每个 PDF CT 单元格 → 类 1 (570, 加短名) / 类 6 (59, 填域代码) / 类 7 (1288, 已一致不动); 类 2/3/4/5 = 0.
- KB→PDF: KB 变量块 1917 个全有 PDF 对应 (kb-only 0); 改后含 C-code 的 CT 行全带 PDF 括号短名 (断言 "un-prefixed C-code" 0).
- 短名↔C-code: 588/588 由断言脚本实时查 `SDTM Terminology.xlsx` codelist 行核 (非 jsonl 自证); KB 原 C-code 与 `SDTMIG_v3.4.xlsx` Variables!H 1917/1917 一致.
- B 部分 (S-EVT…S-SPREL 30 域全字段重比): 无 KB 偏离 PDF 的真错; 唯一新发现 SR SRDY → 本批按 (c) 改正并登记 T-5.

## 改动汇总
| 类 | 内容 | 格/行 |
|---|---|---|
| U5 (类 1) | `C66742` → `(NY) C66742`; 多 codelist `(A) Cx; (B) Cy` (10 格) | 570 行 / 588 码 |
| U6 (类 6) | DOMAIN CT 空 → 本域代码 | 59 行 |
| KB note | 脚注后、Cross References 前, + 1 空行 | 59 文件 × 2 行 |
| SR T-5 | SR/spec.md SRDY CDISC Notes "sponsor- defined" → "sponsor-defined" | 1 行 |
| 合计 | 63 文件, 630 行替换 + 118 行新增 | |

## PDF_TYPO 登记
| T-n | 位置 | PDF 原文 | KB 写 | 依据 |
|---|---|---|---|---|
| SR T-5 (新, 接 B-SR T-1..T-4) | SR/spec.md SRDY CDISC Notes (p377) | "relative to sponsor- defined RFSTDTC" (同一行内连字符后空格, 非折行; layout `ig34_p0377.txt:27` + 渲染 `v_SRDY-377.png`) | "sponsor-defined" | 同表/他域 --DY Notes 均 "sponsor-defined" (PDF 自身可定); 主控裁定 (c) |

## 断言闸 (`ct_assert.py`)
- 规则: 每个 spec.md 与 HEAD 行级 diff; 替换行须 ∈ {Controlled Terms 行, SR SRDY 白名单 (旧/新整行精确匹配)}; 插入块须恰为 [空行, KB note] 且下一非空行为 `## Cross References`、位于 `---` 之后; 删除 / 行数不等替换 → FAIL. CT 行: 去掉 `(SHORT) ` 前缀后 == 改前, 且每个 (SHORT)→C-code 与 Terminology xlsx 一致 (类 1); 或改前空 & 改后 = 本域代码且变量为 DOMAIN (类 6). 每文件: 不得残留无前缀 C-code; DOMAIN CT = 域代码; KB note 数 = 1 (含码) / 0 (无码). 总数: 类 1 = 570 / 码 588 / 类 6 = 59 / note 59 / SRDY 1.
- 正对照: HEAD 原状 → FAIL (notes 0, srdy 0); 测试副本 kbA 改后 → PASS; 仓库改后 → PASS:
```
$ python3 .work/10_tier_b_repair/scripts/t2s/ct_assert.py
domains 63 got {'class1': 570, 'codes': 588, 'class6': 59, 'notes': 59, 'srdy': 1}
RESULT PASS
```

## 变异测试 (retrospective 规则 5; 全在 scratch 副本 kbM = kbA 拷贝, 不在仓库)
命令: `cp -R kbA kbM; python3 (单处 str.replace); python3 .work/10_tier_b_repair/scripts/t2s/ct_assert.py <scratch>/kbM` (每例重建 kbM; 原始输出 `mut.log`).
| 变异 | 植入 | rc | 结果 | 首条 FAIL |
|---|---|---|---|---|
| M1_nonCT_line | AE STUDYID Label 改一字 | 1 | FAIL | `AE STUDYID: non-CT line changed: '- **Label:** Study Identifier' -> '- **Label:** Study Identifer'` |
| M2_wrong_shortname | AE AESEV (AESEV)→(OUT) | 1 | FAIL | `AE AESEV: short name / C-code mismatch vs Terminology xlsx: [('OUT', 'C66769')]` |
| M3_drop_ccode | AE AESEV 删 C66769 | 1 | FAIL | `AE AESEV: CT not a pure prefix add: 'C66769' -> '(AESEV)'` |
| M4_domain_code_on_nonDOMAIN | AE USUBJID CT 空→AE | 1 | FAIL | `AE USUBJID: CT not a pure prefix add: '' -> 'AE'` |
| M5_extra_note_codeless | TE (无码) 加 KB note | 1 | FAIL | `TE: KB note count 1 (has_code=False)` |
| M6_second_note_same_file | AE 第二条 KB note | 1 | FAIL | `AE: illegal insert at 547: ['', '> KB note (not in SDTMIG): C-codes after the parenthesised codelist names are` |
| M7_hyphen_delete_notes | AE AERLPRT Notes 删连字符 | 1 | FAIL | `AE AERLPRT: non-CT line changed: "- **CDISC Notes:** The investigator's opinion as to the causality of the eve` |
| M8_heading_change | AE 标题 ### AESEV→AESEVX | 1 | FAIL | `AE AESEV: non-CT line changed: '### AESEV' -> '### AESEVX'` |
| M9_wrong_DOMAIN_value | AE DOMAIN AE→AF | 1 | FAIL | `AE DOMAIN: CT not a pure prefix add: '' -> 'AF'` |

9/9 变异全部 FAIL (含主控要求的 5 种: 非 CT 行 / 错短名 / 删 C-code / 非 DOMAIN 填域代码 / 多加 KB note; 另加删连字符 / 改标题 / DOMAIN 值错 / 同文件第二条 note).

## 其他闸
- `python3 tools/check_links.py` → `broken relative links: 18668 (live docs: 42)` (不升).
- 改动集 ⊆ CT 行 + note 行 + SRDY 白名单 (断言已证); assumptions/examples 及 domains 以外文件未碰.
- push 时提醒 sdtm-rag: spec.md `Controlled Terms` 字段格式由 `C66742` 变为 `(NY) C66742`, DOMAIN 变量 CT 由空变为域代码.
- Rule A (auditor): 改动 630 格 + 59 note = 689 → N = min(30, max(20, ceil(0.05×689))) = 30, seed 20261126, 逐格对 PDF 渲染 CT 列.

## git diff --stat -- knowledge_base
```
 knowledge_base/domains/AE/spec.md       | 46 ++++++++++++++--------------
 knowledge_base/domains/AG/spec.md       | 28 +++++++++--------
 knowledge_base/domains/BE/spec.md       |  8 +++--
 knowledge_base/domains/BS/spec.md       | 22 ++++++++------
 knowledge_base/domains/CE/spec.md       | 22 ++++++++------
 knowledge_base/domains/CM/spec.md       | 28 +++++++++--------
 knowledge_base/domains/CO/spec.md       | 10 +++---
 knowledge_base/domains/CP/spec.md       | 44 ++++++++++++++-------------
 knowledge_base/domains/CV/spec.md       | 36 +++++++++++-----------
 knowledge_base/domains/DA/spec.md       | 16 +++++-----
 knowledge_base/domains/DD/spec.md       | 10 +++---
 knowledge_base/domains/DM/spec.md       | 16 +++++-----
 knowledge_base/domains/DS/spec.md       | 12 +++++---
 knowledge_base/domains/DV/spec.md       |  6 ++--
 knowledge_base/domains/EC/spec.md       | 32 ++++++++++---------
 knowledge_base/domains/EG/spec.md       | 36 +++++++++++-----------
 knowledge_base/domains/EX/spec.md       | 22 ++++++++------
 knowledge_base/domains/FA/spec.md       | 26 ++++++++--------
 knowledge_base/domains/FT/spec.md       | 24 ++++++++-------
 knowledge_base/domains/GF/spec.md       | 30 +++++++++---------
 knowledge_base/domains/HO/spec.md       | 18 ++++++-----
 knowledge_base/domains/IE/spec.md       | 12 +++++---
 knowledge_base/domains/IS/spec.md       | 38 ++++++++++++-----------
 knowledge_base/domains/LB/spec.md       | 54 +++++++++++++++++----------------
 knowledge_base/domains/MB/spec.md       | 38 ++++++++++++-----------
 knowledge_base/domains/MH/spec.md       | 18 ++++++-----
 knowledge_base/domains/MI/spec.md       | 36 +++++++++++-----------
 knowledge_base/domains/MK/spec.md       | 36 +++++++++++-----------
 knowledge_base/domains/ML/spec.md       | 16 +++++-----
 knowledge_base/domains/MS/spec.md       | 48 +++++++++++++++--------------
 knowledge_base/domains/NV/spec.md       | 34 +++++++++++----------
 knowledge_base/domains/OE/spec.md       | 42 +++++++++++++------------
 knowledge_base/domains/OI/spec.md       |  8 +++--
 knowledge_base/domains/PC/spec.md       | 22 ++++++++------
 knowledge_base/domains/PE/spec.md       | 22 ++++++++------
 knowledge_base/domains/PP/spec.md       | 20 ++++++------
 knowledge_base/domains/PR/spec.md       | 32 ++++++++++---------
 knowledge_base/domains/QS/spec.md       | 22 ++++++++------
 knowledge_base/domains/RE/spec.md       | 36 +++++++++++-----------
 knowledge_base/domains/RELREC/spec.md   |  6 ++--
 knowledge_base/domains/RELSPEC/spec.md  |  4 ++-
 knowledge_base/domains/RELSUB/spec.md   |  4 ++-
 knowledge_base/domains/RP/spec.md       | 22 ++++++++------
 knowledge_base/domains/RS/spec.md       | 38 ++++++++++++-----------
 knowledge_base/domains/SC/spec.md       | 16 +++++-----
 knowledge_base/domains/SE/spec.md       |  6 ++--
 knowledge_base/domains/SM/spec.md       |  2 +-
 knowledge_base/domains/SR/spec.md       | 32 ++++++++++---------
 knowledge_base/domains/SS/spec.md       | 16 +++++-----
 knowledge_base/domains/SU/spec.md       | 28 +++++++++--------
 knowledge_base/domains/SUPPQUAL/spec.md |  6 ++--
 knowledge_base/domains/SV/spec.md       | 12 +++++---
 knowledge_base/domains/TA/spec.md       |  6 ++--
 knowledge_base/domains/TD/spec.md       |  2 +-
 knowledge_base/domains/TE/spec.md       |  2 +-
 knowledge_base/domains/TI/spec.md       |  6 ++--
 knowledge_base/domains/TM/spec.md       |  6 ++--
 knowledge_base/domains/TR/spec.md       | 30 +++++++++---------
 knowledge_base/domains/TS/spec.md       | 10 +++---
 knowledge_base/domains/TU/spec.md       | 32 ++++++++++---------
 knowledge_base/domains/TV/spec.md       |  2 +-
 knowledge_base/domains/UR/spec.md       | 34 +++++++++++----------
 knowledge_base/domains/VS/spec.md       | 30 +++++++++---------
 63 files changed, 748 insertions(+), 630 deletions(-)
```

## attempt 2 delta (assert hardening)
> reviewer CONDITIONAL (`evidence/checkpoints/t2_S-CT_review.md`) 两条, 只改 `scripts/t2s/ct_assert.py`, KB 未动 (`git diff --shortstat -- knowledge_base` 仍为 63 files, 748+/630-).
- **CT 行逐字节**: 去掉 `.strip()`; 类 1 要求 改前行 == `- **Controlled Terms:** ` + `; `.join(codes) 且 改后行 == `- **Controlled Terms:** ` + `; `.join(`(SHORT) Cx`) (码序同改前); 类 6 要求 改前 == `- **Controlled Terms:** ` (尾空格) 且 改后 == `- **Controlled Terms:** <域>`.
- **范围检查**: 遍历 KB_ROOT 全部文件 (剔 gitignored, 如 hook 写的 `knowledge_base/.omc/`), `git hash-object` 对 `git ls-tree -r HEAD knowledge_base`; 新增/删除/内容不同且路径不是 `knowledge_base/domains/*/spec.md` → FAIL; KB_ROOT 为仓库时再并入 `git diff HEAD --name-only -- knowledge_base/`. KB_ROOT 须为完整 knowledge_base/ 树.
- 变异 (scratch 完整副本 kbM = `cp -R knowledge_base` 改后态; 命令 `python3 .work/10_tier_b_repair/scripts/t2s/ct_assert.py <scratch>/kbM/knowledge_base`; 原始输出 scratch `mut2.log`):

| 变异 | 植入 | rc | 首条 FAIL |
|---|---|---|---|
| P0 正对照 | 未改副本 | 0 | — (RESULT PASS) |
| R5 (reviewer) | AE AESEV CT 行尾多 1 空格 | 1 | `AE AESEV: CT line != expected prefix-added line: … '(AESEV) C66769 '` |
| R5b | AE DOMAIN `:**  AE` (双空格) | 1 | `AE DOMAIN: CT line != expected prefix-added line` |
| S1 | 改 `knowledge_base/VARIABLE_INDEX.md` (追加一行) | 1 | `scope: non-spec.md file differs from HEAD: knowledge_base/VARIABLE_INDEX.md` |
| S2 | 新建 `knowledge_base/domains/AE/new.md` | 1 | `scope: non-spec.md file differs from HEAD: knowledge_base/domains/AE/new.md` |
| M2 复测 | AE AESEV (AESEV)→(OUT) | 1 | `short name / C-code mismatch vs Terminology xlsx` |

- 正式复跑 (仓库):
```
$ python3 .work/10_tier_b_repair/scripts/t2s/ct_assert.py
domains 63 got {'class1': 570, 'codes': 588, 'class6': 59, 'notes': 59, 'srdy': 1}
RESULT PASS
```
- `python3 tools/check_links.py` → live docs 42.
