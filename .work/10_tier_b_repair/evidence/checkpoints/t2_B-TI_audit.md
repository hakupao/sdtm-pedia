# T2 B-TI auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26T05:12:32Z, oh-my-claudecode:verifier / opus)

- 先独立判 (只读 PDF 页文本 + KB 现文件 + `git diff HEAD`), 判完才对照 writer 报告 `t2_B-TI.md` / reviewer 结论.
- 抽样脚本: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_auditor/sample.py` (= t2_auditor_v1.0 模板, 两处按 brief 覆盖: files += `TI/assumptions.md` (本批实际改动); 页范围 = p415 a025+ (§7.4 引言) / p416 全 / p417 a001-a015 (TI, 排除 TS 原子) / p425 a026+ (§7.5, 排除 NullFlavor 段) / p426 全).
  复跑: `cd <repo> && python3 -I <scratch>/sample.py`
- seed = 20261126; C = 1; P = 33 (X 排除 a012 spec 首句 / a022 spec 脚注; OTH 0); N = 10.
- 样本: ig34_p0416_a006, p0426_a006, p0415_a027, p0425_a029, p0425_a031, p0415_a028, p0416_a024, p0416_a025, p0425_a030, p0416_a008.
- 机械匹配 (P 全 33 + a012; 规范化空白/弯引号/列表编号): `python3 -I <scratch>/check.py <scratch>` → 31 HIT 精确单处; 3 MISS = p417 a005-a007 (examples.md): a005 = T-1 (PDF "a trial that with", KB "a trial with", 已登记), a006/a007 = `**Rows 1-3:**` / `**Rows 4-6:**` 加粗标记差异, 文字逐字一致 (人工核 examples.md:7,9).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0416_a006 | 416 Description 首句 "A trial design domain … each of the I/E criteria for the trial" | TI/assumptions.md:18 | 否 | 是 | 是 | REAL_GAP 已补, 逐字; 位于 `## TI – Description/Overview` 下 (U+2013 与 PDF 同) |
| 2 | ig34_p0426_a006 | 426 §7.5 step 9 oncology / disease assessments → TD dataset | TI/assumptions.md:50 | 否 | 是 | 是 | 逐字, 未改动行 |
| 3 | ig34_p0415_a027 | 415 末 §7.4 bullet 1 eligibility criteria (Section 7.4.1 …) | TI/assumptions.md:7 | 否 | 是 | 是 | 逐字含交叉引用 |
| 4 | ig34_p0425_a029 | 425 §7.5 引言第 3 句 "Some steps will overlap; …" | TI/assumptions.md:40 | 否 | 是 | 是 | 合段后与 a027/a028 同段, 顺序同 PDF |
| 5 | ig34_p0425_a031 | 425 §7.5 step 2 decision rule / randomization | TI/assumptions.md:43 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0415_a028 | 415 末 §7.4 bullet 2 characteristics (Section 7.4.2 …) | TI/assumptions.md:8 | 否 | 是 | 是 | 逐字 |
| 7 | ig34_p0416_a024 | 416 Assumption 1 amended criteria / TIVERS | TI/assumptions.md:28 | 否 | 是 | 是 | 现紧接 `## TI – Assumptions` (:26), PDF 顺序 |
| 8 | ig34_p0416_a025 | 416 Assumption 2 protocol versions 1-4 例 | TI/assumptions.md:30 | 否 | 是 | 是 | 逐字含数值 |
| 9 | ig34_p0425_a030 | 425 §7.5 step 1 flow chart / schema | TI/assumptions.md:42 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0416_a008 | 416 Description 第 2 段 "TI contains all the I/E criteria …" | TI/assumptions.md:20 | 否 | 是 | 是 | RELOCATE: 与 HEAD 行逐字相同 (diff 空), 由 Assumptions 下归到 Description/Overview 第 2 段 = PDF p416 位置 |

- **独有丢失 0 / 忠实度错误 0 → PASS**.
- 额外核:
  - RELOCATE 2 段: `diff <(git show HEAD:… | grep -F "<段首>") <(grep -F "<段首>" …)` 两段均 IDENTICAL; 位置 = PDF p416 顺序 (TIRL 标题 → TIRL 段 → Description/Overview → a006/a007 → a008/a009 → Specification → Assumptions).
  - 新增 3 标题 + spec 首句 (:12/:16/:22/:24/:26) 与 PDF p416 码位一致 (标题 U+2013, spec 句 U+2014); a012 spec 首句逐字 HIT :24.
  - §7.5 引言合 1 段 (:40): a027/a028/a029 三句文字未改, 顺序同 PDF p425.
  - 授权范围: `git diff HEAD -- knowledge_base/domains/TI/` 只动 assumptions.md (标题/Description/spec 首句/归节/合段); examples.md md5 `9ee76513…` = writer 记录 (未改); spec.md 未在 status 中.
  - 已登记不计: T-1 (p417 "that with"), O48 (§7.4 标题 "(TI, TS)" vs PDF "(TI and TS)" / census 页偏移), O40 (step 6 弯引号).
- G-TB8: trace 中 T2.B-TI 有 executor subagent_done ×2 (05:06:32Z, 05:07:24Z) 与 code-reviewer PASS (05:10:38Z); 无 `agent: main` 记录; assumptions.md mtime 05:07:12Z < reviewer 完成时间 → 终态经 reviewer. md5 `cf4905bc…` = writer a2 记录.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (基线 42).
- 对照 writer/reviewer: 结论一致, 无分歧.
