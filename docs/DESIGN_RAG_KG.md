# SDTM RAG + Knowledge Graph Design Spec

> Created: 2026-04-16
> Status: Approved
> Author: Claude (brainstorming session with user)

---

## 1. Goals & Requirements

### 1.1 What We're Building

A two-phase intelligent retrieval and validation system for the SDTM knowledge base (293 Markdown files, 9.8MB), enabling:

1. **Semantic Q&A** — Ask natural language questions about SDTM, get accurate answers with source citations
2. **Relationship Discovery** — Explore cross-domain relationships, CT usage, variable distributions
3. **Dataset Validation** — Upload SDTM-mapped datasets, get completeness and correctness assessments

### 1.2 User Profiles

- **Primary**: User themselves — local AI-assisted SDTM queries and dataset validation
- **Secondary**: Team members — internal service for SDTM knowledge lookup
- **Tertiary**: Technical exploration — learning vector DB and knowledge graph technologies

### 1.3 Success Criteria

| Criteria | Metric |
|----------|--------|
| Answer accuracy | Better than giving AI raw Markdown files |
| Response speed | Complex cross-domain queries in seconds |
| Discoverability | Surface hidden relationships (e.g., "changing this CT affects which domains?") |
| Validation coverage | Catch Req/Exp completeness, CT compliance, business rule violations |

### 1.4 Constraints & Decisions

- **Local-first**: Everything runs locally via Docker Compose; cloud deployment deferred
- **Provider-agnostic**: LLM layer supports Claude, GPT, and others via LiteLLM
- **Cost-insensitive**: Prioritize quality over cost optimization
- **Tech stack**: Python (RAG ecosystem maturity), FastAPI, Streamlit
- **Read-only source**: `knowledge_base/` is never modified; `sdtm-rag/` is a separate project

---

## 2. Architecture Overview

```
sdtm-rag/
├── scripts/                        # Data processing
│   ├── ingest.py                   # Markdown → chunks → Embedding → Chroma
│   ├── build_graph.py              # YAML → Neo4j nodes/relationships (Phase 2)
│   ├── parse_dataset.py            # Parse user-uploaded datasets (CSV/XPT/SAS7BDAT)
│   └── shared/                     # Chunking strategies, text cleaning
├── server/                         # API layer (FastAPI)
│   ├── main.py                     # API entry point
│   ├── router.py                   # Intent classifier + query routing
│   ├── rag.py                      # Vector retrieval + LLM Q&A
│   ├── graph.py                    # Knowledge graph queries (Phase 2)
│   ├── validator.py                # Rule-based dataset validation
│   ├── reviewer.py                 # RAG-assisted semantic review
│   └── config.py                   # Model/DB configuration
├── ui/                             # Streamlit frontend
├── data/                           # Local data storage
│   ├── chroma/                     # Chroma vector DB files
│   └── graph/                      # Neo4j data (Phase 2)
├── eval/                           # Evaluation scripts + test Q&A pairs
├── docker-compose.yml              # Chroma + Neo4j + FastAPI
└── pyproject.toml
```

### Two-Phase Roadmap

| | Phase 1: RAG + Validation | Phase 2: + Knowledge Graph |
|---|---|---|
| **Data input** | `ingest.py` — Markdown → Chroma | `build_graph.py` — YAML → Neo4j |
| **Query path** | `rag.py` — vector retrieval → LLM | `router.py` intent routing → rag/graph |
| **Validation** | `validator.py` + `reviewer.py` | Graph-enhanced cross-domain checks |
| **Prerequisite** | None (uses existing 293 md files) | P3 structured metadata (YAML) |

---

## 3. Phase 1: RAG Pipeline

### 3.1 Chunking Strategy

Different file types require different chunking approaches:

| File Type | Count | Chunking Strategy | Rationale |
|-----------|-------|-------------------|-----------|
| spec.md | 63 | Per variable (each `###` heading) | Variable is the atomic query unit |
| assumptions.md | 63 | Per numbered item ("1.", "2.") | Each assumption is an independent rule |
| examples.md | 63 | Per Example heading (with full data table) | Example is a complete context unit; tables must not be split |
| chapters/ | 6 | By `##` section, large sections split at `###` | Adaptive to varying section sizes |
| model/ | 6 | By `##` section | Regular structure, section-level chunks |
| terminology/ | 91 | Per codelist (`###` heading) | One codelist is a complete query unit |
| ROUTING.md | 1 | Not chunked — injected as system prompt | Routing rules for LLM, not for retrieval |
| VARIABLE_INDEX.md | 1 | Split by alphabetical groups | Too large (131KB) for single chunk |

