# Gemini Gems — Phase 3 Node 3 Smoke Questions Draft

> 目标: 单批上传 4 文件 (884,918 tokens / 88.49% 窗口占用) + Instructions 后, 由用户在 Gem Preview 跑 5 道 smoke
> 总题数: **5** (vs PLAN §7 完整 10 题留到 Phase 3 Node 5)
> PASS 判据: **≥ 4 PASS 允许继续 Node 4+**; **FAIL ≥ 2 走 P10 停机**
> **P12 末尾召回 hard checkpoint 题 2 道嵌入 smoke** (S3 + S4 对应 T-tail-1/T-tail-2, 是全局 gate, smoke 提前验)
> Writer: oh-my-claudecode:executor (opus), 2026-04-20

---

## 题目选型过程记录 (writer 读 04 确认后)

Writer 在落盘本 draft 前读 `current/uploads/04_terminology_core.md` (6343 行) 的 header + 尾 20 行 + source marker map, 确认如下实际分布:

**坐标系统口径说明** (Phase 3 Node 3a reviewer M1 R1 升级):

本 draft 的 **offset_pct 列使用 line-based 百分比** (line / 总行数 6343), 便于 writer 读文件时快速定位. 与 `_progress.json` 中 V6 tail_start **char-based** 坐标 (777,919 chars / 总 1,111,314 chars = 70%) **不是同一坐标系**. 换算参考:

| 坐标系 | S2 (C65047 头部) | S4 (C67154 中段) | S3 (C100129 末尾) | tail_start |
|-------|---:|---:|---:|---:|
| **line-based** (本 draft) | 0.2% (line 15) | 40.4% (line 2564) | 95.4% (line 6050) | 70.0% (line 4440) |
| **char-based** (_progress.json) | ~0.04% | ~34.0% | ~87.7% | 70.0% (char 777,919) |
| **token-based** (Instructions §知识库组成) | ~0% | ~35-45% (02 中段 block) | ~100% (尾) | ~70% (token ~620K) |

**核心不变语义**: S3 (95.4% line / 87.7% char) 落在 V6 后 30% tail 内 (tail_start 70%); S4 (40.4% line / 34.0% char) 落在 V6 前 70% middle 段 — 两题的 **recency vs middle** 对比语义成立.

---

**04 实际包含的 codelist (13 个, 按文件 offset 升序)**:

| line | codelist | CT Code | 所属 source 段 | offset_pct |
|----:|---------|---------|----------------|---:|
| 15 | Laboratory Test Code | C65047 | `knowledge_base/terminology/core/lb_part2.md` | 0.2% |
| 2564 | Laboratory Test Name | C67154 | `knowledge_base/terminology/core/lb_part3.md` | 40.4% |
| 5113 | Category of Clinical Classification | C118971 | `knowledge_base/terminology/core/oncology_part1.md` | 80.6% |
| 5193 | Category of Oncology Response Assessment | C124298 | `oncology_part1.md` | 81.9% |
| 5285 | Oncology Response Assessment Result | C96785 | `oncology_part1.md` | 83.3% |
| 5376 | Oncology Response Assessment Test Code | C96782 | `oncology_part1.md` | 84.8% |
| 5424 | BRIDG Activity Mood | C125923 | `interventions.md` | 85.5% |
| 5433 | Frequency | C71113 | `interventions.md` | 85.7% |
| 5541 | Pharmaceutical Dosage Form | C66726 | `interventions.md` | 87.4% |
| 5732 | Position | C71148 | `interventions.md` | 90.4% |
| 5756 | Procedure | C101858 | `interventions.md` | 90.7% |
| 5902 | Route of Administration Response | C66729 | `interventions.md` | 93.1% |
| 6050 | **Category of Questionnaire** | **C100129** | `knowledge_base/terminology/core/qs_part1.md` | **95.4%** (最末 codelist) |

**04 文件统计**: 总行数 6343, tail_start (V6 后 30% 门槛) = line 4440 / character offset 777,919 / token offset ~620K. V6 tail 3 markers: oncology_part1 (char 795,262), interventions (char 884,851), qs_part1 (char 974,723) 全落尾段内。

**关键边界信息**:
- `C66742 (No Yes Response)` **不在** 04 (grep 0 匹配) → PLAN §7.1 T2 原题需改
- `AERELN` **不在** 04 (grep 0 匹配) → PLAN §7.4 T9 原题仍成立 (零臆造 gate)

**Smoke 选题映射**:
- **S2 (头部精确查询)**: 选 **首 codelist C65047 Laboratory Test Code** (line 15, offset 0.2%) — 替换 PLAN §7.1 T2 中不存在的 C66742
- **S3 (T-tail-1, 末尾召回)**: 选 **最末 codelist C100129 Category of Questionnaire** (line 6050, offset 95.4%) — 尾部 ≤10% 区间, 属最末 source 段 `qs_part1.md`
- **S4 (T-tail-2, Lost-in-Middle 验证)**: 选 **中段 codelist C67154 Laboratory Test Name** (line 2564, offset 40.4%) — 落 40-60% 危险区

