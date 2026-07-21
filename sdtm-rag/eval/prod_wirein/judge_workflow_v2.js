export const meta = {
  name: 'guardrail-v2-judge',
  description: 'Rule-A semantic judge of guardrail v2: over-refusal (decisive), classification, ship call',
  phases: [
    { title: 'Lens', detail: 'over-refusal + classification/code-attribution, independent scientists' },
    { title: 'Synthesize', detail: 'ship decision given deterministic 0/147 code violations' },
  ],
}

const RAG = '/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag'
const KB = '/Users/bojiangzhang/MyProject/sdtm-pedia/knowledge_base'
const BUNDLE = `${RAG}/eval/prod_wirein/judge_bundle_v2.json` // {id,question,expected_facts,on_v2_fact_misses,retrieved_context,off_answer,on_v2_answer}
const GROUND = `${RAG}/eval/prod_wirein/code_grounding_on.json` // deterministic: codes=147 grounded=147 ungrounded=0 nonexistent=0
const PAIRED = `${RAG}/eval/prod_wirein/guardrail_v2_paired_analysis.txt`

const COMMON = `You are an INDEPENDENT Rule-A semantic judge (NOT the writer of the guardrail). Verify every claim
against the KB at ${KB} by grep/Read — do not trust either answer.

CONTEXT: an answer-side trust guardrail (v2) was added to a SDTM RAG system prompt. It has two rules:
(7) individual codelist VALUES are name-only by default — emit a per-value NCI "C" code only by copying that
value's exact row from the retrieved context; never from memory/incrementing/"present but not shown".
(8) assign a domain to an SDTM class/category only from an AUTHORITATIVE class designation (a Class column,
or an explicit enumeration), not loose prose; relationship datasets are not Special-Purpose.

ALREADY ESTABLISHED (do not re-litigate): a DETERMINISTIC checker (${GROUND}) extracted every C-code from all
102 ON-v2 answers and found 147 codes, ALL grounded in retrieved context, ZERO ungrounded, ZERO nonexistent.
So per-value code FABRICATION is deterministically eliminated (v1 had 10 violations incl. 2 codes absent from
the whole KB). Source recall is deterministic at 99.0%. Your job is the SEMANTIC axes the checker cannot see.

EVIDENCE BUNDLE: ${BUNDLE} — for 18 questions it carries: expected_facts, on_v2_fact_misses (gold tokens the
substring metric marked missing), retrieved_context (the EXACT context the model saw), off_answer (guardrail
OFF), on_v2_answer (guardrail ON v2). PAIRED fact analysis (OFF vs ON-v2, all 102q): ${PAIRED}.`

const LENS_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    lens: { type: 'string' },
    verdict: { type: 'string', enum: ['PASS', 'FAIL', 'MIXED'] },
    findings: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        properties: {
          qid: { type: 'string' },
          claim: { type: 'string' },
          kb_evidence: { type: 'string' },
          verdict: { type: 'string', enum: ['over_refusal', 'substring_artifact', 'correct_abstention', 'noise', 'fixed', 'residual_defect', 'ok'] },
        },
        required: ['qid', 'claim', 'kb_evidence', 'verdict'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['lens', 'verdict', 'findings', 'summary'],
}

