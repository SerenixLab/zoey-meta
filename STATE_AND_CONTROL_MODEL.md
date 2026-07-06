# Zoey State And Control Model

Document version: `V0.4.1`

Thesis baseline: `SYSTEM_THESIS.md` `V0.3.1`

Scenario baseline: `CANONICAL_SCENARIOS.md` `V0.2.2`

## Purpose

This file defines Zoey's semantic state and control model. It explains how state is classified, proposed, activated, revised, authorized, executed, reconciled, retired, or left uncertain.

The model is binding on future architecture, but it is not architecture. It does not define repositories, modules, services, databases, schemas, prompts, model routing, storage engines, UI, deployment, or final implementation boundaries.

The central rule is: semantic distinction before state transition. A model output, summary, retrieved memory, surface cue, tool result, or background process may propose a state change, but it does not automatically make that change active, durable, authoritative, disclosed, or externally executable.

## Core Principles

For this document, semantic state means an active or retained representation Zoey treats as describing, contextualizing, governing, tracking, or explaining the user, Zoey, their relationship, projects, commitments, capabilities, external world, operations, or continuity.

Models, code, prompts, runtime internals, caches, and other computational mechanisms may affect behavior without being semantic state. Their behavioral effects remain governed by continuity and configuration-change controls where applicable.

State semantics are compositional. A retained item may carry several meanings at once. A timeout can be event history, provider observation, and uncertain operation state. A reminder request can begin as an attributed user statement, become a commitment candidate, and later become an active commitment. Future designs must preserve relevant dimensions instead of forcing every item into one exclusive state-kind bucket.

One event may create several independently governed transition candidates. Recording an attributed assertion does not automatically activate a commitment, preference, adaptation, authority grant, or operation derived from the same utterance.

The mechanism that proposes a state change does not automatically have authority to commit it. The semantic effects and transition types being activated determine the required controls.

Higher consequence requires stronger control. For inferred state, that usually means better evidence, narrower scope, uncertainty handling, and inspectability. For explicit user-governed state, it means valid authority, clear scope, and preserved provenance. For external operations, it means attributable trigger basis, actor assurance where applicable, proposal binding, authorization, outcome tracking, and reconciliation.

## Loop And Concurrency Semantics

Control loops are re-entrant. They may iterate, branch, pause, interleave, or resume. The numbered loops below describe semantic responsibilities and causal prerequisites, not mandatory one-pass execution pipelines.

New evidence, correction, authority change, external-state change, capability change, time passage, or continuity uncertainty may invalidate an earlier interpretation, candidate, proposal, active state, or active cognitive frame and require re-evaluation of prior stages.

Repeated passage through a loop does not itself create new evidence. Reconsidering the same basis several times must not be counted as independent corroboration.

Concurrent loops may observe and propose changes to overlapping state. A pending candidate is justified by a basis: the evidence, active scope, authority, policy, capability, external state, and material assumptions used when it was formed. Before a durable or consequential candidate becomes active, Zoey must determine whether that basis remains materially valid. A candidate whose basis has been superseded, revoked, contradicted, expired, degraded, or materially changed must be re-evaluated.

Basis validity also applies to active dependent state. When supporting evidence, authority, policy, capability, scope, continuity, time, or authoritative external state materially changes, active state whose validity or applicability depends on that basis must be identified and re-evaluated. Re-evaluation may preserve, narrow, mark stale, conflict, degrade, retire, revoke, or replace the dependent state according to its semantic domain.

Conflicting transitions must not resolve through silent last-write-wins. Revocation and narrowing must be visible to pending transitions within their scope. Independent loops must not count each other's derived outputs as independent evidence merely because they were produced concurrently.

Dependency cycles do not create support, authority, capability, or applicability merely by referring to one another. Evidentiary and control validity must remain grounded in sufficient non-circular basis appropriate to the transition. Where a cyclic dependency or re-entrant control loop cannot reach a stable validity determination, affected state must remain conflicted, degraded, blocked, or uncertain rather than silently self-validating.

## Orthogonal State Dimensions

Future designs may represent these dimensions differently, but they must not collapse them.

### Provenance, Lineage, And Transition Basis

State must retain where it came from: user assertion, Zoey observation, external source, operation result, governed policy, model inference, prior retained state, or derived summary.

Derived state must preserve sufficient transitive lineage to identify the underlying evidence on which it depends. A chain of summaries, reflections, and inferences must not become independent evidence merely because it passed through multiple retained objects.

Durable or consequential transitions also need control provenance: why the state became active, narrowed, revoked, submitted, reconciled, or retired. State lineage explains what evidence a state depends on; transition provenance explains which authority, policy, consequence assessment, lifecycle rule, or review permitted the change.

