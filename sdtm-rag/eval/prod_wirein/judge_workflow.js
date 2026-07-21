export const meta = {
  name: 'guardrail-semantic-judge',
  description: 'Adversarial multi-lens Rule-A semantic judge of the answer-side trust guardrail (off vs on)',
  phases: [
    { title: 'Lens', detail: 'four independent scientist lenses adversarially verify off-vs-on against KB' },
    { title: 'Synthesize', detail: 'one scientist fuses lens verdicts into the gate decision' },
  ],
}

// Paths the lenses read (absolute, so CWD-independent).
const ROOT = '/Users/bojiangzhang/MyProject/sdtm-pedia'
const RAG = `${ROOT}/branches/07_rag_kg/sdtm-rag`
const FORENSIC = `${RAG}/eval/prod_wirein/forensic_guardrail.json`   // full off/on text, 16q subset
const FORENSIC_DROPS = `${RAG}/eval/prod_wirein/forensic_drops.json` // full off/on text for the 10 fact DROPS
const PAIRED = `${RAG}/eval/prod_wirein/guardrail_paired_analysis.txt` // analyze_paired OFF vs ON (all 102q)
const KB = `${ROOT}/knowledge_base`

// MEASURED temp=0 noise floor (OFF-run1 vs OFF-run2, identical config, NO guardrail change):
// fact avg 94.8% -> 95.7% (+0.9); 4 drops + 8 gains from pure non-determinism; per-category
// swings up to mixed +3.0pt; per-question swings up to q81 100->33, q02 71->57. CRUCIALLY,
// q02/q06/q81 also drop in this pure-noise comparison -> those OFF->ON drops are noise, not
// guardrail. Source recall is deterministic (99.0% identical across all 3 runs).
const NOISE_FLOOR = `MEASURED temp=0 NOISE FLOOR (OFF vs OFF, no guardrail change): fact avg 94.8->95.7 (+0.9), 4 drops + 8 gains, per-category swing up to mixed +3.0pt, per-question up to q81 100->33 and q02 71->57. q02/q06/q81 drop in pure noise too. So the OFF->ON fact delta (-2.0pt, 10 drops/7 gains) is within this envelope; source recall (deterministic) is 99.0% across all runs.`

const COMMON = `You are an INDEPENDENT Rule-A semantic judge (you are NOT the writer of the guardrail).
Your job is to FALSIFY the claim "the guardrail is a clean win." Read full answers, then grep/read the
KB at ${KB} to verify every factual claim yourself — do NOT trust either answer.

Data:
- Full guardrail OFF vs ON answers (16q purposive subset, DeepSeek temp=0, identical retrieval per Q):
  ${FORENSIC}  (each entry: id, category, question, expected_facts, sources, off.answer, on.answer)
- Full OFF vs ON answers for the 10 paired-eval fact DROPS:
  ${FORENSIC_DROPS}  (same schema; use for any dropped question's text)
- Paired fact-recall analysis over ALL 102q (by-category off->on + per-question drops/gains):
  ${PAIRED}
- ${NOISE_FLOOR}
- KB (authoritative, read-only): ${KB}

The guardrail adds two system-prompt rules: (7) never emit a controlled-terminology "C" code unless it
appears verbatim in the retrieved context; (8) never assert a domain's SDTM class/category unless context
states it. Background defects it targets: per-value C-code fabrication (model copied one code then guessed
the rest by incrementing) and special-purpose misclassification of relationship datasets.`

