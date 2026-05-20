---
lang: zh
slug: glossary
order: 40
title: "术语表"
---

# 术语表

本页只解释使用 SDTM Pedia 时最常遇到的临床数据标准术语。平台配置、文件上传和内部验证术语不放在这里，避免影响普通用户阅读。

| 术语 | 中文说明 | 使用提示 |
| --- | --- | --- |
| CDISC | 临床数据交换标准协会。发布 SDTM、ADaM、CDASH 等临床研究数据标准。 | 正式解释应以 CDISC 官方出版物为准。 |
| SDTM | Study Data Tabulation Model，临床研究数据制表模型。 | 用于规定提交用临床研究数据如何组织。 |
| SDTMIG | SDTM Implementation Guide，SDTM 实施指南。 | 说明各域、变量和实现规则。 |
| Domain | 域。SDTM 按主题组织数据，例如 AE、DM、LB、CM。 | 可以理解为标准化数据表。 |
| Variable | 变量。域中的标准字段，例如 AESER、LBTESTCD、CMTRT。 | 查询变量时建议保留英文变量名。 |
| Core | 变量使用属性，常见为 Required、Expected、Permissible。 | 用于判断变量在数据集中应如何出现。 |
| Controlled Terminology | 受控术语。CDISC/NCI 维护的标准取值集合。 | 常用于限制 submission value。 |
| Codelist | 受控术语列表，例如 NY、AESEV、LBNRIND。 | 查询时可同时问 C-code 和 submission values。 |
| C-code | NCI EVS 中的术语或 codelist 编码。 | 便于与官方术语来源核对。 |
| Submission Value | 提交值。数据集中实际使用的标准取值。 | 例如 NY codelist 中的 Y、N、U、NA。 |
| MedDRA | 医学监管活动词典，常用于不良事件编码。 | AEDECOD、AELLT、AEHLT 等变量与 MedDRA 相关。 |
| SUPPQUAL / SUPP-- | 补充限定符机制，用于表达标准域中没有主变量承载的补充信息。 | 并非所有域或场景都适用，应结合 SDTMIG 规则判断。 |
| RELREC | 相关记录关系表，用于表达不同域记录之间的关系。 | 常用于跨域关联说明。 |
| Trial Design | 试验设计相关域，例如 TA、TE、TV、TI、TS。 | 与 subject-level 事件或发现类数据不同。 |
| ISO 8601 | 日期和时间表达标准。 | SDTM 中的 --DTC 变量通常使用此类格式。 |
| Define-XML | 临床研究数据提交中的元数据交换格式。 | 用于说明数据集、变量、术语和来源等元数据。 |

## 阅读建议

如果回答中出现你不熟悉的变量、域名或 C-code，优先让 SDTM Pedia 解释该术语，再回到原问题继续追问。对于正式交付，请把术语解释与 CDISC 官方资料进行核对。
