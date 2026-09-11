# C2R N1 — 附页子集语义 (label + prompt) 收口 (2026-09-11)

> 状态: **工程 DONE + 复审 PASS + gpt 家复测 PASS; opus-5 复测挂起 (供给侧)**; 默认 OFF 不动
> PLAN: `PLAN_c2r_pdf_bypass.md` §6 (判据登记于实现前) · 判分: `evidence/step_c2r_n1_audit.md` (非作者 judge, 规则 A 全量)
> 起源: V3 判分 §4 第 1/2 条 — opus-5 把「附上的块首页没有 X」外推成「整块没有 X」(RETRO §2)

## 1. 改了什么 (4 文件, +62 −2; 检索 / 选页 / 触发 / SSE 契约零改动)

- `server/pdf_context.py` `_wf_label` / `_ann_label`: 块跨多页时 label 追加 `（p.a–b ブロックのうち本頁 p.x のみ添付）` / `（p.a–b のうち p.x）`; 单页块与无块兜底不加 (狼少年防护)。
- `server/router.py` `_PDF_SOURCE_RULE` 第 2 条 (复审 MAJOR-1/MINOR-2 后口径): label 驱动的「部分附页」声明; 画面由来的否定须限定「添付頁 p.x の範囲では」; **卡片事实 (非表示アクティビティ 等) 的否定不在此限**。
- 测试 +4 (label 范围注 / 单页不加注同 selection 双端钉死 / prompt 含限定语与排除条款; `画面目視判読` 计数仍 1)。

## 2. 验证

| 项 | 结果 |
|---|---|
| TDD | 先红 3 / 绿 4; 全量 `scripts/tests` 2226 → **2230 passed** |
| ruff (4 文件) | clean |
| 红线 oidscan (4 文件 + 两份证据) | CLEAN |
| 规则 D 复审 (code-reviewer, opus) | PASS-with-nits → 1 MAJOR + 2 MINOR + 2 NIT 已修; MINOR-3 (选页后再决定加注) / NIT-6 接受不修 |

复跑:
```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_pdf_context.py scripts/tests/test_pdf_context_wiring.py -q   # 69 passed
.venv/bin/python -m pytest scripts/tests -q                                                              # 2230 passed
```

## 3. 复测 (B 臂, T1/T3/T6 × gpt-terra/gpt-sol, 6/6 成功, 真实 `/api/ask`)

runner 已迁入仓库 `scripts/study/c2r_eval/` (原在 scratchpad, 易失); 题面仍只读 gitignored `runs/c2r_v3/questions.json`。
```bash
cd sdtm-rag
nohup env SDTM_RAG_AUTH_ENABLED=false SDTM_RAG_PDF_CONTEXT_ENABLED=true \
  .venv/bin/uvicorn server.main:app --port 8011 > /tmp/armB_8011.log 2>&1 &
until curl -s -m 2 localhost:8011/api/health >/dev/null; do sleep 1; done
.venv/bin/python scripts/study/c2r_eval/run_v3.py --group T --arms B --models gpt-terra,gpt-sol --qids T1,T3,T6 --timeout 900 --out c2r_n1
.venv/bin/python scripts/study/c2r_eval/tabulate_v3.py c2r_n1
```
原始记录 gitignored `data/study/st01/eval/runs/c2r_n1/B_<model>_<qid>.json`; 明细 `runs/c2r_n1/audit_detail.md`。

| qid | 满分 | V3 B gpt-terra | N1 B gpt-terra | N1 B gpt-sol |
|---|---|---|---|---|
| T1 | 5 | 3 | 3 | 3 |
| T3 | 4 | 4 | 4 | 4 |
| T6 | 3 | 2 | 2 | 2 |

画面主张全量 53 条: verified 47 / contradicted 5 / unverifiable 1; **否定断言正确限定 6/6 份**; 同型 (附页缺席→整块缺席) contradicted **0**; 卡片级否定 6/6 保持断言语气 (复审担心的回归未发生)。

| 判据 (PLAN §6) | 结果 |
|---|---|
| ① 同型 contradicted = 0 (两模型) | PASS (但见 §4: gpt 家基线本就为 0) |
| ② T3/T6 逐点 ≥ V3 B gpt-terra | PASS (逐点全等) |
| ③ T1 ≥ V3 | PASS (3 = 3) |
| 默认 ON | **不动** — 绑定 opus-5 补跑 (PLAN §6) |

## 4. 诚实边界

- **判据 ① 在 gpt 家近乎空转**: V3 的两条同型错误 100% 出自 opus-5, 本轮 opus-5 因 Bedrock 账号拒绝 (`bedrock_anthropic_denied_2026-09-11.md`) 跑不了。**本轮不构成「修法已验证」**, 只构成「未引入回归 + 限定语被条件性触发」。
- 正向证据: 6/6 份在多页块上都出现「只附了块中一页, 不能外推」句式, 而在单页块 (wf p.79) 上两模型都**没有**多余限定 → label 的块范围确实被读到。
- 混杂: 路由组 opus-5 同样被拒 → corpus 退到 `both` (V3 为 `study`); T3 annotated 页集与 V3 不同 (少一页无关页, 多一块首页), T1/T6 页集逐字相同。
- 判分敏感性: T3 ④ 裸 OID 按 K2 豁免; 若改 K1 严格口径, 判据 ② 翻 FAIL (judge 已单列)。

## 5. 新暴露的缺陷 (不属本单元, 供立项)

- **来源标签捏造** (gpt-sol ×2): 底层事实对, 但把卡片/索引层事实安上不存在的「画面注记」— 页号越界闸与 N1 作用域规则都不覆盖。
- **T6 ② 面板边界合并** (两模型): 无标题面板不被当成独立组, 与数据定义上的项目组边界逐字重合 → 与 N1 无关的独立缺陷。

## 6. 补跑入口 (Bedrock 恢复后)

```bash
.venv/bin/python scripts/study/c2r_eval/run_v3.py --group T --arms B --models opus-5 --qids T1,T3,T6 --timeout 900 --out c2r_n1
```
判分沿用 `step_c2r_n1_audit.md` 的 K1–K4; 同型 contradicted = 0 且 T3/T6 ≥ V3 B opus-5 (2/4, 3/3) 才可再议默认 ON。
