# T4 G-TB4: census 逐表变化说明 + C3 逐表结案清单

<!-- chain: E (plans) -->
> 状态: 写作者稿 (主控用脚本生成, 2026-11-27); 独立审查结论见文末. KB 未改 (只读).
> 关闭的缺口: 总闸 attempt 1 §3 / attempt 2 D 项 — "census 合计相同不等于差异集相同, 未逐表比对" 与 "C3 逐表结案清单仍缺".

## 1. 复跑 (仓库根; 只读 KB, 产物在 `work/` 下)

```bash
T=.work/10_tier_b_repair; H=$T/work/scratch/t4/census_hist; mkdir -p $H
for r in 50c3958 00a2e93; do rm -rf $H/kb_$r; mkdir -p $H/kb_$r; git archive $r knowledge_base | tar -x -C $H/kb_$r; \
  python3 -I $T/scripts/table_census.py --manifest $T/work/census_full_manifest.json --kb-root $H/kb_$r/knowledge_base --out $H/census_$r.json | tail -2; done
python3 -I $T/scripts/table_census.py --manifest $T/work/census_full_manifest.json --out $H/census_HEAD.json | tail -2
python3 -I $T/scripts/t4/t4_census_tablediff.py   # -> work/t4/census_tablediff.json
python3 -I $T/scripts/t4/t4_c3_closeout.py        # -> work/t4/c3_closeout.json
python3 -I $T/scripts/t4/t4_c3_report.py          # -> 本文件 (文末审查段保留)
```

- 跨提交配对**不按行号**, 分三步: ① 同一文件里表文本逐字节相同的先配 (按出现次序); ② 其余按键 (文件, 归一表头, 例号, 数据集名) 配 — 键唯一时直接配 (此时不设相似度下限; 独立审查实测 53 对里最低相似度 0.70, 未见误配), 键重复时按表文本相似度配; ③ 再剩的在同文件内按相似度 ≥ 0.6 配; 最后剩下的记为删 / 增 (批内整表重建的旧表 / 新表会落在这里, 对应关系见 §6).
- 每张表另算表文本 md5, 所以 census 读不了的表 (UNPARSEABLE) 改没改也看得见.
- `50c3958` = 60 批 T2 之后、22 个 T2S 扫描批之前 (`evidence/t2_census_global_triage.md` 的基准); `00a2e93` = T2S 全部完成、解冻前 (总闸 attempt 1 的 KB); HEAD = 解冻轮之后 (KB 树 `63f857774a42cfaa71798705ad40ab51bc5e378a`).

## 2. 三个时点汇总

| 时点 | KB 表 | OK | DIFF | diffs | NO_PDF | UNPARSEABLE | PDF_ONLY | PDF_UNPARSED |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| `50c3958` | 501 | 311 | 37 | 144 | 4 | 149 | 1 | 2 |
| `00a2e93` | 500 | 311 | 37 | 144 | 4 | 148 | 0 | 2 |
| `HEAD` | 497 | 309 | 38 | 148 | 4 | 146 | 0 | 2 |

## 3. `50c3958` (T2 收尾) → `00a2e93` (解冻前) 逐表变化

配对 493 张, 其中状态 / 差异集 / 行数 / 表文本 md5 都相同的 **457** 张 (这里面有 26 张只是 census 的配对元数据变了, 见下 "只有配对元数据变化"); 内容或判定有变化 36 张; 删 8 张; 增 7 张.

### 删 / 增的表

| 类 | KB 表 | 状态 | 数据行 | 表头 | 归因 (删表: 逐提交追踪到删 / 重建它的那一批; 增表: 该区间内改过此文件的批, 文件级) |
|---|---|---|--:|---|---|
| 删 | `chapters/ch10_appendices.md:119` @`50c3958` | UNPARSEABLE | 61 | Keyword(s) | Fragment |  | Keyword(s) | Fragment | S-CH10 `b80d263` |
| 删 | `chapters/ch10_appendices.md:208` @`50c3958` | UNPARSEABLE | 5 | Domain | Description | S-CH10 `b80d263` |
| 删 | `model/01_concepts_and_terms.md:176` @`50c3958` | UNPARSEABLE | 5 | Subclass | Purpose | Examples | S-MOD1 `ed7fd2b` (表被删 / 重建) |
| 删 | `model/02_observation_classes.md:162` @`50c3958` | UNPARSEABLE | 2 | Variable | Label | Type | Role | S-MOD2 `6f2c38a` (表被删 / 重建) |
| 删 | `model/02_observation_classes.md:169` @`50c3958` | UNPARSEABLE | 5 | Variable | Label | Type | Role | Notes | S-MOD2 `6f2c38a` (表被删 / 重建) |
| 删 | `model/02_observation_classes.md:179` @`50c3958` | UNPARSEABLE | 6 | Variable | Label | Notes | S-MOD2 `6f2c38a` (表被删 / 重建) |
| 删 | `model/02_observation_classes.md:190` @`50c3958` | UNPARSEABLE | 3 | Variable | Label | Notes | S-MOD2 `6f2c38a` (表被删 / 重建) |
| 删 | `model/04_associated_persons.md:31` @`50c3958` | UNPARSEABLE | 4 | Variable | Label | Type | Role | Notes | S-MOD1 `ed7fd2b` |
| 增 | `chapters/ch10_appendices.md:11` @`00a2e93` | UNPARSEABLE | 74 | Name | Company | S-CH10, S-TYPO |
| 增 | `chapters/ch10_appendices.md:177` @`00a2e93` | UNPARSEABLE | 106 | Keyword(s) | Fragment | S-CH10, S-TYPO |
| 增 | `chapters/ch10_appendices.md:323` @`00a2e93` | UNPARSEABLE | 5 | Domain | Domain Abbreviation | S-CH10, S-TYPO |
| 增 | `chapters/ch10_appendices.md:407` @`00a2e93` | UNPARSEABLE | 1 | Section Number | Section Name | Change | S-CH10, S-TYPO |
| 增 | `chapters/ch10_appendices.md:413` @`00a2e93` | UNPARSEABLE | 4 | Section Number | Section Name | Change | S-CH10, S-TYPO |
| 增 | `model/02_observation_classes.md:166` @`00a2e93` | UNPARSEABLE | 100 | # | Variable | Label | Type | Role | Key Notes | S-MOD2 |
| 增 | `model/04_associated_persons.md:37` @`00a2e93` | UNPARSEABLE | 4 | # | Variable | Label | Type | Role | Notes | S-MOD1 |

