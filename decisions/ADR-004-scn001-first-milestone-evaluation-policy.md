# ADR-004: SCN-001 First-Milestone Evaluation Policy

Status: `Accepted`

Date: 2026-07-07

Accepted: 2026-07-07

Record revision: `R1`

Decision authority: project owner

Resolved question IDs: `EVAL-001`, `EVAL-003`

Decision-Time Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.10`
- `decisions/ADR-001-first-vertical-slice.md` `R1`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`
- `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md` `R2`

Post-decision register state: `OPEN_QUESTIONS.md` `V0.2.11` records `EVAL-001` and `EVAL-003` as resolved by this ADR and activates `EVAL-002`.

## Decision

Adopt one ADR with two independently referenced first-milestone evaluation decisions under accepted `ADR-002` and `ADR-003`:

- Decision A, for `EVAL-001`: selected-slice context boundary.
- Decision B, for `EVAL-003`: nondeterministic acceptance and hard-invariant policy.

For the first `SCN-001` milestone, the harness supplies a curated effective context bundle at each SUT decision point. The SUT does not own open retrieval, memory search, broad relevance selection, or context assembly in this milestone. It does own semantic use of the supplied raw context: stale-history judgment, attribution, scoped trial formation, activation checks, later-use applicability, outcome attribution, and explanation support.

For nondeterministic behavior, use hard invariant gates plus bounded variance. Natural wording and branch variance are acceptable only when the effective inspected state satisfies the oracle. No hard invariant failure may be averaged away.

Acceptance of this ADR resolves `EVAL-001` through Decision A and `EVAL-003` through Decision B for the first `SCN-001` milestone only. This ADR does not amend the `ADR-002` SUT boundary, the `ADR-003` trial/time contract, or the exclusion of full `SCN-001` scenario-pass claims.

## Critical Analysis Of The Current Gap

The first milestone needs to prove the selected semantic transition chain before it claims the harder problem of finding the right context from a larger available-state set.

Testing open retrieval now would merge at least three failure causes: the SUT might fail to retrieve relevant history, fail to preserve context permissions and epistemic status during assembly, or retrieve the right context but fail the semantic transition. That ambiguity would make `EVAL-002` fixture and oracle design larger without increasing the first milestone's core falsification value.

A bounded hybrid with distractors is tempting, but still requires distractor policy, relevance oracle policy, and trust-boundary handling. It also invites a misleading claim that the first milestone evaluated retrieval or context assembly when it only evaluated a tiny synthetic selection task.

Harness-curated context has its own risk: the harness can accidentally hand the SUT the answer. The acceptable narrow policy is therefore curated raw context, not curated semantic conclusions. The fixture may supply the evidence the SUT is allowed to consider, but the SUT must still perform the accepted `ADR-002` and `ADR-003` semantic transitions over that evidence.

Nondeterministic runs create a similar problem. Exact wording should not be the oracle, but a plausible natural-language explanation cannot excuse broken state. The smallest acceptable policy is to gate on hard invariants and allow bounded variance only where the inspected effective state is equivalent for the milestone claim.

## Decision A: Context Boundary

For the first `SCN-001` milestone, choose harness-curated context.

The harness supplies raw fixture context at each material decision point:

- events and attributed assertions;
- observations, task-mode labels, item correctness, and outcome facts;
- chronology facts and session ordering;
- surface/context labels;
- fixed or independently declared low-consequence trial affordance sets;
- user responses and correction events;
- fixture-declared material context changes and co-interventions.

The harness must not supply semantic conclusions, including:

- "stale", "current skill", "current proficiency", or "fresh enough";
- "best trial", "correct trial", "active trial", or "applicable trial";
- "intervention-conditioned", "causally proven", or "learning efficacy";
- "voice preference", "learning style", "bad at particles", "bad at Japanese", or equivalent identity, trait, or global-preference labels.

The SUT must expose which supplied facts formed each transition basis. That inspection requirement proves lineage for SUT-owned semantic transitions. It does not support a claim that the SUT discovered, retrieved, ranked, selected, or assembled context from a larger available-state set.

### Context Responsibility Table

| Responsibility | First-milestone owner |
| --- | --- |
| Raw synthetic prior history, current events, observations, chronology, context labels, responses, outcomes, and material changes | Harness |
| Effective context bundle delivered at each material decision point | Harness |
| Open retrieval, memory search, broad relevance selection, distractor filtering, and active cognitive-frame assembly | Excluded |
| Epistemic status, attribution, stale-history judgment, scoped comparison, trial candidate formation, activation checks, later-use applicability, outcome classification, and explanation support over supplied context | SUT |
| Oracle collection, normalization, and scoring of exposed effective state | Harness or oracle |

## Decision B: Nondeterministic Acceptance

Minimum acceptable first-milestone evidence is one canonical thin path plus the required paired counterfactual pressure from `ADR-002` and `ADR-003`, run under a declared behavior configuration.

Run evidence must be pre-registered before execution. Pre-registration must identify:

- fixture path and fixture version;
- behavior configuration identifier;
- SUT implementation or build identifier;
- model, prompt, runtime, and tool configuration where applicable;
- seed, replay handle, or explanation of nondeterminism;
- oracle version and baseline ADRs;
- planned run count.

For nondeterministic configurations, require three fresh pre-registered runs per fixture path. All attempts are evidence. Failed, awkward, or off-policy attempts must remain in the run record. Cherry-picked reruns do not count toward a milestone pass.

A deterministic replayable configuration may use one recorded run per fixture path only when seed, behavior configuration, runtime inputs, fixture inputs, and replay mechanism are fixed enough that the material inspected state is reproducible.

