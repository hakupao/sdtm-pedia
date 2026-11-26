# T2 B-RS reviewer

## attempt 1 (审 writer attempt 1+2 终态; oh-my-claudecode:code-reviewer / opus)

**verdict: CONDITIONAL** (阻断项仅 C-1; 其余全部通过)

- 审核对象 md5: RS/assumptions.md `4976b5443c133bec34b530209fe57362` (128 行), RS/examples.md `d48849808842f843e75d6d1b1e757ab4`, RS/spec.md 未动 `7ec990f0654540174bcbd2f8384f206a`; FT/QS 未动 (git status 无改动).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-RS_reviewer/`
- 节页范围: p329-339 (writer O20 结论复核一致; p329 前半 QS 表尾, p339 下半 §6.3.10 SC).

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-RS_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; KB tables 4: OK 3, DIFF 1 (examples.md:57 RSSTRESC MINIMAL RESPONSE vs PDF MINIMAL REPSONSE = T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # RESULT: RED (全局, 他批页)
grep -cE 'p03(29|3[0-9])|RS/' $S/fp_regress.jsonl   # 0
# p329-339 非 EXACT 原子 52 条 verdict 与 baseline 逐条比: changed 0 (全部为 p329-332 spec 表行, 归 spec.md/O15)
python3 -I $S/cmp.py "([337,338,339],'The following assumptions are common','RS – Examples - Clinical')" knowledge_base/domains/RS/assumptions.md 86 128   # 1179/1179 词, 仅差 T-5/T-6
python3 -I $S/cmp.py "([329],'RS – Description/Overview','Variable      Variable')" knowledge_base/domains/RS/assumptions.md 3 16   # 仅 ##/bullet 格式差
python3 -I $S/cmp.py "([332,333,334],'Assumptions and examples are different','RS – Examples - Disease')" knowledge_base/domains/RS/assumptions.md 18 65   # 仅标题格式 / T-2 / T-4 / 5c 表列交错
# CC p336 段 vs KB 67-83: 仅标题格式 / T-3 / T-4
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
(cmp.py: 词级 difflib, 归一化空白/列表编号/`**`/`|`, 不归一引号 — 所以弯/直引号也逐字核过.)

### 问题表
| ref | 检查项 | 问题 | 证据 (PDF 页 + ≤25 词) |
|---|---|---|---|
| C-1 examples.md:50-53 (4 处) | PDF_TYPO 取舍规则 / 双向全扫 | **FIX**: KB 照录 PDF 笔误 `RSPLNKGRP` (×4), writer 全扫未发现也未登记. 正确值可由 PDF 自身确定: 同例表头/各行为 RSLNKGRP, spec 变量 RSLNKGRP, DR 6a "using CMLNKGRP and RSLNKGRP"; RSPLNKGRP 非任何 SDTM 变量. 与本批 T-6 (--STRNC→--STNRC) 同口径 | p335: "RSPLNKGRP = "CM1" is used to link this record in RS"; p333: "using CMLNKGRP and RSLNKGRP" |
| C-2 examples.md:12 | PDF_TYPO 登记 | **登记** (改或照录由主控定): "the determination of symptomatic determination (pleural effusion)" — KB 照录 PDF; 同例 Row 6 RSTEST = "Symptomatic Deterioration" 且例引言 "symptomatic deterioration", 可判为笔误. 建议改 "symptomatic deterioration" 并登记 T-8; 若主控从严 → 照录 + T4 | p334: "as well as the determination of symptomatic determination (pleural effusion)" |
| L-1 assumptions.md:20-22 / 67-69 | 结构 (LOW, 不阻断) | 新增 `## §6.3.9.3.x` 与既有 `## RS — … Assumptions` 连续两个同级 h2, 无正文间隔; 与 PDF (节标题 → 子标题) 层级一致性略弱. 可接受 (FA/LB 先例同为 `## §`) | p332/p336 节标题 |
| L-2 assumptions.md:84 | D6/导航 (LOW) | `## QRS Shared Assumptions` 为 KB 自写导航标题 (PDF 无标题), 纯导航不加 KB note, 保留可接受 | p337 引言无标题 |

