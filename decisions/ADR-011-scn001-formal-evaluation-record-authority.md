# ADR-011: SCN-001 Formal Evaluation Record Authority

Status: `Proposed`

Date: 2026-07-20

Record revision: `R2`

Decision authority: project owner

Target question IDs: `EVAL-007`

Decision-Time Baselines:

- `SYSTEM_THESIS.md` `V0.3.1`
- `CANONICAL_SCENARIOS.md` `V0.2.2`
- `STATE_AND_CONTROL_MODEL.md` `V0.4.1`
- `OPEN_QUESTIONS.md` `V0.2.22`
- `decisions/ADR-002-scn001-system-under-test-boundary.md` `R2`
- `decisions/ADR-004-scn001-first-milestone-evaluation-policy.md` `R3`
- `decisions/ADR-005-scn001-selected-slice-fixture-oracle-contract.md` `R2`
- `decisions/ADR-007-scn001-selected-slice-dependency-identity.md` `R3`
- `decisions/ADR-009-scn001-first-selected-slice-milestone-completion-gate.md` `R4`

Proposal dependency: `ADR-010 R2` is the proposed behavior-configuration
identity contract. This ADR may be reviewed in parallel and may be accepted only
in an owner decision set that also accepts, or follows, a compatible `EVAL-004`
resolution.

## Decision

Adopt a prospective, manifest-bound, append-preserving formal-evaluation
authority contract for the first synthetic `SCN-001` selected-slice milestone.

Use six distinct artifact families:

1. immutable evaluation-configuration manifest;
2. prospective deterministic-qualification plan and immutable qualification-
   result records;
3. prospective campaign-authorization manifest;
4. immutable run-attempt records and replayable evidence artifacts;
5. immutable correction, reclassification, run-invalidity, authority-
   invalidation, and supersession records;
6. frozen authority-namespace and campaign evidence indexes that establish the
   formal-evidence universe and cutoff.

These artifacts may be stored as package-local files in the governed workbench.
No database or new durable system-project repository is required. Formal
authorization does require the prospective external ordering anchor defined
below. The storage representation must provide one declared authority namespace
in which qualification history, prospective campaign authorizations, and every
resulting formal attempt are discoverable and cut off through immutable indexed
artifacts.

## Identity, Authority, Validity, And Outcome

The contract keeps these properties separate:

```text
configuration identity = what behavior and evaluation policy were bound
record authority       = whether formal production was prospectively authorized
record validity        = whether the intended SUT behavior was evaluable
evaluation outcome     = what the accepted oracle concluded
evidence completeness  = whether the declared authority universe is closed
```

An authoritative record may contain a hard failure, obligation failure, or
invalid attempt. Authority is not success. A valid content fingerprint without
prospective authorization is development evidence, not a formal record.

## Evaluation-Configuration Manifest

Every campaign binds one immutable evaluation-configuration manifest by opaque
identifier, evaluation fingerprint, and manifest-artifact fingerprint. Its
identity payload records:

- a closed evaluator source/build member index or tree digest covering
  `scn001_eval/**`, material fixture/oracle/checkpoint tests, formal schemas,
  simulator/capture code, and behavior-affecting shared/generated evaluator
  inputs;
- evaluator package/build identity, exact resolved transitive dependency
  closure, and runtime/toolchain identity;
- fixture/oracle package `SCN001-SSFO-V0.2.0` or accepted successor;
- exact required fixture paths, bundles, branch policy, completeness
  declarations, checkpoint contract, oracle rule catalogue, and claim-class
  obligation map;
- simulator source/configuration and renderer/realization grammar identity;
- formal record, capture, evidence, correction, and index schema revisions;
- run-validity criteria and invalidity reason catalogue;
- invalid-run replacement limits and stop/review policy inherited from
  `ADR-005 R2`;
- outcome-independent run/seed selection method;
- deterministic-replay qualification policy, deterministic-equivalence profile
  identifier/revision, comparator implementation fingerprint, and closed
  normalization/exclusion rules, or a nondeterministic declaration;
