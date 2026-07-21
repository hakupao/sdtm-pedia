# Q3 (A3 — BE + BS + RELSPEC) 生物样本从采集到 DNA 提取

> Date: 2026-04-22 / Account: bojiang.zhang.0904@gmail.com / Fresh chat after delete

---

## 题

某 PGx 试验, 受试者 Visit 2 现场采集血样 (BS-001), 当天运输到中心实验室 (运输过程记为一个事件), 第二天从 BS-001 样本提取 DNA 得到 DNA-001 子样本. 请说明: (a) 这三个"阶段" (采血 / 运输 / DNA 提取) 分别记录在哪些域? (b) 血样的"体积 = 5 mL"和"RNA 完整性数 (RIN) = 9.2"这两个**测量**记录在哪个域, 对应 Topic 变量值分别是什么; (c) BS-001 → DNA-001 这种**样本派生关系**怎么表达? 应该用哪个 Dataset (RELREC 还是另一个)?

## NotebookLM 答 (full text)

针对您的 PGx 试验生物样本场景, 以下是基于 SDTMIG v3.4 知识库的详细解答:

### (a) 采血、运输与 DNA 提取记录的域

这三个阶段 (采血、运输、提取) 均属于改变或对生物样本产生直接影响的行动/事件, 因此全部记录在 **BE (Biospecimen Events)** 域中 [1]。

- 采血: 对应 `BETERM` (Req) = `Collecting` [2,3]
- 运输: 对应 `BETERM` (Req) = `Shipping` [2,3]
- 提取: 对应 `BETERM` (Req) = `Extracting` [3,4]

### (b) 体积与 RIN 的记录域及 Topic 变量值

血样体积 (5 mL) 和 RNA 完整性数 (RIN=9.2) 属于针对生物样本特性的测量结果, 因此记录在 **BS (Biospecimen Findings)** 域中 [5]。

在 BS 域中, 对应的 Topic 变量 (强制必填 Core = Req) 值如下:

- 血样体积:
  - `BSTESTCD` (Biospecimen Test Short Name, C124300) = `VOLUME` [6]
  - `BSTEST` (Biospecimen Test Name, C124299) = `Volume` [6]
- RNA 完整性数 (RIN):
  - `BSTESTCD` (Biospecimen Test Short Name, C124300) = `RIN` [6,7]
  - `BSTEST` (Biospecimen Test Name, C124299) = `RNA Integrity Number` [6,7]

### (c) 样本派生关系的表达与 Dataset 选择

表达 BS-001 → DNA-001 的样本派生 (父子) 关系**不能使用 RELREC, 而必须使用专用的 RELSPEC (Related Specimens) 数据集** [10]。

RELSPEC 专门用于保留生物样本的谱系和层级关系 (Specimen lineage / hierarchy) [10]。在 RELSPEC 数据集中, 这种关系通过以下三个核心变量表达:

- `SPEC` (Specimen ID, Core = Req): 当前记录所表征的样本标识符 (如 DNA-001) [14,15]
- `PARENT` (Specimen Parent, Core = Exp): 记录产生该样本的直接父样本标识符 (如 BS-001) [14,15]
- `LEVEL` (Specimen Level, Core = Req): 记录样本的代际层级 (例如, 原始采集的现场血样 LEVEL = 1, 直接提取的 DNA 子样本 LEVEL = 2 等) [14,15]

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| (a) 采血/运输/提取 → BE | BE 域 (BECAT/BETERM 三类) | BE 域, BETERM = Collecting/Shipping/Extracting | ⚠️ PARTIAL (用 BETERM 而非 BECAT, 但都是 BE 域且明确区分三类事件; KB BE/spec.md BETERM 接受动名词形式) |
| (b) 体积/RIN → BS, BSTESTCD=VOLUME/RIN | BS, VOLUME, RIN, codelist C124300 | BS, BSTESTCD=VOLUME/RIN, BSTEST=Volume/RNA Integrity Number, C124300 ✓ | ✅ |
| (c) RELSPEC (not RELREC) | RELSPEC | RELSPEC + SPEC/PARENT/LEVEL 三件套明确说明 | ✅ |
| 不混 BS 和 BE | Findings vs Events | 体积/RIN 明确归 BS, 事件归 BE | ✅ |
| 不用 RELREC 记 specimen | RELSPEC 而非 RELREC | "不能使用 RELREC, 必须使用 RELSPEC" 明文 | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 4/5 项完全命中, 1 项 PARTIAL (BETERM vs BECAT 是 BE 域内字段差异, 不影响域归属判断). 加分: 完整 RELSPEC 三件套 (SPEC/PARENT/LEVEL), C124300/C124299 codelist, LEVEL 1→2 代际层级解释。无任何 FAIL 触发 (未把 BS 测量记在 BE, 未用 RELREC, Topic 值正确)。
