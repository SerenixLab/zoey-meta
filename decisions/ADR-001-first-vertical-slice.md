# ADR-001: First Vertical Slice

Status: `Proposed`

Date: 2026-07-07

Decision authority: project owner

Related open question: `SLICE-001`

Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.2`

## Decision

Choose `SCN-001: Japanese Longitudinal Development` as the first vertical slice.

The first slice should be harness-first and state-inspection-first. It should not be a polished tutoring product, a voice/avatar product, or a reconstruction of Yuki. Its purpose is to test whether Zoey can preserve controlled path-dependent growth under stale history, contradictory evidence, scoped trials, user correction, intervention-conditioned outcomes, and trajectory pressure.

## Why

`SCN-001` pressures the most distinctive part of Zoey: useful growth without identity drift, sycophancy, unsupported self-narrative, or memory misuse.

`SCN-002` is also central, but it starts from the Iris-shaped side of the problem: operation authority, auditability, external state, reconciliation, and control-plane discipline. Those are important, but choosing them first risks making Zoey's first executable abstraction an Iris-like operation kernel with developmental continuity added later.

`SCN-001` can start with fewer external dependencies while still forcing the state/control model to become real: event history, attributed assertions, observations, scoped interpretations, trials, adaptations, correction, explanation, and trajectory inspection.

## Evidence Matrix

| Dimension | `SCN-001`: Japanese Longitudinal Development | `SCN-002`: Voice-Originated Calendar Mutation | Judgment |
| --- | --- | --- | --- |
| Central thesis risk pressured | Directly pressures controlled growth, memory provenance, scoped adaptation, anti-sycophancy, medium-scoped behavior, and user correction. | Directly pressures authority, operation safety, external source of truth, disclosure, and practical delegation. | Both are central; `SCN-001` better tests Zoey's unique developmental thesis first. |
| Required semantic transitions | Stale history -> attributed assertions/observations -> scoped interpretation -> behavioral trial -> intervention-conditioned outcome -> possible adaptation -> trajectory inspection. | Utterance -> actor assurance -> target resolution -> proposal -> authorization -> pre-action validation -> external mutation -> uncertain outcome -> reconciliation -> audit. | `SCN-001` exercises more of Zoey's growth semantics; `SCN-002` exercises operation semantics more cleanly. |
| Required persistent state | Event history, attributed assertions, calibration observations, trial/adaptation state, user correction, explanation provenance, trajectory records. | Operation intent, actor assurance state, external projection, proposal, authorization binding, submission, outcome, reconciliation, audit. | Both need state. `SCN-001` builds the personal continuity substrate that later operations can also use. |
| External/runtime dependencies | Can begin with text/harness fixtures and synthetic Japanese sessions. No real voice, TTS, calendar, or provider required. | Needs at least simulated voice input, actor-assurance fixture, calendar source, mutation provider, timeout/reconciliation behavior, and audit. | `SCN-001` has lower infrastructure breadth for a first falsifiable run. |
| Legacy leverage | Yuki has direct material: local voice loop, STT gate, retrieval/context pipeline, session events, flat memory, dashboard/evidence work, and growth/memory planning. Must strip identity assumptions. | Iris/Specialized-LLM has direct material: control plane, policy, capabilities, audit clerk, artifact registry, kernel boundary, memory lifecycle. Must strip Iris product assumptions. | Both have leverage. `SCN-001` uses Yuki evidence structures without needing to adopt Yuki as identity. |
| Demo-gaming risk | High. A fake system can hardcode tutoring behavior or produce a plausible retrospective story. Requires inspectable state checkpoints and longitudinal evidence. | Medium-high. A fake system can script a happy calendar path, but operation components are easier to inspect. | `SCN-001` is riskier but more valuable to falsify early. Harness must not accept prose-only success. |
| Architecture overbuild pressure | Moderate. Temptation is to build a full memory/personality/adaptation system too early. Can be bounded to scenario state and fixtures. | High. Temptation is to build operation kernel, auth model, audit store, calendar integration, voice assurance, and UI confirmation flows. | `SCN-001` is easier to keep narrow if voice/avatar and real personal memory are excluded. |
| Triggered open questions before first run | Likely activates `EVAL-006`, `EVAL-001`, `EVAL-002`, `EVAL-003`, `TIME-001`, `SLICE-002`, `GROW-001`, `DEP-001`, and limited `MEM-001`. May defer `AUTH-*`, `SURF-*`, `TRUST-001`, `CONT-002` if fixture-only/local. | Likely activates `EVAL-006`, `EVAL-001`, `EVAL-002`, `EVAL-003`, `TIME-001`, `AUTH-001`, `AUTH-002`, `AUTH-004`, `AUTH-005`, `DEP-004`, `SURF-002`, `TRUST-001`, and operation audit questions. | `SCN-001` activates fewer authority/external-service questions. |
| First evaluator checkpoints | State checkpoints for stale history, recognition/production split, trial activation, correction, intervention-conditioned outcome, explanation provenance, and trajectory. | State checkpoints for actor assurance, target, proposal, authorization binding, material-state validation, uncertain outcome, reconciliation, and audit. | `SCN-002` checkpoints are crisper. `SCN-001` checkpoints are harder but closer to Zoey's core risk. |
| Cross-scenario transfer | Builds provenance, state lifecycle, dependency tracking, correction, explanation, time, and evaluation harness discipline. Later `SCN-002` can challenge whether these abstractions handle authority and operations. | Builds operation-control and audit discipline. Later `SCN-001` can challenge whether the architecture supports growth rather than only task execution. | `SCN-001` transfers broadly to continuity and state semantics; `SCN-002` will be a strong second challenge. |
| First-slice capture risk | Risk of Yuki-like gravity: Zoey becomes memory/growth/companion first, with operations bolted on. Mitigation: no voice/avatar product, no companionship framing, harness-first state evaluation. | Risk of Iris-like gravity: Zoey becomes control plane/task engine first, with developmental identity bolted on. Mitigation would require explicitly keeping growth in scope later. | `SCN-001` capture risk is real but manageable if strictly harness-first. `SCN-002` would likely amplify the already-strong Iris gravity. |
| Time to first falsifiable run | Moderate if using synthetic sessions and explicit state checkpoints. Longitudinal variant can be staged after base path. | Moderate-high unless heavily simulated; if heavily simulated, system-under-test boundary becomes the main risk. | `SCN-001` should reach a useful thin run sooner. |

## System-Under-Test Boundary Implication

This ADR does not itself define the system-under-test boundary.

If this decision is accepted, the next active question should be `EVAL-006`: define what the first `SCN-001` slice must produce versus what the harness supplies.

The first slice may use fixture Japanese sessions and synthetic evidence. If so, the acceptance claim must say that retrieval/discovery, real personal memory custody, real voice interaction, and production tutoring quality are not yet proven.

## Accepted Exclusions For First Slice Drafting

These exclusions are proposed only for the first `SCN-001` slice definition:

- no real user personal history required;
- no avatar, Live2D, or embodied presence behavior;
- no real voice/STT/TTS requirement;
- no calendar or external operation;
- no embeddings, adapters, training examples, or learned profiles unless explicitly introduced later;
- no claim of full `SCN-001` pass until the longitudinal trajectory pressure is represented and scored;
- no claim that Zoey teaches Japanese well.

## Questions Activated If Accepted

Immediate next frontier:

- `EVAL-006`: system-under-test and fixture boundary.
- `EVAL-001`: context discovery versus harness-injected context.
- `EVAL-002`: fixture and oracle data for selected scenario.
- `EVAL-003`: nondeterministic run acceptance and hard failures.
- `TIME-001`: governed-clock contract for longitudinal and delayed-session behavior.

Likely next after `EVAL-006`:

- `SLICE-002`: minimum persistent state for the selected slice.
- `GROW-001`: posture/trial/adaptation decision boundaries.
- `DEP-001`: minimum dependency identity metadata.
- limited `MEM-001`: retention bases and transient defaults for fixture or retained scenario state.

Conditionally activated:

- `TRUST-001` only if personal or retained semantic state is sent across a materially different inference/runtime trust boundary.
- `CONT-002` only if real authoritative personal state is retained as durable Zoey continuity rather than disposable fixture/test state.
- `GROW-002` only when the longitudinal trajectory variant enters the milestone.

## Consequences

Positive:

- Tests Zoey's controlled-growth thesis before the system becomes an operation engine.
- Keeps the first implementation free from calendar/provider/authentication dependencies.
- Forces inspectable state and explanation provenance early.
- Uses Yuki legacy evidence ideas without preserving Yuki as an identity-bearing system.

Negative:

- Harder to score than an operation path.
- Higher risk of plausible narrative success unless the harness inspects state.
- Does not prove external operation safety, actor assurance, auditability, or practical delegation.
- May bias early abstractions toward growth and memory unless `SCN-002` is kept as the planned second canonical challenge.

## Non-Decisions

This ADR does not decide:

- repository boundaries;
- final state schema;
- memory storage engine;
- vector store or embedding use;
- model/runtime choice;
- real Japanese pedagogy;
- voice/avatar product behavior;
- legacy migration plan;
- GitHub repository layout.

## GitHub Repository Note

The recommended GitHub shape is a docs-only `zoey-meta` repository rooted at `Zoey/meta`.

Do not make the whole `Zoey/` container the GitHub repo while it contains `legacy/` and future subprojects. Legacy projects should remain reference material unless separately archived. Future implementation repos should live separately under `Zoey/projects/` and link back to this meta repo by document/version references.
