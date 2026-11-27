# T4 解冻轮 W1 (规格 §1: 值 / 措辞 / 排版字符) — writer checkpoint
<!-- chain: E (plans) -->
> 状态: **已写入 knowledge_base (未 commit)**, 2026-11-27, writer oh-my-claudecode:executor (opus), attempt 1. 不自评 PASS.
> 规格: `subagent_prompts/t4/t4_thaw_spec_v1.0.md` §1; 依据: `t4_u7_rowcheck.md`、`t4_user_decisions.md` §000 / A6、`t2_S-TYPO.md` "CRF 符号" 口径 A.
> 基线: HEAD 3a24a1c, KB 索引 md5 `29eaa90f82530add622432f9987e2850` (改前工作树 KB = HEAD, `git diff --stat -- knowledge_base` 为空).
> scratch: `.work/10_tier_b_repair/work/scratch/t4/W1_writer/` (gitignored; 脚本 `build_crf_plan.py` / `apply_u7.py` + `a6.tsv` / `registry_sync.py` / `reverse_check.py`, 断言原始输出 `*.txt`).

## 0. 执行顺序
1. 预检: 22 个旧串逐个 grep (文件内行号 + 全库副本), 全部与 rowcheck "精确改法" 的行号 / 处数一致, 无漏列副本 (`DOSFREQ` 3 处 = :43/:48/:50; `includes PP records with PCSEQ values` = :299/:300; `all PP records with PGRPID value` = :333/:334; 其余各 1 处或按表).
2. CRF: 看渲染页 p152 / p153 / p32 / p33 → 生成计划 (58 条) → 58 条追加进 `S-TYPO.fixed.jsonl` → `typo_plan.py --apply … --allow-repo` → `typo_assert --plan` **PASS** (此时树 = HEAD + CRF 计划).
3. U-7 21 行 + A6 2 行: `apply_u7.py` 逐处 "旧串在该行恰好 N 次" 校验后替换 (任一不符则整批不写); 共 32 处 / 15 个文件. 命令: `python3 .work/10_tier_b_repair/work/scratch/t4/W1_writer/apply_u7.py .work/10_tier_b_repair/work/scratch/t4/W1_writer/a6.tsv` → `applied 32 edits to 15 files`.
4. registry 同步 + 补登 2 行.
5. 终态断言 (见 §4).

## 1. 变更清单 (行号改前改后相同, 无增删行)

