# Stage v2.1 Regression Evidence — T3 (PC↔PP RELREC 4 方法)

> 归档日期: 2026-04-19
> 触发: STAGE_V2.1_AB_REPORT 中 T3 精度判定为 ↓
> 规则 B (失败归档不删) + 规则 D (写/审分离) 强制落盘
> 本文件 Writer 段由主控写, Reviewer 段由独立 code-reviewer subagent 落, 两段互相隔离

---

## 1. 题目输入 (原样)

**T3**. PC↔PP 通过 RELREC 关联的 4 种方法?

- 背景: PC (Pharmacokinetics Concentrations) 和 PP (Pharmacokinetics Parameters) 是 PK 分析两核心域, PP 的 NCA 结果需要追溯到 PC 的原始浓度点, RELREC 是 SDTM 标准表达跨域关系的机制.
- SDTMIG v3.4 在 §6.3.5.9.3 给出 4 种方法的完整 example narrative + 数据表 — 这是本题期望答案来源.

## 2. v1 产物 (压缩版, SDTM Expert v3.4)

- 明确声明 `§6.3.5.9.3 不在 Project Knowledge 中`
- **基于可见通用规则重建**:
  - Method A: Peer-record linking (PC record ↔ PP record via matching PCSEQ/PPSEQ)
  - Method B: Group linking (via --GRPID, 每个 concentration group 对应一个 parameter set)
  - Method C: Dataset-level MANY/MANY via RELREC 表 (RELTYPE=MANY/MANY)
  - Method D: Implicit join (无 RELREC, 通过 USUBJID + TPT + VISIT 隐式匹配)
- 每种方法标注 `推测` / `reconstruction based on general rules`
- 给出决策树: 何时用 A vs B vs C vs D
- 用户可得完整实用答案, 但有 1 个推测风险点 (Method B 的 GRPID 用法未必 1:1 对应 v3.4 §6.3.5.9.3 原文)

## 3. v2.1 产物 (chapters 全展开版, SDTM-Knowledge-v2)

- 立即触发 **边界模板** (system_prompt_v2.md 定义的 refusal template):
  > "§6.3.5.9.3 PC↔PP examples 在当前 Project Knowledge 中未完整收录, ch06 仅含 domain 骨架. 无法给出完整 4 种方法 narrative."
- 仅引用 `§8.3 MANY/MANY` 一句 (ch08 §8.3 已在 v2.1 全展开)
- **拒绝重建**, 不给决策树
- 产出长度 ~1/6 v1
- 边界诚实性 ↑, 实用性 ↓

## 4. 技术判定

- **是否 RAG 检索失败**: **否**. v2.1 边界模板正确触发 — §6.3.5.9.3 确实不在本阶段上传文件中 (本批 batch 1 只展开 chapters, 不含 examples 数据表); RAG 找不到内容是预期行为, 非检索故障.
- **是否内容损失**: **否**. v2.1 比 v1 多了 02_chapters.md (ch08 §8.3 MANY/MANY 原文, v1 压缩版没有); 其余 8 文件 md5 与 v1 baseline 完全一致 (A3 Step 1 11/11 PASS + cowork 上传后 capacity 13% vs v1 12% 确认全体上传成功).
- **是否 model 变差**: **否**. 相同 Opus 模型, 相同 Instructions 框架 (system_prompt_v2.md 基于 system_prompt.md 增量修订, 未删除任何 v1 的能力指令).
- **根本成因**: v2.1 更严格地执行了 `拒绝在未收录内容上幻觉` 的设计约束, 这是 PLAN_V2.md §1 规则 A "语义严谨" 的副作用.

## 5. 业务判定 (Writer 初判 — 待 Reviewer 归因)

