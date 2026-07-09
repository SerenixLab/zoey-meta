# Zoey Engineering Standard

Document version: `V0.1.0`

Status: `Draft`

Date: 2026-07-09

Decision basis:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.17`
- `decisions/ADR-001-first-vertical-slice.md` `R1`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`
- `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md` `R2`
- `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md` `R3`
- `decisions/ADR-005-scn001-selected-slice-fixture-oracle-contract.md` `R2`
- `decisions/ADR-006-scn001-selected-slice-state-contract.md` `R2`
- `decisions/ADR-007-scn001-selected-slice-dependency-identity.md` `R3`
- `decisions/ADR-008-scn001-selected-slice-internal-boundary.md` `R2`

## Purpose

This document defines the minimum engineering standard for the first Zoey implementation work after acceptance of the selected-slice internal boundary.

It is not a product architecture, acceptance gate, scoring policy, runtime trust-boundary policy, storage design, UI standard, or final repository convention. Its job is narrower:

- make implementation work auditable against accepted decisions;
- prevent accidental boundary collapse while code is still small;
- define project/package hygiene before implementation habits harden;
- define quality gates for non-throwaway code;
- identify when work must stop and activate a deferred question before making stronger claims.

The standard is intentionally stricter where mistakes could create an unearned selected-slice pass, leak oracle information into SUT behavior, hide state provenance, or make later evidence impossible to inspect.

## Engineering Need Analysis

The accepted ADR sequence creates an unusual engineering problem: the first implementation must be small and synthetic, but its code must preserve distinctions that are normally lost in prototypes.

The standard is needed because ordinary "clean code" rules are not enough for Zoey's first slice. A neat implementation can still be invalid if it lets evaluation code perform SUT semantics, lets fixture metadata leak through record identity, lets the harness choose behavior, or keeps only final answers while losing provenance and relations.

The strongest risks found in the current design baseline are:

- evaluator-side semantic promotion: raw fixture evidence is converted into SUT-owned conclusions before crossing the SUT boundary;
- answer leakage by structure or identity: path, branch, claim, scoring, or canonical-pressure context reaches SUT input through fields, IDs, or shared types;
- harness policy arbitration: the harness chooses which SUT proposal or disposition is realized;
- hidden retrieval expansion: selected-slice state access turns into broad memory search or context assembly;
- retrospective evidence repair: capture, reporting, or inspection creates missing SUT state after the relevant transition;
- overclaiming: implementation artifacts imply acceptance, scoreability, production memory, or full scenario pass before the corresponding questions are resolved.

The engineering response is therefore not to pick a final framework early. It is to create mechanical guardrails around ownership, dependency direction, input safety, output selection, state evidence, relation inspection, test coverage, and claim language.

## Normative Language

`MUST` marks a binding rule for non-throwaway implementation work.

`SHOULD` marks the default expectation. A deviation is allowed only when the implementation records the reason and preserves the same accepted decision pressure.

`MAY` marks an allowed option.

`MUST NOT` marks a prohibited implementation shape unless a later accepted decision supersedes this standard.

`Throwaway` means an experiment that is not used as selected-slice evidence, not presented as architecture-compatible implementation, not reused as the basis of the first implementation projects, and not used to support a milestone claim.

## Scope

This standard applies to:

- first implementation projects or packages created under `ADR-008 R2`;
- selected-slice SUT core code;
- selected-slice evaluation code, including harness, fixture/oracle, simulator, capture, and reporting seams;
- tests that protect accepted ADR boundaries;
- generated artifacts that may later become implementation inputs;
- documentation that claims implementation compatibility with accepted ADRs.

This standard does not apply to:

- exploratory notes that are clearly marked throwaway;
- pure document review in this meta repository;
- future production services not yet authorized by an accepted decision;
- final acceptance scoring, which remains governed by `SLICE-005`;
- formal evaluation-record metadata, which remains governed by `EVAL-004`;
- final scoreability criteria, which remain governed by `EVAL-005`;
- runtime maintenance triggers, which remain governed by `DEP-003`.

## Current Engineering Goal

