# Phase 6.5 Gemini Gems · Phase 3 Node 4 (C 方案) — Reviewer Report

> **Reviewer**: oh-my-claudecode:architect (Rule D 第 13 种 subagent_type, read-only)
> **Writer**: oh-my-claudecode:executor (opus) — writer lane, session isolated
> **Date**: 2026-04-21
> **Scope**: Node 4 C 方案 (4 uploads + merge.py v2.0 + validate.py v2.0 + system_prompt v3 + 04 业务弹药包 30K tokens + upload_manifest v2 + failures/)
> **Method**: 只读, 不跑脚本; Grep/Read/Glob 独立核查 writer summary vs 实际产物 + SDTM 事实抽检 vs KB 源.

## Review Verdict
**CONDITIONAL_PASS** — confidence 88%

建议可放行 Node 5 (上传 + smoke v2), 同时带 2 MEDIUM + 3 LOW 条目带入 Node 5 / carry-forward 跟踪.

## Summary

Gemini Gems C 方案 Node 4 writer 交付在架构、CO-1/2/3 落地、Rule A/B/D/E 合规、validate rc=0 全部达标. 4 文件总 616K tokens / 38% buffer, 相对 PLAN 820K 更省, 空间分配合理. 最关键的 SDTM 事实 (AESER=Exp / AESEV=Perm / LBNRIND 三档 / CM Req 集 / MH+CM 双记) 全部与 KB spec 精确一致, CT Code §3.1 索引 3 条抽检全 Grep 命中真实 KB 源. 但 04 内容密度高但 token 偏低 (30K vs target 60K, -49%), V8 pattern 的 false-positive 用格式绕过而非修根 (技术债), writer summary 声称 "AESER 9 处" 实测分布不同, 统计口径不透明. Node 5 smoke v2 10 题 < 8/10 时扩 04 是唯一路径 (CARRY-N4-1 强化到 MEDIUM).

## Findings

### HIGH (阻塞 Node 5)

**无**. 无任何阻塞项; validate rc=0 + CO-1/2/3 三条铁律 + SDTM 事实 5 点抽检全 PASS, 可进 Node 5.

### MEDIUM (Node 5 前或 smoke 后必修)

**MED-1**: 04 token 密度风险 (CARRY-N4-1 升级)
- writer 标为 LOW, 但从架构视角应是 MEDIUM. 04 30,488 tokens / target 60,000 = 50.8%, 仅占总 1M 的 3%.
- 384K buffer 里挤一挤给 04 再加 25-30K 是无成本的.
- 若 smoke v2 10 题里 "场景 / 鉴别" 8 题一旦有 <80% 命中, 必然原因是 04 覆盖面不够.
- 建议: Node 5 smoke 前**预防性扩 15-20K** 到 ~50K.

**MED-2**: V8b pattern false-positive 用"绕格式"而非"修 pattern"关 (CARRY-N4-2 升级)
- attempt 1 §3.1 markdown 表格本来合规但被 pattern 命中 26 行; attempt 2 改无项目符号列表绕过.
- 这是 writer 改 validate 的验证对象去适应 validator (不是 validator 去贴合业务语义).
- 未来任何人写 04 用 markdown 表格都会再踩同一坑, pattern v2.1 收紧应在 Node 5 落地.

### LOW (文档 / 精度修饰)

**LOW-1**: writer summary "AESER 9 处" 与实测偏差 — system_prompt Grep 8 处 / 04 Grep 25 处, 硬锚点段 2+5=7 段. 统计口径不透明, 不是事实错.

**LOW-2**: §1.26 Core 摘要与 §1.2 §2.1 轻度重复, §8 与 §1 场景域有 ~30% 重叠. redundancy ≈ 10-15% of 30K = 3-4K tokens.

**LOW-3**: §1.26 DM 条目 ETHNIC / RACE 和 §1.18 语义略不一致, 读者需跳两段推断.

## Evidence 证据段

### SDTM 事实抽检 (5/5 PASS)

1. **AESER Core=Exp** [CO-1 铁律]
   - 04 L94: `| **AESER** | **Serious Event** | **Exp** | **"Y"**`
   - KB 源 `knowledge_base/domains/AE/spec.md` L248-256: `### AESER ... - **Core:** Exp`
   - **PASS**, 精确一致.