- **影响**: 单点 (只 T3), 无扩散 (其他 7 题无类似表现 — T1/T2/T4/T5/T6/T7/T8 均未因"内容未收录"而拒答); T6 同样提示边界 (07 是目录不是数据) 但给了更多 catalog 信息, 说明 v2.1 拒答机制是精准的, 只在真正无源时触发.
- **是否值得回滚**: 不建议. v1 的 Method B/D 推测带幻觉风险; v2.1 拒答更符合 SDTM 严谨性要求 (监管场景下幻觉代价 >> 拒答代价). 规则 A 明确"结构检查 ≠ 语义检查, 宁缺毋滥".
- **修复路径**: 在 batch 2 (Stage v2.2, Task D1-D4) 的 examples 高频展开中纳入 ch06 §6.3.5.9.3 PC↔PP example narrative + 数据表; 预计能同时修复 T3 + T6 (AE Ex2 数据行) 两个缺口. 已在 STAGE_V2.1_AB_REPORT §"后续修复方向" 表列出.

## 6. 下一 attempt 输入 (规则 B 要求)

- **要避免的问题**: 下批 extract_examples_data.py 必须包含 PC 和 PP 域 (不依赖单纯打分, 主控人工补 — PLAN_V2.md §6 D1 Step 2 已明确 "PC, PP 为 T_test_hits 必选").
- **预期改善**: v2.2 A/B 测试中 T3 重测, 期望从 ↓ 升到 持平 或 ↑.
- **验证点**: Reviewer 独立抽样 ch06 §6.3.5.9.3 的 4 个 Method narrative 是否均被 09_examples_data_high.md 完整收录.

---

## 7. Reviewer 归因 (独立 code-reviewer subagent, opus, 与 writer 上下文隔离)

> 填写者: code-reviewer subagent (subagent_type=code-reviewer, model=opus)
> 填写时间: (由 reviewer 注入)
> 隔离证据: subagent 由主控 spawn, 不继承 writer session, 独立读取 AB 报告 + v1/v2 system prompts + chapters 源文件

<!-- REVIEWER_VERDICT_BEGIN -->
## 7.1 Reviewer 身份与独立性声明
- Subagent: oh-my-claudecode:code-reviewer, opus (1M context)
- 隔离: 未读 writer session, 独立 Read AB 报告 + v1/v2 system_prompt + v1/v2 02_chapters.md + knowledge_base 源 ch08 + PLAN_V2
- 时间: 2026-04-18T23:58:45Z

## 7.2 证据核查记录
- (1) STAGE_V2.1_AB_REPORT.md: 已读 (172 行); 确认 T3 唯一 ↓, T1-T8 另 5↑/2 持平/0 FAIL, T9-T12 4/4 PASS; §"后续修复方向" 已列 T3 路径 (batch 2 纳入 ch06 §6.3.5.9.3 PP/PC examples) — 注: 表述里写的是 "ch06", 但 SDTMIG §6.3.5.9.3 物理上位于 knowledge_base/chapters/ch08_relationships.md 及 domains/PP,PC/examples.md, 不在独立 ch06 文件 (ch06 不存在).
- (2) system_prompt_v2.md: 已读 (119 行); v2 相对 v1 仅 append `<!-- stage v2.1 begin -->` 块 (113-119 行), 内容为 "02_chapters.md 已升级为完整版 / 原精简兜底句作废"; 无新增 refusal 规则.
- (3) system_prompt.md (v1): 已读 (112 行); 边界规则 (line 60/64/100/110/112 "坦诚边界 > 臆造补全 / 不臆造") 与 v2 完全一致, byte-identical on refusal policy.
- (4) ch06_relationships.md: 不存在于 knowledge_base/chapters/ (glob 仅 ch01/02/03/04/08/10 六文件); §6.3.5.9.3 Method narrative 的源在 ch08_relationships.md 第 140/169 行只给了 "see ... §6.3.5.9.3" 交叉引用, 实际 4 方法原文在 domains/PP/examples.md 与 PC examples — 未上传本批.
- (5) v2 02_chapters.md: grep `6.3.5.9.3` 命中 3 次 (line 1964, 1993, 2520), `PC↔PP` 命中 0 次, `PCREFID` 命中 0 次; 均为交叉引用 + specimen-grouping 段, 无 4 Method narrative 或数据表.
- (6) v1 02_chapters.md: grep `6.3.5.9.3` 命中 2 次 (line 1805, 1821), `PCREFID` 命中 0 次, `Method A/B/C/D` 命中 0 次; 与 v2 一样只含交叉引用, v1 也没有 PC↔PP 4 方法原文. → 决定性: (c) 内容损失否定, v1 也没有源内容, v1 答案的 Method A/B/C/D 完全由模型基于通用 RELREC 规则推测得出.
- (7) PLAN_V2 §1: 已读 (P1-P10); P9 要求压缩率 >50% 步骤 N=10 抽检, 本次 chapters 是 expansion 非 compression, P9 对 T3 不直接适用; P10 "T1-T8 ≥1 题 ↓ 写 regression evidence + reviewer 归因" 已触发, 本文件就是落实.

