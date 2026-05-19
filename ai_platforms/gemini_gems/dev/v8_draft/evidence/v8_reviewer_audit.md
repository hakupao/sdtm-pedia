# Gemini v8 Prompt — Independent Reviewer Audit (Rule D)

> Reviewer: pr-review-toolkit:code-reviewer (independent lane, not main session writer)
> Date: 2026-05-19
> Scope: v8 4-prong system prompt changes vs R3 evidence + KB SDTM correctness
> Files audited: v8 prompt 516L, v7.1 baseline 423L, R3 reviewer §5, KB {IS,BE,BS,RELSPEC}, R3 evidence Q3/Q4/Q11/AHP1

---

## 1. R3 FAIL → v8 prong 映射核

| R3 FAIL | v7.1 gap | v8 prong | 实现位置 | 完整? | 备注 |
|---|---|---|---|:--:|---|
| Q3 BE/BS/RELSPEC 跑题 AE | CO 无 biospecimen keyword 守门 | Prong 1 (CO-4 入口守门) | v8 L217-228 | ✓ | 关键词列表覆盖中英文 13 项, 域锚 BE/BS/RELSPEC + 变量级 BECAT/BSTESTCD/REFID, 触发优先级先于变量表 |
| Q4-A 麻疹 IgG 退回 LB | CO 无 IS scope shift v3.3→v3.4 sticky anchor | Prong 3 (CO-1e IS scope) | v8 L119-157 | ✓ | trap 表 6 行 (麻疹/HBsAb/HCV/COVID/ADA/Mtb) + HIV exemption (Assumption 7) + sticky 锚显式标注 |
| Q11 Dataset-JSON 跑题 AE/CM | CO 无文件格式 ground rule | Prong 2 (CO-2f) | v8 L182-206 | ✓ | XPT v5 8/200/Unicode/metadata 痛点 + Dataset-JSON v1.1 UTF-8/nested/integrated metadata + Define-XML 互补 + 跑题守门 |
| AHP1 LBCLINSIG 跑题 CM/MH | AHP-V1 触发依赖 reflection scaffold | Prong 4 (CO-5 default) | v8 L301-303, L351-364, L499 | ✓ | 3 处协同改: AHP-V1 触发条件 + CO-5 共同执行规则 #1 + 工作流程 Step 1 全部用 regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` 触发 |

**Reviewer §5 4-finding 全部实现**: Finding 1 (HIGH, BE/BS/RELSPEC) → Prong 1 ✓; Finding 2 (MEDIUM bonus, file format) → Prong 2 ✓; Finding 3 (HIGH, IS scope) → Prong 3 ✓; Finding 4 (HIGH, reflection dependency) → Prong 4 ✓.

**完整映射**: 4-FAIL → 4-prong 一一对应, 无 finding 遗漏.

---

## 2. SDTM 技术正确性

### 2.1 CO-1e IS scope (vs KB IS assumption 2)

v8 L121-123 措辞 "anti-microbial antibody / 抗病原体抗体 测量值, 不论采集时机..., 全部归 IS" 与 KB `domains/IS/assumptions.md` §2 一致 (KB §2: "assessments that describe whether an allergen, microorganism, or endogenous molecule provoked/caused/induced an immune response... antibodies produced in response to microbial infection will also be represented in the IS domain").

**Trap 表核**:
- 麻疹 IgG → IS, ISBDAGNT=MEASLES VIRUS — KB §7 ISBDAGNT 用法对 ✓
- HIV Ag/Ab combo exemption → 走 MB — KB §5 明确 "HIV Ag/Ab combination tests should be represented in the Microbiology Specimen (MB) domain" — **v8 措辞偏差**: v8 L138 写 "HIV Ag/Ab combo... 可归 LB (历史 routine HIV screening 路径)", 但 KB 是 **MB** 不是 LB. **MEDIUM finding**: 此处 v8 写错替代域, 应改 "可归 MB (per IS Assumption 5 antigen/antibody combo exemption)" 而非 LB.
- ISTSTOPO SCREEN/CONFIRM/QUANTIFY 三层 — KB §8 nonextensible CT codelist 一致 ✓ (note: v8 标注 "Assumption 7a" 但 KB 实际是 Assumption 8 — **LOW finding**: 编号不准, 但语义对)
- 细胞因子/补体 → LB — KB §6 一致 ✓ (v8 未提, 算可接受边界)

