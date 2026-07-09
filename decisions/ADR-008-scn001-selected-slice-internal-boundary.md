# ADR-008: SCN-001 Selected-Slice Internal Boundary

Status: `Draft`

Date: 2026-07-09

Record revision: `R0`

Decision authority: project owner

Related open question: `SLICE-003`

Decision-Time Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.16`
- `decisions/ADR-001-first-vertical-slice.md` `R1`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`
- `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md` `R2`
- `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md` `R3`
- `decisions/ADR-005-scn001-selected-slice-fixture-oracle-contract.md` `R2`
- `decisions/ADR-006-scn001-selected-slice-state-contract.md` `R2`
- `decisions/ADR-007-scn001-selected-slice-dependency-identity.md` `R3`

## Decision

For the first `SCN-001` selected slice, adopt a two-project minimum internal boundary:

1. a selected-slice SUT core project that owns all behavior-driving semantic transitions, run-scoped effective state, transition evidence, lineage-preserving inspection projections, and public SUT boundary contracts;
2. a selected-slice evaluation project that owns the harness, fixture/oracle package, simulator, capture, oracle scoring, and reporting.

The required dependency direction is one-way:

```text
evaluation project -> SUT core public boundary
SUT core -> no dependency on harness, fixture, oracle, simulator, capture, or reporting
```

The SUT core may receive only declared SUT-visible fixture facts, SUT-visible fixture control facts, simulator realization facts, and lineage-preserving references or projections that expose state already owned by the SUT. It must not receive oracle-only metadata, hidden ground truth, answer keys, claim-class labels, branch policy, scoring rules as guidance, canonical path expectations, or acceptance results.

This is the smallest boundary forced by accepted selected-slice behavior. A single repository or workspace is acceptable. A single deployable process is acceptable. In-memory storage is acceptable. The decision does not require services, a database, a graph engine, production adapters, a product UI, final runtime topology, or final Zoey architecture.

Acceptance of this ADR would resolve `SLICE-003` for the first `SCN-001` selected-slice milestone only.

## Why This Boundary Is Forced

`ADR-002` keeps the central transition chain inside the SUT: stale-history handling, attribution, dimension comparison, trial formation, proposal binding, activation checks, direct correction, later-use applicability, outcome update, and explanation support.

`ADR-004` keeps context curated by the harness while requiring the SUT to perform semantic use of that context. The SUT therefore needs a public input boundary for curated facts and a public output boundary for effective state inspection.

`ADR-005` separates fixture inputs from oracle expectations. The implementation boundary must prevent oracle-only metadata from entering behavior-driving SUT state.

`ADR-006` requires run-scoped cross-transition SUT state and SUT transition evidence, but explicitly avoids a final storage schema. The boundary therefore must surround semantic state ownership, not a database.

`ADR-007` requires stable scoped references, effective endpoint identity, contemporaneous dependency-use evidence, and local relation semantics. The boundary therefore must preserve referenceability and relation inspection, but does not require a graph service.

The minimum that satisfies all five pressures is a SUT core with a narrow public boundary, driven by a separate evaluation project that can hold answer-bearing fixture/oracle machinery.

## Responsibility Map

| Responsibility area | Owner | Required responsibility | Must not own |
| --- | --- | --- | --- |
| SUT core | SUT core project | Ingest SUT-visible facts, classify attribution where assigned to the SUT, retain run-scoped semantic state, perform selected-slice transitions, produce behavior dispositions, record transition evidence and local relations, expose lineage-preserving inspection projections, and produce explanation support. | Fixture path selection, oracle scoring, branch policy, hidden ground truth, claim-class results, run acceptance, product UI, production memory, retrieval, or simulator fidelity decisions. |
| Harness | Evaluation project | Drive decision-point sequence, deliver curated bundles, enforce fixture delivery order, call SUT boundary operations, route SUT intents to simulator, collect exposed projections, and keep SUT run isolation. | SUT semantic conclusions, reconstruction of lost SUT state, activation checks, later-use applicability, or explanation support. |
| Fixture/oracle | Evaluation project, with internal fixture/oracle separation | Define fixture package `SCN001-SSFO-V0.2.0`, SUT-visible payloads, SUT-visible control facts, oracle-only expectations, rule IDs, claim classes, path pressure, and validity/scoring predicates. | Behavior-driving SUT state, SUT-derived temporal/staleness judgments, trial selection, applicability verdicts, or causal conclusions. |
| Simulator | Evaluation project | Realize SUT proposal intents and behavior dispositions into synthetic interaction facts, emit realization facts, fidelity/mismatch facts, and simulated outcome delivery gates. | Choosing the policy being tested, correcting SUT intent, supplying trial applicability, or proving semantic correctness. |
| Capture/reporting | Evaluation project | Snapshot SUT projections, simulator facts, fixture facts, oracle results, invalidity reasons, failure artifacts, and bounded claim evidence with stable references. | SUT behavior-driving memory, post-hoc basis reconstruction as proof of SUT consumption, or acceptance gate decisions not yet accepted under `SLICE-005`. |

