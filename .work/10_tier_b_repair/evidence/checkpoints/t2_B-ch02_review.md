# T2 B-ch02 reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus) — 审 writer attempt 1 + 续 + 续2 终态

**verdict: PASS**

- 审查对象: `knowledge_base/chapters/ch02_fundamentals.md` md5 `d5f9f9b1888b2e304e3104a3cf6cfa5e` (= writer 续2 终态), 基线 553b14b. 只审 ch02 (他批并行改他文件).
- 真值: `work/pdf_pages/ig34_p0007..0016.txt` + `pdftoppm -f 9 -l 16 -r 80` 渲染 (p10/p11/p12/p13/p15/p16 逐页目视).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch02_reviewer/` (scan.py / scan2.py / order.py / kbA kbB / fpA fpB).

### 命令与结果 (可复跑; S=上述 scratch, repo 根执行)
```
git show 553b14b:knowledge_base/chapters/ch02_fundamentals.md > $S/ch02_base.md
python3 -I $S/scan2.py 11 16        # PDF→KB: p11-16 按 bullet/标题/句切 169 单元, fp_match.norm, 判 in norm(KB)
  → units 169 miss 4; 4 条均为切分伪影 (bullet 尾与下一段首无空行被拼成一单元), 拆开后各半逐一在 KB :1/:57+:61/:192+:196/:201+:205 命中; 真缺 0
python3 -I $S/scan.py 7 10 1 44 ; python3 -I $S/scan.py 11 16 45 223   # KB→PDF 逐句
  → 未命中仅: 标题/KB 导航行 (:1 :3 :5 :7 :9 :24 :32 :49 :59 :112 :169 :194 :203 :214, 全为基线已有或 Section 1 摘录导航), D6 note :91 :151, mermaid :153-163. 无自造正文
python3 -I $S/order.py              # p7-16 唯一命中单元 (≥25 字, 170 条) 在 KB 中出现顺序 = PDF 顺序 → 0 OUT-OF-ORDER
cp -R knowledge_base $S/kbA; cp -R knowledge_base $S/kbB; cp $S/ch02_base.md $S/kbA/chapters/ch02_fundamentals.md   # 只差 ch02 的隔离对照
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbA --out $S/fpA.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpB.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regress.jsonl
  → regressions=0 new_hits=96 RESULT: GREEN (exit 0)
  → 本批 31 atoms + recheck a017: 32/32 hit_target = ch02; ig34 p11-16 不命中仅 p15_a006 (FIGURE, Mermaid 呈现); p8-10 不命中均属 §1.4/§1.4.1/§1.5 (ch01, B-ch01 范围)
