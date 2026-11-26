批次 S-SPEC3 (T2-post 扫描批, spec-only), attempt 1. 角色: writer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_writer_v1.0.md` 执行, 它列出的必读文件全部先读 (t2_writer_v1.0.md 规则 1-11 / t2_dispatch_notes.md 含末尾 T2S 段及其后各条主控裁定 / t1_user_ack.md / t2_post_user_ack.md U1-U8)。批次文件 `.work/10_tier_b_repair/work/t2_batches/S-SPEC3.json` (spec_only: CV MI MK NV RE RP QS FT 共 8 个 spec.md)。
目标: 每个 spec.md 对 PDF spec 表逐变量逐字段核 (变量数量/顺序, Order/Label/Type/Role/Core/CDISC Notes; CT 列只核 `*` 与非 C-code 值), 修到与 PDF 一致; 补 spec 表脚注 (U2/U7); CT `*` 照录。**不改** CT 的 C-code 记法与 DOMAIN CT (U5/U6 归后续 S-CT 批)。
工具: `work/scratch/t2s_tools/sc2.py` + `sc2w.py` 与 `speccmp2.py` 交叉使用 (原 speccmp.py 有缺陷勿用; 各自盲区见 t2_dispatch_notes.md S-SPEC2 条; 先 `pdftotext -bbox -f N -l N` 取页到你的 scratch 的 bb_N.html, 用法见脚本头), 每域做 "变量数 + 顺序" 计数闸 + 渲染图复核; CDISC Notes 长文本逐字比 (R2: 改写丢短语即缺)。先例: 各域 S 批 spec 改动 (`t2_S-INT.md` / `t2_S-FND.md` 的 spec 段)。
checkpoint 必须含 "完整节页范围" (每域 spec 表所在 PDF 页) 与 "双向全扫" (每域 spec 表逐变量结果表)。页范围先复核。有别的批同时在跑, 只改本批文件。
回主控 ≤ 10 行。
