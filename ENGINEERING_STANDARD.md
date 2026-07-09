# Zoey Engineering Standard

Document version: `V0.2.0`

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

## Authority And Baseline Validity

This standard is a derivative engineering-conformance artifact. It does not create, redefine, or supersede semantic architecture decisions.

For any selected-slice rule in this standard:

```text
governing ADR or register entry = semantic authority
ENGINEERING_STANDARD.md = engineering consequence and enforcement path
```

If this standard conflicts with a cited governing artifact, the governing artifact wins. The affected standard rule is treated as invalid for conformance claims until corrected.

The standard is valid only against the exact baseline listed above. If any listed governing artifact is superseded, materially revised, or discovered not to be accepted at the declared revision, implementation work MUST revalidate the affected rules before using this standard to support architecture-compatibility, selected-slice, or milestone claims.

The implementation repo MUST record the governing baseline it uses. A conformance ledger entry that cites this standard without also citing the governing ADR/register source is incomplete.

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

The research-backed principle used here is: standards should define outcomes and checkpoints without pretending that one tool or workflow is universal. NIST's SSDF is useful as a model here because it frames practices as outcomes rather than mandating one mechanism. Google Engineering Practices are useful for the code-health layer because they emphasize small, reviewable changes, tests with behavior changes, and continuous code-health improvement. OWASP SAMM is useful for the conformance layer because it treats internal policies and standards as application-specific requirements that can be measured.

## External Engineering References

These references inform the shape of this standard. They are not semantic authority for Zoey; accepted Zoey ADRs and registers remain authoritative.

- NIST SP 800-218, Secure Software Development Framework: <https://csrc.nist.gov/pubs/sp/800/218/final>. Used for the idea that a standard should define high-level outcomes, residual-risk visibility, and common vocabulary without binding the project to one tool.
- Google Engineering Practices, Code Review Standard: <https://google.github.io/eng-practices/review/reviewer/standard.html>. Used for the code-health floor, especially the rule that each change should improve or at least not degrade overall code health.
- Google Engineering Practices, Small CLs: <https://google.github.io/eng-practices/review/developer/small-cls.html>. Used for small, self-contained changes, behavior-change test obligation, and separating refactors from feature changes.
- OWASP SAMM Policy And Compliance: <https://owaspsamm.org/model/governance/policy-and-compliance/>. Used for application-specific requirements, baseline expectations, checkpoints, and measurable adherence.

## Engineering Layers

This standard has two layers.

The first layer is the general code-health floor. It applies to all non-throwaway first implementation work regardless of which selected-slice responsibility the code serves. Its job is to keep the project understandable, reviewable, debuggable, and hard to accidentally expand.

The second layer is the selected-slice conformance profile. It applies specifically to the first `SCN-001` implementation under accepted `ADR-008 R2`. Its job is to prevent code from silently violating the SUT/evaluation boundary, fixture/oracle separation, selected-slice state contract, dependency identity contract, and claim boundaries.

Both layers matter. A codebase can preserve the selected-slice boundary and still become hard to maintain. A codebase can be clean and still be invalid because it lets the harness, fixture, simulator, or oracle do SUT work.

## Normative Language

`MUST` marks a binding rule for non-throwaway implementation work.

`SHOULD` marks the default expectation. A deviation is allowed only when the implementation records the reason and preserves the same accepted decision pressure.

`MAY` marks an allowed option.

`MUST NOT` marks a prohibited implementation shape unless a later accepted decision supersedes this standard.

`Throwaway` means an experiment that is not used as selected-slice evidence, not presented as architecture-compatible implementation, not reused as the basis of the first implementation projects, and not used to support a milestone claim.

## Enforcement Classes

Every important engineering rule SHOULD be assigned one of these enforcement classes in the implementation repo's conformance ledger:

| Class | Meaning |
| --- | --- |
| `static` | A static dependency, schema, lint, or build rule fails before tests run. |
| `contract-test` | A test verifies a public contract, serialization shape, schema behavior, or boundary behavior. |
| `negative-test` | A test deliberately attempts the prohibited behavior and expects rejection or failure. |
| `review-gate` | The rule is checked through explicit code review because it is not yet mechanically enforceable. |
| `unenforced-risk` | The rule is known but not currently enforced; the residual risk is documented. |

Markdown alone does not make a rule protected. If a rule is only stated in this document, it is `review-gate` at best until the implementation repo records stronger enforcement.

Preferred enforcement order:

```text
mechanically impossible
    -> static check
    -> contract/negative test
    -> explicit review gate
    -> documented unenforced risk
```

Rules that protect SUT/evaluation dependency direction, answer-bearing payload exclusion, SUT-visible reference safety, public-boundary behavior evidence, inspection passivity, and harness non-arbitration SHOULD become `static`, `contract-test`, or `negative-test` before they support selected-slice claims.

## Engineering Rule Identity

Binding implementation rules SHOULD have stable rule IDs before they are used in tests, reviews, CI output, trace metadata, or conformance claims.

Use these prefixes unless the implementation repo defines a stricter local scheme:

| Prefix | Rule family |
| --- | --- |
| `ENG-BASE-*` | Baseline validity, source authority, and revision checks. |
| `ENG-HEALTH-*` | General code-health and change-discipline floor. |
| `ENG-CONF-*` | Selected-slice architecture conformance. |
| `ENG-CLAIM-*` | Artifact labeling, evidence labels, and claim boundaries. |
| `ENG-CHANGE-*` | Change-control triggers and deferred-question activation. |

Each binding rule SHOULD be expressible in this form:

```text
ID:
Source:
Rule:
Forbidden Shape:
Required Check:
Enforcement Class:
Failure Consequence:
```

Example:

```text
ID: ENG-CONF-IMPORT-001
Source: ADR-008 R2; ENGINEERING_STANDARD.md V0.2.0
Rule: SUT core has no direct or transitive dependency path to evaluation modules.
Forbidden Shape: scn001_sut_core imports, instantiates, configures, or reflects into scn001_eval.
Required Check: language-appropriate dependency conformance check plus review of dynamic import surfaces.
Enforcement Class: static, with residual-risk review gate for dynamic loading if present.
Failure Consequence: block merge or mark the work throwaway; the run cannot support selected-slice implementation claims.
```

If a test fails, review blocks, or report flags a conformance issue, it SHOULD name the rule ID and governing source. This keeps failures tied to the accepted architecture instead of to reviewer preference.

## Conformance Ledger

Each non-throwaway implementation repo SHOULD maintain a small conformance ledger. It may be a Markdown file, test manifest, CI note, or equivalent project-local artifact.

The ledger SHOULD use this shape:

```text
Rule ID:
Rule:
Source:
Applies To:
Enforcement Class:
Mechanism:
Status:
Residual Risk:
Owner:
Last Checked:
```

Example:

```text
Rule ID: ENG-CONF-IMPORT-001.
Rule: SUT core has no dependency path to evaluation modules.
Source: ADR-008 R2; ENGINEERING_STANDARD.md V0.2.0.
Applies To: scn001_sut_core.
Enforcement Class: static.
Mechanism: implementation-selected import/dependency conformance tool.
Status: enforced in local test/CI gate.
Residual Risk: dynamic imports or generated code require review.
Owner: implementation maintainer.
Last Checked: YYYY-MM-DD.
```

The ledger is not busywork. It prevents standard rot: the project must be able to tell the difference between a rule that is actually enforced and a rule that is only intended.

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

## Code-Health Floor

The first implementation SHOULD stay small, explicit, and local. The goal is not to create a general framework; it is to make the selected-slice pressure executable without losing the accepted distinctions.

Non-throwaway implementation SHOULD follow these rules.

### Change Discipline

