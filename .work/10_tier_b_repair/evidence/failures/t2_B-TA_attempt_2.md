# T2 B-TA attempt 2 (failure archive, 规则 B)

- 输入: attempt 1 产物 + reviewer 修正 ①-⑤ (Mermaid 标签 / arm 箭头 / Ex2-4,7 Retrospective 图).
- 产物: TA/examples.md (attempt 2 终态 md5 a1a95b892cd9c2fbe77eb920f893e964, 983 行, 24 Mermaid); diff = t2_B-TA_attempt_2.patch (vs 466e0c3).
- 技术判定: fp 回归仅 p0396_a009 (ATOM_ERR); live docs 42; reviewer delta 复审通过.
- 业务判定: auditor FAIL (t2_B-TA_audit.md M-1) — 非 Schema 视图 (约 17 张) 缺 PDF 图中带箭头的 "Randomization" 注释, Ex3 缺 "Response Evaluation".
- 根因: 标签核对只覆盖节点/边/箭头, 漏了图内独立注释文字; 未逐张列清单自证.
- 下一 attempt 输入: 24 张图逐张对渲染, 有注释者补注释节点, 清单逐张列出.
