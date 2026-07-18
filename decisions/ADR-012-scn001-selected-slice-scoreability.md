# ADR-012: SCN-001 Selected-Slice Scoreability

Status: `Proposed`

Date: 2026-07-18

Record revision: `R1`

Decision authority: project owner

Target question IDs: `EVAL-005`, `GROW-002`

Decision-Time Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.22`
- `decisions/ADR-003-scn001-selected-slice-trial-time-contract.md` `R2`
- `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md` `R3`
- `decisions/ADR-005-scn001-selected-slice-fixture-oracle-contract.md` `R2`
- `decisions/ADR-009-scn001-first-selected-slice-milestone-completion-gate.md` `R4`

Proposal dependencies: `ADR-010 R1` and `ADR-011 R1` are the proposed
behavior-identity and formal-record-authority contracts. This ADR may be
reviewed in parallel and may be accepted only in an owner decision set that also
accepts, or follows, compatible `EVAL-004` and `EVAL-007` resolutions.

## Decision

Define selected-slice scoreability as eligibility to make one bounded,
conjunctive, nonnumeric formal pass/fail determination under the accepted
fixture/oracle and campaign policy.

All five `ADR-005 R2` claim classes remain mandatory and non-substitutable:

1. `CC-TIME-STALE-BASIS`;
2. `CC-EVIDENCE-TRIAL-FORMATION`;
3. `CC-SCOPE-TRIAL-USE`;
4. `CC-OUTCOME-SEMANTICS`;
5. `CC-EXPLANATION-PROVENANCE`.

This ADR instantiates `ADR-004 R3` and `ADR-005 R2`. It does not redefine
`EVAL-003`, invent a weighted score, or merge validity, hard failure,
obligation result, and lifecycle into one status enum.

For this milestone, resolve `GROW-002` by a named bounded exclusion:

```text
For fixture/oracle package SCN001-SSFO-V0.2.0 and the first synthetic
selected-slice milestone, general longitudinal agreement-drift,
anti-correction-drift, and personality-drift detection are not evaluated
and cannot be claimed.
```

No working assumption supplies that missing capability.

## Scoreability Versus Other Results

Keep these determinations distinct:

```text
run validity                  -> can the intended SUT behavior be scored?
run-global invariant result   -> did a valid run violate a hard invariant?
per-claim obligation result   -> did each pressured claim class pass?
campaign lifecycle            -> is the campaign active, suspended, closed...?
bounded campaign result       -> PASS, FAIL, or not yet determinable
completion determination D    -> are all ADR-009 eligibility conjuncts met?
owner disposition A           -> does the owner accept eligible D?
```

A bounded campaign pass is necessary but not sufficient for completion
eligibility. Engineering promotion, evidence-package, claim-closure, basis-
freshness, and owner-disposition requirements remain in `ADR-009 R4`.

## Inherited Orthogonal Result Domains

### Run Validity

Use exactly the accepted `ADR-005 R2` domain:

- `VALID`;
- `INVALID_UNSCORABLE`.

Invalidity is limited to declared fixture, harness, oracle, simulator, capture,
or infrastructure integrity defects that prevent evaluation of intended SUT
behavior. Awkward, wrong, evasive, off-policy, or claim-failing SUT behavior is
not invalidity.

### Run-Global Hard-Invariant Result

Use exactly:

- `INVARIANTS_CLEAR`;
- `HARD_FAIL`.

A valid hard failure is formal adverse evidence and globally disqualifies the
exact behavior fingerprint from the bounded milestone pass under `ADR-004 R3`.
It is not averaged, isolated to one class, or reset by a later favorable run or
evaluation-only change.

### Per-Claim Obligation Result

For every pre-registered path/claim-class combination, use exactly:

- `PASS`;
- `OBLIGATION_FAIL`;
- `NOT_REACHED`;
- `NOT_APPLICABLE`.

`NOT_REACHED` is non-passing for required coverage. It explains that an earlier
SUT-owned prerequisite failed; it does not turn the run invalid or satisfy the
downstream class.

`NOT_APPLICABLE` is allowed only where the authoritative `ADR-005 R2`
obligation map declares the path non-pressure for that class. It cannot be used
for a required path/claim combination or as a substitute for missing evidence.

### Lifecycle

Run-attempt and campaign lifecycle consume the accepted `EVAL-007` authority
contract. `suspended`, `authority_invalidated`, and `superseded` are lifecycle/
history meanings, not substitutes for the result domains above.

## Required Path And Claim Coverage

The complete required path set is:

- `SCN001-SSFO-V0.2.0-CANONICAL-THIN`;
- `SCN001-SSFO-V0.2.0-CF-CALIBRATION-NO-SPLIT`;
- `SCN001-SSFO-V0.2.0-CF-DRILL-OPT-IN`;
- `SCN001-SSFO-V0.2.0-CF-RECENT-BASIS`.

The authoritative path-to-claim and positive-obligation mapping remains the
`ADR-005 R2` Claim-Class Obligation Map. Every applicable package-local
positive obligation must map to at least one mandatory claim/path combination
as required by `ADR-009 R4`. An unmapped or silently omitted applicable
obligation is a contract defect, not a pass.

Canonical path evidence may support multiple classes only when each class's
distinct obligations are independently classified for every applicable formal
run. Evidence from one counterfactual cannot substitute for another claim
class's required pressure.

## Deterministic Qualification And Formal Run Count

The current workbench appears deterministic, but a label, fixed seed, or one
successful replay is insufficient.

Before a campaign uses the one-formal-run rule, preflight must perform at least
two clean independent executions of every required path under the exact same
behavior and evaluation fingerprints. Each execution starts from the declared
initial state or same-run branch prefix and uses the planned capture/simulator
pipeline.

The two executions must produce equivalent oracle-material state and evidence:

- same path/checkpoint reachability;
- same run validity and hard-invariant classification;
- same per-claim obligation vector;
- same required retained semantic families, identities relative to run-local
  allocation, typed relations, transition envelopes, and material ordering;
- same simulator request/realization meaning and fidelity classification;
- same explanation grammar classification and support closure.

Exact UUIDs, timestamps, storage refs, and other declared run-local identities
need not be byte-equal. Natural wording may vary only within accepted bounded
variance and must not alter oracle-material classification.

Preflight artifacts are integrity-sealed for review but remain explicitly
`development_preflight`, not formal evidence, and may never be promoted into
the campaign.

If deterministic qualification passes, require one prospectively authorized,
sealed formal run per required path. If it fails or cannot be established,
classify the configuration as nondeterministic and require three fresh valid
formal runs per required path under `ADR-004 R3`.

Any later oracle-material divergence under unchanged fingerprints invalidates
the deterministic qualification for future use and triggers campaign review.

## Invalid Attempts And Replacement

The campaign authorization copies the accepted `ADR-005 R2` replacement policy
without alteration:

- every invalid attempt remains in formal history;
- at most two invalid replacements per fixture path before campaign review;
- two invalid attempts with the same root cause in one path require stop and
  review before more formal runs;
- three total invalid attempts across the campaign require suspension or an
  accepted evaluation-policy correction;
- replacement uses the same outcome-independent selection policy;
- a valid hard failure is never replaceable as invalid.

Replacement eligibility is decided from integrity evidence and pre-registered
reason codes without inspecting whether the SUT outcome would help or hurt the
campaign. Exhausted replacement budget leaves the campaign suspended or not
scoreable; it does not convert missing valid coverage into pass or SUT fail.

## Configuration Change And Campaign Disposition

Consume the accepted configuration identity/authority contracts as follows:

| Change class | Consequence |
| --- | --- |
| Envelope-only editorial/provenance change with unchanged content fingerprint | Same configuration identity; no campaign split. |
| Behavior identity change | New behavior configuration and new campaign; prior evidence stays with the original fingerprint. |
| Material evaluation identity change | New evaluation configuration and campaign; unchanged behavior is not rehabilitated from a valid prior hard failure. |
| Fixture/oracle semantic or obligation-map change | New evaluation identity and package/ADR re-triage where required; no silent rescoring. |
| Material runtime/toolchain/environment change | New applicable behavior or evaluation identity according to ownership; unresolved ownership blocks comparison. |
| Unknown, missing, or unsupported comparison | `COMPARABILITY_UNRESOLVED`; no aggregation, evidence transfer, or compatibility claim. |

Campaign supersession preserves the earlier campaign, all attempts, outcomes,
corrections, and indexes. Repeating a failed campaign under materially unchanged
behavior/evaluation fingerprints cannot create a pass.

## Bounded Campaign Result

A campaign is ready for a bounded result only when:

- compatible accepted `EVAL-004` and `EVAL-007` contracts are in force;
- behavior/evaluation manifests and prospective campaign authorization validate;
- authority-namespace and campaign evidence indexes close the record universe;
- run selection, attempt allocation, invalidity, replacement, suspension, and
  supersession history satisfy accepted policy;
- required path/claim and obligation-map closure is complete;
- every required artifact is sealed, reference-resolvable, and within cutoff;
- the unresolved-question matrix below has no undispositioned claim-affecting
  question or undeclared working assumption;
- the exact bounded claim text and exclusion language are bound to the result.

Then:

```text
BOUNDED_PASS =
    every required valid formal run has INVARIANTS_CLEAR
    AND every mandatory path/claim result is PASS
    AND all five claim classes are evidence-eligible

