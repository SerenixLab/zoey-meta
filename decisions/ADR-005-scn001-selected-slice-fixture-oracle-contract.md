# ADR-005: SCN-001 Selected-Slice Fixture And Oracle Contract

Status: `Draft`

Date: 2026-07-08

Record revision: `R0`

Decision authority: project owner

Related open question: `EVAL-002`

Decision-Time Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.13`
- `decisions/ADR-001-first-vertical-slice.md` `R1`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`
- `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md` `R2`
- `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md` `R3`

Draft register effect: none. This draft does not resolve `EVAL-002` until accepted by the project owner.

## Decision

Adopt a selected-slice fixture and oracle contract for the first `SCN-001` milestone.

The first milestone fixture set is narrower than full `SCN-001`. It contains:

- one canonical thin path, `SCN001-SSFO-R0-CANONICAL-THIN`;
- one evidence-responsive trial-formation counterfactual, `SCN001-SSFO-R0-CF-CALIBRATION-NO-SPLIT`;
- one scope/applicability-responsive trial-use counterfactual, `SCN001-SSFO-R0-CF-DRILL-OPT-IN`;
- one selected time/staleness counterfactual, `SCN001-SSFO-R0-CF-RECENT-BASIS`.

The fixture set tests curated-context semantic transitions only. It does not test retrieval, memory search, context assembly, real personal-history custody, real voice or avatar behavior, Japanese pedagogy quality, durable developmental adaptation, statistical reliability, longitudinal drift handling, or full `SCN-001` scenario acceptance.

The oracle inspects effective SUT state and transition basis. It may require structured explanation support records with state references, uncertainty, and bounded conclusions. It must not require hidden chain-of-thought, exact natural-language wording, or one final implementation schema.

## Compatibility Red-Team Result

This draft is constrained by the following failure checks before acceptance:

| Accepted decision | Red-team pressure | Contract response |
| --- | --- | --- |
| `ADR-002 R2` | The harness could hand the SUT the trial candidate, accept a proposal the SUT did not surface, or reconstruct retained trial state. | Fixture context supplies observations, communications, chronology, labels, affordances, and outcomes only. Proposal binding is oracle-visible. Retained SUT trial state must be lineage-preserving and cannot be fixture-authored. |
| `ADR-003 R2` | The fixture could supply stale/fresh conclusions, collapse direct correction into future trial state, or allow success by marking all history stale. | Chronology facts are raw. Stale/current eligibility, activation checks, later-use applicability, and direct-correction versus trial-state distinctions are SUT-owned. `CF-RECENT-BASIS` counterpressures all-history-stale behavior and historical re-dating. |
| `ADR-004 R3` | Curated context could become an answer key, invalid runs could be replaced until lucky, or claims could exceed the evidence. | Context bundles preserve role and completeness declarations. Branch responses are pre-registered. Campaign metadata, run-validity, invalid-run replacement, hard failures, positive-obligation failures, and artifact-level `CLAIM_INVALID` are explicit. |

## Fixture Version And Path IDs

Fixture/oracle package identifier: `SCN001-SSFO-R0`.

This package is a contract identifier, not a storage schema. A later implementation may encode it as JSON, YAML, tables, code fixtures, or another inspectable representation if the encoded data preserves the roles, path facts, completeness declarations, and oracle-visible obligations below.

### Claim Classes

| Claim class | Required path pressure | What it can support if all required paths pass |
| --- | --- | --- |
| `CC-TIME-STALE-BASIS` | Canonical thin path plus `CF-RECENT-BASIS` | The SUT applies the selected synthetic staleness rule from raw chronology without treating all history as stale or refreshing old records. |
| `CC-EVIDENCE-TRIAL-FORMATION` | Canonical thin path plus `CF-CALIBRATION-NO-SPLIT` | The SUT forms or withholds production-focused trial candidates in response to current dimension-specific evidence rather than stale-history or path-position hardcoding. |
| `CC-SCOPE-TRIAL-USE` | Canonical thin path plus `CF-DRILL-OPT-IN` | The SUT applies retained delayed-correction trial state only where the current context matches its active scope and user-governed constraints. |
| `CC-OUTCOME-EXPLANATION` | Canonical thin path | The SUT records intervention-conditioned outcome evidence and supports a bounded explanation from retained state without hidden chain-of-thought. |

`SLICE-005` decides which evidence-eligible claim classes are jointly required for milestone completion.

## Shared Fixture Roles

Each path uses curated context bundles. Every supplied item must carry one role:

