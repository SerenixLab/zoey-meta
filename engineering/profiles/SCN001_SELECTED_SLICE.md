# SCN-001 Selected-Slice Engineering Profile

Profile version: `V0.1.0`

Status: `Draft`

Date: 2026-07-09

Base standard: `ENGINEERING_STANDARD.md` `V0.3.0`

Decision basis:

- `OPEN_QUESTIONS.md` `V0.2.17`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`
- `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md` `R2`
- `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md` `R3`
- `decisions/ADR-005-scn001-selected-slice-fixture-oracle-contract.md` `R2`
- `decisions/ADR-006-scn001-selected-slice-state-contract.md` `R2`
- `decisions/ADR-007-scn001-selected-slice-dependency-identity.md` `R3`
- `decisions/ADR-008-scn001-selected-slice-internal-boundary.md` `R2`

## Purpose

This profile maps the accepted first selected-slice decisions into concrete implementation conformance rules.

It is not a second semantic source for SCN-001. The ADRs listed above remain authoritative. This profile defines engineering consequences, required checks, failure consequences, and attack cases for the first non-throwaway selected-slice implementation.

## Responsibility Shape

The first implementation is expected to keep SUT and evaluation responsibilities distinguishable:

```text
scn001_eval -> declared scn001_sut_core public boundary
scn001_sut_core -> no dependency on scn001_eval
```

The exact language, package manager, test runner, repository layout, and CI provider remain implementation choices.

## Evaluation-Context Barrier

The primary control is semantic, not lexical:

```text
SUT-visible contracts, references, and behavior-driving state do not encode
evaluation-context concepts prohibited by ADR-007 R3 and ADR-008 R2.
```

Known-key scanners for strings such as `expected_transition`, `oracle_rule_id`, `claim_class`, `canonical_match`, or `branch_policy` may be useful as defence in depth. Passing a lexical scanner is not proof of evaluation-context separation.

## Rule Catalogue

### ENG-CONF-IMPORT-001 - SUT Has No Evaluation Dependency

Sources: `ADR-008 R2`.

Scope: `scn001_sut_core`.

Rule: SUT core has no direct or transitive dependency path to evaluation modules, evaluation record families, fixture/oracle packages, harness, simulator, capture/reporting, branch policy, scoring logic, or claim-class labels.

Forbidden shapes:

- `scn001_sut_core -> scn001_eval`;
- `scn001_sut_core -> shared_contracts -> scn001_eval`;
- dynamic imports, reflection, plugin loading, or generated imports that reach evaluation code;
- SUT code using answer-bearing fixture/oracle record types.

Required checks:

- static dependency conformance covers direct and transitive imports where tooling can see them;
- dynamic loading surfaces are forbidden or manual-review gated with residual risk.

Mechanisms: static; manual-review; ci-gate.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-IMPORT-002 - Evaluation Uses Declared SUT Public Surface Only

Sources: `ADR-008 R2`; `ENGINEERING_STANDARD.md` `V0.3.0` `ENG-HEALTH-API-001`.

Scope: `scn001_eval`.

Rule: evaluation code reaches SUT behavior only through declared public boundary surfaces. Harness, simulator, fixture projection, capture, and oracle code do not call private SUT internals or hidden semantic transition commands.

Forbidden shapes:

- simulator imports private SUT modules;
- harness calls internal transition functions by decision-point or expected-transition name;
- tests claim selected-slice behavior evidence while bypassing the public boundary;
- making SUT internals public solely to simplify evaluation setup.

Required checks:

- dependency or import rules distinguish declared public SUT surface from private internals;
- behavior-compatibility samples drive the SUT through the declared public boundary.

Mechanisms: static; automated-test; manual-review.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-PAYLOAD-001 - Closed SUT Ingress

Sources: `ADR-005 R2`; `ADR-008 R2`.

Scope: SUT public input and evaluation-origin payload projection.

Rule: formal SUT ingress is closed against undeclared evaluation-origin material and answer-bearing evaluation context.

Forbidden shapes:

- passing full fixture/oracle records to SUT code;
- passing full simulator evaluation records to SUT code;
- SUT-visible payloads carrying branch policy, path identity, expected transition, oracle rule, claim class, canonical-match, scoring, or hidden answer fields;
- arbitrary extra fields being ignored after crossing into semantic ingestion.

Required checks:

- SUT ingress is closed through separate types, allowlist projection, closed schemas, restricted serializers, typed constructors, or another inspectable closed-contract mechanism;
- if representation permits arbitrary fields, unknown fields are rejected before semantic ingestion;
- negative tests submit full answer-bearing records and prohibited evaluation-context fields.

Mechanisms: structural; static; automated-test; ci-gate.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-PAYLOAD-002 - Rejected Ingress Is Semantically Atomic

Sources: `ADR-005 R2`; `ADR-006 R2`; `ADR-008 R2`.

Scope: SUT public input validation and ingestion.

Rule: rejected SUT ingress has no selected-slice semantic side effects.

Forbidden shapes:

- retaining communication events before discovering prohibited fields;
- creating source relations before rejecting hidden oracle metadata;
- consuming transition order or consumer history for rejected semantic payloads;
- updating behavior-driving state and then returning a validation error.

Required checks:

- `rejected_payload_has_no_semantic_side_effect` negative test or equivalent;
- rejected ingress may create segregated technical/error telemetry but does not alter semantic state, transition evidence, semantic relations, consumer history, or material transition order.

Mechanisms: structural; automated-test.

Test modes: negative; contract.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-ROLE-001 - Role And State-Origin Preservation

Sources: `ADR-005 R2`; `ADR-006 R2`.

Scope: evaluation adapters and SUT-safe projections.

Rule: evaluation adapters preserve input role and state origin. They do not precompute SUT-owned semantic conclusions.

Forbidden shapes:

- raw communication converted by evaluation into correction-control state;
- task observations converted by evaluation into recognition/production split conclusions;
- fixture labels converted into SUT transition results;
- simulator realization converted into semantic correctness.

Required checks:

- adapter tests prove raw communications, observations, chronology facts, context labels, affordances, simulator facts, and state references keep their accepted role;
- negative tests catch pre-promoted semantic conclusions.

Mechanisms: automated-test; manual-review.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-PUBLIC-001 - Public Boundary Behavior Evidence

Sources: `ADR-008 R2`.

Scope: tests, traces, demos, and reports that claim selected-slice behavior evidence.

Rule: selected-slice behavior evidence drives SUT behavior through the accepted public boundary. Internal unit tests may test internals but do not count as selected-slice behavior evidence.

Forbidden shapes:

- `execute_decision_point("DP-...")` as public harness command;
- `run_transition("EXPECTED_TRANSITION")` as behavior input;
- demos or traces presenting internal-transition calls as behavior compatibility.

Required checks:

- behavior evidence cites public boundary calls;
- internal-transition tests are labeled implementation evidence only.

Mechanisms: automated-test; manual-review.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: claim-blocking.

### ENG-CONF-HARNESS-001 - Harness Non-Arbitration

Sources: `ADR-008 R2`.

Scope: harness and simulator-routing behavior.

Rule: the harness transports the SUT-selected material proposal or behavior disposition. It does not choose among competing SUT outputs based on fixture path, branch policy, oracle expectation, canonical answer, or expected outcome.

Forbidden shapes:

- harness selects the canonical candidate from multiple SUT candidates;
- simulator realizes an output not selected by the SUT;
- harness resolves SUT ambiguity in favor of the fixture answer.

Required checks:

- negative test where SUT emits competing candidates and harness does not rescue the run;
- trace identifies which output was SUT-selected for realization.

Mechanisms: automated-test; manual-review.

Test modes: negative; contract.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-RUN-001 - Independent Run Isolation

Sources: `ADR-004 R3`; `ADR-008 R2`.

Scope: harness run lifecycle, SUT run-scoped state, tests, and replay.

Rule: independent selected-slice runs do not inherit behavior-driving semantic state, transition evidence, relations, outcomes, or active trial state from each other.

Forbidden shapes:

- module globals preserving selected-slice semantic state across independent runs;
- static mutable collections or singleton stores leaking run A into run B;
- provider/session reuse that exposes run A semantic state to run B;
- test fixture reuse that makes longitudinal state appear without SUT-owned retention inside the run.

Required checks:

- negative pressure equivalent to:

```text
run_A creates candidate/active trial/outcome
run_A ends
run_B starts fresh
assert run_A state, relations, outcomes, candidates, and active trials are not resolvable in run_B
assert run_A state does not affect run_B behavior
```

Mechanisms: structural; automated-test; ci-gate.

Test modes: negative; replay.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-STATE-001 - Bounded Selected-Slice State Access

Sources: `ADR-004 R3`; `ADR-006 R2`; `ADR-007 R3`.

Scope: SUT state access in selected-slice behavior.

Rule: selected-slice state access is limited to identity resolution, direct access to already active run-scoped state, and local relation traversal required by accepted selected-slice decisions.

Forbidden shapes:

- open memory search;
- broad relevance ranking;
- distractor filtering;
- active cognitive-frame assembly;
- retrieval over a larger state universe.

Required checks:

- later-use paths resolve opaque SUT-owned handles or local relations, not broad retrieval;
- if broader retrieval is needed to pass, stop and re-triage the relevant open question before milestone claims.

Mechanisms: structural; automated-test; manual-review.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-STATE-002 - Transition-Attributable Semantic Mutation

Sources: `ADR-006 R2`; `ADR-007 R3`; `ADR-008 R2`.

Scope: behavior-driving selected-slice semantic state.

Rule: every mutation to behavior-driving selected-slice semantic state remains attributable to a SUT-owned transition responsibility and preserves contemporaneous evidence of material order, consumed basis refs, produced or affected state refs, and transition result/status assertion.

Forbidden shapes:

- normalizers, serializers, state loaders, inspection, capture, or generic helpers silently promoting candidate state to active state;
- writing transition records after the fact as a substitute for contemporaneous mutation evidence;
- changing semantic status without an attributable SUT transition responsibility.

Required checks:

- tests or review inspect mutation provenance for behavior-driving state changes;
- helper layers that can mutate semantic state are explicitly bounded and reviewed.

Mechanisms: structural; automated-test; manual-review.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-DEP-001 - No Post-Hoc Dependency Repair

Sources: `ADR-007 R3`; `ADR-008 R2`.

Scope: relation capture, inspection, reporting, and oracle-visible evidence.

Rule: dependency-use evidence is contemporaneously preserved or reconstructable from contemporaneously preserved inputs/state. Later-created relations, reports, or snapshots do not by themselves prove earlier SUT consumption.

Forbidden shapes:

- inspection creates missing lineage and presents it as prior SUT evidence;
- capture creates basis-use evidence after the transition;
- reporting backdates dependency use;
- later snapshots substitute for material-order state.

Required checks:

- negative tests or review cases:
  - `missing_lineage_is_not_repaired_by_inspection`;
  - `capture_does_not_create_consumption_evidence`;
  - `reporting_relation_does_not_backdate_dependency_use`;
  - `post_hoc_relation_cannot_prove_prior_basis_consumption`;
  - `later_snapshot_cannot_substitute_for_material_order_state`.

Mechanisms: automated-test; manual-review.

Test modes: negative; replay.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-DEP-002 - Historical Effective Endpoint Identity

Sources: `ADR-007 R3`.

Scope: relations to mutable or lifecycle-bearing selected-slice semantic state.

Rule: relations to mutable or lifecycle-bearing semantic state resolve the state, status, and scope effective at the relation's material order. Later mutation does not rewrite prior dependency meaning.

Forbidden shapes:

- relation endpoints as pointers only to current mutable records;
- narrowing, retirement, supersession, or conflict rewriting prior consumed state;
- prior dependency inspection returning current scope/status rather than material-order scope/status.

Required checks:

- test equivalent to:

```text
O10 consumes T12 while active under scope A
T12 later narrows to scope B
inspect O10 relation
assert O10 consumed T12 as active under scope A
```

Mechanisms: structural; automated-test.

Test modes: regression; replay; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-INSPECT-001 - Passive Inspection Invariance

Sources: `ADR-006 R2`; `ADR-008 R2`.

Scope: SUT inspection surfaces.

Rule: inspection is passive. It does not create, repair, narrow, retire, activate, or mutate behavior-driving state, transition evidence, relation sets, consumer history, basis-use evidence, or lifecycle status.

Forbidden shapes:

- lazy relation materialization during inspection;
- inspection writes missing lineage back into SUT state;
- inspection consumes transition order or lifecycle status;
- inspection performs model/tool calls that alter selected-slice evidence.

Required checks:

- inspection mutation tests compare semantic state, relation set, transition order, and lifecycle status before and after inspection.

Mechanisms: automated-test; manual-review.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-INSPECT-002 - Inspection Interleaving Passivity

Sources: `ADR-006 R2`; `ADR-007 R3`; `ADR-008 R2`.

Scope: SUT inspection and later SUT behavior.

Rule: inserting inspection between behavior-driving operations does not change later oracle-material behavior, except for explicitly segregated behavior-neutral observability artifacts.

Forbidden shapes:

- inspection warms caches that change later selected-slice behavior;
- inspection consumes RNG, order counters, or hidden state used by later transitions;
- deferred semantic computation occurs only because inspection was called;
- relation materialization during inspection changes later behavior.

Required checks:

- interleaving test equivalent to:

```text
process(A)
process(B)
```

is oracle-materially equivalent to:

```text
process(A)
inspect(...)
inspect(...)
process(B)
```

Mechanisms: automated-test.

Test modes: interleaving; replay; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-SIM-001 - Simulator Isolation And Projection

Sources: `ADR-002 R2`; `ADR-005 R2`; `ADR-008 R2`.

Scope: simulator realization and simulator outputs returning to SUT.

Rule: simulator realizes SUT-selected proposal intents or behavior dispositions into synthetic facts. It does not choose correction policy, repair SUT decisions, decide semantic correctness, own branch gates, leak canonical matches to SUT, or become a direct SUT dependency.

Forbidden shapes:

- SUT imports simulator code;
- simulator selects canonical behavior;
- simulator output to SUT includes canonical-match, branch, oracle, or scoring fields;
- simulator repairs wrong SUT choices.

Required checks:

- simulator output returning to SUT passes the same closed-ingress projection as fixture inputs;
- negative tests submit full simulator evaluation records to SUT ingress.

Mechanisms: static; structural; automated-test.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-CAPTURE-001 - Capture And Reporting Do Not Drive Or Repair Behavior

Sources: `ADR-006 R2`; `ADR-007 R3`; `ADR-008 R2`.

Scope: capture, reporting, logs, snapshots, debug traces, replay, and restore paths.

Rule: capture and reporting collect evidence and failure artifacts; they do not become behavior-driving input to later SUT transitions and do not create missing SUT evidence after the fact.

Forbidden shapes:

- reports or capture artifacts re-ingested as SUT-visible semantic state;
- evaluation-only metadata in logs or snapshots influencing later SUT behavior;
- replay/restore promoting evaluation capture into SUT state without accepted decision;
- capture/reporting creating relation evidence presented as contemporaneous SUT state.

Required checks:

- replay/restore paths preserve the same visibility and state-origin rules as SUT input;
- tests or review prove evaluation-only metadata is not reintroduced into SUT behavior.

Mechanisms: structural; automated-test; manual-review.

Test modes: contract; negative; replay.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-REF-001 - SUT-Safe References And Handles

Sources: `ADR-005 R2`; `ADR-007 R3`; `ADR-008 R2`.

Scope: SUT-visible references, handles, IDs, and serialized state references.

Rule: SUT-visible references do not encode evaluation context. Evaluation-side fixture IDs may exist inside evaluation records, but SUT-visible handles are opaque or otherwise non-evaluation-bearing.

Forbidden shapes:

- path-qualified fixture IDs used as SUT-visible handles;
- branch, bundle, checkpoint, claim-class, scoring, canonical-pressure, or expected-transition context encoded in handles;
- semantic aliases that carry the same answer-bearing meaning under different field names.

Required checks:

- negative tests reject literal path-qualified fixture IDs where they reveal evaluation context;
- review checks semantic leakage, not only reserved word matches.

Mechanisms: structural; automated-test; manual-review.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking.

### ENG-CONF-CLAIM-001 - Selected-Slice Claim Boundary

Sources: `OPEN_QUESTIONS.md` `V0.2.17`; `ADR-004 R3`; `ADR-005 R2`; `ENGINEERING_STANDARD.md` `V0.3.0` `ENG-CLAIM-001`.

Scope: SCN-001 reports, tests, traces, demos, README text, and implementation docs.

Rule: selected-slice engineering conformance does not imply evaluated behavioral compatibility, formal campaign evidence, final scoreability, full SCN-001 pass, production memory, retrieval, real trust-boundary safety, or milestone acceptance.

Forbidden shapes:

- calling a development trace formal campaign evidence;
- using `score`, `pass`, `accepted_slice`, or equivalent labels to imply final acceptance before governing questions resolve;
- claiming full SCN-001 or production readiness from selected-slice conformance tests.

Required checks:

- docs and reports use bounded language;
- first compatibility/evaluation-record claims trigger `EVAL-004`;
- final scoreability claims trigger `EVAL-005`;
- first selected-slice completion/acceptance claims trigger `SLICE-005`.

Mechanisms: manual-review; static/docs checks where practical.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: claim-blocking.

## Minimum Local Conformance Gates

A governed selected-slice implementation should define local gates for:

- dependency direction and public-surface access;
- closed SUT ingress and rejected-ingress atomicity;
- adapter role/state-origin preservation;
- harness non-arbitration;
- independent run isolation;
- bounded state access;
- transition-attributable mutation;
- no post-hoc dependency repair;
- historical effective endpoint identity;
- passive and interleaving-safe inspection;
- simulator isolation;
- capture/reporting non-repair and non-reingestion;
- SUT-safe references;
- selected-slice claim boundaries.

These gates may start as review-only where necessary, but rules protecting payload leakage, dependency direction, run isolation, semantic mutation attribution, and inspection passivity should become structural, static, automated-test, or CI gates before supporting selected-slice claims.

## Red-Team Prompts

Use these as attack prompts when reviewing implementation:

- Can SUT code import or reflect into evaluation code?
- Can evaluation call private SUT internals and still claim behavior evidence?
- Can a full fixture/oracle object reach SUT input?
- Can rejected input leave semantic residue?
- Can a normalizer or loader silently change behavior-driving state?
- Can run B observe semantic state from run A?
- Can inspection alter later SUT behavior?
- Can capture or reporting repair missing dependency evidence?
- Can a mutable endpoint rewrite prior dependency meaning?
- Can fixture path, branch, claim class, score, expected transition, or canonical pressure leak through references?
- Can the harness choose the output the simulator realizes?
- Can logs, snapshots, or replay artifacts reintroduce evaluation metadata into SUT behavior?
- Can a development artifact be described as formal evaluation evidence?
