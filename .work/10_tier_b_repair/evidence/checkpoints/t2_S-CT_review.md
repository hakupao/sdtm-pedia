# T2S 脚本批 S-CT — Reviewer (attempt 2 写入后)

> 2026-11-26, oh-my-claudecode:code-reviewer (opus), 角色 reviewer. 独立校验, 未 import writer 脚本; 只读 KB; 未 stash/checkout/reset/commit.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CT_reviewer/` (rv_check.py / rv_pdfseq.py / rv_dom.py / rv_crop.py / mut.sh / crops/ / stack*.png). xlsx/PDF 内容不入证据.

## 结论: **CONDITIONAL** (KB 内容 PASS; 断言脚本 1 处变异逃逸 + 1 处登记缺口, 均不需改 KB)

## 1. ct_assert.py / ct_apply.py 盲区分析
| # | 盲区 | 实际影响 (本次改动) | 严重度 |
|---|---|---|---|
| B1 | CT 值比较前 `.strip()` → CT 行尾/首多余空白不报 (变异 R5 逃逸) | 无: 独立 rv_check 逐字核 570 行均为 `' ' + 值` 无多余空白 | LOW (按任务口径判 CONDITIONAL) |
| B2 | 只比 `domains/*/spec.md`; 其他 KB 文件改动不报 (R11 逃逸) | 无: `git diff HEAD --stat -- knowledge_base/` 63 文件全为 spec.md | LOW |
| B3 | 短名只核 "短名→C-code 在 Terminology 唯一对应", 不核 PDF 单元格写的就是该短名/该顺序 (依赖 dryrun.jsonl 的 PDF 抽取) | 无: 独立 PDF 序列核 588/588 (见 §2) | MEDIUM (方法性) |
| B4 | `equal` 行不核: 未改 CT 行 (类 7, 1288) 若 PDF 有短名而 KB 无码, 断言不报 | 无: 独立 PDF 序列核 PDF 侧无多余 CT 短名 (仅 EG Notes 正文引用, 非 CT 列) | MEDIUM (方法性) |
| B5 | 期望计数 (570/588/59/59/1) 硬编码自 writer 产物 (自证) | 已由独立脚本复算一致 | LOW |
| B6 | note 位置只核 "下一非空行 = `## Cross References` 且其前有 `---`", 不核其前是脚注 | 无: 独立核 57 文件紧接 ¹脚注、DM 接 ²脚注、BE 接 `---` (PDF BE 表无脚注, p143-144 已核) | LOW |
| B7 | 空白行: 插入块限 [空行, note], 其余空行增删 → FAIL (R7 抓到); EOF 换行变化 → delete op FAIL | — | — |
ct_apply.py: 以 dryrun.jsonl 为唯一源, `assert cur == kb_ct` / `cur == '; '.join(codes)` 防误配; `'\n'.join` 保留 EOF; 无问题.

## 2. 独立校验 (rv_check.py: openpyxl 读 xlsx, 与 writer 的 raw-XML 解析无共享代码)
命令: `uv run --no-project --with openpyxl python -I rv_check.py` (scratch 内)
```
{'files': 63, 'domain': 59, 'ct_lines': 570, 'multi': 10, 'ins_lines': 118, 'notes': 59, 'srdy': 1}
pairs 588 distinct codes 147
DOMAIN vals ok 59 of 59 []
RESULT PASS 0
```
- 逐行 difflib vs `git show HEAD:`: 改动集 = CT 行 (U5 570 + U6 59) + note 插入 (59×[note, 空行]) + SR SRDY 1 行 (仅 `sponsor- defined`→`sponsor-defined`); 无删除/不等长替换/EOF/CRLF 变化.
- 588/588 `(SHORT) Cxxxx`: Terminology 2022-09-30 codelist 行 (Codelist Code 空) 的 CDISC Submission Value == SHORT.
- **PDF 侧独立核 (rv_pdfseq.py)**: 每域 `pdftotext -layout` 从 `<D> – Specification` 到 `In this column`/Assumptions, 取括号内且为 Terminology 合法 SV 的 token 序列, 与 KB 全部前缀短名序列比: 62/63 域完全一致; EG 差 4 个 = CDISC Notes 正文里的 "(EGTESTCD)…(HETESTCD)"/"(EGTEST)…(HETEST)" 引用 (p186 行 14/19, 非 CT 列), CT 列本身一致 → **588/588 短名与顺序 = PDF**. 非 SV 括号 token (DM/LOINC/H1N1/--TPTREF 等) 抽查均为 Notes 正文.
- **DOMAIN (rv_dom.py)**: 59/59 PDF DOMAIN 行 CT 格 = 域代码 = KB (CV 取 `CV – Specification` 之后 p287; p286 上方 `--.xpt` 通用表的 `--` 不属 CV).
- KB note: 59 个 = 含 C-code 文件; SM/TD/TE/TV 0 码 0 note; 文本全一致.

## 3. PDF 渲染逐格抽样 (21 变量, crops/ + stack0-2.png, 110 dpi; SRDY 另 300 dpi)
| 层 | 域 变量 (页) | PDF CT 格 | KB CT | 判 |
|---|---|---|---|---|
| 单 | SU SUDOSFRQ (130) | (FREQ) | (FREQ) C71113 | ✓ |
| 单 | SC SCTESTCD (340) | (SCTESTCD) | (SCTESTCD) C74559 | ✓ |
| 单 | AG AGENRTPT (94) | (STENRF) | (STENRF) C66728 | ✓ |
| 单 | CP CPLOBXFL (203) | (NY) | (NY) C66742 | ✓ |
| 单 | MK MKEVALID (291) | (MEDEVAL) | (MEDEVAL) C96777 | ✓ |
| 单 | NV NVSTAT (295) | (ND) | (ND) C66789 | ✓ |
| 单 | LB LBSTAT (243) | (ND) | (ND) C66789 | ✓ |
| 单 | ML MLOCCUR (121) | (NY) | (NY) C66742 | ✓ |
| 单 | DA DASTRESU (181) | (UNIT) | (UNIT) C71620 | ✓ |
| 单 | RE RELOC (309) | (LOC) | (LOC) C74456 | ✓ |
| 单 | OE OEPORTOT (300) | (PORTOT) | (PORTOT) C99075 | ✓ |
| 单 | MB MBLOC (250) | (LOC) | (LOC) C74456 | ✓ |
| 多 | DS DSDECOD (155) | (NCOMPLT)(PROTMLST)(OTHEVENT) | 同序 3 码 | ✓ |
| 多 | EG EGSTRESC (186) | (EGSTRESC)(HESTRESC)(NORMABNM) | 同序 3 码 | ✓ |
| 多 | PP PPORRESU (271) | (PKUNIT)/(PKUWG)/(PKUWKG)/(PKUDMG)/(PKUDUG) 竖排 | 同序 5 码 | ✓ |
| 多 | IS ISBDAGNT (229) | (MICROORG)(ISBDAGT) | 同序 2 码 | ✓ |
| 多 | RS RSCAT (330) | (ONCRSCAT)(CCCAT) | 同序 2 码 | ✓ |
| DOMAIN | SM (84) / CV (287) / TS (417) | SM / CV / TS | SM / CV / TS | ✓ ✓ ✓ |
| 白名单 | SR SRDY (377) | 渲染可见 "sponsor- defined" (连字符后有空格, 同一行; bbox 两词) | sponsor-defined | ✓ 属 PDF_TYPO T-5 (主控裁定 c) |
note 位置 (≥3 文件): AE / DM / RELSUB / BE 文件尾逐行看: ¹(DM 为 ²)脚注 → 空行 → note → 空行 → `## Cross References`; BE: `---` → note (PDF BE 表头无 ¹, p143-145 无 "In this column") ✓.
抽样 21/21 + note 4/4 一致, 0 缺陷.

## 4. 变异测试 (scratch kbBase = 仓库改后 domains 拷贝; 每例重建 kbM; `mut.sh`)
| 变异 | ct_assert 结果 | 首条 |
|---|---|---|
| R0 无变异 | PASS | — |
| R1 改错短名 (BE BELOC LOC→DIR, DIR 为合法别表) | **FAIL** | short name / C-code mismatch [('DIR','C74456')] |
| R2 不存在短名 (LOCX) | FAIL | mismatch |
| R3 多 codelist 短名互换 (DS) | FAIL | mismatch |
| R4 名+码一起换序 (DS) | FAIL | CT not a pure prefix add |
| R5 CT 行尾加空格 (AE AESEV) | **PASS (逃逸)** | — ; 独立 rv_check 报 `whitespace` FAIL |
| R6 删 note (AE) | FAIL | KB note count 0 |
| R6b note 移到脚注之上 (AE) | FAIL | KB note misplaced |
| R7 多一个空行 | FAIL | illegal insert [''] |
| R8 note 措辞微改 | FAIL | illegal insert |
| R9 短名与码间双空格 | FAIL | not a pure prefix add |
| R10 多 codelist 中一个短名改错 (PP PKUWG→PKUWKG) | FAIL | mismatch |
| R11 改非 spec 文件 (AE/assumptions.md) | PASS (范围外) | git diff 名单另证无此类改动 |

## 5. 其他
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`.
- 仓库现状 `python3 .work/10_tier_b_repair/scripts/t2s/ct_assert.py` → RESULT PASS (570/588/59/59/1).
- `git diff HEAD --stat -- knowledge_base/` = 63 files, 全 spec.md, 748+/630-.

## 修正清单 (CONDITIONAL → PASS 所需; 均不改 KB)
1. `scripts/t2s/ct_assert.py`: CT 行改为整行精确比 (如 `y == CTP + ' ' + new_expected`, 或 `yv == ' ' + yv.strip()` 且 `xv` 同口径), 让 R5 FAIL; 复跑 R5 变异留证.
2. (建议) ct_assert 加范围闸: `git diff --name-only HEAD -- knowledge_base/` ⊆ `domains/*/spec.md` (R11).
3. SR T-5 未进 `work/t2_pdf_typo_registry.jsonl` (REG 批 09:17 汇总时漏; 现有 B-SR T-1..T-4): 追加一行 (SR/spec.md SRDY, p377, "sponsor- defined"→"sponsor-defined", handling = KB 写正确值).

## attempt 2 复审 (assert hardening) — **PASS**
- 新 `ct_assert.py`: CT 行改为整行逐字节比较 (`x == CTP+' '+codes`, `y == CTP+' '+'(N) C'…`, 不 strip; DOMAIN 行 `y == CTP+' '+d`)，并且 C-code 序列不能变；范围检查对 `git ls-tree HEAD knowledge_base` 与 KB_ROOT 全树逐文件比 hash-object (含新增/删除文件)，gitignored 文件 (`.omc/`) 排除；实仓另并 `git diff --name-only`。上次盲区 B1/B2 已关闭。
- KB 未变：`diff -r` 本人审时副本 `kbBase/domains` 与仓库 `knowledge_base/domains` 无差异；`git diff HEAD --stat -- knowledge_base/` = 63 files 748+/630-。
- 变异 (scratch `kbFull` = 仓库 knowledge_base 全树拷贝，每例重建 kbM)：
| 变异 | 结果 |
|---|---|
| R0 无变异 | PASS |
| R5 CT 行尾空格 (AE AESEV) | FAIL (CT line != expected) |
| R5b 冒号后双空格 | FAIL |
| R11 改 AE/assumptions.md | FAIL (scope) |
| R11b 新增 AE/new.md | FAIL (scope) |
| R11c 删除 AE/examples.md | FAIL (scope) |
| N1 DOMAIN 值后加空格 (BE) | FAIL |
| N2 短名与码之间用 tab | FAIL |
| R1 改错短名 (BE LOC→DIR) 回归 | FAIL (mismatch) |
- 正式断言：`python3 .work/10_tier_b_repair/scripts/t2s/ct_assert.py` → `{'class1': 570, 'codes': 588, 'class6': 59, 'notes': 59, 'srdy': 1}` RESULT PASS。
- 清单 3：registry 第 270 行已有 `SR T-5` (batch S-CT)。LOW，不阻塞：该行 `pdf_page` 为 null，应为 377。
- check_links: `live docs: 42`。
