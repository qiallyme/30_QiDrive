---
title: "QiCode Migration Notes"
aliases:
  - "QiCode Reconciliation Notes"
system: "QiOS"
document_type: "migration-record"
status: "active-record"
version: "1.0"
canonical: false
updated: "2026-07-18"
source:
  - "Original compiled doctrine"
  - "Intermediate cleaned draft"
  - "Final split package"
tags:
  - "qicode"
  - "migration"
  - "archive"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiCode Registry|Final Registry]] · [[QiCode Numbering Standard|Numbering Standard]]

# QiCode Migration Notes

## Why the Source Could Not Remain One Document

The supplied compilation mixed four different jobs:

1. a master numbered registry;
2. active QiLife doctrine and schema content;
3. outline-only records for unrelated domains; and
4. legacy or quarantined material.

It also reused section numbers, repeated source metadata, scattered QiLife content across Titles 01, 03, 04, and 05, and placed a legacy QiLife specification under Security.

## Final Package Decision

- The registry now contains the map, status, and canonical destination only.
- Full QiLife content is split into six focused canonical documents.
- Outline-only sections remain in the registry without fabricated body text.
- Legacy QiLife material is quarantined.
- The original and intermediate compilation are preserved unchanged under `Sources`.

## QiLife Renumbering from the Intermediate Cleaned Draft

| Intermediate code | Final code | Canonical document |
| --- | --- | --- |
| `06.01.001` | `06.01.001` | QiLife Doctrine |
| `06.01.005` | `06.01.002` | QiLife Doctrine |
| `06.01.002–004` | `06.02.001–003` | QiLife Architecture |
| `06.02.001–013` | `06.03.001–013` | QiLife Data Model |
| `06.03.001–004` | `06.04.001–004` | QiLife Workflows |
| `06.04.001–012` | `06.05.001–012` | QiLife Product Surfaces |
| `06.05.001–003` | `06.06.001–003` | QiLife Deferred Finance Bridge |

## Original Collision Repairs Retained

| Original issue | Final treatment |
| --- | --- |
| Repeated `00.01.001–005` IDs | Unique registry order under Chapter 00.01 |
| Repeated `01.01.001–003` IDs | Unique registry order under Chapter 01.01 |
| `05.01` used as parent and section | Treated only as a chapter |
| `07.02` reused by security and QiLife legacy spec | Security remains active; legacy QiLife moved to archive |

## Unresolved Vocabulary

`payment_note`, `bill_note`, and `money_issue` appear in the deferred finance source but not in the canonical QiBit type list. They remain descriptive patterns, not valid `qibit_type` values, until deliberately added or removed.

## Source Preservation Rule

Do not edit the two files in `90 - Archive/Sources` when correcting active doctrine. They exist to show what was actually supplied and how the final structure was derived.
