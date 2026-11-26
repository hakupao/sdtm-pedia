# 10 Tier B 内容修复 — Plan (Tier 3)

<!-- chain: E (plans) ; KB 改动走 Chain D -->
> 状态: **v1.2** (2026-11-26) — T1.4 用户 ack (R1-R4, 见 `evidence/checkpoints/t1_user_ack.md`); T2 范围扩为全 KB census; 执行中
> 模板: `~/.claude/templates/workflow-tier3.md` (+ tier2 基础)
> 前序: `archive/deep_verification/` (06 深审, 已冻结只读) RETRO 缺口 3 / 决策 2; `issues_found.md` Issue 5

> **TL;DR**: 06 深审在 G1 (99.02%) 达标后搁置了 Tier B. 原记 56 SD + 110 CT, 现行数据为 **49 SD + 93 CT = 142 节**,
> 1,389 个 gap 原子 (94% 是 PARTIAL 标签). ledger 标签可信度低 (P7 抽样 31/60 标签错), 所以**先分诊、后修复**:
> T0 立工具与可变异验证的闸 → T1 逐原子对照 PDF 原页分诊 (已在 / IE 候选 / 真缺 / 值差异 / 原子错) →
> T2 按 KB 文件分批修复 (writer / reviewer / auditor 三个不同 subagent_type; 表格逐格全检, prose 抽检 N) →
> T3 在工作副本上重算覆盖 → T4 总闸 + 人工抽样 + Chain D + push. `archive/` 与 `releases/` 全程不动.
> 主要风险: 标签噪声导致白修 / 改写式 PARTIAL 的裁决尺度不一 / 主会话越权直改 (06 Wave 2-3 发生过).

---

## 1. 需求 (why)

- **背景**: 06 深审回答了"每句 PDF 有没有去处"(覆盖率 99.02%), 但 PARTIAL 计为已覆盖. Tier B 的 142 节里,
  KB 内容"有但不全 / 被改写 / 表格值有出入". 用户目标是接近 100% 的高质量 KB, 不是"够用".
- **核心矛盾**: 现有度量 (p4b verdict) 把 IE 算进分母、PARTIAL 永不算命中, 不能直接当修复完成的判据;
  而 ledger / md_atoms 又落后于 KB 现状 (T4b Wave 1-3、v1.3、v1.4 C4 的改动都没回写).
- **衍生需求**: (a) 可复跑、可变异验证的覆盖重算; (b) Issue 5 的 PP-PC 表值差异单独结案;
  (c) 修完后下游 `hakupao/sdtm-rag` bump submodule.

## 2. 方案候选

| # | 路径 | 可达效果 | 核心问题 |
|---|---|---|---|
| A | 按 ledger 的 1,389 gap 直接逐条补写 | 快 | 标签噪声大, 大量白修 + 把已改写的好内容再堆一遍 |
| B | 全量重跑 P2 md_atomize + P4a LLM 匹配 (12,487 原子), 再修 | 度量最干净 | 估 4-7 工作日纯度量成本, 且 P4a 本身标签错率高 |
| **C** | **只对 Tier B 范围的原子做"PDF 原页 vs 现 KB"分诊 (确定性指纹预筛 + LLM 裁决), 再按文件修, 修后只回写这部分 ledger** | 范围精确, 成本可控, 判据落到 PDF 原页 | 需要自建工作副本 ledger + 重算脚本, 须做变异验证 |

**选 C**. B 留作可选后续 (见 §9 Q7).

## 3. 决策

### 3.1 关键边界决策

