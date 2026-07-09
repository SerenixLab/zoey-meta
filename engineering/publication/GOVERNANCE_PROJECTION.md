# Governance Projection Process

Document version: `V0.1.0`

Status: `Draft`

Date: 2026-07-09

## Purpose

This document defines the minimal publication path from canonical `Zoey/meta` governance into a governed implementation repository.

It is a process contract, not a final sync tool design.

## Projection Flow

```text
canonical meta governance
    -> select standard/profile/integration versions
    -> copy pinned governance snapshots
    -> copy required governing source snapshots
    -> write or update governance lock
    -> preserve repo-owned CONFORMANCE.md
    -> validate content digests
```

## Projection Inputs

- canonical `ENGINEERING_STANDARD.md`;
- active profile files;
- active integration contracts;
- source documents cited by active rules;
- Codex `AGENTS.md` templates where Codex is used;
- repository-local conformance ledger.

## Projection Outputs

```text
governance/
    ENGINEERING_STANDARD.md
    ACTIVE_PROFILE.md
    CODEX_INTEGRATION.md
    ZOEY_GOVERNANCE.lock
    CONFORMANCE.md
    sources/
        OPEN_QUESTIONS.md
        ADR-*.md
```

## Drift Check

A governance drift check should verify:

- local snapshot digests match the governance lock;
- rule IDs and revisions in `CONFORMANCE.md` exist in active standard/profile/integration snapshots;
- local evidence referenced by `CONFORMANCE.md` resolves;
- no rule is marked `enforced` when its evidence or gate is missing;
- repo-local `AGENTS.md` keeps required governance routing and does not weaken inherited active rules.

## Manual Edits

Do not edit derived governance snapshots to change obligations. Change canonical governance in `Zoey/meta`, then re-project.

Repo-local differences belong in:

- `CONFORMANCE.md`;
- repo-local `AGENTS.md`;
- explicit engineering exceptions;
- repo-local implementation docs.
