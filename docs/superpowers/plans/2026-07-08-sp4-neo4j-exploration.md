# SP4 — Neo4j 探索层 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 SP1 meta.yaml 之上建 Neo4j 图数据库探索层 (brew+launchd 本机服务 + 幂等导入脚本 + 独立对账门 + Cypher 查询库), 四道验收门全过后收口; 生产答题通道 (内存 DictBackend) 零改动、零依赖、零扰动。

**Architecture:** meta.yaml (唯一源) → `scripts/build_neo4j.py` (纯函数抽取 + driver 批量导入, 幂等) → Neo4j (bolt://127.0.0.1:7687, Browser 127.0.0.1:7474)。验收: `scripts/reconcile_neo4j.py` (独立码路对账, Gate 1 = Rule A lane) + `docs/cypher_cookbook.md` 7 条查询经 `eval/prod_wirein/sp4_cookbook_golden.py` 锚定 (Gate 2) + `eval/prod_wirein/sp4_isolation_probe.py` 停机 byte-identical (Gate 3) + Rule D 异 type 审 (Gate 4)。Spec: `docs/superpowers/specs/2026-07-08-sp4-neo4j-exploration-design.md` (已批准 2026-07-08)。

**Tech Stack:** Python 3.11 (`.venv`), neo4j 官方 driver (dev extra only), Neo4j (brew, arm64, 自带 openjdk 依赖), launchd (com.sdtmrag.* 运维模式), pytest, yaml。

## Global Constraints

- 相对路径基准 = `branches/07_rag_kg/sdtm-rag/` (下称 sdtm-rag 根); **Files 清单一律写 repo-root 相对路径**; Run 命令统一从 repo root 先 `cd branches/07_rag_kg/sdtm-rag`。
- Python 一律 `.venv/bin/python` / `.venv/bin/pytest` (不走 `uv run`; launchd 同理直连二进制)。
- **生产隔离 (spec 硬约束)**: `server/` 零新增 neo4j 引用; neo4j driver 只进 `[project.optional-dependencies].dev` (命令 `uv add --optional dev neo4j`, **不是** `--dev`/`--group`, 那会另开 PEP 735 机制); **任何 pytest 单测不得依赖活 Neo4j** — 活库验证全部走 reconcile/golden 脚本, 这样 Gate 3 "停机全绿" 自然成立。
- localhost-only 双端口 (7474/7687); `NEO4J_PASSWORD` 只进 gitignored `.env` (chmod 600), `.env.example` 加空值行; **不碰** `deploy/.env.service.template` (go-live 范围不含 Neo4j)。
- 保真度纪律 (沿 SP3): RELATED_TO 边必带 `advisory: true` + `fidelity: 'curated_prose'` + nullable `mechanism`; 结构边 (HAS_VARIABLE/USES_CT/IN_CLASS/DEFHOME) 为权威。
- 反过拟合: `reconcile_neo4j.py` **禁止 import** `build_neo4j` / `MetaStore` / `GraphEngine` (可 import neo4j driver 读库 + yaml 读源); golden harness 走 GraphEngine 等价 lane, 两 lane 分工不混。
- 规则 B: 任何门失败归档 `branches/07_rag_kg/sdtm-rag/evidence/failures/sp4_attempt_N.md`, 不删。规则 C: Task 9 写 `RETROSPECTIVE_sp4.md`。规则 D: Task 8 异 `subagent_type` 全量审。规则 A: Gate 1 的独立码路 N=9 分层邻域抽检即 Rule A lane (spec §5 说明, 不另设第三 lane)。
- 每个 task 结尾 commit (git 操作在 repo root)。

## Spec 偏差 (数据接地, 写码前已核实; Rule D 审查项)

计划期用程序对 `data/meta/meta.yaml` 实测, 发现 4 处 spec 表述与数据不符, 按"期望值从 raw meta.yaml 独立程序导" (spec §5 gate 1) 的原则修正:

| # | Spec 原文 | 实测 | 本 plan 的处理 |
|---|----------|------|---------------|
| D1 | C66742 影响分析 "必回 123 变量/**44 域**" (§5 gate 2) | **123 变量 / 41 域** (变量数吻合, 域数是 spec 笔误) | golden 锚 123/41 |
| D2 | USES_CT 边属性 "—" (§3) | C119013 (FOCID, SP2 教训同源) 是唯一 closure≠location 的 codelist (变量级闭包 3 域, 逐域精确 1 域); 无边属性则 impact 查询无法与生产 GraphEngine 逐数吻合 | USES_CT 边加 `domains: [list]` 属性 (该变量实际使用该 CT 的域), cookbook impact 查询 `UNWIND u.domains` |
| D3 | DEFHOME "Variable→**Domain**" (§3) | `model_defhome` 映射变量 → **model 章节文件** (如 `model/03_special_purpose_domains.md`), 非域 | 新增第 5 节点标签 **ModelChapter** (4 节点, `path` 属性); DEFHOME = Variable→ModelChapter |
| D4 | Variable 节点 1523 (§3) | model_defhome 59 变量中 **18 个不在任何 IG 域** (APID/SETCD/SPECIES/STRAIN 等模型级变量) — 若只建 1523 节点, DEFHOME 只能建 41 条, 静默丢 18 条数据 | 18 个模型级变量也建 Variable 节点, 标 `model_only: true` (仅 name 属性); IG 1523 个标 `model_only: false`。Variable 总数 **1541 = 1523 + 18**; DEFHOME 全量 59 条。计数类 cookbook 查询默认 `WHERE NOT v.model_only` |

## Golden 数字 (2026-07-08 程序实测, reconcile/golden/测试的锚)

| 类别 | 值 |
|------|-----|
| 节点 | Domain **63** (DI 桩 `counts_toward_63: false` 不导) / Variable **1541** (1523 IG + 18 model-only) / Codelist **1005** / Class **8** / ModelChapter **4** |
| 边 | HAS_VARIABLE **1917** / USES_CT **542** (唯一 (var,ct) 对, 跨域 union) / IN_CLASS **63** / DEFHOME **59** / RELATED_TO **52** |
| impact C66742 | 123 变量 / 41 域 |
| most-shared top-5 | C66742 (123v/41d), C71620 Unit (58v/32d), C66789 Not Done (36v/36d), C66728 (26v/9d), C74456 (19v/19d) |
| 变量 ≥20 域 | 8 个: STUDYID 63, DOMAIN 59, USUBJID 55, EPOCH 44, TAETORD 43, VISIT 36, VISITDY 36, VISITNUM 36 |
| same_class(DM) | CO, SE, SM, SV |
| class_sizes | Events 7, Findings 30, Findings About 2, Interventions 7, Relationship 4, Special-Purpose 5, Study Reference 1, Trial Design 7 |
| co-users(AECONTRT) | C66742 → others 122 个 |
| ModelChapter 4 路径 | model/02_observation_classes.md, model/03_special_purpose_domains.md, model/05_study_level_data.md, model/06_relationship_datasets.md |
| 跨域属性分歧 | 15 个变量 role/core 跨域不同 (0 个 type 不同), 如 VISIT (Synonym Qualifier vs Timing), USUBJID (Exp in DM / Req 其余) — 佐证逐域权威值放 HAS_VARIABLE 边属性 |

## Task 总览

1. Neo4j 安装 + dev 依赖 + 初始密码 + 前台 smoke (infra)
2. launchd plist 模板 + runbook §Neo4j (deploy 面)
3. `build_neo4j.py` 抽取纯函数 `extract_graph` (TDD)
4. `build_neo4j.py` 导入层 `import_graph` + `main` (幂等全量导入)
5. `reconcile_neo4j.py` 独立对账 + 幂等 snapshot 门 (**Gate 1 / Rule A lane**)
6. `docs/cypher_cookbook.md` 7 条查询 + golden harness (**Gate 2**)
7. 生产隔离门: 停机 pytest + composite byte-identical + grep 闸 (**Gate 3**)
8. Rule D 异 type 全量审 (**Gate 4**)
9. 收口 — 证据 checkpoint + RETROSPECTIVE + Chain 07_RAG 文档链

---

### Task 1: Neo4j 安装 + dev 依赖 + 初始密码 + 前台 smoke (infra)

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/pyproject.toml` (dev extra 加 neo4j)
- Modify: `branches/07_rag_kg/sdtm-rag/uv.lock` (uv 自动)
- Modify: `branches/07_rag_kg/sdtm-rag/.env.example` (加 NEO4J_* 空值区块)
- Modify: `branches/07_rag_kg/sdtm-rag/.env` (本机, gitignored, 填真实密码 — **不 commit**)

**Interfaces:**
- Consumes: brew (arm64 /opt/homebrew), 既有 `.env` 约定 (gitignored, chmod 600)
- Produces: 可用的本机 Neo4j (bolt 7687 + http 7474, localhost-only, 密码已设); `.env` 内 `NEO4J_URI` / `NEO4J_USER` / `NEO4J_PASSWORD` (Task 4/5/6 的连接参数); `.venv` 内可 `import neo4j`

- [ ] **Step 1: dev extra 加 neo4j driver**

```bash
cd branches/07_rag_kg/sdtm-rag
uv add --optional dev neo4j
uv sync --extra dev
.venv/bin/python -c "import neo4j; print(neo4j.__version__)"
```

Expected: 打印 driver 版本 (5.x); `git diff pyproject.toml` 显示 neo4j 只出现在 `[project.optional-dependencies].dev`, **不在** `[project].dependencies`。

- [ ] **Step 2: brew 安装 Neo4j 并核实路径**

```bash
brew install neo4j
brew info neo4j          # 记下版本与路径
which neo4j cypher-shell # 期望 /opt/homebrew/bin/{neo4j,cypher-shell}
neo4j version
```

Expected: 安装成功 (formula 自带 openjdk 依赖, 本机此前无 java — 若 `neo4j version` 报 JVM 错, 记录 `brew info neo4j` 提示的 JAVA_HOME 要求, 后续 plist/runbook 用同样的值)。记录实际 NEO4J_HOME (通常 `/opt/homebrew/opt/neo4j/libexec`) 与 conf 路径 (`libexec/conf/neo4j.conf`), Task 2 模板要用。

- [ ] **Step 3: 生成密码进 .env, 设初始密码**

```bash
cd branches/07_rag_kg/sdtm-rag
PW=$(openssl rand -base64 24)
printf '\n# ─────────── Neo4j 探索层 (SP4; localhost-only, 不进 go-live) ───────────\nNEO4J_URI=bolt://127.0.0.1:7687\nNEO4J_USER=neo4j\nNEO4J_PASSWORD=%s\n' "$PW" >> .env
chmod 600 .env
neo4j-admin dbms set-initial-password "$PW"
```

Expected: `set-initial-password` 成功 (须在首次启动前跑; 若报 "password already set", 用 `cypher-shell` 登入后 `ALTER CURRENT USER SET PASSWORD` 改)。

同时给 `.env.example` 追加同一区块 (密码留空):

```
# ─────────── Neo4j 探索层 (SP4; localhost-only, 不进 go-live) ───────────
NEO4J_URI=bolt://127.0.0.1:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=
```

- [ ] **Step 4: 前台 smoke**

```bash
neo4j console &   # 前台模式后台化, 只为 smoke
sleep 20
source <(grep '^NEO4J_' branches/07_rag_kg/sdtm-rag/.env 2>/dev/null || grep '^NEO4J_' .env)
cypher-shell -a bolt://127.0.0.1:7687 -u neo4j -p "$NEO4J_PASSWORD" "RETURN 1 AS ok;"
curl -s http://127.0.0.1:7474 | head -3
lsof -nP -iTCP:7474 -iTCP:7687 -sTCP:LISTEN
kill %1
```

Expected: `RETURN 1` 回 `ok 1`; curl 有 JSON 应答; **lsof 显示两端口都绑 127.0.0.1** (Neo4j 默认 localhost, 此步是核实, 不达标则改 conf `server.default_listen_address=127.0.0.1` 再验)。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/pyproject.toml branches/07_rag_kg/sdtm-rag/uv.lock branches/07_rag_kg/sdtm-rag/.env.example
git commit -m "infra(sp4): neo4j driver in dev extra + brew neo4j install conventions (.env NEO4J_*)"
```

确认 `git status` 不含 `.env`。

---

### Task 2: launchd plist 模板 + runbook §Neo4j

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/deploy/com.sdtmrag.neo4j.plist.template`
- Modify: `branches/07_rag_kg/sdtm-rag/deploy/README.md` (追加 `## Neo4j 探索层` 节 + 文件清单行)

**Interfaces:**
- Consumes: Task 1 记录的实际二进制/conf 路径; 既有 plist 风格 (`deploy/com.sdtmrag.api.service.plist.template`: 顶部注释块 + Label/ProgramArguments/EnvironmentVariables/RunAtLoad/KeepAlive/ThrottleInterval/日志)
- Produces: 已装载的 `gui/$(id -u)/com.sdtmrag.neo4j` 服务 (Task 5-7 用 `launchctl bootout/bootstrap` 起停它)

- [ ] **Step 1: 写 plist 模板**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  com.sdtmrag.neo4j — Neo4j 探索层 launchd 服务 (SP4)
  spec: docs/superpowers/specs/2026-07-08-sp4-neo4j-exploration-design.md §2/§4
  安装: cp deploy/com.sdtmrag.neo4j.plist.template ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist
        launchctl bootout  gui/$(id -u)/com.sdtmrag.neo4j 2>/dev/null || true
        launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist
  Differences vs com.sdtmrag.api:
  - 前台命令是 brew 的 `neo4j console` (JVM), 非 .venv 内 python 服务
  - localhost-only 双端口 7474/7687 (Neo4j 默认), 不进 go-live 共享范围
  - 日志走 Neo4j 自身 logs 目录 (/opt/homebrew/var/log/neo4j/)
  - heap 上限 1g: 优先 NEO4J_server_memory_heap_max__size 环境变量; 若该版本
    tarball 不吃 env 配置 (SHOW SETTINGS 验证, 见 runbook), 改写 neo4j.conf
    server.memory.heap.max_size=1g, env 行保留无害
-->
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.sdtmrag.neo4j</string>
  <key>ProgramArguments</key>
  <array>
    <string>/opt/homebrew/bin/neo4j</string>
    <string>console</string>
  </array>
  <key>EnvironmentVariables</key>
  <dict>
    <key>HOME</key>
    <string>/Users/bojiangzhang</string>
    <key>PATH</key>
    <string>/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>NEO4J_server_memory_heap_max__size</key>
    <string>1g</string>
  </dict>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>ThrottleInterval</key>
  <integer>10</integer>
  <key>StandardOutPath</key>
  <string>/opt/homebrew/var/log/neo4j/launchd.log</string>
  <key>StandardErrorPath</key>
  <string>/opt/homebrew/var/log/neo4j/launchd.log</string>
</dict>
</plist>
```

写模板前先按 Task 1 Step 2 记录的实际路径核对 `/opt/homebrew/bin/neo4j` 与日志目录 (`mkdir -p /opt/homebrew/var/log/neo4j` 若不存在); 若 `neo4j console` 前台运行需要 JAVA_HOME (Task 1 已探明), 在 EnvironmentVariables 加对应 `<key>JAVA_HOME</key>` 行。

- [ ] **Step 2: 装载 + 验证 (含 heap 与 localhost 双验)**

```bash
cp branches/07_rag_kg/sdtm-rag/deploy/com.sdtmrag.neo4j.plist.template ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist
launchctl bootout  gui/$(id -u)/com.sdtmrag.neo4j 2>/dev/null || true
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist
sleep 25
source <(grep '^NEO4J_' branches/07_rag_kg/sdtm-rag/.env)
cypher-shell -a "$NEO4J_URI" -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" \
  "SHOW SETTINGS YIELD name, value WHERE name = 'server.memory.heap.max_size' RETURN name, value;"
lsof -nP -iTCP:7474 -iTCP:7687 -sTCP:LISTEN
```

Expected: 服务起来, SHOW SETTINGS 回 `1g`; lsof 两端口绑 127.0.0.1。**若 heap 不是 1g** (env 配置未生效): `echo 'server.memory.heap.max_size=1g' >> <Task1 记录的 neo4j.conf 路径>` 后 `launchctl kickstart -k gui/$(id -u)/com.sdtmrag.neo4j` 重验, 并把 conf 方式写实进 runbook (模板注释已预告此分支)。

- [ ] **Step 3: README 追加 §Neo4j runbook**

在 `deploy/README.md` 文件清单表**之前**追加一节, 风格对齐既有 runbook (中文叙述 + bash 块内 # 注释):

```markdown
## Neo4j 探索层 (SP4; 本机自用, 不进 go-live)

> 状态: 本机探索层。localhost-only (7474 Browser / 7687 bolt), 与 8000 生产服务零耦合 —
> Neo4j 挂/停/没装, 生产答题不受影响 (spec 硬约束, Gate 3 有停机 byte-identical 证据)。

```bash
# 1. 安装 (formula 自带 openjdk)
brew install neo4j

# 2. 首次: 生成密码进 .env (chmod 600, 不进 git), 设初始密码
PW=$(openssl rand -base64 24)   # 追加 NEO4J_URI/NEO4J_USER/NEO4J_PASSWORD 到 sdtm-rag/.env
neo4j-admin dbms set-initial-password "$PW"

# 3. 装载 launchd 服务
cp deploy/com.sdtmrag.neo4j.plist.template ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist
launchctl bootout  gui/$(id -u)/com.sdtmrag.neo4j 2>/dev/null || true
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist

# 4. 验证 (heap 1g + localhost-only; heap 若非 1g 见 plist 模板注释的 conf 分支)
cypher-shell -a bolt://127.0.0.1:7687 -u neo4j -p "$NEO4J_PASSWORD" "RETURN 1;"
lsof -nP -iTCP:7474 -iTCP:7687 -sTCP:LISTEN   # 期望全绑 127.0.0.1

# 5. 全量导入 / 重建 (KB 冻结, 低频; 幂等可重跑)
cd <sdtm-rag 根> && .venv/bin/python scripts/build_neo4j.py
.venv/bin/python scripts/reconcile_neo4j.py    # 对账门, exit 0 才算导入成功

# 6. 起停 / 重启 / 卸载
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.neo4j   # 重启
launchctl bootout gui/$(id -u)/com.sdtmrag.neo4j        # 停 (生产不受影响)

# 7. Browser 探索: open http://127.0.0.1:7474 (登录 neo4j/$NEO4J_PASSWORD)
#    精选查询库: docs/cypher_cookbook.md
```
```

同时在文件清单表加两行: plist 模板 + `../docs/cypher_cookbook.md`。

- [ ] **Step 4: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/deploy/com.sdtmrag.neo4j.plist.template branches/07_rag_kg/sdtm-rag/deploy/README.md
git commit -m "infra(sp4): launchd plist template + deploy runbook for neo4j exploration layer"
```

---

### Task 3: `build_neo4j.py` 抽取纯函数 `extract_graph` (TDD)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/scripts/build_neo4j.py` (本 task 只写纯函数部分, 不 import neo4j)
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_build_neo4j.py`

**Interfaces:**
- Consumes: `data/meta/meta.yaml` (SP1 schema: 顶层 `meta_version/domains/codelists/model_defhome`; domain 键 `domain/label/class/structure/counts_toward_63/is_special/variables/same_class/relations_curated`; variable 键 `name/label/role/type/core/ct_codes/ct_dict`; codelist 键 `ct_code/name/extensible/term_count/termfile`; relations_curated 键 `target/mechanism/note/category/fidelity`)
- Produces: `load_meta(path: Path) -> dict` + `extract_graph(meta: dict) -> dict` — 返回 `{"nodes": {label: [row...]}, "edges": {etype: [row...]}}` 纯数据 (Task 4 的 `import_graph` 与 Task 5 测试消费; row 键见实现)

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_build_neo4j.py` (对真 meta.yaml 断言 golden 锚, 沿 test_build_meta.py 风格):

```python
"""SP4 build_neo4j extract layer — anchors pinned to reconcile-verified meta.yaml.

Pure-function tests only: NO live Neo4j needed (Gate 3 requires the whole pytest
suite to pass with Neo4j stopped)."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.build_neo4j import extract_graph, load_meta

META_PATH = Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml"


@pytest.fixture(scope="module")
def graph():
    return extract_graph(load_meta(META_PATH))


# ── 节点分类计数 (spec §3 + plan 偏差 D3/D4) ──────────────────────────────

def test_node_counts(graph):
    n = graph["nodes"]
    assert len(n["Domain"]) == 63          # DI 桩 counts_toward_63=false 不导
    assert len(n["Variable"]) == 1541      # 1523 IG + 18 model-only (偏差 D4)
    assert len(n["Codelist"]) == 1005
    assert len(n["Class"]) == 8
    assert len(n["ModelChapter"]) == 4     # 偏差 D3

def test_variable_model_only_split(graph):
    flags = [v["model_only"] for v in graph["nodes"]["Variable"]]
    assert flags.count(False) == 1523 and flags.count(True) == 18
    by_name = {v["name"]: v for v in graph["nodes"]["Variable"]}
    assert by_name["APID"]["model_only"] is True      # 模型级变量, 不在任何 IG 域
    assert "role" not in by_name["APID"]              # model-only 节点只有 name+model_only
    assert by_name["DTHFL"]["model_only"] is False

def test_di_stub_excluded(graph):
    assert "DI" not in {d["code"] for d in graph["nodes"]["Domain"]}

# ── 边分类计数 ────────────────────────────────────────────────────────────

def test_edge_counts(graph):
    e = graph["edges"]
    assert len(e["HAS_VARIABLE"]) == 1917
    assert len(e["USES_CT"]) == 542        # 唯一 (var, ct) 对, 跨域 union
    assert len(e["IN_CLASS"]) == 63
    assert len(e["DEFHOME"]) == 59         # 偏差 D4: 全量 59, 不静默丢 18
    assert len(e["RELATED_TO"]) == 52

# ── 语义抽点 (跨域分歧 / 逐域权威值 / advisory 保真) ──────────────────────

def test_has_variable_carries_per_domain_attrs(graph):
    rows = {(r["domain"], r["var"]): r for r in graph["edges"]["HAS_VARIABLE"]}
    dm_dthfl = rows[("DM", "DTHFL")]
    assert (dm_dthfl["role"], dm_dthfl["type"], dm_dthfl["core"]) == ("Record Qualifier", "Char", "Exp")
    visit_roles = {r["role"] for r in graph["edges"]["HAS_VARIABLE"] if r["var"] == "VISIT"}
    assert {"Synonym Qualifier", "Timing"} <= visit_roles   # 跨域 role 分歧存在于边上

def test_uses_ct_domains_property(graph):
    rows = {(r["var"], r["code"]): r["domains"] for r in graph["edges"]["USES_CT"]}
    assert rows[("FOCID", "C119013")] == ["OE"]   # 偏差 D2 的动机: 逐域精确
    assert "DM" in rows[("DTHFL", "C66742")]

def test_related_to_advisory_fidelity(graph):
    ae_fa = [r for r in graph["edges"]["RELATED_TO"] if r["src"] == "AE" and r["dst"] == "FA"]
    assert len(ae_fa) == 1
    r = ae_fa[0]
    assert r["advisory"] is True and r["fidelity"] == "curated_prose"
    assert r["category"] == "Findings About" and r["mechanism"] is None

def test_class_and_chapter_nodes(graph):
    sizes = {c["name"]: c["n_domains"] for c in graph["nodes"]["Class"]}
    assert sizes["Findings"] == 30 and sizes["Study Reference"] == 1
    assert {m["path"] for m in graph["nodes"]["ModelChapter"]} == {
        "model/02_observation_classes.md", "model/03_special_purpose_domains.md",
        "model/05_study_level_data.md", "model/06_relationship_datasets.md",
    }

def test_defhome_edge_shape(graph):
    rows = {r["var"]: r["chapter"] for r in graph["edges"]["DEFHOME"]}
    assert rows["APID"] == "model/06_relationship_datasets.md"
    assert len(rows) == 59

def test_load_meta_missing_key_fails_loud(tmp_path):
    bad = tmp_path / "meta.yaml"
    bad.write_text("meta_version: 1\ndomains: []\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing top-level key"):
        load_meta(bad)
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd branches/07_rag_kg/sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_build_neo4j.py -v`
Expected: 全部 FAIL, `ModuleNotFoundError: No module named 'scripts.build_neo4j'`

- [ ] **Step 3: 写实现 (纯函数部分)**

`scripts/build_neo4j.py`:

```python
"""Build the Neo4j exploration layer from data/meta/meta.yaml (SP4).

meta.yaml (SP1, reconcile-verified) is the ONLY source. Production answering
keeps running the in-memory DictBackend; this importer feeds a separate local
Neo4j (bolt://127.0.0.1:7687) for interactive exploration (Browser + cookbook).

Graph model (spec 2026-07-08 §3 + plan deviations D1-D4, data-grounded):
  Nodes: Domain(63, DI stub excluded) / Variable(1541 = 1523 IG + 18
         model-only) / Codelist(1005) / Class(8) / ModelChapter(4)
  Edges: HAS_VARIABLE(1917, per-domain role/type/core on the edge) /
         USES_CT(542 cross-domain union, `domains` list property for
         per-domain precision — C119013/FOCID lesson) / IN_CLASS(63) /
         DEFHOME(59, Variable->ModelChapter) / RELATED_TO(52, advisory)

Production isolation (spec hard constraint): NEVER import this module from
server/ — the neo4j driver lives in the dev extra only. The extract layer
below is pure (no neo4j import) so unit tests run with Neo4j stopped.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import yaml

Graph = dict[str, dict[str, list[dict[str, Any]]]]


def load_meta(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        meta = yaml.safe_load(fh)
    for key in ("meta_version", "domains", "codelists", "model_defhome"):
        if key not in meta:
            raise ValueError(f"meta.yaml missing top-level key: {key} ({path})")
    return meta


def extract_graph(meta: dict) -> Graph:
    real = [d for d in meta["domains"] if d["counts_toward_63"]]

    domain_nodes = [
        {"code": d["domain"], "label": d["label"], "class": d["class"],
         "structure": d["structure"], "n_variables": len(d["variables"])}
        for d in real
    ]

    # Variable nodes: first-seen attrs in meta["domains"] file order — same
    # semantics as MetaStore._var_attrs, so Browser node props match production.
    var_nodes: dict[str, dict] = {}
    has_variable: list[dict] = []
    ct_domains: dict[tuple[str, str], list[str]] = {}
    class_count: Counter[str] = Counter()
    in_class: list[dict] = []
    related: list[dict] = []
    for d in real:
        class_count[d["class"]] += 1
        in_class.append({"domain": d["domain"], "class": d["class"]})
        for r in d["relations_curated"]:
            related.append({"src": d["domain"], "dst": r["target"],
                            "mechanism": r["mechanism"], "note": r["note"],
                            "category": r["category"], "fidelity": r["fidelity"],
                            "advisory": True})
        for v in d["variables"]:
            if v["name"] not in var_nodes:
                var_nodes[v["name"]] = {
                    "name": v["name"], "label": v["label"], "role": v["role"],
                    "type": v["type"], "core": v["core"], "model_only": False,
                }
            has_variable.append({"domain": d["domain"], "var": v["name"],
                                 "role": v["role"], "type": v["type"], "core": v["core"]})
            for code in v["ct_codes"]:
                ct_domains.setdefault((v["name"], code), []).append(d["domain"])

    codelist_nodes = [
        {"code": c["ct_code"], "name": c["name"], "extensible": c["extensible"],
         "term_count": c["term_count"], "termfile": c["termfile"]}
        for c in meta["codelists"]
    ]
    known_codes = {c["code"] for c in codelist_nodes}
    uses_ct = [{"var": var, "code": code, "domains": sorted(doms)}
               for (var, code), doms in sorted(ct_domains.items())]

    class_nodes = [{"name": name, "n_domains": n}
                   for name, n in sorted(class_count.items())]

    # Deviation D3/D4: defhome targets are model chapter files; 18 of the 59
    # variables are model-level only (no IG domain) — materialize them as
    # Variable nodes flagged model_only so all 59 DEFHOME edges exist.
    chapter_nodes = [{"path": p} for p in sorted(set(meta["model_defhome"].values()))]
    defhome = [{"var": var, "chapter": chap}
               for var, chap in sorted(meta["model_defhome"].items())]
    for row in defhome:
        if row["var"] not in var_nodes:
            var_nodes[row["var"]] = {"name": row["var"], "model_only": True}

    # Loud-fail source validation (reconcile_meta._require spirit).
    real_codes = {d["domain"] for d in real}
    bad_rel = [r for r in related if r["dst"] not in real_codes]
    if bad_rel:
        raise ValueError(f"relations_curated targets not in real domains: {bad_rel}")
    bad_ct = [r for r in uses_ct if r["code"] not in known_codes]
    if bad_ct:
        raise ValueError(f"ct_codes not in codelists section: {bad_ct}")

    return {
        "nodes": {"Domain": domain_nodes,
                  "Variable": sorted(var_nodes.values(), key=lambda v: v["name"]),
                  "Codelist": codelist_nodes, "Class": class_nodes,
                  "ModelChapter": chapter_nodes},
        "edges": {"HAS_VARIABLE": has_variable, "USES_CT": uses_ct,
                  "IN_CLASS": in_class, "DEFHOME": defhome, "RELATED_TO": related},
    }
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd branches/07_rag_kg/sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_build_neo4j.py -v`
Expected: 10 passed。随后跑全套 `.venv/bin/python -m pytest scripts/tests/ -q` 确认零回归 + `ruff check scripts/build_neo4j.py scripts/tests/test_build_neo4j.py` + `mypy scripts/build_neo4j.py` 干净 (`.venv/bin/ruff` / `.venv/bin/mypy`)。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/scripts/build_neo4j.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_build_neo4j.py
git commit -m "feat(sp4): pure extract_graph — meta.yaml -> 5-label/5-edge graph rows (golden-anchored TDD)"
```

---

### Task 4: `build_neo4j.py` 导入层 `import_graph` + `main` (幂等全量导入)

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/scripts/build_neo4j.py` (追加导入层)
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_build_neo4j.py` (追加离线测试)

**Interfaces:**
- Consumes: Task 3 的 `extract_graph`/`load_meta`; Task 1 的 `.env` (`NEO4J_URI`/`NEO4J_USER`/`NEO4J_PASSWORD`); Task 2 已装载的服务
- Produces: `import_graph(driver, graph: Graph) -> dict[str, int]` (返回 {label/etype: 导入数}) + `main()`; 常量 `CONSTRAINTS` / `NODE_CYPHER` / `EDGE_CYPHER` / `_batches(rows, size=500)` (Task 5/6 文档引用)

- [ ] **Step 1: 写失败测试 (离线 — cypher 常量完备性 + 批切)**

追加到 `scripts/tests/test_build_neo4j.py` (**不连库**; 活库正确性由 Gate 1 reconcile 验, 不进 pytest):

```python
# ── Task 4: import layer (offline — no live Neo4j in pytest, Gate 3 rule) ──

def test_cypher_statements_cover_graph_keys(graph):
    from scripts.build_neo4j import CONSTRAINTS, EDGE_CYPHER, NODE_CYPHER
    assert set(NODE_CYPHER) == set(graph["nodes"])
    assert set(EDGE_CYPHER) == set(graph["edges"])
    assert len(CONSTRAINTS) == 5           # 每个节点标签一条唯一约束
    for label, stmt in NODE_CYPHER.items():
        assert f":{label}" in stmt and "UNWIND $rows" in stmt
    for etype, stmt in EDGE_CYPHER.items():
        assert f":{etype}" in stmt and "UNWIND $rows" in stmt and "MATCH" in stmt

def test_batches():
    from scripts.build_neo4j import _batches
    rows = [{"i": i} for i in range(1201)]
    chunks = list(_batches(rows, 500))
    assert [len(c) for c in chunks] == [500, 500, 201]
    assert [c["i"] for chunk in chunks for c in chunk] == list(range(1201))
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd branches/07_rag_kg/sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_build_neo4j.py -v`
Expected: 新增 2 个 FAIL, `ImportError: cannot import name 'CONSTRAINTS'`

- [ ] **Step 3: 写导入层实现**

追加到 `scripts/build_neo4j.py` (**neo4j import 放函数内**, 保持模块顶层可在无 driver 环境 import — pytest 纯函数测试不需要 driver):

```python
# ── import layer (requires the dev-extra neo4j driver + a live local Neo4j) ──

BATCH_SIZE = 500

CONSTRAINTS = [
    "CREATE CONSTRAINT domain_code IF NOT EXISTS FOR (n:Domain) REQUIRE n.code IS UNIQUE",
    "CREATE CONSTRAINT variable_name IF NOT EXISTS FOR (n:Variable) REQUIRE n.name IS UNIQUE",
    "CREATE CONSTRAINT codelist_code IF NOT EXISTS FOR (n:Codelist) REQUIRE n.code IS UNIQUE",
    "CREATE CONSTRAINT class_name IF NOT EXISTS FOR (n:Class) REQUIRE n.name IS UNIQUE",
    "CREATE CONSTRAINT chapter_path IF NOT EXISTS FOR (n:ModelChapter) REQUIRE n.path IS UNIQUE",
]

NODE_CYPHER = {
    "Domain": ("UNWIND $rows AS r CREATE (:Domain {code: r.code, label: r.label, "
               "class: r.class, structure: r.structure, n_variables: r.n_variables})"),
    # r.role 等对 model-only 行不存在 -> Cypher null -> 属性自然缺省, 无需分支
    "Variable": ("UNWIND $rows AS r CREATE (:Variable {name: r.name, label: r.label, "
                 "role: r.role, type: r.type, core: r.core, model_only: r.model_only})"),
    "Codelist": ("UNWIND $rows AS r CREATE (:Codelist {code: r.code, name: r.name, "
                 "extensible: r.extensible, term_count: r.term_count, termfile: r.termfile})"),
    "Class": "UNWIND $rows AS r CREATE (:Class {name: r.name, n_domains: r.n_domains})",
    "ModelChapter": "UNWIND $rows AS r CREATE (:ModelChapter {path: r.path})",
}

EDGE_CYPHER = {
    "HAS_VARIABLE": ("UNWIND $rows AS r MATCH (d:Domain {code: r.domain}) "
                     "MATCH (v:Variable {name: r.var}) "
                     "CREATE (d)-[:HAS_VARIABLE {role: r.role, type: r.type, core: r.core}]->(v)"),
    "USES_CT": ("UNWIND $rows AS r MATCH (v:Variable {name: r.var}) "
                "MATCH (c:Codelist {code: r.code}) "
                "CREATE (v)-[:USES_CT {domains: r.domains}]->(c)"),
    "IN_CLASS": ("UNWIND $rows AS r MATCH (d:Domain {code: r.domain}) "
                 "MATCH (k:Class {name: r.class}) CREATE (d)-[:IN_CLASS]->(k)"),
    "DEFHOME": ("UNWIND $rows AS r MATCH (v:Variable {name: r.var}) "
                "MATCH (m:ModelChapter {path: r.chapter}) CREATE (v)-[:DEFHOME]->(m)"),
    # mechanism 可为 null -> 属性缺省; cookbook 查询用 `r.mechanism IS NULL` 语义
    "RELATED_TO": ("UNWIND $rows AS r MATCH (a:Domain {code: r.src}) "
                   "MATCH (b:Domain {code: r.dst}) "
                   "CREATE (a)-[:RELATED_TO {mechanism: r.mechanism, note: r.note, "
                   "category: r.category, fidelity: r.fidelity, advisory: r.advisory}]->(b)"),
}


def _batches(rows: list[dict], size: int = BATCH_SIZE):
    for i in range(0, len(rows), size):
        yield rows[i:i + size]


def import_graph(driver: Any, graph: Graph) -> dict[str, int]:
    """Wipe + full deterministic rebuild. Idempotent: two runs -> identical
    node/edge sets (Gate 1 snapshot diff proves it)."""
    counts: dict[str, int] = {}
    with driver.session(database="neo4j") as session:
        session.run("MATCH (n) DETACH DELETE n")          # ~2.6k nodes: single tx fine
        for stmt in CONSTRAINTS:
            session.run(stmt)
        for label, rows in graph["nodes"].items():
            for chunk in _batches(rows):
                session.run(NODE_CYPHER[label], rows=chunk)
            counts[label] = len(rows)
        for etype, rows in graph["edges"].items():
            for chunk in _batches(rows):
                session.run(EDGE_CYPHER[etype], rows=chunk)
            counts[etype] = len(rows)
    return counts


def main() -> None:
    from dotenv import load_dotenv
    from neo4j import GraphDatabase

    root = Path(__file__).resolve().parents[1]            # scripts -> sdtm-rag
    load_dotenv(root / ".env")
    import os
    uri = os.environ.get("NEO4J_URI", "bolt://127.0.0.1:7687")
    user = os.environ.get("NEO4J_USER", "neo4j")
    password = os.environ.get("NEO4J_PASSWORD")
    if not password:
        raise SystemExit("NEO4J_PASSWORD missing — add it to sdtm-rag/.env (see deploy/README.md §Neo4j)")

    graph = extract_graph(load_meta(root / "data" / "meta" / "meta.yaml"))
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        driver.verify_connectivity()
        counts = import_graph(driver, graph)
    print("imported " + " ".join(f"{k}={v}" for k, v in counts.items()))


if __name__ == "__main__":
    main()
```

注意: `import os` 移到文件顶部 imports 区 (ruff I 规则); 上面内联只为展示归属。

- [ ] **Step 4: 跑测试 + 首次真导入**

```bash
cd branches/07_rag_kg/sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_build_neo4j.py -v      # 全 PASS
.venv/bin/python scripts/build_neo4j.py                              # 首次全量导入
source <(grep '^NEO4J_' .env)
cypher-shell -a "$NEO4J_URI" -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" \
  "MATCH (n) RETURN labels(n)[0] AS label, count(*) ORDER BY label;"
cypher-shell -a "$NEO4J_URI" -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" \
  "MATCH ()-[r]->() RETURN type(r) AS t, count(*) ORDER BY t;"
```

Expected: 导入 print 一行含 `Domain=63 Variable=1541 Codelist=1005 Class=8 ModelChapter=4 HAS_VARIABLE=1917 USES_CT=542 IN_CLASS=63 DEFHOME=59 RELATED_TO=52`; 两条 cypher-shell 计数与之逐项相同 (若 MATCH 因约束冲突或漏节点报错/缺数 → 规则 B 归档 `evidence/failures/sp4_attempt_N.md` 再修)。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/scripts/build_neo4j.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_build_neo4j.py
git commit -m "feat(sp4): idempotent wipe+rebuild neo4j importer (UNWIND batches, 5 uniqueness constraints)"
```

---

### Task 5: `reconcile_neo4j.py` 独立对账 + 幂等 snapshot 门 (Gate 1 / Rule A lane)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/scripts/reconcile_neo4j.py`
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_reconcile_neo4j.py` (只测 yaml 侧派生, 离线)
- Output: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp4_reconcile_gate.txt` (门 artifact)

**Interfaces:**
- Consumes: raw `data/meta/meta.yaml` (自行 yaml.safe_load 遍历) + 活 Neo4j (driver 只读)。**禁止 import** `scripts.build_neo4j` / `server.meta_store` / `server.graph_engine` (反过拟合硬约束; Rule D 审查项)
- Produces: `expected_from_yaml(meta_path) -> dict` + `reconcile(meta_path) -> list[dict]` (`{"check","expected","actual","ok"}`) + `snapshot(out_path)` (全图 canonical 文本导出, 幂等 diff 用); `main()` exit 0/1

- [ ] **Step 1: 写失败测试 (yaml 侧派生锚, 离线)**

`scripts/tests/test_reconcile_neo4j.py`:

```python
"""SP4 reconcile — yaml-side derivation anchors (offline; live checks are the
script's own job, run as Gate 1, never inside pytest)."""

from __future__ import annotations

from pathlib import Path

from scripts.reconcile_neo4j import expected_from_yaml

META_PATH = Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml"


def test_expected_counts_match_golden_anchors():
    exp = expected_from_yaml(META_PATH)
    assert exp["node_counts"] == {"Domain": 63, "Variable": 1541, "Codelist": 1005,
                                  "Class": 8, "ModelChapter": 4}
    assert exp["edge_counts"] == {"HAS_VARIABLE": 1917, "USES_CT": 542, "IN_CLASS": 63,
                                  "DEFHOME": 59, "RELATED_TO": 52}

def test_expected_neighborhood_derivation():
    exp = expected_from_yaml(META_PATH)
    dm = exp["domain_nbhd"]("DM")
    assert dm["in_class"] == "Special-Purpose"
    assert ("DTHFL", "Record Qualifier", "Char", "Exp") in dm["has_variable"]
    v = exp["variable_nbhd"]("VISIT")
    assert len(v["domains"]) == 36

def test_independence_no_forbidden_imports():
    src = (Path(__file__).resolve().parents[1] / "reconcile_neo4j.py").read_text(encoding="utf-8")
    for banned in ("build_neo4j", "meta_store", "graph_engine", "MetaStore", "GraphEngine"):
        assert banned not in src, f"reconcile must not reference {banned} (independence rule)"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd branches/07_rag_kg/sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_reconcile_neo4j.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.reconcile_neo4j'`

- [ ] **Step 3: 写实现**

`scripts/reconcile_neo4j.py`:

```python
"""Independent reconciliation for the SP4 Neo4j exploration layer (Gate 1).

Deliberately does NOT reuse the importer's traversal: expected values are
re-derived from a raw yaml.safe_load of data/meta/meta.yaml with its own code
shapes (Counter/set comprehensions), then compared against the live Neo4j via
read-only driver queries. Rule A lane: N=9 stratified entity neighborhoods
(3 Domain / 3 Variable / 2 Codelist / 1 Class, seeded RNG) compared edge-by-edge.

Honest disclosure (reconcile_meta.py discipline): both sides ultimately trace
to meta.yaml — this breaks *code-path* tautology (importer bug classes: dropped
rows, wrong direction, attr mixups, silent MATCH misses), not source error.
Source-vs-KB truth was already gated by SP1 reconcile_meta.py.

Usage:
  .venv/bin/python scripts/reconcile_neo4j.py                 # full gate, exit 0/1
  .venv/bin/python scripts/reconcile_neo4j.py --snapshot F    # canonical full-graph dump
"""

from __future__ import annotations

import os
import random
import sys
from collections import Counter
from pathlib import Path

import yaml
from dotenv import load_dotenv
from neo4j import GraphDatabase

SEED = 20260708


def _load(meta_path: Path) -> tuple[dict, list[dict]]:
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    real = [d for d in meta["domains"] if d["counts_toward_63"]]
    return meta, real


def expected_from_yaml(meta_path: Path) -> dict:
    meta, real = _load(meta_path)
    ig_vars = {v["name"] for d in real for v in d["variables"]}
    model_only = set(meta["model_defhome"]) - ig_vars
    pairs = {(v["name"], c) for d in real for v in d["variables"] for c in v["ct_codes"]}

    def domain_nbhd(code: str) -> dict:
        d = next(x for x in real if x["domain"] == code)
        return {
            "props": (d["label"], d["class"], d["structure"], len(d["variables"])),
            "has_variable": {(v["name"], v["role"], v["type"], v["core"]) for v in d["variables"]},
            "in_class": d["class"],
            "related_to": {(r["target"], r["mechanism"], r["category"], r["note"], r["fidelity"])
                           for r in d["relations_curated"]},
        }

    def variable_nbhd(name: str) -> dict:
        doms = {d["domain"] for d in real for v in d["variables"] if v["name"] == name}
        cts = {(c, tuple(sorted(d["domain"] for d in real
                                for v in d["variables"]
                                if v["name"] == name and c in v["ct_codes"])))
               for d2 in real for v2 in d2["variables"] if v2["name"] == name
               for c in v2["ct_codes"]}
        return {"domains": doms, "uses_ct": cts,
                "defhome": meta["model_defhome"].get(name)}

    def codelist_nbhd(code: str) -> dict:
        c = next(x for x in meta["codelists"] if x["ct_code"] == code)
        return {"props": (c["name"], c["extensible"], c["term_count"], c["termfile"]),
                "users": {var for (var, ct) in pairs if ct == code}}

    def class_nbhd(name: str) -> dict:
        doms = {d["domain"] for d in real if d["class"] == name}
        return {"n_domains": len(doms), "domains": doms}

    return {
        "node_counts": {"Domain": len(real), "Variable": len(ig_vars | model_only),
                        "Codelist": len(meta["codelists"]),
                        "Class": len({d["class"] for d in real}),
                        "ModelChapter": len(set(meta["model_defhome"].values()))},
        "edge_counts": {"HAS_VARIABLE": sum(len(d["variables"]) for d in real),
                        "USES_CT": len(pairs), "IN_CLASS": len(real),
                        "DEFHOME": len(meta["model_defhome"]),
                        "RELATED_TO": sum(len(d["relations_curated"]) for d in real)},
        "real_domains": sorted(d["domain"] for d in real),
        "ig_vars": sorted(ig_vars), "codelist_codes": sorted(c["ct_code"] for c in meta["codelists"]),
        "classes": sorted({d["class"] for d in real}),
        "domain_nbhd": domain_nbhd, "variable_nbhd": variable_nbhd,
        "codelist_nbhd": codelist_nbhd, "class_nbhd": class_nbhd,
    }


def _driver():
    root = Path(__file__).resolve().parents[1]
    load_dotenv(root / ".env")
    password = os.environ.get("NEO4J_PASSWORD")
    if not password:
        raise SystemExit("NEO4J_PASSWORD missing in sdtm-rag/.env")
    return GraphDatabase.driver(os.environ.get("NEO4J_URI", "bolt://127.0.0.1:7687"),
                                auth=(os.environ.get("NEO4J_USER", "neo4j"), password))


def _rows(session, cypher: str, **params) -> list:
    return [r.data() for r in session.run(cypher, **params)]


def reconcile(meta_path: Path) -> list[dict]:
    exp = expected_from_yaml(meta_path)
    report: list[dict] = []

    def check(name, expected, actual):
        report.append({"check": name, "expected": expected, "actual": actual,
                       "ok": expected == actual})

    with _driver() as driver, driver.session(database="neo4j") as s:
        got_nodes = {r["label"]: r["n"] for r in _rows(
            s, "MATCH (n) RETURN labels(n)[0] AS label, count(*) AS n")}
        got_edges = {r["t"]: r["n"] for r in _rows(
            s, "MATCH ()-[r]->() RETURN type(r) AS t, count(*) AS n")}
        for label, n in exp["node_counts"].items():
            check(f"nodes:{label}", n, got_nodes.get(label, 0))
        check("nodes:no_extra_labels", sorted(exp["node_counts"]), sorted(got_nodes))
        for etype, n in exp["edge_counts"].items():
            check(f"edges:{etype}", n, got_edges.get(etype, 0))
        check("edges:no_extra_types", sorted(exp["edge_counts"]), sorted(got_edges))

        # Rule A lane — N=9 stratified neighborhoods, edge-by-edge.
        rng = random.Random(SEED)
        for code in rng.sample(exp["real_domains"], 3):
            e = exp["domain_nbhd"](code)
            props = _rows(s, "MATCH (d:Domain {code:$c}) RETURN d.label AS l, d.class AS k, "
                             "d.structure AS st, d.n_variables AS nv", c=code)[0]
            check(f"nbhd:Domain:{code}:props", e["props"],
                  (props["l"], props["k"], props["st"], props["nv"]))
            hv = {(r["v"], r["role"], r["type"], r["core"]) for r in _rows(
                s, "MATCH (d:Domain {code:$c})-[h:HAS_VARIABLE]->(v:Variable) "
                   "RETURN v.name AS v, h.role AS role, h.type AS type, h.core AS core", c=code)}
            check(f"nbhd:Domain:{code}:HAS_VARIABLE", e["has_variable"], hv)
            k = _rows(s, "MATCH (d:Domain {code:$c})-[:IN_CLASS]->(k:Class) RETURN k.name AS k", c=code)
            check(f"nbhd:Domain:{code}:IN_CLASS", e["in_class"], k[0]["k"] if k else None)
            rel = {(r["t"], r["m"], r["cat"], r["note"], r["f"]) for r in _rows(
                s, "MATCH (d:Domain {code:$c})-[r:RELATED_TO]->(b:Domain) RETURN b.code AS t, "
                   "r.mechanism AS m, r.category AS cat, r.note AS note, r.fidelity AS f", c=code)}
            check(f"nbhd:Domain:{code}:RELATED_TO", e["related_to"], rel)
        for name in rng.sample(exp["ig_vars"], 3):
            e = exp["variable_nbhd"](name)
            doms = {r["d"] for r in _rows(
                s, "MATCH (d:Domain)-[:HAS_VARIABLE]->(v:Variable {name:$n}) RETURN d.code AS d", n=name)}
            check(f"nbhd:Variable:{name}:domains", e["domains"], doms)
            cts = {(r["c"], tuple(r["ds"])) for r in _rows(
                s, "MATCH (v:Variable {name:$n})-[u:USES_CT]->(c:Codelist) "
                   "RETURN c.code AS c, u.domains AS ds", n=name)}
            check(f"nbhd:Variable:{name}:USES_CT", e["uses_ct"], cts)
            dh = _rows(s, "MATCH (v:Variable {name:$n})-[:DEFHOME]->(m:ModelChapter) "
                          "RETURN m.path AS p", n=name)
            check(f"nbhd:Variable:{name}:DEFHOME", e["defhome"], dh[0]["p"] if dh else None)
        for code in rng.sample(exp["codelist_codes"], 2):
            e = exp["codelist_nbhd"](code)
            props = _rows(s, "MATCH (c:Codelist {code:$c}) RETURN c.name AS n, c.extensible AS x, "
                             "c.term_count AS tc, c.termfile AS tf", c=code)[0]
            check(f"nbhd:Codelist:{code}:props", e["props"],
                  (props["n"], props["x"], props["tc"], props["tf"]))
            users = {r["v"] for r in _rows(
                s, "MATCH (v:Variable)-[:USES_CT]->(c:Codelist {code:$c}) RETURN v.name AS v", c=code)}
            check(f"nbhd:Codelist:{code}:users", e["users"], users)
        for name in rng.sample(exp["classes"], 1):
            e = exp["class_nbhd"](name)
            doms = {r["d"] for r in _rows(
                s, "MATCH (d:Domain)-[:IN_CLASS]->(k:Class {name:$n}) RETURN d.code AS d", n=name)}
            check(f"nbhd:Class:{name}:domains", e["domains"], doms)
            nd = _rows(s, "MATCH (k:Class {name:$n}) RETURN k.n_domains AS nd", n=name)[0]["nd"]
            check(f"nbhd:Class:{name}:n_domains", e["n_domains"], nd)
    return report


def snapshot(out_path: Path) -> None:
    """Canonical full-graph dump (sorted lines) — run after each of two builds,
    byte-diff proves idempotency (spec §2)."""
    lines: list[str] = []
    with _driver() as driver, driver.session(database="neo4j") as s:
        for r in _rows(s, "MATCH (n) RETURN labels(n)[0] AS label, properties(n) AS p"):
            props = ";".join(f"{k}={r['p'][k]!r}" for k in sorted(r["p"]))
            lines.append(f"NODE|{r['label']}|{props}")
        for r in _rows(s, "MATCH (a)-[e]->(b) RETURN labels(a)[0] AS la, properties(a) AS pa, "
                          "type(e) AS t, properties(e) AS pe, labels(b)[0] AS lb, properties(b) AS pb"):
            key = lambda lab, p: p.get("code") or p.get("name") or p.get("path")  # noqa: E731
            props = ";".join(f"{k}={r['pe'][k]!r}" for k in sorted(r["pe"]))
            lines.append(f"EDGE|{r['t']}|{key(r['la'], r['pa'])}->{key(r['lb'], r['pb'])}|{props}")
    out_path.write_text("\n".join(sorted(lines)) + "\n", encoding="utf-8")
    print(f"wrote {out_path} ({len(lines)} lines)")


def main() -> None:
    here = Path(__file__).resolve()
    meta_path = here.parents[1] / "data" / "meta" / "meta.yaml"
    if "--snapshot" in sys.argv:
        snapshot(Path(sys.argv[sys.argv.index("--snapshot") + 1]))
        return
    report = reconcile(meta_path)
    for c in report:
        flag = "OK " if c["ok"] else "FAIL"
        exp_s, act_s = str(c["expected"]), str(c["actual"])
        if len(exp_s) > 120:            # 邻域集合太长, 摘要化输出
            exp_s, act_s = f"<set of {len(c['expected'])}>", f"<set of {len(c['actual'])}>"
        print(f"[{flag}] {c['check']}: expected={exp_s} actual={act_s}")
    n_fail = sum(not c["ok"] for c in report)
    print(f"{len(report) - n_fail}/{len(report)} checks passed")
    if n_fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: 跑离线测试 + 真门 (Gate 1) + 幂等门**

```bash
cd branches/07_rag_kg/sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_reconcile_neo4j.py -v   # 3 passed
.venv/bin/python scripts/reconcile_neo4j.py | tee evidence/checkpoints/sp4_reconcile_gate.txt
# 幂等门: 两次全量重建 -> canonical snapshot byte-diff
.venv/bin/python scripts/build_neo4j.py
.venv/bin/python scripts/reconcile_neo4j.py --snapshot /tmp/sp4_snap_a.txt
.venv/bin/python scripts/build_neo4j.py
.venv/bin/python scripts/reconcile_neo4j.py --snapshot /tmp/sp4_snap_b.txt
diff /tmp/sp4_snap_a.txt /tmp/sp4_snap_b.txt && echo IDEMPOTENT-PASS
echo "" >> evidence/checkpoints/sp4_reconcile_gate.txt
echo "idempotency: two rebuilds -> snapshot byte-diff empty (IDEMPOTENT-PASS $(date +%F))" >> evidence/checkpoints/sp4_reconcile_gate.txt
```

Expected: reconcile 全部 `[OK ]` + exit 0 (10 计数 + 2 无多余标签/边型 + 27 邻域 = 39 checks); diff 空输出 + `IDEMPOTENT-PASS`。任何 FAIL → 规则 B 归档 `evidence/failures/sp4_attempt_N.md` (含 FAIL 行 + 定位分析), 修 build_neo4j.py 后**全门重跑**。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/scripts/reconcile_neo4j.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_reconcile_neo4j.py branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp4_reconcile_gate.txt
git commit -m "feat(sp4): independent reconcile gate — counts + N=9 stratified neighborhoods + idempotency snapshot (Gate 1 PASS)"
```

---

### Task 6: `docs/cypher_cookbook.md` 7 条查询 + golden harness (Gate 2)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/docs/cypher_cookbook.md` (目录 `docs/` 新建)
- Create: `branches/07_rag_kg/sdtm-rag/eval/prod_wirein/sp4_cookbook_golden.py`
- Output: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp4_cookbook_golden.txt`

**Interfaces:**
- Consumes: 活 Neo4j (Task 4 已导入); `server.meta_store.MetaStore` + `server.graph_engine.GraphEngine` (期望值 lane — 生产等价; 与 Gate 1 的 raw-yaml lane 分工); `server.config.settings.meta_path`
- Produces: cookbook 7 条查询 (每条 = 用途一句话 + Cypher + 期望结果形状); harness `QUERIES: dict[str, str]` 常量 (与 cookbook 逐字同步, drift check 强制)

- [ ] **Step 1: 写 cookbook**

`docs/cypher_cookbook.md` — 头部说明 (数据来源 meta.yaml / 重建命令 / Browser 入口 / `:param` 用法 / **advisory 边警示** / model_only 变量说明), 然后 7 节。每节格式: `## N. 标题` + 用途一句话 + ```cypher 块 + 期望结果形状 (golden 数字)。7 条查询逐字如下 (harness 与之逐字同步):

```cypher
// ① 影响分析: 改一个 codelist 波及哪些域/变量 (参数化 C 码)
// USES_CT.domains = 该变量实际用此 CT 的域 (逐域精确, 与生产 GraphEngine 一致)
// :param code => 'C66742'
MATCH (c:Codelist {code: $code})<-[u:USES_CT]-(v:Variable)
UNWIND u.domains AS dom
RETURN c.code AS code, c.name AS codelist,
       count(DISTINCT v) AS n_variables, count(DISTINCT dom) AS n_domains,
       apoc.coll.sort(collect(DISTINCT dom)) AS domains
```

注意: 若未装 APOC (brew 裸装默认没有), 用 `collect(DISTINCT dom)` 去掉 apoc 排序 — **写 cookbook 时以实际可跑为准, harness 会验**。C66742 期望: 123 变量 / 41 域 (spec §5 的 44 是笔误, 见 plan 偏差 D1)。

```cypher
// ② 变量跨域分布: 哪些变量出现在 ≥ N 个域 (参数化阈值)
// :param min => 20
MATCH (d:Domain)-[:HAS_VARIABLE]->(v:Variable)
WITH v.name AS var, count(d) AS n_domains
WHERE n_domains >= $min
RETURN var, n_domains ORDER BY n_domains DESC, var
```

期望 (min=20): 8 行 — STUDYID 63, DOMAIN 59, USUBJID 55, EPOCH 44, TAETORD 43, VISIT 36, VISITDY 36, VISITNUM 36。

```cypher
// ③ same-class 邻域: 与某域同 observation class 的其他域
// :param dom => 'DM'
MATCH (d:Domain {code: $dom})-[:IN_CLASS]->(k:Class)<-[:IN_CLASS]-(o:Domain)
WHERE o.code <> d.code
RETURN k.name AS class, collect(o.code) AS siblings
```

期望 (DM): class=Special-Purpose, siblings={CO,SE,SM,SV} (集合相等, 顺序不定)。

```cypher
// ④ codelist co-users: 与某变量共用同一 CT 的其他变量
// :param var => 'AECONTRT'
MATCH (v:Variable {name: $var})-[:USES_CT]->(c:Codelist)<-[:USES_CT]-(o:Variable)
RETURN c.code AS code, c.name AS codelist, count(o) AS n_others
ORDER BY n_others DESC
```

期望 (AECONTRT): 1 行 C66742 "No Yes Response" n_others=122。

```cypher
// ⑤ 类罗盘: 某 observation class 下全部域 (SP3 因 class 名撞常用词未暴露 NL 的能力, Cypher 里安全)
// :param cls => 'Findings'
MATCH (d:Domain)-[:IN_CLASS]->(k:Class {name: $cls})
RETURN k.name AS class, k.n_domains AS n, collect(d.code) AS domains
```

期望 (Findings): n=30。全类概览变体: `MATCH (k:Class) RETURN k.name, k.n_domains ORDER BY k.name` → 8 行 (Events 7 / Findings 30 / Findings About 2 / Interventions 7 / Relationship 4 / Special-Purpose 5 / Study Reference 1 / Trial Design 7)。

```cypher
// ⑥ model_defhome 邻接: 某 model 章节定义的全部变量 (model_only=true 的变量只在 SDTM model 出现, 不在任何 IG 域)
// :param chapter => 'model/06_relationship_datasets.md'
MATCH (v:Variable)-[:DEFHOME]->(m:ModelChapter {path: $chapter})
RETURN m.path AS chapter, count(v) AS n, collect(v.name + CASE WHEN v.model_only THEN ' (model-only)' ELSE '' END) AS variables
```

期望: 变量集合与 `MetaStore.model_defhome_map` 中该章节的条目逐项相同 (数值由 harness 程序导)。

```cypher
// ⑦ most-shared 排名: 被最多变量共用的 codelist top-K
// :param k => 5
MATCH (c:Codelist)<-[u:USES_CT]-(v:Variable)
WITH c, count(v) AS n_variables, apoc.coll.toSet(apoc.coll.flatten(collect(u.domains))) AS doms
RETURN c.code AS code, c.name AS name, n_variables, size(doms) AS n_domains
ORDER BY n_variables DESC, code LIMIT $k
```

无 APOC 变体 (写 cookbook 时二选一, 与实际可跑一致):

```cypher
MATCH (c:Codelist)<-[u:USES_CT]-(v:Variable)
UNWIND u.domains AS dom
WITH c, count(DISTINCT v) AS n_variables, count(DISTINCT dom) AS n_domains
RETURN c.code AS code, c.name AS name, n_variables, n_domains
ORDER BY n_variables DESC, code LIMIT $k
```

期望 (k=5): C66742 123/41, C71620 58/32, C66789 36/36, C66728 26/9, C74456 19/19 — 与 `GraphEngine.most_shared_codelists(5)` 逐项一致。

另加一节「⑧ 可视化起点 (Browser 画布)」非 golden 查询 2 条 (如 `MATCH p=(d:Domain {code:'AE'})-[:RELATED_TO]->() RETURN p` 看 advisory 邻域; `MATCH p=(d:Domain)-[:IN_CLASS]->(:Class {name:'Trial Design'}) RETURN p`), 标注 "探索用, 不进 golden 门"。

- [ ] **Step 2: 写 golden harness**

`eval/prod_wirein/sp4_cookbook_golden.py`:

```python
"""SP4 Gate 2 — every cookbook query executed via driver, anchored to the
production MetaStore/GraphEngine (equivalence lane; Gate 1 covers raw-yaml lane).
Also fails if a QUERIES entry has drifted from docs/cypher_cookbook.md text.
Run: .venv/bin/python eval/prod_wirein/sp4_cookbook_golden.py"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from server.config import settings          # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore      # noqa: E402

QUERIES: dict[str, str] = {
    # 与 docs/cypher_cookbook.md 各节 cypher 块逐字相同 (drift check 强制)
    "impact": "...",          # 实现时从写定的 cookbook 逐字拷贝 ①
    "min_domains": "...",     # ②
    "same_class": "...",      # ③
    "co_users": "...",        # ④
    "class_compass": "...",   # ⑤
    "defhome": "...",         # ⑥
    "most_shared": "...",     # ⑦
}


def main() -> int:
    load_dotenv(ROOT / ".env")
    cookbook = (ROOT / "docs" / "cypher_cookbook.md").read_text(encoding="utf-8")
    store = MetaStore(settings.meta_path)
    engine = GraphEngine(store)
    fails = 0

    def gate(name: str, ok: bool, detail: str) -> None:
        nonlocal fails
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
        fails += 0 if ok else 1

    for name, q in QUERIES.items():
        gate(f"drift:{name}", q.strip() in cookbook, "query text verbatim in cookbook")

    with GraphDatabase.driver(
        os.environ.get("NEO4J_URI", "bolt://127.0.0.1:7687"),
        auth=(os.environ.get("NEO4J_USER", "neo4j"), os.environ["NEO4J_PASSWORD"]),
    ) as driver, driver.session(database="neo4j") as s:
        rec = s.run(QUERIES["impact"], code="C66742").single()
        truth = engine.impact_of_codelist("C66742")
        gate("impact:C66742", (rec["n_variables"], rec["n_domains"])
             == (truth["n_variables"], truth["n_domains"]),
             f"{rec['n_variables']}/{rec['n_domains']} vs engine {truth['n_variables']}/{truth['n_domains']} (期望 123/41)")
        rec2 = s.run(QUERIES["impact"], code="C119013").single()
        t2 = engine.impact_of_codelist("C119013")
        gate("impact:C119013", (rec2["n_variables"], rec2["n_domains"])
             == (t2["n_variables"], t2["n_domains"]),
             f"逐域精确回归 (D2): {rec2['n_variables']}/{rec2['n_domains']} vs engine (期望 x/1 非 x/3)")

        rows = [(r["var"], r["n_domains"]) for r in s.run(QUERIES["min_domains"], min=20)]
        gate("min_domains:20", rows == engine.variables_in_min_domains(20),
             f"{len(rows)} rows vs engine (期望 8)")

        rec = s.run(QUERIES["same_class"], dom="DM").single()
        gate("same_class:DM", sorted(rec["siblings"]) == engine.same_class_domains("DM"),
             f"{sorted(rec['siblings'])} (期望 CO,SE,SM,SV)")

        rows = [(r["code"], r["n_others"]) for r in s.run(QUERIES["co_users"], var="AECONTRT")]
        truth_cu = engine.codelist_co_users("AECONTRT")
        gate("co_users:AECONTRT",
             rows == [(c, len(v["others"])) for c, v in sorted(truth_cu.items())],
             f"{rows} (期望 [('C66742', 122)])")

        rec = s.run(QUERIES["class_compass"], cls="Findings").single()
        gate("class_compass:Findings", sorted(rec["domains"]) == engine.domains_in_class("Findings")
             and rec["n"] == 30, f"n={rec['n']} (期望 30)")

        chap = "model/06_relationship_datasets.md"
        rec = s.run(QUERIES["defhome"], chapter=chap).single()
        truth_dh = sorted(v for v, p in store.model_defhome_map().items() if p == chap)
        got = sorted(x.replace(" (model-only)", "") for x in rec["variables"])
        gate("defhome:ch06", got == truth_dh, f"{rec['n']} vars vs store {len(truth_dh)}")

        rows = [(r["code"], r["n_variables"], r["n_domains"])
                for r in s.run(QUERIES["most_shared"], k=5)]
        truth_ms = [(t["code"], t["n_variables"], t["n_domains"])
                    for t in engine.most_shared_codelists(5)]
        gate("most_shared:top5", rows == truth_ms, f"{rows}")

    print(f"{'ALL PASS' if fails == 0 else f'{fails} FAIL'}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

实现时把 `QUERIES` 的 `"..."` 换成写定 cookbook 后的逐字 Cypher (先写 cookbook, 后拷进 harness; drift check 保证两边不散)。`store.model_defhome_map()` / `engine.*` 签名已在 SP2/SP3 存在, 不新增 server 代码。

- [ ] **Step 3: 跑 Gate 2**

```bash
cd branches/07_rag_kg/sdtm-rag
.venv/bin/python eval/prod_wirein/sp4_cookbook_golden.py | tee evidence/checkpoints/sp4_cookbook_golden.txt
```

Expected: 全 PASS (7 drift + 9 golden), exit 0。任何 FAIL → 规则 B 归档后修 (查询错改 cookbook+harness 同步; 数据错回 Task 3/4 修并重跑 Gate 1)。

- [ ] **Step 4: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/docs/cypher_cookbook.md branches/07_rag_kg/sdtm-rag/eval/prod_wirein/sp4_cookbook_golden.py branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp4_cookbook_golden.txt
git commit -m "docs(sp4): cypher cookbook (7 anchored queries + viz starters) + golden harness vs GraphEngine (Gate 2 PASS)"
```

---

### Task 7: 生产隔离门 — 停机 pytest + composite byte-identical + grep 闸 (Gate 3)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/eval/prod_wirein/sp4_isolation_probe.py`
- Output: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp4_isolation_gate.txt`

**Interfaces:**
- Consumes: `server.main.maybe_build_answerer(settings)` (生产 composite 接线, SP2→AGG→SP3 顺序; resolve(query) → StructuredFacts|None, 字段 text_block/checkable_counts/advisory_block — 全确定性, 无 LLM)
- Produces: `sp4_isolation_probe.py <out.json>` — 固定 12 题 battery 的 canonical dump; Neo4j 停/起两态 byte-diff 的证据

- [ ] **Step 1: 写探针**

`eval/prod_wirein/sp4_isolation_probe.py`:

```python
"""SP4 Gate 3 — production must be byte-identical with Neo4j stopped vs running.
Dumps the deterministic composite resolve() output for a fixed 12-query battery.
Run twice (Neo4j down / up), then `diff` the two dumps.
Run: .venv/bin/python eval/prod_wirein/sp4_isolation_probe.py /tmp/sp4_iso_<state>.json"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.config import settings          # noqa: E402
from server.main import maybe_build_answerer  # noqa: E402

BATTERY = [
    # SP2 结构化 (计数/穷举/属性/CT)
    "How many domains are in the SDTM IG?",
    "Which domains contain the variable TAETORD?",
    "What are the variables in the DM domain?",
    "Which codelist does DTHFL use?",
    "Is AESER required in AE?",
    # AGG 聚合
    "Which variables appear in at least 30 domains?",
    "What's the most reused controlled terminology?",
    # SP3 图 (impact / relationship)
    "What is affected if codelist C66742 changes?",
    "Which domains are impacted by changing EPOCH?",
    "How is AE related to other domains?",
    "Which domains belong to the same class as VS?",
    # 检索型 (通道应 silent — None 也是被钉住的输出)
    "What does the EX domain describe?",
]


def main() -> None:
    out = Path(sys.argv[1])
    answerer = maybe_build_answerer(settings)
    assert answerer is not None, "composite channels off — flags drifted?"
    dump = []
    for q in BATTERY:
        facts = answerer.resolve(q)
        dump.append({"query": q, "facts": None if facts is None else asdict(facts)})
    out.write_text(json.dumps(dump, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"wrote {out} ({sum(1 for d in dump if d['facts']) } fired / {len(dump)})")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 跑 Gate 3 (三闸)**

```bash
cd branches/07_rag_kg/sdtm-rag
{
echo "== Gate 3 run $(date +%F) =="
# 闸 1: Neo4j 停机 -> 全套 pytest 全绿
launchctl bootout gui/$(id -u)/com.sdtmrag.neo4j 2>/dev/null || true
sleep 3
lsof -nP -iTCP:7687 -sTCP:LISTEN || echo "neo4j DOWN confirmed"
.venv/bin/python -m pytest scripts/tests/ -q 2>&1 | tail -2
# 闸 2: 停机/运行 composite byte-identical
.venv/bin/python eval/prod_wirein/sp4_isolation_probe.py /tmp/sp4_iso_off.json
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist
sleep 25
.venv/bin/python eval/prod_wirein/sp4_isolation_probe.py /tmp/sp4_iso_on.json
diff /tmp/sp4_iso_off.json /tmp/sp4_iso_on.json && echo "BYTE-IDENTICAL PASS"
# 闸 3: server/ 零 neo4j 引用 (import 级 + 小写字面量; 既有 'Neo4j' 大写 docstring 一处是设计注释, 允许)
grep -rniE '(import|from)[[:space:]]+neo4j' server/ && echo "IMPORT-GREP FAIL" || echo "import-grep clean"
grep -rn 'neo4j' server/ --include='*.py' && echo "LITERAL-GREP FAIL (小写命中须逐条判定)" || echo "lowercase-literal-grep clean"
.venv/bin/python -c "import sys; import server.main; assert not any(m.startswith('neo4j') for m in sys.modules), sorted(m for m in sys.modules if m.startswith('neo4j')); print('runtime-import clean')"
} 2>&1 | tee evidence/checkpoints/sp4_isolation_gate.txt
```

Expected: pytest `passed` 零 fail (停机态); `BYTE-IDENTICAL PASS`; 三条 grep/runtime 闸全 clean。fired 数期望 11/12 (最后一题检索型 silent; 实测为准, 关键是 off/on 两态相同)。任何闸破 → 规则 B 归档; 若 byte-diff 非空 = server 被 Neo4j 状态影响, 属 BLOCKER 级设计破坏, 必须先修再继续。

- [ ] **Step 3: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/eval/prod_wirein/sp4_isolation_probe.py branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp4_isolation_gate.txt
git commit -m "eval(sp4): production-isolation gate — pytest green with neo4j down + composite byte-identical + zero server refs (Gate 3 PASS)"
```

---

### Task 8: Rule D 异 type 全量审 (Gate 4)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp4_ruleD_review.md`

**Interfaces:**
- Consumes: Task 1-7 全 diff (`git log --oneline` 找 Task 1 前的 commit 作 BASE)
- Produces: verdict + findings 清单 + 逐条处置记录; BLOCKER/HIGH 修复后相关门重绿

- [ ] **Step 1: 派异 type reviewer 全量审**

派 1 个 `feature-dev:code-reviewer` subagent (与实现 lane 异 type), prompt 给出:
- spec 路径 `docs/superpowers/specs/2026-07-08-sp4-neo4j-exploration-design.md` + 本 plan 路径 (含偏差 D1-D4 段);
- diff 范围: `git diff <BASE>..HEAD -- branches/07_rag_kg/sdtm-rag/`;
- 审查重点 (spec §5 gate 4 四项 + 偏差):
  1. **导入正确性**: extract_graph 有没有丢行/错向/属性错位; EDGE_CYPHER 的 MATCH 若不命中会**静默跳过** — reconcile 计数是否足以兜住 (对照 silent-failure 视角);
  2. **幂等**: wipe+rebuild + snapshot diff 的证明是否完备 (约束重建、事务边界);
  3. **对账独立性**: reconcile_neo4j.py 是否真的没抄 build_neo4j 遍历 (代码形状对比), banned-import 测试是否可绕过;
  4. **安全姿态**: 密码是否可能入 git (.env/.env.example/plist/evidence 逐个查), localhost 双端口证据, runbook 是否引导明文密码落盘他处;
  5. **偏差 D1-D4** 是否数据接地、有没有更优建模 (尤其 D4 model_only 的 18 节点会不会污染 cookbook 计数查询)。
- 产出 verdict + findings 写入 `evidence/checkpoints/sp4_ruleD_review.md`。

- [ ] **Step 2: findings 处置 + 重绿**

BLOCKER/HIGH 必修, MED/LOW 逐条决策记录 (修/defer/reject + 理由) 写进 review md。任何代码改动后重跑受影响的门: Gate 1 (`reconcile_neo4j.py` + 幂等 diff) / Gate 2 (`sp4_cookbook_golden.py`) / Gate 3 (三闸) / 全套 pytest + ruff + mypy, 更新对应 artifact。

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "audit(sp4): Rule D cross-type review — findings resolved, all four gates re-green"
```

---

### Task 9: 收口 — 证据 checkpoint + RETROSPECTIVE + Chain 07_RAG 文档链

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp4_neo4j_summary.md`
- Create: `branches/07_rag_kg/sdtm-rag/RETROSPECTIVE_sp4.md` (规则 C)
- Modify: `branches/07_rag_kg/sdtm-rag/KG_ROADMAP.md`
- Modify: `.work/meta/worklog/phase_07_rag_kg.md` (repo-root)
- Modify: `docs/PROGRESS.md` (repo-root)
- Modify: `branches/07_rag_kg/_progress.json` (若存在, Tier 2 schema 追加)

- [ ] **Step 1: 写 `sp4_neo4j_summary.md`**

四门验收表 (门名 / 命令 / 实测结果 / artifact 路径, 数字填实测值) + 交付物清单 (脚本/plist/cookbook/runbook) + 偏差 D1-D4 披露 + 末尾「限制/诚实缺口:」行 (至少含: Term 节点未物化 (spec §3 backlog) / webchat Graph tab 二期 / 对账两侧同源 meta.yaml 的披露 / heap 配置走 env 还是 conf 的实际落点)。

- [ ] **Step 2: 写 `RETROSPECTIVE_sp4.md` (规则 C, 三段起)**

保留下来的做法 / 必须补上的缺口 / 关键决策复盘 (至少覆盖: 4 个 spec 偏差为什么 plan 期就该抓到 vs brainstorm 期; 纯函数/导入层分层让 pytest 停机全绿是否值得沉淀为惯例; launchd+brew 运维一致性)。

- [ ] **Step 3: KG_ROADMAP + worklog + PROGRESS + _progress**

- `KG_ROADMAP.md`: 头部时间线加一行 (SP4 DONE ✅ 日期 + 一句话); 「恢复方式」行改指 SP5 (下一单元, 需另起 brainstorm); 子项目清单 SP4 行标 DONE; 照 SP1-SP3/AGG 格式加「SP4 DONE (日期) — 交付与发现」段 (产出 / 偏差 D1-D4 / 四门结果 / 关键发现)。
- `.work/meta/worklog/phase_07_rag_kg.md`: append 本单元 work record (做了什么 / 四门 / 产出 / next=SP5 brainstorm)。
- `docs/PROGRESS.md`: 「最后更新」行改 SP4 摘要 (原内容退为 "前:")。
- `branches/07_rag_kg/_progress.json`: 存在则按 Tier 2 schema 追加 SP4 条目。

- [ ] **Step 4: 终 commit + push**

```bash
git add -A
git commit -m "SP4 DONE: Neo4j 探索层收口 (四门全过: 独立对账+幂等 / cookbook golden 7 条 / 停机 byte-identical / Rule D) — brew+launchd, 数据接地偏差 D1-D4 披露"
git push origin main
```

- [ ] **Step 5: 汇报**

向用户一段汇报: 四门结果 + Browser 入口 (http://127.0.0.1:7474 + cookbook 路径) + 偏差 D1-D4 一句话 + 提示 SP5 (图增强校验器) 是独立设计单元、需另起 brainstorm。

---

## Self-Review 记录 (写计划时已跑)

- **Spec coverage**: §1 三决策 → Task 1/2 (brew+launchd) + 全 plan (交付面三件套); §2 组件 → build_neo4j (T3/4), plist (T2), cookbook (T6), reconcile (T5); §3 建模 → T3 (含 4 项数据接地偏差, 头部披露); §4 数据流运维 → T2 runbook + T4 幂等 + T7 隔离验证义务; §5 四门 → T5/T6/T7/T8 一一对应, Rule A=Gate 1 N=9 (spec 要求 N≥8) 写进 PLAN; §6 交付物/文档链 → T9; §7 范围外 5 项均未越界 (Neo4jBackend 未接 seam, Term 未物化, 无 LLM→Cypher)。无缺口。
- **Placeholder scan**: Task 6 harness 的 `QUERIES` 值标注 "实现时从写定 cookbook 逐字拷贝" 且 7 条 Cypher 已在 Step 1 逐字给出, drift check 强制同步 — 非 TBD。其余无 TODO/TBD/"适当处理"。
- **Type consistency**: `extract_graph` 返回键 (Domain/Variable/Codelist/Class/ModelChapter; HAS_VARIABLE/USES_CT/IN_CLASS/DEFHOME/RELATED_TO) 与 T4 `NODE_CYPHER`/`EDGE_CYPHER` 键、T5 reconcile 查询、T6 cookbook 标签逐一核对一致; row 键 (code/label/class/structure/n_variables; name/model_only; var/code/domains; src/dst/mechanism/note/category/fidelity/advisory; var/chapter) 在 T3 实现、T4 Cypher `r.*`、T5 邻域比对三处一致; golden 数字与头部表全一致 (123/41, 1541=1523+18, 542, 59, 52)。
