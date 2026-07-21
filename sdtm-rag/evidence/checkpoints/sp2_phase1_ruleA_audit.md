# SP2 结构化答题通道 — N=8 分层语义抽检 (规则 A, 独立审 规则 D)

> 审阅者: 独立 auditor (与 SP2 实现者非同 agent/session, 规则 D).
> 日期: 2026-06-20.
> 被审对象: `eval/prod_wirein/v3_sp2_on_t0.json` (140q ON-arm, deepseek-chat, t=0).
> 通道职责: 在 count/enumerate/attribute/CT 类问题上, 把 `data/meta/meta.yaml` (SP1 产物) 的权威事实注入 LLM 上下文, 并在模型与某个计数矛盾时追加 correction.
> 独立真值来源: `server/meta_store.MetaStore` 直读 meta.yaml; 其中 2 项另行对账 `knowledge_base/` 原始 KB (非仅以 meta.yaml 为唯一证人).
> 方法学要点: 用户看到的答案文本 = 被审产物. 不看 `fact_recall` 自动指标判分 (它只做子串匹配, 见 q67/s05 假阳性), 而是逐条核验"用户读到的整段答案对所问能力是否语义正确且不误导".

## 抽样: 4 能力类 × 2 = N=8

| # | id | 能力类 | 问题 (节选) |
|---|----|-------|------------|
| 1 | q103 | COUNT (var→#domains) | TAETORD 出现在多少个域, label 是什么 (强制项) |
| 2 | q104 | COUNT (var→#domains) | VISITDY 出现在多少个域, label 代表什么 (强制项) |
| 3 | q34 | ENUMERATE (codelist→域+变量) | C66742 (NY) 被哪些域共享, 各域典型使用变量 |
| 4 | q107 | ENUMERATE (var→数据集列表) | 哪些数据集同时含 ARM 与 ARMCD, 两者 label |
| 5 | q43 | CT/codelist | DM.SEX 的 codelist code 与 Core designation |
| 6 | s05 | CT/codelist | VS.VSTESTCD 的 codelist code/名称/是否可扩展/3 个示例值 |
| 7 | q05 | ATTRIBUTE | PE 结构 + PETESTCD 角色 + 整体检查单记录时取值 |
| 8 | q01 | ATTRIBUTE | AETERM 是什么, 在 AE 域的全部变量属性 |

---

## 逐条核验

### 1. q103 — COUNT (TAETORD → #domains) — **PASS**
- **独立真值 (MetaStore)**: `domains_for_variable('TAETORD')` → 43 个域; label `Planned Order of Element within Arm`; role Timing, type Num, core Perm.
- **答案声称**: "TAETORD 出现在 43 个 SDTM 域中", label "Planned Order of Element within Arm", `[Source: Structured Facts]`.
- **裁定**: PASS. 计数 43 与 label 与真值完全一致.
- **原始 KB 交叉对账 ✅ (项 1/2)**: `knowledge_base/VARIABLE_INDEX.md` L24 独立写明 `TAETORD | 43 | AE, AG, CE, ... VS | Planned Order of Element within Arm | Num | Timing | Perm*`. 域列表逐元素匹配 meta.yaml. **meta.yaml 不是唯一证人.**

### 2. q104 — COUNT (VISITDY → #domains) — **PASS**
- **独立真值 (MetaStore)**: `domains_for_variable('VISITDY')` → 36 个域; label `Planned Study Day of Visit`.
- **答案声称**: "VISITDY 出现在 36 个 SDTM 域中", label "Planned Study Day of Visit", 并**列出全部 36 个域**: AG, BE, BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SC, SR, SS, SV, TR, TU, TV, UR, VS.
- **集合核验**: 答案列出的 36 域 == meta.yaml 真值集合 (差集双向均空, `ans==gt` True). 非仅"数对了 36", 列表成员逐个匹配.
- **裁定**: PASS. 计数 + 列表 + label 全对.

### 3. q34 — ENUMERATE (C66742 → 域 + 典型变量) — **PASS**
- **独立真值 (MetaStore)**: `domains_for_codelist('C66742')` → 41 个域; codelist name "No Yes Response", extensible False, 4 terms.
- **答案声称**: "C66742 被 41 个 SDTM 域共享", 给出 41 行表 (域→典型变量), 4 个值 N/NA/U/Y, 并由通道追加 correction "C66742 appears in exactly 41 SDTM domains".
- **集合核验**: 答案表中 41 个域 == 真值 41 域 (差集双向均空). 抽检典型变量 (AE: AESER/AEPRESP; LB: LBBLFL/LBFAST; VS: VSBLFL/VSCLSIG) 均落在注入事实变量清单内.
- **裁定**: PASS. 41 域 + 列表 + 4 值正确. (注: 自动 `fact_recall=0.5` 因子串没命中 "NY" 缩写 — 与语义正确性无关, 答案确实讲的是 No Yes Response.)

### 4. q107 — ENUMERATE (ARM + ARMCD → 数据集) — **PASS**
- **独立真值 (MetaStore)**: ARM ∈ {DM, TA, TV}; ARMCD ∈ {DM, TA, TV}; 交集 = **DM, TA, TV** (3 个). ARM label `Description of Planned Arm`; ARMCD label `Planned Arm Code`.
- **答案声称**: "同时出现在 3 个数据集: DM, TA, TV"; ARM = Description of Planned Arm; ARMCD = Planned Arm Code.
- **裁定**: PASS. 数据集集合 + 两个 label 全对. (自动 `fact_recall=0.6667` 把 "DM, TA, TV" 当一个整串没命中 — 子串指标缺陷, 实际答案分别列出三者, 语义正确.)

### 5. q43 — CT/codelist (DM.SEX → C66731 / Core) — **PASS**
- **独立真值 (MetaStore)**: SEX attrs → label Sex, role Record Qualifier, type Char, core **Req**, ct_codes `['C66731']`; C66731 name "Sex", extensible False, 4 terms.
- **答案声称**: SEX codelist = C66731 (Sex); Core = Req; type Char; role Record Qualifier; 允许值 F/M/U/UNDIFFERENTIATED.
- **裁定**: PASS. codelist code + Core + role + type 全对.
- **原始 KB 交叉对账 ✅ (项 2/2)**: `knowledge_base/domains/DM/spec.md` L185-192 独立写明 SEX → Controlled Terms **C66731**, Role Record Qualifier, Core **Req**, Type Char. `terminology/core/dm.md` L54 `## Sex (C66731)`. **meta.yaml 不是唯一证人.**

### 6. s05 — CT/codelist (VS.VSTESTCD) — **PARTIAL**
- **独立真值 (MetaStore)**: VSTESTCD ct_codes `['C66741']`; C66741 name "Vital Signs Test Code", **extensible=True (Yes)**, 64 terms. C66741 含 SYSBP/DIABP/**HR** (heart rate, C49677) — HR 与 PULSE (C49676) 是不同 term.
- **答案声称**: code C66741 ✓; name "Vital Signs Test Code" ✓; **可扩展性: "上下文未明确说明" (留空/搪塞)**; 示例值给 SYSBP, DIABP, **PULSE** (而问题点名要 blood pressure + heart rate, 即 HR).
- **裁定**: **PARTIAL**. code/name 对; 但 (a) 该问明确问"是否可扩展", 真值 Yes, 答案答"未说明" — 缺失且对用户误导 (暗示不可知); (b) 问 heart rate 示例, 答案给 PULSE 而非 HR — PULSE 虽是有效 term 但不是所问的 heart-rate code. **根因**: 该问锚定了 "VS 域", 通道只注入了 VS 域级事实并追加 "VS contains exactly 38 variables" (此 correction 正确, 已对账 domain_info VS=38), 但**未注入 C66741 的 codelist 级事实 (extensible/示例值)** — 通道在此问没有补上 codelist 元数据这一缺口.
- **指标假阳性提示**: 自动 `fact_recall=1.0` 报命中 "Extensible: Yes" 与 "HR" — 实为子串匹配假阳性, 答案文本恰恰说"未说明"且用 PULSE. 这正是规则 A 语义核验补住自动指标漏判之处.

### 7. q05 — ATTRIBUTE (PE 结构 / PETESTCD 角色 / 取值) — **PASS**
- **独立真值 (MetaStore)**: PE domain_info → class Findings, structure "One record per body system or abnormality per visit per subject"; PETESTCD role **Topic**, label "Body System Examined Short Name". PHYSEXAM 为整体检查单记录取值 (KB PE spec).
- **答案声称**: 结构 = "One record per body system or abnormality per visit per subject", class Findings `[Source: Structured Facts]`; PETESTCD role Topic; 整体记录取值 PETESTCD = "PHYSEXAM".
- **裁定**: PASS. 结构 + 类 + 角色 + 取值全对.

### 8. q01 — ATTRIBUTE (AETERM 在 AE 域全部属性) — **PASS**
- **独立真值 (MetaStore)**: AETERM attrs → label "Reported Term for the Adverse Event", role **Topic**, type **Char**, core **Req**, ct_codes [] (无受控术语).
- **答案声称**: Order 9; label "Reported Term for the Adverse Event"; Type Char; Controlled Terms 无; Role Topic; Core Req; CDISC Notes "Verbatim name of the event."
- **裁定**: PASS. label/type/role/core/CT(无) 全对; 补充 AEMODIFY/AEDECOD 编码链说明亦正确, 无幻觉变量/域.

---

## 总体规则 A 裁定: **PARTIAL (6 PASS / 1 PARTIAL / 0 FAIL 于抽样 8 题; 另发现 1 项抽样外计数缺陷 q67)**

抽样 8 题: **q103, q104, q34, q107, q43, q05, q01 = 7 PASS; s05 = PARTIAL; 无 FAIL.** COUNT 与 ENUMERATE 两类 (含两个强制项 + 列表成员逐个对账) 全部语义正确, 是本通道最强项 — 计数与列表均来自 meta.yaml 注入且 correction 闸已生效. 因此不能给出"全 8 题语义正确"的无条件 PASS, 整体记 **PARTIAL**, 缺陷集中在 CT/codelist 类的"通道未注入 codelist 级事实"这一覆盖盲区.

### 缺陷清单
1. **s05 (PARTIAL, 抽样内)**: VS.VSTESTCD 问可扩展性 + heart-rate 示例, 答案答"未说明 extensible"且以 PULSE 代 HR. 根因: 该问锚定 "VS 域", 通道只注入域级事实 (并追加 "VS 38 variables" 正确 correction), **未注入 C66741 的 extensible/示例值**. 用户看到的答案在可扩展性上不完整且略误导.
2. **q67 (FAIL on count, 抽样外但同根因, 强烈建议记入)**: 问 "C66742 被多少个**变量**引用". meta.yaml 真值 = **123** 个唯一变量 (123 个 location pair, 无重名); 通道注入的事实块**完整列出了这 123 个变量**, 但通道只对 codelist 做了 **domain 计数**的 checkable correction (`structured_answer.py` L140 `CheckableCount(code,"domains",len(doms))`), **未对变量计数设 correction**. 结果 LLM 在拿到 123 个变量全清单的情况下自报 **"106 个变量"** (幻觉计数), 而通道的 correction 只兜了 "41 domains", 错误的 106 原样透传给用户. 自动 `fact_recall=1.0` 因只查子串 C66742/AESER/AESDTH, 完全没碰这个数 — 又一处子串指标漏判. 这是 SP2 通道一个**真实的语义错误**: enumerate codelist→variables 计数无护栏.

### 给 SP2 的修复建议 (非本审职责, 仅记录)
- 在 `structured_answer.py` 为 codelist 增加一条 **变量计数** 的 `CheckableCount(code,"variables",n_unique_vars)`, 与现有 domain 计数对等, 使 q67 这类 "多少变量引用该 codelist" 也进入 correction 闸.
- 当问题点名 codelist (含通过域内某变量间接问及 codelist 元数据, 如 s05 的 VSTESTCD→C66741) 时, 即便主锚是域, 也注入该 codelist 的 extensible/term 示例事实, 堵住 CT 类覆盖盲区.

### 交叉对账声明
8 题中 **2 题**额外对账原始 KB, 证实 meta.yaml 非唯一证人:
- **q103** → `knowledge_base/VARIABLE_INDEX.md` (TAETORD=43, 域列表与 label 逐项匹配).
- **q43** → `knowledge_base/domains/DM/spec.md` + `terminology/core/dm.md` (SEX→C66731, Core Req, Record Qualifier).
两处原始 KB 与 meta.yaml 完全一致, SP1 元数据层在受审切片上忠实于源.
