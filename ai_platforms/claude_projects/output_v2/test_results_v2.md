# v2 A/B 测试结果矩阵

> 用户每阶段后回填; 主控写入并归档到 evidence_v2/stage_v2.X_audit.md + evidence_v2/checkpoints/ckpt_v2.X.md

## T1-T8 回归 (源自 v1)

| # | 题目 | 期望 | v1 答案 | v2.1 答案 | v2.2 答案 | 精度 vs v1 | 精度 vs v2.1 | 阶段 |
|---|-----|------|--------|----------|----------|-----------|-------------|------|
| T1 | AE.AEDECOD 的 Core 属性是什么? | Req (mega_spec + variable_index) | Core=Req, 引 05 mega_spec §AE + 04 variable_index(Sy/R) + 02 §4.3.6 | 同 v1, 来源等同 | Core=Req + §4.3.6 三元 (AETERM/AEMODIFY/AEDECOD) + AEDECOD 在其他 Events 域为 Perm 对比 + AEPTCD 配套 | 持平 | 持平 (略 ↑) | v2.2 |
| T2 | AE 严重程度变化如何记录? | AEGRPID 方案 | 3 方案 A/B/C + E2B/CTCAE 延伸 | 同 3 方案 + 5 处章节锚点 (§4.2.1/§4.3.6/§8.6.3/assum7e/AE3b) | ↑ | v2.1 |
| T3 | PC↔PP 通过 RELREC 关联的 4 种方法? | Method A-D | 声明 §6.3.5.9.3 不在 Project, 基于通用规则重建 3+1 方法 (含推测标注) | **严格拒答完整 4 种**; 仅引 §8.3 MANY/MANY 一句; 边界模板触发 | **↓** | v2.1 |
| T4 | 哪些域有 EPOCH 变量? | 44 个域 | 44 域按 class 分组 + CT C99079(44) + 19 不含域 | 同 44 域分组, 增 §4.1.3.1 EPOCH-Capable Domains 原文锚点 | ↑ | v2.1 |
| T5 | 如何判断变量是否需要提交到 SUPP--? | ch08 §8.4 规则 | 7 级优先级决策树 + §8.4.4 4 条禁令 | 5 步决策树 (合并 step 6/7) + §8.4.4 + SUPP-- spec 表格 | 持平 | v2.1 |
| T6 | AE Example 2 的具体数据是什么? | 数据表 | 严格拒答 (07 是目录), 给标签+演示意图 | 同严格拒答, 额外给 6 个 AE Examples catalog 表 | ↑ | v2.1 |
| T7 | CT Code C66742 有哪些具体值? | 完整 Term 表 | 高信心推测 Y/N/U/NA, 引 §4.3.7 + 05 mega_spec | 同推测, 增 §4.3.7 "Y or N extended to U or NA" 原文 | ↑ (轻微) | v2.1 |
| T8 | CV 域所有变量值范围? | "需查 examples/terminology" | 42 变量按 6-Role 分层 + CT 引用 + 边界 | 同 42 变量重组为 4-class value-range; CT 等同 | ↑ (轻微, 组织维度) | v2.1 |

## T9-T20 新增 (覆盖 v2 五批)

| # | 批 | 题目 | 期望 | v1 答案 | v2.1 答案 | 精度 | PASS? |
|---|----|-----|------|--------|----------|------|-------|
| T9  | 1 | ch01 SDTM 整体架构 + Foundational concepts? | 完整段落 | PASS with 边界, §1.1-§1.4 + ch02 §2.1-§2.8 + 原则 | **PASS**, 纠正前提 "ch01 is Introduction" + §1.1-§1.5 + byte-exact ch01 p.7-12 | ↑ (轻微) | **PASS** ✅ |
| T10 | 1 | ch02 §2.6 创建新 domain 的所有步骤? | 完整列表 | PASS, §2.6 item 1/2/3 + 11 子步骤 a-k (部分简化) + 4 Key Rules | **PASS**, 完整 11 子步骤 a-k 表格 + 4 Key Rules + **v3.4 新增 SA/SQ 变更条目** + §2.5/§2.7 约束 | ↑ | **PASS** ✅ |
| T11 | 1 | (变体 — v1: ch08 §8.3 RELREC; v2: ch03 §3.1.2.2 虚构 section) | 完整规则+示例 / 虚构检出 | PASS w/caveat, 区分 §8.2 vs §8.3 + RELTYPE 3 值 + 7 延伸 | **PASS**, 立即检出虚构 §3.1.2.2 + 完整 ch03 TOC + 10 条命名规则映射到 §2.2/§4.1.6/§4.1.7/§4.2.1/§4.2.2/§8.4.2/Appendix D | **PASS v2.2**: ch08 §8.3 全文 (§8.2 vs §8.3 对照表 + §8.3.1 TU↔TR relrec.xpt + 5-step 工作流 + 4 应用场景 + 4 提醒), 持平或略 ↑ | N/A (变体) | **PASS** ✅ (各自) |
| T12 | 1 | (变体 — v1: ch10 附录 entity; v2: ch04 §4.4 Timing 变量) | 完整清单 / 完整 §4.4 | PASS, Appendix A-E 完整 + C1 v3.4 已 removed TS 标记 + 9 行边界表 | **PASS**, §4.4.1-§4.4.10 全覆盖 + **§4.4.8 "--STDTC 禁用于 Findings" v3.4 新增** + v3.4 变更对照表 | N/A (变体) | **PASS** ✅ (各自) |
| T13 | 2 | DM 的 Example 1 完整数据表? | 表格 | (兜底模板, 回落到源路径) | (v2.1 09 未在, 同 v1) | **PASS v2.2**: 6×25 dm.xpt 完整表 + Row 4 SCREEN FAILURE ARMNRS 用法 + RACE 6 CT 值覆盖, Source 标 09 | ↑ | **PASS** ✅ |
| T14 | 2 | EX 剂量调整 Example 数据怎么写? | 表格 | (兜底, 回落源路径) | (v2.1 09 未在, 同 v1) | **PASS v2.2**: Ex4 完整 6×14 ex.xpt 表 (EXADJ "Reduced due to toxicity" / "Increased due to suboptimal efficacy") + 3 建模要点 + EC/EX Ex7 延伸, Source 标 09 | ↑ | **PASS** ✅ |
| T15 | 3 | RP 域 Example 数据? | 表格 | (兜底) | TBD (Stage v2.3) | TBD | TBD |
| T16 | 3 | FT 域 Example 数据? | 表格 | (兜底) | TBD (Stage v2.3) | TBD | TBD |
| T17 | 4 | C66742 codelist 所有 Term 值 + Definition? | 完整 Term 表 | (兜底) | TBD (Stage v2.4) | TBD | TBD |
| T18 | 4 | AERELN codelist 全部 Synonyms? | Synonyms 字段 | TBD | TBD (Stage v2.4) | TBD | TBD |
| T19 | 5 | FREQ codelist (中频) 全部 Term + Code? | 表格 | TBD | TBD (Stage v2.5) | TBD | TBD |
| T20 | 5 | PROBLEM_TYPE codelist (中频) 全部值? | 表格 | TBD | TBD (Stage v2.5) | TBD | TBD |

