# Zoey Engineering Standard

Document version: `V0.3.0`

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

Active profile:

- `engineering/profiles/SCN001_SELECTED_SLICE.md` `V0.1.0`

## Purpose

This document defines the general engineering standard for non-throwaway Zoey implementation work.

It is not a product architecture, acceptance gate, scoring policy, storage design, runtime trust-boundary policy, or final repository convention. It defines:

- how engineering rules are identified;
- how accepted decisions remain authoritative;
- how implementation repositories consume governance;
- what counts as enforcement;
- the general code-health floor for non-throwaway work;
- claim boundaries that prevent engineering artifacts from being mistaken for evaluated compatibility or milestone acceptance.

Scenario-specific or milestone-specific conformance rules live in active profiles. The first active profile is `SCN001_SELECTED_SLICE`.

## Authority Model

This standard is a derivative engineering-conformance artifact. It does not create, redefine, or supersede semantic architecture decisions.

For every engineering rule:

```text
governing ADR/register/source = semantic authority
ENGINEERING_STANDARD.md = general engineering rule model and floor
active profile = scenario/milestone-specific engineering consequence
implementation repo = local enforcement mechanism and evidence
```

If this standard or an active profile conflicts with a cited governing artifact, the governing artifact wins. The affected engineering rule becomes `revalidation-required` until corrected or explicitly confirmed against the governing source.

Rule validity is source-bound. When a governing source revision changes, every rule that cites that source becomes `revalidation-required`; rules that do not cite the changed source remain valid unless the change affects them indirectly and that dependency is recorded.

## Normative Surface

The rule catalogue is the normative engineering surface. Guidance, rationale, examples, checklists, and attack catalogues support the rules; they do not create independent binding obligations unless attached to a rule ID.

Rule prefixes:

| Prefix | Rule family |
| --- | --- |
| `ENG-BASE-*` | Authority, baseline, publication, and repository consumption. |
| `ENG-HEALTH-*` | General code-health and change discipline. |
| `ENG-CONF-*` | Architecture or active-profile conformance. |
| `ENG-CLAIM-*` | Artifact labels and claim boundaries. |
| `ENG-CHANGE-*` | Open-question and decision-change triggers. |
| `ENG-AGENT-*` | Persistent coding-agent guidance and instruction-discovery controls. |

Each rule entry uses this shape:

```text
ID:
Sources:
Scope:
Rule:
Forbidden shapes:
Required checks:
Mechanisms:
Test modes:
Status:
Failure consequences:
Notes:
```

Mechanisms are how protection is implemented:

- `structural`: the design makes violation impossible or materially hard, such as separate closed input types;
- `static`: lint, dependency analysis, schema validation, type checks, or build rules;
- `automated-test`: deterministic tests, contract tests, negative tests, replay tests, or property tests;
- `manual-review`: explicit reviewer question and recorded outcome;
- `ci-gate`: automated gate in the implementation repo.

Test modes describe the test shape where applicable:

- `positive`;
- `negative`;
- `contract`;
- `interleaving`;
- `replay`;
- `property`;
- `regression`.

Status describes current coverage:

- `enforced`;
- `review-only`;
- `uncovered`;
- `revalidation-required`.

Failure consequences describe what a failure blocks:

- `merge-blocking`;
- `promotion-blocking`;
- `claim-blocking`;
- `advisory`.

Documentation creates no enforcement status by itself. A rule is manual-review enforced only when the review trigger is declared, the required review question is declared, the review outcome is recorded, and promotion cannot proceed without the required review outcome. Otherwise the rule is `uncovered`.

## Conformance Ledger

Every governed non-throwaway implementation repo keeps a conformance ledger. It may be Markdown, a test manifest, CI configuration, or another inspectable local artifact.

Minimum ledger fields:

```text
Rule ID:
Sources:
Applies To:
Mechanisms:
Test Modes:
Status:
Failure Consequences:
Local Evidence:
Residual Risk:
Owner:
Last Checked:
```

Example:

```text
Rule ID: ENG-CONF-IMPORT-001
Sources: ADR-008 R2; SCN001_SELECTED_SLICE V0.1.0
Applies To: scn001_sut_core
Mechanisms: static; manual-review
Test Modes: contract
Status: enforced
Failure Consequences: merge-blocking; claim-blocking
Local Evidence: dependency conformance check; review checklist item
Residual Risk: dynamic imports are forbidden by local policy
Owner: implementation maintainer
Last Checked: YYYY-MM-DD
```

## Governance Publication And Consumption

`Zoey/meta` owns the canonical engineering governance. Implementation repositories consume pinned projections of the applicable standard and active profiles.

