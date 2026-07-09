# Zoey Engineering Exception Template

Template version: `V0.1.0`

Status: `Draft`

Purpose: a repository-local, time-bounded record for an exception to an engineering control. An exception records residual risk; it does not change canonical rule meaning or prove conformance.

Store active exceptions in `governance/EXCEPTIONS.md` or an equivalently declared repository-local exception register. Reference the exception ID from the affected `CONFORMANCE.md` entry.

```text
Exception ID:
Affected rule ID:
Affected rule revision:
Affected paths/change/repository scope:
Reason:
Compensating control:
Required review actor: human-review
Approver and recorded outcome:
Effective at:
Expiry or reconsideration trigger:
Promotion consequence:
Claim consequence:
Status: active | expired | superseded
```

## Non-Waivable Boundary

An engineering exception cannot waive an accepted semantic obligation, an ADR/register invariant, a governing-source conflict, or a claim boundary. Those require the governing decision process.

An exception also cannot report the affected rule as `enforced` merely because the exception exists. The conformance ledger retains the truthful enforcement status and names the active exception.