const LENS_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    lens: { type: 'string' },
    verdict: { type: 'string', enum: ['PASS', 'FAIL', 'MIXED'] },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          qid: { type: 'string' },
          claim: { type: 'string' },
          kb_evidence: { type: 'string' },
          verdict: { type: 'string', enum: ['fixed', 'residual_defect', 'over_refusal', 'regression', 'no_change', 'ok'] },
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
    key: 'A_code_fabrication',
    prompt: `${COMMON}

LENS A — CONTROLLED-TERMINOLOGY CODE FABRICATION.
Focus questions: q90 (EXROUTE routes), q91 (DSDECOD reasons), q93 (EXDOSFRM dose forms). Also scan EVERY
other ON answer for any "Cxxxxx" code.
For each per-value code the ON answer emits, grep the KB terminology files (e.g. terminology/core/interventions.md,
terminology/core/disposition.md) to check: is that code the TRUE code for that value? Is it present in the
retrieved 'sources' context? Compare to the OFF answer (which fabricated codes — e.g. OFF gave INTRAMUSCULAR=C38239
but true is C28161; INVENTED "INJECTABLE C42899" which does not exist).
Rule on: did ON STOP fabricating (either copies the correct grounded code, or omits the code and gives name-only)?
Any code ON still emits that is wrong OR not in context = residual_defect. Any value where ON correctly
dropped the code to name-only = fixed. Be exhaustive: a single wrong clinical code is a defect.`,
  },
  {
    key: 'B_classification',
    prompt: `${COMMON}

LENS B — CLASS/CATEGORY MEMBERSHIP GROUNDING.
Focus: q37 (Special-Purpose datasets). The TRUE special-purpose domains per model/03_special_purpose_domains.md
are DM, CO, SE, SV, SM (+ SJ). Relationship datasets (RELREC, SUPPQUAL, RELSUB, RELSPEC) live in
model/06_relationship_datasets.md and are NOT special-purpose. OFF wrongly listed RELREC/SUPPQUAL/RELSUB/RELSPEC
as special-purpose. Read the ON answer: does it still misclassify any relationship dataset as special-purpose?
Does it now confine the list to genuine special-purpose members (or hedge appropriately when context is mixed)?
Also scan other concept/cross answers for any ungrounded class assertion. Verify every membership claim against
the KB model/ files.`,
  },
  {
    key: 'C_over_refusal',
    prompt: `${COMMON}

LENS C — OVER-REFUSAL (the guardrail's main risk: false positives).
The guardrail must NOT suppress codes/classes that ARE grounded. Focus on over-refusal probes whose CORRECT
answer carries a grounded codelist code: q16 (AESEV C66769), q19/q91 (DSDECOD C66727), q43 (SEX C66731),
q44 (VS code), s01 (SEX codelist), s05 (VS codelist). For each: the codelist's OWN code (e.g. C66729, C66731)
is normally present in domains/<D>/spec.md "Controlled Terms" and in the terminology header — grep to confirm
it IS in the retrieved 'sources'. Then check: does the ON answer STILL emit that grounded codelist code, or did
the guardrail wrongly make it drop to name-only (= over_refusal)? Also flag any ON answer that refuses/hedges on
content that is plainly present in its context. Over-refusal on a grounded codelist code is a FAIL-level finding.`,
  },
  {
    key: 'D_regression',
    prompt: `${COMMON}

LENS D — GLOBAL REGRESSION / NET QUALITY (noise-aware).
Read ${PAIRED} (all-102q by-category fact off->on + per-question drops/gains). For EACH of the 10 per-question
fact DROPS, open its FULL off/on text in ${FORENSIC_DROPS} and rule whether the drop is (a) a REAL regression
(ON answer genuinely worse / missing a TRUE fact you confirm absent), or (b) an ARTIFACT — substring brittleness
(gold token rephrased, e.g. "Controlled Terms" vs "Controlled Terminology"), temp=0 re-draw (the dropped fact IS
present in the regenerated ON text -> the scored run just sampled differently), or ON dropping a FABRICATED/wrong
token. CRITICAL CONTEXT: ${NOISE_FLOOR} — weigh every drop against this measured envelope; a drop that also
appears in the pure-noise OFF-vs-OFF run (q02/q06/q81) is noise by definition. Conclude: after removing artifacts
and noise-floor drops, how many REAL guardrail-caused regressions remain, and does any category truly regress
beyond the measured noise envelope? Net effect on answer quality.`,
  },
]

phase('Lens')
const lensResults = await parallel(
  LENSES.map((L) => () =>
    agent(L.prompt, {
      label: `lens:${L.key}`,
      phase: 'Lens',
      agentType: 'oh-my-claudecode:scientist',
      model: 'opus',
      schema: LENS_SCHEMA,
    }).then((r) => ({ key: L.key, result: r }))
  )
)
const lenses = lensResults.filter((x) => x && x.result)

phase('Synthesize')
const VERDICT_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    gate_pass: { type: 'boolean' },
    target_defects_fixed: {
      type: 'object',
      additionalProperties: false,
      properties: {
        q37_classification: { type: 'string', enum: ['fixed', 'partial', 'not_fixed'] },
        q90_codes: { type: 'string', enum: ['fixed', 'partial', 'not_fixed'] },
        q91_codes: { type: 'string', enum: ['fixed', 'partial', 'not_fixed'] },
        q93_codes: { type: 'string', enum: ['fixed', 'partial', 'not_fixed'] },
      },
      required: ['q37_classification', 'q90_codes', 'q91_codes', 'q93_codes'],
    },
    over_refusal_detected: { type: 'boolean' },
    over_refusal_detail: { type: 'string' },
    real_regressions: { type: 'array', items: { type: 'string' } },
    net_assessment: { type: 'string' },
    ship_recommendation: { type: 'string' },
  },
  required: ['gate_pass', 'target_defects_fixed', 'over_refusal_detected', 'over_refusal_detail', 'real_regressions', 'net_assessment', 'ship_recommendation'],
}

const synthInput = lenses
  .map((l) => `### Lens ${l.key} -> ${l.result.verdict}\n${l.result.summary}\nfindings: ${JSON.stringify(l.result.findings)}`)
  .join('\n\n')

const verdict = await agent(
  `${COMMON}

You are the SYNTHESIS judge. Below are four independent lens verdicts (code-fabrication, classification,
over-refusal, regression). Fuse them into the GATE decision. Spot-check any disagreement by re-reading the
relevant ON answer + KB yourself before ruling.

GATE (kickoff §4.5): PASS requires ALL of:
  1. q90/q91/q93 no longer fabricate codes (ON either copies grounded codes or omits to name-only);
  2. q37 no longer misclassifies relationship datasets as special-purpose;
  3. NO over-refusal — grounded codelist codes still emitted;
  4. fact recall does not regress beyond temp=0 noise (~1pt) in any category, net non-negative.

LENS VERDICTS:
${synthInput}

Return the structured gate verdict. ship_recommendation: should the guardrail default-ON ship, ship with
caveats, or be reworked? Be decisive and evidence-anchored.`,
  { label: 'synthesize', phase: 'Synthesize', agentType: 'oh-my-claudecode:scientist', model: 'opus', schema: VERDICT_SCHEMA }
)

return { lenses: lenses.map((l) => ({ lens: l.key, verdict: l.result.verdict, summary: l.result.summary })), verdict }
