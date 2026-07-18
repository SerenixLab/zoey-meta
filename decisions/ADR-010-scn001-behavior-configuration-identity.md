# ADR-010: SCN-001 Behavior-Configuration Identity

Status: `Proposed`

Date: 2026-07-18

Record revision: `R1`

Decision authority: project owner

Target question IDs: `EVAL-004`

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

Proposal dependency: `ADR-011 R1` is the separate proposed resolution for
formal-record authority under `EVAL-007`. This ADR does not absorb that target.

## Decision

Adopt a hybrid immutable behavior-configuration manifest for the first
synthetic `SCN-001` selected-slice milestone.

Every formal evaluation record must bind both:

- an opaque behavior-configuration manifest identifier used as a stable local
  reference; and
- a deterministic content fingerprint over the manifest's identity payload.

The referenced manifest carries the complete behavior-affecting identity. A
run record may repeat selected fields for review convenience, but repeated
fields must match the manifest and are not a second authority.

This decision distinguishes four concepts:

```text
manifest identifier = stable reference to one immutable manifest
content fingerprint = exact identity of the behavior payload
record authority     = separately governed by EVAL-007 / ADR-011
evaluation result    = separately governed by accepted run/scoring policy
```

A matching fingerprint proves only that the same canonical behavior payload
was named. It does not prove who authorized a campaign, that evidence is
complete, that a run is valid, or that the behavior passed.

## Manifest Envelope And Identity Payload

The artifact has an envelope and one identity-bearing payload.

Required envelope fields are:

- `schema_id`: `zoey.behavior-configuration-manifest`;
- `schema_revision`: `1`;
- `manifest_id`: an opaque stable identifier unique within the formal-evidence
  authority namespace;
- `identity_payload`: the complete identity-bearing object defined below;
- `canonicalization_scheme`: `RFC8785-JCS`;
- `canonicalization_revision`: `1`;
- `hash_algorithm`: `sha-256`;
- `hash_domain`: `zoey:behavior-configuration:v1`;
- `content_fingerprint`;
- `created_at` and `created_by` provenance;
- optional non-identity annotations;
- optional `supersedes_manifest_id` for a corrected manifest.

The identity payload must contain:

1. source and build identity;
2. SUT public-boundary identity;
3. dependency identity;
4. runtime and behavior-relevant environment identity;
5. behavior policy and external configuration identity;
6. typed model, prompt, tool, provider, and randomness applicability;
7. artifact custody references and digests where content is not embedded.

Envelope provenance, human annotations, storage paths, and the fingerprint
field itself are excluded from the identity payload. Moving an identical
manifest or correcting an annotation therefore does not invent a new behavior
configuration. Any field capable of changing evaluated behavior belongs in the
identity payload and cannot be hidden in an annotation.

## Required Behavior Identity

### Source And Build

The identity payload records:

- repository identity and repository role;
- exact source commit;
- worktree state;
- build/package identifier and version;
- digest of the built or directly executed SUT artifact set;
- package manifest and dependency-lock digests;
- build command or build-recipe identity where a build occurs;
- behavior-affecting generated assets and their digests.

A formal campaign requires a clean worktree, or an exact immutable patch/source
bundle digest that reconstructs every behavior-affecting difference from the
named commit. A bare `dirty` label is not a complete identity and is ineligible
for formal campaign authorization.

### Public SUT Boundary

The identity payload records:

- SUT package/project identity;
- declared public entry point and export surface;
- public input, output, lifecycle, and inspection contract revision or digest;
- selected-slice boundary decision revisions;
- behavior-relevant feature or policy flags exposed at that boundary.

Private source is still covered by source/build identity. The public-boundary
digest exists to make boundary changes reviewable; it does not imply that
private implementation changes are immaterial.

### Dependencies And Runtime

The identity payload records:

- exact resolved dependency graph or a lock artifact that determines it;
- local/package dependencies with their exact source/build identities;
- runtime name, version, implementation, operating system, and architecture;
- toolchain identity used to build or execute the SUT;
- behavior-affecting environment variable names and canonical values or content
  digests;
- locale, timezone, clock mode, and numeric/runtime modes where behavior-
  affecting;
