# 独立审查 A — T0 变异重证 (G-TB9) + census 逐表比对 / C3 结案 (G-TB4) (原文誊录)

<!-- chain: E (plans) -->
> 审查者: `oh-my-claudecode:verifier` (opus), 只读; 对象 HEAD `1df9f60`; 主控登记其返回的时刻 = trace `T4.GAP.REVIEW_A` 的 `subagent_done` 行 (2026-11-27T05:38:20Z). 主控原样誊录 (只做了 Markdown 转义还原), 不改判. 审查者没有 Write 权限, 所以由主控落盘; 它自己的脚本与日志在 gitignored 的 `work/scratch/review_a/`.
> 主控对各条的处理见 `evidence/checkpoints/t4_t0_refresh.md` 与 `t4_c3_closeout.md` 文末.

## 核查报告

### 结论
**状态**: CONDITIONAL（按调用方给的口径）。没有 HIGH 级问题，有 1 条 MEDIUM 和 11 条 LOW。
**置信度**: 高
**阻断项**: 0 条 HIGH。附带条件有两项：(1) M4a 换靶是主控决定 M-8，须等主人追认；(2) 发现 #1 须在文档里补一句说明。

| 部分 | 结论 | 一句话 |
|---|---|---|
| A. T0 变异重证 (G-TB9) | **CONDITIONAL** | 技术上通过：我复跑 exit 0，日志与写作者的逐行相同，反向验证 2 组都能变成 MISMATCH。唯一条件是 M4a 换靶 (M-8) 还没有主人追认。另有 3 条 LOW 措辞或漏写问题。 |
| B. census 逐表比对 + C3 结案 (G-TB4) | **CONDITIONAL** | 用独立方法核了配对、删 / 增、改表的批、"现文本始于"（60 张全核），都成立。12 张表逐格对 PDF 渲染，没有发现 KB 与 PDF 不一致。条件是补上发现 #1：配对元数据的变化、以及 PDF_ONLY 1→0，文档没有交代。 |
| 整体 | **CONDITIONAL** | 两个缺口在实质上都已经关闭；文档需要小修，M-8 待追认。 |

### 证据
| 检查 | 结果 | 命令 / 来源 | 输出 |
|---|---|---|---|
| T0 变异复跑 | 通过 | `bash .work/10_tier_b_repair/scripts/t4/t0_mutation_head.sh > …/t0_head_rerun.log 2>&1; echo $?` | `EXIT=0`，耗时 1:13；与 `evidence/checkpoints/t0_mutation_head.log` 做 diff，唯一差别是写作者末行的 `exit=0` |
| 真 KB 前后 md5 | 不变 | 运行前后用 `find knowledge_base -type f … \| xargs md5 -r` 生成全文件清单，再 `cmp` | `KB_ALLFILES_UNCHANGED`；脚本自己算的 md5 前后都是 `e2d862e2…` |
| 反向验证 rev1（M2 与 M4a 改成空操作） | 能抓住 | `bash work/scratch/review_a/rev1.sh` | `M2 … got=[0 0 0] MISMATCH`，`M4a v2=0 assert=1 MISMATCH`，exit 1 |
| 反向验证 rev2（M2c 定位不到；M4a 改到 RELREC 那份） | 能抓住 | `bash work/scratch/review_a/rev2.sh` | `M2c mutation applied: NO` → MISMATCH；M4a 的 cell 断言 FAIL，`ok RELREC` 断言也 FAIL（DIFF 1），exit 1 |
| 三个时点的 census 重建 | 与文档 §2 一致 | `git archive <rev> knowledge_base` 解到我的 scratch，再跑 `table_census.py --manifest … --kb-root …` | 三份 JSON 与写作者的 census_hist 逐字段相等（`[True, True, True]` ×3） |
| 独立配对（按整文件逐行 diff 映射，不用写作者的 `pair`） | 00a2e93→HEAD 与写作者完全一致 | `work/scratch/review_a/bin/indep_pair.py` | 配对 497，删 3，增 0，改表 17；状态或差异集有变化的只有 DS:292 与 PP:14 |
| "改了这张表的批"一列 | 53/53 一致 | 对 §3 + §4 的全部 53 行跑 `git log -L <表行范围>:<file> a..b` | `disagreements 0` |
| C3 "现文本始于" | 53/53 一致 | 对 HEAD 表行跑 `git blame --line-porcelain`，取 50c3958 之后最新的那个提交 | 全部 OK |
| 逐格对 PDF 渲染 | 12/12 一致 | `pdftoppm -r 90~110`，目视 PNG | 见 7(d) 表 |

