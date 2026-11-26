# S-TYPO attempt 2 — writer checkpoint (写入, 2026-11-26)

> 状态: **已写入 knowledge_base (未 commit)**; 基线 HEAD 44fb042; dry-run 报告见 `evidence/checkpoints/t2_S-TYPO_dryrun.md` (方法、字形抽查、残余分类细节都在那里, 本文件只记 a2 增量与终态数字)

## 0. 本批口径 (完整节页范围 / 双向全扫)

- **完整节页范围**: 本批不另定节页范围, 而是**逐行对各文件已复核过的 PDF 页范围**查找: B 批 `pdf_ranges` ∪ S 批 `sections` (已更正); domains/ 文件取本域目录所有文件范围的并集; B-DI 只有 `pdf_pages` [441], 按它取。202 个文件都有范围。
- **双向全扫**: 本批是排版字符脚本批, **不做**逐句双向内容全扫。KB→PDF 方向: 范围内每个 KB 行 (不含标题、代码块、KB note) 的每个排版单位都在 PDF 里定位; PDF→KB 方向不适用 (本批不补内容)。内容层面的双向全扫已由各 S/B 批完成。
- **闭表 (主控 a2 裁定后)**: `'`↔`’`/`‘`、`"`↔`“`/`”`、`-`↔`–`/`—`、`...`↔`…`; 只在结果为 – / — 时增删相邻空格。另外只在固定清单位置放行: `^1^ `→`¹` (ch08 4 处); `--`→`–` (ch04 2 处, 裁定 ②); U+2212→`-` (ch04 1 处, 裁定 ②)。
- **裁定落实**: ① B-IS T-6 / B-TA T-4 / B-MK T-1 的 span 仍不动 (属 A6, 交用户); ③ CRF 符号 (CE `( )` 33 处 + `[ ]` 6 处, 以及 ch04 / ML / DM) 全部移出计划, 不改; ④ 13 行多命中不一致留在残余清单; ⑤ ch08:78/82 粗体伪标题移出计划 (规则: 整行只有 `**…**` 的行按标题处理, 归 O60); ⑥ registry 本体不修, 34 条计数不符列在 §6; ⑦ `.omc` 跳过。
- **与裁定 ④ 的出入 (请主控确认)**: 裁定 ④ 写 "3 行需定规则本批不改", 这 3 行正是裁定 ② 批准的 ch04:1101 / 1485 / 1514。本批按 ② 执行 (已改, 改前都对渲染页核过), 残余清单里不再列这 3 行。若 ④ 才是本意, 从 `S-TYPO.fixed.jsonl` 删掉这 3 行后重跑 `--apply` 即可回退。

## 1. ch04 新增 3 处的渲染证据

| KB 位置 | 改动 | PDF 页 | 渲染所见 |
|---|---|---|---|
| ch04:1101 | `VSDTC−VSRFTDTC` → `VSDTC-VSRFTDTC` | p46 | `VSDTC-VSRFTDTC.` 中是 hyphen-minus |
| ch04:1485 | `Supplemental Qualifiers -- SUPP--` → `Supplemental Qualifiers – SUPP--` | p56 | 链接文字 `Supplemental Qualifiers – SUPP-- Datasets`; 改的是 en dash, 后面的 `SUPP--` 不动 |
| ch04:1514 | 同上 | p57 | 同上 |

两处 `--` 都在空格之间, 后接 `SUPP`, 不是变量前缀 (变量前缀 `--` 后面紧接大写字母, 断言保护它)。

## 2. 最终替换表计数 (356 处 / 154 行 / 51 个文件)