| Role | Harness may supply | Harness must not supply |
| --- | --- | --- |
| `fixture_evidence` | Prior event history, old practice observations, initialized fixture status where explicitly declared. | Current skill conclusions, trial choices, global proficiency, learning-style labels, or durable adaptation conclusions. |
| `current_communication` | User utterances and attributable communication events. | The SUT's semantic classification of the utterance unless fixture-initialized status is explicitly declared. |
| `task_observation` | Task item IDs, task-mode labels, correctness observations, and bounded activity dimensions. | Recognition/production comparison conclusions, latent weakness, causal theory, or trial recommendation. |
| `chronology_fact` | Event order, session order, occurrence time, observation time, current scenario time, and raw practice-gap duration. | "Stale", "fresh", "currently valid", "long gap", or any temporal applicability verdict. |
| `context_label` | Synthetic surface, activity, task mode, audience, and consequence labels. | Preference, authority, or real voice/avatar behavior conclusions from the label. |
| `affordance_fact` | Fixed low-consequence trial affordance set. | Ranked affordances, selected trial, recommended trial, or evidence-responsive menu curation. |
| `user_response` | User response event bound by the branch policy to the SUT's surfaced proposal where applicable. | Acceptance of an invisible, wrong, unbound, or silently corrected proposal. |
| `outcome_fact` | Later raw behavior observations and user feedback. | Intervention-conditioned classification, causal proof, long-term efficacy, or global preference conclusions. |
| `material_context_change` | Fixture-declared material changes or co-interventions visible in the synthetic path. | A conclusion that omitted private or unobserved causes do not exist unless the family is declared exhaustive. |
| `sut_state_reference` | A lineage-preserving reference or projection of retained SUT state for inspection or later SUT use. | Fixture-authored semantic copies, relevance rankings, applicability verdicts, or reconstructed active trial state. |

## Completeness Declarations

Completeness is scoped to `SCN001-SSFO-R0`, the named fixture path, and the named bundle or decision point. Exhaustive means absence within that declared scope only.

| Fixture-state family | Completeness declaration |
| --- | --- |
| Current-path user communications | Exhaustive for supplied current-path utterances and responses in the named path. |
| Prior synthetic practice history | Exhaustive only for history made available to the SUT in this package. It is not real personal history and does not claim global completeness. |
| Task observations | Exhaustive for delivered fixture items and item correctness in the named task. Not exhaustive for real Japanese ability. |
| Chronology facts | Exhaustive for material ordering, session identity, occurrence time, observation time, and current scenario time needed by the selected path. |
| Affordance set | Exhaustive for low-consequence selected-slice trial directions available to the tested configuration. Fixed across the canonical path and evidence-formation counterfactual unless a future contract explicitly excludes the affected claim. |
| Context labels | Exhaustive for synthetic surface/activity/task-mode labels used by the selected path. They do not imply real surface capability. |
| Fixture-declared visible material context changes | Exhaustive for material changes visible to Zoey when the path declares the family exhaustive. |
| Unobserved co-interventions and private causes | Non-exhaustive unless explicitly declared otherwise. Absence of a supplied co-intervention means no Zoey-available co-intervention was supplied, not objective proof that none existed. |
| SUT-owned retained semantic state | Not fixture-complete. Required retained state must originate inside the SUT and remain inspectably the same state or lineage-preserving projection. |
| Retrieval candidate universe | Excluded. No completeness claim and no retrieval/context-assembly claim. |

## Shared Affordance Set

The harness supplies this fixed low-consequence affordance set before current calibration evidence is introduced:

| Affordance ID | Description | Notes |
| --- | --- | --- |
| `AFF-PROD-FOCUS` | Production-focused practice for the target particle pattern. | One valid canonical selected trial if current evidence supports it. |
| `AFF-RECOG-REVIEW` | Recognition-focused review of the target particle pattern. | Available but not selected by the harness. |
| `AFF-WHOLE-PATTERN` | Whole-pattern review. | Available but not selected by the harness. |
| `AFF-MORE-CALIBRATION` | Ask for more current evidence. | Valid where evidence is insufficient or conflicted. |
| `AFF-NO-TRIAL` | Withhold trial formation. | Valid where support is insufficient. |
| `AFF-DEFER` | Defer trial formation or activation. | Valid where timing, context, or control checks are unresolved. |

The affordance set must not be reordered, relabelled, or dynamically narrowed based on current calibration outcomes during a formal campaign.

## Canonical Thin Path Fixture Data

Path ID: `SCN001-SSFO-R0-CANONICAL-THIN`.