### 3.2 Chunk Metadata

Every chunk carries structured metadata for filtered retrieval:

```python
{
    "source": "domains/AE/spec.md",      # Source file path
    "domain": "AE",                       # Domain (63 values)
    "class": "Events",                    # Observation class (7 values)
    "file_type": "spec",                  # spec | assumptions | examples | chapter | model | terminology
    "section": "AETERM",                  # Section/variable name
    "chunk_index": 0                      # Chunk sequence number
}
```

Metadata enables **filtered retrieval**: when user asks about "AE variables", filter `domain=AE` first, then semantic rank within the subset. This prevents irrelevant cross-domain noise.

### 3.3 Embedding Model

| Option | Dimensions | Multilingual | Cost | Role |
|--------|-----------|-------------|------|------|
| OpenAI `text-embedding-3-small` | 1536 | Good | ~$0.02/1M tokens | Primary choice |
| OpenAI `text-embedding-3-large` | 3072 | Better | ~$0.13/1M tokens | Precision upgrade |
| Open-source `bge-m3` (local) | 1024 | Good | Free | GPU-required fallback |

Knowledge base is ~9.8MB text. One full embedding pass costs < $0.01.

### 3.4 Vector Database: Chroma

- Pure Python, `pip install chromadb`, zero ops
- Local disk persistence (`data/chroma/`)
- Supports metadata filtering (domain, class, file_type)
- ~3000-5000 chunks is well within Chroma's capacity

### 3.5 Retrieval + Q&A Flow

```
User question
  │
  ├─[1] ROUTING.md injected as system prompt
  │     (tells LLM question types and lookup strategies)
  │
  ├─[2] LLM analyzes question → extracts filter conditions
  │     (domain? class? file_type?)
  │
  ├─[3] Chroma retrieval: metadata filter + semantic Top-K (K=10~20)
  │
  ├─[4] Optional Rerank: Cohere Rerank or LLM reranking, take Top-5
  │
  └─[5] LLM generates answer with source citations (file path + section)
```

### 3.6 LLM Abstraction: LiteLLM

```python
import litellm
response = litellm.completion(
    model="claude-sonnet-4-20250514",  # or "gpt-4o", "deepseek-chat"
    messages=[system_prompt, context, user_query]
)
```

Provider-agnostic. Configure API keys and default model in `config.py`.

### 3.7 Frontend: Streamlit

- Chat interface with multi-turn conversation
- Source citations with expandable original text
- Sidebar: domain/type filters, model selector
- Dataset upload panel (for validation feature)

---

## 4. Dataset Validation Module

### 4.1 Overview

Two-layer validation system: rule-based engine (deterministic) + RAG-assisted semantic review (LLM-powered).

Input formats: CSV (primary), XPT, SAS7BDAT.

### 4.2 Layer 1: Rule-Based Validation (validator.py)

Automated checks using spec.md structured data:

| Check | Rule Source | Example |
|-------|-----------|---------|
| **Req completeness** | spec.md Core=Req | AETERM missing → ERROR |
| **Exp completeness** | spec.md Core=Exp | AEACN empty → WARN |
| **CT compliance** | terminology/ Codelists | AESER="Yes" not in C66742 → ERROR |
| **Data type** | spec.md Type (Char/Num) | AESEQ="abc" for Num field → ERROR |
| **Primary key uniqueness** | STUDYID + USUBJID + --SEQ | Duplicate key → ERROR |
| **Cross-domain consistency** | DM as reference | USUBJID not in DM → ERROR |
| **Variable naming** | spec.md variable list | Unknown variable AEXYZ → WARN |

No LLM needed. Accuracy ~100%.

### 4.3 Layer 2: Semantic Review (reviewer.py)

RAG-powered deep review using knowledge base rules:

| Check | Knowledge Source | Example |
|-------|-----------------|---------|
| **Business rule compliance** | assumptions.md | AESER=Y but all seriousness vars empty |
| **Logical consistency** | assumptions.md | AESTDTC > AEENDTC (start after end) |
| **Pattern comparison** | examples.md | User's CMDOSFRQ usage vs standard examples |
| **Completeness assessment** | spec.md + assumptions.md | Expected variables present but never populated |
| **Cross-domain relationship** | ch08 + Cross References | RELREC references exist but targets missing |