Each change SHOULD have one primary purpose:

- feature behavior;
- boundary/conformance protection;
- test coverage;
- refactor;
- documentation;
- build/tooling.

Mixing behavior changes with broad refactors SHOULD NOT happen unless the implementation records why the split would be more dangerous than the combined change. In that case, the review must identify which lines are behavior-changing and which are structural.

Large changes SHOULD be split when they cross multiple ownership areas, introduce new public contracts, move state ownership, or touch both SUT and evaluation code. A change that cannot be understood by direct review is too large to support first-slice evidence without an explicit split plan.

### Behavior-Change Test Obligation

Any non-throwaway behavior change SHOULD add or update tests that fail without the change.

Bug fixes SHOULD include a regression test unless the failure is purely editorial, build-environment-specific, or not reproducible in the implementation test harness. If no regression test is added, the reason must be recorded in the review or ledger.

Tests SHOULD name the behavior, boundary, or rule they protect. A vague test that only checks a happy-path final string is insufficient when the change affects state ownership, evaluation visibility, relation evidence, harness behavior, or claim labels.

### Refactoring Discipline

A refactor must preserve externally relevant behavior and conformance evidence.

Refactors SHOULD be separate from feature changes. If a refactor changes behavior, the change is not a pure refactor and must satisfy the behavior-change test obligation.

Refactors MUST NOT remove, merge, rename, or hide evidence needed to inspect:

- input role and state origin;
- SUT-owned transition basis;
- retained state identity;
- effective endpoint identity;
- order and consumer history;
- local typed relations;
- separation between SUT state and oracle-only facts;
- passive inspection surface.

### Locality And Naming

Modules and files SHOULD have one visible responsibility.

Helpers SHOULD be local before they become shared. Shared helpers MUST NOT hide ownership boundaries or create a transitive path from SUT core to evaluation-owned semantics.

Abstractions SHOULD be introduced only after repeated concrete pressure appears. A generic abstraction is suspect if it appears before at least two concrete call sites prove the shared shape.

Broad names such as `manager`, `engine`, `context`, `memory`, `state`, `handler`, `processor`, `service`, or `system` SHOULD be avoided unless the responsibility is explicitly bounded in the name or module path.

### Dead Code, TODOs, And Scaffolding

Dead scaffolding SHOULD be removed once it is no longer needed.

Throwaway code MUST remain clearly marked and MUST NOT be imported by non-throwaway implementation code.

TODOs in non-throwaway code SHOULD identify one of:

- the governing ADR or open question that blocks completion;
- the follow-up issue or decision record;
- the reason the work is intentionally deferred;
- the review owner responsible for removing or resolving it.

A TODO that says only `fix later`, `temporary`, or `clean up` is not enough for architecture-bearing code.

### Failure Quality

Failure messages SHOULD point to the violated contract, rule ID, or governing ADR.

Boundary failures SHOULD fail closed and explain what was rejected without exposing oracle answers, expected transitions, branch labels, claim-class labels, or scoring metadata to SUT-visible surfaces.

### Generated Structure

Generated code SHOULD be reviewed before it creates project structure, record families, shared contracts, broad DTOs, or serialized payload shapes.

Generated code MUST NOT become the first source of authority for ownership boundaries, state categories, relation names, evidence labels, or acceptance claims.

### Documentation Symmetry

Documentation should explain current non-scope as clearly as current capability.

Implementation documentation SHOULD make unsupported claims hard to copy into demos, reports, or README summaries.

Code-health failures do not automatically violate ADR-008, but they make boundary review weaker. A small confusing helper can become the first dependency leak. A broad DTO can become the first answer leak. A vague test can become the first overclaim.

## Selected-Slice Conformance Profile

The first implementation profile consists of the following mandatory conformance areas:

| Area | Preferred enforcement |
| --- | --- |
| SUT has no direct or transitive dependency path to evaluation modules | `static` |
| Evaluation full records cannot cross SUT public input | `static` or `contract-test` plus `negative-test` |
| SUT-visible payloads reject unknown or prohibited fields | `contract-test` plus `negative-test` |
| Evaluation adapters preserve role and state origin | `contract-test` plus `negative-test` |
| Harness cannot call semantic decision-point commands as public SUT behavior input | `contract-test` plus `negative-test` |
| Harness cannot choose among competing SUT outputs | `contract-test` plus `negative-test` |
| SUT state access does not become retrieval or relevance ranking | `contract-test` or `review-gate` with explicit residual risk |
| Inspection does not mutate or repair state | `contract-test` plus `negative-test` |
| Reports and traces cannot claim acceptance before trigger questions resolve | `review-gate` plus documentation test where practical |

If an implementation cannot enforce one of these areas mechanically yet, the conformance ledger MUST record the residual risk before the code is used as non-throwaway implementation.

## Engineering Consequence Matrix

This matrix is the intended shape of selected-slice enforcement. It does not replace the governing ADRs; it maps them to implementation consequences.

| Rule ID | Source | Engineering consequence | Preferred enforcement | Failure consequence |
| --- | --- | --- | --- | --- |
| `ENG-BASE-001` | Baseline list in this standard | Conformance claims must cite the exact governing ADR/register revisions used by the implementation. | `review-gate` plus ledger check | Claim is incomplete until baseline is recorded. |
| `ENG-CONF-IMPORT-001` | `ADR-008 R2` | SUT core has no direct or transitive dependency path to evaluation modules. | `static` | Block merge or mark work throwaway. |
| `ENG-CONF-PAYLOAD-001` | `ADR-005 R2`; `ADR-008 R2` | SUT-visible payloads use allowlist projection and reject answer-bearing or unknown evaluation fields. | `contract-test` plus `negative-test` | Behavior evidence is invalid until rejected paths fail closed. |
| `ENG-CONF-ROLE-001` | `ADR-005 R2`; `ADR-006 R2` | Evaluation adapters preserve input role and state origin; they do not precompute SUT-owned semantic conclusions. | `contract-test` plus review of adapters | Adapter output cannot support selected-slice claims. |
| `ENG-CONF-PUBLIC-001` | `ADR-008 R2` | Selected-slice behavior evidence drives SUT through the public boundary, not internal transition commands. | `contract-test` plus review gate | Evidence is implementation-only, not behavior-compatibility evidence. |
| `ENG-CONF-HARNESS-001` | `ADR-008 R2` | Harness transports the SUT-selected material output and does not arbitrate among competing candidates. | `negative-test` | Run is invalid for selected-slice behavior claims. |
| `ENG-CONF-STATE-001` | `ADR-006 R2`; `ADR-007 R3` | State access remains selected-slice bounded identity/local-relation access, not retrieval or relevance ranking. | `contract-test` or explicit residual-risk review gate | Stop and re-triage open questions before milestone claims. |
| `ENG-CONF-INSPECT-001` | `ADR-006 R2`; `ADR-008 R2` | Inspection is passive and cannot create, repair, narrow, retire, or activate behavior-driving state. | `contract-test` plus `negative-test` | Inspection artifacts cannot be used as conformance evidence. |
| `ENG-HEALTH-CHANGE-001` | Code-health floor; external engineering references | Changes have one primary purpose and are small enough for direct review. | `review-gate` | Split or record why a combined change is safer. |
| `ENG-HEALTH-TEST-001` | Code-health floor; external engineering references | Non-throwaway behavior changes add or update tests that fail without the change. | `review-gate` plus test result | Block promotion to non-throwaway code unless exception is recorded. |
| `ENG-CLAIM-LABEL-001` | `OPEN_QUESTIONS.md`; evaluation ADRs | Artifacts use labels matching what they can support and do not imply acceptance or scoring early. | `review-gate` plus documentation checks | Report/readme/trace label must be corrected before use. |