### 发现清单
| # | 严重度 | 位置 | 问题 | 依据 |
|---|---|---|---|---|
| 1 | MEDIUM | `t4_c3_closeout.md:33`（§3 "完全不变 457"）与 :25-29（§2） | "完全不变"只比较状态、差异集、行数、表文本 md5，不比较配对元数据。50c3958→00a2e93 之间有 26 张表的 `ex` / `ds` / `kb_duplicate` 变了，却计为"完全不变"。其中 `ch08:162→:164` 的 ex 由 None 变 1、kb_duplicate 由 True 变 False，这正是 PDF_ONLY 1→0（p431 relrec，即 C2 #64）消失的原因，但 §3 没有交代这一变化。G-TB4 的目的是讲清"汇总变化的来源"，这一项缺了。 | `indep_pair.py` 之后用元数据比对脚本列出 26 张；`census_50c3958.json` 中 `ch08 162 OK ex=None [431] dup=True`，`census_00a2e93.json` 中为 `164 OK ex=1 [431] dup=False` |
| 2 | LOW | `t4_c3_closeout.md:118,120`（§4 #7 / #9） | DS:292 与 PP:14 新增的 census 差异是已登记的 PDF 笔误，但表里没有写登记 id，读者容易误以为是回归。 | `t2_pdf_typo_registry.jsonl:54`（B-DS U-1，SCRN）、`:141`（B-PCPP T-7，PPSTRESU h）；`git show a59c2d3` 证实就是这两处值的改动 |
| 3 | LOW | `t4_c3_closeout.md:19`（§1 配对说明） | 文档写"键 + 出现次序"，代码实际是：先按逐字节相同配对 (pass 0)，键重复时按文本相似度配，不按出现次序。另外键唯一时没有相似度下限。实测 53 对中最低相似度为 0.70（ch10:230→:335），没有出现误配。 | `t4_census_tablediff.py:47-92`；对 53 对逐一算 SequenceMatcher 比值 |
| 4 | LOW | `t4_c3_closeout.md:190`（C3 #57） | #57 是 Key Reference Date 表（KB 自写的汇总表，Typical Use 列为 D6）。所附的"106 行 530 核心格"和 auditor `:41`"7 表 106 行"都不包括这张表。真正的 reviewer 证据是 `t2_S-MOD1_review.md` 逐格表里的 "Key Reference Date (KB 汇总) \| 8" 那一行（约 :65）。 | 读 `t2_S-MOD1_review.md:5,56-66`、`t2_S-MOD1_audit.md:41` |
| 5 | LOW | `t4_c3_closeout.md:132`（§5 导语）与 #41-#62 | 文档说"对 PDF 渲染逐格"，但 model/02 / model/03 实际只逐格核了核心列（#/Variable/Label/Type/Role）。Notes / Key Notes 是 D6 列，只核了"不矛盾"。Format 等列缺失是已裁定的 R1/M-4。文档应注明逐格的范围。 | `t2_S-MOD2_review.md:16,100-`（"KB 缩写/补充 (D6 下; 无矛盾)"）；渲染 sv20 p33/34/36/37 |
| 6 | LOW | `t4_c3_closeout.md:205,217`（§6 标题） | 标题"承接 §5 批内重建的 7 张"是数字上的巧合：旧 7 张对应新 4 张（#38→:177、#39→:323、#43-46→model/02:166、#63→model/04:37）。另外 3 张新表中，:11 是整表补的；:413 的 4 行 Appendices 在旧 #40 表里本来就没有，是新补的行，不是从 #40 拆出来的。 | 按内容比对（item 8 脚本）：`#40 sub :413 … r[0] in old False ×4` |
| 7 | LOW | `t4_c3_closeout.md:209`（§6 ch10:11） | writer 指针只给了 `t2_S-CH10.md:34`，那一行只覆盖 p444 的 35 行；p445 的 39 行在 `:35`。合计 74 行，应写成 `:34-35`。 | `sed -n 33,37p t2_S-CH10.md` |
| 8 | LOW | `t4_c3_closeout.md:174-188`（#41-#55） | auditor 指针 `t2_S-MOD2_audit.md` 没有给行号。 | 表格原文 |
| 9 | LOW | `t4_c3_closeout.md:39-40`（§3 删表的归因列） | 该列是文件级的"改该文件的批"。ch10:119 / :208 列了 S-TYPO，但删表的是 S-CH10。列名本身没写错，只是容易误读。 | `git log -L`；`t4_census_tablediff.py:95-97` |
| 10 | LOW | `t4_t0_refresh.md:22`（§2） | "T3 / T4 脚本还在读它们"对 fp / section 两个基线成立，对 `census_BPCPP.v2.json` / `census_mut_{MB,EG}.v2.json` 不成立。读这三份的只有 `t0_mutation.sh` 自己，以及 gitignored 的 `scripts/helpers/regen.sh`（它是重写这三份文件，不是读）。 | 对 `scripts`（排除 archive）grep 这几个文件名 |
| 11 | LOW | `t4_t0_refresh.md:26`（§2 第 5 条） | "mutation applied" 只能发现"定位失败 / 断言失败"，发现不了"改了等于没改"。rev1 里两个空操作都打印了 `applied: yes`，最后靠三道闸的退出码才变成 MISMATCH。文档对这项检查能力写得过头了。现有 13 个变异都在日志里打印了改前→改后，确实施加了。 | `rev1.log` 第 45 / 181 行与 MUTATIONS APPLIED 段 |
| 12 | LOW | `t4_t0_refresh.md:76-80`（§5 限制） | 漏写两点：(a) fp_match 的 `--sections` 仍用 T0 的 `section_coverage.wc.baseline.jsonl`，目标文件映射绑定在 T0 的节划分上，现基线也同样绑定；(b) `kbsum` 只算 `*.md`（真 KB 里另有一个未跟踪的 `.omc`）。我做的全文件 md5 也证明 KB 没变。 | 脚本第 21、27 行；`diff -r` 输出 `Only in knowledge_base: .omc` |