### 内容或判定有变化的表

| # | KB 表 (前 → 后行号) | 状态 | 变化 | 改动行 −/+ | 首处差异 (字符级, 截断) | 改了这张表的批 (逐提交追踪) |
|--:|---|---|---|---|---|---|
| 1 | `chapters/ch04_general_assumptions.md:408` → `:425` | UNPARSEABLE | text | −1/+1 | `Options` → `       ` | S-CH4 `42fecd3` |
| 2 | `chapters/ch04_general_assumptions.md:453` → `:470` | UNPARSEABLE | text | −1/+1 | `Options` → `       ` | S-CH4 `42fecd3` |
| 3 | `chapters/ch04_general_assumptions.md:487` → `:504` | UNPARSEABLE | text | −1/+1 | `'` → `’`; `Options` → `       ` | S-CH4 `42fecd3`; S-TYPO `bc4e42e` |
| 4 | `chapters/ch04_general_assumptions.md:749` → `:766` | UNPARSEABLE | text | −1/+1 | `#` → ` ` | S-CH4 `42fecd3` |
| 5 | `chapters/ch04_general_assumptions.md:761` → `:778` | UNPARSEABLE | text | −1/+1 | `#` → ` ` | S-CH4 `42fecd3` |
| 6 | `chapters/ch04_general_assumptions.md:770` → `:787` | UNPARSEABLE | text | −1/+1 | `#` → ` ` | S-CH4 `42fecd3` |
| 7 | `chapters/ch04_general_assumptions.md:1450` → `:1475` | UNPARSEABLE | text | −5/+5 | `¦ Convention ` → `` | S-CH4 `42fecd3` |
| 8 | `chapters/ch08_relationships.md:319` → `:323` | UNPARSEABLE | text | −3/+3 | `"` → `“`; `"` → `”`; `"` → `“` | S-TYPO `bc4e42e` |
| 9 | `chapters/ch10_appendices.md:19` → `:94` | UNPARSEABLE | text | −6/+6 | ` Abbreviation` → ``; `Full Term ` → `` | S-CH10 `b80d263` |
| 10 | `chapters/ch10_appendices.md:93` → `:161` | UNPARSEABLE | text | −1/+1 | `` → `for an intervention `; `M` → `It m`; `` → `.` | S-CH10 `b80d263` |
| 11 | `chapters/ch10_appendices.md:230` → `:335` | UNPARSEABLE | n_rows, text | −65/+60 | `` → `• `; `` → ` of the`; `` → `.` | S-CH10 `b80d263` |
| 12 | `domains/EX/examples.md:65` → `:67` | UNPARSEABLE | text | −3/+3 | `**` → ``; `**` → `` | S-INT `acb93ae` |
| 13 | `domains/MK/examples.md:49` → `:49` | OK | text | −3/+3 | `-` → `–` | S-TYPO `bc4e42e` |
| 14 | `domains/ML/examples.md:52` → `:52` | UNPARSEABLE | text | −1/+1 | `"` → `“`; `"` → `”` | S-TYPO `bc4e42e` |
| 15 | `domains/TA/assumptions.md:31` → `:31` | UNPARSEABLE | text | −1/+1 | `"` → `“`; `"` → `”` | S-TYPO `bc4e42e` |
| 16 | `model/02_observation_classes.md:41` → `:43` | UNPARSEABLE | text | −4/+4 | `` → `--`; `` → `EASOC is the r`; `` → `int` | S-MOD2 `6f2c38a` |
| 17 | `model/02_observation_classes.md:93` → `:97` | UNPARSEABLE | text | −1/+1 | `E` → `n action taken with a`; `om` → `evice `; `in` → `s the result` | S-MOD2 `6f2c38a` |
| 18 | `model/02_observation_classes.md:202` → `:275` | UNPARSEABLE | text | −3/+3 | `` → `¦ # ` | S-MOD2 `6f2c38a` |
| 19 | `model/02_observation_classes.md:237` → `:320` | UNPARSEABLE | text | −11/+11 | `` → `Role ¦ ` | S-MOD2 `6f2c38a` |
| 20 | `model/02_observation_classes.md:251` → `:334` | UNPARSEABLE | text | −5/+5 | `` → `Role ¦ ` | S-MOD2 `6f2c38a` |
| 21 | `model/02_observation_classes.md:259` → `:342` | UNPARSEABLE | text | −17/+17 | `` → `Role ¦ ` | S-MOD2 `6f2c38a` |
| 22 | `model/02_observation_classes.md:279` → `:362` | UNPARSEABLE | text | −7/+7 | `` → `Role ¦ ` | S-MOD2 `6f2c38a` |
| 23 | `model/02_observation_classes.md:289` → `:372` | UNPARSEABLE | text | −10/+10 | `` → `Role ¦ ` | S-MOD2 `6f2c38a` |
| 24 | `model/02_observation_classes.md:302` → `:385` | UNPARSEABLE | text | −5/+5 | `` → `Role ¦ ` | S-MOD2 `6f2c38a` |
| 25 | `model/02_observation_classes.md:310` → `:393` | UNPARSEABLE | text | −7/+7 | `` → `Role ¦ ` | S-MOD2 `6f2c38a` |
| 26 | `model/03_special_purpose_domains.md:17` → `:23` | UNPARSEABLE | text | −7/+7 | `` → `equivalent to the `; `` → `/time`; `of` → `when` | S-MOD1 `ed7fd2b` |
| 27 | `model/03_special_purpose_domains.md:60` → `:68` | UNPARSEABLE | text | −2/+2 | `` → `equiva`; `as` → `en`; `d` → `t` | S-MOD1 `ed7fd2b` |
| 28 | `model/03_special_purpose_domains.md:152` → `:178` | UNPARSEABLE | text | −1/+1 | `rence` → `` | S-MOD1 `ed7fd2b` |
| 29 | `model/03_special_purpose_domains.md:179` → `:211` | UNPARSEABLE | text | −1/+1 | `U` → `Name of the specific disease milesto`; `` → `e. For d`; `q` → `sease milestones that can occ` | S-MOD1 `ed7fd2b` |
| 30 | `model/05_study_level_data.md:35` → `:35` | UNPARSEABLE | text | −1/+1 | `` → `(ETCD) ` | S-MOD3 `a197773` |
| 31 | `model/05_study_level_data.md:53` → `:53` | UNPARSEABLE | text | −2/+2 | `` → `(ARMCD) ` | S-MOD3 `a197773` |
| 32 | `model/05_study_level_data.md:74` → `:72` | UNPARSEABLE | text | −1/+1 | `` → `(TXPARMCD) ` | S-MOD3 `a197773` |
| 33 | `model/05_study_level_data.md:144` → `:146` | UNPARSEABLE | text | −2/+2 | `` → `(VISITNUM) ` | S-MOD3 `a197773` |
| 34 | `model/05_study_level_data.md:196` → `:198` | UNPARSEABLE | text | −1/+1 | `` → `(IETESTCD) ` | S-MOD3 `a197773` |
| 35 | `model/05_study_level_data.md:215` → `:215` | UNPARSEABLE | text | −1/+1 | `` → `(TSPARMCD) ` | S-MOD3 `a197773` |
| 36 | `model/05_study_level_data.md:235` → `:235` | UNPARSEABLE | text | −1/+1 | `` → `(ACPARMCD) ` | S-MOD3 `a197773` |

