# T2S S-TDM reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus; 含 attempt 1 delta D-5)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 5 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/{TA,TD,TM}` (7 文件, +52/-28; 含主控裁定后 D-5). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TDM_reviewer/`
  自写脚本 (不复用 writer 的): `bscan.py` (p2k: PDF 默认文本按句切→归一后在本域全部 KB 文件查; k2p: KB 逐行逐句 (跳过 Mermaid/表) 在 PDF 页范围查); 渲染 p384/385/398/401/412/413/414; layout 文本 p382-402, p410-415.
- 授权范围: 本批 diff 只落 TA/assumptions, TA/spec, TD/assumptions, TD/examples, TD/spec, TM/assumptions, TM/spec (全 ∈ kb_files; narrow 空). TA/examples、TM/examples 未动. 工作树其余 15 文件属并行批, 未计.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TDM_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB tables 19: OK 10 / UNPARSEABLE 8 / DIFF 1 (TD ex:167 表头 TDTGTPAI vs PDF TDTGPAI = TD T-4); cells 1313, diffs 1; 本批页 PDF_ONLY 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # RED; 71 regress, 不在 expected 的 4 条全为 p79 (他批); 本批页仅 ig34_p0396_a009 (已在 expected, ATOM_ERR)
python3 -I $S/bscan.py p2k 382 402 knowledge_base/domains/TA/*.md ; python3 -I $S/bscan.py k2p 382 402 knowledge_base/domains/TA/assumptions.md knowledge_base/domains/TA/examples.md
python3 -I $S/bscan.py p2k 410 414 knowledge_base/domains/TD/*.md ; python3 -I $S/bscan.py k2p 410 414 knowledge_base/domains/TD/assumptions.md knowledge_base/domains/TD/examples.md
python3 -I $S/bscan.py p2k 415 415 knowledge_base/domains/TM/*.md ; python3 -I $S/bscan.py k2p 415 415 knowledge_base/domains/TM/assumptions.md knowledge_base/domains/TM/examples.md
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
- fp 定点: ig34_p0411_a011 (asm1 补句) EQUIVALENT→TD/assumptions; p0411_a012 EXACT→TD/assumptions. 脚注原子 p0385_a009/p0411_a009/p0415_a012 hit_any 指 PC/spec (glob 序), 直查: 脚注全文 `norm` 后在 TA/TD/TM spec.md 均命中.

### 页范围复核
- TA §7.1-7.2 引言 p382-384 中部; §7.2.1 = p384 下部-p402 中部 (p402 末 §7.2.2 TE 别节). 同意.
- TD §7.3.2 = p410 下部 (上部 §7.3.1.1 TV Issues) - p414; p415 首行即 §7.3.3 → hi=414 (主控已改 json). 同意.
- TM §7.3.3 = p415 上部; 下部 §7.4 别节. 同意.

### 双向全扫 — 逐页 (reviewer 自己的计数 = bscan p2k 句单元 / 未命中)
| 页 | PDF→KB | KB→PDF | 表 | 结论 |
|---|---|---|---|---|
| 382 | 31 / 2: 章/节标题粘连 (§7 无正文, §7.1 KB 自拟标题 X-4); "3 study cell" = TA T-1 (KB cells) | TA/asm 1-41 有出处 | Concept 表 r1-4 句级全命中 | 一致 |
| 383 | 41 / 1: 续表表头粘连 "Concept Definition Element…" (句本体 asm:37 命中) | 同 | Concept r5-9 (Treatments 3 bullet 单格连写, 文字逐字) | 一致 |
| 384 | 27 / 6: §7.2/§7.2.1/Desc/Spec 标题粘连 (句本体逐条直查命中) + spec 表 | asm 43-92 有出处 | spec 见下 | 一致 |
| 385 | 34 / 9: 全为 spec 表列串 + 脚注 "1In" 写法 | asm 110-136 有出处 | CT `*` 渲染 r-385 | 一致 |
| 386 | 32 / 0 | asm 126-136; ex 1-18 | — | 一致 |
| 387-388 | 27 / 1 (Example 1 标题粘连, 句本体命中) | ex Mermaid 前 D6 注 (B-TA) | FIGURE = Mermaid D6 | 一致 |
| 389 | 21 / 1 (ta.xpt 表粘连) | 一致 | 矩阵 + census ta OK | 一致 |
| 390-393 | 27 / 2 (矩阵 / ta 表粘连) | 一致 | 矩阵 Ex2/Ex3 layout 逐格; census OK | 一致 |
| 394-396 | 27 / 3 (表/标题粘连, 句本体直查命中) | 一致 | 矩阵 Ex4 + census OK | 一致 |
| 397-399 | 29 / 3 (矩阵/表粘连) | 一致 | 矩阵 Ex5/Ex6; census OK | 一致 |
| 400-401 | 18 / 3 (矩阵 + 图内 EPOCH 标签) | 一致 | 矩阵 Ex7 渲染 r-401 | 一致 |
| 402 | 27 / 2 (ta 表粘连; §7.2.2 TE 别节) | ex §7.2.1.1 一致 | census OK | 一致 |
| 410 | 25 / 23: 上部 21 句 = §7.3.1.1 TV 别节; 标题粘连 + spec 表 | TD/asm 1-9 有出处 | spec 见下 | 一致 |
| 411 | 32 / 7: spec 表列串 + 脚注 "1 In" | TD/asm 11-21 全有出处 (k2p 27/0) | — | 一致 |
| 412-414 | 37 / 5: 全为标题/td 表粘连, 句本体直查命中 | TD/ex k2p 46 单元 / 9 未命中 = 3 D6 注 + 3 粗体图题 (D6 注覆盖) | td ×3 census + 渲染 | 一致 (T-1..T-4) |
| 415 | 23 / 7: 标题/spec 表/表尾粘连 (句本体直查命中) + §7.4 别节 2 | TM/asm 11/0, TM/ex 7/0 | tm census OK | 一致 |
- TA k2p: asm 103 单元 / 11 未命中 = 全为导航 (KB 标题 :3/:74/:80/:90/:94/:98/:102/:106 + `> See …` :96/:100/:104/:108); ex 271 / 38 = 全为 B-TA 已有 `> KB note (not in SDTMIG):` 块. 无无出处正文.

### spec.md Controlled Terms 逐变量 (layout + 渲染 r-384/r-385; TD/TM layout 全列)
- **TA 10 变量**: STUDYID 空=空; DOMAIN PDF `TA`/KB 空 (U6, S-CT); ARMCD `*`=`*`; ARM `*`=`*`; TAETORD 空=空; ETCD `*`=`*`; ELEMENT `*`=`*`; TABRANCH 空; TATRANS 空; EPOCH `(EPOCH)`/C99079 (U5). `*` 4 = 4. Label/Type/Role/Core/Notes 全一致 (ARMCD Notes 跨 p384/385 拼接一致).
- **TD 9 变量**: STUDYID 空; DOMAIN `TD`/空 (U6); TDORDER 空; TDANCVAR 空; TDSTOFF/TDTGTPAI/TDMINPAI/TDMAXPAI `ISO 8601 duration` = KB; TDNUMRPT 空. `*` 0. 其余字段全一致 (TDANCVAR "must be a referenced" 照录 = U-2).
- **TM 5 变量**: STUDYID 空; DOMAIN `TM`/空 (U6); MIDSTYPE 空; TMDEF 空; TMRPT `(NY)`/C66742 (U5). `*` 0. 其余全一致.

### footnote (U2/U7) 三处
| 文件 | 位置 | 逐字 |
|---|---|---|
| TA/spec.md:96 | EPOCH 块 `---` 后, `## Cross References` 前 | = PDF p385 (¹ 上标) |
| TD/spec.md:87 | TDNUMRPT 块后, Cross References 前 | = p411 |
| TM/spec.md:51 | TMRPT 块后, Cross References 前 | = p415 |

### census_items 人工逐格 (不采信 writer)
| 表 | 方法 | 结果 |
|---|---|---|
| TA/asm:31 Concept/Definition (9×2) | bscan 句级 + layout | 9 概念格一致; 定义格逐句命中, 唯一差 "3 study cell"→KB "cells" (TA T-1 沿用); Treatments 3 bullet 在 KB 单格连写 (文字一致) |
| TA/ex:141 Ex1 矩阵 | layout p389 | 表头 3 + 3 行×3 格一致 |
| TA/ex:325 Ex2 | layout p391 | 表头 7 + 3 行×7 一致 |
| TA/ex:495 Ex3 | layout p393 | 表头 3 + 4 行×3 一致 |
| TA/ex:667 Ex4 | layout p396 | Screen/Treatment/Follow-up; A/B 各 10 格一致 |
| TA/ex:753 Ex5 | layout p397 | A/B 各 8 格一致 |
| TA/ex:835 Ex6 | layout p398 | A 10 格一致; B 8 内容格同序 (PDF 合并宽格, KB 末 2 空格补位) |
| TA/ex:976 Ex7 | 渲染 r-401 | CR: Screen / Initial Chemo + RT / Chemo + RT (non-Surgery) / Chemo / Chemo / Off Treatment Follow-up; CRS: … / Chemo + RT (Surgery) / 3-5 w Rest / Surgery / 4-6 w Rest / Chemo / Chemo / Off Treatment Follow-up — 内容同序一致 (PDF 合并格, KB 空格补位) |
| TD/ex:167 Ex3 td (C1) | 渲染 r414 | 表头 col6 PDF TDTGPAI / KB TDTGTPAI = TD T-4; r1-r3 30 格一致 |
- 另 TD Ex1 (r412) / Ex2 (r413) td 表渲染逐格一致 (30 / 20 格).

### TD Mermaid 三图 (D6 注 + 对渲染图逻辑)
| 图 | PDF (渲染) | KB Mermaid | 结论 |
|---|---|---|---|
| Ex1 p412 | ANCH1DT→Schedule 1 every 8 weeks (8..48)→Schedule 2 every 12 weeks (60..96)→Schedule 3 every 24 weeks (120,144)→"et cetera, until disease progression or death" | 同序同刻度; 子图标题加 "(weeks 8–48)" 等区间 = 由刻度推出, 不矛盾 | 一致 |
| Ex2 p413 | Period 1: ANCH1DT, Sched 1 every 8 weeks 8..56 + et cetera; Period 2: ANCH2DT, Sched 2 every 8 weeks X8 X16 X24 X32 + et cetera | 同; 刻度已改 X8-X32 | 一致 |
| Ex3 p414 | Double Blind Treatment (Standard vs. Experimental Treatment): Sched 1 every 8 weeks 8..48, Sched 2 every 12 weeks 60..144 + et cetera; Extension Treatment: ANCH2DT, Sched 3 every 12 weeks X12..X48 + et cetera | 同; 刻度已改 X12-X48 | 一致 |
- 三处 D6 注措辞 `> KB note (not in SDTMIG): the following label and Mermaid diagram are a KB rendering of the untitled PDF Example N figure (pNNN).` 合规, 覆盖粗体图题 (PDF 图无题). "ANCHnDT(anchor)" 的 "(anchor)" 属 KB 渲染注释, 在 D6 范围内.

### 重点核对项签字
| 项 | 结论 | 证据 |
|---|---|---|
| TD asm 1 补 3 句 | 逐字 = PDF p411 asm 1 ("TD has limited utility within oncology…if appropriate.") | bscan k2p 0 miss |
| D-1 删 TD 顶段 | 原顶段 = asm 1 全文改写副本 (唯一差 "in oncology" vs PDF "within"); 补全后 asm 1 逐句承载其全部信息; PDF Description 段为另一句 (已补 :5) | git diff + p410-411 layout |
| TD asm 2 "(e.g. ANCH1DT," | PDF 原样无逗号, 逐字 | p411 layout |
| TD ex 逐字改动 #16-26 | "+ 1 week" / "- 3 days" / "start of period 2 treatment" / "every 24 weeks" / Ex3 bullet 3 末句, 全部对 p412-414 layout + 渲染一致; Ex1 bullet 1 "(-3 days, +1 week)" PDF 无空格, KB 未改 (正确) | r412-414 |
| TA CT `*` 4 格 | ARMCD/ARM/ETCD/ELEMENT 渲染确认 | r-384/r-385 |
| D-5 删 `## TA-Specific Assumptions` | diff 表现为该行替换为 `## TA – Assumptions` (净效果 = 插入 + 删冗余); `grep -rni "ta-specific-assumptions\|TA-Specific" knowledge_base web/src docs tools` = 0 入站; 列表 1-12 未动 | git diff |
| TD/TM 新标题 S-2/S-5 | PDF p410/411/415 原标题 (en dash), 位置对应 | layout |

### PDF_TYPO / U 项依据
| T | 核 | 判 |
|---|---|---|
| TD T-1 "assessments.." | p412 layout 确认双句点 | 成立 |
| TD T-2 "restarted)." | p414: 句中无左括号 ("re-baselined, i.e., …") | 成立 |
| TD T-3 "( i.e.," | p414 bullet 1 确认 | 成立 (见 L-3) |
| TD T-4 TDTGPAI | p414 表头; p411 spec + Ex1/Ex2 表头 + asm 4 均 TDTGTPAI | 成立 |
| TD U-1 Ex3 bullet 3 "every 24 weeks" | 图 Sched 3 "every 12 weeks" + 表 r3 P12W 与之冲突; 但同句 "from week 96 … (week 120, week 144)" 只与 24 自洽, 整句疑沿用 Ex1 → 正确措辞不唯一 | 照录 + T4 成立 (见 L-1) |
| TD U-2 "must be a referenced" | p411 确认 | 照录成立 |
| TD U-3 Row 2 "-1 week and + 1 week" vs 表 P53D/P9W | p413 确认 | 照录成立 |

### 结构改动 / 删除 / D6 清单签字
- S-1 (`## TA – Assumptions`, 经 D-5 后单一 H2) ✓; S-2 TD 三标题 + D/S 两句 ✓; S-3 = D-1 ✓; S-4 asm 1 补全 ✓; S-5 TM 两标题 ✓; S-6 三处 D6 注 ✓.
- D-1 ✓; D-2/D-3 (旧值替换) ✓ 均回 PDF 值; D-4 CT 空→`*` ✓; D-5 ✓.
- D6-1..3 ✓ (不矛盾, 逻辑一致). TA B-TA 既有 D6 块 (ex 38 行) k2p 复核仍全在 `> KB note` 内.

### 问题表 (LOW, 不阻断)
| ref | 检查项 | 问题 | 证据 / 建议 |
|---|---|---|---|
| L-1 TD/ex:161 | U-1 | KB 由 "every 12 weeks" (与图/表一致) 改为 PDF "every 24 weeks" 照录, 读者现见文字与同例图/表矛盾 | 主控已裁 T4 维持; 建议 T4 用户裁定时附图 Sched 3 + 表 r3 P12W 证据 |
| L-2 TM/asm:3 vs :7/:11 | 排版 | 既有 `## TM — Description/Overview` em dash, 新标题 en dash, 同文件混用 | U1 归 S-TYPO 统一 |
| L-3 TD/ex:157 | 口径一致性 | "- 3 days"/"+ 1 week" 内多余空格按逐字照录, 而 "( i.e.," 括号内空格按 T-3 改正; 两者同属空白怪异, 处理不同 | 可接受 (T-3 有同页 "(i.e.," 自证); 记录 |
| L-4 TA/asm:94-108 | 导航 | 既有 `### §7.2.1 Trial Arms (TA) – Example 2` / `### §7.2.2.1 …` 交叉引用桩标题置于 Assumptions 前, "Example 2" 标题非 PDF 标题 | 非本批改动, 纯导航 (U8), 不计; 留 O 项参考 |
| L-5 TA/asm:3/:74 | X-4 | KB 自拟 §7.1/§7.2 标题与 PDF 不同 | 主控已裁规则 6 不改 |

### R2 recheck
- 本批无 `t2_recheck[]`; 全扫未发现改写丢失短语 (TD 顶段 "in oncology" 改写已随 D-1 删除, asm 1 用 PDF "within").