| 类 | chapters | domains | 合计 |
|---|---:|---:|---:|
| dq: 直 → 左 “ | 28 | 111 | 139 |
| dq: 直 → 右 ” | 28 | 107 | 135 |
| sq: 直 → 右 ’ | 6 | 49 | 55 |
| space: 删 em dash 两侧空格 (O59) | 4 | 6 | 10 |
| dash: hyphen → en (MK 范围值、SUPPQUAL / ch08 Scale–Cognitive) | 1 | 4 | 5 |
| ell: `...` → … | 3 | 1 | 4 |
| sup: `^1^ ` → ¹ (渲染 p429 / 432 / 438 / 439) | 4 | 0 | 4 |
| dashpair: ` -- ` → ` – ` (渲染 p56 / 57) | 2 | 0 | 2 |
| dash: em → en (ch04:194) | 1 | 0 | 1 |
| minus: U+2212 → `-` (渲染 p46) | 1 | 0 | 1 |
| 弯 → 直 | 0 | 0 | 0 |

model/ 没有改动。与 dry-run 相比: 394 − CRF 39 − ch08 伪标题 2 + ch04 3 = 356。

复跑计数: `python3 -c "import json,collections as C;P=[json.loads(l) for l in open('.work/10_tier_b_repair/work/t2_batches/S-TYPO.plan.jsonl')];print(len(P),C.Counter(p['class'] for p in P),len({(p['file'],p['line']) for p in P}),len({p['file'] for p in P}))"`

## 3. 覆盖率 (a2 终态; 合格行 = 去掉标题 / 粗体伪标题 / KB note / 代码后, 含排版单位的行)

| 指标 | chapters | domains | model |
|---|---:|---:|---:|
| ① 合格行 | 608 | 5077 | 166 |
| ② 全部单位命中且一致 | 590 (97.0%) | 4187 (82.5%) | 125 (75.3%) |
| 　其中 与 PDF 相同 / 已改 | 562 / 28 | 4069 / 118 | 125 / 0 |
| ③ 已知与 PDF 不同的行 | 32 | 133 | 0 |
| ④ 已改且整行解决 (**覆盖率 ④/③**) | 27 (84.4%) | 117 (88.0%) | — |
| ⑤ 有不一致单位的行 | 2 | 11 | 0 |
| ⑥ 有 0 命中单位的行 (导航 / 省略列 / 其它) | 13 (2 / 0 / 11) | 874 (681 / 26 / 167) | 41 (2 / 0 / 39) |
| ⑦ registry 拦下的行 | 0 | 6 | 0 |

- 另有固定清单行 7 行 (ch04 3 行、ch08 4 行), 不计入 ②④。
- 与 dry-run 比, model 合格行从 192 降到 166, 是因为粗体伪标题按裁定 ⑤ 改作标题处理。
- 0 命中**不等于**与 PDF 相同 (⑥ 其它 217 行无法判断)。fp_match / 覆盖矩阵对排版不敏感, 不作闸。

## 4. 残余清单

文件 `work/t2_batches/S-TYPO.residual.jsonl`, 共 1091 行, 只含 KB 侧信息。

| 类 | 行数 | 处置 |
|---|---:|---|
| 0 命中 (其它) | 217 | 不改 (无证据) |
| KB 自写导航 (Cross References / 链接行) | 685 | 保持 |
| 标题 + 粗体伪标题 (O60) | 144 | 只登记, 交 T4 |
| 示例表省略列 `...` | 26 | 保持 |
| 多命中不一致 | 13 | T4 人工, 主控登记 (ch04:793; ch08:38; IS ex:108; TA ex:351-357; TU assumptions:68-70) |
| registry do-not-touch | 6 | A6 交用户 (B-IS T-6 ×3, B-MK T-1 ×2, B-TA T-4 ×1) |
| KB note 内 | 1 | 保持 |

**CRF 符号: 给 T4 用户裁定的候选口径**

