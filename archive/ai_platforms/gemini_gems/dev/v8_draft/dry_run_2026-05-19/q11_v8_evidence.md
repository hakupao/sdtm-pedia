# Q11 — Gemini v8.1 dry-run evidence

> 日期: 2026-05-19 16:38-16:39 PM
> Mode: Gemini 3.1 Pro
> Prompt: v8.1

## 题文

> 2025 年 FDA 启动 Dataset-JSON 试点, CDISC 发布 Dataset-JSON v1.1. 请说明: (a) Dataset-JSON 相比 SAS XPT v5 主要解决什么 4-5 个**技术痛点**? (b) 2026 年现状: FDA 接受哪个? (c) 作为 SDTM 程师, 现在实操建议是什么 (开发环境 / 归档 / 提交)? (d) Define-XML 和 Dataset-JSON 互补关系是什么?

## Verdict 矩阵

| 维度 | R3 v7.1 | v8.1 dry-run | Delta |
|---|:---:|:---:|---|
| Verdict | **FAIL** (跑题答 AE/CM) | **PASS+** ✓ | ⬆ 修复 |
| Response len | 1436 chars (off-topic) | **3768 chars** | 2.6× 深 |
| Total ms | — | 30,584 | 快 |
| (a) XPT 痛点 (4-5) | ❌ 不沾 (答 SDTM domain) | ✅ **5 痛点全列**: 8-char / 200-char (label 40-char) / Unicode / Blank padding (sparse) / Long text truncation (SUPP--) / Metadata Integration | PASS 标准 4-5 中 4+, 此 5+1 |
| (b) FDA 现状 | ❌ | ✅ XPT v5 仍 required, Dataset-JSON 试点 evaluation, NDA/BLA 必须 XPT, Pre-NDA 会议可豁免 | 完整 |
| (c) 实操 (dev/archive/submit) | ❌ | ✅ Dev: Python/Pandas + JSON 优势 / Archive: 主版本备份 + 元数据自解释 / Submit: 双轨 + 转 XPT + Pinnacle 21 验证 | 完整三段 |
| (d) Define-XML 互补 | ❌ | ✅ ASCII 图 + OID 引用关系 + "不替代关系" 明示 | 加分 |
| Off-topic AE/CM | YES 1436 chars | NO (zero AE/CM 主体讨论) | 完全修复 |

## Prong 验证

**Prong 2 (CO-2f 文件格式 ground rule)**: ✅ **完全 fire**.
- 关键词 "Dataset-JSON" / "XPT" / "Define-XML" / "FDA 试点" 触发 CDISC 格式 spec 锚
- 切断了 v7.1 R3 时 AE/CM SDTM domain content 替换 fallback path

**Reviewer fix H2 (CO-2f 优先 gate)**: ✅ 实测有效
- 题文有 "JSON" / "XML" / "FDA" 等可能触发 CO-5 regex 的 SDTM-shaped strings, 但 v8.1 优先 gate 让 CO-2f 优先, AHP-V1 路径未误触
- response 没有 "JSON 非 v3.4 standard variable" 类幻觉 (这是 v8.0 草案的 H2 风险点)

## 关键 response 片段

```
(a) Dataset-JSON 相比 SAS XPT v5 解决的核心技术痛点
SAS XPT v5 基于 1988 年的传统规范.

1. 摆脱严格字符长度限制
   - XPT: 变量名 8-char / 标签 40-char (含 "AEACNOTH" 类晦涩缩写)
   - JSON: 解除物理限制
2. 原生支持 Unicode/UTF-8
   - XPT: 不支持, 仅 ASCII/EBCDIC
   - JSON: UTF-8 兼容多语言
3. 消除无效空格填充 (Blank Padding)
   - XPT: 固定列宽, sparse dataset 浪费空间
   - JSON: Key-Value 非固定宽度
4. 长文本拆分痛苦
   - XPT: >200 字符必须切到 SUPP--
   - JSON: 层次化无缝容纳
5. Metadata Integration
   - XPT: 扁平 flat file, 依赖外部 Define-XML
   - JSON: 内嵌 metadata blocks 自解释

(b) 2026 现状: XPT v5 仍是 FDA NDA/BLA required, 
    Dataset-JSON 在 evaluation 试点中, Pre-NDA 会议可获书面豁免

(c) 实操:
- Dev: Python/Pandas + JSON 优势 (免乱码/截断/SUPP--)
- Archive: JSON 作主版本备份, 自解释降低 long-term preservation 风险
- Submit: 双轨, JSON 主开发 → 工具自动降级 XPT → Pinnacle 21 验证

(d) Define-XML 与 Dataset-JSON 互补 (不替代):
[ Define-XML v2.1 ]
  ├── 职责：技术蓝图 (Schema)
  └── 自然键, CT 编码, 变量顺序, 衍生算法
        ▼ 互补验证
[ Dataset-JSON v1.1 ]
  ├── 职责：行级记录 (Tabulation Records)
  └── Metadata Block + Data Records (引用 Define-XML OID)

来源: CDISC Dataset-JSON v1.1 Specification / SDTMIG v3.4 ch03 §3.2
```