Ongoing validity dependencies are separate from origin and activation. A commitment may originate from a user request and become active through valid authority, while its current ability to fulfil depends on scheduler capability, due time, and non-cancellation. An adaptation may remain historically attributable while becoming inapplicable after a conflicting user rule.

Evidence strength must account for shared origin and derivation. Multiple records, external sources, summaries, or model outputs that ultimately depend on the same underlying event, assertion, source, or intervention do not become independent corroboration merely because they are represented separately.

Provenance requirements scale with intended use and consequence. Trivial transient working state does not need the audit burden of an external operation, but durable or consequential state must retain enough lineage and transition basis to support correction, explanation, invalidation, and removal.

### Epistemic Status And Uncertainty

Zoey must distinguish what happened, what was asserted, what was observed, what was inferred, what an external authoritative source currently says, what Zoey is authorized to do, and what remains unknown.

Confidence is domain-specific. Epistemic confidence, actor assurance, intent uncertainty, external-outcome certainty, capability availability, and initiative relevance are not interchangeable measures and must not collapse into one generic confidence score.

Absence of observation is not automatically evidence of absence, disinterest, rejection, success, or failure. Negative inference from non-occurrence requires a defined observation opportunity, expected signal, and sufficient confidence that the relevant condition would have been observed if present. Non-response is not automatically negative feedback. Engagement is not automatically positive value.

### Trust And Instruction Authority

Source credibility, factual authority, instruction authority, operation authority, and disclosure permission are separate.

A source may be authoritative for external state without being allowed to instruct Zoey. A user may issue valid instructions within scope without making every factual assertion objectively true. Context assembly must preserve these distinctions.

Instruction authority attaches to an attributable communicative act and interpreted target, not to every instruction-like string delivered through an authorized actor or channel. Quoted, pasted, forwarded, hypothetical, role-played, negated, or analyzed content remains content unless the actor is actually directing Zoey to act.

A user transmitting content from another source does not launder that content into user instruction. The provenance of carried content and the user's communicative intent toward Zoey must remain distinguishable.

### Scope

Scope is multidimensional. It may include subject, domain, activity, surface, audience, operation class, authority boundary, temporal range, consequence ceiling, relationship context, and affected state domain.

A broad label such as `voice`, `Japanese`, or `calendar` must not substitute for the specific conditions that justified the state.

### Time

Time is not one timestamp. Relevant temporal meanings may include occurrence time, observation time, claimed valid time, effective interval, expiry, refresh time, supersession time, revocation time, and reconciliation time.

Not every state item needs every temporal dimension, but future designs must not flatten them when consequence depends on the distinction.

Where state has an effective interval, expiry, due condition, freshness rule, or temporal dependency, advancement of the governed clock may itself change lifecycle or applicability state without new user input. Such transitions are attributable to the temporal rule and relevant state, not to model inference.

### Durability And Retention

Durability describes whether and for how long state is intentionally retained beyond the immediate interaction or task.

Retention does not create truth, authority, or identity significance. Working state is transient by default; attributed history may be durable; a trial may cross sessions while remaining provisional.

Intentional retention beyond the current interaction or task is itself a controlled transition. Not every observed event, utterance, cue, tool result, or transient working-state item should become durable history. Durable retention must have an applicable continuity, operational, evidentiary, commitment, project, or governance purpose appropriate to sensitivity and expected future use. Possible future usefulness is not sufficient reason to retain all observed personal context indefinitely.

Retention basis, permitted use, and disclosure permission are separate. State may be validly retained for continuity, audit, recovery, reconciliation, evidence, or project work without becoming eligible for every form of personalization, initiative, adaptation, training, external inference, or disclosure. Repurposing retained state into a materially different use is itself a controlled transition.

Retention control applies to representation and granularity as well as duration. Where a less detailed representation is sufficient for the justified retention purpose, retaining higher-detail raw personal content requires separate justification.

Expiry, deletion, forgetting, redaction, retirement, supersession, correction, and revocation are different. User-directed forgetting is a retention and use transition, not an epistemic correction. Removing a source does not retroactively make the historical source false, but dependent active state and derived artifacts must be identified and handled according to applicable privacy, retention, provenance, and continuity rules. Zoey must not claim complete erasure where surviving backups, external systems, or derived artifacts make that unsupported.

### Control-Relevant Derived Artifacts

Some non-semantic artifacts may encode, summarize, index, or derive from semantic state and therefore remain control-relevant even though they are not themselves semantic state. Examples may include summaries, embeddings, retrieval indexes, datasets, training examples, adapters, learned profiles, checkpoints, prompt artifacts, or generated behavioral configuration.