- planned valid run count per required path inherited from `ADR-004 R3`;
- governing thesis, scenario, state/control, ADR, register, engineering, and
  fixture/oracle revisions;
- behavior-relevant evaluator environment and external dependency identity;
- evaluator-private artifact custody and access policy.

Its immutable provenance records the combined-repository identity, full source
commit, root package/lock digests, worktree state, and reconstruction evidence.
Those provenance fields do not change evaluation identity by themselves. A
SUT-only commit therefore leaves evaluation identity unchanged when the closed
evaluator source, dependency, runtime, governing basis, and policy payload is
unchanged; an evaluator checkpoint/oracle/test change covered by the closure
changes evaluation identity without changing behavior identity.

The evaluation manifest uses the same envelope/payload/assertion separation,
`RFC8785-JCS` canonicalization revision, SHA-256 algorithm, typed applicability
discipline, provenance treatment, and alias rules as proposed `ADR-010 R2`,
with behavior-independent hash domains:

```text
evaluation payload:  zoey:evaluation-configuration:v1
manifest assertion:  zoey:evaluation-configuration-manifest:v1
```

Its identity is separate from behavior identity. A campaign manifest binds one
of each; neither fingerprint includes the other.

A formal evaluation requires a clean evaluator worktree, or an exact immutable
patch/source bundle digest that reconstructs every evaluator-affecting
difference from the named commit and reproduces the declared evaluator closure.
A bare `dirty` state is ineligible for campaign authorization.

## Canonical Artifact Identity

Every artifact family in this ADR uses an immutable envelope plus one canonical
identity payload. The envelope holds the opaque artifact ID, storage/custody
location, content fingerprint, and non-semantic annotations. The identity
payload holds every field material to authorization, configuration, evidence,
classification, lifecycle, ordering, cutoff, or supersession. Every identity
payload includes `schema_id`, `schema_revision`, and an exact `artifact_kind`.
Grouped families additionally require `decision_kind` or `evidence_kind` from a
closed catalogue. The fingerprint field and storage location are never hashed
into themselves.

V1 `decision_kind` is exactly `RUN_INVALIDITY`, `AUTHORITY_INVALIDATION`,
`RECORD_CORRECTION`, `ORACLE_POLICY_RECLASSIFICATION`,
`CAMPAIGN_SUPERSESSION`, or `NAMESPACE_RECONCILIATION`. V1 `evidence_kind` is
exactly `SUT_INPUT_CAPTURE`, `SUT_OUTPUT_CAPTURE`, `SUT_INSPECTION_CAPTURE`,
`SIMULATOR_REQUEST_CAPTURE`, `SIMULATOR_REALIZATION_CAPTURE`,
`EVALUATOR_PRIVATE_CAPTURE`, or `RAW_BINARY_ATTACHMENT`. Adding or changing a
kind requires the corresponding schema/domain revision; a free-form subtype is
invalid.

All V1 identity payloads use `RFC8785-JCS`, canonicalization revision `1`,
SHA-256, and `sha256:` plus 64 lowercase hexadecimal characters. Each family
has a separate hash domain:

| Artifact family | Hash domain |
| --- | --- |
| Evaluation configuration | `zoey:evaluation-configuration:v1` |
| Evaluation-configuration manifest assertion | `zoey:evaluation-configuration-manifest:v1` |
| Deterministic-qualification plan | `zoey:deterministic-qualification-plan:v1` |
| Deterministic-qualification result | `zoey:deterministic-qualification-result:v1` |
| Campaign authorization | `zoey:campaign-authorization:v1` |
| Formal run-attempt record | `zoey:formal-run-record:v1` |
| Replayable simulator/capture evidence | `zoey:formal-evidence-artifact:v1` |
| Invalidity/correction/reclassification/supersession decision | `zoey:evaluation-decision:v1` |
| Campaign evidence index | `zoey:campaign-evidence-index:v1` |
| Authority-namespace index | `zoey:authority-namespace-index:v1` |

For each row, compute:

```text
sha256(utf8(hash_domain + "\n") || RFC8785_JCS(identity_payload))
```

