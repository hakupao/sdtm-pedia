# T2 B-SR auditor checkpoint (attempt 1)
> agent: oh-my-claudecode:verifier (opus) | base c8802bf (SR/FA 在 c8802bf..HEAD 无提交) | 只审 SR/{examples,assumptions,spec}.md + FA/assumptions.md | 2026-11-26
> 先独立判 (PDF 文本 + 渲染 p376-380 r110), 判完才读 writer/reviewer checkpoint 对照.

## 抽样 (Rule A)
- 命令: `subagent_prompts/t2_auditor_v1.0.md` 抽样脚本原样, b="B-SR", seed=20261126, 在 repo 根跑; 输出 `<scratchpad>/t2_B-SR_auditor/sample.json` (仓库外)
- 结果: C=0 (本批 atoms/t2_recheck 均 0, 改动全来自 census + R3 新增), P=14, N=10; 样本全部来自 P−C (对照)
- P 余下 4 条 (p0378_a006 / a020, p0380_a001 / a025) 也逐条核过, 均逐字一致 (未计入 N).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0378_a021 | 378 下: Ex2 Rows 1-6 描述+等级, 等级存 SRSTRESC | SR/examples.md:29 | 否 | 是 | 是 | 逐字一致 |
| 2 | ig34_p0380_a032 | 380 下: 皮试给药记在 AG 域 | SR/examples.md:101 | 否 | 是 | 是 | 逐字一致 |
| 3 | ig34_p0378_a001 | 378 上: 假设 3, SROBJ 表示每条反应的测试物; 评估方法 skin-prick/scratch/其他 | SR/assumptions.md:17 | 否 | 是 | 是 | 逐字一致, 位于 `## SR – Assumptions` 下 |
| 4 | ig34_p0380_a023 | 380 中: Ex3 叙述 (PPD/Mantoux, 48h 计划, 53h56m 实际) | SR/examples.md:87 | 否 | 是 | 是 | 逐字一致; 含本批恢复的 "standard tuberculin PPD" 与 "The time point variables show" (writer N-1/N-2) |
| 5 | ig34_p0378_a002 | 378 上: 假设 4, 可加变量 + 16 个不常用 qualifier 列表 | SR/assumptions.md:19 | 否 | 是 | 是 | 16 个 qualifier 逐个一致 |
| 6 | ig34_p0378_a007 | 378 上: Ex1 Rows 5-8 Johnson grass IgE 剂量反应, 见 SROBJ | SR/examples.md:8 | 否 | 是 | 是 | 逐字一致 |
| 7 | ig34_p0378_a008 | 378 上: 所有行背部位置 (SITE1) 用 FOCID | SR/examples.md:10 | 否 | 是 | 是 | 逐字一致 |
| 8 | ig34_p0380_a026 | 380 中: Row 3 判读, SRGRPID 关联结果与判读 | SR/examples.md:91 | 否 | 是 | 是 | 逐字一致 |
| 9 | ig34_p0380_a024 | 380 中: Row 1 硬结最长径, 0.1 mL 含 5TU PPD-S 左前臂 | SR/examples.md:89 | 否 | 是 | 是 | 数值 0.1 mL / 5TU 一致 |
| 10 | ig34_p0378_a005 | 378 上: Ex1 受试者接受递增浓度 Johnson grass IgE | SR/examples.md:5 | 否 | 是 | 是 | 逐字一致 |

**独有信息丢失 0 / 忠实度错误 0.**

## 定向补核: 新增 Description / Specification (不在 P 的 atoms, 主控指定)
| 项 | PDF | KB | 结果 |
|---|---|---|---|
| `## SR – Description/Overview` + 定义句 (dermal responses to antigens) | p375 末 (标题+1 句) | SR/assumptions.md:3,:5 | 逐字一致 |
| `## SR – Specification` + `sr.xpt, Skin Response — Findings About. One record per finding, per object, per time point, per visit per subject, Tabulation.` | p376 顶 | SR/assumptions.md:7,:9 | 逐字一致 (含 em dash), 位置同 CM/IS/MH 先例 |
| `## SR – Assumptions` 标题 | p377 中 | SR/assumptions.md:11 | 一致; 假设 1-2 (:13/:15) 对 p377 逐字, :15 `reactogenicity` = PDF `reactogencity` 拼写错 keep-correct (T-3) |

