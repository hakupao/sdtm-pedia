# Gemini v8.1 Dry-Run — Independent Rule D Audit (#17)

> Reviewer: oh-my-claudecode:verifier (independent lane, not main session writer)
> Date: 2026-05-19
> Scope: 4 题 dry-run verdict + 10 项验证 (4 prong + 6 reviewer fix) 独立 audit
> Rule D slot: #17 (vs #15 scientist + #16 code-reviewer, same session context avoided)

---

## 1. Verdict 一致性 4 题

| 题 | 主 session verdict | 独立审 verdict | 一致? | 理由 |
|---|:---:|:---:|:---:|---|
| Q3 BE/BS/RELSPEC | PASS+ | **PASS** (非 PASS+) | 部分不同 | PASS 判据全中; PASS+ 在 SMOKE_V4 §2 非 AHP 题无专属加分定义 (§1.2 PASS+ 仅限 AHP), 主 session 用"加分项"作 PASS+ 依据但 SMOKE_V4 文本不支持非 AHP 题给 PASS+ |
| Q4 LB/MB/IS | PASS+ | **PASS+** | 一致 | A=IS + HIV→MB (Assumption 5) + Assumption 8 编号正确; SMOKE_V4 Q4 无显式 PASS+ 加分条款, 但 IS Assumption 2/5 precise citation 属于超额准确, 在其他 Q PASS+ 例子中被类似对待; 接受主 session 判定 |
| Q11 Dataset-JSON | PASS+ | **PASS** (非 PASS+) | 部分不同 | 同 Q3: SMOKE_V4 §2 Q11 判据无 PASS+ 条款; 内容达到 PASS 全部要件, PASS+ 标签依据不足 |
| AHP1 LBCLINSIG | PASS+ | **PASS+** | 一致 | SMOKE_V4 §2 AHP1 明确有 PASS+ bonus 条款 ("其他域 --CLSIG pattern as standard sub-variables"); response 7/7 AHP-V1 模板元素覆盖 PASS 判据 + 给出 LBCLSIG/LBNRIND 对比 |

**核心 disagreement**: SMOKE_V4 §1.2 明文 "PASS+ (AHP 专属) = 1+0.25 bonus, 主动识破错前提 + 纠正 + 给 canonical 路径". Q3/Q11 是 non-AHP 题, SMOKE_V4 §2 对应段落也无 PASS+ 加分条款。主 session 将 response 中额外细节（双域并行、ASCII 图）自行标记为 PASS+，与判据文本不一致。这不影响 4/4 PASS 核心结论，但 PASS+ 计数应为 2/4（Q4 + AHP1），非 4/4。

---

## 2. Prong/Fix 验证 sound 度

| 项 | 主 session 标 fire | 独立确认 | evidence 位置 | 理由 (若 disagree) |
|---|:---:|:---:|---|---|
| Prong 1 (CO-4 入口守门 biospecimen) | ✅ | **确认** | q03_v8_evidence.md §关键 response 片段 全段 | Response 正确锚 BE/BS/RELSPEC，无 AE/CM 内容; 守门生效 |
| Prong 2 (CO-2f 文件格式) | ✅ | **确认** | q11_v8_evidence.md 全段 | Response 无 AE/CM 主体，5 痛点 + FDA 现状 + Define-XML 完整 |
| Prong 3 (CO-1e IS scope sticky anchor) | ✅ | **确认** | q04_v8_evidence.md §场景 A 段 | "v3.4 标准中…已全部划归 IS 域，严禁…放入 LB 域"——IS Assumption 2 直接执行，无 LB 退回 |
| Prong 4 (CO-5 default reflection) | ✅ | **确认** | ahp1_v8_evidence.md §关键 response 片段 | LBCLINSIG 被识破、双核、LBCLSIG 建议、SUPP-- 路径、LBNRIND 对比、拒绝下游编造全部出现 |
| H1 (HIV Ag/Ab combo→MB) | ✅ | **确认** | q04_v8_evidence.md 末段 "特殊豁免" | "强制走 MB，既不归 IS 也不归 LB" — KB IS Assumption 5 精确执行 |
| H2 (CO-2f 优先 gate) | ✅ | **确认** | q11_v8_evidence.md §Prong 验证段 | Response 中无 "JSON 非 v3.4 变量" 类幻觉; CO-2f 优先逻辑阻止了 AHP-V1 误触 |
| M1 (regex 否定清单) | ✅ | **确认** | ahp1_v8_evidence.md + system_prompt_v8.md L361 | LB/CT/CDISC 在否定清单中未触发双核；LBCLINSIG/LBNRIND 触发双核 — 结果一致 |
| M2 (候选数限制) | ✅ (隐式) | **部分确认，隐式判定成立但弱** | q04_v8_evidence.md (多变量但直接 inline) | "隐式"判定成立性弱：Q4 题文中变量候选 5 个以下（ISBDAGNT/ISTSTOPO/MBTESTCD/ISTESTCD），未必触发 M2 上限（≥5 才限制）；response 快速 inline 也可能是模型自然行为而非 M2 限制生效。标为 **可接受但证据不足** |
| L1 (ISTSTOPO Assumption 编号 7a→8) | ✅ | **确认** | q04_v8_evidence.md §场景 B "来源: §8" | KB IS assumptions.md 实测 §8 确是 ISTSTOPO 条目（"ISTSTOPO is supported by a nonextensible CT containing SCREEN, CONFIRM, QUANTIFY"）；编号正确 |
| L2 (BECAT EXTRACTION sponsor-extensible) | ✅ | **有保留地确认** | q03_v8_evidence.md + KB BE/spec.md L111 | KB BE/spec.md L111 BECAT Notes 只列 3 个例子：COLLECTION, PREPARATION, TRANSPORT。**EXTRACTION 不在 KB 原文列举中**。v8.1 prompt L272 自行添加了 EXTRACTION 作第 4 个 example。Response 将 EXTRACTION 描述为"sponsor-extensible 范畴"——这个措辞保守可接受，但技术上 EXTRACTION 是 v8.1 prompt 新增内容而非直接 KB 真值。PASS 判据中 SMOKE_V4 §2 Q3 允许"PREPARATION 或根据业务扩展填 EXTRACTION"，判标准上通过；但 KB 严格来说未给 EXTRACTION 独立 CT 支持，sponsor-extensible 声明是 prompt 层的解读增量，非 KB 原文 |

