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
- attach binding obligations to rule IDs;
- distinguish mechanism, test mode, status, and failure consequence;
- avoid treating Markdown text alone as enforcement;
- preserve the split between base standard, active profile, Codex guidance templates, and future local conformance ledgers.

When reviewing selected-slice implementation guidance:

- check dependency direction, closed SUT ingress, run isolation, transition-attributable mutation, passive inspection, no post-hoc evidence repair, historical endpoint identity, and claim boundaries;
- keep engineering conformance separate from evaluated behavioral compatibility and milestone acceptance.
