# T2 B-TU auditor — Rule A 独立抽检

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

- 基线: `git diff HEAD -- knowledge_base/domains/TU/` (HEAD=884560f; 本批改动未提交). 只看 kb_files `TU/assumptions.md`, `TU/examples.md`.
- 抽样页范围 (dispatch notes "抽样页范围"): TU 节完整 PDF 页 = p344-349 (§6.3.12 引言 / §6.3.12.1 TU Description/Spec/Assumptions) + p353-358 (§6.3.12.3 TU/TR 共享例节); 排除同页 SS / TR Assumptions / VS 节原子.
- 抽样脚本: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TU_auditor/sample.py` (= 模板脚本, 仅把 `pdf_pages` 换成上述 PAGES 集合 + parent_section 过滤 TU/§6.3.12/§6.3.12.1/§6.3.12.3); 复跑: `python3 -I <该脚本>` (cwd=repo 根).
- seed = 20261126; C = 0 (本批 4 atoms 全为 TABLE_ROW, t2_recheck 0); P = 74; N = 10 (全部来自 P−C).
- 独立判定先于对照 writer/reviewer 报告; 真值 = `work/pdf_pages/ig34_p0NNN.txt`.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0354_a033 | p354 Ex2 TR 段 "Rows 1-8: Show the measurements of the target tumors… at the screening visit" | `TR/examples.md:9` | 否 | 是 | 是 | 共享例节 TR 部分, KB 放 TR/examples (Example 2 continued); 非本批 kb_files, 存在且逐字 |
| 2 | ig34_p0354_a012 | p354 Ex2 "Rows 1-6: Show for subject 44444 the target and non-target tumors identified by the investigator at the screening visit" | `TU/examples.md:47` | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0345_a001 | p345 Description bullet "anatomical location of the tumor" | `TU/assumptions.md:16` | 否 | 是 | 是 | TU – Description/Overview 列表 |
| 4 | ig34_p0346_a018 | p346 Assumption 1.b split 后 post-baseline 记录 | `TU/assumptions.md:29` | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0348_a010 | p348 Assumption 9 indicator questions (3 个 e.g. 问句 + "do not introduce them into TU") | `TU/assumptions.md:76` | 否 | 是 | 是 | PDF 文本层 "TUTESTs"; 原子 verbatim 作 "TUTEST" (抽取差), KB 随 PDF |
| 6 | ig34_p0349_a006 | p349 Assumption 10 例 "disease recurrence data in an adjuvant breast cancer study … left breast only" | `TU/assumptions.md:96` | 否 | 是 | 是 | 逐字, 同段后续 3 句亦齐 |
| 7 | ig34_p0348_a001 | p348 Assumption 6 "The TU record may contain different levels of detail…" | `TU/assumptions.md:67` | 否 | 是 | 是 | 逐字 |
| 8 | ig34_p0356_a023 | p356 Ex3 "TR shows assessments provided by an independent assessor as opposed to the principal investigator" | `TR/examples.md:58` | 否 | 是 | 是 | 共享例节 TR 部分 (Example 3 continued); 非本批 kb_files, 存在且逐字 |
| 9 | ig34_p0347_a003 | p347 Assumption 2 第 2 段 CT 句 "…CDISC CT includes codelists for use with TUORRES" | `TU/assumptions.md:34` | 否 | 是 | 是 | 原子 verbatim 作 "TULORRES", PDF 文本层为 "TUORRES" → 原子抽取错, KB 与 PDF 一致 |
| 10 | ig34_p0353_a011 | p353 Ex1 "Rows 4-5: Show the target graft lesion located in the left femoro-popliteal graft…" | `TU/examples.md:17` | 否 | 是 | 是 | 逐字 |

- 独有信息丢失: **0/10**; 忠实度错误: **0**; 位置错误: 0.
- 补查 (非抽样, 本批 R3 新增叙述逐字对 PDF): §6.3.12 引言段 (p344) → `TU/assumptions.md:5` 逐字; `## 6.3.12.1` / `## TU – Specification` / `## TU – Assumptions` 标题与 PDF 节结构一致; spec 首句 (p345) → `:23` 逐字; Assumption 2 合段 + "a tumor/lesion might split" (删 KB 自写 "identified at baseline", p347) → `:34` 与 PDF 一致; Assumption 3 拆出 "This example represents tumors assessed by location of interest." (p347) → `:54` 逐字; 6.c "new tumor/lesion" (p348) → `:70` 一致. 全部 OK.
- 表格抽看 (reviewer 已全检, 此处只旁证): Ex1 VSLIDENT×2 / "Limb Lesion" / supptu TUPAGA (p353/p354), Ex3 TUDY 列 -2/-3/-3/-3/-2/48/88 与 R5 CEREBELLUM RIGHT (p356), METIND r3 NOT DONE 在 TUSTAT 列 (p349), DRCRLTLC / CONTRALATERAL (p349) — 与 PDF 文本层一致.
- 观察 (不计 FAIL): T-1 p353 "aorta-iliac" PDF 印刷错, KB 保留 "aorto-iliac" — 正确值可由同例叙述 + TULOC 定, 符合 PDF_TYPO 口径, writer/reviewer 均已登记.
- 范围外发现: 0 (2 个 TR 部分样本均在 TR/examples.md 存在).
- 对照 writer (`t2_B-TU.md`) / reviewer (`t2_B-TU_review.md`) 报告: 与本独立判定无冲突.

### G-TB8
- trace: `T2.B-TU` writer `oh-my-claudecode:executor` subagent_done 2026-11-26T03:34:47Z; reviewer `oh-my-claudecode:code-reviewer` subagent_done PASS 03:37:46Z; 无 `agent: main` 写 TU KB 记录.
- KB mtime 03:41:54Z 晚于 reviewer PASS, 但当前 md5 assumptions `511b50ff9b11056d20a6b038516fc1e0` / examples `2e8e78afc707c4784e2e09a80b73e5cf` = writer 记录的 after md5 → 内容未变; mtime 来自 B-TE writer `git stash`+`pop` (BE/MK/TA/TE 同刻 03:41:54Z, 见 `t2_B-TE.md:70`). 结论: 终态 = reviewer 所审版本, 通过.
- `python3 tools/check_links.py` → `broken relative links: 18668 (live docs: 42)` (基线 42, 不升).

**判定: PASS** (Rule A N=10 seed=20261126: 丢失 0 忠实 0)
