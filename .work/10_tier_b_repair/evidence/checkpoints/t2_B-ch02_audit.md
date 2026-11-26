# T2 B-ch02 auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus) — 审 KB md5 `d5f9f9b1888b2e304e3104a3cf6cfa5e` (= reviewer PASS 终态), 基线 553b14b

**verdict: FAIL** (seeded 样本 0 丢失 0 忠实错; 补充全扫发现 1 处 KB 自写标题改义 → 忠实度 1)

- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch02_auditor/` (sample.json, chk.py, deleted.txt, p-010..016.png, kbA/kbB, fpA/fpB)
- 真值: `work/pdf_pages/ig34_p0007..0016.txt` + `pdftoppm -f 10 -l 16 -r 90` 渲染 (p10/11/12/13/15/16 目视).
- 流程披露: 抽样 + chk.py 双向扫描在读 writer/reviewer 报告前完成; 样本表填写前已读 writer checkpoint 与 reviewer 报告 (仅用于核 §1 裁定来源与 G-TB8), 样本判定依据均为 PDF 原页.

### 1. 抽样 (prompt v1.0 命令原样, batch=B-ch02, seed=20261126)
`python3 -I - <<'EOF' ... EOF > $S/sample.json` (t2_auditor_v1.0.md §抽样 原文)
→ C=32, P=104, N=10; sample = p14_a007, p14_a005, p11_a016, p11_a022, p12_a018 (C 5) + p12_a020, p14_a013, p12_a005, p14_a012, p12_a015 (P−C 5).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0014_a007 | p14:25-28 step 3 找原型; 无合适模型则选 GOC; "As illustrated in the following figure" | ch02:136 | 否 | 是 | §2.6 step 3 | 逐字 |
| 2 | ig34_p0014_a005 | p14:13-20 层级数据建 domain pair + Note (MB/MS, PC/PP, RELREC, DOMAIN 分组) | ch02:134 | 否 | 是 | §2.6 step 1 子项 | 逐字 |
| 3 | ig34_p0011_a016 | p11:19-21 Result Qualifiers 定义 + "answer the question" + 穷举 --ORRES/--STRESC/--STRESN | ch02:64 | 否 | 是 | §2.1 子类 | `--\nSTRESN` 折行, p11 渲染确认连续 |
| 4 | ig34_p0011_a022 | p11:34-36 Timing = study day of start; Record Qualifier = severity "MILD" | ch02:69 | 否 | 是 | §2.1 例段 | 逐字 |
| 5 | ig34_p0012_a018 | p12:28-29 "appropriate to a specific collection of data ... according to these descriptions" | ch02:93 | 否 | 是 | §2.3 | 逐字 |
| 6 | ig34_p0012_a020 | p12:30-32 选 GOC 补充指引见 Section 8.6.1 (xref) | ch02:93 | 否 | 是 | §2.3 | xref 全称在 |
| 7 | ig34_p0014_a013 | p14:42-43 step f 应用 2 字符码; 替换 "--" 前缀 | ch02:142 | 否 | 是 | §2.6 step 3f | 弯引号照录 |
| 8 | ig34_p0012_a005 | p12:4-6 元数据在 data definition document (Define-XML) 随数据提交给监管 | ch02:77 | 否 | 是 | §2.2 | 逐字 |
| 9 | ig34_p0014_a012 | p14:36-41 step e domain code: CT 链接 / 申请 URL / 一致使用 / AD AX AP SQ SA 禁用 | ch02:141 | 否 | 是 | §2.6 step 3e | 2 URL 在 |
| 10 | ig34_p0012_a015 | p12:19-22 Interventions 定义 (protocol/CM/self-administered, e.g.) | ch02:87 | 否 | 是 | §2.3 | e.g. 非 i.e. |

样本: 独有丢失 0, 忠实度错误 0, 位置错 0.

### 2. 补充全扫 (独立脚本 chk.py, 不依赖 fp_match)
chk.py 逻辑: 归一化 (‑→-, 弯引号去除, `-\s+-`→`--`, 空白折叠, 去 `**`) 后 (a) pdf_atoms p11-16 全部 SENTENCE/LIST_ITEM/NOTE/CROSS_REF/HEADING 原子 verbatim ∈ KB(ch02 FA 参考节之前); (b) KB 每行按句切分 ∈ PDF p7-16.
- (a) PDF→KB: 未命中 1 = p11_a001 HEADING "2 Fundamentals of the SDTM" (KB H1 "Chapter 2: Fundamentals of the SDTM", 导航, 不计).
- (b) KB→PDF: 未命中 16 = :1 :3 :5 :7 :9 :24 :32 (标题/摘录导航), :64 :66 (`--\nSTRESN` / `--\nPOS` 折行伪影, p11 渲染确认 KB 正确), :49 :59 :112 :169 :194 :214 (KB 自写小标题, 与 PDF 一致, 不改义), **:203 见 F1**.
- **F1 (FAIL, 忠实度/改义)**: ch02:203 KB 自写小标题 `### Use with extreme caution (not fully evaluated for human clinical trials):` — PDF p16:15 "have not been evaluated for use in human clinical trials", p15:17 "(2) have not yet been evaluated". "not fully evaluated" 暗示已部分评估, 与 PDF 矛盾. 基线已有 (writer 未动标题; reviewer 按 "基线已有" 签字), 但位于本批 kb_file/本批页 → 按 D6/D2 (KB 自写与 PDF 矛盾 → 删/改) 计入. 建议最小修: 改为 `(not evaluated for use in human clinical trials)` 或去掉括号部分.