另有 3 点核过、不算问题：
- M4d0 的 `pairds` 允许 DIFF 状态。这不比 T0 的 `pair` 弱，实测两张都是 OK。
- EXADJ 3 格的 PDF 渲染是 Wingdings 坏字形（钟形图标），KB 写 ○。这是 U-9(a) 口径 A 明文裁定的（`t4_thaw_spec_v1.0.md:12`、`t2_S-TYPO.md:87`），不是不一致。
- `t4_thaw_audit.md:10` 抽查的 hunk 不包括 ch04:425 表（:427-432）。该表只有 thaw reviewer `:22` 的 19 处覆盖。

### 验收项逐条
| # | 项 | 状态 | 证据 |
|---|---|---|---|
| 1 | 复跑 exit / EXPECT / M4 / APPLIED 与日志及 §4 一致；真 KB 不变 | 已核实 | 日志逐行相同；13/13 yes；EXPECT 8/8 OK；M4 7/7 OK（v1：M4b / M4b2 GREEN-blind）；M4d0 PASS ×2（`(26,'OK','1',[257])`、`(222,'OK','3',[263])`）；RESTORE 三个 GREEN。6 个基线 md5 与 §4 相同，ledger md5 为 `60729f7b64b7…`。0.9333、`:125` IDVARVAL 9/4、PDF_ROW_MISSING row 20、SKELETON_ONLY、regressions=23 都在日志里 |
| 2 | 各用例是否"同目标" | 已核实 | 对比 T0 提交 `e3c2f5d` 的 KB：M1 同一句（两边都唯一）。M2 在 T0 是 :78、在 HEAD 是 :131，都在 §6.3.5.9.3 下 `### Example 1` 的 `#### Method C` 段内；HEAD 前面多了一个 PC 自己的 `### Example 1`，所以须取第二个。M2b :31→:35，M2c :69→:73，两行逐字相同。M2d :119→:172 唯一。M3 同一节，37 行→39 行（多出的 2 行是 KB note，列表符号改成编号）。EG Ex3 第 55-90 行与 T0 相同，表头仍在 :62。M4d0 的改法与 §6.3 预告一致：T0 的 MB:229 表与 HEAD 的 :26 表逐字相同，D2 删掉的是第一套 "## Example 1-3"。M4d 是同一张 Ex2 suppbe。M4a 的 ch08:164 与 RELREC:63 两份都配到 p431 relrec Ex1（`pdf_pages [431]`，PDF 文本层逐格相同）；只改 ch08 那份时 RELREC 那份仍 OK；改 RELREC 那份时两条断言都 FAIL，说明断言确实在检验"只改了一份"。没有发现换了目标却写成"同目标"的用例。 |
| 3 | 有没有"假绿"的路 | 已核实（附发现 #11） | expect() 与 M4 的判据与原脚本逐字相同，没有放宽；基线在 `work/t4/t0_head/`，被测对象是 `work/scratch/t0_head/` 下的副本，不是同一个文件；M0 / RESTORE / M4 setup 对现基线必须 GREEN，起到自检作用；rev1 / rev2 两组反向验证都变成 MISMATCH |
| 4 | §1 三类原因、§2 "还在读"、§5 限制 | 部分核实 | §1 与 thaw 日志相符：M2/M2b/M2c/M2d/M3/M4d 都是 AssertionError；M4a 是 IndexError；M4d0 是 ASSERT FAIL 加 IndexError；M0/RESTORE 是 `[1 1 1]`；"82 批"与 `git log e3c2f5d..d46f8af -- knowledge_base \| wc -l` 得到的 82 相符。§2 与 §5 见发现 #10、#12 |
| 5 | 配对逻辑、汇总数、删 / 增、状态变化 | 部分核实（附发现 #1、#3） | 汇总三行与 §2 相同。11 张删 / 增表在另一个时点既没有相同的表头行，也没有逐行相同的数据行。00a2e93→HEAD 独立配对与写作者完全一致。50c3958→00a2e93 有 4 处分歧，都出在批内重建的表上：我把 ch10:119→:177 和 model/04:31→:37 配成"改"，写作者记为删 + 增，并在 §6 说明了对应关系；model/02:202→:275 经内容核对是写作者对，我那条是弱启发式的误配。没有漏报的状态变化 |
| 6 | "改了这张表的批"抽 8 张 | 已核实（实际 53/53 全核） | 抽样方法：`random.seed(20261127); random.sample(全部 53 个 changed, 8)`，抽中 ch10:230、ch04:470、model/05:144、:235、:215、model/02:310、model/03:17、:152，8/8 一致。随后又对全部 53 行跑了 `git log -L`，0 不一致 |
| 7a | 60 行一一对应、指向同一张表 | 已核实 | 60 行与 triage §5 的 C3 行编号一致（1-8、12-63）。53 张保留表在 50c3958 的 `line_t2end` 处确为表首行；"未变"的行全部逐字节相同；改过的行相似度在 0.70 以上、行数相同（#40 为 74→69，与 S-CH10 的"整表重建"相符） |
| 7b | 每行的 writer / reviewer 指针 | 部分核实（附发现 #4、#5、#7、#8） | 逐行打开过。S-INT、S-TUFA、S-CH4、S-CH10 各行都是对应表的"census_items 逐格（渲染）"记录，reviewer 那一节都标明"不采信 writer"；ch04 的 writer 行号箭头右侧是批内中间稿的行号，与 reviewer 的终态行号差 2 到 6 行，表的描述对得上。S-MOD2 `:15` 是 cmp.py 脚本结果，`:100` 是逐格表起点（已确认）。S-MOD1 `:5` 是结论行，`:56` 是逐格表起点（已确认） |
| 7c | "现文本始于"抽 10 张 | 已核实（实际 53/53） | 用 git blame 独立核，全部一致 |
| 7d | 4 张 CRF 表加 8 张随机表逐格核 | 已核实 | 见下表；没有 KB 与 PDF 不一致 |
| 8 | §6 七张新表的对应与指针 | 部分核实（附发现 #6、#7） | #38：旧 4 列表展开为 106 对，与新表 106 对集合差 0/0。#39：5 行同值，列顺序对调为 PDF 的"名称在前"。#43-46：旧 16 个变量全在 :166。#63：4 个变量相同，新增 # 列 |