### 只有配对元数据变化的表 (表文本、状态、差异集都没变)

共 26 张. census 给每张 KB 表认 "例号 (ex) / 数据集名 (ds)" 靠的是表上方的标题行与标签行; 扫描批改了这些行 (例如加 `### Example 1` 标题、把 `qscg.xpt:` 标签补齐), 表本身没动, 但 census 认到的例号 / 数据集名变了, 进而改变了它与 PDF 表的配对和 "是否副本" 的判断.

| KB 表 (前 → 后行号) | 状态 | 变化 (字段: 前 → 后) |
|---|---|---|
| `chapters/ch04_general_assumptions.md:102` → `:104` | OK | ds: None → qscg.xpt |
| `chapters/ch04_general_assumptions.md:115` → `:119` | OK | ds: None → qspi.xpt |
| `chapters/ch04_general_assumptions.md:126` → `:132` | OK | ds: None → qssw.xpt |
| `chapters/ch04_general_assumptions.md:143` → `:151` | OK | ds: None → suppqscg.xpt |
| `chapters/ch04_general_assumptions.md:150` → `:160` | OK | ds: None → suppqspi.xpt |
| `chapters/ch04_general_assumptions.md:165` → `:177` | OK | ds: None → suppqssw.xpt |
| `chapters/ch04_general_assumptions.md:558` → `:574` | UNPARSEABLE | ex: 1 → None |
| `chapters/ch04_general_assumptions.md:564` → `:580` | UNPARSEABLE | ex: 1 → None |
| `chapters/ch04_general_assumptions.md:576` → `:592` | UNPARSEABLE | ex: 1 → None |
| `chapters/ch04_general_assumptions.md:582` → `:598` | UNPARSEABLE | ex: 1 → None |
| `chapters/ch04_general_assumptions.md:597` → `:613` | UNPARSEABLE | ex: 1 → None |
| `chapters/ch04_general_assumptions.md:603` → `:619` | UNPARSEABLE | ex: 1 → None |
| `chapters/ch04_general_assumptions.md:1304` → `:1327` | OK | ds: None → lb.xpt |
| `chapters/ch04_general_assumptions.md:1328` → `:1353` | DIFF | ds: None → eg.xpt |
| `chapters/ch04_general_assumptions.md:1346` → `:1373` | OK | ds: None → vs.xpt |
| `chapters/ch08_relationships.md:162` → `:164` | OK | ex: None → 1; kb_duplicate: True → False |
| `chapters/ch08_relationships.md:232` → `:236` | OK | ex: None → 1; kb_duplicate: True → False |
| `chapters/ch08_relationships.md:241` → `:245` | OK | ex: None → 1 |
| `chapters/ch08_relationships.md:383` → `:390` | OK | ex: None → 1; kb_duplicate: True → False |
| `chapters/ch08_relationships.md:397` → `:406` | OK | ex: None → 1; kb_duplicate: True → False |
| `chapters/ch08_relationships.md:457` → `:468` | OK | ex: None → 1; kb_duplicate: True → False |
| `domains/RELSPEC/examples.md:44` → `:44` | OK | kb_duplicate: False → True |
| `domains/RELSUB/examples.md:17` → `:17` | OK | kb_duplicate: False → True |
| `domains/RELSUB/examples.md:33` → `:33` | OK | kb_duplicate: False → True |
| `domains/SS/examples.md:7` → `:9` | OK | ds: None → ss.xpt |
| `domains/SUPPQUAL/examples.md:13` → `:13` | OK | kb_duplicate: False → True |

