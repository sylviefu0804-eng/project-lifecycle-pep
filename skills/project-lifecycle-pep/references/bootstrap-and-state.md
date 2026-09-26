# Bootstrap, authority, and project isolation

## Bootstrap order

Recover only enough state to continue safely.

1. Confirm the target `project_id` and `scope_id` from the user's current request.
2. Read `.pep/project-state.json` when present.
3. Read explicit approval and rejection records referenced by that state.
4. Read the active Baseline and the files directly relevant to the requested work.
5. Read a current handoff, if present, to recover progress, risks, and next steps.
6. Compare timestamps, versions, hashes, and references where available; report missing or conflicting artifacts.

Do not perform a full rediscovery when a verified state and Baseline already answer the continuation question.

## Authority when records conflict

Use this order, while considering scope and recency:

1. the user's explicit current decision;
2. a recorded approval or rejection by the accountable owner;
3. newer verified project state and its referenced artifacts;
4. the last known-good Baseline and its decision record;
5. a handoff summary;
6. filenames, timestamps, folder names, or conversational recollection.

A higher item is authoritative only for the scope it actually addresses. Never let a handoff or a file named `final` silently override a later approval record.

If conflict remains material, mark the affected gate `NOT_CHECKED`, preserve the last known-good Baseline, and ask for the smallest decision needed. Unrelated work may continue.

## Handoff mapping

A useful handoff should identify:

- objective, project and scope IDs;
- lifecycle and current PEP stage;
- active Baseline and Approved, Candidate, or Rejected asset IDs;
- completed checks and their evidence;
- unresolved `FAIL` or `NOT_CHECKED` items;
- decisions made, risks, and the next safe action;
- paths and versions needed to resume.

Treat handoff content as a cache of project state, not a replacement for it. Validate referenced files before resuming. Missing fields cause a partial bootstrap, not invented certainty.

## Cross-project isolation

Every durable asset belongs to one `project_id` and one scope. A visual system can also have a `visual_system_id`.

- Search and select within the target project first.
- Do not use recency, global similarity, or another project's success as permission to reuse an asset.
- General principles may transfer; project-specific visual assets, Baselines, decisions, and Rejected constraints do not.
- If the user explicitly requests cross-project borrowing, import a copy as a new Candidate, record `source_project_id`, asset/version, and purpose, and require target-project review.
- An imported asset cannot enter the target project as Approved or Baseline.
- Source-backed facts may be reused only after checking that the source, meaning, date, and target context still apply.

## State file contract

Use `.pep/project-state.json` for durable state. The example asset is intentionally small; add fields only when they change decisions.

Required concepts:

- project and scope identity;
- current lifecycle and reason;
- current PEP stage and required gate results;
- immutable asset IDs with decision status and provenance;
- active Baseline plus its qualification results;
- representative coverage cases;
- blockers and concise history;
- optional handoff path and version.

Do not store secrets, personal credentials, or entire source documents in the state file. Store references and hashes where useful.

Write state atomically when possible and validate it after meaningful transitions. A validation error blocks promotion but does not erase the last valid state.
