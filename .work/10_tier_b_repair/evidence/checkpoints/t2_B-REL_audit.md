# T2 B-REL auditor checkpoint (attempt 1)
> agent: oh-my-claudecode:verifier (opus) | base 718c278 | 只审 domains/{RELREC,RELSUB,RELSPEC}/{assumptions,examples,spec}.md (9 文件) | 2026-11-26
> 先独立判 (pdf_pages p427-440 文本 + pdftoppm r110 渲染 p429/430/431/438/439/440), 判完才读 writer/reviewer checkpoint 对照.

## 抽样 (Rule A)
- 标准脚本 (`t2_auditor_v1.0.md`) 在本批退化: B-REL.json 的 atoms / t2_recheck / pdf_pages 全空 → C=0, P 只剩 triage 7 条 (p437/p440). 按主控指示改为从 9 文件对应 PDF prose 原子建 P.
- 命令 (仓外 scratch `S=<scratchpad>/t2_B-REL_auditor`): `python3 -I $S/pop.py .work/10_tier_b_repair > $S/sample.json` (在 `.work/10_tier_b_repair` 下跑)
  - P = ig34 原子, page 427-440, atom_type ∈ SENTENCE/LIST_ITEM/NOTE/CROSS_REF, 且 (§8 引言 p427 a013-a020 = IDVAR 段) 或 parent_section 匹配 `§8.(2|3|7|8)` / `REL(REC|SUB|SPEC) –`; 去 IE/ATOM_ERR/FIGURE/INTENTIONAL_EXCLUDE. (§8.1 / §8.4-8.6 / §9 不在本批文件.)
  - N = max(10, ceil(0.2×|P|)) 上限 30; `random.Random(20261126).sample(P, N)`
- 结果: **C=0, P=83, N=17**; 样本全为 P−C 对照.
- 另: P 全 83 条做了机检 (`python3 -I $S/match.py $S`, 归一化 dash/引号/粗体/列表号后子串匹配): **83/83 同时命中 REL 文件与 ch08**, 无一缺失 (输出 `$S/match_all.txt`).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0427_a017 | 427:31 §8 引言: IDVAR 可用变量引导句 | RELREC/assumptions.md:7 | 否 | 是 | 是 | §8 引言块位于 `## Relating Peer Records` 之前 (=PDF 顺序), 有 D6 说明行 |
| 2 | ig34_p0429_a004 | 429:7 §8.2: 每条相关记录加一条 RELREC 记录 + 唯一字符 ID | RELREC/assumptions.md:16 | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0429_a007 | 429:10 §8.2: 建议 RELID 用标准命名约定 (全字母/数字/大写) | RELREC/assumptions.md:16 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0429_a010 | 429:15 §8.2: 组记录可用 --GRPID 关联 | RELREC/assumptions.md:18 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0430_a017 | 430:20 §8.2.2 Ex2: 收集方式表明 CM/LB 与 AE 同一关系 | RELREC/examples.md:28 | 否 | 是 | 是 | 逐字, Example 2 下 |
| 6 | ig34_p0430_a034 | 430:42 §8.2.2: 更多例子见 §6.2.4 Disposition Ex4 与 §6.3.5.9.3 | RELREC/examples.md:53 | 否 | 是 | 是 | 交叉引用 2 处完整 |
| 7 | ig34_p0431_a004 | 431:4 §8.3.1: 数据集间关系 USUBJID/IDVARVAL 为空 | RELREC/examples.md:59 | 否 | 是 | 是 | Dataset Relationship Example 下 |
| 8 | ig34_p0431_a012 | 431:11 §8.3.1: 两数据集 --LNKID 值由 sponsor 定义 | RELREC/examples.md:68 | 否 | 是 | 是 | 逐字 (PDF 非断连字符已归一) |
| 9 | ig34_p0431_a015 | 431:18 §8.3.1: RELTYPE 允许值 ONE/MANY (CT expected) | RELREC/assumptions.md:38 | 否 | 是 | 是 (注) | 位于 `## Relating Datasets` 下 §8.3 两段之后; §8.3.1 例表+操作库段在 examples.md. 跨文件拆分为既有结构, 主控/reviewer 已裁可接受; Source 行声明 §8.3.1 |
| 10 | ig34_p0431_a021 | 431:31 §8.3.1: IDVAR 是跨数据集合并键, 故 --SEQ 不能用 | RELREC/assumptions.md:46 | 否 | 是 | 是 (注) | 本批新增句, 逐字; 位置同 #9 |
| 11 | ig34_p0431_a022 | 431:32 §8.3.1: --SEQ 只在受试者/数据集内有意义 | RELREC/assumptions.md:46 | 否 | 是 | 是 (注) | 同上 |
| 12 | ig34_p0437_a015 | 437:42 §8.7: RELSUB 描述句 | RELSUB/assumptions.md:7 | 否 | 是 | 是 | `## RELSUB – Description/Overview` 下 |
| 13 | ig34_p0438_a003 | 438:2 §8.7: spec 首句 relsub.xpt, Related Subjects — Relationship | RELSUB/assumptions.md:13 | 否 | 是 | 是 | `## RELSUB – Specification` 下, 含 "One record per … Tabulation." |
| 14 | ig34_p0438_a016 | 438:37 RELSUB 假设 4: 无 POOLID 时 USUBJID 每条必填 | RELSUB/assumptions.md:23 | 否 | 是 | 是 | 编号 4 一致 |
| 15 | ig34_p0439_a012 | 439:14 RELSUB 例: 表对应上表 3 名受试者 | RELSUB/examples.md:23 | 否 | 是 | 是 | 逐字 |
| 16 | ig34_p0440_a004 | 440:5 RELSPEC 假设 3: 3 个 codelist SPEC/SPECTYPE/GENSMP + C-code | RELSPEC/assumptions.md:21 | 否 | 是 | 是 | C77529/C78734/C111114 一致 |
| 17 | ig34_p0440_a008 | 440:12 RELSPEC 图题 "Figure. Sample Specimen Relationship" | RELSPEC/examples.md:9 | 否 | 是 | 是 | 图题逐字; Mermaid 对渲染 p440 核: 节点 6 (含 SPC-003 "(Brain)")、边 4、Level 1/2/3 行标题均一致, D6 标注在 :11 |

