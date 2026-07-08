# ADR-006: SCN-001 Selected-Slice State Contract

Status: `Proposed`

Date: 2026-07-08

Record revision: `Draft R0`

Decision authority: project owner

Related open question: `SLICE-002`

Decision-Time Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.14`
- `decisions/ADR-001-first-vertical-slice.md` `R1`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`
- `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md` `R2`
- `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md` `R3`
- `decisions/ADR-005-scn001-selected-slice-fixture-oracle-contract.md` `R2`

Proposed post-decision register state: acceptance of this ADR would resolve `SLICE-002` for the first `SCN-001` selected slice, activate `DEP-001` as the next immediate frontier, leave `SLICE-003` blocked until dependency identity metadata is known, and re-triage `SLICE-005`, `EVAL-004`, and `EVAL-005` without automatically activating them.

## Decision

Adopt a minimum selected-slice state contract for `SCN001-SSFO-V0.2.0`.

The first selected slice uses run-scoped retained semantic state plus lineage-preserving projections. It must not turn every oracle-visible field from `ADR-005` into independently persisted database state.

For this ADR, "persisted" means retained inside the evaluated synthetic run long enough to drive the later SUT transition, support oracle inspection, and support the final explanation. It does not mean production memory custody, durable Zoey continuity, real personal history, or a final storage schema.

The selected slice classifies oracle-visible information into four categories:

1. `independent_sut_state`: SUT-owned retained semantic state or transition state whose identity, lifecycle, or later use matters.
2. `lineage_preserving_projection`: a view or reference over the same retained SUT state or retained input facts, adding no new fixture-authored semantic conclusion.
3. `derived_inspection_fact`: an oracle-computed fact used to validate, score, or compare exposed state without becoming behavior-driving SUT state.
4. `fixture_or_oracle_only`: fixture setup, evaluator annotation, branch policy, score, claim-class mapping, or hidden ground truth that must not become SUT-owned semantic state.

The implementation may use event-sourced records, mutable semantic records with transition logs, tables, documents, in-memory objects captured by the harness, or another inspectable representation. The representation passes this contract only if the required identities, lineage, ordering, scopes, lifecycle distinctions, and claim boundaries below are preserved.

## Classification Rule

An oracle-visible fact requires independently retained SUT state when any of these are true:

- a later behavior disposition, activation, outcome update, or explanation must use the same SUT-owned object or transition basis;
- the SUT owns the semantic transition and another required transition depends on that result;
- loss or conflation of the fact is a hard invariant or positive-obligation failure under `ADR-005`;
- the fact binds candidate -> proposal -> response -> activation -> active trial -> later use -> outcome -> explanation identity.

An oracle-visible fact may be a lineage-preserving projection when:

- it only exposes the same retained state in an oracle-friendly shape;
- it can be regenerated from retained input facts, retained transition records, and stable state references;
- it does not add relevance rankings, applicability verdicts, trial choices, temporal conclusions, or support claims that the SUT was responsible for producing.

An oracle-visible fact may be a derived inspection fact when:

- it exists only to validate ordering, equivalence, distinguishability, eligibility, claim support, or failure classification;
- it is not consulted by the SUT as behavior-driving state;
- it can be recomputed by the oracle from exposed effective state, fixture facts, and accepted rule IDs.

A fact is fixture/oracle-only when it is an answer key, path-pressure label, claim-class result, campaign score, branch-control rule, evaluator note, hidden scenario ground truth, or canonical expectation. These facts must not be represented as SUT semantic memory.

## Minimum Independent SUT State

The selected slice requires these retained SUT state anchors or equivalent lineage.

