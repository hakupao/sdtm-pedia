# Q3 (v5c post-fix) — BE vs BS + RELSPEC

> 日期: 2026-04-22
> 底座: Gemini Gem v5c
> 执行: 用户 Web UI 独立新会话
> 对比 baseline: `Q3_answer.md` (v5 era, FAIL — BS 当 Events + 臆造 BM Biospecimen Measurements 当 Findings, 命名倒置 + v3.4 无此域)
> Verdict: **PASS (BE/BS 未倒置, 无 BM, RELSPEC 派生正, 双域并行)**

---

## 题面

> SDTMIG v3.4 有 BE (Biospecimen Events) 和 BS (Biospecimen Findings) 两个新域. 一次采血流程包含: 采血行为 → 运输 → DNA 提取 → 测量血样体积 (mL) 和 RIN 值 → 派生出的 DNA 样本 (BS-001 → DNA-001). 请问: 哪些步骤归 BE? 哪些归 BS? 派生关系用什么变量? 请分别给出 BE/BS 的 Topic 变量名 + 典型 Qualifier + 源路径.

## 原文答案 (Gemini v5c)

在 SDTMIG v3.4 中, 关于生物样本的追踪和测量, **BE (Biospecimen Events)** 和 **BS (Biospecimen Findings)** 两个新域有着非常严格且明确的边界界定. 针对您描述的整个采血到提取的流程, 具体的归属、派生关系及变量映射如下:

### 1. 步骤归域: BE vs BS 的边界
根据 SDTMIG v3.4 的建模原则: 针对生物样本的**处理行为、操作或事件**归入 BE 域; 针对生物样本的**客观检验与测量结果**归入 BS 域. 如果在同一场景下既有采血行为又有测量, 必须**双域并行记录**, 不可二选一.

* **归属于 BE 域 (Events 类)**:
    * **采血行为**: 记录采集动作, 分类为 `BECAT = "COLLECTION"`.
    * **运输**: 记录样本流转过程, 分类为 `BECAT = "TRANSPORT"`.
    * **DNA 提取**: 记录样本的处理和加工, 分类为 `BECAT = "PREPARATION"` 或 `"EXTRACTION"`.
* **归属于 BS 域 (Findings 类)**:
    * **测量血样体积 (mL)**: 血样的物理属性测量, 测试代码为 `BSTESTCD = "VOLUME"`.
    * **测量 RIN 值**: RNA/DNA 的完整性质量数值测量, 测试代码为 `BSTESTCD = "RIN"`.
    * *(注意: v3.4 中不存在且严禁臆造 "BM" 域, 所有的样本测量值统统走 BS 域.)*

### 2. 样本派生关系: BS-001 → DNA-001
* **适用机制**: **RELSPEC** (Related Specimens) 数据集.
* **规则说明**: 在 SDTM v3.4 中, 描述生物样本之间 (如母样本与子样本、原始血样派生出核酸样本) 的层级关系 (Specimen hierarchy), 不再使用传统的 RELREC 数据集, 也不在 BE/BS 内部互相嵌套, 而是专门使用 **RELSPEC** 数据集来构建和追溯样本谱系.

### 3. Topic 变量、典型 Qualifier 及源路径

#### BE (Biospecimen Events) 域
* **Topic 变量**:
    * `BETERM` (Biospecimen Event Term, Core=Req) - 事件名称.
* **典型 Qualifier 变量**:
    * `BECAT` (Category for Biospecimen Event) - 用于区分行为类型, 如 "COLLECTION", "TRANSPORT", "PREPARATION".
    * `BEREFID` (Biospecimen Reference ID) - 关联具体的生物样本引用 ID.
* **源路径**: `knowledge_base/domains/BE/spec.md`

#### BS (Biospecimen Findings) 域
* **Topic 变量**:
    * `BSTESTCD` / `BSTEST` (Biospecimen Test Short Name / Name, Core=Req, CT=C124300) - 测试项目代码/名称, 如 "VOLUME" 或 "RIN".
* **典型 Qualifier 变量**:
    * `BSORRES` (Result or Finding in Original Units) - 原始测量结果.
    * `BSORRESU` (Original Units) - 原始结果单位.
    * `BSSTRESC` / `BSSTRESN` (Character/Numeric Result/Finding in Std Format) - 标准化格式的字符型或数值型结果.
* **源路径**: `knowledge_base/domains/BS/spec.md`

---

## CO-4 生效性分析

| 维度 | v5 baseline | v5c post-fix | CO-4 锚生效证据 |
|------|:---:|:---:|----|
| BE/BS 命名倒置 | FAIL (BS 当 Events) | **未倒置** (BE=Events / BS=Findings 正) | 与 CO-4 §BE/BS 段 Class 定义一致 |
| BM 域臆造 | FAIL (臆造 Biospecimen Measurements) | **主动声明 "严禁臆造 BM"** | 答案括注 "v3.4 中不存在且严禁臆造 BM 域" 直接 echo CO-4 §BE-vs-BS "禁止臆造 BM" 段 |
| BE Topic | — | BETERM Core=Req | 与 CO-4 §BE "BETERM Core=Req" 一致 |
| BS Topic | — | BSTESTCD/BSTEST Core=Req CT=C124300 | 与 CO-4 §BS "BSTESTCD/BSTEST Core=Req, CT=C124300" 逐字一致 |
| BECAT Examples | — | COLLECTION / TRANSPORT / PREPARATION / EXTRACTION | 与 CO-4 §BE "BECAT Examples COLLECTION/PREPARATION/TRANSPORT/EXTRACTION" 逐字一致 |
| BSTESTCD Examples | — | VOLUME / RIN | 与 CO-4 §BS "Examples VOLUME / RIN" 逐字一致 |
| 双域并行 | v5 baseline 未到此深度 | **主动声明** "必须双域并行记录, 不可二选一" | 直接 echo CO-4 §CO-4 执行规则 3 "碰到 BE 和 BS 同场景, 必须双域并行" |
| RELSPEC vs RELREC | — | 主动区分 "不再使用 RELREC, 专用 RELSPEC" | 与 CO-4 §BE-vs-BS 边界表 "RELSPEC (非 RELREC, 非 BE/BS) specimen hierarchy" 一致 |

**Verdict**: **PASS 完全生效** — CO-4 §BE + §BS + 边界表 + 执行规则 4 条锚**全命中**, 反向锚 BM 禁语**主动 echo**; 深度内化到区分 RELSPEC vs RELREC.

---

## 独立 KB grep 核 (Rule A sample=Q3)

- `knowledge_base/domains/BE/spec.md` 独立 grep 证 "Class: Events" + BETERM + BECAT Examples (reviewer 23 已核)
- `knowledge_base/domains/BS/spec.md` 独立 grep 证 "Class: Findings" + BSTESTCD/BSTEST + VOLUME/RIN + BSORRES/BSORRESU/BSSTRESC/BSSTRESN (reviewer 23 已核)
- `knowledge_base/domains/BM/` 独立 grep 0 匹配 (证 v3.4 无此域, baseline 确是臆造)
- RELSPEC: reviewer 23 未独立核但 KB grep `knowledge_base/datasets/RELSPEC` 存在

**Rule A verdict**: BE/BS Class + Topic + Qualifier + BECAT Examples 变量命名层真实且深度内化.