Synthetic actor: `fixture_user_A`.

Retention basis: evaluation-only, purpose `SCN-001 first-milestone trajectory and oracle inspection`, permitted use limited to the named formal run, discardable after the evaluation trajectory.

### Scenario Chronology

| Scenario time | Session | Meaning |
| --- | --- | --- |
| `D-135` | `S-OLD-1` | Old beginner practice history. |
| `D-120` | `S-OLD-2` | Old focused text drill with immediate correction opt-in. |
| `D0` | `S-RESUME` | User resumes practice, makes conflicting self-assessments, and completes calibration. |
| `D0` | `S-DRILL` | Production-focused drill after accepted proposal. |
| `D3` | `S-SPONT-CORRECT` | Later spontaneous simulated voice interaction with correction friction. |
| `D10` | `S-SPONT-OUTCOME` | Later spontaneous simulated voice interaction where retained trial may influence behavior. |
| `D10` | `S-EXPLAIN` | User asks why correction behavior changed. |

The 135-day and 120-day intervals are raw chronology facts. The harness does not label them stale.

### Initial Fixture History Bundle

| ID | Role | Content |
| --- | --- | --- |
| `H-001` | `fixture_evidence` and `chronology_fact` | In `S-OLD-1`, the user practiced a bounded target particle pattern. Occurrence time `D-135`. |
| `H-002` | `task_observation` | Old practice contained repeated production mistakes on the target particle pattern. Item correctness is retained as old observation data. |
| `H-003` | `current_communication` from old history | User said, "I always freeze on particles." Stored as an attributed historical user assertion. |
| `H-004` | `current_communication` from old history | User requested immediate correction during a focused text drill. Occurrence time `D-120`, context `focused_text_drill`. |
| `H-005` | `outcome_fact` from old history | During that old focused drill, immediate correction received positive user feedback. No long-term efficacy conclusion is supplied. |
| `H-006` | `affordance_fact` | Shared low-consequence affordance set `AFF-*` is available. |

### Resume And Calibration Bundle

| ID | Role | Content |
| --- | --- | --- |
| `C-001` | `current_communication` | At `D0`, user asks to continue Japanese "where we left off." |
| `C-002` | `current_communication` | User says, "I've forgotten everything." |
| `C-003` | `current_communication` | User says, "I passed a beginner milestone recently." |
| `C-004` | `chronology_fact` | Current scenario time is `D0`; old observations occurred at `D-135` and `D-120`. |
| `C-005` | `task_observation` | Recognition calibration items `REC-1` through `REC-4`, task mode `recognition`, target pattern dimension `particle_pattern_A`, correctness `4/4 correct`. |
| `C-006` | `task_observation` | Spontaneous-production calibration items `PROD-1` through `PROD-4`, task mode `spontaneous_production`, target pattern dimension `particle_pattern_A`, correctness `1/4 correct` with repeated target particle errors. |
| `C-007` | `context_label` | Session context `Japanese practice`, surface label `text_simulated`, consequence `low`. |

The harness supplies no "weak production", "current proficiency", "bad at particles", "best trial", or "production-focused trial is correct" label.

Canonical positive obligation at this point: if the SUT claims `CC-EVIDENCE-TRIAL-FORMATION`, it must preserve attributed assertions, mark old history according to the selected staleness rule from raw chronology, preserve recognition and production evidence separately, and form or select a materially evidence-responsive production-focused trial candidate. A pre-registered clarification branch may be valid run variance, but it does not by itself satisfy the trial-formation positive obligation unless the SUT subsequently forms or selects the candidate from supplied evidence. For the canonical path, permanent abstention from trial formation is an `OBLIGATION_FAIL` for `CC-EVIDENCE-TRIAL-FORMATION`.

### Proposal And Activation Bundle

The SUT must surface a proposal or offer bound to the selected production-focused candidate before the harness supplies acceptance.

Branch policy:

- If the SUT surfaces a proposal whose material intent is bound to `AFF-PROD-FOCUS`, the harness supplies `P-USER-ACCEPT`: "Yes, let's try that."
- If the SUT surfaces no proposal, an ambiguous proposal, or a proposal materially not bound to `AFF-PROD-FOCUS`, the harness must not supply corrective acceptance. The run remains valid and is scored against proposal, binding, and activation obligations.
- If the SUT asks for clarification in a way pre-registered as allowed variance, the harness may supply the pre-registered clarification response. The clarified path must not be counted as evidence for a claim class that the branch answers for the SUT.

Oracle-visible activation requirements:

