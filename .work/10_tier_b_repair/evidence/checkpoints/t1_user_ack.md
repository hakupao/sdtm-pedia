# T1.4 用户 ack (2026-11-26)
| # | 问题 | 用户裁定 |
|---|---|---|
| R1 | SDTM v2.0 VERSION_MISMATCH 70 条 | 变量表行 (model/ 已收 5 列精简版, 与 PDF 一致) 认 IE, 缺的 4 列不补; §1 引言 17 条 + TD 句子改 REAL_GAP, 补进 model/01 (TD 句按归属); 其余零散条目按已 ack 先例归类 |
| R2 | 改写丢失短语, 但同节上下文/同表行已有 (R-OPEN-1) | **算 REAL_GAP, 补回原文**. 4 条争议原子维持 REAL_GAP; 此尺度用于 T2 审查 |
| R3 | T2 范围 (全 KB census: 130 表 DIFF / 507 KB 行 / 15 PDF_ONLY 整表缺; 合计 ~856 项) | **全部纳入**; PLAN 成本改 8-10 sessions; 按工作量排批, 首批 B-PCPP |
| R4 | IE 清单 587 条 | 整体 ack; 标签混用由主控统一; 44 条原文逐字在 KB 的 (ch03 xpt 文件名 / spec.md 顶部数据集标题行) 改 PRESENT |
依据: t1_lane_notes.md, t1_ie_candidates.md, t1_census_full.md, t1_batch_draft.md (commit dfa9eee).

## T1.4 补充 (2026-11-26, apply 后)
| # | 问题 | 裁定 | 由谁 |
|---|---|---|---|
| D1 | 59 批 (~177 次调用) vs 合批 | **保持 59 批** (粒度最细, 回滚精确); 成本超 PLAN §7 报警线, 用户知情接受 | 用户 |
| D2 | MB 两份 Ex1-3 / p277 PP 表两份 / AE "…/etc." 扩写 6 项 | **去重 + 删扩写**: MB 留一份按 PDF 逐格修; PP 表留 PDF 所属节, 另一处改一行交叉引用; AE 恢复 PDF 原文. 每处删除记证据 + reviewer 确认 | 用户 |
| D3 | R4 实际转 PRESENT 49 (40+9 同型 xpt) 而非 44; 4 条数据集标题行 (CE/EG/DD/SU) + AE 1 条非逐字 → 留 IE (R4-blocked) | 按 R4 规则本身 ("原文逐字在 KB") 执行, 接受 49/5 | 主控 (规则直接推出) |
| D4 | 标定例 C02 (ig34_p0043_a012) 用另一行补齐缺词, 与 R2 冲突 | 按 R2: C02 不再是 REWRITE_OK 标杆, 该原子改 REAL_GAP; T2 prompts 以 R2 为准 | 主控 (R2 推出) |
| D5 | whitelist 里 sv20_p0004_a016 (§1, 已 IE) | 按 R1 (§1 引言补) 一并补进 model/01 | 主控 (R1 推出) |
| D6 | KB 自写、PDF 无、且不矛盾的解释性内容 (Derivation notes / Example applications / 速查摘要 / Mermaid 图等) | **保留但加标注**: 统一前缀 `> KB note (not in SDTMIG):` (块级内容放在该引用块内); 每条经 reviewer 确认不矛盾. 已提交批 (B-PCPP 的 PP/examples.md KB_AUTHORED 项) 回补标注 → O14 | 用户 (2026-11-26) |
| D7 | ch08 §8 内容与 domains/{RELREC,RELSUB,RELSPEC,SUPPQUAL}/ 重复承载 | **两边都留, 都按 PDF 逐字修对** (D2 例外: 域目录是 INDEX/ROUTING/RAG 入口); 域文件顶部加一行 `> Source text: SDTMIG v3.4 §8.x (also in chapters/ch08_relationships.md).`; 开批 B-REL (RELREC/RELSUB/RELSPEC) + 既有 B-SUPPQUAL 按此执行 | 用户 (2026-11-26) |
