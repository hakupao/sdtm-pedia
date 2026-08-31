# 联网通道语义抽检 — 答案原文 (人判材料; 不进 gold set)

## 第 1 题: How do other teams handle EDC fields that don't map to any standard SDTM domain?

- web_status=ok web_searches_ok=2 搜索次数=2

## まず標準側の枠組み（【標準 CDISC】）

EDC 上のフィールドが既存 SDTM ドメインに収まらない場合、標準が用意している選択肢は限られており、順序も決まっています。

**1. 変数追加は禁止 → NSV は SUPP-- へ**
- 「Sponsors may not add any variables other than those described above — use Supplemental Qualifiers (SUPP--) for non-standard variables」「Standard variables must not be renamed or modified for novel usage」 [Source: chapters/ch02_fundamentals.md -- 2.5 The SDTM Standard Domain Models]
- 追加可能なのは (a) 同一 GOC 内の他の Qualifier 変数、(b) Timing 変数のみ（ドメイン固有 assumption で制限されていない範囲） [Source: chapters/ch02_fundamentals.md -- 2.5 The SDTM Standard Domain Models]
- 非標準変数は SUPP-- に置き、機構は Section 8.4「Relating Non-standard Variable Values to a Parent Domain」に従う [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]

**2. カスタムドメインは「既存ドメインに入らないことを確認してから」**
- 「Confirm that none of the existing published domains will fit the need. A custom domain may only be created if the data are different in nature and do not fit into an existing published domain.」 [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]
- 重要な判断軸：**収集方法ではなく topic と nature でグルーピングする**。別 CRF ページ／別モジュールで集めたことは新ドメインの理由にならない（例：各種質問票は QS、prior と concomitant medication は共に CM）。ドメイン内の区別には --CAT, --SCAT, --METHOD, --SPEC, --LOC を使う [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]
- CDISC wiki の SDTM Draft Domains を先に確認する [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]、TA 標準等が追加ドメイン提案を出している場合がある [Source: chapters/ch02_fundamentals.md -- 2.5 The SDTM Standard Domain Models]
- 作成手順は a〜k（Required identifiers STUDYID, DOMAIN, USUBJID, --SEQ → GOC の topic 変数 → 同一 GOC の qualifier のみ → timing → ドメインコード決定（Domain Abbreviations codelist に無いもの。AD, AX, AP, SQ, SA は使用禁止）→ prefix 適用 → 変数順序 → label は title case → Define-XML 記載 → 残る非標準変数は SUPP-- へ） [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]
- 将来の CDISC コードとの衝突回避のため、**X, Y, Z 始まりのドメインコードがカスタム用に予約**されている（任意、必須ではない） [Source: chapters/ch04_general_assumptions.md -- 4.1.6 Additional Guidance on Dataset Naming]

**3. やってはいけないパターン（標準が明示）**
- 時間軸だけを理由にドメインを分けない（prior/current は 1 ドメイン。AE と MH は例外） [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]
- 「efficacy」ドメインを作らない。解析目的で集めたデータも標準ドメインに入れる [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]
- 階層データはドメインペアで表現（MB/MS, PC/PP のように）し、RELREC でデータセット間関係を張る [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]

**4. 「収まらないから提出しない」は不可**
- Conformance の条件として「Including all collected and relevant derived data in one of the standard domains, special-purpose datasets, or general observation class structures」が挙げられている [Source: chapters/ch03_submitting_data.md -- 3.2.2 Conformance]。ADaM で使うデータは SDTM に traceable でなければならない [Source: chapters/ch02_fundamentals.md -- 2.5 The SDTM Standard Domain Models]

なお、FA（Findings About Events or Interventions）は Findings クラスのドメインとして標準に存在し [Source: knowledge_base/INDEX.md]、Findings About は Findings のサブタイプとしてモデル上位置づけられています [Source: model/01_concepts_and_terms.md -- 2.1 Model Concepts and Terms — Variables]。イベント／介入「について」の測定値の置き場としては、まず FA の適用可否を検討するのが標準の設計意図に沿います（FA の適用条件そのものは domains/FA/assumptions.md を参照する必要があり、上記コンテキストには含まれていません）。