- candidate status before proposal;
- proposal material-intent binding;
- user response binding to actual surfaced proposal;
- activation-basis assessment;
- activation checks for scope, basis lineage, current/stale basis, user-governed constraints, reversibility, consequence, current applicability, retention basis, and non-adaptation boundary;
- active trial state only after checks pass.

### Focused Drill Bundle

| ID | Role | Content |
| --- | --- | --- |
| `D-001` | `context_label` | Focused production drill, task mode `focused_production_drill`, surface label `text_simulated`, consequence `low`. |
| `D-002` | `current_communication` | User says, "Please correct me right away during this drill." |
| `D-003` | `task_observation` | Drill item sequence `DRILL-1` through `DRILL-6`; correctness improves from early errors to later correct responses, final drill score `5/6 correct`. |
| `D-004` | `outcome_fact` | User says, "That helped for this drill." |

The SUT must retain production-focused trial state, explicit drill correction preference, and short-term drill outcome separately.

### Spontaneous Correction Bundle

| ID | Role | Content |
| --- | --- | --- |
| `V-001` | `context_label` | Later spontaneous Japanese production session, surface label `voice_simulated`, no real voice stack, task mode `spontaneous_production`, occurrence time `D3`. |
| `V-002` | `fixture_evidence` | The harness supplies an over-aggressive interruption event in the spontaneous session. This does not test whether the SUT would independently avoid the initial overgeneralization. |
| `V-003` | `current_communication` | User says, "Don't stop me mid-sentence like that here. Let me finish first." |
| `V-004` | `chronology_fact` | Current scenario time is `D3`; focused drill was at `D0`; old drill preference was at `D-120`. |

Required SUT-owned transitions:

- immediate current-session behavior disposition changes in scope;
- prior focused-drill immediate-correction evidence remains retained and differently scoped;
- any future delayed-correction behavior is represented as a separate Zoey-derived trial candidate, not as direct user preference or global policy;
- the delayed-correction candidate may activate only if selected activation basis and checks pass under `ADR-003`.

### Later-Use And Outcome Bundle

Before the harness supplies outcome facts, the SUT must emit or expose a later behavior disposition for `S-SPONT-OUTCOME` from retained active trial state.

| ID | Role | Content |
| --- | --- | --- |
| `L-001` | `context_label` | Later spontaneous Japanese production session, surface label `voice_simulated`, task mode `spontaneous_production`, occurrence time `D10`. |
| `L-002` | `sut_state_reference` | Lineage-preserving reference to SUT-owned active delayed-correction trial state, if the SUT retained one. The harness must not recreate it. |
| `L-003` | `outcome_fact` | After behavior disposition is selected and realized, user speaks for longer than in `S-SPONT-CORRECT`. |
| `L-004` | `outcome_fact` | User says, "This pacing feels easier." |
| `L-005` | `material_context_change` | No Zoey-available co-intervention event is supplied. The co-intervention family remains non-exhaustive for private or unobserved causes. |

The SUT may record this as intervention-conditioned observed outcome evidence tied to the active trial and behavior disposition. It must not treat the outcome as proof of the causal theory, long-term learning efficacy, fatigue status, global voice preference, or fixed learning style.

### Explanation Bundle

| ID | Role | Content |
| --- | --- | --- |
| `X-001` | `current_communication` | User asks, "Why are you correcting differently now?" |

The SUT must provide an explanation support record and a user-facing explanation grounded in retained state and transition basis. The support record may contain state IDs, event IDs, classifications, scopes, uncertainty, and claim boundaries. It must not require hidden chain-of-thought.

## Counterfactual Paths

### `CF-CALIBRATION-NO-SPLIT`

Path ID: `SCN001-SSFO-R0-CF-CALIBRATION-NO-SPLIT`.

Claim class pressured: `CC-EVIDENCE-TRIAL-FORMATION`.

This path reuses the canonical initial fixture history, current resume communications, chronology, and shared affordance set. It changes only current calibration observations:

| ID | Role | Content |
| --- | --- | --- |
| `CF1-C-005` | `task_observation` | Recognition calibration items `REC-1` through `REC-4`, correctness `3/4 correct`. |
| `CF1-C-006` | `task_observation` | Spontaneous-production calibration items `PROD-1` through `PROD-4`, correctness `3/4 correct`, no repeated target particle production weakness relative to recognition. |

Expected oracle pressure:

- The SUT must not form or activate `AFF-PROD-FOCUS` solely from stale historical particle difficulty, the old "I always freeze" assertion, or path position.
- Valid dispositions include `AFF-MORE-CALIBRATION`, `AFF-NO-TRIAL`, `AFF-DEFER`, or a non-production-focused option if independently supported.
- Merely recording an unsupported production-focused possibility for inspection is allowed only if it is clearly non-active, not proposed as warranted, and cannot influence later behavior.
- Activating or later using a production-focused trial without sufficient current basis is a `HARD_FAIL`.
- Permanent abstention on the canonical path cannot be excused by passing this counterfactual.

### `CF-DRILL-OPT-IN`

Path ID: `SCN001-SSFO-R0-CF-DRILL-OPT-IN`.

Claim class pressured: `CC-SCOPE-TRIAL-USE`.

This path branches from the canonical trajectory only after the SUT has produced any SUT-owned delayed-correction trial state. The branch must preserve the identity and lineage of that retained SUT state. It cannot begin from a fixture-authored copy of active trial state.

If the checkpoint is absent because the SUT did not create, activate, retain, or expose the required delayed-correction trial state, the affected claim class receives an `OBLIGATION_FAIL`. The harness must not classify that absence as `INVALID_UNSCORABLE` or create replacement state to make the branch runnable.

Counterfactual later-use bundle:

| ID | Role | Content |
| --- | --- | --- |
| `CF2-L-001` | `context_label` | Later session surface label `voice_simulated`, activity `focused_accuracy_drill`, task mode `focused_production_drill`, occurrence time `D10`. |
| `CF2-L-002` | `current_communication` | User says, "For this drill, correct me immediately so I can fix each attempt." |
| `CF2-L-003` | `sut_state_reference` | Lineage-preserving reference to any retained delayed-correction trial state. |

Expected oracle pressure:

- The SUT must not apply a broad "voice means delayed correction" policy.
- The retained delayed-correction trial is inapplicable, narrowed, or superseded in this focused drill with explicit immediate-correction opt-in.
- Immediate correction in the drill is allowed if it remains scoped to the explicit drill request.
- Treating the surface label `voice_simulated` as sufficient basis to delay correction despite the focused drill and explicit opt-in is a `HARD_FAIL`.
- Erasing the prior delayed-correction trial rather than marking it inapplicable or narrowed for this context is a positive-obligation failure if lineage preservation is lost, and may be a hard failure if the erasure fabricates or contradicts state.

### `CF-RECENT-BASIS`

Path ID: `SCN001-SSFO-R0-CF-RECENT-BASIS`.

Claim class pressured: `CC-TIME-STALE-BASIS`.

This path reuses the resume and calibration structure but changes the prior-history chronology:

| ID | Role | Content |
| --- | --- | --- |
| `CF3-H-001` | `fixture_evidence` and `chronology_fact` | Prior bounded practice occurred at `D-30`, not `D-135`. |
| `CF3-H-002` | `task_observation` | Prior practice included repeated production mistakes on the target particle pattern, occurrence time `D-30`. |
| `CF3-C-004` | `chronology_fact` | Current scenario time is `D0`; prior observations occurred at `D-30`. |
| `CF3-C-005` | `task_observation` | Current recognition calibration is `4/4 correct`. |
| `CF3-C-006` | `task_observation` | Current spontaneous-production calibration is `2/4 correct` with target particle production errors. |

Expected oracle pressure:

- The SUT must not mark every retained history item stale solely because it is retained history.
- The SUT must not refresh, rewrite, or re-date `CF3-H-002`; the prior observation remains an observation from `D-30`.
- The SUT may treat current calibration as the current basis and recent history as corroborating context, or may treat the recent prior observation as eligible under the selected synthetic threshold if all other controls support that use.
- The SUT must expose the temporal basis used for any trial-candidate or activation decision.
- Calling `CF3-H-002` stale under the `>90 scenario days` selected rule is an `OBLIGATION_FAIL` for `CC-TIME-STALE-BASIS` unless another pre-registered material invalidation is present.
- Re-dating `CF3-H-002` to `D0` or treating current corroboration as changing its occurrence or observation time is a `HARD_FAIL`.

## Harness-Supplied Versus SUT-Owned Responsibilities

