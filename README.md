# Zoey Meta

This repository contains the governing documents for Zoey, the unified personal AI system being designed from the Iris and Yuki legacy lineages.

It is a meta repository, not an implementation repository. Its purpose is to keep the project thesis, scenario pressure tests, state/control rules, open questions, and accepted decisions coherent enough that future implementation repos can be created without rediscovering the same foundations.

## Repository Scope

This repo is responsible for:

- defining what Zoey is and is not;
- preserving the canonical constraints future designs must satisfy;
- recording pressure scenarios used to falsify weak architectures;
- tracking unresolved architectural and governance questions;
- keeping accepted decisions traceable over time.

This repo is not responsible for:

- application code;
- model training code;
- voice, avatar, or UI implementation;
- service deployment;
- copied legacy projects;
- experimental scratch work.

Implementation projects should live in separate repositories under `Zoey/projects/` and reference this repo by document and decision.

## Current Documents

Read in this order:

1. `SYSTEM_THESIS.md`
   Defines Zoey's identity, purpose, growth model, authority boundaries, and non-negotiable invariants.

2. `CANONICAL_SCENARIOS.md`
   Defines behavioral pressure scenarios that future architectures must satisfy without prescribing implementation mechanisms.

3. `STATE_AND_CONTROL_MODEL.md`
   Defines state categories, transition rules, control requirements, and claim boundaries.

4. `OPEN_QUESTIONS.md`
   Tracks unresolved questions, active blockers, bounded assumptions, and decision dependencies.

5. `decisions/`
   Contains ADR-style records for accepted or proposed project decisions.

## Decision Workflow

Open questions are resolved through explicit decision artifacts, not by conversation alone.

Typical flow:

```text
open question
    -> analysis or evidence
    -> proposed ADR / contract / fixture / governance rule
    -> owner acceptance
    -> open question status update
```

A draft ADR can recommend a direction, but it does not close an open question until accepted by the project owner.

## Repository Rules

- Keep documents practical and concise.
- Prefer explicit claim boundaries over broad promises.
- Do not duplicate legacy repositories here.
- Do not place implementation code here unless a future decision changes the repo scope.
- When a baseline document changes materially, re-triage affected open questions.
- When an implementation repo depends on a decision, link the relevant document version or ADR.

## Current Direction

The current proposed first vertical slice is recorded in:

`decisions/ADR-001-first-vertical-slice.md`

Its recommendation is to start from `SCN-001: Japanese Longitudinal Development` as a harness-first, state-inspection-first slice.