### 4.4 Output: Validation Report

```markdown
## SDTM Validation Report — AE Domain

### Completeness: 87%
- Req variables: 12/12 PASS
- Exp variables: 8/10 (missing: AEACN, AEREL)
- Perm variables: 5/15 (normal, Perm is optional)

### Issues
| # | Severity | Variable | Issue | Rule Source |
|---|----------|----------|-------|-------------|
| 1 | ERROR | AESER | Row 3: "Yes" not in CT C66742, should be "Y" | terminology/core/ae.md |
| 2 | ERROR | AESHOSP | Row 3: AESER="Y" but all seriousness vars empty | AE assumptions |
| 3 | WARN | AEACN | Column entirely empty, Exp variable | spec.md Core=Exp |
| 4 | INFO | AEGRPID | Not used; consider if multiple AE records exist per event | AE Example 4 |

### Recommendations
- ...
```

### 4.5 Data Flow

```
User uploads dataset (CSV/XPT)
  │
  ├─[1] parse_dataset.py: parse into DataFrame, detect domain
  │
  ├─[2] validator.py: rule-based checks (Req/CT/PK/type)
  │     → deterministic error list
  │
  ├─[3] reviewer.py: RAG retrieves relevant assumptions + examples
  │     → LLM evaluates business logic, patterns, completeness
  │
  └─[4] Generate structured validation report (Markdown + JSON)
```

---

## 5. Phase 2: Knowledge Graph + Hybrid Routing

### 5.1 Prerequisite: P3 Structured Metadata

Complete P3 — convert spec.md to YAML for graph import:

```yaml
# domains/AE/meta.yaml
domain: AE
class: Events
label: Adverse Events
structure: "One record per adverse event per subject"
variables:
  - name: AETERM
    role: Topic
    type: Char
    core: Req
    ct_code: null
  - name: AESER
    role: Qualifier
    type: Char
    core: Exp
    ct_code: C66742
relationships:
  - target: FA
    type: findings_about
    mechanism: RELREC
  - target: CM
    type: concomitant_treatment
    mechanism: RELREC
```

Auto-generated by Python script from spec.md + Cross References. 63 domains.

### 5.2 Graph Schema

**Nodes:**

| Type | Count | Attributes | Source |
|------|-------|-----------|--------|
| Domain | 63 | name, label, class, structure | meta.yaml |
| Variable | ~1523 | name, type, role, core | meta.yaml |
| Codelist | ~1005 | code, name, extensible | terminology/ |
| Term | ~37939 | code, value, codelist | terminology/ |
| Class | 7 | name | model/ |
| Chapter | 6 | number, title | chapters/ |

**Relationships:**

| Relationship | Direction | Meaning |
|-------------|-----------|---------|
| HAS_VARIABLE | Domain → Variable | Domain contains variable |
| BELONGS_TO | Domain → Class | Domain belongs to observation class |
| USES_CT | Variable → Codelist | Variable uses controlled terminology |
| CONTAINS_TERM | Codelist → Term | Codelist contains term |
| RELATED_TO | Domain → Domain | Inter-domain relationship (+mechanism) |
| DESCRIBED_IN | Domain → Chapter | Rules described in chapter |
| SHARED_VARIABLE | Variable → Variable | Same-name variable across domains |

### 5.3 Graph Query Examples

```cypher
-- "What Codelist does AESER use? What other variables use it?"
MATCH (v:Variable {name:'AESER'})-[:USES_CT]->(c:Codelist)<-[:USES_CT]-(v2:Variable)
RETURN c.name, collect(DISTINCT v2.name)

-- "How is AE related to other domains?"
MATCH (d:Domain {name:'AE'})-[r:RELATED_TO]->(d2:Domain)
RETURN d2.name, r.mechanism

-- "Which variables appear in more than 3 domains?"
MATCH (d:Domain)-[:HAS_VARIABLE]->(v:Variable)
WITH v, count(d) AS cnt WHERE cnt > 3
RETURN v.name, cnt ORDER BY cnt DESC

-- "What domains/variables would be affected by changing C66742?"
MATCH (t:Codelist {code:'C66742'})<-[:USES_CT]-(v:Variable)<-[:HAS_VARIABLE]-(d:Domain)
RETURN d.name, v.name
```

