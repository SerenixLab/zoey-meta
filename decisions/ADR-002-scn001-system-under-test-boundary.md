# ADR-002: SCN-001 System-Under-Test Boundary

Status: `Proposed`

Date: 2026-07-07

Decision authority: project owner

Related open question: `EVAL-006`

Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.3`
- `decisions/ADR-001-first-vertical-slice.md`

## Decision

For the first `SCN-001` milestone, use a transition-inside boundary.

The harness supplies synthetic interaction events, fixture time facts, fixture surface/context labels, Japanese exercise observations, user feedback, and later-session events. The system under test performs the semantic transitions required to make the run falsifiable: stale-history handling, attributed assertion handling, scoped interpretation, behavioral-trial activation, correction handling, intervention-conditioned outcome update, and state-inspection reporting.

The system under test must keep at least one evidence-responsive behavioral-trial transition inside the boundary that crosses an interaction boundary. The required inside transition is:

```text
current and retained evidence
    -> Zoey-derived scoped delayed-correction trial for spontaneous production
    -> later synthetic spontaneous-session behavior changes
    -> observed outcome updates the trial without proving the causal theory
```

This ADR answers only the system-under-test boundary for `EVAL-006`. It does not define implementation architecture, repository boundaries, storage engines, model/runtime choices, real personal-history custody, voice/avatar behavior, external operations, Japanese pedagogy, final state schemas, or acceptance gates.

Until this ADR is accepted by the project owner, `EVAL-006` remains `Active`.

## Relationship To ADR-001 And EVAL-006

`ADR-001` accepted `SCN-001 V0.2.2: Japanese Longitudinal Development` as the first vertical-slice pressure path and made `EVAL-006` the next active question.

`EVAL-006` asks which semantic inputs, control facts, time events, external behavior, and cognitive candidates are inside the selected first-slice system under test versus supplied by the harness or simulated dependencies.

This ADR proposes that split. If accepted, it resolves `EVAL-006` for the first milestone only and enables re-triage of the next evaluation and state questions. It does not claim that the first milestone passes full `SCN-001`.

## Thin SCN-001 Transition Map

The first milestone should exercise this thin path:

1. Harness initializes disposable prior Japanese practice history with old beginner-session events and a known practice gap.
2. The user resumes practice and makes conflicting self-assessments.
3. The system under test records those as attributed statements, marks old history as stale, and avoids creating current skill facts from either source alone.
4. Harness supplies calibration observations showing stronger recognition than spontaneous production.
5. The system under test preserves the recognition/production distinction and may form a weak scoped hypothesis.
6. The system under test proposes or activates a reversible production-focused trial instead of replaying stale difficulty assumptions.
7. Harness supplies focused-drill acceptance, explicit immediate-correction request, drill outcome, and positive drill feedback.
8. The system under test stores the explicit drill preference, trial evidence, and short-term outcome separately.
9. Harness advances to a later synthetic spontaneous spoken-interaction context and supplies correction-friction events.
10. The system under test handles the user's "let me finish first here" correction immediately, without erasing prior positive drill evidence.
11. The system under test creates a broader Zoey-derived scoped trial for spontaneous production: delay minor correction until turn completion unless drill mode is active.
12. Harness advances to a later synthetic spontaneous session and supplies observed outcome evidence.
13. The system under test applies the scoped delayed-correction trial, records the outcome as intervention-conditioned, and does not treat it as proof of the causal theory.
14. When asked why behavior changed, the system under test produces an explanation trace grounded in retained state rather than a plausible retrospective story.

## Boundary Table

| Material transition or responsibility | Boundary class | First-milestone expectation |
| --- | --- | --- |
| Disposable prior Japanese practice history exists before the run | Harness-supplied | The harness provides old beginner-session event history, prior particle-error observations, and prior drill feedback as fixture state. |
| Real authoritative Zoey personal history or continuity exists | Excluded | The milestone uses synthetic or disposable fixture state only. |
| Practice gap and later-session ordering are known | Harness-supplied | The harness supplies explicit time facts such as "after a gap" and "days later." |
| General governed-clock, expiry, freshness, due-state, or scheduling machinery | Deferred | The boundary may require fixture time labels, not a reusable clock contract. |
| User resume request and conflicting self-assessments are received | Harness-supplied | The harness supplies the utterance events. |
| Resume request and self-assessments become attributed statements rather than current facts | Inside system under test | The system records source, time/context, attribution, and epistemic status. |
| Old history is marked relevant but stale | Inside system under test | The system may use old history as context but cannot promote it to current proficiency. |
| Calibration exercise content, scoring, and recognition/production observations | Simulated dependency | A fixture scorer supplies structured observations; the system does not need real Japanese assessment ability. |
| Recognition and spontaneous-production evidence remain separate | Inside system under test | The system must not collapse them into one scalar skill judgment. |
| Weak scoped hypothesis about production difficulty is formed or withheld | Inside system under test | Any hypothesis must preserve evidence lineage, scope, confidence, and uncertainty. |
| Production-focused behavioral trial is proposed or activated from calibration evidence | Inside system under test | This is an evidence-responsive trial, not a broad learning-style or identity claim. |
| User accepts focused drill | Harness-supplied | The harness supplies the acceptance event. |
| Drill item generation and Japanese correction content | Simulated dependency | The harness or a simulated tutoring component supplies the drill content and correctness observations. |
| Immediate correction is requested within the focused drill | Harness-supplied | The harness supplies the explicit request event. |
| Immediate correction is scoped to the focused drill | Inside system under test | The system distinguishes explicit drill preference from broader correction policy. |
| Drill outcome and positive feedback are observed | Harness-supplied | The harness supplies short-term accuracy improvement and user feedback. |
| Drill preference, trial evidence, and short-term outcome are retained separately | Inside system under test | The system must not claim long-term efficacy from drill outcome alone. |
| Later spontaneous voice-session context exists | Harness-supplied | The harness supplies a synthetic surface/context label; no real voice stack is in scope. |
| Real voice, STT, TTS, avatar, Live2D, prosody, or embodied behavior | Excluded | The milestone may reason over a supplied context label but may not claim voice/avatar behavior. |
| Initial over-aggressive interruption occurs in the spontaneous session | Harness-supplied | The harness supplies the relevant event or observed correction-friction fact. |
| User says "let me finish first here" | Harness-supplied | The harness supplies the correction utterance. |
| Current-session behavior changes immediately after the correction | Inside system under test | The system must apply the correction in the current scope. |
| Broader delayed-correction trial for spontaneous production is created | Inside system under test | This Zoey-derived trial must be distinct from the user's direct current-session instruction and from focused-drill preference. |
| Later spontaneous-session behavior differs because of retained trial state | Inside system under test | This is the required cross-interaction behavioral-trial transition inside the boundary. |
| Later user outcome feedback and longer speaking observation | Harness-supplied | The harness supplies the observed outcome and user statement. |
| Outcome updates the delayed-correction trial as intervention-conditioned evidence | Inside system under test | The system may strengthen the observed-effect record but must not prove an untested cause. |
| Explanation of changed correction behavior | Inside system under test | The system must reconstruct from retained state and expose uncertainty. |
| Private learning-history disclosure across real actors, audiences, or trust boundaries | Deferred | The first milestone may carry context labels but does not decide user-facing disclosure policy. |
| Full 40-session longitudinal anti-sycophancy drift detection | Deferred | The first milestone must preserve enough lineage for later trajectory inspection but does not claim full longitudinal-variant pass. |
| SCN-001 adversarial variants and nondeterministic acceptance policy | Deferred | These belong to later fixture, oracle, and acceptance-gate questions. |
| Calendar mutation, external operations, actor-assurance events, and provider reconciliation | Excluded | Those are `SCN-002` pressures and are not part of this milestone. |

## First Milestone Claim Boundary

The first milestone may claim only this:

Under synthetic `SCN-001` fixture inputs and this boundary, the system under test can preserve and transition selected semantic state across interactions such that later behavior changes because of retained, attributable evidence and correction history, while inspection output distinguishes assertion, observation, inference, trial, outcome, correction, and uncertainty.

The first milestone must not claim:

- full `SCN-001 V0.2.2` pass;
- any pass of mandatory adversarial variants or the full longitudinal variant;
- that Zoey teaches Japanese well;
- that Zoey has assessed real Japanese proficiency;
- real user-memory custody or durable Zoey continuity;
- real voice/avatar behavior;
- external-operation safety or authority handling;
- general memory architecture, final state schema, storage engine, model/runtime, or product workflow readiness.

## Claims Allowed

Allowed first-milestone claims:

- The system can treat old practice history as relevant but stale.
- The system can retain user self-assessments as attributed statements without turning them into current facts.
- The system can keep recognition evidence, production evidence, preference, outcome, and causal explanation separate.
- The system can activate a reversible scoped behavioral trial from evidence rather than only replaying explicit user preference.
- The system can apply user correction immediately in scope while preserving prior contradictory evidence.
- The system can carry a Zoey-derived delayed-correction trial across a later interaction.
- The system can record intervention-conditioned outcome evidence without treating it as independent proof of the theory that caused the intervention.
- The system can explain changed behavior from inspectable retained state.

## Claims Not Allowed

Not allowed from this milestone:

- "Zoey passed `SCN-001`."
- "Zoey has a complete growth system."
- "Zoey has learned the user's Japanese learning style."
- "Zoey knows the user's current Japanese level."
- "Immediate correction helps the user learn" as a general or long-term efficacy claim.
- "Voice users prefer delayed correction" or "text users prefer direct correction."
- "The user is bad at particles," "bad at Japanese," or "bad at languages."
- "The user was tired" unless the fixture supplies Zoey-available evidence sufficient for that narrower claim.
- "The system is ready for real personal memory, real voice, or external operations."

## Minimal State-Inspection Output Expectations

The first milestone does not need a final schema, but inspection output must expose at least:

- run boundary and baseline identifiers, including this ADR, `SCN-001 V0.2.2`, and the synthetic fixture name;
- retained event history with source, occurrence/order time, observation time where relevant, surface/context label, and fixture provenance;
- attributed user assertions distinct from objective or operationally authoritative facts;
- calibration and drill observations with recognition and production dimensions preserved separately;
- hypotheses with evidence lineage, scope, confidence or uncertainty marker, and prohibited overgeneralizations where relevant;
- behavioral-trial records with candidate/active/narrowed/retired status, activation basis, declared scope, reversibility/correction path, and outcome lineage;
- explicit user preferences or corrections distinct from Zoey-derived trials;
- intervention-conditioned outcome records that identify the active trial or behavior under which the outcome was observed;
- supersession or narrowing history after user correction;
- explanation trace linking the final "why are you correcting differently now" answer to retained state rather than hidden narrative generation;
- enough transition timestamps or ordering markers to show that the later behavior used prior retained state, not a post-hoc rewrite.

Inspection output may be structured however a future implementation chooses. The requirement is semantic inspectability, not a prescribed storage format.

## Demo-Gaming Risks

The boundary is designed to prevent these narrative-only successes:

| Risk | Boundary response |
| --- | --- |
| A demo hardcodes the final explanation while no state actually changed. | Explanation must be backed by inspectable event, assertion, hypothesis, trial, correction, and outcome records. |
| The harness supplies all semantic transitions and the system only replays them. | Scoped interpretation, trial activation, correction handling, later trial application, and outcome update remain inside the system under test. |
| The system stores a scalar "particle skill" and claims adaptation. | Recognition and production evidence must remain distinct, and global skill or identity claims are prohibited. |
| The system merely replays explicit user preferences. | At least one Zoey-derived scoped trial crossing an interaction boundary is required. |
| The system treats positive feedback as proof of a broad learning style. | Outcomes are intervention-conditioned and scoped; untested causal explanations remain uncertain. |
| The system erases contradictory history after correction. | Prior drill feedback and later voice correction must both remain inspectable with supersession or scope distinctions. |
| The system claims voice behavior because the scenario says "voice." | Voice is only a supplied context label; real voice/avatar behavior is excluded. |
| The system claims a full scenario pass from a base-path demonstration. | The first milestone claim is explicitly narrower than full `SCN-001` pass. |

## Re-Triage Notes

`TIME-001` remains `Open` and should not become automatically active from this ADR alone. The first boundary uses harness-supplied ordering and time facts to express staleness and later interactions. A governed-clock contract becomes blocking only if the next milestone needs reproducible clock advancement, expiry, freshness transitions, or longitudinal time mechanics beyond explicit fixture facts.

Likely next narrow question for `TIME-001`: what minimal scenario-clock fields must the fixture and oracle expose for stale-history and days-later interaction checks without designing a general clock system?

`GROW-001` remains `Open` and should not become automatically active from this ADR alone. The first boundary can proceed by allowing only scoped, reversible behavioral trials and by disallowing durable developmental-adaptation claims. `GROW-001` becomes blocking before the project claims a general criterion for posture versus trial versus durable adaptation, or before durable user-facing adaptations enter scope.

Likely next narrow question for `GROW-001`: what minimum activation and inspection criteria distinguish a selected-slice behavioral trial from a situational correction or durable adaptation?

## Follow-On Questions After Acceptance

If the project owner accepts this ADR, likely next questions are:

- `EVAL-001`: decide whether the first milestone tests context discovery or receives curated scenario context from the harness.
- `EVAL-002`: define fixture and oracle data for this boundary without requiring hidden chain-of-thought.
- `EVAL-003`: define nondeterministic-run handling and hard invariant failures.
- `SLICE-002`: decide the minimum selected-slice state needed after the fixture and evaluation boundary are known.
- `TIME-001`: re-triage for a minimal fixture-clock contract, if needed.
- `GROW-001`: re-triage for the selected-slice trial/adaptation distinction, if needed.
- `EVAL-005`: later, identify which unresolved questions affect scoreability and which can be carried as bounded assumptions.

Acceptance of this ADR should not automatically activate every selected-slice trigger check. The register should be re-triaged according to `OPEN_QUESTIONS.md`.

## Consequences

Positive:

- Keeps the first `SCN-001` milestone falsifiable without requiring real personal memory, voice, or pedagogy.
- Leaves a meaningful evidence-responsive cross-interaction behavioral-trial transition inside the system under test.
- Forces state inspection to carry enough provenance and lineage to reject plausible retrospective storytelling.
- Preserves `ADR-001` guardrails against premature general architecture.

Negative:

- The harness must be explicit enough that fixture-supplied facts do not smuggle in the behavior being tested.
- The milestone still cannot claim full `SCN-001` pass.
- Later questions must still define fixture/oracle data, nondeterministic acceptance, and minimum selected-slice state.

## Non-Decisions

This ADR does not decide:

- final state schema;
- persistence mechanism;
- storage engine;
- model, runtime, prompt, or agent structure;
- product surface or UI;
- Japanese curriculum, exercise generation, or grading quality;
- real voice or avatar behavior;
- real personal-history custody or recovery;
- external operations;
- acceptance-gate scoring;
- full longitudinal drift-detection criteria.
