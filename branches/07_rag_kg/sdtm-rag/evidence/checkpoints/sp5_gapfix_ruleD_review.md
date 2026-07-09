# SP5 缺口修正 — Rule D 独立审阅

> 2026-07-09 · 独立审阅 lane (与实施者不同 subagent)。范围: `git diff c681410..HEAD -- branches/07_rag_kg/sdtm-rag/` (4 commit / 16 file / +342-57)。
> 命令实测: `.venv/bin/python -m pytest scripts/tests/ -q` · `.venv/bin/ruff check` · `.venv/bin/mypy`。

## 裁决: **REQUEST_CHANGES**

一个 **BLOCKER**: 生产 lifespan 启动会崩。其余 7 个审查点全部通过 (逻辑正确 / advisory-only 不变量成立 / 证据诚实 / 503 测试全绿)。BLOCKER 修复只需删一对括号,修完即可 APPROVE。

---

## BLOCKER

### B1 — `main.py:111` lifespan 调用 `n_domains()` 会崩溃生产启动

**文件:行** `server/main.py:111`
```python
log.info("graph_engine", domains=app.state.graph_engine.store.n_domains())
```

**问题**: `MetaStore.n_domains` 是 `@property` (`server/meta_store.py:147-149`, `def n_domains(self) -> int`),不是方法。加括号调用等于 `int(...)` → `TypeError: 'int' object is not callable`。全仓其它调用方全部按属性用 (`server/structured_answer.py:93` `self.store.n_domains`;`scripts/tests/test_meta_store.py:18` `assert store.n_domains == 63`),只有本次新增这一行加了括号。

**实测复现**:
```
$ .venv/bin/python -c "... eng.store.n_domains ..."
n_domains as property: 63
ERROR calling n_domains(): TypeError -> 'int' object is not callable
```

**失败场景 (生产)**: 该行在 `lifespan()` 内、`yield` (main.py:134) 之前,且**无 try/except 包裹**。`lifespan=lifespan` 已挂到 app (`main.py:154`),`app = create_app()` (175),生产 launchd 跑 `uvicorn server.main:app` (`deploy/com.sdtmrag.api.service.plist.template:23`)。启动时 lifespan 执行到 111 行抛异常 → Starlette 判定 "Application startup failed" → **服务根本起不来**。注意异常发生在**求值 `log.info` 实参时**,早于 `log.info` 调用本身,任何日志框架都截不住。

**为什么测试没抓到 (覆盖缺口)**: 两个 study 端点测试都用 bare app + 手工 `app.state.*`,**不跑 lifespan** (`test_validate_study_endpoint.py:16-23` 注释明说 "no lifespan/create_app";`test_validate_study_uses_cached_engine` 也是直接 `app.state.graph_engine = ...`)。正是这条 lifespan 日志行没有任何测试触达,BLOCKER 才漏网。503 测试全绿 ≠ 生产能启动。

**修复**: 去掉括号 —
```python
log.info("graph_engine", domains=app.state.graph_engine.store.n_domains)
```
**建议补一条冒烟**: 用 `create_app()` + `with TestClient(app):` (进入 context 才触发 lifespan startup) 断言不抛,堵住这个 lane。

---

## 逐点核验结论 (审查点 1-8)

**1. advisory-only 不变量 (无 ERROR)**: **成立**。`grep '"ERROR"' server/graph_validator.py` 只命中 docstring ("never ERROR"),无 ERROR 字面量。三个 check 的 severity 全是字面量: completeness=`WARN`(RELREC)/`INFO`(curated),cascade=`WARN`,impact=`INFO`×2;`run_graph_checks` 仅拼接。实测样本提交只产出 `{INFO, WARN}`。✅

**2. completeness 对称 + INFO 正确性**: **正确**。对称图 `relrec_partners[dom].add(target)` + `relrec_partners[target].add(dom)` 用 set 去重,单域内 partner 唯一,不双计;方向不同的 WARN (AE→CM vs CM→AE) 是两条独立 finding,非重复。INFO 去重三重防护 `if target in partners or target in submitted or target in seen`。**关键**: `all_domains()` 实测**包含** RELREC/RELSPEC/RELSUB/SUPPQUAL/CO (它们 counts_toward_63),所以 `target in all_domains` **挡不住**这些关系数据集 —— `_REL_DATASET_TARGETS` 排除集是**load-bearing 且必要的**,M1 问题已正确堵住。实测提交 {AE,CM}: WARN=AE→PR,INFO=AE→FA/CM→EC,无 REL 数据集混入 INFO,无重复,severities={INFO,WARN}。✅