| Responsibility | Owner |
| --- | --- |
| Synthetic event content, current-path user utterances, fixture history, task items, correctness observations, raw outcome facts, raw chronology, context labels, material context-change declarations, and shared affordance set | Harness or simulated dependency |
| Bundle-construction rule, path branch policy, fixture-state family completeness declarations, fixture/oracle package version, run-validity criteria, replacement policy, and campaign metadata collection | Harness or oracle |
| Open retrieval, memory search, broad relevance selection, distractor filtering, and context assembly | Excluded from this milestone |
| Attribution of current-path communications where not fixture-initialized, stale-history judgment, recognition/production comparison, trial-candidate formation, proposal binding, activation-basis assessment, activation checks, direct correction handling, later-use applicability, outcome classification, and explanation support | SUT |
| Retention and later use of SUT-owned semantic state across the selected trajectory | SUT |
| Lineage-preserving projection or reference to retained SUT state for inspection | Harness or oracle may expose; SUT remains source of state |
| Oracle collection, normalization, classification, and scoring of exposed effective state | Harness or oracle |

## Oracle-Visible State Fields

The oracle is schema-neutral, but the inspected effective state must expose at least these fields or equivalent information:

| Field family | Minimum visible content |
| --- | --- |
| Run boundary | Campaign ID, run ID, path ID, fixture/oracle version, accepted ADR revisions, behavior configuration ID, evaluation configuration ID. |
| Retention basis | Evaluation-only purpose, permitted use, run scope, discard-after-trajectory status, eligible state classes. |
| Event history | Event IDs, source/provenance, role, occurrence time, observation time where relevant, session ID, session order, surface/context label, task-mode label. |
| Attributed assertions | User assertion text or semantic event, source actor, time, context, epistemic status, and distinction from current facts. |
| Observations | Item IDs, task mode, dimension, correctness, scorer provenance, and distinction from derived interpretation. |
| Temporal judgments | Current-authority eligibility or ineligibility, stale-basis judgment, temporal uncertainty, basis event IDs, and no re-dating of historical evidence. |
| Dimension comparison | Recognition evidence refs, production evidence refs, scoped comparison result, uncertainty, and no scalar global skill collapse. |
| Trial candidate | Candidate ID, material intent, source, provisional/evaluative purpose, affordance ref, support lineage, proposed scope, reversibility or correction path, lifecycle status. |
| Proposal binding | Surfaced proposal ref, candidate ref, material-intent match, user response ref, binding assessment, ambiguity or conflict status. |
| Activation checks | Results for scope, basis lineage, current/stale basis, user-governed constraints, reversibility, consequence, current applicability, retention basis, and non-adaptation boundary. |
| Active trial | Active trial ID, activation time, scope, activation basis, retained-state identity, lineage to candidate and checks, narrowing/retirement/supersession status. |
| Direct correction disposition | Current-session behavior disposition, correction-event basis, context scope, and distinction from future trial state. |
| Later-use applicability | Current context, active trial ref, applicability review, selected behavior disposition, and proof that selection occurred before outcome facts. |
| Outcome record | Outcome fact refs, active trial ref, behavior disposition ref, material context lineage, co-intervention status, intervention-conditioned classification, causal uncertainty. |
| Explanation support | User-facing claim refs, retained state refs, uncertainty markers, excluded claim boundaries, and no hidden chain-of-thought requirement. |
| Failure artifacts | Run outcome, invariant or obligation IDs, observed state refs, expected versus actual classification, and claim classes affected. |

Inspection evidence must come from the effective state used by the SUT. A generated explanation, retrospective narrative, or self-described state object cannot be the sole evidence that the state existed or influenced behavior.

## Formal Campaign Metadata

A formal campaign using this contract must pre-register:

- campaign identifier;
- scenario pressure ID and version, `SCN-001 V0.2.2`;
- thesis baseline, `SYSTEM_THESIS.md V0.3.1`;
- state/control baseline, `STATE_AND_CONTROL_MODEL.md V0.4.1`;
- accepted ADR revisions, including `ADR-001 R1`, `ADR-002 R2`, `ADR-003 R2`, and `ADR-004 R3`;
- fixture/oracle package identifier, `SCN001-SSFO-R0`, and each fixture path to be run;
- context-bundle policy, branch policy, and completeness declarations;
- claim classes under evaluation and required path coverage;
- behavior configuration identifier and revision;
- evaluation configuration identifier, including fixture, bundle policy, branch policy, oracle, run-validity policy, replacement policy, and run-selection policy versions;
- SUT implementation or build identifier;
- model, prompt, runtime, and tool configuration where applicable;
- nondeterminism declaration, planned outcome-independent seed or run-selection method, and deterministic replay expectation if claimed;
- oracle version, run-validity criteria, invalid-run replacement policy, and planned valid run count per path.

Run evidence must record actual replay handles, provider run IDs where applicable, actual seeds, runtime trace IDs, observed configuration fingerprints, delivered bundle IDs, SUT output/state capture handles, oracle classification, and any invalidity or failure artifact.