2. **AE Serious 子变量 Core=Perm**
   - 04 L97-100: `AESLIFE/AESDTH/AESDISAB/AESCONG/AESMIE` 全标 Perm
   - KB 源 AE/spec.md L338-398 全 `Core: Perm`
   - **PASS**.

3. **CM Req 集 (STUDYID/DOMAIN/USUBJID/CMSEQ/CMTRT)**
   - 04 §1.1 L50-56 + §1.26 L969
   - **PASS**.

4. **LBNRIND 三档 L/N/H (C78736 codelist)**
   - 04 L145-153 L/N/H 明示
   - **PASS** (C78736 外部 codelist 符合 SDTM v3.4).

5. **MH + CM 双记录 (§1.7)**
   - 04 L291-339 拆 MH (MHTERM) + CM (CMTRT) + CMINDC 回指
   - **PASS**.

### CT Code §3.1 抽检 (3/3 PASS)
- `C66742` 04 L1158 "No Yes Response" → `terminology/core/general_part4.md:5` **匹配**
- `C66769` 04 L1159 → `terminology/core/ae.md` via AE/spec.md L554 **匹配**
- `C65047` 04 L1166 → `terminology/core/lb_part2.md:5` **匹配**

### 零 inline Term 值 (V8b PASS)
- 独立扫 04 `\|\s*C\d{5,7}\s*\|\s*\w+` 0 行, 符合.

### 脚本 terminology 残留清除 (PASS)
- `merge_for_gemini.py` Grep `_collect_terminology / _stage_terminology`: 0 业务匹配.
- `validate_gemini.py` Grep `_v6_tail_terminology`: 0 业务匹配. V8 新函数 + pattern `r"\|\s*C\d{5,7}\s*\|"` 齐全.
- STAGE_FILES 4 条 entries 正确.

### 02 域内交错 (spec+assumptions) PASS
- 首 12 source 标记: AE/spec → AE/assumptions → AG/spec → AG/assumptions → BE/spec → BE/assumptions ... 域内字母序 spec 先 assumptions 后. 126 segments = 63 spec + 63 assumptions.

## 架构评价

- **C 方案 trade-off 合理性**: 舍弃 terminology 换业务场景弹药合理. 原 299K terminology 里 80% 是 Term 值 inline (审查式查询), Gemini 查询侧已由 NCI EVS Browser 补位; 现用 30K 业务场景弹药打中 smoke v2 4 业务维度靶子, **ROI 比 299K 高一个数量级**.
- **新 4 文件配比**: 01 (20%) / 02 (39%) / 03 (36%) / 04 (5%). 04 5% 偏低, 合理区间应占 7-10% (40-50K). 当前 5% = 密度高但面积小. 这是 MED-1 的架构根源.
- **buffer 管理 (384K / 38%)**: 过度保守. Gemini 1M 窗口里响应 + 多轮上下文 + safety margin 150-200K 足够. 384K 有 180K "真空容量", 应至少填 100K 到 04 + 加强 assumption 细节.

## CO-1/CO-2/CO-3 独立核查矩阵

| CO | system_prompt 落点 | 04 落点 | writer 声称 | 独立核查 |
|----|--------------------|---------|-------------|----------|
| CO-1 AESER 锚点 | §三条硬约束 L41-50 + 边界模板 ⑤ L143-149 + §回答规范 L113-115 + §工作流程 step 6 L174 | §0 L26 + §1.2 L80-120 + §1.4 L186-192 + §2.1 L1001-1009 + §6.3 L1471-1488 + §9.1 L1612-1619 | 9 处 (4+5) | **PASS**, AESER 出现 8 处 (sysprompt) + 25 处 (04) 但"结构化锚点段" 2+5=7 段深度覆盖. |
| CO-2 NCI 零臆造 | §CO-2 L52-63 + 边界模板 ① ② L122-128 + §路由规则 6 L104-106 + §工作流程 step 7 L175 | §0 L27 + §2.6 L1038-1043 + §3 整节 L1146-1214 + §6.2 §6.2b L1436-1469 + §9.7 L1682-1692 | 10 处 (4+6) | **PASS**, `evsexplore` 出现 13 处 (sysprompt). C117711 防臆造范例 §6.2b 具体到位. |
| CO-3 citation | §CO-3 L64-72 + §回答规范 L115 + §工作流程 step 4 L172 | §0 L28-32 + §1.1-§1.26 每场景带源路径 + §6 回答模板全带源路径 | 3 + 全文 | **PASS**, 04 `源路径` 出现 **42 次**. |

