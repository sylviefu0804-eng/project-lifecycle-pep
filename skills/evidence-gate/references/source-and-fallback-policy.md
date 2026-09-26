# Source and fallback policy

## Source hierarchy

Choose the strongest source that directly supports the exact claim.

### Tier 1: primary or authoritative

- government laws, policies, gazettes, and issuing-authority notices;
- archival item records and institutional collection catalogs;
- original transcripts, recordings, letters, books, or contemporaneous records;
- regulatory filings, audited reports, official statistics, and issuer notices;
- an institution's own record for a person, artifact, event, or collection it controls.

### Tier 2: strong secondary

- reputable scholarship with traceable citations;
- established news or professional publications reporting from named primary sources;
- museum, university, or recognized expert interpretation that identifies its evidence.

Use Tier 2 when primary material is unavailable and the risk permits it. Corroborate high-risk claims with an independent source when feasible.

### Tier 3: discovery only

- reposts, aggregators, marketing decks, social posts, anonymous articles, search snippets, image search labels, forums, and unlabeled scans;
- AI-generated text, images, captions, or remembered facts;
- filenames, alt text, or nearby page copy without provenance.

Tier 3 can point to a better source but cannot by itself PASS a named portrait, direct quotation, exact policy claim, or material corporate number.

## Evidence by item type

### Name–portrait pair

Require an authoritative or well-sourced record that links the image to the named person. Capture the catalog ID, caption, page, or other direct identifier. Cropped copies must be traceable to the identified source image.

Do not use face matching as evidence. Group photos require a reliable caption or positional identification.

### Quotation

Require the original or a trustworthy reproduction. Record the speaker or author, work or event, date, location in the source, and any translation. If exact wording cannot be supported, paraphrase without quotation marks only when the underlying idea is supported and attribution remains accurate.

### Policy or rule

Confirm issuer, title, document number when one exists, publication and effective dates, jurisdiction, amendment or repeal status, and the exact clause supporting the statement. A later summary cannot silently replace the operative text.

### Corporate fact or number

Confirm entity, reporting period, currency, units, accounting or metric definition, consolidated scope, and whether the number is audited, estimated, or restated. When an official press release and filing differ, explain the definitional or timing difference or keep the item blocked.

### Historical claim

Separate documented fact, scholarly interpretation, oral history, and legend. Attribute interpretation and uncertainty. Do not turn a plausible chronology into a documented event.

## Conflict handling

1. Check whether sources address the same entity, period, metric, version, and scope.
2. Prefer the source with direct authority over the fact.
3. Preserve a material discrepancy in the ledger.
4. If it cannot be resolved, narrow the claim, state uncertainty, or remove it. Do not average or silently select a value.

## Safe fallback ladder

When evidence is insufficient, choose the first option that still communicates the intended meaning:

1. omit or narrow the unsupported claim;
2. use an authenticated document excerpt or catalog record;
3. use a verified object, venue, event, team, equipment, medal, or other representative artifact;
4. use a non-identifying silhouette or generic scene clearly labeled as illustrative;
5. use text-only treatment that states the supported facts and uncertainty.

Never use a generated or look-alike face as a documentary substitute for a named real person.

## Minimum ledger fields

```text
item_id | claim_or_asset | type | intended_use | source | pinpoint | result | reason | checked_at
```

Store only what is needed to reproduce the decision. Do not copy entire copyrighted sources into the ledger.