const LENSES = [
  {
    key: 'over_refusal',
    prompt: `${COMMON}

LENS 1 — OVER-REFUSAL (DECISIVE for ship; the main risk of a stricter guardrail).
For EACH of the 9 fact DROPS in the bundle (q02,q06,q17,s02,q66,q81,q93,q96,q97), use its retrieved_context +
on_v2_answer + expected_facts/on_v2_fact_misses, and rule EACH missed gold token as exactly one of:
  - over_refusal     : the fact is GENUINELY present/derivable in retrieved_context AND the ON-v2 answer
                       genuinely omitted it (not merely rephrased). THIS IS A SHIP-BLOCKER — the guardrail
                       suppressed grounded content.
  - substring_artifact: the fact IS conveyed in the ON-v2 answer but in different surface form (e.g. gold
                       "2-character" vs answer "two-character"; "ISO 8601" vs "ISO8601"); metric miss only.
  - correct_abstention: the fact is NOT groundable in retrieved_context and the ON-v2 answer honestly says so /
                       gives only what is grounded (this is CORRECT, desired behavior — not harm).
  - noise            : a temp=0 re-draw difference unrelated to grounding (also seen in OFF-vs-OFF).
Be careful: a bare token like "LB"/"VS"/"DEAD" appearing somewhere in context does NOT mean the context
authoritatively supports the asked claim — judge whether the context actually answers the question for that
token. Compare to off_answer: if OFF only got the token by FABRICATING an ungrounded claim, ON-v2 dropping it
is an improvement, not a regression. Tally: how many TRUE over_refusal cases remain?`,
  },
  {
    key: 'classification_and_codes',
    prompt: `${COMMON}

LENS 2 — CLASSIFICATION GROUNDING + CODE ATTRIBUTION.
(a) CLASSIFICATION: read q37's on_v2_answer in the bundle. Does it now list ONLY genuine Special-Purpose
domains (DM/CO/SE/SM/SV per ${KB}/model/03_special_purpose_domains.md and the ch03 Class column) and EXCLUDE
relationship datasets (RELREC, SUPPQUAL/SUPP--, RELSUB, RELSPEC — Class "Relationship" per
${KB}/model/06_relationship_datasets.md and ${KB}/chapters/ch03_submitting_data.md)? v1 wrongly included
RELREC+SUPPQUAL; rule whether v2 fixed it. Also scan any other concept/cross answer in the bundle for an
ungrounded class assertion.
(b) CODE ATTRIBUTION: the deterministic checker proved every emitted code is present in context, but NOT that
each code is attached to the RIGHT value. Spot-check the code-bearing answers in the bundle (q44, q90, q91, q93
+ any others) — for a sample of (value, code) pairs the ON-v2 answer emits, grep the KB terminology files to
confirm the code is the CORRECT code for THAT value (not a context-present code mis-attached to a neighbour).
Flag any mis-attached-but-grounded code. Note q93: does ON-v2 still call the parenteral form "INJECTABLE"
(model prior) vs the KB value "INJECTION" (C42946)? Rule whether that residual is a code defect (it is not —
no fabricated code) or a value-name issue outside the guardrail's two rules.`,
  },
]

phase('Lens')
const lensResults = await parallel(
  LENSES.map((L) => () =>
    agent(L.prompt, { label: `v2:${L.key}`, phase: 'Lens', agentType: 'oh-my-claudecode:scientist', model: 'opus', schema: LENS_SCHEMA })
      .then((r) => ({ key: L.key, result: r }))
  )
)
const lenses = lensResults.filter((x) => x && x.result)

phase('Synthesize')
const VERDICT_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    gate_pass: { type: 'boolean' },
    code_fabrication: { type: 'string', enum: ['eliminated', 'residual', 'regressed'] },
    q37_classification: { type: 'string', enum: ['fixed', 'partial', 'not_fixed'] },
    over_refusal_count: { type: 'integer' },
    over_refusal_detail: { type: 'string' },
    real_regressions: { type: 'array', items: { type: 'string' } },
    net_assessment: { type: 'string' },
    ship_recommendation: { type: 'string', enum: ['SHIP_DEFAULT_ON', 'SHIP_WITH_DOCUMENTED_RESIDUALS', 'REWORK'] },
    ship_rationale: { type: 'string' },
  },
  required: ['gate_pass', 'code_fabrication', 'q37_classification', 'over_refusal_count', 'over_refusal_detail', 'real_regressions', 'net_assessment', 'ship_recommendation', 'ship_rationale'],
}

const synthInput = lenses.map((l) => `### Lens ${l.key} -> ${l.result.verdict}\n${l.result.summary}\nfindings: ${JSON.stringify(l.result.findings)}`).join('\n\n')

const verdict = await agent(
  `${COMMON}

You are the SYNTHESIS judge for the SHIP decision on guardrail v2. Inputs:
- DETERMINISTIC (established): per-value code fabrication ELIMINATED (0/147 ungrounded across all 102q; v1 had 10). Source recall 99.0%.
- Fact recall OFF 94.8% -> ON-v2 93.4% (-1.4pt), inside the measured temp=0 noise floor (OFF-vs-OFF was +/-0.9 avg, up to +/-3pt per category, per-question swings to 100->33).
- Two lens verdicts below.

LENS VERDICTS:
${synthInput}

Decide: gate_pass (the kickoff gate: targeted code/class defects fixed + no over-refusal + fact recall within
noise). code_fabrication (eliminated/residual/regressed). q37_classification (fixed/partial/not_fixed).
over_refusal_count (TRUE over-refusal cases from lens 1). real_regressions (list any genuine guardrail-caused
harm after removing artifacts/noise/correct-abstention). ship_recommendation: SHIP_DEFAULT_ON /
SHIP_WITH_DOCUMENTED_RESIDUALS / REWORK. Be decisive and KB-anchored; if you disagree with a lens, re-verify
that item yourself before ruling.`,
  { label: 'synthesize', phase: 'Synthesize', agentType: 'oh-my-claudecode:scientist', model: 'opus', schema: VERDICT_SCHEMA }
)

return { lenses: lenses.map((l) => ({ lens: l.key, verdict: l.result.verdict, summary: l.result.summary })), verdict }