### 删除清单 D-1..D-5 逐条确认
| # | 确认 |
|---|---|
| D-1 | examples.md:59/62/63 旧值 (2015-02-18 / FOLLOW-UP MONTH 6,8 / 2015-04-02 / 2015-06-01) 已替换; 新值对 p336 渲染图逐格一致 ✔ |
| D-2 | 原文件末 References 4 行删除, :65-68 逐字出现 (diff 显示内容 byte 相同), 位置 = Ex3 表后、CC 节前, 与 p336 顺序一致; 无指针残留 ✔ |
| D-3 | 仿写句 "The following assumptions are unique to the RS domain disease response use case:" 已删, :24 为 p332 原句; KB 全文件 grep 无残留; CC 节 :71 同型句为 PDF p336 原句, 正确保留 ✔ |
| D-4 | 指针句 "The QRS Shared Assumptions (see FT assumptions) also apply …" 已删, :86-128 为 p337-339 全文 ✔ |
| D-5 | ONCRSRR→ONCRSR ×3 (:29 ×2, :30 ×1; PDF p332 三处均 ONCRSR) ✔; "that domain"→"the domain" (:40, p333 DR 5a) ✔; CC 3a "that domain" 保留 (p336 CC 3a 原文即 "that domain") ✔; sponsor's→sponsor’s (:80, p336 弯撇号) ✔ |

### 人工逐格表
**examples.md Ex3 (p336 渲染图, 5 行 × 23 列)** — 逐格一致, 唯一差异 = T-1:
| Row | 核对结果 |
|---|---|
| 1 | ABC/RS/55555/1/CM1/OVRLRESP/Overall Response/UNSPECIFIED/PD/空/PD/空/空/INVESTIGATOR/10/SCREEN/2010-02-18/-32/空/空/BEFORE/SCREEN 一致 |
| 2 | 66666/2/CM2/BESTRESP/Best Response/UNSPECIFIED/SD/SD/INVESTIGATOR/10/SCREEN, RSDTC/RSDY 空, BEFORE/SCREEN 一致 |
| 3 | 66666/3/PR2/BESTRESP/…/MINIMAL RESPONSE/(RSSTRESC: PDF "MINIMAL REPSONSE", KB "MINIMAL RESPONSE" = T-1)/… BEFORE/SCREEN 一致 |
| 4 | 77777/4/CM3/BESTRESP/SD/SD/240/FOLLOW-UP MONTH 4/2010-04-02/520/AFTER/STUDY TREATMENT DISCONTINUATION/空/空 一致 |
| 5 | 77777/5/CM3/OVRLRESP/PD/PD/260/FOLLOW-UP MONTH 6/2010-06-01/581/AFTER/STUDY TREATMENT DISCONTINUATION/空/空 一致 |

**assumptions.md:46-48 SYMPTDTR 表 (p333 渲染图)**: 表头 RSTESTCD/RSTEST/RSCAT/RSORRES/RSSTRESC 5 列一致; 数据行 SYMPTDTR / Symptomatic Deterioration / PROTOCOL DEFINED RESPONSE CRITERIA / Increased weakness and weight loss / PD 一致. 位置 = 5c 续段之后、5d 之前, 与 PDF 一致.

Ex1 (:16) / Ex2 (:35) / CC Ex1 (:82): census OK (bbox 自比); 本批未触碰, 另对 pdftotext layout 列位置抽读 p334/p335/p339 行值一致.

### T-1..T-6 依据复核
| T | 判定 | 依据 |
|---|---|---|
| T-1 | 接受 | 同行 RSORRES = MINIMAL RESPONSE (渲染图), REPSONSE 为字母换位 |
| T-2 | 接受 | "will contained" 语法错, 单词级 (同 B-ch08 T-7 先例) |
| T-3 | 接受 | "a a" 重复词 |
| T-4 | 接受 | "derived ." / "domains ." 多余空格 (p334 DR10, p336 CC 1a) |
| T-5 | 接受 | "an resolution" 冠词错; PDF 三份 QRS 副本 (p322/p327/p338) 同错, 但语法确定; KB FT/QS 副本已为 "a resolution", 一致 |
| T-6 | 接受 | PDF QRS 三份 (p323/p328/p339) 均 --STRNC; 同节 DR 11 (p334) 及 p194/p265/p349/p353 等均 --STNRC; --STRNC 非 SDTM 变量; KB FT/QS 副本已为 --STNRC |