| KB 位置 | KB 现状 | PDF 证据 |
|---|---|---|
| CE/examples.md:43-46 | `( )` ×18 | p152: CourierNew 字母 `o`, 渲染为小圆 |
| CE/examples.md:74-83 | `( )` ×15, `[ ]` ×6 | p153: 真 ○ (U+25CB) / □ (U+25A1) |
| ch04:427-432, 472-476, 506-510 | `[ ]` ×16 | p32 / p33: CourierNew 字母 `o` |
| ch04:410-412 | `[ ]` ×3 | p32: Wingdings 坏字形 (钟形图标) |
| ML/examples.md:16-18, 27-29 | `[X]` / `[ ]` | p123: 勾选项只有 `X`, 未勾选项没有框 |
| DM/examples.md (Mermaid 代码块) | `☐` / `○` | 代码块, 不在本批范围 |
| FA/examples.md (28 行) | ○ | p367-374: Arial 中的 U+25CB, 已一致 |
| AE/assumptions.md:61/63 | `[ ]` | p139: 字面 `[ ]`, 已一致 |

- **口径 A (按渲染外观)**: 渲染成圆的都写 ○ (CE p152/153、ch04 p32/33 的 `o` 列表符号), 方框写 □ (CE p153); ch04 p32 的 Wingdings 坏字形写 ○; ML 保持 `[X]` / `[ ]`。共改 CE 39 处 + ch04 19 处。
- **口径 B (按 PDF 字符)**: 只改 PDF 字符本身就是 ○ / □ 的位置 (CE p153 共 21 处: `( )`→○ 15、`[ ]`→□ 6); 字母 `o`、坏字形、ML 都保持 KB 现写法。

## 5. 断言与变异测试 (先跑变异, 再写入)

复跑命令 (`$S` = 本 session scratch `t2s_S-TYPO_writer/`):

- `python3 .work/10_tier_b_repair/scripts/t2s/typo_mutate.py $S` → `MUTATION SUITE OK`
- `python3 .work/10_tier_b_repair/scripts/t2s/typo_plan.py --apply .work/10_tier_b_repair/work/t2_batches/S-TYPO.plan.jsonl knowledge_base --allow-repo` → `applied 356 edits to 51 files`
- `python3 .work/10_tier_b_repair/scripts/t2s/typo_assert.py` → `changed files 51, changed lines 154, violations 0` / `PASS`
- 同一命令加 `knowledge_base --plan …/S-TYPO.plan.jsonl` → PASS (工作树 == HEAD + 计划, 逐字节)
- `python3 tools/check_links.py` → `live docs: 42`

| # | 植入缺陷 | 位置 | 结果 |
|---|---|---|---|
| C0 / C1 | 正对照: HEAD + plan / 写入前仓库树 == HEAD | — | PASS / PASS |
| M1 | 字母改动 | ch04:1319 | FAIL |
| M2 | 删一个连字符 | ch01:84 | FAIL |
| M3 | 改标题 | AE/assumptions:1 | FAIL |
| M4 | `--TESTCD`→`–TESTCD` | ch04:74 | FAIL |
| M5 / M5b | 改 registry span (TA T-4 hyphen→en / FA T-1 弯→直) | TA ex:351 / FA as:9 | FAIL / FAIL |
| M6 | 表外字符 `“`→`«` | ch04:1319 | FAIL |
| M7 | 多删一个引号 | ch04:1319 | FAIL |
| M8 | 删普通词间空格 | ch01:84 | FAIL |
| M9 | 跨类替换 `'`→`“` | ch02:83 | FAIL |
| M10 | 改代码块 (Mermaid) | DM ex:117 | FAIL |
| M11 | 改 KB note | ch02:115 | FAIL |
| M12 | 改范围外文件 | terminology/core/ae.md | FAIL |
| M13 | 固定清单外 `[ ]`→`□` | ch04:472 | FAIL |
| M14 | 固定清单外 `--`→`–` (CE `--/---/--`) | CE ex:75 | FAIL |
| M15 | 改行内代码 | ch04:725 | FAIL |
| M16 / M16b | hyphen 旁删空格 / 日期 hyphen 旁加空格 | ch10:196 / ch04:106 | FAIL / FAIL |
| M17 | 插入一行 | AE as:7 | FAIL |
| M18 | 列表符 `-`→`–` | AE spec:7 | FAIL |
| M19 | CRF `( )`→○ (已移出计划) | CE ex:43 | FAIL |
| M19b | 固定清单位置写错字符 (U+2212→`–`) | ch04:1101 | FAIL |
| M20 | 固定清单上标写错数字 (¹→²) | ch08:96 | FAIL |

