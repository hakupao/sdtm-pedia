# T2S S-HOST reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 2 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/NV knowledge_base/domains/TI` → 仅 NV/assumptions.md 10+/0-; TI 0 改动 (md5 `cf4905bc…` = writer 报告的 B-TI 终版). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-HOST_reviewer/`
- 自写脚本 (不复用 writer 的 scan.py): `rv.py` (NV 框归一全等 + NV 非插入部分对 `git show HEAD:` 逐行比 + TI 双向句级), `rv2.py` (TI 逐行 KB→PDF p415-417/425-426), `atoms.py` (pdf_atoms 逐原子查 NV/TI/TV); 渲染 p285/p407/p415/p425/p426 110dpi.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-HOST_reviewer
python3 -I $S/rv.py    # NV box: 唯一差异 = KB 标题前缀 "§" (KB 惯例); "NV rest identical to HEAD: True 58 48"
python3 -I $S/rv2.py   # TI 全文件 24 内容行 KB→PDF 全 OK, 0 NOPDF; 仅 :5 also_p407 (共享句)
python3 -I $S/atoms.py # p285 a001-a005 全命中 NV; p407 a011 命中 TI+TV, a012-a015 仅 TV; p415 a026-a029 / p425 a026-a032 / p426 a001-a009 全命中 TI
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # RESULT: RED, 71 regress; 对 t2_fp_expected_regressions.jsonl 差集 4 = 全为 ig34_p0079 (别批, 非本批页/文件); 本批页 285/407/415/425/426 与 NV/TI 文件回归 0
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
- census: `pdf_ranges` 空 (本批无 Row 表, census_items 空) → 跳过, 无新增表.

### 页范围复核 (同意 writer)
- §6.3.6 = p285 上部红框 (标题 + 框); 框下 §6.3.7 起别节.
- §7.3 引言 = p407 中部 (a010-a015); 上部 §7.2 TA special.xpt + 注释, 下部 §7.3.1 TV.
- §7.4 引言 = p415 末 (a025-a029); 上部 §7.3.3 TM.
- §7.5 = p425 下部 (a026-) – p426 末; p427 首行 `8 Representing Relationships and Data` → p427 无 §7.5 (json 已更正止于 426).

### 双向全扫 — 逐页 (reviewer 自己的计数)
| 页 | 节 | PDF→KB | KB→PDF | 结论 |
|---|---|---|---|---|
| 285 | §6.3.6 MO 框 (narrow) | 5 原子 (a001 HEADING, a002 NOTE 框标题, a003-a005 SENTENCE) 全命中 NV:3-11; 渲染核: 框标题 "Domain Decommissioning Update" PDF 粗体 → KB `**…**` 一致; 3 段文字逐字 (含 "deprecate MO in a future version of the SDTMIG", "body-system based" 连字符位置) | NV:3-11 全有出处; 新插文字无非 ASCII 字符 (PDF 框内无弯引号/dash, 无 U1 问题) | 一致 |
| 285 | §6.3.7 / §6.3.7.1 | 既有 | NV 第 13 行起与 HEAD 第 3 行起逐行全等 (48 行, rv.py) | 未动 |
| 407 | §7.3 引言 (宿主核) | 6 原子: a010 标题/a012-a015 仅在 TV/assumptions.md:3-11; a011 "This section contains the Trial Design (TD) datasets that describe:" 同时命中 TI:5 与 TV:5 | TI 无任何 p407 专属内容 (rv2 仅 :5 also_p407) | **假阳成立**: a011 与 p415 a026 为逐字同句; TI:5 承载的是 §7.4 引言 (其后列表 :7-8 = p415 a027/a028, 指向 7.4.1/7.4.2). TI 不改正确 |
| 415 | §7.4 引言 | 5 原子: a026-a029 全命中 TI:5-10; a025 标题 KB `(TI, TS)` vs PDF `(TI and TS)` = O48 已登记 (规则 6) | TI:3-10 全有出处 | 一致 |
| 425 | §7.5 引言 + step 1-3 前半 | 7 原子 a026-a032 全命中 TI:38-44 | 全有出处 | 一致 |
| 426 | step 3 后半 – 12 | 9 原子 a001-a009 全命中 TI:44-53 | 全有出处 | 一致 (step 6 直引号 vs PDF 弯引号 = 既有排版, 归 S-TYPO) |
- TI 其余段 (:12-36, §7.4.1 p416-417, B-TI 终版) 一并反扫: 全有出处, 0 NOPDF.

### 授权范围 / 清单签字
- `git diff HEAD --stat` 本批文件: NV/assumptions.md 10+ (narrow, 仅 §6.3.7 标题前插入 json 写明的 §6.3.6 节), TI 0. 其余工作树改动 (FA/SR/TA/TD/TM/TR) 属并行批, 未计.
- 结构行签字: NV:3 `## §6.3.6 Morphology (MO)` = PDF a001 标题 (加 § 前缀, 同 :13 `## §6.3.7` 先例); NV:5 `**Domain Decommissioning Update**` = PDF a002 框标题 (粗体照 PDF, 不新建锚点). 均有出处.
- intros[0] (§6.3.6 → NV 顶部, §6.3.7 前, U3/O31): 位置正确, 逐字. gaps / footnote / footnote_moves: 空 (本批无 spec.md).
- 删除清单 / 结构改动清单 / D6 清单: writer 均报 "无", 核实 diff 0 删除行, 无 KB 自写解释 → 签字同意.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 | 范围外 | writer F-1 成立: `chapters/ch10_appendices.md` 也有 MO 退役框文字, 其中一处写 "deprecate MO in SDTMIG v3.4", 与 p285 "deprecate MO in a future version of the SDTMIG" 不同; 需对 §10 原页定性 | p285 框第 1 段; 交 S-CH 批, 本批不碰 |
| L-2 | 观察 | fp_match 全局新增回归 4 条 (ig34_p0079_*) 不在预期清单, 属并行别批 | 非本批页/文件; 提醒主控在对应批核 |

### 结论
NV narrow diff 仅为 §6.3.6 MO 框, 逐字一致, §6.3.7 及其后 0 改动; TI §7.3 归属为共享句假阳 (不改正确); §7.4 引言与 §7.5 双向全扫 0 缺 0 无出处. PASS.