---

## 他チームの実務（【Web：未検証の第三者情報】）

以下は会議論文・ブログ等の第三者情報で、**CDISC 標準текст ではありません**。あくまで参考・推測材料として扱ってください。

- **判断フローとして「SUPPQUAL / FA / カスタム Findings ドメイン」の三択で整理する**のが定番の議論の立て方のようです。Salyers/Lewis/Wood のPharmaSUG 2015 論文は表題そのものが "Supplemental Qualifiers, Findings About, or a Custom Findings Domain" で、非標準変数提出時の考慮点を扱っています [Web: https://pharmasug.org/proceedings/2015/DS/PharmaSUG-2015-DS15.pdf (retrieved 2026-08-31)]。
- **切り分け基準として「親レコードとの関係が 1:1 か」を使うチームがある**：親ドメインの単一レコードに紐づく情報なら SUPPQUAL、複数レコードに関わる／イベント・介入についての測定値なら FA、という整理が示されています [Web: https://www.lexjansen.com/pharmasug/2019/DS/PharmaSUG-2019-DS-254.pdf (retrieved 2026-08-31)]。これは有用な経験則ですが CDISC の要件として書かれたものではなく、**推測（inference）として扱ってください**。
- **NSV の出所として TAUG を確認する運用**：治療領域ユーザガイド（TAUG）が SDTM 未収載の変数を導入していることが多く、CDISC Wiki の "SDTM NSV Registry" に登録済み NSV が追跡されているため、自前で QNAM を発明する前にそこを見る、という実務が報告されています [Web: https://www.lexjansen.com/pharmasug/2020/DS/PharmaSUG-2020-DS-261.pdf (retrieved 2026-08-31)]。同論文は AETRTEM や AESOSP のように規制当局側から求められる SUPPQUAL 変数がある点にも触れています [Web: https://www.lexjansen.com/pharmasug/2020/DS/PharmaSUG-2020-DS-261.pdf (retrieved 2026-08-31)]。
- **「まずカスタムドメインを作りたくなる衝動を抑えて SUPP-- を使え」という指針**を掲げるブログもあります [Web: https://omophub.com/blog/sdtm-clinical-trials (retrieved 2026-08-31)]。ただしこれは単純化しすぎで、標準側は「独自質問票なら QS へ」「data are different in nature なら custom domain 可」と述べており [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]、SUPP-- は**あくまで親レコードに対する非標準 qualifier の器**です。この Web 記述は無条件には採用しないことを推奨します。
- マッピング作業手順の一般論として、「コアドメインに表現できないデータにはカスタムドメインと SUPPQUAL を作る」ステップを工程に組み込む例も紹介されています [Web: https://www.hhmglobal.com/knowledge-bank/news/a-basic-guide-to-sdtm-mapping (retrieved 2026-08-31)]。

---

## 実務上の推奨判断順序（標準記述からの整理＋一部推測）

1. 既存の公開ドメインで表現できないか再確認（topic/nature で判断、収集方法で分けない） [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]
2. 同一 GOC の未使用 Qualifier／Timing 変数で吸収できないか [Source: chapters/ch02_fundamentals.md -- 2.5 The SDTM Standard Domain Models]
3. イベント／介入についての findings なら FA の適用検討（FA assumptions を要確認）
4. 親レコードに付随する単一値なら SUPP-- （Section 8.4 の構造に従う） [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]
5. どれにも該当せず、性質が本質的に異なるならカスタムドメイン（GOC ベース、手順 a〜k、コードは X/Y/Z 推奨） [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain] [Source: chapters/ch04_general_assumptions.md -- 4.1.6 Additional Guidance on Dataset Naming]
6. いずれの場合も Define-XML に記載し、Permissible 変数の扱い（収集していないなら含めない・宣言しない）を守る [Source: chapters/ch02_fundamentals.md -- 2.5 The SDTM Standard Domain Models]

この 3〜4 の優先順位づけ自体は上記コンテキストに明文の規定がないため、**推測（inference）**です。

---

## 注意（フェデレーション）

- 今回の検索では【本研究 (study)】の EDC フィールドカードは取得されていません。したがって、貴研究の具体的フィールドがどこに収まらないかについては本回答では判定できません。対象フィールド名を挙げていただければ個別に検討できます。
- また、**EDC 項目 ↔ SDTM 変数のマッピング文書はどちらのコーパスにも存在しません**。個別フィールドに対して私が提示するマッピングは常に**推測（inference）**であり、文書化された事実ではありません。

## 第 2 题: What do practitioners say about overusing SUPPQUAL versus creating a custom domain?

- web_status=ok web_searches_ok=2 搜索次数=2

I'll ground the standard's own rules from the knowledge base, then search for industry commentary since "what practitioners say" is outside the standard.## 1. What the standard itself constrains (knowledge base)

The SDTMIG never frames this as a "style preference" — it sets hard boundaries on both sides.

**Why SUPP-- exists at all, and its limits:**
- "The SDTM does not allow the addition of new variables. Therefore, the Supplemental Qualifiers ... dataset model is used to capture non-standard variables (NSVs) and their association to parent records" — and critically: "**Data that represent separate observations should be treated as separate observations**" [Source: domains/SUPPQUAL/assumptions.md]. That single sentence is the standard's own anti-overuse rule: SUPP-- is for *qualifiers of an existing observation*, not for smuggling in new observations.
- QNAM is the Topic variable of SUPP--, Type Char, Core Req; QVAL is the Result Qualifier, Type Char, Core Req, and "no records can be in SUPP-- with a null value for QVAL" [Source: domains/SUPPQUAL/spec.md]. Sponsors "must delete the records where QVAL is null prior to submission" — the IG explicitly warns that naive transposition of all source variables makes "the SUPP-- datasets ... extremely large" [Source: domains/SUPPQUAL/assumptions.md].
- QVAL being Char is a structural cost that is often overlooked: every numeric NSV loses its type, and there is no --STRESN/--STRESU analogue in SUPP--.
- One QNAM per parent record: "there should not be multiple records in a SUPP-- dataset for the same QNAM value, as it relates to IDVAR/IDVARVAL for a USUBJID in a domain" — two evaluators require two distinct QNAMs (e.g., "AETRTEMI", "AETRTEMA") [Source: domains/SUPPQUAL/assumptions.md]. So repeating/multi-valued content cannot live in SUPP--.
- Splitting multiplies the files: supplemental qualifiers "would need to be managed at the split-file level (e.g., suppface.xpt, suppfamh.xpt)" and there is "a one-to-one correspondence between a domain dataset and its Supplemental Qualifier dataset"; the single-SUPPQUAL option from SDTMIG v3.1 was **deprecated** [Source: chapters/ch08_relationships.md, §8.4.2].

**When a custom domain is the right answer instead:**
- "A custom domain may only be created if the data are different in nature and do not fit into an existing published domain," must be based on one of the 3 general observation classes, and step (k) of the process is explicitly "Place any non-standard (SDTM) variables in a Supplemental Qualifier dataset" [Source: chapters/ch02_fundamentals.md, §2.6]. So a custom domain does not eliminate SUPP--; it relocates the *observation*, and NSVs still go to SUPP--.
- Guardrails: "Data should be grouped by topic and nature, not by collection method"; do not create separate domains based on time; and "Do not create 'efficacy' domains — data collected for analysis must still go in standard domains" [Source: chapters/ch02_fundamentals.md, §2.6]. This last point is the direct rebuttal to "it's an endpoint, so give it its own domain."

**The IG's own decision aid (SUPP-- vs. FA), which generalizes well:**
- "The choice between representing a data item as a supplemental qualifier or as a finding about an event or intervention may not be clear-cut." Key test: "Does the data item have its own timing, separate from the timing of the event or intervention? If the data item represents some action during or after the event or intervention, it may be considered to have its own timing" → then FA, not SUPP--. Likewise, if a relationship to a disease milestone (RELMIDS) is needed, "it can be represented in FA, but not as a supplemental qualifier to the parent record" [Source: chapters/ch02_fundamentals.md, Findings About — Naming Findings About Domains].
- Practical consequence documented in the IG: a SUPP-- variable can be forced into the **natural key**, written as a 2-part name, e.g. "STUDYID, USUBJID, SPDEVID, VISITNUM, MKTESTCD, MKLOC, MKLAT, MKMETHOD, QNAM.MKHNDPOS" [Source: chapters/ch04_general_assumptions.md, §4.1.9]. If an NSV is doing key work, that is a strong signal the modeling is strained — though note the IG presents this as a legitimate, supported pattern, not as an error.

**A working rule consistent with the above:** SUPP-- if the item qualifies an existing record, has no independent timing, is single-valued per parent record, and is not needed as a real analysis variable. Custom domain (or FA, or an existing domain's standard variable) if the item is its own observation with its own timing/result semantics.

## 2. What practitioners and regulators say (web — unverified, third-party)

- FDA's *Study Data Technical Conformance Guide* is the most-cited external constraint: "SUPPQUAL should be used only when key data cannot be represented in SDTM domains. In general, variables used to support key analyses should not be represented in SUPPQUAL. Discussion with the review division should occur if the sponsor intends to include important variables (e.g., that support key analyses) in SUPPQUAL datasets, and this should be reflected in the SDRG." [Web: https://www.fda.gov/media/136460/download (retrieved 2026-08-31)]
- On reviewer burden, a CDISC-community blog quotes the assessment that the original vision — FDA tools auto-joining NSVs into a parent view — did not materialize: "the representation of NSVs in separate SUPP-- datasets has resulted in increased effort by reviewers"; SDTM data is often viewed "as is," without building a database, so recombining SUPP-- with the parent is not easy [Web: http://cdiscguru.blogspot.com/2013/02/sdtm-and-derived-variables.html (retrieved 2026-08-31)].
- A conference paper on SDTM/ADaM as operational models recommends "always use a domain specific SUPPQUAL" so a separate SUPPxx alerts the reviewer, and suggests supplying an augmented (joined) version of the domain dataset for viewing [Web: https://ww2.amstat.org/meetings/proceedings/2012/data/assets/pdf/303595_71121.pdf (retrieved 2026-08-31)]. Note the domain-specific point is now simply the standard requirement, not an option [Source: chapters/ch08_relationships.md, §8.4.2].
- Practitioner rules-of-thumb circulating in training material: SUPPQUAL for "additional non-standard variable / same observation / existing SDTM domain"; custom domain for "new business concept / separate data structure required / existing domains cannot represent the data" — and, before either, "confirm whether an appropriate standard variable or existing domain" exists [Web: https://www.instagram.com/p/Dbwy1v1G574 (retrieved 2026-08-31)] [Web: https://www.linkedin.com/posts/neelgajjar1710_ep-25-suppqual-and-custom-domains-activity-7495655028565716993-rBef (retrieved 2026-08-31)].

## 3. Practical takeaways — labeled as inference

The following are **inference (推測)** drawn from the borrowed practice above plus the standard's rules; they are not documented CDISC requirements:
- 推測: If an NSV feeds a primary/secondary endpoint or a key safety analysis, treat SUPP-- as a red flag, revisit whether a standard variable, FA, or a custom domain fits, and if you keep it in SUPP--, document the rationale in the SDRG and raise it with the review division (this mirrors FDA's wording, which is guidance-level, not CDISC standard).
- 推測: A very high NSV count on one parent domain usually indicates a modeling problem (multiple observations collapsed into one record) rather than a need for many QNAMs — apply the IG's "separate observations" and "own timing" tests per item [Source: domains/SUPPQUAL/assumptions.md; chapters/ch02_fundamentals.md].
- 推測: Overcorrecting is equally bad — a custom domain built to avoid SUPP-- but grouped by CRF page/collection method, or created as an "efficacy" domain, violates §2.6 outright [Source: chapters/ch02_fundamentals.md, §2.6].

**Caveat:** the knowledge base contains no CDISC-authored numeric threshold ("no more than N QNAMs") and no CDISC statement ranking SUPP-- as inferior to a custom domain. Any such threshold you encounter is sponsor convention, not standard text.

## 第 3 题: How is Findings About (FA) used in practice versus a custom findings domain?

- web_status=ok web_searches_ok=0 搜索次数=0

## Short answer

Both routes exist and are explicitly sanctioned; the choice is about *dataset packaging*, not about a different model. SDTMIG v3.4 §6.4.2 gives sponsors three options for findings-about data, and only one of them is a "custom domain" — and even that custom domain is still a **Findings About** domain (it carries `--OBJ`), not a plain Findings domain. [Source: chapters/ch02_fundamentals.md]

---

## 1. First decide it is FA data at all

FA is used "when findings about an event or intervention need to be captured," qualified by three criteria [Source: domains/FA/assumptions.md]:

- **Criterion 1** — the observation has **different timing from the event/intervention as a whole** (repeated/intermittent symptom assessments, snapshots or "slices" of an event, summaries such as max severity of headache per dosing interval). Noted as less likely to apply to interventions, since an intervention record often represents a single administration.
- **Criterion 2** — the observation **needs more than one variable** to represent it, so it cannot reasonably be a supplemental qualifier.
- **Criterion 3** — data that **indicate the occurrence of pre-specified AEs**.

The older criterion "data about an Event or Intervention for which no Event or Intervention record exists" was **removed**; such data are now best represented using only the FA domain — i.e., FA records may exist **with or without** a parent event/intervention record. [Source: domains/FA/assumptions.md]

The classic competing choice is **SUPP--**: if the data item has its own timing (Criterion 1) or needs >1 variable (Criterion 2), it belongs in FA; also, if a relationship to a disease milestone (`RELMIDS`) is needed, that can be represented in FA but **not** as a supplemental qualifier to the parent record. [Source: chapters/ch02_fundamentals.md]

And before that, the Event-vs-Finding-vs-FA question is worked through in §8.6.3, using diagnostics such as: is it a measurement with units? log form vs per-visit CRF? are the dates start/end dates or assessment dates? is verbatim text collected and coded (topic coded ⇒ Events/Interventions; result coded ⇒ Findings)? and **does it apply to the event as a whole** (yes ⇒ traditional Events qualifier; no ⇒ finding about the event). [Source: chapters/ch08_relationships.md]

## 2. The three implementation patterns (§6.4.2)

[Source: chapters/ch02_fundamentals.md]

| Pattern | What it looks like | Practical notes |
|---|---|---|
| **1. Single FA dataset** | one `fa.xpt` for all findings-about data | separate content streams with `FACAT` / `FASCAT` values |
| **2. Split FA domain** | `DOMAIN` = "FA"; prefixed variables use "FA"; dataset names = domain + up to 2 chars for the **parent domain** (e.g. `FACE` = Findings About Clinical Events, `FAMH` = Findings About Medical History) | `FASEQ` must be unique within `USUBJID` **across all split datasets**; SUPP-- managed at split-file level (`suppface.xpt`, `suppfamh.xpt`) with `RDOMAIN` = "FA"; for a dataset-level RELREC (e.g. CE ↔ FACE) `RDOMAIN` may hold up to 4 characters. The FACE/FAMH naming may be used even when there is only one, unsplit FA dataset. |
| **3. Separate (custom) domain** | sponsor-defined `DOMAIN` that **does not begin with "FA"**, following the SR (Skin Response) precedent | all published FA guidance still applies; all published domain guidance still applies; prefixed variables use the chosen 2-character code |

SR is the model in the standard for pattern 3: it is designated **Findings About** class alongside FA, with AE, CM and PR as source domains. [Source: domains/SR/spec.md] [Source: domains/FA/spec.md]

## 3. The hard rule that separates FA from a custom *Findings* domain

- `--OBJ` (**Object of the Observation**, Char, Record Qualifier; `FAOBJ` is **Req** in FA) is the variable unique to Findings About; its position among Findings qualifiers is **immediately after `--TEST`**. [Source: model/02_observation_classes.md] [Source: VARIABLE_INDEX.md]
- **`--OBJ` cannot be added to a standard Findings domain.** A domain is either a Findings domain or a Findings About domain — not one or the other depending on the situation. When `--OBJ` is included, that *identifies* the domain as an FA domain and `--OBJ` **must be populated on all records**. [Source: chapters/ch02_fundamentals.md]

So "custom findings domain" splits into two very different things in practice:
- a **custom Findings About domain** (has `--OBJ`, e.g. SR) — legitimate pattern 3;
- a **custom standard Findings domain** — then you may *not* bolt on `--OBJ`, and you lose the ability to state which event/intervention the finding is about, which is usually the whole point.

## 4. Content conventions once you are in FA

- `FAOBJ` + `FATESTCD` jointly define the topic: `FATESTCD` = the measurement/evaluation, `FAOBJ` = the event or intervention the measurement is about; **both required on every record**. [Source: model/02_observation_classes.md]
- When the collected data fit an Events/Interventions qualifier, reuse the **variable name as the `FATESTCD` value** and the variable label as `FATEST` — e.g. `OCCUR`/"Occurrence Indicator", `SEV`/"Severity/Intensity", `TOXGR`/"Toxicity Grade". [Source: model/02_observation_classes.md] [Source: domains/FA/assumptions.md]
- Conversely, inside FA these qualifiers should generally **not** be used as variables: `--BODSYS`, `--MODIFY`, `--SEV`, `--TOXGR`. Any Identifier, Timing, or Findings-class qualifier may otherwise be added. [Source: domains/FA/assumptions.md]
- `FATEST` — Label "Findings About Test Name", Char, Synonym Qualifier, **Req**, Controlled Terms **C101833**, value ≤ 40 characters; CT lives in a general FATEST codelist plus several therapeutic-area-specific codelists. `FATESTCD` uses **C101832**. [Source: domains/FA/spec.md] [Source: VARIABLE_INDEX.md]
- `FACAT` (Label "Category for Findings About", Char, Grouping Qualifier, **Perm**, no CT; examples "GERD", "PRE-SPECIFIED AE") and `FASCAT` (further categorization of `FACAT`, Char, Grouping Qualifier, **Perm**) are the levers for keeping one physical FA dataset readable. [Source: domains/FA/spec.md]
- Cardiovascular findings-about tests and their response codelists are associated via the **CV codetable** on the CDISC terminology page. [Source: domains/FA/assumptions.md]
- Typical parent domains that FA points at: AE, CM, PR, EX, EC, ML, SU [Source: domains/FA/spec.md]; QS also lists FA as the findings-about counterpart for questionnaire responses [Source: domains/QS/spec.md], and AE lists FA for prespecified AE findings (`AEPRESP`) [Source: domains/AE/spec.md].

## 5. Practical decision summary

1. Data are about an event/intervention and meet ≥1 of the three criteria → FA structure (else SUPP-- on the parent, or a plain Findings/Events record).
2. Volume/structure manageable → **one `fa.xpt`**, differentiated by `FACAT`/`FASCAT`.
3. Multiple distinct parent domains, large volume, or different value-level metadata per parent → **split FA** (`FACE`, `FAMH`, …), watching `FASEQ` uniqueness, split-level SUPP--, and 4-character `RDOMAIN` in dataset-level RELREC.
4. A coherent, reusable clinical concept that deserves its own identity (the SR precedent) → **custom 2-character Findings About domain**, keeping `--OBJ` populated on every record and applying all FA + domain guidance.

**Coverage caveat:** the retrieved context is truncated in two places (the full §8.6.3 question table and the tail of §6.4.3 on reusing qualifier names), and it does not contain SR's own assumptions or FA examples. If you need the complete decision table or SR-specific rules, read `chapters/ch08_relationships.md` §8.6.3, `domains/FA/examples.md`, and `domains/SR/assumptions.md` directly. All statements above are from the 【標準 CDISC】 corpus; no study-specific (EDC) material was retrieved, so nothing here is study-specific mapping guidance.

