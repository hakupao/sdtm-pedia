# T2 B-REL — writer checkpoint

## attempt 1 (writer, oh-my-claudecode:executor / opus, 2026-11-26)

- base HEAD: `718c2783996f8df787e7a536da7c393ad5fe2691` (B-ch08 已提交)
- 依据: D7 (t1_user_ack.md); PDF SDTMIG v3.4 p427-440 (pdf_pages + pdftoppm 渲染 p429/430/431/437/438/439/440 目视); 次参考 = 已审 ch08 (B-ch08 PASS)
- 节号确认: RELREC = §8.2 / §8.2.1 (p429) / §8.2.2 (p430) / §8.3 (p430) / §8.3.1 (p431); RELSUB = §8.7 (p437-439); RELSPEC = §8.8 (p439-440). 另 RELREC/assumptions 承载 §8 引言 IDVAR 段 (p427).
- 本批无 atoms / census; 方法 = 全量双向扫描 (见末节命令).

### md5 (before → after)
| file | before | after |
|---|---|---|
| RELREC/assumptions.md | 21bd618801ee2c437ed66130888e6086 | af6e9d8ac8afddb43377f0269f82b2b1 |
| RELREC/examples.md | 2f1194fb3d79333d353f8411f44e6a41 | e88209df168a0ba605e20ea7fd090a95 |
| RELREC/spec.md | 5c688de91a81beb087c36b92f3aa5b59 | db68fb45d8597e203fa7b1d22a6c593a |
| RELSUB/assumptions.md | a454baddfdf85c7ee27c6a2678935d75 | c4e130868b5dc0b06d237c141ddbcee9 |
| RELSUB/examples.md | 2388ee6888081de1fea32f7f506a0dae | ec54eaa97fc0e2885de9536e06b95204 |
| RELSUB/spec.md | f6ffa91cd5e115ff45974fcba37eaa87 | 45c301718c0e0cc8dea7fb05e75b888c |
| RELSPEC/assumptions.md | 1b845433aa953735b57dc9435d0cb8dd | 92e92ac4e19bd998dcfc4ef160fc591a |
| RELSPEC/examples.md | 46ce22434338f13f429fe7a7cc642e48 | c3da4faddbfa42d2dcbc8486fa050110 |
| RELSPEC/spec.md | 4e0f3e2b65d93b35cb6348c7876fe066 | fdc93ad014e0c6858a0b3b4af2cf1b7a |