When a new implementation risk appears, prefer adding one row to this matrix plus one ledger entry over expanding narrative prose. The goal is not more text; it is a shorter path from accepted decision to enforceable check.

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

The first non-throwaway implementation repo MUST choose a language-appropriate dependency conformance mechanism before behavior implementation begins. The standard does not choose the tool. The implementation repo MUST record the chosen mechanism in its conformance ledger.

The gate MUST cover direct and transitive dependency paths where the language/tooling can detect them:

```text
scn001_sut_core -> scn001_eval                      prohibited
scn001_sut_core -> shared_contracts -> scn001_eval  prohibited
scn001_eval.simulator -> scn001_sut_core.private    prohibited
```

If the language permits dynamic imports, generated imports, reflection, plugin loading, or runtime module lookup that the static tool cannot fully see, those mechanisms MUST be listed as residual risk and review-gated.

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

Before a shared package is introduced, the implementation plan SHOULD answer:

- Why is this not local to SUT or evaluation?
- Which side can import it?
- Can it import anything?
- Does it contain only SUT-safe contracts or lower-level primitives?
- Does any public type name or field name carry evaluation vocabulary?
- How is transitive contamination tested?

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

SUT-visible payload projection SHOULD be allowlist-based. Unknown fields and explicitly prohibited fields SHOULD fail closed rather than be ignored.

The implementation SHOULD test serialized payloads, not only in-memory objects, whenever serialization exists. A payload that would carry hidden evaluation metadata over JSON, files, message envelopes, logs, snapshots, or fixtures is still a boundary violation even if host-language types are clean.

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

### Reserved Evaluation Vocabulary

The following vocabulary is reserved for evaluation-owned records and MUST NOT appear in SUT public input fields, SUT-visible serialized payloads, SUT-visible state handles, or behavior-driving SUT state unless a later accepted decision explicitly permits the term as SUT-visible non-answer metadata:

- `path`;
- `bundle`;
- `checkpoint`;
- `decision_point`;
- `claim_class`;
- `oracle_rule`;
- `score`;
- `expected_transition`;
- `branch`;
- `canonical`;
- `pressure`;
- `validity`;
- `pass`;
- `fail`;
- `answer_key`.

This is not a ban on comments, documentation, test names, or evaluation-side records. It is a boundary-contract rule for values, field names, type names, and serialized forms that can affect SUT behavior or SUT-visible state.

If a harmless domain word collides with reserved vocabulary, the implementation MUST either rename the SUT-visible contract or record an explicit exception with review evidence that it does not encode evaluation context.

### SUT Processing

The harness MUST NOT call SUT internals by accepted semantic transition name.

Invalid public boundary shapes include:

```text
execute_decision_point("DP-TRIAL-FORM")
run_transition("FORM_DELAYED_CORRECTION_TRIAL")
execute_expected_transition("LATER_USE_APPLY_T12")
```

The SUT MAY internally organize code around named transition functions. Those functions MUST NOT become harness commands that reveal the expected answer.

Internal unit tests MAY call internal transition functions when testing local implementation details. Such tests MUST NOT count as selected-slice behavior evidence, architecture compatibility evidence, or milestone evidence.

Any test, trace, demo, or report that claims selected-slice behavior compatibility MUST drive the SUT through the accepted public boundary. A result produced by calling an internal transition function is implementation evidence only.

### SUT State Access

SUT-owned state access in the selected slice means:

- identity resolution;
- direct access to selected-slice state already active in the current run;
- local relation traversal required by `ADR-006 R2` and `ADR-007 R3`.

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

This section is an engineering conformance profile over `ADR-006 R2` and `ADR-007 R3`. It is not an independent semantic restatement of those ADRs.

The implementation MUST treat `ADR-006 R2` as the authority for selected-slice state categories and `ADR-007 R3` as the authority for dependency identity and local relation semantics.

