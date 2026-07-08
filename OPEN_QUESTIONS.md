# Zoey Open Questions

Document version: `V0.2.14`

Thesis baseline: `SYSTEM_THESIS.md` `V0.3.1`

Scenario baseline: `CANONICAL_SCENARIOS.md` `V0.2.2`

State/control baseline: `STATE_AND_CONTROL_MODEL.md` `V0.4.1`

## Purpose

This file is Zoey's decision register for unresolved questions that materially affect architecture, repository split, evaluation readiness, implementation order, governance, or product shape.

It is not a backlog, wishlist, architecture document, or place to restate settled principles. Its job is to keep uncertainty explicit without letting every unresolved question block the current milestone.

Core rule:

```text
Question exists
    != question is active

Question is important
    != question blocks current work

Question affects future architecture
    != architecture must be decided now
```

## Register Semantics

### Status

- `Active`: blocks the current decision frontier.
- `Open`: trigger has occurred and the question remains unresolved, but it does not currently block the frontier.
- `Deferred`: real question, but its trigger has not occurred.
- `Blocked`: cannot be answered until another question or artifact is resolved.
- `Resolved`: answered elsewhere; this register keeps the ID, outcome, decision authority, and resolution artifact only.

Terminal resolved outcomes include `Decision`, `Bounded exclusion`, `Superseded`, `Merged`, and `Obsolete`.

### ID Rules

Canonical ID stability begins with `OPEN_QUESTIONS.md V0.2.0`. `V0.1.0` was a pre-register drafting version; historical references to `V0.1.0` IDs must include that document version.

From `V0.2.0` onward, question IDs are permanent. Do not reuse an ID after resolution, merge, or deletion. Material reframing that changes a question's closure condition, blocking scope, or decision target requires a new ID. Wording may be tightened under the same ID only when the underlying decision remains materially the same.

When questions merge, each source ID retains a resolved tombstone pointing to the surviving or newly created question. A merge must not silently reuse one existing ID for a materially broader question.

### Resolution Rules

A proposed answer or draft resolution artifact does not by itself make a question `Resolved`. Resolution requires acceptance through the decision authority appropriate to the question.

AI-generated analysis, ADR drafts, experiments, or recommendations may provide evidence or resolution candidates but do not autonomously close strategic, governance, product, or user-control questions.

A question may be closed by:

- an accepted ADR, schema contract, evaluation fixture, migration inventory, surface contract, product decision, or governance rule;
- an explicit bounded exclusion, such as "not supported in this slice";
- a narrower question that replaces a broad one.

A bounded exclusion may close a question for a named milestone only by narrowing that milestone's supported capability and acceptance claim. Excluding a behavior required by a canonical scenario does not remove the scenario obligation or permit full scenario-pass evidence. The exclusion and resulting claim boundary must be reflected in the milestone acceptance artifact.

A bounded-exclusion resolution must name the milestone or capability scope it excludes and the trigger that requires a new linked question if the excluded capability later enters scope. Resolved IDs are not reopened; later scope creates a new ID linked to the earlier exclusion.

A bounded working assumption may allow an experiment, fixture, or slice to proceed while the underlying question remains `Open`. The assumption must identify its scope, the evidence or fixture that supplies it, the claims it supports, the claims it does not support, and the trigger that invalidates or replaces it. Evidence or compatibility claims dependent on a bounded assumption must identify that assumption.

A working assumption is not a question resolution. It has its own lifecycle and must not be listed as a terminal resolved outcome for the source question.

Resolved answers move to the authoritative artifact. This file retains only traceability.

### Baseline Re-Triage

If `SYSTEM_THESIS.md`, `CANONICAL_SCENARIOS.md`, or `STATE_AND_CONTROL_MODEL.md` changes materially, affected open questions must be re-triaged. A baseline change may activate, defer, split, merge, or resolve questions as obsolete, superseded, or merged where appropriate.

If a question resolution, bounded exclusion, working assumption, or authoritative resolution artifact materially changes, is superseded, or is invalidated, dependent questions and claims must be re-triaged. The earlier ID remains historical; if the changed basis creates a new unresolved decision, create a new linked question rather than rewriting the old decision.

Question dependency cycles must not deadlock the register. If active or blocked questions mutually depend on one another, the cycle must be narrowed, split, jointly bounded, or carried under explicit working assumptions before it can support a milestone claim.

The Open Question Index is authoritative for question status, trigger, dependency, and source-pressure metadata. The Active Decision Frontier is a derived working view of the current milestone. Detailed active entries expand the index but must not redefine status independently.

### Source Tags

