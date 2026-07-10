# Zoey Engineering Governance

This directory contains implementation-facing governance derived from Zoey's thesis, open questions, and accepted ADRs.

Canonical artifacts:

- `../ENGINEERING_STANDARD.md`: general engineering rule model and code-health floor.
- `profiles/SCN001_SELECTED_SLICE.md`: first selected-slice conformance profile.
- `integrations/codex/CODEX_INTEGRATION.md`: Codex-specific consumption contract.

Templates and publication:

- `templates/CONFORMANCE_TEMPLATE.md`: implementation-repo conformance ledger template.
- `templates/EXCEPTION_TEMPLATE.md`: repository-local scoped engineering exception template.
- `templates/GOVERNANCE_LOCK_TEMPLATE.md`: implementation-repo governance lock contract.
- `publication/GOVERNANCE_PROJECTION.md`: minimal process for projecting canonical governance into implementation repos.
- `integrations/codex/AGENTS_*_TEMPLATE.md`: starting `AGENTS.md` guidance for governed Codex work.
- `tools/zoey_governance.py`: dependency-free governance projector and portable checker.

Canonical governance lives in this meta repository. Implementation repositories consume pinned projections with local conformance evidence; they do not edit canonical snapshots by hand.