| State anchor | Minimum retained content | Why independent state is required |
| --- | --- | --- |
| Run-scoped semantic namespace | Run state identity, fixture/oracle package ref, accepted baseline refs visible to the SUT where applicable, evaluation-only retention basis refs, permitted-use/run-scope/discard status, and delivered SUT-visible control fact refs. | Prevents selected-slice state from masquerading as real durable memory while allowing cross-interaction retention inside the run. |
| Retained input-fact references | Fixture item IDs actually ingested or used, role/provenance, occurrence/observation time, session order, context labels, task-mode labels, and copied value fields needed for later SUT use. | Later SUT transitions and explanations must cite stable facts without requiring the harness to reconstruct semantic state. |
| Attributed communication/assertion state | Current-path utterance refs, source actor, time/context, attributed status, epistemic status, status origin, and SUT transition-basis refs for SUT-derived attribution. | `C-001`, `C-002`, and `C-003` must become attributed assertions, not current skill facts. Fixture-initialized historical status remains origin-marked input. |
| Observation evidence state | Recognition, production, drill, and outcome observation refs with task mode, dimension, correctness, scorer provenance, and separation from interpretation. | Recognition/production comparison and later outcome lineage require observations to remain distinct from conclusions. |
| Temporal eligibility assessment | Assessed evidence/basis ref, use target, scenario time, selected `>90 scenario days` rule result where applicable, temporal uncertainty, and no re-dating of historical facts. | The SUT owns stale/current-authority judgment; old history cannot be stale because the fixture says so, and recent history cannot be marked stale by blanket retention age. |
| Dimension comparison state | Recognition evidence refs, production evidence refs, target dimension, scoped comparison result, uncertainty, and no global skill/proficiency claim. | Trial formation must be evidence-responsive to the current recognition/production split and inspectably not a scalar Japanese-level judgment. |
| Trial candidate state | Candidate ID, material intent, trial-direction ref or non-activation disposition, source, provisional/evaluative purpose, support lineage, proposed scope, reversibility/correction path, lifecycle status, and current/stale-basis status or unresolved status. | Candidates must retain identity before proposal and activation, and unsupported candidates must not drive behavior. |
| Proposal intent and binding state | Surfaced proposal ref, candidate ref, SUT material intent, realization ref where applicable, user response ref, binding assessment, ambiguity/conflict status, and activation-basis status. | The production-focused trial can activate only through a response bound to the actual candidate-specific proposal. |
| Activation assessment state | Candidate ref, activation basis type, check results for scope, basis lineage, current/stale basis, user-governed constraints, reversibility, consequence, current applicability, retention basis, and non-adaptation boundary. | Active trial state is valid only after inspectable activation checks; acceptance or candidate formation alone is insufficient. |
| Active scoped trial state | Active trial ID, activation time/order, candidate lineage, activation-check refs, active scope, retained-state identity, current status, narrowing/retirement/supersession/conflict refs, and correction path. | Later behavior and counterfactual branches must use the same retained active trial state, not a fixture-authored copy or candidate-only state. |
| Scoped user-governed instruction/preference state | Explicit drill immediate-correction request refs, scope, authority/status origin, applicability, and distinction from active trials and outcomes. | `D-002` must remain a focused-drill request, not a global correction preference or delayed-correction trial. |
| Direct correction disposition state | Current-session behavior disposition ID, correction-event basis, context scope, timing/order, realization ref where applicable, and explicit distinction from future trial state. | `V-003` must change current behavior immediately without silently becoming durable preference, active trial, or global policy. |
| Later-use applicability state | Active trial ref, later context refs, applicability review result, narrowing/supersession/conflict result where applicable, selected behavior disposition ref, and pre-outcome ordering. | Active does not mean indefinitely applicable; later behavior must be selected from retained state before outcome facts are supplied. |
| Behavior disposition state | SUT-selected drill, current-session, and later behavior disposition IDs, material intent, selected timing behavior, basis refs, and simulator realization refs. | Simulated dependencies may realize behavior but must not choose the policy being tested. |
| Realization link state | SUT proposal/disposition ref, simulator realization fact ref, fidelity/mismatch origin where delivered, and realized behavior descriptor where used by the SUT. | Outcome lineage must attach to the behavior actually realized without letting simulator facts choose SUT policy. |
| Intervention-conditioned outcome state | Outcome record ID, outcome fact refs, active trial ref, behavior disposition ref, realized behavior ref, material context refs, co-intervention status, intervention-conditioned classification, and causal uncertainty. | The SUT must record outcome evidence as scoped and intervention-conditioned without proving the causal theory. |
| Explanation support output | Explanation support ID, user-facing claim refs, retained state refs, transition-basis refs, uncertainty markers, excluded claim boundaries, and no hidden chain-of-thought dependency. | The final explanation must be grounded in retained state. The support record may be generated at explanation time, but it must cite retained identities. |
| Non-activation and unsupported-boundary state | Withhold/defer/request-more/ask-clarification/retire/narrow disposition, affected candidate or proposed broader effect, basis refs, and unsupported durable-adaptation boundary where implicated. | Counterfactual success and durable-adaptation exclusion require inspectable non-activation, not silent absence or hidden refusal. |