### 3. 指定专项
- 3 张 KB 自写表 → PDF bullet (渲染 p11/p12/p13 逐条): 子类 5 (:63-67)、GOC 3 (:87-89)、§2.4 4 (:101-104) 文字/顺序/嵌套一致. 粗体为 KB 排版 (非内容).
- §2.7 20 bullet (:173-192) vs p15-16 渲染逐条: 变量名与括号类别全对、顺序一致; DM 4 / caution 4 / POOLID 1 及 3 句引导句、2 框注 (:212 "Trials Sets" 照录, T-1 → T4)、尾段 :222 一致. p15 "(2) have not yet been evaluated" 在 :167.
- 删除行 10 随机 (deleted.txt = diff `^-` 去空行/分隔行 103 行, `random.Random(20261126).sample(range(103),10)`): idx 4 (§2.1 首段 → :47), 10 (子类表头), 28 (a008 改写 + 5/6 节句 → :79/:81), 37 (Events 表行 → :88 + KB note :91), 41 (§2.4 表头), 56 (分组句 → :130), 60 (step a → :137), 79 (§2.7 表头), 81 (--METHOD → :174), 85 (--RESLOC → :178). 3/10 为表头; 其余 7 行 PDF 有据信息全部在新位置, 丢失 0.
- D6 note 2 处: :91 域例 (EX/CM/PR=Interventions, AE/DS/MH=Events, LB/VS/EG=Findings) 与 p12 及 SDTMIG 分类一致, 不矛盾; :151 Mermaid 标注 — 图结构 (Identifier AND Timing AND Topic/Qualifier → 三类 specific OR → New Domain) 与 p15 渲染不矛盾, 位置 = step 3k 之后 (PDF 位置).
- §1.4.1 摘录 (:32-43): 逐字子集, 嵌套 (Variable Label •>2o; Controlled Terms, Codelist, or Format •> Controlled Terms o > asterisk ▪ > 3• ; external code system ▪) 与 p9-10 渲染一致. **非阻断观察 O1**: 截断无标记 — 无引导句 "The columns of the table are:", 7 列只摘 2 列, 父项名含 Controlled Terms/Codelist/Format 三者但只列一子 (Codelist/Format 缺); 完整内容在 ch01:76-85 (B-ch01 范围), 故非信息丢失. 但 §1 内容整体复制自 ch01 所属节, 与补充口径 "KB 自写附录/摘要与 PDF 重复 → 留所属节, 附录处一行交叉引用" 有张力 (本次扩写为主控裁定 续2 #4-6) → 请主控确认是否维持; 另提醒: p7/p9/p10 这些 §1 原子现在 ch02 也命中, B-ch01 评估须看 hit_target=ch01, 不可看 hit_any.

### 4. fp_match 隔离复跑 (auditor 自跑)
```
S=<scratch>; cp -R knowledge_base $S/kbB; cp -R $S/kbB $S/kbA; git show 553b14b:knowledge_base/chapters/ch02_fundamentals.md > $S/kbA/chapters/ch02_fundamentals.md
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbA --out $S/fpA.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpB.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regress.jsonl
  → regressions=0 new_hits=96 RESULT: GREEN; fp_regress.jsonl 0 行; ig34 p11-16 hit_any 未命中仅 ig34_p0015_a006 (FIGURE)
```

### 5. G-TB8
- `md5 -q knowledge_base/chapters/ch02_fundamentals.md` = `d5f9f9b1888b2e304e3104a3cf6cfa5e` = reviewer 审查对象 → reviewer PASS 后无 writer 改动.
- trace.jsonl: T2.B-ch02 writer (executor) subagent_done ×2 (行 82/87), reviewer (code-reviewer) PASS (行 94); 全文件 `"agent": "main"` 6 条, 无一涉及 ch02 → 通过.

### 汇总
独有丢失 0 (样本) / 0 (全扫); 忠实度错误 0 (样本) / **1 (全扫 F1 ch02:203)** → **FAIL**. 修复建议: 仅改 :203 小标题措辞, 回 reviewer 复审 delta 后再派 auditor attempt 2.

## attempt 2 (2026-11-26, oh-my-claudecode:verifier / opus) — 审 KB md5 `4cc3de33cdbb3e103be04e31cc23cdd5` (= reviewer「attempt 2 续 签字」对象), 基线 553b14b

**verdict: PASS**

### 1. Rule A (prompt v1.0 命令, batch=B-ch02, seed=20261127; 命令存 scratch samp2.sh)
→ C=32, P=104, N=10; sample = p11_a016, p12_a015, p12_a019, p11_a029, p12_a001 (C) + p12_a016, p13_a006, p12_a008, p12_a013, p11_a014 (余数).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0011_a016 | p11:19-21 Result Qualifiers 定义 + 穷举 | ch02:28 | 否 | 是 | §2.1 | `--\nSTRESN` 折行伪影 |
| 2 | ig34_p0012_a015 | p12:19-22 Interventions 类 (e.g. 三情形) | ch02:51 | 否 | 是 | §2.3 | 粗体为排版 |
| 3 | ig34_p0012_a019 | p12:29-30 majority … typically … usually … Findings | ch02:57 | 否 | 是 | §2.3 | 逐字 |
| 4 | ig34_p0011_a029 | p11:43-44 唯一 2 字符码, 全提交一致使用 | ch02:39 | 否 | 是 | §2.2 | 逐字 |
| 5 | ig34_p0012_a001 | p12:1-2 DOMAIN 4 用法 + see Section 8 | ch02:39 | 否 | 是 | §2.2 | xref 在 |
| 6 | ig34_p0012_a016 | p12:23-25 Events 类 (randomization; during/prior to trial) | ch02:52 | 否 | 是 | §2.3 | 逐字 |
| 7 | ig34_p0013_a006 | p13:10-12 可用本/他 IG 标准域 + 自定义域 | ch02:74 | 否 | 是 | §2.5 | 逐字 |
| 8 | ig34_p0012_a008 | p12:9-10 SDTM 只列 name/label/type + general description | ch02:43 | 否 | 是 | §2.2 | 逐字 |
| 9 | ig34_p0012_a013 | p12:16-17 观测按 3 类之一表示 | ch02:49 | 否 | 是 | §2.3 | 逐字 |
| 10 | ig34_p0011_a014 | p11:16 Qualifier 5 子类引导句 | ch02:25 | 否 | 是 | §2.1 | 逐字 |

样本: 丢失 0, 忠实度错误 0, 位置错 0.

### 2. F1 + 新补限定 (vs p15/p16 文本)
- :167 "Use with extreme caution (not evaluated for use in human clinical trials)" ↔ p16:15 "have not been evaluated for use in human clinical trials … extreme caution" → 一致, F1 关闭.
- :158 "Must NEVER be used in DM domain for human clinical trials (SEND nonclinical only)" ↔ p16:7-8 → 一致. :178 "May be used in human clinical trials when appropriate" ↔ p16:24-25 → 一致.
- 全部 KB 自写标题重扫 (chk.py KB→PDF 未命中清单): :1 :3 :5 导航; :13 :23 :76 :133 :158 :167 :178 与 PDF 措辞一致无改义; :28 :30 为 `--` 折行伪影. PDF→KB p11-16 未命中仅 p11_a001 H1 (导航). 无新增忠实度问题.

### 3. §1 去重 (D-24..D-27)
- `git diff 553b14b` 删除行中 §1 相关仅 "From §1.x" 3 小标题、2 引导句、3 条 §1.4.1 bullet (+ attempt1 续2 新增的 §1 扩写, 现已整体撤出); :7 改为指向 `ch01_introduction.md` 的交叉引用 (ch01 有 §1.2 :13 / §1.4 :59 / §1.4.1 :76). §2.x 正文未因去重丢内容 (chk.py PDF→KB p11-16 全命中).
- fp 对 553b14b 的 hit_any 变化: p7-10 中仅 ig34_p0009_a009 / a020 / a021、ig34_p0010_a004 四条由 "ch02 命中" 变为未命中, 四条 targets 均为 ch01, base hit_target 即 None → 已转 B-ch01, 可接受. attempt 1 O1 (截断无标记) 随删除消解.

### 4. fp / links / G-TB8
```
cp -R knowledge_base $S/kbB; cp -R $S/kbB $S/kbA; git show 553b14b:knowledge_base/chapters/ch02_fundamentals.md > $S/kbA/chapters/ch02_fundamentals.md
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpB2.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regress2.jsonl
  → regressions=0 new_hits=96 GREEN; ig34 p11-16 hit_any 未命中仅 p15_a006 (FIGURE)
python3 tools/check_links.py | grep 'live docs'  → broken relative links: 18668 (live docs: 42) ≤ 42
md5 -q knowledge_base/chapters/ch02_fundamentals.md → 4cc3de33cdbb3e103be04e31cc23cdd5 = reviewer 签字对象
```
- trace: writer attempt2 续 (行 106, 02:18:53Z) < reviewer PASS 签字 (行 109, 02:19:33Z); 其后无 B-ch02 writer 事件; `"agent": "main"` 无 ch02 记录 → G-TB8 通过.

### 汇总
丢失 0 / 忠实度错误 0 (样本 + 全扫) → **PASS**.