- `T`: `SYSTEM_THESIS.md`
- `S1`: `SCN-001`
- `S2`: `SCN-002`
- `SCM`: `STATE_AND_CONTROL_MODEL.md`
- `LEG`: legacy project evidence
- `PROD`: product workflow pressure
- `TRUST`: inference/runtime trust-boundary pressure
- `CONT`: continuity and recovery pressure

## Entry Format

Detailed active entries use this shape:

- `Status`
- `Question`
- `Why It Matters`
- `Source / Pressure`
- `Blocks`
- `Does Not Block`
- `Depends On`
- `Applies When / Decision Trigger`
- `Known Options`
- `Decision Criteria`
- `Evidence Needed`
- `Working Assumptions / Fixtures`
- `Decision Authority`
- `Needed By`
- `Resolution Shape`

Known options are candidate resolution shapes, not automatically exhaustive or endorsed. A question may declare a closed option set only when the source constraint genuinely limits the choice.

`Evidence Needed` must name inspectable observations, artifacts, experiments, comparisons, or fixture facts capable of informing closure. It must not merely restate the question or decision criteria.

Deferred and blocked questions may stay in compact index form until their trigger fires.

Working assumptions use stable `ASM-*` IDs and this shape:

- `ID`
- `Status`: `Active`, `Superseded`, `Invalidated`, or `Expired`
- `Related Question(s)`
- `Scope / Milestone`
- `Assumption`
- `Fixture Or Evidence Basis`
- `Supports These Claims`
- `Does Not Support`
- `Invalidation / Replacement Trigger`
- `Decision Authority / Accepted By`
- `Resolution Artifact`
- `Date`

## Inclusion Rules

- Prefer narrow, closeable questions over broad topics.
- Tie each question to a blocked decision or concrete artifact.
- Preserve source pressure without restating the source document.
- Declare the trigger that makes the question active.
- For questions governing a capability, durable state transition, external operation, derived artifact, user-facing exposure, or compatibility claim, trigger before the first non-throwaway use or claim that depends on the unresolved control.
- Allow bounded exclusions when a capability is not part of the current slice.
- Merge or link duplicates instead of multiplying entries.

## Exclusion Rules

Do not include:

- restatements of settled thesis, scenario, or state/control principles;
- philosophical questions about consciousness, personhood, aliveness, or companionship;
- wishlists without architecture, governance, eval, repo, or workflow impact;
- technology picks unless the question is about the selection criterion;
- vague risks such as "memory could be dangerous";
- final answers disguised as questions;
- questions that preserve Iris or Yuki as continuing identity-bearing systems.

## Active Decision Frontier

Current milestone: define the minimum selected-slice state required by the accepted `SCN-001` first-milestone boundary, trial/time contract, evaluation policy, and fixture/oracle contract.

Active questions:

- `SLICE-002`

Pending re-triage queue after the current active frontier is resolved:

- `SLICE-005`
- `EVAL-004`
- `EVAL-005`
- selected-slice trigger checks for `MEM`, `DEP`, `GROW`, `AUTH`, `SURF`, `INIT`, `PROD`, `LEG`, `TRUST`, and `CONT`.

`EVAL-001` and `EVAL-003` are resolved by accepted `ADR-004 R3`. The first `SCN-001` milestone uses harness-curated fixture context, excludes retrieval/context-assembly claims, and accepts nondeterministic runs only through formal milestone campaigns with hard invariant gates, bounded variance, outcome-independent run selection, claim-class aggregation, and run-validity controls.

`EVAL-002` is resolved by accepted `ADR-005 R2`. The first `SCN-001` milestone has a selected-slice fixture/oracle contract with canonical and counterfactual paths, decision-point bundles, simulator realization facts, oracle-visible fields, formal run validity, claim-class scoring, rule IDs, and bounded claim language.

`GROW-001` and `TIME-002` are resolved by accepted `ADR-003`. `TIME-001` remains deferred for scheduler, reminder, due-state, expiry, background temporal-maintenance, and full longitudinal-clock semantics.

`SLICE-002` is active because the fixture/oracle contract now defines the oracle-visible semantic responsibilities that the implementation must support without turning every oracle field into independently persisted state.

`SLICE-005`, `EVAL-004`, and `EVAL-005` have been re-triaged after `ADR-005` acceptance and remain non-active until their concrete triggers occur. `SLICE-005` waits for minimum selected-slice state. `EVAL-004` triggers before the first evaluation record, comparison, or compatibility claim. `EVAL-005` triggers before final scoring or scenario-scoreability criteria are defined.

No other open question currently blocks progress. Legacy reading, non-committing experiments, document review, fixture sketching, and rough implementation exploration may continue as long as they do not claim final architecture compatibility, selected-slice pass evidence, first evaluation-record sufficiency, or final acceptance-gate sufficiency.

## Active Questions

### SLICE-002