---

## 题目

### S1 — 精确查询 (PLAN §7.1 T1, 原题保留)

- **题面**: `AE 域 AESER 变量的 Controlled Terms (允许值) 是什么?`
- **命中**: `02_domain_specs.md` (AE 段, 文件内约 offset 18%)
- **预期答**: Y / N 二值 (基于 AE spec.md 中 AESER 的 `Controlled Terms: Y`, 实际为 No Yes Response codelist Y/N 子集)
- **PASS**:
  - 答 Y / N 二值
  - 引用 `<!-- source: --> knowledge_base/domains/AE/spec.md` 源路径
  - **零臆造** (不编出 Y/N/U/NA 四值, AE.AESER 实际是 Y/N)

---

### S2 — codelist 头部 Term (PLAN §7.1 T2 改编, 因 C66742 不在本 Gem)

- **题面**: `04_terminology_core.md 最前面的 codelist (Laboratory Test Code, C65047) 头 5 条 Term (Code + Submission Value + Synonym) 是什么?`
- **命中**: `04_terminology_core.md` line 10-30, offset ~0.2%, source `knowledge_base/terminology/core/lb_part2.md`
- **预期答** (line 21-25 前 5 条):
  1. `C100429 | A1AGLP | Alpha-1 Acid Glycoprotein`
  2. `C181404 | A1ANTRPF | Alpha-1 Antitrypsin, Functional`
  3. `C80167 | A1ANTRYP | Alpha-1 Antitrypsin; Serum Trypsin Inhibitor`
  4. `C186022 | A1MCGEXR | Alpha-1 Microglobulin Excretion Rate`
  5. `C100462 | A1MCREAT | Alpha-1 Microglobulin/Creatinine`
- **PASS**:
  - 5 条 Term 准确 (Code + Submission Value, Synonyms 可简化但不臆造)
  - 引用 `knowledge_base/terminology/core/lb_part2.md`
  - **无臆造** (不编出不存在的 Term)

---

### S3 — P12 末尾召回 T-tail-1 (hard checkpoint, smoke 提前验)

- **题面**: `04_terminology_core.md 最后一个 codelist (Category of Questionnaire, C100129) 最前面的 5 条 Term (Code + Submission Value + Synonym 列) 是什么?`
- **命中**: `04_terminology_core.md` line 6050-6068, offset 95.4-95.6%, source `knowledge_base/terminology/core/qs_part1.md` (第 5 段 = 最末 source)
- **预期答** (line 6056-6060 前 5 条):
  1. `C187516 | ABC | ABC01`
  2. `C122370 | ACQ | ACQ01`
  3. `C123658 | ACT | ACT01`
  4. `C100762 | ADAS-COG | ADC`
  5. `C106888 | ADCS-ADL MCI | ADL03`
- **PASS**:
  - 5 条 Term 准确 (Code + Submission Value)
  - 引用 `knowledge_base/terminology/core/qs_part1.md`
  - **无 "未收录" fallback** (实际 inline 了, 若 FAIL 即 P12 触发)
  - **无臆造**
- **FAIL 响应**: 若 FAIL → P12 R1 触发, 考虑 Node 4+ 移动高频 codelist 到 02 中段或拆 04 (§8 R2)

---

### S4 — P12 末尾召回 T-tail-2 / Lost-in-Middle 验证 (hard checkpoint)

- **题面**: `04_terminology_core.md 中段的 Laboratory Test Name codelist (C67154) 最前面的 3 条 Term (Code + Submission Value + Synonym 列) 是什么?`
- **命中**: `04_terminology_core.md` line 2564-2575, offset 40.4-40.5%, source `knowledge_base/terminology/core/lb_part3.md` (第 2 段, 落 Lost-in-Middle 危险区)
- **预期答** (line 2570-2572 前 3 条):
  1. `C179752 | 1,25-Dihydroxyvitamin D2 | 1,25-Dihydroxycalciferol; 1,25-Dihydroxyergocalciferol; 1,25-Dihydroxyvitamin D2; Ercalcitriol`
  2. `C179754 | 1,25-Dihydroxyvitamin D3 | 1,25-Dihydroxycholecalciferol; 1,25-Dihydroxyvitamin D; 1,25-Dihydroxyvitamin D3; Calcitriol`
  3. `C179753 | 1,25-DihydroxyvitD2+1,25-DihydroxyvitD3 | ...`
- **PASS**:
  - 3 条 Term 准确 (Code + Submission Value)
  - 引用 `knowledge_base/terminology/core/lb_part3.md`
  - **无臆造**
