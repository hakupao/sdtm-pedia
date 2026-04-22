# ChatGPT GPTs — Q11 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q11)
> **执行时间**: 2026-04-22 晚 (之前 session 已跑)
> **执行者**: Bojiang + cowork (先前 thread)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83e5c-c2e4-83a5-a12c-3b545c698994
> **会话标题**: "Dataset-JSON vs SAS XPT"
> **system_prompt**: v2 (7568 bytes, N5.2 lock)
> **题类**: Q11 — Dataset-JSON v1.1 vs XPT v5

---

## 题目原文

2025 年 FDA 启动 Dataset-JSON 试点, CDISC 发布 Dataset-JSON v1.1. 请说明: (a) Dataset-JSON 相比 SAS XPT v5 主要解决什么 4-5 个**技术痛点**? (b) 2026 年现状: FDA 接受哪个? (c) 作为 SDTM 工程师, 现在实操建议是什么 (开发环境 / 归档 / 提交)? (d) Define-XML 和 Dataset-JSON 互补关系是什么?

---

## 发送给模型的 prompt

同上

---

## 模型 raw 回答 (DOM readback)

(双 preface message 展现 knowledge base 核对 + knowledge cutoff 标注)

> "我先核对你上传的 SDTM 资料里有没有 Dataset-JSON / FDA pilot 的直接依据；如果没有，我会明确区分'库内可证实内容'和'基于截至 2025-08 的一般知识判断'."
>
> "我已经确认：你上传的 SDTM 库能很好支撑 XPT 限制、Define-XML 元数据职责这些点；但 FDA 在 2026 年'正式接受哪个格式'属于时效性问题，库里没有直接答案."

### (a) Dataset-JSON 相比 SAS XPT v5, 主要解决的 4-5 个技术痛点

1. **解除老旧 transport 格式带来的长度/命名约束**: --TEST 常被限制到 40 字符; 超过 200 字符文本不能放一个变量里, 只能拆到 SUPP--; --TESTCD / QNAM 之类短名受 8 字符思维影响. Dataset-JSON 的核心价值之一, 就是把"数据交换载体"从这种老旧二进制 transport 约束里解放出来.
2. **改善长文本表达**: SDTMIG 明说因 SAS V5 transport 超过 200 字符拆到 SUPP--, 这是载体格式逼迫拆分, 非业务需要. JSON 作为文本序列化格式更适合承载长字符串.
3. **降低大文件、低效率问题**: SDTMIG 明确提到超大 transport 文件已成监管处理问题, 主因 sponsor 把字符变量一律开到 200. Dataset-JSON 目标之一是避免 XPT padding/固定宽度思维.
4. **减少对 SAS 专有历史实现细节的依赖**: XPT v5 本质是老 SAS 传输格式, 对非 SAS 工具链带"兼容遗产". Dataset-JSON 更接近现代通用数据交换方式, 被 Python/R/Java/云平台直接消费.
5. **让数据序列化和元数据分工更清晰**: XPT 体系下解释性信息必须额外放 Define-XML 或 reviewer guide (被截断长标签/origin/CT/natural key). Dataset-JSON 不替代元数据标准, 把"数据承载"做得更自然; 元数据继续由 Define-XML 承担.

### (b) 2026 年现状: FDA 接受哪个?

**库里证实**: SDTMIG 仍围绕 .xpt / SAS V5 transport / Define-XML 提交要求.

**截至 2025-08 的最佳判断 (未实时核验)**:
- FDA 正式生产接受主格式仍是 **SAS XPT v5**;
- Dataset-JSON 属于试点/过渡性接受, 不应视为已全面替代;
- 到 2026 年最安全答案: **正式主交付 = XPT + Define-XML; Dataset-JSON = 试点/沟通场景可并行**

### (c) 作为 SDTM 程师实操建议

