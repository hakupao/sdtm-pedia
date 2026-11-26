# T2 B-FA auditor (Rule A 独立抽检)

## attempt 1

> auditor = oh-my-claudecode:verifier (opus), 2026-11-26. 审计对象: `git diff 4f8bde8 -- knowledge_base/domains/FA/ knowledge_base/chapters/ch02_fundamentals.md knowledge_base/model/02_observation_classes.md`
> md5 (= writer 续 after, reviewer 续 PASS 之后未变): FA/assumptions b56ccc20… / FA/examples f7178ec1… / ch02 1c39874b… / model/02 2180f142….
> 先独立判 (PDF 页文本 + 渲染), 判完才对照 writer/reviewer 报告.

### 抽样
- 命令: `t2_auditor_v1.0.md` §抽样 脚本原样 (batch_id=B-FA, seed=20261126), 输出 `$S/sample.json` (S=scratchpad/t2_B-FA_auditor).
- 结果: **C=4, P=88, N=10**. 主样本: p0373_a012, p0364_a003, p0363_a014, p0364_a011 (C 全部 4) + p0363_a007, p0363_a012, p0374_a016, p0016_a013, p0374_a020, p0013_a017 (P−C 6).
- **补抽 (§6.4/§6.4.1 改写率 >50%, 主样本只含 1 条)**: 总体 = p361 a011-a018 / p362 a001-a010 / p363 a001-a009 中 prose (26 条, 2 HEADING 除外), 去主样本, `random.Random(20261126).sample(pool,5)` → p0362_a009, p0362_a008, p0361_a013, p0363_a003, p0363_a005. §6.4.1 合计 6/15; §6.4.2 3 条; §6.4.3 1 条; 例子 4 条; 未改 prose (ch02) 2 条.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0373_a012 | p373 Ex5 叙述: 符合 criterion 1 / GERD 症状视为临床事件 / 呕吐量符合 criterion 2 | FA/examples.md:226 | 否 | 是 | 是 (Example 5) | 逐字; "In this study, GERD symptoms…" 为本批补回 |
| 2 | ig34_p0364_a003 | p364 §6.4.2 3. 子项: DOMAIN 由 sponsor 定、不以 FA 开头, SR 例 | FA/assumptions.md:82 | 否 | 是 | 是 (§6.4.2) | 逐字 (源 ch02 已删) |
| 3 | ig34_p0363_a014 | p363 §6.4.2 "2. A split FA domain…Section 4.1.7" | FA/assumptions.md:74 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0364_a011 | p364 §6.4.3 --OBJ 唯一, 与 FATESTCD 共同为 topic | FA/assumptions.md:93 | 否 | 是 | 是 (§6.4.3) | 逐字 (源 model/02 已删) |
| 5 | ig34_p0363_a007 | p363 §6.4.1 PtC 第 2 条: FAGRPID/FACAT/FASCAT 分组 | FA/assumptions.md:63 | 否 | 是 | 是 (§6.4.1 PtC) | 逐字; 旧 KB 漏 FAGRPID 已补 |
| 6 | ig34_p0363_a012 | p363 §6.4.2 "For example, if findings about CE and MH…" | FA/assumptions.md:71 | 否 | 是 | 是 | 逐字 |
| 7 | ig34_p0374_a016 | p374 Ex6 "electronic … 2 related modules" | FA/examples.md:270 | 否 | 是 | 是 (Example 6) | 逐字, 未改 prose 对照 |
| 8 | ig34_p0016_a013 | p16 §2.7 列表 "RPATHCD (Demographics)" | ch02:165 | 否 | 是 | 是 (§2.7 DM 子列表) | 未改 prose 对照 |
| 9 | ig34_p0374_a020 | p374 Ex6 "A module for the severity assessment…" | FA/examples.md:277 | 否 | 是 | 是 | 未改 prose 对照 |
| 10 | ig34_p0013_a017 | p13 §2.5 "A Permissible variable should be used…" | ch02:85 | 否 | 是 | 是 (§2.5) | 未改 prose 对照 |
| S1 | ig34_p0362_a009 | p362 §6.4.1 第一条 "Previous versions…" 删除理由 + MHEVDTYP + CDASH | FA/assumptions.md:51 | 否 | 是 | 是 | 逐字, 全 7 句 |
| S2 | ig34_p0362_a008 | p362 §6.4.1 Criterion 3 正文 (AE 只存实际发生 / FAAE / RELREC) | FA/assumptions.md:49 | 否 | 是* | 是 | *PDF "Section 6.4.4.," → KB "6.4.4," = 登记 T-2 (PDF 自身可定), 非改义 |
| S3 | ig34_p0361_a013 | p361 §6.4.1 首段 (cannot be represented…or as SUPPQUAL; Not all findings…) | FA/assumptions.md:23 | 否 | 是 | 是 | 逐字 (T-1 引号字形) |
| S4 | ig34_p0363_a003 | p363 "Points to Consider" | FA/assumptions.md:57 | 否 | 是 | 是 | 逐字 (粗体) |
| S5 | ig34_p0363_a005 | p363 PtC 第 1 条 (some action during or after… meet Criterion 1) | FA/assumptions.md:61 | 否 | 是 | 是 | 逐字 |

