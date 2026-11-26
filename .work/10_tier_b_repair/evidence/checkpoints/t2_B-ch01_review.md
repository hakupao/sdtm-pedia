# T2 B-ch01 reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base `fb62af2`; 审 `git diff fb62af2 -- knowledge_base/chapters/ch01_introduction.md` (+75/-68, 改动行 83). 工作树其它批未提交改动不计入本批.
- 真值: `work/pdf_pages/ig34_p0007..0010.txt` (p6 = 目录尾, p11 首行 "2 Fundamentals of the SDTM" → chapter 1 = p7-10) + `pdftoppm -f 7 -l 10 -r 80` 渲染 (p9/p10 逐项目视).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch01_reviewer/`

### 命令与结果 (repo 根; S = 上述 scratch)
```
# (6) 独立双向全扫: PDF p7-10 正文 (去节标题, 合并 "-\n" 折行, 去 •/o/▪/编号) vs KB 正文 (去 #/Source 行, 去 "- "/"N. ")
python3 -I $S/bidir.py knowledge_base/chapters/ch01_introduction.md
  → KB->PDF misses 0; PDF->KB misses 0; FULL ORDERED EQUAL: True (归一后整章字符级逐序相等)
  变异自检: 删 "eventual" / 截 "SDTM Core Designations" → MISS 4 (脚本能抓)
# (7) 隔离 fp: git archive HEAD knowledge_base → iso_head; 同份 + 仅换 ch01 → iso_new (diff -rq 仅 ch01)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/iso_head/knowledge_base --scope all --out $S/fp_head.jsonl          # exit 0, hit_target 6140
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/iso_new/knowledge_base --scope all --out $S/fp_new.jsonl \
   --baseline $S/fp_head.jsonl --regress-out $S/fp_regress.jsonl   # exit 0 → regressions=0 new_hits=65 RESULT: GREEN (hit_target 6205)
# p7-10 全部 ig34 原子直查 ch01: norm(verbatim) in norm(ch01)
  → miss 2: ig34_p0007_a001 HEADING "1  Introduction" (KB H1 文件标题约定, 结构行) ; ig34_p0009_a024 (atom 缺逗号, 见下)
python3 tools/check_links.py | grep 'live docs'   → broken relative links: 18668 (live docs: 42)  (= 基线, 未升)
```
- census: 本批 3 张 KB 表均为 UNPARSEABLE 且已全部改为 PDF 列表 (改后 ch01 无表) → 无表可跑 census; 改为下方人工层级核.

### (1)(3) 逐句 / 顺序 / 交叉引用 / URL
- 整章归一后与 PDF 字符级逐序相等 → §1.1-§1.5 每句、顺序 (§1.3: 引导句 → 14 bullet → "A detailed list…" → Version 3.1 段) 均与 PDF 一致.
- §1.3 14 条 bullet 的 "See Section …" 全部在 (逐条核: 6.3.1 / 6.3.5 / 6.3.5.5 / 6.3.5.6 / 6.3.5.3+6.3.5.4 / 6.2.2+6.3.5.2+8.8 / 6.3.9 / 6.3.12 / 6.3.10 / 6.4); 无 See 的 4 条 (MO / Core / CT / C1) PDF 亦无.
- URL 5 处全在: p7 sdtm (§1.1:9), p8 controlled-terminology, p9 cancer.gov (§1.4 第8条), p9 sdtmig guides (:64), p10 cancer.gov (CDISC Notes).
- 其它 R2 短语: "First,"/"Next,"/"Finally,", "of this document", "and should be consulted when needed", "for a domain", "These values are taken directly from the SDTM.", "As noted in the table note", "explained further in Section 4.1.5, SDTM Core Designations", "of the SDTMIG and/or Model document", "when setting up a relationship in RELREC", "the appropriateness of using other identification variables for linking" — 全在.
- 页码行 :3 "Pages 7-10" 与 p11 起 §2 一致.

### (2) 人工层级核 (§1.4.1, p9-10 渲染: • / o / ▪ / •)
| KB 行 | 层级 (KB 缩进) | PDF 渲染 | 结果 |
|---|---|---|---|
| :74-76 Variable Name + 2 子项 | L1 / L2 | • / o ×2 | 一致 |
| :77-79 Variable Label + 2 子项 | L1 / L2 | • / o ×2 | 一致 |
| :80 Type | L1 | • (双空格归一) | 一致 |
| :81 Controlled Terms, Codelist, or Format | L1 | • (渲染有 "Codelist, or") | 一致 |
| :82 Controlled Terms | L2 | o | 一致 |
| :83 As noted in the table note… | L3 | ▪ | 一致 |
| :84-86 3 条 "The controlled terminology might…" | L4 | • ×3 (p10 顶) | 一致 |
| :87 external code system (MedDRA) | L3 (与 :83 同级) | ▪ | 一致 |
| :88 Codelist | L2 | o | 一致 |
| :89-91 3 条 hyperlinked codelist | L3 | ▪ ×3 | 一致 |
| :92 Format: "ISO 8601…" | L2 | o | 一致 |
| :93 Role | L1 | • | 一致 |
| :94-98 CDISC Notes + 4 子项 | L1 / L2 | • / o ×4 | 一致 |
| :99 Core (em-dash) | L1 | • | 一致 |
- §1.2 (:15-26): PDF 引导句 + 10 个 • → KB 引导句 + 10 个 "-", 逐字一致 (原 3 列表 D-1 删).
- §1.4 (:53-62): 编号 1-8 与 PDF 一致; guides (:64-68) 句 + 3 个 • 一致.

### (4) 删除核 (D-1..D-10)
- D-4 `### Related Implementation Guides` + 3 行表: 3 行信息 (AP 非受试者 / MD 器械 / PGx 被并入/取代) 全部由 :66-68 PDF 原文承载; PDF 无此标题; KB 内 0 入链 (仅 releases/v1.4 冻结副本含该标题, 非链接).
- D-1/D-3/D-5/D-6/D-8/D-10 全为 KB 摘要/改写, 被逐字原文覆盖; D-8 原表 "Core" 行 KB 自写展开 "(Required)/(Expected)/(Permissible)" 删除 — PDF 无, 无 PDF 内容丢失; D-2/D-7/D-9 原地替换. 结论: 无 PDF 支持内容丢失 (由 PDF->KB misses 0 兜底).
- batch notes 必补: ig34_p0009_a009 / a020 / a021, ig34_p0010_a004 隔离 fp hit_target = ch01 (已核 fp_new.jsonl).

