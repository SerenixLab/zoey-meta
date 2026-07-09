# ADR-007: SCN-001 Selected-Slice Dependency Identity Contract

Status: `Draft`

Date: 2026-07-09

Record revision: `Draft`

Decision authority: project owner

Resolved question IDs on acceptance: `DEP-001`

Decision-Time Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.15`
- `decisions/ADR-001-first-vertical-slice.md` `R1`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`
- `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md` `R2`
- `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md` `R3`
- `decisions/ADR-005-scn001-selected-slice-fixture-oracle-contract.md` `R2`
- `decisions/ADR-006-scn001-selected-slice-state-contract.md` `R2`

Post-decision register state on acceptance: `OPEN_QUESTIONS.md` should record `DEP-001` as resolved by this ADR for the first `SCN-001` selected-slice milestone, re-triage `SLICE-003` as the recommended next frontier, and re-triage `DEP-003`, `SLICE-005`, `EVAL-004`, and `EVAL-005` without automatically resolving or expanding them.

## Decision

Adopt a minimum dependency identity and relation contract for the first `SCN-001` selected slice.

The selected slice requires stable references and typed local relations sufficient to preserve the state/evidence relationships accepted by `ADR-006`. It does not require a general dependency graph, graph query engine, workflow engine, production memory schema, retrieval/context-assembly system, or final internal module boundary.

The minimum contract is:

1. every oracle-material selected-slice fact, SUT-owned transition evidence record, retained state anchor, lineage-preserving projection, and oracle-visible evaluation record must have an inspectable stable reference within its declared scope;
2. references must carry enough origin, scope, lifecycle, visibility, and ordering metadata to distinguish fixture facts, SUT-owned semantic state, SUT-owned transition evidence, projections, derived inspection facts, and oracle-only records;
3. required relationships must be represented as typed relation semantics: `source`, `basis`, `support`, `binding`, `transition_ancestry`, `applicability`, `realization`, `outcome`, `explanation_support`, `supersession`, `retirement`, `narrowing`, and `conflict`;
4. the relation set may be represented as fields, event records, append-only transition records, tables, documents, object links, logs, or another inspectable representation, provided the oracle can enumerate the required local relations for each inspected record;
5. oracle-only rule IDs, claim-class outcomes, branch policy, scoring labels, answer keys, and hidden expected answers must not be embedded in SUT-owned semantic state.

For this ADR, "dependency identity" means minimum referenceability and relation semantics for selected-slice evidence. It does not mean dependency injection, package management, runtime component wiring, build dependencies, graph database design, task orchestration, or production memory architecture.

## Reference Scope

References need only be stable within the scope where they are inspected.

| Scope | Minimum stability requirement | Not required |
| --- | --- | --- |
| Fixture/oracle package scope | Fixture item IDs, oracle rule IDs, path IDs, bundle IDs, and claim-class IDs remain stable within `SCN001-SSFO-V0.2.0` or its accepted superseding package. | Global permanence across unrelated scenarios or future packages. |
| Formal run scope | SUT state anchors, transition evidence, projections, simulator realization facts, and oracle capture records remain stable for the run and any declared lineage-preserving branch checkpoint. | Production durable identity, cross-campaign identity, or real user identity. |
| Transition scope | A transition record has stable references to its basis, result, created order, and produced/updated state anchors. | Workflow-step identity, retry orchestration, locks, queues, or scheduler state. |
| Reporting scope | Failure artifacts and bounded milestone claims can reference observed state/evidence, rule IDs, and claim classes. | General analytics schema or reusable reporting platform. |

Run-local identifiers are acceptable. They must not be silently reused in a way that causes two distinct semantic records in the same run to appear identical.

## Common Reference Envelope

The following fields are the minimum reference envelope for any oracle-material record. Names are illustrative; equivalent representations are allowed.

