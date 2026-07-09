# Zoey Evaluation Instructions

This directory is evaluation-owned implementation code.

Apply the root repository instructions first, then this evaluation-specific guidance.

## Evaluation Boundary Rules

- Evaluation code may depend on the declared SUT public boundary only.
- Harness, simulator, fixture projection, capture, and oracle code must not call private SUT internals.
- Fixture/oracle records may be answer-bearing internally, but full records never cross SUT ingress.
- Projections into SUT must preserve role and state origin.
- Unknown or prohibited SUT-visible fields must be rejected before semantic ingestion.

## Harness And Simulator Rules

- The harness transports SUT-selected material output; it does not choose among competing SUT outputs.
- The simulator realizes SUT-selected proposal intents or behavior dispositions.
- Simulator outputs returning to SUT use the same closed-ingress barrier as fixture inputs.
- The simulator must not repair SUT behavior, decide semantic correctness, own branch gates, or leak canonical-match facts to the SUT.

## Capture, Reporting, And Claims

- Capture/reporting collect evidence; they do not repair missing SUT state or relation evidence.
- Logs, snapshots, replay, and restore paths must not reintroduce evaluation-only metadata into SUT behavior.
- Development artifacts and engineering conformance results are not formal evaluation evidence.
- Do not claim evaluated behavioral compatibility, final scoreability, selected-slice acceptance, or full `SCN-001` pass unless the governing open questions and record contracts allow it.

## Review Focus

Before completing an evaluation change, check whether it affects:

- fixture projection;
- harness delivery or arbitration;
- simulator realization;
- capture/reporting;
- oracle-visible evidence;
- SUT ingress payloads;
- replay/restore;
- artifact labels or claims.

If yes, update tests or the conformance ledger for the applicable `ENG-CONF-*` and `ENG-CLAIM-*` rules.