### (5) PDF_TYPO / T4
| ref | 判定 | 依据 |
|---|---|---|
| T-1 p10_a002 "for which a codelist not yet been developed" | 照录 + T4 **接受** | 渲染与文本层同缺 "has"; 补词仅凭语法 (p49 同短语为 "has not yet been developed" 可作旁证). 建议 T4 用户裁定倾向补 "has" (同 pre-corrdinating 先例) |
| T-2 p10_a023 RELTYPE = MANY "--LNKID (and not --LNKGRP)" | 照录 + T4 **接受** | 渲染确认 PDF 原样. p31 有 "--LNKGRP … identify a group of records … many-to-one" 可推断应为 LNKGRP, 但原句属 Known Issues 中 CDISC 自述的 "implies" 推理且需互换两处 token, 非 PDF 自身可确定的单值 → T4 合理; T4 包建议附 p31 证据 |
| ig34_p0009_a024 atom 错 | **成立** | p9 渲染与文本层均为 "Controlled Terms, Codelist, or Format"; atom verbatim 缺逗号; fp_new in_pdf_page=False 佐证 |

### (6) R2 recheck
| atom | 判定 | KB 证据 |
|---|---|---|
| ig34_p0010_a009 ("Format:" 标签) | REWRITE_OK → 现已 **PRESENT** (逐字), 不需修 | ch01:92 `- Format: "ISO 8601 datetime or interval" or …` (L2, 对 p10 o 级) |

### atoms 覆盖 (10/10)
| atom | KB 行 | 结果 |
|---|---|---|
| p10_a025 | :109 | 逐字命中 |
| p9_a003..a006 | :58-61 | 逐字命中 |
| p9_a023 | :80 | 逐字命中 |
| p9_a026 | :83 | 逐字命中 (含 "As noted in the table note") |
| p10_a014 | :97 | 逐字命中 |
| p10_a016 | :99 | 逐字命中 |
| p10_a023 | :109 | 逐字命中 (T-2 照录) |

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | 全部 | 无阻断问题 | — |
| T-1 | PDF_TYPO | (LOW, 非阻断) 照录缺 "has", 待 T4 | p10 "but for which a codelist not yet been developed" |
| T-2 | PDF_TYPO | (LOW, 非阻断) MANY 行疑应为 LNKGRP, 待 T4 | p10 "RELTYPE = MANY will have an IDVAR of --LNKID (and not --LNKGRP)"; p31 "identify a group of records" |

### G-TB6 结构行签字
- 标题行: 全部未变 (diff 仅删 `### Related Implementation Guides`, D-4) — 签字.
- `Source: SDTMIG v3.4, Section 1 (Pages 7-10)` — 页范围已核 — 签字.
- 列表标记 (`- ` / `1.`-`8.` / 缩进层级) — 对渲染一致 — 签字.
- 无新增 KB note / 无自造句 (KB->PDF misses 0).

## attempt 1 续 签字 (T-1/T-2 改判 keep-correct 的 delta 复审)

**verdict: PASS (delta 签字)**

- delta (对比上轮已审版本): 仅 ch01:85 补 "has"、ch01:109 MANY 分句两变量对调; bidir.py 归一 diff 仅 `+'has '` 与 `ID↔GRP` 两处, 其余整章仍与 PDF p7-10 逐序相等.
- T-1 唯一性: 缺词处只有 "has" 合语法 (与 "might be" 时态一致; "had" 不自洽); PDF 自身 p49 同短语为 "has not yet been developed" → 可唯一确定, 接受.
- T-2 唯一性: 同段前句 LNKGRP "used to identify a group of records" + p31 定义 (LNKID → one-to-many, LNKGRP → many-to-one) 定出 ONE↔LNKID / MANY↔LNKGRP; ONE 分句与之一致故不动; MANY 分句只改主变量会得 "--LNKGRP (and not --LNKGRP)" 自相矛盾 → 两名对调是唯一自洽改法. 未见第二种合理读法, 接受. 须在登记里保留 PDF 原文与依据 (writer checkpoint 已写).
- 隔离 fp (iso_head = git archive HEAD; iso_new2 = 同份 + 仅换现 ch01):
  `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/iso_new2/knowledge_base --scope all --out $S/fp_new2.jsonl --baseline $S/fp_head.jsonl --regress-out $S/fp_regress2.jsonl`
  → regressions=0 new_hits=63 RESULT: GREEN (fp_regress2.jsonl 空). p7-10 原子直查 ch01 不命中 = p7_a001 (H1 结构行) / p9_a024 (atom 错) / p10_a002 / p10_a023 (改正后预期) — 与预期一致.
- `python3 tools/check_links.py | grep 'live docs'` → 18668 (live docs: 42), 未超过 42.
