# Zoey Conformance Ledger Template

Template version: `V0.1.0`

Status: `Draft`

Purpose: repository-local mapping from active `ENG-*` rules to actual enforcement mechanisms, evidence, and promotion integration.

This file is repo-owned after instantiation. It records local enforcement state; canonical rules do not.

## Governance Baseline

Governance lock: `governance/ZOEY_GOVERNANCE.lock`

Active standard:

- `ENGINEERING_STANDARD.md` `V0.4.0`

Active profiles:

- `SCN001_SELECTED_SLICE.md` `V0.2.0`

Active integrations:

- `CODEX_INTEGRATION.md` `V0.1.0`

## Status Values

- `enforced`: evidence resolves and the declared promotion integration actually runs or requires it.
- `review-only`: qualifying review is required and recorded, but no stronger mechanism exists.
- `uncovered`: no effective enforcement exists yet.
- `revalidation-required`: governing source, rule revision, profile, integration, or local evidence changed and requires review.

## Applicability Index

Use this table as Codex's first routing surface. Add rows for every active rule that applies to this repo.

| Rule ID | Rule revision | Applies to paths/change types | Status | Local evidence | Promotion integration |
| --- | --- | --- | --- | --- | --- |
| `ENG-CONF-IMPORT-001` | `R1` | `scn001_sut_core/**`; dependency files | `uncovered` | TBD | TBD |
| `ENG-CONF-PAYLOAD-001` | `R1` | SUT ingress; fixture/simulator projections | `uncovered` | TBD | TBD |
| `ENG-CONF-RUN-001` | `R1` | run lifecycle; globals; caches; sessions | `uncovered` | TBD | TBD |
| `ENG-CONF-INSPECT-002` | `R1` | inspection implementation | `uncovered` | TBD | TBD |

## Rule Entries

Copy one entry per active applicable rule.

```text
Rule ID:
Rule revision:
Governing source revisions:
Applies To:
Actual mechanisms:
Actual test modes:
Promotion integration:
Status:
Failure consequences:
Local evidence:
Residual risk:
Reviewer/Owner:
Verified at:
```

## Ledger Integrity

A rule may be marked `enforced` only when:

- the rule ID exists in the active standard/profile/integration;
- the rule revision matches the governance lock;
- local evidence paths, test names, check names, or review records resolve;
- the declared promotion integration actually runs or requires the evidence;
- skipped tests, missing tools, removed configs, or renamed jobs are not counted as passing.

Do not update `Verified at` as routine changelog noise. Update it when enforcement coverage, evidence identity, gate mapping, or governance baseline changes.