- external tool or provider identities where applicable.

Authentication secrets are never embedded. A secret used only for access is
recorded as non-behavioral authentication material. If secret content can alter
behavior, its stable content digest and custody reference are identity-bearing;
an undisclosed and unfingerprinted behavior-affecting secret makes the
configuration ineligible for formal evidence.

### Model, Prompt, Tool, Provider, And Randomness

Each category uses a typed applicability object. Omission and free-form
`"not applicable"` strings are invalid.

Allowed applicability values are:

- `applicable`: complete identity fields are present;
- `not_applicable`: a stable reason code explains why the category cannot affect
  this configuration;
- `unknown`: identity is incomplete and the manifest is not eligible for formal
  campaign authorization.

For `applicable` model configuration, record the provider/runtime, exact model
identifier and a stable revision or weight digest sufficient for the attempted
claim, decoding and sampling parameters, adapter/checkpoint identities, and
relevant serving configuration. A mutable alias without a stable revision or
digest is `unknown` and ineligible for formal campaign authorization.

For `applicable` prompt configuration, record prompt/template identifiers,
content fingerprints, composition order, variable-binding policy, and a custody
reference when prompt text is not embedded. Sensitive prompt content may remain
access-controlled; its exact digest and authorized custody reference may not be
omitted. A digest is an identity control, not a privacy guarantee: low-entropy
or guessable prompt content and its manifest may also require access control.

For this deterministic non-model selected-slice SUT, the expected initial
values are typed `not_applicable` entries with reason code
`deterministic_non_model_sut` for model and prompt, and a complete declaration
of any remaining tool/provider/randomness behavior.

## Canonicalization And Fingerprinting

The identity payload is valid JSON restricted to the canonicalization scheme's
supported value domain. Non-finite numbers, platform-dependent encodings,
comments, duplicate object keys, and implicit defaults are forbidden.

The fingerprint is computed as:

```text
sha256(
    utf8("zoey:behavior-configuration:v1\n")
    || RFC8785_JCS(identity_payload)
)
```

Encode `content_fingerprint` as `sha256:` followed by 64 lowercase hexadecimal
characters.

The domain prefix is mandatory. Identical canonical bytes used for another
artifact type must not share an ambiguous cross-type identity. Any future
change to included fields, canonicalization, or hash construction requires a
new schema/domain revision; it must not silently reinterpret an existing
fingerprint.

## Comparison And Material Change

Behavior configurations compare through these outcomes:

| Outcome | Condition | Formal-evidence consequence |
| --- | --- | --- |
| `IDENTICAL` | Same schema/domain and same content fingerprint. | Records name the same exact behavior payload. |
| `METADATA_ONLY_DIFFERENCE` | Identity fingerprint is equal; only excluded envelope provenance, annotation, or storage location differs. | No behavior-configuration split. |
| `BEHAVIOR_CONFIGURATION_CHANGED` | Any identity-bearing field differs under a comparable schema/domain. | New behavior configuration and new campaign identity are required. |
| `COMPARABILITY_UNRESOLVED` | Missing/unknown identity, unsupported schema/domain comparison, or unresolved artifact custody. | Evidence cannot be transferred, merged, or used for compatibility/completion. |

No automatic `semantically equivalent` outcome exists. Different behavior
fingerprints remain different configurations even when a reviewer expects the
same outputs. A later accepted equivalence policy may support a separately
bounded comparison claim, but it cannot rewrite historical identity or erase
formal failures.

Identity-bearing changes include source, build artifacts, public boundary,
runtime/toolchain, resolved dependencies, behavior policy, feature flags,
model, prompt, provider/tool behavior, applicable randomness, and any
environment input capable of changing an evaluated obligation, hard invariant,
or oracle-visible state.

Purely editorial annotations, creation provenance, and artifact relocation are
not identity-bearing only because the envelope explicitly excludes them. A
change described as a refactor or optimization is still behavior-configuration
change when an identity-bearing source/build field changes.

## Immutability, Correction, And Supersession

Manifests are immutable after first formal reference. A malformed or incomplete
manifest is not edited in place. Correction creates a new manifest with a new
`manifest_id`, the corrected fingerprint, and a `supersedes_manifest_id` link.