The immediate engineering goal is to create the first selected-slice implementation shape without reopening or weakening the accepted boundary.

The implementation should be small enough to inspect directly and strong enough that later evaluation work can ask:

```text
Did the SUT own the semantic transition?
Did evaluation supply only permitted evidence and simulator facts?
Did retained state preserve identity, origin, order, status, and local relations?
Can the oracle inspect the result without repairing missing SUT behavior?
```

The first implementation is not expected to prove that Zoey is production-ready, has full memory architecture, supports real personal continuity, passes full `SCN-001`, or can safely route private state across real inference trust boundaries.

## Binding Engineering Principles

### 1. Accepted Decisions Are The Source Of Truth

Implementation MUST preserve accepted ADRs over local convenience.

If code, tests, or documentation would require changing an accepted decision, the change MUST be handled as a decision update or new ADR, not hidden inside implementation.

Implementation comments and issue notes MAY point out friction with accepted decisions, but they MUST NOT silently implement a different boundary.

### 2. Claim Boundaries Are Part Of Engineering Quality

An implementation is not merely "working" because it produces plausible behavior. It must preserve the claim boundary of the milestone.

Code, tests, demos, reports, and README text MUST NOT claim:

- full `SCN-001` pass;
- production memory;
- retrieval or context-assembly capability;
- real Japanese pedagogy quality;
- production voice behavior;
- runtime trust-boundary safety;
- durable Zoey continuity;
- first formal evaluation-record sufficiency;
- final scoreability;
- first selected-slice completion;

unless the applicable open questions have been activated and resolved.

### 3. Boundary Safety Beats Implementation Convenience

The first implementation MUST prefer boring, inspectable, mechanically constrained boundaries over elegant abstractions that make ownership ambiguous.

Shared helpers are allowed only when they do not create transitive dependency from SUT core to evaluation-owned semantics.

Where a shortcut would make the SUT pass because the harness, fixture, simulator, capture, report, or oracle silently did SUT work, the shortcut is invalid.

### 4. Evidence Must Survive Refactoring

The selected slice exists to test state, transition, and dependency evidence. Refactoring must preserve inspectability.

A refactor is not acceptable if it keeps final behavior but loses:

- source and role of input facts;
- SUT-derived transition evidence;
- retained state identity;
- effective endpoint identity;
- order and consumer history;
- local typed relations;
- separation between SUT state and oracle-only facts;
- passive inspection surface needed by the oracle.

## Project And Package Shape

### Minimum Shape

The first implementation SHOULD use two code projects or packages:

```text
scn001_sut_core/
scn001_eval/
```

The exact language, build tool, test runner, and repository layout remain undecided. The engineering requirement is the responsibility boundary, not a specific technology.

The dependency direction MUST be:

```text
scn001_eval -> scn001_sut_core public boundary
scn001_sut_core -> no dependency on scn001_eval
```

The SUT core MUST NOT import, instantiate, call, configure, or depend on:

- harness modules;
- fixture/oracle modules;
- simulator modules;
- capture/reporting modules;
- branch policy;
- scoring logic;
- claim-class labels;
- evaluation-owned record types;
- answer-bearing fixture package records.

### Internal SUT Areas

The SUT core SHOULD keep these responsibilities distinguishable, even if implemented in a small number of files at first:

- public boundary;
- SUT-safe input ingestion;
- run-scoped state;
- selected-slice transitions;
- relation and reference handling;
- passive inspection;
- SUT output emission.

These are responsibility areas, not mandated subpackages. A tiny implementation may keep them compact, but it MUST remain clear which code owns each responsibility.

### Internal Evaluation Areas

The evaluation project SHOULD keep these responsibilities distinguishable:

- harness;
- fixture projection;
- oracle predicates;
- simulator realization;
- capture;
- reporting/output seams.

Evaluation code MAY hold answer-bearing fixture/oracle records internally. Those records MUST NOT cross the SUT public boundary.

### Shared Packages

A shared package MAY exist only if it is lower-level and SUT-safe.

It MUST NOT contain:

