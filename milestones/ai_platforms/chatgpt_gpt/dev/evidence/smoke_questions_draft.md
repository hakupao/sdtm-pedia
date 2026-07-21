# ChatGPT GPTs — Phase 3 Node 3 Smoke Questions Draft

> 目标: 上传批 1 4 文件 + Instructions 后, 由用户在 GPT Preview 面板跑 5 道 smoke 题
> 总题数: 5 (Phase 3b 快速验证 vs PLAN §7 完整 13 题留到 Phase 3 Node 5)
> PASS 判据: 5 题中 **≥ 4 PASS** 允许继续 Node 4; FAIL ≥ 2 走 P10 停机 (§6 失败模式 6)
> 派生: PLAN §7.3 smoke 子集 (T01/T02/T03) + PLAN §7.2 T13 (Q1=C 公开受众提前验证) + Q8 Indexing indicator 实测题 (Phase 1 PARTIAL carry-over)

---

## 题目

### S1 — 路由 (PLAN §7.3 T01)

- **问**: "AE 域的 AESER 变量定义是什么?"
- **命中**: `04_domain_specs_all.md` → AE 段 → AESER 行
- **PASS 判据**:
  - 引用变量名 `AE.AESER` 或 `AESER`
  - 给 Role (Record Qualifier)
  - 给 Core (Perm 或等价描述)
  - 若给 CT, 须是 `C66742` / NY (No Yes Response)
  - **零臆造** (不编允许值, 必须来自源)
  - 源溯源: 答案中出现 `<!-- source: knowledge_base/domains/AE/spec.md -->` 或类似文字溯源

### S2 — 定义查询 (PLAN §7.3 T02)

- **问**: "RELREC 是什么?"
- **命中**: `02_chapters_all.md` (ch08 Representing Relationships) + `04_domain_specs_all.md` 相关域 cross-reference
- **PASS 判据**:
  - 识别为**关联关系数据集** (Related Records, 链接 records / datasets)
  - 给出使用场景 (跨域关联, e.g. AE 关联到 EX / CM 的因果推断)
  - **不臆造具体字段** (RELID / RDOMAIN / IDVAR / IDVARVAL / RELTYPE etc.); 若给字段**必须**来源 ch08 明写

### S3 — 边界诚实 (PLAN §7.3 T03, **关键题**)

- **问**: "AERELN codelist 所有 Synonyms 是什么?"
- **命中**: 批 1 **无 terminology** → 应走边界模板 ② → 应答 "批 1 未上传 terminology (见批 2 07_terminology_core) 或源 `knowledge_base/terminology/core/*.md` 或 [NCI EVS Browser](https://evsexplore.semantics.cancer.gov/)"
- **PASS 判据**:
  - **零臆造 Synonyms** (不列 "Related to" / "Caused by" / "Concomitant Illness" 等具体 term, 即使它们可能真实存在)
  - 明确声明 "批 1 未收录 terminology Term 值"
  - 给外部入口 (NCI EVS Browser 或 源路径)
  - **任何臆造 synonyms 即 FAIL** (公开 GPT 场景零容忍, Rule E Q1=C)

### S4 — Q1=C 公开受众语气 (PLAN §7.2 T13)

- **问**: "我是病人家属, 能简单解释 SDTM 是什么吗?"
- **命中**: `01_navigation.md` (INDEX/ROUTING) + `02_chapters_all.md` (ch01 §1.1 Purpose + ch02 概念段)
- **PASS 判据**:
  - **新手友好**: 首段必有一句通俗类比 (如 "临床试验数据的标准表格格式, 像 Excel 模板让各医院数据对齐") 或等价表达
  - **无生僻术语堆砌**: 不在第一段直接抛 "General Observation Class" / "Domain Model" 等术语
  - **类比恰当**: Excel / 表格 / 标准化病历等生活化类比 (不用股票/编程这类跨域类比)
  - **不假设行业背景**: 不说 "如您熟悉的 CDASH/ADaM..."
  - **若用术语立刻解释**: 如用 "domain" 则一句话说明 "数据主题分类, 如 AE=不良事件"
  - **专家路径仍可见**: 末尾可给 "如需技术细节见 §2.1" 指向

### S5 — Q8 Indexing Indicator 实测 (Phase 1 PARTIAL carry-over)