If this section gives an example that appears broader, narrower, or different from those ADRs, the ADR wins and this standard must be corrected before the affected rule supports a conformance claim.

### Engineering Consequences

For each selected-slice state or relation obligation required by `ADR-006 R2` or `ADR-007 R3`, the implementation SHOULD identify:

- the code owner that creates it;
- the code owner that may consume it;
- whether it is SUT-owned, evaluation-owned, or inspection-derived;
- whether it may cross the SUT public boundary;
- the reference shape used to cite it;
- the inspection surface that exposes it;
- the test, static check, or review gate that protects it.

Implementation MUST NOT collapse semantically distinct state or relation obligations into a convenient generic record when doing so would hide origin, ownership, order, lifecycle, dependency identity, or oracle-only status.

Examples of prohibited collapses include promoting raw evidence into SUT conclusions outside the SUT, turning simulator realization into semantic correctness, treating fixture labels as SUT transition results, or writing oracle scores into behavior-driving SUT state. These are examples only; `ADR-006 R2` and `ADR-007 R3` govern the full set of selected-slice obligations.

### References

Records that must be inspected, related, cited, projected, captured, or reported MUST have stable scoped references sufficient for the selected slice.

References MUST NOT encode evaluation context visible to the SUT when that context reveals path, branch, checkpoint, claim class, scoring, canonical pressure, expected transition, or hidden answer metadata.

Evaluation-side fixture IDs such as `L-002` and `CF2-L-003` MAY exist in fixture/oracle records. SUT-visible state handles MUST be opaque or otherwise non-evaluation-bearing.

### Relations

Implementation MUST preserve the local relation semantics required by `ADR-007 R3` where applicable, but this standard does not copy the relation catalogue as a second source of truth.

The representation may be fields, records, tables, logs, events, object references, or another inspectable structure. The selected representation must make the required relation evidence enumerable for the selected slice.

The oracle MUST be able to enumerate required local relations for inspected records without relying on private manual reasoning or retrospective narrative.

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

Fixture projection tests SHOULD include:

- full fixture item rejected by SUT input;
- extra oracle field rejected by SUT input;
- reserved evaluation vocabulary rejected where it appears in SUT-visible fields;
- literal path-qualified fixture ID rejected as a SUT-visible state handle;
- role-preserving projection accepted for the corresponding permitted input.

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

### Logs, Snapshots, And Debug Traces

Logs, snapshots, debug traces, and captured payloads are engineering artifacts, but they can become accidental state sources.

Evaluation-only metadata MAY appear in evaluation logs and capture artifacts when needed for debugging or oracle work. It MUST NOT be re-ingested as SUT-visible input or used as behavior-driving SUT state.

SUT-facing logs or snapshots MUST preserve the same visibility and state-origin rules as SUT input/output contracts when they are used for replay, debugging, or later execution.

A replay or restore path MUST NOT promote evaluation capture into SUT state unless a later accepted decision explicitly defines that path.

## Testing Standard

### Test Philosophy

Tests must protect semantic boundaries, not only final examples.

A test suite that checks only final user-facing wording is insufficient. The first implementation must make wrong ownership fail.

### Evidence And Artifact Labels

Implementation artifacts MUST use labels that match what they can support.

Allowed labels before `EVAL-004`, `EVAL-005`, and `SLICE-005` resolve include:

- `dev_trace`: exploratory or development execution trace;
- `conformance_test`: test protecting a boundary, dependency, schema, or claim rule;
- `oracle_unit_test`: test of oracle predicate logic outside formal campaign evidence;
- `behavior_sample`: observed behavior useful for debugging or design review;
- `replay_test`: deterministic replay of a known behavior path;
- `implementation_note`: explanation of code behavior or limitation.

The label `formal_campaign_record` MUST NOT be used until `EVAL-004` resolves the formal evaluation-record metadata contract.