## 阶段汇总

### v2.1 (2026-04-18 → 2026-04-19, chapters 全展开 batch)

- **Capacity 实测**: 13% (v1 = 12%, +1pp)
- **T1-T8 分布**: 5 ↑ / 2 持平 / **1 ↓** (T3)
- **T9-T12 分布**: 4/4 PASS
- **T1-T8 整体健康度**: 7/8 无衰减, 符合 "<2 ↓ 继续" 门槛, 但触发 "1 ↓ → 询问用户" 分支
- **关键收益**: chapter byte-exact 展开让 v2 能精确引用 §4.4.8/§2.6 SA/SQ 等 v3.4 新增条目; 主动检出虚构 §3.1.2.2
- **代价**: T3 拒答 (§6.3.5.9.3 未收录时 v2.1 不再重建), 边界严谨换 T3 实用性
- **决议**: 待用户 ack 继续/调整/暂停 (详 `evidence_v2/checkpoints/ckpt_v2.1.md`)
- **后续修复路径**: batch 2 (Task D1-D4) 纳入 ch06 PP/PC examples + ch04 §4.3.6 AE Examples 全展开, 可同时修 T3+T6 缺口

### v2.2 (2026-04-19, examples 高频 28 域 batch)

- **Capacity 实测**: **20%** (v2.1 = 13%, +7pp, 精确匹配规划 20-22% 预期)
- **上传文件**: 9 v2.1 不变 + 1 新 (09_examples_data_high.md, 112,697 tokens, 28 域数据表全量), 总 10 文件 / 318,592 tokens
- **T13 DM Ex1 数据**: **PASS ↑** — 命中 09, 完整 6×25 dm.xpt 表 (含 Row 4 SCREEN FAILURE 场景 + ARMNRS 字段用法 + RACE 6 CT 全覆盖)
- **T14 EX 剂量调整**: **PASS ↑** — 命中 09, Ex4 完整 ex.xpt 表 + EXADJ 真实 free-text ("Reduced due to toxicity" / "Increased due to suboptimal efficacy") + 3 建模要点 + EC/EX Ex7 延伸对照
- **T1 AEDECOD (回归)**: 持平 (Core=Req 稳定, v2.2 增 §4.3.6 三元结构 + 跨域 DECOD 对比 + AEPTCD 配套, 非衰减)
- **T11 ch08 §8.3 RELREC (回归)**: 持平 (ch08 全文未变, v2.2 增 §8.2 vs §8.3 对照 example, 非衰减)
- **回归衰减 ↓**: **0 / 2** (门槛 ≥2 停, ≥1 询问; 本批无衰减)
- **新增 PASS**: **2 / 2**
- **关键观察**:
  - Examples 查询优先级规则 "09 > 07" 被 Instructions 正确解读, 无一 fallback 到 v1 模板
  - 112K 新文件对 05_mega_spec / 02_chapters 召回无挤出/遮蔽
  - +7pp capacity 精确匹配 (13%→20%), 验证 Option A 容量预算
- **异常**: Chrome MCP file_upload 对 sandbox/绝对路径均 `Not allowed`, 本次用户手工拖拽完成; indexing indicator 不可靠, 上传后立即提问即可命中
- **决议**: T1/T11 无 ↓ + T13+T14 = 2/2 PASS → **继续 Task E1 批 3 (examples 剩余域)**