## 10 seeded 表格格 (seed 20261126, `random.sample` 6 examples 格 + 4 spec 字段; 渲染 r110 + layout 文本)
| # | KB loc | 格 | KB 值 | PDF | 结果 |
|---|---|---|---|---|---|
| 1 | examples.md:82 | Ex2 relrec Row17 STUDYID | CC-001 | p380 渲染 | 一致 |
| 2 | examples.md:77 | Ex2 relrec Row12 IDVARVAL | 4 | p380 渲染 (EX EXSPID 4 R4) | 一致 |
| 3 | examples.md:18 | Ex1 sr Row3 STUDYID | SPI-001 | p378 | 一致 |
| 4 | examples.md:21 | Ex1 sr Row6 USUBJID | SPI-001-11035 | p378 (折行 SPI-001-/11035) | 一致 |
| 5 | examples.md:46 | Ex2 sr Row11 SRSTRESC | 1 | p379 渲染 | 一致 |
| 6 | examples.md:54 | ex Row2 EXSPID | 2 | p379 渲染 | 一致 |
| 7 | spec.md:153 | SRSTRESU Controlled Terms | C71620 | p376 `(UNIT)`; KB terminology `## Unit (C71620)` | 一致 (全库 C-code 惯例) |
| 8 | spec.md:198 | SRLOC Controlled Terms | C74456 | p376 `(LOC)`; terminology `## Anatomical Location (C74456)` | 一致 |
| 9 | spec.md:73 | SRTESTCD Role | Topic | p376 | 一致 |
| 10 | spec.md:272 | VISITDY Core | Perm | p377 | 一致 |
另核改动格 (非 seeded, 渲染 p380): Ex2 relrec Row1-18 全部 (SR,SR,EX 序) 一致; Ex3 Row1 SRTESTCD `IDRLDIAM`、Row1-3 SRDTC `2011-01-19T14:08:24`、ag AGTRT `Tuberculin PPD-S` 一致.

## diff 范围核
- `git diff c8802bf -- knowledge_base/domains/SR knowledge_base/domains/FA/assumptions.md`: 4 文件, +25/−13.
- FA/assumptions.md: 只在 `## §6.4.5 Skin Response (SR)` 下加 1 空行 + `> See [SR – Assumptions](../SR/assumptions.md) for §6.4.5 Skin Response.` 一行 (目标文件存在), 无其他改动. **确认.**
- spec.md 只 2 处: :93 `BAU mL`→`BAU/mL` (T-1, PDF p378 同表 Row5/6/8 定值) 与 :336 `EGTPTREF`→`SRTPTREF` (T-4, 同注释前句/第二例 = SRTPTREF). 均为已登记 PDF_TYPO keep-correct, 非忠实度错误.
- T-2 (Ex3 SRDTC): KB 现照录 PDF 表值 14:08:24, 叙述 "53 hours and 56 minutes" 照录 → PDF 自相矛盾, KB 不再含 PDF 无出处的旧值 14:26; 已登记 T4 用户裁定项. 不计错误.

## 独立复跑
- 隔离 fp: `$S/b = git archive HEAD knowledge_base`; `$S/a = b + 本批 4 文件` (`diff -rq` 仅 4 文件不同); `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/b/knowledge_base --out $S/fpb.jsonl`; `... --kb-root $S/a/knowledge_base --out $S/fpa.jsonl --baseline $S/fpb.jsonl --regress-out $S/fpr.jsonl` → `regressions=0 new_hits=0 RESULT: GREEN`
- `python3 tools/check_links.py | tail -1` 附近 → `broken relative links: 18668 (live docs: 42)` (基线 42, 不升)

## G-TB8
- trace 本批: writer `oh-my-claudecode:executor` subagent_done ×3 (03:15:27 / 03:18:21 续 / 03:22:16 续2); reviewer `oh-my-claudecode:code-reviewer` PASS ×2 (03:21:08 / 03:22:53 续签字). reviewer 续签字晚于 writer 最后一次改动 (续2 spec.md:336) → 终态经 reviewer. **满足.**
- trace 中 `agent: main` 记录全部为 user_ack / step_note (T0-T1.4, B-PCPP), 无 T2.B-SR 的 main 写 KB 记录. **满足.**
- auditor ≠ writer ≠ reviewer (verifier / executor / code-reviewer). 规则 D 满足.

## 观察 (不影响判定)
- O-6 (writer 已登记): spec.md DOMAIN CT `SR` 空、无 spec 表脚注 "1 In this column, an asterisk…" — 全库 spec.md 惯例, 交 O15/O16.
- T-2 需主控并入 T4 用户裁定清单 (reviewer 已提).

## 判定: **PASS** (Rule A N=10 seed=20261126: 丢失 0 / 忠实 0; 定向补核 3 项 0 差; 10 seeded 格 0 差; fp 隔离回归 0; live docs 42; G-TB8 满足)