Status: `Active`

Question: What minimum persistent, derived, and inspection-only state is required for the selected slice?

Why It Matters: Accepted `ADR-005` defines what the selected-slice fixture and oracle must inspect, but explicitly does not decide which oracle-visible facts must be independently persisted. The next artifact must identify the minimum implementation state needed to satisfy the selected semantic transitions without copying the oracle checklist into a database schema.

Source / Pressure: `STATE_AND_CONTROL_MODEL.md`; `CANONICAL_SCENARIOS.md` `SCN-001`; `ADR-001`; `ADR-002`; `ADR-003`; `ADR-004`; `ADR-005`.

Blocks: `SLICE-003` minimum internal boundary, `DEP-001` dependency identity metadata, `SLICE-005` acceptance gate, and any implementation claim that the selected-slice state contract satisfies `ADR-005`.

Does Not Block: thesis/scenario/state-model review, legacy inventory, non-committing prototypes, evaluation-record sketching, acceptance-gate sketching, document review, or explicitly throwaway experiments that do not claim final selected-slice state sufficiency.

Depends On: `SLICE-001`, resolved by `ADR-001`; `EVAL-006`, resolved by `ADR-002`; `GROW-001` and `TIME-002`, resolved by `ADR-003`; `EVAL-001` and `EVAL-003`, resolved by `ADR-004`; `EVAL-002`, resolved by `ADR-005`.

Applies When / Decision Trigger: `ADR-005` is accepted and the next artifact would define implementation state, persistence boundaries, derived-state rules, state inspection projections, or internal semantic records for the first `SCN-001` selected slice.

Known Options:

- Minimal retained semantic state plus derived oracle projections: persist only state whose identity or later use matters, derive other oracle-visible facts from event/state lineage.
- Direct oracle-field persistence: store each oracle-visible field as persistent state, simpler to inspect but likely overfits implementation architecture to the evaluation contract.
- Event-sourced transition log with projections: retain transition evidence and derive current semantic state, higher rigor but potentially more machinery than the first slice needs.
- Ephemeral state only: acceptable for throwaway exploration, but insufficient for retained active-trial and later-use obligations under `ADR-005`.

Decision Criteria:

- preserves the SUT-owned semantic distinctions required by `ADR-002`, `ADR-003`, and `ADR-005` without requiring a final production schema;
- distinguishes independently persisted state, lineage-preserving projections, derived inspection facts, and transient run-only artifacts;
- keeps active trial identity, proposal binding, activation checks, direct correction, later-use applicability, outcome lineage, and explanation support inspectable enough for `ADR-005`;
- avoids turning evaluator-only annotations, fixture controls, or oracle result vectors into SUT-owned semantic state;
- excludes retrieval, broad context assembly, durable developmental adaptation, real voice/avatar, production memory custody, and full `SCN-001` claims;
- is small enough to implement as the first selected slice while leaving `SLICE-003`, `DEP-001`, `EVAL-004`, and `SLICE-005` for their proper triggers.

Evidence Needed:

- state responsibility table separating persisted state, derived/projection state, fixture-supplied facts, simulator realization records, oracle-only classifications, and transient run artifacts;
- minimum retained records or equivalent lineage for attributed assertions, temporal eligibility, scoped comparison, trial candidates, proposal bindings, activation checks, active trials, direct correction dispositions, realization refs, outcome records, and explanation support;
- mapping from each `ADR-005` oracle-visible field family to required persistence, derivability, or inspection-only status;
- lifecycle and identity rules for retained trial candidates and active trials across the selected synthetic trajectory;
- examples of what must not be persisted as SUT-owned state, including fixture answer keys, evaluator annotations, claim-class result vectors, and global user/profile conclusions;
- compatibility argument showing the minimum state supports `SCN001-SSFO-V0.2.0` without claiming retrieval/context assembly or durable adaptation.

Working Assumptions / Fixtures: `ADR-001` through `ADR-005` are accepted; first-slice state is synthetic fixture state; oracle-visible does not automatically mean independently persisted; no real retrieval, production context assembly, real personal continuity, real voice/avatar behavior, Japanese pedagogy quality, durable developmental adaptation, statistical reliability, longitudinal drift handling, or full `SCN-001` pass is claimed.

Decision Authority: project owner.

Needed By: before `SLICE-003`, `DEP-001`, `SLICE-005`, and implementation claims of selected-slice state sufficiency.

Resolution Shape: selected-slice minimum-state contract or short ADR.

## Open Question Index