| Field | Required meaning | Notes |
| --- | --- | --- |
| `ref_id` | Stable identifier within the declared reference scope. | May be opaque. Need not be globally unique outside scope. |
| `ref_kind` | Semantic family of the referenced item. | Examples: `fixture_fact`, `transition_evidence`, `state_anchor`, `projection`, `simulator_fact`, `oracle_record`. |
| `ref_scope` | Scope in which the reference is stable. | Examples: package, run, path, bundle, checkpoint, report. |
| `origin_role` | Who originated the semantic content. | Values must distinguish at least fixture, SUT, simulator, harness, and oracle. |
| `visibility_class` | Whether the content was SUT-visible, SUT-owned, projection-only, derived-inspection, or oracle-only. | This prevents hidden oracle-answer metadata from entering SUT state. |
| `lifecycle_class` | Current `ADR-006` classification where applicable. | At minimum: cross-transition SUT state, SUT transition evidence, lineage-preserving projection, derived inspection fact, fixture/oracle-only. |
| `created_order_ref` | Inspectable order marker for when the record or relation was created or observed. | May use scenario time, run sequence number, event order, transition order, or equivalent governed ordering from `ADR-003` and `ADR-005`. |
| `status_origin` | Whether a status or conclusion was fixture-declared, SUT-derived, simulator-produced, or oracle-derived. | Required where stale/current, active/inactive, applicable/inapplicable, bound/unbound, pass/fail, or similar status could be confused. |
| `scope_subject_ref` | Actor, synthetic user, scenario path, task scope, trial scope, or run scope to which the record applies. | May be inherited from an enclosing run or bundle if unambiguous. |
| `material_value_ref` | Pointer, excerpt, structured value, or fingerprint sufficient to identify the material payload inspected. | Full raw content is not required when the accepted fixture/oracle contract permits a structured value or stable handle. |

Records may inherit common metadata from an enclosing run, package, bundle, or retention-basis record if the inheritance relation is inspectable. The contract does not require duplicating all fields on every row, object, or event.

## Minimum Record Contracts

| Record family | Minimum identity/reference metadata | Required relation families |
| --- | --- | --- |
| Selected-slice facts | Common envelope; fixture item or SUT fact reference; source actor or source system where applicable; occurrence/order time; role label; fixture/package or SUT-origin marker; material payload handle. | `source`, plus `basis` when used by a SUT transition. |
| SUT transition evidence | Common envelope; transition kind; producing SUT responsibility; input basis refs; result/status; created order; affected state refs; uncertainty or limitation marker where relevant. | `basis`, `support`, `binding`, `transition_ancestry`, `applicability`, `outcome`, or `explanation_support` as applicable to the transition. |
| State anchors | Common envelope; state kind; retained state identity; lifecycle status; run/retention-basis scope; created-by transition ref; current effective version or status; correction path where required. | `source` or `transition_ancestry`; lifecycle relations including `supersession`, `retirement`, `narrowing`, and `conflict` where applicable. |
| Lineage-preserving projections | Common envelope; projection target refs; projection rule or view identity; generated order; proof that the projection adds no fixture-authored semantic conclusion. | Projection-to-target relation plus all underlying relations needed to reconstruct lineage. |
| Oracle-visible records | Common envelope; observed SUT/fixture/simulator refs; oracle rule or claim-class refs where applicable; capture order; outcome or failure classification; SUT visibility set to oracle-only unless explicitly delivered as a SUT-visible fixture/control fact. | `explanation_support`, `outcome`, or failure/support refs used for reporting. Must not become SUT-owned semantic state. |

## Required Relation Tuple

Each required relation must be inspectable with at least:

- `relation_kind`;
- `from_ref`;
- `to_ref`;
- `created_order_ref`;
- `asserted_by_role`;
- `relation_scope` or use target when the relation is not globally applicable;
- `status` when the relation can be active, inactive, disputed, superseded, retired, narrowed, or conflicting.

Equivalent embedded fields are valid if the oracle can recover the same tuple. No graph-wide reachability, transitive closure, global topological sort, or generic graph API is required.

## Required Relation Semantics

