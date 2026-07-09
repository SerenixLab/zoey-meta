# Zoey SUT Core Instructions

This directory is SUT-owned implementation code.

Apply the root repository instructions first, then this SUT-specific guidance.

## SUT Boundary Rules

- SUT code must not import, reflect into, configure, or depend on evaluation code.
- SUT public ingress must be closed against evaluation-only and undeclared evaluation-origin material.
- Rejected ingress must have no selected-slice semantic side effects.
- Public APIs stay minimal; do not expose internal transitions for harness or test convenience.
- SUT-visible references and handles must not encode evaluation context.

## State And Inspection Rules

- Behavior-driving semantic mutations must be attributable to SUT-owned transition responsibilities.
- Selected-slice state access is bounded to run-scoped state, identity resolution, and required local relation traversal.
- Do not introduce retrieval, relevance ranking, distractor filtering, broad memory search, or context assembly.
- Inspection is passive and interleaving-safe.
- Inspection must not create, repair, activate, retire, narrow, or mutate behavior-driving state or relation evidence.

## Review Focus

Before completing a SUT change, check whether it affects:

- SUT public input/output contracts;
- selected-slice state mutation;
- relation or reference identity;
- transition evidence;
- inspection surfaces;
- logs, snapshots, replay, or restore behavior;
- claim labels or report text.

If yes, update tests or the conformance ledger for the applicable `ENG-CONF-*` rules.

