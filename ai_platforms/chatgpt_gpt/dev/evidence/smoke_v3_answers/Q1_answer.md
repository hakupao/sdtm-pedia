# Q1 (A1 — GF 域) EGFR 基因变异场景

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e82f89-64e8-83a7-b934-24851670bc3d
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 2m 53s

## 完整回答

(thinking phase 略)

**结论**: 这条结果应记录在 **GF (Genomics Findings, 基因组学发现)** 域. GF 专门用于表示基因变异、转录及其相关推断结果, 且可以表示由核酸检测推断出的氨基酸改变; GF 示例里就有用 SNV 记录"预测氨基酸改变"和"预测编码序列改变"的做法.

**为什么是 GF, 不是 LB**: GF 的定义是 "One record per finding per observation per biospecimen per subject", 用于基因组材料相关发现. GF 假设明确说: 它用于 genetic variation, 并且可包含对相关蛋白/氨基酸的后续推断. GF 示例 1 就是肿瘤样本中的 SNV.

### 至少 5 个 Core=Req 变量

| 变量 | 角色/Core | 说明 |
|---|---|---|
| GF.GFTESTCD | Topic, Req | 基因测量短名 |
| GF.GFTEST | Synonym Qualifier, Req | 基因测量长名 |
| GF.STUDYID | Identifier, Req | 研究标识 |
| GF.DOMAIN | Identifier, Req | 固定为 GF |
| GF.USUBJID | Identifier, Req | 受试者唯一标识 |

### 3 个 Core=Exp 变量

| 变量 | 角色/Core | 说明 |
|---|---|---|
| GF.GFORRES | Result Qualifier, Exp | 原始结果 |
| GF.GFSTRESC | Result Qualifier, Exp | 标准化字符结果 |
| GF.GFDTC | Timing, Exp | 样本采集日期时间 |
| GF.VISITNUM | Timing, Exp | (常见 bonus) |

### EGFR 变异 GF 建模思路 (拆多条记录)

- 记录 1 (氨基酸): GFTESTCD=SNV, GFTEST="Single Nucleotide Variation", GFTSTDTL="PREDICTED AMINO ACID CHANGE", GFORRES="p.Leu858Arg" 或 "L858R", GFSTRESC=同, GFSYM="EGFR"
- 记录 2 (编码序列): GFTSTDTL="PREDICTED CODING SEQUENCE CHANGE", GFORRES="c...."

### (a) "Exon 19" 位置信息怎么记

**优先放 GF.GFGENSR** (Genetic Sub-Region). 规范举例直接给了 "Exon 15"、"Kinase domain"; "Exon 19" 语义完全一致.

补充: GFGENLOC 是 location within a sequence for the observed value in GFORRES; 在 GF 示例里 GFGENLOC 有时放 "Exon 15" 有时放具体基因组坐标.

### (b) dbSNP ID 怎么引用

**放在 GF.GFPVRID** (Published Variant Identifier). 规范举例明确包含 rs2231142、COSM41596; GF 示例也直接把 rs121913227 放在 GFPVRID. 本题: GFPVRID = rs121913444

### (c) 基因组参考版本 (GRCh38.p13) 存哪

**放在 GF.GFGENREF** (Genome Reference). 规范注释直接举例: "GRCh38.p13". GF 假设说 GFGENREF/GFSEQID/GFPVRID 应尽量反映收集到的粒度 (版本/build/patch/release). 本题: GFGENREF = GRCh38.p13

### (d) 可遗传给下一代走哪个变量

**走 GF.GFINHERTG**. GF 示例 1 (肿瘤组织) 用 SOMATIC; GF 示例 2 (正常外周血 DNA) 用 GERMLINE. 本题: GFINHERTG = GERMLINE

源溯源:
- `<!-- source: knowledge_base/domains/GF/spec.md -->`
- `<!-- source: knowledge_base/domains/GF/assumptions.md -->`
- `<!-- source: knowledge_base/domains/GF/examples.md -->`

## 判据对齐

- 域 GF ✓ (非 LB / 非旧 PF/PGx)
- 5 Req: STUDYID/DOMAIN/USUBJID/GFTESTCD/GFTEST ✓ (handoff 期望可任 5; 未列 GFSEQ 但 5 个 Req 满足要求)
- 3 Exp: GFORRES/GFSTRESC/GFDTC/VISITNUM ✓
- (a) GFGENSR ✓ (+ GFGENLOC 补充)
- (b) GFPVRID = rs121913444 ✓
- (c) GFGENREF = GRCh38.p13 ✓
- (d) GFINHERTG = GERMLINE ✓ (注: handoff 写 GFINHERT, 实际 KB examples.md 用 GFINHERTG; ChatGPT 答 GFINHERTG 是对的, KB anchor 自身不一致)

## 归因

PASS — Pure generalization (04 无 GF 章节). KB 5 文件 spec/assumptions/examples 命中. 思考过程透明 (Reading documents).