BOUNDED_FAIL =
    an authoritative valid HARD_FAIL exists
    OR a mandatory path/claim result is OBLIGATION_FAIL or NOT_REACHED
    OR a mandatory claim class is otherwise non-passing under complete,
       valid campaign closure

NOT_YET_DETERMINABLE =
    authority, validity, replacement, coverage, comparison, question,
    or evidence-universe closure remains unresolved
```

A campaign may close as bounded failure immediately after an authoritative
valid hard failure if the pre-registered global-disqualification rule is
applied and every unused attempt is explicitly dispositioned. Otherwise, the
planned attempt set must reach accepted closure; optional stopping is forbidden.

These names define semantic outcomes, not a required single status field.
Campaign lifecycle remains separate.

## Unresolved-Question Matrix

This matrix classifies every unresolved register family that could be mistaken
for a prerequisite or silently imported into the selected claim.

| Question IDs | Disposition for this milestone | Claim effect / future trigger |
| --- | --- | --- |
| `EVAL-004`, `EVAL-007` | Blocking dependencies. | Must resolve in the same or an earlier owner decision set before this ADR becomes effective or a formal claim campaign is authorized. |
| `GROW-002` | Milestone-bounded exclusion; no fixture assumption. | General longitudinal agreement/anti-correction/personality drift is not evaluated or claimable. Later scope creates a new linked question. |
| `DEP-003` | Trigger absent; irrelevant to current run-scoped campaign. | No expiry, refresh, revocation maintenance, or background lifecycle claim. Trigger before such runtime maintenance enters the campaign. |
| `MEM-001`, `MEM-002`, `MEM-003`, `MEM-004`, `MEM-005`, `CONT-002`, `TRUST-001` | Trigger absent; outside the synthetic claim. | Fixture state is disposable evaluation state, not real personal memory or continuity. Formal evidence indexes are evaluation/governance artifacts, not SUT control-relevant derived personal state. No materially different inference trust boundary is used. Trigger before real retention, reuse, custody, or inference routing. |
| `DEP-002`, `DEP-004` | Trigger absent; outside the declared mechanism/claim. | No general non-convergence engine, component operation, or grouped workflow state is evaluated. |
| `TIME-001` | Trigger absent; outside the claim under accepted `TIME-002`. | No scheduler, TTL, due state, background clock, or full longitudinal governed-clock claim. |
| `GROW-003`, `GROW-004`, `GROW-005` | Trigger absent; outside the claim. | Configuration identity does not establish replacement continuity, continuity adoption, or durable user-facing adaptation. Trigger before using results for replacement/continuity or durable adaptation. |
| `INIT-001`, `INIT-002` | Trigger absent; outside the claim. | No proactive initiative or arbitration claim. |
| `AUTH-001`, `AUTH-002`, `AUTH-003`, `AUTH-004`, `AUTH-005`, `AUTH-006` | Trigger absent; outside the selected `SCN-001` synthetic path. | No real external operation, standing authority, operation lifecycle, or quoted-content instruction claim. |
| `SURF-001`, `SURF-002` | Trigger absent; outside the claim. | Fixture surface labels and simulated realizations do not establish a real second surface, voice contract, or voice behavior. |
| `LEG-001`, `LEG-002`, `LEG-003`, `LEG-004`, `LEG-005` | Trigger absent; outside the claim. | No legacy component is migrated, reused as authority, or needed by the formal campaign. |
| `PROD-001`, `PROD-002`, `PROD-003`, `PROD-005` | Trigger absent; outside the claim. | No user-facing workflow, memory control, presence demo, or plan promotion is evaluated. |
| `CONT-001` | Trigger absent; outside the claim. | No restore, migration, disconnection, or state-loss continuity claim. |
| `REPO-001` | Trigger absent. | Campaign artifacts remain in the governed workbench; trigger before durable `projects/` extraction. |

No `ASM-*` working assumption is accepted or required by this decision. If a
future implementation needs one, `EVAL-005` cannot be treated as resolved for
that changed basis without register re-triage and owner acceptance.

## GROW-002 Bounded Exclusion

The excluded capability is general longitudinal detection of:

- agreement drift that rewards the latest user statement regardless of retained
  contradictory evidence;
- anti-correction drift that increasingly resists or over-applies corrections
  across a longer trajectory;
- personality or global-preference drift inferred from repeated interactions.

The selected fixture still evaluates exact scoped state transition, current
correction, delayed correction, later applicability, bounded outcome, and
grounded explanation across its named synthetic chronology. That finite path is
not a general drift detector.

Allowed claim: the tested configuration passed or failed the five named claim
classes for `SCN001-SSFO-V0.2.0` under the exact formal campaign.

Forbidden claim: the tested configuration resists longitudinal agreement,
anti-correction, preference, personality, or adaptation drift in general.

If a later milestone brings that capability into scope, create a new linked
question because resolved IDs are not reopened.

## Explanation-Grammar Claim Ceiling

The finite selected-slice explanation grammar can establish only that, on the
registered paths and exact evaluation configuration:

- the emitted explanation belongs to the accepted finite semantic grammar;
- required limitations are present;
- forbidden causal, global, permanent, learning-style, efficacy, fatigue,
  focused-drill, or hidden-reasoning claims are absent within that grammar;
- typed retained-state and transition support closes under the oracle.

It does not establish safety or truthfulness for arbitrary natural-language
explanations, unseen paraphrases, other languages, production model outputs, or
unbounded conversation. The grammar revision/fingerprint is part of evaluation
identity; expanding accepted wording is an evaluation-configuration change with
new regression and campaign consequences.

## Maximum Bounded Claim

Only claim language of this form may close the campaign result:

```text
Under synthetic SCN-001 selected-slice fixture/oracle package
SCN001-SSFO-V0.2.0, the exact declared behavior and evaluation configuration,
and the authoritative formal campaign and evidence cutoff, the tested behavior
configuration [passed|failed] the conjunctive gate across the five mandatory
selected-slice claim classes.
The result covers curated-context temporal handling, evidence-responsive trial
formation, scoped trial use, intervention-conditioned outcome semantics, and
bounded explanation provenance on the registered paths. It does not establish
full SCN-001 success, general longitudinal drift resistance, retrieval,
production memory, durable adaptation, real voice behavior, Japanese teaching
quality, statistical reliability, production readiness, or real continuity.
```

Use the exact behavior/evaluation fingerprints, campaign ID, evidence-universe
index fingerprint, and cutoff in the claim-bearing artifact. Replace
`[passed|failed]` with the actual result of the conjunctive gate across the five
mandatory claim classes. A failure artifact must also name the decisive hard
failure, non-passing class/path result, or unresolved closure; it must not imply
that every class was reached when an early global hard failure ended the
campaign.

## Adversarial Review Requirements

Before acceptance or implementation, reviewers must reject a design that:

- creates one flat enum mixing validity, hard failure, claim result, and
  lifecycle;
- treats `NOT_REACHED`, `NOT_APPLICABLE`, invalidity, suspension, or
  supersession as pass;
- averages, weights, votes, or substitutes among the five mandatory classes;
- substitutes one counterfactual path for another class's required pressure;
- claims determinism from a label, fixed seed, or one replay;
- promotes deterministic preflight artifacts into formal evidence;
- replaces invalid attempts after inspecting whether the SUT outcome was
  favorable;
- exceeds accepted invalid replacement limits or silently discards attempts;
- changes evaluation configuration to reset an unchanged behavior failure;
- treats configuration fingerprints as semantic continuity or replacement
  evidence under `GROW-003`/`GROW-004`;
- represents `GROW-002` as a fixture assumption or claims general drift
  resistance from the bounded trajectory;
- treats finite grammar success as arbitrary-language safety;
- calls a campaign pass milestone completion or owner acceptance;
- begins Phase 7 formal claim implementation before all three active evaluation
  decisions and current governance/review gates resolve.

## Consequences

Positive consequences:

- the milestone has a deterministic, conjunctive, nonnumeric result;
- accepted run semantics remain orthogonal and diagnostically useful;
- deterministic economy is allowed only after explicit reproducibility proof;
- every unresolved question has an explicit claim disposition;
- `GROW-002` cannot be silently overclaimed;
- explanation evidence remains bounded to what the finite oracle can test.

Costs and limitations:

- deterministic preflight requires at least eight non-formal path executions;
- all four required paths and five claim classes must close;
- unresolved record authority, missing evidence, or exhausted invalidity budget
  prevents a result rather than producing a convenient fail/pass;
- the result is not statistical reliability, production readiness, or full
  scenario acceptance.

## Acceptance Effect

If the project owner accepts this exact revision after compatible accepted
`EVAL-004` and `EVAL-007` decisions:

- `EVAL-005` becomes `Resolved` with outcome `Decision` for the first synthetic
  selected-slice milestone;
- `GROW-002` becomes `Resolved` with outcome `Bounded exclusion` for
  `SCN001-SSFO-V0.2.0`, with a future linked-question trigger;
- no `ASM-*` entry is created;
- `OPEN_QUESTIONS.md` gains both resolved tombstones and re-triages dependent
  questions/claims;
- engineering standard/profile sources must be re-triaged and projected;
- Phase 7 may implement the accepted formal campaign/scoreability contract only
  after current workbench review and governance promotion controls are
  satisfied.

Acceptance does not itself declare the workbench behavior compatible, authorize
or run a campaign, create formal evidence, produce completion package `P`,
determine `D`, record owner disposition `A`, or complete the milestone.

Until acceptance, this document is a proposal and authorizes none of those
actions.

## Reconsideration Triggers

Reconsider this decision if:

- deterministic preflight cannot establish oracle-material equivalence;
- the accepted fixture/oracle package changes its path, claim, obligation, or
  invalidity semantics;
- a later milestone requires statistical reliability, full `SCN-001`, general
  longitudinal drift, retrieval, real personal continuity, production memory,
  durable adaptation, real voice, pedagogy quality, or production readiness;
- a new unresolved question materially affects a required obligation or claim;
- the finite explanation grammar cannot represent the bounded supported
  explanations without hiding material variance.

## Non-Decisions

This ADR does not decide:

- behavior/evaluation manifest schemas or record authority beyond consuming
  accepted `EVAL-004` and `EVAL-007` contracts;
- new run validity, hard-invariant, obligation, invalidity, replacement, or
  selection semantics outside `ADR-004 R3` and `ADR-005 R2`;
- completion package `P`, determination `D`, owner disposition `A`, or current
  post-acceptance claim standing beyond `ADR-009 R4`;
- statistical thresholds, confidence intervals, production rollout, real
  memory, retrieval, voice, avatar, Japanese pedagogy, durable adaptation,
  trust-boundary architecture, or repository extraction.