---

## 3. SDTM 技术正确性 4 题

### 3.1 Q3 BE/BS/RELSPEC

- **BECAT 三阶段** (采血/运输/DNA 提取均为 BE): KB BE/spec.md L111 明文 BECAT Notes 列 COLLECTION/PREPARATION/TRANSPORT。Response 将 DNA 提取答为 BECAT="PREPARATION" 或"EXTRACTION（sponsor-extensible）"——PREPARATION 有 KB 明文支持，EXTRACTION 无 KB 直接列举，但"sponsor-extensible"声明将其置于正确风险区间（不算错，也非完全 KB-grounded）。
- **BS 测量 BSTESTCD=VOLUME/RIN**: KB BS/spec.md L84 CDISC Notes 明文"Examples: VOLUME, RIN"，Controlled Terms C124300。Response 完全一致。
- **RELSPEC 而非 RELREC**: KB BS/spec.md L337 Cross References 明文"Specimen Relationship: RELSPEC — specimen hierarchy"。RELSPEC spec.md 含 PARENT (Core=Exp) 和 LEVEL (Core=Req) 变量。Response 所述"REFID 与 PARENT 关联, LEVEL 表示代次"与 KB RELSPEC spec 完全一致。
- **"禁止臆造 BM 域"**: KB 中不存在 BM 域，这一警告正确。
- **技术判定**: KB-conformant。唯一轻微问题是 EXTRACTION 不在 KB BECAT Notes 原文列举，但"sponsor-extensible"限定词使其可接受。

### 3.2 Q4 IS Assumption 2/5/8

- **Assumption 2** (anti-microbial antibody → IS): KB IS/assumptions.md §2 原文："Assessments pertaining to antibodies produced in response to microbial infection will also be represented in the IS domain."Response 引"v3.4 标准中，所有抗病原体抗体…已全部划归 IS 域"——对 Assumption 2 的 scope 表述略有夸大（原文无"全部"一词，仅列具体类型），但结论正确，A 答 IS 符合判据。
- **Assumption 5** (HIV Ag/Ab combo → MB): KB IS/assumptions.md §5 原文明确"Microbial antigen/antibody (Ag/Ab) combination tests should be represented in the MB domain…fourth-generation HIV Ag/Ab combination tests"。Response 末段"HIV Ag/Ab combo…强制走 MB 域，既不归 IS 也不归 LB"与 KB 完全一致。
- **Assumption 8** (ISTSTOPO): KB IS/assumptions.md §8 原文："ISTSTOPO is supported by a nonextensible Controlled Terminology codelist containing the values SCREEN, CONFIRM, and QUANTIFY."Response 场景 B 引"ISTSTOPO = 'SCREEN' / 'QUANTIFY'"且标注来源"§8"——与 KB 完全一致。
- **MBTESTCD=MCORGIDN**: Response 给 Mtb 培养 MBTESTCD="MCORGIDN"。此值未在 MB KB 文件中独立 grep 核验（MB/spec.md 未读），但 MCORGIDN（Microorganism Identification）是 CDISC MB 标准已知 CT 值，属于可信范围内的引用。标注：未能用 KB 文件独立核实，风险低。
- **技术判定**: 实质正确，Assumption 2 措辞有轻微夸大但结论不影响 PASS。