| Relation kind | Minimum semantics | Selected-slice examples | Must not mean |
| --- | --- | --- | --- |
| `source` | Connects a fact, assertion, observation, control event, simulator fact, or projection to the actor/system/package that originated its semantic content. | Current utterance attributed to synthetic user; fixture observation from package; simulator realization fact from simulated dependency. | The source is authoritative for SUT-owned conclusions merely because it exists. |
| `basis` | Identifies material input facts or prior transition evidence consumed by a SUT transition for a declared use target. | Temporal eligibility basis over old `H-002`; comparison basis over recognition and production observations; activation-check basis. | A vague retrospective explanation or all available context. |
| `support` | Indicates evidence that supports a candidate, interpretation, disposition, outcome classification, or explanation without becoming that supported object. | Dimension comparison supports production-focused candidate; direct correction supports delayed-correction candidate. | Proof of causal truth, durable preference, or automatic activation. |
| `binding` | Connects a surfaced proposal, its candidate-specific intent, and the user response/acceptance assessment. | User response binds to `P-001R` proposal before production-focused activation. | User response binds directly to an invisible candidate or hidden intended policy. |
| `transition_ancestry` | Preserves lineage between state created by a transition and the predecessor candidate, assessment, correction, or prior state it descends from. | Active trial descends from candidate plus activation evidence; delayed-correction candidate descends from direct correction disposition. | A generic history note or reconstruction after state loss. |
| `applicability` | Records a SUT-owned assessment that retained state applies, does not apply, narrows, or conflicts in a later context. | Later-use review applies delayed-correction trial; `CF-DRILL-OPT-IN` marks it inapplicable, narrowed, or superseded. | Fixture-provided relevance ranking or hidden oracle applicability answer. |
| `realization` | Connects a SUT proposal or behavior disposition to simulator realization facts and fidelity/mismatch origin. | SUT direct-correction disposition realized by simulated response; proposal wording fidelity checked against SUT intent. | Simulator output as sole evidence that the prior SUT disposition existed. |
| `outcome` | Connects observed outcome facts to active trial, behavior disposition, realization, material context, and uncertainty. | Intervention-conditioned outcome references active trial, disposition, realization, co-intervention status, and outcome fact. | Causal proof, long-term efficacy, global preference, or durable learning. |
| `explanation_support` | Connects user-facing explanation claims to retained state/evidence, transition basis, uncertainty, and excluded claim boundaries. | `DP-EXPLAIN` cites active trial, applicability, outcome, and limitation refs. | Hidden chain-of-thought, fabricated support, or oracle-only answer keys. |
| `supersession` | Marks one state, interpretation, candidate, trial, or control meaning as replaced by a later one while preserving history. | Later scoped correction supersedes a prior candidate or trial scope. | Deleting or rewriting the old record. |
| `retirement` | Marks a state, candidate, trial, or disposition as no longer active/effective, with basis and order preserved. | Candidate withheld or retired after conflict/insufficiency; active trial retired after correction. | Erasure, expiration machinery, or production forgetting. |
| `narrowing` | Marks a state/trial/control meaning as still related but with reduced scope. | Delayed-correction trial narrowed away from focused drill after explicit drill opt-in. | A new unrelated rule or broad preference. |
| `conflict` | Records that two facts, states, controls, candidates, or applicability assessments cannot both be accepted for the same use target without resolution. | Immediate-correction drill opt-in conflicts with broad delayed-correction use in that drill context. | Automatic failure, automatic winner selection, or general contradiction engine. |

## Lifecycle Classification Inspectability

`ADR-006` lifecycle-relative classifications must remain inspectable through this metadata contract.

At each material inspection point, the oracle must be able to determine:

- whether a record is SUT-owned state, SUT transition evidence, a lineage-preserving projection, a derived inspection fact, or fixture/oracle-only;
- whether the status was fixture-declared, SUT-derived, simulator-produced, or oracle-derived;
- which later SUT consumer, if any, required the record to remain cross-transition state;
- when a record stopped being behavior-driving state and remained only transition evidence, if that reclassification occurs;
- which relations preserve source, basis, support, ancestry, applicability, realization, outcome, and explanation lineage after reclassification.

This may be explicit metadata, a transition log, version history, or an oracle-reconstructable relation set. The implementation does not need a universal lifecycle engine, TTL scheduler, dependency invalidation service, or background maintainer.