| ID | 决策 | 默认值 |
|---|---|---|
| B1 | 真值来源 | **PDF 原页** (`source/cdisc/SDTMIG v3.4 (no header footer).pdf` 461 页 / `SDTM_v2.0.pdf` 74 页, 页码与 atom.page 已核对一致). `pdf_atoms` 是 LLM 抽取的, 只当索引, 不当真值 |
| B2 | `archive/` | 全程只读. ledger / section_coverage 复制到 `work/` 下改 |
| B3 | `releases/` | **不动** (v1.4 冻结). 修复只进 `knowledge_base/`; 是否出 v1.5 另议 (§9 Q5) |
| B4 | 改写式 PARTIAL (如 §4.4.7 --STRF 被改成表格) | 语义完整且无信息丢失 → 保留改写, 记 EQUIVALENT; 有任何丢失 → 补回 PDF 原文 (verbatim 优先). 裁决尺度见 §9 Q2 |
| B5 | 域 spec 表行 (452 条探针缺) | 先用脚本逐行比对 `domains/XX/spec.md` 的 name / label / type / core: 全一致 → IE 候选 (按 P6 T2 Round 2 SPEC_TABLE_ROW 先例); 有不一致 → VALUE_DIFF. IE **逐条列清单, 用户 ack 后才生效** |
| B6 | 值差异 (PDF 与 KB 不一致; 现成例: `chapters/ch03_submitting_data.md:31` 写 COOTC, PDF 为 CODTC) | 以 PDF 原页为准修 KB; 若 PDF 自身疑似笔误 → 不改, 记 `discrepancies.md` 并标注 |
| B7 | Rule D | 每批 writer / reviewer / auditor **三个不同 subagent_type**, 各自独立调用. **禁止主会话直接改 KB, 禁止主会话充当 reviewer** (06 Wave 2/3 的教训) |
| B8 | 表格与数据值 | **逐格全检 (census)**, 不抽样. 抽样 N 只用于 prose 的位置与忠实度 |

### 3.2 风险与应对

| 风险 | 应对 |
|---|---|
| 标签噪声 → 白修 | T1 先分诊, 只有"真缺 / 值差异"进 T2 |
| 裁决尺度漂移 (不同 writer 对"改写是否丢信息"标准不一) | T1 出 10 条标定样例 (calibration set) 写进 prompt; reviewer 用同一样例集 |
| 修复引入幻觉 / 非 PDF 内容 | T3 反向溯源: 每条新增 KB 行必须定位到 PDF 页 |
| 同文件并发冲突 | 一批 = 一个 KB 文件 (或一个域目录); 同一文件绝不并行 |
| 闸本身失效 (表上 PASS 实际没测到) | T0 变异验证: 删一句 / 改一格, 闸必须变红 (retrospective §4 规则 5) |
| ledger 回写时把改动外的原子也翻了 | 回写脚本只接受带 `tb_batch` + 证据的原子; T3 diff 断言改动集 ⊆ 分诊集 |

## 4. 实施 (Step 表)

Checkpoint: **hard** = 停等用户 ack (不可预授权跳过); soft = 汇报后继续; none = 直跑.