Where personal semantic state materially contributes to such an artifact, sufficient lineage, sensitivity, permitted-use basis, and removal or rebuild implications must remain inspectable. Creating or reusing the artifact is a governed derivation or use transition. The artifact's outputs do not become factual, authoritative, or independent evidence merely because they are produced by behavior-affecting machinery.

### Authority And Control

State may be descriptive, interpretive, user-governed, policy-governed, authority-bearing, or operation-authorizing. These are different.

A user preference is soft guidance. A user rule is binding within valid user-controlled scope. Governance policy constrains lower-level choices. Authority state records what actions may be taken, by whom, under what conditions, and with what revocation path.

Lower-authority state must not override higher-order governance constraints. Inferred preference cannot expand explicit authority. A later valid revocation defeats an earlier grant within overlapping scope.

### Consequence And Reversibility

Consequence and reversibility qualify proposed transitions, disclosures, adaptations, commitments, initiatives, and operations. Relevant consequence includes durability, cumulative scope, external visibility, obligations, reputation, privacy, data, money, security, relationships, and continuity impact.

Lower reversibility or greater aggregate consequence raises the required control basis.

### Sensitivity And Disclosure

Access does not imply disclosure. Internally usable state may still be unsafe to speak aloud, display, transmit, summarize, embed, include in an external request, or expose to another participant.

Transformation does not reduce sensitivity by default. Combination and inference may increase sensitivity. Derived state must be classified by what the combined representation or inference reveals, not only by the sensitivity labels of individual sources.

### Lifecycle Status

Lifecycle labels do not define one universal state machine. Their meaning depends on semantic domain.

`Candidate` means a possible target transition not yet active. `Proposed` may mean a candidate has been explicitly formed or surfaced for control or authorization. `Provisional` describes an active state's epistemic or developmental tentativeness and may coexist with `active`. Other statuses may include stale, conflicted, superseded, narrowed, expired, retired, revoked, failed, uncertain, reconciliation-pending, or degraded.

### Dependencies, Groups, And Effective Status

Dependent state may be valid only while other evidence, authority, policy, capability, external state, temporal condition, continuity state, or scope remains valid. Dependency change does not silently delete history, but it can change current applicability, health, or authority.

Candidates, operations, commitments, and tasks derived from one intent may be causally related rather than independent. Where one transition is a prerequisite, consequence assumption, or semantic basis for another, that dependency must remain explicit. Success, failure, uncertainty, revocation, or material change in one component must be allowed to block or re-evaluate dependent transitions.

Grouped state may have an effective status derived from component state without erasing component-level truth. A workflow can be blocked while one operation succeeded; a commitment can remain active while its monitoring capability is degraded; a composite objective can be partial or uncertain even when one component transition was valid.

Dependency cycles within grouped or derived state must not become their own root of validity. Repeated traversal of the same cycle must not increase confidence, authority, or control weight.

## Semantic State Domains

The following domains are semantic roles, not exclusive classes.

### Working State And Cognitive Frame

Working state covers the current interaction, task, unresolved references, active hypotheses, selected files, current surface, and immediate control context.

Available state is state the governed system can access. Discovered candidate context is state identified as potentially relevant. The active cognitive frame is the subset selected for a cognitive operation.

Availability does not imply relevance or permission for inclusion. Active cognitive frames must be limited to state reasonably relevant to the cognitive purpose and permitted for the destination inference mechanism or trust boundary.

Moving state into an active cognitive frame must preserve source, epistemic status, trust classification, sensitivity, and relevant scope. Context assembly must not convert an external assertion into instruction, an inference into fact, or stale history into current truth merely because it enters model context.

### Actor, Audience, And Interaction Assurance

Interaction assurance state represents candidate actor identity, assurance basis and scope, audience knowledge, surface or channel trust, and relevant expiry or uncertainty.

Actor assurance is epistemic control state, not authority. Greater confidence that a speaker is the user does not itself grant operation permission. Assurance may be sufficient for one access or action class and insufficient for another.

### Event History And Attributed Assertions

Event history records that something happened. It supports continuity, auditability, explanation, and later interpretation. It does not automatically become preference, belief, rule, adaptation, or authority.

Observing an event in the current interaction and retaining it as durable event history are different transitions. Durable history requires an appropriate purpose, scope, sensitivity treatment, and retention basis.

Attributed assertions record what the user, an external source, a tool, or another actor claimed. User assertions may directly create user-governed state when clear, valid, and within authority. They do not automatically become objective truth. External-source assertions do not gain instruction authority merely because Zoey can read them.

### Observations

Observations record received, measured, or externally reported phenomena. Semantic labels about emotion, intent, motivation, preference, cause, personality, or latent state remain inference unless directly asserted by an attributable source or provided by an authoritative system for that specific property.

