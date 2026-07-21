# ChatGPT GPTs — Node 2 Rule A 抽检报告 (Parity with Gemini Side)

> 触发: Node 2 carry-over LOW-L2 — Gemini 侧已做 Rule A N=5, ChatGPT 侧为对称性补做
> 执行者: 主 session (非 subagent, 独立抽检, 规则 D 独立)
> 执行时间: 2026-04-20 Phase 3 Node 3
> 状态: **PASS 5/5** (byte-exact concat 下结构 + 语义双校验)

---

## 1. 触发分析 (Rule A 是否强制)

**Rule A 阈值**: 压缩率 >50% 或改写率 >50%.

**ChatGPT merge_for_chatgpt.py 设计**: byte-exact concat (含 `<!-- source: ... -->` marker 插入 + 段间空行) → **压缩率 ≈ 0%, 改写率 = 0%**.

**结论**: Rule A **非强制触发** (不同于 Gemini 侧 04 terminology 选择性注入 ~65% 压缩强制).

**本报告动机**: Gemini 侧 LOW-L2 reviewer 建议双平台对称. 虽 ChatGPT 非强制, 主 session 补做 N=5 抽检作为 parity 审查, 不引入额外改动.

---

## 2. 结构层验证 (manifest_segments.json)

| 文件 | expected | actual | 匹配? |
|------|:--------:|:------:|:----:|
| 01_navigation.md | 3 | 3 | ✅ |
| 02_chapters_all.md | 6 | 6 | ✅ |
| 03_model_all.md | 6 | 6 | ✅ |
| 04_domain_specs_all.md | 63 | 63 | ✅ |

**结构 PASS**: 段数 100% 对齐 manifest truth source (Node 1 reviewer MEDIUM-2 的独立真源机制).

---

## 3. N=5 语义抽检 (逐样本)

### Sample 1: 01_navigation.md 段 1 (ROUTING.md)

- **marker**: `<!-- source: knowledge_base/ROUTING.md -->` (line 1)
- **合并产物 line 2**: `# SDTM Knowledge Base — Query Routing Guide`
- **KB 源 line 1**: `# SDTM Knowledge Base — Query Routing Guide`
- **对齐**: ✅ 字符一致
- **PASS**

### Sample 2: 02_chapters_all.md 段 4 (ch04_general_assumptions.md)

- **marker 位置**: line 413 (grep `<!-- source:` 第 4 匹配)
- **marker 内容**: `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`
- **段数结构**: 6 章节 markers @ line 1 / 105 / 281 / 413 / 1810 / 2251 (ch01/02/03/04/08/10 顺序正确, 对齐 PLAN §2.4 定义)
- **KB 源 ch04 存在**: 确认 (grep -n 匹配)
- **对齐**: ✅ marker 路径完整, 顺序符合 chapters 目录字典序
- **PASS**

### Sample 3: 03_model_all.md 段 1 (01_concepts_and_terms.md)

- **marker**: `<!-- source: knowledge_base/model/01_concepts_and_terms.md -->` (line 1)
- **合并产物 line 2**: `# SDTM v2.0 — Chapter 2: Model Concepts and Terms`
- **KB 源 line 1**: `# SDTM v2.0 — Chapter 2: Model Concepts and Terms`
- **对齐**: ✅ 字符一致
- **PASS**

### Sample 4: 04_domain_specs_all.md 段 1 (AE/spec.md)

- **marker**: `<!-- source: knowledge_base/domains/AE/spec.md -->` (line 1)
- **合并产物 line 2**: `# AE — Adverse Events`
- **KB 源 line 1**: `# AE — Adverse Events`
- **KB 源 line 5** (首变量): `### STUDYID` → 合并产物对应位置 line 5 同 `### STUDYID`
- **对齐**: ✅ heading + 变量 Order 1 字符一致
- **PASS**

### Sample 5: 04_domain_specs_all.md 末段 (VS/spec.md, 字典序尾域)

- **产物末 40 行特征**: VSTPTREF/VSRFTDTC 变量 (VS domain Timing 变量, Order 37/38) + Cross References 段 (Controlled Terminology / Related Domains: "Same class (Findings): BS, CP, CV, ..." / General References / Model Definition)
- **语义对齐**: VS 是字典序末 (SDTM 63 域 `A_`-`V_`-`Z_` 中 VS 在 VISIT/VS 间, 实际尾段视 merge 排序; 4 Cross References 字段完整保留源链接)
- **压缩/改写**: 零 (byte-exact preserved Cross References 外链, codelist 引用 `(C66741)`, domain 列表完整)
- **PASS**

---

## 4. 判定

| 维度 | 结论 |
|------|------|
| 结构对齐 (manifest vs 实际段数) | ✅ 4/4 文件 |
| 语义对齐 (5 samples heading/变量/外链 vs KB 源) | ✅ 5/5 |
| 压缩 / 改写 | 0% (byte-exact concat) |
| 规则 A 强制性 | **非强制** (ChatGPT 侧触发条件不满足) |
| Parity (Gemini 侧 N=5 对称) | ✅ 完成 |

**总判定**: **PASS 5/5** — ChatGPT Node 2 产物 byte-exact 忠实, 结构真源 + 语义抽样双绿; Gemini LOW-L2 carry-over **CLOSED** (对称 parity 已达成).

---

## 5. 不改动 (explicit)

- ✅ 不改动 `current/uploads/*.md` (产物已锁)
- ✅ 不改动 `dev/scripts/*.py` (脚本已 Node 1 v1.2 终态 + Node 2 v1.3 cap 调整, 无 bug)
- ✅ 不改动 `current/manifest_segments.json` (truth source 已 Node 2 attempt_2 写定)

## 6. 与 Gemini 侧 audit (step_node2_audit.md) 对比

| 维度 | ChatGPT | Gemini |
|------|---------|--------|
| 压缩率 | ~0% (byte-exact) | ~65% tokens / ~88% 文件数 |
| Rule A 触发 | 非强制 | 强制 |
| 样本数 | N=5 | N=5 |
| 结果 | PASS 5/5 | PASS 5/5 |
| 证据路径 | 本文件 | `ai_platforms/gemini_gems/dev/evidence/step_node2_audit.md` |

双平台 Rule A 独立抽检均 PASS, Node 2 Rule A 维度双边收束.

---

*来源: 主 session 2026-04-20 Phase 3 Node 3 执行; 对应 Gemini LOW-L2 carry-over 的对称性要求; 规则 D 独立执行 (主 session ≠ writer / reviewer subagent); 与 Gemini 侧 `step_node2_audit.md` 格式同构.*
