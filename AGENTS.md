# Zoey Meta Repository Instructions

This repository owns Zoey's canonical governance documents: thesis, scenarios, state/control model, open questions, ADRs, engineering standard, active profiles, and integration templates.

Before changing governance documents:

- preserve accepted ADRs and registers over local convenience;
- check whether a change is semantic or editorial;
- update version/status/date fields when the document's substance changes;
- keep derived artifacts explicit about their source baseline;
- do not let profiles or standards become second semantic sources for ADR content;
- keep implementation-facing guidance concise enough for repository consumption.

When editing `ENGINEERING_STANDARD.md` or `engineering/profiles/*`:

- keep `ENG-*` rule entries as the normative surface;
- attach binding obligations to rule IDs and rule revisions;
- do not store local enforcement `Status` in canonical rules;
- distinguish expected mechanism, test mode, promotion integration, local ledger status, and failure consequence;
- avoid treating Markdown text alone as enforcement;
- preserve the split between base standard, active profiles, integration contracts, templates, source snapshots, and local conformance ledgers.

When editing `engineering/integrations/codex/*`:

- keep Codex-specific discovery behavior out of the tool-neutral base standard;
- preserve monotonic instruction specialization: nested guidance may strengthen or specialize inherited rules, not weaken them;
- route Codex through `ZOEY_GOVERNANCE.lock` and `CONFORMANCE.md` before full governance documents;
- cite exact `ENG-*` rule IDs in templates where practical.

When reviewing selected-slice implementation guidance:

- check dependency direction, closed SUT ingress, run isolation, transition-attributable mutation, passive inspection, no post-hoc evidence repair, historical endpoint identity, and claim boundaries;
- keep engineering conformance separate from evaluated behavioral compatibility and milestone acceptance.
