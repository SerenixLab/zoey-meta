# Zoey Governance Lock Template

Template version: `V0.1.0`

Status: `Draft`

Purpose: repository-local record of the exact canonical governance release, active profiles, integration contracts, source snapshots, rule revisions, and content digests consumed by a governed implementation repo.

The concrete serialization format is not yet mandated. This template defines required meaning.

## Required Fields

```text
lock_version:
generated_or_updated_at:
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

local_conformance:
  path:
  content_digest:
```

## Integrity Rules

- A local governance snapshot is derived, not authoritative.
- Local snapshots must not be hand-edited to change canonical obligations.
- Local differences belong in `CONFORMANCE.md`, repo-local `AGENTS.md`, explicit engineering exceptions, or repo-local docs.
- A governance drift check compares local snapshot content against the lock's content digests.
- If digest validation fails, affected rules are `revalidation-required` until the lock and snapshots are corrected.

## Source Snapshots

Include only the governing source snapshots required by active rules. For the first `SCN-001` profile this normally includes:

- `OPEN_QUESTIONS.md`
- `ADR-002`
- `ADR-003`
- `ADR-004`
- `ADR-005`
- `ADR-006`
- `ADR-007`
- `ADR-008`

Codex and CI must not require a sibling `Zoey/meta` checkout for routine governance discovery.