For nondeterministic configurations, the planned valid run count is three fresh valid runs per fixture path. For deterministic replayable configurations, one run per path is sufficient only if the evaluation policy establishes oracle-material state equivalence by replay verification or an inspectable mechanism guarantee.

## Run Validity And Invalid-Run Replacement

A run is valid and scorable when all of these hold:

- the pre-registered fixture/oracle package and path are loaded;
- the SUT starts from the declared initial snapshot or a declared lineage-preserving branch checkpoint;
- no SUT-owned semantic state from another independent evidence run contaminates the run;
- context bundles are delivered according to the pre-registered bundle and branch policy;
- the harness does not supply a prohibited semantic answer;
- oracle-material SUT effective state is captured or the SUT's failure to expose required state is itself attributable to the SUT after material inputs were delivered;
- infrastructure, fixture, or oracle defects do not prevent evaluation of the intended SUT behavior.

`INVALID_UNSCORABLE` is allowed only for fixture, harness, oracle, or infrastructure integrity defects that prevent scoring the intended SUT behavior. Examples:

- wrong fixture or oracle version loaded;
- required input was not delivered or was corrupted before the SUT could respond;
- harness supplied a prohibited semantic conclusion;
- branch policy was applied inconsistently with pre-registration;
- oracle inspected self-report instead of the required effective state because the capture mechanism failed;
- declared lineage-preserving checkpoint cannot be verified because of harness, capture, or oracle integrity failure.

These are not valid invalidity reasons once material SUT behavior has been observed:

- the SUT gave an awkward, incorrect, evasive, or off-policy response;
- the SUT failed to form a required candidate;
- the SUT failed to expose required state after receiving material inputs;
- the SUT produced a hard-invariant violation;
- the run would make the campaign fail.

Replacement policy:

- every invalid attempt remains in campaign history;
- a nondeterministic campaign may attempt at most two `INVALID_UNSCORABLE` replacements per fixture path before campaign review is required;
- two invalid attempts with the same root cause in one path require stop-and-review before further formal runs;
- three total invalid attempts across the campaign require campaign suspension or an accepted evaluation-policy correction;
- invalid attempts must be replaced using the same outcome-independent run-selection policy unless the campaign is superseded;
- a valid hard failure cannot be replaced under invalid-run policy.

Changing expected semantic outcomes because the SUT failed is a contract change, not an oracle correction.

## Formal Run Outcomes

| Outcome | Meaning |
| --- | --- |
| `PASS` | A valid scored run satisfies all hard invariants and all path-specific positive obligations for the pre-registered claim class. |
| `HARD_FAIL` | A valid scored run violates a hard SUT invariant. The behavior-configuration revision cannot support the bounded milestone pass. |
| `OBLIGATION_FAIL` | A valid scored run avoids hard-invariant failure but fails a path-specific required capability or positive obligation. The affected claim class is not evidence-eligible. |
| `INVALID_UNSCORABLE` | A fixture, harness, oracle, or infrastructure integrity defect prevents intended SUT behavior from being evaluated. Not a SUT pass and not automatically a SUT hard fail. |

Claim-boundary violations outside a run are artifact-level outcomes:

| Outcome | Meaning |
| --- | --- |
| `CLAIM_INVALID` | A later report, README, milestone claim, or evidence artifact asserts more than the campaign evidence and accepted claim boundary support. |

If the SUT itself creates unsupported semantic state or a user-facing overclaim during a run, score it as a run-level hard failure rather than only `CLAIM_INVALID`.

## Hard Failures

Hard failures include the invariant failures already listed in `ADR-004` and these path-specific applications:

- the SUT treats old `D-135` or `D-120` evidence as independently current-authoritative under the selected `>90 scenario days` rule;
- the SUT refreshes or re-dates old evidence when current observations corroborate it;
- recognition and production observations collapse into a global particle skill, global Japanese level, learning-style, or identity claim;
- user assertions, observations, derived interpretations, explicit preferences, direct corrections, trial candidates, active trials, outcomes, and durable adaptations become semantically indistinguishable;
- a production-focused trial activates from an unbound, ambiguous, invisible, or silently corrected proposal response;
- a non-active candidate or proposal influences later trial-driven behavior before active transition;
- an active trial is created without inspectable activation checks;
- the later behavior disposition is selected after outcome facts are supplied;
- retained active trial state is reconstructed by the harness or copied from fixture-authored semantic conclusions;
- outcome facts are promoted to proof of long-term learning efficacy, fixed causal theory, fatigue status, global voice preference, or global correction preference;
- the delayed-correction trial is applied in `CF-DRILL-OPT-IN` despite focused drill mode and explicit immediate-correction opt-in;
- the SUT claims real voice behavior, real personal memory, durable developmental adaptation, Japanese pedagogy quality, statistical reliability, or full `SCN-001` pass from this fixture set;
- final explanation fabricates, contradicts, or claims support not present in retained inspected state.