The minimum contract does not require each row above to be a separate table, class, document, or database collection. It requires that the effective SUT representation preserve the listed semantic identity and lineage.

## ADR-005 Oracle Field Mapping

| `ADR-005` field family | SLICE-002 classification | Minimum contract |
| --- | --- | --- |
| Run boundary | Derived inspection plus retained run namespace | Campaign/run/path/evaluation identifiers are mainly harness/oracle metadata. The SUT must maintain a run-scoped state namespace and any SUT-visible control refs it uses. |
| Retention basis | Retained input/control fact plus SUT application state | `FC-RET-001` remains fixture-supplied, but the SUT must retain enough to show selected state is run-scoped, permitted for evaluation use, and discardable after trajectory. |
| Event history | Retained input-fact references; projected event history view | Fixture event facts keep fixture provenance. SUT projections must not turn them into derived semantic conclusions. |
| Attributed assertions | Independent SUT state for current-path attribution; retained fixture-origin state for initialized history | Current resume utterances require SUT-derived attribution. Fixture-initialized historical status remains marked as fixture-origin. |
| Observations | Retained input-fact references plus independent derived comparison/outcome records where used | Raw item/correctness facts are fixture-origin; SUT-owned comparisons and outcome classifications are separate. |
| Temporal judgments | Independent SUT transition state or equivalent transition log | The SUT owns current-authority eligibility and stale-basis assessment. Oracle may derive correctness from chronology and rule IDs. |
| Dimension comparison | Independent SUT transition state or equivalent transition log | The scoped recognition/production comparison must be inspectable before candidate formation. |
| Trial candidate | Independent SUT state | Candidate identity, material intent, source, scope, support lineage, and lifecycle status must persist until proposal, activation, withholding, retirement, or explanation as applicable. |
| Proposal binding | Independent SUT state | Proposal intent, surfaced proposal, realization, response, and binding assessment must remain distinct from candidate and activation. |
| Activation checks | Independent SUT transition state | Activation-check result sets must be retained or reconstructable from retained transition records without oracle-added conclusions. |
| Active trial | Independent SUT state | Active trial identity must persist across the synthetic interaction boundary and through canonical and counterfactual later-use checks. |
| Direct correction disposition | Independent SUT state | Current-session correction behavior must be inspectable and distinct from future trial state. |
| Later-use applicability | Independent SUT transition state | Later behavior selection must record active trial ref, applicability review, disposition, and pre-outcome ordering. |
| Realized behavior | SUT disposition is independent; simulator realization fact is retained input/projection | The SUT owns the intent or disposition. The simulator owns fidelity and realized-behavior facts. |
| Outcome record | Independent SUT state | Intervention-conditioned classification and uncertainty must be retained with active trial, disposition, realization, outcome, and material-context refs. |
| Explanation support | SUT-generated inspection output over retained state | It may be generated at `DP-EXPLAIN`; it must cite retained state IDs and must not require hidden chain-of-thought. |
| Failure artifacts | Oracle-only | Validity, hard-failure, obligation, aggregation, and claim-boundary classifications are not SUT semantic state. |
| Claim-class result vector | Oracle-only | `PASS`, `OBLIGATION_FAIL`, `NOT_REACHED`, `HARD_FAIL`, and campaign aggregation are scoring artifacts. |
| Completeness declarations | Fixture/oracle-only, except SUT-visible control facts may be retained as input facts | Exhaustiveness rules guide fixture/oracle interpretation; they must not become hidden SUT knowledge beyond declared SUT-visible controls. |
| Branch policy and path gating | Fixture/oracle-only | The SUT may observe delivered facts and simulator results, not the canonical answer path. |
| Bounded claim language | Oracle/reporting boundary | The SUT must avoid overclaims, but campaign claim text is not behavior-driving semantic state. |

## Lineage-Preserving Projection Rules

Lineage-preserving projections are allowed and expected. They are how this state contract avoids becoming a final schema.

A projection is valid only if it:

- points to retained state or retained input facts by stable reference;
- preserves source provenance, chronology, semantic status origin, scope, lifecycle, and transition basis;
- can be regenerated without changing the underlying semantic meaning;
- does not add fixture-authored stale/current labels, trial recommendations, applicability verdicts, relevance rankings, or causal conclusions;
- does not replace a lost candidate, proposal, active trial, behavior disposition, or outcome record.

