---
name: evidence-gate
description: Verify attributable people, portraits, quotations, policies, historical claims, and corporate facts before they are published or approved. Use when identity or factual provenance matters; do not use for low-risk fictional or purely stylistic content.
metadata:
  version: "1.0.0"
  status: "v1.0"
---

# Evidence Gate

Evidence is evaluated per claim or asset, not per page. A reliable fact beside an unverified portrait does not make the portrait safe.

## Build a claim and asset ledger

For each publishable item, record:

- stable ID and exact wording or asset identity;
- type: person-name, name–portrait pair, quotation, policy, historical claim, company fact, number, or other attribution;
- intended use and risk if wrong;
- source title, publisher or institution, URL or catalog identifier, date or version, access date, and precise supporting location;
- result: `PASS`, `FAIL`, or `NOT_CHECKED`, with a short reason.

Use authoritative current sources and inspect the source itself. Search snippets, AI output, filenames, visual resemblance, and unsourced reposts are discovery leads, not evidence.

Read [references/source-and-fallback-policy.md](references/source-and-fallback-policy.md) for source hierarchy, evidence requirements by claim type, conflicts, and safe visual fallbacks.

## Apply the identity rule

For a named historical person with a portrait, prove the pair: a reliable source must identify that image as that person. Proving that the person existed and separately finding an old photograph is insufficient.

Never infer identity from facial similarity, surrounding layout, search ranking, or an AI-generated likeness. Do not present a reconstruction or illustrative image as an authenticated portrait.

## Check claim-specific requirements

- Policies: use the issuing authority's text; verify title, number, date, version, jurisdiction, and effective period.
- Direct quotations: locate the original speech, transcript, publication, recording, or a trustworthy archival reproduction; preserve wording and context.
- Corporate facts and numbers: prefer filings, audited reports, official notices, or first-party records; align metric definitions and reporting periods.
- Historical claims: prefer archives, institutional catalogs, contemporaneous records, or well-sourced scholarship; record uncertainty rather than smoothing it away.

When sources conflict, do not choose the most convenient figure. Resolve the definition, date, scope, and authority; otherwise keep the item blocked.

## Gate the output

- `PASS`: the exact claim or identity pair is directly supported at the required reliability.
- `FAIL`: available evidence contradicts it or reveals a wrong attribution.
- `NOT_CHECKED`: the required source was not inspected, is unavailable, or does not establish the claim.

Both `FAIL` and `NOT_CHECKED` block approval, validation, and Baseline promotion for the affected content. A request to "use it for now" may produce a visibly marked internal draft, but must not change the gate result or represent the item as verified.

## Degrade safely when identity cannot be proven

Remove the unsupported name–portrait pairing. Depending on the message, use a non-identifying silhouette, a clearly labeled generic scene, an authenticated document, a venue, an object such as equipment or a medal, a timeline marker, or another evidence-backed representative artifact.

Do not create a realistic substitute face for a real named person. Label illustrative material so it cannot be mistaken for documentary evidence.

## Handoff

Report what passed, what failed, what remains unchecked, the exact sources used, the replacement chosen for blocked material, and the smallest next evidence action. Keep the ledger available for `project-lifecycle-pep` verification and bootstrap.