## What Crosses Each Boundary

### Harness To SUT Core

Allowed crossings:

- SUT-visible fixture facts with fixture provenance, roles, source, chronology, context labels, task-mode labels, task observations, affordance facts, and selected fixture control facts.
- SUT-visible communication events and user responses.
- Simulator realization facts after the SUT has emitted a proposal intent or behavior disposition.
- Lineage-preserving references or projections to SUT-owned state when the SUT needs to consume its own retained state through a harness-mediated decision point.

Prohibited crossings:

- oracle-only metadata;
- hidden scenario ground truth;
- answer-bearing fixture annotations;
- claim-class IDs or pass/fail labels as behavior guidance;
- branch policy that reveals which proposal or behavior receives canonical continuation;
- precomputed stale/current, best-trial, active-trial, applicability, causal, preference, or learning-style conclusions.

### SUT Core To Harness

Allowed crossings:

- proposal intents and behavior dispositions;
- retained state anchors and transition evidence exposed through inspection projections;
- stable scoped references, effective endpoint identities, lifecycle/status/scope evidence, and local relation tuples required by `ADR-007`;
- explanation support records with state references, uncertainty, scope limits, causal limits, and unsupported generalization limits;
- non-activation dispositions where the SUT withholds, defers, requests more evidence, asks clarification, retires, narrows, or marks inapplicability.

These outputs are evidence from effective SUT state. They are not final product telemetry, production audit records, or a final state schema.

### SUT Core To Simulator

The simulator may receive only SUT-owned material intent or disposition records needed for realization:

- candidate-bound proposal intent;
- drill correction disposition;
- direct current-session correction disposition;
- later-use behavior disposition.

The simulator must not receive oracle expectations or be allowed to select the correction policy. Simulator realization output may later cross back to the SUT as a simulator fact with provenance.

### Fixture/Oracle To Harness

The fixture/oracle package may give the harness:

- fixture manifests and bundle membership;
- SUT-visible payload projections;
- branch gates and delivery policy;
- oracle-only predicates, rule IDs, claim classes, expected pressure, validity criteria, and scoring logic.

The harness must preserve access separation when delivering inputs to the SUT. Holding both fixture and oracle material in the evaluation project is allowed only if the SUT boundary receives the SUT-visible projection, not the answer-bearing package.

### Capture/Reporting From SUT, Fixture, Simulator, And Oracle

Capture/reporting may collect:

- SUT projections and transition evidence;
- fixture fact references and delivered bundle evidence;
- simulator realization facts;
- oracle-derived inspection facts;
- run-validity classifications, hard failures, obligation failures, and bounded claim evidence.

Capture/reporting may not become an alternate state source for later SUT transitions. A post-hoc report relation can support oracle inspection, but it cannot prove contemporaneous SUT dependency use unless the SUT transition record or effective state already preserved that use.

## Minimal Project And Module Shape

The recommended minimum shape is:

```text
selected-slice-workspace/
  scn001_sut_core/
    boundary/
    state/
    transitions/
    relations/
    inspection/
  scn001_eval/
    harness/
    fixture/
    oracle/
    simulator/
    capture/
    reporting/
```

`scn001_sut_core/boundary` exports the callable SUT boundary and SUT-visible input/output contracts. The evaluation project may depend on these exports.

`scn001_sut_core/state`, `transitions`, `relations`, and `inspection` may be separate modules, namespaces, files, or internal packages. The split is responsibility guidance, not a final module API.

`scn001_eval/fixture` must distinguish SUT-visible fixture payload from oracle-only annotations. This may be represented as separate files, modules, views, serializers, or typed accessors.

