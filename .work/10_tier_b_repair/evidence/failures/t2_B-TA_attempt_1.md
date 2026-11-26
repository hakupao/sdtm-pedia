# T2 B-TA attempt 1 (failure archive, 规则 B)

- 输入: work/t2_batches/B-TA.json (17 atoms) + dispatch notes + 主控 X-1/X-2 裁定; base HEAD 466e0c3.
- 产物: TA/assumptions.md + TA/examples.md (diff = t2_B-TA_attempt_1.patch, vs 466e0c3); checkpoint evidence/checkpoints/t2_B-TA.md (attempt 1 + 续).
- 技术判定: fp 新命中 42 / 回归 1 (p0396_a009 ATOM_ERR); census diffs 0; live docs 42.
- 业务判定 (reviewer t2_B-TA_review.md): CONDITIONAL — 叙述/表格/删除/PDF_TYPO 通过; Mermaid 标签与 PDF 图不一致 (Ex7 Prospective epoch 名/跳转标签; Ex5/Ex6 Retro Rest A/B 与周期注; Study Schema 边标签 "Randomized to …"/"P-5-10"/"Response: …").
- 根因: Mermaid 只核了分支/顺序逻辑, 未逐字核节点/边标签.
- 下一 attempt 输入: 只改 examples.md Mermaid 标签, 对 20 图全部节点/边标签逐字对 PDF 渲染.