The `sut_state_reference` items in `ADR-005`, including `L-002` and `CF2-L-003`, are projections to retained SUT state. They are valid only if they reference the same active delayed-correction trial state created and retained earlier in the same formal run trajectory.

## Derived Inspection Facts

The oracle may derive these facts from effective state without requiring them as independently persisted SUT state:

- whether historical evidence was re-dated, refreshed, or rewritten;
- whether a later behavior disposition was recorded before outcome facts;
- whether proposal, response, activation, active trial, later use, outcome, and explanation refs form one valid lineage chain;
- whether recognition and production evidence remained separate;
- whether a projection is identity-preserving or a semantic copy;
- whether a candidate, direct correction, active trial, durable adaptation, and explicit preference remained distinguishable;
- whether hard invariant, positive obligation, invalidity, claim-class, or aggregation rules passed or failed;
- whether an artifact-level claim exceeds the bounded claim language.

These derived facts may appear in oracle reports and failure artifacts. They must not be used to make the SUT behave correctly during the evaluated run.

## Fixture And Oracle Facts That Must Not Become SUT State

The SUT may retain SUT-visible fixture payloads as input facts with fixture provenance. It must not retain evaluator-only or oracle-only material as semantic state.

Prohibited SUT-owned semantic state includes:

- evaluator ground truth such as fatigue contribution, canonical causal explanation, or absence of a real cross-surface preference;
- canonical expectation labels, scoring comments, answer keys, and path-pressure labels;
- claim classes, obligation IDs, invariant IDs, invalidity IDs, aggregation rules, and pass/fail results;
- branch policy that tells the SUT which proposal or behavior will receive canonical continuation;
- hidden labels such as "weak production", "best trial", "current proficiency", "stale", "fresh", "active trial is correct", or "voice preference";
- campaign aggregation results, run-validity classifications, replacement-policy decisions, and failure artifacts;
- global user/profile conclusions such as real Japanese level, learning style, real personal memory, durable Zoey continuity, real voice behavior, or general correction efficacy.

## Identity Across The Selected Trajectory

The selected canonical trajectory requires identity preservation through this chain:

```text
retained input facts
    -> attributed assertions and temporal/comparison transition state
    -> production-focused trial candidate
    -> candidate-bound proposal
    -> proposal realization and bound user acceptance
    -> activation checks
    -> active production-focused trial
    -> focused-drill disposition, explicit drill request, and short-term outcome
    -> direct current-session correction disposition
    -> separate delayed-correction trial candidate
    -> delayed-correction activation checks
    -> active delayed-correction trial
    -> later-use applicability review
    -> later behavior disposition
    -> simulator realization
    -> intervention-conditioned outcome
    -> explanation support refs
```

Identity rules:

- A trial candidate has its own identity before it is proposed or activated.
- A candidate-bound proposal references the candidate; it does not replace the candidate.
- A user response binds to the surfaced proposal, not directly to a hidden candidate.
- Active trial state has its own retained identity and lineage to the candidate and activation checks.
- Focused-drill immediate correction, direct current-session correction, and delayed-correction trial state are separate objects or equivalent distinguishable records.
- Direct correction may support a later candidate, but it is not itself future active trial state.
- Later-use applicability reviews reference retained active trial state; they do not recreate it.
- Outcome records reference the active trial, behavior disposition, realization, and material context under which the outcome was observed.
- Explanation support cites retained identities rather than a retrospective narrative.

For counterfactual paths:

- `CF-CALIBRATION-NO-SPLIT` must retain a withhold/defer/request-more-evidence basis or equivalent non-activation state if no production-focused candidate is active.
- `CF-DRILL-OPT-IN` must branch from the same-run active delayed-correction state and mark it inapplicable, narrowed, or superseded for the focused drill with explicit immediate-correction opt-in.
- `CF-RECENT-BASIS` must expose a temporal eligibility assessment that does not classify `D-30` prior practice as stale under the selected `>90 scenario days` rule unless a pre-registered material invalidation exists.

## Explicit Non-Scope

This state contract does not support or require:

- retrieval, memory search, relevance ranking, distractor filtering, or production context assembly;
- final database schema, storage engine, serialization format, repository split, or runtime architecture;
- real personal-memory custody, production retention policy, or durable Zoey continuity;
- durable developmental adaptation, learned profile, adapter, embedding, summary store, or training artifact;
- real voice, STT, TTS, avatar, Live2D, or embodied-presence behavior;
- Japanese pedagogy quality, curriculum quality, or real proficiency assessment;
- scheduler, reminder, due-state, expiry, background maintenance, active-trial TTL, or full governed-clock semantics;
- statistical reliability, production readiness, general robustness, or full `SCN-001` pass;
- external operations, actor assurance, authorization, provider reconciliation, or `SCN-002` operation safety.

