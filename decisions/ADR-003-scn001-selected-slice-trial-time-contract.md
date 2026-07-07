# ADR-003: SCN-001 Selected-Slice Trial And Time Contract

Status: `Proposed`

Date: 2026-07-07

Record revision: `R0`

Decision authority: project owner

Related open questions: `GROW-001`, `TIME-001`

Decision-Time Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.7`
- `decisions/ADR-001-first-vertical-slice.md` `R1`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`

## Decision

Adopt one selected-slice contract for `GROW-001` and `TIME-001` under accepted `ADR-002`.

For the first `SCN-001` milestone, the system under test may support scoped, reversible behavioral trials that cross the synthetic interaction boundary. It must not claim durable developmental adaptation, a full growth architecture, general time machinery, scheduler behavior, reminders, due-state handling, or expiry machinery.

The harness supplies bounded events, observations, user responses, context labels, and chronology facts. The SUT owns the selected semantic transitions: stale-history classification, trial-candidate formation, candidate-bound proposal where applicable, activation-basis validation, active-trial transition, current-session correction disposition, later behavior disposition, and intervention-conditioned outcome update.

If accepted, this ADR resolves `GROW-001` and `TIME-001` for the first `SCN-001` milestone only. It does not amend the `ADR-002` SUT boundary.

## Critical Analysis Of The Current Gap

The current documents are directionally consistent, but several constraints are not yet tight enough for `EVAL-002`, `SLICE-002`, or `SLICE-005`.

1. `ADR-002` requires trial candidates, accepted candidates, active trials, narrowed/retired state, and unsupported durable adaptation boundaries, but it does not define the minimum status map. Without this, a fixture could pass by storing one generic preference or one generic adaptation record.
2. `ADR-002` requires activation checks for both the production-focused trial and the delayed-correction trial, but only the production-focused path clearly includes a candidate-bound proposal and user acceptance. The delayed-correction path needs a selected-slice activation basis that remains weaker than a durable preference and stronger than mere current-session posture.
3. The docs say old history is relevant but stale, while also requiring the SUT to own stale-history handling. `TIME-001` must prevent the harness from smuggling in the stale judgment while still giving the SUT reproducible chronology.
4. `SCN-001` allows evaluator inspection of adaptation candidates or active adaptations, while `ADR-002` forbids first-milestone durable adaptation claims. The selected slice must reconcile this by allowing no active durable adaptation and, at most, an unsupported or withheld adaptation boundary.
5. The phrase "trial crosses an interaction boundary" can be mistaken for scheduler, reminder, due, expiry, or autonomous background-maintenance scope. The selected slice needs only retained trial state plus supplied session ordering.
6. The State and Control Model requires stale-basis checks, user-governed constraints, scope, consequence, and reversibility, but the first milestone has not named the minimum inspection fields needed to show those checks occurred without prescribing a final schema.

The smallest fix is one joint selected-slice contract. Splitting `GROW-001` and `TIME-001` would create an unnecessary dependency cycle because stale-basis validity is one of the activation checks for trial state.

## Selected-Slice State Meanings

### Direct Situational Correction

A direct situational correction is an immediate behavior change in the current interaction or current declared scope because the user corrected Zoey or gave a valid scoped instruction.

Minimum requirements:

- basis is the user correction or instruction event, with source, chronology, and context preserved;
- scope is current-session or otherwise explicitly narrow from the user's wording and context;
- current behavior changes immediately where the correction is applicable;
- prior differently scoped evidence is not erased;
- the correction is not silently promoted to a future preference, active trial, or durable adaptation.

In the selected path, "Don't stop me mid-sentence like that here. Let me finish first." directly supports a current-session spontaneous-production behavior disposition. Any future generalization remains a separate Zoey-derived trial candidate.

### Trial Candidate

A trial candidate is proposed behavior-affecting state that is not yet active. It may be generated from bounded observations, attributed history, explicit user request, current correction, or governed exploration.

Minimum requirements:

- material trial intent is identifiable;
- basis and evidence lineage are retained;
- candidate source is distinguishable, such as Zoey inference, explicit user request, user correction, or exploration;
- proposed scope is declared across relevant dimensions such as subject, activity, task mode, surface/context label, audience where relevant, temporal relation, and consequence ceiling;
- reversibility or correction path is identifiable;
- current/stale-basis status is not assumed;
- candidate status is inspectable;
- no candidate affects later behavior as an active trial until activation basis and activation checks are satisfied.