### 2.2 CO-4 入口守门变量 (vs KB BE/BS/RELSPEC spec)

**BECAT 值**: v8 L220 "COLLECTION/TRANSPORT/PREPARATION/EXTRACTION" — KB `BE/spec.md` L111 注解 "Example: COLLECTION, PREPARATION, TRANSPORT" — KB 仅列 3 个 (COLLECTION/PREPARATION/TRANSPORT), 未列 EXTRACTION. **LOW finding**: v8 加 EXTRACTION 是合理推论 (KB `BE/assumptions.md` §1 提及 "specimen collection, freezing and thawing, aliquoting, and transportation" + extraction 是常见样本处理), 但严格论 KB 未明列, 建议 writer 注 "EXTRACTION 是 sponsor-extensible Example, 非 CT 锁定".

**BSTESTCD VOLUME/RIN**: v8 L222 — KB `BS/spec.md` L84 "Examples: VOLUME, RIN" 一致 ✓. CT=C124300 一致 ✓.

**RELSPEC REFID/PARENT/LEVEL**: v8 L222 — KB `RELSPEC/spec.md` 变量列 STUDYID/USUBJID/REFID/SPEC/PARENT/LEVEL 一致 ✓ (writer 略过 SPEC, 但 v8 是入口守门提示不是完整列表, 可接受).

### 2.3 CO-2f 文件格式 spec 描述

XPT v5 痛点描述 (v8 L195) "变量名 8-char / label 200-char / no Unicode / 外置 metadata 依赖 Define-XML" — 行业共识, 准确 ✓. Dataset-JSON v1.1 features "UTF-8 / 内嵌 metadata + structure / 兼容大 dataset / FDA 2026 evaluation" — 行业共识, 准确 ✓. Define-XML v2.1 "metadata 规范" 描述准确 ✓.

**KB 边界声明** (L201-202): v8 明示 "本 Gem KB 不 inline Dataset-JSON v1.1 / XPT v5 完整 spec" + 指 CDISC 官方 — 边界处理得当, 防过度自信. PASS.

---

## 3. Prompt-engineering soundness

### 3.1 CO-5 regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` 合理性

**False-positive 风险 HIGH**:
- 常见非 SDTM 缩写命中: FDA / USA / NCI / EVS / ADaM / SDTM / CDISC / EDC / CRF / SAS / XML / JSON / IS (IS 也是 SDTM 域名)
- 题文常态化引用 "FDA Data Catalog" / "ADaM ADAE" / "SDTM v2.0" 等都会强制走双核 grep — **每答都跑 N 次 KB 双核** = 性能 + verbose 重负载
- regex 长度 2-17 字符过宽, e.g. "AESERIOUS" (9 char) / "STUDYID12345" 都命中

**建议 fix (MEDIUM)**: regex 应配合**否定清单**, 至少排除明显非 SDTM 缩写 (FDA/USA/NCI/EVS/CDISC/ADaM/SDTM/SAS/XML/JSON 等). 或 regex 收紧至 `^[A-Z]{2}[A-Z0-9]{1,8}$` 且要求**至少 1 数字混合或末尾 TESTCD/CAT/SEQ 后缀**. 当前 over-trigger 风险 prompt-architecture 层面值得 writer 二轮 review.

### 3.2 工作流程 Step 1 改 default mandatory 性能影响

v8 L499 "答题第一动作 = 用 regex 扫用户问题, 列出所有 SDTM-shaped identifier 候选, 对每一个 (不挑选不过滤), 跑 AHP-V1 §双核强制规则" — 设计正确但**每个候选 × 2 文件 grep × 候选数 = O(N × 2)** 操作. 对 Q5 (3 域 FA/QS/CE) / Q14 (多域多变量题), 候选可能 5-15 个, 即每答开头 10-30 次 grep, response latency 风险 MEDIUM.

