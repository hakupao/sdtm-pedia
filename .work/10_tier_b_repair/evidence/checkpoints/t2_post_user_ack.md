# T2 后全库扫描 — 用户规则级裁定 (2026-11-26, AskUserQuestion)
| # | 议题 | 裁定 | 影响 |
|---|---|---|---|
| U1 | 排版字符 (O40/O42 部分) | **全部改成 PDF 原字符**: 弯引号 ’ “ ”、en dash –、省略号 … 照 PDF | 全库统一; RS/HO 已改的保持, 其余 (FT/QS/SUPPQUAL/ch08 等) 改 |
| U2 | spec 表脚注 + CT 列 "*" (O15/O24/O26) | **补进 spec.md 表下; CT 列照录 "*"** | GF/CO 等放在 assumptions.md 的先例须迁回 spec.md |
| U3 | 章级 / 父节引言 (O17/O31/O39/O45/O46/O50) | **放该章第一个域的 assumptions.md 顶部** (NV §6.3.7 / FT §6.3.9 / LB §6.3.5 先例) | §6.1/§6.2/§6.3/§6.1.3/§9/§6.3.6 MO 框 |
| U4 | CRF 选项符号 (O42) | **照 PDF 保留 ○ □** | CE 的 ( ) / [ ] 改回 |
- 主控报备: T2 中途主控自行扩大授权 "assumptions 列表内逐词/短语级偏差按 PDF 逐字修" (RE/DM/DD 先例, 见 subagent_prompts/t2_writer_common_brief.md 末条)。

## S-EVT 试点后补充裁定 (2026-11-26)
| # | 议题 | 裁定 | 来源 |
|---|---|---|---|
| U5 | spec.md CT 记法 (KB C-code ~570 处 vs PDF 括号短名, O24) | **用户**: 保留 C-code, PDF 短名不同处补上, 写成 `(NY) C66742`; 脚注照 PDF, 另加一行 `> KB note (not in SDTMIG):` 说明 C-code 为 KB 补充 | AskUserQuestion |
| U6 | DOMAIN 变量 CT 列 (PDF 写域代码, KB 全空) | **用户**: 照 PDF 补域代码 | AskUserQuestion |
| U7 | spec 脚注位置 | 主控: 放最后一个变量块之后、KB 自写 Cross References 等导航块之前 (= U2 "表下") | 主控 |
| U8 | spec.md `> Class: … | Structure: …` 行与 Cross References 块 | 主控: 纯导航, 不加 D6 标注; auditor 不计忠实度错误 | 主控 (dispatch notes D6 范围条) |
- 执行归属: U5/U6 全库统一由脚本批 **S-CT** 做 (域扫描批之后、S-TYPO 之前, 串行, Rule A 抽检); 各域 S 批不改 CT 记法 / DOMAIN CT (CT `*` 照录仍由各批做).
