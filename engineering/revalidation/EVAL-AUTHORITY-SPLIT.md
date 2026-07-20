# Evaluation-Authority Split Engineering-Rule Revalidation

Date: 2026-07-18

Source change:

- `OPEN_QUESTIONS.md V0.2.21` to `V0.2.22`;
- `EVAL-004` narrowed to its permanent behavior-configuration decision target;
- linked `EVAL-007` created and activated for evaluation configuration, formal-
  record authority, replayable evidence, evidence-universe/cutoff closure,
  invalidation, and supersession;
- `EVAL-005` constrained to instantiate accepted run/campaign policy rather
  than reopen `EVAL-003`.

This record classifies canonical engineering-rule consequences under the
source-bound rule lifecycle. It does not resolve any active question, accept an
ADR, authorize a campaign, or create formal evidence.

## Material Rule Changes

| Rule | Result | Reason |
| --- | --- | --- |
| `ENG-CLAIM-001 R3` | `R4` | Completion preconditions now name the separate accepted `EVAL-007` authority contract in addition to `EVAL-004` behavior identity and `EVAL-005` scoreability. |
| `ENG-CLAIM-002 R3` | `R4` | Reserved-artifact checks now prohibit formal campaign authorization or authoritative records before `EVAL-007` resolves and reserve authority schemas to that question. |
| `ENG-CHANGE-001 R3` | `R4` | The required trigger audit now checks `EVAL-004`, `EVAL-007`, and `EVAL-005` as distinct frontiers. |
| `ENG-CONF-CLAIM-001 R3` | `R4` | Selected-slice claim checks now distinguish behavior binding/comparison, campaign/record authority, and scoreability triggers. |

Each revision increment is required because the rule lifecycle treats a change
to a forbidden shape or required check as material. The rule targets remain the
same, so no new engineering-rule ID is required.

## Source Revalidation Without Rule-Revision Change

| Rule | Result | Reason |
| --- | --- | --- |
| `ENG-BASE-REPO-001 R2` | source reference updated | `REPO-001` and the workbench-to-project trigger are unchanged in `OPEN_QUESTIONS.md V0.2.22`. |
| `ENG-CLAIM-WORKBENCH-001 R2` | source reference updated | The scenario-provisional workbench boundary and denied durable-project claims are unchanged. |
| `ENG-CONF-EVIDENCE-001 R2` | dependency updated to `ENG-CLAIM-001 R4` | Its public-boundary evidence obligation is unchanged; only the depended-on claim-domain rule revision changed. |

`ENGINEERING_STANDARD.md V0.6.3` and selected-slice profile `V0.4.3` carry the
new register release and rule revisions. No integration rule, implementation-
boundary rule, state/dependency rule, or code-health rule changes target,
obligation, check, enforcement minimum, or failure consequence.

## Claim And Implementation Effect

The split strengthens the existing reservation boundary:

```text
EVAL-004 behavior identity
        +
EVAL-007 record authority
        +
EVAL-005 scoreability
        -> Phase 7 formal-evidence implementation may begin only after
           project-owner acceptance of all applicable decisions
```

Engineering tests, local red-team runs, projected governance, and proposed ADR
text remain non-formal artifacts. Development runs cannot be promoted
retrospectively after the decisions are accepted. `ADR-004 R3`, `ADR-005 R2`,
and `ADR-009 R4` remain unchanged and authoritative.

## Source-Closure Result

Exactly these materially affected claim/trigger rules bind the split:

- `ENG-CLAIM-001 R4`;
- `ENG-CLAIM-002 R4`;
- `ENG-CHANGE-001 R4`;
- `ENG-CONF-CLAIM-001 R4`.

At the time of this 2026-07-18 revalidation, proposed ADR-010 through ADR-012
were not governing sources pending owner acceptance and register re-triage.

Post-acceptance disposition (2026-07-20): the project owner accepted
`ADR-010 R3`, `ADR-011 R3`, and `ADR-012 R3` as one compatible decision set,
and `OPEN_QUESTIONS.md V0.2.23` records the resulting closure. The decisions are
now governing sources. Their engineering-rule/profile consequences still
require a new source-bound re-triage and projection before Phase 7
implementation. That re-triage is recorded separately in
`engineering/revalidation/ADR-010-012-R3.md`; this historical split
revalidation does not perform that projection.
