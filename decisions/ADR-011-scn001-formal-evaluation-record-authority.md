# ADR-011: SCN-001 Formal Evaluation Record Authority

Status: `Proposed`

Date: 2026-07-18

Record revision: `R1`

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

Proposal dependency: `ADR-010 R1` is the proposed behavior-configuration
identity contract. This ADR may be reviewed in parallel and may be accepted only
in an owner decision set that also accepts, or follows, a compatible `EVAL-004`
resolution.

## Decision

Adopt a prospective, manifest-bound, append-preserving formal-evaluation
authority contract for the first synthetic `SCN-001` selected-slice milestone.

Use five distinct artifact families:

1. immutable evaluation-configuration manifest;
2. prospective campaign-authorization manifest;
3. immutable run-attempt records and replayable evidence artifacts;
4. immutable correction, reclassification, run-invalidity, authority-
   invalidation, and supersession records;
5. frozen authority-namespace and campaign evidence indexes that establish the
   formal-evidence universe and cutoff.

These artifacts may be stored as package-local files in the governed workbench.
No database, central service, or new durable system-project repository is
required. The storage representation must nevertheless provide one declared
authority namespace in which prospective campaign authorizations and every
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
identifier and content fingerprint. Its identity payload records:

- evaluator source commit, worktree state, package/build identity, dependency
  lock, and runtime/toolchain identity;
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
- deterministic-replay qualification policy or nondeterministic declaration;
- planned valid run count per required path inherited from `ADR-004 R3`;
- governing thesis, scenario, state/control, ADR, register, engineering, and
  fixture/oracle revisions;
- behavior-relevant evaluator environment and external dependency identity;
- evaluator-private artifact custody and access policy.

The evaluation manifest uses the same envelope/payload separation,
`RFC8785-JCS` canonicalization revision, SHA-256 algorithm, and typed
applicability discipline as proposed `ADR-010 R1`, with hash domain:

```text
zoey:evaluation-configuration:v1
```

Its identity is separate from behavior identity. A campaign manifest binds one
of each; neither fingerprint includes the other.

A formal evaluation requires a clean evaluator worktree, or an exact immutable
patch/source bundle digest that reconstructs every evaluator-affecting
difference from the named commit. A bare `dirty` state is ineligible for
campaign authorization.

## Canonical Artifact Identity

Every artifact family in this ADR uses an immutable envelope plus one canonical
identity payload. The envelope holds the opaque artifact ID, storage/custody
location, content fingerprint, and non-semantic annotations. The identity
payload holds every field material to authorization, configuration, evidence,
classification, lifecycle, ordering, cutoff, or supersession. The fingerprint
field and storage location are never hashed into themselves.

All V1 identity payloads use `RFC8785-JCS`, canonicalization revision `1`,
SHA-256, and `sha256:` plus 64 lowercase hexadecimal characters. Each family
has a separate hash domain:

| Artifact family | Hash domain |
| --- | --- |
| Evaluation configuration | `zoey:evaluation-configuration:v1` |
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
reference. A matching ID with a different fingerprint, or a matching
fingerprint under another domain/schema revision, is a closure failure. Future
canonicalization, included-field, or hash-construction changes require new
schema/domain revisions.

## Prospective Campaign Authorization

A campaign preflight authorizes only future formal record production. It never
promotes historical development or exploratory runs.

Before the first material SUT output for any formal attempt, the campaign must
have an immutable authorization manifest containing:

- campaign identifier;
- authority namespace identifier;
- behavior manifest identifier and fingerprint;
- evaluation manifest identifier and fingerprint;
- scenario, fixture/oracle package, claim classes, required paths, and mandatory
  obligation-map identity;
- deterministic/nondeterministic classification and its evidence basis;
- planned attempt slots or the deterministic rule that allocates them before
  their material outputs are observed;
- planned valid run count per path;
- outcome-independent selection/seed rule and disposition of known exploratory
  outcomes, seeds, replay handles, cached realizations, or candidate pools;