- oracle-only fields;
- answer-bearing fixture metadata;
- path IDs;
- bundle IDs;
- branch policy;
- claim-class guidance;
- scoring results;
- canonical-pressure labels;
- expected-transition identifiers;
- evaluation-owned record families;
- pre-interpreted semantic result types that hand SUT-owned conclusions to the SUT.

If a shared package starts to encode evaluation semantics, it MUST be split or the relevant open question/ADR must be revisited before the code is used as non-throwaway implementation.

## Public Boundary Standard

### SUT Input

Every evaluation-origin input crossing into SUT core MUST pass through a SUT-safe public input contract.

For this standard, SUT-safe means:

```text
visibility-safe + state-origin-safe + role-preserving
```

Visibility-safe means the payload contains no evaluation-only metadata such as oracle expectations, branch policy, path IDs, bundle IDs, claim-class labels, scoring labels, expected-transition identifiers, canonical-pressure labels, canonical-match results, run-validity classifications, or hidden answer fields.

State-origin-safe means the evaluator has not transformed raw evidence into a SUT-owned semantic conclusion.

Role-preserving means the input keeps its accepted role:

- communication remains communication;
- task observation remains task observation;
- chronology remains chronology;
- context label remains context label;
- affordance remains affordance;
- simulator realization remains simulator realization;
- state reference remains a reference to already-owned SUT state.

The evaluation adapter MAY change names, serialization, transport shape, or host-language representation. It MUST NOT perform SUT semantic transitions.

Examples:

```text
allowed:    raw V-003 utterance -> SUT communication event
prohibited: raw V-003 utterance -> current correction-control state

allowed:    C-005/C-006 observations -> SUT task observation records
prohibited: C-005/C-006 observations -> recognition/production split conclusion

allowed:    C-002 utterance -> SUT communication event
prohibited: C-002 utterance -> attributed user assertion

allowed:    L-002 fixture item -> opaque SUT-visible state handle
prohibited: CF2-L-003 literal fixture/path ID -> SUT-visible state handle
```

### SUT Processing

The harness MUST NOT call SUT internals by accepted semantic transition name.

Invalid public boundary shapes include:

```text
execute_decision_point("DP-TRIAL-FORM")
run_transition("FORM_DELAYED_CORRECTION_TRIAL")
execute_expected_transition("LATER_USE_APPLY_T12")
```

The SUT MAY internally organize code around named transition functions. Those functions MUST NOT become harness commands that reveal the expected answer.

### SUT State Access

SUT-owned state access in the selected slice means:

- identity resolution;
- direct access to selected-slice state already active in the current run;
- local relation traversal required by `ADR-006` and `ADR-007`.

It does not authorize:

- open memory search;
- broad relevance ranking;
- distractor filtering;
- active cognitive-frame assembly;
- retrieval over a larger state universe.

If implementation needs any of those capabilities to pass, work MUST stop and the relevant open questions must be re-triaged before the code supports a milestone claim.

### SUT Output

Where simulator realization occurs, the SUT public output MUST identify the material proposal or behavior disposition selected by the SUT for realization.

The harness MUST transport the SUT-selected output. It MUST NOT choose among competing SUT outputs based on fixture path, branch policy, oracle expectations, or expected outcome.

If the SUT emits multiple materially competing realization candidates without selecting one, the harness MUST NOT rescue the run by choosing the canonical output. The run must follow the accepted ambiguity, invalidity, or obligation-failure policy.

### Passive Inspection

The SUT MUST expose enough passive inspection surface for selected-slice state, transition evidence, references, and local relations.

Inspection MUST NOT:

- create behavior-driving state;
- activate state;
- narrow or retire state;
- infer missing lineage and write it back;
- repair missing relation history;
- run a cognitive reconstruction that changes the SUT evidence being inspected.

Acceptable inspection shapes include bounded snapshots and local relation inspection, such as:

```text
capture_inspection_snapshot()
inspect_record(scoped_ref)
enumerate_local_relations(scoped_ref)
inspect_effective_state(scoped_ref, order_ref)
```

The standard does not require a general graph query engine.

## State And Relation Standard

### Required Distinctions

Implementation MUST preserve the selected-slice distinctions accepted by `ADR-006`:

- run-scoped cross-transition SUT state;
- SUT-owned transition evidence;
- lineage-preserving projections;
- derived inspection facts;
- fixture/oracle-only facts.

It MUST NOT collapse:

- user assertion into objective fact;
- raw observation into skill conclusion;
- direct current-session correction into future trial state;
- proposal intent into activation;
- simulator realization into semantic correctness;
- outcome observation into causal proof;
- fixture label into SUT transition result;
- oracle score into SUT state.

### References

Records that must be inspected, related, cited, projected, captured, or reported MUST have stable scoped references sufficient for the selected slice.

References MUST NOT encode evaluation context visible to the SUT when that context reveals path, branch, checkpoint, claim class, scoring, canonical pressure, expected transition, or hidden answer metadata.

Evaluation-side fixture IDs such as `L-002` and `CF2-L-003` MAY exist in fixture/oracle records. SUT-visible state handles MUST be opaque or otherwise non-evaluation-bearing.

### Relations

Implementation MUST preserve the local relation semantics required by `ADR-007` where applicable:

- `source`;
- `basis`;
- `support`;
- `binding`;
- `transition_ancestry`;
- `applicability`;
- `projection_of`;
- `realization`;
- `outcome`;
- `explanation_support`;
- `supersession`;
- `retirement`;
- `narrowing`;
- `conflict`.

The representation may be fields, records, tables, logs, events, object references, or another inspectable structure.

The oracle must be able to enumerate required local relations for inspected records without relying on private manual reasoning or retrospective narrative.

### Time And Order

Implementation MUST preserve enough order information to distinguish:

- delivered input;
- ingested input;
- retained state;
- transition basis use;
- proposal emission;
- simulator realization;
- outcome observation;
- later consumer use;
- inspection/capture after the fact.

Where a relation points to mutable or lifecycle-bearing state, implementation MUST preserve the effective endpoint meaning at the material order point.

## Evaluation Domain Standard

### Fixture Projection

Fixture/oracle package records may be answer-bearing inside evaluation code. The SUT-visible projection MUST be structurally separate or otherwise mechanically constrained.

It is invalid to pass a full answer-bearing object to SUT code with the claim that the SUT ignores hidden fields.

The formal delivery path SHOULD make accidental full-record delivery fail loudly.

### Harness

The harness owns delivery order, fixture bundle control, simulator routing, capture orchestration, run isolation, and oracle invocation.

The harness MUST NOT own:

- SUT semantic conclusions;
- expected-transition selection as SUT input;
- hidden memory retrieval for the SUT;
- reconstruction of lost SUT state;
- activation checks;
- later-use applicability;
- explanation support;
- semantic arbitration among competing SUT outputs.

### Simulator

The simulator realizes SUT-selected proposal intents or behavior dispositions into synthetic facts.

It MUST NOT:

- choose correction policy;
- repair a wrong SUT decision;
- decide semantic correctness;
- own branch gates;
- leak canonical intervention matches to the SUT;
- become a direct SUT dependency.

Simulator outputs that return to SUT MUST use a SUT-visible projection subject to the same input safety barrier as fixture inputs.

### Capture And Reporting

Capture/reporting may collect:

- delivered SUT-visible inputs;
- SUT outputs;
- simulator facts;
- SUT inspection snapshots;
- oracle-derived inspection facts;
- failure artifacts.

Capture/reporting MUST NOT become behavior-driving input to later SUT transitions.

Capture/reporting MUST NOT create missing SUT evidence after the fact and present it as contemporaneous SUT state.

Reporting MAY produce bounded evidence reports and failure artifacts, but MUST NOT claim final milestone acceptance until `SLICE-005` resolves.

## Testing Standard

### Test Philosophy

Tests must protect semantic boundaries, not only final examples.

A test suite that checks only final user-facing wording is insufficient. The first implementation must make wrong ownership fail.

### Minimum Test Categories

Non-throwaway first implementation SHOULD include tests for:

1. Dependency direction:
   `scn001_sut_core` cannot import evaluation modules.

2. SUT input safety:
   full fixture/oracle records and full simulator evaluation records cannot be ingested by the SUT public boundary.