23 个变异全部 FAIL, 2 个正对照 PASS。M19b 首跑漏过 (固定清单替换后的结果还能被闭表再改一次), 已修: 固定清单位置替换后冻结, 不允许再改。M14 原来的位置 (ch04:1485) 已进固定清单, 换成 CE 的 `--/---/--`。

## 6. registry span_count 不符 34 条 (本批不修 registry; 改动对每个 span 的所有出现位置都加了保护)

| id | 登记 count | HEAD 实际出现次数 | 文件 |
|---|---:|---:|---|
| B-ch04 T-1 | 9 | 14 | chapters/ch04_general_assumptions.md |
| B-ch08 T-2 | 8 | 10 | chapters/ch08_relationships.md |
| B-ch08 T-9 (ch08 副本) | 40 | 1 | chapters/ch08_relationships.md |
| B-AE T-4 | 1 | 6 | domains/AE/examples.md |
| B-BE T-1 | 1 | 2 | domains/BE/examples.md |
| B-BS T-1a | 1 | 2 | domains/BS/examples.md |
| S-SPC1 CP T-16b | 6 | 13 | domains/CP/assumptions.md |
| S-SPC1 CP T-18 | 1 | 4 | domains/CP/assumptions.md |
| B-CP T-2 | 18 | 23 | domains/CP/examples.md |
| B-CP T-14 | 1 | 10 | domains/CP/examples.md |
| B-CP T-15 | 22 | 25 | domains/CP/examples.md |
| B-DM T-1 | 6 | 8 | domains/DM/examples.md |
| B-DS T-4 | 40 | 59 | domains/DS/examples.md |
| B-EX T-1 | 16 | 48 | domains/EX/examples.md |
| B-EX T-4 | 5 | 6 | domains/EX/examples.md |
| B-GF T-5 | 40 | 2 | domains/GF/examples.md |
| B-IS T-1 | 14 | 28 | domains/IS/examples.md |
| B-IS T-2 | 14 | 28 | domains/IS/examples.md |
| B-IS T-3 | 5 | 6 | domains/IS/examples.md |
| B-IS U-1 | 12 | 3 | domains/IS/examples.md |
| B-IS U-2 | 4 | 8 | domains/IS/examples.md |
| B-MB T-1 | 9 | 16 | domains/MB/examples.md |
| B-NV N-3 | 1 | 4 | domains/NV/assumptions.md |
| B-PCPP T-2 | 40 | 77 | domains/PC/examples.md |
| B-PCPP T-3 | 40 | 77 | domains/PC/examples.md |
| S-SPC2 PCPP T-11 | 7 | 8 | domains/PC/examples.md |
| B-PCPP T-5 | 3 | 1 | domains/PP/examples.md |
| B-REL T-9 (RELSUB 副本) | 12 | 1 | domains/RELSUB/assumptions.md |
| B-RS T-1 | 1 | 2 | domains/RS/examples.md |
| B-SM T-3 | 5 | 6 | domains/SM/examples.md |
| B-SR T-4 | 1 | 2 | domains/SR/spec.md |
| B-TR T-1 | 2 | 1 | domains/TR/examples.md |
| B-TR T-2 | 2 | 4 | domains/TR/examples.md |
| B-TR T-4 | 2 | 4 | domains/TR/examples.md |

## 7. diff --stat (`git diff --stat -- knowledge_base`)