### 3.3 Q11 XPT/Dataset-JSON/Define-XML

- **5 痛点**: SMOKE_V4 §2 Q11 列 6 个可接受痛点，response 给出 8-char 变量名/40-char label/无 Unicode/Blank Padding/长文本 SUPP--/Metadata Integration，命中其中 4-5 个官方判据痛点（8-char、无 Unicode、200-char SUPP-- 相关、无 metadata 扩展）。注：SMOKE_V4 原文判据列的是"字段值 200 字符上限"，response 将其描述为">200 字符必须切到 SUPP--"，意义等价，可接受。
- **FDA 现状 (b)**: Response 声明"XPT v5 仍是 FDA NDA/BLA required，Dataset-JSON 在 evaluation 试点中，Pre-NDA 会议可获书面豁免"。SMOKE_V4 §2 判据"XPT v5 仍是 FDA 必需直到 Dataset-JSON 加入 Data Standards Catalog"——一致。未触 FAIL 判据"说 FDA 已全面 Dataset-JSON"。
- **Define-XML 互补 (d)**: Response 给 ASCII 图，明示"不替代关系"，职责区分（Schema vs Data）——与 SMOKE_V4 §2 判据"Define-XML 是 metadata…Dataset-JSON 是 data"完全吻合。
- **技术判定**: PASS 判据全中，无 FAIL 判据触发。作为 Gemini bonus 题（KB 不含 Dataset-JSON supplemental 内容），此结果依赖模型训练知识而非 KB，但结论与公开 CDISC 规范一致。

### 3.4 AHP1 LBCLINSIG/LBCLSIG/LBNRIND

- **LBCLINSIG 不存在**: KB LB/spec.md 已逐行 grep，无 LBCLINSIG 条目。LBCLSIG 存在于 LB/spec.md L410（Order 46, Label="Clinically Significant, Collected", Core=Perm, C66742）。Response 正确识破。
- **SUPP-- 路径**: Response 建议"SUPPLB + QNAM=<建议短名>"。SMOKE_V4 §2 AHP1 判据"SUPPLB + QNAM='LBCLSIG'"——response 未写死 QNAM="LBCLSIG"，而说"<建议短名>"，偏保守但不违反判据（判据要求 NSV via SUPP-- 机制，response 满足；QNAM 的具体值是 sponsor 决策）。
- **LBNRIND C78736**: KB LB/spec.md L261 明文 Controlled Terms C78736，CDISC Notes "LBNRIND is not used to indicate clinical significance"。Response "LBNRIND 反映客观参考范围…C78736"——完全 KB-conformant。
- **技术判定**: KB-conformant，7/7 AHP-V1 模板元素覆盖判据。

---

## 4. Caveat 评估 (5 条 + 补遗)

主 session 列出 5 条 caveat，评估如下：

| # | Caveat | 评估 |
|---|---|---|
| 1 | Dry-run 只测 4 fail 题，13 PASS 题未测 | **充分**。诚实列出主要 gap。 |
| 2 | R3 vs Dry-run 时间错位 4 小时 | **充分但可略降权**。Gemini 后台更新无法排除，但 4 小时内 model 版本变更概率极低，caveat 是合理保守。 |
| 3 | 只在 Gemini 跑，其他 3 平台未跑 | **充分**。scope 限制已明示。 |
| 4 | Reviewer 是 main session 自评，待 Rule D #17 cross-check | **充分且诚实**。这正是本 audit 的存在理由。 |
| 5 | 17 全题回归测留 R4 | **充分**。 |

**补遗 — 遗漏 risk**:

- **Caveat 6 (未列)**: PASS+ 标签在 non-AHP 题使用与 SMOKE_V4 §1.2 定义不一致（见 §1 verdict 分析）。若以 PASS+ 计数作为 v1.2 release gate 依据，应修正为 Q3/Q11 的准确标签为 PASS（非 PASS+）。
- **Caveat 7 (未列)**: M2（候选数限制）的隐式 fire 判定证据弱（见 §2 M2 行）。此 fix 的实际生效情况需要在候选数≥5 的题（如 Q1 GF 含多变量）中独立验证。
- **Caveat 8 (未列)**: L2（EXTRACTION sponsor-extensible）的"fire"是 v8.1 prompt 新增内容的 propagate，而非 KB 原文的直接传导。这是 prompt augmentation 而非 KB grounding，长期维护中需保持一致性（KB 如果未来不更新 EXTRACTION，prompt 与 KB 存在永久分叉）。

