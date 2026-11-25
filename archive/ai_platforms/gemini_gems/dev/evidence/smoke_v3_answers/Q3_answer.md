# Q3 — Gemini SDTM Expert 回答 (A3 — BE + BS + RELSPEC)

> 期望核心: 采血行为=BE BECAT="COLLECTION" + 采血测量(VOLUME/RIN)=BS BSTESTCD (C124300) + RELSPEC 表达派生. v3.4 映射:
>   - **BE** = Biospecimen **Events** (采集/运输/提取)
>   - **BS** = Biospecimen **Findings** (体积/RIN 测量)
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/aef7cbfb6150487e
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

这是一个典型的 Biospecimen (生物样本) 业务场景。根据 SDTMIG v3.4 的规定，涉及生物样本的采集、流转、处理及测量，主要分布在 **BS (Biospecimen Events)** 和 **BM (Biospecimen Findings)** 两个域，而样本间的衍生关系则由 **RELSPEC** 域承载。

### (a) 三个"阶段"的归属域

这三个阶段描述的都是对样本的操作过程（Events），应记录在 **BS** 域。

| 阶段 | 域 | 建议变量映射 (BSTERM) | 说明 |
|------|----|----------|------|
| 采血 | BS | BLOOD COLLECTION | 记录样本 BS-001 被采集的时间、地点、状态等 |
| 运输 | BS | SAMPLE SHIPMENT / RECEIPT | 记录样本在站点与中心实验室间的流转事件 |
| DNA 提取 | BS | DNA EXTRACTION | 记录对 BS-001 进行处理并产生 DNA-001 的过程 |

### (b) 体积与 RIN 值的记录

对样本本身的属性测量属于 Findings 类数据，应记录在 **BM** 域。

- **体积 (Volume = 5 mL)**:
  - 域: BM
  - Topic 变量 (BMTEST): Volume
  - 结果变量: BMORRES="5", BMORRESU="mL"
- **RNA 完整性数 (RIN = 9.2)**:
  - 域: BM
  - Topic 变量 (BMTEST): RNA Integrity Number
  - 结果变量: BMORRES="9.2"

### (c) BS-001 → DNA-001 的派生关系表达

这种"父子样本"（Parent-Child）的衍生关系不建议使用 RELREC，而应使用专门为生物样本设计的 **RELSPEC** 域。

- 使用 Dataset: **RELSPEC (Related Specimens)**
- 表达方式:
  - 通过 IDVAR="BSID" 或 IDVAR="BSREFID" 来关联样本标识。
  - 使用 RELTYPE 变量说明关系类型（如 PARENT 或 DERIVED）。
- 为什么不用 RELREC: RELREC 通常用于不同域记录之间的逻辑关联（如 AE 与 LB 的关联）。对于样本的物理演变过程，RELSPEC 提供了更结构化的变量（如 RSPECID, PSPECID 等，视具体 Model 版本而定）来追踪样本链条。

### 源路径
- `knowledge_base/domains/BS/spec.md`
- `knowledge_base/domains/BM/spec.md`
- `knowledge_base/chapters/ch06_special_topics.md` (关于 Biospecimen 关系的处理)
- `04_business_scenarios_and_cross_domain.md §10` (Biospecimen 跨域机制)

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| (a) 采血行为归 BE | BE BECAT="COLLECTION" + 运输 BE BETERM="TRANSPORT" + 提取 BE "PREPARATION" | 3 阶段都归 **"BS" (Biospecimen Events)** — BS/BE 命名**倒置** | ❌ |
| (b) 测量域 | BS (Biospecimen Findings) + BSTESTCD="VOLUME"/"RIN" (C124300) | 答 **BM** 域 + BMTEST (**臆造 BM**, v3.4 无此域) | ❌ |
| (c) 派生关系 | RELSPEC + 不用 RELREC | RELSPEC + 不用 RELREC | ✅ |

## Verdict

**FAIL** — Gemini 把 BE (Biospecimen **Events**) 和 BS (Biospecimen **Findings**) 两个 v3.4 新域**命名彻底倒置**: 实际称 "BS" = Biospecimen Events (错, BS 是 Findings), 称 "BM" = Biospecimen Findings (臆造, v3.4 无此域). 采血/运输/提取 3 事件应在 BE, 但被全部归到 "BS"; 体积/RIN 应在 BS BSTESTCD, 但被归到臆造的 "BM" 域. 触 FAIL 判据 "把 BS 和 BE 混淆 (Findings vs Events)" + "Topic 变量用 VOL/RNAINT" (扩展: BMTEST 域+变量都是臆造). 只有 (c) RELSPEC 正确. 典型 v3.4 新域 generalization 失败.

- 04 引用: 1 次 ("04_business_scenarios_and_cross_domain.md §10 Biospecimen 跨域机制"), 属 04 业务弹药包直接命中 (但 04 是指引业务不是变量层 spec, 即使命中 04 也未救回 BE/BS 本身的倒置)
- CO-2 触发: 无 (但确实说 "请查询 NCI EVS Browser 确认最新的 BMTEST 术语" — 对 臆造域 BMTEST 做 CT 字典查询建议是逻辑缺陷)
- Score: 0 / 1
