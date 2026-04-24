# Gemini Gems — Q4 LB vs MB vs IS 边界 (V5C post-apply v7 LIVE)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q4)
> **执行时间**: 2026-04-24 (V5C regression, post v7 apply)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/353e542155f1eb97
> **题类**: Q4 (B1 — LB/MB/IS 三场景选域)
> **System prompt live**: v7

## Prompt

同 SMOKE_V4.md §2 Q4 原题

## Raw 回答 (DOM readback, trimmed — 04 scenario 片段省略, 保留答案主体)

### 场景 A: 抗麻疹病毒 IgG 滴度 baseline

- (i) **IS** (Immunogenicity Specimen Assessments)
- (ii) IS 专门记录抗原(疫苗/蛋白/微生物)引发的**免疫反应**. 排除 LB: v3.4 体系下免疫原性检测优先 IS. 排除 MB: MB 测微生物本身, 本题测宿主抗体反应.
- (iii) ISTESTCD="MSLIGG"; ISTEST="Measles Virus IgG Antibody"; ISORRES="1:128"
- 依据: IS Assumptions §2 "与微生物感染产生的抗体相关的评估也将呈现在 IS 域中"

### 场景 B: ADA 阳性/阴性 + 滴度

- (i) **IS**
- (ii) 典型免疫原性评估; 受试者对外源治疗药物(mAb)的免疫反应. 非 LB (不是常规生化); 非 MB (无微生物)
- (iii) ISTESTCD="ADATIT"; ISTEST="Anti-Drug Antibody Titer"; ISORRES="1:100" 或 "POSITIVE"
- 依据: IS Assumptions §1

### 场景 C: Mtb 培养 positive

- (i) **MB** (Microbiology Specimen)
- (ii) 培养法 = 微生物鉴定/检测. 非 LB (LB 不处理微生物培养); 非 IS (IS 关注宿主反应, 本题关注病原体实体)
- (iii) MBTESTCD="CULT"; MBTEST="Culture for Microorganism"; MBORRES="POSITIVE"; MBSPEC="SPUTUM"
- 依据: MB 域定义 + IS Assumptions §5 (若检测目的是微生物鉴定, 通常归 MB)

### SDTMIG v3.4 边界规则汇总

1. **宿主 vs 病原体**:
   - 宿主反应 (抗体/滴度/T 细胞) → IS
   - 病原体存在 (PCR/抗原/培养/镜检) → MB
2. **鉴定 vs 表征**:
   - "有没有这个菌/毒" (HIV 筛查/流感快检) → MB
   - 免疫反应强度/持久性/性质 → IS
3. **例外**: 微生物 Ag/Ab 组合检测 (4 代 HIV Ag/Ab) → MB (IS Assumptions §5)
4. 常规生化/血液学 → LB
5. 流式细胞术免疫评估 (CD4+ 计数) → **CP** 域 (非 IS)

**源路径**: `knowledge_base/domains/IS/assumptions.md` §1/§2/§5, `MB/spec.md`, `LB/spec.md`

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据**:
  - A=IS ✓
  - B=IS ✓
  - C=MB ✓
  - 边界规则 3 条齐全 (Host vs Pathogen / Identification vs Characterization / Ag-Ab 例外) ✓
  - 额外: CP 流式例外 (加分)
- **触发 FAIL?** 无
- **v5c→v7 delta**: 无 regression. 答案结构含 IS Assumptions 条目引用, N5.2 baseline 保持. 
- **Observation**: Raw readback 含 04 业务场景文件片段 (§1.15d DS / §1.15e TA-TE-TV / §1.15 CT / §1.20 DV / §1.23 SV / §1.25 BE/MB/MS) 在主回答前冗余输出, 看似 Gem retrieval 机制泄漏. 不影响主答案 verdict, carry-over LOW.