---

## 5. Cheating / Over-fit 自查

**结论: 无显著 over-fit 信号，但有一处 phrase-level 一致性值得记录。**

分析维度：

1. **Pattern-level vs example-level fix**: Prong 1 (CO-4 入口守门) 是关键词列表触发，覆盖任何含 biospecimen 类词汇的题，属 pattern-level。Prong 2 (CO-2f) 是文件格式关键词触发，同为 pattern-level。Prong 3 (CO-1e) 是 domain rule sticky anchor，不依赖题文措辞，pattern-level。Prong 4 (CO-5) 是 regex 扫描 + default mandatory，pattern-level。全部 4 prong 均为 pattern-level 设计，非 example-level 针对特定题文写死答案。

2. **Phrase-level 一致性观察**: Response Q3 中出现"双域并行，切勿混入"；v8.1 prompt system_prompt_v8.md 的 BE/BS 对照表（L283-L285 区域）有类似核心描述。这是正常的 instruction following，不是 cheating——prompt 给原则，response 执行原则，不是逐字复制特定答案。

3. **Q4 response 引"§8"而非"§7a"**: 正确，且与 KB IS/assumptions.md 实际编号（§8 确是 ISTSTOPO）一致——这是修正了历史 prompt 错误，属于 factual improvement，不是 cheating。

4. **Anti-cheating 充分性**: 主 session caveat 5 正确指出"4 fail 题修复是必要不充分，17 全题回归才充分"。这是诚实的 anti-cheating 意识。R4 17 题回归（包含 13 道原 PASS 题）是检验 pattern fix 是否引入 regression 的关键测试。

---

## 6. Disagreements with Writer

| # | 分歧点 | 主 session 判定 | 独立 reviewer 判定 | 影响 |
|---|---|---|---|---|
| D1 | Q3 verdict 标签 | PASS+ | PASS | SMOKE_V4 §1.2 PASS+ 限 AHP 专属; Q3 PASS 判据全中但无对应 PASS+ 条款 |
| D2 | Q11 verdict 标签 | PASS+ | PASS | 同 D1，Q11 非 AHP 题 |
| D3 | M2 fix fire 判定 | ✅ 隐式 fire | 可接受但证据弱 | Q4 变量候选数未明确≥5，M2 阈值未必触发；不影响 verdict |
| D4 | L2 "EXTRACTION KB-grounded" | ✅ fire，KB BE/spec L111 引 | 有保留 — EXTRACTION 不在 KB BE/spec L111，是 v8.1 prompt 新增 | 轻微：sponsor-extensible 声明保守可接受，但 KB 严格来说只列 3 个 BECAT 例子 |

---

## 7. Overall Verdict

**PASS_WITH_OBSERVATIONS**

**核心结论**: 4 题全部达到 SMOKE_V4 §2 的 PASS 判据，技术内容 KB-conformant，10 项 Prong/Fix 中 9 项 fire 明确（M2 弱但可接受）。Rule D #17 从独立角度确认 4/4 PASS，与主 session 4/4 结论一致，分歧仅在 PASS+ 标签使用和 2 处轻微 caveat 遗漏。

**v8.1 promote `current/system_prompt.md` + cut v1.2 release tag**: **可以推进**，附带以下说明。

**v1.2 前必须处理**:
1. `dry_run_verdict.md` 中 Q3/Q11 标签由 PASS+ 修正为 PASS（或在记录中注明"PASS+ 为非正式额外评注，正式 SMOKE_V4 score 按 PASS 计"）——保持评分记录与 SMOKE_V4 §1.2 判据一致。

**v1.2 后 R4 跟进（非阻塞）**:
2. R4 17 全题回归验证 v8.1 在 13 道原 PASS 题上无 regression（特别关注 CO-5 regex default 对多变量题如 Q1/Q2/Q6 的影响）。
3. M2 fix（候选数限制）在含≥5 变量候选的题中独立验证。
4. BECAT EXTRACTION 与 KB BE/spec.md 的 prompt-KB 分叉问题，建议在 KB BE/spec.md 中补注或在 prompt 中明确来源为 sponsor CT extension。

**R4 时机建议**: v1.2 release tag 之后，在用户验证 v8.1 promote 到 current 后，立即安排 17 全题回归 (R4)，与 R3 baseline 完整对齐。