If the corrected identity payload has the same fingerprint, the correction may
repair envelope provenance only. If the fingerprint changes, formal records
remain bound to the original behavior configuration; they are not silently
retargeted to the correction.

Deletion, path replacement, rebasing, or mutable tags must not erase the
original manifest from formal history.

## Relationship To Accepted Evaluation Policy

This ADR instantiates, but does not redefine, the configuration-identity
requirements in `ADR-004 R3`, `ADR-005 R2`, and `ADR-009 R4`.

- A material behavior change ends the affected campaign.
- A valid formal hard failure remains attributable to the exact failed behavior
  fingerprint and cannot be rehabilitated by an evaluation-only change.
- Development runs performed before prospective campaign authorization remain
  development evidence even when their behavior fingerprint later matches an
  authorized campaign.
- Configuration identity alone does not establish the formal-evidence universe,
  evidence cutoff, record authority, scoreability, completion eligibility, or
  owner acceptance.

## Adversarial Review Requirements

Before acceptance or implementation, reviewers must reject a design that:

- treats a Git commit, package version, model name, or prompt label alone as
  complete behavior identity;
- omits build output, dependency lock, runtime, boundary, or behavior-relevant
  environment identity;
- accepts `unknown`, missing, or unfingerprinted behavior-affecting material in
  a formal manifest;
- embeds secrets or sensitive prompts merely to make a manifest self-contained;
- hashes an envelope containing timestamps, paths, or the fingerprint itself;
- uses raw JSON serialization without a pinned canonicalization revision;
- omits hash-domain separation;
- treats equal fingerprints as proof of authority or pass status;
- treats different fingerprints as automatically equivalent;
- edits or retargets a manifest after formal evidence references it;
- lets an evaluation-only configuration change erase a behavior failure.

## Consequences

Positive consequences:

- formal evidence can identify exactly which behavior was evaluated;
- deterministic non-model configurations remain first-class without fake model
  or prompt strings;
- sensitive content can remain in controlled custody while exact identity stays
  inspectable;
- configuration-history comparison becomes deterministic and conservative;
- record authority remains cleanly separated from content identity.

Costs and limitations:

- implementation must inventory behavior-affecting inputs rather than rely on a
  commit label;
- source/build changes create new identities even when output appears unchanged;
- unresolved or inaccessible identity material blocks formal use;
- this ADR does not choose a storage service, central registry, final file
  layout, signing mechanism, or cross-configuration semantic equivalence policy.

## Acceptance Effect

If the project owner accepts this exact revision:

- `EVAL-004` becomes `Resolved` with outcome `Decision` for the first synthetic
  selected-slice milestone;
- `OPEN_QUESTIONS.md` gains a resolved tombstone referencing this ADR;
- `EVAL-007` remains responsible for formal-record authority and evidence-
  universe completeness;
- `EVAL-005` remains responsible for scoreability and unresolved-question
  treatment;
- engineering standard/profile sources must be re-triaged and projected before
  Phase 7 implementation.

Until acceptance, this document is a proposal and authorizes no formal record,
campaign, comparison, compatibility claim, or implementation.

## Reconsideration Triggers

Reconsider this decision if:

- the canonicalization or hash construction cannot be implemented consistently
  across the required toolchains;
- a behavior-affecting input cannot be represented without exposing prohibited
  sensitive content and no stable digest/custody mechanism exists;
- a model/runtime cannot supply a sufficiently exact revision or weight identity
  for the claim being attempted;
- a later milestone needs accepted semantic-equivalence or continuity comparison
  across different behavior fingerprints;
- a trust-boundary, production, or durable-repository trigger changes the
  permitted custody or storage boundary.

## Non-Decisions

This ADR does not decide:

- evaluation-configuration identity or formal-record authority;
- campaign authorization, evidence storage, sealing, cutoff, or supersession;
- scoreability, run aggregation, or completion eligibility;
- final schema file format beyond the canonical identity contract;
- digital signatures, transparency logs, databases, or services;
- production model selection, prompt design, memory, retrieval, voice, avatar,
  durable adaptation, trust-boundary architecture, or repository extraction.