python3 tools/check_links.py | grep 'live docs'   → broken relative links: 18668 (live docs: 42) ≤ 42
diff <(grep '^#' $S/ch02_base.md) <(grep '^#' knowledge_base/chapters/ch02_fundamentals.md)  → 空 (标题不变)
census: 本批 diff_tables / pdf_only / pdf_unparsed = 0; 触碰的 4 张 unparseable 表 (:37 :75 :91 :165) 均已删除换 PDF bullet → 无表可 census, 改为渲染逐条核 (下)
```

### 1. 双向逐句扫描 (reviewer 必做全扫)
- PDF→KB p11-16: 169 单元全命中 (见上), 含所有限定词/计数/交叉引用/URL (Section 8 / 8.4 / 8.6.1 / 3.2 / 3.2.1 / 1.4.1 / 9.2 / 2.6; define-xml / wiki / datascience / ncitermform URL). R2 丢失 0.
- p7 §1.2: 引导句 + 10 bullet 全文命中 (KB :11-22). p9 §1.4: "This implementation guide covers…" 整句 + 3 guides bullet 命中 (:26-30). p9-10 §1.4.1: 摘录的两父项子树逐字命中 (:34-43); §1.4.1 其余项 (Variable Name/Type/Codelist/Format/Role/CDISC Notes/Core) 及 §1.5 不在 ch02 — 属 ch01, 摘录性质, 不判缺.
- KB→PDF: 正文全部有出处; 见上未命中清单.

### 2. 删除的 3 张 KB 自写表 → PDF bullet (渲染 p11/p12/p13 逐条)
| KB 改后 | PDF bullet | 渲染核 |
|---|---|---|
| :63-67 子类 5 条 | p11 Grouping/Result/Synonym/Record/Variable Qualifiers | 一致 (含 "Result Qualifiers are" 穷举、"in a Findings domain" 句末无句点照录) |
| :87-89 GOC 3 条 | p12 Interventions/Events/Findings | 一致 (e.g. 非 i.e.; randomization/study completion; during/prior to the trial) |
| :101-104 §2.4 4 条 | p12-13 Domain datasets/TDM/Relationship/Study Reference | 一致 (含 "Section\n8" 折行合并) |
被删表内容逐格对 diff (D-1..D-21): 表中 PDF 有依据的信息 (域代码、变量名、Section 号) 全部在新 bullet 句内; 被删的仅 KB 改写措辞 ("Findings only" / "including questionnaires" / "Describe relationships among datasets/records" 等, PDF 无或与 PDF 措辞冲突). D-13/D-14 两句移到 PDF 位置 (:127 / :122) 确认; D-20 Key rules 4 条被 step 1 子 bullet (:131/:132/:134) 逐字覆盖; D-21 后缀被 :212/:220 PDF note 覆盖. 无 PDF 内容丢失.

### 3. §2.7 / §1 渲染核
- §2.7 KB :173-192 20 bullet vs p15-16 渲染: 逐条一致, 顺序一致; 与基线 20 行表逐行 (变量, 类) 程序比对全等. 三句引导句在 :171 / :196 / :216, 分别紧接各自 bullet 列表前 = PDF 位置; DM 段 "…all subjects are human." 与 "See Section 9.2 …" 同段 = PDF. SETCD/POOLID 框注 :212/:220, 结尾段 :222 一致.
- §1.4.1 层级 vs p9-10 渲染: Variable Label(•) > 2×o; Controlled Terms, Codelist, or Format(•) > Controlled Terms(o) > asterisk(▪) > 3×• ; external code system(▪) 与 asterisk 同级 — KB 缩进 :34-43 一致.

### 4. 20 处原位替换
order.py + 双向扫描证明 KB p11-16 段落每句 = PDF 句且顺序一致; fp_match 隔离对照 regressions=0 → 替换行上其他原子无回退. 逐条对 writer 变更表 #3-#5,#9,#10,#12,#14,#16-#20,#22-#26,#29-#31 核: 均为同一 PDF 句的错述版本被换回原句.

### 5. Mermaid / D6 note
- Mermaid 内容与基线逐行相同, 从 §2.6 节首移到 step k 之后 (:153-163) = PDF p15 图位置; 前有 PDF 图题 "**Figure. Creating a New Domain**" (:149, PDF 粗体) + D6 note :151. RELOCATE OK. 图结构 (Identifier AND Timing AND Topic/Qualifier → 三类 OR → New Domain) 与渲染一致, 不矛盾.
- :91 GOC KB note: 引导语 "Example domains by class — …" 为新框架文字 (writer 已声明), 9 个域与类的对应均正确 (EX/CM/PR = Interventions; AE/DS/MH = Events; LB/VS/EG = Findings), 与 p12 不矛盾, 已按 D6 前缀标注 → 确认保留.

### 6. T-1 / 页码
- p16: "Trials Sets domain" (渲染框注确认). SDTMIG v3.4 全文 (ig34_p*.txt) 无 "Trial Sets"; 仅 sv20 p51/p53 → 不能由 SDTMIG 自身确定 → KB :212 照录 "Trials Sets" + T4 登记 (checkpoint 续2 #1, writer.jsonl 行 39) — 符合 PDF_TYPO 取舍规则.
- :3 "Pages 11-16": §2 正文起 p11 止 p16 (本 PDF 页码口径) — 正确.

### 7. a017 recheck
| atom | 判定 | 证据 |
|---|---|---|
| ig34_p0011_a017 | 基线 = **REAL_GAP** (R2: 表格 "(for --TRT/--TERM)" 丢 "which are equivalent terms"; 现 :65 已逐字补回 → 已修) | 基线 ch02:41 vs 现 :65; p11 "which are equivalent terms for a --TRT or --TERM topic variable" |
writer 偏离 "recheck 不改" 合理 (子类表整表被换, 不可能保留旧改写), 接受.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| ch02:63-67, :87-89, :116 | 格式 | (LOW, 不阻断) 术语粗体为 KB 排版, PDF 非粗体; 不影响文字/归一化命中 | p11/p12/p13 渲染 |
| ch02:37 | 摘录 | (LOW, 不阻断) §1.4.1 父项 "Controlled Terms, Codelist, or Format" 只摘 Controlled Terms 子树, Codelist/Format 子项不在 ch02 (在 ch01 :85 表) — 摘录节性质, 非缺失 | p10 渲染 |
| T-1 | T4 | "Trials Sets" 待用户裁定 (主控汇总 T4) | p16 框注 |
无 FAIL / CONDITIONAL 项.

### G-TB6 结构行签字 (新增/改动, 非 PDF 正文)
:3 Source 页码行 (改 11-16, 正确); :9 / :24 / :32 "From §1.x …" 摘录小标题 (基线已有); :49 :59 :112 :169 :194 :203 :214 小标题 (基线已有, 文字未改); :91 :151 D6 note (确认); :149 PDF 图题; :153-163 mermaid (基线原样移位). 签字: reviewer 确认.

## attempt 2 复审 (2026-11-26, oh-my-claudecode:code-reviewer / opus) — delta: md5 d5f9f9b1… → af07c931…

**verdict: CONDITIONAL** (delta 两项均 OK; 自省重扫标题发现 1 处同类问题, 须改)

### 命令 (S = reviewer scratch, repo 根)
```
diff $S/ch02_att1.md knowledge_base/chapters/ch02_fundamentals.md   # ch02_att1 = attempt1 终态, md5 d5f9f9b1 已核
  → 仅 3 处: :7 引导句 → 交叉引用一行; 原 :9-44 (§1.2/§1.4/§1.4.1 三小节) 删除; :203→:167 标题括号改
