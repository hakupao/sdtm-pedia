# Q12 (D2 — CT 版本锁定 + MedDRA + Define-XML) ChatGPT 专属

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83fdf-5248-83a8-9f9e-20290097d9b5
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 2m 51s

## 完整回答 (要点摘录)

### (a) 3 年期试验锁哪个 CT 版本

**SDTMIG v3.4 没有规定"必须用开组时 CT 或 DBL 当季最新 CT"**. 它要求的是: 在 Define-XML 里提交本研究采用的 CT (或其引用), 并把本研究的 permissible value set 写清楚.

**真正被"锁定"的是提交包里的 study-specific CT snapshot**, 而不是试验开始日期本身.

实践上: 3 年期研究通常会在 **final SDTM / DBL / submission cut** 选定**一个版本并全研究一致使用**, 而不是最终包里混用多个季度的 release.

依据: SDTMIG 关于 CT 单独季度发布、需频繁查看网站, 以及 Define-XML 必须包含研究所用 CT/引用的说明.

### (b) 锁定机制 — Define-XML external codelist

对**外部字典 (如 MedDRA)**: SDTMIG 明确说要用 Define-XML **external codelist element / attributes** 提供字典名称和版本.

对 **CT**: 一般要在 Define-XML 中包含 controlled terminology 或其 reference, 并列出本研究允许值集合.

**诚实约束**: 模型说"SDTMIG 给到的表述是 'external codelist element' / 'external codelist attributes', 但没有展开到具体 XML attribute 名称; 那个精确字段名属于 **Define-XML 规范本身**, 而不是 SDTMIG 文本." (没瞎编 attribute 名).

### (c) AETERM 用 MedDRA 字典 (重要纠正)

**ChatGPT 主动纠正**: AETERM **不是 MedDRA 编码字段**, AETERM 是 **verbatim (原始报告词)**; MedDRA 影响的是 **AEDECOD / AELLT / AELLTCD / AEPTCD / AEHLT / AEHLGT** 等字典派生字段.

**v25→v27 影响**:
- PT/LLT/SOC 映射可能变化, 进而影响 AEDECOD / AEBODSYS / 层级字段 / 汇总计数 / reviewer 看到的分组
- SDTM 结构合规上, 关键不是"必须 v27", 而是**全研究一致 + Define-XML 准确声明字典名与版本**
- 如 DBL 前决定从 v25 全量重编到 v27, 可以; 但**应全研究统一重编, 并同步更新 metadata / reviewer guide**

### (d) Retire / alias 处理

**诚实约束**: 模型说"上传的 SDTMIG 文本里没有找到逐字规则; 下面是基于 SDTMIG 原则的稳妥处理".

两条可接受治理路径:
1. **冻结旧版本**: 研究一直按某个 CT release / MedDRA version 编码, 提交时继续用这个版本, 在 Define-XML 明确声明
2. **全量重映射到新版本**: 在 DBL 前把全研究重映射到新有效 term / preferred term, 再提交新版本

**禁止**: 不要在同一最终 submission 里混用 old term 和 alias / new preferred term.

**保证**: Define-XML 所声明的版本与数据中实际使用的 term/code 一致.

**优化**: 如某 codelist term 在新 release 已 retire 但不是本研究 planned/permissible value set, 不要放进 Define-XML; SDTMIG 只要求写本研究的 permissible values, 不是把整本 codelist 全搬进去.

**兜底**: 如因历史数据原因必须保留旧 term, 最安全的做法是保留原 study CT version, 不做半途局部替换; 必要时在 **Define comments / cSDRG** 解释.

## 判据对齐

- (a) 单一 CT 版本贯穿全研究 ✓; final SDTM/DBL/submission cut 选版本 ✓; **诚实指出 SDTMIG 不强制"开组 CT vs DBL CT"二选一**, 而是 study-specific CT snapshot 概念 ✓ (高于 PASS 判据)
- (b) Define-XML external codelist element/attributes ✓; **诚实标记精确 attribute 名属 Define-XML spec 不属 SDTMIG** ✓
- (c) **主动纠正 AETERM = verbatim 不是 MedDRA 编码字段** ✓ (PASS 判据原本未要求此纠正); MedDRA 影响 AEDECOD/AELLT/AEPTCD/AEBODSYS/层级 ✓; v25→v27 全研究统一 recode ✓; Define-XML 准确声明字典版本 ✓
- (d) 两路径 (冻结旧版本 / 全量 remap) ✓; 禁止混用 old/new term ✓; Define-XML 声明与数据一致 ✓; **不必把整本 codelist 搬进 Define-XML** (优化建议) ✓; cSDRG 解释 ✓
- bonus: Define comments / cSDRG 兜底解释机制 ✓
- bonus: 主动纠正用户 question 中的概念错误 (AETERM ≠ MedDRA 字段) — 教练员级别指正 ✓

源溯源命中:
- `knowledge_base/chapters/ch01_introduction.md`
- `knowledge_base/chapters/ch04_general_assumptions.md`
- `knowledge_base/domains/AE/spec.md`
- `knowledge_base/domains/AE/assumptions.md`

## 归因

PASS — Pure generalization (KB 0 直接 CT 版本锁定 / Define-XML attribute 名). 4 子问题全完整. **(c) 主动纠正 AETERM verbatim vs AEDECOD 编码字段的概念错误**是非 trivial 加分项, 体现 SDTM 专家级精确度 (普通 LLM 会顺着用户错误前提答). (d) 两路径治理 + cSDRG 兜底有可操作性. 思考时长 2m 51s.