The preferred publication model is:

```text
Zoey/meta
    canonical standard and profiles

governed implementation repo
    AGENTS.md
    governance/ENGINEERING_STANDARD.md
    governance/ACTIVE_PROFILE.md
    governance/ZOEY_GOVERNANCE.lock
    governance/CONFORMANCE.md
```

The local governance snapshot is not a new authority. It records exactly which canonical release, active profile, source revisions, and conformance mechanisms the repo consumes.

Do not solve governance consumption by relying on conversational memory, a developer remembering to paste rules, a sibling repository being present, or a personal global Codex instruction file. Repository-level governance must travel with the repository.

## Rule Catalogue

### ENG-BASE-001 - Source Authority

Sources: this standard; accepted Zoey ADRs and registers.

Scope: all governed non-throwaway implementation work.

Rule: implementation work preserves accepted governing sources over local convenience. If code, tests, or documentation require changing an accepted source, the change is handled as a decision update or new ADR.

Forbidden shapes:

- silently implementing a different boundary than an accepted ADR;
- hiding a decision change inside code;
- claiming conformance to a rule whose cited source has changed without revalidation.

Required checks:

- cite governing sources in the conformance ledger;
- mark affected rules `revalidation-required` when governing sources change.

Mechanisms: manual-review; static where source locks are machine-checkable.

Test modes: contract where source-lock checks exist.

Status: review-only until implemented locally.

Failure consequences: promotion-blocking; claim-blocking.

### ENG-BASE-002 - Rule-Level Revalidation

Sources: this standard.

Scope: all standard/profile releases and governed implementation repos.

Rule: rule validity is tied to cited sources. When a cited source revision changes, every rule citing it becomes `revalidation-required` until the standard/profile is reissued or the rule is explicitly confirmed unchanged.

Forbidden shapes:

- treating the whole standard as silently valid after source changes;
- treating the whole standard as invalid when only a source-bound subset needs review;
- omitting source revisions from local governance locks.

Required checks:

- local governance lock lists standard version, active profile version, and governing source revisions;
- conformance ledger can identify rules affected by source changes.

Mechanisms: structural; manual-review; static where lock files exist.

Test modes: contract where lock validation exists.

Status: review-only until implemented locally.

Failure consequences: claim-blocking.

### ENG-BASE-PUBLISH-001 - Repository Governance Projection

Sources: this standard.

Scope: every governed non-throwaway implementation repo.

Rule: each implementation repo can determine the canonical engineering-standard release it consumes, every active profile it consumes, the governing source revisions for active rules, and where local conformance mechanisms are recorded.

Forbidden shapes:

- relying on a sibling `meta` checkout for routine governance discovery;
- relying on a developer to remind Codex or reviewers about the standard;
- manually edited local governance copies that no longer identify their canonical source.

Required checks:

- local governance snapshot or lock exists before non-throwaway implementation work is promoted;
- snapshot header identifies canonical source and says local copies are derived, not authoritative.

Mechanisms: structural; manual-review; ci-gate where snapshot validation exists.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: promotion-blocking; claim-blocking.

### ENG-AGENT-001 - Persistent Agent Routing

Sources: this standard; OpenAI Codex `AGENTS.md` guidance.

Scope: implementation repos where Codex or similar coding agents perform governed work.

Rule: repository-integrated coding agents receive persistent project guidance that routes them to applicable active rules and required gates before governed changes.

Forbidden shapes:

- loading the full canonical standard as always-on agent guidance;
- relying on personal global instructions for project governance;
- requiring each prompt to restate active Zoey rules.

Required checks:

- root `AGENTS.md` or equivalent router exists in governed implementation repos;
- nested guidance exists where responsibility-specific rules differ, such as SUT and evaluation packages;
- agent guidance references local governance snapshots and conformance ledgers.

Mechanisms: structural; manual-review.

Test modes: contract where instruction-discovery checks exist.

Status: review-only until implemented locally.

Failure consequences: promotion-blocking.

### ENG-AGENT-002 - Instruction Override Control

Sources: this standard; OpenAI Codex `AGENTS.md` discovery behavior.

Scope: governed repos that use Codex instruction files.

Rule: committed instruction overrides do not silently weaken active engineering rules.

Forbidden shapes:

- committing `AGENTS.override.md` on protected non-throwaway branches without an explicit engineering exception;
- using an override to bypass a root or nested governance router;
- introducing alternate instruction filenames that hide required Zoey guidance.

Required checks:

- review or CI flags committed `AGENTS.override.md`;
- any authorized override records scope, reason, expiry, and rules it may not weaken.