The opaque ID and content fingerprint are both required at every cross-artifact
reference. Behavior/evaluation manifest references additionally carry their
payload fingerprint and manifest-artifact fingerprint. A matching ID with a
different artifact fingerprint, a payload fingerprint inconsistent with its
manifest assertion, or a matching fingerprint under another domain/schema
revision is a closure failure. Future canonicalization, included-field, or
hash-construction changes require new schema/domain revisions.

## Field Authority And Conflict Closure

Repeated values are references, never competing declarations. They must be
canonically equal to the sole authority below; conflict is an authority-closure
failure and never `latest wins`.

| Field family | Sole authority | Referencing artifacts |
| --- | --- | --- |
| SUT behavior payload | Behavior manifest | Campaign, qualification, run, indexes |
| Fixture/oracle semantics, required paths, claim/obligation map, validity and deterministic-equivalence policy | Evaluation manifest | Qualification, campaign, run, indexes |
| Qualification allocation and comparison basis | Qualification plan | Qualification result, campaign |
| Qualification observations and result | Qualification result | Campaign, indexes |
| Planned formal attempt set, contingency slots, selection/replacement rules, and custody plan | Campaign authorization | Run, campaign index |
| Actual attempt capture and initial classification | Sealed run record | Decisions, campaign index |
| Post-seal correction, authority invalidation, or reclassification | Effective evaluation decision record | Run history, indexes, completion package |
| Scoreability aggregation | Accepted `ADR-012` implementation over the frozen closure | Campaign-result/completion artifacts |

For this selected-slice claim campaign, campaign authorization must repeat the
evaluation manifest's complete required path/claim set and may not narrow,
weaken, or replace fixture/oracle semantics, validity criteria, run counts, or
replacement limits. A run cannot introduce an undeclared path, slot, policy,
or claim. A stricter prospective campaign stop condition is allowed only when
the evaluation manifest explicitly declares that extension point and the
campaign still cannot obtain a pass with less evidence than the manifest
requires.

## Deterministic-Qualification Authority

Deterministic qualification is support for choosing the formal run-count rule;
its executions are not formal SUT evidence. It uses two immutable subtypes.

Before any qualification output is observed, a qualification plan fixes:

- behavior and evaluation manifest IDs and both payload/artifact fingerprints;
- every required path and the exact qualification execution slots;
- initial-state, isolation, capture, and simulator policy;
- deterministic-equivalence profile/revision and comparator implementation
  fingerprint;
- outcome-independent allocation and the rule that invalid, missing, or
  divergent preflight output cannot be discarded or retried into qualification;
- producer, distinct validator role, custody, and prospective anchor evidence.

The qualification plan must satisfy the same external anchor profiles defined
for campaign authorization before its first material preflight output. In that
application, substitute the qualification plan for the authorization manifest
and require the cumulative namespace index to include the plan.

The sealed qualification-result record contains:

- plan ID/fingerprint and behavior/evaluation identity closure;
- every planned execution ID, path, capture, and evidence digest;
- normalized oracle-material projections and comparator inputs;
- equivalence result, mismatch class, and divergence details for every pair or
  declared all-member comparison;
- `QUALIFIED`, `NOT_QUALIFIED`, or `INCONCLUSIVE` result;
- producer and distinct validator identity and validation result;
- result fingerprint and any supersession link.

All qualification plans/results appear in the authority namespace and in the
support closure of any campaign that uses one formal run per path. A campaign
authorization may reference only a prospectively anchored, sealed `QUALIFIED`
record for the same exact behavior/evaluation fingerprints. No campaign ID is
included in the qualification result, avoiding a circular authorization
dependency; the later campaign references the already sealed result.

The first anchored qualification plan for an exact behavior/evaluation pair is
the sole plan eligible to establish the one-run rule. `NOT_QUALIFIED` or
`INCONCLUSIVE` selects the three-run policy; repeating new plans under unchanged
fingerprints until one qualifies is forbidden. A later qualifying plan requires
a new applicable configuration identity or an independently reviewed, owner-
accepted correction proving that the earlier qualification record itself had
an authority defect. The earlier plan/result remains indexed.

## Prospective Campaign Authorization And Anchor