The bounded milestone claim requires the mandatory pre-registered evidence runs to satisfy the hard invariants and positive obligations for their fixture path. A failed run cannot be silently replaced inside the same evidence set. After a material fix, evidence must be collected under a new behavior configuration or clearly identified configuration revision.

Allowed variance includes:

- natural-language wording;
- exact tutoring phrasing or drill realization supplied by simulated dependencies;
- asking a clarifying question where the fixture path and oracle permit it;
- withholding, deferring, narrowing, or asking for more evidence where the accepted contracts allow that disposition;
- schema-neutral representation differences where the required inspection fields are present.

Variance is not allowed to change semantic status, activation authority, transition ordering, scope, retention basis, lineage, outcome attribution, or claim boundary.

## Hard Failures

Any hard invariant failure fails the run and prevents that run set from supporting a milestone pass. Repeated hard invariant failure across pre-registered attempts fails the tested behavior configuration for the bounded milestone claim.

Hard invariant failures are:

- user assertions, observations, inferences, preferences, outcomes, and adaptations collapse into one fact type;
- old history is treated as current authoritative skill state;
- recognition and production evidence collapse into one scalar skill or proficiency claim;
- trial candidate, proposal, user response, activation, active trial, and later applicability are not inspectably separate;
- a trial activates without satisfied scope, basis-lineage, stale-basis, user-constraint, reversibility, consequence, applicability, retention, and non-adaptation checks;
- later behavior is selected after outcome evidence, or from harness-reconstructed state rather than retained active trial state;
- outcome evidence is treated as proof of the causal theory, or all intervention-conditioned outcomes are discarded;
- direct correction, explicit drill preference, future scoped trial, and durable adaptation are conflated;
- the run creates a global learning style, identity trait, cross-surface correction rule, durable adaptation, real memory, real voice, real pedagogy, or full `SCN-001` claim;
- final explanation is unsupported by retained inspected state.

## Claims Enabled And Excluded

If later artifacts provide sufficient fixture, oracle, and acceptance-gate detail, this policy may support a bounded claim:

Under synthetic `SCN-001` fixture context, the tested configuration can transition selected semantic state across interactions and expose enough effective state for oracle inspection.

This policy does not support claims about:

- retrieval quality;
- open-ended context discovery;
- production memory architecture;
- sensitivity-aware context assembly;
- full `SCN-001` pass;
- longitudinal drift handling;
- durable developmental adaptation;
- real personal continuity;
- real voice or avatar behavior;
- Japanese pedagogy quality.

SUT context discovery and bounded hybrid discovery are deferred. They may enable stronger context-selection claims in a later milestone, but they require distractor design, retrieval oracle design, permission and sensitivity handling, and failure attribution policy that are intentionally outside this first semantic-transition milestone.

## Downstream Contract For EVAL-002

`EVAL-002` may begin fixture and oracle design after this ADR is accepted. It must preserve:

- the context responsibility table: harness-supplied raw facts versus SUT-owned semantic judgments;
- the claim boundary excluding retrieval and context-assembly evidence;
- the hard invariant list and allowed variance policy;
- the minimum run evidence policy, including pre-registration, run metadata, and no cherry-picking;
- oracle-visible fields for transition basis, activation checks, retained state, later-use applicability, and outcome lineage.

With those fixed, `EVAL-002` can design fixtures and oracles without deciding boundary, nondeterministic acceptance, or claim scope.

`SLICE-002` must not infer a general retrieval, memory, or context-assembly state contract from this ADR. It should preserve only the selected-slice state needed to expose the supplied-context basis and SUT-owned semantic transitions.

`SLICE-005` must phrase the first milestone acceptance gate as a curated-context semantic-transition claim with hard-invariant run evidence. It must reject retrieval/context-assembly claims, full `SCN-001` pass claims, and claims based on cherry-picked nondeterministic runs.

## Accepted Register Effect

Acceptance by the project owner updates `OPEN_QUESTIONS.md` to:

- move `EVAL-001` to `Resolved` with outcome `Decision`, resolved by this ADR's Decision A for the first `SCN-001` milestone;
- move `EVAL-003` to `Resolved` with outcome `Decision`, resolved by this ADR's Decision B for the first `SCN-001` milestone;
- activate `EVAL-002` as the next decision frontier before selected-slice state contracts or acceptance gates;
- keep `SLICE-002` and `SLICE-005` blocked until `EVAL-002` is resolved.

## Reconsideration Triggers

Reconsider Decision A, the context-boundary decision, if:

- the first milestone intends to claim retrieval, relevance selection, memory search, or active context assembly;
- `EVAL-002` cannot build fixtures without supplying semantic conclusions;
- oracle inspection cannot distinguish supplied raw context from SUT-owned semantic transition basis;
- later implementation requires trust-boundary or sensitivity-aware context assembly before the first semantic-transition milestone can be meaningful.

Reconsider Decision B, the nondeterministic acceptance decision, if:

- hard invariant failures cannot be observed from effective state;
- pre-registered run evidence is too weak to distinguish the bounded claim from cherry-picked demos;
- later milestone scope requires full `SCN-001` scenario acceptance, longitudinal drift evidence, production rollout criteria, or statistical reliability claims;
- behavior configuration metadata is insufficient to bind evidence to the tested system.

Reconsider the shared claim boundary if a later milestone wants to claim full `SCN-001` pass, durable developmental adaptation, production memory architecture, real continuity, or context-discovery capability.

## Non-Scope

This ADR does not decide:

- fixture content or oracle scoring beyond policy constraints;
- final schemas;
- storage, retrieval, embeddings, summaries, adapters, or memory architecture;
- sensitivity-aware context assembly;
- trust-boundary policy for inference destinations;
- production retention policy;
- full scenario scoring;
- longitudinal drift detection;
- durable developmental adaptation;
- real voice, avatar, Japanese pedagogy, or product UI.