| Step | 任务 | 输入 | 输出 | 目标指标 | Ckpt | Parallel |
|---|---|---|---|---|---|---|
| T0.1 | 基线清单 | archive 数据 + git `f024a3f` | `inventory.{md,jsonl}`, `inventory_table.md` | 56/110 复现; 现行 49/93 | none | — |
| T0.2 | 工作副本 + 重算脚本 | archive ledger/atoms | `work/coverage_ledger.wc.jsonl`, `scripts/t3_recompute.py` (p4b 重定向 + §5 新指标) | 未改动时输出与现行 section_coverage 去掉 `aggregated_by` 后全等 (本次已验: 399 行全等) | none | T0.3 |
| T0.3 | PDF 页文本缓存 | source PDF | `work/pdf_pages/{ig34,sv20}_pNNNN.txt` (`pdftotext -layout`) | 535 页齐全, 抽 5 页人工比对 | none | T0.2 |
| T0.3b | 读 KB 的两个检查器 | PDF 页缓存 + 现 KB | `scripts/fp_match.py` (指纹匹配, 以 `t0_inventory.py` 的 `norm()` 为起点) + `scripts/table_census.py` (KB 表格 vs PDF 页逐格) | 在 p275-284 (B-PCPP) 试跑: census 能解析该段全部表; 解析失败的表列出来改人工逐格 | soft | — |
| T0.4 | 闸的变异验证 | T0.2-T0.3b 全部脚本 | `evidence/checkpoints/t0_mutation.md` | 在 KB 临时副本里: 删 1 句 prose → fp_match 红; 改 1 表格值 → census 红; 删 1 子节 → fp_match + t3_recompute 红; 复原后全绿. 注意 p4b 本身只读 ledger, 单独变异它测不到 KB | **hard** | — |
| T1.1 | 确定性预筛 | 分诊范围 (§5.0) 1,459 gap 原子 + PDF 页 + 现 KB | `work/triage_prefilter.jsonl` | 每原子一行: 指纹命中位置 / spec 行判定 / 目标文件 | none | — |
| T1.2 | LLM 分诊 (按节分包, ~50 原子/包) | 预筛 + PDF 页 + KB 片段 | `work/triage.jsonl` | 100% 原子有 class ∈ {PRESENT, REWRITE_OK, RELOCATE, IE_CAND, REAL_GAP, VALUE_DIFF, ATOM_ERR, FIGURE, LOCATE} | soft | 包间并行 ≤4 |
| T1.3 | 分诊复核 | T1.2 | `evidence/checkpoints/t1_review.md` | REAL_GAP / VALUE_DIFF / ATOM_ERR / REWRITE_OK / RELOCATE / FIGURE / LOCATE **100% 复核**; PRESENT / IE_CAND 抽 20% | soft | — |
| T1.4 | 用户 ack | IE_CAND 清单 + REWRITE_OK 尺度 + 分诊汇总 | `evidence/checkpoints/t1_user_ack.md` | 用户逐类确认; 定 T2 批次表 | **hard** | — |
| T2.n | 分批修复 (§6 批次表) | T1 的 REAL_GAP + VALUE_DIFF + RELOCATE (+ LOCATE 定位后) | KB 改动 + `evidence/checkpoints/t2_<batch>.md` | 见 §5 G-TB4/5/6 | 首批 **hard**, 其后 soft | 不同文件 ≤4 批并行 |
| T2S.n | T2 后扫描批 (实际 22 批: S-EVT/INT/FND/SPC1/SPC2/HOST/TDM/TUFA/SPREL, S-CH1/CH4/CH8/CH10, S-MOD1-3, S-SPEC1-4, 然后 S-CT (U5/U6 脚本批, 先 dry-run) → S-TYPO 串行) | `evidence/t2_coverage_matrix.md` §7 分组 + U1-U4 | KB 改动 + `evidence/checkpoints/t2_S-*.md` | 批内文件按 PDF 完整节页范围双向全扫; 覆盖矩阵重跑后该批文件全 F 且 D/S/A/F 缺口清零; Rule A: auditor N = min(30, max(20, ⌈0.1·|P|⌉)) seed 20261126 (`subagent_prompts/t2s_scan_review_audit_v1.0.md`) | 首批 S-EVT 试点 soft (吸收教训后再并行), 其后 soft | 不同文件 ≤4 批并行; S-TYPO 最后串行 |
| T3.1 | ledger 回写 (工作副本) | triage + 各批证据 | `work/coverage_ledger.wc.jsonl` 更新 | 改动集 ⊆ 分诊集; 每条带 `matched_by.phase="TB"` | none | — |
| T3.2 | 重算 + 反向溯源 | wc ledger + KB git diff; 先用 fp_match 对**所有**靠指纹定的 EXACT/EQUIVALENT 在现 KB 上复验一遍 | `evidence/checkpoints/t3_recompute.md` | §5 G-TB1/2/3/7 | soft | — |
| T4.1 | 总闸独立审 | 全部证据 | `evidence/checkpoints/t4_gate_review.md` | 第四个 subagent_type 判 PASS | soft | — |
| T4.2 | 人工抽样 | 分层 N=30 (§5.3) | `evidence/checkpoints/t4_human_sample.md` | 用户判内容错误 0 | **hard** | — |
| T4.3 | 收尾 | — | Chain D 三件 + worklog + PROGRESS + RETROSPECTIVE.md + commit/push + 提醒 sdtm-rag | links live docs ≤ 42 | soft | — |

## 5. 验证

### 5.0 范围

分诊与闸统一覆盖: Tier B 并集 173 节 (现 142 + 已升级 31, 其 gap 共 1,446) **+ Issue 5 主节** §6.3.5.9.3 (STRUCTURE_DRIFTED, 13 MISPLACED) = **1,459 gap 原子**.
已升级的 31 节只剩 57 gap, 一并处理, 避免闸范围与分诊范围不一致.

终态类 (每个原子必落其一): EXACT / EQUIVALENT (含 REWRITE_OK, RELOCATE 移位后) / INTENTIONAL_EXCLUDE (已 ack) / ATOM_ERR (登记) /
PDF_TYPO (PDF 疑似笔误, 登记 + 用户 ack) / FIGURE_DEFERRED (图, 12 条, 登记; 06 已有同类先例).