## Compatibility Red-Team

| Accepted decision | Red-team pressure | State-contract response |
| --- | --- | --- |
| `ADR-001 R1` | The state contract could become a general Zoey memory architecture derived from one Japanese slice. | State is explicitly run-scoped, synthetic, fixture-bound, and non-durable. It preserves first-slice pressure without claiming full `SCN-001`, real continuity, Japanese pedagogy, or architecture generality. |
| `ADR-002 R2` | The harness could satisfy transition-inside obligations by reconstructing retained trial state or handing the SUT a semantic copy. | Active trials, candidates, proposal bindings, activation checks, direct correction, later-use applicability, outcomes, and explanations require retained SUT identities or lineage-preserving projections to those identities. |
| `ADR-003 R2` | Direct correction, explicit drill preference, active scoped trial, stale history, and durable adaptation could collapse into one lifecycle enum. | The contract requires orthogonal state anchors for attribution, temporal eligibility, comparison, candidate, proposal, activation, active trial, direct correction, later-use applicability, outcome, and unsupported adaptation boundary. |
| `ADR-004 R3` | Curated context and oracle fields could become the SUT's database schema or hidden answer key. | SUT-visible fixture facts may be retained only with fixture provenance. Answer keys, claim classes, branch policy, failure artifacts, campaign scores, and evaluator-only notes are fixture/oracle-only. |
| `ADR-005 R2` | The oracle-visible checklist could be copied wholesale into independent state, or under-persisted so later behavior is narrative-only. | The mapping separates independent state from projections and derived inspection facts. Behavior-driving transitions retain identity; scoring, validity, aggregation, and claim-boundary facts remain oracle-only. |

## Proposed Register Effect

If accepted, update `OPEN_QUESTIONS.md` as follows:

- move `SLICE-002` to `Resolved` with outcome `Decision`, resolved by this ADR for the first `SCN-001` selected-slice milestone;
- record that the selected state contract uses minimum run-scoped retained semantic state plus lineage-preserving projections, not a final schema or production memory architecture;
- activate `DEP-001` as the next immediate decision frontier because the selected state/transitions are now known and dependency identity metadata is needed before the internal boundary can be finalized;
- keep `SLICE-003` blocked until `DEP-001` resolves;
- re-triage `SLICE-005` now that minimum state is known, but do not allow it to claim acceptance-gate sufficiency until evaluation-record and scoreability triggers are honored;
- keep `EVAL-004` deferred until the selected slice prepares its first evaluation record, comparison, or compatibility claim;
- keep `EVAL-005` deferred until the selected slice prepares final scoring or scenario-scoreability criteria;
- keep `MEM-001`, `TIME-001`, `GROW-005`, `SURF`, `PROD`, `TRUST`, `CONT`, and `AUTH` questions deferred unless a later artifact introduces their trigger conditions.

## Next Frontier

The recommended next frontier is `DEP-001`: minimum dependency identity metadata for the selected state and transitions.

`DEP-001` should decide what stable reference metadata is required to connect input facts, derived transition state, candidates, active trials, behavior dispositions, outcomes, projections, and explanation support without building a full dependency graph, workflow engine, or production memory system.

## Reconsideration Triggers

Reconsider or supersede this ADR if:

- implementation cannot expose the required retained identities without adopting a materially broader architecture;
- oracle inspection cannot distinguish retained SUT state from fixture-authored projections;
- later behavior cannot be shown to use retained active trial state rather than a generated explanation;
- the selected slice needs retrieval, context assembly, durable adaptation, real memory custody, real voice/avatar, Japanese pedagogy assessment, statistical reliability, or broader `SCN-001` coverage;
- `DEP-001`, `SLICE-003`, `SLICE-005`, `EVAL-004`, or `EVAL-005` cannot preserve this state/projection boundary.

## Non-Decisions

This ADR does not decide:

- internal module or repository boundaries;
- dependency identity metadata beyond naming it as the next frontier;
- implementation storage format;
- evaluation-record metadata;
- final acceptance gate;
- scoreability criteria;
- production memory policy;
- product inspection UI;
- model, prompt, runtime, or dependency choices.
