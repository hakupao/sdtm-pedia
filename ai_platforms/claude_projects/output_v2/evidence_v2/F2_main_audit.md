# F2 Main Controller Audit — N=10 independent sample

> 规则 A (语义抽检强制) + 规则 D (审阅隔离): Main controller (Opus, 本 session) 独立抽 10 codelist, 与 reviewer subagent (oh-my-claudecode:code-reviewer) 不重叠.
> 抽样日期: 2026-04-19 (E4+F1+F2 committed session 续)
> 审计范围: `ai_platforms/claude_projects/output_v2/11a/b/c_terminology_high_*.md` (F2 executor A+B+D 修订版)

## Verdict

**10/10 PASS** — 所有 10 个 codelist 在 5 个独立维度 (heading, term_count, extensible, row_order, related_domains) 全部通过.

## 10 抽样 codelist + 验证方法

Main controller sampled (disjoint from reviewer):

| # | Subdir | C-code | Codelist | Source |
|---|--------|--------|---------|--------|
| 1 | 11a_core | C66742 | No Yes Response | terminology/core/general_part4.md |
| 2 | 11a_core | C71620 | Unit | terminology/core/general_part5.md |
| 3 | 11a_core | C99079 | Epoch | terminology/core/general_part2.md |
| 4 | 11a_core | C71148 | Position | terminology/core/interventions.md |
| 5 | 11b_questionnaires | C135677 | PASI Clinical Classification Test Name | questionnaires/questionnaires_part32.md |
| 6 | 11b_questionnaires | C147541 | FACIT-Dyspnea 10-Item Test Name | questionnaires/questionnaires_part16.md |
| 7 | 11b_questionnaires | C130272 | WHODAS 2.0 36-Item Self Test Name | questionnaires/questionnaires_part43.md |
| 8 | 11b_questionnaires | C166184 | FACT-Cog V3 Test Code | questionnaires/questionnaires_part14.md |
| 9 | 11c_supp | C111111 | Device Properties Test Code | supplementary/supplementary_part2.md |
| 10 | 11c_supp | C150770 | MMSE 2 Standard Version Test Code | supplementary/supplementary_part3.md |

## 5 维度验证结果 (逐项 ✓)

| # | C-code | heading | term_count (out/src) | extensible | row_order (first_3 + last_3) | related_domains (out/derived) | truncated_defs |
|---|--------|:-------:|--------------------:|:----------:|:-----------------:|---------------------:|---:|
| 1 | C66742 | ✓ | 4/4 | ✓ | ✓ | ✓ 41/41 | 0 |
| 2 | C71620 | ✓ | 830/830 | ✓ | ✓ | ✓ 32/32 | 88 |
| 3 | C99079 | ✓ | 12/12 | ✓ | ✓ | ✓ 44/44 | 1 |
| 4 | C71148 | ✓ | 17/17 | ✓ | ✓ | ✓ 6/6 | 1 |
| 5 | C135677 | ✓ | 29/29 | ✓ | ✓ | ✓ 0/0 | 0 |
| 6 | C147541 | ✓ | 30/30 | ✓ | ✓ | ✓ 0/0 | 26 |
| 7 | C130272 | ✓ | 39/39 | ✓ | ✓ | ✓ 0/0 | 8 |
| 8 | C166184 | ✓ | 41/41 | ✓ | ✓ | ✓ 0/0 | 0 |
| 9 | C111111 | ✓ | 29/29 | ✓ | ✓ | ✓ 0/0 | 4 |
| 10 | C150770 | ✓ | 33/33 | ✓ | ✓ | ✓ 0/0 | 0 |

**维度口径:**
- **heading**: `## <Name> (<Cxxxxx>)` 逐字节匹配源
- **term_count**: 输出的 Term 行数 (leftmost `| Cxxx |` 格) == 源 Term 行数
- **extensible**: `Extensible: Yes/No` 行存在且匹配源
- **row_order**: 前 3 行 + 后 3 行 Term Code 完全匹配源 (样本内无重排)
- **related_domains**: 独立 `grep C-code \b` `knowledge_base/domains/*/spec.md` 得到域名集合, 与输出 "Related Domains:" 行逗号分列后 sorted set 相等
- **truncated_defs**: 统计输出中以 `...` 结尾的 Definition 单元格数 (诊断用, 不计入 PASS/FAIL)

## 关键观察

1. **C71620 Unit (830 terms) 全量保留**: 最大 outlier 830 行源全部保留, 88 行 Definition 触发 200-char 截断. 未丢行, 未合并. 规则 A (完整保留) 精神符合.

2. **C66742 NY Related Domains = 41**: 独立 grep 得 41 个 SDTM 域 (AE, AG, BS, CE, CM, CP, CV, DM, EC, EG, EX, FA, FT, GF, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SR, SU, SV, TM, TR, TU, UR, VS) — 与输出完全一致. B refinement (codelist-header 级 Related Domains) 在高关联度 codelist 上节省最显著.

3. **Questionnaire/Supplementary codelists Related Domains = 0**: 所有 6 个来自 questionnaires / supplementary 的抽样 (C135677 / C147541 / C130272 / C166184 / C111111 / C150770) 均为 0. 合理解释: 这些是 QRS / Device Test 专属 codelist, SDTM 域 spec 中不通过 C-code 引用 (域 spec 的 Controlled Terms 只列 --TESTCD 为 QS/FT, 具体 Test Code 枚举不写入 domain spec). **独立 grep 验证一致 → 非 bug, 是 domain-spec 引用粒度的真实客观结构**.

4. **Row order 保留**: 前后 3 行 Code 样本比对全通过, 未发现重排. 规则 B 归档需求无触发 (未有失败).

5. **Definition 截断分布**: 抽样中 88+26+8+4+1+1 = 128 行被截断. Truncation 是 hard budget 设计, `...` 尾标清晰, 未见截断错位.

## 交叉校验 — Reviewer subagent 独立审

并行 dispatch `oh-my-claudecode:code-reviewer` (agentId `abbd925b66528d695`), 其审计范围:
- 10 个**不重叠**抽样 C-code
- Script quality (LOC, CLI, idempotency, read-only, error handling)
- Per-file token + codelist count 独立验证
- 2 个 Related Domain 集合独立再推导 (对照 grep)

Reviewer 产物: `output_v2/evidence_v2/F2_reviewer_audit.md` (pending). 本 main audit 与 reviewer audit 同为 PASS, 并交叉覆盖 20 个 codelist 即认定 F2 产物 PASS → 进 F3 (build_v2_stage.py --stage v2.4).

## 附件

- `F2_main_audit.json` — 10 codelist 原始审计结果 (机器可读)
- `F1_codelist_high.txt` — 200 C-code 输入列表
- `11a/b/c_terminology_high_*.md` — 审计目标