**PDF_ONLY 1 → 0 的来源**: `50c3958` 时的 PDF_ONLY = relrec.xpt Ex1 p[431] (T2 收尾分诊记为 C2 假阳: KB 有两份逐格 OK 的副本). 上表 `chapters/ch08_relationships.md:162` → `:164` 这一行: 当时 census 认不出它的例号 (ex = None), 只能把它当成另一张表的副本 (kb_duplicate = True), 于是 p431 的这张 PDF relrec 表没有 "正主" 配对, 落成 PDF_ONLY; S-CH8 之后它被认成 Example 1 (ex = 1, 不再是副本), 与 p431 那张表直接配上, PDF_ONLY 消失. 表文本没变, KB 内容没有因此增减.
**KB 表数 501 → 500、UNPARSEABLE 149 → 148 的来源**: 上面 "删 / 增的表" 里删 8 增 7, 全部是 UNPARSEABLE 表 (批内整表重建 / 表改成列表 / 新补的表).

## 4. `00a2e93` (解冻前) → `HEAD` (HEAD) 逐表变化

配对 497 张, 其中状态 / 差异集 / 行数 / 表文本 md5 都相同的 **480** 张 (这里面有 0 张只是 census 的配对元数据变了, 见下 "只有配对元数据变化"); 内容或判定有变化 17 张; 删 3 张; 增 0 张.

### 删 / 增的表

| 类 | KB 表 | 状态 | 数据行 | 表头 | 归因 (删表: 逐提交追踪到删 / 重建它的那一批; 增表: 该区间内改过此文件的批, 文件级) |
|---|---|---|--:|---|---|
| 删 | `domains/PP/examples.md:120` @`00a2e93` | UNPARSEABLE | 4 | Method | Cardinality | PC-side IDVAR | PP-side IDVAR | T4 解冻轮 `a59c2d3` (表被删 / 重建) |
| 删 | `domains/PP/examples.md:152` @`00a2e93` | OK | 8 | Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTY | T4 解冻轮 `a59c2d3` |
| 删 | `model/06_relationship_datasets.md:50` @`00a2e93` | UNPARSEABLE | 4 | Source RELTYPE | Target RELTYPE | Meaning | T4 解冻轮 `a59c2d3` (表被删 / 重建) |

### 内容或判定有变化的表

| # | KB 表 (前 → 后行号) | 状态 | 变化 | 改动行 −/+ | 首处差异 (字符级, 截断) | 改了这张表的批 (逐提交追踪) |
|--:|---|---|---|---|---|---|
| 1 | `chapters/ch04_general_assumptions.md:408` → `:408` | UNPARSEABLE | text | −3/+3 | `[ ]` → `○` | T4 解冻轮 `a59c2d3` |
| 2 | `chapters/ch04_general_assumptions.md:425` → `:425` | UNPARSEABLE | text | −6/+6 | `[ ]` → `○` | T4 解冻轮 `a59c2d3` |
| 3 | `chapters/ch04_general_assumptions.md:470` → `:470` | UNPARSEABLE | text | −5/+5 | `[ ]` → `○` | T4 解冻轮 `a59c2d3` |
| 4 | `chapters/ch04_general_assumptions.md:504` → `:504` | UNPARSEABLE | text | −5/+5 | `[ ]` → `○` | T4 解冻轮 `a59c2d3` |
| 5 | `domains/CE/examples.md:41` → `:41` | UNPARSEABLE | text | −4/+4 | `( )` → `○`; `( )` → `○`; `( )` → `○` | T4 解冻轮 `a59c2d3` |
| 6 | `domains/CE/examples.md:72` → `:72` | UNPARSEABLE | text | −7/+7 | `( )` → `○`; `( )` → `○` | T4 解冻轮 `a59c2d3` |
| 7 | `domains/DS/examples.md:292` → `:292` | DIFF | diffset, text | −2/+2 | `EE` → `` census 差异: +1/ETCD KB `SCRN` vs PDF `SCREEN`; +5/ETCD KB `SCRN` vs PDF `SCREEN` — 不是回归: 已登记 PDF 笔误 `B-DS U-1` (KB 写正确值 SCRN; U-7 A1-9) | T4 解冻轮 `a59c2d3` |
| 8 | `domains/IS/examples.md:203` → `:203` | OK | text | −3/+3 | `-` → `–` | T4 解冻轮 `a59c2d3` |
| 9 | `domains/PP/examples.md:14` → `:14` | OK → **DIFF** | status, diffset, text | −2/+2 | `H` → `h` census 差异: +1/PPSTRESU KB `h` vs PDF `H`; +4/PPSTRESU KB `h` vs PDF `H` — 不是回归: 已登记 PDF 笔误 `B-PCPP T-7` (KB 写正确值 h; U-7 A1-21) | T4 解冻轮 `a59c2d3` |
| 10 | `domains/TA/examples.md:335` → `:335` | OK | text | −1/+1 | `-` → `–` | T4 解冻轮 `a59c2d3` |
| 11 | `domains/TS/assumptions.md:45` → `:45` | UNPARSEABLE | text | −2/+2 | `E` → `` | T4 解冻轮 `a59c2d3` |
| 12 | `model/05_study_level_data.md:99` → `:99` | UNPARSEABLE | text | −2/+2 | `N` → `Usage Restricti`; `te` → `n` | T4 解冻轮 `a59c2d3` |
| 13 | `model/05_study_level_data.md:119` → `:119` | UNPARSEABLE | text | −2/+2 | `N` → `Usage Restricti`; `te` → `n` | T4 解冻轮 `a59c2d3` |
| 14 | `model/05_study_level_data.md:215` → `:217` | UNPARSEABLE | text | −13/+13 | `` → ` Usage Restrictions ¦` | T4 解冻轮 `a59c2d3` |
| 15 | `model/06_relationship_datasets.md:33` → `:35` | UNPARSEABLE | text | −1/+1 | `` → ` of associated persons`; `` → `. If APID identifies a pool, POOLDEF rec` | T4 解冻轮 `a59c2d3` |
| 16 | `model/06_relationship_datasets.md:71` → `:64` | UNPARSEABLE | text | −1/+1 | `` → ` (QNAM)` | T4 解冻轮 `a59c2d3` |
| 17 | `model/06_relationship_datasets.md:190` → `:183` | UNPARSEABLE | text | −1/+1 | `Y` → `Par`; `s` → `nt record (USUBJID, APID, POOLID, or SPD` | T4 解冻轮 `a59c2d3` |