`scn001_eval/oracle` may depend on fixture, simulator output, capture, and SUT inspection projections. The SUT core must not depend on oracle.

No third shared package is required for R0. If implementation friction makes shared types necessary, a later narrow `scn001_boundary_contracts` package is allowed only if it contains no oracle-only fields, no answer-bearing fixture metadata, no branch policy, no claim-class guidance, and no scoring results.

## Required Interfaces Before First Implementation

The first implementation should define these interfaces or equivalent contracts before behavior work begins:

| Interface | Owner | Minimum purpose |
| --- | --- | --- |
| SUT run lifecycle | SUT core | Start an isolated synthetic run with SUT-visible run controls and evaluation-only retention basis. |
| Fixture fact ingestion | SUT core public boundary | Accept declared SUT-visible fixture facts while preserving fixture provenance and distinguishing delivered, ingested, retained, and used facts. |
| Decision-point execution | SUT core public boundary | Execute named selected-slice transition responsibilities without receiving oracle-only path expectations as behavior input. |
| Proposal and disposition output | SUT core public boundary | Emit proposal intents and behavior dispositions before simulator realization and outcome delivery. |
| Simulator realization input/output | Evaluation project | Accept SUT proposal/disposition refs and emit realization facts with fidelity/mismatch metadata. |
| Inspection projection | SUT core public boundary | Expose lineage-preserving projections over retained SUT state and transition evidence, including scoped references, effective endpoint identity, ordering, status, scope, and local relations. |
| Oracle input capture | Evaluation project | Capture fixture deliveries, SUT projections, simulator facts, and oracle-derived inspection facts without modifying SUT state. |
| Fixture visibility projection | Evaluation project | Produce SUT-visible bundle payloads from the fixture/oracle package while excluding oracle-only fields. |
| Oracle scoring contract | Evaluation project | Evaluate captured effective state against accepted hard-invariant and positive-obligation predicates. |
| Report artifact contract | Evaluation project | Produce bounded evidence reports and failure artifacts that cite stable refs without becoming SUT input. |

These contracts may be plain in-memory interfaces, function signatures, files, structs, records, or test harness adapters. They need not be network APIs.

## Boundary Invariants

The internal boundary is accepted only if all of the following remain true:

- The SUT core owns semantic transitions required by `ADR-002`; the harness cannot satisfy them by fixture labels or reconstruction.
- The harness supplies curated context under `ADR-004`; the SUT core does not claim retrieval, memory search, relevance ranking, or context assembly.
- Fixture/oracle metadata remains separated under `ADR-005`; answer-bearing material cannot enter SUT behavior-driving state.
- The SUT core preserves `ADR-006` state classifications and retention horizons; oracle-visible fields are not copied wholesale into SUT state.
- The SUT core preserves `ADR-007` stable scoped references, effective endpoint identity, contemporaneous dependency-use evidence, and local typed relation semantics.
- Simulator outputs are facts about realization, not evidence that the SUT selected a semantically correct policy.
- Capture/reporting can cite and score state, but cannot create the missing basis that the SUT failed to retain.

## Explicit Non-Decisions

This ADR does not decide:

- final services or service topology;
- storage engine, database, event store, graph store, schema, serialization format, or migration strategy;
- product UI, inspection UI, dashboard, voice UI, avatar UI, or user-facing memory controls;
- runtime adapters, model routing, provider sessions, prompt architecture, inference gateway, tool runtime, or production trust-boundary adapters;
- production memory, real personal-history custody, durable Zoey continuity, retention policy, summaries, embeddings, learned profiles, adapters, or training artifacts;
- retrieval, memory search, relevance ranking, active cognitive-frame assembly, distractors, or context discovery;
- maintenance triggers, expiry, revocation propagation, capability degradation, external refresh, manual review, background invalidation, or active-trial TTL;
- final acceptance gate for `SLICE-005`;
- first evaluation-record metadata, behavior-configuration comparison, or compatibility metadata for `EVAL-004`;
- scenario scoreability criteria for `EVAL-005`;
- production Japanese pedagogy, real proficiency assessment, real voice behavior, real calendar behavior, external operations, actor assurance, authorization, or provider reconciliation.

## Red-Team Assessment