| ID | Status | Trigger | Depends On | Source | Question |
| --- | --- | --- | --- | --- | --- |
| `SLICE-001` | Resolved | Accepted by `ADR-001` | - | S1, S2, SCM | Choose first vertical slice: `SCN-001` or `SCN-002`. |
| `SLICE-002` | Active | After `EVAL-001`, `EVAL-002`, `EVAL-003`, and accepted first-milestone boundary/trial/time/evaluation semantics are known | `SLICE-001`, `EVAL-006`, `EVAL-001`, `EVAL-002`, `EVAL-003`, `GROW-001`, `TIME-002` | SCM, S1, S2 | What minimum persistent state is required for the selected slice? |
| `SLICE-003` | Blocked | After selected-slice state/eval pressure is known | `SLICE-002`, `DEP-001`, `EVAL-002`, `EVAL-006` | SCM | What minimum internal boundary is forced by selected-slice behavior? |
| `SLICE-005` | Blocked | After selected-slice oracle, system-under-test boundary, trial/time semantics, and acceptance semantics are known | `EVAL-002`, `EVAL-003`, `EVAL-006`, `GROW-001`, `TIME-002` | S1, S2 | What acceptance gate says the first slice is done? |
| `MEM-001` | Deferred | Selected slice proposes retaining personal state | `SLICE-001` | T, SCM | What retention bases and transient defaults does the selected slice need? |
| `MEM-002` | Deferred | Selected slice proposes reusing retained state across purposes | `MEM-001` | T, SCM | What permitted-use rule prevents silent repurposing into personalization, initiative, adaptation, training, or external inference? |
| `MEM-003` | Deferred | Selected slice proposes retaining personal evidence | `MEM-001` | SCM | What granularity rule chooses raw content, excerpt, structured observation, or summary? |
| `MEM-004` | Deferred | Selected slice proposes creating or reusing a control-relevant derived artifact | `MEM-001`, `MEM-002` | SCM | What common minimum lineage and permitted-use contract must any control-relevant derived artifact satisfy, and what extension is required for the first artifact type introduced? |
| `MEM-005` | Deferred | A milestone proposes exposing user-facing memory or retained-state correction controls | `MEM-001` | T, SCM | What user-visible distinctions are required between correction, revocation, deletion, forgetting, redaction, retirement, and supersession? |
| `DEP-001` | Blocked | After `SLICE-002` identifies selected state/transitions | `SLICE-002` | SCM | What minimum dependency identity metadata does the selected slice require? |
| `DEP-002` | Deferred | Selected slice can produce insufficient non-circular support or non-convergence | `DEP-001` | SCM | What minimum V0 detection condition identifies insufficient non-circular support or control non-convergence, and how does the affected domain select lifecycle state? |
| `DEP-003` | Blocked | After selected state/dependency types are known | `DEP-001` | SCM | Which runtime maintenance triggers are required: expiry, revocation, capability degradation, external refresh, or manual review? |
| `DEP-004` | Deferred | Selected slice has component operations or grouped state | `SLICE-002` | S2, SCM | What component/group status model is required without building a full workflow engine? |
| `TIME-001` | Deferred | Scheduler, reminders, due state, expiry, background temporal maintenance, or full longitudinal governed-clock semantics enter active milestone scope | `SLICE-001` | S1, S2, SCM | What governed-clock contract is needed for reproducible expiry, freshness, due state, and longitudinal time? |
| `TIME-002` | Resolved | Accepted by `ADR-003` Decision B | `EVAL-006` | S1, S2, SCM | What minimal selected-slice chronology and staleness contract supports stale-history handling, trial-basis freshness, and later-session ordering without designing a general governed-clock system? |
| `GROW-001` | Resolved | Accepted by `ADR-003` Decision A | `EVAL-006` | S1, SCM | What selected-slice minimum criteria distinguish situational behavior, trial candidate, active scoped behavioral trial, and unsupported durable developmental adaptation? |
| `GROW-002` | Deferred | `SCN-001` longitudinal eval enters milestone scope | `GROW-001`, `EVAL-002` | S1, T | What trajectory signals detect anti-correction or agreement drift without a full personality model? |
| `GROW-003` | Deferred | Behavior-affecting replacement is proposed | - | T, SCM | What continuity reference must exist before evaluating model, runtime, prompt, specialist, or context-policy change? |
| `GROW-004` | Deferred | Continuity evaluation work begins | `GROW-003` | T, SCM | What evidence lets valid developmental behavior enter established Zoey continuity? |
| `GROW-005` | Deferred | User-facing durable adaptation is proposed | `GROW-001` | T, SCM, PROD | What inspection and correction path is required before durable cross-session adaptations are enabled? |
| `INIT-001` | Deferred | Proactivity enters slice scope | `SLICE-001` | T, SCM | Which initiative candidate classes are allowed in V0? |
| `INIT-002` | Deferred | Selected design can place multiple initiative candidates into competing disposition | `INIT-001` | T, SCM, PROD | What set-level attention policy arbitrates distinct worthwhile candidates? |
| `INIT-003` | Resolved | Merged into `INIT-001` and selected-slice scope decisions | `INIT-001` | T, SCM | Which proactive behaviors are explicitly unsupported in the selected slice? |
| `AUTH-001` | Deferred | `SCN-002` selected | `SLICE-001` | S2, SCM | What actor-assurance event is sufficient for the selected private calendar fixture? |
| `AUTH-002` | Deferred | `SCN-002` selected and operation transitions are known | `AUTH-001`, `EVAL-002` | S2, SCM | Which selected operation transitions require proposal, confirmation, or fresh authorization after material change? |
| `AUTH-003` | Deferred | Standing authority is proposed for an active milestone | `AUTH-002` | S2, SCM | Is standing authority supported in this slice, and if so with what scope, review, expiry, and revocation fields? |
| `AUTH-004` | Deferred | `SCN-002` or operation lifecycle enters scope | `AUTH-002` | S2, SCM | How does revocation propagate through operation lifecycle states introduced by the slice? |
| `AUTH-005` | Deferred | Selected operation slice requires accountable operation history | `AUTH-002` | S2, SCM | What minimum operation accountability record is required without deciding final audit storage? |
| `AUTH-006` | Deferred | Content analysis or code/document review enters active milestone scope | - | T, SCM, PROD | What input/event representation distinguishes user-directed instructions from quoted, pasted, forwarded, or analyzed content? |
| `SURF-001` | Deferred | Second surface is planned | `SLICE-001` | T, SCM | What surface contract preserves identity, authority, disclosure, state updates, and uncertainty reporting? |
| `SURF-002` | Deferred | Voice slice selected | `SURF-001`, `AUTH-001` | S2, SCM, PROD | Which console/voice differences are governed behavior rather than UI detail? |
| `SURF-003` | Resolved | Obsolete as standalone scope prompt; future embodiment proposals create concrete questions | `SURF-001` | T, SCM, PROD | Which embodiment questions are unsupported until surface contracts are stable? |
| `EVAL-001` | Resolved | Accepted by `ADR-004` Decision A | `SLICE-001`, `EVAL-006`, `GROW-001`, `TIME-002` | S1, S2, SCM | Does the first slice test context discovery, or does the harness inject curated context? |
| `EVAL-002` | Resolved | Accepted by `ADR-005 R2` | `SLICE-001`, `EVAL-006`, `EVAL-001`, `EVAL-003`, `GROW-001`, `TIME-002` | S1, S2, SCM | What fixture and oracle data must the selected scenario expose without requiring hidden chain-of-thought? |
| `EVAL-003` | Resolved | Accepted by `ADR-004` Decision B | `SLICE-001`, `EVAL-006`, `GROW-001`, `TIME-002` | S1, S2 | How are nondeterministic runs accepted, and which invariant failures are hard failures? |
| `EVAL-004` | Deferred | The selected slice is preparing its first evaluation record, comparison, or compatibility claim | `EVAL-002`, `EVAL-003`, `EVAL-006` | S1, S2, SCM | What behavior-configuration metadata must each evaluation record include? |
| `EVAL-005` | Deferred | The selected slice is preparing to define scoring or claim scenario scoreability | `EVAL-002`, `EVAL-003`, `EVAL-006` | S1, S2 | For the selected slice and declared system-under-test boundary, which unresolved questions affect specific pass criteria, and which may be carried as identified fixture assumptions without strengthening the evaluation claim? |
| `EVAL-006` | Resolved | Accepted by `ADR-002` | `SLICE-001` | S1, S2, SCM | What is inside the system-under-test boundary for the selected slice, and which semantic inputs, control facts, time events, actor-assurance facts, external-system behavior, or cognitive candidates are supplied by the harness or simulated dependencies? |
| `LEG-001` | Deferred | Migration inventory starts | `SLICE-001` | T, LEG | Which legacy directories are migration candidates, reference-only, archive-only, or out of scope? |
| `LEG-002` | Deferred | Legacy component reuse is considered | `LEG-001` | T, LEG | What criteria reject or rewrite legacy material that encodes Iris/Yuki identity or authority assumptions? |
| `LEG-003` | Deferred | Selected slice needs legacy help | `SLICE-001`, `LEG-002` | T, LEG | For the selected slice's required responsibilities, which concrete legacy components or patterns may be reused or adapted under Zoey rules, and which remain reference-only? |
| `LEG-004` | Deferred | A milestone proposes migrating or incorporating legacy material into Zoey | `LEG-002` | T, LEG | What provenance must migrated legacy material retain without making Iris/Yuki ongoing authorities? |
| `LEG-005` | Blocked | After `SLICE-001` and actual legacy dependency is identified | `SLICE-001`, `LEG-001` | LEG | Which legacy extraction decisions block the selected slice, and which can wait? |
| `PROD-001` | Deferred | User-facing surface is planned | `SLICE-001` | T, PROD | Which V0 workflows are product scope rather than internal harness behavior? |
| `PROD-002` | Deferred | First user-facing state domain is planned | `PROD-001` | T, SCM, PROD | For the first user-facing state domain introduced, what minimum inspection and correction actions are required before exposure? |
| `PROD-003` | Deferred | Voice or presence demo is planned | `SURF-001` | S2, SCM, PROD | What private/shared controls are required before exposing personal context through voice or presence? |
| `PROD-004` | Resolved | Merged into `PROD-001` product-scope decision | `PROD-001` | T, PROD | Which tempting product features are explicitly out of scope for V0? |
| `PROD-005` | Deferred | Selected workflow proposes promoting Zoey-generated planning structure into active project state | `PROD-001` | SCM, PROD | What evidence promotes Zoey-generated plans/tasks into accepted active project state? |
| `CONT-001` | Deferred | A milestone intends to claim continuity across restore, migration, disconnection, or state loss | - | SCM | What minimum restore-gap handling is required before claiming continuity after state loss or migration? |
| `CONT-002` | Deferred | Selected milestone proposes retaining real authoritative personal state or durable personal history as Zoey continuity rather than disposable fixture/test state | - | T, SCM, CONT | What minimum user-controlled custody and recoverability evidence is required before the milestone may treat retained state as durable Zoey continuity? |
| `TRUST-001` | Deferred | Selected slice proposes sending personal or retained semantic state to an inference runtime, model, service, or process across a materially different trust boundary | `EVAL-006`, `MEM-002` | T, SCM, TRUST | What trust-boundary and destination-use policy governs which selected-slice state may enter each inference or processing destination? |