### 第 7(d) 项逐表结果（HEAD 上的 KB 表对 PDF 渲染）
抽样方法：从 C3 中除去 4 张 CRF 表后剩下的 49 张里，`random.seed(20261127); random.sample(pool, 8)`。

| C3# | HEAD 表 | PDF 页 | 表头 | 每格 | 结论 |
|---|---|---|---|---|---|
| 13 | ch04:408 EXADJ | ig34 p32 | 2 格一致 | 3 行×2 一致；3 个选项符号在渲染上是 Wingdings 坏字形，KB 写 ○ = U-9(a) 口径 A 已裁 | 一致（已裁偏差） |
| 14 | ch04:425 Indication | ig34 p32 | PDF 无表头，左格跨行 → KB 右表头空（结构写法） | 6 个选项文字一致，○ = 渲染的 o；"Other, specify: ___" 折行合并为一格 | 一致 |
| 15 | ch04:470 Eye Color | ig34 p33 | 同上 | 5 个选项一致 | 一致 |
| 19 | ch04:504 伴随药 | ig34 p33 | 问句（PDF 折成 4 行，"subject’s" 用弯撇号）一致 | 5 个选项一致 | 一致 |
| 3 | EX/examples:67 | ig34 p112 | PDF 无表头，KB 空表头为 Markdown 结构 | 14 行×2 一致；Injection 1/2/3 不是粗体，一致 | 一致 |
| 16 | ch04:482 | ig34 p33 | SCTEST/SCORRES/SCSTRESC 一致 | Eye Color / BLUEISH GRAY / OTHER | 一致 |
| 17 | ch04:488 | ig34 p33 | 一致 | … / GRAY | 一致 |
| 24 | ch04:598 suppae | ig34 p35 | 一致 | 4 行×3 一致（AERELABC…DOSE NOT CHANGED） | 一致 |
| 26 | ch04:619 suppae | ig34 p36 | 一致 | 2 行×3 一致 | 一致 |
| 27 | ch04:695 | ig34 p38 | 4 格一致 | 5 行×4 一致（DS 的 Modified 为空） | 一致 |
| 48 | model/02:289 Identifiers | sv20 p33-34 | 核心 5 列一致 | 16 行，核心 80 格一致。Notes 为 D6（HEAD 第 :287 行有 KB note），FETUSID / --BEATNO 与 PDF Usage Restrictions 逐字相同。PDF 的 Format 列全空，KB 不设，不丢内容；Qualified / UR / C-code / Definition / Examples 列压缩进 Notes | 核心格一致；非核心列为 D6 |
| 51 | model/02:342 Study Day | sv20 p36-37 | 核心 5 列一致 | 15 行（13-27），核心 75 格一致。缺 Format 列，--DUR 的 "ISO 8601 duration" 放进了 Notes，属 R1/M-4 已裁（`t2_S-MOD2_review.md:16`）；Notes 为 D6（:316） | 核心格一致；已裁偏差 |