- inherited invalidity, replacement, stop, suspension, and correction rules;
- replayable-evidence storage/custody locations and access boundaries;
- campaign authority identity, authorization time, and authorization result;
- authorization manifest fingerprint.

The campaign authority is the project owner unless an accepted governance
artifact explicitly delegates that role for this milestone. A validator may
confirm preflight mechanically, but it does not create strategic authority by
calling itself authoritative.

Authorization must be recorded in the authority-namespace index before the
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
- behavior and evaluation manifest IDs/fingerprints;
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

One declared authority namespace contains an index of every campaign
authorization under its control. A campaign is formal only if its prospective
authorization appears in this index before execution.

The project owner designates exactly one effective namespace for this milestone
or accepts an explicit union/supersession rule covering every predecessor. A
second unmerged namespace, divergent index head, or unresolved index fork makes
the formal-evidence universe incomplete. Campaigns outside the effective
namespace are non-formal; they cannot be selectively imported after outcomes
are known.

Each immutable namespace-index revision records:

- namespace identity and authority;
- every campaign authorization ID/fingerprint within the revision's scope;
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
AND attempt allocated outcome-independently before material output
AND behavior/evaluation fingerprints match authorization
AND declared initial state and isolation verified
AND required raw and simulator evidence durably captured
AND SUT/evaluator privacy boundary preserved
AND record schema, fingerprint, references, and digests validate
AND seal completed without an unresolved authority-invalidating defect
AND attempt and record appear in the frozen campaign evidence index
```

Authority does not require `PASS`. An authoritative valid hard failure remains
formal evidence. An authoritative invalid-attempt record remains formal campaign
history but is not a valid scored SUT run; its declared run-invalidity is not by
itself an authority-invalidating defect.

## Invalidity, Authority Invalidation, Reclassification, And Supersession

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

An `authority_invalidated` lifecycle record is different: it records a later
finding that prospective authorization, identity, capture, sealing, or index
closure was defective. It preserves the original record and evidence, states
the exact authority defect and affected claims, and cannot be used to relabel
undesirable but valid SUT behavior as `INVALID_UNSCORABLE`.

Reclassification for an oracle or evaluation-policy defect uses the immutable
superseding decision required by `ADR-004 R3`: original and corrected
classification, exact defect, supporting evidence, authority, affected records,
campaigns, and claims. The original classification remains in history.

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
proposed `ADR-010 R1`. Unknown or unsupported identity comparison is fail-
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
- promotes an exploratory/development run because it later matches the formal
  configuration;
- allocates seeds or attempt slots from known favorable outcomes;
- treats a hash, signature, Git commit, or directory location as authority by
  itself;
- stores simulator evidence only in memory or reconstructs it after the run;
- makes evaluator-private evidence SUT-visible;
- omits invalid, failed, abandoned, replacement, or superseded attempts;
- uses a timestamp alone as the evidence cutoff;
- lets a campaign index prove that no unindexed campaign existed without the
  authority-namespace index;
- mutates or deletes a sealed record, manifest, index, or historical failure;
- classifies undesirable SUT output as infrastructure invalidity;
- changes evaluation configuration to reset a valid behavior hard failure;
- introduces `D -> P`, `A -> D`, or another self-certifying completion cycle.

## Consequences

Positive consequences:

- formal authority is prospective and outcome-independent;
- replayable simulator evidence replaces process-local claims;
- every attempt and correction remains attributable;
- a lightweight artifact index satisfies cross-campaign completeness without a
  mandatory service or database;
- formal failure evidence cannot be hidden by later success;
- SUT/evaluator privacy and ownership remain intact.

Costs and limitations:

- Phase 7 must implement durable capture, validation, sealing, and indexing;
- the authority namespace requires disciplined prospective registration;
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
- a final implementation language, file layout, database, service, signature,
  transparency log, cloud archive, or repository extraction;
- production memory, retrieval, model selection, voice, avatar, durable
  adaptation, product UI, or broader `SCN-001` acceptance.