Mechanisms: static; ci-gate; manual-review.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; promotion-blocking.

### ENG-HEALTH-CHANGE-001 - Focused Change

Sources: this standard; Google Engineering Practices.

Scope: all non-throwaway implementation changes.

Rule: each change has one primary purpose and is small enough for direct review.

Forbidden shapes:

- mixing behavior change, broad refactor, generated structure, and conformance change without an explicit split rationale;
- hiding semantic changes inside formatting, renames, or cleanup.

Required checks:

- review identifies primary purpose;
- broad changes record why splitting would be riskier than combining.

Mechanisms: manual-review.

Test modes: none.

Status: review-only until implemented locally.

Failure consequences: merge-blocking or promotion-blocking.

### ENG-HEALTH-TEST-001 - Behavior-Change Test Obligation

Sources: this standard; Google Engineering Practices.

Scope: non-throwaway behavior changes and bug fixes.

Rule: behavior changes add or update tests that fail without the change. Bug fixes include regression tests unless the failure is not reproducible in the implementation test harness or is purely editorial/build-environment-specific.

Forbidden shapes:

- changing behavior with only final-output smoke tests where boundary, state, or claim behavior is affected;
- skipping a regression test without recording the exception.

Required checks:

- test evidence or recorded exception appears in the change review.

Mechanisms: automated-test; manual-review; ci-gate.

Test modes: positive; negative; regression.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; promotion-blocking.

### ENG-HEALTH-API-001 - Minimal Public API

Sources: this standard.

Scope: all public implementation APIs, especially SUT public boundaries.

Rule: public API is minimal by default. Code is not made public solely to make tests, fixtures, or evaluation setup easier.

Forbidden shapes:

- exporting internal transition functions to let the harness or tests drive hidden semantics;
- making private state mutation public to simplify setup;
- expanding selected-slice public boundary without a governing decision or rule.

Required checks:

- public API additions identify their governing source and consumer;
- tests use local/internal seams rather than broadening the selected-slice public boundary.

Mechanisms: manual-review; static where export boundaries can be checked.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; claim-blocking where behavior evidence depends on the expanded API.

### ENG-HEALTH-ABSTRACTION-001 - Current Justification For Abstractions

Sources: this standard; ADR-001 generalization caution.

Scope: non-throwaway implementation abstractions and shared helpers.

Rule: new abstractions require current justification: repeated concrete pressure, an accepted boundary or contract obligation, testability or conformance need, or an accepted ADR/working assumption. Anticipated future Zoey scope alone is insufficient.

Forbidden shapes:

- broad `engine`, `manager`, `context`, `memory`, `shared`, `common`, or `utils` modules without a one-sentence responsibility;
- abstractions that hide SUT/evaluation ownership or state origin.

Required checks:

- review can state the abstraction responsibility and current justification.

Mechanisms: manual-review.

Test modes: none.

Status: review-only until implemented locally.

Failure consequences: merge-blocking or advisory, depending on risk.

### ENG-HEALTH-DEAD-001 - Dead Code And Throwaway Promotion

Sources: this standard.

Scope: non-throwaway implementation code and throwaway artifacts.

Rule: dead code is deleted rather than commented out. Throwaway artifacts receive no conformance credit, and promotion into non-throwaway implementation requires normal review and conformance as if newly introduced.

Forbidden shapes:

- non-throwaway code importing throwaway code;
- commented-out implementation bodies retained as pseudo-history;
- prototype code promoted without conformance review.

Required checks:

- review flags throwaway imports and commented-out dead code;
- promotion review applies active rules and tests.

Mechanisms: manual-review; static where throwaway paths are declared.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; promotion-blocking.

### ENG-HEALTH-TODO-001 - Tracked TODO Identity

Sources: this standard.

Scope: TODOs in non-throwaway code.

Rule: TODOs reference a tracked issue, open-question ID, ADR trigger/reconsideration, or stable implementation follow-up ID. A prose reason may accompany the ID but cannot replace it.

Forbidden shapes:

- `TODO: fix later`;
- `TODO: temporary`;
- architecture-bearing TODOs with no owner, trigger, or follow-up identity.

Required checks:

- review flags untracked TODOs in non-throwaway code.

Mechanisms: manual-review; static where TODO scanning exists.

Test modes: none.

Status: review-only until implemented locally.

Failure consequences: merge-blocking or promotion-blocking.

### ENG-HEALTH-COMMENT-001 - Useful Comment Discipline

Sources: this standard.

Scope: comments in non-throwaway code.

Rule: comments explain why, invariants, non-obvious limitations, accepted trade-offs, or consequences of change. Comments do not narrate obvious syntax or duplicate implementation.

