# T2S 脚本批 S-CT — Auditor a2 (Rule A 独立抽检, 写入后终态)

> 2026-11-26, oh-my-claudecode:verifier (opus), 角色 auditor. 先独立判 (§1-§5), 判完才读 writer/reviewer 报告 (§6). 只读 KB; 未 stash/checkout/reset/commit.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CT_auditor/` (sample.py / samples.json / find.py / crop2.py / c_<页>_<变量>_{h,r}.png / xl.py / mut/). xlsx/PDF 内容不入证据.

## 结论: **PASS** — 30/30 样本一致, 独有信息丢失 0, 忠实度错 0

## 1. 总体与抽样 (脚本适配: 总体 = 全部改动单元, 自算, 不用 writer 产物)
- `sample.py`: 对 63 个 `domains/*/spec.md` 比 `git show HEAD:` 与工作树, 按 `### 变量` 归属取变化的 `Controlled Terms` 行 + `> KB note (not in SDTMIG)` 行 + SR 改动 CDISC Notes 行.
- 自算总体: multi (≥2 码) **10** / single **560** (合 570) / DOMAIN **59** / note **59** / SR **1** — 与 brief 数一致.
- 分层配额 multi 6 / single 12 / DOMAIN 6 / note 5 / SR 1 = **N 30**, `random.Random(20261126).sample` 逐层 (层序 multi→single→domain→note→sr). 复跑: `cd <scratch> && python3 sample.py`.
- 未改的 4 个 note 缺位文件 SM/TD/TE/TV: CT 行 C-code 计数 0 (应无 note) ✓; 无 DOMAIN 改动的 4 文件 RELREC/RELSPEC/RELSUB/SUPPQUAL 均无 `### DOMAIN` ✓.

## 2. 逐样本 (PDF = SDTMIG v3.4 no header footer; 渲染 150 dpi 行裁剪 `crop2.py`, 另 pdftotext -layout 对照; xlsx = SDTM Terminology 2022-09-30 sheet, 自写 XML 解析按表头名取列 `xl.py`)
| # | 层 | 域 变量 (PDF 页) | PDF CT 格 (渲染) | KB 新 CT | 顺序 | xlsx C-code→SV | 判 |
|---|---|---|---|---|---|---|---|
| 1 | multi | BS BSSPEC (197) | (SPECTYPE)(GENSMP) | (SPECTYPE) C78734; (GENSMP) C111114 | ✓ | ✓✓ | ✓ |
| 2 | multi | EG EGSTRESC (186) | (EGSTRESC)(HESTRESC)(NORMABNM) | 同序 3 码 | ✓ | ✓✓✓ | ✓ |
| 3 | multi | IS ISBDAGNT (229) | (MICROORG)(ISBDAGT) | 同序 2 码 | ✓ | ✓✓ | ✓ |
| 4 | multi | PP PPSTRESU (272) | 竖排 (PKUNIT)/(PKUWG)/(PKUWKG)/(PKUDMG)/(PKUDUG) | 同序 5 码 | ✓ | ✓×5 | ✓ |
| 5 | multi | RELSPEC SPEC (439) | (SPECTYPE)(GENSMP) | 同序 2 码 | ✓ | ✓✓ | ✓ |
| 6 | multi | RS RSCAT (330) | (ONCRSCAT)(CCCAT) | 同序 2 码 | ✓ | ✓✓ | ✓ |
| 7 | single | DA DASTRESU (181) | (UNIT) | (UNIT) C71620 | — | ✓ | ✓ |
| 8 | single | EC ECDIR (108) | (DIR) | (DIR) C99074 | — | ✓ | ✓ |
| 9 | single | LB LBSTAT (243) | (ND) | (ND) C66789 | — | ✓ | ✓ |
| 10 | single | MB MBLOC (250) | (LOC) | (LOC) C74456 | — | ✓ | ✓ |
| 11 | single | MK MKEVALID (291) | (MEDEVAL) | (MEDEVAL) C96777 | — | ✓ | ✓ |
| 12 | single | ML MLOCCUR (121) | (NY) | (NY) C66742 | — | ✓ | ✓ |
| 13 | single | NV NVSTAT (295) | (ND) | (ND) C66789 | — | ✓ | ✓ |
| 14 | single | OE OEPORTOT (300) | (PORTOT) | (PORTOT) C99075 | — | ✓ | ✓ |
| 15 | single | RE RELOC (309) | (LOC) | (LOC) C74456 | — | ✓ | ✓ |
| 16 | single | RE RESTRESU (309) | (UNIT) | (UNIT) C71620 | — | ✓ | ✓ |
| 17 | single | VS VSBLFL (359) | (NY) | (NY) C66742 | — | ✓ | ✓ |
| 18 | single | VS VSTEST (358) | (VSTEST) | (VSTEST) C67153 | — | ✓ | ✓ |
| 19-24 | DOMAIN | DV (178) / LB (242) / MH (171) / OE (299) / SR (376) / TV (407) | DV / LB / MH / OE / SR / TV | 同 | — | n/a | ✓×6 |
| 25-29 | note | CE / EG / PR / SR / TM | — | 位置: 最后变量块 `---` → ¹脚注 → 空行 → note → 空行 → `## Cross References` (U7); 措辞属实: 该文件 CT 行含 C-code 9/16/14/13/1 处, 均为 `(SV) Cxxxx` 形 | — | 码均为 xlsx codelist 行 (NCI code) | ✓×5 |
| 30 | SR | SR SRDY (377) | 渲染可见 "sponsor- defined" (连字符后空格) | sponsor-defined | — | — | ✓ 登记 PDF_TYPO `SR T-5` (registry L270, handling = KB 写正确值, 主控裁定 c) |
- 加核 (总体内其余 4 个 multi, layout 文本): DS DSDECOD (NCOMPLT)(PROTMLST)(OTHEVENT) / EG EGTESTCD (EGTESTCD)(HETESTCD) / EG EGTEST (EGTEST)(HETEST) / PP PPORRESU 5 码竖排 — KB 同序 ✓ → multi 层 10/10 全核.
- 合计: 30/30 一致; 独有信息丢失 0; 忠实度错 0; 位置错 0.

## 3. ct_assert.py 独立运行 (先读代码: 参数 `[KB_ROOT]`, 默认仓库 knowledge_base; 对 HEAD 逐行 difflib, CT 行整行逐字节比, 码序不变, 短名=xlsx SV, note 位置/计数, SR 白名单, 全树 scope, 期望计数 570/588/59/59/1)
`python3 .work/10_tier_b_repair/scripts/t2s/ct_assert.py` → `domains 63 got {'class1': 570, 'codes': 588, 'class6': 59, 'notes': 59, 'srdy': 1}` / `RESULT PASS` (exit 0).

## 4. 变异 (scratch `mut/knowledge_base` = 仓库全树拷贝, 绝对路径传参; 每例后还原)
| 变异 | 结果 |
|---|---|
| M0 无变异 | PASS |
| M1 ML (NY)→(ND) | FAIL (short name / C-code mismatch) |
| M2 PP PPORRESU 两组 名+码 互换序 | FAIL (CT line != expected; class1 569) |
| M3 TV DOMAIN TV→TA | FAIL |
| M4 CT 行尾空格 | FAIL |
| M5 改 AE/assumptions.md | FAIL (scope) |
| 还原 | PASS |
- 注: 断言的"短名正确性"只核 xlsx 映射, 不核 PDF 格内容/顺序 (码序锁 HEAD); PDF 侧由本审 §2 渲染 + reviewer 全量 PDF 序列核兜底. 首次用相对路径传 KB_ROOT 报 `git hash-object` 128 (脚本按 `git -C REPO` 解析相对路径) — 用法限制, 非缺陷.

## 5. 其他
- `git diff HEAD --stat -- knowledge_base/` = 63 files, 748+/630-, 全 `domains/*/spec.md`.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42`.
- G-TB8: trace 有 S-CT writer (executor a1 DRYRUN, a2 DONE×2) + reviewer (a2 CONDITIONAL → PASS) subagent_done ✓.

## 6. 判后读 writer/reviewer 报告
- 与 reviewer 一致: 570/588/59/59/1, 多 codelist 顺序, note 位置, SR T-5. reviewer 的 B1 (strip)/B2 (scope) 已在现行 ct_assert 修 (本审 M4/M5 复现 FAIL). registry SR T-5 `pdf_page` 现为 377 (reviewer 记 null 已补).
- 本审样本与 reviewer 渲染样本重合 10 个 (seed 不同, 独立抽), 另 20 个为新增覆盖.