## Category Guide

| Category | Use For | Do Not Use For |
| --- | --- | --- |
| Memory | Retention basis, permitted use, forgetting, granularity, derived artifacts. | Generic memory philosophy or storage-engine choices. |
| Dependency And Time | Dependency identity, maintenance triggers, cycles, governed clock, grouped status. | Full transaction, lock, or event-sourcing design. |
| Growth And Behavioral Continuity | Posture/trial/adaptation criteria, drift detection, model/runtime continuity references. | Restore gaps or migration continuity recovery. |
| Continuity And Recovery | Restore gaps, migration gaps, state-loss uncertainty, reconciliation, scoped degraded continuity. | Behavioral drift caused by model/runtime replacement. |
| Initiative | Proactive classes, attention cost, batching, deferred proactivity. | Reminder wishlists. |
| Authority And Operations | Actor assurance, confirmation, revocation, standing grants, audit. | Broad autonomy ambitions. |
| Surfaces | Console/voice/avatar contracts, disclosure, confirmation, handoff. | UI polish or avatar lore. |
| Evaluation | Scenario fixtures, oracle data, nondeterminism, metadata, scoreability. | Demo scripts without pass/fail criteria. |
| Legacy | Extraction, rewrite/archive decisions, provenance, selected-slice blockers. | Preserving Iris/Yuki as active authorities. |
| Trust Boundaries And Inference | Inference destinations, runtime trust boundaries, external processing, destination-use limits. | General model selection or performance preferences. |
| Product | User-facing workflows, inspection UX, privacy controls, V0 non-scope. | Marketing, wishlists, or visual design. |