1. **开发环境**: 双轨 — 内部主表示 = dataframe / parquet / dataset-json-ready; 对外监管交付 = 稳定生成 *.xpt
2. **归档 3 层**: canonical tabulation source (标准化中间层) + submission render (XPT) + metadata package (Define-XML + aCRF + cSDRG + 验证报告). Dataset-JSON 可作内部/回归/试点副本, 但不做唯一归档制品
3. **提交**: 正式 = XPT; 元数据 = Define-XML 必备; Dataset-JSON 仅在试点/获准场景并行
4. **验证 (独到)**: 立即做 XPT/Dataset-JSON 一致性回归 (row count / 主键 / null pattern / CT 值 / sort / Define-XML 指向 variable/origin/value-level metadata), 监管接受范围扩大时切换成本低
5. "现在不要等 FDA 完全切换后再准备; 内部就支持 Dataset-JSON, 但外部正式交付仍以 XPT 为准"

### (d) Define-XML 和 Dataset-JSON 互补关系

- **Define-XML 是"说明书 / 元数据合同"**: 描述 submitted dataset / 结构 / purpose / location / key / CT / origin / value-level metadata
- **Dataset-JSON 是"数据载体 / 数据包"**: 承载行、列、值, 把 XPT 历史格式问题降下来; 不等于完整监管元数据说明
- **关系**: 不是替代, 是分工. Define-XML 告诉审评者"这些数据是什么/怎么来/怎么解释/键是什么/CT 是什么/derived vs assigned vs CRF collected"; Dataset-JSON 把"数据本身"送过去.
- **准确表述**: **Define-XML 解决"语义与监管可解释性", Dataset-JSON 解决"数据序列化与技术承载效率"**

### 结论先行 + 源溯源

(a) XPT v5 历史技术债: 长度/命名限制 + 长文本拆分 + 文件低效 + 现代工具链兼容差 + 过度依赖 SAS transport
(b) 截至 2025-08: FDA 主接受仍 XPT; Dataset-JSON 试点过渡接受, 不默认完全替代
(c) SDTM 程师: 内部现代化 + 外部 XPT 交付 + 并行 Dataset-JSON + Define-XML 权威元数据
(d) Define-XML ⊕ Dataset-JSON 互补非互斥

**源溯源**:
- Define-XML 随 submission 描述 dataset/keys: `knowledge_base/chapters/ch03_submitting_data.md`
- XPT/SAS V5 长度/长文本/文件体积限制: `knowledge_base/chapters/ch04_general_assumptions.md`, `SDTMIG34_02_Assumptions.md`
- Define-XML 承担 origin / CT / value-level metadata: `knowledge_base/chapters/ch04_general_assumptions.md`

**Citation 数**: 3 inline source comments + 多 SDTMIG 引文

---

## Self-score verdict

- **Verdict**: **PASS+ 最强** (5/5 痛点 + 诚实 knowledge cutoff + 源溯源 + 独到验证建议)
- **对照 PASS 判据**:
  - (a) ✓ **5/5 痛点**: 长度命名约束 + 长文本 + 存储低效 + SAS 依赖 + metadata 分工 (判据 4/5 任 4 → 超标)
  - (b) ✓ FDA 主接受 = XPT; Dataset-JSON 试点过渡. **诚实标注 "截至 2025-08, 未实时核验"** (anti-hallucination 锚点生效)
  - (c) ✓ 双轨 + 3 层归档 + XPT 提交 + Dataset-JSON 试点并行 + **独到 XPT/JSON 一致性回归验证建议**
  - (d) ✓ Define-XML = 说明书/元数据合同 / Dataset-JSON = 数据载体/数据包 / 不替代是分工 / 语义 vs 序列化二维
- **触发 FAIL 判据?** 无
- **加分**:
  - **anti-hallucination 锚点生效**: 先 "我先核对库" → "库里没有 FDA 2026 直接答案" 两 preface message, 把"库内可证实"和"知识截止 2025-08 判断"严格分层
  - **独到**: XPT/JSON 一致性回归验证建议 (row count / 主键 / null pattern / CT / sort / Define-XML ref), 判据未列但工程价值高
  - **源溯源 3 条 inline** (ch03 / ch04 / SDTMIG34_02)
- **F-* carry-over 观察**:
  - ChatGPT v2 system prompt v2 在 Q11 supplemental topic 下表现最强 (5/5 痛点 + 诚实 cutoff + bonus 建议)
  - anti-hallucination 分层答法 ("库内可证实 vs 截至 2025-08 最佳判断") 是 ChatGPT 独有优势 (NotebookLM 无 web search 直接 PUNT / Gemini 训练知识答但无声明 / Claude 待测)