A campaign preflight authorizes only future formal record production. It never
promotes historical development or exploratory runs.

Before the first material SUT output for any formal attempt, the campaign must
have an immutable authorization manifest containing:

- campaign identifier;
- authority namespace identifier;
- behavior manifest identifier and behavior fingerprint;
- behavior manifest-artifact fingerprint;
- evaluation manifest identifier, evaluation fingerprint, and manifest-
  artifact fingerprint;
- scenario, fixture/oracle package, claim classes, required paths, and mandatory
  obligation-map identity;
- deterministic/nondeterministic classification and its evidence basis;
- deterministic-qualification plan/result references when the one-run rule is
  used, otherwise the explicit nondeterministic declaration;
- planned attempt slots or the deterministic rule that allocates them before
  their material outputs are observed;
- prospectively allocated deterministic-divergence contingency slots or the
  rule that campaign supersession is mandatory if qualification later fails;
- planned valid run count per path;
- outcome-independent selection/seed rule and disposition of known exploratory
  outcomes, seeds, replay handles, cached realizations, or candidate pools;
- inherited invalidity, replacement, stop, suspension, and correction rules;
- replayable-evidence storage/custody locations and access boundaries;
- campaign authority identity, authorization time, and authorization result;
- prospective anchor profile, target authority ref/custody, and required anchor
  evidence shape;
- authorization manifest fingerprint.

The campaign authority is the project owner unless an accepted governance
artifact explicitly delegates that role for this milestone. A validator may
confirm preflight mechanically, but it does not create strategic authority by
calling itself authoritative.

Self-authored timestamps, local file mtimes, local Git commits, and mutable
branch labels do not prove prospective order. Before the first material formal
output, both the authorization and the cumulative namespace-index revision that
includes it must be committed and published through one declared anchor profile:

- `PROTECTED_REMOTE_GATE`: fast-forward publish the exact commit to the declared
  non-rewrite authority ref, then obtain a platform-issued immutable gate/event
  identity for that exact commit before starting any attempt; or
- `INDEPENDENT_PREOUTPUT_ATTESTATION`: an actor independent of campaign
  production records the exact authorization/index fingerprints and immutable
  commit identity in separately controlled custody before attempt start.

Every attempt records the anchor profile, repository/authority ref, exact commit
SHA, external gate/event or attestation identity, and observed predecessor.

The anchor must also establish a causal post-anchor execution start; ordering a
manifest before a claimed timestamp is insufficient if old output can be
replayed. Use one of:

- `GATE_LAUNCHED_ATTEMPT`: the successful external gate creates a fresh attempt
  challenge/nonce and launches the exact declared command/capture pipeline; or
- `INDEPENDENT_START_ATTESTATION`: the independent attestor creates a fresh
  challenge/nonce after anchoring and observes the attempt start and capture
  binding.

The challenge belongs to the evaluator-private capture envelope, not SUT
semantic input, and every run/qualification capture binds it. Cached or prior
output cannot satisfy fresh execution merely by copying the challenge into a
later record.

Missing anchor/start proof, publication after output, or an anchor controlled
solely by the result producer irrevocably leaves already observed output as
development evidence; backdated timestamps or later reconciliation cannot
promote it. A force move or history rewrite after a valid prospective anchor
quarantines affected authority until owner-authorized, independently reviewed
reconciliation proves the original external anchor/start chain and includes all
fork history.

Authorization must therefore be both indexed and externally anchored before the
attempt starts. A run performed earlier remains development evidence even when
its source, configuration, seed, and output later match an authorized attempt.

## Formal Attempt Allocation And Lifecycle

Every formal attempt receives an immutable attempt identifier before its
material SUT output is observed. Replacement attempts are allocated only under
the pre-registered replacement rule and keep an explicit `replaces_attempt_id`.

Attempt lifecycle is distinct from scoring:

- `authorized`: attempt identity and selection basis are fixed;
- `started`: declared initial state/checkpoint has been opened;
- `evidence_captured`: required raw artifacts have been durably written;
- `sealed`: record validation and artifact-digest closure passed;
- `authority_invalidated`: a later authority/integrity finding withdraws the
  record from authoritative use without deleting it;
