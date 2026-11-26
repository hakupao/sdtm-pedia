# T2S.S-TUFA Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-TUFA.md` / `t2_S-TUFA_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TUFA_auditor/`

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (N=30).

## 抽样 (可复跑; repo 根执行 `python3 -I $S/sample.py`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW}, 页与 parent_section 前缀:
    TR 350-353 ("§6.3.12.2" / "TR –"); §6.3.12.3 共用例 353-358 ("§6.3.12.3");
    FA 361-375 ("§6.4 Findings" / "§6.4.1" / "§6.4.2" / "§6.4.3" / "§6.4.4" / "FA –")  ← 含 FA 顶 §6.4-§6.4.3 引言 (json intros 为空, 按任务 p361-375 并入);
    SR 375-381 ("§6.4.5" / "SR –"); 边界页别节 (TU 349 / VS 358-361 / §7 382) 排除; 减 ledger INTENTIONAL_EXCLUDE 38.
C = P 中落在 writer 改动页的原子; 改动页 = S-TUFA.writer.jsonl 中 action ∈ {INSERTED, REPLACED, MOVED} 的 pdf_page = {350, 352, 365, 366, 377}
    (比 S-EVT 先例更严: census VERIFIED / SKIPPED 行不算改动).
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 506, |C| = 72, N = 30 (改动页 10 + 其余 20), seed = 20261126.

## 样本判定 (TABLE_ROW 渲染 90dpi 逐格: p355/365/368/369/371/377/378/380; spec 行另对 pdftotext -layout 逐列)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0366_a019 | 366: FA asm 4a CV codetable + URL | FA/assumptions.md:112 | 否 | 是 | 是 | 移位后在 `## FA – Assumptions` 下, 逐字 |
| 2 | ig34_p0366_a015 | 366: FA asm 1 | FA/assumptions.md:105 | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0350_a007 | 350: TR Desc bullet "a unique … ID value" | TR/assumptions.md:9 | 否 | 是 | 是 | 本批恢复 5 项 bullet |
| 4 | ig34_p0350_a013 | 350: TR 不含解剖位置 (避免与 TU 重复) | TR/assumptions.md:15 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0365_a017 | 365: spec FAORRESU 行 | FA/spec.md:113-120 | 否 | 是 | 是 | CT (UNIT) → C71620 = U5 归 S-CT, 不计 |
| 6 | ig34_p0365_a021 | 365: spec FASTAT 行 | FA/spec.md:149-156 | 否 | 是 | 是 | CT (ND) → C66789 = U5 |
| 7 | ig34_p0352_a010 | 352: TR asm 4 Note 例外 4.1.5.1 | TR/assumptions.md:35 | 否 | 是 | 是 | 粗体 Note = 排版 |
| 8 | ig34_p0377_a012 | 377: spec SRDY 行 | SR/spec.md:302-309 | 否 | 是 | 是 | 含 PDF "sponsor- defined" 原样 |
| 9 | ig34_p0350_a018 | 350: spec STUDYID 行 | TR/spec.md:5-12 | 否 | 是 | 是 | |
| 10 | ig34_p0352_a007 | 352: TR asm 4 标准化 TOO SMALL TO MEASURE | TR/assumptions.md:29 | 否 | 是 | 是 | 开引号直/弯差 = 排版 (S-TYPO) |
| 11 | ig34_p0362_a005 | 362: Criterion 2 标题句 | FA/assumptions.md:29 | 否 | 是 | 是 | 逐字 |
| 12 | ig34_p0356_a023 | 356: Ex3 TR 独立评估者叙述 | TR/examples.md:58 | 否 | 是 | 是 | 逐字 |
| 13 | ig34_p0369_a001 | 369: face r10 Aura OCCUR 30M | FA/examples.md:56 | 否 | 是 | 是 | 渲染 17 格一致 |
| 14 | ig34_p0375_a008 | 375: Ex6 FAOBJ 取自 AEDECOD / FASPID / FAEVINTX | FA/examples.md:298 | 否 | 是 | 是 | 逐字 |
| 15 | ig34_p0354_a013 | 354: TU Ex2 Rows 7-8 肿瘤分裂 | TU/examples.md:49 | 否 | 是 | 是 | 共用例 TU 部分 (TU FINAL, 只读对照) |
| 16 | ig34_p0368_a019 | 368: face r6 SEV MODERATE 30M | FA/examples.md:52 | 否 | 是 | 是 | 渲染逐格 |
| 17 | ig34_p0371_a023 | 371: mh r6 EARLY MORNING STIFFNESS | FA/examples.md:160 | 否 | 是 | 是 | 渲染 16 格一致 (MHSEV 空) |
| 18 | ig34_p0380_a030 | 380: SR Ex3 r2 BLISTIND | SR/examples.md:98 | 否 | 是 | 是 | 渲染逐格 (SRMETHOD 空) |
| 19 | ig34_p0369_a018 | 369: Rash CRF "Lesion type and count" | FA/examples.md:81 | 否 | 是 | 是 | 渲染 |
| 20 | ig34_p0378_a012 | 378: SR Ex1 r2 SITE2 Histamine 4 mm | SR/examples.md:17 | 否 | 是 | 是 | 渲染逐格 |
| 21 | ig34_p0364_a008 | 364: §6.4.2 前缀用 2 字符域码 | FA/assumptions.md:73 | 否 | 是 | 是 | 三级子项 |
| 22 | ig34_p0364_a002 | 364: §6.4.2 "3. Separate domains where:" | FA/assumptions.md:67 | 否 | 是 | 是 | |
| 23 | ig34_p0372_a027 | 372: "Note that not all AE expected variables…" | FA/examples.md:203 | 否 | 是 | 是 | 顺序同 PDF (Row 1 之前) |
| 24 | ig34_p0363_a007 | 363: PtC 分组 FAGRPID/FACAT/FASCAT | FA/assumptions.md:49 | 否 | 是 | 是 | 逐字 |
| 25 | ig34_p0363_a009 | 363: PtC 多评估者 FAEVALID | FA/assumptions.md:51 | 否 | 是 | 是 | "may provided" = B-FA T-6 照录 |
| 26 | ig34_p0355_a023 | 355: tr r22 NT02 TUMSTATE WEEK 6 | TR/examples.md:39 | 否 | 是 | 是 | KB Row/TRSEQ 21 = B-TR T-1 (PDF 跳 12; 叙述 Rows 9-21/22-27 佐证); 其余格渲染一致 |
| 27 | ig34_p0367_a010 | 367: Ex1 CRF "When was study treatment taken?" | FA/examples.md:11 | 否 | 是 | 是 | |
| 28 | ig34_p0377_a015 | 377: spec SRELTM 行 | SR/spec.md:329-336 | 否 | 是 | 是 | PDF "EGTPTREF" → KB SRTPTREF = 已登记 B-SR T-4 keep-correct |
| 29 | ig34_p0352_a004 | 352: TR asm 1 TRLNKID/RELREC | TR/assumptions.md:23 | 否 | 是 | 是 | 逐字 |
| 30 | ig34_p0369_a020 | 369: Rash CRF Papules 6 选项 ○ | FA/examples.md:83 | 否 | 是 | 是 | 渲染 ○ 照录 |

