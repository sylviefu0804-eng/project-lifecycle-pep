# Lifecycle and PEP rules

## Lifecycle classification

Classify the current project and scope from evidence, not from how long the project has existed.

### GENESIS

Use when no trustworthy Baseline exists for the requested scope, the objective or system is still being discovered, or prior assumptions were fundamentally invalidated.

Primary behavior:

- inventory goals, constraints, assets, stakeholders, evidence risks, and missing inputs;
- keep unapproved material as Candidate;
- create a representative Coverage Gate before freezing a direction;
- explore enough alternatives to make a real decision, without premature consistency.

Exit when a coherent direction has explicit approval and is ready to be tested across representative cases. Move to `CALIBRATION`, not directly to `MATURE`.

### CALIBRATION

Use when a direction or Approved Seeds exist but the system, rules, coverage, or verification has not converged.

Primary behavior:

- test the direction across the required coverage matrix;
- remove uncontrolled variation and resolve exceptions;
- preserve Approved decisions while iterating through new Candidates;
- freeze only the scope that is explicitly approved and sufficiently covered.

Exit to `MATURE` only when the active Baseline is explicit, required coverage is complete, verification passes, validation is recorded, and continuation rules are clear.

### MATURE

Use when a project-scope has a current Baseline, representative coverage, passing verification, recorded validation, and repeatable continuation rules.

Primary behavior is Baseline Continuation: start from the current Baseline, preserve its invariants, make the smallest scoped delta, and verify the affected area plus essential regressions. Do not reopen visual or methodological exploration for a routine update.

A new Candidate may fail while the project remains `MATURE`; never confuse project maturity with current-delivery approval.

### Reclassification

- `MATURE → CALIBRATION`: a system-level change, a new representative case, or a demonstrated baseline failure requires recalibration.
- `CALIBRATION → GENESIS`: only when the governing direction or assumptions are no longer viable.
- A local defect or one failed Candidate does not by itself downgrade the whole project.
- A new project, workstream, audience, or incompatible visual system starts its own classification.

## PEP state machine

PEP is ordered, but work may loop backward when evidence changes.

1. `discover`: define the problem, project identity, scope, constraints, assets, evidence obligations, and coverage matrix.
2. `review`: assess options and gaps; separate facts from preferences; decide which Candidate is ready for explicit approval.
3. `freeze`: record the approving person or source, timestamp, scope, asset version, and decision. Freeze does not imply verification.
4. `verify`: check objective requirements and label every required check `PASS`, `FAIL`, or `NOT_CHECKED`.
5. `validate`: confirm the verified result works for the intended audience, environment, and outcome, including user or accountable-owner acceptance when required.

Rules:

- A stage can return to any earlier stage when a real gap is found.
- `FAIL` and `NOT_CHECKED` both block downstream transitions for the affected scope.
- Partial PASS never cancels a blocking result.
- A user can accept risk, but the record must keep the failed or unchecked condition visible; do not relabel it PASS.
- Explicit user instructions outrank this workflow, except that the skill must not make false claims about checks or evidence.

## Coverage Gate

Define required cases before claiming convergence. Coverage is scoped and domain-specific.

For a presentation or exhibition, consider page or zone families, information densities, languages, screen or print sizes, accessibility, imagery types, and factual-risk categories. For a non-visual process, consider source types, decision branches, exception classes, roles, and representative outputs.

Every required case needs:

- a stable identifier and scope;
- an owner or decision source when applicable;
- a status of `PASS`, `FAIL`, or `NOT_CHECKED`;
- a reference to the tested artifact or evidence;
- a short reason for the result.

Coverage passes only when every required case passes. Adding a new required case reopens coverage for that scope.

## Asset transitions

Allowed ordinary transitions:

- new work → `Candidate`;
- `Candidate` → `Approved` after explicit acceptance;
- `Approved` → `Baseline` after coverage, verification, and validation pass for the intended scope;
- `Candidate` → `Rejected` after an explicit decline or demonstrated invalidity;
- `Baseline` → `Approved` when replaced but still valid as an approved historical asset;
- any materially revised asset → a new `Candidate` with provenance.

Do not mutate `Rejected` directly to Approved or Baseline. Derive a materially revised Candidate and retain the rejection record.

## Baseline Continuation

Continuation is valid only when the requested change remains inside the Baseline's project, scope, and governing rules.

1. Load the active Baseline and its continuation rules.
2. Create a Candidate derived from it; keep the Baseline untouched.
3. Change only the requested content or affected system rule.
4. Verify the changed area and the smallest meaningful regression set.
5. Validate the new Candidate before replacing the Baseline.

Return to `CALIBRATION` when the change alters a system-wide invariant, expands representative coverage, creates repeated exceptions, or shows that the current rules no longer hold.
