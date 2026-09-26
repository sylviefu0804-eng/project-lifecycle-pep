---
name: project-lifecycle-pep
description: Govern multi-step projects that need lifecycle classification, durable state, approved assets, coverage gates, or safe continuation across sessions. Use for iterative design, research, production, and other complex projects; do not use for a simple one-off task with no meaningful project state.
metadata:
  version: "1.0.0"
  status: "v1.0"
---

# Project Lifecycle + PEP

The project owner reports using this method in two real projects: a corporate presentation and a sports exhibition. This v1.0 package has structural checks and scenario-based evaluation; it has not replayed those private project artifacts. Classify each current project independently from its evidence.

## Start by recovering the project

1. Identify the exact `project_id`, workstream or `scope_id`, requested outcome, and current deliverable.
2. Bootstrap from project-local state, explicit approval records, current files, and any handoff. Never infer approval from a filename such as `final`, recency, or visual similarity.
3. Classify the project as `GENESIS`, `CALIBRATION`, or `MATURE` using current evidence.
4. State the classification, the evidence supporting it, the active PEP stage, and any blockers before making a consequential change.

Read [references/lifecycle-and-pep.md](references/lifecycle-and-pep.md) whenever classifying a project, changing lifecycle, freezing an asset, promoting a baseline, or deciding whether Baseline Continuation applies.

Read [references/bootstrap-and-state.md](references/bootstrap-and-state.md) when starting a new conversation, resuming from handoff, reconstructing missing state, resolving conflicting records, persisting state, or importing anything from another project.

## Run PEP proportionately

Use `discover → review → freeze → verify → validate` as governed states, not as ceremony. A mature, narrow continuation may use a short discover/review pass; a new or unstable system needs the full cycle.

- `discover`: establish scope, inventory assets and constraints, identify unknowns, and build the coverage map.
- `review`: compare candidates, diagnose gaps, resolve conflicts, and decide what is ready for approval.
- `freeze`: record explicit approval and lock the intended scope. Exporting or naming a file `final` is not approval.
- `verify`: run objective checks. Record each required check as `PASS`, `FAIL`, or `NOT_CHECKED`.
- `validate`: confirm the verified result serves the user, audience, and real context; record acceptance.

Do not enter `validate`, replace a Baseline, or claim completion while any required check is `FAIL` or `NOT_CHECKED`.

## Preserve asset state

Use only these decision states:

- `Candidate`: proposed or changed; not authoritative.
- `Approved`: explicitly accepted for a defined scope; not necessarily the continuation source.
- `Baseline`: the current Approved continuation source for its project and scope.
- `Rejected`: explicitly declined or invalidated; never silently revive it.

Create a new Candidate for material revisions. Do not overwrite an Approved or Baseline asset in place. A replaced Baseline normally returns to `Approved` unless the user explicitly rejects it.

## Enforce the non-negotiable gates

- Coverage is about representative scope, not item count. Required cases must be named and passed.
- `MATURE` describes the proven system, not every new deliverable. A mature project can contain a failing Candidate.
- Approved Seeds and Baselines are project- and scope-bound. Do not import them across projects without explicit user intent and recorded provenance.
- A handoff is a progress snapshot, not a higher authority than explicit user decisions or newer verified project state.
- If state is missing or contradictory, preserve the last known-good Baseline, mark uncertain items `NOT_CHECKED`, and stop only the transitions affected by that uncertainty.

## State files

For durable projects, keep project state at `.pep/project-state.json` when the task authorizes workspace changes. Initialize it from [assets/project-state.example.json](assets/project-state.example.json), then run the validator using the actual absolute paths. Resolve the script against this Skill directory and the state file against the target project, not the current working directory:

```bash
python3 /path/to/this-skill/scripts/validate_project_state.py /path/to/project/.pep/project-state.json
```

For a read-only review, do not create or update state; report the proposed state changes instead.

## Finish each meaningful cycle

Report the lifecycle, PEP stage reached, asset transitions, coverage result, verification and validation results, unresolved blockers, active Baseline, and the smallest safe next step. Keep the record concise enough to bootstrap the next session.
