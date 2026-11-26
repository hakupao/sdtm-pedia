# T2 B-SV auditor (Rule A 独立抽检) — attempt 1

- agent: oh-my-claudecode:verifier (opus); 先独立判, 判完才对照 writer/reviewer 报告
- 改动 (`git diff HEAD -- knowledge_base/domains/SV/`): assumptions.md Description/Overview 重写为 PDF 3 段 (补 a003-a007, a011 恢复原义, 删旧改写句); :51 15b "collected"→"recorded"; examples.md:53 ds Row 6 DSSTDY 28→26
- 抽样命令: 模板 t2_auditor_v1.0 脚本, 偏离 2 处 (按 common brief): files = batch kb_files ∪ {SV/assumptions.md}; pages = 86-91 (SV 全节, 非 batch json 的 [89,90]); scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SV_auditor/sample.json`
- seed 20261126; C=0, P=68 (p86 a001/a002 等 SM/标题非 prose 不在 P; p86 上部 CE 例子原子不在 P), N=10 (全取自 P−C)
- 真值 = PDF 渲染图 p86-p90 (`pdftoppm -r 110`, source/cdisc/SDTMIG v3.4 (no header footer).pdf)

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0090_a008 | p90 Row 4 说明: subject 85 WEEK 1 未发生, 原因见 SVREASOC | SV/examples.md:61 | 否 | 是 | 是 | 逐字一致 |
| 2 | ig34_p0090_a004 | p90 第 1 段第 2 句: 原计划面访, 疫情干扰导致部分远程 | SV/examples.md:55 | 否 | 是 | 是 | 原子 verbatim 错 ("epidemic…necessitated"); 渲染图为 "pandemic disruption included conducting some visits remotely", KB 与渲染逐字一致 |
| 3 | ig34_p0086_a007 | p86 Desc 第 2 段末前句: 多日期时 SVSTDTC/SVENDTC 推导更复杂 | SV/assumptions.md:7 | 否 | 是 | 是 | 本批新增, 逐字 |
| 4 | ig34_p0086_a015 | p86 spec 标题 "Subject Visits — Special Purpose." | SV/assumptions.md:13 | 否 | 是 | 是 | spec 首句逐字 |
| 5 | ig34_p0088_a015 | p88 A15e: --STRF/--ENRF 可用, 但似无必要 | SV/assumptions.md:54 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0087_a018 | p87 A4d: 见 Section 4.5.7 Presence or Absence of Prespecified… | SV/assumptions.md:27 | 否 | 是 | 是 | 原子 verbatim 错 ("of/Absence of Prespefified"); 渲染为 "Presence or Absence of Prespecified", KB 一致 |
| 7 | ig34_p0089_a003 | p89 Ex1 首句: 计划访视表 + 3 名受试者处置/事件 | SV/examples.md:5 | 否 | 是 | 是 | 逐字 |
| 8 | ig34_p0087_a012 | p87 A2: 每 VISITNUM 仅 1 条 | SV/assumptions.md:19 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0090_a009 | p90 Rows 5-9: subject 85 其余访视正常完成 | SV/examples.md:63 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0090_a007 | p90 Rows 2-3: subject 85 前 2 次访视正常完成 | SV/examples.md:59 | 否 | 是 | 是 | 逐字 |

- **独有丢失 0, 忠实度错误 0 → 抽检 PASS**

## 额外核查 (主控指定)
- Description/Overview 5 新句 (a003-a007) + a008-a012 逐字对 p86 渲染图: 全部一致; 段落切分 (a003 单段 / a004-a009 / a010-a012) 与渲染一致. a011 渲染为 "planned but not expected visits due to a subject not completing the study", KB:9 逐字一致 (pdf_atoms a011 verbatim "planned but not completed visits" 为原子错, 非 KB 错). 旧改写短语 grep `not completed visits` 在 SV/ 0 命中 (已删).
- 15b "recorded" 对 p88 渲染: "the date on which information about the visit was recorded" 一致.
- ds Row 6 DSSTDY = 26 对 p90 渲染一致.
- P 全 68 原子机械匹配 (规范化空白/列表号): 10 条未精确命中, 逐条对渲染: a011/p87 a018/p88 a001 ("for unplanned visits")/p88 a002 ("TELEPHONE")/p88 a009 ("--GRPID")/p89 a006 (句点)/p90 a004/a005 = 原子 verbatim 错, KB 与渲染一致; p87 a020 = 原子跨页截断, KB:31 完整; p87 a009 = spec 表脚注 1 (见下, 范围外).
- T-1 (p89 ds Row 5 说明句末缺句点, KB 保留句点): 渲染确认 PDF 无句点, 同组 Row 1-6 其余均有句点 → 依据成立, 同意.
- diff 授权: Description/Overview 属通用授权; 15b 为主控本批指定项 (O33/批备注), 非 writer 越权; examples 改动为 census 表格格.

## 范围外发现 (不计本批)
- p87 a009 spec 表脚注 1 ("In this column, an asterisk (*) …") SV/spec.md 缺; spec.md 不在本批 kb_files; 全 64 域 spec.md 0 处含此脚注 → 全域同类, 已由 writer F-1 归 O26.

## G-TB8
- trace.jsonl:282 writer `oh-my-claudecode:executor` subagent_done; :296 reviewer `oh-my-claudecode:code-reviewer` subagent_done PASS; 本批无 `agent: main` 写 KB 记录.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (基线 42, 写本文件前测得)

**Verdict: PASS** (N=10 seed=20261126, 丢失 0 忠实 0)