- `superseded`: a later immutable decision replaces a record-level conclusion
  without deleting history.

Lifecycle names define semantic distinctions, not a mandatory implementation
enum. Impossible combinations must be rejected. In particular, an attempt
cannot become `sealed` before evidence capture, and authority invalidation
cannot be used to hide an observed undesirable SUT outcome.
`INVALID_UNSCORABLE` remains the
separate accepted run-validity result. An invalid/unscorable attempt can and
must have a sealed immutable history record when its evidence was captured;
that does not make it a valid scored SUT run.

Campaign lifecycle is separate:

- `planned`;
- `authorized`;
- `active`;
- `suspended`;
- `closed`;
- `superseded`.

`suspended` and `superseded` are campaign lifecycle states, not run outcomes.

## Authoritative Run Record

Each run-attempt record contains at least:

- record schema/domain revision, record identifier, and content fingerprint;
- authority namespace, campaign, and attempt identifiers;
- behavior and evaluation manifest IDs, payload fingerprints, and manifest-
  artifact fingerprints;
- prospective authorization anchor profile, commit, and external gate/event or
  attestation reference;
- causal start-proof profile and fresh challenge/capture binding;
- path ID, claim classes pressured, attempt slot, actual seed/replay/provider
  handles where applicable, and selection-basis reference;
- initial snapshot/checkpoint identity and run-isolation evidence;
- start, evidence-capture, seal, run-invalidity, authority-invalidation, and
  supersession references;
- delivered bundle IDs and exact ordered delivery/capture references;
- raw SUT input/output/inspection capture identities and digests;
- simulator request and replayable-realization evidence references;
- evaluator-private evidence references kept outside SUT visibility;
- run validity, run-global hard-invariant result, and per-claim obligation
  result vector using accepted `ADR-005 R2` domains;
- rule IDs, observed refs, expected/actual classification, and affected claim
  classes for every failure artifact;
- producer/validator identity and seal result;
- correction, reclassification, run-invalidity, authority-invalidation,
  replacement, and supersession links where applicable.

The record fingerprint uses its own domain:

```text
zoey:formal-run-record:v1
```

Mutable lifecycle state is not edited into a sealed record. Later lifecycle or
classification changes are separate immutable linked records.

## Replayable Simulator Evidence

In-memory routing is insufficient for formal authority. Every simulator
interaction material to a checkpoint, outcome, invalidity decision, or oracle
classification must have a durable replayable evidence envelope containing:

- simulator request identity and exact requested SUT output/disposition ref;
- projected SUT-visible realization exactly as delivered;
- evaluator-private realization/premise data where applicable;
- simulator/evaluation configuration fingerprint;
- creation and delivery order;
- fidelity or mismatch data and origin;
- capture schema/domain revision, content digest, and storage/custody reference;
- validation and seal status.

For non-JSON or binary evidence, the canonical structured envelope records the
media type, encoding, byte length, and `sha256:` digest of the exact stored
bytes. Canonical JSON identity applies to the envelope; it must not normalize or
re-encode the raw artifact before verifying its byte digest.

Durable means the bytes are written to an immutable or content-addressed
artifact that remains resolvable at record sealing and at the evidence cutoff.
A process-local object, console log, or reconstructable expectation is not
durable evidence.

Durability must preserve the `ADR-002 R2` and `ADR-008 R2` boundary. Persisting
evaluator-private evidence never makes it SUT-visible, behavior-driving, or a
fixture answer.

## Formal-Evidence Universe And Cutoff

### Authority-Namespace Index

One declared authority namespace contains an index of every qualification plan,
qualification result, campaign authorization, and post-seal decision under its
control. A campaign is formal only if its prospective authorization appears in
this index and satisfies the external anchor before execution.

The project owner designates exactly one effective namespace for this milestone
or accepts an explicit union/supersession rule covering every predecessor. A
second unmerged namespace, divergent index head, or unresolved index fork makes
the formal-evidence universe incomplete. Reconciliation must be outcome-
independent, enumerate both complete fork histories, receive independent review,
and be accepted by the project owner; selecting one favorable head is invalid.
Campaigns outside the effective namespace are non-formal and cannot be
selectively imported after outcomes are known.