## Working Assumption Index

No active working assumptions yet.

When a working assumption is accepted, add:

```text
ID:
Status:
Related Question(s):
Scope / Milestone:
Assumption:
Fixture Or Evidence Basis:
Supports These Claims:
Does Not Support:
Invalidation / Replacement Trigger:
Decision Authority / Accepted By:
Resolution Artifact:
Date:
```

## Resolved Question Index

### SLICE-001

Outcome: `Decision`

Decision Authority / Accepted By: project owner by accepting `ADR-001`.

Resolution Artifact: `decisions/ADR-001-first-vertical-slice.md`.

Resolved Against / Scope: first vertical-slice pressure path selects `SCN-001 V0.2.2: Japanese Longitudinal Development` as the canonical pressure path for Zoey's first vertical-slice implementation sequence.

Supersedes / Split From: none.

Future Trigger: materially new first-slice selection pressure or accepted supersession of `ADR-001`; second-slice sequencing remains a separate future decision.

Date: 2026-07-07

### EVAL-006

Outcome: `Decision`

Decision Authority / Accepted By: project owner by accepting `ADR-002`.

Resolution Artifact: `decisions/ADR-002-scn001-system-under-test-boundary.md`.

Resolved Against / Scope: first `SCN-001` milestone uses a transition-inside system-under-test boundary. The harness supplies bounded fixture events, chronology, task facts, user feedback, and simulated dependencies; the SUT owns the selected semantic transitions enumerated by `ADR-002 R2`.

