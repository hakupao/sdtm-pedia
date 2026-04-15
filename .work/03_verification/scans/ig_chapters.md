# Step 3.6 图像扫描：SDTMIG v3.4 通用章节 (p.1-59)

## 扫描范围

- 批次 1：p.1-20
- 批次 2：p.21-40
- 批次 3：p.41-59

---

## 扫描结果

| 序号 | 页码 | 所属章节 | 图像类型 | 简要描述 |
|------|------|----------|----------|----------|
| 1 | 1 | 封面 | Logo / 封面装饰图 | CDISC 彩色圆点 Logo，置于文档标题上方 |
| 2 | 15 | 2.6 Creating a New Domain | 关系/层次图 | "Figure. Creating a New Domain"：方框与箭头组成的层次图，展示 Identifier Variables、Timing Variables、Topic and Qualifier Variables（含 Interventions-/Events-/Findings-Specific Variables）如何组合构成 New Domain，使用 AND / OR 逻辑连接符 |
| 3 | 31 | 4.2.7.1 "Specify" Values for Non-result Qualifier Variables | CRF 模拟图 | 两个 CRF 模拟框：① "Reason for Dose Adjustment (EXADJ)" 复选框列表（含 Adverse Event、Insufficient Response、Non-medical Reason）；② "Indication for analgesic" 选项框（含 Post-operative pain、Headache、Menstrual pain 等及 Other specify 空白行），用于说明 CRF 自由文本提交场景 |
| 4 | 32 | 4.2.7.2 "Specify" Values for Result Qualifier Variables | CRF 模拟图 | "Eye Color" CRF 模拟框，列出 Brown、Black、Blue、Green、Other specify 选项，用于说明结果限定变量的 Specify 提交方式 |
| 5 | 33 | 4.2.7.3 "Specify" Values for Topic Variables | CRF 模拟图 | "Indicate which of the following concomitant medications was used to treat the subject's headaches" CRF 模拟框，列出 Acetaminophen、Aspirin、Ibuprofen、Naproxen、Other specify 选项，说明 Interventions 主题变量的自由文本处理 |
| 6 | 34 | 4.2.7.4 "Specify" Values for --OBJ | 决策树 | "Figure. Decision Tree for Populating --OBJ"：多分支流程决策树，包含菱形判断节点（Topic variable coded? / Parent record exists? / Name of event or intervention coded?）和矩形动作节点（Populate --OBJ with --DECOD / topic variable value / coded value / verbatim value），箭头标注 Yes/No 路径 |
| 7 | 44 | 4.4.7 Use of Relative Timing Variables（--STRTPT/--STTPT/--ENRTPT/--ENTPT 示例） | 时间轴 | "Figure. Example of --ENRTPT and --ENTPT for Medical History"：水平时间轴，标注 2002 年事件起点（黄色框）和 2006-11-02 参考时间点（MHENTPT，黄色框），配有说明框描述 MHDTC、MHSTDTC、MHENRTPT、MHENTPT 变量值，展示医学史条目的相对时间表示 |
| 8 | 46 | 4.4.10 Representing Time Points | 时间轴 / 架构图 | "Figure. Representing Time Points"：水平时间轴，标注 Reference Time Point（含 --TPTREF、--RFTDTC）、Planned Elapsed Time（--ELTM）、Collection Time Point（含 --TPT、--TPTNUM、--DTC）三个关键概念及其关系，使用箭头和方框说明时间点变量结构 |
| 9 | 51 | 4.5.1.1 Original and Standardized Results | 流程图 | "Figure. Original to Standardized Results"：三框线性流程箭头图，展示 --ORRES（All original values）→ --STRESC（Derive or copy all results）→ --STRESN（Numeric results only）的转换关系 |

---

## 批次摘要

- **p.1-20**：发现 2 处视觉内容（p.1 封面 Logo，p.15 新建域层次图）
- **p.21-40**：发现 4 处视觉内容（p.31、p.32、p.33 CRF 模拟框，p.34 决策树）
- **p.41-59**：发现 3 处视觉内容（p.44 时间轴，p.46 时间点架构图，p.51 流程图）

**合计：9 处图像**