### 5.1 闸定义 (G-TB, 全部量化)

stock p4b verdict 只做**参考列**, 不当闸: 它的密度分母含 IE, PARTIAL 永不算命中 (现 142 节里 47 节去 IE 后密度已 ≥0.80).

| Gate | 条件 | 阈值 |
|---|---|---|
| G-TB1 | §5.0 范围内每个非 HEADING 原子都落到一个终态类 | 残留 PARTIAL / MISSING / ERROR / MISPLACED / LOCATE = **0**; ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED 每条有登记 + 用户 ack |
| G-TB2 | 节级: `density_excl_ie = (EXACT+EQUIV) / (非 HEADING − IE − ATOM_ERR − PDF_TYPO − FIGURE_DEFERRED)` | 每个有内容的节 = **1.00**; 纯结构父节 (21 个) 所有子节达标即达标 |
| G-TB3 | 全局覆盖率 (06 口径, 便于对比) | ≥ 99.02% 且不下降; 报告新值 |
| G-TB4 | 表格逐格 census (`table_census.py`; 解析不了的表由 reviewer 人工逐格并留表): 本项目触碰过的表 | 不一致 = **0** (PDF_TYPO 登记例外) |
| G-TB5 | Rule A prose 抽检 (§5.3) | 独有信息丢失 = **0**, 忠实度错误 = **0**; 任何 1 条错 → 该批 FAIL 重做 |
| G-TB6 | 反向溯源: KB git diff 每条新增内容行 → 能在 PDF 对应页找到 (归一化子串或 reviewer 签字的结构性行如表头/锚点) | **100%** |
| G-TB7 | `python3 tools/check_links.py` 末行 live docs | ≤ **42** (现基线, `docs/PATH_MAP.md`) |
| G-TB8 | trace.jsonl 中每批有 3 个不同 subagent_type 的 `subagent_done`; 无 main-session 写 KB 的记录 | 100% 批次 |
| G-TB9 | T0.4 变异验证 (针对 fp_match / table_census / t3_recompute) | 3/3 变红再复原变绿 |

### 5.2 覆盖重算 (T3) 怎么做

1. `scripts/t3_recompute.py` = `archive/deep_verification/scripts/p4b_section_aggregate.py` 的重定向副本 (BASE 指 `work/`, 输出 `work/section_coverage.wc.jsonl`), 外加 G-TB1/G-TB2 新指标列. 不改原脚本.
2. PARTIAL 的重新裁决没有 P4a 脚本可用, 两条路:
   - 确定性: 用 T0.3b 的 `fp_match.py` (起点是 `t0_inventory.py` 的 `norm()`; 扩展 tab/空格、粗体、弯引号、表格管道符), 命中目标节 → EXACT/EQUIVALENT, 记 `matched_by`.
     **不要**照搬 `p6_t5_update_ledger.py`: 它没有匹配器, 只是把 MISSING 批量翻成 EQUIVALENT (依据是 Wave 1-3 的人工确认), 只能参考它的 `matched_by` 字段格式;
   - 非逐字的 (REWRITE_OK): 以 T1.2 + T1.3 两个 agent 的一致判定为准, 写入 `matched_by.evidence`.
3. `md_atoms.jsonl` 不重抽 (D7 后续项); 反向方向用 G-TB6 的 git-diff 溯源代替.
4. 每次重算前后各留 md5, 写进 `_progress.json`.

### 5.3 Rule A 抽样 N

- **每批 (prose)**: N = max(10, ceil(0.2 × 本批改动 prose 原子数)), 上限 30; 随机种子写进 checkpoint; 样本不限于 writer 声明的改动.
- **表格 / 数据值**: 不抽样, G-TB4 全检.
- **T1 分诊复核**: 高风险类 100%, PRESENT / IE_CAND 20%.
- **T4.1 总闸**: 跨批分层 N=72 (PRESENT / REWRITE_OK / REAL_GAP / VALUE_DIFF / IE 五类各 12, 外加**对照层 12 条**: 本范围内原本就标 EXACT/EQUIVALENT、本项目没碰过的原子 — 验 P4a 匹配器的旧标签, 见 Q9), 总闸 reviewer 与各批 auditor 不同 agent.
- **T4.2 人工**: 分层 N=30 交用户 (REWRITE_OK 10 / REAL_GAP 10 / VALUE_DIFF+IE 10). 判据: 内容错误 0 (P7 用 <5%, 这里按接近 100% 的标准收紧).
- 结果统一进 `audit_matrix.md`; 失败条目不删 (规则 B).