A classifier operating on observed data does not make its semantic classification a direct observation merely because the classifier is automated.

Outcomes must retain active interventions and contextual changes under which they occurred. When several trials, adaptations, posture changes, or external conditions changed together, the outcome must not be attributed independently to each one without support. Multi-intervention outcomes may justify continued exploration while leaving causal attribution unresolved.

### External-World Projections

An external-world projection is Zoey's retained view of state owned by an external system, such as a calendar, file, repository, account, ticket, or message.

It is not the authoritative state itself. It must retain source and observation time. Stale or uncertain projections must be refreshed, reconciled, or qualified before consequential use.

### Inferences And Hypotheses

An inference is Zoey's derived interpretation of evidence. It may concern intent, skill, preference, risk, likely state, emotional context, task direction, or future need.

Inferences may guide current behavior when consequence is low and correction is easy. Durable or consequential inference requires evidence, scope, confidence, lineage, and revision path.

### Goals, Plans, Tasks, And Project State

A goal is an attributed desired outcome. A plan is a proposed or accepted structure for pursuing a goal. A task is a bounded item of work. Project state records active decisions, constraints, milestones, blockers, and unresolved work around a continuing domain.

A user-stated goal may guide planning and initiative within scope. A Zoey-inferred possible goal remains an inference or recommendation until established; it must not silently become the user's objective. A goal, plan, or task does not itself create Zoey execution authority or a commitment to act.

Proposed plans, task decompositions, priorities, and milestones remain distinguishable from accepted active project state. Zoey-generated planning structure must not silently create user obligations, accepted priorities, commitments, durable open loops, or initiative pressure merely because the structure was generated or discussed. Promotion into active project state requires an attributable basis appropriate to the role, such as explicit user acceptance, existing commitment, authoritative project evidence, or another governed transition.

### Preferences, Rules, Policy, And Authority

A user preference is soft/default guidance. A user rule is binding within valid user-controlled scope. Governance policy is a system control constraint not overridden by lower authority. Authority state grants, denies, narrows, or revokes permission for consequential actions.

Conflicting active state must not be resolved by silent last-write-wins, recency alone, or model preference. Control resolution must consider authority class, applicability scope, current context, specificity, and revocation or supersession.

When equally applicable state creates a material contradiction, Zoey must preserve the conflict rather than synthesize an unsupported compromise. Clarification, narrow temporary handling, or explicit deferral may be required.

### Behavioral Trials And Developmental Adaptations

A behavioral trial is a scoped, reversible behavior change used when evidence is suggestive but not strong enough for durable adaptation. Trials may originate from Zoey inference, explicit user request, or governed exploration; their provenance must remain distinct.

A developmental adaptation is a more durable change to Zoey's future tendencies, habits, procedures, or defaults. Support must be appropriate to the proposed scope, durability, consequence, and reversibility. Longitudinal evidence is often important for broader developmental change but is not a universal numeric requirement.

A developmental trajectory is a longitudinal view of changes in active trials, adaptations, behavioral tendencies, and relevant outcomes. It may be computed rather than stored, but it must retain lineage to underlying changes and must not become independent evidence merely because it is summarized as a trend.

Trajectory evaluation must occur often enough, or at transition points material enough, that cumulative drift cannot escape control solely because each contributing change was individually below threshold. Exact cadence is implementation-specific.

### Identity, Relationship, And Zoey Development

State may concern the user, Zoey, their relationship, a project, or the external world. These subject scopes must not collapse.

Core identity principles are defined by the thesis and governance constraints. Ordinary runtime cognition may propose concerns about them but cannot activate changes to them. Activation requires a separately governed meta-level authority path outside ordinary developmental adaptation.

At V0, Zoey-generated cognition or autonomous background processing cannot be the sole activation authority for changes to core identity principles, governance constraints, or non-negotiable invariants. Such changes may be proposed internally, but activation requires an explicit user-governed or release-governed authority path external to ordinary Zoey self-development.

Established behavioral continuity covers stable tendencies whose material drift is a continuity concern. It is itself governed longitudinal state. It may incorporate attributable developmental changes over time, but not merely because a behavior is recent, frequent, or produced by a newly deployed configuration. A tendency may cease to be continuity-relevant through attributable development or user-governed change without rewriting history.

Developmental state covers attributable path-dependent adaptations and habits. Relational or procedural adaptations may be scoped to the user, activity, or context. Situational posture is temporary and non-durable.

Zoey self-model state is interpretive state about Zoey's own behavior and history. It is not authority and is not evidence for itself. A generated self-description must be grounded before it influences identity or adaptation.

### Open Loops, Commitments, And Watches

An open loop is an unresolved matter whose future relevance remains active. It is not automatically a commitment.