| # | kb_file:line(改后) | 行号/登记 id | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | domains/DS/examples.md:294, :298 | A1-9 / B-DS U-1 | 值 (2 格) | se ETCD `SCREEN` → `SCRN` | p165 |
| 2 | domains/PP/examples.md:16, :19 | A1-21 / B-PCPP T-7 | 值 (2 格) | PPSTRESU `H` → `h` | p273 (登记写 p271) |
| 3 | domains/PC/examples.md:284, :285 | A2-2 / B-PCPP T-8 | 值 (2 处) | `DYIDRGX_A` / `DYIDRGX_HALF` → `DY1DRGX_A` / `DY1DRGX_HALF` | p280 |
| 4 | domains/PC/examples.md:278 | A2-3 / B-PCPP T-8b | 值 | `DYDRGX_HALF` → `DY1DRGX_HALF` | p280 |
| 5 | domains/TS/assumptions.md:43 | A2-4 / B-TS T-2 | 值 | `TSPARMCD = "Dose"` → `"DOSE"` | p419 |
| 6 | domains/TS/assumptions.md:43, :48, :50 | A2-5 / B-TS T-3 | 值 (叙述 1 + 表 2) | `DOSFREQ` → `DOSFRQ` | p419 |
| 7 | domains/TS/assumptions.md:57 | A2-6 / B-TS T-4 | 值 | `"OUTMSPR"` → `"OUTMSPRI"` (同句 `TSPARM =` 未动) | p419 |
| 8 | domains/TS/assumptions.md:115 | A2-7 / B-TS T-6 | 值 | `the MAXAGE case` → `the AGEMAX case` | p425 |
| 9 | domains/SM/examples.md:7 | A2-8 / B-SM O32 | 变量名 | `SMDY is not populated` → `SMSTDY …` | p85 |
| 10 | chapters/ch02_fundamentals.md:176 | A2-11 / B-ch02 T-1 | 措辞 | `Trials Sets domain` → `Trial Sets domain` | p16 |
| 11 | domains/BS/assumptions.md:23 | A2-14 / REG BS N-1 | 变量名 | `--ORNLO, --ORNHI` → `--ORNRLO, --ORNRHI` | p198 |
| 12 | domains/PC/examples.md:299, :300 | A2-15 / S-SPC2 N-1 | 措辞 (2 处) | `includes PP records with PCSEQ values` → `PC records` | p281 |
| 13 | domains/PC/examples.md:333, :334 | A2-16 / S-SPC2 N-2 | 措辞 (2 处) | `all PP records with PGRPID value(s)` → `all PC records with PCGRPID value(s)` (审查者更正值, 非草拟 PPGRPID) | p281 |
| 14 | domains/DS/examples.md:87 | A3-2 / B-DS U-4 | 语法 | `the DS record and in the AE record` → 删 `in` | p160 |
| 15 | domains/EG/examples.md:42 | A3-5 / B-EG T-3 | 措辞 | `principal investigation` → `principal investigator` | p190 |
| 16 | domains/FA/assumptions.md:39 | A3-7 / B-FA T-4 | 语法 | `thought be related` → `thought to be related` | p362 |
| 17 | domains/FA/assumptions.md:51 | A3-8 / B-FA T-6 | 语法 | `FA may provided` → `FA may provide` | p363 |
| 18 | domains/FA/examples.md:183 | A3-9 / B-FA T-8 | 语法 | `used to populated FADTC` → `used to populate FADTC` | p372 |
| 19 | domains/NV/assumptions.md:23 | A3-14 / B-NV N-1 | 语法 | `may included` → `may include` | p285 (登记写 p294) |
| 20 | domains/NV/examples.md:63 | A3-15 / B-NV N-2 | 语法 | `links the each` → `links each` | p298 (登记写 p297) |
| 21 | chapters/ch04_general_assumptions.md:863 | A3-34 / B-ch04 N-1 | 拼写 | `foreword slash` → `forward slash` | p41 |
| 22 | domains/IS/examples.md:205, :206, :207 | A6-1 / B-IS T-6 | 排版 (U1, 3 格) | `AUREUS-EPITOPE X` → `AUREUS–EPITOPE X` (en dash, 无空格) | p239 (登记写 p241) |
| 23 | domains/TA/examples.md:351 | A6-2 / B-TA T-4 | 排版 (U1) | `5 mg - 10 mg - Placebo` → `5 mg - 10 mg – Placebo` (只改第二处) | p391 |

- 维持 B 21 行 = #1-#21; A6 = #22-#23. 合计 32 处编辑 = U-7 28 处 (落在 27 个 KB 行; TS:43 同时承载 A2-4 与 A2-5) + A6 4 处 (IS 3 + TA 1).
- 本 writer 亲自看过的渲染页: p152、p153、p32、p33、p391 (裁剪 400dpi)、p239 (裁剪 400dpi); p280 / p281 只核了文本层 (`work/pdf_pages/ig34_p0280.txt` / `ig34_p0281.txt`). 其余 PDF 页 (p165 / p273 / p419 / p425 / p85 / p16 / p198 / p160 / p190 / p362 / p363 / p372 / p285 / p298 / p41) 沿用 `t4_u7_rowcheck.md` 审查者的渲染核对, 本轮未重看.
- **未改** (按规格): 改回 A 的 5 行 (A2-12, A3-24, A3-28, A3-31, A3-32)、草拟即为 A 的各行、B-MK T-1 (代裁 Q3).
- A6 渲染核对: p391 TA 表 row 15 TABRANCH 渲染为 "5 mg - 10 / mg – Placebo" (第一处 hyphen, 第二处 en dash; bbox 第二处宽 3.9pt vs hyphen 2.3pt); p239 IS 表 3 格渲染为 "AUREUS–EPITOPE X" (en dash 无空格). 同例叙述 :199 `S. aureus-epitope X` 在 PDF 也是连字符, 未动.
- A2-16 依据复核: p281 Method C 两句原文 "all PP records with PGRPID value(s)", 同页 relrec r1/r2/r8 RDOMAIN=PC、IDVAR=PCGRPID, 节标题 "Using PCGRPID and PPSEQ" (文本层 `ig34_p0281.txt:34-48`).

## 2. CRF 符号 (U-9(a) 口径 A) — 58 处