3. State-origin preservation:
   raw communications, task observations, chronology facts, context labels, affordances, simulator facts, and state references are not pre-promoted into SUT-owned conclusions by evaluation adapters.

4. Expected-transition leakage:
   public boundary calls do not expose decision-point names, path stages, expected transitions, claim classes, branch policy, or canonical pressure.

5. Harness non-arbitration:
   if the SUT emits competing outputs without selecting one for realization, the harness does not choose the canonical one.

6. Bounded state access:
   later-use paths resolve opaque SUT-owned handles or local relations, not broad retrieval/ranking.

7. Passive inspection:
   inspection calls do not mutate SUT state or create missing lineage.

8. Relation preservation:
   inspected records expose required local relations and effective endpoint identity for selected-slice obligations.

9. Simulator isolation:
   SUT code cannot import or call simulator code.

10. Claim boundary:
    reports and README text do not claim acceptance, scoring, production readiness, or broader scenario pass.

### Negative Tests

Each boundary-critical positive test SHOULD have at least one negative test.

Examples:

- passing `CF2-L-003` as a SUT-visible handle should fail if it reveals evaluation context;
- passing a full fixture item with hidden oracle fields should fail;
- passing a full simulator realization record with canonical-match fields should fail;
- harness selecting the only canonical output among two SUT outputs should fail;
- inspection that writes missing relation evidence should fail.

### Determinism And Nondeterminism

Implementation tests may use deterministic stubs where the tested responsibility is not model behavior.

When nondeterministic model behavior is introduced, tests MUST distinguish:

- deterministic contract tests;
- replay tests;
- exploratory behavior samples;
- formal milestone evidence.

Formal nondeterministic campaign policy remains governed by accepted evaluation decisions and later acceptance-gate work. Ordinary implementation tests MUST NOT pretend to satisfy formal campaign acceptance unless the relevant evaluation questions have been resolved.

## Review Standard

### Review Stance

Code review for Zoey implementation must prioritize:

1. boundary violations;
2. state-origin and role-preservation failures;
3. oracle/evaluation leakage;
4. missing transition evidence;
5. relation/reference ambiguity;
6. hidden retrieval or context assembly;
7. harness arbitration;
8. passive inspection violations;
9. overbroad claims;
10. ordinary correctness, maintainability, and readability.

### Required Review Questions

For any non-throwaway change, reviewers SHOULD ask:

- Which accepted ADR does this change rely on?
- Does this create or weaken a SUT/evaluation dependency?
- Does any evaluation-origin object cross into the SUT?
- Does an adapter perform a semantic transition that belongs to the SUT?
- Does the harness choose among SUT outputs?
- Does SUT state access become retrieval or relevance ranking?
- Can the oracle inspect required evidence without private-state spelunking or repair?
- Does the change preserve references, effective endpoint identity, order, and local relations?
- Does any text overclaim acceptance, scoreability, production readiness, or continuity?
- Does this change trigger `SLICE-005`, `EVAL-004`, `EVAL-005`, `DEP-003`, or another open question?

### Review Outcomes

A review MUST block merge or promotion to non-throwaway implementation when it finds:

- SUT imports evaluation code;
- oracle or branch metadata can reach behavior-driving SUT input;
- evaluation adapter precomputes SUT semantic conclusions;
- harness arbitrates among competing SUT outputs;
- SUT pass depends on retrieval/context assembly excluded from the milestone;
- inspection mutates or repairs SUT evidence;
- implementation claims acceptance or scoring before the relevant question resolves.

## Documentation Standard

Implementation documentation MUST identify:

- governing baseline documents and ADR versions;
- project/package responsibility split;
- public SUT boundary;
- evaluation-only record families;
- SUT-visible input contracts;
- SUT output and inspection contracts;
- known non-scope and unsupported claims.

Documentation MUST NOT describe selected-slice scaffolding as final Zoey architecture.

Documentation SHOULD use bounded phrasing:

```text
Supports first selected-slice implementation under ADR-008 R2.
Does not claim final acceptance, production memory, retrieval, trust-boundary safety, or full SCN-001 pass.
```