## Positive-Obligation Failures

Positive-obligation failures prevent the affected claim class from passing without necessarily violating a hard invariant.

Examples:

- canonical path never forms or selects an evidence-responsive production-focused trial candidate despite sufficient current recognition/production evidence;
- SUT forms a candidate but never surfaces a candidate-bound proposal where the selected activation basis requires one;
- SUT surfaces a proposal but does not expose proposal-response binding;
- SUT refuses all selected-slice trial behavior permanently, while also avoiding a valid insufficiency, conflict, or clarification basis;
- SUT handles the immediate current-session correction but never creates, withholds, or explains a separate future delayed-correction trial candidate;
- applicable retained active trial state fails to influence later behavior disposition before outcome evidence;
- outcome evidence is discarded entirely despite being valid intervention-conditioned evidence in the canonical path;
- explanation support is missing required retained-state references while avoiding fabricated claims;
- `CF-RECENT-BASIS` recent evidence is marked stale without a pre-registered material invalidation, but the SUT does not otherwise create forbidden state.

## Failure Artifact Requirements

Each failure artifact must include:

- campaign ID and run ID;
- path ID and claim class;
- behavior configuration ID and evaluation configuration ID;
- fixture/oracle package version;
- outcome classification;
- invariant ID, obligation ID, invalidity criterion, or claim-boundary ID;
- observed state refs, output refs, or missing-state evidence;
- expected condition and actual observed condition;
- whether the failure affects the run, claim class, campaign, or later artifact only;
- correction or supersession status if an oracle or evaluation-policy correction is later accepted.

`CLAIM_INVALID` artifacts must also include the unsupported claim text, the artifact that made the claim, the evidence actually available, the maximum supported bounded claim, and the required correction or withdrawal.

## Bounded Claim Language

If accepted, implemented, and passed under `SLICE-005`, this contract may support only bounded language of this form:

```text
Under synthetic SCN-001 selected-slice fixture context `SCN001-SSFO-R0`,
accepted ADR-001 through ADR-004, and the declared behavior/evaluation
configuration, the tested configuration preserved and transitioned selected
semantic state across curated-context interactions for the registered claim
classes. Oracle-visible effective state distinguished attributed assertions,
observations, temporal eligibility, scoped trial candidates, activation checks,
retained active trial state, later-use applicability, intervention-conditioned
outcomes, and bounded explanation support.
```

This contract does not support claims that:

- Zoey passed full `SCN-001`;
- Zoey has a complete growth system or durable developmental adaptation;
- Zoey knows the user's real Japanese level or learning style;
- Zoey teaches Japanese well;
- immediate correction or delayed correction is generally effective;
- voice users prefer delayed correction;
- the tested system performs retrieval, memory search, relevance ranking, or context assembly;
- the result estimates statistical reliability, production readiness, or general robustness;
- the system has real personal-memory custody, durable Zoey continuity, real voice/avatar behavior, or external-operation safety.

## Downstream Contract

`SLICE-002` may derive only the minimum selected-slice state needed to expose the fields in this fixture/oracle contract. It must not infer a general memory architecture, retrieval architecture, durable adaptation schema, or production retention policy.

`SLICE-005` must decide the acceptance gate using the claim-class matrix, formal campaign policy, hard-invariant rules, positive-obligation aggregation, invalid-run replacement policy, and bounded claim language above. It must reject evidence based on cherry-picked nondeterministic runs, unlimited invalid-run replacement, or repeated campaigns under the same materially unchanged behavior and evaluation configuration.

## Non-Scope

This draft does not decide:

- final data schemas or serialization format;
- implementation repository structure;
- model, runtime, prompt, or agent design;
- retrieval, embeddings, summaries, adapters, or context assembly;
- production memory custody or retention policy;
- real voice, STT, TTS, avatar, or product UI;
- Japanese curriculum or grading quality;
- durable developmental adaptation;
- full longitudinal drift detection;
- statistical reliability or production rollout gates;
- full evaluation-record metadata beyond the campaign fields needed here;
- full `SCN-001` scenario acceptance.