**实战 mitigation 建议**: writer 在 Step 1 加 "若候选 ≥ 5, 优先扫题文显式提及的 (3-5 个), 其余在 response 内嵌入时再核". 当前 v8 未限制 候选数 — 可能放大 verbose tendency.

### 3.3 4 prong 之间冲突分析

- **CO-1e IS scope vs CO-4 入口守门**: 题文 "麻疹 IgG 滴定 + 血液样本采集" 同时命中 IS scope (anti-microbial antibody) + biospecimen keyword (血液样本). 两触发器都激活 → IS (测量) + BE (采集行为) + BS (体积测量) 多域并行 — **设计合理, 不冲突** (v8 L224 明确 "必双域并行"). ✓
- **CO-2f vs CO-5 regex**: 题文 "Dataset-JSON v1.1" 含 SDTM-shaped 标识符 "JSON" / "XPT" 吗? "JSON" 4 char 全大写命中 regex → 跑 KB 双核 → 必然未命中 → 走 AHP-V1 模板. 但 CO-2f 也触发. **潜在矛盾**: AHP-V1 模板会判 "JSON 非 v3.4 standard variable", CO-2f 会判 "Dataset-JSON 是文件格式". 两个 trigger 输出**不同模板**, 哪个优先? v8 未明确优先级 — **MEDIUM finding**.
- **建议 fix**: 工作流程 Step 1 加 "若候选命中 CO-2f 关键词 (XPT/Dataset-JSON/JSON/XML 等), CO-2f 优先于 AHP-V1, 不走变量幻觉路径".

---

## 4. v8 vs v7.1 完整性 diff

| 段 | v7.1 | v8 | Delta |
|---|---|---|---|
| CO-1/1b/1c/1d (AE/DM/ARM/SUPP) | L42-111 | L49-117 | 不变 ✓ |
| **CO-1e (新)** | — | L119-157 | +新, 不破坏原 CO-1 系列 ✓ |
| CO-2/2e/2c (NCI EVS/CT) | L113-141 | L159-181 | 不变 ✓ |
| **CO-2f (新)** | — | L182-206 | +新, 插在 CO-2e 后 CO-2c 前 ✓ |
| CO-4 GF/CP/BE/BS 变量表 | L143-206 | L215-293 | 主体不变, 顶部加 "入口守门" 段 L217-228 ✓ |
| CO-5 AHP-V1/V2/V3 | L208-269 | L295-364 | AHP-V1 触发条件改 (L301-303), CO-5 共同执行规则 #1 改 + 新 #7 跑题守门 (L353-364) ✓ |
| 工作流程 Step 1 | L405 | L499 | regex 强化 ✓ |
| 边界处理模板 ①-⑧ | L347-386 | L441-480 | 不变 ✓ |
| Rule E | L418-422 | L512-516 | 不变 ✓ |

**verdict**: 完整性 PASS. 原 v7.1 所有 CO-1/CO-1b/CO-1c/CO-1d/CO-2/CO-2c/CO-2e/CO-3/CO-4/CO-5/AHP-V1/V2/V3 保留, 无意删除. 新增段落与原段落格式风格一致.

**MINOR**: design rationale 称 v8 ~600 行 / +42%, 实际 v8 是 516 行 / +22% (513-423=93 行). Rationale 行数估算偏高, 但 risk 评估方向对.

---

## 5. Risk surface 评估

**Rationale §"风险与未尽事项" 5 条独立核验**:
1. ChatGPT vs Claude trend — v8 scope 外, 评估合理 ✓
2. NotebookLM PUNT 评分 — v8 scope 外, 合理 ✓
3. R3 vs R1 题库 noise — 合理 ✓
4. v8 prompt 长度 — rationale 称 +42% (实际 +22%), 但 Gemini 1M 窗口 attention recall 风险评估方向对 ✓
5. Sticky anchor decay — 关键 finding, R2 修过的 Q4-A 退回 R3 是确实信号, 长期 monitor 必要 ✓

