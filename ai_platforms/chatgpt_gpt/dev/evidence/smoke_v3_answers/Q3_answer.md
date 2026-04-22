# Q3 (A3 — BE + BS + RELSPEC) 生物样本采集→运输→DNA 提取场景

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e832ef-db6c-83a9-82b4-d3bf32f06bbb
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 1m 59s

## 完整回答

**结论 (按 SDTMIG v3.4)**:

| 阶段 | 推荐域 | 关键变量 |
|---|---|---|
| 采血 (现场采集 BS-001) | BE | BE.BETERM (Topic), BE.BEREFID=BS-001 |
| 运输 (当天到中心实验室) | BE | BE.BETERM (Topic), BE.BEREFID=BS-001, BECAT=TRANSPORT |
| DNA 提取 (BS-001 派生 DNA-001) | BE | BE.BETERM (Topic), 通常记"提取/制备", BEREFID 记新样本 |
| 血样体积 5 mL | BS | BSTESTCD=VOLUME, BSTEST=Volume |
| RIN=9.2 | BS | BSTESTCD=RIN, BSTEST=RNA Integrity Number |
| BS-001 → DNA-001 派生关系 | RELSPEC | REFID/PARENT/LEVEL |

### (a) 三个"阶段"分别在哪些域

**BE (Biospecimen Events)** 专门放"对样本产生影响的动作/事件", 包括 specimen collection / aliquoting / transportation. 因此采血、运输、DNA 提取**都属于 BE 范畴**.
- BE.BETERM = Topic
- BE.BEREFID = "受该事件影响或由该事件创建的 specimen ID"

**BS (Biospecimen Findings)** 放"关于样本的测量/特征/处理相关 findings", **不是动作本身**.

具体:
- 采血: BE, 例 BETERM=Collecting (示例)
- 运输: BE, 示例 BETERM=Shipping, BECAT=TRANSPORT
- DNA 提取: BE (KB 无 "DNA extraction" 明文行, 但属"affect a specimen"事件, 应 BE 不 BS)

### (b) "体积"和"RIN"记在哪个域, Topic 是什么

两个都是 **BS** findings, **不是 BE 事件**. BS Topic 变量:
- BS.BSTESTCD (Role: Topic, Core: Req)
- BS.BSTEST (Role: Synonym Qualifier, Core: Req)

规范 BSTESTCD/BSTEST 说明里**直接给了例子 VOLUME 和 RIN**.

填值:
- 体积: BSTESTCD=VOLUME, BSTEST=Volume, BSORRES=5, BSORRESU=mL
- RIN: BSTESTCD=RIN, BSTEST=RNA Integrity Number, BSORRES=9.2

**业务诚实纠偏**: RIN 是 RNA 质量指标, 示例里 RIN 对应 BSSPEC=RNA, 不是 DNA. 若场景只是 BS-001 (blood) → DNA-001 (DNA), 则 "RIN=9.2" 测量本身和 DNA-001 不匹配, 应挂在 RNA specimen. 若实际是 DNA 质量指标, 应换 BSTESTCD/BSTEST (不能臆造).

### (c) BS-001 → DNA-001 派生关系: RELREC 还是别的?

**应使用 RELSPEC, 不是 RELREC.**

RELSPEC 是专门的 **Related Specimens** dataset, 用于表示 specimen genealogy / lineage (样本谱系、父子派生关系). 规范明确.

源溯源:
- `<!-- source: knowledge_base/domains/BE/spec.md -->`
- `<!-- source: knowledge_base/domains/BS/spec.md -->`
- `<!-- source: knowledge_base/domains/RELSPEC/spec.md -->` (Related Specimens dataset)

## 判据对齐

- (a) 采血/运输/DNA 提取 = BE ✓ (BECAT=TRANSPORT 命中 KB 明文)
- (b) 体积+RIN = BS ✓; BSTESTCD=VOLUME, BSTESTCD=RIN ✓ (Topic 变量正确, C124300 官方支持)
- (c) RELSPEC 而非 RELREC ✓ (明确区分: RELSPEC=specimen 谱系; RELREC=跨 dataset/记录关系)
- bonus: BEREFID 派生新样本 ID 的角色 ✓
- bonus: RIN 通常对应 RNA specimen 的诚实纠偏 (避免误用) ✓

## 归因

PASS — Pure generalization (04 仅 §1.25 BE+MB 一行). KB 三域 spec 全锚命中. v3.4 PGx 迁入后的 BE/BS/RELSPEC 三件套全部答对. 思考过程透明 (1m 59s 含 RELSPEC vs RELREC 边界核对).