Supersedes / Split From: none.

Future Trigger: material change to the accepted first-slice SUT boundary, inability of `EVAL-001`, `EVAL-002`, `GROW-001`, `TIME-002`, or `SLICE-005` to preserve the accepted boundary, or a later milestone claiming broader `SCN-001` evidence than `ADR-002` permits.

Date: 2026-07-07

### GROW-001

Outcome: `Decision`

Decision Authority / Accepted By: project owner by accepting `ADR-003`.

Resolution Artifact: `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md`, Decision A.

Resolved Against / Scope: first `SCN-001` milestone supports scoped, reversible selected-slice behavioral trials only. It defines minimum distinctions for direct situational correction, trial candidate, candidate-bound proposal where applicable, active scoped trial, later-use applicability, non-activation dispositions, and unsupported durable developmental adaptation. Durable developmental adaptation remains unsupported for the first milestone.

Supersedes / Split From: none.

Future Trigger: material change to selected-slice trial semantics, a future milestone claiming durable developmental adaptation, broader trial generalization, user-facing durable adaptation, or inability of `EVAL-002`, `SLICE-002`, or `SLICE-005` to preserve `ADR-003` Decision A.

Date: 2026-07-07

### TIME-002

Outcome: `Decision`

Decision Authority / Accepted By: project owner by accepting `ADR-003`.

Resolution Artifact: `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md`, Decision B.

Resolved Against / Scope: first `SCN-001` milestone uses a selected-slice chronology and staleness contract. The harness supplies chronology facts, not temporal-applicability verdicts; the SUT owns prior-evidence current-authority eligibility and stale-history handling under the selected synthetic rule. This does not resolve `TIME-001` or define scheduler, reminders, due state, expiry, background temporal maintenance, active-trial TTL, or full longitudinal governed-clock semantics.

Supersedes / Split From: split from `TIME-001`, whose broader governed-clock scope remains deferred.

Future Trigger: material change to the selected-slice staleness rule, need for active-trial age-based expiry or TTL, need for scheduler/reminder/due/expiry semantics, or inability of `EVAL-002`, `SLICE-002`, or `SLICE-005` to preserve `ADR-003` Decision B.

Date: 2026-07-07

### EVAL-001

Outcome: `Decision`

Decision Authority / Accepted By: project owner by accepting `ADR-004 R3`.

Resolution Artifact: `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md`, Decision A.

Resolved Against / Scope: first `SCN-001` milestone uses harness-curated fixture context at each material decision point. The SUT owns semantic use of supplied context, but this milestone excludes open retrieval, memory search, broad relevance selection, distractor filtering, and active context-assembly claims. Curated context is constrained by state-origin, role-preservation, completeness, and anti-adaptive-rescue rules.

Supersedes / Split From: none.

Future Trigger: a later milestone claims retrieval quality, context discovery, relevance selection, sensitivity-aware context assembly, production memory architecture, or inability of `EVAL-002`, `SLICE-002`, or `SLICE-005` to preserve `ADR-004` Decision A.

Date: 2026-07-08

### EVAL-003

Outcome: `Decision`

Decision Authority / Accepted By: project owner by accepting `ADR-004 R3`.

Resolution Artifact: `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md`, Decision B.

Resolved Against / Scope: first `SCN-001` milestone uses formal milestone evaluation campaigns with hard invariant gates plus bounded variance. Nondeterministic configurations require three fresh valid runs per fixture path, outcome-independent run selection, fresh-run isolation, run-validity controls, invalid-run replacement review, claim-class aggregation, and no hard-invariant averaging. Deterministic replayable configurations may use one recorded run per fixture path only when material inspected-state replayability is established.

Supersedes / Split From: none.

Future Trigger: a later milestone claims full `SCN-001` pass, longitudinal drift handling, production rollout reliability, statistical acceptance, or inability of `EVAL-002` or `SLICE-005` to preserve `ADR-004` Decision B.

Date: 2026-07-08

### EVAL-002

Outcome: `Decision`

Decision Authority / Accepted By: project owner by accepting `ADR-005 R2`.

Resolution Artifact: `decisions/ADR-005-scn001-selected-slice-fixture-oracle-contract.md`.

Resolved Against / Scope: first `SCN-001` milestone uses selected-slice fixture/oracle package `SCN001-SSFO-V0.2.0`. The contract defines canonical and counterfactual paths, exact decision-point bundle membership, fixture-control facts, simulator realization facts, oracle-visible fields, run-validity rules, claim-class obligation mapping, package-local oracle rule IDs, bounded variance, failure artifacts, and bounded claim language without requiring hidden chain-of-thought or a final implementation schema.