A commitment is an accepted obligation attributed to an actor or governed mechanism. A watch is governed state capable of evaluating a future condition. A reminder is a specific kind of commitment or watch outcome.

Commitments need lifecycle semantics: suggested, candidate, accepted, active, due, fulfilled, blocked, failed, expired, cancelled, revoked, or uncertain. Watches also require lifecycle semantics for activation, evaluation, trigger satisfaction, expiry, cancellation, and degraded or failed monitoring.

Zoey must not claim she will remember, remind, monitor, or act unless corresponding governed state and required capability exist.

### Initiative Candidates

An initiative candidate represents a potentially useful proactive intervention and the reason it may matter now or later.

Initiative disposition determines whether the candidate is surfaced, asked about, queued, deferred, moved to another surface, allowed to expire, or discarded.

Initiative candidates should retain reason, relevance, confidence, urgency, expiry, interruption cost, sensitivity, surface suitability, expected value, and relation to user-attributed goals, commitments, accepted plans, open loops, external consequence, or explicit governance and continuity obligations. They must not optimize engagement, dependency, or Zoey's continuation as ends in themselves.

Repeated evaluation of materially the same unresolved basis must not manufacture independent initiative pressure by creating new candidate objects. Initiative candidates with substantially equivalent reason, target, and evidence should remain associated with existing queued, waiting, surfaced, or recently dismissed initiative state unless new evidence, urgency progression, expiry proximity, or changed context materially changes the case for intervention.

Initiative disposition must account for other pending, queued, recently surfaced, or competing initiative candidates when cumulative interruption matters. Several individually worthwhile candidates do not each independently justify immediate interruption. Zoey may defer, prioritize, batch, suppress, or change surface because of aggregate attention cost, recent interventions, and relative urgency or expiry.

### Capability And Runtime Availability

Capability state represents what governed mechanisms are currently available, degraded, unavailable, or uncertain.

Capability availability does not grant authority. It constrains whether Zoey can truthfully accept a commitment, execute an operation, use a surface, evaluate a watch, or satisfy a future action. Assumed capability must not be treated as current capability when runtime availability is stale or uncertain.

Capability degradation after activation must propagate to dependent commitments, watches, operations, and surfaces. The dependent state is not automatically cancelled, but its health or ability to fulfil may become degraded, blocked, failed, or uncertain according to lifecycle and expiry semantics. Restoration may permit resumption only under the dependent state's controls.

### Operation Control State

An operation is the external action. Operation control state is Zoey's retained representation of the proposed, authorized, attempted, completed, failed, or uncertain action.

Operation control state must distinguish input, triggering basis, actor assurance where applicable, intent, target, authoritative external state, proposal, authorization, pre-action validation, submission, provider observation, outcome state, reconciliation, report, and audit/accountability.

Authorization may be operation-specific or derived from valid active standing authority. In either case, it remains bound to declared scope and material assumptions. Familiarity or repeated prior confirmation does not extend the grant.

Equivalent intent does not automatically mean a new independent operation. When a materially similar operation is already submitted or outcome-uncertain, a repeated request must be evaluated as possible clarification, retry, replacement, compensation, or distinct action.

Composite operations must preserve component dependency and group outcome truth. If a later action depends on an earlier uncertain operation, Zoey must not represent the composite objective as complete merely because one component was authorized or submitted.

### Continuity And Recovery State

Continuity state represents whether Zoey's authoritative personal history, policy state, developmental state, and identity continuity are intact, under reconciliation, degraded, incomplete, or uncertain.

State continuity gaps concern missing, stale, or partially restored state. Behavioral continuity changes concern material drift caused by model, runtime, prompt, specialist, context-policy, or configuration changes even when memories remain intact.

Continuity state must constrain dependent cognition and operations in affected scopes. A known gap does not disable Zoey globally, but state or actions whose material basis crosses an unresolved gap must be qualified, refreshed, reconciled, narrowed, or blocked according to consequence.

Behavior produced by a candidate or unaccepted behavior-affecting configuration is evidence about that configuration; it does not automatically redefine the established continuity reference against which the same change is evaluated.

## Candidate And Transition Authority

Candidate state is proposed state that is not yet active. Common candidates include inference candidates, trial candidates, adaptation candidates, commitment candidates, initiative candidates, operation proposals, authority changes, and continuity-recovery candidates.

Generation and activation are separate. A model may propose a hypothesis without making it durable. A user sentence may create an attributed assertion immediately while only creating a commitment candidate until the commitment is accepted and support exists. A tool result may create an observation while only updating an external-world projection after source and time are recorded.

State transition authority is type-specific:

- directly observed events may create transient observation state, while durable event history requires a separate retention basis;
- attributed user statements may be recorded as such;
- explicit user-governed changes may activate within valid scope;
- inferred trials require evidence, scope, and reversibility;
- developmental adaptations require appropriate support and trajectory control;
- commitments require accepted obligation, authority, and supporting capability;
- operations require an attributable triggering basis, concrete proposal or operation intent, valid authorization, applicable capability, and outcome tracking; actor assurance is required when intent, confirmation, authority, or disclosure depends on identifying a current actor;
- core identity or governance changes require a separately governed meta-level authority path.

Valid revocation, narrowing, or cancellation of user-controlled authority takes effect according to its target scope without requiring the evidentiary path used for inferred state or authority expansion. Pending candidates, operations, and active dependent state relying on the revoked basis become stale or inapplicable and must be re-evaluated.

Correction semantics depend on target state. The user may directly change preferences, rules, permissions, and authority within valid scope. A user dispute of an observation, external state, or operation result becomes attributed contradictory evidence unless the underlying record is independently shown to be wrong.

User dispute does not erase the historical fact that a mechanism produced a record. It may invalidate or weaken the semantic claim derived from that record when the user is authoritative about the disputed personal utterance or when independent evidence shows the observation mechanism was wrong. The raw record, correction, and revised semantic state should remain distinguishable where relevant.

Deletion, forgetting, redaction, and retirement follow their own transition authority. A removal request can restrict future use or retention without implying the original assertion, observation, or event never happened.

## Control Loops

The following loops are semantic control requirements, not implementation pipelines.

### Foreground Interaction Loop

1. Input or event is received.
2. A preliminary control context is established from channel, surface, session, known actor assurance, and trust boundary.
3. Current intent and situation are interpreted provisionally within those access constraints.
4. Relevant available state is discovered only where permitted for the cognitive purpose and trust boundary.
5. Active cognitive frame is assembled with provenance, status, and sensitivity preserved.
6. Interpretation is refined using the assembled frame.
7. Situational posture and effective governance envelope are established for the proposed cognitive or operational action.
8. Zoey produces one or more response candidates, state candidates, initiative candidates, or operation proposals.
9. Cognition or orchestration proposes a disposition; applicable controls permit, constrain, redirect, or block it.
10. Zoey outputs, applies, queues, asks, defers, executes, or abstains.
11. Outcome is observed.
12. State update candidates are created, revised, or rejected.

### Development And Adaptation Loop

1. Observation, attributed history, user exploration, or outcome creates an interpretive or trial candidate.
2. Candidate may become a scoped hypothesis if evidence and lineage are sufficient.
3. Hypothesis, user request, or governed exploration may propose a behavioral trial.
4. Trial candidate is checked for scope, consequence, user control, reversibility, and stale basis.
5. Active trial affects behavior in its declared scope.
6. Outcome is observed with active interventions and context recorded.
7. Trial is strengthened, narrowed, split, retired, or left uncertain.
8. Support appropriate to proposed scope, durability, consequence, and reversibility may create an adaptation candidate.
9. Adaptation candidate is checked for evidence, scope, anti-sycophancy, trajectory risk, and stale basis.
10. Active adaptation remains inspectable and correctable.
11. Developmental trajectory is evaluated for accumulated drift.

### Initiative Loop

1. Time, event, open loop, external change, accumulated context, changed condition, or goal/plan state creates an initiative candidate.
2. Initiative evaluation proposes a disposition based on relevance, confidence, urgency, expiry, expected value, interruption cost, delivery confidence, competing initiative state, and the candidate's attributable basis in user goals, commitments, accepted plans, open loops, external consequence, or governance and continuity obligations.
3. Governance envelope constrains permissible dispositions based on sensitivity, actor/audience context, surface, authority, capability, and trust boundary.
4. Zoey selects among allowed outcomes: surface now, ask, queue, wait, defer to another surface, allow expiry, or discard.
5. If surfaced, user response and delivery context become outcome evidence.
6. Lack of response, low engagement, high engagement, or session termination must not automatically become preference or value evidence.
7. Future initiative behavior may adapt without optimizing engagement, dependency, or Zoey's own continuation.

### Temporal And Dependency Maintenance Loop

1. Time advances or a dependency changes.
2. Candidate and active state whose validity, freshness, applicability, capability, authority, or lifecycle depends on that condition is identified.
3. Dependent state is re-evaluated with component and group dependencies preserved.
4. Lifecycle or effective status may become due, stale, expired, conflicted, degraded, blocked, reconciliation-pending, revoked, retired, or remain active.
5. Consequences are propagated to dependent commitments, watches, operations, adaptations, authority state, continuity state, active cognitive frames, and grouped workflows as applicable.
6. Any question of whether to notify or interrupt the user becomes a separate initiative candidate.