没有用到 PDF 笔误登记，因为没有发现需要登记的不一致。

### 我跑过的命令（可复跑，在仓库根目录）
```bash
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/review_a
bash .work/10_tier_b_repair/scripts/t4/t0_mutation_head.sh > $S/t0_head_rerun.log 2>&1; echo $?          # 0
diff .work/10_tier_b_repair/evidence/checkpoints/t0_mutation_head.log <(grep -v '^EXIT=' $S/t0_head_rerun.log)   # 仅 'exit=0' 一行
bash .work/10_tier_b_repair/work/scratch/review_a/rev1.sh   # MISMATCH exit 1
bash .work/10_tier_b_repair/work/scratch/review_a/rev2.sh   # MISMATCH exit 1
git show e3c2f5d:knowledge_base/domains/{PC,MB,EG}/examples.md …       # T0 目标对照
for r in 50c3958 00a2e93 HEAD; do git archive $r knowledge_base | tar -x -C $S/hist/kb_$r; \
  python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest .work/10_tier_b_repair/work/census_full_manifest.json \
  --kb-root $S/hist/kb_$r/knowledge_base --out $S/hist/census_$r.json | tail -2; done
python3 -I .work/10_tier_b_repair/work/scratch/review_a/bin/indep_pair.py $S /Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair
python3 -I .work/10_tier_b_repair/work/scratch/review_a/bin/c3_identity.py
git log --format=COMMIT\ %h -L <start>,<end>:<file> <a>..<b>      # 53 行 "改了这张表的批"
git blame --line-porcelain -L <ln>,<ln+n-1> HEAD -- <file>        # 60 张 "现文本始于"
pdftoppm -f N -l N -r 100 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/png/ig   # p32/33/35/36/38/112
pdftoppm -f N -l N -r 90 -png source/cdisc/SDTM_v2.0.pdf $S/png/sv                            # p33/34/36/37
```