Each immutable namespace-index revision records:

- namespace identity and authority;
- every deterministic-qualification plan/result ID and fingerprint within the
  revision's scope;
- every campaign authorization ID/fingerprint within the revision's scope;
- prospective anchor profile and external evidence for each qualification plan
  and campaign authorization;
- behavior and evaluation fingerprints bound by each campaign;
- authorization, suspension, closure, and supersession links;
- prior index revision/fingerprint where applicable;
- monotonic revision number and exactly one accepted predecessor, with any fork
  explicitly reconciled rather than selected by favorable outcomes;
- exact included-entry count and content fingerprint;
- cutoff boundary expressed by index revision/fingerprint, not merely a date.

Namespace revisions are cumulative. A later revision may supersede a campaign
or decision, but it must continue to enumerate the earlier identity and its
supersession link. It cannot drop an earlier campaign from history.

This is the minimum registry needed to satisfy `ADR-009 R4` cross-campaign
configuration-history closure. It is an artifact, not a required central
service. A self-authored claim that all known campaigns were included is not a
substitute.

### Campaign Evidence Index

When a campaign closes or is suspended for review, freeze an immutable campaign
evidence index containing:

- every authorized attempt slot;
- every started, invalid, replacement, sealed, and unstarted/dispositioned
  attempt;
- every run record and raw evidence artifact identity/digest;
- behavior/evaluation manifest identities;
- selection-independence evidence;
- invalidity reasons, replacement links, stop/review decisions, corrections,
  reclassifications, and supersessions;
- deterministic-qualification plan/result and divergence-contingency links;
- campaign lifecycle result;
- exact member count, cutoff, prior index link if any, and index fingerprint.

An omitted failed, awkward, off-policy, invalid, abandoned, or unstarted
authorized attempt is an index defect. A later favorable campaign cannot remove
an earlier campaign from the namespace index.

### Completion Evidence Universe

For an `ADR-009 R4` completion determination, the formal-evidence-universe basis
is a frozen namespace-index revision plus every campaign index and material
record attributable to the tested behavior fingerprint through its cutoff.
Unresolved attribution, a missing campaign index, or an unresolvable artifact
blocks configuration-history closure.

The cutoff does not license ignoring a newer material namespace revision before
owner acceptance. `ADR-009 R4` basis-freshness control requires reevaluation or
a superseding completion determination when new attributable formal evidence or
authority history enters the effective namespace.

## Record Authority Predicate

A sealed run record is authoritative formal evidence only when all conditions
hold:

```text
campaign prospectively authorized
AND authorization indexed before attempt start
AND authorization/index externally anchored before material output
AND causal fresh-start proof binds execution/capture after that anchor
AND attempt allocated outcome-independently before material output
AND behavior/evaluation payload and manifest-artifact fingerprints match authorization
AND every repeated field closes to its sole authority without conflict
AND any one-run policy closes to an anchored sealed qualification result
AND declared initial state and isolation verified
AND required raw and simulator evidence durably captured
AND SUT/evaluator privacy boundary preserved
AND record schema, fingerprint, references, and digests validate
AND seal completed without an unresolved authority-invalidating defect
AND attempt and record appear in the frozen campaign evidence index
```

Before frozen campaign-index inclusion, a sealed run is an immutable formal-
attempt artifact with `authority_pending_index_closure`; it must be retained and
cannot be called authoritative evidence. Inclusion in the frozen index changes
that authority predicate, not the sealed record or its outcome. A campaign may
not omit an adverse pending record to avoid making it authoritative.

Authority does not require `PASS`. An authoritative valid hard failure remains
formal evidence. An authoritative invalid-attempt record remains formal campaign
history but is not a valid scored SUT run; its declared run-invalidity is not by
itself an authority-invalidating defect.

## Invalidity, Authority Invalidation, Reclassification, And Supersession

Decision rights are closed as follows:

| Role | Permitted authority |
| --- | --- |
| Mechanical validator | Recompute schema, canonicalization, digest, reference, anchor, and index predicates; report or quarantine a defect; never make a discretionary semantic reclassification. |
| Campaign evaluator | Produce the initial validity, invariant, and obligation classifications strictly under the accepted manifest/rule catalogue; cannot revise its own sealed result. |
| Independent reviewer | Attest the evidence and outcome-independence of a proposed post-observation authority invalidation, oracle/policy correction, namespace reconciliation, or campaign-authority supersession; cannot alone accept it. |
| Project owner | Solely make those material post-observation decisions effective and accept campaign supersession or namespace-fork reconciliation. |

A record that fails a closed authority predicate at initial sealing never becomes
authoritative. A later mechanically detected defect immediately quarantines the
affected evidence from new aggregation, but permanent authority invalidation or
material reclassification after output was observed requires an immutable
proposal, independent review, and project-owner acceptance. The campaign
producer cannot unilaterally withdraw adverse evidence.

Run-invalidity reasons and replacement limits are inherited from `ADR-004 R3`
and `ADR-005 R2` and copied into the campaign authorization. They are not
chosen after observing an inconvenient outcome.

Every run-invalidity record preserves:

- attempt and record identity;
- pre-registered or independently inspectable reason code;
- evidence proving the integrity defect;
- decision actor/time;
- replacement eligibility and replacement attempt link;
- campaign stop/suspension consequence.

Initial run-invalidity classification may be made by the designated campaign
evaluator only from the pre-registered catalogue. Before campaign-index freeze,
a validator distinct from the output-producing process must recompute the
declared integrity predicate from sealed evidence; disagreement suspends the
campaign. A post-seal change to validity is a material reclassification and
follows the independent-review/owner rule.

An `authority_invalidated` lifecycle record is different: it records a later
finding that prospective authorization, identity, capture, sealing, or index
closure was defective. It preserves the original record and evidence, states
the exact authority defect and affected claims, and cannot be used to relabel
undesirable but valid SUT behavior as `INVALID_UNSCORABLE`.

Reclassification for an oracle or evaluation-policy defect uses the immutable
superseding decision required by `ADR-004 R3`: original and corrected
classification, exact defect, supporting evidence, authority, affected records,
campaigns, and claims. It becomes effective only after independent review and
project-owner acceptance. The original classification remains in history.

No record, evidence artifact, manifest, index, or failure is edited or deleted
to make a campaign pass. Corrections append linked artifacts. A behavior-
configuration change creates a new behavior identity and campaign. A material
evaluation change creates a new evaluation identity and campaign but cannot by
itself rehabilitate a valid hard failure of unchanged behavior.

## Comparison Rules

Formal records may be directly aggregated only when they bind the same behavior
and evaluation fingerprints and belong to an accepted common campaign/index
scope. Equal behavior identity with different evaluation identity requires a
new campaign and explicit historical disposition; it is not an implicit
apples-to-apples comparison.

Different behavior fingerprints remain different configurations under
proposed `ADR-010 R2`. Unknown or unsupported identity comparison is fail-
closed and cannot transfer evidence.

## Relationship To Completion Artifacts

This ADR supplies record authority and evidence-universe inputs to `ADR-009 R4`.
It does not collapse the completion artifact dependency:

```text
formal records and indexes -> completion evidence package P
P -> completion-eligibility determination D
D -> project-owner disposition A
```

The authority index, campaign index, or run record must not cite `D` or `A` as
proof of its own completeness or validity. Owner acceptance cannot repair
missing formal evidence.

## Adversarial Review Requirements

Before acceptance or implementation, reviewers must reject a design that:

- authorizes a campaign after any material formal output was observed;
- treats a self-authored timestamp, local commit, mutable remote ref, or
  producer-controlled receipt as proof of prospective order;
- anchors metadata prospectively but reuses output observed before the anchor
  without a gate-launched or independently witnessed fresh-start chain;
- promotes an exploratory/development run because it later matches the formal
  configuration;
- allocates seeds or attempt slots from known favorable outcomes;
- treats a hash, signature, Git commit, or directory location as authority by
  itself;