The labels `pass_evidence`, `score`, `scenario_score`, `accepted_slice`, `milestone_complete`, or equivalent MUST NOT be used until the relevant acceptance and scoreability questions resolve.

Development traces MAY be useful evidence for debugging. They are not formal selected-slice pass evidence.

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

11. Reserved vocabulary:
    SUT-visible contracts and serialized payloads do not expose reserved evaluation vocabulary.

12. Artifact labeling:
    development traces, conformance tests, oracle unit tests, and behavior samples cannot be mistaken for formal campaign records or pass evidence.

### Negative Tests

Each boundary-critical positive test SHOULD have at least one negative test.

Examples:

- passing `CF2-L-003` as a SUT-visible handle should fail if it reveals evaluation context;
- passing a full fixture item with hidden oracle fields should fail;
- passing a full simulator realization record with canonical-match fields should fail;
- passing a SUT-visible payload with reserved evaluation vocabulary should fail unless an explicit exception is recorded;
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

### Conformance Before Behavior

Boundary conformance tests SHOULD run before high-level behavior examples. A behavior test that passes after a boundary conformance failure is not meaningful selected-slice evidence.

The implementation test suite SHOULD make these failures fast and obvious:

- SUT imports evaluation module;
- full fixture/oracle object crosses SUT input;
- full simulator evaluation record crosses SUT input;
- reserved evaluation vocabulary appears in SUT-visible serialized payload;
- harness calls an expected transition selector;
- inspection mutates state.

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
- Is the rule protected by static check, contract test, negative test, review gate, or only documented as risk?
- Does the change add logs, snapshots, or traces that could later be re-ingested as SUT state?
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
- a boundary-critical rule is marked enforced but has no actual check or review gate;
- generated code creates broad DTOs or shared contracts that mix SUT and evaluation roles;
- logs, snapshots, or replay artifacts can reintroduce evaluation-only metadata into SUT behavior;
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

Generated code that creates public contracts, shared packages, fixture projections, simulator records, capture records, or inspection surfaces MUST receive explicit review before becoming non-throwaway implementation. The review must check reserved vocabulary, state-origin preservation, dependency direction, and claim boundary.

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
- What conformance ledger exists, and which rules are static, tested, review-gated, or currently unenforced?
- Which architecture conformance tool or equivalent mechanism is selected?
- What public SUT input, output, run lifecycle, and inspection seams exist?
- What record families are evaluation-only?
- How are SUT-visible fixture projections created?
- Do SUT-visible projections reject unknown and prohibited fields?
- How are SUT-visible simulator projections created?
- How are opaque SUT state handles represented without leaking fixture path identity?
- How does the SUT identify the proposal or disposition selected for simulator realization?
- How is broad retrieval/context assembly prevented?
- How is passive inspection kept read-only?
- Which negative tests protect the boundary?
- How are development traces labeled differently from formal evidence?
- How are logs, snapshots, and replay artifacts prevented from reintroducing evaluation-only metadata?
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
- Can reserved evaluation vocabulary appear in SUT-visible contract fields or serialized payloads?
- Can evaluation adapt raw communication into scoped correction/control state before SUT processing?
- Can evaluation adapt task observations into a recognition/production conclusion before SUT processing?
- Can the harness pick the proposal or disposition that gets realized?
- Can capture/reporting create the missing relation evidence after the fact?
- Can inspection mutate state or repair lineage?
- Can logs, snapshots, or replay artifacts carry evaluation-only metadata back into SUT behavior?
- Can the SUT pass by broad memory retrieval or relevance ranking?
- Can a rule be described as enforced without a static check, contract test, negative test, or explicit review gate?
- Can report text claim milestone completion before `SLICE-005` resolves?
- Can repeated exploratory runs be cherry-picked and presented as formal campaign evidence?

Any `yes` requires a fix, a bounded throwaway label, or a new decision before the work can support first-slice implementation claims.
