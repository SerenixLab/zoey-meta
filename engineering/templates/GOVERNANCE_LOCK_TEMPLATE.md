# Zoey Governance Lock Template

Template version: `V0.2.0`

Status: `Draft`

Purpose: repository-local, machine-parseable record of the exact canonical governance set consumed by a governed implementation repository. It pins canonical inputs; it does not digest mutable conformance or exception state.

The first projector serializes `ZOEY_GOVERNANCE.lock` as deterministic JSON encoded as UTF-8 with LF line endings. Every `content_digest` is SHA-256 of those normalized bytes. `generated_at` is informational and is excluded from baseline-change comparison.

## Required Fields

```text
lock_version:
serialization: json
content_digest_algorithm: sha256
content_digest_canonicalization: utf-8-lf
generated_at:
canonical_meta_source:
canonical_meta_commit:

standard:
  path:
  version:
  content_digest:

profiles:
  - id:
    path:
    version:
    content_digest:

integrations:
  - id:
    path:
    version:
    content_digest:

governing_source_snapshots:
  - id:
    path:
    version_or_revision:
    canonical_path:
    content_digest:

rule_revisions:
  - rule_id:
    revision:
    source_artifact:

conformance_index:
  path: governance/CONFORMANCE.md
```

## Integrity Rules

- A local governance snapshot is derived, not authoritative.
- Local snapshots must not be hand-edited to change canonical obligations.
- The lock digests only canonical standard, profile, integration, and governing-source snapshots.
- `CONFORMANCE.md`, `EXCEPTIONS.md`, local `AGENTS.md`, evidence records, and `generated_at` are mutable local state and are not lock-digested inputs.
- A projection-integrity check compares canonical snapshots against the lock's digests. A separate conformance audit checks the ledger, exceptions, evidence, gates, and instruction routing.
- A baseline change is a change to a pinned version, rule revision, active artifact set, or canonical snapshot digest. It is not a timestamp-only rewrite.

## Source Closure

The projector derives governing-source snapshots from the complete active rule set:

```text
standard + active profiles + active integrations
    -> active rule IDs and revisions
    -> exact external governing-source references
    -> deduplicated governing-source snapshot set
```

Do not maintain a hand-written scenario list of ADRs. A source reference must resolve to a specific canonical artifact and revision, or be marked as a non-snapshot base-rule source under the Standard's source-identity rules.

Codex and CI must not require a sibling `Zoey/meta` checkout for routine governance discovery.
