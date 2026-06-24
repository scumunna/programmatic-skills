# DV360 naming and taxonomy template

Read this when defining or enforcing a naming convention. Emit it as the team standard and hold every new campaign, insertion order, line item, creative, and audience to it. Names are the join keys for reporting, the filters analysts pivot on, and the values that structured data file automation reads and writes, so one inconsistent field breaks a dashboard or a bulk edit.

## The three rules

1. **One delimiter, used everywhere.** Default to the pipe ` | ` (space-pipe-space) because it reads cleanly and rarely appears inside a value. An underscore `_` works too. Whatever you choose, it must never appear inside a field value, or splitting the name in a report breaks.
2. **A fixed, ordered field set, same order on every entity type.** Order most-stable field first, most-specific last, so a name read at any level decodes the same way.
3. **A controlled vocabulary per field.** A documented, closed list of allowed values and abbreviations. No free text. "Q3" and "Q03" and "Quarter3" cannot all be legal.

## Ordered fields

Use this field order across all entity types. Not every field applies to every entity; drop trailing fields that do not apply rather than reordering.

| Position | Field | Meaning | Applies to |
| --- | --- | --- | --- |
| 1 | Brand | Advertiser or brand code | All |
| 2 | Market | Country or region | All |
| 3 | Objective | Business goal | Campaign, IO, line item |
| 4 | FunnelStage | Where in the funnel | IO, line item |
| 5 | Channel | Format or environment | IO, line item, creative |
| 6 | InventorySource | How inventory is bought | Line item |
| 7 | Flight | Time period | Campaign, IO, line item |
| 8 | Variant | Size or creative variant | Line item, creative |

## Controlled vocabulary (example values)

Treat the lists below as a starting controlled vocabulary. Extend them deliberately and keep the master list in one place. The point is that every legal value is enumerated.

- **Brand:** short stable code per advertiser, for example `ACME`, `GLOBEX`, `INITECH`. No spaces.
- **Market:** ISO-style codes, for example `US`, `CA`, `UK`, `DE`, `EMEA`, `APAC`.
- **Objective:** `Awareness`, `Consideration`, `Sales`, `AppInstall`, `Lead`.
- **FunnelStage:** `Prospecting`, `Retargeting`, `Retention`, `Full`.
- **Channel:** `Display`, `OLV` (online video), `CTV`, `Audio`, `Native`, `DOOH`, `YouTube`.
- **InventorySource:** `OpenAuction`, `PMP`, `PG` (programmatic guaranteed), `PA` (preferred), `Direct`.
- **Flight:** `2026Q3`, `2026-07`, `2026-07-01_2026-07-31`. Pick one flight format and keep it.
- **Variant:** creative size or version, for example `728x90`, `300x250`, `15s`, `30s`, `SummerSale_v2`.

For first-party audience naming, use `Brand | Market | 1P | Descriptor_Window`, for example `ACME | US | 1P | CartAbandoners_30d`. Audiences auto-share from the partner down to advertisers, so a vague audience name pollutes every advertiser.

## Worked examples

Pipe delimiter, fields in order, trailing fields dropped where they do not apply:

```
Campaign        ACME | US | Sales | Full | AllChannels | 2026Q3
Insertion order ACME | US | Sales | Prospecting | Display | 2026Q3
Line item       ACME | US | Sales | Prospecting | Display | PMP | 2026Q3 | 728x90
Creative        ACME | US | Sales | Prospecting | Display | 728x90 | SummerSale_v2
Audience        ACME | US | 1P | CartAbandoners_30d
```

Decoding the line item left to right: ACME brand, US market, Sales objective, Prospecting funnel stage, Display channel, bought via PMP, flighting in 2026 Q3, the 728x90 unit. An analyst can filter on any field by splitting on the delimiter, and a structured data file can read or write any field deterministically.

## Why it matters for SDF automation

Structured data files create and edit entities in bulk by reading and writing the Name column among others. If names follow a strict, delimited, controlled convention:
- A script can construct names deterministically when generating hundreds of line items.
- A bulk edit can target exactly the right rows by matching a field segment.
- A report can break out spend by Channel or FunnelStage by parsing the name, even where a native dimension is missing.

If names are free text, none of this is reliable, and every bulk operation risks editing the wrong entity. Enforce the convention at creation, never retroactively, because renaming after reporting has accrued breaks historical filters and saved dashboards.
