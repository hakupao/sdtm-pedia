# SP5 Rule D BLOCKER "B1" 修复独立复核

- 复核对象 commit: `8a0f771` — `fix(sp5): Rule D BLOCKER B1 — main.py lifespan called n_domains property as method`
- 复核 lane: 独立 reviewer (与实现者不同 session / 不同 context, 满足规则 D 审阅隔离)
- 日期: 2026-07-09
- **裁定: APPROVE**
- **护栏可证明捕获原 bug: 是 (YES) — 有 before/after 命令证据**
- BLOCKER / HIGH: 无

---

## 1. 修复正确性 (verify #1)

**结论: 正确。**

- `MetaStore.n_domains` 确为 `@property` (`server/meta_store.py:147-149`), 返回 `int` (`len(self._real_domains)`)。因此原代码 `store.n_domains()` = 对一个 `int` 加 `()` → `TypeError: 'int' object is not callable`, 与 B1 描述完全一致。
- 修复把 `store.n_domains()` 改为属性访问 `store.n_domains` (`server/main.py:111`), 语义正确, 返回域计数 int, `log.info(...)` 行不再抛错。
- **同类 bug 扫描**: 对全仓 (排除 `.venv`) grep `n_domains() / n_variable_entries() / n_unique_variables() / model_defhome_map() / known_domains()` 等"属性被当方法调用"模式 → **NONE FOUND**。main.py 中 `n_domains` 仅此一处调用点, 已修复, 无遗漏同类问题。

环境确认:
```
n_domains 定义: server/meta_store.py:148  @property def n_domains(self) -> int: return len(self._real_domains)
chroma_dir= .../data/chroma   exists= True     (本机索引存在 → 冒烟测试实际执行, 不 skip)
meta_path=  .../data/meta/meta.yaml  exists= True
```

## 2. 护栏是否真的能拦住 bug (verify #2 — 最关键)

**结论: 能。护栏可证明捕获原 bug。** 做了"重新注入 bug → 跑测试 → 复原"的对照实验:

**Before 修复 (临时把 `store.n_domains` 改回 `store.n_domains()`)** — 运行
`pytest ...::test_create_app_boots_through_lifespan -q`:
```
>       log.info("graph_engine", domains=app.state.graph_engine.store.n_domains())
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: 'int' object is not callable
server/main.py:111: TypeError
=========================== short test summary info ============================
FAILED scripts/tests/test_validate_study_endpoint.py::test_create_app_boots_through_lifespan
```
→ 新增的 lifespan 冒烟测试**如实失败**, 且失败点 (`main.py:111`) 与失败类型 (`TypeError: 'int' object is not callable`) 正是原 B1。证明它确实进入了 `create_app()` 的完整 lifespan (日志里已见 `startup` / `answer_channels` / `spec_loader`), 这是其它测试从不触达的路径。

**After (复原为 `store.n_domains`)** — 同一测试重跑: `. [100%]` (通过)。

即: 如果这个测试当初就存在, 绿色套件不会漏掉 B1。护栏名副其实。

## 3. 冒烟测试健壮性 (verify #3)

- **skip 守卫正确**: `if not settings.chroma_dir.exists(): pytest.skip(...)`。索引缺失时干净 skip 而非 error (缺 chroma 时 lifespan 里 `app.state.rag` 会真去加载 collection, 提前 skip 合理)。本机索引存在, 故实际执行, 全量套件 504 passed **0 skipped** 也印证它真跑了。
- **无 import 期副作用**: `create_app` 仅构造 FastAPI 对象并注册 lifespan (不执行)。`server.main` 模块级 `app = create_app()` (line 175) 同理不 boot RAG。lifespan 只在 `with TestClient(create_app()) as c:` 进入 ASGI startup 时才跑 → 即便走 skip 分支, 惰性 `import server.main` 也不会崩。
- **干净关停**: 用 `with TestClient(...) as c:` 上下文管理器, 退出时触发 lifespan shutdown (`log.info("shutdown")`), 无悬挂状态。
- **无状态泄漏 / 排序依赖**: 该测试用 `create_app()` 新建独立 app, 不复用模块级全局 `app`, 也不改动 `settings` 全局; 与 module 作用域 `client` fixture (裸 app) 互不影响。断言 `c.app.state.graph_engine.store.n_domains > 0` 读的是本次新建 app 的缓存引擎, 合理。
- 轻微代价 (非问题): 该测试会构建完整 RAG engine (含 BM25 索引), 比其它用例慢, 但对冒烟测试可接受。

## 4. 有无新引入问题 (verify #4)

全部在 `branches/07_rag_kg/sdtm-rag` 下运行 `.venv/bin/`:

| 检查 | 命令 | 结果 |
|------|------|------|
| 全量测试 | `pytest scripts/tests/` | **504 passed**, 0 failed, 0 skipped (与 commit message 一致) |
| Lint | `ruff check server/main.py scripts/tests/test_validate_study_endpoint.py` | **All checks passed!** |
| Types | `mypy server/main.py scripts/tests/test_validate_study_endpoint.py` | **Success: no issues found in 2 source files** |

无回归、无资源泄漏、无 lint/type 问题。

## 5. 工作树状态

对照实验后已 revert 临时编辑; `git status --short` 为空, `git diff --stat` 无输出 —— 工作树与复核开始时完全一致, 未提交任何改动。

---

### 裁定汇总

**APPROVE。** 修复本身正确 (属性访问替换错误的方法调用), 且新增的 `test_create_app_boots_through_lifespan` 经"注入-复现-复原"对照实验证明**确实能拦住**原 B1 (TypeError at main.py:111)。全量 504 passed / ruff clean / mypy clean, 无 BLOCKER/HIGH, 无新问题。
