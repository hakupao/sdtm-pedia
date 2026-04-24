# ChatGPT GPTs — Q4 LB vs MB vs IS 边界 (V5C post-apply v2.2 LIVE)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q4)
> **执行时间**: 2026-04-24 (V5C regression, post v2.2 apply)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69ead37f-1088-83aa-9567-4a96da090741
> **题类**: Q4 (B1 — LB/MB/IS 三场景选域)
> **System prompt live**: v2.2

## Prompt

同 SMOKE_V4.md §2 Q4 原题 (3 场景 A/B/C + i/ii/iii + 边界规则)

## Raw 回答 (DOM readback, trimmed)

结论：**A = IS，B = IS，C = MB**。关键不是"是否在实验室测"，而是测量对象是免疫反应、一般临床实验室结果，还是非宿主微生物本身/培养识别。

| 场景 | 域 | Topic 变量值示例 | 理由；为什么不是另外两个 |
|---|---|---|---|
| A. baseline IgG 抗麻疹病毒滴度 1:128 | **IS** | ISTESTCD=MBIGSAB; ISTEST=IgG Antibody; ISBDAGNT=MEASLES VIRUS; ISORRES=1:128; ISORRESU=titer | IS 收抗原诱导的体液/细胞免疫反应; v3.4 明确: 针对微生物感染产生的抗体进 IS. 非 MB (结果不是 organism 检出); 非 LB (v3.4 把免疫原性/抗体反应分出) |
| B. ADA 阳性/阴性 + 滴度 | **IS** | 筛查/确认: ISTESTCD=ADA_BAB; ISTEST=Binding Antidrug Antibody; ISTSTOPO=SCREEN/CONFIRM; ISORRES=POSITIVE/NEGATIVE. 滴度: 同 test, ISTSTOPO=QUANTIFY; ISORRES=40; ISORRESU=titer | IS 明确覆盖 biologic/drug/vaccine 等治疗诱导的免疫反应; v3.4 IS example 里 ADA 用 SCREEN/CONFIRM/QUANTIFY 区分. 非 LB (不是常规 lab); 非 MB (无 organism 识别) |
| C. 痰样 Mtb 培养 positive | **MB** | MBTEST=Mycobacterium tuberculosis; MBTSTDTL=DETECTION; MBORRES=POSITIVE; MBSPEC=SPUTUM; MBMETHOD=CULTURE | MB = Microbiology Specimen 非宿主生物识别/检测; target organism, 结果 PRESENT/ABSENT. 非 IS (非宿主反应); 非 LB (lab 定义不含 microbiology) |

### v3.4 边界规则

- **IS**: 宿主免疫反应 — 抗体/ADA/疫苗或感染诱导的体液免疫. ISTESTCD (Topic/Req), ISBDAGNT 表达结合/靶抗原.
- **MB**: 非宿主微生物/抗原识别/检测/培养. MBTESTCD (Topic/Req). 药敏在 MS, 不在 MB.
- **LB**: 一般实验室兜底; microbiology + PK 排除到独立域; 免疫原性抗体反应走 IS.
- **特殊例外**: microbial Ag/Ab combination assay (如 4 代 HIV Ag/Ab) — v3.4 明确放 MB (identification/detection 为主).

**源路径**: `knowledge_base/domains/IS/assumptions.md`, `IS/spec.md`, `MB/assumptions.md`, `LB/assumptions.md`, `IS/examples.md`, `terminology/core/general_part*.md`

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据**:
  - A=IS ✓ (理由精确: v3.4 anti-microbial antibody → IS)
  - B=IS ✓ (ADA 经典免疫原性)
  - C=MB ✓ (Mtb 培养 = 直接检出 organism)
  - v3.4 边界规则: IS 免疫应答 / MB 直接微生物 / LB 常规生化 ✓ 全提
  - 特殊例外 Ag/Ab combo → MB (加分)
- **触发 FAIL?** 无 (A 未答 MB; A 未答 LB; B 未答 LB; C 未答 IS)
- **v5c→v2.2 delta**: 无 regression. 答案深度 (ISBDAGNT + ISTSTOPO SCREEN/CONFIRM/QUANTIFY) 等于或超 N5.2 baseline 水平.