- **对比判定**:
  - 若 **S3 PASS + S4 PASS** → 末尾和中段召回都好, P12 全绿
  - 若 **S3 PASS + S4 FAIL** → 典型 Lost-in-Middle, 记录但不阻塞 Node 4 (可通过 query anchor 缓解, PLAN §8 R1)
  - 若 **S3 FAIL** → 末尾 recency bias 失效, Gemini 1M 窗口末尾召回假设破, **严重**, 停机 Node 4

---

### S5 — 边界诚实 (PLAN §7.4 T9, 原题保留; 零臆造硬门槛)

- **题面**: `AERELN codelist 的所有 Synonyms 是什么?`
- **命中**: **04 不含 AERELN codelist** (grep 0 匹配); 04 仅 inline 5 段 (lb_part2/lb_part3/oncology_part1/interventions/qs_part1), 不含 AE 相关 codelist
- **预期答** (合规响应):
  > "`AERELN` codelist 未收录于本 Gem 的 `04_terminology_core.md`. 本 Gem 04 仅 inline 5 段高频 codelist: `lb_part2` / `lb_part3` / `oncology_part1` / `interventions` / `qs_part1`. 完整 Term + Synonyms 请查源 `knowledge_base/terminology/core/*.md` (若 AERELN 存在于源) 或 NCI EVS Browser: https://evsexplore.semantics.cancer.gov/evsexplore/"
- **PASS**:
  - 声明未收录
  - 给外部入口 (NCI EVS 或源路径)
  - **零臆造 Synonym** (这是硬门槛, 1 条假 Synonym = FAIL)

---

## 用户执行步骤

1. 所有 4 文件上传 + Save Gem 完成后 (无 indexing 等待, 秒级就绪)
2. 在 Gem Preview 按 S1 → S2 → S3 → S4 → S5 顺序逐题
3. 每题答案逐字记录到 `dev/test_results.md` smoke 段 (问/答/PASS-FAIL/引用路径/臆造?)
4. 5 题答完, 计 PASS 比 (目标 ≥ 4/5)
5. **S3 + S4 独立 gate (P12 hard checkpoint)**: 即使其他 3 题全 PASS, 若 **S3 FAIL** 或 **S4 FAIL** 任一, 均触发 PLAN §1.3 P12 FAIL 响应, **不推进 Node 4**, 回传 session 决策 (§1.3 P12 FAIL 响应矩阵: 1 题 FAIL 记 evidence + 归因 / 2 题 FAIL 停机拆 04)
6. 回报结果到 session, 主 session 派 Rule D reviewer (不同 subagent_type) + commit C3b

---

## 题目设计说明

- **S1**: PLAN §7.1 T1 原题 — 精确查询基准, 低风险确认 02 spec 注入有效
- **S2**: PLAN §7.1 T2 原题改编 — C66742 不在本 Gem 04, 改用实际 inline 的 **首 codelist C65047 Laboratory Test Code** (同样 "codelist 头部 Term" 语义), 选题经 writer 实读 04 header 确认 (见本 draft 顶部选型过程)
- **S3 / S4**: PLAN §7.3 T-tail-1 / T-tail-2 前置到 smoke — 本是 Node 5 全量 A/B gate, 但 smoke 就能暴露末尾召回问题, 不等到 Node 5
- **S5**: PLAN §7.4 T9 原题保留 — AERELN 未 inline 于本 Gem (grep 已证实), 边界诚实 + 零臆造硬门槛
- **未含 T10 超范围题** (smoke 节制, 可选 Node 5 补)
- **未含全域对比类 (T5-T8)** — 多针任务费时 (PLAN §8 R4), 留到 Node 5 Mom full A/B 做

---

## Writer 选题过程记录 (本 draft 写作时)

Writer 在落盘前读 `current/uploads/04_terminology_core.md` (用 Grep + Read 采样), 确认:

- **04 头部首 codelist** (S2 用): `C65047 Laboratory Test Code` @ line 15, source `lb_part2.md`, offset 0.2%
- **04 中段 codelist** (S4 用, offset 40-60%): `C67154 Laboratory Test Name` @ line 2564, source `lb_part3.md`, offset 40.4%; 这是唯一落 40-60% 危险区的 codelist (其他 codelist 要么 <5%, 要么 >80%)
- **04 最末 codelist** (S3 用): `C100129 Category of Questionnaire` @ line 6050, source `qs_part1.md`, offset 95.4%; 整段延伸到 line 6341 (C102124 YMRS 为最末 entry)
- **C66742 不存在于 04** (grep 匹配 0) → S2 原题改编
- **AERELN 不存在于 04** (grep 匹配 0) → S5 原题保留

选题原则: S2/S3/S4 Term 数**控制在 3-5 条**, 避免 smoke 因答题长度大 timeout; 保留 Node 5 全量 A/B 深度验证的空间。