**3. cascade extensible-skip + 非嵌套**: **正确**。`cl.get("extensible")` 为真则 `continue`;非嵌套判据 `not (a<=b or b<=a)` —— 子集覆盖 (AE={Y} ⊆ MH={Y,N,U}) 静默,双向发散 (AE={N} vs LB={Y}) 触发,逻辑正确。missing-flag 行为=fail-closed (无 flag 当闭合处理→可能 WARN),但实测 meta.yaml **0 个 codelist 缺 extensible 键**,该默认永不触发,无实际风险。✅

**4. impact Identifier-skip**: **正确**。`variable_attributes(var)` 未知变量返回 None → `role=None` → `None != "Identifier"` 为真,但此时 `iv["n_domains"]` 对未知变量 <阈值,不会误报,无崩溃。实测 STUDYID/DOMAIN/USUBJID=`Identifier` (跳过),VISITNUM/VISIT/EPOCH=`Timing` (仍上报,符合证据里 VISITNUM 高 impact)。✅

**5. lint chore 行为保持**: **正确**。report.py 循环变量 `f→rf`/`sev_findings→rev_findings` 纯改名 + `datetime.now(timezone.utc)→datetime.now(UTC)` (py3.12 等价) + 删未用 `SemanticFinding` 导入 (grep 确认 report.py 已无引用)。router.py `from e`/`from None` 只改异常链 `__cause__`,不改控制流。pyproject `extend-immutable-calls` 仅 lint 配置、无运行时效果,且是 FastAPI 官方推荐做法,安全。改动 5 文件 `ruff check` 全 pass、`mypy` `Success: no issues found in 5 source files`。(全仓仍有 42 个 ruff error,但全在**本 diff 未碰**的 eval//scripts//ui//rag.py//reviewer.py//validator.py,属既有债,与本次无关。)✅

**6. GraphEngine 缓存**: 懒回退正确 —— `getattr(app.state,"graph_engine",None); if None: 新建` (router.py:648-650),None 处理妥当;engine 基于只读静态 meta.yaml,无 stale 风险。**但**: 因 B1,生产 lifespan 起不来,缓存路径在 prod 里形同虚设 (要靠 B1 修复才生效)。⚠️ (逻辑本身✅,受 B1 拖累)

**7. 真实数据证据诚实性**: **诚实**。`sp5_real_data_validation.md` 称 C71620 extensible=True(830 词)/C66742 extensible=False(4 词) —— 实测 `codelist(C71620)["extensible"]=True`、`codelist(C66742)["extensible"]=False`,完全吻合。extensible-skip 代码在位 (graph_validator.py:98)。残余限制 (小样本值域不全→假阳、grab-bag codelist 跨域无需一致) 是代码**确实未覆盖**的真实弱点,如实披露,未夸大修复。✅

**8. 零回归**: `503 passed, 1 warning in 18.18s`。新增/改动测试均为真实断言 (对称 RELREC / curated INFO / extensible-skip / 子集静默 / Identifier-skip 全有专测);无 `test.skip`/`.only`/`xfail` ("skip" 命中的是测试**函数名**)。e2e 放宽 `not any(GXDOM)` → `not any(GXDOM and WARN)` 是配合新 INFO 提示的合理放宽,仍守住 "无 GXDOM WARN"。✅ (注: 测试口径零回归,但 B1 是测试**未覆盖**的生产回归。)

---

## 更低优先级 (非阻塞,供参考)

- **MED (测试缺口)**: 无任何测试进入 `lifespan` startup,导致 B1 漏网。建议 B1 修复时一并加 `with TestClient(create_app()):` 冒烟,或在缓存测试里覆盖启动路径。
- **LOW (可选)**: cascade missing-extensible 默认 fail-closed。当前 meta.yaml 全带 flag 无影响;若未来 meta 结构变动,建议显式处理缺失 flag 或加断言,避免静默假阳。

## 复现命令
```
cd branches/07_rag_kg/sdtm-rag
.venv/bin/python -m pytest scripts/tests/ -q      # 503 passed
.venv/bin/ruff check server/graph_validator.py server/report.py \
    server/router.py server/main.py server/meta_store.py   # All checks passed!
.venv/bin/mypy server/graph_validator.py server/report.py \
    server/router.py server/main.py server/meta_store.py   # Success: no issues in 5 files
.venv/bin/python -c "from server.config import settings; from server.meta_store import MetaStore; \
    print(MetaStore(settings.meta_path).n_domains())"       # TypeError: 'int' object is not callable
```