## Oracle Visibility Guardrail

Oracle-visible does not mean SUT-visible.

The SUT may hold:

- SUT-visible fixture facts with fixture provenance;
- SUT-owned selected-slice state and transition evidence;
- lineage-preserving projections over SUT-owned state or delivered fixture facts when the projection adds no prohibited conclusion.

The SUT must not hold as behavior-driving semantic state:

- oracle rule IDs as answer guidance;
- claim-class pass/fail labels;
- branch policy, canonical path labels, or expected outcomes;
- evaluator-only comments or hidden ground truth;
- hidden stale/current, best-trial, applicability, causal, preference, or full-scenario verdicts.

Oracle records may reference SUT state and transition evidence after capture, but those references do not make oracle conclusions part of SUT state.

## Minimum Closure Rules

The selected slice requires local relation closure only.

For each inspected candidate, proposal, active trial, applicability assessment, behavior disposition, outcome record, projection, or explanation-support record, the oracle must be able to enumerate the directly required source, basis, support, binding, ancestry, applicability, realization, outcome, lifecycle, and explanation-support relations named by this ADR and `ADR-006`.

The implementation is not required to:

- answer arbitrary dependency queries;
- compute all upstream or downstream descendants;
- maintain graph indexes;
- perform automatic invalidation propagation;
- detect all cycles;
- resolve conflicts generally;
- model grouped component operations;
- expose final internal modules.

If a later claim needs non-circular support or non-convergence detection beyond these local selected-slice relations, that belongs to `DEP-002`, not this ADR.

## Explicit Non-Scope

This dependency identity contract does not require or decide:

- a general dependency graph, graph database, graph traversal API, or universal edge schema;
- a workflow engine, orchestration lifecycle, task engine, retry policy, or queue;
- production memory schema, durable personal-memory custody, summary store, embedding store, adapter, or training artifact;
- retrieval, memory search, relevance ranking, distractor filtering, or context assembly;
- final database schema, storage engine, serialization format, repository split, service boundary, or internal module boundary;
- model, prompt, agent, provider, runtime, tool, or inference-destination identity beyond optional provenance refs when already captured elsewhere;
- behavior-configuration metadata required by `EVAL-004`;
- acceptance scoring or scenario-scoreability criteria required by `SLICE-005` and `EVAL-005`;
- background maintenance triggers, expiry, revocation propagation, capability degradation handling, external refresh, or manual review queues required by `DEP-003`;
- real personal continuity, durable developmental adaptation, real voice/avatar behavior, Japanese pedagogy quality, statistical reliability, production readiness, or full `SCN-001` pass.

## Downstream Effects

| Downstream question | Effect of this ADR on acceptance | What remains undecided |
| --- | --- | --- |
| `SLICE-003` | Unblocks the internal-boundary question by defining the minimum reference families and relation semantics that any selected-slice boundary must preserve. The boundary may now be drawn around producers, consumers, and inspectors of these records. | Final module split, repository layout, service topology, model/runtime boundary, and production architecture. |
| `DEP-003` | Provides the dependency relation kinds that future maintenance triggers would inspect. It does not itself introduce expiry, revocation propagation, capability degradation, external refresh, or manual review. | Whether any runtime maintenance trigger is required for this milestone or a later one. |
| `SLICE-005` | Gives the acceptance gate a concrete evidence-adequacy precondition: required claim classes may depend on records only if their references and local relations satisfy this contract. | Which claim classes are jointly required, campaign aggregation for final milestone completion, and bounded pass language beyond prior ADRs. |
| `EVAL-004` | Identifies which evidence records need stable references to behavior/evaluation configuration IDs where those already exist in campaign metadata. | The full behavior-configuration metadata contract, compatibility claims, comparison metadata, and model/runtime/prompt configuration rules. |
| `EVAL-005` | Clarifies which unresolved dependency questions can be carried as bounded assumptions for this slice: no graph engine, no runtime maintenance, no retrieval, no production memory. | Final scoreability, unresolved-question impact on pass criteria, and which assumptions weaken or prevent specific claims. |

