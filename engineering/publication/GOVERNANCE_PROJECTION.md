# Governance Projection Process

Document version: `V0.2.0`

Status: `Draft`

Date: 2026-07-10

## Purpose

This document defines the minimal publication path from canonical `Zoey/meta` governance into a governed implementation repository.

It is a process contract for the first projector and checker, not a service or plugin design.

## Projection As A Governance-Set Transaction

```text
1. Select complete standard, profile, and integration set.
2. Derive active rule/revision set and governing-source closure.
3. Stage every canonical snapshot outside the live governance directory.
4. Compute digests and construct the complete new lock.
5. Validate the staged set against its lock.
6. Publish canonical snapshots.
7. Publish the lock last as the new baseline marker.
8. Run the separate local conformance audit.
```

If step 8 fails, projection integrity remains valid but local conformance is `revalidation-required` or otherwise degraded. Promotion is blocked where the affected rules require it; projection does not roll back a coherent new canonical baseline.

## Projection Inputs

- canonical `ENGINEERING_STANDARD.md`;
- active profile files;
- active integration contracts;
- exact governing source documents derived from active rule sources;
- Codex `AGENTS.md` templates where Codex is used;
- repository-local conformance index and optional exception register.

## Projection Outputs

```text
governance/
    ENGINEERING_STANDARD.md
    profiles/
        SCN001_SELECTED_SLICE.md
    integrations/
        CODEX_INTEGRATION.md
    sources/
        OPEN_QUESTIONS.md
        ADR-*.md
    ZOEY_GOVERNANCE.lock
    zoey_governance.py             portable projection-integrity checker
    CONFORMANCE.md
    EXCEPTIONS.md                  if an exception is active
```

Projection initializes missing root or nested `AGENTS.md` files from templates. It records the seed template ID/version in the instantiated file and never overwrites later repo-owned guidance during routine synchronization.

The canonical meta repository provides the first projector as:

```text
python3 engineering/tools/zoey_governance.py project \
  --target <implementation-repo> \
  --profile engineering/profiles/SCN001_SELECTED_SLICE.md \
  --integration engineering/integrations/codex/CODEX_INTEGRATION.md
```

Projection copies its portable checker into `governance/zoey_governance.py`. A consuming repository verifies its snapshot without a sibling meta checkout:

```text
python3 governance/zoey_governance.py check --target . --conformance
```

## Projection Integrity Check

A projection-integrity check verifies that:

- all live canonical snapshots match the lock's algorithm and digests;
- the lock's active profile/integration set matches projected directories;
- locked rule IDs, revisions, and source artifacts resolve exactly once;
- every governing source snapshot is derived from the active rule-source closure;
- `CONFORMANCE.md` is declared by the lock but is not hashed as a canonical input.

## Conformance Audit

A separate conformance audit verifies that:

- the applicability index completely covers the locked rule set;
- evidence, gate, review, and exception references resolve;
- actual promotion mechanisms meet the canonical minimums;
- no rule is marked `enforced` without its required evidence;
- root and path-scoped `AGENTS.md` retain required routing and monotonic specialization;
- every governed Codex working-directory instruction chain fits its configured `project_doc_max_bytes` limit without relying on a personal override.

## Manual Edits

Do not edit derived canonical snapshots to change obligations. Change canonical governance in `Zoey/meta`, then project a new governance set.

Repo-local differences belong in `CONFORMANCE.md`, `EXCEPTIONS.md`, repo-local `AGENTS.md`, or implementation documentation. They do not alter canonical source snapshots or governance-lock digests.
