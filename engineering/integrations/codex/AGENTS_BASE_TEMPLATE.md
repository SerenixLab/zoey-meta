# Zoey Repository Instructions

This repository contains governed non-throwaway Zoey implementation work.

Before editing governed code, identify the applicable `ENG-*` rules and the local conformance evidence.

## Governing Baseline

Read:

- `governance/ZOEY_GOVERNANCE.lock`
- `governance/ENGINEERING_STANDARD.md`
- `governance/ACTIVE_PROFILE.md`
- `governance/CONFORMANCE.md`

The local governance files are derived snapshots. If they conflict with cited ADRs or registers, stop and report the conflict. Do not silently choose a weaker rule.

## Always Apply

- Preserve accepted Zoey decisions over implementation convenience.
- Do not weaken, bypass, or delete conformance gates to make a task pass.
- Keep public APIs minimal; do not make internals public only for tests or evaluation setup.
- Add or update tests for non-throwaway behavior changes.
- Do not import throwaway code into governed implementation.
- Keep generated code out of public contracts until reviewed.
- Separate engineering conformance, evaluated behavioral compatibility, and milestone acceptance.

## Before Changing Boundary-Bearing Code

Boundary-bearing code includes SUT/evaluation boundaries, fixture projection, simulator routing, state mutation, references, inspection, capture, reporting, replay, and claim artifacts.

Before editing it:

- identify the active `ENG-CONF-*` rules;
- read the cited ADRs for those rules;
- check `governance/CONFORMANCE.md` for local mechanisms and status;
- preserve or update the local tests/gates that enforce the rule.

## Required Local Gates

Use the implementation repo's configured commands for:

- code quality;
- architecture/dependency conformance;
- boundary conformance;
- state integrity;
- tests.

If a required gate is missing, record the rule as `uncovered` or `review-only` in `governance/CONFORMANCE.md`; do not call it enforced.

## Instruction Overrides

Do not commit `AGENTS.override.md` on governed branches unless an explicit engineering exception authorizes it and records scope, reason, expiry, and rules it may not weaken.