```
 51 files changed, 154 insertions(+), 154 deletions(-)
 chapters: ch02 2, ch04 34, ch08 28, ch10 6
 domains: AE/assumptions 18, AE/examples 6, CE/assumptions 2, CM/assumptions 4, CM/examples 4, DD/examples 2, DM/assumptions 4,
   DS/assumptions 10, DS/examples 4, EG/examples 6, FA/examples 4, FT/assumptions 14, IS/assumptions 4, IS/examples 14,
   LB/assumptions 2, LB/examples 2, MB/assumptions 4, MH/assumptions 12, MH/examples 2, MK/examples 6, ML/examples 2,
   MS/assumptions 2, NV/examples 4, OI/assumptions 4, PP/assumptions 6, PR/assumptions 2, QS/assumptions 14, RELREC/examples 2,
   RP/assumptions 2, SE/assumptions 14, SM/assumptions 2, SM/examples 2, SU/assumptions 4, SU/examples 2, SUPPQUAL/assumptions 6,
   SUPPQUAL/examples 4, SV/assumptions 2, TA/assumptions 4, TA/examples 6, TD/assumptions 2, TE/assumptions 8, TE/examples 4,
   TI/assumptions 2, TR/assumptions 2, TU/assumptions 4, TV/assumptions 2, TV/examples 6
```

(数字为 +/- 行数之和。) 逐条改动记录在 `work/t2_batches/S-TYPO.writer.jsonl` (356 行)。

## 8. 给 Rule A auditor

按类分层抽样: dq 左 / dq 右 / sq / space / dash / ell / sup / 固定清单 3 处。dry-run 统计时, 有 15 条匹配类改动的上下文字母数字只有 12-23 个, 可以单列一层。另从 0 命中和不一致的残余里抽 10 条, 核 "不改" 是否正确。

## attempt 2 delta (assert hardening)

> 按 reviewer CONDITIONAL (`evidence/checkpoints/t2_S-TYPO_review.md`) 修门禁。KB 未改 (`git diff --stat -- knowledge_base` 仍是 51 files / 154+ / 154−)。

- `typo_assert.py` 加**引号方向断言** (不带 `--plan` 也生效): 改动引入的每个弯引号都要符合前后字符。规则: 开引号 “ ‘ 左边不是字母数字、右边不是空白; 闭引号 ” 左边不是空白、右边不是字母数字; ’ (闭引号或撇号) 左边不是空白。违反即 FAIL。
- 白名单只有 `domains/MH/assumptions.md:27` 的 2 个 “ (`History“` / `History,“`), 是 PDF p173 原文印反、按 U1 照录 (主控记入 T4 知悉项)。白名单只放行该行最多 2 个、且必须是 “。
- `typo_assert.py` 把整行只有 `**…**` 的粗体伪标题当标题保护, 改动即 FAIL (与计划端裁定 ⑤ 同口径)。
- 变异测试新增 4 个: V1 (开引号写成闭)、V4 (撇号写成 ‘)、V6 (改粗体伪标题)、V9 (闭引号写成开)。连同原 23 个一起复跑: **27/27 FAIL**, 2 个正对照 PASS。C1 已改名为 "repo knowledge_base as written (no --plan)"。

| # | 植入缺陷 | 位置 | 结果 |
|---|---|---|---|
| V1 | `“NOT DONE”` → `”NOT DONE”` | ch04:1319 | FAIL (quote direction) |
| V4 | `sponsor’s` → `sponsor‘s` | ch03:20 | FAIL (quote direction) |
| V6 | `**RELREC — Description/Overview**` 的 — → – | ch08:78 | FAIL (changed heading line) |
| V9 | `“NOT DONE”` → `“NOT DONE“` | ch04:1319 | FAIL (quote direction) |

复跑命令:
- `python3 .work/10_tier_b_repair/scripts/t2s/typo_mutate.py $S` → `MUTATION SUITE OK`
- `python3 .work/10_tier_b_repair/scripts/t2s/typo_assert.py` → PASS
- 同一命令加 `knowledge_base --plan .work/10_tier_b_repair/work/t2_batches/S-TYPO.plan.jsonl` → PASS
- `python3 tools/check_links.py` → `live docs: 42`