- **问**: "根据 04_domain_specs_all.md, 请列出 AE 域 Core=Req 的变量名 (至少 3 个)"
- **命中**: `04_domain_specs_all.md` → AE 段前部 Identifier + Topic 变量
- **PASS 判据**:
  - 命中 3+ Req 变量. 预期候选集: `STUDYID` / `DOMAIN` / `USUBJID` / `AESEQ` / `AETERM` / `AEDECOD` 等
  - 变量名拼写正确 (无 `AE.` 前缀或有, 均 OK, 但不能写成 `AETerm` / `AE_TERM` 等错拼)
  - 答案须注明 Core 字段来自 `04_domain_specs_all.md` (验证文件确实可检索)
- **Q8 失败信号**:
  - UI 已显示 "Ready" 但答 "无法找到该文件 / 无法访问 knowledge" → **Indexing indicator 不可靠**
  - 答错 (e.g. 给出非 Req 的变量如 AESPID) → 可能是 chunk 覆盖不足, 非 Q8 问题
  - 上述两种情况归档入 `dev/evidence/phase3_q8_indexing_reality.md` (待建)

---

## 用户执行步骤

1. 所有 4 文件 Processing → Ready 后 (UI "Ready" 标志)
2. 在 GPT Preview 面板按 **S1 → S5 顺序**逐题提问
3. 每题答案截图或复制 markdown 到 `dev/evidence/smoke_batch1_results.md` (待建)
4. 5 题答完后计算 PASS/FAIL 比
5. **若 ≥ 4 PASS**: 本 session 或新 session 回报, 主 session 派 Rule D reviewer 独立复核 + commit C3b + 进 Node 4
6. **若 < 4 PASS**: 触发 P10, **不推进** Node 4, 归档入 `dev/evidence/failures/stage_3_node3_attempt_<M>.md` 走规则 B, 主 session 按 FAIL 项决策 (重上传 / 改 Instructions / 重合并) 再跑 attempt_2

---

## 题目设计说明

- **S1-S3** 直接采自 PLAN §7.3 smoke 子集 (T01/T02/T03), 保持可复现 + Phase 3 Node 5 全量 A/B 时可对比
- **S4** 把 PLAN §7.2 T13 (完整 A/B 13 题之一) **提前**到 smoke, **提前验证 Rule E Q1=C 公开语气** (若在 smoke 即失败, 说明 Instructions 新手段失效, 不必等 Phase 3 Node 5 全量 A/B; 提前回路省一轮)
- **S5** 是 **Phase 1 Q8 PARTIAL carry-over 兑现题**, **必考** — ChatGPT 的 Indexing indicator 可靠性是 Phase 1 未答死的关键问题, Node 3b 必须用实测回答
- **PLAN §7 完整 13 题**留到 Phase 3 **Node 5** 全量 A/B, 本 smoke 不重复 (Node 4 批 2 上传后, Node 5 才跑 T04-T14/T15)

---

## 潜在陷阱 (用户执行时注意)

- **S2 RELREC 臆造陷阱**: ch08 的 RELREC 字段是常识 (RDOMAIN/IDVAR/IDVARVAL/RELTYPE/RELID), 模型**可能从预训练知识**直接答出; PASS 要求必须源溯源到 ch08. 若答案列了字段但无 `<!-- source: ... ch08 -->` 溯源, 暗示走了预训练知识, 降级为 PARTIAL (记录入 smoke 结果备注)
- **S3 Synonyms 引诱**: AERELN 的 Synonyms 在 NCI EVS 中实际存在 (Cxxxxx → "Related to" 等), 模型可能被问题诱导编造; PASS 要求**拒绝作答具体 Synonyms**, 只给路径. 这是公开 GPT Store 发布前的底线题.
- **S4 新手友好判定**: 允许模型给**多段答案** (先通俗 → 再专业), 只要**第一段**必须通俗即 PASS; 第二段可以有术语. 若全答案纯术语无类比 → FAIL.
- **S5 文件引用格式**: 模型可能答 "见知识库 01" 或 "见 navigation" 而不明确到 `04_domain_specs_all.md`; 只要能确认检索了 04 文件即 PASS (可从答出的变量名精确度反推).

---

*来源: PLAN v1.2 §7.2 (T01/T02/T03/T13) + §7.3 smoke 子集 + §4 Task E1 (Q8 Indexing 实测) + Phase 1 research.md MEDIUM/PARTIAL carry-over*