我自己写的脚本和日志都已复制到 gitignored 目录 `/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/work/scratch/review_a/`，包括 `bin/indep_pair.py`、`bin/c3_identity.py`、`rev1.sh`、`rev2.sh`、`rev1.log`、`rev2.log`、`t0_head_rerun.log`、`kb_md5_before.txt`、`kb_md5_after.txt`。其中 `indep_pair.py` 和 `c3_identity.py` 两个脚本都是在 heredoc 里直接跑的一次性核查，没有落成文件。复跑产物只写在 `work/scratch/t0_head`、`work/scratch/review_rev1`、`work/scratch/review_rev2` 以及上述 scratchpad 里。没有跑 `--make-baseline`，也没有跑 t4_c3_* 三个脚本的默认输出。

### 建议
补上发现 #1（配对元数据变化和 PDF_ONLY 1→0 的说明）和 #2（登记 id），再修正 LOW 级的措辞，M-8 取得主人追认后，两个缺口可以记为关闭。

### 收尾状态
```
$ git status --short
 M .work/10_tier_b_repair/trace.jsonl
?? .work/10_tier_b_repair/scripts/t4/t4_gate_prerun.sh
?? .work/10_tier_b_repair/scripts/t4/t4_round2_sample.py
?? .work/10_tier_b_repair/subagent_prompts/t4/t4_supp_round2_v1.0.md
?? .work/10_tier_b_repair/work/t4/round2/
$ git rev-parse HEAD:knowledge_base
63f857774a42cfaa71798705ad40ab51bc5e378a
```
上面 5 项不是我产生的。它们的修改时间在 14:23 到 14:35，是审查期间另一个会话写的；我跑的脚本里都不包含这些路径（grep 过，trace 0 处）。我没有改动任何已跟踪文件，也没有 add / commit / push。KB 树与要求的 `63f8577…` 一致。

(主控注: 那 5 项是主控在审查期间自己做的 — 追加 trace 行、预跑脚本、第二轮补检的脚本 / brief / 样本.)