| 文件 | KB 行 | PDF 页 | 改法 | 处数 |
|---|---|---|---|---:|
| domains/CE/examples.md | 43-46 | p152 | `( )` → ○ (CourierNew `o`, 渲染为小圆) | 18 |
| domains/CE/examples.md | 74, 77, 79, 80, 82 | p153 | `( )` → ○ (U+25CB) | 15 |
| domains/CE/examples.md | 81, 83 | p153 | `[ ]` → □ (U+25A1) | 6 |
| chapters/ch04_general_assumptions.md | 410-412 | p32 | `[ ]` → ○ (Wingdings 坏字形, 渲染为钟形图标) | 3 |
| chapters/ch04_general_assumptions.md | 427-432 | p32 | `[ ]` → ○ (CourierNew `o`) | 6 |
| chapters/ch04_general_assumptions.md | 472-476 | p33 | `[ ]` → ○ | 5 |
| chapters/ch04_general_assumptions.md | 506-510 | p33 | `[ ]` → ○ | 5 |
| **合计** | | | CE 39 + ch04 19 | **58** |

- 渲染逐个数过: p152 Nausea/Vomit/Diarrhea 各 5、Other 3 = 18; p153 ○ 2+4+3+3+3 = 15、□ 3+3 = 6; p32 3 + 6; p33 5 + 5.
- 只替换符号本身 (3 字符 → 1 字符), 后面的空格与选项文字不动; ch04 网格表的对齐填充未补 (Markdown 渲染不受影响).
- ML `[X]` / `[ ]`、FA ○、AE `[ ]`、DM Mermaid: 未动 (`git diff --stat` 无这些文件).
- 计划: `work/t2_batches/T4-THAW.typo.plan.jsonl` (58 行, 字段同 S-TYPO 计划, `fixed: true`, 列号基于 HEAD). 复跑计数:
  `python3 -c "import json,collections as C;P=[json.loads(l) for l in open('.work/10_tier_b_repair/work/t2_batches/T4-THAW.typo.plan.jsonl')];print(len(P),C.Counter((p['file'].split('/')[-2],p['pdf_page'],p['class']) for p in P))"` → `58 … ('CE',152,'crf:( )->○'): 18, ('CE',153,'crf:( )->○'): 15, ('chapters',33,…): 10, ('chapters',32,…): 9, ('CE',153,'crf:[ ]->□'): 6`
- **未运行 `typo_plan.py` 的规划模式** (读源码可知它按硬编码路径覆盖 `S-TYPO.fixed.jsonl` / `S-TYPO.residual.jsonl`; 原 7 条固定项按旧 HEAD 行号与已替换后的串定位, 推断在当前 HEAD 上不能复现 — 未实跑验证). 计划由 scratch `build_crf_plan.py` 按同一字段生成; 写入用 `typo_plan.py --apply`.
- **门禁输入改动**: `work/t2_batches/S-TYPO.fixed.jsonl` 追加 58 行 (这 58 个 CRF 位置, 渲染已核); 原 7 行逐字节不变 (`head -7 | cmp` 与改前副本一致). `typo_assert.py` 只放行固定清单里的括号→符号改动, 不追加则 CRF 必 FAIL. 未把 U-7 / A6 文字放进固定清单.
- 变异 (scratch 副本, 在 CRF 写入后、U-7 之前跑): 把 ch04:410 的 ○ 改成 □ → `typo_assert` FAIL (`touches protected position 2: '○'->'□'`). 复跑 (需在只含 CRF 改动的树上): `S=$PWD/.work/10_tier_b_repair/work/scratch/t4/W1_writer; cp -R knowledge_base $S/kbm; python3 -c "import sys;p=sys.argv[1];L=open(p).read().split('\n');L[409]=L[409].replace('○','□',1);open(p,'w').write('\n'.join(L))" $S/kbm/chapters/ch04_general_assumptions.md; python3 .work/10_tier_b_repair/scripts/t2s/typo_assert.py $S/kbm; rm -rf $S/kbm` (终态树上同命令也会因 U-7 FAIL, 需看 ch04:410 那一条).

## 3. registry 改动 (`work/t2_pdf_typo_registry.jsonl`, 270 → 272 行)

