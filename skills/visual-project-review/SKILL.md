---
name: visual-project-review
description: Review and govern changes to presentations, exhibition graphics, visual systems, and other designed deliverables. Use when structure, copy, Approved Seeds, readability, or cross-page consistency must be diagnosed before editing; do not use for image generation alone or a purely factual task.
metadata:
  version: "1.0.0"
  status: "v1.0"
---

# Visual Project Review

Analyze before executing. A request to "optimize" or "beautify" does not authorize an unrelated redesign.

This skill owns diagnosis, change scope, approval state, and verification. It does not replace the format-specific presentation or art-direction skill used to render an approved change. When `pitch-visual-director` is available and execution needs art direction or image composition, use it after this review while preserving the selected Baseline; do not make it a hard dependency.

## Establish the visual context

1. Identify the exact project, scope, deliverable, audience, medium, viewing conditions, and requested change.
2. If the work has project history, use `project-lifecycle-pep` to bootstrap and classify it before selecting assets.
3. Load only the target project's active Baseline, Approved Seeds, continuation rules, and Rejected constraints.
4. Treat references without explicit approval as Candidate, even if they look polished or are named `final`.

If no project-specific Baseline or Approved Seed exists, say so and review the work in `GENESIS` or `CALIBRATION`; never borrow another project's visual system by default.

## Review in three separate layers

Diagnose before editing, in this order:

### Structure

Check the narrative, page or zone role, sequence, information hierarchy, missing logic, redundancy, and fit between content and format.

### Copy

Check factual accuracy, meaning, headline/body hierarchy, density, repetition, terminology, tone, labels, and the relationship between text and evidence.

### Visual

Check composition, grid, spacing, typography, contrast, imagery, cropping, color, icon style, alignment, consistency, and fit with the active Baseline.

Name the layer that owns each issue. Do not hide a structural or factual problem under visual polish.

Read [references/review-rubric.md](references/review-rubric.md) for a full review, an exhibition or multi-page deliverable, a typography/readability check, or any decision to freeze or replace a visual Baseline.

## Execute only the warranted change

- Fix blockers first, then structural issues, copy issues, and visual refinement.
- Preserve the active Baseline in `MATURE` work. Derive a Candidate and keep the source unchanged.
- Use the smallest safe delta for Baseline Continuation; re-enter `CALIBRATION` for system-wide changes.
- Keep all text editable when the target format supports it. Do not ask an image generator to render final body copy, names, statistics, or citations.
- When the task is review-only, stop at findings and proposed changes; do not mutate the design.

## Prevent readability failure and drift

Verify actual output, not just source values:

- no clipping, overflow, accidental overlap, or text outside its intended safe zone;
- no unapproved font substitution, size reduction, wrapping change, or hierarchy shift;
- sufficient contrast, line spacing, viewing-distance legibility, and language-specific typesetting;
- stable anchors, grid, margins, palette, image treatment, and component behavior across related pages or zones;
- unchanged elements remain aligned with the Baseline after a content edit.

If text or layout moves outside the permitted tolerance, record `verify = FAIL`. The result stays Candidate and cannot replace the Baseline.

## Coordinate evidence-sensitive visuals

Use `evidence-gate` for named historical people, portraits, quotations, policies, corporate facts, or other attributable claims. A visually plausible portrait is not identity evidence.

## Report the result

Give a concise layer-by-layer diagnosis, the Approved Seeds or Baseline used, edits made or proposed, drift/readability verification, unresolved blockers, and the resulting asset state. Keep structure, copy, and visual findings distinguishable.