### 双向全扫 (p329-339, 含表格原子)
- PDF→KB: p329 Description/Overview + spec 首句 (✔ 逐字); p329-332 spec 表 → spec.md (未在本批范围, fp 0 变化, 归 O15); p332 共用引言 + 6.3.9.3.1 + DR 引言 + 1-2d (✔); p333-334 DR 3-11 + 5c 表 (✔); p334-336 DR examples 叙述 + Ex1-3 表 + References (✔, 除 C-1/C-2 PDF 笔误照录); p336 6.3.9.3.2 + CC 1-3d (✔); p337-339 QRS 引言 + 1-10 (✔ 1179 词逐字, 除 T-5/T-6); p339 CC Examples 引言 + Ex1 + 表 (✔).
- KB→PDF: assumptions.md 全 128 行、examples.md 全 95 行逐句均有出处; 无 KB 自写解释性内容, 无伪节号 (`§6.3.9.3.1/2` 为 PDF 真实节号).

### G-TB6 结构行签字
`## RS – Description/Overview` (:3), `## RS – Specification` (:14), `## §6.3.9.3.1 Disease Response Use Case` (:20), `## §6.3.9.3.2 Clinical Classifications Use Case` (:67) — 均对应 PDF 标题 ✔; SYMPTDTR 表头+分隔线 (:46-47) ✔; examples.md `### References` (:65, 移位, 原有) ✔; `## QRS Shared Assumptions` (:84, 原有导航) ✔.

### 无副作用
- KB 全仓 diff 中 RS 以外文件 (CV/DM/model05) 属他批; RS/spec.md、FT、QS 未动; 授权范围 (examples.md + assumptions.md Description/spec 首句 + M-1/M-2/M-3) 内, 无授权外改动.

### CONDITIONAL 修正清单 (writer attempt 3)
1. C-1: examples.md:50/51/52/53 `RSPLNKGRP` → `RSLNKGRP` (共 4 处), checkpoint 登记 T-7 (依据见问题表).
2. C-2: examples.md:12 "symptomatic determination (pleural effusion)" → "symptomatic deterioration (pleural effusion)" 并登记 T-8; 或主控裁定照录 + T4 登记 (二选一, 必须登记).
3. 改后复跑 census (应仍 OK 3 / DIFF 1=T-1)、fp RS 回归 0、check_links 42; 回 reviewer 复审 delta.

## attempt 2 (复审 writer attempt 3 delta; oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- md5: RS/assumptions.md `4976b5443c133bec34b530209fe57362` (= attempt 1 审过, 未动); RS/examples.md `d48849808842f843e75d6d1b1e757ab4` → `6e121b076e5c37e7728492e5dc027ddf`; spec.md `7ec990f0654540174bcbd2f8384f206a` 未动; FT/QS 无改动.
- delta 隔离证明: 对当前 examples.md 逆向还原两处 (`sed -e '50,53s/RSLNKGRP = "/RSPLNKGRP = "/' -e '12s/symptomatic deterioration (pleural/symptomatic determination (pleural/'`) 后 md5 = `d48849808842f843e75d6d1b1e757ab4` (= 上轮审过版本) → 除 C-1/C-2 外终态与 attempt 1 审过的完全一致.
- C-1 ✔: `grep -c RSPLNKGRP knowledge_base/domains/RS/examples.md` = 0; :50-53 四处为 `RSLNKGRP = "CM1"/"CM2"/"PR2"/"CM3"`, 与 Ex3 表 RSLNKGRP 列值一致. T-7 登记依据 (表头 / spec / DR 6a) 成立.
- C-2 ✔: :12 "the determination of symptomatic deterioration (pleural effusion)"; 依据同例 Row 6 RSTEST "Symptomatic Deterioration" + 例引言, T-8 登记成立.
- 复跑 (scratch t2_B-RS_reviewer):
  - `table_census.py --manifest $S/manifest.json --out $S/census_after2.json` → KB tables 4: OK 3 / DIFF 1, diffs 1 (= T-1, 不变; RESULT RED 来自全局 PDF_ONLY)
  - `fp_match.py ... --regress-out $S/fp_regress2.jsonl`; `grep -cE 'p03(29|3[0-9])|RS/' $S/fp_regress2.jsonl` → 0; p329-339 52 原子 verdict 对 baseline changed 0
  - `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42