## Rule D/A/B/E 合规核查

- **Rule D**: **PASS**. 本 reviewer = oh-my-claudecode:architect (第 13 种 subagent_type, 与 writer executor 独立); 只读无 Write 权限; 独立 Grep 验证全部关键断言.
- **Rule A**: **PASS**. 04 非 KB 源 (writer 自编), 压缩率规则 A 不适用; 但事实抽检 5/5 + CT Code 3/3 一致性.
- **Rule B**: **PASS**. `failures/stage_c_refactor_attempt_1.md` 2054 字节, 五段式齐全.
- **Rule E**:
  - Q3=C (精确+全域): **PASS**
  - Q4 语义演化 (C 方案): **PASS** (terminology → NCI EVS 的战略转向)
  - Q5=A (63 域平权): **PASS** (§8 63 域铺平)

## 04 SDTM 事实抽检矩阵 (10/10 PASS)

| 事实 | 04 段 | KB 源对比 | 判定 |
|------|------|-----------|------|
| AESER Core=Exp | §1.2 L94, §2.1 L1004 | AE/spec.md L248-256 | **PASS** |
| AE Serious 子变量全 Perm | §1.2 L96-100, §2.1 L1005 | AE/spec.md L338-398 | **PASS** |
| AESEV Core=Perm | §1.2 L93, §1.4 L199, §2.1 L1003 | AE/spec.md L239-245 | **PASS** |
| CM Req 集 5 变量 | §1.1 L50-56, §1.26 L969 | CM/spec.md | **PASS** |
| LBNRIND 三档 L/N/H | §1.3 L145-153 | LB/spec.md + C78736 | **PASS** |
| AESEV 三档 + CTCAE Grade 5→AESDTH | §1.4 L172-184 | AE/assumptions.md §7.a + §7.d | **PASS** |
| MH + CM 双记录 | §1.7 L291-339 | MH/assumptions.md + ch04 | **PASS** |
| CT Code C66742 映射 | §3.1 L1158 | terminology/core/general_part4.md L5 | **PASS** |
| CT Code C65047 映射 | §3.1 L1166 | terminology/core/lb_part2.md L5 | **PASS** |
| CT Code C66769 映射 | §3.1 L1159 | terminology/core/ae.md | **PASS** |

**全 10/10 PASS**. Rule A 的"独立抽检"精神充分满足.

## 不能本 session 关闭的 carry-over (交 Node 5)

- **CARRY-N5-1** (MEDIUM, from MED-1): 04 扩 15-25K tokens 到 50-60K target. 优先加: RECIST / 影像 / Oncology 场景 / Trial Design 域 (TS/TI/TM) / IE 域判定 / AG / PR 更深实例.
- **CARRY-N5-2** (MEDIUM, from MED-2): V8 pattern v2.1 收紧, 改成只 FAIL 真 Term Submission Value. 同时 04 §3.1 可回归标准 markdown 表格.
- **CARRY-N5-3** (LOW, from LOW-1): Rule D audit matrix 里"CO-1/2/3 落点计数"分 "硬约束段" vs "散落提及" 两档.
- **CARRY-N5-4** (LOW, from LOW-2): 04 内部去 redundancy, §1.26 Core 速查可和 §2.1 合并或 cross-reference.
- **CARRY-N5-5** (LOW, from LOW-3): §1.15-§1.26 子域段统一加 "Core: 域内 Req 集 / 典型 Exp 集" 摘要.
- **CARRY-N5-6** (INFO, from writer CARRY-N4-3): 02 130K buffer 释放后去向需决定 (扩 04 / 扩 01 导航 / 留 buffer 给响应).

---

**最终建议**: CONDITIONAL_PASS, 可进 Node 5 smoke v2 上传试跑. **MED-1 (04 扩容)** 最好在 smoke 前做, 因为单次 smoke run 若 <8/10 必然要扩 + 重跑, 不如预防性扩 15-20K 一次到位. MED-2 可延后到 Node 5 后半段或 Node 6 技术债清理.