grep -rn 'ch02_fundamentals\(\.md\)\?#' knowledge_base web/src docs releases/v1.4 tools ; grep -rni 'from-12\|from-14\|from-141\|from-§1' knowledge_base web/src docs   → 均 0 行 (不截断)
fp_match 隔离对照 (kbA = 现 KB 但 ch02 换基线 553b14b; kbB = 现 KB; ch01 两侧同为当前版) → regressions=0 new_hits=96 GREEN; p11-16 absent 仅 p15_a006
  hit_any 丢失 4 = p9_a009 / p9_a020 / p9_a021 / p10_a004 (targets 均 ch01, 基线只在 ch02 §1 摘录命中) → 转 B-ch01 必补, 可接受
python3 tools/check_links.py | grep 'live docs'   → 18668 (live docs: 42)
```

### delta 判定
| ref | 判定 | 证据 |
|---|---|---|
| F1 ch02:167 "(not evaluated for use in human clinical trials)" | OK | p16 "have not been evaluated for use in human clinical trials"; p15 "(2) have not yet been evaluated" — 不再暗示部分评估 |
| D-24 :7 KB 自写引导句 | OK (导航, 非 PDF) | — |
| D-25..D-27 原 :9-44 | OK: 删除行全部为 p7 §1.2 / p9 §1.4 / p9-10 §1.4.1 原文 + 3 个 KB 摘录小标题; 无 p11-16 内容 (attempt 1 的 PDF→KB 169 单元扫描不含这些行; 本次 fp p11-16 回归 0) | p7/p9/p10 文本 |
| :7 交叉引用 `ch01_introduction.md` | OK: 文件存在, live docs 不升; 纯导航不加 KB note | — |

### 自省 (attempt 1 漏判 F1 的原因)
attempt 1 我把 KB 自写小标题按 "基线已有, 文字未改" 一律签字, 未与 PDF 措辞对比 — 错误; 基线已有的自写标题只要落在本批页且与 PDF 矛盾/丢限定, 同样是本批缺陷. 本次逐条重扫全部 KB 自写标题:
| KB 标题 | PDF 依据 | 判定 |
|---|---|---|
| :1 "Chapter 2: Fundamentals of the SDTM" | p11 "2 Fundamentals of the SDTM" | OK |
| :5 "Section 1 Context (Reference Material)" | 导航 | OK |
| :13 "Variable Roles (5 major roles)" | p11 "classified into 5 major roles" | OK |
| :23 "Qualifier Variable Subclasses" | p11 "further categorized into 5 subclasses" | OK |
| :76 "General rules for determining which variables to include:" | p13 "These general rules apply when determining which variables to include" | OK |
| :133 "Must NEVER be used in human clinical trials (SEND-only):" | p15 "defined for use in nonclinical studies (SEND), must NEVER be used … for human clinical trials" | OK |
| **:158 "Must NEVER be used in DM domain (SEND nonclinical only):"** | p16 "must NEVER be used in the Demographics (DM) domain for human clinical trials" | **CONDITIONAL**: 丢限定 "for human clinical trials" → 读作 DM 一律禁用 (SEND 的 DM 正是用它们); 与 F1 同类 |
| :167 (F1 已修) | p16 | OK |
| :178 "May be used when appropriate:" | p16 "may be used in human clinical trials when appropriate" | 丢 "in human clinical trials" (LOW, 不矛盾; 建议同步补) |
| :188 / :214 FA 节 | B-FA 范围 | 不审 |

### 修正清单 (writer 下一 attempt; 只改标题括号/限定, 无入链已核)
1. ch02:158 → `### Must NEVER be used in DM domain for human clinical trials (SEND nonclinical only):` (或去括号, 取 p16 "for human clinical trials").
2. (建议) ch02:178 → `### May be used in human clinical trials when appropriate:`.
改后回 reviewer 复审 delta (终态必经 reviewer).

## attempt 2 续 签字 (2026-11-26, oh-my-claudecode:code-reviewer / opus) — md5 af07c931… → 4cc3de33cdbb3e103be04e31cc23cdd5

**verdict: PASS**
- `diff` (上一版 vs 现 ch02): 仅 2 行. :158 → "Must NEVER be used in DM domain for human clinical trials (SEND nonclinical only):"，与 p16 "must NEVER be used in the Demographics (DM) domain for human clinical trials" 一致. :178 → "May be used in human clinical trials when appropriate:"，与 p16 "may be used in human clinical trials when appropriate" 一致.
- 入链检查: `grep -rn 'ch02_fundamentals\(\.md\)\?#' knowledge_base web/src docs releases/v1.4 tools` 和 `grep -rni 'must-never-be-used-in-dm\|may-be-used-when' knowledge_base web/src docs` 都是 0 行.
- fp_match 隔离对照 (fpA2 为基线): regressions=0, new_hits=96, GREEN; p11-16 不命中仅 p15_a006. `python3 tools/check_links.py | grep 'live docs'` → live docs: 42.
- 本批 KB 自写标题全部与 PDF 措辞对上, 修正清单已清空.