### 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | 9 个文件 :3 | D7 | INSERTED | H1 后加 `> Source text: SDTMIG v3.4 §… (also in chapters/ch08_relationships.md).` (RELREC/assumptions §8 (introduction), §8.2, §8.2.1, §8.3, §8.3.1; RELREC/examples §8.2.2, §8.3.1; RELREC/spec §8.2.1; RELSUB/* §8.7; RELSPEC/* §8.8) | 427-440 |
| 2 | RELREC/assumptions.md:5 | scan:p0429:8.2-para1 | REPLACED | "(relating peer records) and … (relating datasets)" → PDF 原文 "(as described in this section), and … (as described in Section 8.3, Relating Datasets)" | 429 |
| 3 | RELREC/assumptions.md:17 | D6 | INSERTED | `> KB note (not in SDTMIG):` 说明下段/列表出自 §8 引言 p427, 非 §8.2 | — |
| 4 | RELREC/assumptions.md:19 | scan:p0427:8-intro-para | REPLACED | 原只剩引导句 "The following are examples … IDVAR:" → 补全 PDF 整段 (前 4 句 "All relationships make use of …" + 引导句) | 427 |
| 5 | RELREC/assumptions.md:20 | scan:p0427:idvar-SEQ | REPLACED | --SEQ 条截断 (缺 "For example, if a subject has 25 …" 等 3 句) → PDF 全文 | 427 |
| 6 | RELREC/assumptions.md:21 | scan:p0427:idvar-REFID | REPLACED | --REFID 条截断 (缺 "such as an identifier provided in an electronic data transfer" 与 "and can be any alphanumeric strings …") → PDF 全文 | 427 |
| 7 | RELREC/assumptions.md:22 | scan:p0427:idvar-GRPID | REPLACED | 节名 "Relating Groups of Records Within a --GRPID Variable" → PDF "…Within a Domain Using the --GRPID Variable" | 427 |
| 8 | RELREC/assumptions.md:24-26 | scan:p0429:8.2.1-desc | INSERTED | 新增 `## RELREC – Description/Overview` + PDF 描述句 (原 KB 缺) | 429 |
| 9 | RELREC/assumptions.md:28-30 | scan:p0429:8.2.1-spec-title | INSERTED | 新增 `## RELREC – Specification` + spec 首句 "relrec.xpt, Related Records — Relationship. …" (CM/IS 先例) | 429 |
| 10 | RELREC/assumptions.md:40-44 | scan:p0431:reltype-combos | REPLACED | "**ONE and ONE.**" 等 3 处项首粗体 → 非粗体 (p431 渲染仅 NO / IS 粗体; 同 ch08) | 431 |
| 11 | RELREC/assumptions.md:46 | scan:p0431:because-idvar | INSERTED | 补 "Because IDVAR identifies the keys … --SEQ cannot be used. --SEQ only has meaning …" (KB 缺) | 431 |
| 12 | RELSUB/assumptions.md:5-15 | scan:p0437:desc / p0438:spec-title | INSERTED | 新增 PDF 3 标题 `## RELSUB – Description/Overview` / `– Specification` / `– Assumptions`; 补 spec 首句; 原描述句与段落移入 Description 节 (仅加标题, 文字未改) | 437-438 |
| 13 | RELSUB/examples.md:25 | scan:p0439:rows1-2 | REPLACED | "The relationships of the mother" → PDF "The relationship of the mother" | 439 |
| 14 | RELSPEC/assumptions.md:7-15 | scan:p0439:desc / spec-title | INSERTED | 新增 PDF 3 标题 + spec 首句 "relspec.xpt, Related Specimens — Relationship. …"; BE/BS 注段保持在标题前 (PDF §8.8 首段) | 439 |
| 15 | RELSPEC/assumptions.md:19 | scan:p0440:assump2 (T-7) | REPLACED | "therefore it does not" → 照录 PDF "therefore is does not" (镜像 B-ch08 review 改判: T-7 照录 + T4) | 440 |
| 16 | RELSPEC/examples.md:9 | scan:p0440:fig-title | REPLACED | KB 自写 "**Specimen Relationship Diagram:**" → PDF 图题 "**Figure. Sample Specimen Relationship**" | 440 |
| 17 | RELSPEC/examples.md:11 | D6 | INSERTED | Mermaid 前加 `> KB note (not in SDTMIG):` "KB rendering of the PDF figure …" ; Mermaid 本体未改 (逻辑与 p440 图一致: L1 SPC-001/SPC-003(Brain), L2 SPC-001-A/-B, SPC-003-A(RNA), L3 SPC-001-B-1(DNA); 边 4 条一致) | 440 |
| 18 | RELREC/spec.md, RELSUB/spec.md, RELSPEC/spec.md | scan:p0429/p0438/p0439 spec 表 | VERIFIED | 逐变量核 Order/Label/Type/Role/Core/CDISC Notes + Structure 行 = PDF (脚本对 ch08 已审表 + 渲染目视): 18/18 变量全一致; CT C-code 对应 (DOMAIN)=C66734, (RELTYPE)=C78737, (RELSUB)=C100130, (SPECTYPE)=C78734, (GENSMP)=C111114 ✓ | 429, 438, 439 |
| 19 | RELREC/examples.md 全表 4 张, RELSUB/examples.md 2 张, RELSPEC/examples.md 1 张 | scan 表格原子 | VERIFIED | 渲染逐格: relrec Ex1 6×8, Ex2 5×8, Ex3 4×8, 数据集例 2×8; dm 3×8; relsub 6×5; relspec 6×7 — 全部与 PDF 一致, 无改动 | 430, 431, 439, 440 |