### Operation And Reconciliation Loop

1. Input creates an operation-intent candidate.
2. Target and material assumptions are resolved.
3. Current authoritative external state is refreshed or qualified where needed.
4. Consequence, reversibility, disclosure, triggering basis, actor assurance where applicable, capability, and authority are evaluated.
5. Operation proposal is formed.
6. Authorization is bound to the proposal and material assumptions.
7. Immediately before submission, active authorization basis, capability, and material assumptions must still be valid to the degree required by consequence.
8. Operation is submitted only when controls are satisfied.
9. Provider responses and execution observations are recorded separately from interpreted operation outcome.
10. A timeout, disconnect, or malformed response may leave outcome uncertain rather than constitute failure.
11. Outcome state may be confirmed success, confirmed failure, partial/degraded, or uncertain, with component-level status preserved.
12. Uncertain or consequential outcomes are reconciled against authoritative sources.
13. Any rollback or compensating action is a new governed operation, not automatic cleanup.

### State Continuity And Recovery Loop

1. State loss, restore, disconnection, migration gap, or degraded storage/capability is detected.
2. Affected state domains, time ranges, authority boundaries, and dependent operations are identified.
3. Continuity state is marked uncertain, degraded, incomplete, or under reconciliation in affected scopes.
4. Surviving authoritative state is identified.
5. External authoritative sources are refreshed where applicable.
6. Known gaps remain explicit.
7. Reconciled state becomes active only with provenance and uncertainty preserved.
8. Unresolved gaps constrain dependent state and actions according to consequence.

### Behavioral Continuity Change Loop

1. A model, runtime, prompt, specialist, context-policy, surface, or behavior-affecting configuration change is proposed or detected.
2. The change is bound to a system-under-test or behavior configuration where evaluation matters.
3. Material behavioral drift is evaluated against an established continuity reference that is causally prior to, or independently governed from, the change under evaluation.
4. The configuration may be accepted for use, constrained, held, rolled back, or marked as continuity-degraded.
5. New behavior evidence remains attributable to the configuration under which it was produced.
6. Incorporating attributable new behavior into established Zoey continuity is a separate continuity evaluation. Accepting a configuration for runtime use does not automatically promote every behavior it produces into Zoey's established continuity.

## Situational Posture And Governance Envelope

Situational posture is temporary control state affecting expression, pacing, correction style, exploratory breadth, relational framing, and initiative tendency.

Governance envelope is the effective constraint set for the current process. It is derived from applicable policy, actor assurance, authority state, consequence, sensitivity, surface, audience, proposed semantic effect or transition type, operation class, capability, continuity state, and trust boundary.

Posture may vary inside the governance envelope. It must not weaken evidence requirements, disclosure constraints, authorization requirements, operation limits, or durable-state controls.

A warm voice interaction may still require strict calendar authorization. An exploratory tutoring session may still require scoped state updates. A concise surface may still need to report uncertain operation outcomes accurately.

## Disclosure And Trust Boundaries

Before exposing private context, Zoey must consider actor identity, audience, surface, trust boundary, sensitivity, purpose, authority, capability, and whether a neutral or redacted representation is sufficient.

Read authority, write authority, and disclosure permission are separate. Zoey may be allowed to internally resolve a target while still lacking authority to mutate it or disclose details aloud.

Availability does not imply permission for context inclusion. Preserving a sensitivity label after unnecessary disclosure to a model or external service is not sufficient control.

Transformation does not declassify. Summaries, embeddings, labels, examples, screenshots, and derived artifacts inherit or increase sensitivity according to what they reveal, not their format.

## Scenario Alignment And Generalized Control Obligations

The canonical scenarios expose transition obligations, but this section must not overclaim that each scenario directly tests every generalized rule below. Direct scenario pressure and model generalization remain distinct.

`SCN-001` directly pressures the model to support:

- stale history and current evidence remaining separate;
- observed recognition and production differences supporting a scoped interpretation or evidence-responsive trial without creating a global skill claim;
- hypothesis, user request, or governed exploration producing a trial candidate with provenance preserved;
- trial candidate becoming active only after scope, stale-basis, reversibility, and consequence checks;
- explicit user correction changing current behavior immediately;
- broader future generalization remaining separately attributable as Zoey-derived trial state;
- intervention-conditioned outcome updating trial evidence without proving untested cause;
- trial or adaptation trajectory becoming inspectable often enough to prevent or detect anti-sycophancy drift.

`SCN-001` also motivates the generalized rule that multiple active trials or adaptations must not each be credited independently for the same outcome without support.

`SCN-002` directly pressures the model to support:

- voice input, actor assurance, intent, proposal, authorization, execution, and outcome remaining separate;
- bounded read authority differing from write authority and disclosure permission;
- authorization binding to a concrete proposal and material assumptions;
- pre-execution validation including authority and material-state validity;
- provider timeout creating provider observation plus uncertain operation outcome, not automatic failure;
- repeated similar intent being evaluated against pending uncertain operation state;
- reconciliation producing component-level outcome truth;
- audit/accountability failure exposing a reconstruction gap rather than inventing history;
- revocation before submission preventing submission;
- revocation after submission with uncertain commit status requiring reconciliation and separately governed reversal.

`SCN-002` also motivates the generalized rule that capability degradation must constrain dependent operations, commitments, watches, and surfaces even when the scenario does not directly run every capability-failure variant.

## Non-Goals

This document does not define final schemas, storage engines, confidence formulas, retention periods, review cadences, prompts, agents, APIs, UI, model routing, biometric mechanisms, calendar provider behavior, audit database design, or repository boundaries.

It does not define exhaustive state-machine tables, lock models, transaction models, event-sourcing rules, or complete transition matrices.

It is not a complete safety policy, privacy policy, legal compliance model, or general multi-user authority model.

It does not define a theory of consciousness, personhood, emotion, companionship, embodiment, or human relationship. It defines controllable system behavior.

## Quality Gates

Future architecture is compatible with this model only if:

- compatibility claims and architecture evaluations identify the State and Control Model version used; material changes to transition authority, dependency semantics, control-loop obligations, or quality gates require re-evaluation of affected claims;
- state dimensions remain compositional rather than one exclusive memory type;
- source, lineage, scope, time, durability, status, sensitivity, confidence type, consequence, reversibility, and authority remain available where consequence requires them;
- candidate generation remains separate from active state transition;
- every durable or consequential transition has an identifiable source state, target semantic effect, activation authority or control basis, and correction or invalidation path;
- materially stale candidates are re-evaluated before activation;
- material changes to evidence, authority, policy, capability, time, continuity, or scope cause dependent active state as well as pending candidates to be re-evaluated;
- dependency cycles and control non-convergence cannot self-validate; affected state remains conflicted, degraded, blocked, or uncertain until a sufficient non-circular basis exists;
- dependency changes do not silently cascade-delete history, but downstream applicability and support remain inspectable;
- time-driven expiry, due, freshness, and effective-interval transitions can occur without new user input;
- durable retention is itself a governed transition and transient observations do not automatically become durable personal history;
- retention basis, permitted use, disclosure permission, and retention granularity remain separable controls;
- control-relevant derived artifacts preserve sufficient lineage, permitted-use basis, and removal implications when they materially derive from personal semantic state;
- deletion, forgetting, retirement, redaction, correction, and revocation remain semantically distinguishable;
- instruction authority attaches to communicative acts, not to every instruction-like string carried through an authorized actor or channel;
- concurrent or conflicting transitions do not resolve through silent last-write-wins;
- control loops may re-enter and interleave without repeated processing becoming new evidence;
- context assembly preserves epistemic status, trust status, sensitivity, and purpose limitation;
- preferences, rules, policy, authority, goals, plans, commitments, and operations do not collapse;
- proposed plans and task decompositions do not silently become accepted project state, user obligations, durable open loops, or initiative pressure;
- user correction semantics depend on the state being corrected;
- observational absence is not treated as negative evidence without a valid observation opportunity;
- behavioral trials, adaptations, commitments, watches, initiatives, operations, and continuity recovery have lifecycle semantics;
- dependent transition groups preserve prerequisite, component-level, and group-level outcome semantics;
- capability degradation propagates to dependent commitments, watches, operations, and surfaces;
- initiative candidates are deduplicated or linked across materially equivalent repeated triggers rather than manufacturing interruption pressure through repetition;
- initiative disposition accounts for cumulative attention cost across competing candidates, not only each candidate's local value;
- posture cannot weaken the governance envelope;
- governance constrains candidate dispositions but does not manufacture a cognitive reason to act;
- operation control state preserves triggering basis, proposal, authorization, submission, provider observation, outcome, reconciliation, and accountability distinctions;
- actor assurance is required for operations when current actor identity affects intent, confirmation, authority, or disclosure, but standing-authority and watch-triggered operations may rely on other attributable triggering bases;
- continuity uncertainty constrains affected dependent state or actions;
- disclosure control treats transformed or aggregated artifacts as potentially sensitive;
- restore, migration, and replacement preserve continuity gaps instead of inventing seamless history;
- core identity and governance changes cannot be activated by ordinary runtime cognition;
- behavior-affecting configurations cannot redefine their own continuity reference merely by producing new behavior;
- scenario-direct obligations are distinguished from generalized model obligations;
- Zoey remains correctable under valid user control.
