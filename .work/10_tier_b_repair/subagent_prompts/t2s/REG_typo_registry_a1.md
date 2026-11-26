任务: 建 PDF_TYPO / T-n 登记总表 + T4 用户裁定汇总 (O25)。只读 KB, 不改 KB。角色: writer (汇总)。
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。
来源: `.work/10_tier_b_repair/evidence/checkpoints/t2_B-*.md` 与 `t2_S-*.md` (含 _review / _audit 中对 T-n 的更正), `work/out_of_scope_findings.md` (O1-O61), `work/t1_errata.json`, `evidence/checkpoints/t2_post_user_ack.md`。
产出:
1. `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` — 每条 PDF_TYPO / T-n / U-n (照录或 KB 写正确值) 一行: {batch, id (如 "B-EX T-5"), kb_file, kb_line_now (按当前 HEAD 用内容重新定位), kb_text_span (KB 中该处的精确字符片段, 供 S-TYPO 作 do-not-touch 匹配), pdf_page, pdf_value, kb_value, handling ("KB 写正确值" | "照录+T4"), basis (≤25 词)}。每条必须在当前 KB 中定位到; 定位不到的单列 (可能已被后续批改写)。
2. `.work/10_tier_b_repair/evidence/checkpoints/t4_user_decisions.md` — T4 用户裁定汇总表 (O25): 所有 "照录+T4" 项与各 checkpoint "交 T4 / 用户裁" 项 (含 TR T-5 TAETORD、TD U-1 "every 24 weeks"、UR U-1 + O55 "per per"、O56 PP 摘要节、O60 标题口径统一、O35-1/O35-3、ch10 4.1 行重复等), 列: 批次 / 位置 / PDF 原值 / 候选值 / 依据 / 主控建议。按类别分组, 每条可直接让用户 A/B 选。
3. 统计: 总条数、KB 写正确值 n、照录+T4 n、定位失败 n。
引文 ≤ 25 词/处 (CDISC 版权)。evidence 里 markdown 链接用反引号。禁止 git stash/checkout/reset/commit。scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/reg_typo/`。trace 追加一行 (step "T2S.REG", agent executor)。
回主控 ≤ 8 行。