## 6. 批次 (按 KB 文件切, 避免冲突)

最终批次表在 T1.4 定 (只给有 REAL_GAP / VALUE_DIFF 的文件开批). 下表为预排, 数字是 T0 探针上界:

| 批次 | 文件 | 节 | 探针缺 | 说明 |
|---|---|--:|--:|---|
| B-PCPP | domains/PC/{examples,assumptions}.md + PP/examples.md | 3 | — | Issue 5; 整表逐格; 首批 (hard) 用它定型 |
| B-ch04a / B-ch04b | chapters/ch04_general_assumptions.md (§4.1-4.3 / §4.4-4.5) | 22 | 126 | 同文件, **串行** |
| B-ch02 | chapters/ch02_fundamentals.md | 8 | 57 | |
| B-ch01 | chapters/ch01_introduction.md | 5 | 53 | |
| B-ch08 / B-ch03 | chapters/ch08 / ch03 | 8 | 37 | 两文件一批 |
| B-model | model/02,03,04,05 (sv20) | 14 | 48 | 4 文件一批, 文件间串行 |
| B-dom1..dom6 | domains/* 按探针缺量装箱, 每批 ≤ 8 个域目录 | 58 | 619 | 其中 spec 行 452 预计走 IE, 真修量大幅小于此 |

- 并行: 不同文件的批次一次最多 4 个; 每 3-5 批写一次 `phase_report`.
- 每批流程: writer (`oh-my-claudecode:executor`, opus) 改 KB → reviewer (`oh-my-claudecode:code-reviewer`) 对 PDF 页逐条核 + 表格 census 脚本 → auditor (`oh-my-claudecode:verifier`) 做 §5.3 抽样 → 主控判定. 批 FAIL → **先** `git diff -- <files> > evidence/failures/t2_<batch>_attempt_N.patch` 并写同名 `.md` (输入/产物/技术判定/业务判定/下一 attempt 输入), **再**按 §8 回到批前 commit 重派.
- RELOCATE: writer 可把内容从错的文件/节移到正确节 (这是唯一允许的删除), 报告里逐条列出原位置与新位置.
- T1 分诊: writer `oh-my-claudecode:scientist`, reviewer `oh-my-claudecode:critic`. T4.1 总闸: `feature-dev:code-reviewer` (未在本项目其它环节用过).

## 7. 成本估计 (区间, T1 后收敛)

| 段 | 依据 | 估计 |
|---|---|---|
| T0 | 脚本 + 变异验证 | 0.5 session |
| T1 | 1,459 原子 / 50 每包 ≈ 30 包 + 复核 | 1.5-2.5 sessions; ~28 writer + ~10 reviewer 调用 |
| T2 | 真修量假设 300-700 原子 (944 上界扣 spec 行与改写合格) → 10-14 批 | 3-6 sessions; 每批 3 个 agent 调用, 共 30-42 |
| T3-T4 | 重算 + 总闸 + 人工 30 条 + 收尾 | 1-1.5 sessions |
| T2 (v1.1 重估) | 分诊 308 + 全 KB census 净 548 ≈ 856 项 → 16-17 批 | ~8 sessions; 48-51 次调用 |
| T2 (v1.2) | 59 批 (D1, 每 KB 单元一批), 886 项 | ~177 次调用, 约 15-20 sessions |
| 合计 | | **v1.2: 18-24 sessions** (v1.1: 10-12) (v1.0: 6-10), ~70-90 次 subagent 调用 (opus 为主) |

超出上限 20% → phase_report 里报警, 停下问用户是否收缩范围.

## 8. 回滚与下游

- **回滚**: 每批过闸后一个本地 commit (不 push; 需用户同意, 见 Q8). 失败批: 先存 patch 到 `failures/` (规则 B), 再 `git checkout <上一批 commit> -- <本批文件>`, 只回本批文件 — 同文件串行批 (ch04a → ch04b) 因此不会丢掉已过闸的前半. 已 commit 的批事后要撤 → `git revert <commit>`. 工作副本 ledger 每次回写前备份 `work/*.bak.<step>`. `archive/` 从不写, 无需回滚.
- **Chain D**: 每个改过的 KB 文件 → `.work/meta/mapping.md` → `docs/TRACEABILITY.md` → `.work/meta/worklog/<phase>.md`.
- **Issue 关闭**: Issue 5 在 B-PCPP 过闸后改为"已修复 (含值层)"; 其余新问题顺延 issues 编号.
- **releases/**: 不碰 (v1.4 冻结). web 站读 v1.4, 也不变.
- **push 时机**: 默认 T4 全过后一次 push (见 §9 Q4); push 后提醒用户在 sdtm-rag 仓说「KB 更新」bump submodule.
- **不在 archive 里补记**: 06 的 RETRO / ledger 保持原样; 本项目结论写在 `.work/10_tier_b_repair/RETROSPECTIVE.md`, 并在 `docs/PROGRESS.md` 指向它.

## 9. 开放决策 — 已拍板 (2026-11-25, 用户: "按你的建议开工" → 全部采用默认建议)

> §3.1 的 B1-B8 是本 PLAN 已定的边界; 下面 Q1-Q9 是待用户定的.

| ID | 问题 | 默认建议 |
|---|---|---|
| Q1 | 452 条域 spec 表行归 IE? (前提: 脚本逐行比对 spec.md 的 name/label/type/core, 不一致的转 VALUE_DIFF) | 归 IE, 逐条清单 ack |
| Q2 | 改写式 PARTIAL 的尺度: 语义完整即可 (REWRITE_OK), 还是一律补回 PDF 原文? | 语义完整即可; 有丢失才补原文 |
| Q3 | 闸用 G-TB1/2 (残留 0 / 去 IE 密度 1.00, 带登记例外) 替代 p4b verdict? | 是 |
| Q4 | push 节奏: T4 后一次推, 还是每批过闸就推 (sdtm-rag 可更早受益)? | 一次推 |
| Q5 | 修完是否出 v1.5 release / 刷 web? | 本项目不做, 另立 |
| Q6 | 目录编号: `.work/08_` 已被 `08_repo_refactor_v2` 占用, 是否改名 `10_tier_b_repair`? | 已改名 `10_tier_b_repair` |
| Q7 | 是否把全量 md_atoms/P4a 重跑 (方案 B) 列为后续? | 列后续, 不在本项目 |
| Q8 | 允许每批在本地 commit (便于按批回滚; 不 push)? | 允许 |
| Q9 | 已标 EXACT/EQUIVALENT 的原子 (同一 P4a 匹配器, P7 发现过同表错行) 是否也要验? | T4.1 加对照层 12 条; 若发现错 → 扩为全量指纹复验 |

## Changelog

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-11-25 | 初稿: T0 基线已出, 其余待 §9 拍板 |
| v1.3 | 2026-11-26 | 加 T2S 扫描批步 (覆盖矩阵 §7 分组; 新 brief `t2s_scan_writer_v1.0.md` / `t2s_scan_review_audit_v1.0.md`; U3 宿主按 PDF 标题序定首域; 排版字符统一归 S-TYPO) |
| v1.2 | 2026-11-26 | T1.4 补充 D1-D5: 59 批; 去重 + 删扩写 (RELOCATE 外新增允许的删除: 重复副本去重 / 超出 PDF 的扩写); 成本 18-24 sessions |
| v1.1 | 2026-11-26 | T1.4 ack: R1 v2.0 表行 IE / §1 引言补; R2 丢短语即 REAL_GAP (B4 收紧); R3 T2 纳入全 KB census (Q9 升级触发); R4 IE 587 ack, 44→PRESENT; 成本 10-12 sessions |
| v1.0 | 2026-11-25 | 用户拍板 Q1-Q9 = 默认建议; 进入 T0.2 |
| v0.1.1 | 2026-11-25 | advisor 复核: 加 T0.3b 读 KB 的检查器 + 变异对象改正; 分诊/闸范围统一 1,459; 加 RELOCATE/FIGURE/PDF_TYPO 终态; 回滚先存 patch; §9 改 Q 编号; T4.1 加对照层 |