### 删除清单 (D2 / 替换)
| file:line (before) | 内容 | 原因 | 保留位置 |
|---|---|---|---|
| RELREC/assumptions.md:5 (before) | "(relating peer records)" / "(relating datasets)" 两个括注 | KB 词替换改写, 恢复 PDF 原文 (行不承载其它原子) | 同行 PDF 原文 |
| RELREC/assumptions.md:15-18 (before) | IDVAR 引导句 + 3 条截断 bullet | R2 截断丢短语, 以 PDF 全文替换 | 改后 :19-22 |
| RELSPEC/examples.md:7 (before) | "**Specimen Relationship Diagram:**" | KB 自写图题, 换 PDF 图题 | 改后 :9 |
| RELSPEC/assumptions.md:9 (before) | "it" (单词) | T-7 照录 PDF | 改后 :19 |
| RELSUB/examples.md:23 (before) | "relationships" → "relationship" | VALUE_DIFF | 改后 :25 |

### PDF_TYPO 清单 (镜像 B-ch08 已登记口径)
| T | 位置 | PDF | KB | 处理 |
|---|---|---|---|---|
| T-7 (=ch08 T-7) | RELSPEC/assumptions.md:19, p440 assumption 2 | "therefore is does not" | 照录 | 照录 + T4 用户裁定 (同 ch08) |
| T-9 (=ch08 review 认可项) | RELSUB/assumptions.md:29 (item 7), p438 | 末尾无句号 | 保留句号 | KB 写正确值 (同列表其余项均有句号; ch08 同) |
| — (PDF 自相矛盾, 非 typo) | RELREC/examples.md Ex3 正文 "COMBO 1" vs 表 Row 2 "COMBO1"; RELSPEC 图 SPC-003 "(Brain)" vs relspec Row 5 "TISSUE" | — | 两处均照录 | 同 ch08 |

注: p430 Ex3 正文为弯引号 “COMBO 1”; KB 与 ch08 均为直引号, 未改 (与 ch08 保持一致; 若主控要求弯引号, 两边需同步).

### KB_AUTHORED 保留 (纯导航, 不标 D6)
- 各文件 H1 (`# RELREC — Assumptions` 等); RELREC/assumptions `## Relating Peer Records` / `## Relating Datasets` (= §8.2/§8.3 PDF 标题简写, 锚点不动); RELREC/examples `## Peer Record Examples` / `## Dataset Relationship Example` / `### Example n`; RELSUB/RELSPEC examples `## Example 1`; 表前 `**relrec.xpt**` / `**dm.xpt**` 等; `**Row 1:**` 等标签.
- spec.md: `> Class: … | Structure: …` 行、`### VAR` 字段块、`## Cross References` 段 (全库统一格式).

### 范围外发现 / 需主控决定
1. **spec.md 记法系统差异 (全库, 非本批可独改)**: (a) RELREC IDVAR 的 CT 列 PDF 为 "*", KB spec.md 格式全库把 "*" 记为空 (1171 处空值); (b) CT 列以 C-code 代替 PDF 的 "(DOMAIN)" 等 codelist 名 (映射已核正确); (c) spec 表脚注 ¹ "In this column, an asterisk (*) …" 三个 spec.md 均无 — 全库 spec.md 均无此脚注 (无先例). 按 O15 (spec 首句/脚注全域扫描) 归口, 本批未改.
2. **RELREC/assumptions 结构**: §8.2 前两段位于 `## Relating Peer Records` 标题之前 (KB 原结构, 未搬动; 无 RELOCATE 授权). RELTYPE 组合段 + "Because IDVAR…" 在 PDF 属 §8.3.1 (例后), KB 放在 assumptions 的 `## Relating Datasets` 下 (内容全, 位置跨文件). 是否重排由主控定.
3. **ch08 差异**: 无内容冲突. 唯一形式差: ch08 RELSPEC Mermaid 为节点内标注, 域文件为 subgraph 标注 — 两者逻辑均与 p440 图一致.
4. 本批触碰的 unparseable 表: 无 (表格均未改).