**独有丢失 0/15, 忠实度错误 0** (主样本 0/10, 补抽 0/5).
复跑: `python3 -I $S/chk.py $S` / `python3 -I $S/chk2.py $S` (全原子在 PDF 页文本 = True; KB 行 == 原子; 所在 `##` 节核过).

### 附加: §6.4/§6.4.1 全量 (26 prose 原子)
`$S/sec641_full.txt`: 24/26 逐字 (T-1/T-2/T-5 归一后); 非逐字 2 = **原子抽错, KB 与 PDF 页文本一致**: p0361_a016 (原子漏 "so"; p361:39 有 "interval, so the"), p0362_a010 (原子多 "to"; p362:50 为 "thought be related" = T-4 照录).

### 10 格复核 (渲染 p370/371/373/374, `pdftoppm -r 110`)
seeded (`random.Random(20261126).sample(cells,7)` over Ex2 faae / Ex3 mh / Ex5 face / Ex6 CRF) + 指定 3:
Ex5 row11 FAORRES=N ✓; Ex5 row9 VISIT="VISIT 1" ✓; Ex2 row3 DOMAIN=FA ✓; Ex2 row6 FATEST="Number of Scabs Range" ✓; Ex3 row6 MHCAT="RHEUMATOID ARTHRITIS HISTORY" ✓; Ex5 row3 FAOBJ=Vomiting ✓; Ex3 row2 MHSEQ=2 ✓; Ex2 row3/row10 FATESTCD=**PAPRNG** ✓✓; Ex6 CRF Visit 2 格 "○ Mild ○ Moderate ○ Severe" ✓ + 表头两行结构 (首行 4 空 + 跨列 "At each visit…", 次行 AE ID…Visit 6) ✓. 另目视 Ex5 rows 3/6/9/13 **NUMEPISD** ✓, Ex3 mh row1 MHEVLINT 空 / row6 MHOCCUR=Y / MHSCAT "RHEUMATOID ARTHRITIS SYMPTOMS" ✓. **10/10 (+附加) 一致.**
顺序: Ex2 "Additional data…" 段在 ae.xpt 后 (p370) ✓; Ex4 Row 1/2 注释在 ae.xpt 前 (p372:34-37 → p373:1 ae.xpt) ✓; Ex1 "The time migraine medication" = p368:7 ✓.

### RELOCATE 源侧删除核
- 删除非空行 35 (ch02 25 + model/02 10); prose 27. 抽 10 (`random.Random(20261126).sample(prose,10)`, `$S/deleted_check.txt`): 10/10 逐字在 FA/assumptions.md, 10/10 在自身源 (ig34 p1-19 / sv20 全部页) 0 命中, 实际出处 ig34 p363-364.
- 扩为全量 (`$S/deleted_all.txt`): 27 prose 中 26 逐字在 FA 且自身源 0 命中; 1 条 = ch02 KB 自写引导句 ("The following content is reference material…") + 2 个 KB 自写标题, 随 RELOCATE 删除 (不留指针, 符合 dispatch). model/02 FATESTCD 小表 3 行在 FA/assumptions.md §6.4.3 保留; sv20 中 "Severity/Intensity"/"Toxicity Grade" 命中为变量标签偶合 (p17/20/31), 非此表.

### fp (独立跑; basekb = 当前 KB 副本仅换回本批 4 文件 base 版 → 排除他批噪声)
`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/basekb --out $S/fp_before.jsonl`; `… --out $S/fp_after.jsonl`; 比较 hit_target.
- hit_target 丢失 **26** = 23 target 迁移 (p0363_a011-a013,a015-a019; p0364_a001-a009; p0364_a011-a013,a017-a019; 全部 hit_any → FA/assumptions.md, a013 表头 → FA/examples.md) + 3 登记原子错误 (p0370_a021 T-7, p0373_a013 T-9, p0374_a011 Ex6 CRF 结构; 均在 `work/t1_errata.json:58-60`). **其他 0**; verdict 变化 0; 新增 hit_target 13.
- 与预期 (23 迁移 + 3 登记) 一致. writer 续 "27" 为把 a013 重复计 1 次, reviewer 已更正为 26, 本审计复现 26.
- `python3 tools/check_links.py` → live docs: 42 (= 基线).

### G-TB8
- trace: writer `oh-my-claudecode:executor` subagent_done (02:32:03Z, 续 03:04:26Z); reviewer `oh-my-claudecode:code-reviewer` CONDITIONAL (02:55:00Z) → 续复审 **PASS** (03:05:36Z), 晚于 writer 最后 KB 改动 (FA/*.md mtime 03:03:33Z).
- 当前 4 文件 md5 = writer 续 after = reviewer 续复审对象; 无 `agent: main` 写 KB 记录 (main 仅 user_ack / step_note). **G-TB8 PASS.**

### 观察 (不阻断)
- O-1: p0361_a016 / p0362_a010 原子抽错 (KB 正确) 与 p0373_a021 表头抽错未进 `t1_errata.json` (目前不在 fp 台账故无回归); 建议主控补登, 以免日后入账产生假回归.
- O-2: 主控需按 writer 提示把 23 条迁移原子的台账 targets 补 FA/assumptions.md (或 FA/examples.md for a013).

### 判定
独有丢失 0, 忠实度错误 0, 10 格 0 差, 删除源 10/10 (全量 26/26) 合规, fp 非预期 0, G-TB8 PASS → **B-FA auditor PASS**.