- 23 行更新 (#1-#23 对应的登记 id): `handling` → `KB 写正确值` (U-7 21 行由 `照录+T4` 改; A6 2 行原本就是 `KB 写正确值`); `kb_text_span` / `kb_value` 改为改后值; `kb_line_now` / `span_count_in_file` / `span_lines_in_file` 按改后 KB 重算; 新增字段 `t4_decision` = `U-7 B (委托代裁 2026-11-27) [行号]` 或 `U-7 A6 B (委托代裁 2026-11-27; U1 排版照 PDF) [A6-n]`.
- S-SPC2 N-2 (A2-16) `note` = "草拟候选值 PPGRPID 有误, 由 U-7 审查者按同页 relrec 更正 (t4_u7_rowcheck.md)".
- 新 span 有额外命中 (已写入 span_lines, kb_value 注明目标行): B-PCPP T-7 `| h | PLASMA | 1 | DAY 1 | 2001-03-01 |` = 4 处 (:16/:19 为改动格, :22/:25 原本就是 h); S-SPC2 N-1 `includes PC records with PCSEQ values "1"` = 6 处 (:299/:300 改动, :438-:441 原文即 PC). 无 PDF 页内唯一写法能同时覆盖两处目标.
- 新增 2 行 (batch `T4-THAW`, handling `照录`, cat `obs`): `T4 U-10④` (TR/examples.md:7 `TRTEST = "Lymph Nodes State"`, p354 叙述 vs p355 表 "Lymph Node State"; p357 Ex2 表亦为 Nodes, KB :82/:94 照录); `T4 U-10①` (model/05:29 `(TE)`, sv20 p51; 5.1.x/5.2.x 标题 "(XX)" 后缀 = S-MOD3 规则保留的检索导航, 不改 KB).
- `pdf_page` 未改 (规格 §1.4 不含; 错页见 §6).
- 复跑: `python3 -c "import json,collections as C;R=[json.loads(l) for l in open('.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl')];print(len(R),C.Counter(r['handling'] for r in R),sum('t4_decision' in r for r in R))"` → `272 Counter({'KB 写正确值': 195, '照录+T4': 75, '照录': 2}) 25`

逐行清单 (旧 span → 新 span / handling / 新 span 在文件中的次数 / 行):

| id | kb_text_span | handling | count | lines |
|---|---|---|---:|---|
| B-DS U-1 | `\| SCREEN \|` → `\| 1 \| SCRN \| Screen \| 2016-02-0` | 照录+T4 → KB 写正确值 | 2 | [294, 298] |
| B-DS U-4 | `and in the AE record was represented` → `and the AE record was represented` | 照录+T4 → KB 写正确值 | 1 | [87] |
| B-EG T-3 | `principal investigation` → `principal investigator` | 照录+T4 → KB 写正确值 | 1 | [42] |
| B-FA T-4 | `thought be related` → `thought to be related` | 照录+T4 → KB 写正确值 | 1 | [39] |
| B-FA T-6 | `FA may provided` → `FA may provide ` | 照录+T4 → KB 写正确值 | 1 | [51] |
| B-FA T-8 | `used to populated FADTC` → `used to populate FADTC` | 照录+T4 → KB 写正确值 | 1 | [183] |
| B-IS T-6 | `AUREUS-EPITOPE X` → `AUREUS–EPITOPE X` | KB 写正确值 → KB 写正确值 | 3 | [205, 206, 207] |
| B-NV N-1 | `may included` → `may include additional` | 照录+T4 → KB 写正确值 | 1 | [23] |
| B-NV N-2 | `links the each` → `links each` | 照录+T4 → KB 写正确值 | 1 | [63] |
| B-PCPP T-7 | `\| H \|` → `\| h \| PLASMA \| 1 \| DAY 1 \| 2001-03-01 \|` | 照录+T4 → KB 写正确值 | 4 | [16, 19, 22, 25] |
| B-PCPP T-8 | `DYIDRGX_A` → `all PP records with PPGRPID = "DY1DRGX_` | 照录+T4 → KB 写正确值 | 2 | [284, 285] |
| B-PCPP T-8b | `DYDRGX_HALF` → `PPGRPID = "DY1DRGX_HALF", whereas` | 照录+T4 → KB 写正确值 | 1 | [278] |
| B-SM O32 | `SMDY` → `SMSTDY is not populated` | 照录+T4 → KB 写正确值 | 1 | [7] |
| B-TA T-4 | `Randomized to 5 mg - 10 mg - Placebo` → `Randomized to 5 mg - 10 mg – Placebo` | KB 写正确值 → KB 写正确值 | 1 | [351] |
| B-TS T-2 | `TSPARMCD = "Dose"` → `TSPARMCD = "DOSE"` | 照录+T4 → KB 写正确值 | 1 | [43] |
| B-TS T-3 | `DOSFREQ` → `DOSFRQ` | 照录+T4 → KB 写正确值 | 3 | [43, 48, 50] |
| B-TS T-4 | `OUTMSPR` → `TSPARM = "OUTMSPRI"` | 照录+T4 → KB 写正确值 | 1 | [57] |
| B-TS T-6 | `MAXAGE case` → `AGEMAX case` | 照录+T4 → KB 写正确值 | 1 | [115] |
| B-ch02 T-1 | `Trials Sets` → `Trial Sets domain` | 照录+T4 → KB 写正确值 | 1 | [176] |
| B-ch04 N-1 | `foreword slash` → `forward slash` | 照录+T4 → KB 写正确值 | 1 | [863] |
| S-SPC2 N-1 | `includes PP records with PCSEQ` → `includes PC records with PCSEQ values "1"` | 照录+T4 → KB 写正确值 | 6 | [299, 300, 438, 439, 440, 441] |
| S-SPC2 N-2 | `PGRPID values` → `all PC records with PCGRPID value` | 照录+T4 → KB 写正确值 | 2 | [333, 334] |
| REG BS N-1 | `--ORNLO, --ORNHI` → `--ORNRLO, --ORNRHI` | 照录+T4 → KB 写正确值 | 1 | [23] |
| T4 U-10④ | `(新增)` → `TRTEST = "Lymph Nodes State"` | — → 照录 | 1 | [7] |
| T4 U-10① | `(新增)` → `(TE)` | — → 照录 | 1 | [29] |

命令: `python3 .work/10_tier_b_repair/work/scratch/t4/W1_writer/registry_sync.py` (改前副本 `scratch/t4/W1_writer/registry.orig.jsonl`; U-10① 的 pdf_page 随后补为 sv20 p51, 因 `t3_errata_build.py` 对 pdf_page 做减法, 不能为 null).

## 4. 断言 (命令 + 输出原文)

**4.1 `typo_assert --plan` — CRF-only 状态 PASS; 终态 FAIL (结构性, 见 4.4)**
- CRF 计划写入后、U-7/A6 之前:
  `python3 .work/10_tier_b_repair/scripts/t2s/typo_assert.py knowledge_base --plan .work/10_tier_b_repair/work/t2_batches/T4-THAW.typo.plan.jsonl`
  → `changed files 2, changed lines 30, violations 0` / `PASS`
- 终态同一命令 → `changed files 16, changed lines 61, violations 65` / `FAIL` (exit 1). 脚本只打印前 60 条; 用打印全部的 scratch 副本 (`sed 's/errs\[:60\]/errs/'`) 看全 65 条: **全部落在 U-7 / A6 的 15 个文件**, CE/examples.md 0 条; 种类只有 `tree != HEAD + plan` (15)、`registry span count changed` (23 个新 span)、`non-table char change` (27 = U-7 的字母改动). 原文 `scratch/t4/W1_writer/typo_assert_final_all.txt`.
- 补充证明 (终态 = HEAD + CRF 计划 + 恰好这 32 处): 在 KB 副本上按正向编辑列位置撤回 32 处, 临时换回改前 registry 跑门禁, 再换回并 cmp. 复跑:
  ```
  S=$PWD/.work/10_tier_b_repair/work/scratch/t4/W1_writer; REG=.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl
  python3 $S/reverse_check.py $S && cp $REG $S/reg_new.jsonl && cp $S/registry.orig.jsonl $REG
  python3 .work/10_tier_b_repair/scripts/t2s/typo_assert.py $S/kbrev --plan .work/10_tier_b_repair/work/t2_batches/T4-THAW.typo.plan.jsonl
  cp $S/reg_new.jsonl $REG; cmp $S/reg_new.jsonl $REG && echo reg-restored; rm -rf $S/kbrev
  ```
  → `reverted 32 edits in 15 files` / `changed files 2, changed lines 30, violations 0` / `PASS` / `reg-restored`.

**4.2 `ct_assert.py` — 改前改后都 FAIL (脚本相对 S-CT 提交前的 HEAD 写死期望计数)**
- `python3 .work/10_tier_b_repair/scripts/t2s/ct_assert.py`
- 改前 (干净树): `domains 63 got {'class1': 0, 'codes': 0, 'class6': 0, 'notes': 59, 'srdy': 0}`, `FAIL count class1/codes/class6/srdy` + 59 条 `KB note count 1` (输出共 65 行) → `RESULT FAIL`.
- 改后: `got` 行**完全相同** (`notes: 59` 不变); 与改前 diff 只多 16 条 `FAIL scope: non-spec.md file differs from HEAD: <本轮 16 个文件>`. 没有 spec.md 改动 (`git diff --name-only -- 'knowledge_base/domains/*/spec.md'` 为空). 原文 `ct_assert_baseline.txt` / `ct_assert_final.txt`.

**4.3 check_links**: `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (≤ 42).

**4.4 需主控决定**: 规格 §1.5 要求的 "typo_assert --plan PASS / ct_assert PASS" 在本轮终态**做不到**: `typo_assert` 只认排版闭表, U-7 的字母改动和登记 span 变化必然 FAIL; `ct_assert` 在未改动的 HEAD 上就 FAIL. 本轮按 "CRF-only PASS + 撤回 32 处后 PASS + 每条 FAIL 可对到 #1-#23" 给证据, 未改脚本、未绕过. 是否接受这一替代证明, 或另写 T4 专用断言, 由主控定. 另两项一并请主控定: (b) `S-TYPO.fixed.jsonl` 追加 58 行 (门禁输入改动); (c) CRF 计划由 scratch 脚本生成, 未走 `typo_plan.py` 规划模式.

## 5. `git diff --stat -- knowledge_base`

```
 knowledge_base/chapters/ch02_fundamentals.md       |  2 +-
 .../chapters/ch04_general_assumptions.md           | 40 +++++++++++-----------
 knowledge_base/domains/BS/assumptions.md           |  2 +-
 knowledge_base/domains/CE/examples.md              | 22 ++++++------
 knowledge_base/domains/DS/examples.md              |  6 ++--
 knowledge_base/domains/EG/examples.md              |  2 +-
 knowledge_base/domains/FA/assumptions.md           |  4 +--
 knowledge_base/domains/FA/examples.md              |  2 +-
 knowledge_base/domains/IS/examples.md              |  6 ++--
 knowledge_base/domains/NV/assumptions.md           |  2 +-
 knowledge_base/domains/NV/examples.md              |  2 +-
 knowledge_base/domains/PC/examples.md              | 14 ++++----
 knowledge_base/domains/PP/examples.md              |  4 +--
 knowledge_base/domains/SM/examples.md              |  2 +-
 knowledge_base/domains/TA/examples.md              |  2 +-
 knowledge_base/domains/TS/assumptions.md           | 10 +++---
 16 files changed, 61 insertions(+), 61 deletions(-)
```
(ch04 20 行 = CRF 19 + A3-34 1; CE 11 行 = CRF.) 非 KB: `S-TYPO.fixed.jsonl` +58, registry 25+/23−, 新文件 `T4-THAW.typo.plan.jsonl`.

## 6. 范围外发现 (未改)
1. registry `pdf_page` 错页: B-PCPP T-7 271→实为 p273; B-NV N-1 294→p285; B-NV N-2 297→p298 (以上 rowcheck §4.1 已报); **新**: B-IS T-6 241→实为 p239 (bbox `AUREUS–EPITOPE` 在 p239, p241 无此串).
2. B-PCPP T-7 basis 写 "UNIT CT C25529" 不准 (codelist 是 PKUNIT C85494; rowcheck §4.2), 未改 basis.
3. A2-6 同句 `TSPARM = "OUTMSPRI"` 用 TSPARM 表参数码 (同段 OUTMSSEC 等同), 严格应为 TSPARMCD; PDF 原样, 未登记 (rowcheck §4.4), 本轮不动.
4. U-10④: p357 Ex2 表 TRTEST 也是 "Lymph Nodes State" (KB TR/examples.md:82/:94 照录), 不一致只在 Ex1 表 (p355) 一侧; 已写进新登记行 basis.
5. (给 W3) 本轮 21 行由 `照录+T4` 改为 `KB 写正确值` 后会进入 `t3_writeback.py` 的 `reg_diff`: 它丢弃长度 < 3 的差异 token (H→h、PP→PC、补 `to`、删 `in` 等), A6 两行的新 span 已与 PDF 相同 → 部分行可能落入 `K3B_UNUSABLE` 或标签变化. 本轮未为此调 span, W3 重算时逐条列原因.
6. ch04 CRF 网格表 (:410-:510) 改符号后列宽填充不再对齐 (纯源码外观, 渲染无影响); 未补空格以免偏离计划列号.