## Boundary Red-Team

| Overbuild pressure | Guardrail |
| --- | --- |
| The relation list could become a full dependency graph. | Relations are local typed semantics recoverable per inspected record. No graph engine, global traversal, generic edge schema, or transitive closure is required. |
| The reference envelope could become the final schema. | Field names are illustrative and may be inherited, embedded, logged, or projected. The contract defines inspectable semantics only. |
| Lifecycle relations could become a workflow engine. | `supersession`, `retirement`, `narrowing`, and `conflict` are semantic history relations, not tasks, queues, retries, approvals, or background jobs. |
| Basis/support relations could become retrieval or context assembly. | The harness still curates context under `ADR-004`; this ADR only records which delivered facts or retained state the SUT used. |
| State anchors could become production memory architecture. | Identity is run-scoped and fixture-bound unless a later ADR deliberately expands it. Durable personal memory and real continuity remain out of scope. |
| Oracle records could leak answer metadata into the SUT. | `visibility_class`, `origin_role`, and `status_origin` must distinguish SUT-visible facts from oracle-only rules, labels, scores, and expected answers. |
| Model/runtime provenance could become semantic authority. | Producing-mechanism refs are optional provenance unless separately required; they do not make a candidate active, true, applicable, or supported. |

## Register Effect

Upon acceptance, update `OPEN_QUESTIONS.md` as follows:

- move `DEP-001` to `Resolved` with outcome `Decision`, resolved by this ADR for the first `SCN-001` selected-slice milestone;
- record that the selected slice uses stable scoped references and local typed relation semantics for source, basis, support, binding, transition ancestry, applicability, realization, outcome, explanation support, supersession, retirement, narrowing, and conflict;
- record that this does not decide a full dependency graph, workflow engine, production memory schema, retrieval/context-assembly system, behavior-configuration metadata, acceptance gate, runtime maintenance triggers, or final internal module boundary;
- re-triage `SLICE-003` as the recommended next active frontier because selected state and dependency identity are now known;
- re-triage `DEP-003`; this ADR supplies relation types but introduces no expiry, revocation, capability degradation, external refresh, or manual-review trigger;
- re-triage `SLICE-005`; this ADR supplies evidence-reference adequacy constraints but does not decide final acceptance;
- keep `EVAL-004` deferred unless a later artifact prepares a first evaluation record, comparison, or evaluated compatibility claim requiring behavior-configuration metadata;
- keep `EVAL-005` deferred unless a later artifact prepares final scoring or scenario-scoreability criteria.

No other question automatically activates merely because this ADR is accepted.

## Reconsideration Triggers

Reconsider or supersede this ADR if:

- the oracle cannot verify `ADR-006` state/evidence relationships from local typed references without a broader graph mechanism;
- implementation cannot preserve stable run-scoped identities for candidates, proposals, active trials, applicability assessments, dispositions, outcomes, projections, or explanation support;
- lifecycle-relative classification cannot be inspected without relying on retrospective self-report;
- fixture/oracle-only answer metadata is found inside behavior-driving SUT state;
- `SLICE-003` cannot draw a minimum internal boundary while preserving this contract;
- `SLICE-005`, `EVAL-004`, or `EVAL-005` requires broader metadata to make bounded first-milestone evidence or claims scoreable;
- `DEP-003` becomes active because expiry, revocation propagation, capability degradation, external refresh, or manual review enters the milestone;
- a later milestone claims retrieval, production memory, durable adaptation, real personal continuity, statistical reliability, or full `SCN-001` evidence from relations broader than this selected-slice contract.

## Non-Decisions

This ADR does not decide:

- the final internal boundary for `SLICE-003`;
- runtime maintenance triggers for `DEP-003`;
- acceptance gate or final done criteria for `SLICE-005`;
- behavior-configuration metadata for `EVAL-004`;
- scoreability criteria for `EVAL-005`;
- non-circular support or convergence detection for `DEP-002`;
- concrete storage schemas, class names, database tables, event buses, API payloads, or product inspection UI.