Supersedes / Split From: none.

Future Trigger: material change to selected-slice fixture/oracle semantics, inability of `SLICE-002`, `SLICE-005`, `EVAL-004`, or `EVAL-005` to preserve the accepted fixture/oracle boundary, or a later milestone claiming broader `SCN-001` evidence than `ADR-005` permits.

Date: 2026-07-08

### INIT-003

Outcome: `Merged`

Decision Authority / Accepted By: project owner by adopting this document version.

Resolution Artifact: this register, `V0.2.2`.

Resolved Against / Scope: standalone non-scope prompt removed from the register; unsupported initiative classes belong in `INIT-001` or selected-slice scope decisions.

Supersedes / Split From: merged into `INIT-001` and selected-slice scope decisions.

Future Trigger: selected slice proposes initiative behavior not covered by `INIT-001` or its scope decision.

Date: 2026-07-06

### SURF-003

Outcome: `Obsolete`

Decision Authority / Accepted By: project owner by adopting this document version.

Resolution Artifact: this register, `V0.2.2`.

Resolved Against / Scope: standalone non-scope prompt removed from the register; concrete embodiment proposals will create concrete questions.

Supersedes / Split From: obsolete as standalone scope prompt; future embodiment proposals create concrete questions.

Future Trigger: avatar or embodied-presence behavior is proposed with specific identity, authority, disclosure, affect, or interaction commitments.

Date: 2026-07-06

### PROD-004

Outcome: `Merged`

Decision Authority / Accepted By: project owner by adopting this document version.

Resolution Artifact: this register, `V0.2.2`.

Resolved Against / Scope: standalone non-scope prompt removed from the register; product non-scope belongs in `PROD-001` or the applicable product decision.

Supersedes / Split From: merged into `PROD-001`.

Future Trigger: product scope decision is drafted or a feature needs explicit bounded exclusion.

Date: 2026-07-06

When a question is resolved, add:

```text
ID:
Outcome:
Decision Authority / Accepted By:
Resolution Artifact:
Resolved Against / Scope:
Supersedes / Split From:
Future Trigger:
Date:
```

Do not keep the full answer here.

## Quality Gates

The register is acceptable only if:

- every active question has a concrete blocking scope;
- every active question states what it does not block;
- every active question has a decision trigger, decision criteria, evidence needed, and decision authority;
- `Evidence Needed` names inspectable evidence or comparison artifacts rather than restating the decision criterion;
- no question is marked active before its trigger has occurred;
- triggered unresolved questions carried under working assumptions remain `Open`, not `Resolved`;
- governance/control questions trigger before the first non-throwaway use, state transition, artifact creation, user-facing exposure, or compatibility claim that depends on the unresolved control;
- no question's deadline precedes an unresolved dependency;
- the compact index preserves enough dependency and source-pressure metadata to recompute the active frontier and re-triage questions after baseline changes;
- material change, supersession, or invalidation of a question resolution or working assumption triggers re-triage of dependent questions and claims;
- active question dependency cycles are narrowed, split, jointly bounded, or broken through explicit working assumptions instead of deadlocking;
- questions conditional on a slice, feature, surface, or capability declare that condition;
- questions do not reopen settled thesis or state/control semantics;
- questions do not presume repositories, services, APIs, or modules unless active slice pressure requires the boundary question;
- duplicate questions are merged or linked;
- material question redefinition creates a new ID rather than mutating an old one;
- resolved IDs remain traceable and are never reused;
- material source-baseline changes trigger re-triage;
- the active decision frontier contains only questions that block the current milestone;
- bounded exclusions and working assumptions narrow the resulting milestone, evaluation, or compatibility claim and cannot silently remove canonical scenario obligations;
- selected-slice evaluations identify what semantic responsibilities are inside the system under test and what the harness or simulated dependencies supply;
- resolved decisions retain enough scope or baseline information to identify the basis against which they were accepted;
- resolution requires the applicable decision authority; a draft answer or AI-generated proposal is not closure;
- unsupported capabilities may be explicitly excluded from a bounded milestone instead of being fully designed in advance.

## Next Decision Step

Prepare the minimum selected-slice state contract for `SLICE-002` under accepted `ADR-001` through `ADR-005`.

Define which `ADR-005` oracle-visible facts require independently persisted state, which may be lineage-preserving projections, which may be derived inspection facts, and which remain fixture/oracle-only artifacts. Preserve the accepted SUT boundary, selected-slice trial/time semantics, curated-context policy, and fixture/oracle contract without turning oracle fields into a final database schema.