### 5.4 Hybrid Routing

```
User question
  │
  ├─ Intent classifier (LLM structured output)
  │
  ├─ CONCEPT ("how to", "what is", rules)
  │   → RAG path (vector retrieval + LLM)
  │
  ├─ RELATION ("which domains", "what uses", "impact of")
  │   → Graph path (LLM → Cypher → Neo4j → LLM format)
  │
  └─ HYBRID (mixed)
      → Both paths in parallel → LLM fusion
```

### 5.5 Neo4j Local Setup

```yaml
# docker-compose.yml
neo4j:
  image: neo4j:5-community
  ports: ["7474:7474", "7687:7687"]
  volumes: ["./data/graph:/data"]
```

### 5.6 Graph-Enhanced Validation (Phase 2 Extension)

Knowledge graph strengthens dataset validation:

- **Impact analysis**: "You changed AESER values — here are all downstream dependencies"
- **Cross-domain completeness**: Graph traversal to check if all RELREC-linked domains are present
- **CT cascade validation**: Check if CT values are consistent across all domains that share a codelist

---

## 6. Evaluation System

### 6.1 Test Q&A Set

~50 manually curated questions with ground-truth answers:

| Category | Count | Example |
|----------|-------|---------|
| Single-domain precise | ~12 | "What is AETERM's Core status?" |
| Cross-domain relation | ~12 | "Which domains share Codelist C66742?" |
| Concept/rule | ~12 | "When must EPOCH be populated?" |
| Hybrid | ~12 | "AESER definition + what CT it uses + who else uses it?" |

### 6.2 Metrics

| Metric | What It Measures |
|--------|-----------------|
| Answer correctness | Exact match or semantic equivalence to ground truth |
| Source citation accuracy | Did it cite the right file and section? |
| Recall | For relationship queries, did it find all matching results? |
| Validation precision | For dataset validation, false positive / false negative rate |

### 6.3 Eval Workflow

```python
# eval/run_eval.py
# For each test question:
#   1. Run through system
#   2. Compare answer to ground truth
#   3. Output accuracy/recall/citation metrics
```

Run after every change to chunking strategy, embedding model, or retrieval parameters.

---

## 7. Implementation Roadmap

### Phase 1: RAG + Validation (local)

```
Step 1   Project scaffolding
         - Create sdtm-rag/ directory structure
         - pyproject.toml + dependency management
         - Docker Compose (Chroma)

Step 2   Data ingestion (ingest.py)
         - Implement 6 file-type chunking strategies
         - Embedding + write to Chroma
         - Verify: sample queries confirm retrieval quality

Step 3   Q&A service (server/)
         - FastAPI + ROUTING.md injection
         - Metadata filtering + semantic retrieval
         - LiteLLM multi-model support

Step 4   Dataset validation (validator.py + reviewer.py)
         - parse_dataset.py: CSV/XPT/SAS7BDAT parsing
         - Rule-based validation engine
         - RAG-assisted semantic review
         - Structured report generation

Step 5   Frontend (ui/)
         - Streamlit chat interface
         - Source citation display
         - Dataset upload + validation report view

Step 6   Evaluation
         - Write 50 test Q&A pairs
         - Run baseline, tune chunking/retrieval parameters
```

### Phase 2: Knowledge Graph + Hybrid Routing

```
Step 7   P3 structured metadata
         - Python script: spec.md + Cross References → meta.yaml
         - 63 domains full coverage

Step 8   Graph database (build_graph.py)
         - Docker Compose add Neo4j
         - Import nodes + relationships
         - Verify: Cypher query sampling

Step 9   Graph query service (graph.py)
         - LLM → Cypher generation + execution
         - Common query template caching

Step 10  Hybrid routing (router.py)
         - Intent classifier
         - RAG / Graph / Hybrid three-way routing
         - Answer fusion

Step 11  Graph-enhanced validation
         - Cross-domain dependency checks via graph traversal
         - CT cascade validation
         - Impact analysis for dataset changes

Step 12  Phase 2 evaluation
         - Expand eval set (relation + hybrid + validation cases)
         - Compare against Phase 1 baseline
```

---

## 8. Out of Scope (Deferred to Deployment Phase)

- Cloud deployment (Vercel / AWS / other)
- User authentication and access control
- Multi-tenancy
- Continuous data update pipeline (knowledge base update → auto re-ingest)
- SDTM version management (multiple IG versions)