The SUT may withhold trial formation, ask for more evidence, defer, or record insufficient support. The affordance set must allow those outcomes.

### Active Scoped Trial

An active scoped trial is a retained, provisional, reversible behavior change that may influence later behavior disposition inside its declared scope.

Minimum requirements:

- activation basis is satisfied and inspectable;
- activation checks have passed;
- active scope is no broader than the basis supports;
- active trial can be narrowed, retired, corrected, or superseded;
- later behavior disposition can reference the retained active trial state before outcome evidence is supplied;
- outcomes are recorded as intervention-conditioned and scoped, not as proof of the causal theory that motivated the trial;
- active trial state remains distinct from explicit user preference, direct situational correction, short-term outcome, and durable developmental adaptation.

An active scoped trial may cross synthetic interaction boundaries under the evaluation-only retention basis. That persistence is not a claim of real Zoey continuity or real personal-memory custody.

### Unsupported Durable Developmental Adaptation

For the first `SCN-001` milestone, durable developmental adaptation is unsupported.

The SUT must not activate or claim a durable developmental adaptation when a proposed state would:

- change Zoey's future tendencies, habits, procedures, or defaults beyond a scoped reversible trial;
- create a broad learning-style, identity, personality, motivation, or proficiency claim;
- claim long-term learning efficacy from short-term or intervention-conditioned outcomes;
- turn a surface label such as `voice`, `text`, or `Japanese` into a broad policy;
- require longitudinal trajectory controls not present in the first milestone;
- depend on real personal-history continuity, production retention policy, or full growth architecture.

Valid selected-slice outcomes are: withhold the adaptation, narrow it into a scoped trial candidate, keep it as unsupported for inspection, or retire it. An unsupported durable adaptation must not drive later behavior as active state.

## Minimal Status Map

The first milestone does not require a final schema, but it must preserve these lifecycle distinctions:

| Status | Meaning | May drive later behavior? |
| --- | --- | --- |
| `withheld` | Support is insufficient, no trial candidate is formed. | No. |
| `candidate` | Trial-like state is proposed but activation basis is incomplete. | No. |
| `proposed` | The SUT has surfaced or recorded a proposal bound to the candidate's material intent. | No. |
| `accepted` | The selected activation basis is satisfied, but activation checks have not yet all passed. | No. |
| `active` | Activation basis and checks passed; the trial may influence behavior in scope. | Yes, only in scope. |
| `narrowed` | Scope or applicability has been reduced by correction, conflict, outcome, or stale-basis review. | Yes, only in narrowed scope if still active. |
| `retired` | The trial no longer influences behavior. | No. |
| `unsupported_durable_adaptation` | Proposed durable adaptation exceeds first-milestone support or scope. | No. |

`accepted` is not the same as `active`. User acceptance or correction can satisfy the selected activation basis, but the SUT must still check scope, stale-basis validity, user-governed constraints, reversibility, consequence, and current applicability.

## Selected Activation Basis

The selected slice has two activation-basis paths.

### Production-Focused Trial

For the calibration-derived production-focused trial:

1. The SUT forms or selects a materially evidence-responsive candidate from bounded recognition/production observations and the fixed or independently declared affordance set.
2. The SUT surfaces an inspectable proposal or offer bound to the candidate's material trial intent.
3. The harness supplies a user response semantically bound to the actual surfaced proposal.
4. An unbound, ambiguous, fixed, or silently corrective response cannot satisfy activation basis.
5. After bound acceptance, the candidate still becomes active only if all activation checks pass.

### Delayed-Correction Trial

For the later spontaneous-production delayed-correction trial:

1. The user's correction changes current-session behavior immediately as direct situational correction.
2. A future delayed-correction trial candidate must be separately attributable to the current correction event, prior scoped drill evidence, and spontaneous-production context.
3. Candidate activation does not require a second explicit approval in this selected slice if the proposed trial is low consequence, reversible, materially close to the correction, and scoped no broader than spontaneous production where drill mode or explicit immediate-correction opt-in remains excluded.
4. If the correction basis is ambiguous, materially broader than the user's wording, consequential, conflicting, or not reversible, the SUT must ask, defer, narrow, or withhold activation.
5. The active trial must remain labelled as Zoey-derived trial state, not as a direct user preference or global correction policy.