**Reviewer 补充 risk** (rationale 未提):
- **6. 4-prong 触发优先级未明** (见 §3.3) — CO-2f vs CO-5 regex 触发候选冲突, 可能导致 Q11-like 题在 v8 下走错模板
- **7. regex over-triggering** (见 §3.1) — 每答开头 N × 2 grep, response latency + verbose 风险
- **8. EXTRACTION 在 BECAT 非 KB 明列 Example** (见 §2.2) — 严格论应注释 "sponsor-extensible"
- **9. v8 CO-1e HIV Ag/Ab 错替代域** (见 §2.1) — 应是 MB 不是 LB

---

## 6. Disagreements with writer

**D1 (MEDIUM)**: design rationale §"4 Prong 具体改动详述" Prong 3 §"例外" 称 "HIV Ag/Ab combo 有 IS Assumption 7 exemption (可 LB, 历史 routine HIV screening 路径)" — 但 KB IS Assumption 5 明确该 exemption 走 **MB**, 不是 LB. v8 prompt L138 同错. 这是事实错误.

**D2 (LOW)**: v8 标注 IS Assumption 7a (SCREEN/CONFIRM/QUANTIFY) — 但 KB IS Assumption 8 才是 ISTSTOPO 三层定义. 编号不准.

**D3 (LOW)**: rationale 行数估算 600 行 / +42%, 实际 516 行 / +22% — risk 方向对但数字夸大.

---

## 7. Overall verdict

**PASS_WITH_OBSERVATIONS** — v8 4-prong 架构对, 实现完整, R3 FAIL→prong 一一覆盖. 但有 2 个事实错误 (HIV exemption 域名错 / Assumption 编号错) 和 2 个 prompt-engineering 隐患 (regex over-trigger / prong 优先级未定) 需 v8.1 修.

**必须修的项 (HIGH)**:
- **H1**: v8 L138 + rationale 把 HIV Ag/Ab combo exemption 域名从 LB 改为 **MB** (KB IS Assumption 5)
- **H2**: 4-prong 触发优先级显式定义 (CO-2f 关键词命中时优先于 CO-5 regex AHP-V1 路径, 避免 Dataset-JSON 题误走变量幻觉模板)

**建议改的项 (MEDIUM)**:
- **M1**: CO-5 regex 加否定清单 (FDA/USA/NCI/EVS/CDISC/ADaM/SDTM/SAS/XML/JSON 等) 或收紧 regex 至要求数字混合, 防 over-trigger
- **M2**: 工作流程 Step 1 加候选数上限 (e.g., 候选 ≥ 5 时只扫题文显式提及的 3-5 个) 防 verbose

**建议改的项 (LOW)**:
- **L1**: v8 L139 IS ISTSTOPO 编号 Assumption 7a → Assumption 8 (per KB)
- **L2**: CO-4 入口守门 BECAT EXTRACTION 加 "sponsor-extensible" 注释
- **L3**: rationale 行数估算更新为实际 +22% (而非 +42%)

**Dry-run 决策**:
- **可进 dry-run** 4 fail 题 (Q3/Q4-A/Q11/AHP1), 4-prong 主体架构对, H1/H2 不阻塞 dry-run (Q4-A 是麻疹不是 HIV; Q11 与 CO-5 regex 冲突可被 R3 evidence 4 题 dry-run 实测验证)
- **dry-run 后必修** H1/H2 再 cut v1.2 release. H1 是事实错, H2 是架构隐患, 都不能进 prod
- **若 dry-run 4 题全 PASS**, 走 v8.1 修 H1/H2/M1/M2 后 cut v1.2

---

*Audit completed: 2026-05-19. Reviewer: pr-review-toolkit:code-reviewer (Rule D #16, independent lane). Evidence base: v8 prompt 516L + v7.1 baseline 423L + R3 reviewer §5 + KB {IS/BE/BS/RELSPEC} spec+assumptions + R3 evidence Q3/Q4/Q11/AHP1 + design rationale. No main session context consulted during finding formation.*