## 7.3 归因结论
- 主因: **(a) 设计意图 — 边界模板严谨性**
- 次因: v2.1 stage 增量 (`system_prompt_v2.md` 113-119 行) 显式声明 "02_chapters.md 已升级为完整版", 使模型对 "某 section 未收录" 的判断更有信心, 从 v1 "没有源就推测" 漂移到 v2 "没有源就拒答"; 这不是新增规则, 是既有 "不臆造" 规则在更清晰覆盖信号下的行为加强.
- 理由: §7.2-(5)(6) 确认 v1/v2 02_chapters.md 对 §6.3.5.9.3 都只有交叉引用, 零内容损失 → 否 (c); §7.2-(2)(3) v1/v2 prompt 边界规则 byte-identical → 否 (d); §7.2-(4)(5) 源确实未上传, RAG 找不到是正确行为 → 否 (b). v1 的 4 方法是纯幻觉重建, v2 拒答是规则 A "宁缺毋滥" 的正确执行.

## 7.4 与 Writer §5 业务判定是否一致
- **一致**
- Writer §4 技术判定 (非 RAG fail / 非内容损失 / 非 model 变差 / 根因=规则 A 副作用) 与 §5 业务判定 (单点无扩散 / 不建议回滚 / 修复走 batch 2 examples) 均与本 Reviewer 独立结论吻合; 仅微调: Writer §5 写 "ch06 §6.3.5.9.3", 实际应为 "ch08 交叉引用 + domains/PP+PC examples §6.3.5.9.3 narrative" (ch06 文件不存在, 不影响结论, 修复路径语义正确).

## 7.5 对下一步的建议
- 是否继续 Phase D Task D1? **yes**
- 域清单约束: D1 的 `extract_examples_data.py` 高频域列表必须**硬性包含 PC 和 PP** (不依赖打分排名, 主控人工 pin). 对应 PLAN_V2 §6 已记录 "PC, PP 为 T_test_hits 必选", 请 executor 落实到脚本参数, 并在 v2.2 A/B 中重测 T3.
- 额外验证点: D1 完成后, reviewer 需抽样确认 09_examples_data_high.md 完整包含 PP examples §6.3.5.9.3 的 4 Method narrative (Peer-record via --SEQ、Group via --GRPID、Dataset MANY/MANY via RELREC、Implicit join) — 若源 PP/PC examples 实际只给 1-2 种而非 4 种, 则 Writer §2 "4 方法" 假设本身需修订.

## 7.6 规则 P9 语义抽检补充
- 建议对 T3 做 **N=3 样本复测** (v2.1 Project 不重建, 只改写问法), 确认是 boundary-rigor 一致表现而非 prompt 措辞偶发:
  - Q3a: "PP 如何追溯到 PC 的原始浓度点? 列出所有机制."
  - Q3b: "SDTMIG §6.3.5.9.3 给出哪些 PC↔PP 关联方式? 请逐一说明."
- 预期: 3/3 均触发边界模板 (拒答 + 指向源) 则确认 (a) 归因; 若出现 1 次给完整 4 方法答案, 则说明 prompt 措辞会绕过边界模板, 属 model 鲁棒性问题, 需在 system_prompt_v2.md 明示 "问 §6.3.5.9.3 时必走 template ①".
<!-- REVIEWER_VERDICT_END -->
