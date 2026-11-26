# T2 B-ch04 auditor 报告 (Rule A 独立抽检)

## attempt 1 (审 writer attempt 2 终态; 2026-11-26, oh-my-claudecode:verifier / opus)

- 审计对象: `knowledge_base/chapters/ch04_general_assumptions.md` md5 `545883c16b8d4f3e161f3176df3c517a` (diff vs 6fea563: +111/−63)
- 判定: **FAIL** (seeded 样本 0/10 错; 但补充全扫在本批 kb_files + 本批页内发现 R2 丢失 3 处, 其中 1 处实质语义丢失, 见 §3). 修法极小, 建议 writer attempt 3 只补 3 处后复验.

### 1. 抽样 (命令 = t2_auditor_v1.0 原样, 仅 S 改为 scratch)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch04_auditor
python3 -I - <<'X' > $S/sample.json   # 脚本体同 subagent_prompts/t2_auditor_v1.0.md, b="B-ch04", seed=20261126
```
结果: seed 20261126, |C|=30, |P|=214, N=10. s1 (从 C 抽 5) = p43_a026/a024, p29_a028, p43_a032, p44_a001; 余 5 从 P−s1 抽 = p29_a002, p42_a013 (∈C), p42_a023, p53_a002, p41_a036 (∈C). 合计改动原子 7 + 未改动对照 3.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0043_a026 | p43:37-39 "In general, sponsors are cautioned … may not be as precise …" | ch04:912 | 否 | 是 | §4.4.7 --STRF/--ENRF ✓ | 逐字 |
| 2 | ig34_p0043_a024 | p43:32-34 "Sponsors are cautioned that doing so … will blur the distinction …" | ch04:910 | 否 | 是 | ✓ | 逐字; 行首 KB 粗体标签 "Caution on mixing…" 属既有导航标签 |
| 3 | ig34_p0029_a028 | p29 "Conventions for representing observations not done … Section 4.5.1.2, Tests Not Done …" | ch04:300 | 否 | 是 | §4.2.5 ✓ | 逐字; 旧改写句已 D2 删 |
| 4 | ig34_p0043_a032 | p43:46-47 "As a result, 4 new timing variables were added in SDTMIG v3.1.2 …" | ch04:916 | 否 | 是 | §4.4.7 --STRTPT 小节 ✓ | 逐字 |
| 5 | ig34_p0044_a001 | p44:1-2 "… are defined by each sponsor for each study." (续 p43 末句) | ch04:916 | 否 | 是 | ✓ | 与 p43_a034 拼成完整句, 逐字 |
| 6 | ig34_p0029_a002 | p29 "Required identifiers are not prefixed because … keys when merging/joining …" | ch04:268 | 否 | 是 | §4.2.2 ✓ | 未改动对照, 逐字 |
| 7 | ig34_p0042_a013 | p42:20-23 "For studies … prospectively defined schedule … expected to include VISITNUM …" | ch04:863 | 否 | 是 | §4.4.5 ✓ | 逐字 |
| 8 | ig34_p0042_a023 | p42:40-41 "VISIT may be left null or … generic value (e.g., "Unscheduled") …" | ch04:876 | 否 | 是 | ✓ | 未改动对照, 逐字 |
| 9 | ig34_p0053_a002 | p53 "Row 7: A result was derived from multiple results, so LBDRVFL = "Y". …" | ch04:1260 | 否 | 是 | §4.5.1.3 ✓ | 未改动对照, 逐字 |
| 10 | ig34_p0041_a036 | p41 "When an interval of time is an amount of time (duration) following … e.g., when one knows …" | ch04:824 | 否 | 是 | §4.4.3.2 ✓ | 逐字 (补回 e.g. 从句) |

样本: 独有丢失 0/10, 忠实度错 0.

### 2. 补充核查
- **全部新增 prose 逐字反查**: diff 中 82 个 "+" 句 (去表格/KB note) 对 p22-59 页文本做规范化子串匹配, 非逐字 8 句: 3 条 KB note 内容 + 1 个 markdown 标题 + 2 个既有 KB 粗体标签 + VISITDY 既有改写前缀 + ch04:865 (见 §3 F1). 其余 74 句逐字.
- **fp_match** (`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_now.jsonl`): 本批 atoms+t2_recheck 33 条中不命中恰为 3: ig34_p0043_a034 (verbatim 截断标记; 内容在 ch04:916 完整) / ig34_p0056_a005 / a006 (atom verbatim 与页面不符; KB 与渲染一致). 对 fp_baseline 的 ch04 回归 0. 本批页上其余 fp 不命中原子 = EQUIVALENT/EXACT 改写 18、CROSS_REF IE 2、REWRITE_OK 2 (p43_a014/a017 由 KB 表承载)、FIGURE/ATOM_ERR/TABLE 若干 — 逐条人工对过, 发现见 §3.
- **两张不可机检表 vs 渲染图** (`pdftoppm -f N -l N -r 110 -png`): p42 lb.xpt (ch04:881-885) 3 行×5 列 15 格与渲染逐格一致 (Week 1 VISITDY/LBDY = 7/7 ✓); p56 约定表 (ch04:1407-1411) 表头 4 格 + 3 行×4 格与渲染逐字一致. 注: KB 首列 "Convention / Storage / Split rule / Label" PDF 无, 属 KB 自加行标签, 不矛盾, 未标 KB note (既有, 不阻断).
- **其他表抽查** (reviewer 已全检, 只抽): p25 QS 行 1/5 QSLOBXFL=Y、VISITDY=1, SWLS 表 QSTESTCD SWLS0101-0105 ✓; p53 LB 行 5 WBC/++/2+、行 6 日期 2016-02-01、行 7 LBDRVFL=Y/VISITNUM 3 ✓; p23 "A Permissible variable should be used … wherever appropriate." ✓.
- **KB note 5 处 (D6) 全查, 无与 PDF 矛盾**:
  | ch04:line | 内容摘要 | PDF 对照 |
  |---|---|---|
  | 859 | Partial dates 不用于推 study day | p41-42 §4.4.4 未提, 不矛盾 |
  | 868 | VISIT = 方案中的访视名 | p42 未定义 VISIT 文本, TV 定义值, 不矛盾 |
  | 870 | VISITDY 是计划日, 非实际日; 勿用 --DY | p42:42-43 "VISITDY is, by definition, the planned study day …" 一致 |
  | 940-943 | Example applications (MH/CM/AE 取值例) | 取值均在 p43-44 允许值内; 与 p44-45 正式例子不冲突 |
  | 960 | Mermaid 为 PDF 图的 KB 渲染 | p44 渲染图: 2002 / 2006-11-02 / ONGOING / 图注 "may or may not have ended" 一致 |
  (trace "D6 KB note 7 处" − C2/C3 删除的 2 处 = 5, 对得上.)
- **删除行 10 条抽核** (diff 共 48 删行, 含表行):
  | # | 删除内容摘要 | PDF 内容去向 |
  |---|---|---|
  | D1 | :300 "Missing values are represented as null … See Section 4.5.1.2" | p29 原文 ch04:300 |
  | D2 | :848 "… consistent with the ICH E3 recommendation …" | p41-42 无 ICH (KB 自写); PDF 原文 ch04:848 |
  | D3 | Derivation "--DY is calculated as: --DTC - RFSTDTC" | p42 公式块 ch04:852-855 |
  | D4 | "Partial dates should not be used …" | KB note ch04:859 |
  | D5 | "Study Day is not suitable for mathematical calculations …" | p42 原句 ch04:848 |
  | D6 | §4.4.5 "In the Findings … at least 1 timing variable must be used" | p42 原文 ch04:863 (旧句与 PDF 不符) |
  | D7 | VISITDY "(not the actual study day; do not use --DY)" | KB note ch04:870 |
  | D8 | "There must be a one-to-one relationship" | p42 "should" 原句 ch04:871 |
  | D9 | §4.4.6 "--XSTDY and --CHSTDY may be used … (e.g., crossover studies)" | p43 段 ch04:889. 注: 二者是 SDTM v2.0 变量 (sv20 p36-37, 相对首次暴露 / challenge agent 的研究日), 并非"多参考起始日 / crossover"; KB 原句与 SDTM 定义不符, 删除成立 (writer 理由 "非 SDTMIG 变量" 不够精确) |
  | D10 | "Restriction on --STRTPT values: … AFTER is not a valid value …" | p44 清单 ch04:925-937 |
  另核: Ex1/2/3 旧 "CRF contains … When … checked:" 三行 → Assumptions 清单 + "Example when … checked:" 原句 (ch04:949-998, 对 p44-45 逐字); :1399 旧压缩行 → p56 CO/IE/TS/TI 清单. 删除无 PDF 内容丢失.

### 3. 发现 (本批 kb_files 内、本批 pdf_pages 内, 非 seeded 样本)
| F | atom_id | PDF 页 + 摘要 | KB 现状 | 类别 | 处理建议 |
|---|---|---|---|---|---|
| F1 | ig34_p0042_a015 (+a016) | p42:24-25 "… defined in the Trial Visits (TV) dataset (see Section 7.3.1, Trial Visits)." | ch04:865 句末无括号交叉引用; **本批 writer 改过该行** (句首插入 a014) | R2 丢短语 (cross-ref) | 补回 "(see Section 7.3.1, Trial Visits)". ledger 把 a016 作 CROSS_REF_NAVIGATION 自动 IE, 但本批对 §4.4.6 / §4.5.3.2 都补了同类括号引用, 口径应一致 |
| F2 | ig34_p0055_a016 | p55 "… both QNAM and QLABEL must be uniquely named (see Section 4.2.8.3 …) because they represent multiple values for a single variable." | ch04:1349 缺原因从句 "because they represent multiple values for a single variable" | **R2 实质语义丢失** (理由从句) | 补回原因从句 (ledger EQUIVALENT, T1 未分诊, 属 R3 "批内发现的叙述缺失也补") |
| F3 | ig34_p0054_a025 | p54 "… limitations of the SAS V5 transport file format (https://documentation.sas.com/)." | ch04:1328 缺 URL | R2 丢短语 (外链) | 补回 URL |
其余本批页 EQUIVALENT 改写 (p42_a018 "numeric," 前缀 / a020 / a021 / a025; p43_a019 加粗标签; p44_a010 "**Note:** … but describe"; p45_a011/a014 "is"→"="; p55_a010-a017/a021/a032 加粗/压缩) 逐条核: 无信息点丢失, 属词替换/标签, 记观察不计错; 按 B-CP 后补充口径 "词替换型改写" 可选恢复原词.

### 4. G-TB8
- trace 有本批 writer (`oh-my-claudecode:executor`, attempt 1×3 + attempt 2×2) 与 reviewer (`oh-my-claudecode:code-reviewer`, a1 CONDITIONAL / a2 PASS) 的 subagent_done; 无 `agent: main` 写 ch04 的记录 ✓. attempt 1 已按规则 B 归档 `evidence/failures/t2_B-ch04_attempt_1.{md,patch}` ✓.
- 时序缺口: writer "attempt2 续" (01:51:35, 三处 "Example when … checked:") 晚于 reviewer a2 PASS (01:50:21), review 文件无后续复审. 本 auditor 已核该三行与 p44/p45 逐字一致, 但终态无 reviewer 覆盖 — 记录在案.

### 5. 汇总
- seeded 样本: 独有丢失 0/10, 忠实度错 0.
- 补充发现: R2 丢失 3 (F1-F3, 其中 F2 实质), 忠实度错 0.
- **本批 FAIL** (按 R2 + R3, kb_files 内已知丢失不放行). 失败条目不删, 主控按规则 B 归档; attempt 3 只需补 F1-F3 三处 + fp/live docs 复跑.

## attempt 2 (审 writer attempt 4 终态; 2026-11-26, oh-my-claudecode:verifier / opus)

- 对象: ch04 md5 `4ea2579c4a8b7229a433d75e9c44cf92` (vs 6fea563 +323/−230). 文件 mtime 02:24:47Z < writer a4 done 02:26:33Z < reviewer a4 PASS 02:28:47Z.
- 判定: **PASS**. 样本 0/23 错; 全扫 (含表格原子) 无 R2 丢失; 上次 F1-F3 已修.

### 1. F1-F3 复核
| F | ch04:line | 现状 |
|---|---|---|
| F1 | 866 | "(see Section 7.3.1, Trial Visits)" 已补, 与 p42 逐字 |
| F2 | 1385 区 | p55_a016 原因从句 "because they represent multiple values for a single variable" 已在 (fwd 扫命中) |
| F3 | 1344 | URL (https://documentation.sas.com/) 已补 |

### 2. 抽样 (seed 20261127)
- 公式同 t2_auditor_v1.0; 因 attempt 3/4 已扩到 p22-59 全章, **C 扩为** 本批 atoms+recheck 的 prose ∪ p22-59 prose 原子中对 fp_baseline 新命中 ch04 的 (= attempt 1-4 实际改动原子); P 扩为 p22-59 prose (去 IE/ATOM_ERR/FIGURE/别批). 脚本: `$S/sample2.py` (S = scratch `t2_B-ch04_auditor`), 先 `fp_match.py --out $S/fp_a2.jsonl`.
- 结果: |C|=115, |P|=730, N=23 (=ceil(0.2×115)); 样本 C 12 + P−C 11.

| # | atom_id | PDF 页 + 摘要 | KB ch04:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | p32_a011 | p32 Note "QNAM references the parent variable name …" | 402 | 否 | 是 | §4.2.7.1 ✓ | 逐字 (L2 去 Note 标签) |
| 2 | p45_a025 | p45 "AEENTPT is final subject contact date …" | 1026 | 否 | 是 | §4.4.7 Examples ✓ | "=" 已还原 "is" |
| 3 | p43_a014 | p43 "Allowable values for --STRF are …" | 926 | 否 | 是 | ✓ | 新插入逐字 |
| 4 | p55_a012 | p55 "… first QNAM should describe the NSV without any numeric suffix." | 1382 | 否 | 是 | §4.5.3.2 ✓ | 逐字 |
| 5 | p43_a019 | p43 "Although COINCIDENT and ONGOING … --ENRF variables." | 930 | 否 | 是 | ✓ | 逐字 (行首导航标签保留) |
| 6 | p45_a011 | p45 "CMSTTPT is screening date …" | 1010 | 否 | 是 | ✓ | 逐字 |
| 7 | p55_a015 | p55 "The reason a digit integer or suffix is not appended …" | 1385 | 否 | 是 | ✓ | 逐字 |
| 8 | p42_a007 | p42 "This algorithm … fixed reference point …" | 868 | 否 | 是 | §4.4.4 ✓ | 逐字 |
| 9 | p42_a013 | p42 "For studies … prospectively defined schedule …" | 881 | 否 | 是 | §4.4.5 ✓ | 逐字 |
| 10 | p43_a017 | p43 "Allowable values for --ENRF are …" | 928 | 否 | 是 | ✓ | 逐字 |
| 11 | p44_a001 | p44 "… defined by each sponsor for each study." | 938 | 否 | 是 | ✓ | 逐字 |
| 12 | p42_a025 | p42 "The following lb.xpt sample rows show …" | 897 | 否 | 是 | ✓ | 逐字 |
| 13 | p37_a018 | p37 §4.3.5 句 | 665 | 否 | 是 | §4.3.5 ✓ | 未改动对照, 逐字 |
| 14 | p27_a027 | p27 §4.1.9 句 | 219 | 否 | 是 | §4.1.9 ✓ | 对照, 逐字 |
| 15 | p31_a014 | p31 Differences Between Grouping Variables 句 | 372 | 否 | 是 | §4.2.6 (PDF 同名小标题) ✓ | 对照 |
| 16 | p45_a040 | p45-46 "Note that using a date as a result … approached with caution" (原子截断) | 1041 | 否 | 是 | §4.4.9 ✓ | 原子带截断标记; KB 含完整句 |
| 17 | p23_a020 | p23 §4.1.7 句 | 71 | 否 | 是 | §4.1.7 ✓ | 对照 |
| 18 | p31_a016 | p31 同 #15 段 | 372 | 否 | 是 | ✓ | 对照 |
| 19 | p34_a007 | p34 §4.2.7.3 句 | 508 | 否 | 是 | §4.2.7.3 ✓ | 对照 |
| 20 | p24_a004 | p24 §4.1.7 列表项 | 79 | 否 | 是 | ✓ | 对照 |
| 21 | p52_a017 | p52 §4.5.1.2 列表项 | 1270 | 否 | 是 | §4.5.1.2 ✓ | 整节替换区, 逐字 |
| 22 | p57_a006 | 原子 "…Values to a Datasets." (原子错; PDF p56 "… to a Parent Domain") | 1464 | 否 | 是 | §4.5.4 ✓ | 原子 verbatim 错, KB = PDF 渲染 |
| 23 | p47_a008 | p47 §4.4.10 列表项 | 1102 | 否 | 是 | §4.4.10 ✓ | 整节替换区, 逐字 |

独有丢失 0/23, 忠实度错 0.

### 3. 重点区 (attempt 3/4 大改动) 对渲染 (`pdftoppm -r 110`)
| 区 | ch04:line | 核法 | 结果 |
|---|---|---|---|
| §4.4.10-§4.5.1 整节替换 | 1050-1290 | fwd: p46-52 全部原子子串比; rev: 该区每句/每格对 PDF | fwd 不命中仅 p46_a022 (KB "VSDTC−VSRFTDTC" 用 U+2212, PDF 为连字符; 信息无差), p49_a008 (PDF 笔误 occurrs, T-4), p51_a014 (原子含西里尔字母). rev 不命中仅 D6 变量表 (:1059-1063, 上方有 KB note)、导航标签 ":1096 **Scenarios where …**" / "Example n (xx.xpt)"、:1176 笔误更正. 节标题 (Disease Milestone Naming / Name (MIDS) / Timing Relative … / Use of … / Linking …) 与 p49-51 一致 |
| 伪节号 D6 块 | 248-261 | 读块 + 查 ch04 全部 "4.x.y" 标题在 p22-59 是否存在 | 4.2.1.1-3 伪节号已无; ch04 全部数字标题在 PDF 都有. D6 块 (--TESTCD ≤8 字符 / --TRT / --TERM 惯例) 不与 p28 矛盾 |
| --OBJ Mermaid | 516-528 | 对 p34 渲染 | 7 节点 / 6 条边方向与 Yes/No 标签逐一一致 (根→Parent record exists? Yes→Topic coded? / No→Name coded?) |
| 时长表 | 826-836 | p41 渲染 | 10 行 × 2 列 20 格一致 (P14DT7H57M, 12¼, 4 ½) |
| MK 表 | 223-225 | p28 渲染 | 7 格一致 |
| §4.2.7.1 5 张小表 | 421-447 | p32 渲染 | CMINDC ×3 + QNAM/QLABEL/QVAL ×2, 14 格一致 |
| 缺项日期表 | 770-777 | p40 渲染 | 6 行 × 3 列 18 格一致 ("2003-12-15T-:15", "13:-:17" 单连字符 ✓) |
| 基线表 (附带) | 1545-1549 | p59 渲染 | 3 行 × 5 列 15 格一致 |

### 4. 全扫 (独立脚本, 不用 writer scan5)
- 正向 `$S/fwd.py`: p22-59 ig34 全部原子 (含 TABLE_ROW/HEADER/CODE_LITERAL; 表格退到逐格比) 对 ch04 规范化子串. 不命中 41 条, 逐条定性: 原子 verbatim 错/截断 (p40_a024, p41_a010, p51_a014, p56_a001/a004/a005/a007, p57_a001/a002/a006/a012/a015/a018, p58_a003/a007/a013/a017, p59_a005/a010/a011/a018/a020/a021/a024/a025/a030, p25_a015 表头拼写) — 均以 PDF 页文本/渲染核过, KB = PDF; PDF 笔误已登记 (p26_a037 T-7, p37_a002, p49_a008, p53_a023, p57_a011); 标点/格式 (p22_a001 文件标题, p23_a010 URL 写法, p26_a039 冒号, p39_a004/a016 句末标点/"e.g.,"); CRF 选项块 3 (p32_a014, p33_a004/a021, 选项文字全在); p46_a022 U+2212. **无 R2 丢失**.
- 反向 `$S/rev.py`: ch04 :1-1549 每句/每格 (跳过 KB note 块/代码/标题) 对 p22-59 文本. 不命中 100 行, 全部可归类: D6 标注表 (Core / --STRF / --STRTPT / §4.4.10 变量表) 与 Mermaid 图注; 导航标签 (xx.xpt:, **For the subject:**, **Example n …**, **Important restriction …**, **Caution …**, **Exception — IETEST …**, 约定表 "Storage/Split rule/Label" 列); PDF 单元格折行 (qspi/suppqspi/MK/日期表/suppmh/约定表/基线表 — 已对渲染); CRF "[ ]" 选项; 已登记笔误更正 (:651, :1176, :1321, :1480). 未发现未标注的 KB 自写解释句.

### 5. 闸
- fp_match: ch04 对 base 唯一变化 ig34_p0013_a019 (hit_any 记 ch02; 句子仍在 ch04, grep -c = 1; 并行批所致) → 回归 0. 本批不命中 = p43_a034 / p56_a005 / p56_a006 (预期 3).
- `python3 tools/check_links.py` → `broken relative links: 18671 (live docs: 45)`. **超出基线 42 的 3 条来自 B-GF 的 evidence 文件** (`t2_B-GF.md` ×2, `t2_B-GF_review.md` ×1), 与 ch04 无关; ch04 本身没有新增坏链接. 请主控在 B-GF 处理.
- G-TB8: writer (executor, a1-a4) / reviewer (code-reviewer, a1-a4) 的 subagent_done 齐全; reviewer a4 PASS (02:28:47Z) 晚于 writer 最后一次改动 (a4 02:26:33Z; 文件 mtime 02:24:47Z) ✓; 无 main 写 KB; attempt 1-3 已归档 failures/ ✓.

### 6. 汇总
- 样本: 丢失 0/23, 忠实度错 0. 重点区 7 处对渲染 0 错. 全扫: 无 R2 丢失.
- 观察 (LOW, 不阻断): ch04:1080 "VSDTC−VSRFTDTC" 用 U+2212 (PDF 为 ASCII 连字符), 可选改回.
- **本批 PASS.**
