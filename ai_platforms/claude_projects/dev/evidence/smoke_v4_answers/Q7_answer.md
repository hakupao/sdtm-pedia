# Claude Q7 answer — Partial date SDTM/ADaM

**Verdict**: PASS+ (verified)

## 结论
SDTMIG 对 partial date 完全通过 **ISO 8601 truncation** 实现 — SDTM 不做 imputation, **imputation 属 ADaM 级** (ADaM IG *DTF / *TMF 缺失补齐 flag 机制). 原则: "有多少精度记多少, 不猜不补" (§4.4.2).

## 三场景填值

| 场景 | 信息 | 填值 | ISO 8601 机制 |
|---|---|---|---|
| A | AE 2024 年 6 月 (无日) | `2024-06` | 右截断 (§4.4.2 表行 6) |
| B | CM 2024 年 (无月日) | `2024` | 右截断 (§4.4.2 表行 7) |
| C | 完全未知 | **null (空字符串)** | §4.4.2: completely missing → SDTM field should be null |

## 关键语法点 (§4.4.1/§4.4.2)
- Extended format 带分隔符 (-, :, T), 禁 basic format
- 右截断不补 `-` 占位 (2024-06 ✓, 2024-06--- ✗)
- **中间缺失才用单 `-` 占位** (知日不知月 → `2024---15`; 知月日不知年 → `--12-15`)
- 无时间分量时 T 分隔符必须省略
- 区间: `AESTDTC=2024-01-01/2024-06-30` (solidus, §4.4.2)

## 场景 C 补救: Relative Timing

**§4.4.7 Example 3** (AE Unknown outcome) 范本:
```
AESTDTC  = null
AESTRTPT = "BEFORE" 或 "UNKNOWN"   (C66728 codelist)
AESTTPT  = "INFORMED CONSENT" (文本描述锚点)
```
AE 进行中不知结束:
```
AEENDTC  = null
AEENRTPT = "ONGOING" | "UNKNOWN"
AEENTPT  = "DATE OF LAST DOSE"
```

## (d) SDTM --STDTC 是否 imputation
**不需要且不应该**. 原因:
1. §4.4.2 明确: precision 通过 ISO 8601 truncation "inferred from presence or absence of components" — **精度即信息, imputation 会破坏**
2. SDTM 定位 as-collected / faithful representation, imputation 属分析层决策 ("补 15 日 vs 补 01 日" 是 statistical convention 非数据标准)
3. AE assumptions 未要求 imputation, 仅要求 AEENRF / AEENRTPT 补位

## (e) ADaM imputation 时 SDTM 额外记什么

核心原则: **让 ADaM 有足够信息做 imputation, 让 imputation 可追溯**.
1. **忠实保留 partial date** — 不 pre-填默认值 (2024-06 清晰缺日 vs 2024-06-15 猜不出原始/imputed)
2. **补充 relative timing 变量** (若有价值):
   - `--STRF / --ENRF` (C66728: BEFORE / DURING / DURING/AFTER / AFTER / UNKNOWN)
   - `--STRTPT / --ENRTPT` + `--STTPT / --ENTPT` (文本锚点)
   - `--STDY / --ENDY` 通常不推荐 partial 情况填
3. **SUPPQUAL 记缺失原因** (可选): CRF 有"Date Unknown"/"Not Assessed" → SUPP-- 加 QNAM (e.g. AESTDTRC="DATE UNKNOWN PER SUBJECT")
4. **不加自定义 imputed date 列** — SDTM 侧加 AESTDTCIMP 等非标变量违反 v3.4

### ADaM 侧对照 (超 Project 范围, 仅概念)
ADaM IG 定义:
- `ASTDTF / AENDTF` = "Y" (year imputed) / "M" (month imputed) / "D" (day imputed) / null
- `ASTDT` 数值日期变量配合
- 例: SDTM AESTDTC='2024-06' → ADaM ASTDT=2024-06-15, ASTDTF='D' — 互不污染, 可追溯

## 源溯源
- SDTMIG §4.4.1 ISO 8601 格式 → 02_chapters.md (ch04 全文)
- §4.4.2 Date/Time Precision + truncation 表 → 02_chapters.md
- §4.4.7 Relative Timing (Ex 3 AE Unknown) → 02_chapters.md
- AE Timing (AESTDTC/AEENRF/AEENRTPT) → 05_mega_spec.md (AE 行 53-60)
- C66728 → 11a_terminology_high_core.md (Term 值本答未展开)
- **ADaM IG v1.3 §3.1.4** (*DTF/*TMF flag 规则, SDTM Project 外)

## 评分要点
- ✓ 3 场景全对
- ✓ §4.4.2 truncation 表锚点精确
- ✓ Extended format + 占位规则 (中间 vs 右截断)
- ✓ Solidus 区间表达法 (ChatGPT 未提)
- ✓ §4.4.7 Example 3 具体范本 (AESTRTPT="BEFORE"/"UNKNOWN" + AESTTPT)
- ✓ C66728 codelist + 5 值完整
- ✓ (d) 3 个拒绝 imputation 的硬理由
- ✓ (e) 4 条 SDTM-ADaM 接口清单 + SUPPQUAL 选项 + 禁加自定义列警告
- ✓ ADaM ASTDTF/AENDTF 机制 + 具体派生示例 (超范围明确标)
- ✓ 边界自律: ADaM IG 不在 Project, 坦诚引外部 §ref