| Risk | Boundary response |
| --- | --- |
| Overbuild into production architecture | The boundary is project/responsibility only: SUT core plus evaluation project. It permits one process, in-memory state, no database, no services, no product UI, no runtime adapter architecture, and no final module split. |
| Answer leakage from fixture/oracle | The evaluation project may hold oracle material, but only SUT-visible fixture projections cross into the SUT. Oracle-only path labels, expected outcomes, branch policy, claim classes, and answer metadata remain outside SUT cognitive input. |
| Retrospective dependency reconstruction | Capture/reporting may add oracle-derived inspection relations, but those cannot prove SUT consumption unless contemporaneous SUT transition records or effective state already preserved the dependency use and order required by `ADR-007`. |
| Premature production memory | SUT state is run-scoped, synthetic, and evaluation-retained only. Cross-transition persistence means surviving the evaluated trajectory, not becoming real Zoey memory. |
| Simulator policy substitution | Simulator receives SUT intent/disposition and reports what was realized. It cannot choose the correction policy or repair a wrong SUT decision into the canonical answer. |
| Fixture-curated context becomes retrieval | Harness-curated bundle delivery is explicitly not retrieval, search, ranking, distractor filtering, or active context assembly. |
| Oracle-visible fields become SUT schema | SUT core must expose required semantic distinctions, but implementation representation remains open. Oracle score, validity, claim, and branch metadata stay evaluation-side. |

## Unresolved Risks Before Acceptance

- The exact language, framework, and test runner are still undecided; this ADR only constrains dependency direction and responsibility ownership.
- The first implementation may discover that shared boundary types are useful. If introduced, they must be audited for oracle leakage before acceptance evidence is trusted.
- The fixture/oracle package must enforce visibility separation mechanically enough that accidental answer-bearing fields cannot be passed to the SUT during formal runs.
- `EVAL-004` may later require richer behavior-configuration metadata for formal evaluation records; this ADR does not pre-solve that metadata.
- `SLICE-005` may require stricter report or claim evidence than this boundary alone provides.
- `DEP-003` remains open; if runtime maintenance semantics enter the first milestone, this boundary may need revision.

## Register Effect If Accepted

Upon acceptance, update `OPEN_QUESTIONS.md` as follows:

- move `SLICE-003` to `Resolved` with outcome `Decision`, resolved by this ADR for the first `SCN-001` selected-slice milestone;
- record that the accepted minimum internal boundary is a two-project SUT core and evaluation project split with one-way evaluation-to-SUT dependency and strict SUT-visible versus oracle-only data separation;
- record that the boundary preserves transition-inside SUT responsibilities from `ADR-002`, curated fixture context from `ADR-004`, fixture/oracle separation from `ADR-005`, state/projection responsibilities from `ADR-006`, and dependency identity/effective endpoint rules from `ADR-007`;
- keep `DEP-003` `Open` and non-active unless runtime maintenance semantics block implementation;
- re-triage `SLICE-005` as the likely next acceptance-gate frontier, without resolving final done criteria;
- keep `EVAL-004` deferred unless the next artifact prepares a first evaluation record, comparison, or evaluated compatibility claim;
- keep `EVAL-005` deferred unless the next artifact prepares final scoring or scenario-scoreability criteria.

No other question automatically activates merely because this ADR is accepted.

## Reconsideration Triggers

Reconsider or supersede this ADR if:

- implementation cannot preserve fixture/oracle separation without a stronger physical package, process, or repository boundary;
- SUT-visible contracts accidentally encode branch, path, claim-class, scoring, canonical-pressure, expected-transition, or hidden answer metadata;
- oracle inspection cannot verify SUT-owned state and dependency relations through public projections without reading private SUT internals in a way that changes behavior;
- the simulator must choose behavior policy for the SUT to complete the path;
- capture/reporting becomes necessary input to later SUT transitions;
- the selected slice introduces real production memory, retrieval, model/runtime trust boundaries, maintenance triggers, external operations, product surfaces, or full `SCN-001` pass claims;
- `SLICE-005`, `EVAL-004`, `EVAL-005`, or `DEP-003` requires a broader boundary to make first-milestone claims scoreable.

## Non-Scope

This ADR answers only the minimum internal boundary forced by the first selected slice. It is not a general Zoey architecture, not a service design, not a persistence design, not an evaluation acceptance gate, and not a claim that the first milestone passes `SCN-001`.