## Generated Code And AI Assistance

AI-generated code, schemas, tests, or documentation MAY be used, but they are not authoritative.

Generated artifacts MUST be reviewed against this standard before becoming non-throwaway implementation.

Generated code is especially suspect when it:

- creates broad DTOs carrying hidden fields;
- introduces generic memory/retrieval abstractions;
- adds services, queues, stores, event buses, or graph APIs without accepted need;
- merges fixture, oracle, harness, and SUT record types;
- writes user-facing claims from final behavior without preserving evidence;
- invents acceptance scoring or report metadata;
- uses plausible comments instead of inspectable state.

## Change Control

### Changes To This Standard

This standard may be revised as implementation pressure becomes concrete.

A change is editorial when it clarifies language without changing:

- required project/package boundary;
- SUT/evaluation dependency direction;
- SUT-safe input definition;
- state/relation obligations;
- test gate;
- claim boundary;
- activation trigger for open questions.

A material change requires explicit review against accepted ADRs and `OPEN_QUESTIONS.md`.

### Implementation Trigger Checks

Before creating or merging non-throwaway implementation that does any of the following, re-triage the named question:

| Implementation pressure | Required trigger check |
| --- | --- |
| Drafting final acceptance gate or claiming first slice done | `SLICE-005` |
| Creating first formal evaluation record, comparison, or compatibility claim | `EVAL-004` |
| Defining final scoring or scenario-scoreability criteria | `EVAL-005` |
| Introducing expiry, revocation propagation, capability degradation, external refresh, or manual review maintenance | `DEP-003` |
| Introducing real personal retention or reuse across purposes | `MEM-*` |
| Sending retained personal state across materially different inference/runtime trust boundary | `TRUST-001` |
| Adding product/user-facing surfaces or workflows | `PROD-*`, `SURF-*` |
| Claiming continuity across restore, migration, disconnection, or state loss | `CONT-*` |
| Reusing legacy material as active Zoey implementation | `LEG-*` |

## First Implementation Readiness Checklist

Before first implementation project creation, the engineering plan SHOULD answer:

- What are the SUT core and evaluation package names?
- How is one-way dependency mechanically enforced?
- What public SUT input, output, run lifecycle, and inspection seams exist?
- What record families are evaluation-only?
- How are SUT-visible fixture projections created?
- How are SUT-visible simulator projections created?
- How are opaque SUT state handles represented without leaking fixture path identity?
- How does the SUT identify the proposal or disposition selected for simulator realization?
- How is broad retrieval/context assembly prevented?
- How is passive inspection kept read-only?
- Which negative tests protect the boundary?
- What documentation text prevents overclaiming?

## Non-Scope

This standard does not decide:

- programming language;
- package manager;
- test runner;
- repository host;
- CI provider;
- service topology;
- database or storage engine;
- event bus;
- graph store;
- model provider;
- inference gateway;
- prompt architecture;
- production trust-boundary policy;
- product UI;
- acceptance gate;
- final scoreability;
- full `SCN-001` pass criteria.

Those choices should be made only when concrete implementation pressure requires them and the appropriate open questions or ADRs allow them.

## Red-Team Checklist

An implementation that appears to pass selected-slice behavior is suspect if any answer below is yes:

- Can the SUT import evaluation code?
- Can a full fixture/oracle object reach SUT input?
- Can a full simulator evaluation record reach SUT input?
- Can fixture path, branch, claim class, score, expected transition, or canonical pressure leak through IDs?
- Can evaluation adapt raw communication into scoped correction/control state before SUT processing?
- Can evaluation adapt task observations into a recognition/production conclusion before SUT processing?
- Can the harness pick the proposal or disposition that gets realized?
- Can capture/reporting create the missing relation evidence after the fact?
- Can inspection mutate state or repair lineage?
- Can the SUT pass by broad memory retrieval or relevance ranking?
- Can report text claim milestone completion before `SLICE-005` resolves?
- Can repeated exploratory runs be cherry-picked and presented as formal campaign evidence?

Any `yes` requires a fix, a bounded throwaway label, or a new decision before the work can support first-slice implementation claims.
