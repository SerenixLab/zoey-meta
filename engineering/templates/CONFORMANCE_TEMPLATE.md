# Zoey Conformance Ledger Template

Template version: `V0.2.0`

Status: `Draft`

Purpose: repository-local, human-readable applicability router and enforcement ledger for the full active `ENG-*` rule set.

This file is repo-owned after instantiation. It records mutable local enforcement truth; canonical rules and the governance lock do not.

## Governance Baseline

Authoritative local governance set: `governance/ZOEY_GOVERNANCE.lock`

Do not duplicate pinned standard, profile, or integration versions here. The lock owns that baseline.

## Status Values

- `enforced`: applicable rule whose evidence resolves and whose actual promotion mechanism satisfies the canonical minimum.
- `review-only`: applicable rule whose declared minimum is a qualifying recorded review and has no stronger local mechanism.
- `uncovered`: applicable rule with no effective enforcement meeting its canonical minimum.
- `revalidation-required`: applicable rule whose pinned baseline, evidence, mechanism, or applicability needs review.

## Applicability Index

Projection initializes one row for every rule in `ZOEY_GOVERNANCE.lock.rule_revisions`. A missing row is an audit failure. `not-applicable` requires a repository-specific rationale.

| Rule ID | Revision | Rule source artifact | Applicability | Rationale / applies to paths and change types | Status | Local evidence | Actual promotion mechanism |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ENG-EXAMPLE-001` | `R1` | `profiles/EXAMPLE.md` | `not-applicable` | Example only; replace during projection | N/A | N/A | N/A |

## Rule Entries

Copy one entry for each `applicable` rule. Its rule ID, revision, source artifact, and canonical minimums must resolve through the lock and canonical snapshot.

```text
Rule ID:
Rule revision:
Rule source artifact:
Governing source revisions:
Applicability: applicable
Applies To:
Actual mechanisms:
Actual test modes:
Actual promotion mechanism:
Status:
Failure consequences:
Local evidence:
Residual risk:
Reviewer/Owner:
Active exception:
Verified at:
```

## Ledger Integrity

A conformance audit verifies that:

- every active locked rule has exactly one applicability disposition;
- every `not-applicable` disposition has a rationale;
- every applicable entry matches the locked rule revision and source artifact;
- local evidence paths, test names, check names, review records, and active exception IDs resolve;
- actual promotion mechanisms meet the canonical minimum integration;
- an `enforced` claim meets canonical minimum promotion enforcement;
- expired, out-of-scope, or missing exceptions do not satisfy a rule;
- skipped tests, missing tools, removed configs, or renamed jobs are not counted as passing.

`Verified at` identifies a commit, build, configuration, or comparable evidence identity. Do not update it as routine changelog noise.
