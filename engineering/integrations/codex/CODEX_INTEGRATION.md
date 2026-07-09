# Codex Integration Contract

Integration version: `V0.1.0`

Status: `Draft`

Date: 2026-07-09

Base standard: `ENGINEERING_STANDARD.md` `V0.4.0`

Verified external behavior assumptions:

- OpenAI Codex `AGENTS.md` guidance checked on 2026-07-09.
- Codex reads `AGENTS.md` guidance before work.
- Codex builds the instruction chain once per run/session.
- Codex checks `AGENTS.override.md` before `AGENTS.md` in each directory.
- Codex includes at most one instruction file per directory.
- Codex walks from project root toward the current working directory.
- Later, closer instruction files override earlier guidance on conflict.
- Codex stops adding project instruction content at `project_doc_max_bytes`, default `32 KiB`.

These are external behavior assumptions, not Zoey semantic authority. If Codex behavior changes materially, this integration contract becomes revalidation-required.

## Purpose

This integration defines how Codex consumes Zoey governance in implementation repositories.

It does not make Codex an enforcement authority. Durable enforcement remains in local conformance ledgers, structural design, static checks, automated tests, manual review, CI, and protected promotion paths.

## Template Ownership

The templates in this directory are starting points for repo-local `AGENTS.md` files.

Instantiation model:

```text
canonical template -> repo-local AGENTS.md
repo-local AGENTS.md -> locally maintained guidance
```

Repo-local `AGENTS.md` may add repository map, commands, repeated local feedback, and directory-specific conventions. It must not remove or weaken required governance routing, active rule references, claim separation, or conformance gate expectations.

## Codex Rule Catalogue

### ENG-AGENT-CODEX-001 - Codex Guidance Projection

Rule revision: `R1`

Governing sources:

- `ENG-AGENT-001 R1`

External behavior assumptions:

- Codex `AGENTS.md` discovery behavior verified 2026-07-09

Scope: governed repositories using Codex.

Applies when: a repo-local `AGENTS.md` file is created, updated, synchronized, or reviewed.

Rule: Codex guidance routes work through the local governance lock and conformance index before reading full governance documents.

Forbidden shapes:

- requiring Codex to read the full standard and full active profile before every routine change;
- requiring prompts to restate active Zoey rules;
- omitting `CONFORMANCE.md` as the applicability router.

Required checks:

- root `AGENTS.md` points first to `governance/ZOEY_GOVERNANCE.lock` and `governance/CONFORMANCE.md`;
- guidance tells Codex to read only applicable rule entries and cited source snapshots unless broader governance review is required.

Expected mechanisms:

- structural
- manual-review

Promotion integration:

- local

Failure consequences:

- promotion-blocking

Review question: does Codex have a short path from changed files to applicable rule IDs and local gates?

### ENG-AGENT-CODEX-002 - Monotonic Instruction Specialization

Rule revision: `R1`

Governing sources:

- `ENG-AGENT-001 R1`

External behavior assumptions:

- Codex closer-directory guidance overrides earlier guidance on conflict

Scope: root and nested Codex instruction files.

Applies when: any root, nested, or override Codex guidance file is added or changed.

Rule: nested Codex guidance may specialize or strengthen inherited active engineering rules. It must not weaken, negate, bypass, or silently reinterpret inherited rules.

Forbidden shapes:

- nested SUT guidance allowing public internal transitions when root guidance forbids public API widening;
- nested evaluation guidance bypassing closed SUT ingress;
- `AGENTS.override.md` committed without explicit engineering exception;
- alternate instruction filenames hiding required Zoey guidance.

Required checks:

- guidance review compares nested rule references against inherited rule references;
- committed `AGENTS.override.md` is blocked unless exception scope, reason, expiry, and non-weakening constraints are recorded.

Expected mechanisms:

- static
- manual-review

Expected test modes:

- contract

Promotion integration:

- CI

Failure consequences:

- merge-blocking
- promotion-blocking

Review question: does this instruction file only specialize inherited rules, or does it weaken them?

### ENG-AGENT-CODEX-003 - Instruction Refresh After Governance Changes

Rule revision: `R1`

Governing sources:

- `ENG-AGENT-001 R1`

External behavior assumptions:

- Codex builds the instruction chain once per run/session

Scope: active Codex sessions and governance/instruction changes.

Applies when: a governed change modifies `AGENTS.md`, `AGENTS.override.md`, governance lock, active profile selection, integration contract, or instruction routing configuration.

Rule: do not continue unrelated governed implementation under an old instruction chain without explicitly reloading/verifying guidance or starting a fresh Codex run.

Forbidden shapes:

- updating active profile or AGENTS routing and then continuing unrelated implementation as if Codex reloaded automatically;
- relying on stale prompt context after governance lock changes.

Required checks:

- final report for governance/instruction changes says whether further implementation should start from a fresh run or after explicit guidance reread.

Expected mechanisms:

- manual-review

Promotion integration:

- local

Failure consequences:

- advisory
- promotion-blocking

Review question: does this session need fresh instruction discovery before further governed implementation?

## Future Skill

A future `zoey-conformance-review` skill may automate rule discovery, diff-to-rule mapping, conformance gate execution, and residual-risk reporting. Such a skill is a reusable review workflow, not an enforcement authority.