## 5. C3 60 张逐表结案

C3 = T2 收尾分诊 (`evidence/t2_census_global_triage.md` §5) 里 "census 读不了、当时也没有人工逐格证据" 的 60 张表. 之后 6 个扫描批 (S-CH4 / S-INT / S-TUFA / S-CH10 / S-MOD1 / S-MOD2) 各自在 checkpoint 里留了 "census_items 逐格" 段: writer 一遍 + reviewer "不采信 writer" 再一遍 (都对 PDF 渲染页).
"逐格" 的范围: SDTMIG 的表 (ch04 / ch10 / EX / TR) 是全部格对渲染页; SDTM v2.0 的变量表 (model/02 / 03 / 04) 逐格核的是核心列 (# / Variable / Label / Type / Role), KB 的 Notes / Key Notes 列是 KB 自写说明 (D6), 只核 "与 PDF 不矛盾"; PDF 的 Format / C-code / Definition / Examples 等列 KB 不设 (T1.4 R1).
"现文本始于" = HEAD 上这张表的文本最早出现的提交 (一路到 HEAD 未再变): 等于 `50c3958` 表示扫描批核过但没改; 等于扫描批提交表示批内改过, 逐格记录写的是改后内容; 晚于扫描批的 (解冻轮) 另指到解冻轮的审查证据.

| # | T2 收尾位置 | HEAD 位置 | 表行数 | 现文本始于 | 逐格证据: writer | 逐格证据: reviewer (独立) | 结案 |
|--:|---|---|--:|---|---|---|---|
| 1 | `domains/EX/examples.md:13` | `:15` | 3 | T2 收尾起未变 | S-INT `t2_S-INT.md:68` | `t2_S-INT_review.md:79` | 已结案 |
| 2 | `domains/EX/examples.md:19` | `:21` | 5 | T2 收尾起未变 | S-INT `t2_S-INT.md:69` | `t2_S-INT_review.md:80` | 已结案 |
| 3 | `domains/EX/examples.md:65` | `:67` | 16 | S-INT `acb93ae` | S-INT `t2_S-INT.md:70` | `t2_S-INT_review.md:81` | 已结案 |
| 4 | `domains/EX/examples.md:173` | `:175` | 4 | T2 收尾起未变 | S-INT `t2_S-INT.md:71` | `t2_S-INT_review.md:82` | 已结案 |
| 5 | `domains/EX/examples.md:180` | `:182` | 4 | T2 收尾起未变 | S-INT `t2_S-INT.md:71` | `t2_S-INT_review.md:82` | 已结案 |
| 6 | `domains/EX/examples.md:187` | `:189` | 4 | T2 收尾起未变 | S-INT `t2_S-INT.md:71` | `t2_S-INT_review.md:82` | 已结案 |
| 7 | `domains/EX/examples.md:422` | `:424` | 3 | T2 收尾起未变 | S-INT `t2_S-INT.md:76` | `t2_S-INT_review.md:87` | 已结案 |
| 8 | `domains/EX/examples.md:426` | `:428` | 4 | T2 收尾起未变 | S-INT `t2_S-INT.md:76` | `t2_S-INT_review.md:87` | 已结案 |
| 12 | `domains/TR/assumptions.md:15` | `:31` | 3 | T2 收尾起未变 | S-TUFA `t2_S-TUFA.md:67` | `t2_S-TUFA_review.md:92` | 已结案 |
| 13 | `chapters/ch04_general_assumptions.md:391` | `:408` | 5 | T4 解冻轮 `a59c2d3` | S-CH4 `t2_S-CH4.md:70` | `t2_S-CH4_review.md:30` | 已结案 (解冻轮改了 CRF 选项符号, 另见 §5.1) |
| 14 | `chapters/ch04_general_assumptions.md:408` | `:425` | 8 | T4 解冻轮 `a59c2d3` | S-CH4 `t2_S-CH4.md:71` | `t2_S-CH4_review.md:31` | 已结案 (解冻轮改了 CRF 选项符号, 另见 §5.1) |
| 15 | `chapters/ch04_general_assumptions.md:453` | `:470` | 7 | T4 解冻轮 `a59c2d3` | S-CH4 `t2_S-CH4.md:72` | `t2_S-CH4_review.md:32` | 已结案 (解冻轮改了 CRF 选项符号, 另见 §5.1) |
| 16 | `chapters/ch04_general_assumptions.md:465` | `:482` | 3 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:73` | `t2_S-CH4_review.md:33` | 已结案 |
| 17 | `chapters/ch04_general_assumptions.md:471` | `:488` | 3 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:74` | `t2_S-CH4_review.md:33` | 已结案 |
| 18 | `chapters/ch04_general_assumptions.md:477` | `:494` | 3 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:75` | `t2_S-CH4_review.md:33` | 已结案 |
| 19 | `chapters/ch04_general_assumptions.md:487` | `:504` | 7 | T4 解冻轮 `a59c2d3` | S-CH4 `t2_S-CH4.md:76` | `t2_S-CH4_review.md:34` | 已结案 (解冻轮改了 CRF 选项符号, 另见 §5.1) |
| 20 | `chapters/ch04_general_assumptions.md:497` | `:514` | 4 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:77` | `t2_S-CH4_review.md:35` | 已结案 |
| 21 | `chapters/ch04_general_assumptions.md:558` | `:574` | 3 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:78` | `t2_S-CH4_review.md:36` | 已结案 |
| 22 | `chapters/ch04_general_assumptions.md:564` | `:580` | 5 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:79` | `t2_S-CH4_review.md:36` | 已结案 |
| 23 | `chapters/ch04_general_assumptions.md:576` | `:592` | 3 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:80` | `t2_S-CH4_review.md:36` | 已结案 |
| 24 | `chapters/ch04_general_assumptions.md:582` | `:598` | 6 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:81` | `t2_S-CH4_review.md:36` | 已结案 |
| 25 | `chapters/ch04_general_assumptions.md:597` | `:613` | 3 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:82` | `t2_S-CH4_review.md:36` | 已结案 |
| 26 | `chapters/ch04_general_assumptions.md:603` | `:619` | 4 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:83` | `t2_S-CH4_review.md:37` | 已结案 |
| 27 | `chapters/ch04_general_assumptions.md:678` | `:695` | 7 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:84` | `t2_S-CH4_review.md:38` | 已结案 |
| 28 | `chapters/ch04_general_assumptions.md:749` | `:766` | 9 | S-CH4 `42fecd3` | S-CH4 `t2_S-CH4.md:85` | `t2_S-CH4_review.md:39` | 已结案 |
| 29 | `chapters/ch04_general_assumptions.md:761` | `:778` | 6 | S-CH4 `42fecd3` | S-CH4 `t2_S-CH4.md:86` | `t2_S-CH4_review.md:40` | 已结案 |
| 30 | `chapters/ch04_general_assumptions.md:1034` | `:1053` | 4 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:87` | `t2_S-CH4_review.md:41` | 已结案 |
| 31 | `chapters/ch04_general_assumptions.md:1074` | `:1095` | 5 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:88` | `t2_S-CH4_review.md:42` | 已结案 |
| 32 | `chapters/ch04_general_assumptions.md:1084` | `:1105` | 5 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:89` | `t2_S-CH4_review.md:42` | 已结案 |
| 33 | `chapters/ch04_general_assumptions.md:1112` | `:1131` | 20 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:90` | `t2_S-CH4_review.md:43` | 已结案 |
| 34 | `chapters/ch04_general_assumptions.md:1135` | `:1154` | 20 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:91` | `t2_S-CH4_review.md:43` | 已结案 |
| 35 | `chapters/ch04_general_assumptions.md:1511` | `:1536` | 6 | T2 收尾起未变 | S-CH4 `t2_S-CH4.md:92` | `t2_S-CH4_review.md:44` | 已结案 |
| 36 | `chapters/ch10_appendices.md:19` | `:94` | 42 | S-CH10 `b80d263` | S-CH10 `t2_S-CH10.md:62` | `t2_S-CH10_review.md:62` | 已结案 |
| 37 | `chapters/ch10_appendices.md:93` | `:161` | 5 | S-CH10 `b80d263` | S-CH10 `t2_S-CH10.md:63` | `t2_S-CH10_review.md:63` | 已结案 |
| 38 | `chapters/ch10_appendices.md:119` | (批内重建, 见 §6) | — | — | S-CH10 `t2_S-CH10.md:64` | `t2_S-CH10_review.md:64` | 已结案 (原表不存在, 由 §6 的新表承接) |
| 39 | `chapters/ch10_appendices.md:208` | (批内重建, 见 §6) | — | — | S-CH10 `t2_S-CH10.md:65` | `t2_S-CH10_review.md:65` | 已结案 (原表不存在, 由 §6 的新表承接) |
| 40 | `chapters/ch10_appendices.md:230` | `:335` | 71 | S-CH10 `b80d263` | S-CH10 `t2_S-CH10.md:66` | `t2_S-CH10_review.md:66` | 已结案 |
| 41 | `model/02_observation_classes.md:41` | `:43` | 45 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:125` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 42 | `model/02_observation_classes.md:93` | `:97` | 58 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:126` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 43 | `model/02_observation_classes.md:162` | (批内重建, 见 §6) | — | — | S-MOD2 `t2_S-MOD2.md:127` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 (原表不存在, 由 §6 的新表承接) |
| 44 | `model/02_observation_classes.md:169` | (批内重建, 见 §6) | — | — | S-MOD2 `t2_S-MOD2.md:127` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 (原表不存在, 由 §6 的新表承接) |
| 45 | `model/02_observation_classes.md:179` | (批内重建, 见 §6) | — | — | S-MOD2 `t2_S-MOD2.md:127` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 (原表不存在, 由 §6 的新表承接) |
| 46 | `model/02_observation_classes.md:190` | (批内重建, 见 §6) | — | — | S-MOD2 `t2_S-MOD2.md:127` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 (原表不存在, 由 §6 的新表承接) |
| 47 | `model/02_observation_classes.md:202` | `:275` | 3 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:128` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 48 | `model/02_observation_classes.md:212` | `:289` | 18 | T2 收尾起未变 | S-MOD2 `t2_S-MOD2.md:129` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 49 | `model/02_observation_classes.md:237` | `:320` | 11 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:130` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 50 | `model/02_observation_classes.md:251` | `:334` | 5 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:130` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 51 | `model/02_observation_classes.md:259` | `:342` | 17 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:130` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 52 | `model/02_observation_classes.md:279` | `:362` | 7 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:130` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 53 | `model/02_observation_classes.md:289` | `:372` | 10 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:130` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 54 | `model/02_observation_classes.md:302` | `:385` | 5 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:130` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 55 | `model/02_observation_classes.md:310` | `:393` | 7 | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:130` | `t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表; auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格) | 已结案 |
| 56 | `model/03_special_purpose_domains.md:17` | `:23` | 40 | S-MOD1 `ed7fd2b` | S-MOD1 `t2_S-MOD1.md:204` | `t2_S-MOD1_review.md:5` (106 行 530 核心格) + `:56` 起逐格表; auditor `t2_S-MOD1_audit.md:41` (7 表 106 行渲染全看) | 已结案 |
| 57 | `model/03_special_purpose_domains.md:60` | `:68` | 10 | S-MOD1 `ed7fd2b` | S-MOD1 `t2_S-MOD1.md:205` | `t2_S-MOD1_review.md:66` (Key Reference Date (KB 汇总) 8 行: Description = PDF DM Label 逐字; Typical Use 为 D6); KB 自写汇总表, 不在 auditor 的 "7 表 106 行" 内 | 已结案 |
| 58 | `model/03_special_purpose_domains.md:79` | `:91` | 17 | T2 收尾起未变 | S-MOD1 `t2_S-MOD1.md:206` | `t2_S-MOD1_review.md:5` (106 行 530 核心格) + `:56` 起逐格表; auditor `t2_S-MOD1_audit.md:41` (7 表 106 行渲染全看) | 已结案 |
| 59 | `model/03_special_purpose_domains.md:105` | `:127` | 15 | T2 收尾起未变 | S-MOD1 `t2_S-MOD1.md:207` | `t2_S-MOD1_review.md:5` (106 行 530 核心格) + `:56` 起逐格表; auditor `t2_S-MOD1_audit.md:41` (7 表 106 行渲染全看) | 已结案 |
| 60 | `model/03_special_purpose_domains.md:131` | `:153` | 12 | T2 收尾起未变 | S-MOD1 `t2_S-MOD1.md:208` | `t2_S-MOD1_review.md:5` (106 行 530 核心格) + `:56` 起逐格表; auditor `t2_S-MOD1_audit.md:41` (7 表 106 行渲染全看) | 已结案 |
| 61 | `model/03_special_purpose_domains.md:152` | `:178` | 18 | S-MOD1 `ed7fd2b` | S-MOD1 `t2_S-MOD1.md:209` | `t2_S-MOD1_review.md:5` (106 行 530 核心格) + `:56` 起逐格表; auditor `t2_S-MOD1_audit.md:41` (7 表 106 行渲染全看) | 已结案 |
| 62 | `model/03_special_purpose_domains.md:179` | `:211` | 12 | S-MOD1 `ed7fd2b` | S-MOD1 `t2_S-MOD1.md:210` | `t2_S-MOD1_review.md:5` (106 行 530 核心格) + `:56` 起逐格表; auditor `t2_S-MOD1_audit.md:41` (7 表 106 行渲染全看) | 已结案 |
| 63 | `model/04_associated_persons.md:31` | (批内重建, 见 §6) | — | — | S-MOD1 `t2_S-MOD1.md:211` | `t2_S-MOD1_review.md:5` (106 行 530 核心格) + `:56` 起逐格表; auditor `t2_S-MOD1_audit.md:41` (7 表 106 行渲染全看) | 已结案 (原表不存在, 由 §6 的新表承接) |

合计 60 = 已结案且扫描批之后未再改 49 + 解冻轮改过符号 4 + 批内重建 7. 没有 "仍未逐格核" 的 C3 表.

### 5.1 解冻轮改过的 4 张 ch04 CRF 表

- 改动 = U-9(a) CRF 选项符号按渲染外观 (`[ ]` → ○ 等), 共 ch04 19 处 (§4 表里 ch04 四行). 表格文字未动.
- 审查证据: `t4_thaw_review.md:22` ("ch04 p32 坏字形 3 + ○6, p33 ○10 (=19) … 渲染逐一一致"); `t4_thaw_audit.md:10` (auditor 抽 CRF 6 hunk, 含 ch04:410-412 / :472-476 / :506-510); 写作者记录 `t4_thaw_W1.md`.

## 6. C3 文件里由扫描批新建的 7 张表 (其中 4 张承接 §5 里 "批内重建" 的 7 张旧表, 3 张是新补的)

| HEAD 位置 | 表行数 | 表头 | 现文本始于 | 逐格证据 |
|---|--:|---|---|---|
| `chapters/ch10_appendices.md:11` | 76 | Name | Company | S-CH10 `b80d263` | S-CH10 `t2_S-CH10.md:34-35` (App A 名单整表补: p444 35 行 + p445 39 行) / `t2_S-CH10_review.md:67` (tabA 74×2 + 渲染) |
| `chapters/ch10_appendices.md:177` | 108 | Keyword(s) | Fragment | S-CH10 `b80d263` | S-CH10 `t2_S-CH10.md:64` (#38 重建为 2 列 106 行) / `t2_S-CH10_review.md:64` (tabD 106×2 + 渲染) |
| `chapters/ch10_appendices.md:323` | 7 | Domain | Domain Abbreviation | S-CH10 `b80d263` | S-CH10 `t2_S-CH10.md:65` (#39 重建) / `t2_S-CH10_review.md:65` |
| `chapters/ch10_appendices.md:407` | 3 | Section Number | Section Name | Change | S-CH10 `b80d263` | S-CH10 `t2_S-CH10.md:66` (#40 §9 子表) / `t2_S-CH10_review.md:66` |
| `chapters/ch10_appendices.md:413` | 6 | Section Number | Section Name | Change | S-CH10 `b80d263` | S-CH10 `t2_S-CH10.md:66` (#40 Appendices 子表) / `t2_S-CH10_review.md:66` |
| `model/02_observation_classes.md:166` | 102 | # | Variable | Label | Type | Role | Key Notes | S-MOD2 `6f2c38a` | S-MOD2 `t2_S-MOD2.md:127` (FND 四表并入一张 100 行) / `t2_S-MOD2_review.md:54` (100 行逐格对渲染) |
| `model/04_associated_persons.md:37` | 6 | # | Variable | Label | Type | Role | Notes | S-MOD1 `ed7fd2b` | S-MOD1 `t2_S-MOD1.md:211` (AP 重建) / `t2_S-MOD1_audit.md:41` |

对应关系 (旧 7 张 → 新 4 张): C3 #38 → `ch10:177`; #39 → `ch10:323`; #43-#46 (model/02 Findings 四张) → `model/02:166`; #63 (model/04 AP) → `model/04:37`. 另外 3 张不对应旧 C3 表: `ch10:11` (App A 名单) 是 T2 收尾时整表缺、S-CH10 新补的; `ch10:407` (§9 子表 1 行) 与 `ch10:413` (Appendices 子表 4 行) 是 S-CH10 重建 #40 变更表时按 PDF 新补的行, 旧 #40 表里没有 (#40 主表仍在 `:335`, 见 §5).

<!-- REVIEW: 以下由独立审查后誊入, 脚本重跑时原样保留 -->

## 独立审查 (审查者 `oh-my-claudecode:verifier` opus, 只读, 2026-11-27; 对象 HEAD `1df9f60` 的第 1 稿; 原文 `evidence/t4_gap_review_raw/review_a.md`; 主控不改判)

**结论 (B 部分 = census 逐表比对 + C3 结案): CONDITIONAL** — 用独立方法核过配对、删 / 增、改表的批、"现文本始于", 都成立; 12 张表逐格对 PDF 渲染无不一致. 条件 = 补上发现 #1 (已补, 见 §3 "只有配对元数据变化的表" 与 PDF_ONLY 来源说明). HIGH 0 / MEDIUM 1 / LOW 8 (B 部分).

审查者做的事 (摘):
- 三个时点的 census 自己重建, 与写作者的逐字段相等; 汇总三行与 §2 相同.
- 独立配对 (按整文件逐行 diff 映射, 不用写作者的 `pair`): `00a2e93` → HEAD 与写作者完全一致 (配对 497, 删 3, 增 0, 改 17; 状态 / 差异集有变化的只有 DS:292 与 PP:14); `50c3958` → `00a2e93` 的分歧只出在批内重建的表上, 没有漏报的状态变化.
- "改了这张表的批" 一列: 对 §3 + §4 全部 53 行跑 `git log -L`, 0 不一致. "现文本始于": 53 张用 `git blame` 独立核, 全部一致.
- C3 60 行与 triage §5 一一对应; writer / reviewer 指针逐行打开过.
- **逐格对 PDF 渲染 12 张** (解冻轮改过符号的 4 张 ch04 CRF 表 + `random.seed(20261127)` 抽的 8 张: EX:67、ch04:482 / :488 / :598 / :619 / :695、model/02:289 / :342): 表头与每格都一致; model/02 两张核的是核心列, 非核心列为 D6 / R1 已裁.

发现与处理:

| # | 严重度 | 审查意见 (摘) | 处理 |
|--:|---|---|---|
| 1 | MEDIUM | "完全不变 457" 不比较配对元数据; 26 张表的 ex / ds / kb_duplicate 变了; PDF_ONLY 1 → 0 的来源没交代 | 已补: `t4_census_tablediff.py` 记录 `meta_only`; §3 新增 "只有配对元数据变化的表" 26 行 + PDF_ONLY / 表数变化来源说明 |
| 2 | LOW | DS:292 / PP:14 的新增 census 差异没写登记 id | 已补 (`B-DS U-1`, `B-PCPP T-7`) |
| 3 | LOW | §1 配对说明与代码不符 | 已按代码改写 (三步; 键唯一时无相似度下限, 实测最低 0.70) |
| 4 | LOW | C3 #57 (Key Reference Date) 的 reviewer 指针指错 | 已改为 `t2_S-MOD1_review.md:66`, 并注明不在 auditor 的 7 表内 |
| 5 | LOW | "逐格" 对 model 表只是核心列 | §5 导语已注明逐格的范围 |
| 6 | LOW | §6 标题 "承接 7 张" 是数字巧合 | 已改: 旧 7 张 → 新 4 张, 另 3 张是新补的 |
| 7 | LOW | ch10:11 的 writer 指针应为 `:34-35` | 已改 |
| 8 | LOW | S-MOD2 auditor 指针没行号 | 已补 `:14` |
| 9 | LOW | §3 删表的归因列是文件级, 易误读 | 已改: 删表按逐提交追踪给出删 / 重建它的那一批 |

审查者另记 (不算问题): `t4_thaw_audit.md:10` 抽查的 hunk 不含 ch04:425 表, 该表只有解冻轮 reviewer 的覆盖 — 本次 7(d) 已对它重新逐格核 (一致).