This selected basis is narrower than a general rule for all future trials. Later milestones may require explicit approval for broader, higher-consequence, less reversible, or more durable behavior changes.

## Activation Checks

Before any trial candidate becomes active, the SUT must inspectably satisfy these checks:

1. `scope`: the active scope is declared and does not exceed the evidence, request, correction, or proposal basis.
2. `basis_lineage`: supporting events, observations, assertions, corrections, and proposal/response binding where applicable are retained with provenance.
3. `current_stale_basis`: old history is not treated as current skill authority; the active basis includes current or currently applicable evidence sufficient for the selected trial.
4. `user_governed_constraints`: explicit preferences, corrections, rules, opt-ins, opt-outs, revocations, and scope conflicts are preserved and resolved by applicability and specificity, not silent last-write-wins.
5. `reversibility`: the trial can be corrected, narrowed, retired, or superseded without requiring a broad migration or identity change.
6. `consequence`: the trial is low consequence within the fixture and does not affect external operations, disclosure rights, commitments, reminders, or real personal history.
7. `current_applicability`: the current context matches the declared scope, and material context changes or co-interventions do not invalidate the basis.
8. `retention_basis`: retained state is covered by the evaluation-only retention basis and remains disposable after the evaluation trajectory.
9. `non_adaptation_boundary`: activation would not constitute an unsupported durable developmental adaptation.

Failing any check prevents activation. The SUT may narrow the candidate and re-check, ask for clarification, defer, retire the candidate, or keep an unsupported state for inspection.

## Minimal Harness Chronology Contract

The harness supplies chronology facts, not temporal conclusions.

For each material event or observation, the harness must supply at least:

- stable event or observation identifier;
- source or fixture provenance;
- occurrence order within the synthetic trajectory;
- occurrence time or relative scenario time;
- observation time if materially different from occurrence time;
- session identifier and session order;
- current scenario time at each SUT decision point or enough ordering to derive it;
- surface/context label and task-mode label where relevant;
- relation to fixture-declared material context changes or co-interventions where relevant.

For the stale-history and later-interaction path, the harness must supply enough chronology to distinguish:

- old beginner-session history before the practice gap;
- current resume session;
- calibration events before the production-focused proposal;
- focused drill and immediate-correction request;
- later spontaneous correction session;
- later spontaneous outcome session;
- outcome evidence occurring after the later behavior disposition.

The harness may supply the practice-gap duration or raw timestamps from which the gap is derivable. It must not supply the conclusion "stale for current skill authority", "fresh enough for activation", "currently valid", or any equivalent temporal-applicability verdict.

Exact wall-clock dates, time zones, calendar recurrence, and real clock synchronization are unnecessary unless a later fixture chooses to express scenario time through wall-clock values.

## SUT-Owned Temporal Judgments

Under this selected contract, the SUT owns these temporal judgments:

- old practice history is relevant historical evidence but stale for current-skill authority when it predates the supplied long practice gap and lacks current corroborating observations;
- old history may guide context, calibration choice, or weak hypothesis formation, but cannot by itself establish current proficiency or activate the production-focused trial;
- current calibration observations are temporally applicable to the production-focused trial only if no material supersession or context invalidation occurs before proposal and activation;
- the current-session correction is immediately applicable to current spontaneous-production behavior in that session;
- a delayed-correction future trial can use the current correction as basis only in materially similar later spontaneous-production contexts, excluding focused drill or explicit immediate-correction opt-in;
- later behavior disposition must be selected from retained active trial state before the harness supplies later outcome evidence;
- outcome updates must preserve the active intervention context, behavior disposition, chronology, material context lineage, and fixture-declared co-interventions;
- temporal uncertainty, insufficient chronology, material gap, or material context change may require narrowing, deferral, clarification, or withholding activation.

The selected stale-history rule is qualitative but fixture-reproducible: pre-gap beginner history is stale for current skill authority until refreshed by current observations in the selected path. User self-assessment remains an attributed assertion, not a current-skill authority source by itself. The old history remains relevant historical evidence.

## Minimum Inspection Fields

The first milestone remains schema-neutral, but inspection output must expose enough effective state to show:

- event chronology and session ordering used by the SUT;
- stale-history judgment and basis;
- trial candidate material intent, source, scope, support lineage, and status;
- proposal binding and bound user response for the production-focused trial;
- activation-basis type and activation-check results for every active trial;
- current-session correction disposition and its current-scope basis;
- distinction between explicit drill preference, production-focused trial, direct correction, delayed-correction trial, and outcome evidence;
- active trial state used by later behavior disposition before outcome evidence;
- outcome record with intervention-conditioned lineage, material context lineage, and co-interventions;
- unsupported durable adaptation boundary where a broader adaptation would otherwise be implied;
- narrowing, retirement, supersession, or conflict history where applicable.

Inspection evidence must come from the effective state and transition basis that the SUT actually uses. A generated explanation or retrospective narrative is not enough.

## Downstream Contract For Blocked Questions

`EVAL-002` must define fixture and oracle data that exercise this contract without handing the SUT the semantic answers. In particular, it must include raw chronology, stable affordance sets, proposal-response binding, counterfactual evidence for hardcoding checks, and oracle checks for activation status and stale-basis handling.

`SLICE-002` must preserve at least the selected-slice state needed by this contract: event chronology, attributed assertions, observations, trial candidate and active trial lifecycle state, current-session dispositions, activation-check basis, and outcome lineage. It need not define a final memory architecture.

`SLICE-005` must phrase the first milestone claim as scoped-trial and selected-slice time/staleness evidence only. It must reject claims of durable developmental adaptation, full growth architecture, scheduler behavior, real personal continuity, or full `SCN-001` pass.

## Claim Boundary

If later artifacts provide sufficient fixture and acceptance semantics, this contract may support a claim that the tested configuration:

- marks old practice history relevant but stale for current skill authority from supplied chronology;
- forms, proposes, activates, and applies selected scoped trials without collapsing them into preferences or durable adaptations;
- distinguishes direct situational correction from future trial state;
- carries active scoped trial state across a synthetic interaction boundary under an evaluation-only retention basis;
- selects later behavior from retained active trial state before later outcome evidence;
- records intervention-conditioned outcomes without proving the causal theory.

This contract does not support claims that:

- Zoey has a complete growth or developmental adaptation system;
- any durable developmental adaptation is active;
- Zoey knows the user's current Japanese proficiency beyond bounded fixture evidence;
- Zoey learned a fixed learning style or cross-surface correction preference;
- Zoey can schedule, remind, monitor due state, expire state, or run a general governed clock;
- Zoey has real personal-memory custody, real continuity, real voice behavior, or real Japanese pedagogy.

## Non-Scope

This ADR does not decide:

- final schemas;
- storage, retrieval, embeddings, summaries, adapters, or learned profiles;
- production retention policy or real personal-history custody;
- full developmental adaptation theory;
- trajectory-level drift detection beyond preserving selected lineage;
- scheduler, reminders, watches, due state, expiry machinery, or background temporal maintenance;
- initiative behavior or proactive follow-up;
- external operations;
- real Japanese curriculum, grading, or pedagogy;
- voice, STT, TTS, avatar, or product UI;
- nondeterministic acceptance policy;
- fixture content, oracle scoring, or paired-counterfactual details beyond the contract constraints above.

## Post-Acceptance Register Effect

If accepted by the project owner, update `OPEN_QUESTIONS.md` to:

- move `GROW-001` to `Resolved` with outcome `Decision`, resolved by this ADR for the first `SCN-001` milestone;
- move `TIME-001` to `Resolved` with outcome `Decision`, resolved by this ADR for the first `SCN-001` milestone;
- preserve the bounded non-support of durable developmental adaptation as part of the first milestone claim boundary;
- preserve the explicit non-scope for scheduler, reminders, due state, expiry machinery, full governed-clock architecture, and full growth architecture;
- re-triage the active frontier before `EVAL-002`, `SLICE-002`, or `SLICE-005`.

Until accepted, this proposed ADR is evidence and a resolution candidate only. It does not close `GROW-001` or `TIME-001`.

## Reconsideration Triggers

Reconsider this contract if:

- `EVAL-002` cannot build fixture data without supplying the stale judgment, trial candidate, activation decision, or later behavior disposition;
- the selected delayed-correction trial requires broader user authorization than the low-consequence, reversible selected basis allows;
- oracle inspection cannot show that later behavior used retained active trial state rather than post-hoc explanation;
- stale-history handling requires background time advancement, expiry, reminders, due state, or general scheduler semantics;
- the first milestone wants to claim durable developmental adaptation, real personal continuity, or full `SCN-001` pass.