**独有信息丢失 0 / 忠实度错误 0.**

## ch08 交叉核 (5 句, 取自样本)
#1 p427_a017 → ch08:18; #2 p429_a004 → ch08:67; #9 p431_a015 → ch08:169; #12 p437_a015 → ch08:343; #16 p440_a004 → ch08:435 — 三方 (PDF/域文件/ch08) 归一化后逐字一致. 全 83 条亦同时命中 ch08 (match_all.txt), 无冲突.

## 表格 / spec 10 格复核 (seed 20261126 随机, 对渲染页目视)
| # | 位置 | KB 值 | PDF (渲染) | 结果 |
|---|------|------|-----------|------|
| 1 | RELSUB/examples dm R1 USUBJID | HEM021-001 | p439 同 | ✓ |
| 2 | RELREC/examples 8.3.1 R2 RDOMAIN | TR | p431 同 | ✓ |
| 3 | RELREC/examples Ex1 R2 RDOMAIN | CM | p430 同 | ✓ |
| 4 | RELSUB/examples relsub R5 SREL | CHILD, BIOLOGICAL | p439 同 | ✓ |
| 5 | RELSPEC/examples R2 USUBJID | 001-01 | p440 同 | ✓ |
| 6 | RELREC/examples Ex1 R3 RELID | 1 | p430 同 | ✓ |
| 7 | RELREC/examples Ex2 R5 IDVARVAL | 48 | p430 同 | ✓ |
| 8 | RELREC/spec RELID CDISC Notes | "Unique value within USUBJID … related/associated domain records." | p429 同 (3 句) | ✓ |
| 9 | RELSPEC/spec USUBJID Role | Identifier | p439 同 | ✓ |
| 10 | RELREC/spec IDVARVAL Core | Exp | p429 同 | ✓ |
(格抽取命令: 解析 3 个 examples.md 的 7 张表 = 200 格 + 3 spec.md 108 字段, `random.Random(20261126)` 抽 7 格 + 3 字段.) 另目视: 7 张表行数/空格位置 (RELTYPE 空、8.3.1 USUBJID/IDVARVAL 空、RELSPEC R1/R5 PARENT 空) 全一致.

## RELOCATE / 删除核 (vs 718c278)
- 句级 diff (旧句集 − 新句集) 仅 7 条, 全部为替换为 PDF 原文, 无丢信息:
  RELREC/assumptions: 旧首段括注 "(relating peer records)/(relating datasets)" → PDF "(as described in this section)/(as described in Section 8.3, …)"; --REFID 截断 2 句 → 全文; --GRPID 节名错 → "Within a Domain Using the --GRPID Variable". RELSPEC/assumptions "it does" → 照录 PDF "is does" (T-7). RELSPEC/examples KB 自写图题 → PDF 图题. RELSUB/examples "relationships of the mother" → PDF "relationship".
- RELOCATE 2 次 (§8.2 首两段移到 `## Relating Peer Records` 下; §8 引言 IDVAR 块移到该标题前): 移后文字与 PDF 逐字, 无指针, 无残留重复.

## 其他观察 (不阻断)
- RELSUB 假设 7 末尾句号 KB 有 / PDF 无 = 已登记 T-9 (与 ch08 同).
- RELREC/assumptions:5 D6 行措辞 "KB note (not in SDTMIG): the next paragraph and list are from the SDTMIG v3.4 §8 introduction" — 说明行本身为 KB 自写导航, 合规; 但前缀 "not in SDTMIG" 与 "are from SDTMIG" 字面易误读, 可在 T4 统一措辞 (LOW).
- spec.md: IDVAR CT "*" 记为空、codelist 名→C-code、脚注 ¹ 缺 = O24/O15 已延后, 不判.

## 隔离 fp 回归 / 链接
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → 全局 RED 48 条 (他批在途: p118-p396), **ig34 p427-440 回归 0**, regress 中 `domains/REL` 0.
- `python3 tools/check_links.py | grep live` → `live docs: 42` (= 基线).

## G-TB8
- trace: writer `oh-my-claudecode:executor` subagent_done ×3 (03:16:21, 03:17:48, 03:24:46); reviewer `oh-my-claudecode:code-reviewer` CONDITIONAL (03:23:52) → **终态签字 PASS (03:25:27, 在 writer 最后改动 03:24:46 之后)**; 无 `agent: main` 写 KB 记录.
- md5 现值 = reviewer 终签值: RELREC/assumptions 69882fb2…; 其余 8 文件 = writer checkpoint after 列 (e88209df / db68fb45 / c4e13086 / ec54eaa9 / 45c30171 / 92e92ac4 / c3da4fad / fdc93ad0) ✓.
- 判后对照 writer/reviewer checkpoint: 结论一致, 无新增分歧.

## 判定: **PASS** (Rule A N=17 seed=20261126: 丢失 0 / 忠实 0; 全 83 prose 机检 0 缺; 10 格 0 差; RELOCATE 无损; fp REL 回归 0; G-TB8 ✓)