Forbidden shapes:

- generated comments such as "loop through items" for obvious code;
- comments that assert conformance without evidence;
- stale comments that contradict active rules.

Required checks:

- review removes or corrects misleading or low-value comments.

Mechanisms: manual-review.

Test modes: none.

Status: review-only until implemented locally.

Failure consequences: advisory or merge-blocking when comments affect claims or conformance.

### ENG-HEALTH-GEN-001 - Generated Artifact Review

Sources: this standard.

Scope: AI-generated or tool-generated code, schemas, tests, docs, and project structure.

Rule: generated artifacts are not authoritative and are reviewed before becoming non-throwaway implementation.

Forbidden shapes:

- generated shared DTOs that mix SUT and evaluation fields;
- generated public contracts that become the first authority for ownership boundaries;
- generated documentation that overclaims acceptance, compatibility, or production readiness.

Required checks:

- generated public contracts, shared packages, fixture projections, simulator records, capture records, and inspection surfaces receive explicit review.

Mechanisms: manual-review; automated-test where applicable.

Test modes: contract; negative.

Status: review-only until implemented locally.

Failure consequences: merge-blocking; promotion-blocking.

### ENG-CLAIM-001 - Claim Domain Separation

Sources: `OPEN_QUESTIONS.md` `V0.2.17`; this standard.

Scope: docs, tests, reports, traces, demos, README text, and review language.

Rule: engineering conformance, evaluated behavioral compatibility, and milestone acceptance are separate claim domains.

Forbidden shapes:

- presenting engineering conformance as evaluated behavioral compatibility;
- presenting development traces or conformance tests as formal evaluation evidence;
- claiming milestone acceptance before the applicable acceptance question resolves.

Required checks:

- artifact labels and documentation use claim language that matches their domain;
- compatibility claims trigger the relevant evaluation-record metadata question.

Mechanisms: manual-review; static/docs checks where practical.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: claim-blocking; promotion-blocking.

### ENG-CLAIM-002 - Formal Evaluation Artifact Reservation

Sources: `OPEN_QUESTIONS.md` `V0.2.17`; `ADR-004 R3`; `ADR-005 R2`.

Scope: evaluation records, reports, comparisons, and scoring language.

Rule: formal evaluation artifacts remain inactive/reserved until their governing open questions and record contracts resolve. Development artifacts and engineering conformance results are not promoted, copied, renamed, or described as formal evaluation evidence.

Forbidden shapes:

- `formal_campaign_record`, `pass_evidence`, `accepted_slice`, `milestone_complete`, or equivalent labels before governing decisions allow them;
- using internal scoring-related evaluation package data to imply final scoreability.

Required checks:

- reports and docs distinguish development artifact, engineering conformance result, and formal evaluation artifact.

Mechanisms: manual-review; static/docs checks where practical.

Test modes: contract.

Status: review-only until implemented locally.

Failure consequences: claim-blocking.

### ENG-CHANGE-001 - Open Question Trigger Discipline

Sources: `OPEN_QUESTIONS.md` `V0.2.17`; this standard.

Scope: implementation work that crosses unresolved governance frontiers.

Rule: implementation stops and re-triages the relevant open question before the first non-throwaway use or claim that depends on an unresolved control.

Forbidden shapes:

- implementing production memory, retrieval, trust-boundary routing, final scoreability, formal evaluation-record metadata, product surfaces, or continuity claims under selected-slice assumptions;
- burying an open-question trigger inside code.

Required checks:

- review asks whether the change triggers `SLICE-005`, `EVAL-004`, `EVAL-005`, `DEP-003`, `MEM-*`, `TRUST-*`, `PROD-*`, `SURF-*`, `CONT-*`, or `LEG-*`.

Mechanisms: manual-review.

Test modes: none.

Status: review-only until implemented locally.

Failure consequences: promotion-blocking; claim-blocking.

## External References

These references inform the engineering shape. Zoey governing documents remain authoritative.

- NIST SP 800-218, Secure Software Development Framework: <https://csrc.nist.gov/pubs/sp/800/218/final>
- Google Engineering Practices, Code Review Standard: <https://google.github.io/eng-practices/review/reviewer/standard.html>
- Google Engineering Practices, Small CLs: <https://google.github.io/eng-practices/review/developer/small-cls.html>
- OWASP SAMM Policy And Compliance: <https://owaspsamm.org/model/governance/policy-and-compliance/>
- OpenAI Codex AGENTS.md guidance: <https://learn.chatgpt.com/docs/agent-configuration/agents-md>
- OpenAI Codex customization and skills: <https://learn.chatgpt.com/docs/customization/overview>