- lets behavior-only repository changes alter evaluation identity, or
  evaluation-only repository changes alter behavior identity;
- permits repeated manifest/campaign/run fields to conflict or uses latest-wins
  precedence;
- qualifies deterministic execution without an anchored plan, complete planned
  executions, closed comparison profile, or distinct validation;
- stores simulator evidence only in memory or reconstructs it after the run;
- makes evaluator-private evidence SUT-visible;
- omits invalid, failed, abandoned, replacement, or superseded attempts;
- uses a timestamp alone as the evidence cutoff;
- lets a campaign index prove that no unindexed campaign existed without the
  authority-namespace index;
- mutates or deletes a sealed record, manifest, index, or historical failure;
- calls a sealed run authoritative before frozen campaign-index inclusion or
  omits an adverse authority-pending record from that index;
- classifies undesirable SUT output as infrastructure invalidity;
- lets a campaign producer unilaterally invalidate or reclassify observed
  adverse evidence;
- changes evaluation configuration to reset a valid behavior hard failure;
- introduces `D -> P`, `A -> D`, or another self-certifying completion cycle.

## Consequences

Positive consequences:

- formal authority is prospective and outcome-independent;
- externally anchored ordering prevents authorization from being reconstructed
  solely from mutable repository files after outcomes are known;
- sole-field authority and conflict closure prevent contradictory locally valid
  artifacts;
- deterministic qualification is inspectable, non-circular, and indexed;
- replayable simulator evidence replaces process-local claims;
- every attempt and correction remains attributable;
- a lightweight artifact index satisfies cross-campaign completeness without a
  mandatory service or database;
- formal failure evidence cannot be hidden by later success;
- SUT/evaluator privacy and ownership remain intact.

Costs and limitations:

- Phase 7 must implement durable capture, validation, sealing, and indexing;
- the authority namespace requires disciplined prospective registration;
- formal execution requires a protected remote gate/event or independent pre-
  output attestation outside the result producer's sole control;
- sensitive evaluator evidence needs controlled custody;
- missing artifacts or unresolved identity fail closed;
- this ADR does not select a signing system, database, hosted registry,
  long-term archive, or durable project-repository boundary.

## Acceptance Effect

If the project owner accepts this exact revision after a compatible accepted
`EVAL-004` resolution:

- `EVAL-007` becomes `Resolved` with outcome `Decision` for the first synthetic
  selected-slice milestone;
- `OPEN_QUESTIONS.md` gains a resolved tombstone referencing this ADR;
- Phase 7 may implement the accepted manifest, capture, record, sealing, and
  index contracts only after the governance projection and current workbench
  review gates are satisfied;
- `EVAL-005` remains required before a formal campaign intended to support the
  bounded milestone claim is authorized or scored.

Until acceptance, this document is a proposal and authorizes no campaign,
formal record, evidence promotion, compatibility claim, or implementation.

## Reconsideration Triggers

Reconsider this decision if:

- a repository-local authority namespace cannot establish the completeness
  basis required by `ADR-009 R4`;
- durable replayable evidence cannot preserve evaluator-private custody;
- formal records require cryptographic signer identity or third-party
  attestation beyond content fingerprints and recorded authority;
- the selected prospective anchor profiles cannot provide stable external
  ordering or their declared authority refs cannot prevent/reveal rewrites;
- a provider/runtime prevents exact attempt, model, seed, or trace attribution
  needed by the attempted claim;
- a durable system-project extraction, trust boundary, retention, or production
  archive triggers a separately governed storage/custody decision.

## Non-Decisions

This ADR does not decide:

- behavior-configuration identity beyond consuming `EVAL-004`;
- selected-slice scoreability or unresolved-question disposition;
- the accepted run validity, hard failure, claim obligation, or replacement
  semantics already owned by `ADR-004 R3` and `ADR-005 R2`;
- a final implementation language, file layout, database, signature,
  transparency log, cloud archive, or repository extraction beyond the minimum
  external ordering anchor required above;
- production memory, retrieval, model selection, voice, avatar, durable
  adaptation, product UI, or broader `SCN-001` acceptance.