### git diff --stat (kb_files)
```
 knowledge_base/domains/RELREC/assumptions.md  | 30 ++++++++++++++++++++-------
 knowledge_base/domains/RELREC/examples.md     |  2 ++
 knowledge_base/domains/RELREC/spec.md         |  2 ++
 knowledge_base/domains/RELSPEC/assumptions.md | 12 ++++++++++-
 knowledge_base/domains/RELSPEC/examples.md    |  6 +++++-
 knowledge_base/domains/RELSPEC/spec.md        |  2 ++
 knowledge_base/domains/RELSUB/assumptions.md  | 10 +++++++++
 knowledge_base/domains/RELSUB/examples.md     |  4 +++-
 knowledge_base/domains/RELSUB/spec.md         |  2 ++
 9 files changed, 59 insertions(+), 11 deletions(-)
```

### 全扫命令 (可复跑; 脚本在 writer scratch, 逻辑如下)
- `xcheck.py`: 6 个 assumptions/examples 文件逐行切句/切格 → 归一化 (dash/引号/粗体/空白) 后查 (a) PDF p427-440 pdftotext 拼接文本, (b) ch08 :5-180 + :339-末. 结果: 未命中仅 = H1/Source 行/导航标题/D6 KB note/Mermaid 首行 + T-9 句号 (ch08 命中, PDF 无句号). 无自造句.
- `rcheck.py`: ch08 :63-180, :339-末 逐句/逐格 → 查域 9 文件. 未命中仅 = ch08 节标题、`relrec.xpt:`/`Example 1:` 标签、spec 表表头、CT 列 "(DOMAIN)"/"*"/"(RELTYPE)"/"(RELSUB)"/"(SPECTYPE)(GENSMP)" 与脚注 ¹ (见范围外 1). 无叙述句缺失.
- spec 逐变量脚本: 18/18 OK.
- `python3 tools/check_links.py | grep live` → `live docs: 42` (基线 42, 不升).

## attempt 1 续 (主控裁定后)
- (a) spec.md 记法差异 → O24 并入 O15, 本批不改. (c) 引号与 ch08 一致, 不改.
- (b) RELOCATE (同文件, dispatch notes 新条): RELREC/assumptions.md §8.2 前两段 (before :5 "The Related Records (RELREC) special-purpose dataset is used…", :7 "A relationship is defined…") 移到 `## Relating Peer Records` 标题下 (after :7, :9); 不留指针; 文字未改. 锚点先 grep 核对.
- RELTYPE 组合段 + "Because IDVAR…": 在本文件内已位于 `## Relating Datasets` 的 §8.3 两段之后 = 同文件内的 §8.3.1 相对位置 (PDF 中二者之间的 §8.3.1 Example 1 + 表 + 操作库段在 RELREC/examples.md). 跨文件搬到 examples.md 超出"同文件"授权 → 未搬, 如需请主控另裁.
- RELREC/assumptions.md md5 → ae6ed604546ffa52974ade20e82aade8 (其余 8 文件不变).
- 复跑: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → 全局 RESULT RED (他批在途, 如 p363 FA), 过滤 REL / p427-440 回归 = 0; `python3 tools/check_links.py | grep live` → live docs 42.

## attempt 1 续 2 (reviewer CONDITIONAL 修正)
- RELOCATE (同文件): RELREC/assumptions.md 的 KB note + §8 引言 IDVAR 段 + 3 bullet (before :17, :19-22) 整块移到 Source 行之后、`## Relating Peer Records` 之前 (after :5, :7-10); 正文未改, 不留指针.
- KB note 删去 ", not from §8.2" (改后: "…from the SDTMIG v3.4 §8 introduction (p427).").
- md5 RELREC/assumptions.md → 69882fb2c0d1772d33c21ca7f61dc1ee (其余 8 文件不变).
- 复跑: fp_match (同前命令, out fp_after2/fp_regress2) → 全局 RED (他批在途), REL / p427-440 回归 0; check_links live docs 42; xcheck.py RELREC/assumptions 未命中仅导航/Source/KB note.