独有丢失 0 / 30; 忠实度错误 0 / 30; 位置错误 0.

## 另查
- **gaps**: TR DSAF — `## TR – Description/Overview` (:3) / `## TR – Specification` + tr.xpt 首句 (:17-19, 对 p350 逐字) / `## TR – Assumptions` (:21) / 脚注 TR/spec.md:294; FA AF — `## FA – Assumptions` (:103) + 脚注 FA/spec.md:276; SR F — SR/spec.md:357. 三处脚注逐字同 p352/p366/p377, 均在最后变量块 `---` 之后、`## Cross References` 之前 (U7), 写法同 AE/DS 先例. ✔
- **FA 假设 1-6 移位**: HEAD :3-15 与现 :105-117 逐行全等 (`python3` 比对 True), 唯一新增行 = `## FA – Assumptions`; 新位置在 `FA – Specification` 首句之后、§6.4.5 之前 = PDF p366-367 顺序. 文件顶无残留. ✔
- **intros (json 空)**: FA 顶 §6.4-§6.4.3 (p361-364) 已在样本 11/21/22/24/25 覆盖, 并经反向扫; 仅 B-FA T-2 ("6.4.4.,"→"6.4.4,") / T-5 ("e.g,"→"e.g.,") 已登记改正值.
- **CT `*`**: pdftotext -layout p350-352 / p365-366 / p376-377 CT 列为 `*` 的变量 = FACAT/FASCAT (2), KB `Controlled Terms:** *` 恰为此 2; TR/SR 无 `*`. ✔
- **TR 列表恢复**: p350 冒号 + 5 项 • → KB :7-13 逐字; 旧 KB 自加 "and" 已去. ✔
- **反向 KB→PDF 全文件扫** (9 文件, `python3 -I $S/reverse.py` layout 版 + 内联 raw 版 `rev2.out`): 未命中全部可归类 — (a) 导航: TR/ex:3 "TU and TR share examples. See also …" (与 TU FINAL 同形, B-TU/B-TR review 认可为导航), FA/asm:121 §6.4.5 交叉引用, spec `> Class|Structure` 行与 Cross References 块 (U8), spec `Order` 字段; (b) U5 C-code; (c) 已登记 PDF_TYPO keep-correct: FA/ex:118 B-FA T-7 (parent CE→AE), FA/ex:228 T-9 (FAEVINTX→FAEVLINT), SR/asm:15 SR T-3 (reactogencity), SR/spec:336 T-4, SR/ex:22 T-1 (BAU mL); (d) D6 已标: FA/ex:283; (e) pdftotext 折行/跨列伪阴性 (TR spec EPOCH/TRDTC/TRDY, FA spec VISITDY/TAETORD, SR spec SRTEST/SRSTRESN 标签, FA Ex1 90M POST-DOSE, ○ 选项组; 逐一对 layout 文本目视一致). 无 PDF 出处且未 D6 的行 = 0.
- **授权范围**: `git diff HEAD --stat -- knowledge_base/domains/{TR,FA,SR,TU}` 仅 FA/assumptions.md, FA/spec.md, SR/spec.md, TR/assumptions.md, TR/spec.md (∈ kb_files), TU 0, narrow_files 空. ✔
- **G-TB8**: trace 有 writer (executor) 07:28:07Z + delta 07:28:48Z (KB 未改)、reviewer (code-reviewer, PASS) 07:36:54Z; 本批 5 个改动文件 mtime 最晚 07:24:16Z < reviewer 完成; 无 agent main 写 KB. ✔
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).

## 观察 (不计缺陷)
- FA/assumptions.md:95 `## §6.4.4 FA – Description/Overview` 合并了 PDF §6.4.4 节标题 "Findings About Events or Interventions (FA)" 与 Desc 小标题 (标题类, B-FA N-2 既有; 规则 6 不改).
- TR/spec.md TAETORD Notes 与 Label 不符 = PDF p351 原文, KB 照录 (writer delta 登记 TR T-5, T4 待用户裁).

## 对照 writer / reviewer (判完后读)
与 writer 报告 (KB→PDF 无出处行分类、需主控定 3 项) 及 reviewer PASS (6 LOW) 结论一致; FA 假设移位、CT `*` 2/2、脚注位置、T-n 清单无分歧.
